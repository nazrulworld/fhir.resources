# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/TriggerDefinition
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict

from pydantic import Field, root_validator

from . import element, fhirtypes


class TriggerDefinition(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Defines an expected trigger for a module.
    A description of a triggering event.
    """

    resource_type = Field("TriggerDefinition", const=True)

    eventData: fhirtypes.DataRequirementType = Field(
        None,
        alias="eventData",
        title="Type `DataRequirement` (represented as `dict` in JSON)",
        description="Triggering data of the event",
    )

    eventName: fhirtypes.String = Field(
        None,
        alias="eventName",
        title="Type `String`",
        description="Triggering event name",
    )
    eventName__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_eventName", title="Extension field for ``eventName``."
    )

    eventTimingDate: fhirtypes.Date = Field(
        None,
        alias="eventTimingDate",
        title="Type `Date`",
        description="Timing of the event",
        one_of_many="eventTiming",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    eventTimingDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_eventTimingDate", title="Extension field for ``eventTimingDate``."
    )

    eventTimingDateTime: fhirtypes.DateTime = Field(
        None,
        alias="eventTimingDateTime",
        title="Type `DateTime`",
        description="Timing of the event",
        one_of_many="eventTiming",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    eventTimingDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_eventTimingDateTime",
        title="Extension field for ``eventTimingDateTime``.",
    )

    eventTimingReference: fhirtypes.ReferenceType = Field(
        None,
        alias="eventTimingReference",
        title=(
            "Type `Reference` referencing `Schedule` (represented as `dict` in " "JSON)"
        ),
        description="Timing of the event",
        one_of_many="eventTiming",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    eventTimingTiming: fhirtypes.TimingType = Field(
        None,
        alias="eventTimingTiming",
        title="Type `Timing` (represented as `dict` in JSON)",
        description="Timing of the event",
        one_of_many="eventTiming",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code`",
        description=(
            "named-event | periodic | data-added | data-modified | data-removed | "
            "data-accessed | data-access-ended"
        ),
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
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
            "eventTiming": [
                "eventTimingDate",
                "eventTimingDateTime",
                "eventTimingReference",
                "eventTimingTiming",
            ]
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
