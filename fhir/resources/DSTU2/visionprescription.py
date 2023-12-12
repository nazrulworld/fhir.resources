# -*- coding: utf-8 -*-
"""
Profile: https://www.hl7.org/fhir/DSTU2/visionprescription.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic.v1 import Field, root_validator

from . import domainresource, fhirtypes
from .backboneelement import BackboneElement


class VisionPrescription(domainresource.DomainResource):
    """Prescription for vision correction products for a patient.

    An authorization for the supply of glasses and/or contact lenses to a patient.
    """

    resource_type = Field("VisionPrescription", const=True)

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier for the resource",
        description="A unique identifier assigned to this explanation of benefit.",
        element_property=True,
    )

    dateWritten: fhirtypes.DateTime = Field(
        None,
        alias="dateWritten",
        title="When prescription was authorized",
        description="The date (and perhaps time) when the prescription was written",
        element_property=True,
    )

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="Type 'Reference' referencing 'Patient' (represented as 'dict' in JSON).",
        description="Who prescription is for",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
        element_property=True,
    )

    prescriber: fhirtypes.ReferenceType = Field(
        None,
        alias="prescriber",
        title="Type 'Reference' referencing 'Practitioner' (represented as 'dict' in JSON).",
        description="Who authorizes the vision product",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
        element_property=True,
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Type 'Reference' referencing 'Encounter' (represented as 'dict' in JSON).",
        description="Created during encounter / admission / stay",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
        element_property=True,
    )

    reasonCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reasonCodeableConcept",
        title="Reason or indication for writing the prescription",
        description="Can be the reason or the indication for writing the prescription.",
        # if property is element of this resource.
        element_property=True,
        # 9/24 edit per @nazrulworld comment regarding reason[x]
        one_of_many="reason",
        one_of_many_required=False,
    )

    reasonReference: fhirtypes.ReferenceType = Field(
        None,
        alias="reasonReference",
        title="Type 'Reference' referencing 'Condition' (represented as 'dict' in JSON).",
        description="Can be the reason or the indication for writing the prescription.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Condition"],
        # 9/24 edit per @nazrulworld comment regarding reason[x]
        one_of_many="reason",
        one_of_many_required=False,
    )

    # 9/24 edit per @nazrulworld comment regarding `dispense` field is missing
    dispense: ListType[fhirtypes.VisionPrescriptionDispenseType] = Field(
        None,
        alias="dispense",
        title="List of `VisionPrescription` items(represented as `dict` in JSON)",
        description="Vision supply authorization",
        element_property=True,
    )

    # 9/24 adding special validator per @nazrulworld comment
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
        one_of_many_fields = {
            "reason": ["reasonCodeableConcept", "reasonReference"],
        }
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


class VisionPrescriptionDispense(BackboneElement):
    """
    Deals with details of the dispense part of the supply specification.
    """

    resource_type = Field("VisionPrescriptionDispense", const=True)

    product: fhirtypes.CodingType = Field(
        ...,
        alias="product",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Product to be supplied",
        element_property=True,
    )

    eye: fhirtypes.Code = Field(
        None,
        alias="eye",
        title="right | left",
        description="The eye for which the lens applies.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["right", "left"],
        element_property=True,
    )

    sphere: fhirtypes.Decimal = Field(
        None,
        alias="sphere",
        title="Lens sphere",
        description="Lens power measured in diopters (0.25 units)",
        # if property is element of this resource.
        element_property=True,
    )

    cylinder: fhirtypes.Decimal = Field(
        None,
        alias="cylinder",
        title="Lens cylinder",
        description="Power adjustment for astigmatism measured in diopters (0.25 units)",
        # if property is element of this resource.
        element_property=True,
    )

    axis: fhirtypes.Integer = Field(
        None,
        alias="axis",
        title="Lens axis",
        description="Adjustment for astigmatism measured in integer degrees",
        # if property is element of this resource.
        element_property=True,
    )

    prism: fhirtypes.Decimal = Field(
        None,
        alias="prism",
        title="Lens prism",
        description="Amount of prism to compensate for eye alignment in fractional units",
        # if property is element of this resource.
        element_property=True,
    )

    base: fhirtypes.Code = Field(
        None,
        alias="base",
        title="up | down | in | out",
        description="The relative base, or reference lens edge, for the prism",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["up", "down", "in", "out"],
        element_property=True,
    )

    add: fhirtypes.Decimal = Field(
        None,
        alias="add",
        title="Lens add",
        description="Power adjustment for multifocal lenses measured in diopters (0.25 units)",
        # if property is element of this resource.
        element_property=True,
    )

    power: fhirtypes.Decimal = Field(
        None,
        alias="power",
        title="Contact lens power",
        description="Contact lens power measured in diopters (0.25 units)",
        # if property is element of this resource.
        element_property=True,
    )

    backCurve: fhirtypes.Decimal = Field(
        None,
        alias="backCurve",
        title="Contact lens back curvature",
        description="Back curvature measured in millimeters",
        # if property is element of this resource.
        element_property=True,
    )

    diameter: fhirtypes.Decimal = Field(
        None,
        alias="diameter",
        title="Contact lens diameter",
        description="Contact lens diameter measured in millimeters",
        # if property is element of this resource.
        element_property=True,
    )

    duration: fhirtypes.QuantityType = Field(
        None,
        alias="duration",
        title="Lens wear duration",
        description="The recommended maximum wear period for the lens",
        element_property=True,
    )

    color: fhirtypes.String = Field(
        None,
        alias="color",
        title="Lens add",
        description="Special color or pattern",
    )

    brand: fhirtypes.String = Field(
        None,
        alias="brand",
        title="Lens add",
        description="Brand recommendations or restrictions",
        element_property=True,
    )

    notes: fhirtypes.String = Field(
        None,
        alias="notes",
        title="Notes for coatings",
        description="Notes for special requirements such as coatings and lens materials",
        element_property=True,
    )
