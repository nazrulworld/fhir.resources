# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationRequest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class MedicationRequest(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Ordering of medication for patient or group.
    An order or request for both supply of the medication and the instructions
    for administration of the medication to a patient. The resource is called
    "MedicationRequest" rather than "MedicationPrescription" or
    "MedicationOrder" to generalize the use across inpatient and outpatient
    settings, including care plans, etc., and to harmonize with workflow
    patterns.
    """

    resource_type = Field("MedicationRequest", const=True)

    authoredOn: fhirtypes.DateTime = Field(
        None,
        alias="authoredOn",
        title="Type `DateTime`",
        description="When request was initially authored",
    )
    authoredOn__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_authoredOn", title="Extension field for ``authoredOn``."
    )

    basedOn: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title=(
            "List of `Reference` items referencing `CarePlan, MedicationRequest, "
            "ProcedureRequest, ReferralRequest` (represented as `dict` in JSON)"
        ),
        description="What request fulfills",
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
        title=(
            "Type `Reference` referencing `Encounter, EpisodeOfCare` (represented "
            "as `dict` in JSON)"
        ),
        description="Created during encounter/admission/stay",
    )

    definition: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="definition",
        title=(
            "List of `Reference` items referencing `ActivityDefinition, "
            "PlanDefinition` (represented as `dict` in JSON)"
        ),
        description="Protocol or definition",
    )

    detectedIssue: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="detectedIssue",
        title=(
            "List of `Reference` items referencing `DetectedIssue` (represented as "
            "`dict` in JSON)"
        ),
        description="Clinical Issue with action",
    )

    dispenseRequest: fhirtypes.MedicationRequestDispenseRequestType = Field(
        None,
        alias="dispenseRequest",
        title=(
            "Type `MedicationRequestDispenseRequest` (represented as `dict` in " "JSON)"
        ),
        description="Medication supply authorization",
    )

    dosageInstruction: ListType[fhirtypes.DosageType] = Field(
        None,
        alias="dosageInstruction",
        title="List of `Dosage` items (represented as `dict` in JSON)",
        description="How the medication should be taken",
    )

    eventHistory: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="eventHistory",
        title=(
            "List of `Reference` items referencing `Provenance` (represented as "
            "`dict` in JSON)"
        ),
        description="A list of events of interest in the lifecycle",
    )

    groupIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="groupIdentifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Composite request this is part of",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="External ids for this request",
    )

    intent: fhirtypes.Code = Field(
        ...,
        alias="intent",
        title="Type `Code`",
        description="proposal | plan | order | instance-order",
    )
    intent__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_intent", title="Extension field for ``intent``."
    )

    medicationCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="medicationCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Medication to be taken",
        one_of_many="medication",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    medicationReference: fhirtypes.ReferenceType = Field(
        None,
        alias="medicationReference",
        title=(
            "Type `Reference` referencing `Medication` (represented as `dict` in "
            "JSON)"
        ),
        description="Medication to be taken",
        one_of_many="medication",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Information about the prescription",
    )

    priorPrescription: fhirtypes.ReferenceType = Field(
        None,
        alias="priorPrescription",
        title=(
            "Type `Reference` referencing `MedicationRequest` (represented as "
            "`dict` in JSON)"
        ),
        description="An order/prescription that is being replaced",
    )

    priority: fhirtypes.Code = Field(
        None,
        alias="priority",
        title="Type `Code`",
        description="routine | urgent | stat | asap",
    )
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_priority", title="Extension field for ``priority``."
    )

    reasonCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Reason or indication for writing the prescription",
    )

    reasonReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title=(
            "List of `Reference` items referencing `Condition, Observation` "
            "(represented as `dict` in JSON)"
        ),
        description=(
            "Condition or Observation that supports why the prescription is being "
            "written"
        ),
    )

    recorder: fhirtypes.ReferenceType = Field(
        None,
        alias="recorder",
        title=(
            "Type `Reference` referencing `Practitioner` (represented as `dict` in "
            "JSON)"
        ),
        description="Person who entered the request",
    )

    requester: fhirtypes.MedicationRequestRequesterType = Field(
        None,
        alias="requester",
        title="Type `MedicationRequestRequester` (represented as `dict` in JSON)",
        description="Who/What requested the Request",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code`",
        description=(
            "active | on-hold | cancelled | completed | entered-in-error | stopped "
            "| draft | unknown"
        ),
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
        description="Who or group medication request is for",
    )

    substitution: fhirtypes.MedicationRequestSubstitutionType = Field(
        None,
        alias="substitution",
        title="Type `MedicationRequestSubstitution` (represented as `dict` in JSON)",
        description="Any restrictions on medication substitution",
    )

    supportingInformation: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingInformation",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="Information to support ordering of the medication",
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
            "medication": ["medicationCodeableConcept", "medicationReference"]
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


class MedicationRequestDispenseRequest(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Medication supply authorization.
    Indicates the specific details for the dispense or medication supply part
    of a medication request (also known as a Medication Prescription or
    Medication Order).  Note that this information is not always sent with the
    order.  There may be in some settings (e.g. hospitals) institutional or
    system support for completing the dispense details in the pharmacy
    department.
    """

    resource_type = Field("MedicationRequestDispenseRequest", const=True)

    expectedSupplyDuration: fhirtypes.DurationType = Field(
        None,
        alias="expectedSupplyDuration",
        title="Type `Duration` (represented as `dict` in JSON)",
        description="Number of days supply per dispense",
    )

    numberOfRepeatsAllowed: fhirtypes.PositiveInt = Field(
        None,
        alias="numberOfRepeatsAllowed",
        title="Type `PositiveInt`",
        description="Number of refills authorized",
    )
    numberOfRepeatsAllowed__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_numberOfRepeatsAllowed",
        title="Extension field for ``numberOfRepeatsAllowed``.",
    )

    performer: fhirtypes.ReferenceType = Field(
        None,
        alias="performer",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Intended dispenser",
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Amount of medication to supply per dispense",
    )

    validityPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="validityPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Time period supply is authorized for",
    )


class MedicationRequestRequester(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who/What requested the Request.
    The individual, organization or device that initiated the request and has
    responsibility for its activation.
    """

    resource_type = Field("MedicationRequestRequester", const=True)

    agent: fhirtypes.ReferenceType = Field(
        ...,
        alias="agent",
        title=(
            "Type `Reference` referencing `Practitioner, Organization, Patient, "
            "RelatedPerson, Device` (represented as `dict` in JSON)"
        ),
        description="Who ordered the initial medication(s)",
    )

    onBehalfOf: fhirtypes.ReferenceType = Field(
        None,
        alias="onBehalfOf",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Organization agent is acting for",
    )


class MedicationRequestSubstitution(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Any restrictions on medication substitution.
    Indicates whether or not substitution can or should be part of the
    dispense. In some cases substitution must happen, in other cases
    substitution must not happen. This block explains the prescriber's intent.
    If nothing is specified substitution may be done.
    """

    resource_type = Field("MedicationRequestSubstitution", const=True)

    allowed: bool = Field(
        ...,
        alias="allowed",
        title="Type `bool`",
        description="Whether substitution is allowed or not",
    )
    allowed__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_allowed", title="Extension field for ``allowed``."
    )

    reason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reason",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Why should (not) substitution be made",
    )
