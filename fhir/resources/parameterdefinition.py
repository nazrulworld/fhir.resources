# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ParameterDefinition
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
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

    profile: fhirtypes.Canonical = Field(
        None,
        alias="profile",
        title="Type `Canonical` referencing `StructureDefinition` (represented as `dict` in JSON)",
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
