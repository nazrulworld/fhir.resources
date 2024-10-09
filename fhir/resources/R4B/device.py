from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Device
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Device(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Item used in healthcare.
    A type of a manufactured item that is used in the provision of healthcare
    without being substantially changed through that activity. The device may
    be a medical or non-medical device.
    """

    __resource_type__ = "Device"

    contact: typing.List[fhirtypes.ContactPointType] | None = Field(  # type: ignore
        None,
        alias="contact",
        title="Details for human/organization for support",
        description=(
            "Contact details for an organization or a particular human that is "
            "responsible for the device."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    definition: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="definition",
        title="The reference to the definition for the device",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DeviceDefinition"],
        },
    )

    deviceName: typing.List[fhirtypes.DeviceDeviceNameType] | None = Field(  # type: ignore
        None,
        alias="deviceName",
        title="The name of the device as given by the manufacturer",
        description=(
            "This represents the manufacturer's name of the device as provided by "
            "the device, from a UDI label, or by a person describing the Device.  "
            "This typically would be used when a person provides the name(s) or "
            "when the device represents one of the names available from "
            "DeviceDefinition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    distinctIdentifier: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="distinctIdentifier",
        title="The distinct identification string",
        description=(
            "The distinct identification string as required by regulation for a "
            "human cell, tissue, or cellular and tissue-based product."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    distinctIdentifier__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_distinctIdentifier",
        title="Extension field for ``distinctIdentifier``.",
    )

    expirationDate: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="expirationDate",
        title="Date and time of expiry of this device (if applicable)",
        description=(
            "The date and time beyond which this device is no longer valid or "
            "should not be used (if applicable)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    expirationDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_expirationDate", title="Extension field for ``expirationDate``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Instance identifier",
        description=(
            "Unique instance identifiers assigned to a device by manufacturers "
            "other organizations or owners."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    location: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="location",
        title="Where the device is found",
        description="The place where the device can be found.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    lotNumber: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="lotNumber",
        title="Lot number of manufacture",
        description="Lot number assigned by the manufacturer.",
        json_schema_extra={
            "element_property": True,
        },
    )
    lotNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_lotNumber", title="Extension field for ``lotNumber``."
    )

    manufactureDate: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="manufactureDate",
        title="Date when the device was made",
        description="The date and time when the device was manufactured.",
        json_schema_extra={
            "element_property": True,
        },
    )
    manufactureDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_manufactureDate", title="Extension field for ``manufactureDate``."
    )

    manufacturer: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="manufacturer",
        title="Name of device manufacturer",
        description="A name of the manufacturer.",
        json_schema_extra={
            "element_property": True,
        },
    )
    manufacturer__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_manufacturer", title="Extension field for ``manufacturer``."
    )

    modelNumber: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="modelNumber",
        title="The manufacturer's model number for the device",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    modelNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_modelNumber", title="Extension field for ``modelNumber``."
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="note",
        title="Device notes and comments",
        description=(
            "Descriptive information, usage information or implantation information"
            " that is not captured in an existing element."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    owner: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="owner",
        title="Organization responsible for device",
        description=(
            "An organization that is responsible for the provision and ongoing "
            "maintenance of the device."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    parent: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="parent",
        title="The device that this device is attached to or is part of",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Device"],
        },
    )

    partNumber: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="partNumber",
        title="The part number or catalog number of the device",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    partNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_partNumber", title="Extension field for ``partNumber``."
    )

    patient: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="patient",
        title="Patient to whom Device is affixed",
        description="Patient information, If the device is affixed to a person.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient"],
        },
    )

    property: typing.List[fhirtypes.DevicePropertyType] | None = Field(  # type: ignore
        None,
        alias="property",
        title=(
            "The actual configuration settings of a device as it actually operates,"
            " e.g., regulation status, time properties"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    safety: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="safety",
        title="Safety Characteristics of Device",
        description=(
            "Provides additional safety characteristics about a medical device.  "
            "For example devices containing latex."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    serialNumber: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="serialNumber",
        title="Serial number assigned by the manufacturer",
        description=(
            "The serial number assigned by the organization when the device was "
            "manufactured."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    serialNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_serialNumber", title="Extension field for ``serialNumber``."
    )

    specialization: typing.List[fhirtypes.DeviceSpecializationType] | None = Field(  # type: ignore
        None,
        alias="specialization",
        title=(
            "The capabilities supported on a  device, the standards to which the "
            "device conforms for a particular purpose, and used for the "
            "communication"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="active | inactive | entered-in-error | unknown",
        description="Status of the Device availability.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["active", "inactive", "entered-in-error", "unknown"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    statusReason: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="statusReason",
        title=(
            "online | paused | standby | offline | not-ready | transduc-discon | "
            "hw-discon | off"
        ),
        description="Reason for the dtatus of the Device availability.",
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="The kind or type of device",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    udiCarrier: typing.List[fhirtypes.DeviceUdiCarrierType] | None = Field(  # type: ignore
        None,
        alias="udiCarrier",
        title="Unique Device Identifier (UDI) Barcode string",
        description=(
            "Unique device identifier (UDI) assigned to device label or package.  "
            "Note that the Device may include multiple udiCarriers as it either may"
            " include just the udiCarrier for the jurisdiction it is sold, or for "
            "multiple jurisdictions it could have been sold."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    url: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="url",
        title="Network address to contact device",
        description="A network address on which the device may be contacted directly.",
        json_schema_extra={
            "element_property": True,
        },
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_url", title="Extension field for ``url``."
    )

    version: typing.List[fhirtypes.DeviceVersionType] | None = Field(  # type: ignore
        None,
        alias="version",
        title=(
            "The actual design of the device or software version running on the "
            "device"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Device`` according specification,
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
            "definition",
            "udiCarrier",
            "status",
            "statusReason",
            "distinctIdentifier",
            "manufacturer",
            "manufactureDate",
            "expirationDate",
            "lotNumber",
            "serialNumber",
            "deviceName",
            "modelNumber",
            "partNumber",
            "type",
            "specialization",
            "version",
            "property",
            "patient",
            "owner",
            "contact",
            "location",
            "url",
            "note",
            "safety",
            "parent",
        ]


class DeviceDeviceName(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The name of the device as given by the manufacturer.
    This represents the manufacturer's name of the device as provided by the
    device, from a UDI label, or by a person describing the Device.  This
    typically would be used when a person provides the name(s) or when the
    device represents one of the names available from DeviceDefinition.
    """

    __resource_type__ = "DeviceDeviceName"

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="The name that identifies the device",
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title=(
            "udi-label-name | user-friendly-name | patient-reported-name | "
            "manufacturer-name | model-name | other"
        ),
        description=(
            "The type of deviceName. UDILabelName | UserFriendlyName | "
            "PatientReportedName | ManufactureDeviceName | ModelName."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "udi-label-name",
                "user-friendly-name",
                "patient-reported-name",
                "manufacturer-name",
                "model-name",
                "other",
            ],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceDeviceName`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "name", "type"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("name", "name__ext"), ("type", "type__ext")]
        return required_fields


class DeviceProperty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The actual configuration settings of a device as it actually operates,
    e.g., regulation status, time properties.
    """

    __resource_type__ = "DeviceProperty"

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title=(
            "Code that specifies the property DeviceDefinitionPropetyCode "
            "(Extensible)"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    valueCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="valueCode",
        title="Property value as a code, e.g., NTP4 (synced to NTP)",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    valueQuantity: typing.List[fhirtypes.QuantityType] | None = Field(  # type: ignore
        None,
        alias="valueQuantity",
        title="Property value as a quantity",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceProperty`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "valueQuantity",
            "valueCode",
        ]


class DeviceSpecialization(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The capabilities supported on a  device, the standards to which the device
    conforms for a particular purpose, and used for the communication.
    """

    __resource_type__ = "DeviceSpecialization"

    systemType: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="systemType",
        title="The standard that is used to operate and communicate",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="The version of the standard that is used to operate and communicate",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_version", title="Extension field for ``version``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceSpecialization`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "systemType", "version"]


class DeviceUdiCarrier(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Unique Device Identifier (UDI) Barcode string.
    Unique device identifier (UDI) assigned to device label or package.  Note
    that the Device may include multiple udiCarriers as it either may include
    just the udiCarrier for the jurisdiction it is sold, or for multiple
    jurisdictions it could have been sold.
    """

    __resource_type__ = "DeviceUdiCarrier"

    carrierAIDC: fhirtypes.Base64BinaryType | None = Field(  # type: ignore
        None,
        alias="carrierAIDC",
        title="UDI Machine Readable Barcode String",
        description=(
            "The full UDI carrier of the Automatic Identification and Data Capture "
            "(AIDC) technology representation of the barcode string as printed on "
            "the packaging of the device - e.g., a barcode or RFID.   Because of "
            "limitations on character sets in XML and the need to round-trip JSON "
            "data through XML, AIDC Formats *SHALL* be base64 encoded."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    carrierAIDC__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_carrierAIDC", title="Extension field for ``carrierAIDC``."
    )

    carrierHRF: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="carrierHRF",
        title="UDI Human Readable Barcode String",
        description=(
            "The full UDI carrier as the human readable form (HRF) representation "
            "of the barcode string as printed on the packaging of the device."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    carrierHRF__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_carrierHRF", title="Extension field for ``carrierHRF``."
    )

    deviceIdentifier: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="deviceIdentifier",
        title="Mandatory fixed portion of UDI",
        description=(
            "The device identifier (DI) is a mandatory, fixed portion of a UDI that"
            " identifies the labeler and the specific version or model of a device."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    deviceIdentifier__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_deviceIdentifier",
        title="Extension field for ``deviceIdentifier``.",
    )

    entryType: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="entryType",
        title="barcode | rfid | manual +",
        description="A coded entry to indicate how the data was entered.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["barcode", "rfid", "manual", "+"],
        },
    )
    entryType__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_entryType", title="Extension field for ``entryType``."
    )

    issuer: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="issuer",
        title="UDI Issuing Organization",
        description=(
            "Organization that is charged with issuing UDIs for devices.  For "
            "example, the US FDA issuers include : 1) GS1:  "
            "http://hl7.org/fhir/NamingSystem/gs1-di,  2) HIBCC: "
            "http://hl7.org/fhir/NamingSystem/hibcc-dI,  3) ICCBBA for blood "
            "containers: http://hl7.org/fhir/NamingSystem/iccbba-blood-di,  4) "
            "ICCBA for other devices: http://hl7.org/fhir/NamingSystem/iccbba-"
            "other-di."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    issuer__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_issuer", title="Extension field for ``issuer``."
    )

    jurisdiction: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="jurisdiction",
        title="Regional UDI authority",
        description=(
            "The identity of the authoritative source for UDI generation within a  "
            "jurisdiction.  All UDIs are globally unique within a single namespace "
            "with the appropriate repository uri as the system.  For example,  UDIs"
            " of devices managed in the U.S. by the FDA, the value is  "
            "http://hl7.org/fhir/NamingSystem/fda-udi."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    jurisdiction__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_jurisdiction", title="Extension field for ``jurisdiction``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceUdiCarrier`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "deviceIdentifier",
            "issuer",
            "jurisdiction",
            "carrierAIDC",
            "carrierHRF",
            "entryType",
        ]


class DeviceVersion(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The actual design of the device or software version running on the device.
    """

    __resource_type__ = "DeviceVersion"

    component: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="component",
        title="A single component of the device version",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="The type of the device version, e.g. manufacturer, approved, internal",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    value: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="value",
        title="The version text",
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceVersion`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "component", "value"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("value", "value__ext")]
        return required_fields
