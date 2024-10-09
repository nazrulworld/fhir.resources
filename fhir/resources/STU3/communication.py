from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Communication
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Communication(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A record of information transmitted from a sender to a receiver.
    An occurrence of information being transmitted; e.g. an alert that was sent
    to a responsible provider, a public health agency was notified about a
    reportable condition.
    """

    __resource_type__ = "Communication"

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

    context: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="context",
        title="Encounter or episode leading to message",
        description="The encounter within which the communication was sent.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter", "EpisodeOfCare"],
        },
    )

    definition: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="definition",
        title="Instantiates protocol or definition",
        description=(
            "A protocol, guideline, or other definition that was adhered to in "
            "whole or in part by this communication event."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["PlanDefinition", "ActivityDefinition"],
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Unique identifier",
        description=(
            "Identifiers associated with this Communication that are defined by "
            "business processes and/ or used to refer to it when a direct URL "
            "reference to the resource itself is not appropriate (e.g. in CDA "
            "documents, or in written / printed documentation)."
        ),
        json_schema_extra={
            "element_property": True,
        },
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

    notDone: bool | None = Field(  # type: ignore
        None,
        alias="notDone",
        title="Communication did not occur",
        description=(
            "If true, indicates that the described communication event did not "
            "actually occur."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    notDone__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_notDone", title="Extension field for ``notDone``."
    )

    notDoneReason: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="notDoneReason",
        title="Why communication did not occur",
        description=(
            "Describes why the communication event did not occur in coded and/or "
            "textual form."
        ),
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
        title="Part of this action",
        description=None,
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

    reasonCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="reasonCode",
        title="Indication for message",
        description="The reason or justification for the communication.",
        json_schema_extra={
            "element_property": True,
        },
    )

    reasonReference: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="reasonReference",
        title="Why was communication done?",
        description=(
            "Indicates another resource whose existence justifies this "
            "communication."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Condition", "Observation"],
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
        title="Message recipient",
        description=(
            "The entity (e.g. person, organization, clinical information system, or"
            " device) which was the target of the communication. If receipts need "
            "to be tracked by individual, a separate resource instance will need to"
            " be created for each recipient. \u00a0Multiple recipient communications are"
            " intended where either a receipt(s) is not tracked (e.g. a mass mail-"
            "out) or is captured in aggregate (all emails confirmed received by a "
            "particular time)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Device",
                "Organization",
                "Patient",
                "Practitioner",
                "RelatedPerson",
                "Group",
            ],
        },
    )

    sender: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="sender",
        title="Message sender",
        description=(
            "The entity (e.g. person, organization, clinical information system, or"
            " device) which was the source of the communication."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Device",
                "Organization",
                "Patient",
                "Practitioner",
                "RelatedPerson",
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
            "preparation | in-progress | suspended | aborted | completed | entered-"
            "in-error"
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
                "suspended",
                "aborted",
                "completed",
                "entered-in-error",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
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

    topic: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="topic",
        title="Focal resources",
        description=(
            "The resources which were responsible for or related to producing this "
            "communication."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
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
            "definition",
            "basedOn",
            "partOf",
            "status",
            "notDone",
            "notDoneReason",
            "category",
            "medium",
            "subject",
            "recipient",
            "topic",
            "context",
            "sent",
            "received",
            "sender",
            "reasonCode",
            "reasonReference",
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

    contentString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="contentString",
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
    contentString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_contentString", title="Extension field for ``contentString``."
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
            "contentString",
            "contentAttachment",
            "contentReference",
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
            "content": ["contentAttachment", "contentReference", "contentString"]
        }
        return one_of_many_fields
