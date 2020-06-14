# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Communication
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Communication(domainresource.DomainResource):
    """ A record of information transmitted from a sender to a receiver.
    An occurrence of information being transmitted; e.g. an alert that was sent
    to a responsible provider, a public health agency was notified about a
    reportable condition.
    """

    resource_type = Field("Communication", const=True)

    basedOn: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="List of `Reference` items referencing `Resource` (represented as `dict` in JSON)",
        description="Request fulfilled by this communication",
    )

    category: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Message category",
    )

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title="Type `Reference` referencing `Encounter, EpisodeOfCare` (represented as `dict` in JSON)",
        description="Encounter or episode leading to message",
    )

    definition: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="definition",
        title="List of `Reference` items referencing `PlanDefinition, ActivityDefinition` (represented as `dict` in JSON)",
        description="Instantiates protocol or definition",
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

    notDone: bool = Field(
        None,
        alias="notDone",
        title="Type `bool`",
        description="Communication did not occur",
    )

    notDoneReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="notDoneReason",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Why communication did not occur",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Comments made about the communication",
    )

    partOf: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title="List of `Reference` items referencing `Resource` (represented as `dict` in JSON)",
        description="Part of this action",
    )

    payload: ListType[fhirtypes.CommunicationPayloadType] = Field(
        None,
        alias="payload",
        title="List of `CommunicationPayload` items (represented as `dict` in JSON)",
        description="Message payload",
    )

    reasonCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Indication for message",
    )

    reasonReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title="List of `Reference` items referencing `Condition, Observation` (represented as `dict` in JSON)",
        description="Why was communication done?",
    )

    received: fhirtypes.DateTime = Field(
        None,
        alias="received",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When received",
    )

    recipient: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="recipient",
        title="List of `Reference` items referencing `Device, Organization, Patient, Practitioner, RelatedPerson, Group` (represented as `dict` in JSON)",
        description="Message recipient",
    )

    sender: fhirtypes.ReferenceType = Field(
        None,
        alias="sender",
        title="Type `Reference` referencing `Device, Organization, Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON)",
        description="Message sender",
    )

    sent: fhirtypes.DateTime = Field(
        None,
        alias="sent",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When sent",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="preparation | in-progress | suspended | aborted | completed | entered-in-error",
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Type `Reference` referencing `Patient, Group` (represented as `dict` in JSON)",
        description="Focus of message",
    )

    topic: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="topic",
        title="List of `Reference` items referencing `Resource` (represented as `dict` in JSON)",
        description="Focal resources",
    )


class CommunicationPayload(backboneelement.BackboneElement):
    """ Message payload.
    Text, attachment(s), or resource(s) that was communicated to the recipient.
    """

    resource_type = Field("CommunicationPayload", const=True)

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
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="Message part content",
        one_of_many="content",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    contentString: fhirtypes.String = Field(
        None,
        alias="contentString",
        title="Type `String` (represented as `dict` in JSON)",
        description="Message part content",
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
            "content": ["contentAttachment", "contentReference", "contentString",],
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
