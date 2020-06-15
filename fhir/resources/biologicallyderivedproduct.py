# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/BiologicallyDerivedProduct
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class BiologicallyDerivedProduct(domainresource.DomainResource):
    """ A material substance originating from a biological entity.
    A material substance originating from a biological entity intended to be
    transplanted or infused
    into another (possibly the same) biological entity.
    """

    resource_type = Field("BiologicallyDerivedProduct", const=True)

    collection: fhirtypes.BiologicallyDerivedProductCollectionType = Field(
        None,
        alias="collection",
        title=(
            "Type `BiologicallyDerivedProductCollection` (represented as `dict` in "
            "JSON)"
        ),
        description="How this product was collected",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="External ids for this item",
    )

    manipulation: fhirtypes.BiologicallyDerivedProductManipulationType = Field(
        None,
        alias="manipulation",
        title=(
            "Type `BiologicallyDerivedProductManipulation` (represented as `dict` "
            "in JSON)"
        ),
        description="Any manipulation of product post-collection",
    )

    parent: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="parent",
        title=(
            "List of `Reference` items referencing `BiologicallyDerivedProduct` "
            "(represented as `dict` in JSON)"
        ),
        description="BiologicallyDerivedProduct parent",
    )

    processing: ListType[fhirtypes.BiologicallyDerivedProductProcessingType] = Field(
        None,
        alias="processing",
        title=(
            "List of `BiologicallyDerivedProductProcessing` items (represented as "
            "`dict` in JSON)"
        ),
        description="Any processing of the product during collection",
    )

    productCategory: fhirtypes.Code = Field(
        None,
        alias="productCategory",
        title="Type `Code` (represented as `dict` in JSON)",
        description="organ | tissue | fluid | cells | biologicalAgent",
    )

    productCode: fhirtypes.CodeableConceptType = Field(
        None,
        alias="productCode",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="What this biologically derived product is",
    )

    quantity: fhirtypes.Integer = Field(
        None,
        alias="quantity",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="The amount of this biologically derived product",
    )

    request: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="request",
        title=(
            "List of `Reference` items referencing `ServiceRequest` (represented as"
            " `dict` in JSON)"
        ),
        description="Procedure request",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="available | unavailable",
    )

    storage: ListType[fhirtypes.BiologicallyDerivedProductStorageType] = Field(
        None,
        alias="storage",
        title=(
            "List of `BiologicallyDerivedProductStorage` items (represented as "
            "`dict` in JSON)"
        ),
        description="Product storage",
    )


class BiologicallyDerivedProductCollection(backboneelement.BackboneElement):
    """ How this product was collected.
    """

    resource_type = Field("BiologicallyDerivedProductCollection", const=True)

    collectedDateTime: fhirtypes.DateTime = Field(
        None,
        alias="collectedDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Time of product collection",
        one_of_many="collected",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    collectedPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="collectedPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Time of product collection",
        one_of_many="collected",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    collector: fhirtypes.ReferenceType = Field(
        None,
        alias="collector",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole` "
            "(represented as `dict` in JSON)"
        ),
        description="Individual performing collection",
    )

    source: fhirtypes.ReferenceType = Field(
        None,
        alias="source",
        title=(
            "Type `Reference` referencing `Patient, Organization` (represented as "
            "`dict` in JSON)"
        ),
        description="Who is product from",
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
        one_of_many_fields = {"collected": ["collectedDateTime", "collectedPeriod"]}
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


class BiologicallyDerivedProductManipulation(backboneelement.BackboneElement):
    """ Any manipulation of product post-collection.
    Any manipulation of product post-collection that is intended to alter the
    product.  For example a buffy-coat enrichment or CD8 reduction of
    Peripheral Blood Stem Cells to make it more suitable for infusion.
    """

    resource_type = Field("BiologicallyDerivedProductManipulation", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Description of manipulation",
    )

    timeDateTime: fhirtypes.DateTime = Field(
        None,
        alias="timeDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Time of manipulation",
        one_of_many="time",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    timePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="timePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Time of manipulation",
        one_of_many="time",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
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
        one_of_many_fields = {"time": ["timeDateTime", "timePeriod"]}
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


class BiologicallyDerivedProductProcessing(backboneelement.BackboneElement):
    """ Any processing of the product during collection.
    Any processing of the product during collection that does not change the
    fundamental nature of the product. For example adding anti-coagulants
    during the collection of Peripheral Blood Stem Cells.
    """

    resource_type = Field("BiologicallyDerivedProductProcessing", const=True)

    additive: fhirtypes.ReferenceType = Field(
        None,
        alias="additive",
        title=(
            "Type `Reference` referencing `Substance` (represented as `dict` in "
            "JSON)"
        ),
        description="Substance added during processing",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Description of of processing",
    )

    procedure: fhirtypes.CodeableConceptType = Field(
        None,
        alias="procedure",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Procesing code",
    )

    timeDateTime: fhirtypes.DateTime = Field(
        None,
        alias="timeDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Time of processing",
        one_of_many="time",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    timePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="timePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Time of processing",
        one_of_many="time",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
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
        one_of_many_fields = {"time": ["timeDateTime", "timePeriod"]}
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


class BiologicallyDerivedProductStorage(backboneelement.BackboneElement):
    """ Product storage.
    """

    resource_type = Field("BiologicallyDerivedProductStorage", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Description of storage",
    )

    duration: fhirtypes.PeriodType = Field(
        None,
        alias="duration",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Storage timeperiod",
    )

    scale: fhirtypes.Code = Field(
        None,
        alias="scale",
        title="Type `Code` (represented as `dict` in JSON)",
        description="farenheit | celsius | kelvin",
    )

    temperature: fhirtypes.Decimal = Field(
        None,
        alias="temperature",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Storage temperature",
    )
