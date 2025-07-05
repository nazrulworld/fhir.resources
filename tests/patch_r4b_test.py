# -*- coding: utf-8 -*-
import typing

__author__ = "Md Nazrul Islam<>"
__email__ = "email2nazrul@gmail.com"

_APPLIED: bool = False


def SearchParameter_get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
    """https://www.hl7.org/fhir/extensibility.html#Special-Case
    In some cases, implementers might find that they do not have appropriate data for
    an element with minimum cardinality = 1. In this case, the element must be present,
    but unless the resource or a profile on it has made the actual value of the primitive
    data type mandatory, it is possible to provide an extension that explains why
    the primitive value is not present.
    """
    required_fields = [
        # ("base", "base__ext"),
        ("code", "code__ext"),
        ("description", "description__ext"),
        ("name", "name__ext"),
        ("status", "status__ext"),
        ("type", "type__ext"),
        ("url", "url__ext"),
    ]
    return required_fields


def apply():
    global _APPLIED
    if _APPLIED is True:
        # Already applied, one time only.
        return
    # import importlib
    # from fhir_core import constraints
    # from fhir_core import types as ftypes
    # constraints.TYPES_ID_MAX_LENGTH = 64
    # importlib.reload(ftypes)
    from fhir.resources.R4B.searchparameter import SearchParameter

    # Id.max_length = 255
    # some example json file has ID value more than default 64 character
    # IdType.configure_constraints(min_length=1, max_length=128, regex=None)
    # SearchParameter.model_fields['id'].metadata[0] = Id(max_length=128, pattern="")
    # SearchParameter.__pydantic_core_schema__['schema']['schema']['fields']['id']['schema']['schema'].update({
    #    'max_length': 255
    # })
    # {'type': 'str', 'pattern': '^[A-Za-z0-9\\-.]+$', 'max_length': 64, 'min_length': 1, 'metadata': {}}

    SearchParameter.get_required_fields = SearchParameter_get_required_fields
    _APPLIED = True
