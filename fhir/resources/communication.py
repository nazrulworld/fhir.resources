from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Communication
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Communication(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A clinical or business level record of information being transmitted or
    shared.
    A clinical or business level record of information being transmitted or
    shared; e.g. an alert that was sent to a responsible provider, a public
    health agency communication to a provider/reporter in response to a case
    report for a reportable condition.
    """

    __resource_type__ = "Communication"

    about: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="about",
        title="Resources that pertain to this communication",
        description=(
            "Other resources that pertain to this communication and to which this "
            "communication should be associated."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    basedOn: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="basedOn",
        title="Request fulfilled by this communication",
        description=(
            "An order, proposal or plan fulfilled in whole or in part by this "
            "Communication."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    category: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="category",
        title="Message category",
        description=(
            "The type of message conveyed such as alert, notification, reminder, "
            "instruction, etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    encounter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="encounter",
        title="The Encounter during which this Communication was created",
        description=(
            "The Encounter during which this Communication was created or to which "
            "the creation of this record is tightly associated."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter"],
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Unique identifier",
        description=(
            "Business identifiers assigned to this communication by the performer "
            "or other systems which remain constant as the resource is updated and "
            "propagates from server to server."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    inResponseTo: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="inResponseTo",
        title="Reply to",
        description="Prior communication that this communication is in response to.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Communication"],
        },
    )

    instantiatesCanonical: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="instantiatesCanonical",
        title="Instantiates FHIR protocol or definition",
        description=(
            "The URL pointing to a FHIR-defined protocol, guideline, orderset or "
            "other definition that is adhered to in whole or in part by this "
            "Communication."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "PlanDefinition",
                "ActivityDefinition",
                "Measure",
                "OperationDefinition",
                "Questionnaire",
            ],
        },
    )
    instantiatesCanonical__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_instantiatesCanonical",
        title="Extension field for ``instantiatesCanonical``.",
    )

    instantiatesUri: typing.List[fhirtypes.UriType | None] | None = Field(  # type: ignore
        None,
        alias="instantiatesUri",
        title="Instantiates external protocol or definition",
        description=(
            "The URL pointing to an externally maintained protocol, guideline, "
            "orderset or other definition that is adhered to in whole or in part by"
            " this Communication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    instantiatesUri__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_instantiatesUri", title="Extension field for ``instantiatesUri``."
    )

    medium: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="medium",
        title="A channel of communication",
        description="A channel that was used for this communication (e.g. email, fax).",
        json_schema_extra={
            "element_property": True,
        },
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="note",
        title="Comments made about the communication",
        description=(
            "Additional notes or commentary about the communication by the sender, "
            "receiver or other interested parties."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    partOf: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="partOf",
        title="Part of referenced event (e.g. Communication, Procedure)",
        description=(
            "A larger event (e.g. Communication, Procedure) of which this "
            "particular communication is a component or step."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    payload: typing.List[fhirtypes.CommunicationPayloadType] | None = Field(  # type: ignore
        None,
        alias="payload",
        title="Message payload",
        description=(
            "Text, attachment(s), or resource(s) that was communicated to the "
            "recipient."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    priority: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="priority",
        title="routine | urgent | asap | stat",
        description=(
            "Characterizes how quickly the planned or in progress communication "
            "must be addressed. Includes concepts such as stat, urgent, routine."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["routine", "urgent", "asap", "stat"],
        },
    )
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_priority", title="Extension field for ``priority``."
    )

    reason: typing.List[fhirtypes.CodeableReferenceType] | None = Field(  # type: ignore
        None,
        alias="reason",
        title="Indication for message",
        description="The reason or justification for the communication.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    received: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="received",
        title="When received",
        description="The time when this communication arrived at the destination.",
        json_schema_extra={
            "element_property": True,
        },
    )
    received__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_received", title="Extension field for ``received``."
    )

    recipient: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="recipient",
        title="Who the information is shared with",
        description=(
            "The entity (e.g. person, organization, clinical information system, "
            "care team or device) which is the target of the communication."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "CareTeam",
                "Device",
                "Group",
                "HealthcareService",
                "Location",
                "Organization",
                "Patient",
                "Practitioner",
                "PractitionerRole",
                "RelatedPerson",
                "Endpoint",
            ],
        },
    )

    sender: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="sender",
        title="Who shares the information",
        description=(
            "The entity (e.g. person, organization, clinical information system, or"
            " device) which is the source of the communication."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Device",
                "Organization",
                "Patient",
                "Practitioner",
                "PractitionerRole",
                "RelatedPerson",
                "HealthcareService",
                "Endpoint",
                "CareTeam",
            ],
        },
    )

    sent: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="sent",
        title="When sent",
        description="The time when this communication was sent.",
        json_schema_extra={
            "element_property": True,
        },
    )
    sent__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sent", title="Extension field for ``sent``."
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title=(
            "preparation | in-progress | not-done | on-hold | stopped | completed |"
            " entered-in-error | unknown"
        ),
        description="The status of the transmission.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "preparation",
                "in-progress",
                "not-done",
                "on-hold",
                "stopped",
                "completed",
                "entered-in-error",
                "unknown",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    statusReason: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="statusReason",
        title="Reason for current status",
        description="Captures the reason for the current state of the Communication.",
        json_schema_extra={
            "element_property": True,
        },
    )

    subject: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="subject",
        title="Focus of message",
        description="The patient or group that was the focus of this communication.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "Group"],
        },
    )

    topic: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="topic",
        title="Description of the purpose/content",
        description=(
            "Description of the purpose/content, similar to a subject line in an "
            "email."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Communication`` according specification,
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
            "instantiatesCanonical",
            "instantiatesUri",
            "basedOn",
            "partOf",
            "inResponseTo",
            "status",
            "statusReason",
            "category",
            "priority",
            "medium",
            "subject",
            "topic",
            "about",
            "encounter",
            "sent",
            "received",
            "recipient",
            "sender",
            "reason",
            "payload",
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
        required_fields = [("status", "status__ext")]
        return required_fields


class CommunicationPayload(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Message payload.
    Text, attachment(s), or resource(s) that was communicated to the recipient.
    """

    __resource_type__ = "CommunicationPayload"

    contentAttachment: fhirtypes.AttachmentType | None = Field(  # type: ignore
        None,
        alias="contentAttachment",
        title="Message part content",
        description=(
            "A communicated content (or for multi-part communications, one portion "
            "of the communication)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e content[x]
            "one_of_many": "content",
            "one_of_many_required": True,
        },
    )

    contentCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="contentCodeableConcept",
        title="Message part content",
        description=(
            "A communicated content (or for multi-part communications, one portion "
            "of the communication)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e content[x]
            "one_of_many": "content",
            "one_of_many_required": True,
        },
    )

    contentReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="contentReference",
        title="Message part content",
        description=(
            "A communicated content (or for multi-part communications, one portion "
            "of the communication)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e content[x]
            "one_of_many": "content",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CommunicationPayload`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "contentAttachment",
            "contentReference",
            "contentCodeableConcept",
        ]

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
        one_of_many_fields = {
            "content": [
                "contentAttachment",
                "contentCodeableConcept",
                "contentReference",
            ]
        }
        return one_of_many_fields
