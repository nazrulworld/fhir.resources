# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Timing
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType
from typing import Union

from pydantic import Field, root_validator

from . import backboneelement, element, fhirtypes


class Timing(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A timing schedule that specifies an event that may occur multiple times.
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
        description="BID | TID | QID | AM | PM | QD | QOD | +",
    )

    event: ListType[fhirtypes.DateTime] = Field(
        None,
        alias="event",
        title="List of `DateTime` items",
        description="When the event occurs",
    )
    event__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_event", title="Extension field for ``event``."
    )

    repeat: fhirtypes.TimingRepeatType = Field(
        None,
        alias="repeat",
        title="Type `TimingRepeat` (represented as `dict` in JSON)",
        description="When the event is to occur",
    )


class TimingRepeat(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    When the event is to occur.
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

    count: fhirtypes.PositiveInt = Field(
        None,
        alias="count",
        title="Type `PositiveInt`",
        description="Number of times to repeat",
    )
    count__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_count", title="Extension field for ``count``."
    )

    countMax: fhirtypes.PositiveInt = Field(
        None,
        alias="countMax",
        title="Type `PositiveInt`",
        description="Maximum number of times to repeat",
    )
    countMax__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_countMax", title="Extension field for ``countMax``."
    )

    dayOfWeek: ListType[fhirtypes.Code] = Field(
        None,
        alias="dayOfWeek",
        title="List of `Code` items",
        description="mon | tue | wed | thu | fri | sat | sun",
    )
    dayOfWeek__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_dayOfWeek", title="Extension field for ``dayOfWeek``."
    )

    duration: fhirtypes.Decimal = Field(
        None,
        alias="duration",
        title="Type `Decimal`",
        description="How long when it happens",
    )
    duration__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_duration", title="Extension field for ``duration``."
    )

    durationMax: fhirtypes.Decimal = Field(
        None,
        alias="durationMax",
        title="Type `Decimal`",
        description="How long when it happens (Max)",
    )
    durationMax__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_durationMax", title="Extension field for ``durationMax``."
    )

    durationUnit: fhirtypes.Code = Field(
        None,
        alias="durationUnit",
        title="Type `Code`",
        description="s | min | h | d | wk | mo | a - unit of time (UCUM)",
    )
    durationUnit__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_durationUnit", title="Extension field for ``durationUnit``."
    )

    frequency: fhirtypes.PositiveInt = Field(
        None,
        alias="frequency",
        title="Type `PositiveInt`",
        description="Event occurs frequency times per period",
    )
    frequency__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_frequency", title="Extension field for ``frequency``."
    )

    frequencyMax: fhirtypes.PositiveInt = Field(
        None,
        alias="frequencyMax",
        title="Type `PositiveInt`",
        description="Event occurs up to frequencyMax times per period",
    )
    frequencyMax__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_frequencyMax", title="Extension field for ``frequencyMax``."
    )

    offset: fhirtypes.UnsignedInt = Field(
        None,
        alias="offset",
        title="Type `UnsignedInt`",
        description="Minutes from event (before or after)",
    )
    offset__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_offset", title="Extension field for ``offset``."
    )

    period: fhirtypes.Decimal = Field(
        None,
        alias="period",
        title="Type `Decimal`",
        description="Event occurs frequency times per period",
    )
    period__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_period", title="Extension field for ``period``."
    )

    periodMax: fhirtypes.Decimal = Field(
        None,
        alias="periodMax",
        title="Type `Decimal`",
        description="Upper limit of period (3-4 hours)",
    )
    periodMax__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_periodMax", title="Extension field for ``periodMax``."
    )

    periodUnit: fhirtypes.Code = Field(
        None,
        alias="periodUnit",
        title="Type `Code`",
        description="s | min | h | d | wk | mo | a - unit of time (UCUM)",
    )
    periodUnit__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_periodUnit", title="Extension field for ``periodUnit``."
    )

    timeOfDay: ListType[fhirtypes.Time] = Field(
        None,
        alias="timeOfDay",
        title="List of `Time` items",
        description="Time of day for action",
    )
    timeOfDay__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_timeOfDay", title="Extension field for ``timeOfDay``."
    )

    when: ListType[fhirtypes.Code] = Field(
        None,
        alias="when",
        title="List of `Code` items",
        description="Code for time period of occurrence",
    )
    when__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_when", title="Extension field for ``when``."
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
            "bounds": ["boundsDuration", "boundsPeriod", "boundsRange"]
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
