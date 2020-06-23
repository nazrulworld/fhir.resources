# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductPackaged
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class MedicinalProductPackaged(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A medicinal product in a container or package.
    """

    resource_type = Field("MedicinalProductPackaged", const=True)

    batchIdentifier: ListType[
        fhirtypes.MedicinalProductPackagedBatchIdentifierType
    ] = Field(
        None,
        alias="batchIdentifier",
        title=(
            "List of `MedicinalProductPackagedBatchIdentifier` items (represented "
            "as `dict` in JSON)"
        ),
        description="Batch numbering",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Textual description",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Unique identifier",
    )

    legalStatusOfSupply: fhirtypes.CodeableConceptType = Field(
        None,
        alias="legalStatusOfSupply",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "The legal status of supply of the medicinal product as classified by "
            "the regulator"
        ),
    )

    manufacturer: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="manufacturer",
        title=(
            "List of `Reference` items referencing `Organization` (represented as "
            "`dict` in JSON)"
        ),
        description="Manufacturer of this Package Item",
    )

    marketingAuthorization: fhirtypes.ReferenceType = Field(
        None,
        alias="marketingAuthorization",
        title=(
            "Type `Reference` referencing `MedicinalProductAuthorization` "
            "(represented as `dict` in JSON)"
        ),
        description="Manufacturer of this Package Item",
    )

    marketingStatus: ListType[fhirtypes.MarketingStatusType] = Field(
        None,
        alias="marketingStatus",
        title="List of `MarketingStatus` items (represented as `dict` in JSON)",
        description="Marketing information",
    )

    packageItem: ListType[fhirtypes.MedicinalProductPackagedPackageItemType] = Field(
        ...,
        alias="packageItem",
        title=(
            "List of `MedicinalProductPackagedPackageItem` items (represented as "
            "`dict` in JSON)"
        ),
        description=(
            "A packaging item, as a contained for medicine, possibly with other "
            "packaging items within"
        ),
    )

    subject: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="subject",
        title=(
            "List of `Reference` items referencing `MedicinalProduct` (represented "
            "as `dict` in JSON)"
        ),
        description="The product with this is a pack for",
    )


class MedicinalProductPackagedBatchIdentifier(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Batch numbering.
    """

    resource_type = Field("MedicinalProductPackagedBatchIdentifier", const=True)

    immediatePackaging: fhirtypes.IdentifierType = Field(
        None,
        alias="immediatePackaging",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description=(
            "A number appearing on the immediate packaging (and not the outer "
            "packaging)"
        ),
    )

    outerPackaging: fhirtypes.IdentifierType = Field(
        ...,
        alias="outerPackaging",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="A number appearing on the outer packaging of a specific batch",
    )


class MedicinalProductPackagedPackageItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A packaging item, as a contained for medicine, possibly with other
    packaging items within.
    """

    resource_type = Field("MedicinalProductPackagedPackageItem", const=True)

    alternateMaterial: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="alternateMaterial",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="A possible alternate material for the packaging",
    )

    device: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="device",
        title=(
            "List of `Reference` items referencing `DeviceDefinition` (represented "
            "as `dict` in JSON)"
        ),
        description="A device accompanying a medicinal product",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Including possibly Data Carrier Identifier",
    )

    manufacturedItem: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="manufacturedItem",
        title=(
            "List of `Reference` items referencing `MedicinalProductManufactured` "
            "(represented as `dict` in JSON)"
        ),
        description="The manufactured item as contained in the packaged medicinal product",
    )

    manufacturer: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="manufacturer",
        title=(
            "List of `Reference` items referencing `Organization` (represented as "
            "`dict` in JSON)"
        ),
        description="Manufacturer of this Package Item",
    )

    material: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="material",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Material type of the package item",
    )

    otherCharacteristics: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="otherCharacteristics",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Other codeable characteristics",
    )

    packageItem: ListType[fhirtypes.MedicinalProductPackagedPackageItemType] = Field(
        None,
        alias="packageItem",
        title=(
            "List of `MedicinalProductPackagedPackageItem` items (represented as "
            "`dict` in JSON)"
        ),
        description="Allows containers within containers",
    )

    physicalCharacteristics: fhirtypes.ProdCharacteristicType = Field(
        None,
        alias="physicalCharacteristics",
        title="Type `ProdCharacteristic` (represented as `dict` in JSON)",
        description="Dimensions, color etc.",
    )

    quantity: fhirtypes.QuantityType = Field(
        ...,
        alias="quantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description=(
            "The quantity of this package in the medicinal product, at the current "
            "level of packaging. The outermost is always 1"
        ),
    )

    shelfLifeStorage: ListType[fhirtypes.ProductShelfLifeType] = Field(
        None,
        alias="shelfLifeStorage",
        title="List of `ProductShelfLife` items (represented as `dict` in JSON)",
        description="Shelf Life and storage information",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The physical type of the container of the medicine",
    )
