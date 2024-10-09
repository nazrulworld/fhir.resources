from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Device
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Device(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Item used in healthcare.
    This resource identifies an instance or a type of a manufactured item that
    is used in the provision of healthcare without being substantially changed
    through that activity. The device may be a medical or non-medical device.
    Medical devices include durable (reusable) medical equipment, implantable
    devices, as well as disposable equipment used for diagnostic, treatment,
    and research for healthcare and public health.  Non-medical devices may
    include items such as a machine, cellphone, computer, application, etc.
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
        title="Where the resource is found",
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

    model: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="model",
        title="Model id assigned by the manufacturer",
        description=(
            'The "model" is an identifier assigned by the manufacturer to identify '
            "the product by its type. This number is shared by the all devices sold"
            " as the same type."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    model__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_model", title="Extension field for ``model``."
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

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="What kind of device this is",
        description="Code or identifier to identify a kind of device.",
        json_schema_extra={
            "element_property": True,
        },
    )

    udi: fhirtypes.DeviceUdiType | None = Field(  # type: ignore
        None,
        alias="udi",
        title="Unique Device Identifier (UDI) Barcode string",
        description=(
            "[Unique device identifier (UDI)](device.html#5.11.3.2.2) assigned to "
            "device label or package."
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

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="Version number (i.e. software)",
        description=(
            "The version of the device, if the device has multiple releases under "
            "the same model, or if the device is software or carries firmware."
        ),
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
            "udi",
            "status",
            "type",
            "lotNumber",
            "manufacturer",
            "manufactureDate",
            "expirationDate",
            "model",
            "version",
            "patient",
            "owner",
            "contact",
            "location",
            "url",
            "note",
            "safety",
        ]


class DeviceUdi(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Unique Device Identifier (UDI) Barcode string.
    [Unique device identifier (UDI)](device.html#5.11.3.2.2) assigned to device
    label or package.
    """

    __resource_type__ = "DeviceUdi"

    carrierAIDC: fhirtypes.Base64BinaryType | None = Field(  # type: ignore
        None,
        alias="carrierAIDC",
        title="UDI Machine Readable Barcode String",
        description=(
            "The full UDI carrier of the Automatic Identification and Data Capture "
            "(AIDC) technology representation of the barcode string as printed on "
            "the packaging of the device - E.g a barcode or RFID.   Because of "
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
            "jurisdiction.  All UDIs are globally unique within a single namespace."
            " with the appropriate repository uri as the system.  For example,  "
            "UDIs of devices managed in the U.S. by the FDA, the value is  "
            "http://hl7.org/fhir/NamingSystem/fda-udi."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    jurisdiction__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_jurisdiction", title="Extension field for ``jurisdiction``."
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Device Name as appears on UDI label",
        description="Name of device as used in labeling or catalog.",
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceUdi`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "deviceIdentifier",
            "name",
            "jurisdiction",
            "carrierHRF",
            "carrierAIDC",
            "issuer",
            "entryType",
        ]
