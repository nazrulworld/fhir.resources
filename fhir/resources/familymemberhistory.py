# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/FamilyMemberHistory
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType
from typing import Union

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class FamilyMemberHistory(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about patient's relatives, relevant for patient.
    Significant health conditions for a person related to the patient relevant
    in the context of care for the patient.
    """

    resource_type = Field("FamilyMemberHistory", const=True)

    ageAge: fhirtypes.AgeType = Field(
        None,
        alias="ageAge",
        title="Type `Age` (represented as `dict` in JSON)",
        description="(approximate) age",
        one_of_many="age",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    ageRange: fhirtypes.RangeType = Field(
        None,
        alias="ageRange",
        title="Type `Range` (represented as `dict` in JSON)",
        description="(approximate) age",
        one_of_many="age",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    ageString: fhirtypes.String = Field(
        None,
        alias="ageString",
        title="Type `String`",
        description="(approximate) age",
        one_of_many="age",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    ageString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_ageString", title="Extension field for ``ageString``."
    )

    bornDate: fhirtypes.Date = Field(
        None,
        alias="bornDate",
        title="Type `Date`",
        description="(approximate) date of birth",
        one_of_many="born",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    bornDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_bornDate", title="Extension field for ``bornDate``."
    )

    bornPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="bornPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="(approximate) date of birth",
        one_of_many="born",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    bornString: fhirtypes.String = Field(
        None,
        alias="bornString",
        title="Type `String`",
        description="(approximate) date of birth",
        one_of_many="born",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    bornString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_bornString", title="Extension field for ``bornString``."
    )

    condition: ListType[fhirtypes.FamilyMemberHistoryConditionType] = Field(
        None,
        alias="condition",
        title=(
            "List of `FamilyMemberHistoryCondition` items (represented as `dict` in"
            " JSON)"
        ),
        description="Condition that the related person had",
    )

    dataAbsentReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="dataAbsentReason",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="subject-unknown | withheld | unable-to-obtain | deferred",
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime`",
        description="When history was recorded or last updated",
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    deceasedAge: fhirtypes.AgeType = Field(
        None,
        alias="deceasedAge",
        title="Type `Age` (represented as `dict` in JSON)",
        description="Dead? How old/when?",
        one_of_many="deceased",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    deceasedBoolean: bool = Field(
        None,
        alias="deceasedBoolean",
        title="Type `bool`",
        description="Dead? How old/when?",
        one_of_many="deceased",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    deceasedBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_deceasedBoolean", title="Extension field for ``deceasedBoolean``."
    )

    deceasedDate: fhirtypes.Date = Field(
        None,
        alias="deceasedDate",
        title="Type `Date`",
        description="Dead? How old/when?",
        one_of_many="deceased",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    deceasedDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_deceasedDate", title="Extension field for ``deceasedDate``."
    )

    deceasedRange: fhirtypes.RangeType = Field(
        None,
        alias="deceasedRange",
        title="Type `Range` (represented as `dict` in JSON)",
        description="Dead? How old/when?",
        one_of_many="deceased",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    deceasedString: fhirtypes.String = Field(
        None,
        alias="deceasedString",
        title="Type `String`",
        description="Dead? How old/when?",
        one_of_many="deceased",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    deceasedString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_deceasedString", title="Extension field for ``deceasedString``."
    )

    estimatedAge: bool = Field(
        None, alias="estimatedAge", title="Type `bool`", description="Age is estimated?"
    )
    estimatedAge__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_estimatedAge", title="Extension field for ``estimatedAge``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="External Id(s) for this record",
    )

    instantiatesCanonical: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="instantiatesCanonical",
        title=(
            "List of `Canonical` items referencing `PlanDefinition, Questionnaire, "
            "ActivityDefinition, Measure, OperationDefinition`"
        ),
        description="Instantiates FHIR protocol or definition",
    )
    instantiatesCanonical__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_instantiatesCanonical",
        title="Extension field for ``instantiatesCanonical``.",
    )

    instantiatesUri: ListType[fhirtypes.Uri] = Field(
        None,
        alias="instantiatesUri",
        title="List of `Uri` items",
        description="Instantiates external protocol or definition",
    )
    instantiatesUri__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_instantiatesUri", title="Extension field for ``instantiatesUri``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`",
        description="The family member described",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="General note about related person",
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="Patient history is about",
    )

    reasonCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Why was family member history performed?",
    )

    reasonReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title=(
            "List of `Reference` items referencing `Condition, Observation, "
            "AllergyIntolerance, QuestionnaireResponse, DiagnosticReport, "
            "DocumentReference` (represented as `dict` in JSON)"
        ),
        description="Why was family member history performed?",
    )

    relationship: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="relationship",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Relationship to the subject",
    )

    sex: fhirtypes.CodeableConceptType = Field(
        None,
        alias="sex",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="male | female | other | unknown",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`",
        description="partial | completed | entered-in-error | health-unknown",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
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
            "age": ["ageAge", "ageRange", "ageString"],
            "born": ["bornDate", "bornPeriod", "bornString"],
            "deceased": [
                "deceasedAge",
                "deceasedBoolean",
                "deceasedDate",
                "deceasedRange",
                "deceasedString",
            ],
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


class FamilyMemberHistoryCondition(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Condition that the related person had.
    The significant Conditions (or condition) that the family member had. This
    is a repeating section to allow a system to represent more than one
    condition per resource, though there is nothing stopping multiple resources
    - one per condition.
    """

    resource_type = Field("FamilyMemberHistoryCondition", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Condition suffered by relation",
    )

    contributedToDeath: bool = Field(
        None,
        alias="contributedToDeath",
        title="Type `bool`",
        description="Whether the condition contributed to the cause of death",
    )
    contributedToDeath__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_contributedToDeath",
        title="Extension field for ``contributedToDeath``.",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Extra information about condition",
    )

    onsetAge: fhirtypes.AgeType = Field(
        None,
        alias="onsetAge",
        title="Type `Age` (represented as `dict` in JSON)",
        description="When condition first manifested",
        one_of_many="onset",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    onsetPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="onsetPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When condition first manifested",
        one_of_many="onset",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    onsetRange: fhirtypes.RangeType = Field(
        None,
        alias="onsetRange",
        title="Type `Range` (represented as `dict` in JSON)",
        description="When condition first manifested",
        one_of_many="onset",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    onsetString: fhirtypes.String = Field(
        None,
        alias="onsetString",
        title="Type `String`",
        description="When condition first manifested",
        one_of_many="onset",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    onsetString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_onsetString", title="Extension field for ``onsetString``."
    )

    outcome: fhirtypes.CodeableConceptType = Field(
        None,
        alias="outcome",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="deceased | permanent disability | etc.",
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
            "onset": ["onsetAge", "onsetPeriod", "onsetRange", "onsetString"]
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
