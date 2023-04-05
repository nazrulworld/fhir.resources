# -*- coding: utf-8 -*-
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

    resource_type = Field("SubstancePolymer", const=True)

    class_fhir: fhirtypes.CodeableConceptType = Field(
        None,
        alias="class",
        title="Overall type of the polymer",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    copolymerConnectivity: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="copolymerConnectivity",
        title="Descrtibes the copolymer sequence type (polymer connectivity)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    geometry: fhirtypes.CodeableConceptType = Field(
        None,
        alias="geometry",
        title=(
            "Polymer geometry, e.g. linear, branched, cross-linked, network or "
            "dendritic"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title=(
            "A business idenfier for this polymer, but typically this is handled by"
            " a SubstanceDefinition identifier"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    modification: fhirtypes.String = Field(
        None,
        alias="modification",
        title=(
            "Todo - this is intended to connect to a repeating full modification "
            "structure, also used by Protein and Nucleic Acid . String is just a "
            "placeholder"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    modification__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_modification", title="Extension field for ``modification``."
    )

    monomerSet: typing.List[fhirtypes.SubstancePolymerMonomerSetType] = Field(
        None,
        alias="monomerSet",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    repeat: typing.List[fhirtypes.SubstancePolymerRepeatType] = Field(
        None,
        alias="repeat",
        title="Specifies and quantifies the repeated units and their configuration",
        description=None,
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("SubstancePolymerMonomerSet", const=True)

    ratioType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="ratioType",
        title=(
            "Captures the type of ratio to the entire polymer, e.g. Monomer/Polymer"
            " ratio, SRU/Polymer Ratio"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    startingMaterial: typing.List[
        fhirtypes.SubstancePolymerMonomerSetStartingMaterialType
    ] = Field(
        None,
        alias="startingMaterial",
        title=(
            "The starting materials - monomer(s) used in the synthesis of the "
            "polymer"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("SubstancePolymerMonomerSetStartingMaterial", const=True)

    amount: fhirtypes.QuantityType = Field(
        None,
        alias="amount",
        title="A percentage",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Substance high level category, e.g. chemical substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="The type of substance for this starting material",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    isDefining: bool = Field(
        None,
        alias="isDefining",
        title=(
            "Used to specify whether the attribute described is a defining element "
            "for the unique identification of the polymer"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    isDefining__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    resource_type = Field("SubstancePolymerRepeat", const=True)

    averageMolecularFormula: fhirtypes.String = Field(
        None,
        alias="averageMolecularFormula",
        title="A representation of an (average) molecular formula from a polymer",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    averageMolecularFormula__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_averageMolecularFormula",
        title="Extension field for ``averageMolecularFormula``.",
    )

    repeatUnit: typing.List[fhirtypes.SubstancePolymerRepeatRepeatUnitType] = Field(
        None,
        alias="repeatUnit",
        title="An SRU - Structural Repeat Unit",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    repeatUnitAmountType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="repeatUnitAmountType",
        title=(
            "How the quantitative amount of Structural Repeat Units is captured "
            "(e.g. Exact, Numeric, Average)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("SubstancePolymerRepeatRepeatUnit", const=True)

    amount: fhirtypes.Integer = Field(
        None,
        alias="amount",
        title="Number of repeats of this unit",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    amount__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_amount", title="Extension field for ``amount``."
    )

    degreeOfPolymerisation: typing.List[
        fhirtypes.SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisationType
    ] = Field(
        None,
        alias="degreeOfPolymerisation",
        title=(
            "Applies to homopolymer and block co-polymers where the degree of "
            "polymerisation within a block can be described"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    orientation: fhirtypes.CodeableConceptType = Field(
        None,
        alias="orientation",
        title=(
            "The orientation of the polymerisation, e.g. head-tail, head-head, "
            "random"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    structuralRepresentation: typing.List[
        fhirtypes.SubstancePolymerRepeatRepeatUnitStructuralRepresentationType
    ] = Field(
        None,
        alias="structuralRepresentation",
        title="A graphical structure for this SRU",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    unit: fhirtypes.String = Field(
        None,
        alias="unit",
        title="Structural repeat units are essential elements for defining polymers",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    unit__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    resource_type = Field(
        "SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation", const=True
    )

    average: fhirtypes.Integer = Field(
        None,
        alias="average",
        title="An average amount of polymerisation",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    average__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_average", title="Extension field for ``average``."
    )

    high: fhirtypes.Integer = Field(
        None,
        alias="high",
        title="A high expected limit of the amount",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    high__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_high", title="Extension field for ``high``."
    )

    low: fhirtypes.Integer = Field(
        None,
        alias="low",
        title="A low expected limit of the amount",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    low__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_low", title="Extension field for ``low``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title=(
            "The type of the degree of polymerisation shall be described, e.g. "
            "SRU/Polymer Ratio"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field(
        "SubstancePolymerRepeatRepeatUnitStructuralRepresentation", const=True
    )

    attachment: fhirtypes.AttachmentType = Field(
        None,
        alias="attachment",
        title="An attached file with the structural representation",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    format: fhirtypes.CodeableConceptType = Field(
        None,
        alias="format",
        title=(
            "The format of the representation e.g. InChI, SMILES, MOLFILE, CDX, "
            "SDF, PDB, mmCIF"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    representation: fhirtypes.String = Field(
        None,
        alias="representation",
        title=(
            "The structural representation as text string in a standard format e.g."
            " InChI, SMILES, MOLFILE, CDX, SDF, PDB, mmCIF"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    representation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_representation", title="Extension field for ``representation``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="The type of structure (e.g. Full, Partial, Representative)",
        description=None,
        # if property is element of this resource.
        element_property=True,
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
