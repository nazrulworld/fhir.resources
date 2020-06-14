# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductManufactured
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import domainresource, fhirtypes


class MedicinalProductManufactured(domainresource.DomainResource):
    """ The manufactured item as contained in the packaged medicinal product.
    """

    resource_type = Field("MedicinalProductManufactured", const=True)

    ingredient: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="ingredient",
        title="List of `Reference` items referencing `MedicinalProductIngredient` (represented as `dict` in JSON)",
        description="Ingredient",
    )

    manufacturedDoseForm: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="manufacturedDoseForm",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Dose form as manufactured and before any transformation into the pharmaceutical product",
    )

    manufacturer: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="manufacturer",
        title="List of `Reference` items referencing `Organization` (represented as `dict` in JSON)",
        description='Manufacturer of the item (Note that this should be named "manufacturer" but it currently causes technical issues)',
    )

    otherCharacteristics: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="otherCharacteristics",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Other codeable characteristics",
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
        description='The quantity or "count number" of the manufactured item',
    )

    unitOfPresentation: fhirtypes.CodeableConceptType = Field(
        None,
        alias="unitOfPresentation",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The \u201creal world\u201d units in which the quantity of the manufactured item is described",
    )
