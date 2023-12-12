# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceDispense
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class DeviceDispense(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A record of dispensation of a device.
    A record of dispensation of a device - i.e., assigning a device to a
    patient, or to a professional for their use.
    """

    resource_type = Field("DeviceDispense", const=True)

    basedOn: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="The order or request that this dispense is fulfilling",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["CarePlan", "DeviceRequest"],
    )

    category: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="Type of device dispense",
        description="Indicates the type of device dispense.",
        # if property is element of this resource.
        element_property=True,
    )

    destination: fhirtypes.ReferenceType = Field(
        None,
        alias="destination",
        title="Where the device was sent or should be sent",
        description=(
            "Identification of the facility/location where the device was /should "
            "be shipped to, as part of the dispense process."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    device: fhirtypes.CodeableReferenceType = Field(
        ...,
        alias="device",
        title="What device was supplied",
        description=(
            "Identifies the device being dispensed. This is either a link to a "
            "resource representing the details of the device or a simple attribute "
            "carrying a code that identifies the device from a known list of "
            "devices."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device", "DeviceDefinition"],
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Encounter associated with event",
        description="The encounter that establishes the context for this event.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    eventHistory: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="eventHistory",
        title="A list of relevant lifecycle events",
        description=(
            "A summary of the events of interest that have occurred, such as when "
            "the dispense was verified."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Provenance"],
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier for this dispensation",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title="Where the dispense occurred",
        description="The principal physical location where the dispense was performed.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Information about the dispense",
        description=(
            "Extra information about the dispense that could not be conveyed in the"
            " other attributes."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    partOf: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title="The bigger event that this dispense is a part of",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Procedure"],
    )

    performer: typing.List[fhirtypes.DeviceDispensePerformerType] = Field(
        None,
        alias="performer",
        title="Who performed event",
        description="Indicates who or what performed the event.",
        # if property is element of this resource.
        element_property=True,
    )

    preparedDate: fhirtypes.DateTime = Field(
        None,
        alias="preparedDate",
        title="When product was packaged and reviewed",
        description="The time when the dispensed product was packaged and reviewed.",
        # if property is element of this resource.
        element_property=True,
    )
    preparedDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_preparedDate", title="Extension field for ``preparedDate``."
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Amount dispensed",
        description="The number of devices that have been dispensed.",
        # if property is element of this resource.
        element_property=True,
    )

    receiver: fhirtypes.ReferenceType = Field(
        None,
        alias="receiver",
        title="Who collected the device or where the medication was delivered",
        description=(
            "Identifies the person who picked up the device or the person or "
            "location where the device was delivered.  This may be a patient or "
            "their caregiver, but some cases exist where it can be a healthcare "
            "professional or a location."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "Practitioner",
            "RelatedPerson",
            "Location",
            "PractitionerRole",
        ],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title=(
            "preparation | in-progress | cancelled | on-hold | completed | entered-"
            "in-error | stopped | declined | unknown"
        ),
        description="A code specifying the state of the set of dispense events.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "preparation",
            "in-progress",
            "cancelled",
            "on-hold",
            "completed",
            "entered-in-error",
            "stopped",
            "declined",
            "unknown",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    statusReason: fhirtypes.CodeableReferenceType = Field(
        None,
        alias="statusReason",
        title="Why a dispense was or was not performed",
        description="Indicates the reason why a dispense was or was not performed.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DetectedIssue"],
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Who the dispense is for",
        description=(
            "A link to a resource representing the person to whom the device is "
            "intended."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Practitioner"],
    )

    supportingInformation: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingInformation",
        title="Information that supports the dispensing of the device",
        description="Additional information that supports the device being dispensed.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Trial fill, partial fill, emergency fill, etc",
        description="Indicates the type of dispensing event that is performed.",
        # if property is element of this resource.
        element_property=True,
    )

    usageInstruction: fhirtypes.Markdown = Field(
        None,
        alias="usageInstruction",
        title="Full representation of the usage instructions",
        description="The full representation of the instructions.",
        # if property is element of this resource.
        element_property=True,
    )
    usageInstruction__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_usageInstruction",
        title="Extension field for ``usageInstruction``.",
    )

    whenHandedOver: fhirtypes.DateTime = Field(
        None,
        alias="whenHandedOver",
        title="When product was given out",
        description=(
            "The time the dispensed product was made available to the patient or "
            "their representative."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    whenHandedOver__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_whenHandedOver", title="Extension field for ``whenHandedOver``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceDispense`` according specification,
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
            "partOf",
            "status",
            "statusReason",
            "category",
            "device",
            "subject",
            "receiver",
            "encounter",
            "supportingInformation",
            "performer",
            "location",
            "type",
            "quantity",
            "preparedDate",
            "whenHandedOver",
            "destination",
            "note",
            "usageInstruction",
            "eventHistory",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1588(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
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


class DeviceDispensePerformer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who performed event.
    Indicates who or what performed the event.
    """

    resource_type = Field("DeviceDispensePerformer", const=True)

    actor: fhirtypes.ReferenceType = Field(
        ...,
        alias="actor",
        title="Individual who was performing",
        description=(
            "The device, practitioner, etc. who performed the action.  It should be"
            " assumed that the actor is the dispenser of the device."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "Organization",
            "Patient",
            "Device",
            "RelatedPerson",
            "CareTeam",
        ],
    )

    function: fhirtypes.CodeableConceptType = Field(
        None,
        alias="function",
        title="Who performed the dispense and what they did",
        description=(
            "Distinguishes the type of performer in the dispense.  For example, "
            "date enterer, packager, final checker."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceDispensePerformer`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "function", "actor"]
