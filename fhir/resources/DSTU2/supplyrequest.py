# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/DSTU2/supplyrequest.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic.v1 import Field, root_validator

from . import domainresource, fhirtypes
from .backboneelement import BackboneElement


class SupplyRequest(domainresource.DomainResource):
    """Request for a medication, substance or device.

    A record of a request for a medication, substance or device used in the healthcare setting.
    """

    resource_type = Field("SupplyRequest", const=True)

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="Type 'Reference' referencing 'Patient' (represented as 'dict' in JSON).",
        description="Patient for whom the item is supplied",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
        element_property=True,
    )

    source: fhirtypes.ReferenceType = Field(
        None,
        alias="source",
        title=(
            "Type `Reference` referencing "
            "`Practitioner, Organization, Patient` (represented as `dict` in JSON)."
        ),
        description="Who initiated this order",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Organization", "Patient"],
        element_property=True,
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="When the request was made",
        description="When the request was made",
        element_property=True,
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Unique identifier",
        description="Unique identifier for this supply request",
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="requested | completed | failed | cancelled",
        description="Status of the supply request",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["requested", "completed", "failed", "cancelled"],
        element_property=True,
    )

    kind: fhirtypes.CodeableConceptType = Field(
        None,
        alias="kind",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="The kind of supply (central, non-stock, etc.)",
        element_property=True,
    )

    orderedItem: fhirtypes.ReferenceType = Field(
        None,
        alias="orderedItem",
        title=(
            "Type `Reference` referencing "
            "`Medication, Substance, Device` (represented as `dict` in JSON)."
        ),
        description="Medication, Substance, or Device requested to be supplied",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Medication", "Substance", "Device"],
        element_property=True,
    )

    supplier: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="supplier",
        title=(
            "List of `Reference` items referencing `Organization` (represented as `dict` in"
            " JSON)"
        ),
        description="Who is intended to fulfill the request",
        enum_reference_types=["Organization"],
        element_property=True,
    )

    reasonCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reasonCodeableConcept",
        title="Why the supply item was requested",
        description="Why the supply item was requested.",
        # if property is element of this resource.
        element_property=True,
        one_of_many="reason",
        one_of_many_required=False,
    )

    reasonReference: fhirtypes.ReferenceType = Field(
        None,
        alias="reasonReference",
        title="Type 'Reference' referencing 'Any' (represented as 'dict' in JSON).",
        description="Why the supply item was requested.",
        # if property is element of this resource.
        element_property=True,
        one_of_many="reason",
        one_of_many_required=False,
        enum_reference_types=["Resource"],
    )

    when: fhirtypes.SupplyRequestWhenType = Field(
        None,
        alias="when",
        title="Type `SupplyRequestWhen` (represented as `dict` in JSON).",
        description="When the request should be fulfilled",
        element_property=True,
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


class SupplyRequestWhen(BackboneElement):
    """When the request should be fulfilled


    When the request should be fulfilled.
    """

    resource_type = Field("SupplyRequestWhen", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Fulfilment code",
        element_property=True,
    )

    schedule: fhirtypes.TimingType = Field(
        None,
        alias="schedule",
        title="Type `Timing` (represented as `dict` in JSON).",
        description="Formal fulfillment schedule",
        element_property=True,
    )
