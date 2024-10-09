from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationRequest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
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
        title="What request fulfills",
        description=(
            "A plan or request that is fulfilled in whole or in part by this "
            "medication request."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "CarePlan",
                "MedicationRequest",
                "ProcedureRequest",
                "ReferralRequest",
            ],
        },
    )

    category: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="category",
        title="Type of medication usage",
        description=(
            "Indicates the type of medication order and where the medication is "
            "expected to be consumed or administered."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    context: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="context",
        title="Created during encounter/admission/stay",
        description=(
            "A link to an encounter, or episode of care, that identifies the "
            "particular occurrence or set occurrences of contact between patient "
            "and health care provider."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter", "EpisodeOfCare"],
        },
    )

    definition: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="definition",
        title="Protocol or definition",
        description="Protocol or definition followed by this request.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ActivityDefinition", "PlanDefinition"],
        },
    )

    detectedIssue: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="detectedIssue",
        title="Clinical Issue with action",
        description=(
            "Indicates an actual or potential clinical issue with or between one or"
            " more active or proposed clinical actions for a patient; e.g. Drug-"
            "drug interaction, duplicate therapy, dosage alert etc."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DetectedIssue"],
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

    dosageInstruction: typing.List[fhirtypes.DosageType] | None = Field(  # type: ignore
        None,
        alias="dosageInstruction",
        title="How the medication should be taken",
        description="Indicates how the medication is to be used by the patient.",
        json_schema_extra={
            "element_property": True,
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
            "A shared identifier common to all requests that were authorized more "
            "or less simultaneously by a single author, representing the identifier"
            " of the requisition or prescription."
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
            "This records identifiers associated with this medication request that "
            "are defined by business processes and/or used to refer to it when a "
            "direct URL reference to the resource itself is not appropriate. For "
            "example a re-imbursement system might issue its own id for each "
            "prescription that is created.  This is particularly important where "
            "FHIR only provides part of an entire workflow process where records "
            "must be tracked through an entire system."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    intent: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="intent",
        title="proposal | plan | order | instance-order",
        description="Whether the request is a proposal, plan, or an original order.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["proposal", "plan", "order", "instance-order"],
        },
    )
    intent__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_intent", title="Extension field for ``intent``."
    )

    medicationCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="medicationCodeableConcept",
        title="Medication to be taken",
        description=(
            "Identifies the medication being requested. This is a link to a "
            "resource that represents the medication which may be the details of "
            "the medication or simply an attribute carrying a code that identifies "
            "the medication from a known list of medications."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e medication[x]
            "one_of_many": "medication",
            "one_of_many_required": True,
        },
    )

    medicationReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="medicationReference",
        title="Medication to be taken",
        description=(
            "Identifies the medication being requested. This is a link to a "
            "resource that represents the medication which may be the details of "
            "the medication or simply an attribute carrying a code that identifies "
            "the medication from a known list of medications."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e medication[x]
            "one_of_many": "medication",
            "one_of_many_required": True,
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

    priorPrescription: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="priorPrescription",
        title="An order/prescription that is being replaced",
        description=(
            "A link to a resource representing an earlier order related order or "
            "prescription."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["MedicationRequest"],
        },
    )

    priority: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="priority",
        title="routine | urgent | stat | asap",
        description=(
            "Indicates how quickly the Medication Request should be addressed with "
            "respect to other requests."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["routine", "urgent", "stat", "asap"],
        },
    )
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_priority", title="Extension field for ``priority``."
    )

    reasonCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="reasonCode",
        title="Reason or indication for writing the prescription",
        description="The reason or the indication for ordering the medication.",
        json_schema_extra={
            "element_property": True,
        },
    )

    reasonReference: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="reasonReference",
        title=(
            "Condition or Observation that supports why the prescription is being "
            "written"
        ),
        description="Condition or observation that supports why the medication was ordered.",
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
            "enum_reference_types": ["Practitioner"],
        },
    )

    requester: fhirtypes.MedicationRequestRequesterType | None = Field(  # type: ignore
        None,
        alias="requester",
        title="Who/What requested the Request",
        description=(
            "The individual, organization or device that initiated the request and "
            "has responsibility for its activation."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title=(
            "active | on-hold | cancelled | completed | entered-in-error | stopped "
            "| draft | unknown"
        ),
        description=(
            "A code specifying the current state of the order.  Generally this will"
            " be active or completed state."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "active",
                "on-hold",
                "cancelled",
                "completed",
                "entered-in-error",
                "stopped",
                "draft",
                "unknown",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="subject",
        title="Who or group medication request is for",
        description=(
            "A link to a resource representing the person or set of individuals to "
            "whom the medication will be given."
        ),
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
            "dispense. In some cases substitution must happen, in other cases "
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
        title="Information to support ordering of the medication",
        description=(
            "Include additional information (for example, patient height and "
            "weight) that supports the ordering of the medication."
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
            "definition",
            "basedOn",
            "groupIdentifier",
            "status",
            "intent",
            "category",
            "priority",
            "medicationCodeableConcept",
            "medicationReference",
            "subject",
            "context",
            "supportingInformation",
            "authoredOn",
            "requester",
            "recorder",
            "reasonCode",
            "reasonReference",
            "note",
            "dosageInstruction",
            "dispenseRequest",
            "substitution",
            "priorPrescription",
            "detectedIssue",
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
        required_fields = [("intent", "intent__ext")]
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
            "medication": ["medicationCodeableConcept", "medicationReference"]
        }
        return one_of_many_fields


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

    numberOfRepeatsAllowed: fhirtypes.PositiveIntType | None = Field(  # type: ignore
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

    performer: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="performer",
        title="Intended dispenser",
        description=(
            "Indicates the intended dispensing Organization specified by the "
            "prescriber."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
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
            "validityPeriod",
            "numberOfRepeatsAllowed",
            "quantity",
            "expectedSupplyDuration",
            "performer",
        ]


class MedicationRequestRequester(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who/What requested the Request.
    The individual, organization or device that initiated the request and has
    responsibility for its activation.
    """

    __resource_type__ = "MedicationRequestRequester"

    agent: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="agent",
        title="Who ordered the initial medication(s)",
        description=(
            "The healthcare professional responsible for authorizing the initial "
            "prescription."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "Organization",
                "Patient",
                "RelatedPerson",
                "Device",
            ],
        },
    )

    onBehalfOf: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="onBehalfOf",
        title="Organization agent is acting for",
        description="The organization the device or practitioner was acting on behalf of.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationRequestRequester`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "agent", "onBehalfOf"]


class MedicationRequestSubstitution(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Any restrictions on medication substitution.
    Indicates whether or not substitution can or should be part of the
    dispense. In some cases substitution must happen, in other cases
    substitution must not happen. This block explains the prescriber's intent.
    If nothing is specified substitution may be done.
    """

    __resource_type__ = "MedicationRequestSubstitution"

    allowed: bool | None = Field(  # type: ignore
        None,
        alias="allowed",
        title="Whether substitution is allowed or not",
        description=(
            "True if the prescriber allows a different drug to be dispensed from "
            "what was prescribed."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    allowed__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_allowed", title="Extension field for ``allowed``."
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
        return ["id", "extension", "modifierExtension", "allowed", "reason"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("allowed", "allowed__ext")]
        return required_fields
