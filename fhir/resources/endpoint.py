# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Endpoint
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType
from typing import Union

from pydantic import Field

from . import domainresource, fhirtypes


class Endpoint(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The technical details of an endpoint that can be used for electronic
    services.
    The technical details of an endpoint that can be used for electronic
    services, such as for web services providing XDS.b or a REST endpoint for
    another FHIR server. This may include any security context information.
    """

    resource_type = Field("Endpoint", const=True)

    address: fhirtypes.Url = Field(
        ...,
        alias="address",
        title="The technical base address for connecting to this endpoint",
        description="The uri that describes the actual end-point to connect to.",
        # if property is element of this resource.
        element_property=True,
    )
    address__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_address", title="Extension field for ``address``."
    )

    connectionType: fhirtypes.CodingType = Field(
        ...,
        alias="connectionType",
        title="Protocol/Profile/Standard to be used with this endpoint connection",
        description=(
            "A coded value that represents the technical details of the usage of "
            "this endpoint, such as what WSDLs should be used in what way. (e.g. "
            "XDS.b/DICOM/cds-hook)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    contact: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="contact",
        title="Contact details for source (e.g. troubleshooting)",
        description=(
            "Contact details for a human to contact about the subscription. The "
            "primary use of this for system administrator troubleshooting."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    header: ListType[fhirtypes.String] = Field(
        None,
        alias="header",
        title="Usage depends on the channel type",
        description="Additional headers / information to send as part of the notification.",
        # if property is element of this resource.
        element_property=True,
    )
    header__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_header", title="Extension field for ``header``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Identifies this endpoint across multiple systems",
        description=(
            "Identifier for the organization that is used to identify the endpoint "
            "across multiple disparate systems."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    managingOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="managingOrganization",
        title=(
            "Organization that manages this endpoint (might not be the organization"
            " that exposes the endpoint)"
        ),
        description=(
            "The organization that manages this endpoint (even if technically "
            "another organization is hosting this in the cloud, it is the "
            "organization associated with the data)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="A name that this endpoint can be identified by",
        description="A friendly name that this endpoint can be referred to with.",
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    payloadMimeType: ListType[fhirtypes.Code] = Field(
        None,
        alias="payloadMimeType",
        title=(
            "Mimetype to send. If not specified, the content could be anything "
            "(including no payload, if the connectionType defined this)"
        ),
        description=(
            "The mime type to send the payload in - e.g. application/fhir+xml, "
            "application/fhir+json. If the mime type is not specified, then the "
            "sender could send any content (including no content depending on the "
            "connectionType)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    payloadMimeType__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_payloadMimeType", title="Extension field for ``payloadMimeType``."
    )

    payloadType: ListType[fhirtypes.CodeableConceptType] = Field(
        ...,
        alias="payloadType",
        title=(
            "The type of content that may be used at this endpoint (e.g. XDS "
            "Discharge summaries)"
        ),
        description=(
            "The payload type describes the acceptable content that can be "
            "communicated on the endpoint."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Interval the endpoint is expected to be operational",
        description="The interval during which the endpoint is expected to be operational.",
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="active | suspended | error | off | entered-in-error | test",
        description="active | suspended | error | off | test.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "suspended", "error", "off", "entered-in-error", "test"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )
