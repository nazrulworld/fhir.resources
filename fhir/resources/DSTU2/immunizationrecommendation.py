# -*- coding: utf-8 -*-
"""
Profile: https://www.hl7.org/fhir/DSTU2/immunizationrecommendation.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ImmunizationRecommendation(domainresource.DomainResource):
    """Guidance or advice relating to an immunization.

    A patient's point-in-time set of recommendations (i.e. forecasting)
    according to a published schedule with optional supporting justification.
    """

    resource_type = Field("ImmunizationRecommendation", const=True)

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier",
        description="A unique identifier assigned to this particular recommendation record.",
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Who this profile is for",
        description="The patient the recommendation(s) are for.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    recommendation: ListType[
        fhirtypes.ImmunizationRecommendationRecommendationType
    ] = Field(
        ...,
        alias="recommendation",
        title="Vaccine administration recommendations",
        description=None,
    )


class ImmunizationRecommendationRecommendation(backboneelement.BackboneElement):
    """Vaccine administration recommendations."""

    resource_type = Field("ImmunizationRecommendationRecommendation", const=True)

    date: fhirtypes.DateTime = Field(
        ...,
        alias="date",
        title="Type `Date` (represented as `str` in JSON).",
        description="Date recommendation created.",
    )

    dateCriterion: ListType[
        fhirtypes.ImmunizationRecommendationRecommendationDateCriterionType
    ] = Field(
        None,
        alias="dateCriterion",
        title="Dates governing proposed immunization",
        description=(
            "Vaccine date recommendations.  For example, earliest date to "
            "administer, latest date to administer, etc."
        ),
    )

    doseNumber: fhirtypes.PositiveInt = Field(
        None,
        alias="doseNumber",
        title="Recommended dose number within series",
        description=(
            "Nominal position of the recommended dose in a series (e.g. dose 2 is "
            "the next recommended dose)."
        ),
    )

    forecastStatus: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="forecastStatus",
        title="Vaccine recommendation status",
        description=(
            "Indicates the patient status with respect to the path to immunity for "
            "the target disease."
        ),
    )

    protocol: fhirtypes.ImmunizationRecommendationRecommendationProtocolType = Field(
        None,
        alias="protocol",
        title=(
            "Type `ImmunizationRecommendationRecommendationProtocol` (represented as "
            "`dict` in JSON)."
        ),
        description="Protocol used by recommendation.",
    )

    supportingImmunization: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingImmunization",
        title="Past immunizations supporting recommendation",
        description=(
            "Immunization event history and/or evaluation that supports the status "
            "and recommendation."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Immunization"],
    )

    supportingPatientInformation: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingPatientInformation",
        title="Patient observations supporting recommendation",
        description=(
            "Patient Information that supports the status and recommendation.  This"
            " includes patient observations, adverse reactions and "
            "allergy/intolerance information."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Observation", "AllergyIntolerance"],
    )

    vaccineCode: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="vaccineCode",
        title="Vaccine or vaccine group recommendation applies to",
        description="Vaccine(s) or vaccine group that pertain to the recommendation.",
    )


class ImmunizationRecommendationRecommendationDateCriterion(
    backboneelement.BackboneElement
):
    """Dates governing proposed immunization.

    Vaccine date recommendations.  For example, earliest date to administer,
    latest date to administer, etc.
    """

    resource_type = Field(
        "ImmunizationRecommendationRecommendationDateCriterion", const=True
    )

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Type of date",
        description=(
            "Date classification of recommendation.  For example, earliest date to "
            "give, latest date to give, etc."
        ),
    )

    value: fhirtypes.DateTime = Field(
        ...,
        alias="value",
        title="Recommended date",
        description="The date whose meaning is specified by dateCriterion.code.",
    )


class ImmunizationRecommendationRecommendationProtocol(backboneelement.BackboneElement):
    """"""

    resource_type = Field(
        "ImmunizationRecommendationRecommendationProtocol", const=True
    )

    authority: fhirtypes.ReferenceType = Field(
        None,
        alias="authority",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON).",
        description="Who is responsible for protocol.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `str`.",
        description="Protocol details.",
    )

    doseSequence: fhirtypes.Integer = Field(
        None,
        alias="doseSequence",
        title="Type `int`.",
        description="Dose number within sequence.",
    )

    series: fhirtypes.String = Field(
        None,
        alias="series",
        title="Type `str`.",
        description="Name of vaccination series.",
    )
