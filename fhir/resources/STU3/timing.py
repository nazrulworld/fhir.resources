# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Timing
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field, root_validator

from . import element, fhirtypes


class Timing(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
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
        title="BID | TID | QID | AM | PM | QD | QOD | Q4H | Q6H +",
        description=(
            "A code for the timing schedule. Some codes such as BID are ubiquitous,"
            " but many institutions define their own additional codes. If a code is"
            " provided, the code is understood to be a complete statement of "
            "whatever is specified in the structured timing data, and either the "
            "code or the data may be used to interpret the Timing, with the "
            "exception that .repeat.bounds still applies over the code (and is not "
            "contained in the code)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    event: typing.List[fhirtypes.DateTime] = Field(
        None,
        alias="event",
        title="When the event occurs",
        description="Identifies specific times when the event occurs.",
        # if property is element of this resource.
        element_property=True,
    )
    event__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_event", title="Extension field for ``event``.")

    repeat: fhirtypes.TimingRepeatType = Field(
        None,
        alias="repeat",
        title="When the event is to occur",
        description="A set of rules that describe when the event is scheduled.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Timing`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "event", "repeat", "code"]


class TimingRepeat(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    When the event is to occur.
    A set of rules that describe when the event is scheduled.
    """

    resource_type = Field("TimingRepeat", const=True)

    boundsDuration: fhirtypes.DurationType = Field(
        None,
        alias="boundsDuration",
        title="Length/Range of lengths, or (Start and/or end) limits",
        description=(
            "Either a duration for the length of the timing schedule, a range of "
            "possible length, or outer bounds for start and/or end limits of the "
            "timing schedule."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e bounds[x]
        one_of_many="bounds",
        one_of_many_required=False,
    )

    boundsPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="boundsPeriod",
        title="Length/Range of lengths, or (Start and/or end) limits",
        description=(
            "Either a duration for the length of the timing schedule, a range of "
            "possible length, or outer bounds for start and/or end limits of the "
            "timing schedule."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e bounds[x]
        one_of_many="bounds",
        one_of_many_required=False,
    )

    boundsRange: fhirtypes.RangeType = Field(
        None,
        alias="boundsRange",
        title="Length/Range of lengths, or (Start and/or end) limits",
        description=(
            "Either a duration for the length of the timing schedule, a range of "
            "possible length, or outer bounds for start and/or end limits of the "
            "timing schedule."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e bounds[x]
        one_of_many="bounds",
        one_of_many_required=False,
    )

    count: fhirtypes.Integer = Field(
        None,
        alias="count",
        title="Number of times to repeat",
        description="A total count of the desired number of repetitions.",
        # if property is element of this resource.
        element_property=True,
    )
    count__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_count", title="Extension field for ``count``."
    )

    countMax: fhirtypes.Integer = Field(
        None,
        alias="countMax",
        title="Maximum number of times to repeat",
        description=(
            "A maximum value for the count of the desired repetitions (e.g. do "
            "something 6-8 times)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    countMax__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_countMax", title="Extension field for ``countMax``."
    )

    dayOfWeek: typing.List[fhirtypes.Code] = Field(
        None,
        alias="dayOfWeek",
        title="mon | tue | wed | thu | fri | sat | sun",
        description=(
            "If one or more days of week is provided, then the action happens only "
            "on the specified day(s)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["mon", "tue", "wed", "thu", "fri", "sat", "sun"],
    )
    dayOfWeek__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_dayOfWeek", title="Extension field for ``dayOfWeek``.")

    duration: fhirtypes.Decimal = Field(
        None,
        alias="duration",
        title="How long when it happens",
        description="How long this thing happens for when it happens.",
        # if property is element of this resource.
        element_property=True,
    )
    duration__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_duration", title="Extension field for ``duration``."
    )

    durationMax: fhirtypes.Decimal = Field(
        None,
        alias="durationMax",
        title="How long when it happens (Max)",
        description="The upper limit of how long this thing happens for when it happens.",
        # if property is element of this resource.
        element_property=True,
    )
    durationMax__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_durationMax", title="Extension field for ``durationMax``."
    )

    durationUnit: fhirtypes.Code = Field(
        None,
        alias="durationUnit",
        title="s | min | h | d | wk | mo | a - unit of time (UCUM)",
        description="The units of time for the duration, in UCUM units.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["s", "min", "h", "d", "wk", "mo", "a"],
    )
    durationUnit__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_durationUnit", title="Extension field for ``durationUnit``."
    )

    frequency: fhirtypes.Integer = Field(
        None,
        alias="frequency",
        title="Event occurs frequency times per period",
        description=(
            "The number of times to repeat the action within the specified period /"
            " period range (i.e. both period and periodMax provided)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    frequency__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_frequency", title="Extension field for ``frequency``."
    )

    frequencyMax: fhirtypes.Integer = Field(
        None,
        alias="frequencyMax",
        title="Event occurs up to frequencyMax times per period",
        description=(
            "If present, indicates that the frequency is a range - so to repeat "
            "between [frequency] and [frequencyMax] times within the period or "
            "period range."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    frequencyMax__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_frequencyMax", title="Extension field for ``frequencyMax``."
    )

    offset: fhirtypes.UnsignedInt = Field(
        None,
        alias="offset",
        title="Minutes from event (before or after)",
        description=(
            "The number of minutes from the event. If the event code does not "
            "indicate whether the minutes is before or after the event, then the "
            "offset is assumed to be after the event."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    offset__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_offset", title="Extension field for ``offset``."
    )

    period: fhirtypes.Decimal = Field(
        None,
        alias="period",
        title="Event occurs frequency times per period",
        description=(
            "Indicates the duration of time over which repetitions are to occur; "
            'e.g. to express "3 times per day", 3 would be the frequency and "1 '
            'day" would be the period.'
        ),
        # if property is element of this resource.
        element_property=True,
    )
    period__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_period", title="Extension field for ``period``."
    )

    periodMax: fhirtypes.Decimal = Field(
        None,
        alias="periodMax",
        title="Upper limit of period (3-4 hours)",
        description=(
            "If present, indicates that the period is a range from [period] to "
            '[periodMax], allowing expressing concepts such as "do this once every '
            "3-5 days."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    periodMax__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_periodMax", title="Extension field for ``periodMax``."
    )

    periodUnit: fhirtypes.Code = Field(
        None,
        alias="periodUnit",
        title="s | min | h | d | wk | mo | a - unit of time (UCUM)",
        description="The units of time for the period in UCUM units.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["s", "min", "h", "d", "wk", "mo", "a"],
    )
    periodUnit__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_periodUnit", title="Extension field for ``periodUnit``."
    )

    timeOfDay: typing.List[fhirtypes.Time] = Field(
        None,
        alias="timeOfDay",
        title="Time of day for action",
        description="Specified time of day for action to take place.",
        # if property is element of this resource.
        element_property=True,
    )
    timeOfDay__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_timeOfDay", title="Extension field for ``timeOfDay``.")

    when: typing.List[fhirtypes.Code] = Field(
        None,
        alias="when",
        title="Regular life events the event is tied to",
        description="Real world events that the occurrence of the event should be tied to.",
        # if property is element of this resource.
        element_property=True,
    )
    when__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_when", title="Extension field for ``when``.")

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TimingRepeat`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "boundsDuration",
            "boundsRange",
            "boundsPeriod",
            "count",
            "countMax",
            "duration",
            "durationMax",
            "durationUnit",
            "frequency",
            "frequencyMax",
            "period",
            "periodMax",
            "periodUnit",
            "dayOfWeek",
            "timeOfDay",
            "when",
            "offset",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1425(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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
