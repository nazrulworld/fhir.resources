from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Media
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import domainresource, fhirtypes


class Media(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A photo, video, or audio recording acquired or used in healthcare. The
    actual content may be inline or provided by direct reference.
    """

    __resource_type__ = "Media"

    basedOn: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="basedOn",
        title="Procedure that caused this media to be created",
        description=(
            "A procedure that is fulfilled in whole or in part by the creation of "
            "this media."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ProcedureRequest"],
        },
    )

    bodySite: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="bodySite",
        title="Body part in media",
        description=(
            "Indicates the site on the subject's body where the media was collected"
            " (i.e. the target site)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    content: fhirtypes.AttachmentType = Field(  # type: ignore
        ...,
        alias="content",
        title="Actual Media - reference or data",
        description=(
            "The actual content of the media - inline or by direct reference to the"
            " media source file."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    context: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="context",
        title="Encounter / Episode associated with media",
        description=(
            "The encounter or episode of care that establishes the context for this"
            " media."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter", "EpisodeOfCare"],
        },
    )

    device: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="device",
        title="Observing Device",
        description="The device used to collect the media.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Device", "DeviceMetric"],
        },
    )

    duration: fhirtypes.UnsignedIntType | None = Field(  # type: ignore
        None,
        alias="duration",
        title="Length in seconds (audio / video)",
        description="The duration of the recording in seconds - for audio and video.",
        json_schema_extra={
            "element_property": True,
        },
    )
    duration__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_duration", title="Extension field for ``duration``."
    )

    frames: fhirtypes.PositiveIntType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )
    frames__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_frames", title="Extension field for ``frames``."
    )

    height: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="height",
        title="Height of the image in pixels (photo/video)",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    height__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_height", title="Extension field for ``height``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Identifier(s) for the image",
        description=(
            "Identifiers associated with the image - these may include identifiers "
            "for the image itself, identifiers for the context of its collection "
            "(e.g. series ids) and context ids such as accession numbers or other "
            "workflow identifiers."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="note",
        title="Comments made about the media",
        description=(
            "Comments made about the media by the performer, subject or other "
            "participants."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    occurrenceDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="occurrenceDateTime",
        title="When Media was collected",
        description="The date and time(s) at which the media was collected.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e occurrence[x]
            "one_of_many": "occurrence",
            "one_of_many_required": False,
        },
    )
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_occurrenceDateTime",
        title="Extension field for ``occurrenceDateTime``.",
    )

    occurrencePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="occurrencePeriod",
        title="When Media was collected",
        description="The date and time(s) at which the media was collected.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e occurrence[x]
            "one_of_many": "occurrence",
            "one_of_many_required": False,
        },
    )

    operator: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="operator",
        title="The person who generated the image",
        description="The person who administered the collection of the image.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner"],
        },
    )

    reasonCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="reasonCode",
        title="Why was event performed?",
        description="Describes why the event occurred in coded or textual form.",
        json_schema_extra={
            "element_property": True,
        },
    )

    subject: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="subject",
        title="Who/What this Media is a record of",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Patient",
                "Practitioner",
                "Group",
                "Device",
                "Specimen",
            ],
        },
    )

    subtype: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="subtype",
        title="The type of acquisition equipment/process",
        description=(
            "Details of the type of the media - usually, how it was acquired (what "
            "type of device). If images sourced from a DICOM system, are wrapped in"
            " a Media resource, then this is the modality."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="photo | video | audio",
        description=(
            "Whether the media is a photo (still image), an audio recording, or a "
            "video recording."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["photo", "video", "audio"],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    view: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="view",
        title="Imaging view, e.g. Lateral or Antero-posterior",
        description="The name of the imaging view e.g. Lateral or Antero-posterior (AP).",
        json_schema_extra={
            "element_property": True,
        },
    )

    width: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="width",
        title="Width of the image in pixels (photo/video)",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    width__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_width", title="Extension field for ``width``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Media`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "identifier",
            "basedOn",
            "type",
            "subtype",
            "view",
            "subject",
            "context",
            "occurrenceDateTime",
            "occurrencePeriod",
            "operator",
            "reasonCode",
            "bodySite",
            "device",
            "height",
            "width",
            "frames",
            "duration",
            "content",
            "note",
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
        one_of_many_fields = {"occurrence": ["occurrenceDateTime", "occurrencePeriod"]}
        return one_of_many_fields
