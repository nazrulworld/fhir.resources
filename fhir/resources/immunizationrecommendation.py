# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ImmunizationRecommendation
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class ImmunizationRecommendation(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Guidance or advice relating to an immunization.
    A patient's point-in-time set of recommendations (i.e. forecasting)
    according to a published schedule with optional supporting justification.
    """

    resource_type = Field("ImmunizationRecommendation", const=True)

    authority: fhirtypes.ReferenceType = Field(
        None,
        alias="authority",
        title="Who is responsible for protocol",
        description="Indicates the authority who published the protocol (e.g. ACIP).",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    date: fhirtypes.DateTime = Field(
        ...,
        alias="date",
        title="Date recommendation(s) created",
        description="The date the immunization recommendation(s) were created.",
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

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
        description="The patient the recommendation(s) are for.",
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

    contraindicatedVaccineCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="contraindicatedVaccineCode",
        title="Vaccine which is contraindicated to fulfill the recommendation",
        description="Vaccine(s) which should not be used to fulfill the recommendation.",
        # if property is element of this resource.
        element_property=True,
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

    doseNumberPositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="doseNumberPositiveInt",
        title="Recommended dose number within series",
        description=(
            "Nominal position of the recommended dose in a series (e.g. dose 2 is "
            "the next recommended dose)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e doseNumber[x]
        one_of_many="doseNumber",
        one_of_many_required=False,
    )
    doseNumberPositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_doseNumberPositiveInt",
        title="Extension field for ``doseNumberPositiveInt``.",
    )

    doseNumberString: fhirtypes.String = Field(
        None,
        alias="doseNumberString",
        title="Recommended dose number within series",
        description=(
            "Nominal position of the recommended dose in a series (e.g. dose 2 is "
            "the next recommended dose)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e doseNumber[x]
        one_of_many="doseNumber",
        one_of_many_required=False,
    )
    doseNumberString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_doseNumberString",
        title="Extension field for ``doseNumberString``.",
    )

    forecastReason: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="forecastReason",
        title="Vaccine administration status reason",
        description="The reason for the assigned forecast status.",
        # if property is element of this resource.
        element_property=True,
    )

    forecastStatus: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="forecastStatus",
        title="Vaccine recommendation status",
        description=(
            "Indicates the patient status with respect to the path to immunity for "
            "the target disease."
        ),
        # if property is element of this resource.
        element_property=True,
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

    seriesDosesPositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="seriesDosesPositiveInt",
        title="Recommended number of doses for immunity",
        description="The recommended number of doses to achieve immunity.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e seriesDoses[x]
        one_of_many="seriesDoses",
        one_of_many_required=False,
    )
    seriesDosesPositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_seriesDosesPositiveInt",
        title="Extension field for ``seriesDosesPositiveInt``.",
    )

    seriesDosesString: fhirtypes.String = Field(
        None,
        alias="seriesDosesString",
        title="Recommended number of doses for immunity",
        description="The recommended number of doses to achieve immunity.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e seriesDoses[x]
        one_of_many="seriesDoses",
        one_of_many_required=False,
    )
    seriesDosesString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_seriesDosesString",
        title="Extension field for ``seriesDosesString``.",
    )

    supportingImmunization: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingImmunization",
        title="Past immunizations supporting recommendation",
        description=(
            "Immunization event history and/or evaluation that supports the status "
            "and recommendation."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Immunization", "ImmunizationEvaluation"],
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
        enum_reference_types=["Resource"],
    )

    targetDisease: fhirtypes.CodeableConceptType = Field(
        None,
        alias="targetDisease",
        title="Disease to be immunized against",
        description="The targeted disease for the recommendation.",
        # if property is element of this resource.
        element_property=True,
    )

    vaccineCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="vaccineCode",
        title="Vaccine  or vaccine group recommendation applies to",
        description="Vaccine(s) or vaccine group that pertain to the recommendation.",
        # if property is element of this resource.
        element_property=True,
    )

    @root_validator(pre=True)
    def validate_one_of_many(cls, values: Dict[str, Any]) -> Dict[str, Any]:
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
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values


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
