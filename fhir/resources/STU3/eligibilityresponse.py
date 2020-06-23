# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EligibilityResponse
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class EligibilityResponse(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    EligibilityResponse resource.
    This resource provides eligibility and plan details from the processing of
    an Eligibility resource.
    """

    resource_type = Field("EligibilityResponse", const=True)

    created: fhirtypes.DateTime = Field(
        None, alias="created", title="Type `DateTime`", description="Creation date"
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

    error: ListType[fhirtypes.EligibilityResponseErrorType] = Field(
        None,
        alias="error",
        title=(
            "List of `EligibilityResponseError` items (represented as `dict` in "
            "JSON)"
        ),
        description="Processing errors",
    )

    form: fhirtypes.CodeableConceptType = Field(
        None,
        alias="form",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Printed Form Identifier",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business Identifier",
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

    insurance: ListType[fhirtypes.EligibilityResponseInsuranceType] = Field(
        None,
        alias="insurance",
        title=(
            "List of `EligibilityResponseInsurance` items (represented as `dict` in"
            " JSON)"
        ),
        description="Details by insurance coverage",
    )

    insurer: fhirtypes.ReferenceType = Field(
        None,
        alias="insurer",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Insurer issuing the coverage",
    )

    outcome: fhirtypes.CodeableConceptType = Field(
        None,
        alias="outcome",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="complete | error | partial",
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title=(
            "Type `Reference` referencing `EligibilityRequest` (represented as "
            "`dict` in JSON)"
        ),
        description="Eligibility reference",
    )

    requestOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="requestOrganization",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Responsible organization",
    )

    requestProvider: fhirtypes.ReferenceType = Field(
        None,
        alias="requestProvider",
        title=(
            "Type `Reference` referencing `Practitioner` (represented as `dict` in "
            "JSON)"
        ),
        description="Responsible practitioner",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code`",
        description="active | cancelled | draft | entered-in-error",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )


class EligibilityResponseError(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Processing errors.
    Mutually exclusive with Services Provided (Item).
    """

    resource_type = Field("EligibilityResponseError", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Error code detailing processing issues",
    )


class EligibilityResponseInsurance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details by insurance coverage.
    The insurer may provide both the details for the requested coverage as well
    as details for additional coverages known to the insurer.
    """

    resource_type = Field("EligibilityResponseInsurance", const=True)

    benefitBalance: ListType[
        fhirtypes.EligibilityResponseInsuranceBenefitBalanceType
    ] = Field(
        None,
        alias="benefitBalance",
        title=(
            "List of `EligibilityResponseInsuranceBenefitBalance` items "
            "(represented as `dict` in JSON)"
        ),
        description="Benefits by Category",
    )

    contract: fhirtypes.ReferenceType = Field(
        None,
        alias="contract",
        title=(
            "Type `Reference` referencing `Contract` (represented as `dict` in " "JSON)"
        ),
        description="Contract details",
    )

    coverage: fhirtypes.ReferenceType = Field(
        None,
        alias="coverage",
        title=(
            "Type `Reference` referencing `Coverage` (represented as `dict` in " "JSON)"
        ),
        description="Updated Coverage details",
    )


class EligibilityResponseInsuranceBenefitBalance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Benefits by Category.
    Benefits and optionally current balances by Category.
    """

    resource_type = Field("EligibilityResponseInsuranceBenefitBalance", const=True)

    category: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of services covered",
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

    financial: ListType[
        fhirtypes.EligibilityResponseInsuranceBenefitBalanceFinancialType
    ] = Field(
        None,
        alias="financial",
        title=(
            "List of `EligibilityResponseInsuranceBenefitBalanceFinancial` items "
            "(represented as `dict` in JSON)"
        ),
        description="Benefit Summary",
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

    subCategory: fhirtypes.CodeableConceptType = Field(
        None,
        alias="subCategory",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Detailed services covered within the type",
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


class EligibilityResponseInsuranceBenefitBalanceFinancial(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
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
        description="Deductable, visits, benefit amount",
    )

    usedMoney: fhirtypes.MoneyType = Field(
        None,
        alias="usedMoney",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Benefits used",
        one_of_many="used",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
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
