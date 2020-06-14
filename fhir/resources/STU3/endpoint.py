# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Endpoint
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import domainresource, fhirtypes


class Endpoint(domainresource.DomainResource):
    """ The technical details of an endpoint that can be used for electronic
    services.
    The technical details of an endpoint that can be used for electronic
    services, such as for web services providing XDS.b or a REST endpoint for
    another FHIR server. This may include any security context information.
    """

    resource_type = Field("Endpoint", const=True)

    address: fhirtypes.Uri = Field(
        ...,
        alias="address",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="The technical base address for connecting to this endpoint",
    )

    connectionType: fhirtypes.CodingType = Field(
        ...,
        alias="connectionType",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Protocol/Profile/Standard to be used with this endpoint connection",
    )

    contact: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="contact",
        title="List of `ContactPoint` items (represented as `dict` in JSON)",
        description="Contact details for source (e.g. troubleshooting)",
    )

    header: ListType[fhirtypes.String] = Field(
        None,
        alias="header",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Usage depends on the channel type",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Identifies this endpoint across multiple systems",
    )

    managingOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="managingOrganization",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Organization that manages this endpoint (may not be the organization that exposes the endpoint)",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="A name that this endpoint can be identified by",
    )

    payloadMimeType: ListType[fhirtypes.Code] = Field(
        None,
        alias="payloadMimeType",
        title="List of `Code` items (represented as `dict` in JSON)",
        description="Mimetype to send. If not specified, the content could be anything (including no payload, if the connectionType defined this)",
    )

    payloadType: ListType[fhirtypes.CodeableConceptType] = Field(
        ...,
        alias="payloadType",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="The type of content that may be used at this endpoint (e.g. XDS Discharge summaries)",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Interval the endpoint is expected to be operational",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="active | suspended | error | off | entered-in-error | test",
    )
