from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ImmunizationEvaluation
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import domainresource, fhirtypes


class ImmunizationEvaluation(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Immunization evaluation information.
    Describes a comparison of an immunization event against published
    recommendations to determine if the administration is "valid" in relation
    to those  recommendations.
    """

    __resource_type__ = "ImmunizationEvaluation"

    authority: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="authority",
        title="Who is responsible for publishing the recommendations",
        description="Indicates the authority who published the protocol (e.g. ACIP).",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="date",
        title="Date evaluation was performed",
        description=(
            "The date the evaluation of the vaccine administration event was "
            "performed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Evaluation notes",
        description="Additional information about the evaluation.",
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    doseNumberPositiveInt: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="doseNumberPositiveInt",
        title="Dose number within series",
        description="Nominal position in a series.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e doseNumber[x]
            "one_of_many": "doseNumber",
            "one_of_many_required": False,
        },
    )
    doseNumberPositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_doseNumberPositiveInt",
        title="Extension field for ``doseNumberPositiveInt``.",
    )

    doseNumberString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="doseNumberString",
        title="Dose number within series",
        description="Nominal position in a series.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e doseNumber[x]
            "one_of_many": "doseNumber",
            "one_of_many_required": False,
        },
    )
    doseNumberString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_doseNumberString",
        title="Extension field for ``doseNumberString``.",
    )

    doseStatus: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="doseStatus",
        title="Status of the dose relative to published recommendations",
        description=(
            "Indicates if the dose is valid or not valid with respect to the "
            "published recommendations."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    doseStatusReason: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="doseStatusReason",
        title="Reason for the dose status",
        description=(
            "Provides an explanation as to why the vaccine administration event is "
            "valid or not relative to the published recommendations."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business identifier",
        description="A unique identifier assigned to this immunization evaluation record.",
        json_schema_extra={
            "element_property": True,
        },
    )

    immunizationEvent: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="immunizationEvent",
        title="Immunization being evaluated",
        description="The vaccine administration event being evaluated.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Immunization"],
        },
    )

    patient: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="patient",
        title="Who this evaluation is for",
        description="The individual for whom the evaluation is being done.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient"],
        },
    )

    series: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="series",
        title="Name of vaccine series",
        description=(
            "One possible path to achieve presumed immunity against a disease - "
            "within the context of an authority."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    series__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_series", title="Extension field for ``series``."
    )

    seriesDosesPositiveInt: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="seriesDosesPositiveInt",
        title="Recommended number of doses for immunity",
        description="The recommended number of doses to achieve immunity.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e seriesDoses[x]
            "one_of_many": "seriesDoses",
            "one_of_many_required": False,
        },
    )
    seriesDosesPositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_seriesDosesPositiveInt",
        title="Extension field for ``seriesDosesPositiveInt``.",
    )

    seriesDosesString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="seriesDosesString",
        title="Recommended number of doses for immunity",
        description="The recommended number of doses to achieve immunity.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e seriesDoses[x]
            "one_of_many": "seriesDoses",
            "one_of_many_required": False,
        },
    )
    seriesDosesString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_seriesDosesString",
        title="Extension field for ``seriesDosesString``.",
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="completed | entered-in-error",
        description=(
            "Indicates the current status of the evaluation of the vaccination "
            "administration event."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["completed", "entered-in-error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    targetDisease: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="targetDisease",
        title="Evaluation target disease",
        description="The vaccine preventable disease the dose is being evaluated against.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImmunizationEvaluation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "identifier",
            "status",
            "patient",
            "date",
            "authority",
            "targetDisease",
            "immunizationEvent",
            "doseStatus",
            "doseStatusReason",
            "description",
            "series",
            "doseNumberPositiveInt",
            "doseNumberString",
            "seriesDosesPositiveInt",
            "seriesDosesString",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        return required_fields

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "doseNumber": ["doseNumberPositiveInt", "doseNumberString"],
            "seriesDoses": ["seriesDosesPositiveInt", "seriesDosesString"],
        }
        return one_of_many_fields
