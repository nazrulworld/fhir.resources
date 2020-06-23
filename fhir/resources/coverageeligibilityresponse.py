# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CoverageEligibilityResponse
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType
from typing import Union

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class CoverageEligibilityResponse(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    CoverageEligibilityResponse resource.
    This resource provides eligibility and plan details from the processing of
    an CoverageEligibilityRequest resource.
    """

    resource_type = Field("CoverageEligibilityResponse", const=True)

    created: fhirtypes.DateTime = Field(
        ...,
        alias="created",
        title="Type `DateTime`",
        description="Response creation date",
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
    )

    disposition: fhirtypes.String = Field(
        None,
        alias="disposition",
        title="Type `String`",
        description="Disposition Message",
    )
    disposition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_disposition", title="Extension field for ``disposition``."
    )

    error: ListType[fhirtypes.CoverageEligibilityResponseErrorType] = Field(
        None,
        alias="error",
        title=(
            "List of `CoverageEligibilityResponseError` items (represented as "
            "`dict` in JSON)"
        ),
        description="Processing errors",
    )

    form: fhirtypes.CodeableConceptType = Field(
        None,
        alias="form",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Printed form identifier",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business Identifier for coverage eligiblity request",
    )

    insurance: ListType[fhirtypes.CoverageEligibilityResponseInsuranceType] = Field(
        None,
        alias="insurance",
        title=(
            "List of `CoverageEligibilityResponseInsurance` items (represented as "
            "`dict` in JSON)"
        ),
        description="Patient insurance information",
    )

    insurer: fhirtypes.ReferenceType = Field(
        ...,
        alias="insurer",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Coverage issuer",
    )

    outcome: fhirtypes.Code = Field(
        ...,
        alias="outcome",
        title="Type `Code`",
        description="queued | complete | error | partial",
    )
    outcome__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_outcome", title="Extension field for ``outcome``."
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="Intended recipient of products and services",
    )

    preAuthRef: fhirtypes.String = Field(
        None,
        alias="preAuthRef",
        title="Type `String`",
        description="Preauthorization reference",
    )
    preAuthRef__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_preAuthRef", title="Extension field for ``preAuthRef``."
    )

    purpose: ListType[fhirtypes.Code] = Field(
        ...,
        alias="purpose",
        title="List of `Code` items",
        description="auth-requirements | benefits | discovery | validation",
    )
    purpose__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    request: fhirtypes.ReferenceType = Field(
        ...,
        alias="request",
        title=(
            "Type `Reference` referencing `CoverageEligibilityRequest` (represented"
            " as `dict` in JSON)"
        ),
        description="Eligibility request reference",
    )

    requestor: fhirtypes.ReferenceType = Field(
        None,
        alias="requestor",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole, "
            "Organization` (represented as `dict` in JSON)"
        ),
        description="Party responsible for the request",
    )

    servicedDate: fhirtypes.Date = Field(
        None,
        alias="servicedDate",
        title="Type `Date`",
        description="Estimated date or dates of service",
        one_of_many="serviced",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    servicedDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_servicedDate", title="Extension field for ``servicedDate``."
    )

    servicedPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="servicedPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Estimated date or dates of service",
        one_of_many="serviced",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`",
        description="active | cancelled | draft | entered-in-error",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    @root_validator(pre=True)
    def validate_one_of_many(cls, values: Dict[str, Any]) -> Dict[str, Any]:
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


class CoverageEligibilityResponseError(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Processing errors.
    Errors encountered during the processing of the request.
    """

    resource_type = Field("CoverageEligibilityResponseError", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Error code detailing processing issues",
    )


class CoverageEligibilityResponseInsurance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Patient insurance information.
    Financial instruments for reimbursement for the health care products and
    services.
    """

    resource_type = Field("CoverageEligibilityResponseInsurance", const=True)

    benefitPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="benefitPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When the benefits are applicable",
    )

    coverage: fhirtypes.ReferenceType = Field(
        ...,
        alias="coverage",
        title=(
            "Type `Reference` referencing `Coverage` (represented as `dict` in " "JSON)"
        ),
        description="Insurance information",
    )

    inforce: bool = Field(
        None,
        alias="inforce",
        title="Type `bool`",
        description="Coverage inforce indicator",
    )
    inforce__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_inforce", title="Extension field for ``inforce``."
    )

    item: ListType[fhirtypes.CoverageEligibilityResponseInsuranceItemType] = Field(
        None,
        alias="item",
        title=(
            "List of `CoverageEligibilityResponseInsuranceItem` items (represented "
            "as `dict` in JSON)"
        ),
        description="Benefits and authorization details",
    )


class CoverageEligibilityResponseInsuranceItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Benefits and authorization details.
    Benefits and optionally current balances, and authorization details by
    category or service.
    """

    resource_type = Field("CoverageEligibilityResponseInsuranceItem", const=True)

    authorizationRequired: bool = Field(
        None,
        alias="authorizationRequired",
        title="Type `bool`",
        description="Authorization required flag",
    )
    authorizationRequired__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_authorizationRequired",
        title="Extension field for ``authorizationRequired``.",
    )

    authorizationSupporting: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="authorizationSupporting",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Type of required supporting materials",
    )

    authorizationUrl: fhirtypes.Uri = Field(
        None,
        alias="authorizationUrl",
        title="Type `Uri`",
        description="Preauthorization requirements endpoint",
    )
    authorizationUrl__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_authorizationUrl",
        title="Extension field for ``authorizationUrl``.",
    )

    benefit: ListType[
        fhirtypes.CoverageEligibilityResponseInsuranceItemBenefitType
    ] = Field(
        None,
        alias="benefit",
        title=(
            "List of `CoverageEligibilityResponseInsuranceItemBenefit` items "
            "(represented as `dict` in JSON)"
        ),
        description="Benefit Summary",
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Benefit classification",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Description of the benefit or services covered",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    excluded: bool = Field(
        None,
        alias="excluded",
        title="Type `bool`",
        description="Excluded from the plan",
    )
    excluded__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_excluded", title="Extension field for ``excluded``."
    )

    modifier: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="modifier",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Product or service billing modifiers",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`",
        description="Short name for the benefit",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    network: fhirtypes.CodeableConceptType = Field(
        None,
        alias="network",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="In or out of network",
    )

    productOrService: fhirtypes.CodeableConceptType = Field(
        None,
        alias="productOrService",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Billing, service, product, or drug code",
    )

    provider: fhirtypes.ReferenceType = Field(
        None,
        alias="provider",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole` "
            "(represented as `dict` in JSON)"
        ),
        description="Performing practitioner",
    )

    term: fhirtypes.CodeableConceptType = Field(
        None,
        alias="term",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Annual or lifetime",
    )

    unit: fhirtypes.CodeableConceptType = Field(
        None,
        alias="unit",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Individual or family",
    )


class CoverageEligibilityResponseInsuranceItemBenefit(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Benefit Summary.
    Benefits used to date.
    """

    resource_type = Field("CoverageEligibilityResponseInsuranceItemBenefit", const=True)

    allowedMoney: fhirtypes.MoneyType = Field(
        None,
        alias="allowedMoney",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Benefits allowed",
        one_of_many="allowed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    allowedString: fhirtypes.String = Field(
        None,
        alias="allowedString",
        title="Type `String`",
        description="Benefits allowed",
        one_of_many="allowed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    allowedString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_allowedString", title="Extension field for ``allowedString``."
    )

    allowedUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="allowedUnsignedInt",
        title="Type `UnsignedInt`",
        description="Benefits allowed",
        one_of_many="allowed",  # Choice of Data Types. i.e value[x]
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
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Benefit classification",
    )

    usedMoney: fhirtypes.MoneyType = Field(
        None,
        alias="usedMoney",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Benefits used",
        one_of_many="used",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    usedString: fhirtypes.String = Field(
        None,
        alias="usedString",
        title="Type `String`",
        description="Benefits used",
        one_of_many="used",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    usedString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_usedString", title="Extension field for ``usedString``."
    )

    usedUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="usedUnsignedInt",
        title="Type `UnsignedInt`",
        description="Benefits used",
        one_of_many="used",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    usedUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_usedUnsignedInt", title="Extension field for ``usedUnsignedInt``."
    )

    @root_validator(pre=True)
    def validate_one_of_many(cls, values: Dict[str, Any]) -> Dict[str, Any]:
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
