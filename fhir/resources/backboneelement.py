# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/BackboneElement
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import element, fhirtypes


class BackboneElement(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Base for elements defined inside a resource.
    Base definition for all elements that are defined inside a resource - but
    not those in a data type.
    """

    resource_type = Field("BackboneElement", const=True)

    modifierExtension: ListType[fhirtypes.ExtensionType] = Field(
        None,
        alias="modifierExtension",
        title="List of `Extension` items (represented as `dict` in JSON)",
        description="Extensions that cannot be ignored even if unrecognized",
    )
