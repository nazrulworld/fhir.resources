# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Communication
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic.v1 import Field, root_validator

from . import fhirtypes
from .backboneelement import BackboneElement
from .domainresource import DomainResource


class Communication(DomainResource):
    """A record of information transmitted from a sender to a receiver.

    An occurrence of information being transmitted; e.g. an alert that was sent
    to a responsible provider, a public health agency was notified about a
    reportable condition.
    """

    resource_type = Field("Communication", const=True)

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

    payload: ListType[fhirtypes.CommunicationPayloadType] = Field(
        None,
        alias="payload",
        title="List of `CommunicationPayload` items (represented as `dict` in JSON).",
        description="Message payload.",
    )
    reason: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reason",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="Indication for message.",
    )
    received: fhirtypes.DateTime = Field(
        None, alias="received", title="Type DateTime.", description="When received."
    )

    recipient: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="recipient",
        title=(
            "List of `FHIRReference` items referencing `Device, "
            "Organization, Patient, Practitioner, RelatedPerson, "
            "Group` (represented as `dict` in JSON)."
        ),
        description="Message recipient.",
    )
    requestDetail: fhirtypes.ReferenceType = Field(
        None,
        alias="requestDetail",
        title=(
            "Type `Reference` referencing `CommunicationRequest`"
            " (represented as `dict` in JSON)."
        ),
        description="CommunicationRequest producing this message.",
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

    sent: fhirtypes.DateTime = Field(
        None, alias="sent", title="Type `DateTime.", description="When sent."
    )
    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code.",
        description="in-progress | completed | suspended | rejected | failed.",
    )
    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON).",
        description="Focus of message.",
    )


class CommunicationPayload(BackboneElement):
    """Message payload.

    Text, attachment(s), or resource(s) that was communicated to the recipient.
    """

    resource_type = Field("CommunicationPayload", const=True)
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
