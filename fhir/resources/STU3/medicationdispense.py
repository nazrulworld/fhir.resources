# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationDispense
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class MedicationDispense(domainresource.DomainResource):
    """ Dispensing a medication to a named patient.
    Indicates that a medication product is to be or has been dispensed for a
    named person/patient.  This includes a description of the medication
    product (supply) provided and the instructions for administering the
    medication.  The medication dispense is the result of a pharmacy system
    responding to a medication order.
    """

    resource_type = Field("MedicationDispense", const=True)

    authorizingPrescription: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="authorizingPrescription",
        title="List of `Reference` items referencing `MedicationRequest` (represented as `dict` in JSON)",
        description="Medication order that authorizes the dispense",
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of medication dispense",
    )

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title="Type `Reference` referencing `Encounter, EpisodeOfCare` (represented as `dict` in JSON)",
        description="Encounter / Episode associated with event",
    )

    daysSupply: fhirtypes.QuantityType = Field(
        None,
        alias="daysSupply",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Amount of medication expressed as a timing amount",
    )

    destination: fhirtypes.ReferenceType = Field(
        None,
        alias="destination",
        title="Type `Reference` referencing `Location` (represented as `dict` in JSON)",
        description="Where the medication was sent",
    )

    detectedIssue: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="detectedIssue",
        title="List of `Reference` items referencing `DetectedIssue` (represented as `dict` in JSON)",
        description="Clinical issue with action",
    )

    dosageInstruction: ListType[fhirtypes.DosageType] = Field(
        None,
        alias="dosageInstruction",
        title="List of `Dosage` items (represented as `dict` in JSON)",
        description="How the medication is to be used by the patient or administered by the caregiver",
    )

    eventHistory: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="eventHistory",
        title="List of `Reference` items referencing `Provenance` (represented as `dict` in JSON)",
        description="A list of releveant lifecycle events",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="External identifier",
    )

    medicationCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="medicationCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="What medication was supplied",
        one_of_many="medication",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    medicationReference: fhirtypes.ReferenceType = Field(
        None,
        alias="medicationReference",
        title="Type `Reference` referencing `Medication` (represented as `dict` in JSON)",
        description="What medication was supplied",
        one_of_many="medication",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    notDone: bool = Field(
        None,
        alias="notDone",
        title="Type `bool`",
        description="Whether the dispense was or was not performed",
    )

    notDoneReasonCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="notDoneReasonCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Why a dispense was not performed",
        one_of_many="notDoneReason",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    notDoneReasonReference: fhirtypes.ReferenceType = Field(
        None,
        alias="notDoneReasonReference",
        title="Type `Reference` referencing `DetectedIssue` (represented as `dict` in JSON)",
        description="Why a dispense was not performed",
        one_of_many="notDoneReason",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Information about the dispense",
    )

    partOf: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title="List of `Reference` items referencing `Procedure` (represented as `dict` in JSON)",
        description="Event that dispense is part of",
    )

    performer: ListType[fhirtypes.MedicationDispensePerformerType] = Field(
        None,
        alias="performer",
        title="List of `MedicationDispensePerformer` items (represented as `dict` in JSON)",
        description="Who performed event",
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Amount dispensed",
    )

    receiver: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="receiver",
        title="List of `Reference` items referencing `Patient, Practitioner` (represented as `dict` in JSON)",
        description="Who collected the medication",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="preparation | in-progress | on-hold | completed | entered-in-error | stopped",
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Type `Reference` referencing `Patient, Group` (represented as `dict` in JSON)",
        description="Who the dispense is for",
    )

    substitution: fhirtypes.MedicationDispenseSubstitutionType = Field(
        None,
        alias="substitution",
        title="Type `MedicationDispenseSubstitution` (represented as `dict` in JSON)",
        description="Whether a substitution was performed on the dispense",
    )

    supportingInformation: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingInformation",
        title="List of `Reference` items referencing `Resource` (represented as `dict` in JSON)",
        description="Information that supports the dispensing of the medication",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Trial fill, partial fill, emergency fill, etc.",
    )

    whenHandedOver: fhirtypes.DateTime = Field(
        None,
        alias="whenHandedOver",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When product was given out",
    )

    whenPrepared: fhirtypes.DateTime = Field(
        None,
        alias="whenPrepared",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When product was packaged and reviewed",
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
            "medication": ["medicationCodeableConcept", "medicationReference",],
            "notDoneReason": [
                "notDoneReasonCodeableConcept",
                "notDoneReasonReference",
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


class MedicationDispensePerformer(backboneelement.BackboneElement):
    """ Who performed event.
    Indicates who or what performed the event.  It should be assumed that the
    performer is the dispenser of the medication.
    """

    resource_type = Field("MedicationDispensePerformer", const=True)

    actor: fhirtypes.ReferenceType = Field(
        ...,
        alias="actor",
        title="Type `Reference` referencing `Practitioner, Organization, Patient, Device, RelatedPerson` (represented as `dict` in JSON)",
        description="Individual who was performing",
    )

    onBehalfOf: fhirtypes.ReferenceType = Field(
        None,
        alias="onBehalfOf",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Organization organization was acting for",
    )


class MedicationDispenseSubstitution(backboneelement.BackboneElement):
    """ Whether a substitution was performed on the dispense.
    Indicates whether or not substitution was made as part of the dispense.  In
    some cases substitution will be expected but does not happen, in other
    cases substitution is not expected but does happen.  This block explains
    what substitution did or did not happen and why.  If nothing is specified,
    substitution was not done.
    """

    resource_type = Field("MedicationDispenseSubstitution", const=True)

    reason: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reason",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Why was substitution made",
    )

    responsibleParty: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="responsibleParty",
        title="List of `Reference` items referencing `Practitioner` (represented as `dict` in JSON)",
        description="Who is responsible for the substitution",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Code signifying whether a different drug was dispensed from what was prescribed",
    )

    wasSubstituted: bool = Field(
        ...,
        alias="wasSubstituted",
        title="Type `bool`",
        description="Whether a substitution was or was not performed on the dispense",
    )
