# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/RiskAssessment
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class RiskAssessment(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Potential outcomes for a subject with likelihood.
    An assessment of the likely outcome(s) for a patient or other subject as
    well as the likelihood of each outcome.
    """

    resource_type = Field("RiskAssessment", const=True)

    basedOn: fhirtypes.ReferenceType = Field(
        None,
        alias="basedOn",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Request fulfilled by this assessment",
    )

    basis: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basis",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="Information used in assessment",
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of assessment",
    )

    condition: fhirtypes.ReferenceType = Field(
        None,
        alias="condition",
        title=(
            "Type `Reference` referencing `Condition` (represented as `dict` in "
            "JSON)"
        ),
        description="Condition assessed",
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title=(
            "Type `Reference` referencing `Encounter` (represented as `dict` in "
            "JSON)"
        ),
        description="Where was assessment performed?",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
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
        title="Type `String`",
        description="How to reduce risk",
    )
    mitigation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_mitigation", title="Extension field for ``mitigation``."
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Comments on the risk assessment",
    )

    occurrenceDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurrenceDateTime",
        title="Type `DateTime`",
        description="When was assessment made?",
        one_of_many="occurrence",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_occurrenceDateTime",
        title="Extension field for ``occurrenceDateTime``.",
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
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Part of this occurrence",
    )

    performer: fhirtypes.ReferenceType = Field(
        None,
        alias="performer",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole, Device` "
            "(represented as `dict` in JSON)"
        ),
        description="Who did assessment?",
    )

    prediction: ListType[fhirtypes.RiskAssessmentPredictionType] = Field(
        None,
        alias="prediction",
        title=(
            "List of `RiskAssessmentPrediction` items (represented as `dict` in "
            "JSON)"
        ),
        description="Outcome predicted",
    )

    reasonCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Why the assessment was necessary?",
    )

    reasonReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title=(
            "List of `Reference` items referencing `Condition, Observation, "
            "DiagnosticReport, DocumentReference` (represented as `dict` in JSON)"
        ),
        description="Why the assessment was necessary?",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`",
        description="registered | preliminary | final | amended +",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title=(
            "Type `Reference` referencing `Patient, Group` (represented as `dict` "
            "in JSON)"
        ),
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
        one_of_many_fields = {"occurrence": ["occurrenceDateTime", "occurrencePeriod"]}
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Outcome predicted.
    Describes the expected outcome for the subject.
    """

    resource_type = Field("RiskAssessmentPrediction", const=True)

    outcome: fhirtypes.CodeableConceptType = Field(
        None,
        alias="outcome",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Possible outcome for the subject",
    )

    probabilityDecimal: fhirtypes.Decimal = Field(
        None,
        alias="probabilityDecimal",
        title="Type `Decimal`",
        description="Likelihood of specified outcome",
        one_of_many="probability",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    probabilityDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_probabilityDecimal",
        title="Extension field for ``probabilityDecimal``.",
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
        title="Type `String`",
        description="Explanation of prediction",
    )
    rationale__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_rationale", title="Extension field for ``rationale``."
    )

    relativeRisk: fhirtypes.Decimal = Field(
        None,
        alias="relativeRisk",
        title="Type `Decimal`",
        description="Relative likelihood",
    )
    relativeRisk__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_relativeRisk", title="Extension field for ``relativeRisk``."
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
            "probability": ["probabilityDecimal", "probabilityRange"],
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
