# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ParameterDefinition
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic import Field

from . import element, fhirtypes


class ParameterDefinition(element.Element):
    """ Definition of a parameter to a module.
    The parameters to the module. This collection specifies both the input and
    output parameters. Input parameters are provided by the caller as part of
    the $evaluate operation. Output parameters are included in the
    GuidanceResponse.
    """

    resource_type = Field("ParameterDefinition", const=True)

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String` (represented as `dict` in JSON)",
        description="A brief description of the parameter",
    )

    max: fhirtypes.String = Field(
        None,
        alias="max",
        title="Type `String` (represented as `dict` in JSON)",
        description="Maximum cardinality (a number of *)",
    )

    min: fhirtypes.Integer = Field(
        None,
        alias="min",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Minimum cardinality",
    )

    name: fhirtypes.Code = Field(
        None,
        alias="name",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Name used to access the parameter value",
    )

    profile: fhirtypes.ReferenceType = Field(
        None,
        alias="profile",
        title="Type `Reference` referencing `StructureDefinition` (represented as `dict` in JSON)",
        description="What profile the value is expected to be",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="What type of value",
    )

    use: fhirtypes.Code = Field(
        ...,
        alias="use",
        title="Type `Code` (represented as `dict` in JSON)",
        description="in | out",
    )
