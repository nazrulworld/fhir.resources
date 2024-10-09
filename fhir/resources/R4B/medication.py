from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Medication
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
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
    medication for the purposes of prescribing, dispensing, and administering a
    medication as well as for making statements about medication use.
    """

    __resource_type__ = "Medication"

    amount: fhirtypes.RatioType | None = Field(  # type: ignore
        None,
        alias="amount",
        title="Amount of drug in package",
        description=(
            "Specific amount of the drug in the packaged product.  For example, "
            "when specifying a product that has the same strength (For example, "
            "Insulin glargine 100 unit per mL solution for injection), this "
            "attribute provides additional clarification of the package amount (For"
            " example, 3 mL, 10mL, etc.)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    batch: fhirtypes.MedicationBatchType | None = Field(  # type: ignore
        None,
        alias="batch",
        title="Details about packaged medications",
        description="Information that only applies to packages (not products).",
        json_schema_extra={
            "element_property": True,
        },
    )

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

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business identifier for this medication",
        description=None,
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
            "identifier",
            "code",
            "status",
            "manufacturer",
            "form",
            "amount",
            "ingredient",
            "batch",
        ]


class MedicationBatch(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details about packaged medications.
    Information that only applies to packages (not products).
    """

    __resource_type__ = "MedicationBatch"

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
        ``MedicationBatch`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "lotNumber", "expirationDate"]


class MedicationIngredient(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Active or inactive ingredient.
    Identifies a particular constituent of interest in the product.
    """

    __resource_type__ = "MedicationIngredient"

    isActive: bool | None = Field(  # type: ignore
        None,
        alias="isActive",
        title="Active ingredient indicator",
        description=(
            "Indication of whether this ingredient affects the therapeutic action "
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
        title="The actual ingredient or content",
        description=(
            "The actual ingredient - either a substance (simple ingredient) or "
            "another medication of a medication."
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
        title="The actual ingredient or content",
        description=(
            "The actual ingredient - either a substance (simple ingredient) or "
            "another medication of a medication."
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

    strength: fhirtypes.RatioType | None = Field(  # type: ignore
        None,
        alias="strength",
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
            "isActive",
            "strength",
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
