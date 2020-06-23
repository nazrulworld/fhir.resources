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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Definition of a parameter to a module.
    The parameters to the module. This collection specifies both the input and
    output parameters. Input parameters are provided by the caller as part of
    the $evaluate operation. Output parameters are included in the
    GuidanceResponse.
    """

    resource_type = Field("ParameterDefinition", const=True)

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String`",
        description="A brief description of the parameter",
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    max: fhirtypes.String = Field(
        None,
        alias="max",
        title="Type `String`",
        description="Maximum cardinality (a number of *)",
    )
    max__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_max", title="Extension field for ``max``."
    )

    min: fhirtypes.Integer = Field(
        None, alias="min", title="Type `Integer`", description="Minimum cardinality"
    )
    min__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_min", title="Extension field for ``min``."
    )

    name: fhirtypes.Code = Field(
        None,
        alias="name",
        title="Type `Code`",
        description="Name used to access the parameter value",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    profile: fhirtypes.Canonical = Field(
        None,
        alias="profile",
        title="Type `Canonical` referencing `StructureDefinition`",
        description="What profile the value is expected to be",
    )
    profile__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_profile", title="Extension field for ``profile``."
    )

    type: fhirtypes.Code = Field(
        ..., alias="type", title="Type `Code`", description="What type of value"
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    use: fhirtypes.Code = Field(
        ..., alias="use", title="Type `Code`", description="in | out"
    )
    use__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_use", title="Extension field for ``use``."
    )
