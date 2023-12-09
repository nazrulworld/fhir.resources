# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/FamilyMemberHistory
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class FamilyMemberHistory(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about patient's relatives, relevant for patient.
    Significant health events and conditions for a person related to the
    patient relevant in the context of care for the patient.
    """

    resource_type = Field("FamilyMemberHistory", const=True)

    ageAge: fhirtypes.AgeType = Field(
        None,
        alias="ageAge",
        title="(approximate) age",
        description=(
            "The age of the relative at the time the family member history is "
            "recorded."
        ),
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e age[x]
        one_of_many="age",
        one_of_many_required=False,
    )
    ageString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_ageString", title="Extension field for ``ageString``."
    )

    bornDate: fhirtypes.Date = Field(
        None,
        alias="bornDate",
        title="(approximate) date of birth",
        description="The actual or approximate date of birth of the relative.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e born[x]
        one_of_many="born",
        one_of_many_required=False,
    )
    bornDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_bornDate", title="Extension field for ``bornDate``."
    )

    bornPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="bornPeriod",
        title="(approximate) date of birth",
        description="The actual or approximate date of birth of the relative.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e born[x]
        one_of_many="born",
        one_of_many_required=False,
    )

    bornString: fhirtypes.String = Field(
        None,
        alias="bornString",
        title="(approximate) date of birth",
        description="The actual or approximate date of birth of the relative.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e born[x]
        one_of_many="born",
        one_of_many_required=False,
    )
    bornString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_bornString", title="Extension field for ``bornString``."
    )

    condition: typing.List[fhirtypes.FamilyMemberHistoryConditionType] = Field(
        None,
        alias="condition",
        title="Condition that the related person had",
        description=(
            "The significant Conditions (or condition) that the family member had. "
            "This is a repeating section to allow a system to represent more than "
            "one condition per resource, though there is nothing stopping multiple "
            "resources - one per condition."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="When history was captured/updated",
        description="The date (and possibly time) when the family member history was taken.",
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    deceasedAge: fhirtypes.AgeType = Field(
        None,
        alias="deceasedAge",
        title="Dead? How old/when?",
        description=(
            "Deceased flag or the actual or approximate age of the relative at the "
            "time of death for the family member history record."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e deceased[x]
        one_of_many="deceased",
        one_of_many_required=False,
    )

    deceasedBoolean: bool = Field(
        None,
        alias="deceasedBoolean",
        title="Dead? How old/when?",
        description=(
            "Deceased flag or the actual or approximate age of the relative at the "
            "time of death for the family member history record."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e deceased[x]
        one_of_many="deceased",
        one_of_many_required=False,
    )
    deceasedBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_deceasedBoolean", title="Extension field for ``deceasedBoolean``."
    )

    deceasedDate: fhirtypes.Date = Field(
        None,
        alias="deceasedDate",
        title="Dead? How old/when?",
        description=(
            "Deceased flag or the actual or approximate age of the relative at the "
            "time of death for the family member history record."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e deceased[x]
        one_of_many="deceased",
        one_of_many_required=False,
    )
    deceasedDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_deceasedDate", title="Extension field for ``deceasedDate``."
    )

    deceasedRange: fhirtypes.RangeType = Field(
        None,
        alias="deceasedRange",
        title="Dead? How old/when?",
        description=(
            "Deceased flag or the actual or approximate age of the relative at the "
            "time of death for the family member history record."
        ),
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e deceased[x]
        one_of_many="deceased",
        one_of_many_required=False,
    )
    deceasedString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_deceasedString", title="Extension field for ``deceasedString``."
    )

    definition: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="definition",
        title="Instantiates protocol or definition",
        description=(
            "A protocol or questionnaire that was adhered to in whole or in part by"
            " this event."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["PlanDefinition", "Questionnaire"],
    )

    estimatedAge: bool = Field(
        None,
        alias="estimatedAge",
        title="Age is estimated?",
        description="If true, indicates that the age value specified is an estimated value.",
        # if property is element of this resource.
        element_property=True,
    )
    estimatedAge__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_estimatedAge", title="Extension field for ``estimatedAge``."
    )

    gender: fhirtypes.Code = Field(
        None,
        alias="gender",
        title="male | female | other | unknown",
        description=(
            "Administrative Gender - the gender that the relative is considered to "
            "have for administration and record keeping purposes."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["male", "female", "other", "unknown"],
    )
    gender__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_gender", title="Extension field for ``gender``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
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
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="The family member described",
        description=(
            'This will either be a name or a description; e.g. "Aunt Susan", "my '
            'cousin with the red hair".'
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    notDone: bool = Field(
        None,
        alias="notDone",
        title="The taking of a family member's history did not occur",
        description=(
            "If true, indicates the taking of an individual family member's history"
            " did not occur. The notDone element should not be used to document "
            "negated conditions, such as a family member that did not have a "
            "condition."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    notDone__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_notDone", title="Extension field for ``notDone``."
    )

    notDoneReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="notDoneReason",
        title="subject-unknown | withheld | unable-to-obtain | deferred",
        description="Describes why the family member's history is absent.",
        # if property is element of this resource.
        element_property=True,
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="General note about related person",
        description=(
            "This property allows a non condition-specific note to the made about "
            "the related person. Ideally, the note would be in the condition "
            "property, but this is not always possible."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Patient history is about",
        description="The person who this history concerns.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    reasonCode: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="Why was family member history performed?",
        description=(
            "Describes why the family member history occurred in coded or textual "
            "form."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    reasonReference: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title="Why was family member history performed?",
        description=(
            "Indicates a Condition, Observation, AllergyIntolerance, or "
            "QuestionnaireResponse that justifies this family member history event."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Condition",
            "Observation",
            "AllergyIntolerance",
            "QuestionnaireResponse",
        ],
    )

    relationship: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="relationship",
        title="Relationship to the subject",
        description=(
            "The type of relationship this person has to the patient (father, "
            "mother, brother etc.)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="partial | completed | entered-in-error | health-unknown",
        description=(
            "A code specifying the status of the record of the family history of a "
            "specific family member."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["partial", "completed", "entered-in-error", "health-unknown"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2155(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2155(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
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
        title="Condition suffered by relation",
        description=(
            "The actual condition specified. Could be a coded condition (like MI or"
            " Diabetes) or a less specific string like 'cancer' depending on how "
            "much is known about the condition and the capabilities of the creating"
            " system."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Extra information about condition",
        description=(
            "An area where general notes can be placed about this specific "
            "condition."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    onsetAge: fhirtypes.AgeType = Field(
        None,
        alias="onsetAge",
        title="When condition first manifested",
        description=(
            "Either the age of onset, range of approximate age or descriptive "
            "string can be recorded.  For conditions with multiple occurrences, "
            "this describes the first known occurrence."
        ),
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e onset[x]
        one_of_many="onset",
        one_of_many_required=False,
    )
    onsetString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_onsetString", title="Extension field for ``onsetString``."
    )

    outcome: fhirtypes.CodeableConceptType = Field(
        None,
        alias="outcome",
        title="deceased | permanent disability | etc.",
        description=(
            "Indicates what happened as a result of this condition.  If the "
            "condition resulted in death, deceased date is captured on the "
            "relation."
        ),
        # if property is element of this resource.
        element_property=True,
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3079(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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
