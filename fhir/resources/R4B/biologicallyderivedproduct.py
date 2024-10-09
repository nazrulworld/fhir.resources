from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/BiologicallyDerivedProduct
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class BiologicallyDerivedProduct(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A material substance originating from a biological entity.
    A material substance originating from a biological entity intended to be
    transplanted or infused
    into another (possibly the same) biological entity.
    """

    __resource_type__ = "BiologicallyDerivedProduct"

    collection: fhirtypes.BiologicallyDerivedProductCollectionType | None = Field(  # type: ignore
        None,
        alias="collection",
        title="How this product was collected",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="External ids for this item",
        description=(
            "This records identifiers associated with this biologically derived "
            "product instance that are defined by business processes and/or used to"
            " refer to it when a direct URL reference to the resource itself is not"
            " appropriate (e.g. in CDA documents, or in written / printed "
            "documentation)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    manipulation: fhirtypes.BiologicallyDerivedProductManipulationType | None = Field(  # type: ignore
        None,
        alias="manipulation",
        title="Any manipulation of product post-collection",
        description=(
            "Any manipulation of product post-collection that is intended to alter "
            "the product.  For example a buffy-coat enrichment or CD8 reduction of "
            "Peripheral Blood Stem Cells to make it more suitable for infusion."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    parent: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="parent",
        title="BiologicallyDerivedProduct parent",
        description="Parent product (if any).",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["BiologicallyDerivedProduct"],
        },
    )

    processing: typing.List[fhirtypes.BiologicallyDerivedProductProcessingType] | None = Field(  # type: ignore
        None,
        alias="processing",
        title="Any processing of the product during collection",
        description=(
            "Any processing of the product during collection that does not change "
            "the fundamental nature of the product. For example adding anti-"
            "coagulants during the collection of Peripheral Blood Stem Cells."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    productCategory: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="productCategory",
        title="organ | tissue | fluid | cells | biologicalAgent",
        description="Broad category of this product.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["organ", "tissue", "fluid", "cells", "biologicalAgent"],
        },
    )
    productCategory__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_productCategory", title="Extension field for ``productCategory``."
    )

    productCode: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="productCode",
        title="What this biologically derived product is",
        description=(
            "A code that identifies the kind of this biologically derived product "
            "(SNOMED Ctcode)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    quantity: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="The amount of this biologically derived product",
        description="Number of discrete units within this product.",
        json_schema_extra={
            "element_property": True,
        },
    )
    quantity__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_quantity", title="Extension field for ``quantity``."
    )

    request: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="request",
        title="Procedure request",
        description="Procedure request to obtain this biologically derived product.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ServiceRequest"],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="available | unavailable",
        description="Whether the product is currently available.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["available", "unavailable"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    storage: typing.List[fhirtypes.BiologicallyDerivedProductStorageType] | None = Field(  # type: ignore
        None,
        alias="storage",
        title="Product storage",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BiologicallyDerivedProduct`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "identifier",
            "productCategory",
            "productCode",
            "status",
            "request",
            "quantity",
            "parent",
            "collection",
            "processing",
            "manipulation",
            "storage",
        ]


class BiologicallyDerivedProductCollection(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    How this product was collected.
    """

    __resource_type__ = "BiologicallyDerivedProductCollection"

    collectedDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="collectedDateTime",
        title="Time of product collection",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e collected[x]
            "one_of_many": "collected",
            "one_of_many_required": False,
        },
    )
    collectedDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_collectedDateTime",
        title="Extension field for ``collectedDateTime``.",
    )

    collectedPeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="collectedPeriod",
        title="Time of product collection",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e collected[x]
            "one_of_many": "collected",
            "one_of_many_required": False,
        },
    )

    collector: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="collector",
        title="Individual performing collection",
        description="Healthcare professional who is performing the collection.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner", "PractitionerRole"],
        },
    )

    source: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="source",
        title="Who is product from",
        description=(
            "The patient or entity, such as a hospital or vendor in the case of a "
            "processed/manipulated/manufactured product, providing the product."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "Organization"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BiologicallyDerivedProductCollection`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "collector",
            "source",
            "collectedDateTime",
            "collectedPeriod",
        ]

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
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
        return one_of_many_fields


class BiologicallyDerivedProductManipulation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Any manipulation of product post-collection.
    Any manipulation of product post-collection that is intended to alter the
    product.  For example a buffy-coat enrichment or CD8 reduction of
    Peripheral Blood Stem Cells to make it more suitable for infusion.
    """

    __resource_type__ = "BiologicallyDerivedProductManipulation"

    description: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Description of manipulation",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    timeDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="timeDateTime",
        title="Time of manipulation",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e time[x]
            "one_of_many": "time",
            "one_of_many_required": False,
        },
    )
    timeDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_timeDateTime", title="Extension field for ``timeDateTime``."
    )

    timePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="timePeriod",
        title="Time of manipulation",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e time[x]
            "one_of_many": "time",
            "one_of_many_required": False,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BiologicallyDerivedProductManipulation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "description",
            "timeDateTime",
            "timePeriod",
        ]

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
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
        return one_of_many_fields


class BiologicallyDerivedProductProcessing(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Any processing of the product during collection.
    Any processing of the product during collection that does not change the
    fundamental nature of the product. For example adding anti-coagulants
    during the collection of Peripheral Blood Stem Cells.
    """

    __resource_type__ = "BiologicallyDerivedProductProcessing"

    additive: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="additive",
        title="Substance added during processing",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Substance"],
        },
    )

    description: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Description of of processing",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    procedure: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="procedure",
        title="Procesing code",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    timeDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="timeDateTime",
        title="Time of processing",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e time[x]
            "one_of_many": "time",
            "one_of_many_required": False,
        },
    )
    timeDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_timeDateTime", title="Extension field for ``timeDateTime``."
    )

    timePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="timePeriod",
        title="Time of processing",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e time[x]
            "one_of_many": "time",
            "one_of_many_required": False,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BiologicallyDerivedProductProcessing`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "description",
            "procedure",
            "additive",
            "timeDateTime",
            "timePeriod",
        ]

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
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
        return one_of_many_fields


class BiologicallyDerivedProductStorage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Product storage.
    """

    __resource_type__ = "BiologicallyDerivedProductStorage"

    description: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Description of storage",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    duration: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="duration",
        title="Storage timeperiod",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    scale: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="scale",
        title="farenheit | celsius | kelvin",
        description="Temperature scale used.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["farenheit", "celsius", "kelvin"],
        },
    )
    scale__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_scale", title="Extension field for ``scale``."
    )

    temperature: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="temperature",
        title="Storage temperature",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    temperature__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_temperature", title="Extension field for ``temperature``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BiologicallyDerivedProductStorage`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "description",
            "temperature",
            "scale",
            "duration",
        ]
