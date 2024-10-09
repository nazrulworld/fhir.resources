from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ImmunizationRecommendation
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ImmunizationRecommendation(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Guidance or advice relating to an immunization.
    A patient's point-in-time set of recommendations (i.e. forecasting)
    according to a published schedule with optional supporting justification.
    """

    __resource_type__ = "ImmunizationRecommendation"

    authority: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="authority",
        title="Who is responsible for protocol",
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
        title="Date recommendation(s) created",
        description="The date the immunization recommendation(s) were created.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

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
        description="The patient the recommendation(s) are for.",
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
            "date",
            "authority",
            "recommendation",
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


class ImmunizationRecommendationRecommendation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Vaccine administration recommendations.
    """

    __resource_type__ = "ImmunizationRecommendationRecommendation"

    contraindicatedVaccineCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="contraindicatedVaccineCode",
        title="Vaccine which is contraindicated to fulfill the recommendation",
        description="Vaccine(s) which should not be used to fulfill the recommendation.",
        json_schema_extra={
            "element_property": True,
        },
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

    doseNumberPositiveInt: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="doseNumberPositiveInt",
        title="Recommended dose number within series",
        description=(
            "Nominal position of the recommended dose in a series (e.g. dose 2 is "
            "the next recommended dose)."
        ),
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
        title="Recommended dose number within series",
        description=(
            "Nominal position of the recommended dose in a series (e.g. dose 2 is "
            "the next recommended dose)."
        ),
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

    forecastReason: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="forecastReason",
        title="Vaccine administration status reason",
        description="The reason for the assigned forecast status.",
        json_schema_extra={
            "element_property": True,
        },
    )

    forecastStatus: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="forecastStatus",
        title="Vaccine recommendation status",
        description=(
            "Indicates the patient status with respect to the path to immunity for "
            "the target disease."
        ),
        json_schema_extra={
            "element_property": True,
        },
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

    supportingImmunization: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="supportingImmunization",
        title="Past immunizations supporting recommendation",
        description=(
            "Immunization event history and/or evaluation that supports the status "
            "and recommendation."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Immunization", "ImmunizationEvaluation"],
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
            "enum_reference_types": ["Resource"],
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

    vaccineCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="vaccineCode",
        title="Vaccine  or vaccine group recommendation applies to",
        description="Vaccine(s) or vaccine group that pertain to the recommendation.",
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
            "vaccineCode",
            "targetDisease",
            "contraindicatedVaccineCode",
            "forecastStatus",
            "forecastReason",
            "dateCriterion",
            "description",
            "series",
            "doseNumberPositiveInt",
            "doseNumberString",
            "seriesDosesPositiveInt",
            "seriesDosesString",
            "supportingImmunization",
            "supportingPatientInformation",
        ]

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
