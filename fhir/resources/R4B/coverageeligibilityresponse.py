from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/CoverageEligibilityResponse
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class CoverageEligibilityResponse(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    CoverageEligibilityResponse resource.
    This resource provides eligibility and plan details from the processing of
    an CoverageEligibilityRequest resource.
    """

    __resource_type__ = "CoverageEligibilityResponse"

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

    error: typing.List[fhirtypes.CoverageEligibilityResponseErrorType] | None = Field(  # type: ignore
        None,
        alias="error",
        title="Processing errors",
        description="Errors encountered during the processing of the request.",
        json_schema_extra={
            "element_property": True,
        },
    )

    form: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="form",
        title="Printed form identifier",
        description="A code for the form to be used for printing the content.",
        json_schema_extra={
            "element_property": True,
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

    insurance: typing.List[fhirtypes.CoverageEligibilityResponseInsuranceType] | None = Field(  # type: ignore
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
            "The Insurer who issued the coverage in question and is the author of "
            "the response."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    outcome: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="outcome",
        title="queued | complete | error | partial",
        description="The outcome of the request processing.",
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

    preAuthRef: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="preAuthRef",
        title="Preauthorization reference",
        description=(
            "A reference from the Insurer to which these services pertain to be "
            "used on further communication and as proof that the request occurred."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    preAuthRef__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_preAuthRef", title="Extension field for ``preAuthRef``."
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

    request: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="request",
        title="Eligibility request reference",
        description="Reference to the original request resource.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["CoverageEligibilityRequest"],
        },
    )

    requestor: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="requestor",
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

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CoverageEligibilityResponse`` according specification,
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
            "purpose",
            "patient",
            "servicedDate",
            "servicedPeriod",
            "created",
            "requestor",
            "request",
            "outcome",
            "disposition",
            "insurer",
            "insurance",
            "preAuthRef",
            "form",
            "error",
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


class CoverageEligibilityResponseError(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Processing errors.
    Errors encountered during the processing of the request.
    """

    __resource_type__ = "CoverageEligibilityResponseError"

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
        ``CoverageEligibilityResponseError`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code"]


class CoverageEligibilityResponseInsurance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Patient insurance information.
    Financial instruments for reimbursement for the health care products and
    services.
    """

    __resource_type__ = "CoverageEligibilityResponseInsurance"

    benefitPeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="benefitPeriod",
        title="When the benefits are applicable",
        description="The term of the benefits documented in this response.",
        json_schema_extra={
            "element_property": True,
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

    inforce: bool | None = Field(  # type: ignore
        None,
        alias="inforce",
        title="Coverage inforce indicator",
        description=(
            "Flag indicating if the coverage provided is inforce currently if no "
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

    item: typing.List[fhirtypes.CoverageEligibilityResponseInsuranceItemType] | None = Field(  # type: ignore
        None,
        alias="item",
        title="Benefits and authorization details",
        description=(
            "Benefits and optionally current balances, and authorization details by"
            " category or service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CoverageEligibilityResponseInsurance`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "coverage",
            "inforce",
            "benefitPeriod",
            "item",
        ]


class CoverageEligibilityResponseInsuranceItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Benefits and authorization details.
    Benefits and optionally current balances, and authorization details by
    category or service.
    """

    __resource_type__ = "CoverageEligibilityResponseInsuranceItem"

    authorizationRequired: bool | None = Field(  # type: ignore
        None,
        alias="authorizationRequired",
        title="Authorization required flag",
        description=(
            "A boolean flag indicating whether a preauthorization is required prior"
            " to actual service delivery."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    authorizationRequired__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_authorizationRequired",
        title="Extension field for ``authorizationRequired``.",
    )

    authorizationSupporting: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="authorizationSupporting",
        title="Type of required supporting materials",
        description=(
            "Codes or comments regarding information or actions associated with the"
            " preauthorization."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    authorizationUrl: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="authorizationUrl",
        title="Preauthorization requirements endpoint",
        description=(
            "A web location for obtaining requirements or descriptive information "
            "regarding the preauthorization."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    authorizationUrl__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_authorizationUrl",
        title="Extension field for ``authorizationUrl``.",
    )

    benefit: typing.List[fhirtypes.CoverageEligibilityResponseInsuranceItemBenefitType] | None = Field(  # type: ignore
        None,
        alias="benefit",
        title="Benefit Summary",
        description="Benefits used to date.",
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
        title="Performing practitioner",
        description=(
            "The practitioner who is eligible for the provision of the product or "
            "service."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner", "PractitionerRole"],
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
        ``CoverageEligibilityResponseInsuranceItem`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "category",
            "productOrService",
            "modifier",
            "provider",
            "excluded",
            "name",
            "description",
            "network",
            "unit",
            "term",
            "benefit",
            "authorizationRequired",
            "authorizationSupporting",
            "authorizationUrl",
        ]


class CoverageEligibilityResponseInsuranceItemBenefit(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Benefit Summary.
    Benefits used to date.
    """

    __resource_type__ = "CoverageEligibilityResponseInsuranceItemBenefit"

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

    usedString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="usedString",
        title="Benefits used",
        description="The quantity of the benefit which have been consumed to date.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e used[x]
            "one_of_many": "used",
            "one_of_many_required": False,
        },
    )
    usedString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_usedString", title="Extension field for ``usedString``."
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
        ``CoverageEligibilityResponseInsuranceItemBenefit`` according specification,
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
            "usedString",
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
            "used": ["usedMoney", "usedString", "usedUnsignedInt"],
        }
        return one_of_many_fields
