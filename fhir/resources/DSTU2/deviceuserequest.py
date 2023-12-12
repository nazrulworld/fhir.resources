# -*- coding: utf-8 -*-
"""
Profile: https://www.hl7.org/fhir/DSTU2/deviceuserequest.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic.v1 import Field, root_validator

from . import domainresource, fhirtypes


class DeviceUseRequest(domainresource.DomainResource):
    """A request for a patient to use or be given a medical device.

    Represents a request for a patient to employ a medical device. The device
    may be an implantable device, or an external assistive device, such as a
    walker.
    """

    resource_type = Field("DeviceUseRequest", const=True)

    bodySiteCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="bodySiteCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Target body site.",
        # Choice of Data Types. i.e bodySite[x]
        one_of_many="bodySite",
        one_of_many_required=False,
    )

    bodySiteReference: fhirtypes.ReferenceType = Field(
        None,
        alias="bodySiteReference",
        title="Type `FHIRReference` referencing `BodySite` (represented as `dict` in JSON).",
        description="Target body site.",
        # Choice of Data Types. i.e bodySite[x]
        one_of_many="bodySite",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["BodySite"],
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Encounter motivating request",
        description=(
            "An encounter that provides additional context in which this request is"
            " made."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="External Request identifier",
        description="Identifiers assigned to this order by the orderer or by the receiver.",
    )

    notes: ListType[fhirtypes.String] = Field(
        None,
        alias="notes",
        title="Notes or comments",
        description=(
            "Details about this request that were not represented at all or "
            "sufficiently in one of the attributes provided in a class. These may "
            "include for example a comment, an instruction, or a note associated "
            "with the statement."
        ),
    )

    priority: fhirtypes.Code = Field(
        None,
        alias="priority",
        title="routine | urgent | asap | stat",
        description=(
            "Indicates how quickly the {{title}} should be addressed with respect "
            "to other requests."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["routine", "urgent", "asap", "stat"],
    )

    prnReason: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="PRN.",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title=(
            "proposed | planned | requested | received | accepted | in-progress | "
            "completed | suspended | rejected | aborted"
        ),
        description="Type `str`.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "proposed",
            "planned",
            "requested",
            "received",
            "accepted",
            "in-progress",
            "completed",
            "suspended",
            "rejected",
            "aborted",
        ],
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Focus of request",
        description="The patient who will use the device.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    device: fhirtypes.ReferenceType = Field(
        ...,
        alias="device",
        title=(
            "Type `FHIRReference` referencing `Device` (represented as `dict` in JSON)."
        ),
        description="Device requested.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device"],
    )

    indication: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="indication",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="Reason for request.",
    )

    orderedOn: fhirtypes.DateTime = Field(
        None,
        alias="orderedOn",
        title="Type `FHIRDate` (represented as `str` in JSON).",
        description="When ordered.",
    )

    recordedOn: fhirtypes.DateTime = Field(
        None,
        alias="recordedOn",
        title="Type `FHIRDate` (represented as `str` in JSON).",
        description="When recorded.",
    )

    timingTiming: fhirtypes.TimingType = Field(
        None,
        alias="timingTiming",
        title="Type `Timing` (represented as `dict` in JSON).",
        description="Schedule for use.",
        # Choice of Data Types. i.e timing[x]
        one_of_many="timing",
        one_of_many_required=False,
    )

    timingPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="timingPeriod",
        title="Type `Period` (represented as `dict` in JSON).",
        description="Schedule for use.",
        # Choice of Data Types. i.e timing[x]
        one_of_many="timing",
        one_of_many_required=False,
    )

    timingDateTime: fhirtypes.DateTime = Field(
        None,
        alias="timingDateTime",
        title="Type `FHIRDate` (represented as `str` in JSON).",
        description="Schedule for use.",
        # Choice of Data Types. i.e timing[x]
        one_of_many="timing",
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
            "bodySite": ["bodySiteCodeableConcept", "bodySiteReference"],
            "timing": ["timingTiming", "timingPeriod", "timingDateTime"],
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
