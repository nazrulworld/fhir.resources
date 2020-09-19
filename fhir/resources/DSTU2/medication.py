# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Medication
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""

from typing import List as ListType

from pydantic import Field

from . import fhirtypes
from .backboneelement import BackboneElement
from .domainresource import DomainResource


class Medication(DomainResource):
    """Definition of a Medication.

    This resource is primarily used for the identification and definition of a
    medication. It covers the ingredients and the packaging for a medication.
    """

    resource_type = Field("Medication", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Codes that identify this medication.",
    )

    isBrand: fhirtypes.Boolean = Field(
        None, alias="isBrand", title="Type `Boolean`.", description="True if a brand."
    )

    manufacturer: fhirtypes.ReferenceType = Field(
        None,
        alias="manufacturer",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON).",
        description="Manufacturer of the item.",
    )

    package: fhirtypes.MedicationPackageType = Field(
        None,
        alias="package",
        title="Type `MedicationPackage` (represented as `dict` in JSON).",
        description="Details about packaged medications.",
    )

    product: fhirtypes.MedicationProductType = Field(
        None,
        alias="product",
        title="Type `MedicationProduct` (represented as `dict` in JSON).",
        description="Administrable medication details.",
    )


class MedicationPackage(BackboneElement):
    """Details about packaged medications.

    Information that only applies to packages (not products).
    """

    resource_type = Field("MedicationPackage", const=True)

    container: fhirtypes.CodeableConceptType = Field(
        None,
        alias="container",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="E.g. box, vial, blister-pack.",
    )

    content: ListType[fhirtypes.MedicationPackageContentType] = Field(
        None,
        alias="content",
        title="List of `MedicationPackageContent` items (represented as `dict` in JSON).",
        description="What is  in the package.",
    )


class MedicationPackageContent(BackboneElement):
    """What is  in the package.

    A set of components that go to make up the described item.
    """

    resource_type = Field("MedicationPackageContent", const=True)

    amount: fhirtypes.QuantityType = Field(
        None,
        alias="amount",
        title="Type `Quantity` (represented as `dict` in JSON).",
        description="Quantity present in the package.",
    )

    item: fhirtypes.ReferenceType = Field(
        None,
        alias="item",
        title="Type `Reference` referencing `Medication` (represented as `dict` in JSON).",
        description="A product in the package.",
    )


class MedicationProduct(BackboneElement):
    """Administrable medication details.

    Information that only applies to products (not packages).
    """

    resource_type = Field("MedicationProduct", const=True)

    form: fhirtypes.CodeableConceptType = Field(
        None,
        alias="form",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="powder | tablets | carton +.",
    )
    batch: ListType[fhirtypes.MedicationProductBatchType] = Field(
        None,
        alias="batch",
        title="List of `MedicationProductBatch` items (represented as `dict` in JSON).",
        description=None,
    )

    ingredient: ListType[fhirtypes.MedicationProductIngredientType] = Field(
        None,
        alias="ingredient",
        title="List of `MedicationProductIngredient` items (represented as `dict` in JSON).",
        description="Active or inactive ingredient.",
    )


class MedicationProductBatch(BackboneElement):
    """None.

    Information about a group of medication produced or packaged from one
    production run.
    """

    resource_type = Field("MedicationProductBatch", const=True)

    expirationDate: fhirtypes.DateTime = Field(
        None, alias="expirationDate", title="Type `DateTime`.", description=None
    )
    lotNumber: fhirtypes.String = Field(
        None, alias="lotNumber", title="Type `String`.", description=None
    )


class MedicationProductIngredient(BackboneElement):
    """Active or inactive ingredient.

    Identifies a particular constituent of interest in the product.
    """

    resource_type = Field("MedicationProductIngredient", const=True)

    amount: fhirtypes.RatioType = Field(
        None,
        alias="amount",
        title="Type `Ratio` (represented as `dict` in JSON).",
        description="Quantity of ingredient present.",
    )

    item: fhirtypes.ReferenceType = Field(
        None,
        alias="item",
        title=(
            "Type `Reference` referencing "
            "`Substance, Medication` (represented as `dict` in JSON)."
        ),
        description="The product contained.",
    )
