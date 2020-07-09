# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Media
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import domainresource, fhirtypes


class Media(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A photo, video, or audio recording acquired or used in healthcare. The
    actual content may be inline or provided by direct reference.
    """

    resource_type = Field("Media", const=True)

    basedOn: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="Procedure that caused this media to be created",
        description=(
            "A procedure that is fulfilled in whole or in part by the creation of "
            "this media."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ServiceRequest", "CarePlan"],
    )

    bodySite: fhirtypes.CodeableConceptType = Field(
        None,
        alias="bodySite",
        title="Observed body part",
        description=(
            "Indicates the site on the subject's body where the observation was "
            "made (i.e. the target site)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    content: fhirtypes.AttachmentType = Field(
        ...,
        alias="content",
        title="Actual Media - reference or data",
        description=(
            "The actual content of the media - inline or by direct reference to the"
            " media source file."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    createdDateTime: fhirtypes.DateTime = Field(
        None,
        alias="createdDateTime",
        title="When Media was collected",
        description="The date and time(s) at which the media was collected.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e created[x]
        one_of_many="created",
        one_of_many_required=False,
    )
    createdDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_createdDateTime", title="Extension field for ``createdDateTime``."
    )

    createdPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="createdPeriod",
        title="When Media was collected",
        description="The date and time(s) at which the media was collected.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e created[x]
        one_of_many="created",
        one_of_many_required=False,
    )

    device: fhirtypes.ReferenceType = Field(
        None,
        alias="device",
        title="Observing Device",
        description="The device used to collect the media.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device", "DeviceMetric", "Device"],
    )

    deviceName: fhirtypes.String = Field(
        None,
        alias="deviceName",
        title="Name of the device/manufacturer",
        description=(
            "The name of the device / manufacturer of the device  that was used to "
            "make the recording."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    deviceName__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_deviceName", title="Extension field for ``deviceName``."
    )

    duration: fhirtypes.Decimal = Field(
        None,
        alias="duration",
        title="Length in seconds (audio / video)",
        description="The duration of the recording in seconds - for audio and video.",
        # if property is element of this resource.
        element_property=True,
    )
    duration__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_duration", title="Extension field for ``duration``."
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Encounter associated with media",
        description="The encounter that establishes the context for this media.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    frames: fhirtypes.PositiveInt = Field(
        None,
        alias="frames",
        title="Number of frames if > 1 (photo)",
        description=(
            "The number of frames in a photo. This is used with a multi-page fax, "
            "or an imaging acquisition context that takes multiple slices in a "
            "single image, or an animated gif. If there is more than one frame, "
            "this SHALL have a value in order to alert interface software that a "
            "multi-frame capable rendering widget is required."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    frames__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_frames", title="Extension field for ``frames``."
    )

    height: fhirtypes.PositiveInt = Field(
        None,
        alias="height",
        title="Height of the image in pixels (photo/video)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    height__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_height", title="Extension field for ``height``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Identifier(s) for the image",
        description=(
            "Identifiers associated with the image - these may include identifiers "
            "for the image itself, identifiers for the context of its collection "
            "(e.g. series ids) and context ids such as accession numbers or other "
            "workflow identifiers."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    issued: fhirtypes.Instant = Field(
        None,
        alias="issued",
        title="Date/Time this version was made available",
        description=(
            "The date and time this version of the media was made available to "
            "providers, typically after having been reviewed."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    issued__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_issued", title="Extension field for ``issued``."
    )

    modality: fhirtypes.CodeableConceptType = Field(
        None,
        alias="modality",
        title="The type of acquisition equipment/process",
        description=(
            "Details of the type of the media - usually, how it was acquired (what "
            "type of device). If images sourced from a DICOM system, are wrapped in"
            " a Media resource, then this is the modality."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Comments made about the media",
        description=(
            "Comments made about the media by the performer, subject or other "
            "participants."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    operator: fhirtypes.ReferenceType = Field(
        None,
        alias="operator",
        title="The person who generated the image",
        description="The person who administered the collection of the image.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "Organization",
            "CareTeam",
            "Patient",
            "Device",
            "RelatedPerson",
        ],
    )

    partOf: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title="Part of referenced event",
        description="A larger event of which this particular event is a component or step.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    reasonCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="Why was event performed?",
        description="Describes why the event occurred in coded or textual form.",
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title=(
            "preparation | in-progress | not-done | on-hold | stopped | completed |"
            " entered-in-error | unknown"
        ),
        description="The current state of the {{title}}.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "preparation",
            "in-progress",
            "not-done",
            "on-hold",
            "stopped",
            "completed",
            "entered-in-error",
            "unknown",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Who/What this Media is a record of",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "Practitioner",
            "PractitionerRole",
            "Group",
            "Device",
            "Specimen",
            "Location",
        ],
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Classification of media as image, video, or audio",
        description=(
            "A code that classifies whether the media is an image, video or audio "
            "recording or some other media category."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    view: fhirtypes.CodeableConceptType = Field(
        None,
        alias="view",
        title="Imaging view, e.g. Lateral or Antero-posterior",
        description="The name of the imaging view e.g. Lateral or Antero-posterior (AP).",
        # if property is element of this resource.
        element_property=True,
    )

    width: fhirtypes.PositiveInt = Field(
        None,
        alias="width",
        title="Width of the image in pixels (photo/video)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    width__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_width", title="Extension field for ``width``."
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
        one_of_many_fields = {"created": ["createdDateTime", "createdPeriod"]}
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
