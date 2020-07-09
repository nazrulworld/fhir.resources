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
        title="A brief description of the parameter",
        description=(
            "A brief discussion of what the parameter is for and how it is used by "
            "the module."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    max: fhirtypes.String = Field(
        None,
        alias="max",
        title="Maximum cardinality (a number of *)",
        description=(
            "The maximum number of times this element is permitted to appear in the"
            " request or response."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    max__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_max", title="Extension field for ``max``."
    )

    min: fhirtypes.Integer = Field(
        None,
        alias="min",
        title="Minimum cardinality",
        description=(
            "The minimum number of times this parameter SHALL appear in the request"
            " or response."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    min__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_min", title="Extension field for ``min``."
    )

    name: fhirtypes.Code = Field(
        None,
        alias="name",
        title="Name used to access the parameter value",
        description=(
            "The name of the parameter used to allow access to the value of the "
            "parameter in evaluation contexts."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    profile: fhirtypes.Canonical = Field(
        None,
        alias="profile",
        title="What profile the value is expected to be",
        description=(
            "If specified, this indicates a profile that the input data must "
            "conform to, or that the output data will conform to."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureDefinition"],
    )
    profile__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_profile", title="Extension field for ``profile``."
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="What type of value",
        description="The type of the parameter.",
        # if property is element of this resource.
        element_property=True,
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    use: fhirtypes.Code = Field(
        ...,
        alias="use",
        title="in | out",
        description="Whether the parameter is input or output for the module.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["in", "out"],
    )
    use__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_use", title="Extension field for ``use``."
    )
