# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Timing
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import element, fhirtypes


class Timing(element.Element):
    """ A timing schedule that specifies an event that may occur multiple times.
    Specifies an event that may occur multiple times. Timing schedules are used
    to record when things are planned, expected or requested to occur. The most
    common usage is in dosage instructions for medications. They are also used
    when planning care of various kinds, and may be used for reporting the
    schedule to which past regular activities were carried out.
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


class TimingRepeat(element.Element):
    """ When the event is to occur.
    A set of rules that describe when the event is scheduled.
    """

    resource_type = Field("TimingRepeat", const=True)

    boundsDuration: fhirtypes.DurationType = Field(
        None,
        alias="boundsDuration",
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

    countMax: fhirtypes.Integer = Field(
        None,
        alias="countMax",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Maximum number of times to repeat",
    )

    dayOfWeek: ListType[fhirtypes.Code] = Field(
        None,
        alias="dayOfWeek",
        title="List of `Code` items (represented as `dict` in JSON)",
        description="mon | tue | wed | thu | fri | sat | sun",
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

    durationUnit: fhirtypes.Code = Field(
        None,
        alias="durationUnit",
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

    offset: fhirtypes.UnsignedInt = Field(
        None,
        alias="offset",
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="Minutes from event (before or after)",
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

    periodUnit: fhirtypes.Code = Field(
        None,
        alias="periodUnit",
        title="Type `Code` (represented as `dict` in JSON)",
        description="s | min | h | d | wk | mo | a - unit of time (UCUM)",
    )

    timeOfDay: ListType[fhirtypes.Time] = Field(
        None,
        alias="timeOfDay",
        title="List of `Time` items (represented as `dict` in JSON)",
        description="Time of day for action",
    )

    when: ListType[fhirtypes.Code] = Field(
        None,
        alias="when",
        title="List of `Code` items (represented as `dict` in JSON)",
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
            "bounds": ["boundsDuration", "boundsPeriod", "boundsRange",],
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
