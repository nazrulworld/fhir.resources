# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Medication
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Medication(domainresource.DomainResource):
    """ Definition of a Medication.
    This resource is primarily used for the identification and definition of a
    medication. It covers the ingredients and the packaging for a medication.
    """

    resource_type = Field("Medication", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Codes that identify this medication",
    )

    form: fhirtypes.CodeableConceptType = Field(
        None,
        alias="form",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="powder | tablets | capsule +",
    )

    image: ListType[fhirtypes.AttachmentType] = Field(
        None,
        alias="image",
        title="List of `Attachment` items (represented as `dict` in JSON)",
        description="Picture of the medication",
    )

    ingredient: ListType[fhirtypes.MedicationIngredientType] = Field(
        None,
        alias="ingredient",
        title="List of `MedicationIngredient` items (represented as `dict` in JSON)",
        description="Active or inactive ingredient",
    )

    isBrand: bool = Field(
        None, alias="isBrand", title="Type `bool`", description="True if a brand",
    )

    isOverTheCounter: bool = Field(
        None,
        alias="isOverTheCounter",
        title="Type `bool`",
        description="True if medication does not require a prescription",
    )

    manufacturer: fhirtypes.ReferenceType = Field(
        None,
        alias="manufacturer",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Manufacturer of the item",
    )

    package: fhirtypes.MedicationPackageType = Field(
        None,
        alias="package",
        title="Type `MedicationPackage` (represented as `dict` in JSON)",
        description="Details about packaged medications",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="active | inactive | entered-in-error",
    )


class MedicationIngredient(backboneelement.BackboneElement):
    """ Active or inactive ingredient.
    Identifies a particular constituent of interest in the product.
    """

    resource_type = Field("MedicationIngredient", const=True)

    amount: fhirtypes.RatioType = Field(
        None,
        alias="amount",
        title="Type `Ratio` (represented as `dict` in JSON)",
        description="Quantity of ingredient present",
    )

    isActive: bool = Field(
        None,
        alias="isActive",
        title="Type `bool`",
        description="Active ingredient indicator",
    )

    itemCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="itemCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The product contained",
        one_of_many="item",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    itemReference: fhirtypes.ReferenceType = Field(
        None,
        alias="itemReference",
        title="Type `Reference` referencing `Substance, Medication` (represented as `dict` in JSON)",
        description="The product contained",
        one_of_many="item",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
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
            "item": ["itemCodeableConcept", "itemReference",],
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


class MedicationPackage(backboneelement.BackboneElement):
    """ Details about packaged medications.
    Information that only applies to packages (not products).
    """

    resource_type = Field("MedicationPackage", const=True)

    batch: ListType[fhirtypes.MedicationPackageBatchType] = Field(
        None,
        alias="batch",
        title="List of `MedicationPackageBatch` items (represented as `dict` in JSON)",
        description="Identifies a single production run",
    )

    container: fhirtypes.CodeableConceptType = Field(
        None,
        alias="container",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="E.g. box, vial, blister-pack",
    )

    content: ListType[fhirtypes.MedicationPackageContentType] = Field(
        None,
        alias="content",
        title="List of `MedicationPackageContent` items (represented as `dict` in JSON)",
        description="What is  in the package",
    )


class MedicationPackageBatch(backboneelement.BackboneElement):
    """ Identifies a single production run.
    Information about a group of medication produced or packaged from one
    production run.
    """

    resource_type = Field("MedicationPackageBatch", const=True)

    expirationDate: fhirtypes.DateTime = Field(
        None,
        alias="expirationDate",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When batch will expire",
    )

    lotNumber: fhirtypes.String = Field(
        None,
        alias="lotNumber",
        title="Type `String` (represented as `dict` in JSON)",
        description="Identifier assigned to batch",
    )


class MedicationPackageContent(backboneelement.BackboneElement):
    """ What is  in the package.
    A set of components that go to make up the described item.
    """

    resource_type = Field("MedicationPackageContent", const=True)

    amount: fhirtypes.QuantityType = Field(
        None,
        alias="amount",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Quantity present in the package",
    )

    itemCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="itemCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The item in the package",
        one_of_many="item",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    itemReference: fhirtypes.ReferenceType = Field(
        None,
        alias="itemReference",
        title="Type `Reference` referencing `Medication` (represented as `dict` in JSON)",
        description="The item in the package",
        one_of_many="item",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
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
            "item": ["itemCodeableConcept", "itemReference",],
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
