# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EligibilityResponse
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class EligibilityResponse(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    EligibilityResponse resource.
    This resource provides eligibility and plan details from the processing of
    an Eligibility resource.
    """

    resource_type = Field("EligibilityResponse", const=True)

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Creation date",
        description=(
            "The date when the enclosed suite of services were performed or "
            "completed."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
    )

    disposition: fhirtypes.String = Field(
        None,
        alias="disposition",
        title="Disposition Message",
        description="A description of the status of the adjudication.",
        # if property is element of this resource.
        element_property=True,
    )
    disposition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_disposition", title="Extension field for ``disposition``."
    )

    error: typing.List[fhirtypes.EligibilityResponseErrorType] = Field(
        None,
        alias="error",
        title="Processing errors",
        description="Mutually exclusive with Services Provided (Item).",
        # if property is element of this resource.
        element_property=True,
    )

    form: fhirtypes.CodeableConceptType = Field(
        None,
        alias="form",
        title="Printed Form Identifier",
        description="The form to be used for printing the content.",
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier",
        description="The Response business identifier.",
        # if property is element of this resource.
        element_property=True,
    )

    inforce: bool = Field(
        None,
        alias="inforce",
        title="Coverage inforce indicator",
        description=(
            "Flag indicating if the coverage provided is inforce currently  if no "
            "service date(s) specified or for the whole duration of the service "
            "dates."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    inforce__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_inforce", title="Extension field for ``inforce``."
    )

    insurance: typing.List[fhirtypes.EligibilityResponseInsuranceType] = Field(
        None,
        alias="insurance",
        title="Details by insurance coverage",
        description=(
            "The insurer may provide both the details for the requested coverage as"
            " well as details for additional coverages known to the insurer."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    insurer: fhirtypes.ReferenceType = Field(
        None,
        alias="insurer",
        title="Insurer issuing the coverage",
        description="The Insurer who produced this adjudicated response.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    outcome: fhirtypes.CodeableConceptType = Field(
        None,
        alias="outcome",
        title="complete | error | partial",
        description="Transaction status: error, complete.",
        # if property is element of this resource.
        element_property=True,
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title="Eligibility reference",
        description="Original request resource reference.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["EligibilityRequest"],
    )

    requestOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="requestOrganization",
        title="Responsible organization",
        description=(
            "The organization which is responsible for the services rendered to the"
            " patient."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    requestProvider: fhirtypes.ReferenceType = Field(
        None,
        alias="requestProvider",
        title="Responsible practitioner",
        description=(
            "The practitioner who is responsible for the services rendered to the "
            "patient."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="active | cancelled | draft | entered-in-error",
        description="The status of the resource instance.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "cancelled", "draft", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    resource_type = Field("EligibilityResponseError", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Error code detailing processing issues",
        description=(
            "An error code,from a specified code system, which details why the "
            "eligibility check could not be performed."
        ),
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("EligibilityResponseInsurance", const=True)

    benefitBalance: typing.List[
        fhirtypes.EligibilityResponseInsuranceBenefitBalanceType
    ] = Field(
        None,
        alias="benefitBalance",
        title="Benefits by Category",
        description="Benefits and optionally current balances by Category.",
        # if property is element of this resource.
        element_property=True,
    )

    contract: fhirtypes.ReferenceType = Field(
        None,
        alias="contract",
        title="Contract details",
        description="The contract resource which may provide more detailed information.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Contract"],
    )

    coverage: fhirtypes.ReferenceType = Field(
        None,
        alias="coverage",
        title="Updated Coverage details",
        description="A suite of updated or additional Coverages from the Insurer.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Coverage"],
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

    resource_type = Field("EligibilityResponseInsuranceBenefitBalance", const=True)

    category: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="category",
        title="Type of services covered",
        description="Dental, Vision, Medical, Pharmacy, Rehab etc.",
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Description of the benefit or services covered",
        description=(
            "A richer description of the benefit, for example 'DENT2 covers 100% of"
            " basic, 50% of major but exclused Ortho, Implants and Costmetic "
            "services'."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    excluded: bool = Field(
        None,
        alias="excluded",
        title="Excluded from the plan",
        description=(
            "True if the indicated class of service is excluded from the plan, "
            "missing or False indicated the service is included in the coverage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    excluded__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_excluded", title="Extension field for ``excluded``."
    )

    financial: typing.List[
        fhirtypes.EligibilityResponseInsuranceBenefitBalanceFinancialType
    ] = Field(
        None,
        alias="financial",
        title="Benefit Summary",
        description="Benefits Used to date.",
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Short name for the benefit",
        description="A short name or tag for the benefit, for example MED01, or DENT2.",
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    network: fhirtypes.CodeableConceptType = Field(
        None,
        alias="network",
        title="In or out of network",
        description="Network designation.",
        # if property is element of this resource.
        element_property=True,
    )

    subCategory: fhirtypes.CodeableConceptType = Field(
        None,
        alias="subCategory",
        title="Detailed services covered within the type",
        description="Dental: basic, major, ortho; Vision exam, glasses, contacts; etc.",
        # if property is element of this resource.
        element_property=True,
    )

    term: fhirtypes.CodeableConceptType = Field(
        None,
        alias="term",
        title="Annual or lifetime",
        description=(
            "The term or period of the values such as 'maximum lifetime benefit' or"
            " 'maximum annual vistis'."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    unit: fhirtypes.CodeableConceptType = Field(
        None,
        alias="unit",
        title="Individual or family",
        description="Unit designation: individual or family.",
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field(
        "EligibilityResponseInsuranceBenefitBalanceFinancial", const=True
    )

    allowedMoney: fhirtypes.MoneyType = Field(
        None,
        alias="allowedMoney",
        title="Benefits allowed",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e allowed[x]
        one_of_many="allowed",
        one_of_many_required=False,
    )

    allowedString: fhirtypes.String = Field(
        None,
        alias="allowedString",
        title="Benefits allowed",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e allowed[x]
        one_of_many="allowed",
        one_of_many_required=False,
    )
    allowedString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_allowedString", title="Extension field for ``allowedString``."
    )

    allowedUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="allowedUnsignedInt",
        title="Benefits allowed",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e allowed[x]
        one_of_many="allowed",
        one_of_many_required=False,
    )
    allowedUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_allowedUnsignedInt",
        title="Extension field for ``allowedUnsignedInt``.",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Deductable, visits, benefit amount",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    usedMoney: fhirtypes.MoneyType = Field(
        None,
        alias="usedMoney",
        title="Benefits used",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e used[x]
        one_of_many="used",
        one_of_many_required=False,
    )

    usedUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="usedUnsignedInt",
        title="Benefits used",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e used[x]
        one_of_many="used",
        one_of_many_required=False,
    )
    usedUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_5383(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values
