# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ProcessResponse
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ProcessResponse(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    ProcessResponse resource.
    This resource provides processing status, errors and notes from the
    processing of a resource.
    """

    resource_type = Field("ProcessResponse", const=True)

    communicationRequest: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="communicationRequest",
        title=(
            "List of `Reference` items referencing `CommunicationRequest` "
            "(represented as `dict` in JSON)"
        ),
        description="Request for additional information",
    )

    created: fhirtypes.DateTime = Field(
        None, alias="created", title="Type `DateTime`", description="Creation date"
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
    )

    disposition: fhirtypes.String = Field(
        None,
        alias="disposition",
        title="Type `String`",
        description="Disposition Message",
    )
    disposition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_disposition", title="Extension field for ``disposition``."
    )

    error: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="error",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Error code",
    )

    form: fhirtypes.CodeableConceptType = Field(
        None,
        alias="form",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Printed Form Identifier",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business Identifier",
    )

    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Authoring Organization",
    )

    outcome: fhirtypes.CodeableConceptType = Field(
        None,
        alias="outcome",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Processing outcome",
    )

    processNote: ListType[fhirtypes.ProcessResponseProcessNoteType] = Field(
        None,
        alias="processNote",
        title=(
            "List of `ProcessResponseProcessNote` items (represented as `dict` in "
            "JSON)"
        ),
        description="Processing comments or additional requirements",
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Request reference",
    )

    requestOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="requestOrganization",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Responsible organization",
    )

    requestProvider: fhirtypes.ReferenceType = Field(
        None,
        alias="requestProvider",
        title=(
            "Type `Reference` referencing `Practitioner` (represented as `dict` in "
            "JSON)"
        ),
        description="Responsible Practitioner",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code`",
        description="active | cancelled | draft | entered-in-error",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )


class ProcessResponseProcessNote(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
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
        title="Type `String`",
        description="Comment on the processing",
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="display | print | printoper",
    )
