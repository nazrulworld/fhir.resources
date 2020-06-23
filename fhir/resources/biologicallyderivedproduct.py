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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A material substance originating from a biological entity.
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
        title="Type `Code`",
        description="organ | tissue | fluid | cells | biologicalAgent",
    )
    productCategory__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_productCategory", title="Extension field for ``productCategory``."
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
        title="Type `Integer`",
        description="The amount of this biologically derived product",
    )
    quantity__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_quantity", title="Extension field for ``quantity``."
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
        None, alias="status", title="Type `Code`", description="available | unavailable"
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    How this product was collected.
    """

    resource_type = Field("BiologicallyDerivedProductCollection", const=True)

    collectedDateTime: fhirtypes.DateTime = Field(
        None,
        alias="collectedDateTime",
        title="Type `DateTime`",
        description="Time of product collection",
        one_of_many="collected",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    collectedDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_collectedDateTime",
        title="Extension field for ``collectedDateTime``.",
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Any manipulation of product post-collection.
    Any manipulation of product post-collection that is intended to alter the
    product.  For example a buffy-coat enrichment or CD8 reduction of
    Peripheral Blood Stem Cells to make it more suitable for infusion.
    """

    resource_type = Field("BiologicallyDerivedProductManipulation", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Description of manipulation",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    timeDateTime: fhirtypes.DateTime = Field(
        None,
        alias="timeDateTime",
        title="Type `DateTime`",
        description="Time of manipulation",
        one_of_many="time",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    timeDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_timeDateTime", title="Extension field for ``timeDateTime``."
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Any processing of the product during collection.
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
        title="Type `String`",
        description="Description of of processing",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
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
        title="Type `DateTime`",
        description="Time of processing",
        one_of_many="time",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    timeDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_timeDateTime", title="Extension field for ``timeDateTime``."
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Product storage.
    """

    resource_type = Field("BiologicallyDerivedProductStorage", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Description of storage",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
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
        title="Type `Code`",
        description="farenheit | celsius | kelvin",
    )
    scale__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_scale", title="Extension field for ``scale``."
    )

    temperature: fhirtypes.Decimal = Field(
        None,
        alias="temperature",
        title="Type `Decimal`",
        description="Storage temperature",
    )
    temperature__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_temperature", title="Extension field for ``temperature``."
    )
