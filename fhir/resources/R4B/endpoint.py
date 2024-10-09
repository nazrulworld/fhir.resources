from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Endpoint
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import domainresource, fhirtypes


class Endpoint(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The technical details of an endpoint that can be used for electronic
    services.
    The technical details of an endpoint that can be used for electronic
    services, such as for web services providing XDS.b or a REST endpoint for
    another FHIR server. This may include any security context information.
    """

    __resource_type__ = "Endpoint"

    address: fhirtypes.UrlType | None = Field(  # type: ignore
        None,
        alias="address",
        title="The technical base address for connecting to this endpoint",
        description="The uri that describes the actual end-point to connect to.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    address__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_address", title="Extension field for ``address``."
    )

    connectionType: fhirtypes.CodingType = Field(  # type: ignore
        ...,
        alias="connectionType",
        title="Protocol/Profile/Standard to be used with this endpoint connection",
        description=(
            "A coded value that represents the technical details of the usage of "
            "this endpoint, such as what WSDLs should be used in what way. (e.g. "
            "XDS.b/DICOM/cds-hook)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    contact: typing.List[fhirtypes.ContactPointType] | None = Field(  # type: ignore
        None,
        alias="contact",
        title="Contact details for source (e.g. troubleshooting)",
        description=(
            "Contact details for a human to contact about the subscription. The "
            "primary use of this for system administrator troubleshooting."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    header: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="header",
        title="Usage depends on the channel type",
        description="Additional headers / information to send as part of the notification.",
        json_schema_extra={
            "element_property": True,
        },
    )
    header__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_header", title="Extension field for ``header``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Identifies this endpoint across multiple systems",
        description=(
            "Identifier for the organization that is used to identify the endpoint "
            "across multiple disparate systems."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    managingOrganization: fhirtypes.ReferenceType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="A name that this endpoint can be identified by",
        description="A friendly name that this endpoint can be referred to with.",
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    payloadMimeType: typing.List[fhirtypes.CodeType | None] | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )
    payloadMimeType__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_payloadMimeType", title="Extension field for ``payloadMimeType``."
    )

    payloadType: typing.List[fhirtypes.CodeableConceptType] = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="period",
        title="Interval the endpoint is expected to be operational",
        description="The interval during which the endpoint is expected to be operational.",
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="active | suspended | error | off | entered-in-error | test",
        description="active | suspended | error | off | test.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "active",
                "suspended",
                "error",
                "off",
                "entered-in-error",
                "test",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Endpoint`` according specification,
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
            "connectionType",
            "name",
            "managingOrganization",
            "contact",
            "period",
            "payloadType",
            "payloadMimeType",
            "address",
            "header",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("address", "address__ext"), ("status", "status__ext")]
        return required_fields
