# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ContactDetail
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import element, fhirtypes


class ContactDetail(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Contact information.
    Specifies contact information for a person or organization.
    """

    resource_type = Field("ContactDetail", const=True)

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`",
        description="Name of an individual to contact",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="List of `ContactPoint` items (represented as `dict` in JSON)",
        description="Contact details for individual or organization",
    )
