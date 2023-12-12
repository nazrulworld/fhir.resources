# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ProcedureRequest
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic.v1 import Field, root_validator

from . import fhirtypes
from .domainresource import DomainResource


class ProcedureRequest(DomainResource):
    """A request for a procedure to be performed.

    A request for a procedure to be performed. May be a proposal or an order.
    """

    resource_type = Field("ProcedureRequest", const=True)

    asNeededBoolean: fhirtypes.Boolean = Field(
        None,
        alias="asNeededBoolean",
        title="Type `bool`.",
        description="Preconditions for procedure.",
        one_of_many="asNeeded",  # Choice of Data Types. i.e asNeeded[x]
        one_of_many_required=False,
    )
    asNeededCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="asNeededCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Preconditions for procedure.",
        one_of_many="asNeeded",  # Choice of Data Types. i.e asNeeded[x]
        one_of_many_required=False,
    )

    bodySite: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="bodySite",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="What part of body to perform on.",
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="What procedure to perform.",
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Type `Reference` referencing `Encounter` (represented as `dict` in JSON).",
        description="Encounter request created during.",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON).",
        description="Unique identifier for the request.",
    )

    notes: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="notes",
        title="List of `Annotation` items (represented as `dict` in JSON).",
        description="Additional information about desired procedure.",
    )

    orderedOn: fhirtypes.DateTime = Field(
        None,
        alias="orderedOn",
        title="Type `DateTime`.",
        description="When request was created.",
    )

    orderer: fhirtypes.ReferenceType = Field(
        None,
        alias="orderer",
        title=(
            "Type `Reference` referencing `Practitioner, Patient, "
            "RelatedPerson, Device` (represented as `dict` in JSON)."
        ),
        description="Who made request.",
    )
    performer: fhirtypes.ReferenceType = Field(
        None,
        alias="performer",
        title=(
            "Type `Reference` referencing `Practitioner, Organization,"
            " Patient, RelatedPerson` (represented as `dict` in JSON)."
        ),
        description="Who made request.",
    )

    reasonReference: fhirtypes.ReferenceType = Field(
        None,
        alias="reasonReference",
        title="Type `Reference` referencing `Condition` (represented as `dict` in JSON).",
        description="Why procedure should occur.",
        one_of_many="reason",  # Choice of Data Types. i.e reason[x]
        one_of_many_required=False,
    )
    reasonCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reasonCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Why procedure should occur.",
        one_of_many="reason",  # Choice of Data Types. i.e reason[x]
        one_of_many_required=False,
    )

    priority: fhirtypes.Code = Field(
        None,
        alias="priority",
        title="Type `Cide`.",
        description="routine | urgent | stat | asap.",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Cide`.",
        description=(
            "proposed | draft | requested | received | accepted | in-progress |"
            "completed | suspended | rejected | aborted."
        ),
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Type `Reference` referencing `Patient, Group` (represented as `dict` in JSON).",
        description="Who the procedure should be done to.",
    )

    scheduledDateTime: fhirtypes.DateTime = Field(
        None,
        alias="scheduledDateTime",
        title="Type `DateTime`.",
        description="When procedure should occur.",
        one_of_many="scheduled",  # Choice of Data Types. i.e scheduled[x]
        one_of_many_required=False,
    )
    scheduledPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="scheduledPeriod",
        title="Type `Period` (represented as `dict` in JSON).",
        description="When procedure should occur.",
        one_of_many="scheduled",  # Choice of Data Types. i.e scheduled[x]
        one_of_many_required=False,
    )

    scheduledTiming: fhirtypes.TimingType = Field(
        None,
        alias="scheduledTiming",
        title="Type `Timing` (represented as `dict` in JSON).",
        description="When procedure should occur.",
        one_of_many="scheduled",  # Choice of Data Types. i.e scheduled[x]
        one_of_many_required=False,
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
            "scheduled": ["scheduledDateTime", "scheduledPeriod", "scheduledTiming"],
            "reason": ["reasonCodeableConcept", "reasonReference"],
            "asNeeded": ["asNeededBoolean", "asNeededCodeableConcept"],
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
