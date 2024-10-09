from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ParameterDefinition
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import datatype, fhirtypes


class ParameterDefinition(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Definition of a parameter to a module.
    The parameters to the module. This collection specifies both the input and
    output parameters. Input parameters are provided by the caller as part of
    the $evaluate operation. Output parameters are included in the
    GuidanceResponse.
    """

    __resource_type__ = "ParameterDefinition"

    documentation: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="documentation",
        title="A brief description of the parameter",
        description=(
            "A brief discussion of what the parameter is for and how it is used by "
            "the module."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    max: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="max",
        title="Maximum cardinality (a number of *)",
        description=(
            "The maximum number of times this element is permitted to appear in the"
            " request or response."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    max__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_max", title="Extension field for ``max``."
    )

    min: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="min",
        title="Minimum cardinality",
        description=(
            "The minimum number of times this parameter SHALL appear in the request"
            " or response."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    min__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_min", title="Extension field for ``min``."
    )

    name: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name used to access the parameter value",
        description=(
            "The name of the parameter used to allow access to the value of the "
            "parameter in evaluation contexts."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    profile: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="profile",
        title="What profile the value is expected to be",
        description=(
            "If specified, this indicates a profile that the input data must "
            "conform to, or that the output data will conform to."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["StructureDefinition"],
        },
    )
    profile__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_profile", title="Extension field for ``profile``."
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="What type of value",
        description="The type of the parameter.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    use: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="use",
        title="in | out",
        description="Whether the parameter is input or output for the module.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["in", "out"],
        },
    )
    use__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_use", title="Extension field for ``use``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ParameterDefinition`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "name",
            "use",
            "min",
            "max",
            "documentation",
            "type",
            "profile",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("type", "type__ext"), ("use", "use__ext")]
        return required_fields
