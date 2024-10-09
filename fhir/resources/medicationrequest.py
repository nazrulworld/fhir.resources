from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationRequest
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class MedicationRequest(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
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

    __resource_type__ = "MedicationRequest"

    authoredOn: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="authoredOn",
        title="When request was initially authored",
        description=(
            "The date (and perhaps time) when the prescription was initially "
            "written or authored on."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    authoredOn__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_authoredOn", title="Extension field for ``authoredOn``."
    )

    basedOn: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="basedOn",
        title=(
            "A plan or request that is fulfilled in whole or in part by this "
            "medication request"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "CarePlan",
                "MedicationRequest",
                "ServiceRequest",
                "ImmunizationRecommendation",
            ],
        },
    )

    category: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="category",
        title="Grouping or category of medication request",
        description=(
            "An arbitrary categorization or grouping of the medication request.  It"
            " could be used for indicating where meds are intended to be "
            "administered, eg. in an inpatient setting or in a patient's home, or a"
            " legal category of the medication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    courseOfTherapyType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="courseOfTherapyType",
        title="Overall pattern of medication administration",
        description=(
            "The description of the overall pattern of the administration of the "
            "medication to the patient."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    device: typing.List[fhirtypes.CodeableReferenceType] | None = Field(  # type: ignore
        None,
        alias="device",
        title="Intended type of device for the administration",
        description=(
            "The intended type of device that is to be used for the administration "
            "of the medication (for example, PCA Pump)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DeviceDefinition"],
        },
    )

    dispenseRequest: fhirtypes.MedicationRequestDispenseRequestType | None = Field(  # type: ignore
        None,
        alias="dispenseRequest",
        title="Medication supply authorization",
        description=(
            "Indicates the specific details for the dispense or medication supply "
            "part of a medication request (also known as a Medication Prescription "
            "or Medication Order).  Note that this information is not always sent "
            "with the order.  There may be in some settings (e.g. hospitals) "
            "institutional or system support for completing the dispense details in"
            " the pharmacy department."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    doNotPerform: bool | None = Field(  # type: ignore
        None,
        alias="doNotPerform",
        title=(
            "True if patient is to stop taking or not to start taking the " "medication"
        ),
        description=(
            "If true, indicates that the provider is asking for the patient to "
            "either stop taking or to not start taking the specified medication. "
            "For example, the patient is taking an existing medication and the "
            "provider is changing their medication. They want to create two "
            "seperate requests: one to stop using the current medication and "
            "another to start the new medication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    doNotPerform__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_doNotPerform", title="Extension field for ``doNotPerform``."
    )

    dosageInstruction: typing.List[fhirtypes.DosageType] | None = Field(  # type: ignore
        None,
        alias="dosageInstruction",
        title="Specific instructions for how the medication should be taken",
        description=(
            "Specific instructions for how the medication is to be used by the "
            "patient."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    effectiveDosePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="effectiveDosePeriod",
        title="Period over which the medication is to be taken",
        description=(
            "The period over which the medication is to be taken.  Where there are "
            "multiple dosageInstruction lines (for example, tapering doses), this "
            "is the earliest date and the latest end date of the "
            "dosageInstructions."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    encounter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="encounter",
        title="Encounter created as part of encounter/admission/stay",
        description=(
            "The Encounter during which this [x] was created or to which the "
            "creation of this record is tightly associated."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter"],
        },
    )

    eventHistory: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="eventHistory",
        title="A list of events of interest in the lifecycle",
        description=(
            "Links to Provenance records for past versions of this resource or "
            "fulfilling request or event resources that identify key state "
            "transitions or updates that are likely to be relevant to a user "
            "looking at the current version of the resource."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Provenance"],
        },
    )

    groupIdentifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="groupIdentifier",
        title="Composite request this is part of",
        description=(
            "A shared identifier common to multiple independent Request instances "
            "that were activated/authorized more or less simultaneously by a single"
            " author.  The presence of the same identifier on each request ties "
            "those requests together and may have business ramifications in terms "
            "of reporting of results, billing, etc.  E.g. a requisition number "
            "shared by a set of lab tests ordered together, or a prescription "
            "number shared by all meds ordered at one time."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="External ids for this request",
        description=(
            "Identifiers associated with this medication request that are defined "
            "by business processes and/or used to refer to it when a direct URL "
            "reference to the resource itself is not appropriate. They are business"
            " identifiers assigned to this resource by the performer or other "
            "systems and remain constant as the resource is updated and propagates "
            "from server to server."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    informationSource: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="informationSource",
        title=(
            "The person or organization who provided the information about this "
            "request, if the source is someone other than the requestor"
        ),
        description=(
            "The person or organization who provided the information about this "
            "request, if the source is someone other than the requestor.  This is "
            "often used when the MedicationRequest is reported by another person."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Patient",
                "Practitioner",
                "PractitionerRole",
                "RelatedPerson",
                "Organization",
            ],
        },
    )

    insurance: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="insurance",
        title="Associated insurance coverage",
        description=(
            "Insurance plans, coverage extensions, pre-authorizations and/or pre-"
            "determinations that may be required for delivering the requested "
            "service."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Coverage", "ClaimResponse"],
        },
    )

    intent: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="intent",
        title=(
            "proposal | plan | order | original-order | reflex-order | filler-order"
            " | instance-order | option"
        ),
        description="Whether the request is a proposal, plan, or an original order.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "proposal",
                "plan",
                "order",
                "original-order",
                "reflex-order",
                "filler-order",
                "instance-order",
                "option",
            ],
        },
    )
    intent__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_intent", title="Extension field for ``intent``."
    )

    medication: fhirtypes.CodeableReferenceType = Field(  # type: ignore
        ...,
        alias="medication",
        title="Medication to be taken",
        description=(
            "Identifies the medication being requested. This is a link to a "
            "resource that represents the medication which may be the details of "
            "the medication or simply an attribute carrying a code that identifies "
            "the medication from a known list of medications."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Medication"],
        },
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="note",
        title="Information about the prescription",
        description=(
            "Extra information about the prescription that could not be conveyed by"
            " the other attributes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    performer: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="performer",
        title="Intended performer of administration",
        description=(
            "The specified desired performer of the medication treatment (e.g. the "
            "performer of the medication administration).  For devices, this is the"
            " device that is intended to perform the administration of the "
            "medication.  An IV Pump would be an example of a device that is "
            "performing the administration.  Both the IV Pump and the practitioner "
            "that set the rate or bolus on the pump can be listed as performers."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
                "Patient",
                "DeviceDefinition",
                "RelatedPerson",
                "CareTeam",
                "HealthcareService",
            ],
        },
    )

    performerType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="performerType",
        title="Desired kind of performer of the medication administration",
        description=(
            "Indicates the type of performer of the administration of the "
            "medication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    priorPrescription: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="priorPrescription",
        title=(
            "Reference to an order/prescription that is being replaced by this "
            "MedicationRequest"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["MedicationRequest"],
        },
    )

    priority: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="priority",
        title="routine | urgent | asap | stat",
        description=(
            "Indicates how quickly the Medication Request should be addressed with "
            "respect to other requests."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["routine", "urgent", "asap", "stat"],
        },
    )
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_priority", title="Extension field for ``priority``."
    )

    reason: typing.List[fhirtypes.CodeableReferenceType] | None = Field(  # type: ignore
        None,
        alias="reason",
        title="Reason or indication for ordering or not ordering the medication",
        description=(
            "The reason or the indication for ordering or not ordering the "
            "medication."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Condition", "Observation"],
        },
    )

    recorder: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="recorder",
        title="Person who entered the request",
        description=(
            "The person who entered the order on behalf of another individual for "
            "example in the case of a verbal or a telephone order."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner", "PractitionerRole"],
        },
    )

    renderedDosageInstruction: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="renderedDosageInstruction",
        title="Full representation of the dosage instructions",
        description=(
            "The full representation of the dose of the medication included in all "
            "dosage instructions.  To be used when multiple dosage instructions are"
            " included to represent complex dosing such as increasing or tapering "
            "doses."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    renderedDosageInstruction__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_renderedDosageInstruction",
        title="Extension field for ``renderedDosageInstruction``.",
    )

    reported: bool | None = Field(  # type: ignore
        None,
        alias="reported",
        title="Reported rather than primary record",
        description=(
            "Indicates if this record was captured as a secondary 'reported' record"
            " rather than as an original primary source-of-truth record.  It may "
            "also indicate the source of the report."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    reported__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_reported", title="Extension field for ``reported``."
    )

    requester: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="requester",
        title="Who/What requested the Request",
        description=(
            "The individual, organization, or device that initiated the request and"
            " has responsibility for its activation."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
                "Patient",
                "RelatedPerson",
                "Device",
            ],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title=(
            "active | on-hold | ended | stopped | completed | cancelled | entered-"
            "in-error | draft | unknown"
        ),
        description=(
            "A code specifying the current state of the order.  Generally, this "
            "will be active or completed state."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "active",
                "on-hold",
                "ended",
                "stopped",
                "completed",
                "cancelled",
                "entered-in-error",
                "draft",
                "unknown",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    statusChanged: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="statusChanged",
        title="When the status was changed",
        description="The date (and perhaps time) when the status was changed.",
        json_schema_extra={
            "element_property": True,
        },
    )
    statusChanged__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_statusChanged", title="Extension field for ``statusChanged``."
    )

    statusReason: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="statusReason",
        title="Reason for current status",
        description="Captures the reason for the current state of the MedicationRequest.",
        json_schema_extra={
            "element_property": True,
        },
    )

    subject: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="subject",
        title="Individual or group for whom the medication has been requested",
        description="The individual or group for whom the medication has been requested.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "Group"],
        },
    )

    substitution: fhirtypes.MedicationRequestSubstitutionType | None = Field(  # type: ignore
        None,
        alias="substitution",
        title="Any restrictions on medication substitution",
        description=(
            "Indicates whether or not substitution can or should be part of the "
            "dispense. In some cases, substitution must happen, in other cases "
            "substitution must not happen. This block explains the prescriber's "
            "intent. If nothing is specified substitution may be done."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    supportingInformation: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="supportingInformation",
        title="Information to support fulfilling of the medication",
        description=(
            "Information to support fulfilling (i.e. dispensing or administering) "
            "of the medication, for example, patient height and weight, a "
            "MedicationStatement for the patient)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationRequest`` according specification,
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
            "priorPrescription",
            "groupIdentifier",
            "status",
            "statusReason",
            "statusChanged",
            "intent",
            "category",
            "priority",
            "doNotPerform",
            "medication",
            "subject",
            "informationSource",
            "encounter",
            "supportingInformation",
            "authoredOn",
            "requester",
            "reported",
            "performerType",
            "performer",
            "device",
            "recorder",
            "reason",
            "courseOfTherapyType",
            "insurance",
            "note",
            "renderedDosageInstruction",
            "effectiveDosePeriod",
            "dosageInstruction",
            "dispenseRequest",
            "substitution",
            "eventHistory",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("intent", "intent__ext"), ("status", "status__ext")]
        return required_fields


class MedicationRequestDispenseRequest(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
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

    __resource_type__ = "MedicationRequestDispenseRequest"

    dispenseInterval: fhirtypes.DurationType | None = Field(  # type: ignore
        None,
        alias="dispenseInterval",
        title="Minimum period of time between dispenses",
        description=(
            "The minimum period of time that must occur between dispenses of the "
            "medication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    dispenser: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="dispenser",
        title="Intended performer of dispense",
        description=(
            "Indicates the intended performing Organization that will dispense the "
            "medication as specified by the prescriber."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    dispenserInstruction: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="dispenserInstruction",
        title="Additional information for the dispenser",
        description=(
            "Provides additional information to the dispenser, for example, "
            "counselling to be provided to the patient."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    doseAdministrationAid: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="doseAdministrationAid",
        title="Type of adherence packaging to use for the dispense",
        description=(
            "Provides information about the type of adherence packaging to be "
            "supplied for the medication dispense."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    expectedSupplyDuration: fhirtypes.DurationType | None = Field(  # type: ignore
        None,
        alias="expectedSupplyDuration",
        title="Number of days supply per dispense",
        description=(
            "Identifies the period time over which the supplied product is expected"
            " to be used, or the length of time the dispense is expected to last."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    initialFill: fhirtypes.MedicationRequestDispenseRequestInitialFillType | None = Field(  # type: ignore
        None,
        alias="initialFill",
        title="First fill details",
        description=(
            "Indicates the quantity or duration for the first dispense of the "
            "medication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    numberOfRepeatsAllowed: fhirtypes.UnsignedIntType | None = Field(  # type: ignore
        None,
        alias="numberOfRepeatsAllowed",
        title="Number of refills authorized",
        description=(
            "An integer indicating the number of times, in addition to the original"
            " dispense, (aka refills or repeats) that the patient can receive the "
            "prescribed medication. Usage Notes: This integer does not include the "
            "original order dispense. This means that if an order indicates "
            'dispense 30 tablets plus "3 repeats", then the order can be dispensed '
            "a total of 4 times and the patient can receive a total of 120 tablets."
            "  A prescriber may explicitly say that zero refills are permitted "
            "after the initial dispense."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    numberOfRepeatsAllowed__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_numberOfRepeatsAllowed",
        title="Extension field for ``numberOfRepeatsAllowed``.",
    )

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="Amount of medication to supply per dispense",
        description="The amount that is to be dispensed for one fill.",
        json_schema_extra={
            "element_property": True,
        },
    )

    validityPeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="validityPeriod",
        title="Time period supply is authorized for",
        description=(
            "This indicates the validity period of a prescription (stale dating the"
            " Prescription)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationRequestDispenseRequest`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "initialFill",
            "dispenseInterval",
            "validityPeriod",
            "numberOfRepeatsAllowed",
            "quantity",
            "expectedSupplyDuration",
            "dispenser",
            "dispenserInstruction",
            "doseAdministrationAid",
        ]


class MedicationRequestDispenseRequestInitialFill(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    First fill details.
    Indicates the quantity or duration for the first dispense of the
    medication.
    """

    __resource_type__ = "MedicationRequestDispenseRequestInitialFill"

    duration: fhirtypes.DurationType | None = Field(  # type: ignore
        None,
        alias="duration",
        title="First fill duration",
        description="The length of time that the first dispense is expected to last.",
        json_schema_extra={
            "element_property": True,
        },
    )

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="First fill quantity",
        description="The amount or quantity to provide as part of the first dispense.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationRequestDispenseRequestInitialFill`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "quantity", "duration"]


class MedicationRequestSubstitution(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Any restrictions on medication substitution.
    Indicates whether or not substitution can or should be part of the
    dispense. In some cases, substitution must happen, in other cases
    substitution must not happen. This block explains the prescriber's intent.
    If nothing is specified substitution may be done.
    """

    __resource_type__ = "MedicationRequestSubstitution"

    allowedBoolean: bool | None = Field(  # type: ignore
        None,
        alias="allowedBoolean",
        title="Whether substitution is allowed or not",
        description=(
            "True if the prescriber allows a different drug to be dispensed from "
            "what was prescribed."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e allowed[x]
            "one_of_many": "allowed",
            "one_of_many_required": True,
        },
    )
    allowedBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_allowedBoolean", title="Extension field for ``allowedBoolean``."
    )

    allowedCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="allowedCodeableConcept",
        title="Whether substitution is allowed or not",
        description=(
            "True if the prescriber allows a different drug to be dispensed from "
            "what was prescribed."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e allowed[x]
            "one_of_many": "allowed",
            "one_of_many_required": True,
        },
    )

    reason: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="reason",
        title="Why should (not) substitution be made",
        description=(
            "Indicates the reason for the substitution, or why substitution must or"
            " must not be performed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationRequestSubstitution`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "allowedBoolean",
            "allowedCodeableConcept",
            "reason",
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
        one_of_many_fields = {"allowed": ["allowedBoolean", "allowedCodeableConcept"]}
        return one_of_many_fields
