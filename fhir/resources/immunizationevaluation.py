from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ImmunizationEvaluation
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
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

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
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

    doseNumber: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="doseNumber",
        title="Dose number within series",
        description=(
            "Nominal position in a series as determined by the outcome of the "
            "evaluation process."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    doseNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_doseNumber", title="Extension field for ``doseNumber``."
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
        title="Reason why the doese is considered valid, invalid or some other status",
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

    seriesDoses: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="seriesDoses",
        title="Recommended number of doses for immunity",
        description=(
            "The recommended number of doses to achieve immunity as determined by "
            "the outcome of the evaluation process."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    seriesDoses__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_seriesDoses", title="Extension field for ``seriesDoses``."
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
        title="The vaccine preventable disease schedule being evaluated",
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
            "doseNumber",
            "seriesDoses",
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
