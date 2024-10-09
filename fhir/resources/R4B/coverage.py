from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Coverage
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
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
        description="A unique identifier for a dependent under the coverage.",
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
        title="Business Identifier for the coverage",
        description="A unique identifier assigned to this coverage.",
        json_schema_extra={
            "element_property": True,
        },
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
            "specific positioning of coverages depends upon the episode of care."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    order__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_order", title="Extension field for ``order``."
    )

    payor: typing.List[fhirtypes.ReferenceType] = Field(  # type: ignore
        ...,
        alias="payor",
        title="Issuer of the policy",
        description=(
            "The program or plan underwriter or payor including both insurance and "
            "non-insurance agreements, such as patient-pay agreements."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization", "Patient", "RelatedPerson"],
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

    subscriberId: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="subscriberId",
        title="ID assigned to the subscriber",
        description="The insurer assigned ID for the Subscriber.",
        json_schema_extra={
            "element_property": True,
        },
    )
    subscriberId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_subscriberId", title="Extension field for ``subscriberId``."
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
            "type",
            "policyHolder",
            "subscriber",
            "subscriberId",
            "beneficiary",
            "dependent",
            "relationship",
            "period",
            "payor",
            "class",
            "order",
            "network",
            "costToBeneficiary",
            "subrogation",
            "contract",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
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
            "or number and optional name is provided, for example may be used to "
            "identify a class of coverage or employer group, Policy, Plan."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    value: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="value",
        title="Value associated with the type",
        description=(
            "The alphanumeric string value associated with the insurer issued " "label."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CoverageClass`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "value", "name"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("value", "value__ext")]
        return required_fields


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

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Cost category",
        description="The category of patient centric costs associated with treatment.",
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
            "one_of_many_required": True,
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
            "one_of_many_required": True,
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
        description="The timeframe during when the exception is in force.",
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
