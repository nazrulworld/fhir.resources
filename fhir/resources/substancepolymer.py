from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/SubstancePolymer
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class SubstancePolymer(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Properties of a substance specific to it being a polymer.
    """

    __resource_type__ = "SubstancePolymer"

    class_fhir: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="class",
        title="Overall type of the polymer",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    copolymerConnectivity: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="copolymerConnectivity",
        title="Descrtibes the copolymer sequence type (polymer connectivity)",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    geometry: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="geometry",
        title=(
            "Polymer geometry, e.g. linear, branched, cross-linked, network or "
            "dendritic"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="identifier",
        title=(
            "A business idenfier for this polymer, but typically this is handled by"
            " a SubstanceDefinition identifier"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    modification: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="modification",
        title=(
            "Todo - this is intended to connect to a repeating full modification "
            "structure, also used by Protein and Nucleic Acid . String is just a "
            "placeholder"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    modification__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_modification", title="Extension field for ``modification``."
    )

    monomerSet: typing.List[fhirtypes.SubstancePolymerMonomerSetType] | None = Field(  # type: ignore
        None,
        alias="monomerSet",
        title="Todo",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    repeat: typing.List[fhirtypes.SubstancePolymerRepeatType] | None = Field(  # type: ignore
        None,
        alias="repeat",
        title="Specifies and quantifies the repeated units and their configuration",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstancePolymer`` according specification,
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
            "class",
            "geometry",
            "copolymerConnectivity",
            "modification",
            "monomerSet",
            "repeat",
        ]


class SubstancePolymerMonomerSet(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Todo.
    """

    __resource_type__ = "SubstancePolymerMonomerSet"

    ratioType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="ratioType",
        title=(
            "Captures the type of ratio to the entire polymer, e.g. Monomer/Polymer"
            " ratio, SRU/Polymer Ratio"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    startingMaterial: typing.List[fhirtypes.SubstancePolymerMonomerSetStartingMaterialType] | None = Field(  # type: ignore
        None,
        alias="startingMaterial",
        title=(
            "The starting materials - monomer(s) used in the synthesis of the "
            "polymer"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstancePolymerMonomerSet`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "ratioType", "startingMaterial"]


class SubstancePolymerMonomerSetStartingMaterial(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The starting materials - monomer(s) used in the synthesis of the polymer.
    """

    __resource_type__ = "SubstancePolymerMonomerSetStartingMaterial"

    amount: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="amount",
        title="A percentage",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    category: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="category",
        title="Substance high level category, e.g. chemical substance",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title="The type of substance for this starting material",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    isDefining: bool | None = Field(  # type: ignore
        None,
        alias="isDefining",
        title=(
            "Used to specify whether the attribute described is a defining element "
            "for the unique identification of the polymer"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    isDefining__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_isDefining", title="Extension field for ``isDefining``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstancePolymerMonomerSetStartingMaterial`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "category",
            "isDefining",
            "amount",
        ]


class SubstancePolymerRepeat(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Specifies and quantifies the repeated units and their configuration.
    """

    __resource_type__ = "SubstancePolymerRepeat"

    averageMolecularFormula: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="averageMolecularFormula",
        title="A representation of an (average) molecular formula from a polymer",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    averageMolecularFormula__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_averageMolecularFormula",
        title="Extension field for ``averageMolecularFormula``.",
    )

    repeatUnit: typing.List[fhirtypes.SubstancePolymerRepeatRepeatUnitType] | None = Field(  # type: ignore
        None,
        alias="repeatUnit",
        title="An SRU - Structural Repeat Unit",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    repeatUnitAmountType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="repeatUnitAmountType",
        title=(
            "How the quantitative amount of Structural Repeat Units is captured "
            "(e.g. Exact, Numeric, Average)"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstancePolymerRepeat`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "averageMolecularFormula",
            "repeatUnitAmountType",
            "repeatUnit",
        ]


class SubstancePolymerRepeatRepeatUnit(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An SRU - Structural Repeat Unit.
    """

    __resource_type__ = "SubstancePolymerRepeatRepeatUnit"

    amount: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="amount",
        title="Number of repeats of this unit",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    amount__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_amount", title="Extension field for ``amount``."
    )

    degreeOfPolymerisation: typing.List[fhirtypes.SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisationType] | None = Field(  # type: ignore
        None,
        alias="degreeOfPolymerisation",
        title=(
            "Applies to homopolymer and block co-polymers where the degree of "
            "polymerisation within a block can be described"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    orientation: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="orientation",
        title=(
            "The orientation of the polymerisation, e.g. head-tail, head-head, "
            "random"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    structuralRepresentation: typing.List[fhirtypes.SubstancePolymerRepeatRepeatUnitStructuralRepresentationType] | None = Field(  # type: ignore
        None,
        alias="structuralRepresentation",
        title="A graphical structure for this SRU",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    unit: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="unit",
        title="Structural repeat units are essential elements for defining polymers",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    unit__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_unit", title="Extension field for ``unit``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstancePolymerRepeatRepeatUnit`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "unit",
            "orientation",
            "amount",
            "degreeOfPolymerisation",
            "structuralRepresentation",
        ]


class SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Applies to homopolymer and block co-polymers where the degree of
    polymerisation within a block can be described.
    """

    __resource_type__ = "SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation"

    average: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="average",
        title="An average amount of polymerisation",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    average__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_average", title="Extension field for ``average``."
    )

    high: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="high",
        title="A high expected limit of the amount",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    high__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_high", title="Extension field for ``high``."
    )

    low: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="low",
        title="A low expected limit of the amount",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    low__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_low", title="Extension field for ``low``."
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title=(
            "The type of the degree of polymerisation shall be described, e.g. "
            "SRU/Polymer Ratio"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "average",
            "low",
            "high",
        ]


class SubstancePolymerRepeatRepeatUnitStructuralRepresentation(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A graphical structure for this SRU.
    """

    __resource_type__ = "SubstancePolymerRepeatRepeatUnitStructuralRepresentation"

    attachment: fhirtypes.AttachmentType | None = Field(  # type: ignore
        None,
        alias="attachment",
        title="An attached file with the structural representation",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    format: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="format",
        title=(
            "The format of the representation e.g. InChI, SMILES, MOLFILE, CDX, "
            "SDF, PDB, mmCIF"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    representation: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="representation",
        title=(
            "The structural representation as text string in a standard format e.g."
            " InChI, SMILES, MOLFILE, CDX, SDF, PDB, mmCIF"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    representation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_representation", title="Extension field for ``representation``."
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="The type of structure (e.g. Full, Partial, Representative)",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstancePolymerRepeatRepeatUnitStructuralRepresentation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "representation",
            "format",
            "attachment",
        ]
