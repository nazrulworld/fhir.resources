# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Location
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType
from typing import Union

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Location(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details and position information for a physical place.
    Details and position information for a physical place where services are
    provided and resources and participants may be stored, found, contained, or
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
        title="List of `String` items",
        description=(
            "A list of alternate names that the location is known as, or was known "
            "as, in the past"
        ),
    )
    alias__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_alias", title="Extension field for ``alias``."
    )

    availabilityExceptions: fhirtypes.String = Field(
        None,
        alias="availabilityExceptions",
        title="Type `String`",
        description="Description of availability exceptions",
    )
    availabilityExceptions__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_availabilityExceptions",
        title="Extension field for ``availabilityExceptions``.",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description=(
            "Additional details about the location that could be displayed as "
            "further information to identify the location beyond its name"
        ),
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    endpoint: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="endpoint",
        title=(
            "List of `Reference` items referencing `Endpoint` (represented as "
            "`dict` in JSON)"
        ),
        description=(
            "Technical endpoints providing access to services operated for the "
            "location"
        ),
    )

    hoursOfOperation: ListType[fhirtypes.LocationHoursOfOperationType] = Field(
        None,
        alias="hoursOfOperation",
        title=(
            "List of `LocationHoursOfOperation` items (represented as `dict` in "
            "JSON)"
        ),
        description="What days/times during a week is this location usually open",
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
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Organization responsible for provisioning and upkeep",
    )

    mode: fhirtypes.Code = Field(
        None, alias="mode", title="Type `Code`", description="instance | kind"
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_mode", title="Extension field for ``mode``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`",
        description="Name of the location as used by humans",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    operationalStatus: fhirtypes.CodingType = Field(
        None,
        alias="operationalStatus",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="The operational status of the location (typically only for a bed/room)",
    )

    partOf: fhirtypes.ReferenceType = Field(
        None,
        alias="partOf",
        title=(
            "Type `Reference` referencing `Location` (represented as `dict` in " "JSON)"
        ),
        description="Another Location this one is physically a part of",
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
        title="Type `Code`",
        description="active | suspended | inactive",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="List of `ContactPoint` items (represented as `dict` in JSON)",
        description="Contact details of the location",
    )

    type: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Type of function performed",
    )


class LocationHoursOfOperation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What days/times during a week is this location usually open.
    """

    resource_type = Field("LocationHoursOfOperation", const=True)

    allDay: bool = Field(
        None,
        alias="allDay",
        title="Type `bool`",
        description="The Location is open all day",
    )
    allDay__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_allDay", title="Extension field for ``allDay``."
    )

    closingTime: fhirtypes.Time = Field(
        None,
        alias="closingTime",
        title="Type `Time`",
        description="Time that the Location closes",
    )
    closingTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_closingTime", title="Extension field for ``closingTime``."
    )

    daysOfWeek: ListType[fhirtypes.Code] = Field(
        None,
        alias="daysOfWeek",
        title="List of `Code` items",
        description="mon | tue | wed | thu | fri | sat | sun",
    )
    daysOfWeek__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_daysOfWeek", title="Extension field for ``daysOfWeek``.")

    openingTime: fhirtypes.Time = Field(
        None,
        alias="openingTime",
        title="Type `Time`",
        description="Time that the Location opens",
    )
    openingTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_openingTime", title="Extension field for ``openingTime``."
    )


class LocationPosition(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The absolute geographic location.
    The absolute geographic location of the Location, expressed using the WGS84
    datum (This is the same co-ordinate system used in KML).
    """

    resource_type = Field("LocationPosition", const=True)

    altitude: fhirtypes.Decimal = Field(
        None,
        alias="altitude",
        title="Type `Decimal`",
        description="Altitude with WGS84 datum",
    )
    altitude__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_altitude", title="Extension field for ``altitude``."
    )

    latitude: fhirtypes.Decimal = Field(
        ...,
        alias="latitude",
        title="Type `Decimal`",
        description="Latitude with WGS84 datum",
    )
    latitude__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_latitude", title="Extension field for ``latitude``."
    )

    longitude: fhirtypes.Decimal = Field(
        ...,
        alias="longitude",
        title="Type `Decimal`",
        description="Longitude with WGS84 datum",
    )
    longitude__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_longitude", title="Extension field for ``longitude``."
    )
