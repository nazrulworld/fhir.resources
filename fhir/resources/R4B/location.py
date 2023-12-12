# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Location
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class Location(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
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
        title="Physical location",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    alias: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="alias",
        title=(
            "A list of alternate names that the location is known as, or was known "
            "as, in the past"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    alias__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_alias", title="Extension field for ``alias``.")

    availabilityExceptions: fhirtypes.String = Field(
        None,
        alias="availabilityExceptions",
        title="Description of availability exceptions",
        description=(
            "A description of when the locations opening ours are different to "
            "normal, e.g. public holiday availability. Succinctly describing all "
            "possible exceptions to normal site availability as detailed in the "
            "opening hours Times."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    availabilityExceptions__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_availabilityExceptions",
        title="Extension field for ``availabilityExceptions``.",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title=(
            "Additional details about the location that could be displayed as "
            "further information to identify the location beyond its name"
        ),
        description=(
            "Description of the Location, which helps in finding or referencing the"
            " place."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    endpoint: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="endpoint",
        title=(
            "Technical endpoints providing access to services operated for the "
            "location"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Endpoint"],
    )

    hoursOfOperation: typing.List[fhirtypes.LocationHoursOfOperationType] = Field(
        None,
        alias="hoursOfOperation",
        title="What days/times during a week is this location usually open",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Unique code or number identifying the location to its users",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    managingOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="managingOrganization",
        title="Organization responsible for provisioning and upkeep",
        description=(
            "The organization responsible for the provisioning and upkeep of the "
            "location."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    mode: fhirtypes.Code = Field(
        None,
        alias="mode",
        title="instance | kind",
        description=(
            "Indicates whether a resource instance represents a specific location "
            "or a class of locations."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["instance", "kind"],
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_mode", title="Extension field for ``mode``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name of the location as used by humans",
        description="Name of the location as used by humans. Does not need to be unique.",
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    operationalStatus: fhirtypes.CodingType = Field(
        None,
        alias="operationalStatus",
        title="The operational status of the location (typically only for a bed/room)",
        description=(
            "The operational status covers operation values most relevant to beds "
            "(but can also apply to rooms/units/chairs/etc. such as an isolation "
            "unit/dialysis chair). This typically covers concepts such as "
            "contamination, housekeeping, and other activities like maintenance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    partOf: fhirtypes.ReferenceType = Field(
        None,
        alias="partOf",
        title="Another Location this one is physically a part of",
        description="Another Location of which this Location is physically a part of.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    physicalType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="physicalType",
        title="Physical form of the location",
        description="Physical form of the location, e.g. building, room, vehicle, road.",
        # if property is element of this resource.
        element_property=True,
    )

    position: fhirtypes.LocationPositionType = Field(
        None,
        alias="position",
        title="The absolute geographic location",
        description=(
            "The absolute geographic location of the Location, expressed using the "
            "WGS84 datum (This is the same co-ordinate system used in KML)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="active | suspended | inactive",
        description=(
            "The status property covers the general availability of the resource, "
            "not the current value which may be covered by the operationStatus, or "
            "by a schedule/slots if they are configured for the location."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "suspended", "inactive"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    telecom: typing.List[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="Contact details of the location",
        description=(
            "The contact details of communication devices available at the "
            "location. This can include phone numbers, fax numbers, mobile numbers,"
            " email addresses and web sites."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="Type of function performed",
        description="Indicates the type of function performed at the location.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Location`` according specification,
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
            "operationalStatus",
            "name",
            "alias",
            "description",
            "mode",
            "type",
            "telecom",
            "address",
            "physicalType",
            "position",
            "managingOrganization",
            "partOf",
            "hoursOfOperation",
            "availabilityExceptions",
            "endpoint",
        ]


class LocationHoursOfOperation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What days/times during a week is this location usually open.
    """

    resource_type = Field("LocationHoursOfOperation", const=True)

    allDay: bool = Field(
        None,
        alias="allDay",
        title="The Location is open all day",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    allDay__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_allDay", title="Extension field for ``allDay``."
    )

    closingTime: fhirtypes.Time = Field(
        None,
        alias="closingTime",
        title="Time that the Location closes",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    closingTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_closingTime", title="Extension field for ``closingTime``."
    )

    daysOfWeek: typing.List[typing.Optional[fhirtypes.Code]] = Field(
        None,
        alias="daysOfWeek",
        title="mon | tue | wed | thu | fri | sat | sun",
        description=(
            "Indicates which days of the week are available between the start and "
            "end Times."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["mon", "tue", "wed", "thu", "fri", "sat", "sun"],
    )
    daysOfWeek__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_daysOfWeek", title="Extension field for ``daysOfWeek``.")

    openingTime: fhirtypes.Time = Field(
        None,
        alias="openingTime",
        title="Time that the Location opens",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    openingTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_openingTime", title="Extension field for ``openingTime``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``LocationHoursOfOperation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "daysOfWeek",
            "allDay",
            "openingTime",
            "closingTime",
        ]


class LocationPosition(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
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
        title="Altitude with WGS84 datum",
        description=(
            "Altitude. The value domain and the interpretation are the same as for "
            "the text of the altitude element in KML (see notes below)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    altitude__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_altitude", title="Extension field for ``altitude``."
    )

    latitude: fhirtypes.Decimal = Field(
        None,
        alias="latitude",
        title="Latitude with WGS84 datum",
        description=(
            "Latitude. The value domain and the interpretation are the same as for "
            "the text of the latitude element in KML (see notes below)."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    latitude__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_latitude", title="Extension field for ``latitude``."
    )

    longitude: fhirtypes.Decimal = Field(
        None,
        alias="longitude",
        title="Longitude with WGS84 datum",
        description=(
            "Longitude. The value domain and the interpretation are the same as for"
            " the text of the longitude element in KML (see notes below)."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    longitude__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_longitude", title="Extension field for ``longitude``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``LocationPosition`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "longitude",
            "latitude",
            "altitude",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1864(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("latitude", "latitude__ext"),
            ("longitude", "longitude__ext"),
        ]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values
