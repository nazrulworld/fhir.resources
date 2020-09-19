# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Device
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic import Field

from . import fhirtypes
from .domainresource import DomainResource


class Device(DomainResource):
    """An instance of a manufactured te that is used in the provision of
    healthcare.

    This resource identifies an instance of a manufactured item that is used in
    the provision of healthcare without being substantially changed through
    that activity. The device may be a medical or non-medical device.  Medical
    devices includes durable (reusable) medical equipment, implantable devices,
    as well as disposable equipment used for diagnostic, treatment, and
    research for healthcare and public health.  Non-medical devices may include
    items such as a machine, cellphone, computer, application, etc.
    """

    resource_type = Field("Device", const=True)

    manufacturer: fhirtypes.String = Field(
        None,
        alias="manufacturer",
        title="Type `String`.",
        description="Name of device manufacturer.",
    )
    model: fhirtypes.String = Field(
        None,
        alias="model",
        title="Type `String`.",
        description="Model id assigned by the manufacturer.",
    )
    lotNumber: fhirtypes.String = Field(
        None,
        alias="lotNumber",
        title="Type `String`.",
        description="Lot number of manufacture.",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code`.",
        description="available | not-available | entered-in-error.",
    )

    udi: fhirtypes.String = Field(
        None,
        alias="udi",
        title="Type `String`.",
        description="FDA mandated Unique Device Identifier.",
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri`.",
        description="Network address to contact device.",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String`.",
        description="Version number (i.e. software).",
    )
    manufactureDate: fhirtypes.DateTime = Field(
        None,
        alias="manufactureDate",
        title="Type `DateTime`.",
        description="Manufacture date.",
    )
    expiry: fhirtypes.DateTime = Field(
        None,
        alias="expiry",
        title="Type `DateTime`.",
        description="Date and time of expiry of this device (if applicable).",
    )
    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="What kind of device this is.",
    )
    owner: fhirtypes.ReferenceType = Field(
        None,
        alias="owner",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON).",
        description="Organization responsible for device.",
    )

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON).",
        description="If the resource is affixed to a person.",
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title="Type `Reference` referencing `Location` (represented as `dict` in JSON).",
        description="Where the resource is found.",
    )

    contact: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="contact",
        title="List of `ContactPoint` items (represented as `dict` in JSON).",
        description="Details for human/organization for support.",
    )
    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON).",
        description="Instance id from manufacturer, owner, and others.",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON).",
        description="Device notes and comments.",
    )
