# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Resource
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic import Field

from . import fhirresourcemodel, fhirtypes


class Resource(fhirresourcemodel.FHIRResourceModel):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Base Resource.
    This is the base resource type for everything.
    """

    resource_type = Field("Resource", const=True)

    id: fhirtypes.Id = Field(
        None, alias="id", title="Type `Id`", description="Logical id of this artifact"
    )
    id__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_id", title="Extension field for ``id``."
    )

    implicitRules: fhirtypes.Uri = Field(
        None,
        alias="implicitRules",
        title="Type `Uri`",
        description="A set of rules under which this content was created",
    )
    implicitRules__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_implicitRules", title="Extension field for ``implicitRules``."
    )

    language: fhirtypes.Code = Field(
        None,
        alias="language",
        title="Type `Code`",
        description="Language of the resource content",
    )
    language__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_language", title="Extension field for ``language``."
    )

    meta: fhirtypes.MetaType = Field(
        None,
        alias="meta",
        title="Type `Meta` (represented as `dict` in JSON)",
        description="Metadata about the resource",
    )
