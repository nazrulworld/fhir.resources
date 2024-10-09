from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ProcessResponse
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ProcessResponse(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    ProcessResponse resource.
    This resource provides processing status, errors and notes from the
    processing of a resource.
    """

    __resource_type__ = "ProcessResponse"

    communicationRequest: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="communicationRequest",
        title="Request for additional information",
        description=(
            "Request for additional supporting or authorizing information, such as:"
            " documents, images or resources."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["CommunicationRequest"],
        },
    )

    created: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="created",
        title="Creation date",
        description=(
            "The date when the enclosed suite of services were performed or "
            "completed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_created", title="Extension field for ``created``."
    )

    disposition: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="disposition",
        title="Disposition Message",
        description="A description of the status of the adjudication or processing.",
        json_schema_extra={
            "element_property": True,
        },
    )
    disposition__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_disposition", title="Extension field for ``disposition``."
    )

    error: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="error",
        title="Error code",
        description="Processing errors.",
        json_schema_extra={
            "element_property": True,
        },
    )

    form: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="form",
        title="Printed Form Identifier",
        description="The form to be used for printing the content.",
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business Identifier",
        description="The Response business identifier.",
        json_schema_extra={
            "element_property": True,
        },
    )

    organization: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="organization",
        title="Authoring Organization",
        description="The organization who produced this adjudicated response.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    outcome: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="outcome",
        title="Processing outcome",
        description="Transaction status: error, complete, held.",
        json_schema_extra={
            "element_property": True,
        },
    )

    processNote: typing.List[fhirtypes.ProcessResponseProcessNoteType] | None = Field(  # type: ignore
        None,
        alias="processNote",
        title="Processing comments or additional requirements",
        description=(
            "Suite of processing notes or additional requirements if the processing"
            " has been held."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    request: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="request",
        title="Request reference",
        description="Original request resource reference.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    requestOrganization: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="requestOrganization",
        title="Responsible organization",
        description=(
            "The organization which is responsible for the services rendered to the"
            " patient."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    requestProvider: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="requestProvider",
        title="Responsible Practitioner",
        description=(
            "The practitioner who is responsible for the services rendered to the "
            "patient."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner"],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="active | cancelled | draft | entered-in-error",
        description="The status of the resource instance.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["active", "cancelled", "draft", "entered-in-error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ProcessResponse`` according specification,
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
            "status",
            "created",
            "organization",
            "request",
            "outcome",
            "disposition",
            "requestProvider",
            "requestOrganization",
            "form",
            "processNote",
            "error",
            "communicationRequest",
        ]


class ProcessResponseProcessNote(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Processing comments or additional requirements.
    Suite of processing notes or additional requirements if the processing has
    been held.
    """

    __resource_type__ = "ProcessResponseProcessNote"

    text: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="text",
        title="Comment on the processing",
        description="The note text.",
        json_schema_extra={
            "element_property": True,
        },
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_text", title="Extension field for ``text``."
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="display | print | printoper",
        description="The note purpose: Print/Display.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ProcessResponseProcessNote`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "text"]
