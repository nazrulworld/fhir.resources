# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Timing
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import fhirtypes
from .element import Element


class Timing(Element):
    """A timing schedule that specifies an event that may occur multiple times.

    Specifies an event that may occur multiple times. Timing schedules are used
    to record when things are expected or requested to occur. The most common
    usage is in dosage instructions for medications. They are also used when
    planning care of various kinds.
    """

    resource_type = Field("Timing", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="BID | TID | QID | AM | PM | QD | QOD | Q4H | Q6H +",
    )

    event: ListType[fhirtypes.DateTime] = Field(
        None,
        alias="event",
        title="List of `DateTime` items (represented as `dict` in JSON)",
        description="When the event occurs",
    )

    repeat: fhirtypes.TimingRepeatType = Field(
        None,
        alias="repeat",
        title="Type `TimingRepeat` (represented as `dict` in JSON)",
        description="When the event is to occur",
    )


class TimingRepeat(Element):
    """When the event is to occur.

    A set of rules that describe when the event should occur.
    """

    resource_type = Field("TimingRepeat", const=True)

    boundsQuantity: fhirtypes.DurationType = Field(
        None,
        alias="boundsQuantity",
        title="Type `Duration` (represented as `dict` in JSON)",
        description="Length/Range of lengths, or (Start and/or end) limits",
        one_of_many="bounds",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    boundsPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="boundsPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Length/Range of lengths, or (Start and/or end) limits",
        one_of_many="bounds",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    boundsRange: fhirtypes.RangeType = Field(
        None,
        alias="boundsRange",
        title="Type `Range` (represented as `dict` in JSON)",
        description="Length/Range of lengths, or (Start and/or end) limits",
        one_of_many="bounds",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    count: fhirtypes.Integer = Field(
        None,
        alias="count",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Number of times to repeat",
    )

    duration: fhirtypes.Decimal = Field(
        None,
        alias="duration",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="How long when it happens",
    )

    durationMax: fhirtypes.Decimal = Field(
        None,
        alias="durationMax",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="How long when it happens (Max)",
    )

    durationUnits: fhirtypes.Code = Field(
        None,
        alias="durationUnits",
        title="Type `Code` (represented as `dict` in JSON)",
        description="s | min | h | d | wk | mo | a - unit of time (UCUM)",
    )

    frequency: fhirtypes.Integer = Field(
        None,
        alias="frequency",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Event occurs frequency times per period",
    )

    frequencyMax: fhirtypes.Integer = Field(
        None,
        alias="frequencyMax",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Event occurs up to frequencyMax times per period",
    )

    period: fhirtypes.Decimal = Field(
        None,
        alias="period",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Event occurs frequency times per period",
    )

    periodMax: fhirtypes.Decimal = Field(
        None,
        alias="periodMax",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Upper limit of period (3-4 hours)",
    )

    periodUnits: fhirtypes.Code = Field(
        None,
        alias="periodUnits",
        title="Type `Code` (represented as `dict` in JSON)",
        description="s | min | h | d | wk | mo | a - unit of time (UCUM)",
    )

    when: fhirtypes.Code = Field(
        None,
        alias="when",
        title="Code Type",
        description="Regular life events the event is tied to",
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
            "bounds": ["boundsQuantity", "boundsPeriod", "boundsRange"]
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
