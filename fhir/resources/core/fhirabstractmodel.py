# -*- coding: utf-8 -*-
"""Base class for all FHIR elements. """
import inspect
import logging
import pathlib
import typing
from collections import OrderedDict
from functools import lru_cache

from pydantic import (
    BaseModel,
    Field,
    SerializationInfo,
    model_serializer,
    ConfigDict,
    model_validator,
)
from pydantic.fields import FieldInfo
from pydantic.main import IncEx
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import PydanticValueError
from pydantic.v1.parse import Protocol
from pydantic_core import ValidationError, InitErrorDetails, PydanticCustomError
from typing_extensions import Literal
from typing_extensions import Self

from .utils import is_primitive_type, load_file, load_str_bytes, xml_dumps, yaml_dumps

if typing.TYPE_CHECKING:
    from pydantic.main import Model, TupleGenerator
    from pydantic.v1.types import StrBytes

__author__ = "Md Nazrul Islam"
__email__ = "email2nazrul@gmail.com"

logger = logging.getLogger(__name__)
ROOT_KEY = "root"
FHIR_COMMENTS_FIELD_NAME = "fhir_comments"
FHIRErrorCodes = Literal[
    "fhir-validation-missing-resource-type",
    "fhir-validation-wrong-resource-type",
]


class WrongResourceType(PydanticValueError):
    code = "wrong.resource_type"
    msg_template = "Wrong ResourceType: {error}"


class FHIRAbstractModel(BaseModel):
    """Abstract base model class for all FHIR elements."""

    __fhir_serialization_include_comment__: bool = None
    # __resource_type__: Literal['ResourceType'] = 'ResourceType'
    __resource_type__ = ...

    fhir_comments: typing.Union[str, typing.List[str]] = Field(
        None, alias="fhir_comments", json_schema_extra={"element_property": False}
    )

    def __init__(self, /, **data: typing.Any) -> None:  # type: ignore
        """
        from pydantic_core import PydanticCustomError
        raise PydanticCustomError(
            'sequence_str',
            "'{type_name}' instances are not allowed as a Sequence value",
            {'type_name': value_type.__name__},
        )
        https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.InitErrorDetails
        """
        if self.__resource_type__ is Ellipsis:
            raise ValueError("__resource_type__ must be defined in subclasses")

        resource_type = data.pop("resource_type", None)
        if "resourceType" in data and "resourceType" not in self.model_fields:
            resource_type = data.pop("resourceType", None)

        if resource_type is not None and resource_type != self.__resource_type__:
            expected_resource_type = self.__resource_type__
            error_type: PydanticCustomError = PydanticCustomError(
                "fhir-validation-wrong-resource-type",
                message_template="""``{module_name}.{class_name}`` expects resource type ``{expected_resource_type}``,
                    but got ``{resource_type}``. Make sure resource type name is correct and right
                    ModelClass has been chosen.""",
                context={
                    "module_name": self.__class__.__module__,
                    "class_name": self.__class__.__name__,
                    "expected_resource_type": expected_resource_type,
                    "resource_type": resource_type,
                },
            )
            error_: InitErrorDetails = {
                "type": error_type,
                "loc": ("resource_type",),
                "input": resource_type,
            }
            raise ValidationError.from_exception_data(self.__class__.__name__, [error_])

        BaseModel.__init__(self, **data)

    @classmethod
    def element_properties(
        cls: typing.Type["Model"],
    ) -> typing.Generator[FieldInfo, None, None]:
        """ """
        for field_info in cls.model_fields.values():
            if field_info.json_schema_extra.get("element_property", False):
                yield field_info

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``Resource`` according specification,
        with preserving original sequence order.
        """
        return []

    @classmethod
    @lru_cache(maxsize=1024, typed=True)
    def has_resource_base(cls: typing.Type["BaseModel"]) -> bool:
        """ """
        # xxx: calculate metrics, other than cache it!
        for cl in inspect.getmro(cls)[:-4]:
            if cl.__name__ == "Resource":
                return True
        return False

    @classmethod
    @lru_cache(maxsize=None, typed=True)
    def get_resource_type(cls: typing.Type["Model"]) -> str:
        """ """
        return cls.__resource_type__

    @classmethod
    @lru_cache(maxsize=None, typed=True)
    def get_alias_mapping(
        cls: typing.Type["FHIRAbstractModel"],
    ) -> typing.Dict[str, str]:
        """Mappings between field's name and alias"""
        aliases = cls.elements_sequence()
        return {
            fi.alias: fn for fn, fi in cls.model_fields.items() if fi.alias in aliases
        }

    @classmethod
    def get_json_encoder(cls) -> typing.Callable[[typing.Any], typing.Any]:
        """ """
        return cls.__pydantic_serializer__.to_json

    @classmethod
    def parse_file(
        cls: typing.Type["Model"],
        path: typing.Union[str, pathlib.Path],
        *,
        content_type: typing.Optional[str] = None,
        encoding: str = "utf8",
        proto: typing.Optional[Protocol] = None,
        allow_pickle: bool = False,
        **extra,
    ) -> "Model":
        extra.update({"cls": cls})
        obj = load_file(
            path,
            proto=proto,  # type: ignore[arg-type]
            content_type=content_type,  # type: ignore[arg-type]
            encoding=encoding,
            allow_pickle=allow_pickle,
            json_loads=cls.__config__.json_loads,
            **extra,
        )
        return cls.parse_obj(obj)

    @classmethod
    def parse_raw(
        cls: typing.Type["Model"],
        b: "StrBytes",
        *,
        content_type: typing.Optional[str] = None,
        encoding: str = "utf8",
        proto: typing.Optional[Protocol] = None,
        allow_pickle: bool = False,
        **extra,
    ) -> "Model":
        extra.update({"cls": cls})
        try:
            obj = load_str_bytes(
                b,
                proto=proto,  # type: ignore[arg-type]
                content_type=content_type,  # type: ignore[arg-type]
                encoding=encoding,
                allow_pickle=allow_pickle,
                json_loads=cls.__config__.json_loads,
                **extra,
            )
        except (ValueError, TypeError, UnicodeDecodeError) as e:  # noqa: B014
            raise ValidationError([ErrorWrapper(e, loc=ROOT_KEY)], cls)
        return cls.parse_obj(obj)

    def yaml(  # type: ignore
        self,
        *,
        by_alias: typing.Optional[bool] = None,
        exclude_none: typing.Optional[bool] = None,
        exclude_comments: bool = False,
        return_bytes: bool = False,
        **dumps_kwargs: typing.Any,
    ) -> typing.Union[str, bytes]:
        """Fully overridden method but codes are copied from BaseMode and business logic added
        in according to support ``fhir_comments``filter and other FHIR specific requirments.
        """
        if by_alias is None:
            by_alias = True

        if exclude_none is None:
            exclude_none = True

        data = self.dict(
            by_alias=by_alias,
            exclude_none=exclude_none,
            exclude_comments=exclude_comments,
        )
        # __pydantic_root_model__
        if self.__pydantic_root_model__:
            data = data[ROOT_KEY]

        if typing.TYPE_CHECKING:
            result: typing.Union[str, bytes]

        result = yaml_dumps(data, return_bytes=return_bytes, **dumps_kwargs)
        return result

    def xml(  # type: ignore
        self,
        *,
        exclude_comments: bool = False,
        pretty_print=False,
        xml_declaration=True,
        return_bytes: bool = False,
        **dumps_kwargs: typing.Any,
    ) -> typing.Union[str, bytes]:
        """ """
        params = {
            "with_comments": not exclude_comments,
            "xml_declaration": xml_declaration,
            "pretty_print": pretty_print,
        }
        params.update(dumps_kwargs)

        xml_string = xml_dumps(self, **params)
        if return_bytes is False:
            xml_string = xml_string.decode()

        return xml_string

    def model_dump_json(
        self,
        *,
        indent: int | None = None,
        include: IncEx = None,
        exclude: IncEx = None,
        context: dict[str, typing.Any] | None = None,
        by_alias: bool = False,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        round_trip: bool = False,
        warnings: bool | Literal["none", "warn", "error"] = True,
        serialize_as_any: bool = False,
        # Custom
        exclude_comments: bool = False,
    ) -> str:
        """Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#modelmodel_dump_json

        Generates a JSON representation of the model using Pydantic's `to_json` method.

        Args:
            indent: Indentation to use in the JSON output. If None is passed, the output will be compact.
            include: Field(s) to include in the JSON output.
            exclude: Field(s) to exclude from the JSON output.
            context: Additional context to pass to the serializer.
            by_alias: Whether to serialize using field aliases.
            exclude_unset: Whether to exclude fields that have not been explicitly set.
            exclude_defaults: Whether to exclude fields that are set to their default value.
            exclude_none: Whether to exclude fields that have a value of `None`.
            round_trip: If True, dumped values should be valid as input for non-idempotent types such as Json[T].
            warnings: How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,
                "error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError].
            serialize_as_any: Whether to serialize fields with duck-typing serialization behavior.
            exclude_comments: FHIR comment

        Returns:
            A JSON string representation of the model.
        """
        """Fully overridden method but codes are copied from BaseMode and business logic added
        in according to support ``fhir_comments``filter and other FHIR specific requirments.
        """
        if by_alias is None:
            by_alias = True

        if exclude_none is None:
            exclude_none = True

        org_config_val = None
        if exclude_comments is not None:
            org_config_val = self.__fhir_serialization_include_comment__
            self.__fhir_serialization_include_comment__ = exclude_comments

        result = BaseModel.model_dump_json(
            self,
            indent=indent,
            include=include,
            exclude=exclude,
            context=context,
            by_alias=by_alias,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            round_trip=round_trip,
            warnings=warnings,
            serialize_as_any=serialize_as_any,
        )
        if exclude_comments is not None:
            self.__fhir_serialization_include_comment__ = org_config_val
        return result

    def model_dump(
        self,
        *,
        mode: Literal["json", "python"] | str = "python",
        include: IncEx = None,
        exclude: IncEx = None,
        context: dict[str, typing.Any] | None = None,
        by_alias: bool = False,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        round_trip: bool = False,
        warnings: bool | Literal["none", "warn", "error"] = True,
        serialize_as_any: bool = False,
        # extra
        exclude_comments: bool = False,
    ) -> dict[str, typing.Any]:
        """Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#modelmodel_dump

        Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

        Args:
            mode: The mode in which `to_python` should run.
                If mode is 'json', the output will only contain JSON serializable types.
                If mode is 'python', the output may contain non-JSON-serializable Python objects.
            include: A set of fields to include in the output.
            exclude: A set of fields to exclude from the output.
            context: Additional context to pass to the serializer.
            by_alias: Whether to use the field's alias in the dictionary key if defined.
            exclude_unset: Whether to exclude fields that have not been explicitly set.
            exclude_defaults: Whether to exclude fields that are set to their default value.
            exclude_none: Whether to exclude fields that have a value of `None`.
            round_trip: If True, dumped values should be valid as input for non-idempotent types such as Json[T].
            warnings: How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,
                "error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError].
            serialize_as_any: Whether to serialize fields with duck-typing serialization behavior.

        Returns:
            A dictionary representation of the model.

        if len(pydantic_extra) > 0:
            logger.warning(
                f"{self.__class__.__name__}.dict method accepts only"
                "´by_alias´, ´exclude_none´, ´exclude_comments` as parameters"
                " since version v6.2.0, any extra parameter is simply ignored. "
                "You should not provide any extra argument."
        )
        """
        if by_alias is None:
            by_alias = True

        if exclude_none is None:
            exclude_none = True

        org_config_val = None
        if exclude_comments is False:
            org_config_val = self.__fhir_serialization_include_comment__
            self.__fhir_serialization_include_comment__ = True

        result = BaseModel.model_dump(
            self,
            mode=mode,
            include=include,
            exclude=exclude,
            context=context,
            by_alias=by_alias,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            round_trip=round_trip,
            warnings=warnings,
            serialize_as_any=serialize_as_any,
        )
        if exclude_comments is False:
            self.__fhir_serialization_include_comment__ = org_config_val
        return result

    # Serializers
    @model_serializer(mode="wrap", when_used="always", return_type=OrderedDict)
    def fhir_model_serializer(
        self,
        serialize: typing.Callable[[typing.Any], typing.Any],
        info: SerializationInfo,
    ) -> OrderedDict:
        return OrderedDict(self._fhir_iter(serialize, info))

    # Private methods
    def _fhir_iter(
        self,
        serialize: typing.Callable[[typing.Any], typing.Any],
        info: SerializationInfo,
    ) -> "TupleGenerator":
        return None, None
        if self.__class__.has_resource_base():
            yield "resourceType", self.__resource_type__

        alias_maps = self.get_alias_mapping()
        for prop_name in self.elements_sequence():
            field_key = alias_maps[prop_name]
            field = self.model_fields[field_key]
            is_primitive = is_primitive_type(field)
            dict_key = info.by_alias and field.alias or field_key
            value = serialize(self.__dict__.get(field_key, None))

            if value is not None or (info.exclude_none is False and value is None):
                yield dict_key, value

            # looking for comments or primitive extension for primitive data type
            if is_primitive:
                ext_key = f"{field_key}__ext"
                ext_val = serialize(self.__dict__.get(ext_key, None))
                if ext_val is not None:
                    dict_key_ = (
                        info.by_alias and self.model_fields[ext_key].alias or ext_key
                    )
                    if ext_val is not None and len(ext_val) > 0:
                        yield dict_key_, ext_val
        # looking for comments
        comments = self.__dict__.get(FHIR_COMMENTS_FIELD_NAME, None)

        if comments is not None and self.__fhir_serialization_include_comment__:
            yield FHIR_COMMENTS_FIELD_NAME, comments

    @model_validator(mode="after")
    def validate_after_model_construction(self) -> Self:
        """ """
        # do after validation for primitive elements
        self._validate_required_primitive_elements()

        # do after validation for one of many
        self._validate_one_of_many()

        return self

    def _validate_one_of_many(self):
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = self.get_one_of_many_fields()
        if len(one_of_many_fields) == 0:
            return
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

    def _validate_required_primitive_elements(self):
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = self.get_required_fields()
        if len(required_fields) == 0:
            return
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """This method should be overridden in each subclass.
        [("type", "type__ext")]"""
        return []

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
        """This method should be override in subclasses to specify one set of fields

        return {
            "allowed": ["allowedMoney", "allowedString", "allowedUnsignedInt"],
            "used": ["usedMoney", "usedUnsignedInt"],
        }
        """
        return {}

    model_config = ConfigDict(
        extra="forbid", validate_assignment=True, populate_by_name=True
    )
