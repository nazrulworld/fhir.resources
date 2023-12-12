# -*- coding: utf-8 -*-
"""
Profile: https://www.hl7.org/fhir/DSTU2/deviceusestatement.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic.v1 import Field, root_validator

from . import domainresource, fhirtypes


class DeviceUseStatement(domainresource.DomainResource):
    """Record of use of a device.

    A record of a device being used by a patient where the record is the result
    of a report from the patient or another clinician.
    """

    resource_type = Field("DeviceUseStatement", const=True)

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

    device: fhirtypes.ReferenceType = Field(
        ...,
        alias="device",
        title="Reference to device used",
        description="The details of the device used.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device"],
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="External identifier for this record",
        description="An external identifier for this statement such as an IRI.",
    )

    notes: ListType[fhirtypes.String] = Field(
        None,
        alias="notes",
        title="Addition details (comments, instructions)",
        description=(
            "Details about the device statement that were not represented at all or"
            " sufficiently in one of the attributes provided in a class. These may "
            "include for example a comment, an instruction, or a note associated "
            "with the statement."
        ),
    )

    recordedOn: fhirtypes.DateTime = Field(
        None,
        alias="recordedOn",
        title="When statement was recorded",
        description="The time at which the statement was made/recorded.",
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Patient using device",
        description="The patient who used the device.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    timingDateTime: fhirtypes.DateTime = Field(
        None,
        alias="timingDateTime",
        title="How often  the device was used",
        description="How often the device was used.",
        # Choice of Data Types. i.e timing[x]
        one_of_many="timing",
        one_of_many_required=False,
    )

    timingPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="timingPeriod",
        title="How often  the device was used",
        description="How often the device was used.",
        # Choice of Data Types. i.e timing[x]
        one_of_many="timing",
        one_of_many_required=False,
    )

    timingTiming: fhirtypes.TimingType = Field(
        None,
        alias="timingTiming",
        title="How often  the device was used",
        description="How often the device was used.",
        # Choice of Data Types. i.e timing[x]
        one_of_many="timing",
        one_of_many_required=False,
    )

    whenUsed: fhirtypes.PeriodType = Field(
        None,
        alias="whenUsed",
        title="Type `Period` (represented as `dict` in JSON).",
        description=None,
    )

    indication: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="indication",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description=None,
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
            "timing": ["timingDateTime", "timingPeriod", "timingTiming"],
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
