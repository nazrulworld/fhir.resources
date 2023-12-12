# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Location
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
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
    provided  and resources and participants may be stored, found, contained or
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
            "A list of\u00a0alternate names that the location is known as, or was known "
            "as in the past"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    alias__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_alias", title="Extension field for ``alias``.")

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
        title="The Operational status of the location (typically only for a bed/room)",
        description=(
            "The Operational status covers operation values most relevant to beds "
            "(but can also apply to rooms/units/chair/etc such as an isolation "
            "unit/dialisys chair). This typically covers concepts such as "
            "contamination, housekeeping and other activities\u00a0like maintenance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    partOf: fhirtypes.ReferenceType = Field(
        None,
        alias="partOf",
        title="Another Location this one is physically part of",
        description="Another Location which this Location is physically part of.",
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

    type: fhirtypes.CodeableConceptType = Field(
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
            "endpoint",
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
