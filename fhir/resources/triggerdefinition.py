# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/TriggerDefinition
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import element, fhirtypes


class TriggerDefinition(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Defines an expected trigger for a module.
    A description of a triggering event. Triggering events can be named events,
    data events, or periodic, as determined by the type element.
    """

    resource_type = Field("TriggerDefinition", const=True)

    condition: fhirtypes.ExpressionType = Field(
        None,
        alias="condition",
        title="Type `Expression` (represented as `dict` in JSON)",
        description="Whether the event triggers (boolean expression)",
    )

    data: ListType[fhirtypes.DataRequirementType] = Field(
        None,
        alias="data",
        title="List of `DataRequirement` items (represented as `dict` in JSON)",
        description="Triggering data of the event (multiple = \u0027and\u0027)",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`",
        description="Name or URI that identifies the event",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    timingDate: fhirtypes.Date = Field(
        None,
        alias="timingDate",
        title="Type `Date`",
        description="Timing of the event",
        one_of_many="timing",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    timingDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_timingDate", title="Extension field for ``timingDate``."
    )

    timingDateTime: fhirtypes.DateTime = Field(
        None,
        alias="timingDateTime",
        title="Type `DateTime`",
        description="Timing of the event",
        one_of_many="timing",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    timingDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_timingDateTime", title="Extension field for ``timingDateTime``."
    )

    timingReference: fhirtypes.ReferenceType = Field(
        None,
        alias="timingReference",
        title=(
            "Type `Reference` referencing `Schedule` (represented as `dict` in " "JSON)"
        ),
        description="Timing of the event",
        one_of_many="timing",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    timingTiming: fhirtypes.TimingType = Field(
        None,
        alias="timingTiming",
        title="Type `Timing` (represented as `dict` in JSON)",
        description="Timing of the event",
        one_of_many="timing",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code`",
        description=(
            "named-event | periodic | data-changed | data-added | data-modified | "
            "data-removed | data-accessed | data-access-ended"
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
            "timing": [
                "timingDate",
                "timingDateTime",
                "timingReference",
                "timingTiming",
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
