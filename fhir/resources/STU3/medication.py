from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Medication
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Medication(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Definition of a Medication.
    This resource is primarily used for the identification and definition of a
    medication. It covers the ingredients and the packaging for a medication.
    """

    __resource_type__ = "Medication"

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Codes that identify this medication",
        description=(
            "A code (or set of codes) that specify this medication, or a textual "
            "description if no code is available. Usage note: This could be a "
            "standard medication code such as a code from RxNorm, SNOMED CT, IDMP "
            "etc. It could also be a national or local formulary code, optionally "
            "with translations to other code systems."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    form: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="form",
        title="powder | tablets | capsule +",
        description="Describes the form of the item.  Powder; tablets; capsule.",
        json_schema_extra={
            "element_property": True,
        },
    )

    image: typing.List[fhirtypes.AttachmentType] | None = Field(  # type: ignore
        None,
        alias="image",
        title="Picture of the medication",
        description="Photo(s) or graphic representation(s) of the medication.",
        json_schema_extra={
            "element_property": True,
        },
    )

    ingredient: typing.List[fhirtypes.MedicationIngredientType] | None = Field(  # type: ignore
        None,
        alias="ingredient",
        title="Active or inactive ingredient",
        description="Identifies a particular constituent of interest in the product.",
        json_schema_extra={
            "element_property": True,
        },
    )

    isBrand: bool | None = Field(  # type: ignore
        None,
        alias="isBrand",
        title="True if a brand",
        description="Set to true if the item is attributable to a specific manufacturer.",
        json_schema_extra={
            "element_property": True,
        },
    )
    isBrand__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_isBrand", title="Extension field for ``isBrand``."
    )

    isOverTheCounter: bool | None = Field(  # type: ignore
        None,
        alias="isOverTheCounter",
        title="True if medication does not require a prescription",
        description=(
            "Set to true if the medication can be obtained without an order from a "
            "prescriber."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    isOverTheCounter__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_isOverTheCounter",
        title="Extension field for ``isOverTheCounter``.",
    )

    manufacturer: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="manufacturer",
        title="Manufacturer of the item",
        description=(
            "Describes the details of the manufacturer of the medication product.  "
            "This is not intended to represent the distributor of a medication "
            "product."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    package: fhirtypes.MedicationPackageType | None = Field(  # type: ignore
        None,
        alias="package",
        title="Details about packaged medications",
        description="Information that only applies to packages (not products).",
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="active | inactive | entered-in-error",
        description="A code to indicate if the medication is in active use.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["active", "inactive", "entered-in-error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Medication`` according specification,
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
            "code",
            "status",
            "isBrand",
            "isOverTheCounter",
            "manufacturer",
            "form",
            "ingredient",
            "package",
            "image",
        ]


class MedicationIngredient(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Active or inactive ingredient.
    Identifies a particular constituent of interest in the product.
    """

    __resource_type__ = "MedicationIngredient"

    amount: fhirtypes.RatioType | None = Field(  # type: ignore
        None,
        alias="amount",
        title="Quantity of ingredient present",
        description=(
            "Specifies how many (or how much) of the items there are in this "
            "Medication.  For example, 250 mg per tablet.  This is expressed as a "
            "ratio where the numerator is 250mg and the denominator is 1 tablet."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    isActive: bool | None = Field(  # type: ignore
        None,
        alias="isActive",
        title="Active ingredient indicator",
        description=(
            "Indication of whether this\u00a0ingredient affects\u00a0the therapeutic action "
            "of the drug."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    isActive__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_isActive", title="Extension field for ``isActive``."
    )

    itemCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="itemCodeableConcept",
        title="The product contained",
        description=(
            "The actual ingredient - either a substance (simple ingredient) or "
            "another medication."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e item[x]
            "one_of_many": "item",
            "one_of_many_required": True,
        },
    )

    itemReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="itemReference",
        title="The product contained",
        description=(
            "The actual ingredient - either a substance (simple ingredient) or "
            "another medication."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e item[x]
            "one_of_many": "item",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Substance", "Medication"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationIngredient`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "itemCodeableConcept",
            "itemReference",
            "itemReference",
            "isActive",
            "amount",
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
        one_of_many_fields = {"item": ["itemCodeableConcept", "itemReference"]}
        return one_of_many_fields


class MedicationPackage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details about packaged medications.
    Information that only applies to packages (not products).
    """

    __resource_type__ = "MedicationPackage"

    batch: typing.List[fhirtypes.MedicationPackageBatchType] | None = Field(  # type: ignore
        None,
        alias="batch",
        title="Identifies a single production run",
        description=(
            "Information about a group of medication produced or packaged from one "
            "production run."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    container: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="container",
        title="E.g. box, vial, blister-pack",
        description="The kind of container that this package comes as.",
        json_schema_extra={
            "element_property": True,
        },
    )

    content: typing.List[fhirtypes.MedicationPackageContentType] | None = Field(  # type: ignore
        None,
        alias="content",
        title="What is  in the package",
        description="A set of components that go to make up the described item.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationPackage`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "container", "content", "batch"]


class MedicationPackageBatch(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Identifies a single production run.
    Information about a group of medication produced or packaged from one
    production run.
    """

    __resource_type__ = "MedicationPackageBatch"

    expirationDate: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="expirationDate",
        title="When batch will expire",
        description="When this specific batch of product will expire.",
        json_schema_extra={
            "element_property": True,
        },
    )
    expirationDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_expirationDate", title="Extension field for ``expirationDate``."
    )

    lotNumber: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="lotNumber",
        title="Identifier assigned to batch",
        description="The assigned lot number of a batch of the specified product.",
        json_schema_extra={
            "element_property": True,
        },
    )
    lotNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_lotNumber", title="Extension field for ``lotNumber``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationPackageBatch`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "lotNumber", "expirationDate"]


class MedicationPackageContent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What is  in the package.
    A set of components that go to make up the described item.
    """

    __resource_type__ = "MedicationPackageContent"

    amount: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="amount",
        title="Quantity present in the package",
        description="The amount of the product that is in the package.",
        json_schema_extra={
            "element_property": True,
        },
    )

    itemCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="itemCodeableConcept",
        title="The item in the package",
        description="Identifies one of the items in the package.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e item[x]
            "one_of_many": "item",
            "one_of_many_required": True,
        },
    )

    itemReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="itemReference",
        title="The item in the package",
        description="Identifies one of the items in the package.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e item[x]
            "one_of_many": "item",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Medication"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationPackageContent`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "itemCodeableConcept",
            "itemReference",
            "amount",
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
        one_of_many_fields = {"item": ["itemCodeableConcept", "itemReference"]}
        return one_of_many_fields
