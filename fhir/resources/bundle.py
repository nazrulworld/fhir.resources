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
    """ Contains a collection of resources.
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
        title="Type `Instant` (represented as `dict` in JSON)",
        description="When the bundle was assembled",
    )

    total: fhirtypes.UnsignedInt = Field(
        None,
        alias="total",
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="If search, the total number of matches",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="document | message | transaction | transaction-response | batch | batch-response | history | searchset | collection",
    )


class BundleEntry(backboneelement.BackboneElement):
    """ Entry in the bundle - will have a resource or information.
    An entry in a bundle resource - will either contain a resource or
    information about a resource (transactions and history only).
    """

    resource_type = Field("BundleEntry", const=True)

    fullUrl: fhirtypes.Uri = Field(
        None,
        alias="fullUrl",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="URI for resource (Absolute URL server address or URI for UUID/OID)",
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
    """ Additional execution information (transaction/batch/history).
    Additional information about how this entry should be processed as part of
    a transaction or batch.  For history, it shows how the entry was processed
    to create the version contained in the entry.
    """

    resource_type = Field("BundleEntryRequest", const=True)

    ifMatch: fhirtypes.String = Field(
        None,
        alias="ifMatch",
        title="Type `String` (represented as `dict` in JSON)",
        description="For managing update contention",
    )

    ifModifiedSince: fhirtypes.Instant = Field(
        None,
        alias="ifModifiedSince",
        title="Type `Instant` (represented as `dict` in JSON)",
        description="For managing cache currency",
    )

    ifNoneExist: fhirtypes.String = Field(
        None,
        alias="ifNoneExist",
        title="Type `String` (represented as `dict` in JSON)",
        description="For conditional creates",
    )

    ifNoneMatch: fhirtypes.String = Field(
        None,
        alias="ifNoneMatch",
        title="Type `String` (represented as `dict` in JSON)",
        description="For managing cache currency",
    )

    method: fhirtypes.Code = Field(
        ...,
        alias="method",
        title="Type `Code` (represented as `dict` in JSON)",
        description="GET | HEAD | POST | PUT | DELETE | PATCH",
    )

    url: fhirtypes.Uri = Field(
        ...,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="URL for HTTP equivalent of this entry",
    )


class BundleEntryResponse(backboneelement.BackboneElement):
    """ Results of execution (transaction/batch/history).
    Indicates the results of processing the corresponding 'request' entry in
    the batch or transaction being responded to or what the results of an
    operation where when returning history.
    """

    resource_type = Field("BundleEntryResponse", const=True)

    etag: fhirtypes.String = Field(
        None,
        alias="etag",
        title="Type `String` (represented as `dict` in JSON)",
        description="The Etag for the resource (if relevant)",
    )

    lastModified: fhirtypes.Instant = Field(
        None,
        alias="lastModified",
        title="Type `Instant` (represented as `dict` in JSON)",
        description="Server\u0027s date time modified",
    )

    location: fhirtypes.Uri = Field(
        None,
        alias="location",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="The location (if the operation returns a location)",
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
        title="Type `String` (represented as `dict` in JSON)",
        description="Status response code (text optional)",
    )


class BundleEntrySearch(backboneelement.BackboneElement):
    """ Search related information.
    Information about the search process that lead to the creation of this
    entry.
    """

    resource_type = Field("BundleEntrySearch", const=True)

    mode: fhirtypes.Code = Field(
        None,
        alias="mode",
        title="Type `Code` (represented as `dict` in JSON)",
        description="match | include | outcome - why this is in the result set",
    )

    score: fhirtypes.Decimal = Field(
        None,
        alias="score",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Search ranking (between 0 and 1)",
    )


class BundleLink(backboneelement.BackboneElement):
    """ Links related to this Bundle.
    A series of links that provide context to this bundle.
    """

    resource_type = Field("BundleLink", const=True)

    relation: fhirtypes.String = Field(
        ...,
        alias="relation",
        title="Type `String` (represented as `dict` in JSON)",
        description="See http://www.iana.org/assignments/link-relations/link-relations.xhtml#link-relations-1",
    )

    url: fhirtypes.Uri = Field(
        ...,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Reference details for the link",
    )
