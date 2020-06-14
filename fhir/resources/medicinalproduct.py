# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProduct
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class MedicinalProduct(domainresource.DomainResource):
    """ Detailed definition of a medicinal product, typically for uses other than
    direct patient care (e.g. regulatory use).
    """

    resource_type = Field("MedicinalProduct", const=True)

    additionalMonitoringIndicator: fhirtypes.CodeableConceptType = Field(
        None,
        alias="additionalMonitoringIndicator",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Whether the Medicinal Product is subject to additional monitoring for regulatory reasons",
    )

    attachedDocument: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="attachedDocument",
        title="List of `Reference` items referencing `DocumentReference` (represented as `dict` in JSON)",
        description="Supporting documentation, typically for regulatory submission",
    )

    clinicalTrial: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="clinicalTrial",
        title="List of `Reference` items referencing `ResearchStudy` (represented as `dict` in JSON)",
        description="Clinical trials or studies that this product is involved in",
    )

    combinedPharmaceuticalDoseForm: fhirtypes.CodeableConceptType = Field(
        None,
        alias="combinedPharmaceuticalDoseForm",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The dose form for a single part product, or combined form of a multiple part product",
    )

    contact: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="contact",
        title="List of `Reference` items referencing `Organization, PractitionerRole` (represented as `dict` in JSON)",
        description="A product specific contact, person (in a role), or an organization",
    )

    crossReference: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="crossReference",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Reference to another product, e.g. for linking authorised to investigational product",
    )

    domain: fhirtypes.CodingType = Field(
        None,
        alias="domain",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="If this medicine applies to human or veterinary uses",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business identifier for this product. Could be an MPID",
    )

    legalStatusOfSupply: fhirtypes.CodeableConceptType = Field(
        None,
        alias="legalStatusOfSupply",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The legal status of supply of the medicinal product as classified by the regulator",
    )

    manufacturingBusinessOperation: ListType[
        fhirtypes.MedicinalProductManufacturingBusinessOperationType
    ] = Field(
        None,
        alias="manufacturingBusinessOperation",
        title="List of `MedicinalProductManufacturingBusinessOperation` items (represented as `dict` in JSON)",
        description="An operation applied to the product, for manufacturing or adminsitrative purpose",
    )

    marketingStatus: ListType[fhirtypes.MarketingStatusType] = Field(
        None,
        alias="marketingStatus",
        title="List of `MarketingStatus` items (represented as `dict` in JSON)",
        description="Marketing status of the medicinal product, in contrast to marketing authorizaton",
    )

    masterFile: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="masterFile",
        title="List of `Reference` items referencing `DocumentReference` (represented as `dict` in JSON)",
        description="A master file for to the medicinal product (e.g. Pharmacovigilance System Master File)",
    )

    name: ListType[fhirtypes.MedicinalProductNameType] = Field(
        ...,
        alias="name",
        title="List of `MedicinalProductName` items (represented as `dict` in JSON)",
        description="The product\u0027s name, including full name and possibly coded parts",
    )

    packagedMedicinalProduct: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="packagedMedicinalProduct",
        title="List of `Reference` items referencing `MedicinalProductPackaged` (represented as `dict` in JSON)",
        description="Package representation for the product",
    )

    paediatricUseIndicator: fhirtypes.CodeableConceptType = Field(
        None,
        alias="paediatricUseIndicator",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="If authorised for use in children",
    )

    pharmaceuticalProduct: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="pharmaceuticalProduct",
        title="List of `Reference` items referencing `MedicinalProductPharmaceutical` (represented as `dict` in JSON)",
        description="Pharmaceutical aspects of product",
    )

    productClassification: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="productClassification",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Allows the product to be classified by various systems",
    )

    specialDesignation: ListType[
        fhirtypes.MedicinalProductSpecialDesignationType
    ] = Field(
        None,
        alias="specialDesignation",
        title="List of `MedicinalProductSpecialDesignation` items (represented as `dict` in JSON)",
        description="Indicates if the medicinal product has an orphan designation for the treatment of a rare disease",
    )

    specialMeasures: ListType[fhirtypes.String] = Field(
        None,
        alias="specialMeasures",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Whether the Medicinal Product is subject to special measures for regulatory reasons",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Regulatory type, e.g. Investigational or Authorized",
    )


class MedicinalProductManufacturingBusinessOperation(backboneelement.BackboneElement):
    """ An operation applied to the product, for manufacturing or adminsitrative
    purpose.
    """

    resource_type = Field("MedicinalProductManufacturingBusinessOperation", const=True)

    authorisationReferenceNumber: fhirtypes.IdentifierType = Field(
        None,
        alias="authorisationReferenceNumber",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Regulatory authorization reference number",
    )

    confidentialityIndicator: fhirtypes.CodeableConceptType = Field(
        None,
        alias="confidentialityIndicator",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="To indicate if this proces is commercially confidential",
    )

    effectiveDate: fhirtypes.DateTime = Field(
        None,
        alias="effectiveDate",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Regulatory authorization date",
    )

    manufacturer: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="manufacturer",
        title="List of `Reference` items referencing `Organization` (represented as `dict` in JSON)",
        description="The manufacturer or establishment associated with the process",
    )

    operationType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="operationType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The type of manufacturing operation",
    )

    regulator: fhirtypes.ReferenceType = Field(
        None,
        alias="regulator",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="A regulator which oversees the operation",
    )


class MedicinalProductName(backboneelement.BackboneElement):
    """ The product's name, including full name and possibly coded parts.
    """

    resource_type = Field("MedicinalProductName", const=True)

    countryLanguage: ListType[
        fhirtypes.MedicinalProductNameCountryLanguageType
    ] = Field(
        None,
        alias="countryLanguage",
        title="List of `MedicinalProductNameCountryLanguage` items (represented as `dict` in JSON)",
        description="Country where the name applies",
    )

    namePart: ListType[fhirtypes.MedicinalProductNameNamePartType] = Field(
        None,
        alias="namePart",
        title="List of `MedicinalProductNameNamePart` items (represented as `dict` in JSON)",
        description="Coding words or phrases of the name",
    )

    productName: fhirtypes.String = Field(
        ...,
        alias="productName",
        title="Type `String` (represented as `dict` in JSON)",
        description="The full product name",
    )


class MedicinalProductNameCountryLanguage(backboneelement.BackboneElement):
    """ Country where the name applies.
    """

    resource_type = Field("MedicinalProductNameCountryLanguage", const=True)

    country: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="country",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Country code for where this name applies",
    )

    jurisdiction: fhirtypes.CodeableConceptType = Field(
        None,
        alias="jurisdiction",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Jurisdiction code for where this name applies",
    )

    language: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="language",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Language code for this name",
    )


class MedicinalProductNameNamePart(backboneelement.BackboneElement):
    """ Coding words or phrases of the name.
    """

    resource_type = Field("MedicinalProductNameNamePart", const=True)

    part: fhirtypes.String = Field(
        ...,
        alias="part",
        title="Type `String` (represented as `dict` in JSON)",
        description="A fragment of a product name",
    )

    type: fhirtypes.CodingType = Field(
        ...,
        alias="type",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Idenifying type for this part of the name (e.g. strength part)",
    )


class MedicinalProductSpecialDesignation(backboneelement.BackboneElement):
    """ Indicates if the medicinal product has an orphan designation for the
    treatment of a rare disease.
    """

    resource_type = Field("MedicinalProductSpecialDesignation", const=True)

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date when the designation was granted",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Identifier for the designation, or procedure number",
    )

    indicationCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="indicationCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Condition for which the medicinal use applies",
        one_of_many="indication",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    indicationReference: fhirtypes.ReferenceType = Field(
        None,
        alias="indicationReference",
        title="Type `Reference` referencing `MedicinalProductIndication` (represented as `dict` in JSON)",
        description="Condition for which the medicinal use applies",
        one_of_many="indication",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    intendedUse: fhirtypes.CodeableConceptType = Field(
        None,
        alias="intendedUse",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The intended use of the product, e.g. prevention, treatment",
    )

    species: fhirtypes.CodeableConceptType = Field(
        None,
        alias="species",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Animal species for which this applies",
    )

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="For example granted, pending, expired or withdrawn",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The type of special designation, e.g. orphan drug, minor use",
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
            "indication": ["indicationCodeableConcept", "indicationReference",],
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
