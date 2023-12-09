# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Resource
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1 import Field

from . import fhirresourcemodel, fhirtypes


class Resource(fhirresourcemodel.FHIRResourceModel):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Base Resource.
    This is the base resource type for everything.
    """

    resource_type = Field("Resource", const=True)

    id: fhirtypes.Id = Field(
        None,
        alias="id",
        title="Logical id of this artifact",
        description=(
            "The logical id of the resource, as used in the URL for the resource. "
            "Once assigned, this value never changes."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    implicitRules: fhirtypes.Uri = Field(
        None,
        alias="implicitRules",
        title="A set of rules under which this content was created",
        description=(
            "A reference to a set of rules that were followed when the resource was"
            " constructed, and which must be understood when processing the "
            "content."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    implicitRules__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_implicitRules", title="Extension field for ``implicitRules``."
    )

    language: fhirtypes.Code = Field(
        None,
        alias="language",
        title="Language of the resource content",
        description="The base language in which the resource is written.",
        # if property is element of this resource.
        element_property=True,
    )
    language__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_language", title="Extension field for ``language``."
    )

    meta: fhirtypes.MetaType = Field(
        None,
        alias="meta",
        title="Metadata about the resource",
        description=(
            "The metadata about the resource. This is content that is maintained by"
            " the infrastructure. Changes to the content may not always be "
            "associated with version changes to the resource."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Resource`` according specification,
        with preserving original sequence order.
        """
        return ["id", "meta", "implicitRules", "language"]
