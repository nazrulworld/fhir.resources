# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MessageHeader
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class MessageHeader(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A resource that describes a message that is exchanged between systems.
    The header for a message exchange that is either requesting or responding
    to an action.  The reference(s) that are the subject of the action as well
    as other information related to the action are typically transmitted in a
    bundle in which the MessageHeader resource instance is the first resource
    in the bundle.
    """

    resource_type = Field("MessageHeader", const=True)

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole` "
            "(represented as `dict` in JSON)"
        ),
        description="The source of the decision",
    )

    definition: fhirtypes.Canonical = Field(
        None,
        alias="definition",
        title="Type `Canonical` referencing `MessageDefinition`",
        description="Link to the definition for this message",
    )
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_definition", title="Extension field for ``definition``."
    )

    destination: ListType[fhirtypes.MessageHeaderDestinationType] = Field(
        None,
        alias="destination",
        title=(
            "List of `MessageHeaderDestination` items (represented as `dict` in "
            "JSON)"
        ),
        description="Message destination application(s)",
    )

    enterer: fhirtypes.ReferenceType = Field(
        None,
        alias="enterer",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole` "
            "(represented as `dict` in JSON)"
        ),
        description="The source of the data entry",
    )

    eventCoding: fhirtypes.CodingType = Field(
        None,
        alias="eventCoding",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Code for the event this message represents or link to event definition",
        one_of_many="event",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    eventUri: fhirtypes.Uri = Field(
        None,
        alias="eventUri",
        title="Type `Uri`",
        description="Code for the event this message represents or link to event definition",
        one_of_many="event",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    eventUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_eventUri", title="Extension field for ``eventUri``."
    )

    focus: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="focus",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="The actual content of the message",
    )

    reason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reason",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Cause of event",
    )

    response: fhirtypes.MessageHeaderResponseType = Field(
        None,
        alias="response",
        title="Type `MessageHeaderResponse` (represented as `dict` in JSON)",
        description="If this is a reply to prior message",
    )

    responsible: fhirtypes.ReferenceType = Field(
        None,
        alias="responsible",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole, "
            "Organization` (represented as `dict` in JSON)"
        ),
        description="Final responsibility for event",
    )

    sender: fhirtypes.ReferenceType = Field(
        None,
        alias="sender",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole, "
            "Organization` (represented as `dict` in JSON)"
        ),
        description="Real world sender of the message",
    )

    source: fhirtypes.MessageHeaderSourceType = Field(
        ...,
        alias="source",
        title="Type `MessageHeaderSource` (represented as `dict` in JSON)",
        description="Message source application",
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
        one_of_many_fields = {"event": ["eventCoding", "eventUri"]}
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


class MessageHeaderDestination(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Message destination application(s).
    The destination application which the message is intended for.
    """

    resource_type = Field("MessageHeaderDestination", const=True)

    endpoint: fhirtypes.Url = Field(
        ...,
        alias="endpoint",
        title="Type `Url`",
        description="Actual destination address or id",
    )
    endpoint__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_endpoint", title="Extension field for ``endpoint``."
    )

    name: fhirtypes.String = Field(
        None, alias="name", title="Type `String`", description="Name of system"
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    receiver: fhirtypes.ReferenceType = Field(
        None,
        alias="receiver",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole, "
            "Organization` (represented as `dict` in JSON)"
        ),
        description='Intended "real-world" recipient for the data',
    )

    target: fhirtypes.ReferenceType = Field(
        None,
        alias="target",
        title="Type `Reference` referencing `Device` (represented as `dict` in JSON)",
        description="Particular delivery destination within the destination",
    )


class MessageHeaderResponse(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    If this is a reply to prior message.
    Information about the message that this message is a response to.  Only
    present if this message is a response.
    """

    resource_type = Field("MessageHeaderResponse", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Type `Code`",
        description="ok | transient-error | fatal-error",
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    details: fhirtypes.ReferenceType = Field(
        None,
        alias="details",
        title=(
            "Type `Reference` referencing `OperationOutcome` (represented as `dict`"
            " in JSON)"
        ),
        description="Specific list of hints/warnings/errors",
    )

    identifier: fhirtypes.Id = Field(
        ..., alias="identifier", title="Type `Id`", description="Id of original message"
    )
    identifier__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_identifier", title="Extension field for ``identifier``."
    )


class MessageHeaderSource(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Message source application.
    The source application from which this message originated.
    """

    resource_type = Field("MessageHeaderSource", const=True)

    contact: fhirtypes.ContactPointType = Field(
        None,
        alias="contact",
        title="Type `ContactPoint` (represented as `dict` in JSON)",
        description="Human contact for problems",
    )

    endpoint: fhirtypes.Url = Field(
        ...,
        alias="endpoint",
        title="Type `Url`",
        description="Actual message source address or id",
    )
    endpoint__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_endpoint", title="Extension field for ``endpoint``."
    )

    name: fhirtypes.String = Field(
        None, alias="name", title="Type `String`", description="Name of system"
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    software: fhirtypes.String = Field(
        None,
        alias="software",
        title="Type `String`",
        description="Name of software running the system",
    )
    software__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_software", title="Extension field for ``software``."
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String`",
        description="Version of software running",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )
