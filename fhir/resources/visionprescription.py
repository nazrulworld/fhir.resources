# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/VisionPrescription
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class VisionPrescription(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Prescription for vision correction products for a patient.
    An authorization for the provision of glasses and/or contact lenses to a
    patient.
    """

    resource_type = Field("VisionPrescription", const=True)

    created: fhirtypes.DateTime = Field(
        ...,
        alias="created",
        title="Type `DateTime`",
        description="Response creation date",
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
    )

    dateWritten: fhirtypes.DateTime = Field(
        ...,
        alias="dateWritten",
        title="Type `DateTime`",
        description="When prescription was authorized",
    )
    dateWritten__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_dateWritten", title="Extension field for ``dateWritten``."
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title=(
            "Type `Reference` referencing `Encounter` (represented as `dict` in "
            "JSON)"
        ),
        description="Created during encounter / admission / stay",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business Identifier for vision prescription",
    )

    lensSpecification: ListType[
        fhirtypes.VisionPrescriptionLensSpecificationType
    ] = Field(
        ...,
        alias="lensSpecification",
        title=(
            "List of `VisionPrescriptionLensSpecification` items (represented as "
            "`dict` in JSON)"
        ),
        description="Vision lens authorization",
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="Who prescription is for",
    )

    prescriber: fhirtypes.ReferenceType = Field(
        ...,
        alias="prescriber",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole` "
            "(represented as `dict` in JSON)"
        ),
        description="Who authorized the vision prescription",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`",
        description="active | cancelled | draft | entered-in-error",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )


class VisionPrescriptionLensSpecification(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Vision lens authorization.
    Contain the details of  the individual lens specifications and serves as
    the authorization for the fullfillment by certified professionals.
    """

    resource_type = Field("VisionPrescriptionLensSpecification", const=True)

    add: fhirtypes.Decimal = Field(
        None,
        alias="add",
        title="Type `Decimal`",
        description="Added power for multifocal levels",
    )
    add__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_add", title="Extension field for ``add``."
    )

    axis: fhirtypes.Integer = Field(
        None,
        alias="axis",
        title="Type `Integer`",
        description="Lens meridian which contain no power for astigmatism",
    )
    axis__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_axis", title="Extension field for ``axis``."
    )

    backCurve: fhirtypes.Decimal = Field(
        None,
        alias="backCurve",
        title="Type `Decimal`",
        description="Contact lens back curvature",
    )
    backCurve__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_backCurve", title="Extension field for ``backCurve``."
    )

    brand: fhirtypes.String = Field(
        None, alias="brand", title="Type `String`", description="Brand required"
    )
    brand__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_brand", title="Extension field for ``brand``."
    )

    color: fhirtypes.String = Field(
        None, alias="color", title="Type `String`", description="Color required"
    )
    color__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_color", title="Extension field for ``color``."
    )

    cylinder: fhirtypes.Decimal = Field(
        None,
        alias="cylinder",
        title="Type `Decimal`",
        description="Lens power for astigmatism",
    )
    cylinder__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_cylinder", title="Extension field for ``cylinder``."
    )

    diameter: fhirtypes.Decimal = Field(
        None,
        alias="diameter",
        title="Type `Decimal`",
        description="Contact lens diameter",
    )
    diameter__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_diameter", title="Extension field for ``diameter``."
    )

    duration: fhirtypes.QuantityType = Field(
        None,
        alias="duration",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Lens wear duration",
    )

    eye: fhirtypes.Code = Field(
        ..., alias="eye", title="Type `Code`", description="right | left"
    )
    eye__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_eye", title="Extension field for ``eye``."
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Notes for coatings",
    )

    power: fhirtypes.Decimal = Field(
        None, alias="power", title="Type `Decimal`", description="Contact lens power"
    )
    power__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_power", title="Extension field for ``power``."
    )

    prism: ListType[fhirtypes.VisionPrescriptionLensSpecificationPrismType] = Field(
        None,
        alias="prism",
        title=(
            "List of `VisionPrescriptionLensSpecificationPrism` items (represented "
            "as `dict` in JSON)"
        ),
        description="Eye alignment compensation",
    )

    product: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="product",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Product to be supplied",
    )

    sphere: fhirtypes.Decimal = Field(
        None, alias="sphere", title="Type `Decimal`", description="Power of the lens"
    )
    sphere__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sphere", title="Extension field for ``sphere``."
    )


class VisionPrescriptionLensSpecificationPrism(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Eye alignment compensation.
    Allows for adjustment on two axis.
    """

    resource_type = Field("VisionPrescriptionLensSpecificationPrism", const=True)

    amount: fhirtypes.Decimal = Field(
        ..., alias="amount", title="Type `Decimal`", description="Amount of adjustment"
    )
    amount__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_amount", title="Extension field for ``amount``."
    )

    base: fhirtypes.Code = Field(
        ..., alias="base", title="Type `Code`", description="up | down | in | out"
    )
    base__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_base", title="Extension field for ``base``."
    )
