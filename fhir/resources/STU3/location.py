# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Location
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Location(domainresource.DomainResource):
    """ Details and position information for a physical place.
    Details and position information for a physical place where services are
    provided  and resources and participants may be stored, found, contained or
    accommodated.
    """

    resource_type = Field("Location", const=True)

    address: fhirtypes.AddressType = Field(
        None,
        alias="address",
        title="Type `Address` (represented as `dict` in JSON)",
        description="Physical location",
    )

    alias: ListType[fhirtypes.String] = Field(
        None,
        alias="alias",
        title="List of `String` items (represented as `dict` in JSON)",
        description="A list of\u00a0alternate names that the location is known as, or was known as in the past",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Additional details about the location that could be displayed as further information to identify the location beyond its name",
    )

    endpoint: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="endpoint",
        title="List of `Reference` items referencing `Endpoint` (represented as `dict` in JSON)",
        description="Technical endpoints providing access to services operated for the location",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Unique code or number identifying the location to its users",
    )

    managingOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="managingOrganization",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Organization responsible for provisioning and upkeep",
    )

    mode: fhirtypes.Code = Field(
        None,
        alias="mode",
        title="Type `Code` (represented as `dict` in JSON)",
        description="instance | kind",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of the location as used by humans",
    )

    operationalStatus: fhirtypes.CodingType = Field(
        None,
        alias="operationalStatus",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="The Operational status of the location (typically only for a bed/room)",
    )

    partOf: fhirtypes.ReferenceType = Field(
        None,
        alias="partOf",
        title="Type `Reference` referencing `Location` (represented as `dict` in JSON)",
        description="Another Location this one is physically part of",
    )

    physicalType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="physicalType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Physical form of the location",
    )

    position: fhirtypes.LocationPositionType = Field(
        None,
        alias="position",
        title="Type `LocationPosition` (represented as `dict` in JSON)",
        description="The absolute geographic location",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="active | suspended | inactive",
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="List of `ContactPoint` items (represented as `dict` in JSON)",
        description="Contact details of the location",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of function performed",
    )


class LocationPosition(backboneelement.BackboneElement):
    """ The absolute geographic location.
    The absolute geographic location of the Location, expressed using the WGS84
    datum (This is the same co-ordinate system used in KML).
    """

    resource_type = Field("LocationPosition", const=True)

    altitude: fhirtypes.Decimal = Field(
        None,
        alias="altitude",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Altitude with WGS84 datum",
    )

    latitude: fhirtypes.Decimal = Field(
        ...,
        alias="latitude",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Latitude with WGS84 datum",
    )

    longitude: fhirtypes.Decimal = Field(
        ...,
        alias="longitude",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Longitude with WGS84 datum",
    )
