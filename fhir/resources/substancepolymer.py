# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubstancePolymer
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
import typing

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
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    copolymerConnectivity: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="copolymerConnectivity",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    geometry: fhirtypes.CodeableConceptType = Field(
        None,
        alias="geometry",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    modification: typing.List[fhirtypes.String] = Field(
        None,
        alias="modification",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    modification__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
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
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
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
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    startingMaterial: typing.List[
        fhirtypes.SubstancePolymerMonomerSetStartingMaterialType
    ] = Field(
        None,
        alias="startingMaterial",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
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
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    isDefining: bool = Field(
        None,
        alias="isDefining",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    isDefining__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_isDefining", title="Extension field for ``isDefining``."
    )

    material: fhirtypes.CodeableConceptType = Field(
        None,
        alias="material",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class SubstancePolymerRepeat(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Todo.
    """

    resource_type = Field("SubstancePolymerRepeat", const=True)

    averageMolecularFormula: fhirtypes.String = Field(
        None,
        alias="averageMolecularFormula",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    averageMolecularFormula__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_averageMolecularFormula",
        title="Extension field for ``averageMolecularFormula``.",
    )

    numberOfUnits: fhirtypes.Integer = Field(
        None,
        alias="numberOfUnits",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    numberOfUnits__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_numberOfUnits", title="Extension field for ``numberOfUnits``."
    )

    repeatUnit: typing.List[fhirtypes.SubstancePolymerRepeatRepeatUnitType] = Field(
        None,
        alias="repeatUnit",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    repeatUnitAmountType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="repeatUnitAmountType",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
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
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    degreeOfPolymerisation: typing.List[
        fhirtypes.SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisationType
    ] = Field(
        None,
        alias="degreeOfPolymerisation",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    orientationOfPolymerisation: fhirtypes.CodeableConceptType = Field(
        None,
        alias="orientationOfPolymerisation",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    repeatUnit: fhirtypes.String = Field(
        None,
        alias="repeatUnit",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    repeatUnit__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_repeatUnit", title="Extension field for ``repeatUnit``."
    )

    structuralRepresentation: typing.List[
        fhirtypes.SubstancePolymerRepeatRepeatUnitStructuralRepresentationType
    ] = Field(
        None,
        alias="structuralRepresentation",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
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
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    degree: fhirtypes.CodeableConceptType = Field(
        None,
        alias="degree",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
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
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    representation: fhirtypes.String = Field(
        None,
        alias="representation",
        title="Todo",
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
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
