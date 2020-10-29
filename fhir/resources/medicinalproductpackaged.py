# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductPackaged
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class MedicinalProductPackaged(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A medicinal product in a container or package.
    """

    resource_type = Field("MedicinalProductPackaged", const=True)

    batchIdentifier: typing.List[
        fhirtypes.MedicinalProductPackagedBatchIdentifierType
    ] = Field(
        None,
        alias="batchIdentifier",
        title="Batch numbering",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Textual description",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Unique identifier",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    legalStatusOfSupply: fhirtypes.CodeableConceptType = Field(
        None,
        alias="legalStatusOfSupply",
        title=(
            "The legal status of supply of the medicinal product as classified by "
            "the regulator"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    manufacturer: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="manufacturer",
        title="Manufacturer of this Package Item",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    marketingAuthorization: fhirtypes.ReferenceType = Field(
        None,
        alias="marketingAuthorization",
        title="Manufacturer of this Package Item",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicinalProductAuthorization"],
    )

    marketingStatus: typing.List[fhirtypes.MarketingStatusType] = Field(
        None,
        alias="marketingStatus",
        title="Marketing information",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    packageItem: typing.List[fhirtypes.MedicinalProductPackagedPackageItemType] = Field(
        ...,
        alias="packageItem",
        title=(
            "A packaging item, as a contained for medicine, possibly with other "
            "packaging items within"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    subject: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="subject",
        title="The product with this is a pack for",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicinalProduct"],
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
        title=(
            "A number appearing on the immediate packaging (and not the outer "
            "packaging)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    outerPackaging: fhirtypes.IdentifierType = Field(
        ...,
        alias="outerPackaging",
        title="A number appearing on the outer packaging of a specific batch",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class MedicinalProductPackagedPackageItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A packaging item, as a contained for medicine, possibly with other
    packaging items within.
    """

    resource_type = Field("MedicinalProductPackagedPackageItem", const=True)

    alternateMaterial: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="alternateMaterial",
        title="A possible alternate material for the packaging",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    device: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="device",
        title="A device accompanying a medicinal product",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DeviceDefinition"],
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Including possibly Data Carrier Identifier",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    manufacturedItem: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="manufacturedItem",
        title="The manufactured item as contained in the packaged medicinal product",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicinalProductManufactured"],
    )

    manufacturer: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="manufacturer",
        title="Manufacturer of this Package Item",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    material: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="material",
        title="Material type of the package item",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    otherCharacteristics: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="otherCharacteristics",
        title="Other codeable characteristics",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    packageItem: typing.List[fhirtypes.MedicinalProductPackagedPackageItemType] = Field(
        None,
        alias="packageItem",
        title="Allows containers within containers",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    physicalCharacteristics: fhirtypes.ProdCharacteristicType = Field(
        None,
        alias="physicalCharacteristics",
        title="Dimensions, color etc.",
        description="Dimensions, color etc.",
        # if property is element of this resource.
        element_property=True,
    )

    quantity: fhirtypes.QuantityType = Field(
        ...,
        alias="quantity",
        title=(
            "The quantity of this package in the medicinal product, at the current "
            "level of packaging. The outermost is always 1"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    shelfLifeStorage: typing.List[fhirtypes.ProductShelfLifeType] = Field(
        None,
        alias="shelfLifeStorage",
        title="Shelf Life and storage information",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="The physical type of the container of the medicine",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
