# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Device
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Device(domainresource.DomainResource):
    """ Item used in healthcare.
    This resource identifies an instance or a type of a manufactured item that
    is used in the provision of healthcare without being substantially changed
    through that activity. The device may be a medical or non-medical device.
    Medical devices include durable (reusable) medical equipment, implantable
    devices, as well as disposable equipment used for diagnostic, treatment,
    and research for healthcare and public health.  Non-medical devices may
    include items such as a machine, cellphone, computer, application, etc.
    """

    resource_type = Field("Device", const=True)

    contact: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="contact",
        title="List of `ContactPoint` items (represented as `dict` in JSON)",
        description="Details for human/organization for support",
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
        title="Type `Reference` referencing `Location` (represented as `dict` in JSON)",
        description="Where the resource is found",
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

    model: fhirtypes.String = Field(
        None,
        alias="model",
        title="Type `String` (represented as `dict` in JSON)",
        description="Model id assigned by the manufacturer",
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
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Organization responsible for device",
    )

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="Patient to whom Device is affixed",
    )

    safety: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="safety",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Safety Characteristics of Device",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="active | inactive | entered-in-error | unknown",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="What kind of device this is",
    )

    udi: fhirtypes.DeviceUdiType = Field(
        None,
        alias="udi",
        title="Type `DeviceUdi` (represented as `dict` in JSON)",
        description="Unique Device Identifier (UDI) Barcode string",
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Network address to contact device",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String` (represented as `dict` in JSON)",
        description="Version number (i.e. software)",
    )


class DeviceUdi(backboneelement.BackboneElement):
    """ Unique Device Identifier (UDI) Barcode string.
    [Unique device identifier (UDI)](device.html#5.11.3.2.2) assigned to device
    label or package.
    """

    resource_type = Field("DeviceUdi", const=True)

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

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Device Name as appears on UDI label",
    )
