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
        title="Business identifier",
        description="A unique identifier assigned to this particular recommendation record.",
        # if property is element of this resource.
        element_property=True,
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Who this profile is for",
        description="The patient the recommendations are for.",
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
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
        title="Date recommendation created",
        description="The date the immunization recommendation was created.",
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
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
        # if property is element of this resource.
        element_property=True,
    )

    doseNumber: fhirtypes.PositiveInt = Field(
        None,
        alias="doseNumber",
        title="Recommended dose number",
        description=(
            "The next recommended dose number (e.g. dose 2 is the next recommended "
            "dose)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    doseNumber__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_doseNumber", title="Extension field for ``doseNumber``."
    )

    forecastStatus: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="forecastStatus",
        title="Vaccine administration status",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    protocol: fhirtypes.ImmunizationRecommendationRecommendationProtocolType = Field(
        None,
        alias="protocol",
        title="Protocol used by recommendation",
        description=(
            "Contains information about the protocol under which the vaccine was "
            "administered."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    supportingImmunization: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingImmunization",
        title="Past immunizations supporting recommendation",
        description=(
            "Immunization event history that supports the status and " "recommendation."
        ),
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Observation", "AllergyIntolerance"],
    )

    targetDisease: fhirtypes.CodeableConceptType = Field(
        None,
        alias="targetDisease",
        title="Disease to be immunized against",
        description="The targeted disease for the recommendation.",
        # if property is element of this resource.
        element_property=True,
    )

    vaccineCode: fhirtypes.CodeableConceptType = Field(
        None,
        alias="vaccineCode",
        title="Vaccine recommendation applies to",
        description="Vaccine that pertains to the recommendation.",
        # if property is element of this resource.
        element_property=True,
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
        title="Type of date",
        description=(
            "Date classification of recommendation.  For example, earliest date to "
            "give, latest date to give, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    value: fhirtypes.DateTime = Field(
        ...,
        alias="value",
        title="Recommended date",
        description="The date whose meaning is specified by dateCriterion.code.",
        # if property is element of this resource.
        element_property=True,
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
        title="Who is responsible for protocol",
        description=(
            "Indicates the authority who published the protocol.  For example, " "ACIP."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Protocol details",
        description=(
            "Contains the description about the protocol under which the vaccine "
            "was administered."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    doseSequence: fhirtypes.PositiveInt = Field(
        None,
        alias="doseSequence",
        title="Dose number within sequence",
        description=(
            "Indicates the nominal position in a series of the next dose.  This is "
            "the recommended dose number as per a specified protocol."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    doseSequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_doseSequence", title="Extension field for ``doseSequence``."
    )

    series: fhirtypes.String = Field(
        None,
        alias="series",
        title="Name of vaccination series",
        description=(
            "One possible path to achieve presumed immunity against a disease - "
            "within the context of an authority."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    series__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_series", title="Extension field for ``series``."
    )
