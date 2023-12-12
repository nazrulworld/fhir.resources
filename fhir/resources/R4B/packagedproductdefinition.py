# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PackagedProductDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic.v1 import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class PackagedProductDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A medically related item or items, in a container or package.
    """

    resource_type = Field("PackagedProductDefinition", const=True)

    characteristic: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="characteristic",
        title=(
            'Allows the key features to be recorded, such as "hospital pack", '
            '"nurse prescribable"'
        ),
        description=(
            'Allows the key features to be recorded, such as "hospital pack", '
            '"nurse prescribable", "calendar pack".'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    containedItemQuantity: typing.List[fhirtypes.QuantityType] = Field(
        None,
        alias="containedItemQuantity",
        title=(
            "A total of the complete count of contained items of a particular "
            "type/form, independent of sub-packaging or organization. This can be "
            "considered as the pack size"
        ),
        description=(
            "A total of the complete count of contained items of a particular "
            "type/form, independent of sub-packaging or organization. This can be "
            "considered as the pack size. This attribute differs from "
            "containedItem.amount in that it can give a single aggregated count of "
            "all tablet types in a pack, even when these are different manufactured"
            " items. For example a pill pack of 21 tablets plus 7 sugar tablets, "
            "can be denoted here as '28 tablets'. This attribute is repeatable so "
            "that the different item types in one pack type can be counted (e.g. a "
            "count of vials and count of syringes). Each repeat must have different"
            " units, so that it is clear what the different sets of counted items "
            "are, and it is not intended to allow different counts of similar items"
            " (e.g. not '2 tubes and 3 tubes'). Repeats are not to be used to "
            "represent different pack sizes (e.g. 20 pack vs. 50 pack) - which "
            "would be different instances of this resource."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    copackagedIndicator: bool = Field(
        None,
        alias="copackagedIndicator",
        title=(
            "If the drug product is supplied with another item such as a diluent or"
            " adjuvant"
        ),
        description=(
            "States whether a drug product is supplied with another item such as a "
            "diluent or adjuvant."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    copackagedIndicator__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_copackagedIndicator",
        title="Extension field for ``copackagedIndicator``.",
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title=(
            "Textual description. Note that this is not the name of the package or "
            "product"
        ),
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
        title="A unique identifier for this package as whole",
        description=(
            "A unique identifier for this package as whole. Unique instance "
            "identifiers assigned to a package by manufacturers, regulators, drug "
            "catalogue custodians or other organizations."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    legalStatusOfSupply: typing.List[
        fhirtypes.PackagedProductDefinitionLegalStatusOfSupplyType
    ] = Field(
        None,
        alias="legalStatusOfSupply",
        title=(
            "The legal status of supply of the packaged item as classified by the "
            "regulator"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    manufacturer: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="manufacturer",
        title=(
            "Manufacturer of this package type (multiple means these are all "
            "possible manufacturers)"
        ),
        description=(
            "Manufacturer of this package type. When there are multiple it means "
            "these are all possible manufacturers."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    marketingStatus: typing.List[fhirtypes.MarketingStatusType] = Field(
        None,
        alias="marketingStatus",
        title=(
            "Allows specifying that an item is on the market for sale, or that it "
            "is not available, and the dates and locations associated"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title=(
            "A name for this package. Typically as listed in a drug formulary, "
            "catalogue, inventory etc"
        ),
        description=(
            "A name for this package. Typically what it would be listed as in a "
            "drug formulary or catalogue, inventory etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    package: fhirtypes.PackagedProductDefinitionPackageType = Field(
        None,
        alias="package",
        title=(
            "A packaging item, as a container for medically related items, possibly"
            " with other packaging items within, or a packaging component, such as "
            "bottle cap"
        ),
        description=(
            "A packaging item, as a container for medically related items, possibly"
            " with other packaging items within, or a packaging component, such as "
            "bottle cap (which is not a device or a medication manufactured item)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    packageFor: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="packageFor",
        title="The product that this is a pack for",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicinalProductDefinition"],
    )

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title=(
            "The status within the lifecycle of this item. High level - not "
            "intended to duplicate details elsewhere e.g. legal status, or "
            "authorization/marketing status"
        ),
        description=(
            "The status within the lifecycle of this item. A high level status, "
            "this is not intended to duplicate details carried elsewhere such as "
            "legal status, or authorization or marketing status."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    statusDate: fhirtypes.DateTime = Field(
        None,
        alias="statusDate",
        title="The date at which the given status became applicable",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    statusDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_statusDate", title="Extension field for ``statusDate``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title=(
            "A high level category e.g. medicinal product, raw material, shipping "
            "container etc"
        ),
        description=(
            "A high level category e.g. medicinal product, raw material, "
            "shipping/transport container, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PackagedProductDefinition`` according specification,
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
            "name",
            "type",
            "packageFor",
            "status",
            "statusDate",
            "containedItemQuantity",
            "description",
            "legalStatusOfSupply",
            "marketingStatus",
            "characteristic",
            "copackagedIndicator",
            "manufacturer",
            "package",
        ]


class PackagedProductDefinitionLegalStatusOfSupply(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The legal status of supply of the packaged item as classified by the
    regulator.
    """

    resource_type = Field("PackagedProductDefinitionLegalStatusOfSupply", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title=(
            "The actual status of supply. In what situation this package type may "
            "be supplied for use"
        ),
        description=(
            "The actual status of supply. Conveys in what situation this package "
            "type may be supplied for use."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    jurisdiction: fhirtypes.CodeableConceptType = Field(
        None,
        alias="jurisdiction",
        title="The place where the legal status of supply applies",
        description=(
            "The place where the legal status of supply applies. When not "
            "specified, this indicates it is unknown in this context."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PackagedProductDefinitionLegalStatusOfSupply`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "jurisdiction"]


class PackagedProductDefinitionPackage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A packaging item, as a container for medically related items, possibly with
    other packaging items within, or a packaging component, such as bottle cap.
    A packaging item, as a container for medically related items, possibly with
    other packaging items within, or a packaging component, such as bottle cap
    (which is not a device or a medication manufactured item).
    """

    resource_type = Field("PackagedProductDefinitionPackage", const=True)

    alternateMaterial: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="alternateMaterial",
        title=(
            "A possible alternate material for this part of the packaging, that is "
            "allowed to be used instead of the usual material"
        ),
        description=(
            "A possible alternate material for this part of the packaging, that is "
            "allowed to be used instead of the usual material (e.g. different types"
            " of plastic for a blister sleeve)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    containedItem: typing.List[
        fhirtypes.PackagedProductDefinitionPackageContainedItemType
    ] = Field(
        None,
        alias="containedItem",
        title="The item(s) within the packaging",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title=(
            "An identifier that is specific to this particular part of the "
            "packaging. Including possibly a Data Carrier Identifier"
        ),
        description=(
            "An identifier that is specific to this particular part of the "
            "packaging. Including possibly Data Carrier Identifier (a GS1 barcode)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    manufacturer: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="manufacturer",
        title=(
            "Manufacturer of this package Item (multiple means these are all "
            "possible manufacturers)"
        ),
        description=(
            "Manufacturer of this package Item. When there are multiple it means "
            "these are all possible manufacturers."
        ),
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

    package: typing.List[fhirtypes.PackagedProductDefinitionPackageType] = Field(
        None,
        alias="package",
        title=(
            "Allows containers (and parts of containers) within containers, still a"
            " single packaged product"
        ),
        description=(
            "Allows containers (and parts of containers) parwithin containers, "
            "still a single packaged product.  See also PackagedProductDefinition.p"
            "ackage.containedItem.item(PackagedProductDefinition)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    property: typing.List[
        fhirtypes.PackagedProductDefinitionPackagePropertyType
    ] = Field(
        None,
        alias="property",
        title="General characteristics of this item",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    quantity: fhirtypes.Integer = Field(
        None,
        alias="quantity",
        title=(
            "The quantity of this level of packaging in the package that contains "
            "it (with the outermost level being 1)"
        ),
        description=(
            "The quantity of this level of packaging in the package that contains "
            "it. If specified, the outermost level is always 1."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    quantity__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_quantity", title="Extension field for ``quantity``."
    )

    shelfLifeStorage: typing.List[
        fhirtypes.PackagedProductDefinitionPackageShelfLifeStorageType
    ] = Field(
        None,
        alias="shelfLifeStorage",
        title="Shelf Life and storage information",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="The physical type of the container of the items",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PackagedProductDefinitionPackage`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "identifier",
            "type",
            "quantity",
            "material",
            "alternateMaterial",
            "shelfLifeStorage",
            "manufacturer",
            "property",
            "containedItem",
            "package",
        ]


class PackagedProductDefinitionPackageContainedItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The item(s) within the packaging.
    """

    resource_type = Field("PackagedProductDefinitionPackageContainedItem", const=True)

    amount: fhirtypes.QuantityType = Field(
        None,
        alias="amount",
        title="The number of this type of item within this packaging",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    item: fhirtypes.CodeableReferenceType = Field(
        ...,
        alias="item",
        title=(
            "The actual item(s) of medication, as manufactured, or a device, or "
            "other medically related item (food, biologicals, raw materials, "
            "medical fluids, gases etc.), as contained in the package"
        ),
        description=(
            "The actual item(s) of medication, as manufactured, or a device "
            "(typically, but not necessarily, a co-packaged one), or other "
            "medically related item (such as food, biologicals, raw materials, "
            "medical fluids, gases etc.), as contained in the package. This also "
            "allows another whole packaged product to be included, which is solely "
            "for the case where a package of other entire packages is wanted - such"
            " as a wholesale or distribution pack (for layers within one package, "
            "use PackagedProductDefinition.package.package)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "ManufacturedItemDefinition",
            "DeviceDefinition",
            "PackagedProductDefinition",
            "BiologicallyDerivedProduct",
            "NutritionProduct",
        ],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PackagedProductDefinitionPackageContainedItem`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "item", "amount"]


class PackagedProductDefinitionPackageProperty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    General characteristics of this item.
    """

    resource_type = Field("PackagedProductDefinitionPackageProperty", const=True)

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="A code expressing the type of characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="A value for the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="A value for the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="valueCodeableConcept",
        title="A value for the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueDate: fhirtypes.Date = Field(
        None,
        alias="valueDate",
        title="A value for the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDate", title="Extension field for ``valueDate``."
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="A value for the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PackagedProductDefinitionPackageProperty`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "valueCodeableConcept",
            "valueQuantity",
            "valueDate",
            "valueBoolean",
            "valueAttachment",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_4308(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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
            "value": [
                "valueAttachment",
                "valueBoolean",
                "valueCodeableConcept",
                "valueDate",
                "valueQuantity",
            ]
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


class PackagedProductDefinitionPackageShelfLifeStorage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Shelf Life and storage information.
    """

    resource_type = Field(
        "PackagedProductDefinitionPackageShelfLifeStorage", const=True
    )

    periodDuration: fhirtypes.DurationType = Field(
        None,
        alias="periodDuration",
        title=(
            "The shelf life time period can be specified using a numerical value "
            "for the period of time and its unit of time measurement The unit of "
            "measurement shall be specified in accordance with ISO 11240 and the "
            "resulting terminology The symbol and the symbol identifier shall be "
            "used"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e period[x]
        one_of_many="period",
        one_of_many_required=False,
    )

    periodString: fhirtypes.String = Field(
        None,
        alias="periodString",
        title=(
            "The shelf life time period can be specified using a numerical value "
            "for the period of time and its unit of time measurement The unit of "
            "measurement shall be specified in accordance with ISO 11240 and the "
            "resulting terminology The symbol and the symbol identifier shall be "
            "used"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e period[x]
        one_of_many="period",
        one_of_many_required=False,
    )
    periodString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_periodString", title="Extension field for ``periodString``."
    )

    specialPrecautionsForStorage: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="specialPrecautionsForStorage",
        title=(
            "Special precautions for storage, if any, can be specified using an "
            "appropriate controlled vocabulary. The controlled term and the "
            "controlled term identifier shall be specified"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title=(
            "This describes the shelf life, taking into account various scenarios "
            "such as shelf life of the packaged Medicinal Product itself, shelf "
            "life after transformation where necessary and shelf life after the "
            "first opening of a bottle, etc. The shelf life type shall be specified"
            " using an appropriate controlled vocabulary The controlled term and "
            "the controlled term identifier shall be specified"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PackagedProductDefinitionPackageShelfLifeStorage`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "periodDuration",
            "periodString",
            "specialPrecautionsForStorage",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_5026(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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
        one_of_many_fields = {"period": ["periodDuration", "periodString"]}
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
