# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Media
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import domainresource, fhirtypes


class Media(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A photo, video, or audio recording acquired or used in healthcare. The
    actual content may be inline or provided by direct reference.
    """

    resource_type = Field("Media", const=True)

    basedOn: typing.List[fhirtypes.ReferenceType] = Field(
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
        enum_reference_types=["ProcedureRequest"],
    )

    bodySite: fhirtypes.CodeableConceptType = Field(
        None,
        alias="bodySite",
        title="Body part in media",
        description=(
            "Indicates the site on the subject's body where the media was collected"
            " (i.e. the target site)."
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

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title="Encounter / Episode associated with media",
        description=(
            "The encounter or episode of care that establishes the context for this"
            " media."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter", "EpisodeOfCare"],
    )

    device: fhirtypes.ReferenceType = Field(
        None,
        alias="device",
        title="Observing Device",
        description="The device used to collect the media.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device", "DeviceMetric"],
    )

    duration: fhirtypes.UnsignedInt = Field(
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

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
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

    note: typing.List[fhirtypes.AnnotationType] = Field(
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

    occurrenceDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurrenceDateTime",
        title="When Media was collected",
        description="The date and time(s) at which the media was collected.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_occurrenceDateTime",
        title="Extension field for ``occurrenceDateTime``.",
    )

    occurrencePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="occurrencePeriod",
        title="When Media was collected",
        description="The date and time(s) at which the media was collected.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )

    operator: fhirtypes.ReferenceType = Field(
        None,
        alias="operator",
        title="The person who generated the image",
        description="The person who administered the collection of the image.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    reasonCode: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="Why was event performed?",
        description="Describes why the event occurred in coded or textual form.",
        # if property is element of this resource.
        element_property=True,
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Who/What this Media is a record of",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Practitioner", "Group", "Device", "Specimen"],
    )

    subtype: fhirtypes.CodeableConceptType = Field(
        None,
        alias="subtype",
        title="The type of acquisition equipment/process",
        description=(
            "Details of the type of the media - usually, how it was acquired (what "
            "type of device). If images sourced from a DICOM system, are wrapped in"
            " a Media resource, then this is the modality."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="photo | video | audio",
        description=(
            "Whether the media is a photo (still image), an audio recording, or a "
            "video recording."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["photo", "video", "audio"],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_654(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("type", "type__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_654(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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
