# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Resource
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from pydantic.v1 import Field

from . import fhirtypes
from .fhirresourcemodel import FHIRResourceModel


class Resource(FHIRResourceModel):
    """Base Resource.
    This is the base resource type for everything.
    """

    resource_type = Field("Resource", const=True)

    id: fhirtypes.Id = Field(
        None,
        alias="id",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Logical id of this artifact",
    )

    implicitRules: fhirtypes.Uri = Field(
        None,
        alias="implicitRules",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="A set of rules under which this content was created",
    )

    language: fhirtypes.Code = Field(
        None,
        alias="language",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Language of the resource content",
    )

    meta: fhirtypes.MetaType = Field(
        None,
        alias="meta",
        title="Type `Meta` (represented as `dict` in JSON)",
        description="Metadata about the resource",
    )
