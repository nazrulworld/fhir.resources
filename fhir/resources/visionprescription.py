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
    """ Prescription for vision correction products for a patient.
    An authorization for the provision of glasses and/or contact lenses to a
    patient.
    """

    resource_type = Field("VisionPrescription", const=True)

    created: fhirtypes.DateTime = Field(
        ...,
        alias="created",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Response creation date",
    )

    dateWritten: fhirtypes.DateTime = Field(
        ...,
        alias="dateWritten",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When prescription was authorized",
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
        title="Type `Code` (represented as `dict` in JSON)",
        description="active | cancelled | draft | entered-in-error",
    )


class VisionPrescriptionLensSpecification(backboneelement.BackboneElement):
    """ Vision lens authorization.
    Contain the details of  the individual lens specifications and serves as
    the authorization for the fullfillment by certified professionals.
    """

    resource_type = Field("VisionPrescriptionLensSpecification", const=True)

    add: fhirtypes.Decimal = Field(
        None,
        alias="add",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Added power for multifocal levels",
    )

    axis: fhirtypes.Integer = Field(
        None,
        alias="axis",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Lens meridian which contain no power for astigmatism",
    )

    backCurve: fhirtypes.Decimal = Field(
        None,
        alias="backCurve",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Contact lens back curvature",
    )

    brand: fhirtypes.String = Field(
        None,
        alias="brand",
        title="Type `String` (represented as `dict` in JSON)",
        description="Brand required",
    )

    color: fhirtypes.String = Field(
        None,
        alias="color",
        title="Type `String` (represented as `dict` in JSON)",
        description="Color required",
    )

    cylinder: fhirtypes.Decimal = Field(
        None,
        alias="cylinder",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Lens power for astigmatism",
    )

    diameter: fhirtypes.Decimal = Field(
        None,
        alias="diameter",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Contact lens diameter",
    )

    duration: fhirtypes.QuantityType = Field(
        None,
        alias="duration",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Lens wear duration",
    )

    eye: fhirtypes.Code = Field(
        ...,
        alias="eye",
        title="Type `Code` (represented as `dict` in JSON)",
        description="right | left",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Notes for coatings",
    )

    power: fhirtypes.Decimal = Field(
        None,
        alias="power",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Contact lens power",
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
        None,
        alias="sphere",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Power of the lens",
    )


class VisionPrescriptionLensSpecificationPrism(backboneelement.BackboneElement):
    """ Eye alignment compensation.
    Allows for adjustment on two axis.
    """

    resource_type = Field("VisionPrescriptionLensSpecificationPrism", const=True)

    amount: fhirtypes.Decimal = Field(
        ...,
        alias="amount",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Amount of adjustment",
    )

    base: fhirtypes.Code = Field(
        ...,
        alias="base",
        title="Type `Code` (represented as `dict` in JSON)",
        description="up | down | in | out",
    )
