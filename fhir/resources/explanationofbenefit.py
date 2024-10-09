from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ExplanationOfBenefit
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ExplanationOfBenefit(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Explanation of Benefit resource.
    This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """

    __resource_type__ = "ExplanationOfBenefit"

    accident: fhirtypes.ExplanationOfBenefitAccidentType | None = Field(  # type: ignore
        None,
        alias="accident",
        title="Details of the event",
        description=(
            "Details of a accident which resulted in injuries which required the "
            "products and services listed in the claim."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    addItem: typing.List[fhirtypes.ExplanationOfBenefitAddItemType] | None = Field(  # type: ignore
        None,
        alias="addItem",
        title="Insurer added line items",
        description=(
            "The first-tier service adjudications for payor added product or "
            "service lines."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    adjudication: typing.List[fhirtypes.ExplanationOfBenefitItemAdjudicationType] | None = Field(  # type: ignore
        None,
        alias="adjudication",
        title="Header-level adjudication",
        description=(
            "The adjudication results which are presented at the header level "
            "rather than at the line-item or add-item levels."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    benefitBalance: typing.List[fhirtypes.ExplanationOfBenefitBenefitBalanceType] | None = Field(  # type: ignore
        None,
        alias="benefitBalance",
        title="Balance by Benefit Category",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    benefitPeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="benefitPeriod",
        title="When the benefits are applicable",
        description="The term of the benefits documented in this response.",
        json_schema_extra={
            "element_property": True,
        },
    )

    billablePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="billablePeriod",
        title="Relevant time frame for the claim",
        description="The period for which charges are being submitted.",
        json_schema_extra={
            "element_property": True,
        },
    )

    careTeam: typing.List[fhirtypes.ExplanationOfBenefitCareTeamType] | None = Field(  # type: ignore
        None,
        alias="careTeam",
        title="Care Team members",
        description="The members of the team who provided the products and services.",
        json_schema_extra={
            "element_property": True,
        },
    )

    claim: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="claim",
        title="Claim reference",
        description=(
            "The business identifier for the instance of the adjudication request: "
            "claim predetermination or preauthorization."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Claim"],
        },
    )

    claimResponse: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="claimResponse",
        title="Claim response reference",
        description=(
            "The business identifier for the instance of the adjudication response:"
            " claim, predetermination or preauthorization response."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ClaimResponse"],
        },
    )

    created: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="created",
        title="Response creation date",
        description="The date this resource was created.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_created", title="Extension field for ``created``."
    )

    decision: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="decision",
        title="Result of the adjudication",
        description=(
            "The result of the claim, predetermination, or preauthorization "
            "adjudication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    diagnosis: typing.List[fhirtypes.ExplanationOfBenefitDiagnosisType] | None = Field(  # type: ignore
        None,
        alias="diagnosis",
        title="Pertinent diagnosis information",
        description="Information about diagnoses relevant to the claim items.",
        json_schema_extra={
            "element_property": True,
        },
    )

    diagnosisRelatedGroup: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="diagnosisRelatedGroup",
        title="Package billing code",
        description=(
            "A package billing code or bundle code used to group products and "
            "services to a particular health condition (such as heart attack) which"
            " is based on a predetermined grouping code system."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    disposition: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="disposition",
        title="Disposition Message",
        description="A human readable description of the status of the adjudication.",
        json_schema_extra={
            "element_property": True,
        },
    )
    disposition__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_disposition", title="Extension field for ``disposition``."
    )

    encounter: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="encounter",
        title="Encounters associated with the listed treatments",
        description="Healthcare encounters related to this claim.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter"],
        },
    )

    enterer: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="enterer",
        title="Author of the claim",
        description=(
            "Individual who created the claim, predetermination or " "preauthorization."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Patient",
                "RelatedPerson",
            ],
        },
    )

    event: typing.List[fhirtypes.ExplanationOfBenefitEventType] | None = Field(  # type: ignore
        None,
        alias="event",
        title="Event information",
        description="Information code for an event with a corresponding date or period.",
        json_schema_extra={
            "element_property": True,
        },
    )

    facility: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="facility",
        title="Servicing Facility",
        description="Facility where the services were provided.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location", "Organization"],
        },
    )

    form: fhirtypes.AttachmentType | None = Field(  # type: ignore
        None,
        alias="form",
        title="Printed reference or actual form",
        description=(
            "The actual form, by reference or inclusion, for printing the content "
            "or an EOB."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    formCode: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="formCode",
        title="Printed form identifier",
        description="A code for the form to be used for printing the content.",
        json_schema_extra={
            "element_property": True,
        },
    )

    fundsReserve: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="fundsReserve",
        title="Funds reserved status",
        description=(
            "A code, used only on a response to a preauthorization, to indicate "
            "whether the benefits payable have been reserved and for whom."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    fundsReserveRequested: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="fundsReserveRequested",
        title="For whom to reserve funds",
        description=(
            "A code to indicate whether and for whom funds are to be reserved for "
            "future claims."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business Identifier for the resource",
        description="A unique identifier assigned to this explanation of benefit.",
        json_schema_extra={
            "element_property": True,
        },
    )

    insurance: typing.List[fhirtypes.ExplanationOfBenefitInsuranceType] | None = Field(  # type: ignore
        None,
        alias="insurance",
        title="Patient insurance information",
        description=(
            "Financial instruments for reimbursement for the health care products "
            "and services specified on the claim."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    insurer: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="insurer",
        title="Party responsible for reimbursement",
        description=(
            "The party responsible for authorization, adjudication and "
            "reimbursement."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    item: typing.List[fhirtypes.ExplanationOfBenefitItemType] | None = Field(  # type: ignore
        None,
        alias="item",
        title="Product or service provided",
        description=(
            "A claim line. Either a simple (a product or service) or a 'group' of "
            "details which can also be a simple items or groups of sub-details."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    originalPrescription: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="originalPrescription",
        title="Original prescription if superceded by fulfiller",
        description=(
            "Original prescription which has been superseded by this prescription "
            "to support the dispensing of pharmacy services, medications or "
            "products."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["MedicationRequest"],
        },
    )

    outcome: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="outcome",
        title="queued | complete | error | partial",
        description=(
            "The outcome of the claim, predetermination, or preauthorization "
            "processing."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["queued", "complete", "error", "partial"],
        },
    )
    outcome__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_outcome", title="Extension field for ``outcome``."
    )

    patient: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="patient",
        title="The recipient of the products and services",
        description=(
            "The party to whom the professional services and/or products have been "
            "supplied or are being considered and for whom actual for forecast "
            "reimbursement is sought."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient"],
        },
    )

    patientPaid: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="patientPaid",
        title="Paid by the patient",
        description=(
            "The amount paid by the patient, in total at the claim claim level or "
            "specifically for the item and detail level, to the provider for goods "
            "and services."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    payee: fhirtypes.ExplanationOfBenefitPayeeType | None = Field(  # type: ignore
        None,
        alias="payee",
        title="Recipient of benefits payable",
        description=(
            "The party to be reimbursed for cost of the products and services "
            "according to the terms of the policy."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    payment: fhirtypes.ExplanationOfBenefitPaymentType | None = Field(  # type: ignore
        None,
        alias="payment",
        title="Payment Details",
        description="Payment details for the adjudication of the claim.",
        json_schema_extra={
            "element_property": True,
        },
    )

    preAuthRef: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="preAuthRef",
        title="Preauthorization reference",
        description=(
            "Reference from the Insurer which is used in later communications which"
            " refers to this adjudication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    preAuthRef__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_preAuthRef", title="Extension field for ``preAuthRef``."
    )

    preAuthRefPeriod: typing.List[fhirtypes.PeriodType] | None = Field(  # type: ignore
        None,
        alias="preAuthRefPeriod",
        title="Preauthorization in-effect period",
        description=(
            "The timeframe during which the supplied preauthorization reference may"
            " be quoted on claims to obtain the adjudication as provided."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    precedence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="precedence",
        title="Precedence (primary, secondary, etc.)",
        description=(
            "This indicates the relative order of a series of EOBs related to "
            "different coverages for the same suite of services."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    precedence__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_precedence", title="Extension field for ``precedence``."
    )

    prescription: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="prescription",
        title="Prescription authorizing services or products",
        description=(
            "Prescription is the document/authorization given to the claim author "
            "for them to provide products and services for which consideration "
            "(reimbursement) is sought. Could be a RX for medications, an 'order' "
            "for oxygen or wheelchair or physiotherapy treatments."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["MedicationRequest", "VisionPrescription"],
        },
    )

    priority: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="priority",
        title="Desired processing urgency",
        description=(
            "The provider-required urgency of processing the request. Typical "
            "values include: stat, normal deferred."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    procedure: typing.List[fhirtypes.ExplanationOfBenefitProcedureType] | None = Field(  # type: ignore
        None,
        alias="procedure",
        title="Clinical procedures performed",
        description=(
            "Procedures performed on the patient relevant to the billing items with"
            " the claim."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    processNote: typing.List[fhirtypes.ExplanationOfBenefitProcessNoteType] | None = Field(  # type: ignore
        None,
        alias="processNote",
        title="Note concerning adjudication",
        description=(
            "A note that describes or explains adjudication results in a human "
            "readable form."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    provider: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="provider",
        title="Party responsible for the claim",
        description=(
            "The provider which is responsible for the claim, predetermination or "
            "preauthorization."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
            ],
        },
    )

    referral: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="referral",
        title="Treatment Referral",
        description=(
            "The referral information received by the claim author, it is not to be"
            " used when the author generates a referral for a patient. A copy of "
            "that referral may be provided as supporting information. Some insurers"
            " require proof of referral to pay for services or to pay specialist "
            "rates for services."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ServiceRequest"],
        },
    )

    related: typing.List[fhirtypes.ExplanationOfBenefitRelatedType] | None = Field(  # type: ignore
        None,
        alias="related",
        title="Prior or corollary claims",
        description=(
            "Other claims which are related to this claim such as prior submissions"
            " or claims for related services or for the same event."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="active | cancelled | draft | entered-in-error",
        description="The status of the resource instance.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["active", "cancelled", "draft", "entered-in-error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    subType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="subType",
        title="More granular claim type",
        description=(
            "A finer grained suite of claim type codes which may convey additional "
            "information such as Inpatient vs Outpatient and/or a specialty "
            "service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    supportingInfo: typing.List[fhirtypes.ExplanationOfBenefitSupportingInfoType] | None = Field(  # type: ignore
        None,
        alias="supportingInfo",
        title="Supporting information",
        description=(
            "Additional information codes regarding exceptions, special "
            "considerations, the condition, situation, prior or concurrent issues."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    total: typing.List[fhirtypes.ExplanationOfBenefitTotalType] | None = Field(  # type: ignore
        None,
        alias="total",
        title="Adjudication totals",
        description="Categorized monetary totals for the adjudication.",
        json_schema_extra={
            "element_property": True,
        },
    )

    traceNumber: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="traceNumber",
        title="Number for tracking",
        description=(
            "Trace number for tracking purposes. May be defined at the jurisdiction"
            " level or between trading partners."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Category or discipline",
        description=(
            "The category of claim, e.g. oral, pharmacy, vision, institutional, "
            "professional."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    use: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="use",
        title="claim | preauthorization | predetermination",
        description=(
            "A code to indicate whether the nature of the request is: Claim - A "
            "request to an Insurer to adjudicate the supplied charges for health "
            "care goods and services under the identified policy and to pay the "
            "determined Benefit amount, if any; Preauthorization - A request to an "
            "Insurer to adjudicate the supplied proposed future charges for health "
            "care goods and services under the identified policy and to approve the"
            " services and provide the expected benefit amounts and potentially to "
            "reserve funds to pay the benefits when Claims for the indicated "
            "services are later submitted; or, Pre-determination - A request to an "
            "Insurer to adjudicate the supplied 'what if' charges for health care "
            "goods and services under the identified policy and report back what "
            "the Benefit payable would be had the services actually been provided."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["claim", "preauthorization", "predetermination"],
        },
    )
    use__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_use", title="Extension field for ``use``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefit`` according specification,
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
            "traceNumber",
            "status",
            "type",
            "subType",
            "use",
            "patient",
            "billablePeriod",
            "created",
            "enterer",
            "insurer",
            "provider",
            "priority",
            "fundsReserveRequested",
            "fundsReserve",
            "related",
            "prescription",
            "originalPrescription",
            "event",
            "payee",
            "referral",
            "encounter",
            "facility",
            "claim",
            "claimResponse",
            "outcome",
            "decision",
            "disposition",
            "preAuthRef",
            "preAuthRefPeriod",
            "diagnosisRelatedGroup",
            "careTeam",
            "supportingInfo",
            "diagnosis",
            "procedure",
            "precedence",
            "insurance",
            "accident",
            "patientPaid",
            "item",
            "addItem",
            "adjudication",
            "total",
            "payment",
            "formCode",
            "form",
            "processNote",
            "benefitPeriod",
            "benefitBalance",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("created", "created__ext"),
            ("outcome", "outcome__ext"),
            ("status", "status__ext"),
            ("use", "use__ext"),
        ]
        return required_fields


class ExplanationOfBenefitAccident(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details of the event.
    Details of a accident which resulted in injuries which required the
    products and services listed in the claim.
    """

    __resource_type__ = "ExplanationOfBenefitAccident"

    date: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="date",
        title="When the incident occurred",
        description=(
            "Date of an accident event  related to the products and services "
            "contained in the claim."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    locationAddress: fhirtypes.AddressType | None = Field(  # type: ignore
        None,
        alias="locationAddress",
        title="Where the event occurred",
        description="The physical location of the accident event.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e location[x]
            "one_of_many": "location",
            "one_of_many_required": False,
        },
    )

    locationReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="locationReference",
        title="Where the event occurred",
        description="The physical location of the accident event.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e location[x]
            "one_of_many": "location",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="The nature of the accident",
        description=(
            "The type or context of the accident event for the purposes of "
            "selection of potential insurance coverages and determination of "
            "coordination between insurers."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitAccident`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "date",
            "type",
            "locationAddress",
            "locationReference",
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
        one_of_many_fields = {"location": ["locationAddress", "locationReference"]}
        return one_of_many_fields


class ExplanationOfBenefitAddItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Insurer added line items.
    The first-tier service adjudications for payor added product or service
    lines.
    """

    __resource_type__ = "ExplanationOfBenefitAddItem"

    adjudication: typing.List[fhirtypes.ExplanationOfBenefitItemAdjudicationType] | None = Field(  # type: ignore
        None,
        alias="adjudication",
        title="Added items adjudication",
        description="The adjudication results.",
        json_schema_extra={
            "element_property": True,
        },
    )

    bodySite: typing.List[fhirtypes.ExplanationOfBenefitAddItemBodySiteType] | None = Field(  # type: ignore
        None,
        alias="bodySite",
        title="Anatomical location",
        description="Physical location where the service is performed or applies.",
        json_schema_extra={
            "element_property": True,
        },
    )

    detail: typing.List[fhirtypes.ExplanationOfBenefitAddItemDetailType] | None = Field(  # type: ignore
        None,
        alias="detail",
        title="Insurer added line items",
        description="The second-tier service adjudications for payor added services.",
        json_schema_extra={
            "element_property": True,
        },
    )

    detailSequence: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="detailSequence",
        title="Detail sequence number",
        description=(
            "The sequence number of the details within the claim item which this "
            "line is intended to replace."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    detailSequence__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_detailSequence", title="Extension field for ``detailSequence``."
    )

    factor: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="factor",
        title="Price scaling factor",
        description=(
            "A real number that represents a multiplier used in determining the "
            "overall value of services delivered and/or goods received. The concept"
            " of a Factor allows for a discount or surcharge multiplier to be "
            "applied to a monetary amount."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_factor", title="Extension field for ``factor``."
    )

    itemSequence: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="itemSequence",
        title="Item sequence number",
        description="Claim items which this service line is intended to replace.",
        json_schema_extra={
            "element_property": True,
        },
    )
    itemSequence__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_itemSequence", title="Extension field for ``itemSequence``."
    )

    locationAddress: fhirtypes.AddressType | None = Field(  # type: ignore
        None,
        alias="locationAddress",
        title="Place of service or where product was supplied",
        description="Where the product or service was provided.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e location[x]
            "one_of_many": "location",
            "one_of_many_required": False,
        },
    )

    locationCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="locationCodeableConcept",
        title="Place of service or where product was supplied",
        description="Where the product or service was provided.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e location[x]
            "one_of_many": "location",
            "one_of_many_required": False,
        },
    )

    locationReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="locationReference",
        title="Place of service or where product was supplied",
        description="Where the product or service was provided.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e location[x]
            "one_of_many": "location",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    modifier: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="modifier",
        title="Service/Product billing modifiers",
        description=(
            "Item typification or modifiers codes to convey additional context for "
            "the product or service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    net: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="net",
        title="Total item cost",
        description=(
            "The total amount claimed for the group (if a grouper) or the addItem. "
            "Net = unit price * quantity * factor."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    noteNumber: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="noteNumber",
        title="Applicable note numbers",
        description=(
            "The numbers associated with notes below which apply to the "
            "adjudication of this item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    noteNumber__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_noteNumber", title="Extension field for ``noteNumber``."
    )

    patientPaid: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="patientPaid",
        title="Paid by the patient",
        description=(
            "The amount paid by the patient, in total at the claim claim level or "
            "specifically for the item and detail level, to the provider for goods "
            "and services."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    productOrService: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="productOrService",
        title="Billing, service, product, or drug code",
        description=(
            "When the value is a group code then this item collects a set of "
            "related item details, otherwise this contains the product, service, "
            "drug or other billing code for the item. This element may be the start"
            " of a range of .productOrService codes used in conjunction with "
            ".productOrServiceEnd or it may be a solo element where "
            ".productOrServiceEnd is not used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    productOrServiceEnd: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="productOrServiceEnd",
        title="End of a range of codes",
        description=(
            "This contains the end of a range of product, service, drug or other "
            "billing codes for the item. This element is not used when the "
            ".productOrService is a group code. This value may only be present when"
            " a .productOfService code has been provided to convey the start of the"
            " range. Typically this value may be used only with preauthorizations "
            "and not with claims."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    programCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="programCode",
        title="Program the product or service is provided under",
        description="Identifies the program under which this may be recovered.",
        json_schema_extra={
            "element_property": True,
        },
    )

    provider: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="provider",
        title="Authorized providers",
        description=(
            "The providers who are authorized for the services rendered to the "
            "patient."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
            ],
        },
    )

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="Count of products or services",
        description="The number of repetitions of a service or product.",
        json_schema_extra={
            "element_property": True,
        },
    )

    request: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="request",
        title="Request or Referral for Service",
        description="Request or Referral for Goods or Service to be rendered.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "DeviceRequest",
                "MedicationRequest",
                "NutritionOrder",
                "ServiceRequest",
                "SupplyRequest",
                "VisionPrescription",
            ],
        },
    )

    revenue: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="revenue",
        title="Revenue or cost center code",
        description=(
            "The type of revenue or cost center providing the product and/or "
            "service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reviewOutcome: fhirtypes.ExplanationOfBenefitItemReviewOutcomeType | None = Field(  # type: ignore
        None,
        alias="reviewOutcome",
        title="Additem level adjudication results",
        description=(
            "The high-level results of the adjudication if adjudication has been "
            "performed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    servicedDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="servicedDate",
        title="Date or dates of service or product delivery",
        description=(
            "The date or dates when the service or product was supplied, performed "
            "or completed."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e serviced[x]
            "one_of_many": "serviced",
            "one_of_many_required": False,
        },
    )
    servicedDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_servicedDate", title="Extension field for ``servicedDate``."
    )

    servicedPeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="servicedPeriod",
        title="Date or dates of service or product delivery",
        description=(
            "The date or dates when the service or product was supplied, performed "
            "or completed."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e serviced[x]
            "one_of_many": "serviced",
            "one_of_many_required": False,
        },
    )

    subDetailSequence: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="subDetailSequence",
        title="Subdetail sequence number",
        description=(
            "The sequence number of the sub-details woithin the details within the "
            "claim item which this line is intended to replace."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    subDetailSequence__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_subDetailSequence",
        title="Extension field for ``subDetailSequence``.",
    )

    tax: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="tax",
        title="Total tax",
        description="The total of taxes applicable for this product or service.",
        json_schema_extra={
            "element_property": True,
        },
    )

    traceNumber: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="traceNumber",
        title="Number for tracking",
        description=(
            "Trace number for tracking purposes. May be defined at the jurisdiction"
            " level or between trading partners."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    unitPrice: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="unitPrice",
        title="Fee, charge or cost per item",
        description=(
            "If the item is not a group then this is the fee for the product or "
            "service, otherwise this is the total of the fees for the details of "
            "the group."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitAddItem`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "itemSequence",
            "detailSequence",
            "subDetailSequence",
            "traceNumber",
            "provider",
            "revenue",
            "productOrService",
            "productOrServiceEnd",
            "request",
            "modifier",
            "programCode",
            "servicedDate",
            "servicedPeriod",
            "locationCodeableConcept",
            "locationAddress",
            "locationReference",
            "patientPaid",
            "quantity",
            "unitPrice",
            "factor",
            "tax",
            "net",
            "bodySite",
            "noteNumber",
            "reviewOutcome",
            "adjudication",
            "detail",
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
            "location": [
                "locationAddress",
                "locationCodeableConcept",
                "locationReference",
            ],
            "serviced": ["servicedDate", "servicedPeriod"],
        }
        return one_of_many_fields


class ExplanationOfBenefitAddItemBodySite(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Anatomical location.
    Physical location where the service is performed or applies.
    """

    __resource_type__ = "ExplanationOfBenefitAddItemBodySite"

    site: typing.List[fhirtypes.CodeableReferenceType] = Field(  # type: ignore
        ...,
        alias="site",
        title="Location",
        description="Physical service site on the patient (limb, tooth, etc.).",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["BodyStructure"],
        },
    )

    subSite: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="subSite",
        title="Sub-location",
        description=(
            "A region or surface of the bodySite, e.g. limb region or tooth "
            "surface(s)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitAddItemBodySite`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "site", "subSite"]


class ExplanationOfBenefitAddItemDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Insurer added line items.
    The second-tier service adjudications for payor added services.
    """

    __resource_type__ = "ExplanationOfBenefitAddItemDetail"

    adjudication: typing.List[fhirtypes.ExplanationOfBenefitItemAdjudicationType] | None = Field(  # type: ignore
        None,
        alias="adjudication",
        title="Added items adjudication",
        description="The adjudication results.",
        json_schema_extra={
            "element_property": True,
        },
    )

    factor: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="factor",
        title="Price scaling factor",
        description=(
            "A real number that represents a multiplier used in determining the "
            "overall value of services delivered and/or goods received. The concept"
            " of a Factor allows for a discount or surcharge multiplier to be "
            "applied to a monetary amount."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_factor", title="Extension field for ``factor``."
    )

    modifier: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="modifier",
        title="Service/Product billing modifiers",
        description=(
            "Item typification or modifiers codes to convey additional context for "
            "the product or service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    net: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="net",
        title="Total item cost",
        description=(
            "The total amount claimed for the group (if a grouper) or the "
            "addItem.detail. Net = unit price * quantity * factor."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    noteNumber: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="noteNumber",
        title="Applicable note numbers",
        description=(
            "The numbers associated with notes below which apply to the "
            "adjudication of this item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    noteNumber__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_noteNumber", title="Extension field for ``noteNumber``."
    )

    patientPaid: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="patientPaid",
        title="Paid by the patient",
        description=(
            "The amount paid by the patient, in total at the claim claim level or "
            "specifically for the item and detail level, to the provider for goods "
            "and services."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    productOrService: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="productOrService",
        title="Billing, service, product, or drug code",
        description=(
            "When the value is a group code then this item collects a set of "
            "related item details, otherwise this contains the product, service, "
            "drug or other billing code for the item. This element may be the start"
            " of a range of .productOrService codes used in conjunction with "
            ".productOrServiceEnd or it may be a solo element where "
            ".productOrServiceEnd is not used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    productOrServiceEnd: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="productOrServiceEnd",
        title="End of a range of codes",
        description=(
            "This contains the end of a range of product, service, drug or other "
            "billing codes for the item. This element is not used when the "
            ".productOrService is a group code. This value may only be present when"
            " a .productOfService code has been provided to convey the start of the"
            " range. Typically this value may be used only with preauthorizations "
            "and not with claims."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="Count of products or services",
        description="The number of repetitions of a service or product.",
        json_schema_extra={
            "element_property": True,
        },
    )

    revenue: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="revenue",
        title="Revenue or cost center code",
        description=(
            "The type of revenue or cost center providing the product and/or "
            "service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reviewOutcome: fhirtypes.ExplanationOfBenefitItemReviewOutcomeType | None = Field(  # type: ignore
        None,
        alias="reviewOutcome",
        title="Additem detail level adjudication results",
        description=(
            "The high-level results of the adjudication if adjudication has been "
            "performed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    subDetail: typing.List[fhirtypes.ExplanationOfBenefitAddItemDetailSubDetailType] | None = Field(  # type: ignore
        None,
        alias="subDetail",
        title="Insurer added line items",
        description="The third-tier service adjudications for payor added services.",
        json_schema_extra={
            "element_property": True,
        },
    )

    tax: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="tax",
        title="Total tax",
        description="The total of taxes applicable for this product or service.",
        json_schema_extra={
            "element_property": True,
        },
    )

    traceNumber: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="traceNumber",
        title="Number for tracking",
        description=(
            "Trace number for tracking purposes. May be defined at the jurisdiction"
            " level or between trading partners."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    unitPrice: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="unitPrice",
        title="Fee, charge or cost per item",
        description=(
            "If the item is not a group then this is the fee for the product or "
            "service, otherwise this is the total of the fees for the details of "
            "the group."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitAddItemDetail`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "traceNumber",
            "revenue",
            "productOrService",
            "productOrServiceEnd",
            "modifier",
            "patientPaid",
            "quantity",
            "unitPrice",
            "factor",
            "tax",
            "net",
            "noteNumber",
            "reviewOutcome",
            "adjudication",
            "subDetail",
        ]


class ExplanationOfBenefitAddItemDetailSubDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Insurer added line items.
    The third-tier service adjudications for payor added services.
    """

    __resource_type__ = "ExplanationOfBenefitAddItemDetailSubDetail"

    adjudication: typing.List[fhirtypes.ExplanationOfBenefitItemAdjudicationType] | None = Field(  # type: ignore
        None,
        alias="adjudication",
        title="Added items adjudication",
        description="The adjudication results.",
        json_schema_extra={
            "element_property": True,
        },
    )

    factor: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="factor",
        title="Price scaling factor",
        description=(
            "A real number that represents a multiplier used in determining the "
            "overall value of services delivered and/or goods received. The concept"
            " of a Factor allows for a discount or surcharge multiplier to be "
            "applied to a monetary amount."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_factor", title="Extension field for ``factor``."
    )

    modifier: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="modifier",
        title="Service/Product billing modifiers",
        description=(
            "Item typification or modifiers codes to convey additional context for "
            "the product or service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    net: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="net",
        title="Total item cost",
        description=(
            "The total amount claimed for the addItem.detail.subDetail. Net = unit "
            "price * quantity * factor."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    noteNumber: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="noteNumber",
        title="Applicable note numbers",
        description=(
            "The numbers associated with notes below which apply to the "
            "adjudication of this item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    noteNumber__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_noteNumber", title="Extension field for ``noteNumber``."
    )

    patientPaid: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="patientPaid",
        title="Paid by the patient",
        description=(
            "The amount paid by the patient, in total at the claim claim level or "
            "specifically for the item and detail level, to the provider for goods "
            "and services."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    productOrService: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="productOrService",
        title="Billing, service, product, or drug code",
        description=(
            "When the value is a group code then this item collects a set of "
            "related item details, otherwise this contains the product, service, "
            "drug or other billing code for the item. This element may be the start"
            " of a range of .productOrService codes used in conjunction with "
            ".productOrServiceEnd or it may be a solo element where "
            ".productOrServiceEnd is not used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    productOrServiceEnd: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="productOrServiceEnd",
        title="End of a range of codes",
        description=(
            "This contains the end of a range of product, service, drug or other "
            "billing codes for the item. This element is not used when the "
            ".productOrService is a group code. This value may only be present when"
            " a .productOfService code has been provided to convey the start of the"
            " range. Typically this value may be used only with preauthorizations "
            "and not with claims."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="Count of products or services",
        description="The number of repetitions of a service or product.",
        json_schema_extra={
            "element_property": True,
        },
    )

    revenue: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="revenue",
        title="Revenue or cost center code",
        description=(
            "The type of revenue or cost center providing the product and/or "
            "service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reviewOutcome: fhirtypes.ExplanationOfBenefitItemReviewOutcomeType | None = Field(  # type: ignore
        None,
        alias="reviewOutcome",
        title="Additem subdetail level adjudication results",
        description=(
            "The high-level results of the adjudication if adjudication has been "
            "performed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    tax: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="tax",
        title="Total tax",
        description="The total of taxes applicable for this product or service.",
        json_schema_extra={
            "element_property": True,
        },
    )

    traceNumber: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="traceNumber",
        title="Number for tracking",
        description=(
            "Trace number for tracking purposes. May be defined at the jurisdiction"
            " level or between trading partners."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    unitPrice: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="unitPrice",
        title="Fee, charge or cost per item",
        description=(
            "If the item is not a group then this is the fee for the product or "
            "service, otherwise this is the total of the fees for the details of "
            "the group."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitAddItemDetailSubDetail`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "traceNumber",
            "revenue",
            "productOrService",
            "productOrServiceEnd",
            "modifier",
            "patientPaid",
            "quantity",
            "unitPrice",
            "factor",
            "tax",
            "net",
            "noteNumber",
            "reviewOutcome",
            "adjudication",
        ]


class ExplanationOfBenefitBenefitBalance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Balance by Benefit Category.
    """

    __resource_type__ = "ExplanationOfBenefitBenefitBalance"

    category: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="category",
        title="Benefit classification",
        description=(
            "Code to identify the general type of benefits under which products and"
            " services are provided."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    description: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Description of the benefit or services covered",
        description="A richer description of the benefit or services covered.",
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    excluded: bool | None = Field(  # type: ignore
        None,
        alias="excluded",
        title="Excluded from the plan",
        description=(
            "True if the indicated class of service is excluded from the plan, "
            "missing or False indicates the product or service is included in the "
            "coverage."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    excluded__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_excluded", title="Extension field for ``excluded``."
    )

    financial: typing.List[fhirtypes.ExplanationOfBenefitBenefitBalanceFinancialType] | None = Field(  # type: ignore
        None,
        alias="financial",
        title="Benefit Summary",
        description="Benefits Used to date.",
        json_schema_extra={
            "element_property": True,
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Short name for the benefit",
        description="A short name or tag for the benefit.",
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    network: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="network",
        title="In or out of network",
        description=(
            "Is a flag to indicate whether the benefits refer to in-network "
            "providers or out-of-network providers."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    term: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="term",
        title="Annual or lifetime",
        description=(
            "The term or period of the values such as 'maximum lifetime benefit' or"
            " 'maximum annual visits'."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    unit: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="unit",
        title="Individual or family",
        description="Indicates if the benefits apply to an individual or to the family.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitBenefitBalance`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "category",
            "excluded",
            "name",
            "description",
            "network",
            "unit",
            "term",
            "financial",
        ]


class ExplanationOfBenefitBenefitBalanceFinancial(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Benefit Summary.
    Benefits Used to date.
    """

    __resource_type__ = "ExplanationOfBenefitBenefitBalanceFinancial"

    allowedMoney: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="allowedMoney",
        title="Benefits allowed",
        description="The quantity of the benefit which is permitted under the coverage.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e allowed[x]
            "one_of_many": "allowed",
            "one_of_many_required": False,
        },
    )

    allowedString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="allowedString",
        title="Benefits allowed",
        description="The quantity of the benefit which is permitted under the coverage.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e allowed[x]
            "one_of_many": "allowed",
            "one_of_many_required": False,
        },
    )
    allowedString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_allowedString", title="Extension field for ``allowedString``."
    )

    allowedUnsignedInt: fhirtypes.UnsignedIntType | None = Field(  # type: ignore
        None,
        alias="allowedUnsignedInt",
        title="Benefits allowed",
        description="The quantity of the benefit which is permitted under the coverage.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e allowed[x]
            "one_of_many": "allowed",
            "one_of_many_required": False,
        },
    )
    allowedUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_allowedUnsignedInt",
        title="Extension field for ``allowedUnsignedInt``.",
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Benefit classification",
        description="Classification of benefit being provided.",
        json_schema_extra={
            "element_property": True,
        },
    )

    usedMoney: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="usedMoney",
        title="Benefits used",
        description="The quantity of the benefit which have been consumed to date.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e used[x]
            "one_of_many": "used",
            "one_of_many_required": False,
        },
    )

    usedUnsignedInt: fhirtypes.UnsignedIntType | None = Field(  # type: ignore
        None,
        alias="usedUnsignedInt",
        title="Benefits used",
        description="The quantity of the benefit which have been consumed to date.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e used[x]
            "one_of_many": "used",
            "one_of_many_required": False,
        },
    )
    usedUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_usedUnsignedInt", title="Extension field for ``usedUnsignedInt``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitBenefitBalanceFinancial`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "allowedUnsignedInt",
            "allowedString",
            "allowedMoney",
            "usedUnsignedInt",
            "usedMoney",
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
            "allowed": ["allowedMoney", "allowedString", "allowedUnsignedInt"],
            "used": ["usedMoney", "usedUnsignedInt"],
        }
        return one_of_many_fields


class ExplanationOfBenefitCareTeam(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Care Team members.
    The members of the team who provided the products and services.
    """

    __resource_type__ = "ExplanationOfBenefitCareTeam"

    provider: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="provider",
        title="Practitioner or organization",
        description="Member of the team who provided the product or service.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
            ],
        },
    )

    responsible: bool | None = Field(  # type: ignore
        None,
        alias="responsible",
        title="Indicator of the lead practitioner",
        description=(
            "The party who is billing and/or responsible for the claimed products "
            "or services."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    responsible__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_responsible", title="Extension field for ``responsible``."
    )

    role: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="role",
        title="Function within the team",
        description=(
            "The lead, assisting or supervising practitioner and their discipline "
            "if a multidisciplinary team."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    sequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="sequence",
        title="Order of care team",
        description="A number to uniquely identify care team entries.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    specialty: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="specialty",
        title="Practitioner or provider specialization",
        description=(
            "The specialization of the practitioner or provider which is applicable"
            " for this service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitCareTeam`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "provider",
            "responsible",
            "role",
            "specialty",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sequence", "sequence__ext")]
        return required_fields


class ExplanationOfBenefitDiagnosis(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Pertinent diagnosis information.
    Information about diagnoses relevant to the claim items.
    """

    __resource_type__ = "ExplanationOfBenefitDiagnosis"

    diagnosisCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="diagnosisCodeableConcept",
        title="Nature of illness or problem",
        description=(
            "The nature of illness or problem in a coded form or as a reference to "
            "an external defined Condition."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e diagnosis[x]
            "one_of_many": "diagnosis",
            "one_of_many_required": True,
        },
    )

    diagnosisReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="diagnosisReference",
        title="Nature of illness or problem",
        description=(
            "The nature of illness or problem in a coded form or as a reference to "
            "an external defined Condition."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e diagnosis[x]
            "one_of_many": "diagnosis",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Condition"],
        },
    )

    onAdmission: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="onAdmission",
        title="Present on admission",
        description=(
            "Indication of whether the diagnosis was present on admission to a "
            "facility."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    sequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="sequence",
        title="Diagnosis instance identifier",
        description="A number to uniquely identify diagnosis entries.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    type: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="type",
        title="Timing or nature of the diagnosis",
        description="When the condition was observed or the relative ranking.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitDiagnosis`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "diagnosisCodeableConcept",
            "diagnosisReference",
            "type",
            "onAdmission",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sequence", "sequence__ext")]
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
            "diagnosis": ["diagnosisCodeableConcept", "diagnosisReference"]
        }
        return one_of_many_fields


class ExplanationOfBenefitEvent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Event information.
    Information code for an event with a corresponding date or period.
    """

    __resource_type__ = "ExplanationOfBenefitEvent"

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Specific event",
        description="A coded event such as when a service is expected or a card printed.",
        json_schema_extra={
            "element_property": True,
        },
    )

    whenDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="whenDateTime",
        title="Occurance date or period",
        description=(
            "A date or period in the past or future indicating when the event "
            "occurred or is expectd to occur."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e when[x]
            "one_of_many": "when",
            "one_of_many_required": True,
        },
    )
    whenDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_whenDateTime", title="Extension field for ``whenDateTime``."
    )

    whenPeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="whenPeriod",
        title="Occurance date or period",
        description=(
            "A date or period in the past or future indicating when the event "
            "occurred or is expectd to occur."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e when[x]
            "one_of_many": "when",
            "one_of_many_required": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitEvent`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "whenDateTime",
            "whenPeriod",
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
        one_of_many_fields = {"when": ["whenDateTime", "whenPeriod"]}
        return one_of_many_fields


class ExplanationOfBenefitInsurance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Patient insurance information.
    Financial instruments for reimbursement for the health care products and
    services specified on the claim.
    """

    __resource_type__ = "ExplanationOfBenefitInsurance"

    coverage: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="coverage",
        title="Insurance information",
        description=(
            "Reference to the insurance card level information contained in the "
            "Coverage resource. The coverage issuing insurer will use these details"
            " to locate the patient's actual coverage within the insurer's "
            "information system."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Coverage"],
        },
    )

    focal: bool | None = Field(  # type: ignore
        None,
        alias="focal",
        title="Coverage to be used for adjudication",
        description=(
            "A flag to indicate that this Coverage is to be used for adjudication "
            "of this claim when set to true."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    focal__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_focal", title="Extension field for ``focal``."
    )

    preAuthRef: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="preAuthRef",
        title="Prior authorization reference number",
        description=(
            "Reference numbers previously provided by the insurer to the provider "
            "to be quoted on subsequent claims containing services or products "
            "related to the prior authorization."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    preAuthRef__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_preAuthRef", title="Extension field for ``preAuthRef``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitInsurance`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "focal",
            "coverage",
            "preAuthRef",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("focal", "focal__ext")]
        return required_fields


class ExplanationOfBenefitItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Product or service provided.
    A claim line. Either a simple (a product or service) or a 'group' of
    details which can also be a simple items or groups of sub-details.
    """

    __resource_type__ = "ExplanationOfBenefitItem"

    adjudication: typing.List[fhirtypes.ExplanationOfBenefitItemAdjudicationType] | None = Field(  # type: ignore
        None,
        alias="adjudication",
        title="Adjudication details",
        description=(
            "If this item is a group then the values here are a summary of the "
            "adjudication of the detail items. If this item is a simple product or "
            "service then this is the result of the adjudication of this item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    bodySite: typing.List[fhirtypes.ExplanationOfBenefitItemBodySiteType] | None = Field(  # type: ignore
        None,
        alias="bodySite",
        title="Anatomical location",
        description="Physical location where the service is performed or applies.",
        json_schema_extra={
            "element_property": True,
        },
    )

    careTeamSequence: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="careTeamSequence",
        title="Applicable care team members",
        description="Care team members related to this service or product.",
        json_schema_extra={
            "element_property": True,
        },
    )
    careTeamSequence__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_careTeamSequence",
        title="Extension field for ``careTeamSequence``.",
    )

    category: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="category",
        title="Benefit classification",
        description=(
            "Code to identify the general type of benefits under which products and"
            " services are provided."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    detail: typing.List[fhirtypes.ExplanationOfBenefitItemDetailType] | None = Field(  # type: ignore
        None,
        alias="detail",
        title="Additional items",
        description="Second-tier of goods and services.",
        json_schema_extra={
            "element_property": True,
        },
    )

    diagnosisSequence: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="diagnosisSequence",
        title="Applicable diagnoses",
        description="Diagnoses applicable for this service or product.",
        json_schema_extra={
            "element_property": True,
        },
    )
    diagnosisSequence__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_diagnosisSequence",
        title="Extension field for ``diagnosisSequence``.",
    )

    encounter: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="encounter",
        title="Encounters associated with the listed treatments",
        description="Healthcare encounters related to this claim.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter"],
        },
    )

    factor: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="factor",
        title="Price scaling factor",
        description=(
            "A real number that represents a multiplier used in determining the "
            "overall value of services delivered and/or goods received. The concept"
            " of a Factor allows for a discount or surcharge multiplier to be "
            "applied to a monetary amount."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_factor", title="Extension field for ``factor``."
    )

    informationSequence: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="informationSequence",
        title="Applicable exception and supporting information",
        description=(
            "Exceptions, special conditions and supporting information applicable "
            "for this service or product."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    informationSequence__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_informationSequence",
        title="Extension field for ``informationSequence``.",
    )

    locationAddress: fhirtypes.AddressType | None = Field(  # type: ignore
        None,
        alias="locationAddress",
        title="Place of service or where product was supplied",
        description="Where the product or service was provided.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e location[x]
            "one_of_many": "location",
            "one_of_many_required": False,
        },
    )

    locationCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="locationCodeableConcept",
        title="Place of service or where product was supplied",
        description="Where the product or service was provided.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e location[x]
            "one_of_many": "location",
            "one_of_many_required": False,
        },
    )

    locationReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="locationReference",
        title="Place of service or where product was supplied",
        description="Where the product or service was provided.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e location[x]
            "one_of_many": "location",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    modifier: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="modifier",
        title="Product or service billing modifiers",
        description=(
            "Item typification or modifiers codes to convey additional context for "
            "the product or service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    net: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="net",
        title="Total item cost",
        description=(
            "The total amount claimed for the group (if a grouper) or the line "
            "item. Net = unit price * quantity * factor."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    noteNumber: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="noteNumber",
        title="Applicable note numbers",
        description=(
            "The numbers associated with notes below which apply to the "
            "adjudication of this item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    noteNumber__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_noteNumber", title="Extension field for ``noteNumber``."
    )

    patientPaid: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="patientPaid",
        title="Paid by the patient",
        description=(
            "The amount paid by the patient, in total at the claim claim level or "
            "specifically for the item and detail level, to the provider for goods "
            "and services."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    procedureSequence: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="procedureSequence",
        title="Applicable procedures",
        description="Procedures applicable for this service or product.",
        json_schema_extra={
            "element_property": True,
        },
    )
    procedureSequence__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_procedureSequence",
        title="Extension field for ``procedureSequence``.",
    )

    productOrService: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="productOrService",
        title="Billing, service, product, or drug code",
        description=(
            "When the value is a group code then this item collects a set of "
            "related item details, otherwise this contains the product, service, "
            "drug or other billing code for the item. This element may be the start"
            " of a range of .productOrService codes used in conjunction with "
            ".productOrServiceEnd or it may be a solo element where "
            ".productOrServiceEnd is not used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    productOrServiceEnd: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="productOrServiceEnd",
        title="End of a range of codes",
        description=(
            "This contains the end of a range of product, service, drug or other "
            "billing codes for the item. This element is not used when the "
            ".productOrService is a group code. This value may only be present when"
            " a .productOfService code has been provided to convey the start of the"
            " range. Typically this value may be used only with preauthorizations "
            "and not with claims."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    programCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="programCode",
        title="Program the product or service is provided under",
        description="Identifies the program under which this may be recovered.",
        json_schema_extra={
            "element_property": True,
        },
    )

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="Count of products or services",
        description="The number of repetitions of a service or product.",
        json_schema_extra={
            "element_property": True,
        },
    )

    request: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="request",
        title="Request or Referral for Service",
        description="Request or Referral for Goods or Service to be rendered.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "DeviceRequest",
                "MedicationRequest",
                "NutritionOrder",
                "ServiceRequest",
                "SupplyRequest",
                "VisionPrescription",
            ],
        },
    )

    revenue: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="revenue",
        title="Revenue or cost center code",
        description=(
            "The type of revenue or cost center providing the product and/or "
            "service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reviewOutcome: fhirtypes.ExplanationOfBenefitItemReviewOutcomeType | None = Field(  # type: ignore
        None,
        alias="reviewOutcome",
        title="Adjudication results",
        description=(
            "The high-level results of the adjudication if adjudication has been "
            "performed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    sequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="sequence",
        title="Item instance identifier",
        description="A number to uniquely identify item entries.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    servicedDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="servicedDate",
        title="Date or dates of service or product delivery",
        description=(
            "The date or dates when the service or product was supplied, performed "
            "or completed."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e serviced[x]
            "one_of_many": "serviced",
            "one_of_many_required": False,
        },
    )
    servicedDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_servicedDate", title="Extension field for ``servicedDate``."
    )

    servicedPeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="servicedPeriod",
        title="Date or dates of service or product delivery",
        description=(
            "The date or dates when the service or product was supplied, performed "
            "or completed."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e serviced[x]
            "one_of_many": "serviced",
            "one_of_many_required": False,
        },
    )

    tax: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="tax",
        title="Total tax",
        description="The total of taxes applicable for this product or service.",
        json_schema_extra={
            "element_property": True,
        },
    )

    traceNumber: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="traceNumber",
        title="Number for tracking",
        description=(
            "Trace number for tracking purposes. May be defined at the jurisdiction"
            " level or between trading partners."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    udi: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="udi",
        title="Unique device identifier",
        description="Unique Device Identifiers associated with this line item.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Device"],
        },
    )

    unitPrice: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="unitPrice",
        title="Fee, charge or cost per item",
        description=(
            "If the item is not a group then this is the fee for the product or "
            "service, otherwise this is the total of the fees for the details of "
            "the group."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitItem`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "careTeamSequence",
            "diagnosisSequence",
            "procedureSequence",
            "informationSequence",
            "traceNumber",
            "revenue",
            "category",
            "productOrService",
            "productOrServiceEnd",
            "request",
            "modifier",
            "programCode",
            "servicedDate",
            "servicedPeriod",
            "locationCodeableConcept",
            "locationAddress",
            "locationReference",
            "patientPaid",
            "quantity",
            "unitPrice",
            "factor",
            "tax",
            "net",
            "udi",
            "bodySite",
            "encounter",
            "noteNumber",
            "reviewOutcome",
            "adjudication",
            "detail",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sequence", "sequence__ext")]
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
            "location": [
                "locationAddress",
                "locationCodeableConcept",
                "locationReference",
            ],
            "serviced": ["servicedDate", "servicedPeriod"],
        }
        return one_of_many_fields


class ExplanationOfBenefitItemAdjudication(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Adjudication details.
    If this item is a group then the values here are a summary of the
    adjudication of the detail items. If this item is a simple product or
    service then this is the result of the adjudication of this item.
    """

    __resource_type__ = "ExplanationOfBenefitItemAdjudication"

    amount: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="amount",
        title="Monetary amount",
        description="Monetary amount associated with the category.",
        json_schema_extra={
            "element_property": True,
        },
    )

    category: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="category",
        title="Type of adjudication information",
        description=(
            "A code to indicate the information type of this adjudication record. "
            "Information types may include: the value submitted, maximum values or "
            "percentages allowed or payable under the plan, amounts that the "
            "patient is responsible for in-aggregate or pertaining to this item, "
            "amounts paid by other coverages, and the benefit payable for this "
            "item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="Non-monitary value",
        description=(
            "A non-monetary value associated with the category. Mutually exclusive "
            "to the amount element above."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reason: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="reason",
        title="Explanation of adjudication outcome",
        description=(
            "A code supporting the understanding of the adjudication result and "
            "explaining variance from expected amount."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitItemAdjudication`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "category",
            "reason",
            "amount",
            "quantity",
        ]


class ExplanationOfBenefitItemBodySite(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Anatomical location.
    Physical location where the service is performed or applies.
    """

    __resource_type__ = "ExplanationOfBenefitItemBodySite"

    site: typing.List[fhirtypes.CodeableReferenceType] = Field(  # type: ignore
        ...,
        alias="site",
        title="Location",
        description="Physical service site on the patient (limb, tooth, etc.).",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["BodyStructure"],
        },
    )

    subSite: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="subSite",
        title="Sub-location",
        description=(
            "A region or surface of the bodySite, e.g. limb region or tooth "
            "surface(s)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitItemBodySite`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "site", "subSite"]


class ExplanationOfBenefitItemDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional items.
    Second-tier of goods and services.
    """

    __resource_type__ = "ExplanationOfBenefitItemDetail"

    adjudication: typing.List[fhirtypes.ExplanationOfBenefitItemAdjudicationType] | None = Field(  # type: ignore
        None,
        alias="adjudication",
        title="Detail level adjudication details",
        description="The adjudication results.",
        json_schema_extra={
            "element_property": True,
        },
    )

    category: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="category",
        title="Benefit classification",
        description=(
            "Code to identify the general type of benefits under which products and"
            " services are provided."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    factor: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="factor",
        title="Price scaling factor",
        description=(
            "A real number that represents a multiplier used in determining the "
            "overall value of services delivered and/or goods received. The concept"
            " of a Factor allows for a discount or surcharge multiplier to be "
            "applied to a monetary amount."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_factor", title="Extension field for ``factor``."
    )

    modifier: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="modifier",
        title="Service/Product billing modifiers",
        description=(
            "Item typification or modifiers codes to convey additional context for "
            "the product or service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    net: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="net",
        title="Total item cost",
        description=(
            "The total amount claimed for the group (if a grouper) or the line "
            "item.detail. Net = unit price * quantity * factor."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    noteNumber: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="noteNumber",
        title="Applicable note numbers",
        description=(
            "The numbers associated with notes below which apply to the "
            "adjudication of this item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    noteNumber__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_noteNumber", title="Extension field for ``noteNumber``."
    )

    patientPaid: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="patientPaid",
        title="Paid by the patient",
        description=(
            "The amount paid by the patient, in total at the claim claim level or "
            "specifically for the item and detail level, to the provider for goods "
            "and services."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    productOrService: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="productOrService",
        title="Billing, service, product, or drug code",
        description=(
            "When the value is a group code then this item collects a set of "
            "related item details, otherwise this contains the product, service, "
            "drug or other billing code for the item. This element may be the start"
            " of a range of .productOrService codes used in conjunction with "
            ".productOrServiceEnd or it may be a solo element where "
            ".productOrServiceEnd is not used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    productOrServiceEnd: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="productOrServiceEnd",
        title="End of a range of codes",
        description=(
            "This contains the end of a range of product, service, drug or other "
            "billing codes for the item. This element is not used when the "
            ".productOrService is a group code. This value may only be present when"
            " a .productOfService code has been provided to convey the start of the"
            " range. Typically this value may be used only with preauthorizations "
            "and not with claims."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    programCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="programCode",
        title="Program the product or service is provided under",
        description="Identifies the program under which this may be recovered.",
        json_schema_extra={
            "element_property": True,
        },
    )

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="Count of products or services",
        description="The number of repetitions of a service or product.",
        json_schema_extra={
            "element_property": True,
        },
    )

    revenue: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="revenue",
        title="Revenue or cost center code",
        description=(
            "The type of revenue or cost center providing the product and/or "
            "service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reviewOutcome: fhirtypes.ExplanationOfBenefitItemReviewOutcomeType | None = Field(  # type: ignore
        None,
        alias="reviewOutcome",
        title="Detail level adjudication results",
        description=(
            "The high-level results of the adjudication if adjudication has been "
            "performed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    sequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="sequence",
        title="Product or service provided",
        description=(
            "A claim detail line. Either a simple (a product or service) or a "
            "'group' of sub-details which are simple items."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    subDetail: typing.List[fhirtypes.ExplanationOfBenefitItemDetailSubDetailType] | None = Field(  # type: ignore
        None,
        alias="subDetail",
        title="Additional items",
        description="Third-tier of goods and services.",
        json_schema_extra={
            "element_property": True,
        },
    )

    tax: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="tax",
        title="Total tax",
        description="The total of taxes applicable for this product or service.",
        json_schema_extra={
            "element_property": True,
        },
    )

    traceNumber: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="traceNumber",
        title="Number for tracking",
        description=(
            "Trace number for tracking purposes. May be defined at the jurisdiction"
            " level or between trading partners."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    udi: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="udi",
        title="Unique device identifier",
        description="Unique Device Identifiers associated with this line item.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Device"],
        },
    )

    unitPrice: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="unitPrice",
        title="Fee, charge or cost per item",
        description=(
            "If the item is not a group then this is the fee for the product or "
            "service, otherwise this is the total of the fees for the details of "
            "the group."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitItemDetail`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "traceNumber",
            "revenue",
            "category",
            "productOrService",
            "productOrServiceEnd",
            "modifier",
            "programCode",
            "patientPaid",
            "quantity",
            "unitPrice",
            "factor",
            "tax",
            "net",
            "udi",
            "noteNumber",
            "reviewOutcome",
            "adjudication",
            "subDetail",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sequence", "sequence__ext")]
        return required_fields


class ExplanationOfBenefitItemDetailSubDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional items.
    Third-tier of goods and services.
    """

    __resource_type__ = "ExplanationOfBenefitItemDetailSubDetail"

    adjudication: typing.List[fhirtypes.ExplanationOfBenefitItemAdjudicationType] | None = Field(  # type: ignore
        None,
        alias="adjudication",
        title="Subdetail level adjudication details",
        description="The adjudication results.",
        json_schema_extra={
            "element_property": True,
        },
    )

    category: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="category",
        title="Benefit classification",
        description=(
            "Code to identify the general type of benefits under which products and"
            " services are provided."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    factor: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="factor",
        title="Price scaling factor",
        description=(
            "A real number that represents a multiplier used in determining the "
            "overall value of services delivered and/or goods received. The concept"
            " of a Factor allows for a discount or surcharge multiplier to be "
            "applied to a monetary amount."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_factor", title="Extension field for ``factor``."
    )

    modifier: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="modifier",
        title="Service/Product billing modifiers",
        description=(
            "Item typification or modifiers codes to convey additional context for "
            "the product or service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    net: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="net",
        title="Total item cost",
        description=(
            "The total amount claimed for the line item.detail.subDetail. Net = "
            "unit price * quantity * factor."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    noteNumber: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="noteNumber",
        title="Applicable note numbers",
        description=(
            "The numbers associated with notes below which apply to the "
            "adjudication of this item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    noteNumber__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_noteNumber", title="Extension field for ``noteNumber``."
    )

    patientPaid: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="patientPaid",
        title="Paid by the patient",
        description=(
            "The amount paid by the patient, in total at the claim claim level or "
            "specifically for the item and detail level, to the provider for goods "
            "and services."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    productOrService: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="productOrService",
        title="Billing, service, product, or drug code",
        description=(
            "When the value is a group code then this item collects a set of "
            "related item details, otherwise this contains the product, service, "
            "drug or other billing code for the item. This element may be the start"
            " of a range of .productOrService codes used in conjunction with "
            ".productOrServiceEnd or it may be a solo element where "
            ".productOrServiceEnd is not used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    productOrServiceEnd: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="productOrServiceEnd",
        title="End of a range of codes",
        description=(
            "This contains the end of a range of product, service, drug or other "
            "billing codes for the item. This element is not used when the "
            ".productOrService is a group code. This value may only be present when"
            " a .productOfService code has been provided to convey the start of the"
            " range. Typically this value may be used only with preauthorizations "
            "and not with claims."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    programCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="programCode",
        title="Program the product or service is provided under",
        description="Identifies the program under which this may be recovered.",
        json_schema_extra={
            "element_property": True,
        },
    )

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="Count of products or services",
        description="The number of repetitions of a service or product.",
        json_schema_extra={
            "element_property": True,
        },
    )

    revenue: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="revenue",
        title="Revenue or cost center code",
        description=(
            "The type of revenue or cost center providing the product and/or "
            "service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reviewOutcome: fhirtypes.ExplanationOfBenefitItemReviewOutcomeType | None = Field(  # type: ignore
        None,
        alias="reviewOutcome",
        title="Subdetail level adjudication results",
        description=(
            "The high-level results of the adjudication if adjudication has been "
            "performed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    sequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="sequence",
        title="Product or service provided",
        description=(
            "A claim detail line. Either a simple (a product or service) or a "
            "'group' of sub-details which are simple items."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    tax: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="tax",
        title="Total tax",
        description="The total of taxes applicable for this product or service.",
        json_schema_extra={
            "element_property": True,
        },
    )

    traceNumber: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="traceNumber",
        title="Number for tracking",
        description=(
            "Trace number for tracking purposes. May be defined at the jurisdiction"
            " level or between trading partners."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    udi: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="udi",
        title="Unique device identifier",
        description="Unique Device Identifiers associated with this line item.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Device"],
        },
    )

    unitPrice: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="unitPrice",
        title="Fee, charge or cost per item",
        description=(
            "If the item is not a group then this is the fee for the product or "
            "service, otherwise this is the total of the fees for the details of "
            "the group."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitItemDetailSubDetail`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "traceNumber",
            "revenue",
            "category",
            "productOrService",
            "productOrServiceEnd",
            "modifier",
            "programCode",
            "patientPaid",
            "quantity",
            "unitPrice",
            "factor",
            "tax",
            "net",
            "udi",
            "noteNumber",
            "reviewOutcome",
            "adjudication",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sequence", "sequence__ext")]
        return required_fields


class ExplanationOfBenefitItemReviewOutcome(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Adjudication results.
    The high-level results of the adjudication if adjudication has been
    performed.
    """

    __resource_type__ = "ExplanationOfBenefitItemReviewOutcome"

    decision: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="decision",
        title="Result of the adjudication",
        description=(
            "The result of the claim, predetermination, or preauthorization "
            "adjudication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    preAuthPeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="preAuthPeriod",
        title="Preauthorization reference effective period",
        description="The time frame during which this authorization is effective.",
        json_schema_extra={
            "element_property": True,
        },
    )

    preAuthRef: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="preAuthRef",
        title="Preauthorization reference",
        description=(
            "Reference from the Insurer which is used in later communications which"
            " refers to this adjudication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    preAuthRef__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_preAuthRef", title="Extension field for ``preAuthRef``."
    )

    reason: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="reason",
        title="Reason for result of the adjudication",
        description=(
            "The reasons for the result of the claim, predetermination, or "
            "preauthorization adjudication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitItemReviewOutcome`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "decision",
            "reason",
            "preAuthRef",
            "preAuthPeriod",
        ]


class ExplanationOfBenefitPayee(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Recipient of benefits payable.
    The party to be reimbursed for cost of the products and services according
    to the terms of the policy.
    """

    __resource_type__ = "ExplanationOfBenefitPayee"

    party: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="party",
        title="Recipient reference",
        description=(
            "Reference to the individual or organization to whom any payment will "
            "be made."
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
            ],
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Category of recipient",
        description="Type of Party to be reimbursed: Subscriber, provider, other.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitPayee`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "party"]


class ExplanationOfBenefitPayment(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Payment Details.
    Payment details for the adjudication of the claim.
    """

    __resource_type__ = "ExplanationOfBenefitPayment"

    adjustment: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="adjustment",
        title="Payment adjustment for non-claim issues",
        description=(
            "Total amount of all adjustments to this payment included in this "
            "transaction which are not related to this claim's adjudication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    adjustmentReason: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="adjustmentReason",
        title="Explanation for the variance",
        description="Reason for the payment adjustment.",
        json_schema_extra={
            "element_property": True,
        },
    )

    amount: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="amount",
        title="Payable amount after adjustment",
        description="Benefits payable less any payment adjustment.",
        json_schema_extra={
            "element_property": True,
        },
    )

    date: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="date",
        title="Expected date of payment",
        description=(
            "Estimated date the payment will be issued or the actual issue date of "
            "payment."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    identifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business identifier for the payment",
        description="Issuer's unique identifier for the payment instrument.",
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Partial or complete payment",
        description=(
            "Whether this represents partial or complete payment of the benefits "
            "payable."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitPayment`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "adjustment",
            "adjustmentReason",
            "date",
            "amount",
            "identifier",
        ]


class ExplanationOfBenefitProcedure(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Clinical procedures performed.
    Procedures performed on the patient relevant to the billing items with the
    claim.
    """

    __resource_type__ = "ExplanationOfBenefitProcedure"

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="date",
        title="When the procedure was performed",
        description="Date and optionally time the procedure was performed.",
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    procedureCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="procedureCodeableConcept",
        title="Specific clinical procedure",
        description=(
            "The code or reference to a Procedure resource which identifies the "
            "clinical intervention performed."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e procedure[x]
            "one_of_many": "procedure",
            "one_of_many_required": True,
        },
    )

    procedureReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="procedureReference",
        title="Specific clinical procedure",
        description=(
            "The code or reference to a Procedure resource which identifies the "
            "clinical intervention performed."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e procedure[x]
            "one_of_many": "procedure",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Procedure"],
        },
    )

    sequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="sequence",
        title="Procedure instance identifier",
        description="A number to uniquely identify procedure entries.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    type: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="type",
        title="Category of Procedure",
        description="When the condition was observed or the relative ranking.",
        json_schema_extra={
            "element_property": True,
        },
    )

    udi: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="udi",
        title="Unique device identifier",
        description="Unique Device Identifiers associated with this line item.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Device"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitProcedure`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "type",
            "date",
            "procedureCodeableConcept",
            "procedureReference",
            "udi",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sequence", "sequence__ext")]
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
            "procedure": ["procedureCodeableConcept", "procedureReference"]
        }
        return one_of_many_fields


class ExplanationOfBenefitProcessNote(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Note concerning adjudication.
    A note that describes or explains adjudication results in a human readable
    form.
    """

    __resource_type__ = "ExplanationOfBenefitProcessNote"

    language: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="language",
        title="Language of the text",
        description="A code to define the language used in the text of the note.",
        json_schema_extra={
            "element_property": True,
        },
    )

    number: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="number",
        title="Note instance identifier",
        description="A number to uniquely identify a note entry.",
        json_schema_extra={
            "element_property": True,
        },
    )
    number__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_number", title="Extension field for ``number``."
    )

    text: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="text",
        title="Note explanatory text",
        description="The explanation or description associated with the processing.",
        json_schema_extra={
            "element_property": True,
        },
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_text", title="Extension field for ``text``."
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Note purpose",
        description="The business purpose of the note text.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitProcessNote`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "number",
            "type",
            "text",
            "language",
        ]


class ExplanationOfBenefitRelated(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Prior or corollary claims.
    Other claims which are related to this claim such as prior submissions or
    claims for related services or for the same event.
    """

    __resource_type__ = "ExplanationOfBenefitRelated"

    claim: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="claim",
        title="Reference to the related claim",
        description="Reference to a related claim.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Claim"],
        },
    )

    reference: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="reference",
        title="File or case reference",
        description=(
            "An alternate organizational reference to the case or file to which "
            "this particular claim pertains."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    relationship: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="relationship",
        title="How the reference claim is related",
        description="A code to convey how the claims are related.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitRelated`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "claim",
            "relationship",
            "reference",
        ]


class ExplanationOfBenefitSupportingInfo(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Supporting information.
    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues.
    """

    __resource_type__ = "ExplanationOfBenefitSupportingInfo"

    category: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="category",
        title="Classification of the supplied information",
        description=(
            "The general class of the information supplied: information; exception;"
            " accident, employment; onset, etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Type of information",
        description=(
            "System and code pertaining to the specific information regarding "
            "special conditions relating to the setting, treatment or patient  for "
            "which care is sought."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reason: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="reason",
        title="Explanation for the information",
        description=(
            "Provides the reason in the situation where a reason code is required "
            "in addition to the content."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    sequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="sequence",
        title="Information instance identifier",
        description="A number to uniquely identify supporting information entries.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    timingDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="timingDate",
        title="When it occurred",
        description="The date when or period to which this information refers.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e timing[x]
            "one_of_many": "timing",
            "one_of_many_required": False,
        },
    )
    timingDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_timingDate", title="Extension field for ``timingDate``."
    )

    timingPeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="timingPeriod",
        title="When it occurred",
        description="The date when or period to which this information refers.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e timing[x]
            "one_of_many": "timing",
            "one_of_many_required": False,
        },
    )

    valueAttachment: fhirtypes.AttachmentType | None = Field(  # type: ignore
        None,
        alias="valueAttachment",
        title="Data to be provided",
        description=(
            "Additional data or information such as resources, documents, images "
            "etc. including references to the data or the actual inclusion of the "
            "data."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueBoolean: bool | None = Field(  # type: ignore
        None,
        alias="valueBoolean",
        title="Data to be provided",
        description=(
            "Additional data or information such as resources, documents, images "
            "etc. including references to the data or the actual inclusion of the "
            "data."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueIdentifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="valueIdentifier",
        title="Data to be provided",
        description=(
            "Additional data or information such as resources, documents, images "
            "etc. including references to the data or the actual inclusion of the "
            "data."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="valueQuantity",
        title="Data to be provided",
        description=(
            "Additional data or information such as resources, documents, images "
            "etc. including references to the data or the actual inclusion of the "
            "data."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="valueReference",
        title="Data to be provided",
        description=(
            "Additional data or information such as resources, documents, images "
            "etc. including references to the data or the actual inclusion of the "
            "data."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    valueString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="valueString",
        title="Data to be provided",
        description=(
            "Additional data or information such as resources, documents, images "
            "etc. including references to the data or the actual inclusion of the "
            "data."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitSupportingInfo`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "category",
            "code",
            "timingDate",
            "timingPeriod",
            "valueBoolean",
            "valueString",
            "valueQuantity",
            "valueAttachment",
            "valueReference",
            "valueIdentifier",
            "reason",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sequence", "sequence__ext")]
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
            "timing": ["timingDate", "timingPeriod"],
            "value": [
                "valueAttachment",
                "valueBoolean",
                "valueIdentifier",
                "valueQuantity",
                "valueReference",
                "valueString",
            ],
        }
        return one_of_many_fields


class ExplanationOfBenefitTotal(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Adjudication totals.
    Categorized monetary totals for the adjudication.
    """

    __resource_type__ = "ExplanationOfBenefitTotal"

    amount: fhirtypes.MoneyType = Field(  # type: ignore
        ...,
        alias="amount",
        title="Financial total for the category",
        description="Monetary total amount associated with the category.",
        json_schema_extra={
            "element_property": True,
        },
    )

    category: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="category",
        title="Type of adjudication information",
        description=(
            "A code to indicate the information type of this adjudication record. "
            "Information types may include: the value submitted, maximum values or "
            "percentages allowed or payable under the plan, amounts that the "
            "patient is responsible for in aggregate or pertaining to this item, "
            "amounts paid by other coverages, and the benefit payable for this "
            "item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitTotal`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "category", "amount"]
