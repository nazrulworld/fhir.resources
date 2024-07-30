# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/FamilyMemberHistory
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class FamilyMemberHistory(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about patient's relatives, relevant for patient.
    Significant health conditions for a person related to the patient relevant
    in the context of care for the patient.
    """

    __resource_type__ = "FamilyMemberHistory"

    ageAge: fhirtypes.AgeType = Field(  # type: ignore
        None,
        alias="ageAge",
        title="(approximate) age",
        description=(
            "The age of the relative at the time the family member history is "
            "recorded."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e age[x]
            "one_of_many": "age",
            "one_of_many_required": False,
        },
    )

    ageRange: fhirtypes.RangeType = Field(  # type: ignore
        None,
        alias="ageRange",
        title="(approximate) age",
        description=(
            "The age of the relative at the time the family member history is "
            "recorded."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e age[x]
            "one_of_many": "age",
            "one_of_many_required": False,
        },
    )

    ageString: fhirtypes.StringType = Field(  # type: ignore
        None,
        alias="ageString",
        title="(approximate) age",
        description=(
            "The age of the relative at the time the family member history is "
            "recorded."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e age[x]
            "one_of_many": "age",
            "one_of_many_required": False,
        },
    )
    ageString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_ageString", title="Extension field for ``ageString``."
    )

    bornDate: fhirtypes.DateType = Field(  # type: ignore
        None,
        alias="bornDate",
        title="(approximate) date of birth",
        description="The actual or approximate date of birth of the relative.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e born[x]
            "one_of_many": "born",
            "one_of_many_required": False,
        },
    )
    bornDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_bornDate", title="Extension field for ``bornDate``."
    )

    bornPeriod: fhirtypes.PeriodType = Field(  # type: ignore
        None,
        alias="bornPeriod",
        title="(approximate) date of birth",
        description="The actual or approximate date of birth of the relative.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e born[x]
            "one_of_many": "born",
            "one_of_many_required": False,
        },
    )

    bornString: fhirtypes.StringType = Field(  # type: ignore
        None,
        alias="bornString",
        title="(approximate) date of birth",
        description="The actual or approximate date of birth of the relative.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e born[x]
            "one_of_many": "born",
            "one_of_many_required": False,
        },
    )
    bornString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_bornString", title="Extension field for ``bornString``."
    )

    condition: typing.List[fhirtypes.FamilyMemberHistoryConditionType] = Field(  # type: ignore
        None,
        alias="condition",
        title="Condition that the related person had",
        description=(
            "The significant Conditions (or condition) that the family member had. "
            "This is a repeating section to allow a system to represent more than "
            "one condition per resource, though there is nothing stopping multiple "
            "resources - one per condition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    dataAbsentReason: fhirtypes.CodeableConceptType = Field(  # type: ignore
        None,
        alias="dataAbsentReason",
        title="subject-unknown | withheld | unable-to-obtain | deferred",
        description="Describes why the family member's history is not available.",
        json_schema_extra={
            "element_property": True,
        },
    )

    date: fhirtypes.DateTimeType = Field(  # type: ignore
        None,
        alias="date",
        title="When history was recorded or last updated",
        description=(
            "The date (and possibly time) when the family member history was "
            "recorded or last updated."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    deceasedAge: fhirtypes.AgeType = Field(  # type: ignore
        None,
        alias="deceasedAge",
        title="Dead? How old/when?",
        description=(
            "Deceased flag or the actual or approximate age of the relative at the "
            "time of death for the family member history record."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e deceased[x]
            "one_of_many": "deceased",
            "one_of_many_required": False,
        },
    )

    deceasedBoolean: bool = Field(  # type: ignore
        None,
        alias="deceasedBoolean",
        title="Dead? How old/when?",
        description=(
            "Deceased flag or the actual or approximate age of the relative at the "
            "time of death for the family member history record."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e deceased[x]
            "one_of_many": "deceased",
            "one_of_many_required": False,
        },
    )
    deceasedBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_deceasedBoolean", title="Extension field for ``deceasedBoolean``."
    )

    deceasedDate: fhirtypes.DateType = Field(  # type: ignore
        None,
        alias="deceasedDate",
        title="Dead? How old/when?",
        description=(
            "Deceased flag or the actual or approximate age of the relative at the "
            "time of death for the family member history record."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e deceased[x]
            "one_of_many": "deceased",
            "one_of_many_required": False,
        },
    )
    deceasedDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_deceasedDate", title="Extension field for ``deceasedDate``."
    )

    deceasedRange: fhirtypes.RangeType = Field(  # type: ignore
        None,
        alias="deceasedRange",
        title="Dead? How old/when?",
        description=(
            "Deceased flag or the actual or approximate age of the relative at the "
            "time of death for the family member history record."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e deceased[x]
            "one_of_many": "deceased",
            "one_of_many_required": False,
        },
    )

    deceasedString: fhirtypes.StringType = Field(  # type: ignore
        None,
        alias="deceasedString",
        title="Dead? How old/when?",
        description=(
            "Deceased flag or the actual or approximate age of the relative at the "
            "time of death for the family member history record."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e deceased[x]
            "one_of_many": "deceased",
            "one_of_many_required": False,
        },
    )
    deceasedString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_deceasedString", title="Extension field for ``deceasedString``."
    )

    estimatedAge: bool = Field(  # type: ignore
        None,
        alias="estimatedAge",
        title="Age is estimated?",
        description="If true, indicates that the age value specified is an estimated value.",
        json_schema_extra={
            "element_property": True,
        },
    )
    estimatedAge__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_estimatedAge", title="Extension field for ``estimatedAge``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(  # type: ignore
        None,
        alias="identifier",
        title="External Id(s) for this record",
        description=(
            "Business identifiers assigned to this family member history by the "
            "performer or other systems which remain constant as the resource is "
            "updated and propagates from server to server."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    instantiatesCanonical: typing.List[typing.Optional[fhirtypes.CanonicalType]] = Field(  # type: ignore
        None,
        alias="instantiatesCanonical",
        title="Instantiates FHIR protocol or definition",
        description=(
            "The URL pointing to a FHIR-defined protocol, guideline, orderset or "
            "other definition that is adhered to in whole or in part by this "
            "FamilyMemberHistory."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "PlanDefinition",
                "Questionnaire",
                "ActivityDefinition",
                "Measure",
                "OperationDefinition",
            ],
        },
    )
    instantiatesCanonical__ext: typing.List[typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(  # type: ignore
        None,
        alias="_instantiatesCanonical",
        title="Extension field for ``instantiatesCanonical``.",
    )

    instantiatesUri: typing.List[typing.Optional[fhirtypes.UriType]] = Field(  # type: ignore
        None,
        alias="instantiatesUri",
        title="Instantiates external protocol or definition",
        description=(
            "The URL pointing to an externally maintained protocol, guideline, "
            "orderset or other definition that is adhered to in whole or in part by"
            " this FamilyMemberHistory."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    instantiatesUri__ext: typing.List[typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(  # type: ignore
        None, alias="_instantiatesUri", title="Extension field for ``instantiatesUri``."
    )

    name: fhirtypes.StringType = Field(  # type: ignore
        None,
        alias="name",
        title="The family member described",
        description=(
            'This will either be a name or a description; e.g. "Aunt Susan", "my '
            'cousin with the red hair".'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(  # type: ignore
        None,
        alias="note",
        title="General note about related person",
        description=(
            "This property allows a non condition-specific note to the made about "
            "the related person. Ideally, the note would be in the condition "
            "property, but this is not always possible."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    patient: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="patient",
        title="Patient history is about",
        description="The person who this history concerns.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient"],
        },
    )

    reasonCode: typing.List[fhirtypes.CodeableConceptType] = Field(  # type: ignore
        None,
        alias="reasonCode",
        title="Why was family member history performed?",
        description=(
            "Describes why the family member history occurred in coded or textual "
            "form."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reasonReference: typing.List[fhirtypes.ReferenceType] = Field(  # type: ignore
        None,
        alias="reasonReference",
        title="Why was family member history performed?",
        description=(
            "Indicates a Condition, Observation, AllergyIntolerance, or "
            "QuestionnaireResponse that justifies this family member history event."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Condition",
                "Observation",
                "AllergyIntolerance",
                "QuestionnaireResponse",
                "DiagnosticReport",
                "DocumentReference",
            ],
        },
    )

    relationship: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="relationship",
        title="Relationship to the subject",
        description=(
            "The type of relationship this person has to the patient (father, "
            "mother, brother etc.)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    sex: fhirtypes.CodeableConceptType = Field(  # type: ignore
        None,
        alias="sex",
        title="male | female | other | unknown",
        description="The birth sex of the family member.",
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType = Field(  # type: ignore
        None,
        alias="status",
        title="partial | completed | entered-in-error | health-unknown",
        description=(
            "A code specifying the status of the record of the family history of a "
            "specific family member."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "partial",
                "completed",
                "entered-in-error",
                "health-unknown",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``FamilyMemberHistory`` according specification,
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
            "instantiatesCanonical",
            "instantiatesUri",
            "status",
            "dataAbsentReason",
            "patient",
            "date",
            "name",
            "relationship",
            "sex",
            "bornPeriod",
            "bornDate",
            "bornString",
            "ageAge",
            "ageRange",
            "ageString",
            "estimatedAge",
            "deceasedBoolean",
            "deceasedAge",
            "deceasedRange",
            "deceasedDate",
            "deceasedString",
            "reasonCode",
            "reasonReference",
            "note",
            "condition",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        return required_fields

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
        return one_of_many_fields


class FamilyMemberHistoryCondition(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Condition that the related person had.
    The significant Conditions (or condition) that the family member had. This
    is a repeating section to allow a system to represent more than one
    condition per resource, though there is nothing stopping multiple resources
    - one per condition.
    """

    __resource_type__ = "FamilyMemberHistoryCondition"

    code: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="code",
        title="Condition suffered by relation",
        description=(
            "The actual condition specified. Could be a coded condition (like MI or"
            " Diabetes) or a less specific string like 'cancer' depending on how "
            "much is known about the condition and the capabilities of the creating"
            " system."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    contributedToDeath: bool = Field(  # type: ignore
        None,
        alias="contributedToDeath",
        title="Whether the condition contributed to the cause of death",
        description=(
            "This condition contributed to the cause of death of the related "
            "person. If contributedToDeath is not populated, then it is unknown."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    contributedToDeath__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None,
        alias="_contributedToDeath",
        title="Extension field for ``contributedToDeath``.",
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(  # type: ignore
        None,
        alias="note",
        title="Extra information about condition",
        description=(
            "An area where general notes can be placed about this specific "
            "condition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    onsetAge: fhirtypes.AgeType = Field(  # type: ignore
        None,
        alias="onsetAge",
        title="When condition first manifested",
        description=(
            "Either the age of onset, range of approximate age or descriptive "
            "string can be recorded.  For conditions with multiple occurrences, "
            "this describes the first known occurrence."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e onset[x]
            "one_of_many": "onset",
            "one_of_many_required": False,
        },
    )

    onsetPeriod: fhirtypes.PeriodType = Field(  # type: ignore
        None,
        alias="onsetPeriod",
        title="When condition first manifested",
        description=(
            "Either the age of onset, range of approximate age or descriptive "
            "string can be recorded.  For conditions with multiple occurrences, "
            "this describes the first known occurrence."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e onset[x]
            "one_of_many": "onset",
            "one_of_many_required": False,
        },
    )

    onsetRange: fhirtypes.RangeType = Field(  # type: ignore
        None,
        alias="onsetRange",
        title="When condition first manifested",
        description=(
            "Either the age of onset, range of approximate age or descriptive "
            "string can be recorded.  For conditions with multiple occurrences, "
            "this describes the first known occurrence."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e onset[x]
            "one_of_many": "onset",
            "one_of_many_required": False,
        },
    )

    onsetString: fhirtypes.StringType = Field(  # type: ignore
        None,
        alias="onsetString",
        title="When condition first manifested",
        description=(
            "Either the age of onset, range of approximate age or descriptive "
            "string can be recorded.  For conditions with multiple occurrences, "
            "this describes the first known occurrence."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e onset[x]
            "one_of_many": "onset",
            "one_of_many_required": False,
        },
    )
    onsetString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_onsetString", title="Extension field for ``onsetString``."
    )

    outcome: fhirtypes.CodeableConceptType = Field(  # type: ignore
        None,
        alias="outcome",
        title="deceased | permanent disability | etc.",
        description=(
            "Indicates what happened following the condition.  If the condition "
            "resulted in death, deceased date is captured on the relation."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``FamilyMemberHistoryCondition`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "outcome",
            "contributedToDeath",
            "onsetAge",
            "onsetRange",
            "onsetPeriod",
            "onsetString",
            "note",
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
            "onset": ["onsetAge", "onsetPeriod", "onsetRange", "onsetString"]
        }
        return one_of_many_fields
