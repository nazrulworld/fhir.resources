# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationStatement
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import domainresource, fhirtypes


class MedicationStatement(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Record of medication being taken by a patient.
    A record of a medication that is being consumed by a patient.   A
    MedicationStatement may indicate that the patient may be taking the
    medication now, or has taken the medication in the past or will be taking
    the medication in the future.  The source of this information can be the
    patient, significant other (such as a family member or spouse), or a
    clinician.  A common scenario where this information is captured is during
    the history taking process during a patient visit or stay.   The medication
    information may come from sources such as the patient's memory, from a
    prescription bottle,  or from a list of medications the patient, clinician
    or other party maintains

    The primary difference between a medication statement and a medication
    administration is that the medication administration has complete
    administration information and is based on actual administration
    information from the person who administered the medication.  A medication
    statement is often, if not always, less specific.  There is no required
    date/time when the medication was administered, in fact we only know that a
    source has reported the patient is taking this medication, where details
    such as time, quantity, or rate or even medication product may be
    incomplete or missing or less precise.  As stated earlier, the medication
    statement information may come from the patient's memory, from a
    prescription bottle or from a list of medications the patient, clinician or
    other party maintains.  Medication administration is more formal and is not
    missing detailed information.
    """

    resource_type = Field("MedicationStatement", const=True)

    basedOn: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="Fulfils plan, proposal or order",
        description=(
            "A plan, proposal or order that is fulfilled in whole or in part by "
            "this event."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "MedicationRequest",
            "CarePlan",
            "ProcedureRequest",
            "ReferralRequest",
        ],
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type of medication usage",
        description=(
            "Indicates where type of medication statement and where the medication "
            "is expected to be consumed or administered."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title="Encounter / Episode associated with MedicationStatement",
        description=(
            "The encounter or episode of care that establishes the context for this"
            " MedicationStatement."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter", "EpisodeOfCare"],
    )

    dateAsserted: fhirtypes.DateTime = Field(
        None,
        alias="dateAsserted",
        title="When the statement was asserted?",
        description=(
            "The date when the medication statement was asserted by the information"
            " source."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    dateAsserted__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_dateAsserted", title="Extension field for ``dateAsserted``."
    )

    derivedFrom: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="derivedFrom",
        title="Additional supporting information",
        description=(
            "Allows linking the MedicationStatement to the underlying "
            "MedicationRequest, or to other information that supports or is used to"
            " derive the MedicationStatement."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    dosage: typing.List[fhirtypes.DosageType] = Field(
        None,
        alias="dosage",
        title="Details of how medication is/was taken or should be taken",
        description="Indicates how the medication is/was or should be taken by the patient.",
        # if property is element of this resource.
        element_property=True,
    )

    effectiveDateTime: fhirtypes.DateTime = Field(
        None,
        alias="effectiveDateTime",
        title="The date/time or interval when the medication was taken",
        description=(
            "The interval of time during which it is being asserted that the "
            "patient was taking the medication (or was not taking, when the "
            "wasNotGiven element is true)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e effective[x]
        one_of_many="effective",
        one_of_many_required=False,
    )
    effectiveDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_effectiveDateTime",
        title="Extension field for ``effectiveDateTime``.",
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="The date/time or interval when the medication was taken",
        description=(
            "The interval of time during which it is being asserted that the "
            "patient was taking the medication (or was not taking, when the "
            "wasNotGiven element is true)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e effective[x]
        one_of_many="effective",
        one_of_many_required=False,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="External identifier",
        description=(
            "External identifier - FHIR will generate its own internal identifiers "
            "(probably URLs) which do not need to be explicitly managed by the "
            "resource.  The identifier here is one that would be used by another "
            "non-FHIR system - for example an automated medication pump would "
            "provide a record each time it operated; an administration while the "
            "patient was off the ward might be made with a different system and "
            "entered after the event.  Particularly important if these records have"
            " to be updated."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    informationSource: fhirtypes.ReferenceType = Field(
        None,
        alias="informationSource",
        title=(
            "Person or organization that provided the information about the taking "
            "of this medication"
        ),
        description=(
            "The person or organization that provided the information about the "
            "taking of this medication. Note: Use derivedFrom when a "
            "MedicationStatement is derived from other resources, e.g Claim or "
            "MedicationRequest."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "Practitioner",
            "RelatedPerson",
            "Organization",
        ],
    )

    medicationCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="medicationCodeableConcept",
        title="What medication was taken",
        description=(
            "Identifies the medication being administered. This is either a link to"
            " a resource representing the details of the medication or a simple "
            "attribute carrying a code that identifies the medication from a known "
            "list of medications."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e medication[x]
        one_of_many="medication",
        one_of_many_required=True,
    )

    medicationReference: fhirtypes.ReferenceType = Field(
        None,
        alias="medicationReference",
        title="What medication was taken",
        description=(
            "Identifies the medication being administered. This is either a link to"
            " a resource representing the details of the medication or a simple "
            "attribute carrying a code that identifies the medication from a known "
            "list of medications."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e medication[x]
        one_of_many="medication",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Medication"],
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Further information about the statement",
        description=(
            "Provides extra information about the medication statement that is not "
            "conveyed by the other attributes."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    partOf: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title="Part of referenced event",
        description="A larger event of which this particular event is a component or step.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "MedicationAdministration",
            "MedicationDispense",
            "MedicationStatement",
            "Procedure",
            "Observation",
        ],
    )

    reasonCode: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="Reason for why the medication is being/was taken",
        description="A reason for why the medication is being/was taken.",
        # if property is element of this resource.
        element_property=True,
    )

    reasonNotTaken: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonNotTaken",
        title="True if asserting medication was not given",
        description="A code indicating why the medication was not taken.",
        # if property is element of this resource.
        element_property=True,
    )

    reasonReference: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title=(
            "Condition or observation that supports why the medication is being/was"
            " taken"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Condition", "Observation"],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="active | completed | entered-in-error | intended | stopped | on-hold",
        description=(
            "A code representing the patient or other source's judgment about the "
            "state of the medication used that this statement is about.  Generally "
            "this will be active or completed."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "active",
            "completed",
            "entered-in-error",
            "intended",
            "stopped",
            "on-hold",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Who is/was taking  the medication",
        description="The person, animal or group who is/was taking the medication.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group"],
    )

    taken: fhirtypes.Code = Field(
        None,
        alias="taken",
        title="y | n | unk | na",
        description=(
            "Indicator of the certainty of whether the medication was taken by the "
            "patient."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["y", "n", "unk", "na"],
    )
    taken__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_taken", title="Extension field for ``taken``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationStatement`` according specification,
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
            "basedOn",
            "partOf",
            "context",
            "status",
            "category",
            "medicationCodeableConcept",
            "medicationReference",
            "effectiveDateTime",
            "effectivePeriod",
            "dateAsserted",
            "informationSource",
            "subject",
            "derivedFrom",
            "taken",
            "reasonNotTaken",
            "reasonCode",
            "reasonReference",
            "note",
            "dosage",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2163(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext"), ("taken", "taken__ext")]
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
    def validate_one_of_many_2163(
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
            "effective": ["effectiveDateTime", "effectivePeriod"],
            "medication": ["medicationCodeableConcept", "medicationReference"],
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
