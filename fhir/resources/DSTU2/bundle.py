# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Bundle
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic.v1 import Field

from . import fhirtypes
from .backboneelement import BackboneElement
from .resource import Resource


class Bundle(Resource):
    """Contains a collection of resources.

    A container for a collection of resources.
    """

    resource_type = Field("Bundle", const=True)

    entry: ListType[fhirtypes.BundleEntryType] = Field(
        None,
        alias="entry",
        title="List of `BundleEntry` items (represented as `dict` in JSON)",
        description="Entry in the bundle - will have a resource, or information",
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
        description=(
            "document | message | transaction | transaction-response | batch | "
            "batch-response | history | searchset | collection"
        ),
    )


class BundleEntry(BackboneElement):
    """Entry in the bundle - will have a resource, or information.

    An entry in a bundle resource - will either contain a resource, or
    information about a resource (transactions and history only).
    """

    resource_type = Field("BundleEntry", const=True)

    fullUrl: fhirtypes.Uri = Field(
        None,
        alias="fullUrl",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Absolute URL for resource (server address, or UUID/OID)",
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
        description="Transaction Related Information",
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
        description="Transaction Related Information",
    )

    search: fhirtypes.BundleEntrySearchType = Field(
        None,
        alias="search",
        title="Type `BundleEntrySearch` (represented as `dict` in JSON)",
        description="Search related information",
    )


class BundleEntryRequest(BackboneElement):
    """Transaction Related Information.

    Additional information about how this entry should be processed as part of
    a transaction.
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
        description="For managing update contention",
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
        description="GET | POST | PUT | DELETE",
    )

    url: fhirtypes.Uri = Field(
        ...,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="URL for HTTP equivalent of this entry",
    )


class BundleEntryResponse(BackboneElement):
    """Transaction Related Information.

    Additional information about how this entry should be processed as part of
    a transaction.
    """

    resource_type = Field("BundleEntryResponse", const=True)

    etag: fhirtypes.String = Field(
        None,
        alias="etag",
        title="Type `String` (represented as `dict` in JSON)",
        description="The etag for the resource (if relevant)",
    )

    lastModified: fhirtypes.Instant = Field(
        None,
        alias="lastModified",
        title="Type `Instant` (represented as `dict` in JSON)",
        description="Server's date time modified",
    )

    location: fhirtypes.Uri = Field(
        None,
        alias="location",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="The location, if the operation returns a location",
    )

    status: fhirtypes.String = Field(
        ...,
        alias="status",
        title="Type `String` (represented as `dict` in JSON)",
        description="Status response code (text optional)",
    )


class BundleEntrySearch(BackboneElement):
    """Search related information.

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


class BundleLink(BackboneElement):
    """Links related to this Bundle.

    A series of links that provide context to this bundle.
    """

    resource_type = Field("BundleLink", const=True)

    relation: fhirtypes.String = Field(
        ...,
        alias="relation",
        title="Type `String` (represented as `dict` in JSON)",
        description=(
            "See http://www.iana.org/assignments/link-relations/link-"
            "relations.xhtml#link-relations-1"
        ),
    )

    url: fhirtypes.Uri = Field(
        ...,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Reference details for the link",
    )
