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
        None, alias="class", title="Todo", description=None,
    )

    copolymerConnectivity: ListType[fhirtypes.CodeableConceptType] = Field(
        None, alias="copolymerConnectivity", title="Todo", description=None,
    )

    geometry: fhirtypes.CodeableConceptType = Field(
        None, alias="geometry", title="Todo", description=None,
    )

    modification: ListType[fhirtypes.String] = Field(
        None, alias="modification", title="Todo", description=None,
    )
    modification__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_modification", title="Extension field for ``modification``."
    )

    monomerSet: ListType[fhirtypes.SubstancePolymerMonomerSetType] = Field(
        None, alias="monomerSet", title="Todo", description=None,
    )

    repeat: ListType[fhirtypes.SubstancePolymerRepeatType] = Field(
        None, alias="repeat", title="Todo", description=None,
    )


class SubstancePolymerMonomerSet(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Todo.
    """

    resource_type = Field("SubstancePolymerMonomerSet", const=True)

    ratioType: fhirtypes.CodeableConceptType = Field(
        None, alias="ratioType", title="Todo", description=None,
    )

    startingMaterial: ListType[
        fhirtypes.SubstancePolymerMonomerSetStartingMaterialType
    ] = Field(
        None, alias="startingMaterial", title="Todo", description=None,
    )


class SubstancePolymerMonomerSetStartingMaterial(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Todo.
    """

    resource_type = Field("SubstancePolymerMonomerSetStartingMaterial", const=True)

    amount: fhirtypes.SubstanceAmountType = Field(
        None, alias="amount", title="Todo", description=None,
    )

    isDefining: bool = Field(
        None, alias="isDefining", title="Todo", description=None,
    )
    isDefining__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_isDefining", title="Extension field for ``isDefining``."
    )

    material: fhirtypes.CodeableConceptType = Field(
        None, alias="material", title="Todo", description=None,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None, alias="type", title="Todo", description=None,
    )


class SubstancePolymerRepeat(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Todo.
    """

    resource_type = Field("SubstancePolymerRepeat", const=True)

    averageMolecularFormula: fhirtypes.String = Field(
        None, alias="averageMolecularFormula", title="Todo", description=None,
    )
    averageMolecularFormula__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_averageMolecularFormula",
        title="Extension field for ``averageMolecularFormula``.",
    )

    numberOfUnits: fhirtypes.Integer = Field(
        None, alias="numberOfUnits", title="Todo", description=None,
    )
    numberOfUnits__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_numberOfUnits", title="Extension field for ``numberOfUnits``."
    )

    repeatUnit: ListType[fhirtypes.SubstancePolymerRepeatRepeatUnitType] = Field(
        None, alias="repeatUnit", title="Todo", description=None,
    )

    repeatUnitAmountType: fhirtypes.CodeableConceptType = Field(
        None, alias="repeatUnitAmountType", title="Todo", description=None,
    )


class SubstancePolymerRepeatRepeatUnit(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Todo.
    """

    resource_type = Field("SubstancePolymerRepeatRepeatUnit", const=True)

    amount: fhirtypes.SubstanceAmountType = Field(
        None, alias="amount", title="Todo", description=None,
    )

    degreeOfPolymerisation: ListType[
        fhirtypes.SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisationType
    ] = Field(
        None, alias="degreeOfPolymerisation", title="Todo", description=None,
    )

    orientationOfPolymerisation: fhirtypes.CodeableConceptType = Field(
        None, alias="orientationOfPolymerisation", title="Todo", description=None,
    )

    repeatUnit: fhirtypes.String = Field(
        None, alias="repeatUnit", title="Todo", description=None,
    )
    repeatUnit__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_repeatUnit", title="Extension field for ``repeatUnit``."
    )

    structuralRepresentation: ListType[
        fhirtypes.SubstancePolymerRepeatRepeatUnitStructuralRepresentationType
    ] = Field(
        None, alias="structuralRepresentation", title="Todo", description=None,
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
        None, alias="amount", title="Todo", description=None,
    )

    degree: fhirtypes.CodeableConceptType = Field(
        None, alias="degree", title="Todo", description=None,
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
        None, alias="attachment", title="Todo", description=None,
    )

    representation: fhirtypes.String = Field(
        None, alias="representation", title="Todo", description=None,
    )
    representation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_representation", title="Extension field for ``representation``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None, alias="type", title="Todo", description=None,
    )
