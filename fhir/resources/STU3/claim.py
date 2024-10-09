from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Claim
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Claim(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Claim, Pre-determination or Pre-authorization.
    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """

    __resource_type__ = "Claim"

    accident: fhirtypes.ClaimAccidentType | None = Field(  # type: ignore
        None,
        alias="accident",
        title="Details about an accident",
        description="An accident which resulted in the need for healthcare services.",
        json_schema_extra={
            "element_property": True,
        },
    )

    billablePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="billablePeriod",
        title="Period for charge submission",
        description="The billable period for which charges are being submitted.",
        json_schema_extra={
            "element_property": True,
        },
    )

    careTeam: typing.List[fhirtypes.ClaimCareTeamType] | None = Field(  # type: ignore
        None,
        alias="careTeam",
        title="Members of the care team",
        description=(
            "The members of the team who provided the overall service as well as "
            "their role and whether responsible and qualifications."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    created: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="created",
        title="Creation date",
        description=(
            "The date when the enclosed suite of services were performed or "
            "completed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_created", title="Extension field for ``created``."
    )

    diagnosis: typing.List[fhirtypes.ClaimDiagnosisType] | None = Field(  # type: ignore
        None,
        alias="diagnosis",
        title="List of Diagnosis",
        description="List of patient diagnosis for which care is sought.",
        json_schema_extra={
            "element_property": True,
        },
    )

    employmentImpacted: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="employmentImpacted",
        title="Period unable to work",
        description=(
            "The start and optional end dates of when the patient was precluded "
            "from working due to the treatable condition(s)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    enterer: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="enterer",
        title="Author",
        description=(
            "Person who created the invoice/claim/pre-determination or pre-"
            "authorization."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner"],
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
            "enum_reference_types": ["Location"],
        },
    )

    fundsReserve: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="fundsReserve",
        title="Funds requested to be reserved",
        description=(
            "In the case of a Pre-Determination/Pre-Authorization the provider may "
            "request that funds in the amount of the expected Benefit be reserved "
            "('Patient' or 'Provider') to pay for the Benefits determined on the "
            "subsequent claim(s). 'None' explicitly indicates no funds reserving is"
            " requested."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    hospitalization: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="hospitalization",
        title="Period in hospital",
        description=(
            "The start and optional end dates of when the patient was confined to a"
            " treatment center."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Claim number",
        description=(
            "The business identifier for the instance: claim number, pre-"
            "determination or pre-authorization number."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    information: typing.List[fhirtypes.ClaimInformationType] | None = Field(  # type: ignore
        None,
        alias="information",
        title=(
            "Exceptions, special considerations, the condition, situation, prior or"
            " concurrent issues"
        ),
        description=(
            "Additional information codes regarding exceptions, special "
            "considerations, the condition, situation, prior or concurrent issues. "
            "Often there are mutiple jurisdiction specific valuesets which are "
            "required."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    insurance: typing.List[fhirtypes.ClaimInsuranceType] | None = Field(  # type: ignore
        None,
        alias="insurance",
        title="Insurance or medical plan",
        description="Financial instrument by which payment information for health care.",
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
        title="Goods and Services",
        description="First tier of goods and services.",
        json_schema_extra={
            "element_property": True,
        },
    )

    organization: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="organization",
        title="Responsible organization",
        description=(
            "The organization which is responsible for the bill, claim pre-"
            "determination, pre-authorization."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    originalPrescription: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="originalPrescription",
        title="Original prescription if superceded by fulfiller",
        description=(
            "Original prescription which has been superceded by this prescription "
            "to support the dispensing of pharmacy services, medications or "
            "products. For example, a physician may prescribe a medication which "
            "the pharmacy determines is contraindicated, or for which the patient "
            "has an intolerance, and therefor issues a new precription for an "
            "alternate medication which has the same theraputic intent. The "
            "prescription from the pharmacy becomes the 'prescription' and that "
            "from the physician becomes the 'original prescription'."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["MedicationRequest"],
        },
    )

    patient: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="patient",
        title="The subject of the Products and Services",
        description="Patient Resource.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient"],
        },
    )

    payee: fhirtypes.ClaimPayeeType | None = Field(  # type: ignore
        None,
        alias="payee",
        title="Party to be paid any benefits payable",
        description="The party to be reimbursed for the services.",
        json_schema_extra={
            "element_property": True,
        },
    )

    prescription: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="prescription",
        title="Prescription authorizing services or products",
        description="Prescription to support the dispensing of Pharmacy or Vision products.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["MedicationRequest", "VisionPrescription"],
        },
    )

    priority: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="priority",
        title="Desired processing priority",
        description="Immediate (STAT), best effort (NORMAL), deferred (DEFER).",
        json_schema_extra={
            "element_property": True,
        },
    )

    procedure: typing.List[fhirtypes.ClaimProcedureType] | None = Field(  # type: ignore
        None,
        alias="procedure",
        title="Procedures performed",
        description=(
            "Ordered list of patient procedures performed to support the "
            "adjudication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    provider: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="provider",
        title="Responsible provider",
        description=(
            "The provider which is responsible for the bill, claim pre-"
            "determination, pre-authorization."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner"],
        },
    )

    referral: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="referral",
        title="Treatment Referral",
        description=(
            "The referral resource which lists the date, practitioner, reason and "
            "other supporting information."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ReferralRequest"],
        },
    )

    related: typing.List[fhirtypes.ClaimRelatedType] | None = Field(  # type: ignore
        None,
        alias="related",
        title="Related Claims which may be revelant to processing this claimn",
        description=(
            "Other claims which are related to this claim such as prior claim "
            "versions or for related services."
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
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["active", "cancelled", "draft", "entered-in-error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    subType: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="subType",
        title="Finer grained claim type information",
        description=(
            "A finer grained suite of claim subtype codes which may convey "
            "Inpatient vs Outpatient and/or a specialty service. In the US the "
            "BillType."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    total: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="total",
        title="Total claim cost",
        description="The total value of the claim.",
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Type or discipline",
        description=(
            "The category of claim, eg, oral, pharmacy, vision, insitutional, "
            "professional."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    use: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="use",
        title="complete | proposed | exploratory | other",
        description=(
            "Complete (Bill or Claim), Proposed (Pre-Authorization), Exploratory "
            "(Pre-determination)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["complete", "proposed", "exploratory", "other"],
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
            "organization",
            "priority",
            "fundsReserve",
            "related",
            "prescription",
            "originalPrescription",
            "payee",
            "referral",
            "facility",
            "careTeam",
            "information",
            "diagnosis",
            "procedure",
            "insurance",
            "accident",
            "employmentImpacted",
            "hospitalization",
            "item",
            "total",
        ]


class ClaimAccident(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details about an accident.
    An accident which resulted in the need for healthcare services.
    """

    __resource_type__ = "ClaimAccident"

    date: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="date",
        title="When the accident occurred see information codes see information codes",
        description="Date of an accident which these services are addressing.",
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
        title="Accident Place",
        description=None,
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
        title="Accident Place",
        description=None,
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
        description="Type of accident: work, auto, etc.",
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
    The members of the team who provided the overall service as well as their
    role and whether responsible and qualifications.
    """

    __resource_type__ = "ClaimCareTeam"

    provider: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="provider",
        title="Provider individual or organization",
        description="Member of the team who provided the overall service.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner", "Organization"],
        },
    )

    qualification: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="qualification",
        title="Type, classification or Specialization",
        description="The qualification which is applicable for this service.",
        json_schema_extra={
            "element_property": True,
        },
    )

    responsible: bool | None = Field(  # type: ignore
        None,
        alias="responsible",
        title="Billing provider",
        description=(
            "The party who is billing and responsible for the claimed good or "
            "service rendered to the patient."
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
        title="Role on the team",
        description=(
            "The lead, assisting or supervising practitioner and their discipline "
            "if a multidisiplinary team."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    sequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="sequence",
        title="Number to covey order of careTeam",
        description="Sequence of the careTeam which serves to order and provide a link.",
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
            "qualification",
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

    List of Diagnosis.
    List of patient diagnosis for which care is sought.
    """

    __resource_type__ = "ClaimDiagnosis"

    diagnosisCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="diagnosisCodeableConcept",
        title="Patient's diagnosis",
        description="The diagnosis.",
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
        title="Patient's diagnosis",
        description="The diagnosis.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e diagnosis[x]
            "one_of_many": "diagnosis",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Condition"],
        },
    )

    packageCode: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="packageCode",
        title="Package billing code",
        description=(
            "The package billing code, for example DRG, based on the assigned "
            "grouping code system."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    sequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="sequence",
        title="Number to covey order of diagnosis",
        description="Sequence of diagnosis which serves to provide a link.",
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
        description=(
            "The type of the Diagnosis, for example: admitting, primary, secondary,"
            " discharge."
        ),
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
            "packageCode",
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


class ClaimInformation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Exceptions, special considerations, the condition, situation, prior or
    concurrent issues.
    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues. Often there are
    mutiple jurisdiction specific valuesets which are required.
    """

    __resource_type__ = "ClaimInformation"

    category: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="category",
        title="General class of information",
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
            "which care is sought which may influence the adjudication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reason: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="reason",
        title="Reason associated with the information",
        description=(
            "For example, provides the reason for: the additional stay, or missing "
            "tooth or any other situation where a reason code is required in "
            "addition to the content."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    sequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="sequence",
        title="Information instance identifier",
        description="Sequence of the information element which serves to provide a link.",
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
        title="Additional Data or supporting information",
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
        title="Additional Data or supporting information",
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
        title="Additional Data or supporting information",
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
        title="Additional Data or supporting information",
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
        ``ClaimInformation`` according specification,
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
            "valueString",
            "valueQuantity",
            "valueAttachment",
            "valueReference",
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
                "valueQuantity",
                "valueReference",
                "valueString",
            ],
        }
        return one_of_many_fields


class ClaimInsurance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Insurance or medical plan.
    Financial instrument by which payment information for health care.
    """

    __resource_type__ = "ClaimInsurance"

    businessArrangement: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="businessArrangement",
        title="Business agreement",
        description=(
            "The contract number of a business agreement which describes the terms "
            "and conditions."
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
        description="The Coverages adjudication details.",
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
        description="Reference to the program or plan identification, underwriter or payor.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Coverage"],
        },
    )

    focal: bool | None = Field(  # type: ignore
        None,
        alias="focal",
        title="Is the focal Coverage",
        description=(
            "A flag to indicate that this Coverage is the focus for adjudication. "
            "The Coverage against which the claim is to be adjudicated."
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
        title="Pre-Authorization/Determination Reference",
        description="A list of references from the Insurer to which these services pertain.",
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
        title="Service instance identifier",
        description=(
            "Sequence of coverage which serves to provide a link and convey "
            "coordination of benefit order."
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

    Goods and Services.
    First tier of goods and services.
    """

    __resource_type__ = "ClaimItem"

    bodySite: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="bodySite",
        title="Service Location",
        description="Physical service site on the patient (limb, tooth, etc).",
        json_schema_extra={
            "element_property": True,
        },
    )

    careTeamLinkId: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="careTeamLinkId",
        title="Applicable careTeam members",
        description="CareTeam applicable for this service or product line.",
        json_schema_extra={
            "element_property": True,
        },
    )
    careTeamLinkId__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_careTeamLinkId", title="Extension field for ``careTeamLinkId``."
    )

    category: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="category",
        title="Type of service or product",
        description=(
            "Health Care Service Type Codes  to identify the classification of "
            "service or benefits."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    detail: typing.List[fhirtypes.ClaimItemDetailType] | None = Field(  # type: ignore
        None,
        alias="detail",
        title="Additional items",
        description="Second tier of goods and services.",
        json_schema_extra={
            "element_property": True,
        },
    )

    diagnosisLinkId: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="diagnosisLinkId",
        title="Applicable diagnoses",
        description="Diagnosis applicable for this service or product line.",
        json_schema_extra={
            "element_property": True,
        },
    )
    diagnosisLinkId__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_diagnosisLinkId", title="Extension field for ``diagnosisLinkId``."
    )

    encounter: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="encounter",
        title="Encounters related to this billed item",
        description=(
            "A billed item may include goods or services provided in multiple "
            "encounters."
        ),
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

    informationLinkId: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="informationLinkId",
        title="Applicable exception and supporting information",
        description=(
            "Exceptions, special conditions and supporting information pplicable "
            "for this service or product line."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    informationLinkId__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_informationLinkId",
        title="Extension field for ``informationLinkId``.",
    )

    locationAddress: fhirtypes.AddressType | None = Field(  # type: ignore
        None,
        alias="locationAddress",
        title="Place of service",
        description="Where the service was provided.",
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
        title="Place of service",
        description="Where the service was provided.",
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
        title="Place of service",
        description="Where the service was provided.",
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
            "Item typification or modifiers codes, eg for Oral whether the "
            "treatment is cosmetic or associated with TMJ, or for medical whether "
            "the treatment was outside the clinic or out of office hours."
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
            "The quantity times the unit price for an addittional service or "
            "product or charge. For example, the formula: unit Quantity * unit "
            "Price (Cost per Point) * factor Number  * points = net Amount. "
            "Quantity, factor and points are assumed to be 1 if not supplied."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    procedureLinkId: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="procedureLinkId",
        title="Applicable procedures",
        description="Procedures applicable for this service or product line.",
        json_schema_extra={
            "element_property": True,
        },
    )
    procedureLinkId__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_procedureLinkId", title="Extension field for ``procedureLinkId``."
    )

    programCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="programCode",
        title="Program specific reason for item inclusion",
        description=(
            "For programs which require reason codes for the inclusion or covering "
            "of this billed item under the program or sub-program."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="Count of Products or Services",
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
            "The type of reveneu or cost center providing the product and/or "
            "service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    sequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="sequence",
        title="Service instance",
        description="A service line number.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    service: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="service",
        title="Billing Code",
        description=(
            "If this is an actual service or product line, ie. not a Group, then "
            "use code to indicate the Professional Service or Product supplied (eg."
            " CTP, HCPCS,USCLS,ICD10, NCPDP,DIN,RXNorm,ACHI,CCI). If a grouping "
            "item then use a group code to indicate the type of thing being grouped"
            " eg. 'glasses' or 'compound'."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    servicedDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="servicedDate",
        title="Date or dates of Service",
        description=(
            "The date or dates when the enclosed suite of services were performed "
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
        title="Date or dates of Service",
        description=(
            "The date or dates when the enclosed suite of services were performed "
            "or completed."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e serviced[x]
            "one_of_many": "serviced",
            "one_of_many_required": False,
        },
    )

    subSite: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="subSite",
        title="Service Sub-location",
        description="A region or surface of the site, eg. limb region or tooth surface(s).",
        json_schema_extra={
            "element_property": True,
        },
    )

    udi: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="udi",
        title="Unique Device Identifier",
        description="List of Unique Device Identifiers associated with this line item.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Device"],
        },
    )

    unitPrice: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="unitPrice",
        title="Fee, charge or cost per point",
        description=(
            "If the item is a node then this is the fee for the product or service,"
            " otherwise this is the total of the fees for the children of the "
            "group."
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
            "careTeamLinkId",
            "diagnosisLinkId",
            "procedureLinkId",
            "informationLinkId",
            "revenue",
            "category",
            "service",
            "modifier",
            "programCode",
            "servicedDate",
            "servicedPeriod",
            "locationCodeableConcept",
            "locationAddress",
            "locationReference",
            "quantity",
            "unitPrice",
            "factor",
            "net",
            "udi",
            "bodySite",
            "subSite",
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


class ClaimItemDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional items.
    Second tier of goods and services.
    """

    __resource_type__ = "ClaimItemDetail"

    category: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="category",
        title="Type of service or product",
        description=(
            "Health Care Service Type Codes  to identify the classification of "
            "service or benefits."
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
            "Item typification or modifiers codes, eg for Oral whether the "
            "treatment is cosmetic or associated with TMJ, or for medical whether "
            "the treatment was outside the clinic or out of office hours."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    net: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="net",
        title="Total additional item cost",
        description=(
            "The quantity times the unit price for an addittional service or "
            "product or charge. For example, the formula: unit Quantity * unit "
            "Price (Cost per Point) * factor Number  * points = net Amount. "
            "Quantity, factor and points are assumed to be 1 if not supplied."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    programCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="programCode",
        title="Program specific reason for item inclusion",
        description=(
            "For programs which require reson codes for the inclusion, covering, of"
            " this billed item under the program or sub-program."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="Count of Products or Services",
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
            "The type of reveneu or cost center providing the product and/or "
            "service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    sequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="sequence",
        title="Service instance",
        description="A service line number.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    service: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="service",
        title="Billing Code",
        description=(
            "If this is an actual service or product line, ie. not a Group, then "
            "use code to indicate the Professional Service or Product supplied (eg."
            " CTP, HCPCS,USCLS,ICD10, NCPDP,DIN,ACHI,CCI). If a grouping item then "
            "use a group code to indicate the type of thing being grouped eg. "
            "'glasses' or 'compound'."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    subDetail: typing.List[fhirtypes.ClaimItemDetailSubDetailType] | None = Field(  # type: ignore
        None,
        alias="subDetail",
        title="Additional items",
        description="Third tier of goods and services.",
        json_schema_extra={
            "element_property": True,
        },
    )

    udi: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="udi",
        title="Unique Device Identifier",
        description="List of Unique Device Identifiers associated with this line item.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Device"],
        },
    )

    unitPrice: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="unitPrice",
        title="Fee, charge or cost per point",
        description=(
            "If the item is a node then this is the fee for the product or service,"
            " otherwise this is the total of the fees for the children of the "
            "group."
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
            "revenue",
            "category",
            "service",
            "modifier",
            "programCode",
            "quantity",
            "unitPrice",
            "factor",
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

    Additional items.
    Third tier of goods and services.
    """

    __resource_type__ = "ClaimItemDetailSubDetail"

    category: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="category",
        title="Type of service or product",
        description=(
            "Health Care Service Type Codes  to identify the classification of "
            "service or benefits."
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
            "Item typification or modifiers codes, eg for Oral whether the "
            "treatment is cosmetic or associated with TMJ, or for medical whether "
            "the treatment was outside the clinic or out of office hours."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    net: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="net",
        title="Net additional item cost",
        description=(
            "The quantity times the unit price for an addittional service or "
            "product or charge. For example, the formula: unit Quantity * unit "
            "Price (Cost per Point) * factor Number  * points = net Amount. "
            "Quantity, factor and points are assumed to be 1 if not supplied."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    programCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="programCode",
        title="Program specific reason for item inclusion",
        description=(
            "For programs which require reson codes for the inclusion, covering, of"
            " this billed item under the program or sub-program."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="Count of Products or Services",
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
            "The type of reveneu or cost center providing the product and/or "
            "service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    sequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="sequence",
        title="Service instance",
        description="A service line number.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    service: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="service",
        title="Billing Code",
        description=(
            "A code to indicate the Professional Service or Product supplied (eg. "
            "CTP, HCPCS,USCLS,ICD10, NCPDP,DIN,ACHI,CCI)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    udi: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="udi",
        title="Unique Device Identifier",
        description="List of Unique Device Identifiers associated with this line item.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Device"],
        },
    )

    unitPrice: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="unitPrice",
        title="Fee, charge or cost per point",
        description="The fee for an addittional service or product or charge.",
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
            "revenue",
            "category",
            "service",
            "modifier",
            "programCode",
            "quantity",
            "unitPrice",
            "factor",
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

    Party to be paid any benefits payable.
    The party to be reimbursed for the services.
    """

    __resource_type__ = "ClaimPayee"

    party: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="party",
        title="Party to receive the payable",
        description="Party to be reimbursed: Subscriber, provider, other.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "Organization",
                "Patient",
                "RelatedPerson",
            ],
        },
    )

    resourceType: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="resourceType",
        title="organization | patient | practitioner | relatedperson",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Type of party: Subscriber, Provider, other",
        description="Type of Party to be reimbursed: Subscriber, provider, other.",
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
        return ["id", "extension", "modifierExtension", "type", "resourceType", "party"]


class ClaimProcedure(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Procedures performed.
    Ordered list of patient procedures performed to support the adjudication.
    """

    __resource_type__ = "ClaimProcedure"

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="date",
        title="When the procedure was performed",
        description="Date and optionally time the procedure was performed .",
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
        title="Patient's list of procedures performed",
        description="The procedure code.",
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
        title="Patient's list of procedures performed",
        description="The procedure code.",
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
        title="Procedure sequence for reference",
        description="Sequence of procedures which serves to order and provide a link.",
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
        ``ClaimProcedure`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "date",
            "procedureCodeableConcept",
            "procedureReference",
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

    Related Claims which may be revelant to processing this claimn.
    Other claims which are related to this claim such as prior claim versions
    or for related services.
    """

    __resource_type__ = "ClaimRelated"

    claim: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="claim",
        title="Reference to the related claim",
        description=(
            "Other claims which are related to this claim such as prior claim "
            "versions or for related services."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Claim"],
        },
    )

    reference: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="reference",
        title="Related file or case reference",
        description=(
            "An alternate organizational reference to the case or file to which "
            "this particular claim pertains - eg Property/Casualy insurer claim # "
            "or Workers Compensation case # ."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    relationship: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="relationship",
        title="How the reference claim is related",
        description="For example prior or umbrella.",
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
