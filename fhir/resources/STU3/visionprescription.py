# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/VisionPrescription
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class VisionPrescription(domainresource.DomainResource):
    """ Prescription for vision correction products for a patient.
    An authorization for the supply of glasses and/or contact lenses to a
    patient.
    """

    resource_type = Field("VisionPrescription", const=True)

    dateWritten: fhirtypes.DateTime = Field(
        None,
        alias="dateWritten",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When prescription was authorized",
    )

    dispense: ListType[fhirtypes.VisionPrescriptionDispenseType] = Field(
        None,
        alias="dispense",
        title=(
            "List of `VisionPrescriptionDispense` items (represented as `dict` in "
            "JSON)"
        ),
        description="Vision supply authorization",
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
        description="Business identifier",
    )

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="Who prescription is for",
    )

    prescriber: fhirtypes.ReferenceType = Field(
        None,
        alias="prescriber",
        title=(
            "Type `Reference` referencing `Practitioner` (represented as `dict` in "
            "JSON)"
        ),
        description="Who authorizes the vision product",
    )

    reasonCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reasonCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Reason or indication for writing the prescription",
        one_of_many="reason",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    reasonReference: fhirtypes.ReferenceType = Field(
        None,
        alias="reasonReference",
        title=(
            "Type `Reference` referencing `Condition` (represented as `dict` in "
            "JSON)"
        ),
        description="Reason or indication for writing the prescription",
        one_of_many="reason",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="active | cancelled | draft | entered-in-error",
    )

    @root_validator(pre=True)
    def validate_one_of_many(cls, values: Dict[str, Any]) -> Dict[str, Any]:
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
        one_of_many_fields = {"reason": ["reasonCodeableConcept", "reasonReference"]}
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


class VisionPrescriptionDispense(backboneelement.BackboneElement):
    """ Vision supply authorization.
    Deals with details of the dispense part of the supply specification.
    """

    resource_type = Field("VisionPrescriptionDispense", const=True)

    add: fhirtypes.Decimal = Field(
        None,
        alias="add",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Lens add",
    )

    axis: fhirtypes.Integer = Field(
        None,
        alias="axis",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Lens axis",
    )

    backCurve: fhirtypes.Decimal = Field(
        None,
        alias="backCurve",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Contact lens back curvature",
    )

    base: fhirtypes.Code = Field(
        None,
        alias="base",
        title="Type `Code` (represented as `dict` in JSON)",
        description="up | down | in | out",
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
        description="Lens cylinder",
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
        None,
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

    prism: fhirtypes.Decimal = Field(
        None,
        alias="prism",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Lens prism",
    )

    product: fhirtypes.CodeableConceptType = Field(
        None,
        alias="product",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Product to be supplied",
    )

    sphere: fhirtypes.Decimal = Field(
        None,
        alias="sphere",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Lens sphere",
    )
