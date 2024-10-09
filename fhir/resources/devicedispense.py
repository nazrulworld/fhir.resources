from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceDispense
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class DeviceDispense(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A record of dispensation of a device.
    A record of dispensation of a device - i.e., assigning a device to a
    patient, or to a professional for their use.
    """

    __resource_type__ = "DeviceDispense"

    basedOn: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="basedOn",
        title="The order or request that this dispense is fulfilling",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["CarePlan", "DeviceRequest"],
        },
    )

    category: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="category",
        title="Type of device dispense",
        description="Indicates the type of device dispense.",
        json_schema_extra={
            "element_property": True,
        },
    )

    destination: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="destination",
        title="Where the device was sent or should be sent",
        description=(
            "Identification of the facility/location where the device was /should "
            "be shipped to, as part of the dispense process."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    device: fhirtypes.CodeableReferenceType = Field(  # type: ignore
        ...,
        alias="device",
        title="What device was supplied",
        description=(
            "Identifies the device being dispensed. This is either a link to a "
            "resource representing the details of the device or a simple attribute "
            "carrying a code that identifies the device from a known list of "
            "devices."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Device", "DeviceDefinition"],
        },
    )

    encounter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="encounter",
        title="Encounter associated with event",
        description="The encounter that establishes the context for this event.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter"],
        },
    )

    eventHistory: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="eventHistory",
        title="A list of relevant lifecycle events",
        description=(
            "A summary of the events of interest that have occurred, such as when "
            "the dispense was verified."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Provenance"],
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business identifier for this dispensation",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    location: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="location",
        title="Where the dispense occurred",
        description="The principal physical location where the dispense was performed.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="note",
        title="Information about the dispense",
        description=(
            "Extra information about the dispense that could not be conveyed in the"
            " other attributes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    partOf: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="partOf",
        title="The bigger event that this dispense is a part of",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Procedure"],
        },
    )

    performer: typing.List[fhirtypes.DeviceDispensePerformerType] | None = Field(  # type: ignore
        None,
        alias="performer",
        title="Who performed event",
        description="Indicates who or what performed the event.",
        json_schema_extra={
            "element_property": True,
        },
    )

    preparedDate: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="preparedDate",
        title="When product was packaged and reviewed",
        description="The time when the dispensed product was packaged and reviewed.",
        json_schema_extra={
            "element_property": True,
        },
    )
    preparedDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_preparedDate", title="Extension field for ``preparedDate``."
    )

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="Amount dispensed",
        description="The number of devices that have been dispensed.",
        json_schema_extra={
            "element_property": True,
        },
    )

    receiver: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="receiver",
        title="Who collected the device or where the medication was delivered",
        description=(
            "Identifies the person who picked up the device or the person or "
            "location where the device was delivered.  This may be a patient or "
            "their caregiver, but some cases exist where it can be a healthcare "
            "professional or a location."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Patient",
                "Practitioner",
                "RelatedPerson",
                "Location",
                "PractitionerRole",
            ],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title=(
            "preparation | in-progress | cancelled | on-hold | completed | entered-"
            "in-error | stopped | declined | unknown"
        ),
        description="A code specifying the state of the set of dispense events.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
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
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    statusReason: fhirtypes.CodeableReferenceType | None = Field(  # type: ignore
        None,
        alias="statusReason",
        title="Why a dispense was or was not performed",
        description="Indicates the reason why a dispense was or was not performed.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DetectedIssue"],
        },
    )

    subject: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="subject",
        title="Who the dispense is for",
        description=(
            "A link to a resource representing the person to whom the device is "
            "intended."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "Practitioner"],
        },
    )

    supportingInformation: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="supportingInformation",
        title="Information that supports the dispensing of the device",
        description="Additional information that supports the device being dispensed.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Trial fill, partial fill, emergency fill, etc",
        description="Indicates the type of dispensing event that is performed.",
        json_schema_extra={
            "element_property": True,
        },
    )

    usageInstruction: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="usageInstruction",
        title="Full representation of the usage instructions",
        description="The full representation of the instructions.",
        json_schema_extra={
            "element_property": True,
        },
    )
    usageInstruction__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_usageInstruction",
        title="Extension field for ``usageInstruction``.",
    )

    whenHandedOver: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="whenHandedOver",
        title="When product was given out",
        description=(
            "The time the dispensed product was made available to the patient or "
            "their representative."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    whenHandedOver__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
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

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        return required_fields


class DeviceDispensePerformer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who performed event.
    Indicates who or what performed the event.
    """

    __resource_type__ = "DeviceDispensePerformer"

    actor: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="actor",
        title="Individual who was performing",
        description=(
            "The device, practitioner, etc. who performed the action.  It should be"
            " assumed that the actor is the dispenser of the device."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
                "Patient",
                "Device",
                "RelatedPerson",
                "CareTeam",
            ],
        },
    )

    function: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="function",
        title="Who performed the dispense and what they did",
        description=(
            "Distinguishes the type of performer in the dispense.  For example, "
            "date enterer, packager, final checker."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceDispensePerformer`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "function", "actor"]
