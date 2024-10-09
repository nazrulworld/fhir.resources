from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Bundle
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, fhirtypes, resource


class Bundle(resource.Resource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Contains a collection of resources.
    A container for a collection of resources.
    """

    __resource_type__ = "Bundle"

    entry: typing.List[fhirtypes.BundleEntryType] | None = Field(  # type: ignore
        None,
        alias="entry",
        title="Entry in the bundle - will have a resource, or information",
        description=(
            "An entry in a bundle resource - will either contain a resource, or "
            "information about a resource (transactions and history only)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Persistent identifier for the bundle",
        description=(
            "A persistent identifier for the batch that won't change as a batch is "
            "copied from server to server."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    link: typing.List[fhirtypes.BundleLinkType] | None = Field(  # type: ignore
        None,
        alias="link",
        title="Links related to this Bundle",
        description="A series of links that provide context to this bundle.",
        json_schema_extra={
            "element_property": True,
        },
    )

    signature: fhirtypes.SignatureType | None = Field(  # type: ignore
        None,
        alias="signature",
        title="Digital Signature",
        description="Digital Signature - base64 encoded. XML-DSIg or a JWT.",
        json_schema_extra={
            "element_property": True,
        },
    )

    total: fhirtypes.UnsignedIntType | None = Field(  # type: ignore
        None,
        alias="total",
        title="If search, the total number of matches",
        description=(
            "If a set of search matches, this is the total number of matches for "
            "the search (as opposed to the number of results in this bundle)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    total__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_total", title="Extension field for ``total``."
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title=(
            "document | message | transaction | transaction-response | batch | "
            "batch-response | history | searchset | collection"
        ),
        description="Indicates the purpose of this bundle - how it was intended to be used.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "document",
                "message",
                "transaction",
                "transaction-response",
                "batch",
                "batch-response",
                "history",
                "searchset",
                "collection",
            ],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Bundle`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "identifier",
            "type",
            "total",
            "link",
            "entry",
            "signature",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("type", "type__ext")]
        return required_fields


class BundleEntry(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Entry in the bundle - will have a resource, or information.
    An entry in a bundle resource - will either contain a resource, or
    information about a resource (transactions and history only).
    """

    __resource_type__ = "BundleEntry"

    fullUrl: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="fullUrl",
        title="Absolute URL for resource (server address, or UUID/OID)",
        description=(
            "The Absolute URL for the resource.  The fullUrl SHALL not disagree "
            "with the id in the resource. The fullUrl is a version independent "
            "reference to the resource. The fullUrl element SHALL have a value "
            "except that:  * fullUrl can be empty on a POST (although it does not "
            "need to when specifying a temporary id for reference in the bundle) * "
            "Results from operations might involve resources that are not "
            "identified."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    fullUrl__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_fullUrl", title="Extension field for ``fullUrl``."
    )

    link: typing.List[fhirtypes.BundleLinkType] | None = Field(  # type: ignore
        None,
        alias="link",
        title="Links related to this entry",
        description="A series of links that provide context to this entry.",
        json_schema_extra={
            "element_property": True,
        },
    )

    request: fhirtypes.BundleEntryRequestType | None = Field(  # type: ignore
        None,
        alias="request",
        title="Transaction Related Information",
        description=(
            "Additional information about how this entry should be processed as "
            "part of a transaction."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    resource: fhirtypes.ResourceType | None = Field(  # type: ignore
        None,
        alias="resource",
        title="A resource in the bundle",
        description="The Resources for the entry.",
        json_schema_extra={
            "element_property": True,
        },
    )

    response: fhirtypes.BundleEntryResponseType | None = Field(  # type: ignore
        None,
        alias="response",
        title="Transaction Related Information",
        description=(
            "Additional information about how this entry should be processed as "
            "part of a transaction."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    search: fhirtypes.BundleEntrySearchType | None = Field(  # type: ignore
        None,
        alias="search",
        title="Search related information",
        description=(
            "Information about the search process that lead to the creation of this"
            " entry."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BundleEntry`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "link",
            "fullUrl",
            "resource",
            "search",
            "request",
            "response",
        ]


class BundleEntryRequest(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Transaction Related Information.
    Additional information about how this entry should be processed as part of
    a transaction.
    """

    __resource_type__ = "BundleEntryRequest"

    ifMatch: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="ifMatch",
        title="For managing update contention",
        description=(
            "Only perform the operation if the Etag value matches. For more "
            'information, see the API section ["Managing Resource '
            'Contention"](http.html#concurrency).'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    ifMatch__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_ifMatch", title="Extension field for ``ifMatch``."
    )

    ifModifiedSince: fhirtypes.InstantType | None = Field(  # type: ignore
        None,
        alias="ifModifiedSince",
        title="For managing update contention",
        description=(
            "Only perform the operation if the last updated date matches. See the "
            'API documentation for ["Conditional Read"](http.html#cread).'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    ifModifiedSince__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_ifModifiedSince", title="Extension field for ``ifModifiedSince``."
    )

    ifNoneExist: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="ifNoneExist",
        title="For conditional creates",
        description=(
            "Instruct the server not to perform the create if a specified resource "
            "already exists. For further information, see the API documentation for"
            ' ["Conditional Create"](http.html#ccreate). This is just the query '
            'portion of the URL - what follows the "?" (not including the "?").'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    ifNoneExist__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_ifNoneExist", title="Extension field for ``ifNoneExist``."
    )

    ifNoneMatch: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="ifNoneMatch",
        title="For managing cache currency",
        description=(
            "If the ETag values match, return a 304 Not Modified status. See the "
            'API documentation for ["Conditional Read"](http.html#cread).'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    ifNoneMatch__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_ifNoneMatch", title="Extension field for ``ifNoneMatch``."
    )

    method: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="method",
        title="GET | POST | PUT | DELETE",
        description=(
            "The HTTP verb for this entry in either a change history, or a "
            "transaction/ transaction response."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["GET", "POST", "PUT", "DELETE"],
        },
    )
    method__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_method", title="Extension field for ``method``."
    )

    url: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="url",
        title="URL for HTTP equivalent of this entry",
        description=(
            "The URL for this entry, relative to the root (the address to which the"
            " request is posted)."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_url", title="Extension field for ``url``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BundleEntryRequest`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "method",
            "url",
            "ifNoneMatch",
            "ifModifiedSince",
            "ifMatch",
            "ifNoneExist",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("method", "method__ext"), ("url", "url__ext")]
        return required_fields


class BundleEntryResponse(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Transaction Related Information.
    Additional information about how this entry should be processed as part of
    a transaction.
    """

    __resource_type__ = "BundleEntryResponse"

    etag: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="etag",
        title="The etag for the resource (if relevant)",
        description=(
            "The etag for the resource, it the operation for the entry produced a "
            "versioned resource (see [Resource Metadata and "
            "Versioning](http.html#versioning) and [Managing Resource "
            "Contention](http.html#concurrency))."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    etag__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_etag", title="Extension field for ``etag``."
    )

    lastModified: fhirtypes.InstantType | None = Field(  # type: ignore
        None,
        alias="lastModified",
        title="Server's date time modified",
        description="The date/time that the resource was modified on the server.",
        json_schema_extra={
            "element_property": True,
        },
    )
    lastModified__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_lastModified", title="Extension field for ``lastModified``."
    )

    location: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="location",
        title="The location, if the operation returns a location",
        description="The location header created by processing this operation.",
        json_schema_extra={
            "element_property": True,
        },
    )
    location__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_location", title="Extension field for ``location``."
    )

    outcome: fhirtypes.ResourceType | None = Field(  # type: ignore
        None,
        alias="outcome",
        title="OperationOutcome with hints and warnings (for batch/transaction)",
        description=(
            "An OperationOutcome containing hints and warnings produced as part of "
            "processing this entry in a batch or transaction."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="status",
        title="Status response code (text optional)",
        description=(
            "The status code returned by processing this entry. The status SHALL "
            "start with a 3 digit HTTP code (e.g. 404) and may contain the standard"
            " HTTP description associated with the status code."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BundleEntryResponse`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "status",
            "location",
            "etag",
            "lastModified",
            "outcome",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        return required_fields


class BundleEntrySearch(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Search related information.
    Information about the search process that lead to the creation of this
    entry.
    """

    __resource_type__ = "BundleEntrySearch"

    mode: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="mode",
        title="match | include | outcome - why this is in the result set",
        description=(
            "Why this entry is in the result set - whether it's included as a match"
            " or because of an _include requirement."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["match", "include", "outcome"],
        },
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_mode", title="Extension field for ``mode``."
    )

    score: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="score",
        title="Search ranking (between 0 and 1)",
        description="When searching, the server's search ranking score for the entry.",
        json_schema_extra={
            "element_property": True,
        },
    )
    score__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_score", title="Extension field for ``score``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BundleEntrySearch`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "mode", "score"]


class BundleLink(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Links related to this Bundle.
    A series of links that provide context to this bundle.
    """

    __resource_type__ = "BundleLink"

    relation: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="relation",
        title=(
            "See http://www.iana.org/assignments/link-relations/link-"
            "relations.xhtml#link-relations-1"
        ),
        description=(
            "A name which details the functional use for this link - see "
            "[http://www.iana.org/assignments/link-relations/link-"
            "relations.xhtml#link-"
            "relations-1](http://www.iana.org/assignments/link-relations/link-"
            "relations.xhtml#link-relations-1)."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    relation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_relation", title="Extension field for ``relation``."
    )

    url: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="url",
        title="Reference details for the link",
        description="The reference details for the link.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_url", title="Extension field for ``url``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BundleLink`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "relation", "url"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("relation", "relation__ext"), ("url", "url__ext")]
        return required_fields
