from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Reference
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic import Field

from . import datatype, fhirtypes


class Reference(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A reference from one resource to another.
    """

    __resource_type__ = "Reference"

    display: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="display",
        title="Text alternative for the resource",
        description=(
            "Plain text narrative that identifies the resource in addition to the "
            "resource reference."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_display", title="Extension field for ``display``."
    )

    identifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Logical reference, when literal reference is not known",
        description=(
            "An identifier for the target resource. This is used when there is no "
            "way to reference the other resource directly, either because the "
            "entity it represents is not available through a FHIR server, or "
            "because there is no way for the author of the resource to convert a "
            "known identifier to an actual location. There is no requirement that a"
            " Reference.identifier point to something that is actually exposed as a"
            " FHIR instance, but it SHALL point to a business concept that would be"
            " expected to be exposed as a FHIR instance, and that instance would "
            "need to be of a FHIR resource type allowed by the reference."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reference: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="reference",
        title="Literal reference, Relative, internal or absolute URL",
        description=(
            "A reference to a location at which the other resource is found. The "
            "reference may be a relative reference, in which case it is relative to"
            " the service base URL, or an absolute URL that resolves to the "
            "location where the resource is found. The reference may be version "
            "specific or not. If the reference is not to a FHIR RESTful server, "
            "then it should be assumed to be version specific. Internal fragment "
            "references (start with '#') refer to contained resources."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    reference__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_reference", title="Extension field for ``reference``."
    )

    type: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="type",
        title=(
            'Type the reference refers to (e.g. "Patient") - must be a resource in '
            "resources"
        ),
        description=(
            "The expected type of the target of the reference. If both "
            "Reference.type and Reference.reference are populated and "
            "Reference.reference is a FHIR URL, both SHALL be consistent.  The type"
            " is the Canonical URL of Resource Definition that is the type this "
            "reference refers to. References are URLs that are relative to "
            'http://hl7.org/fhir/StructureDefinition/ e.g. "Patient" is a reference'
            " to http://hl7.org/fhir/StructureDefinition/Patient. Absolute URLs are"
            " only allowed for logical models (and can only be used in references "
            "in logical models, not resources)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Reference`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "reference", "type", "identifier", "display"]
