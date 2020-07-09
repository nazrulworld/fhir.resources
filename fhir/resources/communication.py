# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Communication
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType
from typing import Union

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Communication(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A record of information transmitted from a sender to a receiver.
    An occurrence of information being transmitted; e.g. an alert that was sent
    to a responsible provider, a public health agency that was notified about a
    reportable condition.
    """

    resource_type = Field("Communication", const=True)

    about: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="about",
        title="Resources that pertain to this communication",
        description=(
            "Other resources that pertain to this communication and to which this "
            "communication should be associated."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    basedOn: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="Request fulfilled by this communication",
        description=(
            "An order, proposal or plan fulfilled in whole or in part by this "
            "Communication."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    category: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="Message category",
        description=(
            "The type of message conveyed such as alert, notification, reminder, "
            "instruction, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Encounter created as part of",
        description=(
            "The Encounter during which this Communication was created or to which "
            "the creation of this record is tightly associated."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Unique identifier",
        description=(
            "Business identifiers assigned to this communication by the performer "
            "or other systems which remain constant as the resource is updated and "
            "propagates from server to server."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    inResponseTo: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="inResponseTo",
        title="Reply to",
        description="Prior communication that this communication is in response to.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Communication"],
    )

    instantiatesCanonical: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="instantiatesCanonical",
        title="Instantiates FHIR protocol or definition",
        description=(
            "The URL pointing to a FHIR-defined protocol, guideline, orderset or "
            "other definition that is adhered to in whole or in part by this "
            "Communication."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "PlanDefinition",
            "ActivityDefinition",
            "Measure",
            "OperationDefinition",
            "Questionnaire",
        ],
    )
    instantiatesCanonical__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_instantiatesCanonical",
        title="Extension field for ``instantiatesCanonical``.",
    )

    instantiatesUri: ListType[fhirtypes.Uri] = Field(
        None,
        alias="instantiatesUri",
        title="Instantiates external protocol or definition",
        description=(
            "The URL pointing to an externally maintained protocol, guideline, "
            "orderset or other definition that is adhered to in whole or in part by"
            " this Communication."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    instantiatesUri__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_instantiatesUri", title="Extension field for ``instantiatesUri``."
    )

    medium: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="medium",
        title="A channel of communication",
        description="A channel that was used for this communication (e.g. email, fax).",
        # if property is element of this resource.
        element_property=True,
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Comments made about the communication",
        description=(
            "Additional notes or commentary about the communication by the sender, "
            "receiver or other interested parties."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    partOf: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title="Part of this action",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    payload: ListType[fhirtypes.CommunicationPayloadType] = Field(
        None,
        alias="payload",
        title="Message payload",
        description=(
            "Text, attachment(s), or resource(s) that was communicated to the "
            "recipient."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    priority: fhirtypes.Code = Field(
        None,
        alias="priority",
        title="routine | urgent | asap | stat",
        description=(
            "Characterizes how quickly the planned or in progress communication "
            "must be addressed. Includes concepts such as stat, urgent, routine."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["routine", "urgent", "asap", "stat"],
    )
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_priority", title="Extension field for ``priority``."
    )

    reasonCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="Indication for message",
        description="The reason or justification for the communication.",
        # if property is element of this resource.
        element_property=True,
    )

    reasonReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title="Why was communication done?",
        description=(
            "Indicates another resource whose existence justifies this "
            "communication."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Condition",
            "Observation",
            "DiagnosticReport",
            "DocumentReference",
        ],
    )

    received: fhirtypes.DateTime = Field(
        None,
        alias="received",
        title="When received",
        description="The time when this communication arrived at the destination.",
        # if property is element of this resource.
        element_property=True,
    )
    received__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_received", title="Extension field for ``received``."
    )

    recipient: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="recipient",
        title="Message recipient",
        description=(
            "The entity (e.g. person, organization, clinical information system, "
            "care team or device) which was the target of the communication. If "
            "receipts need to be tracked by an individual, a separate resource "
            "instance will need to be created for each recipient.  Multiple "
            "recipient communications are intended where either receipts are not "
            "tracked (e.g. a mass mail-out) or a receipt is captured in aggregate "
            "(all emails confirmed received by a particular time)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Device",
            "Organization",
            "Patient",
            "Practitioner",
            "PractitionerRole",
            "RelatedPerson",
            "Group",
            "CareTeam",
            "HealthcareService",
        ],
    )

    sender: fhirtypes.ReferenceType = Field(
        None,
        alias="sender",
        title="Message sender",
        description=(
            "The entity (e.g. person, organization, clinical information system, or"
            " device) which was the source of the communication."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Device",
            "Organization",
            "Patient",
            "Practitioner",
            "PractitionerRole",
            "RelatedPerson",
            "HealthcareService",
        ],
    )

    sent: fhirtypes.DateTime = Field(
        None,
        alias="sent",
        title="When sent",
        description="The time when this communication was sent.",
        # if property is element of this resource.
        element_property=True,
    )
    sent__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sent", title="Extension field for ``sent``."
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title=(
            "preparation | in-progress | not-done | on-hold | stopped | completed |"
            " entered-in-error | unknown"
        ),
        description="The status of the transmission.",
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

    statusReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="statusReason",
        title="Reason for current status",
        description="Captures the reason for the current state of the Communication.",
        # if property is element of this resource.
        element_property=True,
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Focus of message",
        description="The patient or group that was the focus of this communication.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group"],
    )

    topic: fhirtypes.CodeableConceptType = Field(
        None,
        alias="topic",
        title="Description of the purpose/content",
        description=(
            "Description of the purpose/content, similar to a subject line in an "
            "email."
        ),
        # if property is element of this resource.
        element_property=True,
    )


class CommunicationPayload(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Message payload.
    Text, attachment(s), or resource(s) that was communicated to the recipient.
    """

    resource_type = Field("CommunicationPayload", const=True)

    contentAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="contentAttachment",
        title="Message part content",
        description=(
            "A communicated content (or for multi-part communications, one portion "
            "of the communication)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e content[x]
        one_of_many="content",
        one_of_many_required=True,
    )

    contentReference: fhirtypes.ReferenceType = Field(
        None,
        alias="contentReference",
        title="Message part content",
        description=(
            "A communicated content (or for multi-part communications, one portion "
            "of the communication)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e content[x]
        one_of_many="content",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    contentString: fhirtypes.String = Field(
        None,
        alias="contentString",
        title="Message part content",
        description=(
            "A communicated content (or for multi-part communications, one portion "
            "of the communication)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e content[x]
        one_of_many="content",
        one_of_many_required=True,
    )
    contentString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_contentString", title="Extension field for ``contentString``."
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
            "content": ["contentAttachment", "contentReference", "contentString"]
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
