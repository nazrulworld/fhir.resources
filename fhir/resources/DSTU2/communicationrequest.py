# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CommunicationRequest
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import fhirtypes
from .backboneelement import BackboneElement
from .domainresource import DomainResource


class CommunicationRequest(DomainResource):
    """A request for information to be sent to a receiver.

    A request to convey information; e.g. the CDS system proposes that an alert
    be sent to a responsible provider, the CDS system proposes that the public
    health agency be notified about a reportable condition.
    """

    resource_type = Field("CommunicationRequest", const=True)

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Message category.",
    )
    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Type `Reference` referencing `Encounter` (represented as `dict` in JSON).",
        description="Encounter leading to message.",
    )
    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON).",
        description="Unique identifier.",
    )
    medium: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="medium",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="A channel of communication.",
    )
    payload: ListType[fhirtypes.CommunicationRequestPayloadType] = Field(
        None,
        alias="medium",
        title="List of `CommunicationRequestPayload` items (represented as `dict` in JSON).",
        description="A channel of communication.",
    )

    priority: fhirtypes.CodeableConceptType = Field(
        None,
        alias="priority",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Message urgency.",
    )
    reason: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reason",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Indication for message.",
    )
    recipient: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="recipient",
        title=(
            "List of `Reference` items referencing `Device, "
            "Organization, Patient, Practitioner, RelatedPerson`"
            " (represented as `dict` in JSON)."
        ),
        description="Message recipient.",
    )

    requestedOn: fhirtypes.DateTime = Field(
        None,
        alias="requestedOn",
        title="Type `DateTime",
        description="When ordered or proposed.",
    )
    requester: fhirtypes.ReferenceType = Field(
        None,
        alias="requester",
        title=(
            "Type `Reference` referencing `Practitioner, Patient, "
            "RelatedPerson` (represented as `dict` in JSON)."
        ),
        description="An individual who requested a communication.",
    )

    scheduledDateTime: fhirtypes.DateTime = Field(
        None,
        alias="scheduledDateTime",
        title="Type `DateTime",
        description="When scheduled.",
        one_of_many="scheduled",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    scheduledPeriod: fhirtypes.DateTime = Field(
        None,
        alias="scheduledPeriod",
        title="Type `Period` (represented as `dict` in JSON).",
        description="When scheduled.",
        one_of_many="scheduled",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    sender: fhirtypes.ReferenceType = Field(
        None,
        alias="sender",
        title=(
            "Type `Reference` referencing `Device, Organization, "
            "Patient, Practitioner, RelatedPerson` "
            "(represented as `dict` in JSON)."
        ),
        description="Message sender.",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `str`.",
        description=(
            "proposed | planned | requested | "
            "received | accepted | in-progress"
            "| completed | suspended | rejected | failed."
        ),
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON).",
        description="Focus of message.",
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
        one_of_many_fields = {"scheduled": ["scheduledDateTime", "scheduledPeriod"]}
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


class CommunicationRequestPayload(BackboneElement):
    """Message payload.

    Text, attachment(s), or resource(s) to be communicated to the recipient.
    """

    resource_type = Field("CommunicationRequestPayload", const=True)

    contentAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="contentAttachment",
        title="Type `Attachment` (represented as `dict` in JSON).",
        description="Message part content",
        one_of_many="content",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    contentReference: fhirtypes.ReferenceType = Field(
        None,
        alias="contentReference",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON).",
        description="Message part content.",
        one_of_many="content",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    contentString: fhirtypes.String = Field(
        None,
        alias="contentString",
        title="Type `str`.",
        description="Message part content.",
        one_of_many="content",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
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
            "content": ["contentString", "contentReference", "contentAttachment"]
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
