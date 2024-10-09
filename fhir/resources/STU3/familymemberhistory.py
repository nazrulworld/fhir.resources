from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/FamilyMemberHistory
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class FamilyMemberHistory(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about patient's relatives, relevant for patient.
    Significant health events and conditions for a person related to the
    patient relevant in the context of care for the patient.
    """

    __resource_type__ = "FamilyMemberHistory"

    ageAge: fhirtypes.AgeType | None = Field(  # type: ignore
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

    ageRange: fhirtypes.RangeType | None = Field(  # type: ignore
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

    ageString: fhirtypes.StringType | None = Field(  # type: ignore
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
    ageString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_ageString", title="Extension field for ``ageString``."
    )

    bornDate: fhirtypes.DateType | None = Field(  # type: ignore
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
    bornDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_bornDate", title="Extension field for ``bornDate``."
    )

    bornPeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
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

    bornString: fhirtypes.StringType | None = Field(  # type: ignore
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
    bornString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_bornString", title="Extension field for ``bornString``."
    )

    condition: typing.List[fhirtypes.FamilyMemberHistoryConditionType] | None = Field(  # type: ignore
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

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="date",
        title="When history was captured/updated",
        description="The date (and possibly time) when the family member history was taken.",
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    deceasedAge: fhirtypes.AgeType | None = Field(  # type: ignore
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

    deceasedBoolean: bool | None = Field(  # type: ignore
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
    deceasedBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_deceasedBoolean", title="Extension field for ``deceasedBoolean``."
    )

    deceasedDate: fhirtypes.DateType | None = Field(  # type: ignore
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
    deceasedDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_deceasedDate", title="Extension field for ``deceasedDate``."
    )

    deceasedRange: fhirtypes.RangeType | None = Field(  # type: ignore
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

    deceasedString: fhirtypes.StringType | None = Field(  # type: ignore
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
    deceasedString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_deceasedString", title="Extension field for ``deceasedString``."
    )

    definition: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="definition",
        title="Instantiates protocol or definition",
        description=(
            "A protocol or questionnaire that was adhered to in whole or in part by"
            " this event."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["PlanDefinition", "Questionnaire"],
        },
    )

    estimatedAge: bool | None = Field(  # type: ignore
        None,
        alias="estimatedAge",
        title="Age is estimated?",
        description="If true, indicates that the age value specified is an estimated value.",
        json_schema_extra={
            "element_property": True,
        },
    )
    estimatedAge__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_estimatedAge", title="Extension field for ``estimatedAge``."
    )

    gender: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="gender",
        title="male | female | other | unknown",
        description=(
            "Administrative Gender - the gender that the relative is considered to "
            "have for administration and record keeping purposes."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["male", "female", "other", "unknown"],
        },
    )
    gender__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_gender", title="Extension field for ``gender``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="External Id(s) for this record",
        description=(
            "This records identifiers associated with this family member history "
            "record that are defined by business processes and/ or used to refer to"
            " it when a direct URL reference to the resource itself is not "
            "appropriate (e.g. in CDA documents, or in written / printed "
            "documentation)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
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
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    notDone: bool | None = Field(  # type: ignore
        None,
        alias="notDone",
        title="The taking of a family member's history did not occur",
        description=(
            "If true, indicates the taking of an individual family member's history"
            " did not occur. The notDone element should not be used to document "
            "negated conditions, such as a family member that did not have a "
            "condition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    notDone__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_notDone", title="Extension field for ``notDone``."
    )

    notDoneReason: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="notDoneReason",
        title="subject-unknown | withheld | unable-to-obtain | deferred",
        description="Describes why the family member's history is absent.",
        json_schema_extra={
            "element_property": True,
        },
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
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

    reasonCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
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

    reasonReference: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
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

    status: fhirtypes.CodeType | None = Field(  # type: ignore
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
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
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
            "definition",
            "status",
            "notDone",
            "notDoneReason",
            "patient",
            "date",
            "name",
            "relationship",
            "gender",
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

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
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

    onsetAge: fhirtypes.AgeType | None = Field(  # type: ignore
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

    onsetPeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
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

    onsetRange: fhirtypes.RangeType | None = Field(  # type: ignore
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

    onsetString: fhirtypes.StringType | None = Field(  # type: ignore
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
    onsetString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_onsetString", title="Extension field for ``onsetString``."
    )

    outcome: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="outcome",
        title="deceased | permanent disability | etc.",
        description=(
            "Indicates what happened as a result of this condition.  If the "
            "condition resulted in death, deceased date is captured on the "
            "relation."
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
