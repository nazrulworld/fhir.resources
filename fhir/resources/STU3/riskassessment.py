# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/RiskAssessment
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class RiskAssessment(domainresource.DomainResource):
    """ Potential outcomes for a subject with likelihood.
    An assessment of the likely outcome(s) for a patient or other subject as
    well as the likelihood of each outcome.
    """

    resource_type = Field("RiskAssessment", const=True)

    basedOn: fhirtypes.ReferenceType = Field(
        None,
        alias="basedOn",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="Request fulfilled by this assessment",
    )

    basis: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basis",
        title="List of `Reference` items referencing `Resource` (represented as `dict` in JSON)",
        description="Information used in assessment",
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of assessment",
    )

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Type `String` (represented as `dict` in JSON)",
        description="Comments on the risk assessment",
    )

    condition: fhirtypes.ReferenceType = Field(
        None,
        alias="condition",
        title="Type `Reference` referencing `Condition` (represented as `dict` in JSON)",
        description="Condition assessed",
    )

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title="Type `Reference` referencing `Encounter, EpisodeOfCare` (represented as `dict` in JSON)",
        description="Where was assessment performed?",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Unique identifier for the assessment",
    )

    method: fhirtypes.CodeableConceptType = Field(
        None,
        alias="method",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Evaluation mechanism",
    )

    mitigation: fhirtypes.String = Field(
        None,
        alias="mitigation",
        title="Type `String` (represented as `dict` in JSON)",
        description="How to reduce risk",
    )

    occurrenceDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurrenceDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When was assessment made?",
        one_of_many="occurrence",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    occurrencePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="occurrencePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When was assessment made?",
        one_of_many="occurrence",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    parent: fhirtypes.ReferenceType = Field(
        None,
        alias="parent",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="Part of this occurrence",
    )

    performer: fhirtypes.ReferenceType = Field(
        None,
        alias="performer",
        title="Type `Reference` referencing `Practitioner, Device` (represented as `dict` in JSON)",
        description="Who did assessment?",
    )

    prediction: ListType[fhirtypes.RiskAssessmentPredictionType] = Field(
        None,
        alias="prediction",
        title="List of `RiskAssessmentPrediction` items (represented as `dict` in JSON)",
        description="Outcome predicted",
    )

    reasonCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reasonCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Why the assessment was necessary?",
        one_of_many="reason",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    reasonReference: fhirtypes.ReferenceType = Field(
        None,
        alias="reasonReference",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="Why the assessment was necessary?",
        one_of_many="reason",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="registered | preliminary | final | amended +",
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Type `Reference` referencing `Patient, Group` (represented as `dict` in JSON)",
        description="Who/what does assessment apply to?",
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
            "occurrence": ["occurrenceDateTime", "occurrencePeriod",],
            "reason": ["reasonCodeableConcept", "reasonReference",],
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


class RiskAssessmentPrediction(backboneelement.BackboneElement):
    """ Outcome predicted.
    Describes the expected outcome for the subject.
    """

    resource_type = Field("RiskAssessmentPrediction", const=True)

    outcome: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="outcome",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Possible outcome for the subject",
    )

    probabilityDecimal: fhirtypes.Decimal = Field(
        None,
        alias="probabilityDecimal",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Likelihood of specified outcome",
        one_of_many="probability",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    probabilityRange: fhirtypes.RangeType = Field(
        None,
        alias="probabilityRange",
        title="Type `Range` (represented as `dict` in JSON)",
        description="Likelihood of specified outcome",
        one_of_many="probability",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    qualitativeRisk: fhirtypes.CodeableConceptType = Field(
        None,
        alias="qualitativeRisk",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Likelihood of specified outcome as a qualitative value",
    )

    rationale: fhirtypes.String = Field(
        None,
        alias="rationale",
        title="Type `String` (represented as `dict` in JSON)",
        description="Explanation of prediction",
    )

    relativeRisk: fhirtypes.Decimal = Field(
        None,
        alias="relativeRisk",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Relative likelihood",
    )

    whenPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="whenPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Timeframe or age range",
        one_of_many="when",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    whenRange: fhirtypes.RangeType = Field(
        None,
        alias="whenRange",
        title="Type `Range` (represented as `dict` in JSON)",
        description="Timeframe or age range",
        one_of_many="when",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
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
            "probability": ["probabilityDecimal", "probabilityRange",],
            "when": ["whenPeriod", "whenRange",],
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
