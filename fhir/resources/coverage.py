from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Coverage
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Coverage(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Insurance or medical plan or a payment agreement.
    Financial instrument which may be used to reimburse or pay for health care
    products and services. Includes both insurance and self-payment.
    """

    __resource_type__ = "Coverage"

    beneficiary: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="beneficiary",
        title="Plan beneficiary",
        description=(
            "The party who benefits from the insurance coverage; the patient when "
            "products and/or services are provided."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient"],
        },
    )

    class_fhir: typing.List[fhirtypes.CoverageClassType] | None = Field(  # type: ignore
        None,
        alias="class",
        title="Additional coverage classifications",
        description="A suite of underwriter specific classifiers.",
        json_schema_extra={
            "element_property": True,
        },
    )

    contract: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="contract",
        title="Contract details",
        description="The policy(s) which constitute this insurance coverage.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Contract"],
        },
    )

    costToBeneficiary: typing.List[fhirtypes.CoverageCostToBeneficiaryType] | None = Field(  # type: ignore
        None,
        alias="costToBeneficiary",
        title="Patient payments for services/products",
        description=(
            "A suite of codes indicating the cost category and associated amount "
            "which have been detailed in the policy and may have been  included on "
            "the health card."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    dependent: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="dependent",
        title="Dependent number",
        description="A designator for a dependent under the coverage.",
        json_schema_extra={
            "element_property": True,
        },
    )
    dependent__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_dependent", title="Extension field for ``dependent``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business identifier(s) for this coverage",
        description="The identifier of the coverage as issued by the insurer.",
        json_schema_extra={
            "element_property": True,
        },
    )

    insurancePlan: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="insurancePlan",
        title="Insurance plan details",
        description=(
            "The insurance plan details, benefits and costs, which constitute this "
            "insurance coverage."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["InsurancePlan"],
        },
    )

    insurer: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="insurer",
        title="Issuer of the policy",
        description="The program or plan underwriter, payor, insurance company.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    kind: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="kind",
        title="insurance | self-pay | other",
        description=(
            "The nature of the coverage be it insurance, or cash payment such as "
            "self-pay."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["insurance", "self-pay", "other"],
        },
    )
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_kind", title="Extension field for ``kind``."
    )

    network: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="network",
        title="Insurer network",
        description=(
            "The insurer-specific identifier for the insurer-defined network of "
            "providers to which the beneficiary may seek treatment which will be "
            "covered at the 'in-network' rate, otherwise 'out of network' terms and"
            " conditions apply."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    network__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_network", title="Extension field for ``network``."
    )

    order: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="order",
        title="Relative order of the coverage",
        description=(
            "The order of applicability of this coverage relative to other "
            "coverages which are currently in force. Note, there may be gaps in the"
            " numbering and this does not imply primary, secondary etc. as the "
            "specific positioning of coverages depends upon the episode of care. "
            "For example; a patient might have (0) auto insurance (1) their own "
            "health insurance and (2) spouse's health insurance. When claiming for "
            "treatments which were not the result of an auto accident then only "
            "coverages (1) and (2) above would be applicatble and would apply in "
            "the order specified in parenthesis."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    order__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_order", title="Extension field for ``order``."
    )

    paymentBy: typing.List[fhirtypes.CoveragePaymentByType] | None = Field(  # type: ignore
        None,
        alias="paymentBy",
        title="Self-pay parties and responsibility",
        description=(
            "Link to the paying party and optionally what specifically they will be"
            " responsible to pay."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="period",
        title="Coverage start and end dates",
        description=(
            "Time period during which the coverage is in force. A missing start "
            "date indicates the start date isn't known, a missing end date means "
            "the coverage is continuing to be in force."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    policyHolder: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="policyHolder",
        title="Owner of the policy",
        description="The party who 'owns' the insurance policy.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "RelatedPerson", "Organization"],
        },
    )

    relationship: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="relationship",
        title="Beneficiary relationship to the subscriber",
        description="The relationship of beneficiary (patient) to the subscriber.",
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

    subrogation: bool | None = Field(  # type: ignore
        None,
        alias="subrogation",
        title="Reimbursement to insurer",
        description=(
            "When 'subrogation=true' this insurance instance has been included not "
            "for adjudication but to provide insurers with the details to recover "
            "costs."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    subrogation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_subrogation", title="Extension field for ``subrogation``."
    )

    subscriber: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="subscriber",
        title="Subscriber to the policy",
        description=(
            "The party who has signed-up for or 'owns' the contractual relationship"
            " to the policy or to whom the benefit of the policy for services "
            "rendered to them or their family is due."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "RelatedPerson"],
        },
    )

    subscriberId: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="subscriberId",
        title="ID assigned to the subscriber",
        description="The insurer assigned ID for the Subscriber.",
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Coverage category such as medical or accident",
        description=(
            "The type of coverage: social program, medical plan, accident coverage "
            "(workers compensation, auto), group health or payment by an individual"
            " or organization."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Coverage`` according specification,
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
            "kind",
            "paymentBy",
            "type",
            "policyHolder",
            "subscriber",
            "subscriberId",
            "beneficiary",
            "dependent",
            "relationship",
            "period",
            "insurer",
            "class",
            "order",
            "network",
            "costToBeneficiary",
            "subrogation",
            "contract",
            "insurancePlan",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("kind", "kind__ext"), ("status", "status__ext")]
        return required_fields


class CoverageClass(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional coverage classifications.
    A suite of underwriter specific classifiers.
    """

    __resource_type__ = "CoverageClass"

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Human readable description of the type and value",
        description="A short description for the class.",
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Type of class such as 'group' or 'plan'",
        description=(
            "The type of classification for which an insurer-specific class label "
            "or number and optional name is provided.  For example, type may be "
            "used to identify a class of coverage or employer group, policy, or "
            "plan."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    value: fhirtypes.IdentifierType = Field(  # type: ignore
        ...,
        alias="value",
        title="Value associated with the type",
        description="The alphanumeric identifier associated with the insurer issued label.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CoverageClass`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "value", "name"]


class CoverageCostToBeneficiary(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Patient payments for services/products.
    A suite of codes indicating the cost category and associated amount which
    have been detailed in the policy and may have been  included on the health
    card.
    """

    __resource_type__ = "CoverageCostToBeneficiary"

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

    exception: typing.List[fhirtypes.CoverageCostToBeneficiaryExceptionType] | None = Field(  # type: ignore
        None,
        alias="exception",
        title="Exceptions for patient payments",
        description=(
            "A suite of codes indicating exceptions or reductions to patient costs "
            "and their effective periods."
        ),
        json_schema_extra={
            "element_property": True,
        },
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

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Cost category",
        description="The category of patient centric costs associated with treatment.",
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

    valueMoney: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="valueMoney",
        title="The amount or percentage due from the beneficiary",
        description="The amount due from the patient for the cost category.",
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
        title="The amount or percentage due from the beneficiary",
        description="The amount due from the patient for the cost category.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CoverageCostToBeneficiary`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "category",
            "network",
            "unit",
            "term",
            "valueQuantity",
            "valueMoney",
            "exception",
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
        one_of_many_fields = {"value": ["valueMoney", "valueQuantity"]}
        return one_of_many_fields


class CoverageCostToBeneficiaryException(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Exceptions for patient payments.
    A suite of codes indicating exceptions or reductions to patient costs and
    their effective periods.
    """

    __resource_type__ = "CoverageCostToBeneficiaryException"

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="period",
        title="The effective period of the exception",
        description="The timeframe the exception is in force.",
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Exception category",
        description="The code for the specific exception.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CoverageCostToBeneficiaryException`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "period"]


class CoveragePaymentBy(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Self-pay parties and responsibility.
    Link to the paying party and optionally what specifically they will be
    responsible to pay.
    """

    __resource_type__ = "CoveragePaymentBy"

    party: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="party",
        title="Parties performing self-payment",
        description=(
            "The list of parties providing non-insurance payment for the treatment "
            "costs."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "RelatedPerson", "Organization"],
        },
    )

    responsibility: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="responsibility",
        title="Party's responsibility",
        description=" Description of the financial responsibility.",
        json_schema_extra={
            "element_property": True,
        },
    )
    responsibility__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_responsibility", title="Extension field for ``responsibility``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CoveragePaymentBy`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "party", "responsibility"]
