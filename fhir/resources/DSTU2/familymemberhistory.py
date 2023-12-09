# -*- coding: utf-8 -*-
"""
Profile: https://www.hl7.org/fhir/DSTU2/familymemberhistory.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic.v1 import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class FamilyMemberHistory(domainresource.DomainResource):
    """Information about patient's relatives, relevant for patient.

    Significant health conditions for a person related to the patient relevant
    in the context of care for the patient.
    """

    resource_type = Field("FamilyMemberHistory", const=True)

    ageQuantity: fhirtypes.AgeType = Field(
        None,
        alias="ageQuantity",
        title="(approximate) age",
        description=(
            "The age of the relative at the time the family member history is "
            "recorded."
        ),
        # Choice of Data Types. i.e age[x]
        one_of_many="age",
        one_of_many_required=False,
    )

    ageRange: fhirtypes.RangeType = Field(
        None,
        alias="ageRange",
        title="(approximate) age",
        description=(
            "The age of the relative at the time the family member history is "
            "recorded."
        ),
        # Choice of Data Types. i.e age[x]
        one_of_many="age",
        one_of_many_required=False,
    )

    ageString: fhirtypes.String = Field(
        None,
        alias="ageString",
        title="(approximate) age",
        description=(
            "The age of the relative at the time the family member history is "
            "recorded."
        ),
        # Choice of Data Types. i.e age[x]
        one_of_many="age",
        one_of_many_required=False,
    )

    bornDate: fhirtypes.Date = Field(
        None,
        alias="bornDate",
        title="(approximate) date of birth",
        description="The actual or approximate date of birth of the relative.",
        # Choice of Data Types. i.e born[x]
        one_of_many="born",
        one_of_many_required=False,
    )

    bornPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="bornPeriod",
        title="(approximate) date of birth",
        description="The actual or approximate date of birth of the relative.",
        # Choice of Data Types. i.e born[x]
        one_of_many="born",
        one_of_many_required=False,
    )

    bornString: fhirtypes.String = Field(
        None,
        alias="bornString",
        title="(approximate) date of birth",
        description="The actual or approximate date of birth of the relative.",
        # Choice of Data Types. i.e born[x]
        one_of_many="born",
        one_of_many_required=False,
    )

    condition: ListType[fhirtypes.FamilyMemberHistoryConditionType] = Field(
        None,
        alias="condition",
        title="Condition that the related person had",
        description=(
            "The significant Conditions (or condition) that the family member had. "
            "This is a repeating section to allow a system to represent more than "
            "one condition per resource, though there is nothing stopping multiple "
            "resources - one per condition."
        ),
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="When history was recorded or last updated",
        description=(
            "The date (and possibly time) when the family member history was "
            "recorded or last updated."
        ),
    )

    deceasedQuantity: fhirtypes.AgeType = Field(
        None,
        alias="deceasedQuantity",
        title="Dead? How old/when?",
        description=(
            "Deceased flag or the actual or approximate age of the relative at the "
            "time of death for the family member history record."
        ),
        # Choice of Data Types. i.e deceased[x]
        one_of_many="deceased",
        one_of_many_required=False,
    )

    deceasedBoolean: fhirtypes.Boolean = Field(
        None,
        alias="deceasedBoolean",
        title="Dead? How old/when?",
        description=(
            "Deceased flag or the actual or approximate age of the relative at the "
            "time of death for the family member history record."
        ),
        # Choice of Data Types. i.e deceased[x]
        one_of_many="deceased",
        one_of_many_required=False,
    )

    deceasedDate: fhirtypes.Date = Field(
        None,
        alias="deceasedDate",
        title="Dead? How old/when?",
        description=(
            "Deceased flag or the actual or approximate age of the relative at the "
            "time of death for the family member history record."
        ),
        # Choice of Data Types. i.e deceased[x]
        one_of_many="deceased",
        one_of_many_required=False,
    )

    deceasedRange: fhirtypes.RangeType = Field(
        None,
        alias="deceasedRange",
        title="Dead? How old/when?",
        description=(
            "Deceased flag or the actual or approximate age of the relative at the "
            "time of death for the family member history record."
        ),
        # Choice of Data Types. i.e deceased[x]
        one_of_many="deceased",
        one_of_many_required=False,
    )

    deceasedString: fhirtypes.String = Field(
        None,
        alias="deceasedString",
        title="Dead? How old/when?",
        description=(
            "Deceased flag or the actual or approximate age of the relative at the "
            "time of death for the family member history record."
        ),
        # Choice of Data Types. i.e deceased[x]
        one_of_many="deceased",
        one_of_many_required=False,
    )

    gender: fhirtypes.Code = Field(
        None,
        alias="gender",
        title="Type `str`.",
        description="male | female | other | unknown.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["male", "female", "other", "unknown"],
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="External Id(s) for this record",
        description=(
            "Business identifiers assigned to this family member history by the "
            "performer or other systems which remain constant as the resource is "
            "updated and propagates from server to server."
        ),
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="The family member described",
        description=(
            'This will either be a name or a description; e.g. "Aunt Susan", "my '
            'cousin with the red hair".'
        ),
    )

    note: fhirtypes.AnnotationType = Field(
        None,
        alias="note",
        title="General note about related person",
        description=(
            "This property allows a non condition-specific note to the made about "
            "the related person. Ideally, the note would be in the condition "
            "property, but this is not always possible."
        ),
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Patient history is about",
        description="The person who this history concerns.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    relationship: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="relationship",
        title="Relationship to the subject",
        description=(
            "The type of relationship this person has to the patient (father, "
            "mother, brother etc.)."
        ),
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="partial | completed | entered-in-error | health-unknown",
        description=(
            "A code specifying the status of the record of the family history of a "
            "specific family member."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["partial", "completed", "entered-in-error", "health-unknown"],
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
            "age": ["ageQuantity", "ageRange", "ageString"],
            "born": ["bornDate", "bornPeriod", "bornString"],
            "deceased": [
                "deceasedQuantity",
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
    """Condition that the related person had.

    The significant Conditions (or condition) that the family member had. This
    is a repeating section to allow a system to represent more than one
    condition per resource, though there is nothing stopping multiple resources
    - one per condition.
    """

    resource_type = Field("FamilyMemberHistoryCondition", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Condition suffered by relation",
        description=(
            "The actual condition specified. Could be a coded condition (like MI or"
            " Diabetes) or a less specific string like 'cancer' depending on how "
            "much is known about the condition and the capabilities of the creating"
            " system."
        ),
    )

    note: fhirtypes.AnnotationType = Field(
        None,
        alias="note",
        title="Extra information about condition",
        description=(
            "An area where general notes can be placed about this specific "
            "condition."
        ),
    )

    onsetQuantity: fhirtypes.AgeType = Field(
        None,
        alias="onsetQuantity",
        title="When condition first manifested",
        description=(
            "Either the age of onset, range of approximate age or descriptive "
            "string can be recorded.  For conditions with multiple occurrences, "
            "this describes the first known occurrence."
        ),
        # Choice of Data Types. i.e onset[x]
        one_of_many="onset",
        one_of_many_required=False,
    )

    onsetPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="onsetPeriod",
        title="When condition first manifested",
        description=(
            "Either the age of onset, range of approximate age or descriptive "
            "string can be recorded.  For conditions with multiple occurrences, "
            "this describes the first known occurrence."
        ),
        # Choice of Data Types. i.e onset[x]
        one_of_many="onset",
        one_of_many_required=False,
    )

    onsetRange: fhirtypes.RangeType = Field(
        None,
        alias="onsetRange",
        title="When condition first manifested",
        description=(
            "Either the age of onset, range of approximate age or descriptive "
            "string can be recorded.  For conditions with multiple occurrences, "
            "this describes the first known occurrence."
        ),
        # Choice of Data Types. i.e onset[x]
        one_of_many="onset",
        one_of_many_required=False,
    )

    onsetString: fhirtypes.String = Field(
        None,
        alias="onsetString",
        title="When condition first manifested",
        description=(
            "Either the age of onset, range of approximate age or descriptive "
            "string can be recorded.  For conditions with multiple occurrences, "
            "this describes the first known occurrence."
        ),
        # Choice of Data Types. i.e onset[x]
        one_of_many="onset",
        one_of_many_required=False,
    )

    outcome: fhirtypes.CodeableConceptType = Field(
        None,
        alias="outcome",
        title="deceased | permanent disability | etc.",
        description=(
            "Indicates what happened following the condition.  If the condition "
            "resulted in death, deceased date is captured on the relation."
        ),
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
            "onset": ["onsetQuantity", "onsetPeriod", "onsetRange", "onsetString"]
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
