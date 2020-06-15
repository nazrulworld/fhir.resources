# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Media
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import domainresource, fhirtypes


class Media(domainresource.DomainResource):
    """ A photo, video, or audio recording acquired or used in healthcare. The
    actual content may be inline or provided by direct reference.
    """

    resource_type = Field("Media", const=True)

    basedOn: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title=(
            "List of `Reference` items referencing `ProcedureRequest` (represented "
            "as `dict` in JSON)"
        ),
        description="Procedure that caused this media to be created",
    )

    bodySite: fhirtypes.CodeableConceptType = Field(
        None,
        alias="bodySite",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Body part in media",
    )

    content: fhirtypes.AttachmentType = Field(
        ...,
        alias="content",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="Actual Media - reference or data",
    )

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title=(
            "Type `Reference` referencing `Encounter, EpisodeOfCare` (represented "
            "as `dict` in JSON)"
        ),
        description="Encounter / Episode associated with media",
    )

    device: fhirtypes.ReferenceType = Field(
        None,
        alias="device",
        title=(
            "Type `Reference` referencing `Device, DeviceMetric` (represented as "
            "`dict` in JSON)"
        ),
        description="Observing Device",
    )

    duration: fhirtypes.UnsignedInt = Field(
        None,
        alias="duration",
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="Length in seconds (audio / video)",
    )

    frames: fhirtypes.PositiveInt = Field(
        None,
        alias="frames",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Number of frames if \u003e 1 (photo)",
    )

    height: fhirtypes.PositiveInt = Field(
        None,
        alias="height",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Height of the image in pixels (photo/video)",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Identifier(s) for the image",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Comments made about the media",
    )

    occurrenceDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurrenceDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When Media was collected",
        one_of_many="occurrence",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    occurrencePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="occurrencePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When Media was collected",
        one_of_many="occurrence",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    operator: fhirtypes.ReferenceType = Field(
        None,
        alias="operator",
        title=(
            "Type `Reference` referencing `Practitioner` (represented as `dict` in "
            "JSON)"
        ),
        description="The person who generated the image",
    )

    reasonCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Why was event performed?",
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title=(
            "Type `Reference` referencing `Patient, Practitioner, Group, Device, "
            "Specimen` (represented as `dict` in JSON)"
        ),
        description="Who/What this Media is a record of",
    )

    subtype: fhirtypes.CodeableConceptType = Field(
        None,
        alias="subtype",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The type of acquisition equipment/process",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="photo | video | audio",
    )

    view: fhirtypes.CodeableConceptType = Field(
        None,
        alias="view",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Imaging view, e.g. Lateral or Antero-posterior",
    )

    width: fhirtypes.PositiveInt = Field(
        None,
        alias="width",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Width of the image in pixels (photo/video)",
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
        one_of_many_fields = {"occurrence": ["occurrenceDateTime", "occurrencePeriod"]}
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
