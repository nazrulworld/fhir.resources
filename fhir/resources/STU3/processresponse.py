# -*- coding: utf-8 -*-
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

    resource_type = Field("ProcessResponse", const=True)

    communicationRequest: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="communicationRequest",
        title="Request for additional information",
        description=(
            "Request for additional supporting or authorizing information, such as:"
            " documents, images or resources."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["CommunicationRequest"],
    )

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Creation date",
        description=(
            "The date when the enclosed suite of services were performed or "
            "completed."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
    )

    disposition: fhirtypes.String = Field(
        None,
        alias="disposition",
        title="Disposition Message",
        description="A description of the status of the adjudication or processing.",
        # if property is element of this resource.
        element_property=True,
    )
    disposition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_disposition", title="Extension field for ``disposition``."
    )

    error: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="error",
        title="Error code",
        description="Processing errors.",
        # if property is element of this resource.
        element_property=True,
    )

    form: fhirtypes.CodeableConceptType = Field(
        None,
        alias="form",
        title="Printed Form Identifier",
        description="The form to be used for printing the content.",
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier",
        description="The Response business identifier.",
        # if property is element of this resource.
        element_property=True,
    )

    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title="Authoring Organization",
        description="The organization who produced this adjudicated response.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    outcome: fhirtypes.CodeableConceptType = Field(
        None,
        alias="outcome",
        title="Processing outcome",
        description="Transaction status: error, complete, held.",
        # if property is element of this resource.
        element_property=True,
    )

    processNote: typing.List[fhirtypes.ProcessResponseProcessNoteType] = Field(
        None,
        alias="processNote",
        title="Processing comments or additional requirements",
        description=(
            "Suite of processing notes or additional requirements if the processing"
            " has been held."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title="Request reference",
        description="Original request resource reference.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    requestOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="requestOrganization",
        title="Responsible organization",
        description=(
            "The organization which is responsible for the services rendered to the"
            " patient."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    requestProvider: fhirtypes.ReferenceType = Field(
        None,
        alias="requestProvider",
        title="Responsible Practitioner",
        description=(
            "The practitioner who is responsible for the services rendered to the "
            "patient."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="active | cancelled | draft | entered-in-error",
        description="The status of the resource instance.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "cancelled", "draft", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    resource_type = Field("ProcessResponseProcessNote", const=True)

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Comment on the processing",
        description="The note text.",
        # if property is element of this resource.
        element_property=True,
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="display | print | printoper",
        description="The note purpose: Print/Display.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ProcessResponseProcessNote`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "text"]
