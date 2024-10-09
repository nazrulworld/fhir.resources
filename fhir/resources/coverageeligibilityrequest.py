from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/CoverageEligibilityRequest
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class CoverageEligibilityRequest(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    CoverageEligibilityRequest resource.
    The CoverageEligibilityRequest provides patient and insurance coverage
    information to an insurer for them to respond, in the form of an
    CoverageEligibilityResponse, with information regarding whether the stated
    coverage is valid and in-force and optionally to provide the insurance
    details of the policy.
    """

    __resource_type__ = "CoverageEligibilityRequest"

    created: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="created",
        title="Creation date",
        description="The date when this resource was created.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_created", title="Extension field for ``created``."
    )

    enterer: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="enterer",
        title="Author",
        description="Person who created the request.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner", "PractitionerRole"],
        },
    )

    event: typing.List[fhirtypes.CoverageEligibilityRequestEventType] | None = Field(  # type: ignore
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
        description="Facility where the services are intended to be provided.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business Identifier for coverage eligiblity request",
        description="A unique identifier assigned to this coverage eligiblity request.",
        json_schema_extra={
            "element_property": True,
        },
    )

    insurance: typing.List[fhirtypes.CoverageEligibilityRequestInsuranceType] | None = Field(  # type: ignore
        None,
        alias="insurance",
        title="Patient insurance information",
        description=(
            "Financial instruments for reimbursement for the health care products "
            "and services."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    insurer: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="insurer",
        title="Coverage issuer",
        description=(
            "The Insurer who issued the coverage in question and is the recipient "
            "of the request."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    item: typing.List[fhirtypes.CoverageEligibilityRequestItemType] | None = Field(  # type: ignore
        None,
        alias="item",
        title="Item to be evaluated for eligibiity",
        description=(
            "Service categories or billable services for which benefit details "
            "and/or an authorization prior to service delivery may be required by "
            "the payor."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    patient: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="patient",
        title="Intended recipient of products and services",
        description=(
            "The party who is the beneficiary of the supplied coverage and for whom"
            " eligibility is sought."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient"],
        },
    )

    priority: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="priority",
        title="Desired processing priority",
        description="When the requestor expects the processor to complete processing.",
        json_schema_extra={
            "element_property": True,
        },
    )

    provider: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="provider",
        title="Party responsible for the request",
        description="The provider which is responsible for the request.",
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

    purpose: typing.List[fhirtypes.CodeType | None] | None = Field(  # type: ignore
        None,
        alias="purpose",
        title="auth-requirements | benefits | discovery | validation",
        description=(
            "Code to specify whether requesting: prior authorization requirements "
            "for some service categories or billing codes; benefits for coverages "
            "specified or discovered; discovery and return of coverages for the "
            "patient; and/or validation that the specified coverage is in-force at "
            "the date/period specified or 'now' if not specified."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["auth-requirements", "benefits", "discovery", "validation"],
        },
    )
    purpose__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    servicedDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="servicedDate",
        title="Estimated date or dates of service",
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
        title="Estimated date or dates of service",
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

    supportingInfo: typing.List[fhirtypes.CoverageEligibilityRequestSupportingInfoType] | None = Field(  # type: ignore
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

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CoverageEligibilityRequest`` according specification,
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
            "priority",
            "purpose",
            "patient",
            "event",
            "servicedDate",
            "servicedPeriod",
            "created",
            "enterer",
            "provider",
            "insurer",
            "facility",
            "supportingInfo",
            "insurance",
            "item",
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
            ("purpose", "purpose__ext"),
            ("status", "status__ext"),
        ]
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
        one_of_many_fields = {"serviced": ["servicedDate", "servicedPeriod"]}
        return one_of_many_fields


class CoverageEligibilityRequestEvent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Event information.
    Information code for an event with a corresponding date or period.
    """

    __resource_type__ = "CoverageEligibilityRequestEvent"

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
        ``CoverageEligibilityRequestEvent`` according specification,
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


class CoverageEligibilityRequestInsurance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Patient insurance information.
    Financial instruments for reimbursement for the health care products and
    services.
    """

    __resource_type__ = "CoverageEligibilityRequestInsurance"

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
        title="Applicable coverage",
        description=(
            "A flag to indicate that this Coverage is to be used for evaluation of "
            "this request when set to true."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    focal__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_focal", title="Extension field for ``focal``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CoverageEligibilityRequestInsurance`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "focal",
            "coverage",
            "businessArrangement",
        ]


class CoverageEligibilityRequestItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Item to be evaluated for eligibiity.
    Service categories or billable services for which benefit details and/or an
    authorization prior to service delivery may be required by the payor.
    """

    __resource_type__ = "CoverageEligibilityRequestItem"

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

    detail: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="detail",
        title="Product or service details",
        description="The plan/proposal/order describing the proposed service in detail.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    diagnosis: typing.List[fhirtypes.CoverageEligibilityRequestItemDiagnosisType] | None = Field(  # type: ignore
        None,
        alias="diagnosis",
        title="Applicable diagnosis",
        description="Patient diagnosis for which care is sought.",
        json_schema_extra={
            "element_property": True,
        },
    )

    facility: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="facility",
        title="Servicing facility",
        description="Facility where the services will be provided.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location", "Organization"],
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

    productOrService: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="productOrService",
        title="Billing, service, product, or drug code",
        description=(
            "This contains the product, service, drug or other billing code for the"
            " item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    provider: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="provider",
        title="Perfoming practitioner",
        description=(
            "The practitioner who is responsible for the product or service to be "
            "rendered to the patient."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner", "PractitionerRole"],
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

    supportingInfoSequence: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="supportingInfoSequence",
        title="Applicable exception or supporting information",
        description=(
            "Exceptions, special conditions and supporting information applicable "
            "for this service or product line."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    supportingInfoSequence__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_supportingInfoSequence",
        title="Extension field for ``supportingInfoSequence``.",
    )

    unitPrice: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="unitPrice",
        title="Fee, charge or cost per item",
        description="The amount charged to the patient by the provider for a single unit.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CoverageEligibilityRequestItem`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "supportingInfoSequence",
            "category",
            "productOrService",
            "modifier",
            "provider",
            "quantity",
            "unitPrice",
            "facility",
            "diagnosis",
            "detail",
        ]


class CoverageEligibilityRequestItemDiagnosis(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Applicable diagnosis.
    Patient diagnosis for which care is sought.
    """

    __resource_type__ = "CoverageEligibilityRequestItemDiagnosis"

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
            "one_of_many_required": False,
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
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Condition"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CoverageEligibilityRequestItemDiagnosis`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "diagnosisCodeableConcept",
            "diagnosisReference",
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
            "diagnosis": ["diagnosisCodeableConcept", "diagnosisReference"]
        }
        return one_of_many_fields


class CoverageEligibilityRequestSupportingInfo(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Supporting information.
    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues.
    """

    __resource_type__ = "CoverageEligibilityRequestSupportingInfo"

    appliesToAll: bool | None = Field(  # type: ignore
        None,
        alias="appliesToAll",
        title="Applies to all items",
        description=(
            "The supporting materials are applicable for all detail items, "
            "product/servce categories and specific billing codes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    appliesToAll__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_appliesToAll", title="Extension field for ``appliesToAll``."
    )

    information: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="information",
        title="Data to be provided",
        description=(
            "Additional data or information such as resources, documents, images "
            "etc. including references to the data or the actual inclusion of the "
            "data."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
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

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CoverageEligibilityRequestSupportingInfo`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "information",
            "appliesToAll",
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
