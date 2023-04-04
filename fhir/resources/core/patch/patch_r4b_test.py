# -*- coding: utf-8 -*-
import typing

from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

__author__ = "Md Nazrul Islam<email2nazrul@gmail.com>"

_APPLIED: bool = False


def validate_required_primitive_elements_1724(
    cls, values: typing.Dict[str, typing.Any]
) -> typing.Dict[str, typing.Any]:
    """This patch is made for
    SearchParameter.validate_required_primitive_elements_1724 for purpose of testing.
    Some json file doesn't contain value of 'base' which is required."""
    required_fields = [
        # ("base", "base__ext"),
        ("code", "code__ext"),
        ("description", "description__ext"),
        ("name", "name__ext"),
        ("status", "status__ext"),
        ("type", "type__ext"),
        ("url", "url__ext"),
    ]
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
                errors.append(ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias))
    if len(errors) > 0:
        raise ValidationError(errors, cls)  # type: ignore

    return values


def apply():
    global _APPLIED
    if _APPLIED is True:
        # Already applied, one time only.
        return
    from fhir.resources.R4B.fhirtypes import Id
    from fhir.resources.R4B.searchparameter import SearchParameter

    # some example json file has ID value more than default 64 character
    Id.configure_constraints(min_length=1, max_length=128, regex=None)
    SearchParameter.__pre_root_validators__ = [
        validate_required_primitive_elements_1724
    ]
    _APPLIED = True
