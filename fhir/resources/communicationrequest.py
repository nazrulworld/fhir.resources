# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CommunicationRequest
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class CommunicationRequest(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A request for information to be sent to a receiver.
    A request to convey information; e.g. the CDS system proposes that an alert
    be sent to a responsible provider, the CDS system proposes that the public
    health agency be notified about a reportable condition.
    """

    resource_type = Field("CommunicationRequest", const=True)

    about: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="about",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="Resources that pertain to this communication request",
    )

    authoredOn: fhirtypes.DateTime = Field(
        None,
        alias="authoredOn",
        title="Type `DateTime`",
        description="When request transitioned to being actionable",
    )
    authoredOn__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_authoredOn", title="Extension field for ``authoredOn``."
    )

    basedOn: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="Fulfills plan or proposal",
    )

    category: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Message category",
    )

    doNotPerform: bool = Field(
        None,
        alias="doNotPerform",
        title="Type `bool`",
        description="True if request is prohibiting action",
    )
    doNotPerform__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_doNotPerform", title="Extension field for ``doNotPerform``."
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title=(
            "Type `Reference` referencing `Encounter` (represented as `dict` in "
            "JSON)"
        ),
        description="Encounter created as part of",
    )

    groupIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="groupIdentifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Composite request this is part of",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Unique identifier",
    )

    medium: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="medium",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="A channel of communication",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Comments made about communication request",
    )

    occurrenceDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurrenceDateTime",
        title="Type `DateTime`",
        description="When scheduled",
        one_of_many="occurrence",  # Choice of Data Types. i.e value[x]
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
        title="Type `Period` (represented as `dict` in JSON)",
        description="When scheduled",
        one_of_many="occurrence",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    payload: ListType[fhirtypes.CommunicationRequestPayloadType] = Field(
        None,
        alias="payload",
        title=(
            "List of `CommunicationRequestPayload` items (represented as `dict` in "
            "JSON)"
        ),
        description="Message payload",
    )

    priority: fhirtypes.Code = Field(
        None,
        alias="priority",
        title="Type `Code`",
        description="routine | urgent | asap | stat",
    )
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_priority", title="Extension field for ``priority``."
    )

    reasonCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Why is communication needed?",
    )

    reasonReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title=(
            "List of `Reference` items referencing `Condition, Observation, "
            "DiagnosticReport, DocumentReference` (represented as `dict` in JSON)"
        ),
        description="Why is communication needed?",
    )

    recipient: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="recipient",
        title=(
            "List of `Reference` items referencing `Device, Organization, Patient, "
            "Practitioner, PractitionerRole, RelatedPerson, Group, CareTeam, "
            "HealthcareService` (represented as `dict` in JSON)"
        ),
        description="Message recipient",
    )

    replaces: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="replaces",
        title=(
            "List of `Reference` items referencing `CommunicationRequest` "
            "(represented as `dict` in JSON)"
        ),
        description="Request(s) replaced by this request",
    )

    requester: fhirtypes.ReferenceType = Field(
        None,
        alias="requester",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole, "
            "Organization, Patient, RelatedPerson, Device` (represented as `dict` "
            "in JSON)"
        ),
        description="Who/what is requesting service",
    )

    sender: fhirtypes.ReferenceType = Field(
        None,
        alias="sender",
        title=(
            "Type `Reference` referencing `Device, Organization, Patient, "
            "Practitioner, PractitionerRole, RelatedPerson, HealthcareService` "
            "(represented as `dict` in JSON)"
        ),
        description="Message sender",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`",
        description=(
            "draft | active | on-hold | revoked | completed | entered-in-error | "
            "unknown"
        ),
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    statusReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="statusReason",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Reason for current status",
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title=(
            "Type `Reference` referencing `Patient, Group` (represented as `dict` "
            "in JSON)"
        ),
        description="Focus of message",
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


class CommunicationRequestPayload(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Message payload.
    Text, attachment(s), or resource(s) to be communicated to the recipient.
    """

    resource_type = Field("CommunicationRequestPayload", const=True)

    contentAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="contentAttachment",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="Message part content",
        one_of_many="content",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    contentReference: fhirtypes.ReferenceType = Field(
        None,
        alias="contentReference",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Message part content",
        one_of_many="content",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    contentString: fhirtypes.String = Field(
        None,
        alias="contentString",
        title="Type `String`",
        description="Message part content",
        one_of_many="content",  # Choice of Data Types. i.e value[x]
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
