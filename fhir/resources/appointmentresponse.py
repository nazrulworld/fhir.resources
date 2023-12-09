# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AppointmentResponse
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import domainresource, fhirtypes


class AppointmentResponse(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A reply to an appointment request for a patient and/or practitioner(s),
    such as a confirmation or rejection.
    """

    resource_type = Field("AppointmentResponse", const=True)

    actor: fhirtypes.ReferenceType = Field(
        None,
        alias="actor",
        title="Person(s), Location, HealthcareService, or Device",
        description=(
            "A Person, Location, HealthcareService, or Device that is participating"
            " in the appointment."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "Group",
            "Practitioner",
            "PractitionerRole",
            "RelatedPerson",
            "Device",
            "HealthcareService",
            "Location",
        ],
    )

    appointment: fhirtypes.ReferenceType = Field(
        ...,
        alias="appointment",
        title="Appointment this response relates to",
        description="Appointment that this response is replying to.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Appointment"],
    )

    comment: fhirtypes.Markdown = Field(
        None,
        alias="comment",
        title="Additional comments",
        description="Additional comments about the appointment.",
        # if property is element of this resource.
        element_property=True,
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    end: fhirtypes.Instant = Field(
        None,
        alias="end",
        title="Time from appointment, or requested new end time",
        description=(
            "This may be either the same as the appointment request to confirm the "
            "details of the appointment, or alternately a new time to request a re-"
            "negotiation of the end time."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    end__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_end", title="Extension field for ``end``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="External Ids for this item",
        description=(
            "This records identifiers associated with this appointment response "
            "concern that are defined by business processes and/ or used to refer "
            "to it when a direct URL reference to the resource itself is not "
            "appropriate."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    occurrenceDate: fhirtypes.Date = Field(
        None,
        alias="occurrenceDate",
        title="Original date within a recurring request",
        description=(
            "The original date within a recurring request. This could be used in "
            "place of the recurrenceId to be more direct (or where the template is "
            "provided through the simple list of dates in "
            "`Appointment.occurrenceDate`)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    occurrenceDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_occurrenceDate", title="Extension field for ``occurrenceDate``."
    )

    participantStatus: fhirtypes.Code = Field(
        None,
        alias="participantStatus",
        title="accepted | declined | tentative | needs-action | entered-in-error",
        description=(
            "Participation status of the participant. When the status is declined "
            "or tentative if the start/end times are different to the appointment, "
            "then these times should be interpreted as a requested time change. "
            "When the status is accepted, the times can either be the time of the "
            "appointment (as a confirmation of the time) or can be empty."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "accepted",
            "declined",
            "tentative",
            "needs-action",
            "entered-in-error",
        ],
    )
    participantStatus__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_participantStatus",
        title="Extension field for ``participantStatus``.",
    )

    participantType: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="participantType",
        title="Role of participant in the appointment",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    proposedNewTime: bool = Field(
        None,
        alias="proposedNewTime",
        title="Indicator for a counter proposal",
        description=(
            "Indicates that the response is proposing a different time that was "
            "initially requested.  The new proposed time will be indicated in the "
            "start and end properties."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    proposedNewTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_proposedNewTime", title="Extension field for ``proposedNewTime``."
    )

    recurrenceId: fhirtypes.PositiveInt = Field(
        None,
        alias="recurrenceId",
        title="The recurrence ID of the specific recurring request",
        description=(
            "The recurrence ID (sequence number) of the specific appointment when "
            "responding to a recurring request."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    recurrenceId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_recurrenceId", title="Extension field for ``recurrenceId``."
    )

    recurring: bool = Field(
        None,
        alias="recurring",
        title="This response is for all occurrences in a recurring request",
        description=(
            "Indicates that this AppointmentResponse applies to all occurrences in "
            "a recurring request."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    recurring__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_recurring", title="Extension field for ``recurring``."
    )

    start: fhirtypes.Instant = Field(
        None,
        alias="start",
        title="Time from appointment, or requested new start time",
        description=(
            "Date/Time that the appointment is to take place, or requested new "
            "start time."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    start__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_start", title="Extension field for ``start``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AppointmentResponse`` according specification,
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
            "appointment",
            "proposedNewTime",
            "start",
            "end",
            "participantType",
            "actor",
            "participantStatus",
            "comment",
            "recurring",
            "occurrenceDate",
            "recurrenceId",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2180(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("participantStatus", "participantStatus__ext")]
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
