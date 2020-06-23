# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Bundle
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, fhirtypes, resource


class Bundle(resource.Resource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Contains a collection of resources.
    A container for a collection of resources.
    """

    resource_type = Field("Bundle", const=True)

    entry: ListType[fhirtypes.BundleEntryType] = Field(
        None,
        alias="entry",
        title="List of `BundleEntry` items (represented as `dict` in JSON)",
        description="Entry in the bundle - will have a resource or information",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Persistent identifier for the bundle",
    )

    link: ListType[fhirtypes.BundleLinkType] = Field(
        None,
        alias="link",
        title="List of `BundleLink` items (represented as `dict` in JSON)",
        description="Links related to this Bundle",
    )

    signature: fhirtypes.SignatureType = Field(
        None,
        alias="signature",
        title="Type `Signature` (represented as `dict` in JSON)",
        description="Digital Signature",
    )

    timestamp: fhirtypes.Instant = Field(
        None,
        alias="timestamp",
        title="Type `Instant`",
        description="When the bundle was assembled",
    )
    timestamp__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_timestamp", title="Extension field for ``timestamp``."
    )

    total: fhirtypes.UnsignedInt = Field(
        None,
        alias="total",
        title="Type `UnsignedInt`",
        description="If search, the total number of matches",
    )
    total__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_total", title="Extension field for ``total``."
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code`",
        description=(
            "document | message | transaction | transaction-response | batch | "
            "batch-response | history | searchset | collection"
        ),
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )


class BundleEntry(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Entry in the bundle - will have a resource or information.
    An entry in a bundle resource - will either contain a resource or
    information about a resource (transactions and history only).
    """

    resource_type = Field("BundleEntry", const=True)

    fullUrl: fhirtypes.Uri = Field(
        None,
        alias="fullUrl",
        title="Type `Uri`",
        description="URI for resource (Absolute URL server address or URI for UUID/OID)",
    )
    fullUrl__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fullUrl", title="Extension field for ``fullUrl``."
    )

    link: ListType[fhirtypes.BundleLinkType] = Field(
        None,
        alias="link",
        title="List of `BundleLink` items (represented as `dict` in JSON)",
        description="Links related to this entry",
    )

    request: fhirtypes.BundleEntryRequestType = Field(
        None,
        alias="request",
        title="Type `BundleEntryRequest` (represented as `dict` in JSON)",
        description="Additional execution information (transaction/batch/history)",
    )

    resource: fhirtypes.ResourceType = Field(
        None,
        alias="resource",
        title="Type `Resource` (represented as `dict` in JSON)",
        description="A resource in the bundle",
    )

    response: fhirtypes.BundleEntryResponseType = Field(
        None,
        alias="response",
        title="Type `BundleEntryResponse` (represented as `dict` in JSON)",
        description="Results of execution (transaction/batch/history)",
    )

    search: fhirtypes.BundleEntrySearchType = Field(
        None,
        alias="search",
        title="Type `BundleEntrySearch` (represented as `dict` in JSON)",
        description="Search related information",
    )


class BundleEntryRequest(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional execution information (transaction/batch/history).
    Additional information about how this entry should be processed as part of
    a transaction or batch.  For history, it shows how the entry was processed
    to create the version contained in the entry.
    """

    resource_type = Field("BundleEntryRequest", const=True)

    ifMatch: fhirtypes.String = Field(
        None,
        alias="ifMatch",
        title="Type `String`",
        description="For managing update contention",
    )
    ifMatch__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_ifMatch", title="Extension field for ``ifMatch``."
    )

    ifModifiedSince: fhirtypes.Instant = Field(
        None,
        alias="ifModifiedSince",
        title="Type `Instant`",
        description="For managing cache currency",
    )
    ifModifiedSince__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_ifModifiedSince", title="Extension field for ``ifModifiedSince``."
    )

    ifNoneExist: fhirtypes.String = Field(
        None,
        alias="ifNoneExist",
        title="Type `String`",
        description="For conditional creates",
    )
    ifNoneExist__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_ifNoneExist", title="Extension field for ``ifNoneExist``."
    )

    ifNoneMatch: fhirtypes.String = Field(
        None,
        alias="ifNoneMatch",
        title="Type `String`",
        description="For managing cache currency",
    )
    ifNoneMatch__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_ifNoneMatch", title="Extension field for ``ifNoneMatch``."
    )

    method: fhirtypes.Code = Field(
        ...,
        alias="method",
        title="Type `Code`",
        description="GET | HEAD | POST | PUT | DELETE | PATCH",
    )
    method__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_method", title="Extension field for ``method``."
    )

    url: fhirtypes.Uri = Field(
        ...,
        alias="url",
        title="Type `Uri`",
        description="URL for HTTP equivalent of this entry",
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )


class BundleEntryResponse(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Results of execution (transaction/batch/history).
    Indicates the results of processing the corresponding 'request' entry in
    the batch or transaction being responded to or what the results of an
    operation where when returning history.
    """

    resource_type = Field("BundleEntryResponse", const=True)

    etag: fhirtypes.String = Field(
        None,
        alias="etag",
        title="Type `String`",
        description="The Etag for the resource (if relevant)",
    )
    etag__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_etag", title="Extension field for ``etag``."
    )

    lastModified: fhirtypes.Instant = Field(
        None,
        alias="lastModified",
        title="Type `Instant`",
        description="Server\u0027s date time modified",
    )
    lastModified__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastModified", title="Extension field for ``lastModified``."
    )

    location: fhirtypes.Uri = Field(
        None,
        alias="location",
        title="Type `Uri`",
        description="The location (if the operation returns a location)",
    )
    location__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_location", title="Extension field for ``location``."
    )

    outcome: fhirtypes.ResourceType = Field(
        None,
        alias="outcome",
        title="Type `Resource` (represented as `dict` in JSON)",
        description="OperationOutcome with hints and warnings (for batch/transaction)",
    )

    status: fhirtypes.String = Field(
        ...,
        alias="status",
        title="Type `String`",
        description="Status response code (text optional)",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )


class BundleEntrySearch(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Search related information.
    Information about the search process that lead to the creation of this
    entry.
    """

    resource_type = Field("BundleEntrySearch", const=True)

    mode: fhirtypes.Code = Field(
        None,
        alias="mode",
        title="Type `Code`",
        description="match | include | outcome - why this is in the result set",
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_mode", title="Extension field for ``mode``."
    )

    score: fhirtypes.Decimal = Field(
        None,
        alias="score",
        title="Type `Decimal`",
        description="Search ranking (between 0 and 1)",
    )
    score__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_score", title="Extension field for ``score``."
    )


class BundleLink(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Links related to this Bundle.
    A series of links that provide context to this bundle.
    """

    resource_type = Field("BundleLink", const=True)

    relation: fhirtypes.String = Field(
        ...,
        alias="relation",
        title="Type `String`",
        description=(
            "See http://www.iana.org/assignments/link-relations/link-"
            "relations.xhtml#link-relations-1"
        ),
    )
    relation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_relation", title="Extension field for ``relation``."
    )

    url: fhirtypes.Uri = Field(
        ...,
        alias="url",
        title="Type `Uri`",
        description="Reference details for the link",
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )
