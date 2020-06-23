# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubstancePolymer
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType
from typing import Union

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class SubstancePolymer(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Todo.
    """

    resource_type = Field("SubstancePolymer", const=True)

    class_fhir: fhirtypes.CodeableConceptType = Field(
        None,
        alias="class",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Todo",
    )

    copolymerConnectivity: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="copolymerConnectivity",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Todo",
    )

    geometry: fhirtypes.CodeableConceptType = Field(
        None,
        alias="geometry",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Todo",
    )

    modification: ListType[fhirtypes.String] = Field(
        None, alias="modification", title="List of `String` items", description="Todo"
    )
    modification__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_modification", title="Extension field for ``modification``."
    )

    monomerSet: ListType[fhirtypes.SubstancePolymerMonomerSetType] = Field(
        None,
        alias="monomerSet",
        title=(
            "List of `SubstancePolymerMonomerSet` items (represented as `dict` in "
            "JSON)"
        ),
        description="Todo",
    )

    repeat: ListType[fhirtypes.SubstancePolymerRepeatType] = Field(
        None,
        alias="repeat",
        title="List of `SubstancePolymerRepeat` items (represented as `dict` in JSON)",
        description="Todo",
    )


class SubstancePolymerMonomerSet(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Todo.
    """

    resource_type = Field("SubstancePolymerMonomerSet", const=True)

    ratioType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="ratioType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Todo",
    )

    startingMaterial: ListType[
        fhirtypes.SubstancePolymerMonomerSetStartingMaterialType
    ] = Field(
        None,
        alias="startingMaterial",
        title=(
            "List of `SubstancePolymerMonomerSetStartingMaterial` items "
            "(represented as `dict` in JSON)"
        ),
        description="Todo",
    )


class SubstancePolymerMonomerSetStartingMaterial(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Todo.
    """

    resource_type = Field("SubstancePolymerMonomerSetStartingMaterial", const=True)

    amount: fhirtypes.SubstanceAmountType = Field(
        None,
        alias="amount",
        title="Type `SubstanceAmount` (represented as `dict` in JSON)",
        description="Todo",
    )

    isDefining: bool = Field(
        None, alias="isDefining", title="Type `bool`", description="Todo"
    )
    isDefining__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_isDefining", title="Extension field for ``isDefining``."
    )

    material: fhirtypes.CodeableConceptType = Field(
        None,
        alias="material",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Todo",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Todo",
    )


class SubstancePolymerRepeat(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Todo.
    """

    resource_type = Field("SubstancePolymerRepeat", const=True)

    averageMolecularFormula: fhirtypes.String = Field(
        None, alias="averageMolecularFormula", title="Type `String`", description="Todo"
    )
    averageMolecularFormula__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_averageMolecularFormula",
        title="Extension field for ``averageMolecularFormula``.",
    )

    numberOfUnits: fhirtypes.Integer = Field(
        None, alias="numberOfUnits", title="Type `Integer`", description="Todo"
    )
    numberOfUnits__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_numberOfUnits", title="Extension field for ``numberOfUnits``."
    )

    repeatUnit: ListType[fhirtypes.SubstancePolymerRepeatRepeatUnitType] = Field(
        None,
        alias="repeatUnit",
        title=(
            "List of `SubstancePolymerRepeatRepeatUnit` items (represented as "
            "`dict` in JSON)"
        ),
        description="Todo",
    )

    repeatUnitAmountType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="repeatUnitAmountType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Todo",
    )


class SubstancePolymerRepeatRepeatUnit(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Todo.
    """

    resource_type = Field("SubstancePolymerRepeatRepeatUnit", const=True)

    amount: fhirtypes.SubstanceAmountType = Field(
        None,
        alias="amount",
        title="Type `SubstanceAmount` (represented as `dict` in JSON)",
        description="Todo",
    )

    degreeOfPolymerisation: ListType[
        fhirtypes.SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisationType
    ] = Field(
        None,
        alias="degreeOfPolymerisation",
        title=(
            "List of `SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation` items"
            " (represented as `dict` in JSON)"
        ),
        description="Todo",
    )

    orientationOfPolymerisation: fhirtypes.CodeableConceptType = Field(
        None,
        alias="orientationOfPolymerisation",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Todo",
    )

    repeatUnit: fhirtypes.String = Field(
        None, alias="repeatUnit", title="Type `String`", description="Todo"
    )
    repeatUnit__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_repeatUnit", title="Extension field for ``repeatUnit``."
    )

    structuralRepresentation: ListType[
        fhirtypes.SubstancePolymerRepeatRepeatUnitStructuralRepresentationType
    ] = Field(
        None,
        alias="structuralRepresentation",
        title=(
            "List of `SubstancePolymerRepeatRepeatUnitStructuralRepresentation` "
            "items (represented as `dict` in JSON)"
        ),
        description="Todo",
    )


class SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Todo.
    """

    resource_type = Field(
        "SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation", const=True
    )

    amount: fhirtypes.SubstanceAmountType = Field(
        None,
        alias="amount",
        title="Type `SubstanceAmount` (represented as `dict` in JSON)",
        description="Todo",
    )

    degree: fhirtypes.CodeableConceptType = Field(
        None,
        alias="degree",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Todo",
    )


class SubstancePolymerRepeatRepeatUnitStructuralRepresentation(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Todo.
    """

    resource_type = Field(
        "SubstancePolymerRepeatRepeatUnitStructuralRepresentation", const=True
    )

    attachment: fhirtypes.AttachmentType = Field(
        None,
        alias="attachment",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="Todo",
    )

    representation: fhirtypes.String = Field(
        None, alias="representation", title="Type `String`", description="Todo"
    )
    representation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_representation", title="Extension field for ``representation``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Todo",
    )
