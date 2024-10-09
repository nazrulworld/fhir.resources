from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ImmunizationRecommendation
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ImmunizationRecommendation(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Guidance or advice relating to an immunization.
    A patient's point-in-time immunization and recommendation (i.e. forecasting
    a patient's immunization eligibility according to a published schedule)
    with optional supporting justification.
    """

    __resource_type__ = "ImmunizationRecommendation"

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business identifier",
        description="A unique identifier assigned to this particular recommendation record.",
        json_schema_extra={
            "element_property": True,
        },
    )

    patient: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="patient",
        title="Who this profile is for",
        description="The patient the recommendations are for.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient"],
        },
    )

    recommendation: typing.List[fhirtypes.ImmunizationRecommendationRecommendationType] = Field(  # type: ignore
        ...,
        alias="recommendation",
        title="Vaccine administration recommendations",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImmunizationRecommendation`` according specification,
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
            "patient",
            "recommendation",
        ]


class ImmunizationRecommendationRecommendation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Vaccine administration recommendations.
    """

    __resource_type__ = "ImmunizationRecommendationRecommendation"

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="date",
        title="Date recommendation created",
        description="The date the immunization recommendation was created.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    dateCriterion: typing.List[fhirtypes.ImmunizationRecommendationRecommendationDateCriterionType] | None = Field(  # type: ignore
        None,
        alias="dateCriterion",
        title="Dates governing proposed immunization",
        description=(
            "Vaccine date recommendations.  For example, earliest date to "
            "administer, latest date to administer, etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    doseNumber: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="doseNumber",
        title="Recommended dose number",
        description=(
            "The next recommended dose number (e.g. dose 2 is the next recommended "
            "dose)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    doseNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_doseNumber", title="Extension field for ``doseNumber``."
    )

    forecastStatus: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="forecastStatus",
        title="Vaccine administration status",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    protocol: fhirtypes.ImmunizationRecommendationRecommendationProtocolType | None = Field(  # type: ignore
        None,
        alias="protocol",
        title="Protocol used by recommendation",
        description=(
            "Contains information about the protocol under which the vaccine was "
            "administered."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    supportingImmunization: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="supportingImmunization",
        title="Past immunizations supporting recommendation",
        description=(
            "Immunization event history that supports the status and " "recommendation."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Immunization"],
        },
    )

    supportingPatientInformation: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="supportingPatientInformation",
        title="Patient observations supporting recommendation",
        description=(
            "Patient Information that supports the status and recommendation.  This"
            " includes patient observations, adverse reactions and "
            "allergy/intolerance information."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Observation", "AllergyIntolerance"],
        },
    )

    targetDisease: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="targetDisease",
        title="Disease to be immunized against",
        description="The targeted disease for the recommendation.",
        json_schema_extra={
            "element_property": True,
        },
    )

    vaccineCode: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="vaccineCode",
        title="Vaccine recommendation applies to",
        description="Vaccine that pertains to the recommendation.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImmunizationRecommendationRecommendation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "date",
            "vaccineCode",
            "targetDisease",
            "doseNumber",
            "forecastStatus",
            "dateCriterion",
            "protocol",
            "supportingImmunization",
            "supportingPatientInformation",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("date", "date__ext")]
        return required_fields


class ImmunizationRecommendationRecommendationDateCriterion(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Dates governing proposed immunization.
    Vaccine date recommendations.  For example, earliest date to administer,
    latest date to administer, etc.
    """

    __resource_type__ = "ImmunizationRecommendationRecommendationDateCriterion"

    code: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="code",
        title="Type of date",
        description=(
            "Date classification of recommendation.  For example, earliest date to "
            "give, latest date to give, etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    value: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="value",
        title="Recommended date",
        description="The date whose meaning is specified by dateCriterion.code.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImmunizationRecommendationRecommendationDateCriterion`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "value"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("value", "value__ext")]
        return required_fields


class ImmunizationRecommendationRecommendationProtocol(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Protocol used by recommendation.
    Contains information about the protocol under which the vaccine was
    administered.
    """

    __resource_type__ = "ImmunizationRecommendationRecommendationProtocol"

    authority: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="authority",
        title="Who is responsible for protocol",
        description=(
            "Indicates the authority who published the protocol.  For example, " "ACIP."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    description: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Protocol details",
        description=(
            "Contains the description about the protocol under which the vaccine "
            "was administered."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    doseSequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="doseSequence",
        title="Dose number within sequence",
        description=(
            "Indicates the nominal position in a series of the next dose.  This is "
            "the recommended dose number as per a specified protocol."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    doseSequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_doseSequence", title="Extension field for ``doseSequence``."
    )

    series: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="series",
        title="Name of vaccination series",
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

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImmunizationRecommendationRecommendationProtocol`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "doseSequence",
            "description",
            "authority",
            "series",
        ]
