# -*- coding: utf-8 -*-
"""Base class for all FHIR elements. """
import abc
import inspect
import logging
import pathlib
import typing
from collections import OrderedDict
from enum import Enum
from functools import lru_cache

from pydantic.v1 import BaseModel, Extra, Field
from pydantic.v1.class_validators import ROOT_VALIDATOR_CONFIG_KEY, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import ConfigError, PydanticValueError
from pydantic.v1.fields import ModelField
from pydantic.v1.parse import Protocol
from pydantic.v1.utils import ROOT_KEY, sequence_like

from .utils import is_primitive_type, load_file, load_str_bytes, xml_dumps, yaml_dumps

try:
    import orjson

    def json_dumps(v, *, default, option=0, return_bytes=False):
        params = {"default": default}
        if option > 0:
            params["option"] = option
        result = orjson.dumps(v, **params)
        if return_bytes is False:
            result = result.decode()
        if typing.TYPE_CHECKING and return_bytes is True:
            result = typing.cast(str, result)
        return result

    json_dumps.__qualname__ = "orjson_json_dumps"
    json_loads = orjson.loads

except ImportError:
    try:
        from simplejson import loads as json_loads
        from simplejson import dumps as json_dumps  # type:ignore
    except ImportError:
        from json import loads as json_loads
        from json import dumps as json_dumps  # type:ignore


if typing.TYPE_CHECKING:
    from pydantic.v1.typing import TupleGenerator
    from pydantic.v1.types import StrBytes
    from pydantic.v1.typing import AnyCallable
    from pydantic.v1.main import Model

__author__ = "Md Nazrul Islam<email2nazrul@gmail.com>"

logger = logging.getLogger(__name__)
FHIR_COMMENTS_FIELD_NAME = "fhir_comments"


class WrongResourceType(PydanticValueError):
    code = "wrong.resource_type"
    msg_template = "Wrong ResourceType: {error}"


class FHIRAbstractModel(BaseModel, abc.ABC):
    """Abstract base model class for all FHIR elements."""

    resource_type: str = ...  # type: ignore

    fhir_comments: typing.Union[str, typing.List[str]] = Field(
        None, alias="fhir_comments", element_property=False
    )

    def __init__(__pydantic_self__, **data: typing.Any) -> None:
        """ """
        resource_type = data.pop("resource_type", None)
        errors = []
        if (
            "resourceType" in data
            and "resourceType" not in __pydantic_self__.__fields__
        ):
            resource_type = data.pop("resourceType", None)

        if (
            resource_type is not None
            and resource_type != __pydantic_self__.__fields__["resource_type"].default
        ):
            expected_resource_type = __pydantic_self__.__fields__[
                "resource_type"
            ].default
            error = (
                f"``{__pydantic_self__.__class__.__module__}."
                f"{__pydantic_self__.__class__.__name__}`` "
                f"expects resource type ``{expected_resource_type}``, "
                f"but got ``{resource_type}``. "
                "Make sure resource type name is correct and right "
                "ModelClass has been chosen."
            )
            errors.append(
                ErrorWrapper(WrongResourceType(error=error), loc="resource_type")
            )
        if errors:
            raise ValidationError(errors, __pydantic_self__.__class__)

        BaseModel.__init__(__pydantic_self__, **data)

    @classmethod
    def add_root_validator(
        cls: typing.Type["Model"],
        validator: typing.Union["AnyCallable", classmethod],
        *,
        pre: bool = False,
        skip_on_failure: bool = False,
        allow_reuse: bool = True,
        index: int = -1,
    ):
        """ """
        from inspect import signature
        from inspect import ismethod

        if isinstance(validator, classmethod) or ismethod(validator):
            validator = validator.__func__  # type:ignore

        func_name = validator.__name__

        # first level validation
        if any([func_name in cls_.__dict__ for cls_ in cls.mro()]):
            raise ConfigError(
                f"{cls} already has same name '{func_name}' method or attribute!"
            )
        if func_name in cls.__fields__:
            raise ConfigError(f"{cls} already has same name '{func_name}' field!")

        # evaluate through root_validator
        validator = root_validator(
            pre=pre, allow_reuse=allow_reuse, skip_on_failure=skip_on_failure
        )(validator)

        validator_config = getattr(validator, ROOT_VALIDATOR_CONFIG_KEY)
        sig = signature(validator_config.func)
        arg_list = list(sig.parameters.keys())

        if len(arg_list) != 2:
            raise ConfigError(
                f"Invalid signature for root validator {func_name}: {sig}"
                ", should be: (cls, values)."
            )

        if arg_list[0] != "cls":
            raise ConfigError(
                f"Invalid signature for root validator {func_name}: {sig}, "
                f'"{arg_list[0]}" not permitted as first argument, '
                "should be: (cls, values)."
            )
        # check function signature
        if validator_config.pre:
            if index == -1:
                cls.__pre_root_validators__.append(validator_config.func)
            else:
                cls.__pre_root_validators__.insert(index, validator_config.func)
        else:
            if index == -1:
                cls.__post_root_validators__.append(
                    (validator_config.skip_on_failure, validator_config.func)
                )
            else:
                cls.__post_root_validators__.insert(
                    index, (validator_config.skip_on_failure, validator_config.func)
                )
        # inject to class
        setattr(validator, "__manually_injected__", True)  # noqa:B010
        setattr(cls, func_name, validator)

    @classmethod
    def element_properties(
        cls: typing.Type["Model"],
    ) -> typing.Generator[ModelField, None, None]:
        """ """
        for model_field in cls.__fields__.values():
            if model_field.field_info.extra.get("element_property", False):
                yield model_field

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``Resource`` according specification,
        with preserving original sequence order.
        """
        return []

    @classmethod
    @lru_cache(maxsize=1024, typed=True)
    def has_resource_base(cls: typing.Type["Model"]) -> bool:
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
        return cls.__fields__["resource_type"].default

    @classmethod
    @lru_cache(maxsize=None, typed=True)
    def get_alias_mapping(
        cls: typing.Type["FHIRAbstractModel"],
    ) -> typing.Dict[str, str]:
        """Mappings between field's name and alias"""
        aliases = cls.elements_sequence()
        return {
            f.alias: fname for fname, f in cls.__fields__.items() if f.alias in aliases
        }

    @classmethod
    def get_json_encoder(cls) -> typing.Callable[[typing.Any], typing.Any]:
        """ """
        return cls.__json_encoder__

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
        if self.__custom_root_type__:
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

    def json(  # type: ignore
        self,
        *,
        by_alias: typing.Optional[bool] = None,
        exclude_none: typing.Optional[bool] = None,
        exclude_comments: bool = False,
        encoder: typing.Optional[typing.Callable[[typing.Any], typing.Any]] = None,
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

        if (
            getattr(self.__config__.json_dumps, "__qualname__", "")
            == "orjson_json_dumps"
        ):
            option = dumps_kwargs.pop("option", 0)
            if option == 0:
                if "indent" in dumps_kwargs:
                    dumps_kwargs.pop("indent")
                    # only indent 2 is accepted
                    option |= orjson.OPT_INDENT_2

                sort_keys = dumps_kwargs.pop("sort_keys", False)
                if sort_keys:
                    option |= orjson.OPT_SORT_KEYS

            if len(dumps_kwargs) > 0:
                logger.debug(
                    "When ``dumps`` method is used from ``orjson`` "
                    "all dumps kwargs are ignored except `indent`, `sort_keys` "
                    "and of course ``option`` from orjson"
                )
                dumps_kwargs = {}

            if option > 0:
                dumps_kwargs["option"] = option

            dumps_kwargs["return_bytes"] = return_bytes

        data = self.dict(
            by_alias=by_alias,
            exclude_none=exclude_none,
            exclude_comments=exclude_comments,
        )
        if self.__custom_root_type__:
            data = data[ROOT_KEY]

        encoder = typing.cast(
            typing.Callable[[typing.Any], typing.Any], encoder or self.__json_encoder__
        )

        if typing.TYPE_CHECKING:
            result: typing.Union[str, bytes]

        result = self.__config__.json_dumps(data, default=encoder, **dumps_kwargs)

        if return_bytes is True:
            if isinstance(result, str):
                result = result.encode("utf-8", errors="strict")
        else:
            if isinstance(result, bytes):
                result = result.decode()

        return result

    @typing.no_type_check
    def dict(
        self,
        *,
        by_alias: bool = True,
        exclude_none: bool = True,
        exclude_comments: bool = False,
        **pydantic_extra,
    ) -> OrderedDict:
        """important!
        there is no impact on ``pydantic_extra`` we keep it as backward compatibility.
        @see issues https://github.com/nazrulworld/fhir.resources/issues/90
        & https://github.com/nazrulworld/fhir.resources/issues/89
        """
        if len(pydantic_extra) > 0:
            logger.warning(
                f"{self.__class__.__name__}.dict method accepts only"
                "´by_alias´, ´exclude_none´, ´exclude_comments` as parameters"
                " since version v6.2.0, any extra parameter is simply ignored. "
                "You should not provide any extra argument."
            )
        return OrderedDict(
            self._fhir_iter(
                by_alias=by_alias,
                exclude_none=exclude_none,
                exclude_comments=exclude_comments,
            )
        )

    # Private methods
    def _fhir_iter(
        self, *, by_alias: bool, exclude_none: bool, exclude_comments: bool
    ) -> "TupleGenerator":
        if self.__class__.has_resource_base():
            yield "resourceType", self.resource_type

        alias_maps = self.get_alias_mapping()
        for prop_name in self.elements_sequence():
            field_key = alias_maps[prop_name]

            field = self.__fields__[field_key]
            is_primitive = is_primitive_type(field)
            v = self.__dict__.get(field_key, None)
            dict_key = by_alias and field.alias or field_key
            if v is not None:
                v = self._fhir_get_value(
                    v,
                    by_alias=by_alias,
                    exclude_none=exclude_none,
                    exclude_comments=exclude_comments,
                )

            if v is not None or (exclude_none is False and v is None):
                yield dict_key, v

            # looking for comments or primitive extension for primitive data type
            if is_primitive:
                ext_key = f"{field_key}__ext"
                ext_val = self.__dict__.get(ext_key, None)
                if ext_val is not None:
                    dict_key_ = by_alias and self.__fields__[ext_key].alias or ext_key
                    ext_val = self._fhir_get_value(
                        ext_val,
                        by_alias=by_alias,
                        exclude_none=exclude_none,
                        exclude_comments=exclude_comments,
                    )
                    if ext_val is not None and len(ext_val) > 0:
                        yield dict_key_, ext_val
        # looking for comments
        comments = self.__dict__.get(FHIR_COMMENTS_FIELD_NAME, None)
        if comments is not None and not exclude_comments:
            yield FHIR_COMMENTS_FIELD_NAME, comments

    @classmethod
    @typing.no_type_check
    def _fhir_get_value(
        cls, v: typing.Any, by_alias: bool, exclude_none: bool, exclude_comments: bool
    ) -> typing.Any:
        if isinstance(v, (FHIRAbstractModel, BaseModel)):
            v_dict = v.dict(
                by_alias=by_alias,
                exclude_none=exclude_none,
                exclude_comments=exclude_comments,
            )
            if "__root__" in v_dict:
                return v_dict["__root__"]
            value = v_dict

        elif isinstance(v, dict):
            value = {
                k_: cls._fhir_get_value(
                    v_,
                    by_alias=by_alias,
                    exclude_none=exclude_none,
                    exclude_comments=exclude_comments,
                )
                for k_, v_ in v.items()
            }
        elif sequence_like(v):
            value = v.__class__(
                cls._fhir_get_value(
                    v_,
                    by_alias=by_alias,
                    exclude_none=exclude_none,
                    exclude_comments=exclude_comments,
                )
                for v_ in v
            )

        elif isinstance(v, Enum) and getattr(cls.Config, "use_enum_values", False):
            value = v.value

        else:
            value = v
        if (
            (sequence_like(value) or isinstance(value, dict))
            and exclude_none is True
            and len(value) == 0
        ):
            return None
        return value

    class Config:
        json_loads = json_loads
        json_dumps = json_dumps
        allow_population_by_field_name = True
        extra = Extra.forbid
        validate_assignment = True
        error_msg_templates = {"value_error.extra": "extra fields not permitted"}
