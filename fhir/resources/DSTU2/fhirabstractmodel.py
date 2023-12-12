# -*- coding: utf-8 -*-
"""Base class for all FHIR elements. """
import abc
import inspect
import logging
import typing
from functools import lru_cache
from typing import TYPE_CHECKING, Any, Callable, Type

from pydantic.v1 import BaseModel, Extra, Field
from pydantic.v1.class_validators import ROOT_VALIDATOR_CONFIG_KEY, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import ConfigError, PydanticValueError
from pydantic.v1.typing import AnyCallable
from pydantic.v1.utils import ROOT_KEY

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


if TYPE_CHECKING:
    from pydantic.v1.typing import AbstractSetIntStr, MappingIntStrAny, DictStrAny
    from pydantic.v1.main import Model

__author__ = "Md Nazrul Islam<email2nazrul@gmail.com>"

logger = logging.getLogger(__name__)
FHIR_COMMENTS_FIELD_NAME = "fhir_comments"


def fallback_type_method():
    """lambda like function, is used as fallback of ``is_primitive``
    method for non FHIR Type class"""
    return True


def filter_empty_list_dict(items):
    """A special helper function, which is removing
    any item which contains empty list/dict value.
    It is used by ``FHIRAbstractModel::json``"""
    if not isinstance(items, (list, dict)):
        return items

    if len(items) == 0:
        return None

    if isinstance(items, list):
        for idx, item in enumerate(items):
            if item is None:
                # may be ``exclude_none`` False
                continue
            result = filter_empty_list_dict(item)
            if result is None:
                del items[idx]
    else:
        for key in tuple(items.keys()):
            item = items[key]
            if item is None:
                # may be ``exclude_none`` False
                continue
            result = filter_empty_list_dict(item)
            if result is None:
                del items[key]

    if len(items) == 0:
        return None

    return items


class WrongResourceType(PydanticValueError):
    code = "wrong.resource_type"
    msg_template = "Wrong ResourceType: {error}"


class FHIRAbstractModel(BaseModel, abc.ABC):
    """Abstract base model class for all FHIR elements."""

    resource_type: str = ...  # type: ignore

    fhir_comments: typing.Union[str, typing.List[str]] = Field(
        None, alias="fhir_comments", element_property=False
    )

    def __init__(__pydantic_self__, **data: Any) -> None:
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
        validator: typing.Union[AnyCallable, classmethod],
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
    @lru_cache(maxsize=1024, typed=True)
    def has_resource_base(cls) -> bool:
        """ """
        # xxx: calculate metrics, other than cache it!
        for cl in inspect.getmro(cls)[:-4]:
            if cl.__name__ == "Resource":
                return True
        return False

    @classmethod
    @lru_cache(maxsize=None, typed=True)
    def get_resource_type(cls: Type["Model"]) -> str:
        """ """
        return cls.__fields__["resource_type"].default

    @classmethod
    def get_json_encoder(cls) -> Callable[[Any], Any]:
        """ """
        return cls.__json_encoder__

    def dict(
        self,
        *,
        include: typing.Union["AbstractSetIntStr", "MappingIntStrAny", None] = None,
        exclude: typing.Union["AbstractSetIntStr", "MappingIntStrAny", None] = None,
        by_alias: typing.Optional[bool] = None,
        skip_defaults: typing.Optional[bool] = None,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: typing.Optional[bool] = None,
    ) -> "DictStrAny":
        """ """
        # xxx: do validation? if object changed
        if by_alias is None:
            by_alias = True

        if exclude_none is None:
            exclude_none = True

        if exclude is None:
            exclude = {"resource_type"}
        elif isinstance(exclude, set):
            exclude.add("resource_type")
        elif isinstance(exclude, dict):
            if "resource_type" not in exclude:
                exclude["resource_type"] = ...

        exclude_comments = False

        if FHIR_COMMENTS_FIELD_NAME in exclude:
            exclude_comments = True

        if exclude_comments:
            children_excludes: typing.Dict[
                str, typing.Union[typing.Set[str], typing.Dict[str, typing.Any]]
            ] = dict()
            for field in self.__fields__.values():
                if getattr(field.type_, "is_primitive", fallback_type_method)():
                    # no treatment for Primitive Type
                    continue
                if field.outer_type_ != field.type_ and str(
                    field.outer_type_
                ).startswith("typing.List["):
                    children_excludes[field.name] = {
                        "__all__": {FHIR_COMMENTS_FIELD_NAME}
                    }
                else:
                    children_excludes[field.name] = {FHIR_COMMENTS_FIELD_NAME}

            if len(children_excludes) > 0:
                if isinstance(exclude, set):
                    exclude = {e: ... for e in exclude}
                if typing.TYPE_CHECKING:
                    exclude = typing.cast(typing.Dict, exclude)
                exclude.update(children_excludes)

            if FHIR_COMMENTS_FIELD_NAME not in exclude:
                if isinstance(exclude, set):
                    exclude.add(FHIR_COMMENTS_FIELD_NAME)
                elif isinstance(exclude, dict):
                    exclude[FHIR_COMMENTS_FIELD_NAME] = ...

        result = BaseModel.dict(
            self,
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            skip_defaults=skip_defaults,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
        )
        if self.__class__.has_resource_base():
            result["resourceType"] = self.resource_type

        return result

    def json(  # type: ignore
        self,
        *,
        include: typing.Union["AbstractSetIntStr", "MappingIntStrAny", None] = None,
        exclude: typing.Union["AbstractSetIntStr", "MappingIntStrAny", None] = None,
        by_alias: typing.Optional[bool] = None,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
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

        if exclude_comments:
            if exclude is None:
                exclude = {FHIR_COMMENTS_FIELD_NAME}
            elif isinstance(exclude, set):
                exclude.add(FHIR_COMMENTS_FIELD_NAME)
            elif isinstance(exclude, dict):
                exclude[FHIR_COMMENTS_FIELD_NAME] = ...
            else:
                raise NotImplementedError(
                    "Only Set or Dict type ``exclude`` value is accepted "
                    f"but got type ``{type(exclude)}``"
                )

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
                logger.warning(
                    "When ``dumps`` method is used from ``orjson`` "
                    "all dumps kwargs are ignored except `indent`, `sort_keys` "
                    "and of course ``option`` from orjson"
                )
                dumps_kwargs = {}

            if option > 0:
                dumps_kwargs["option"] = option

            dumps_kwargs["return_bytes"] = return_bytes

        data = self.dict(
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
        )
        if self.__custom_root_type__:
            data = data[ROOT_KEY]

        if exclude_comments:
            data = filter_empty_list_dict(data)

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

    class Config:
        json_loads = json_loads
        json_dumps = json_dumps
        allow_population_by_field_name = True
        extra = Extra.allow
        validate_assignment = True
        error_msg_templates = {"value_error.extra": "extra fields not permitted"}
