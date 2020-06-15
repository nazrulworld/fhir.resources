# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceUseStatement
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import domainresource, fhirtypes


class DeviceUseStatement(domainresource.DomainResource):
    """ Record of use of a device.
    A record of a device being used by a patient where the record is the result
    of a report from the patient or another clinician.
    """

    resource_type = Field("DeviceUseStatement", const=True)

    bodySite: fhirtypes.CodeableConceptType = Field(
        None,
        alias="bodySite",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Target body site",
    )

    device: fhirtypes.ReferenceType = Field(
        ...,
        alias="device",
        title="Type `Reference` referencing `Device` (represented as `dict` in JSON)",
        description="Reference to device used",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="External identifier for this record",
    )

    indication: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="indication",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Why device was used",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Addition details (comments, instructions)",
    )

    recordedOn: fhirtypes.DateTime = Field(
        None,
        alias="recordedOn",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When statement was recorded",
    )

    source: fhirtypes.ReferenceType = Field(
        None,
        alias="source",
        title=(
            "Type `Reference` referencing `Patient, Practitioner, RelatedPerson` "
            "(represented as `dict` in JSON)"
        ),
        description="Who made the statement",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="active | completed | entered-in-error +",
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title=(
            "Type `Reference` referencing `Patient, Group` (represented as `dict` "
            "in JSON)"
        ),
        description="Patient using device",
    )

    timingDateTime: fhirtypes.DateTime = Field(
        None,
        alias="timingDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="How often  the device was used",
        one_of_many="timing",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    timingPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="timingPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="How often  the device was used",
        one_of_many="timing",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    timingTiming: fhirtypes.TimingType = Field(
        None,
        alias="timingTiming",
        title="Type `Timing` (represented as `dict` in JSON)",
        description="How often  the device was used",
        one_of_many="timing",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    whenUsed: fhirtypes.PeriodType = Field(
        None,
        alias="whenUsed",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Period device was used",
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
            "timing": ["timingDateTime", "timingPeriod", "timingTiming"]
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
