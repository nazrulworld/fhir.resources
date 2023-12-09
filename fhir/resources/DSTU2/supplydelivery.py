# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/DSTU2/supplydelivery.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic.v1 import Field

from . import domainresource, fhirtypes


class SupplyDelivery(domainresource.DomainResource):
    """Delivery of Supply
    Record of delivery of what is supplied.
    """

    resource_type = Field("SupplyDelivery", const=True)

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="External identifier",
        description=(
            "Identifier assigned by the dispensing"
            " facility when the item(s) is dispensed."
        ),
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="in-progress | completed | abandoned",
        description="A code specifying the state of the dispense event",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["in-progress", "completed", "abandoned"],
        element_property=True,
    )

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="Type 'Reference' referencing 'Patient' (represented as 'dict' in JSON).",
        description="Patient for whom the item is supplied",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Category of dispense event",
        element_property=True,
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title=(
            "Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in "
            "JSON)."
        ),
        description="Amount dispensed",
        element_property=True,
    )

    suppliedItem: fhirtypes.ReferenceType = Field(
        None,
        alias="suppliedItem",
        title=(
            "Type `Reference` referencing "
            "`Medication, Substance, Device` (represented as `dict` in JSON)."
        ),
        description="Medication, Substance, or Device supplied",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Medication", "Substance", "Device"],
        element_property=True,
    )

    supplier: fhirtypes.ReferenceType = Field(
        None,
        alias="supplier",
        title=(
            "List of `Reference` items referencing `Practitioner` (represented as `dict` in"
            " JSON)"
        ),
        description="Dispenser",
        enum_reference_types=["Practitioner"],
        element_property=True,
    )

    whenPrepared: fhirtypes.PeriodType = Field(
        None,
        alias="whenPrepared",
        title="collectedPeriod",
        description="Dispensing time",
        element_property=True,
    )

    time: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Handover time",
        description="Handover time",
        element_property=True,
    )

    destination: fhirtypes.ReferenceType = Field(
        None,
        alias="destination",
        title="Type `Reference` referencing `Location` (represented as `dict` in JSON).",
        description="Where the Supply was sent",
        element_property=True,
    )

    receiver: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="receiver",
        title=(
            "List of `Reference` items referencing `Practitioner` (represented as `dict` in"
            " JSON)"
        ),
        description="Who collected the Supply",
        enum_reference_types=["Practitioner"],
        element_property=True,
    )
