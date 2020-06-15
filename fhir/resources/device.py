# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Device
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Device(domainresource.DomainResource):
    """ Item used in healthcare.
    A type of a manufactured item that is used in the provision of healthcare
    without being substantially changed through that activity. The device may
    be a medical or non-medical device.
    """

    resource_type = Field("Device", const=True)

    contact: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="contact",
        title="List of `ContactPoint` items (represented as `dict` in JSON)",
        description="Details for human/organization for support",
    )

    definition: fhirtypes.ReferenceType = Field(
        None,
        alias="definition",
        title=(
            "Type `Reference` referencing `DeviceDefinition` (represented as `dict`"
            " in JSON)"
        ),
        description="The reference to the definition for the device",
    )

    deviceName: ListType[fhirtypes.DeviceDeviceNameType] = Field(
        None,
        alias="deviceName",
        title="List of `DeviceDeviceName` items (represented as `dict` in JSON)",
        description="The name of the device as given by the manufacturer",
    )

    distinctIdentifier: fhirtypes.String = Field(
        None,
        alias="distinctIdentifier",
        title="Type `String` (represented as `dict` in JSON)",
        description="The distinct identification string",
    )

    expirationDate: fhirtypes.DateTime = Field(
        None,
        alias="expirationDate",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date and time of expiry of this device (if applicable)",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Instance identifier",
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title=(
            "Type `Reference` referencing `Location` (represented as `dict` in " "JSON)"
        ),
        description="Where the device is found",
    )

    lotNumber: fhirtypes.String = Field(
        None,
        alias="lotNumber",
        title="Type `String` (represented as `dict` in JSON)",
        description="Lot number of manufacture",
    )

    manufactureDate: fhirtypes.DateTime = Field(
        None,
        alias="manufactureDate",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date when the device was made",
    )

    manufacturer: fhirtypes.String = Field(
        None,
        alias="manufacturer",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of device manufacturer",
    )

    modelNumber: fhirtypes.String = Field(
        None,
        alias="modelNumber",
        title="Type `String` (represented as `dict` in JSON)",
        description="The model number for the device",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Device notes and comments",
    )

    owner: fhirtypes.ReferenceType = Field(
        None,
        alias="owner",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Organization responsible for device",
    )

    parent: fhirtypes.ReferenceType = Field(
        None,
        alias="parent",
        title="Type `Reference` referencing `Device` (represented as `dict` in JSON)",
        description="The parent device",
    )

    partNumber: fhirtypes.String = Field(
        None,
        alias="partNumber",
        title="Type `String` (represented as `dict` in JSON)",
        description="The part number of the device",
    )

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="Patient to whom Device is affixed",
    )

    property: ListType[fhirtypes.DevicePropertyType] = Field(
        None,
        alias="property",
        title="List of `DeviceProperty` items (represented as `dict` in JSON)",
        description=(
            "The actual configuration settings of a device as it actually operates,"
            " e.g., regulation status, time properties"
        ),
    )

    safety: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="safety",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Safety Characteristics of Device",
    )

    serialNumber: fhirtypes.String = Field(
        None,
        alias="serialNumber",
        title="Type `String` (represented as `dict` in JSON)",
        description="Serial number assigned by the manufacturer",
    )

    specialization: ListType[fhirtypes.DeviceSpecializationType] = Field(
        None,
        alias="specialization",
        title="List of `DeviceSpecialization` items (represented as `dict` in JSON)",
        description=(
            "The capabilities supported on a  device, the standards to which the "
            "device conforms for a particular purpose, and used for the "
            "communication"
        ),
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="active | inactive | entered-in-error | unknown",
    )

    statusReason: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="statusReason",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description=(
            "online | paused | standby | offline | not-ready | transduc-discon | "
            "hw-discon | off"
        ),
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The kind or type of device",
    )

    udiCarrier: ListType[fhirtypes.DeviceUdiCarrierType] = Field(
        None,
        alias="udiCarrier",
        title="List of `DeviceUdiCarrier` items (represented as `dict` in JSON)",
        description="Unique Device Identifier (UDI) Barcode string",
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Network address to contact device",
    )

    version: ListType[fhirtypes.DeviceVersionType] = Field(
        None,
        alias="version",
        title="List of `DeviceVersion` items (represented as `dict` in JSON)",
        description=(
            "The actual design of the device or software version running on the "
            "device"
        ),
    )


class DeviceDeviceName(backboneelement.BackboneElement):
    """ The name of the device as given by the manufacturer.
    This represents the manufacturer's name of the device as provided by the
    device, from a UDI label, or by a person describing the Device.  This
    typically would be used when a person provides the name(s) or when the
    device represents one of the names available from DeviceDefinition.
    """

    resource_type = Field("DeviceDeviceName", const=True)

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="The name of the device",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "udi-label-name | user-friendly-name | patient-reported-name | "
            "manufacturer-name | model-name | other"
        ),
    )


class DeviceProperty(backboneelement.BackboneElement):
    """ The actual configuration settings of a device as it actually operates,
    e.g., regulation status, time properties.
    """

    resource_type = Field("DeviceProperty", const=True)

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "Code that specifies the property DeviceDefinitionPropetyCode "
            "(Extensible)"
        ),
    )

    valueCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="valueCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Property value as a code, e.g., NTP4 (synced to NTP)",
    )

    valueQuantity: ListType[fhirtypes.QuantityType] = Field(
        None,
        alias="valueQuantity",
        title="List of `Quantity` items (represented as `dict` in JSON)",
        description="Property value as a quantity",
    )


class DeviceSpecialization(backboneelement.BackboneElement):
    """ The capabilities supported on a  device, the standards to which the device
    conforms for a particular purpose, and used for the communication.
    """

    resource_type = Field("DeviceSpecialization", const=True)

    systemType: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="systemType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The standard that is used to operate and communicate",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String` (represented as `dict` in JSON)",
        description="The version of the standard that is used to operate and communicate",
    )


class DeviceUdiCarrier(backboneelement.BackboneElement):
    """ Unique Device Identifier (UDI) Barcode string.
    Unique device identifier (UDI) assigned to device label or package.  Note
    that the Device may include multiple udiCarriers as it either may include
    just the udiCarrier for the jurisdiction it is sold, or for multiple
    jurisdictions it could have been sold.
    """

    resource_type = Field("DeviceUdiCarrier", const=True)

    carrierAIDC: fhirtypes.Base64Binary = Field(
        None,
        alias="carrierAIDC",
        title="Type `Base64Binary` (represented as `dict` in JSON)",
        description="UDI Machine Readable Barcode String",
    )

    carrierHRF: fhirtypes.String = Field(
        None,
        alias="carrierHRF",
        title="Type `String` (represented as `dict` in JSON)",
        description="UDI Human Readable Barcode String",
    )

    deviceIdentifier: fhirtypes.String = Field(
        None,
        alias="deviceIdentifier",
        title="Type `String` (represented as `dict` in JSON)",
        description="Mandatory fixed portion of UDI",
    )

    entryType: fhirtypes.Code = Field(
        None,
        alias="entryType",
        title="Type `Code` (represented as `dict` in JSON)",
        description="barcode | rfid | manual +",
    )

    issuer: fhirtypes.Uri = Field(
        None,
        alias="issuer",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="UDI Issuing Organization",
    )

    jurisdiction: fhirtypes.Uri = Field(
        None,
        alias="jurisdiction",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Regional UDI authority",
    )


class DeviceVersion(backboneelement.BackboneElement):
    """ The actual design of the device or software version running on the device.
    """

    resource_type = Field("DeviceVersion", const=True)

    component: fhirtypes.IdentifierType = Field(
        None,
        alias="component",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="A single component of the device version",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The type of the device version",
    )

    value: fhirtypes.String = Field(
        ...,
        alias="value",
        title="Type `String` (represented as `dict` in JSON)",
        description="The version text",
    )
