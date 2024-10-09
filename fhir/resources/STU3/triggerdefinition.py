from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/TriggerDefinition
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import element, fhirtypes


class TriggerDefinition(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Defines an expected trigger for a module.
    A description of a triggering event.
    """

    __resource_type__ = "TriggerDefinition"

    eventData: fhirtypes.DataRequirementType | None = Field(  # type: ignore
        None,
        alias="eventData",
        title="Triggering data of the event",
        description="The triggering data of the event (if this is a data trigger).",
        json_schema_extra={
            "element_property": True,
        },
    )

    eventName: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="eventName",
        title="Triggering event name",
        description="The name of the event (if this is a named-event trigger).",
        json_schema_extra={
            "element_property": True,
        },
    )
    eventName__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_eventName", title="Extension field for ``eventName``."
    )

    eventTimingDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="eventTimingDate",
        title="Timing of the event",
        description="The timing of the event (if this is a period trigger).",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e eventTiming[x]
            "one_of_many": "eventTiming",
            "one_of_many_required": False,
        },
    )
    eventTimingDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_eventTimingDate", title="Extension field for ``eventTimingDate``."
    )

    eventTimingDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="eventTimingDateTime",
        title="Timing of the event",
        description="The timing of the event (if this is a period trigger).",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e eventTiming[x]
            "one_of_many": "eventTiming",
            "one_of_many_required": False,
        },
    )
    eventTimingDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_eventTimingDateTime",
        title="Extension field for ``eventTimingDateTime``.",
    )

    eventTimingReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="eventTimingReference",
        title="Timing of the event",
        description="The timing of the event (if this is a period trigger).",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e eventTiming[x]
            "one_of_many": "eventTiming",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Schedule"],
        },
    )

    eventTimingTiming: fhirtypes.TimingType | None = Field(  # type: ignore
        None,
        alias="eventTimingTiming",
        title="Timing of the event",
        description="The timing of the event (if this is a period trigger).",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e eventTiming[x]
            "one_of_many": "eventTiming",
            "one_of_many_required": False,
        },
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title=(
            "named-event | periodic | data-added | data-modified | data-removed | "
            "data-accessed | data-access-ended"
        ),
        description="The type of triggering event.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "named-event",
                "periodic",
                "data-added",
                "data-modified",
                "data-removed",
                "data-accessed",
                "data-access-ended",
            ],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TriggerDefinition`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "type",
            "eventName",
            "eventTimingTiming",
            "eventTimingReference",
            "eventTimingDate",
            "eventTimingDateTime",
            "eventData",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("type", "type__ext")]
        return required_fields

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
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
            "eventTiming": [
                "eventTimingDate",
                "eventTimingDateTime",
                "eventTimingReference",
                "eventTimingTiming",
            ]
        }
        return one_of_many_fields
