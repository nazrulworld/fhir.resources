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
    """ Guidance or advice relating to an immunization.
    A patient's point-in-time set of recommendations (i.e. forecasting)
    according to a published schedule with optional supporting justification.
    """

    resource_type = Field("ImmunizationRecommendation", const=True)

    authority: fhirtypes.ReferenceType = Field(
        None,
        alias="authority",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Who is responsible for protocol",
    )

    date: fhirtypes.DateTime = Field(
        ...,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date recommendation(s) created",
    )

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
    """ Vaccine administration recommendations.
    """

    resource_type = Field("ImmunizationRecommendationRecommendation", const=True)

    contraindicatedVaccineCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="contraindicatedVaccineCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Vaccine which is contraindicated to fulfill the recommendation",
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

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Protocol details",
    )

    doseNumberPositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="doseNumberPositiveInt",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Recommended dose number within series",
        one_of_many="doseNumber",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    doseNumberString: fhirtypes.String = Field(
        None,
        alias="doseNumberString",
        title="Type `String` (represented as `dict` in JSON)",
        description="Recommended dose number within series",
        one_of_many="doseNumber",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    forecastReason: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="forecastReason",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Vaccine administration status reason",
    )

    forecastStatus: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="forecastStatus",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Vaccine recommendation status",
    )

    series: fhirtypes.String = Field(
        None,
        alias="series",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of vaccination series",
    )

    seriesDosesPositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="seriesDosesPositiveInt",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Recommended number of doses for immunity",
        one_of_many="seriesDoses",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    seriesDosesString: fhirtypes.String = Field(
        None,
        alias="seriesDosesString",
        title="Type `String` (represented as `dict` in JSON)",
        description="Recommended number of doses for immunity",
        one_of_many="seriesDoses",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    supportingImmunization: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingImmunization",
        title=(
            "List of `Reference` items referencing `Immunization, "
            "ImmunizationEvaluation` (represented as `dict` in JSON)"
        ),
        description="Past immunizations supporting recommendation",
    )

    supportingPatientInformation: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingPatientInformation",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="Patient observations supporting recommendation",
    )

    targetDisease: fhirtypes.CodeableConceptType = Field(
        None,
        alias="targetDisease",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Disease to be immunized against",
    )

    vaccineCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="vaccineCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Vaccine  or vaccine group recommendation applies to",
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
    """ Dates governing proposed immunization.
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
        ...,
        alias="value",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Recommended date",
    )
