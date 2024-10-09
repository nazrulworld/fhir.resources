from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/TriggerDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import element, fhirtypes


class TriggerDefinition(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Defines an expected trigger for a module.
    A description of a triggering event. Triggering events can be named events,
    data events, or periodic, as determined by the type element.
    """

    __resource_type__ = "TriggerDefinition"

    condition: fhirtypes.ExpressionType | None = Field(  # type: ignore
        None,
        alias="condition",
        title="Whether the event triggers (boolean expression)",
        description=(
            "A boolean-valued expression that is evaluated in the context of the "
            "container of the trigger definition and returns whether or not the "
            "trigger fires."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    data: typing.List[fhirtypes.DataRequirementType] | None = Field(  # type: ignore
        None,
        alias="data",
        title="Triggering data of the event (multiple = 'and')",
        description=(
            "The triggering data of the event (if this is a data trigger). If more "
            "than one data is requirement is specified, then all the data "
            "requirements must be true."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name or URI that identifies the event",
        description=(
            "A formal name for the event. This may be an absolute URI that "
            "identifies the event formally (e.g. from a trigger registry), or a "
            "simple relative URI that identifies the event in a local context."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    timingDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="timingDate",
        title="Timing of the event",
        description="The timing of the event (if this is a periodic trigger).",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e timing[x]
            "one_of_many": "timing",
            "one_of_many_required": False,
        },
    )
    timingDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_timingDate", title="Extension field for ``timingDate``."
    )

    timingDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="timingDateTime",
        title="Timing of the event",
        description="The timing of the event (if this is a periodic trigger).",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e timing[x]
            "one_of_many": "timing",
            "one_of_many_required": False,
        },
    )
    timingDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_timingDateTime", title="Extension field for ``timingDateTime``."
    )

    timingReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="timingReference",
        title="Timing of the event",
        description="The timing of the event (if this is a periodic trigger).",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e timing[x]
            "one_of_many": "timing",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Schedule"],
        },
    )

    timingTiming: fhirtypes.TimingType | None = Field(  # type: ignore
        None,
        alias="timingTiming",
        title="Timing of the event",
        description="The timing of the event (if this is a periodic trigger).",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e timing[x]
            "one_of_many": "timing",
            "one_of_many_required": False,
        },
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title=(
            "named-event | periodic | data-changed | data-added | data-modified | "
            "data-removed | data-accessed | data-access-ended"
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
                "data-changed",
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
            "name",
            "timingTiming",
            "timingReference",
            "timingDate",
            "timingDateTime",
            "data",
            "condition",
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
            "timing": [
                "timingDate",
                "timingDateTime",
                "timingReference",
                "timingTiming",
            ]
        }
        return one_of_many_fields
