# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/DSTU2/riskassessment.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import domainresource, fhirtypes
from .backboneelement import BackboneElement


class RiskAssessment(domainresource.DomainResource):
    """Potential outcomes for a subject with likelihood
    An assessment of the likely outcome(s) for a patient or other subject as
    well as the likelihood of each outcome.
    """

    resource_type = Field("RiskAssessment", const=True)

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title=(
            "Type 'Reference' referencing 'Patient' and 'Group'  "
            "(represented as 'dict' in JSON)."
        ),
        description="Who/what does assessment apply to?",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group"],
        element_property=True,
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="When was assessment made?",
        description="The date (and possibly time) the risk assessment was performed.",
        element_property=True,
    )

    condition: fhirtypes.ReferenceType = Field(
        None,
        alias="condition",
        title="Type 'Reference' referencing 'Condition'  (represented as 'dict' in JSON).",
        description="Condition assessed",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Condition"],
        element_property=True,
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Type 'Reference' referencing 'Encounter'  (represented as 'dict' in JSON).",
        description="Where was assessment performed?",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
        element_property=True,
    )

    performer: fhirtypes.ReferenceType = Field(
        None,
        alias="performer",
        title=(
            "Type 'Reference' referencing 'Practitioner' and "
            "'Device'  (represented as 'dict' in JSON)."
        ),
        description="Who did assessment?",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Device"],
        element_property=True,
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Unique identifier",
        description="Unique identifier for the assessment",
        element_property=True,
    )

    method: fhirtypes.CodeableConceptType = Field(
        None,
        alias="method",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Evaluation mechanism",
        element_property=True,
    )

    basis: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basis",
        title="Type 'Reference' referencing 'Any'  (represented as 'dict' in JSON).",
        description="Information used in assessment",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Any"],
        element_property=True,
    )

    prediction: fhirtypes.RiskAssessmentPredictionType = Field(
        None,
        alias="prediction",
        title="List of Type `RiskAssessmentPrediction` (represented as `dict` in JSON).",
        description="Describes the expected outcome for the subject.",
        element_property=True,
    )

    mitigation: fhirtypes.String = Field(
        None,
        alias="mitigation",
        title="Type `String` (represented as `dict` in JSON)",
        description="How to reduce risk",
        element_property=True,
    )


class RiskAssessmentPrediction(BackboneElement):
    """Outcome predicted

    Describes the expected outcome for the subject.
    """

    resource_type = Field("RiskAssessmentPrediction", const=True)

    outcome: fhirtypes.CodeableConceptType = Field(
        None,
        alias="outcome",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Possible outcome for the subject",
        element_property=True,
    )

    probabilityDecimal: fhirtypes.Decimal = Field(
        None,
        alias="probabilityDecimal",
        title="How likely is the outcome (in the specified timeframe).",
        description="How likely is the outcome (in the specified timeframe).",
        # if property is element of this resource.
        element_property=True,
        one_of_many="probability",
        one_of_many_required=False,
    )

    probabilityRange: fhirtypes.RangeType = Field(
        None,
        alias="probabilityRange",
        title="How likely is the outcome (in the specified timeframe).",
        description="How likely is the outcome (in the specified timeframe).",
        # if property is element of this resource.
        element_property=True,
        one_of_many="probability",
        one_of_many_required=False,
    )

    probabilityCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="probabilityCodeableConcept",
        title="How likely is the outcome (in the specified timeframe).",
        description="How likely is the outcome (in the specified timeframe).",
        # if property is element of this resource.
        element_property=True,
        one_of_many="probability",
        one_of_many_required=False,
    )

    relativeRisk: fhirtypes.Decimal = Field(
        None,
        alias="relativeRisk",
        title="Relative likelihood",
        description=(
            "Indicates the risk for this particular subject (with their specific "
            "characteristics) divided by the risk of the population in general. "
            "(Numbers greater than 1 = higher risk than the population, numbers "
            "less than 1 = lower risk.)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    whenPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="whenPeriod",
        title=(
            "Indicates the period of time or age range of the subject to which"
            " the specified probability applies."
        ),
        description=(
            "Indicates the period of time or age range of the subject to which "
            "the specified probability applies."
        ),
        # if property is element of this resource.
        element_property=True,
        one_of_many="when",
        one_of_many_required=False,
    )

    whenRange: fhirtypes.RangeType = Field(
        None,
        alias="whenRange",
        title=(
            "Indicates the period of time or age range of the subject "
            "to which the specified probability applies."
        ),
        description=(
            "Indicates the period of time or age range of the subject "
            "to which the specified probability applies."
        ),
        # if property is element of this resource.
        element_property=True,
        one_of_many="when",
        one_of_many_required=False,
    )

    rationale: fhirtypes.String = Field(
        None,
        alias="rationale",
        title="Type `String` (represented as `dict` in JSON)",
        description="Explanation of prediction",
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
            "probability": [
                "probabilityDecimal",
                "probabilityRange",
                "probabilityCodeableConcept",
            ],
            "when": ["whenPeriod", "whenRange"],
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
