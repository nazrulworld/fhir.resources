from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/EligibilityResponse
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class EligibilityResponse(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    EligibilityResponse resource.
    This resource provides eligibility and plan details from the processing of
    an Eligibility resource.
    """

    __resource_type__ = "EligibilityResponse"

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

    disposition: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="disposition",
        title="Disposition Message",
        description="A description of the status of the adjudication.",
        json_schema_extra={
            "element_property": True,
        },
    )
    disposition__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_disposition", title="Extension field for ``disposition``."
    )

    error: typing.List[fhirtypes.EligibilityResponseErrorType] | None = Field(  # type: ignore
        None,
        alias="error",
        title="Processing errors",
        description="Mutually exclusive with Services Provided (Item).",
        json_schema_extra={
            "element_property": True,
        },
    )

    form: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="form",
        title="Printed Form Identifier",
        description="The form to be used for printing the content.",
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business Identifier",
        description="The Response business identifier.",
        json_schema_extra={
            "element_property": True,
        },
    )

    inforce: bool | None = Field(  # type: ignore
        None,
        alias="inforce",
        title="Coverage inforce indicator",
        description=(
            "Flag indicating if the coverage provided is inforce currently  if no "
            "service date(s) specified or for the whole duration of the service "
            "dates."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    inforce__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_inforce", title="Extension field for ``inforce``."
    )

    insurance: typing.List[fhirtypes.EligibilityResponseInsuranceType] | None = Field(  # type: ignore
        None,
        alias="insurance",
        title="Details by insurance coverage",
        description=(
            "The insurer may provide both the details for the requested coverage as"
            " well as details for additional coverages known to the insurer."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    insurer: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="insurer",
        title="Insurer issuing the coverage",
        description="The Insurer who produced this adjudicated response.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    outcome: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="outcome",
        title="complete | error | partial",
        description="Transaction status: error, complete.",
        json_schema_extra={
            "element_property": True,
        },
    )

    request: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="request",
        title="Eligibility reference",
        description="Original request resource reference.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["EligibilityRequest"],
        },
    )

    requestOrganization: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="requestOrganization",
        title="Responsible organization",
        description=(
            "The organization which is responsible for the services rendered to the"
            " patient."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    requestProvider: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="requestProvider",
        title="Responsible practitioner",
        description=(
            "The practitioner who is responsible for the services rendered to the "
            "patient."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner"],
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

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EligibilityResponse`` according specification,
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
            "created",
            "requestProvider",
            "requestOrganization",
            "request",
            "outcome",
            "disposition",
            "insurer",
            "inforce",
            "insurance",
            "form",
            "error",
        ]


class EligibilityResponseError(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Processing errors.
    Mutually exclusive with Services Provided (Item).
    """

    __resource_type__ = "EligibilityResponseError"

    code: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="code",
        title="Error code detailing processing issues",
        description=(
            "An error code,from a specified code system, which details why the "
            "eligibility check could not be performed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EligibilityResponseError`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code"]


class EligibilityResponseInsurance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details by insurance coverage.
    The insurer may provide both the details for the requested coverage as well
    as details for additional coverages known to the insurer.
    """

    __resource_type__ = "EligibilityResponseInsurance"

    benefitBalance: typing.List[fhirtypes.EligibilityResponseInsuranceBenefitBalanceType] | None = Field(  # type: ignore
        None,
        alias="benefitBalance",
        title="Benefits by Category",
        description="Benefits and optionally current balances by Category.",
        json_schema_extra={
            "element_property": True,
        },
    )

    contract: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="contract",
        title="Contract details",
        description="The contract resource which may provide more detailed information.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Contract"],
        },
    )

    coverage: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="coverage",
        title="Updated Coverage details",
        description="A suite of updated or additional Coverages from the Insurer.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Coverage"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EligibilityResponseInsurance`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "coverage",
            "contract",
            "benefitBalance",
        ]


class EligibilityResponseInsuranceBenefitBalance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Benefits by Category.
    Benefits and optionally current balances by Category.
    """

    __resource_type__ = "EligibilityResponseInsuranceBenefitBalance"

    category: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="category",
        title="Type of services covered",
        description="Dental, Vision, Medical, Pharmacy, Rehab etc.",
        json_schema_extra={
            "element_property": True,
        },
    )

    description: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Description of the benefit or services covered",
        description=(
            "A richer description of the benefit, for example 'DENT2 covers 100% of"
            " basic, 50% of major but exclused Ortho, Implants and Costmetic "
            "services'."
        ),
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
            "missing or False indicated the service is included in the coverage."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    excluded__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_excluded", title="Extension field for ``excluded``."
    )

    financial: typing.List[fhirtypes.EligibilityResponseInsuranceBenefitBalanceFinancialType] | None = Field(  # type: ignore
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
        description="A short name or tag for the benefit, for example MED01, or DENT2.",
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
        description="Network designation.",
        json_schema_extra={
            "element_property": True,
        },
    )

    subCategory: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="subCategory",
        title="Detailed services covered within the type",
        description="Dental: basic, major, ortho; Vision exam, glasses, contacts; etc.",
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
            " 'maximum annual vistis'."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    unit: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="unit",
        title="Individual or family",
        description="Unit designation: individual or family.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EligibilityResponseInsuranceBenefitBalance`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "category",
            "subCategory",
            "excluded",
            "name",
            "description",
            "network",
            "unit",
            "term",
            "financial",
        ]


class EligibilityResponseInsuranceBenefitBalanceFinancial(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Benefit Summary.
    Benefits Used to date.
    """

    __resource_type__ = "EligibilityResponseInsuranceBenefitBalanceFinancial"

    allowedMoney: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="allowedMoney",
        title="Benefits allowed",
        description=None,
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
        description=None,
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
        description=None,
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
        title="Deductable, visits, benefit amount",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    usedMoney: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="usedMoney",
        title="Benefits used",
        description=None,
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
        description=None,
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
        ``EligibilityResponseInsuranceBenefitBalanceFinancial`` according specification,
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
