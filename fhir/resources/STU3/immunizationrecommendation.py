# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ImmunizationRecommendation
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ImmunizationRecommendation(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Guidance or advice relating to an immunization.
    A patient's point-in-time immunization and recommendation (i.e. forecasting
    a patient's immunization eligibility according to a published schedule)
    with optional supporting justification.
    """

    resource_type = Field("ImmunizationRecommendation", const=True)

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business identifier",
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="Who this profile is for",
    )

    recommendation: ListType[
        fhirtypes.ImmunizationRecommendationRecommendationType
    ] = Field(
        ...,
        alias="recommendation",
        title=(
            "List of `ImmunizationRecommendationRecommendation` items (represented "
            "as `dict` in JSON)"
        ),
        description="Vaccine administration recommendations",
    )


class ImmunizationRecommendationRecommendation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Vaccine administration recommendations.
    """

    resource_type = Field("ImmunizationRecommendationRecommendation", const=True)

    date: fhirtypes.DateTime = Field(
        ...,
        alias="date",
        title="Type `DateTime`",
        description="Date recommendation created",
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    dateCriterion: ListType[
        fhirtypes.ImmunizationRecommendationRecommendationDateCriterionType
    ] = Field(
        None,
        alias="dateCriterion",
        title=(
            "List of `ImmunizationRecommendationRecommendationDateCriterion` items "
            "(represented as `dict` in JSON)"
        ),
        description="Dates governing proposed immunization",
    )

    doseNumber: fhirtypes.PositiveInt = Field(
        None,
        alias="doseNumber",
        title="Type `PositiveInt`",
        description="Recommended dose number",
    )
    doseNumber__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_doseNumber", title="Extension field for ``doseNumber``."
    )

    forecastStatus: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="forecastStatus",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Vaccine administration status",
    )

    protocol: fhirtypes.ImmunizationRecommendationRecommendationProtocolType = Field(
        None,
        alias="protocol",
        title=(
            "Type `ImmunizationRecommendationRecommendationProtocol` (represented "
            "as `dict` in JSON)"
        ),
        description="Protocol used by recommendation",
    )

    supportingImmunization: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingImmunization",
        title=(
            "List of `Reference` items referencing `Immunization` (represented as "
            "`dict` in JSON)"
        ),
        description="Past immunizations supporting recommendation",
    )

    supportingPatientInformation: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingPatientInformation",
        title=(
            "List of `Reference` items referencing `Observation, "
            "AllergyIntolerance` (represented as `dict` in JSON)"
        ),
        description="Patient observations supporting recommendation",
    )

    targetDisease: fhirtypes.CodeableConceptType = Field(
        None,
        alias="targetDisease",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Disease to be immunized against",
    )

    vaccineCode: fhirtypes.CodeableConceptType = Field(
        None,
        alias="vaccineCode",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Vaccine recommendation applies to",
    )


class ImmunizationRecommendationRecommendationDateCriterion(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Dates governing proposed immunization.
    Vaccine date recommendations.  For example, earliest date to administer,
    latest date to administer, etc.
    """

    resource_type = Field(
        "ImmunizationRecommendationRecommendationDateCriterion", const=True
    )

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of date",
    )

    value: fhirtypes.DateTime = Field(
        ..., alias="value", title="Type `DateTime`", description="Recommended date"
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )


class ImmunizationRecommendationRecommendationProtocol(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Protocol used by recommendation.
    Contains information about the protocol under which the vaccine was
    administered.
    """

    resource_type = Field(
        "ImmunizationRecommendationRecommendationProtocol", const=True
    )

    authority: fhirtypes.ReferenceType = Field(
        None,
        alias="authority",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Who is responsible for protocol",
    )

    description: fhirtypes.String = Field(
        None, alias="description", title="Type `String`", description="Protocol details"
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    doseSequence: fhirtypes.PositiveInt = Field(
        None,
        alias="doseSequence",
        title="Type `PositiveInt`",
        description="Dose number within sequence",
    )
    doseSequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_doseSequence", title="Extension field for ``doseSequence``."
    )

    series: fhirtypes.String = Field(
        None,
        alias="series",
        title="Type `String`",
        description="Name of vaccination series",
    )
    series__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_series", title="Extension field for ``series``."
    )
