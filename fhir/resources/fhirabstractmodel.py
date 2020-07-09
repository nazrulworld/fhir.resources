# -*- coding: utf-8 -*-
"""Base class for all FHIR elements. """
import abc
import inspect
import logging
from copy import deepcopy
from functools import lru_cache
from typing import TYPE_CHECKING, Any, Callable, Generator, Optional, Type, Union

from pydantic import BaseModel, Extra
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import ConfigError, PydanticValueError
from pydantic.fields import ModelField

if TYPE_CHECKING:
    from pydantic.typing import AbstractSetIntStr, MappingIntStrAny, DictStrAny, SetStr
    from pydantic.main import Model

__author__ = "Md Nazrul Islam<email2nazrul@gmail.com>"

logger = logging.getLogger(__name__)


class WrongResourceType(PydanticValueError):
    code = "wrong.resource_type"
    msg_template = "Wrong ResourceType: {error}"


class FHIRAbstractModel(BaseModel, abc.ABC):
    """ Abstract base model class for all FHIR elements.
    """

    resource_type: str = ...  # type: ignore

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
        cls: Type["Model"],
        validator: Callable,
        *,
        pre: bool = False,
        skip_on_failure: bool = False,
        index: int = -1,
    ):
        """ """
        from inspect import signature
        from inspect import isfunction

        if not isfunction(validator):
            raise ConfigError(
                f"'{validator.__qualname__}' must be function not method from class."
            )
        sig = signature(validator)
        args = list(sig.parameters.keys())
        if args[0] != "cls":
            raise ConfigError(
                f"Invalid signature for root validator {validator.__qualname__}: {sig}, "
                f'"args[0]" not permitted as first argument, '
                f"should be: (cls, values)."
            )
        if len(args) != 2:
            raise ConfigError(
                f"Invalid signature for root validator {validator.__qualname__}: {sig}, "
                "should be: (cls, values)."
            )
        if pre:
            if validator not in cls.__pre_root_validators__:
                if index == -1:
                    cls.__pre_root_validators__.append(validator)
                else:
                    cls.__pre_root_validators__.insert(index, validator)
            return
        if validator in map(lambda x: x[1], cls.__post_root_validators__):
            return
        if index == -1:
            cls.__post_root_validators__.append((skip_on_failure, validator))
        else:
            cls.__post_root_validators__.insert(index, (skip_on_failure, validator))

    @classmethod
    def element_properties(cls: Type["Model"]) -> Generator[ModelField, None, None]:
        """ """
        for model_field in cls.__fields__.values():
            if model_field.field_info.extra.get("element_property", False):
                yield model_field

    @classmethod
    @lru_cache(maxsize=1024, typed=True)
    def has_resource_base(cls: Type["Model"]) -> bool:
        """ """
        # xxx: calculate metrics, other than cache it!
        for cl in inspect.getmro(cls)[:-4]:
            if cl.__name__ == "Resource":
                return True
        return False

    def dict(
        self,
        *,
        include: Union["AbstractSetIntStr", "MappingIntStrAny"] = None,
        exclude: Union["AbstractSetIntStr", "MappingIntStrAny"] = None,
        by_alias: bool = None,
        skip_defaults: bool = None,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = None,
    ) -> "DictStrAny":
        """ """
        # xxx: do validation? if object changed
        if by_alias is None:
            by_alias = True

        if exclude_none is None:
            exclude_none = True

        exclude_ = {"resource_type"}
        if isinstance(exclude, (list, tuple, set)):
            exclude_ = exclude_.union(exclude)

        result = BaseModel.dict(
            self,
            include=include,
            exclude=exclude_,
            by_alias=by_alias,
            skip_defaults=skip_defaults,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
        )
        if self.__class__.has_resource_base():
            result["resourceType"] = self.resource_type
        return result

    def json(
        self,
        *,
        include: Union["AbstractSetIntStr", "MappingIntStrAny"] = None,
        exclude: Union["AbstractSetIntStr", "MappingIntStrAny"] = None,
        by_alias: bool = None,
        skip_defaults: bool = None,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = None,
        encoder: Optional[Callable[[Any], Any]] = None,
        **dumps_kwargs: Any,
    ) -> str:
        """ """
        if by_alias is None:
            by_alias = True

        if exclude_none is None:
            exclude_none = True

        return BaseModel.json(
            self,
            include=include,
            by_alias=by_alias,
            skip_defaults=skip_defaults,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            encoder=encoder,
            **dumps_kwargs,
        )

    @classmethod
    def construct(
        cls: Type["Model"], _fields_set: Optional["SetStr"] = None, **values: Any
    ) -> "Model":
        """Disclaimer: for now this method is 1:1 with BaseModel's method.
        But in future we may apply some validation, for example disallow
        unknown field (extra), construct any Model Type field value (if dict value has
        been provided)
        """
        m = cls.__new__(cls)
        object.__setattr__(
            m, "__dict__", {**deepcopy(cls.__field_defaults__), **values}
        )
        if _fields_set is None:
            _fields_set = set(values.keys())
        object.__setattr__(m, "__fields_set__", _fields_set)
        return m

    class Config:
        allow_population_by_field_name = True
        extra = Extra.forbid
        validate_assignment = True
        error_msg_templates = {"value_error.extra": "extra fields not permitted"}
