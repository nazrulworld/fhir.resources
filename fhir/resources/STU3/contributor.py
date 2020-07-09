# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Contributor
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import element, fhirtypes


class Contributor(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Contributor information.
    A contributor to the content of a knowledge asset, including authors,
    editors, reviewers, and endorsers.
    """

    resource_type = Field("Contributor", const=True)

    contact: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="Contact details of the contributor",
        description=(
            "Contact details to assist a user in finding and communicating with the"
            " contributor."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Who contributed the content",
        description=(
            "The name of the individual or organization responsible for the "
            "contribution."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="author | editor | reviewer | endorser",
        description="The type of contributor.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["author", "editor", "reviewer", "endorser"],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )
