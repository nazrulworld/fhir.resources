# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Resource
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
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

    id: fhirtypes.String = Field(
        None,
        alias="id",
        title="Type `String`",
        description="Logical id of this artifact",
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
