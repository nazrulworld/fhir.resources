# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Medication
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Medication(domainresource.DomainResource):
    """ Definition of a Medication.
    This resource is primarily used for the identification and definition of a
    medication for the purposes of prescribing, dispensing, and administering a
    medication as well as for making statements about medication use.
    """

    resource_type = Field("Medication", const=True)

    amount: fhirtypes.RatioType = Field(
        None,
        alias="amount",
        title="Type `Ratio` (represented as `dict` in JSON)",
        description="Amount of drug in package",
    )

    batch: fhirtypes.MedicationBatchType = Field(
        None,
        alias="batch",
        title="Type `MedicationBatch` (represented as `dict` in JSON)",
        description="Details about packaged medications",
    )

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

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business identifier for this medication",
    )

    ingredient: ListType[fhirtypes.MedicationIngredientType] = Field(
        None,
        alias="ingredient",
        title="List of `MedicationIngredient` items (represented as `dict` in JSON)",
        description="Active or inactive ingredient",
    )

    manufacturer: fhirtypes.ReferenceType = Field(
        None,
        alias="manufacturer",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Manufacturer of the item",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="active | inactive | entered-in-error",
    )


class MedicationBatch(backboneelement.BackboneElement):
    """ Details about packaged medications.
    Information that only applies to packages (not products).
    """

    resource_type = Field("MedicationBatch", const=True)

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


class MedicationIngredient(backboneelement.BackboneElement):
    """ Active or inactive ingredient.
    Identifies a particular constituent of interest in the product.
    """

    resource_type = Field("MedicationIngredient", const=True)

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
        description="The actual ingredient or content",
        one_of_many="item",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    itemReference: fhirtypes.ReferenceType = Field(
        None,
        alias="itemReference",
        title=(
            "Type `Reference` referencing `Substance, Medication` (represented as "
            "`dict` in JSON)"
        ),
        description="The actual ingredient or content",
        one_of_many="item",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    strength: fhirtypes.RatioType = Field(
        None,
        alias="strength",
        title="Type `Ratio` (represented as `dict` in JSON)",
        description="Quantity of ingredient present",
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
        one_of_many_fields = {"item": ["itemCodeableConcept", "itemReference"]}
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
