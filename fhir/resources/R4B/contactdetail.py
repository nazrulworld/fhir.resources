from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ContactDetail
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import element, fhirtypes


class ContactDetail(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Contact information.
    Specifies contact information for a person or organization.
    """

    __resource_type__ = "ContactDetail"

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name of an individual to contact",
        description="The name of an individual to contact.",
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    telecom: typing.List[fhirtypes.ContactPointType] | None = Field(  # type: ignore
        None,
        alias="telecom",
        title="Contact details for individual or organization",
        description=(
            "The contact details for the individual (if a name was provided) or the"
            " organization."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ContactDetail`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "name", "telecom"]
