# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Reference
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1 import Field

from . import element, fhirtypes


class Reference(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A reference from one resource to another.
    """

    resource_type = Field("Reference", const=True)

    display: fhirtypes.String = Field(
        None,
        alias="display",
        title="Text alternative for the resource",
        description=(
            "Plain text narrative that identifies the resource in addition to the "
            "resource reference."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_display", title="Extension field for ``display``."
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Logical reference, when literal reference is not known",
        description=(
            "An identifier for the other resource. This is used when there is no "
            "way to reference the other resource directly, either because the "
            "entity is not available through a FHIR server, or because there is no "
            "way for the author of the resource to convert a known identifier to an"
            " actual location. There is no requirement that a Reference.identifier "
            "point to something that is actually exposed as a FHIR instance, but it"
            " SHALL point to a business concept that would be expected to be "
            "exposed as a FHIR instance, and that instance would need to be of a "
            "FHIR resource type allowed by the reference."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    reference: fhirtypes.String = Field(
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
        # if property is element of this resource.
        element_property=True,
    )
    reference__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_reference", title="Extension field for ``reference``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Reference`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "reference", "identifier", "display"]
