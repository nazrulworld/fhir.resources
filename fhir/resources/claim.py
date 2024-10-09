from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Claim
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Claim(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Claim, Pre-determination or Pre-authorization.
    A provider issued list of professional services and products which have
    been provided, or are to be provided, to a patient which is sent to an
    insurer for reimbursement.
    """

    __resource_type__ = "Claim"

    accident: fhirtypes.ClaimAccidentType | None = Field(  # type: ignore
        None,
        alias="accident",
        title="Details of the event",
        description=(
            "Details of an accident which resulted in injuries which required the "
            "products and services listed in the claim."
        ),
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

    careTeam: typing.List[fhirtypes.ClaimCareTeamType] | None = Field(  # type: ignore
        None,
        alias="careTeam",
        title="Members of the care team",
        description="The members of the team who provided the products and services.",
        json_schema_extra={
            "element_property": True,
        },
    )

    created: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="created",
        title="Resource creation date",
        description="The date this resource was created.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_created", title="Extension field for ``created``."
    )

    diagnosis: typing.List[fhirtypes.ClaimDiagnosisType] | None = Field(  # type: ignore
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

    event: typing.List[fhirtypes.ClaimEventType] | None = Field(  # type: ignore
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
        title="Servicing facility",
        description="Facility where the services were provided.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location", "Organization"],
        },
    )

    fundsReserve: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="fundsReserve",
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
        title="Business Identifier for claim",
        description="A unique identifier assigned to this claim.",
        json_schema_extra={
            "element_property": True,
        },
    )

    insurance: typing.List[fhirtypes.ClaimInsuranceType] | None = Field(  # type: ignore
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
        title="Target",
        description="The Insurer who is target of the request.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    item: typing.List[fhirtypes.ClaimItemType] | None = Field(  # type: ignore
        None,
        alias="item",
        title="Product or service provided",
        description=(
            "A claim line. Either a simple  product or service or a 'group' of "
            "details which can each be a simple items or groups of sub-details."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    originalPrescription: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="originalPrescription",
        title="Original prescription if superseded by fulfiller",
        description=(
            "Original prescription which has been superseded by this prescription "
            "to support the dispensing of pharmacy services, medications or "
            "products."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "DeviceRequest",
                "MedicationRequest",
                "VisionPrescription",
            ],
        },
    )

    patient: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="patient",
        title="The recipient of the products and services",
        description=(
            "The party to whom the professional services and/or products have been "
            "supplied or are being considered and for whom actual or forecast "
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

    payee: fhirtypes.ClaimPayeeType | None = Field(  # type: ignore
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

    prescription: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="prescription",
        title="Prescription authorizing services and products",
        description=(
            "Prescription is the document/authorization given to the claim author "
            "for them to provide products and services for which consideration "
            "(reimbursement) is sought. Could be a RX for medications, an 'order' "
            "for oxygen or wheelchair or physiotherapy treatments."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "DeviceRequest",
                "MedicationRequest",
                "VisionPrescription",
            ],
        },
    )

    priority: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="priority",
        title="Desired processing urgency",
        description=(
            "The provider-required urgency of processing the request. Typical "
            "values include: stat, normal, deferred."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    procedure: typing.List[fhirtypes.ClaimProcedureType] | None = Field(  # type: ignore
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
        title="Treatment referral",
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

    related: typing.List[fhirtypes.ClaimRelatedType] | None = Field(  # type: ignore
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

    supportingInfo: typing.List[fhirtypes.ClaimSupportingInfoType] | None = Field(  # type: ignore
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

    total: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="total",
        title="Total claim cost",
        description="The total value of the all the items in the claim.",
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
        ``Claim`` according specification,
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
            "fundsReserve",
            "related",
            "prescription",
            "originalPrescription",
            "payee",
            "referral",
            "encounter",
            "facility",
            "diagnosisRelatedGroup",
            "event",
            "careTeam",
            "supportingInfo",
            "diagnosis",
            "procedure",
            "insurance",
            "accident",
            "patientPaid",
            "item",
            "total",
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
            ("status", "status__ext"),
            ("use", "use__ext"),
        ]
        return required_fields


class ClaimAccident(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details of the event.
    Details of an accident which resulted in injuries which required the
    products and services listed in the claim.
    """

    __resource_type__ = "ClaimAccident"

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
            "element_required": True,
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
        ``ClaimAccident`` according specification,
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

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("date", "date__ext")]
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
        one_of_many_fields = {"location": ["locationAddress", "locationReference"]}
        return one_of_many_fields


class ClaimCareTeam(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Members of the care team.
    The members of the team who provided the products and services.
    """

    __resource_type__ = "ClaimCareTeam"

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
        ``ClaimCareTeam`` according specification,
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


class ClaimDiagnosis(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Pertinent diagnosis information.
    Information about diagnoses relevant to the claim items.
    """

    __resource_type__ = "ClaimDiagnosis"

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
        ``ClaimDiagnosis`` according specification,
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


class ClaimEvent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Event information.
    Information code for an event with a corresponding date or period.
    """

    __resource_type__ = "ClaimEvent"

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
        ``ClaimEvent`` according specification,
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


class ClaimInsurance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Patient insurance information.
    Financial instruments for reimbursement for the health care products and
    services specified on the claim.
    """

    __resource_type__ = "ClaimInsurance"

    businessArrangement: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="businessArrangement",
        title="Additional provider contract number",
        description=(
            "A business agreement number established between the provider and the "
            "insurer for special business processing purposes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    businessArrangement__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_businessArrangement",
        title="Extension field for ``businessArrangement``.",
    )

    claimResponse: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="claimResponse",
        title="Adjudication results",
        description=(
            "The result of the adjudication of the line items for the Coverage "
            "specified in this insurance."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ClaimResponse"],
        },
    )

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

    identifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Pre-assigned Claim number",
        description=(
            "The business identifier to be used when the claim is sent for "
            "adjudication against this insurance policy."
        ),
        json_schema_extra={
            "element_property": True,
        },
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

    sequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="sequence",
        title="Insurance instance identifier",
        description=(
            "A number to uniquely identify insurance entries and provide a sequence"
            " of coverages to convey coordination of benefit order."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimInsurance`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "focal",
            "identifier",
            "coverage",
            "businessArrangement",
            "preAuthRef",
            "claimResponse",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("focal", "focal__ext"), ("sequence", "sequence__ext")]
        return required_fields


class ClaimItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Product or service provided.
    A claim line. Either a simple  product or service or a 'group' of details
    which can each be a simple items or groups of sub-details.
    """

    __resource_type__ = "ClaimItem"

    bodySite: typing.List[fhirtypes.ClaimItemBodySiteType] | None = Field(  # type: ignore
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
        title="Applicable careTeam members",
        description="CareTeam members related to this service or product.",
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

    detail: typing.List[fhirtypes.ClaimItemDetailType] | None = Field(  # type: ignore
        None,
        alias="detail",
        title="Product or service provided",
        description=(
            "A claim detail line. Either a simple (a product or service) or a "
            "'group' of sub-details which are simple items."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    diagnosisSequence: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="diagnosisSequence",
        title="Applicable diagnoses",
        description="Diagnosis applicable for this service or product.",
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
        ``ClaimItem`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "traceNumber",
            "careTeamSequence",
            "diagnosisSequence",
            "procedureSequence",
            "informationSequence",
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


class ClaimItemBodySite(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Anatomical location.
    Physical location where the service is performed or applies.
    """

    __resource_type__ = "ClaimItemBodySite"

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
        ``ClaimItemBodySite`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "site", "subSite"]


class ClaimItemDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Product or service provided.
    A claim detail line. Either a simple (a product or service) or a 'group' of
    sub-details which are simple items.
    """

    __resource_type__ = "ClaimItemDetail"

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

    subDetail: typing.List[fhirtypes.ClaimItemDetailSubDetailType] | None = Field(  # type: ignore
        None,
        alias="subDetail",
        title="Product or service provided",
        description=(
            "A claim detail line. Either a simple (a product or service) or a "
            "'group' of sub-details which are simple items."
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
        ``ClaimItemDetail`` according specification,
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


class ClaimItemDetailSubDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Product or service provided.
    A claim detail line. Either a simple (a product or service) or a 'group' of
    sub-details which are simple items.
    """

    __resource_type__ = "ClaimItemDetailSubDetail"

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
            "The total amount claimed for line item.detail.subDetail. Net = unit "
            "price * quantity * factor."
        ),
        json_schema_extra={
            "element_property": True,
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
        ``ClaimItemDetailSubDetail`` according specification,
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


class ClaimPayee(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Recipient of benefits payable.
    The party to be reimbursed for cost of the products and services according
    to the terms of the policy.
    """

    __resource_type__ = "ClaimPayee"

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

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Category of recipient",
        description="Type of Party to be reimbursed: subscriber, provider, other.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimPayee`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "party"]


class ClaimProcedure(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Clinical procedures performed.
    Procedures performed on the patient relevant to the billing items with the
    claim.
    """

    __resource_type__ = "ClaimProcedure"

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
        ``ClaimProcedure`` according specification,
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


class ClaimRelated(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Prior or corollary claims.
    Other claims which are related to this claim such as prior submissions or
    claims for related services or for the same event.
    """

    __resource_type__ = "ClaimRelated"

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
        ``ClaimRelated`` according specification,
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


class ClaimSupportingInfo(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Supporting information.
    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues.
    """

    __resource_type__ = "ClaimSupportingInfo"

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

    reason: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
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
        ``ClaimSupportingInfo`` according specification,
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
