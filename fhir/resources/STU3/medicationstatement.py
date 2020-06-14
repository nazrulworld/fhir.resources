# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationStatement
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import domainresource, fhirtypes


class MedicationStatement(domainresource.DomainResource):
    """ Record of medication being taken by a patient.
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

    basedOn: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="List of `Reference` items referencing `MedicationRequest, CarePlan, ProcedureRequest, ReferralRequest` (represented as `dict` in JSON)",
        description="Fulfils plan, proposal or order",
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of medication usage",
    )

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title="Type `Reference` referencing `Encounter, EpisodeOfCare` (represented as `dict` in JSON)",
        description="Encounter / Episode associated with MedicationStatement",
    )

    dateAsserted: fhirtypes.DateTime = Field(
        None,
        alias="dateAsserted",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When the statement was asserted?",
    )

    derivedFrom: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="derivedFrom",
        title="List of `Reference` items referencing `Resource` (represented as `dict` in JSON)",
        description="Additional supporting information",
    )

    dosage: ListType[fhirtypes.DosageType] = Field(
        None,
        alias="dosage",
        title="List of `Dosage` items (represented as `dict` in JSON)",
        description="Details of how medication is/was taken or should be taken",
    )

    effectiveDateTime: fhirtypes.DateTime = Field(
        None,
        alias="effectiveDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="The date/time or interval when the medication was taken",
        one_of_many="effective",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="The date/time or interval when the medication was taken",
        one_of_many="effective",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="External identifier",
    )

    informationSource: fhirtypes.ReferenceType = Field(
        None,
        alias="informationSource",
        title="Type `Reference` referencing `Patient, Practitioner, RelatedPerson, Organization` (represented as `dict` in JSON)",
        description="Person or organization that provided the information about the taking of this medication",
    )

    medicationCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="medicationCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="What medication was taken",
        one_of_many="medication",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    medicationReference: fhirtypes.ReferenceType = Field(
        None,
        alias="medicationReference",
        title="Type `Reference` referencing `Medication` (represented as `dict` in JSON)",
        description="What medication was taken",
        one_of_many="medication",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Further information about the statement",
    )

    partOf: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title="List of `Reference` items referencing `MedicationAdministration, MedicationDispense, MedicationStatement, Procedure, Observation` (represented as `dict` in JSON)",
        description="Part of referenced event",
    )

    reasonCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Reason for why the medication is being/was taken",
    )

    reasonNotTaken: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonNotTaken",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="True if asserting medication was not given",
    )

    reasonReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title="List of `Reference` items referencing `Condition, Observation` (represented as `dict` in JSON)",
        description="Condition or observation that supports why the medication is being/was taken",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="active | completed | entered-in-error | intended | stopped | on-hold",
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Type `Reference` referencing `Patient, Group` (represented as `dict` in JSON)",
        description="Who is/was taking  the medication",
    )

    taken: fhirtypes.Code = Field(
        ...,
        alias="taken",
        title="Type `Code` (represented as `dict` in JSON)",
        description="y | n | unk | na",
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
            "effective": ["effectiveDateTime", "effectivePeriod",],
            "medication": ["medicationCodeableConcept", "medicationReference",],
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
