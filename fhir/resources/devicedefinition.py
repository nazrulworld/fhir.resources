# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceDefinition
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType
from typing import Union

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class DeviceDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An instance of a medical-related component of a medical device.
    The characteristics, operational status and capabilities of a medical-
    related component of a medical device.
    """

    resource_type = Field("DeviceDefinition", const=True)

    capability: ListType[fhirtypes.DeviceDefinitionCapabilityType] = Field(
        None,
        alias="capability",
        title=(
            "List of `DeviceDefinitionCapability` items (represented as `dict` in "
            "JSON)"
        ),
        description="Device capabilities",
    )

    contact: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="contact",
        title="List of `ContactPoint` items (represented as `dict` in JSON)",
        description="Details for human/organization for support",
    )

    deviceName: ListType[fhirtypes.DeviceDefinitionDeviceNameType] = Field(
        None,
        alias="deviceName",
        title=(
            "List of `DeviceDefinitionDeviceName` items (represented as `dict` in "
            "JSON)"
        ),
        description="A name given to the device to identify it",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Instance identifier",
    )

    languageCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="languageCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description=(
            "Language code for the human-readable text strings produced by the "
            "device (all supported)"
        ),
    )

    manufacturerReference: fhirtypes.ReferenceType = Field(
        None,
        alias="manufacturerReference",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Name of device manufacturer",
        one_of_many="manufacturer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    manufacturerString: fhirtypes.String = Field(
        None,
        alias="manufacturerString",
        title="Type `String`",
        description="Name of device manufacturer",
        one_of_many="manufacturer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    manufacturerString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_manufacturerString",
        title="Extension field for ``manufacturerString``.",
    )

    material: ListType[fhirtypes.DeviceDefinitionMaterialType] = Field(
        None,
        alias="material",
        title=(
            "List of `DeviceDefinitionMaterial` items (represented as `dict` in "
            "JSON)"
        ),
        description="A substance used to create the material(s) of which the device is made",
    )

    modelNumber: fhirtypes.String = Field(
        None,
        alias="modelNumber",
        title="Type `String`",
        description="The model number for the device",
    )
    modelNumber__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_modelNumber", title="Extension field for ``modelNumber``."
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Device notes and comments",
    )

    onlineInformation: fhirtypes.Uri = Field(
        None,
        alias="onlineInformation",
        title="Type `Uri`",
        description="Access to on-line information",
    )
    onlineInformation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_onlineInformation",
        title="Extension field for ``onlineInformation``.",
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

    parentDevice: fhirtypes.ReferenceType = Field(
        None,
        alias="parentDevice",
        title=(
            "Type `Reference` referencing `DeviceDefinition` (represented as `dict`"
            " in JSON)"
        ),
        description="The parent device it can be part of",
    )

    physicalCharacteristics: fhirtypes.ProdCharacteristicType = Field(
        None,
        alias="physicalCharacteristics",
        title="Type `ProdCharacteristic` (represented as `dict` in JSON)",
        description="Dimensions, color etc.",
    )

    property: ListType[fhirtypes.DeviceDefinitionPropertyType] = Field(
        None,
        alias="property",
        title=(
            "List of `DeviceDefinitionProperty` items (represented as `dict` in "
            "JSON)"
        ),
        description=(
            "The actual configuration settings of a device as it actually operates,"
            " e.g., regulation status, time properties"
        ),
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description=(
            "The quantity of the device present in the packaging (e.g. the number "
            "of devices present in a pack, or the number of devices in the same "
            "package of the medicinal product)"
        ),
    )

    safety: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="safety",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Safety characteristics of the device",
    )

    shelfLifeStorage: ListType[fhirtypes.ProductShelfLifeType] = Field(
        None,
        alias="shelfLifeStorage",
        title="List of `ProductShelfLife` items (represented as `dict` in JSON)",
        description="Shelf Life and storage information",
    )

    specialization: ListType[fhirtypes.DeviceDefinitionSpecializationType] = Field(
        None,
        alias="specialization",
        title=(
            "List of `DeviceDefinitionSpecialization` items (represented as `dict` "
            "in JSON)"
        ),
        description=(
            "The capabilities supported on a  device, the standards to which the "
            "device conforms for a particular purpose, and used for the "
            "communication"
        ),
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="What kind of device or device system this is",
    )

    udiDeviceIdentifier: ListType[
        fhirtypes.DeviceDefinitionUdiDeviceIdentifierType
    ] = Field(
        None,
        alias="udiDeviceIdentifier",
        title=(
            "List of `DeviceDefinitionUdiDeviceIdentifier` items (represented as "
            "`dict` in JSON)"
        ),
        description="Unique Device Identifier (UDI) Barcode string",
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri`",
        description="Network address to contact device",
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    version: ListType[fhirtypes.String] = Field(
        None,
        alias="version",
        title="List of `String` items",
        description="Available versions",
    )
    version__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    @root_validator(pre=True)
    def validate_one_of_many(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "manufacturer": ["manufacturerReference", "manufacturerString"]
        }
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values


class DeviceDefinitionCapability(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Device capabilities.
    """

    resource_type = Field("DeviceDefinitionCapability", const=True)

    description: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="description",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Description of capability",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of capability",
    )


class DeviceDefinitionDeviceName(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A name given to the device to identify it.
    """

    resource_type = Field("DeviceDefinitionDeviceName", const=True)

    name: fhirtypes.String = Field(
        ..., alias="name", title="Type `String`", description="The name of the device"
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code`",
        description=(
            "udi-label-name | user-friendly-name | patient-reported-name | "
            "manufacturer-name | model-name | other"
        ),
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )


class DeviceDefinitionMaterial(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A substance used to create the material(s) of which the device is made.
    """

    resource_type = Field("DeviceDefinitionMaterial", const=True)

    allergenicIndicator: bool = Field(
        None,
        alias="allergenicIndicator",
        title="Type `bool`",
        description="Whether the substance is a known or suspected allergen",
    )
    allergenicIndicator__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_allergenicIndicator",
        title="Extension field for ``allergenicIndicator``.",
    )

    alternate: bool = Field(
        None,
        alias="alternate",
        title="Type `bool`",
        description="Indicates an alternative material of the device",
    )
    alternate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_alternate", title="Extension field for ``alternate``."
    )

    substance: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="substance",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The substance",
    )


class DeviceDefinitionProperty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The actual configuration settings of a device as it actually operates,
    e.g., regulation status, time properties.
    """

    resource_type = Field("DeviceDefinitionProperty", const=True)

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


class DeviceDefinitionSpecialization(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The capabilities supported on a  device, the standards to which the device
    conforms for a particular purpose, and used for the communication.
    """

    resource_type = Field("DeviceDefinitionSpecialization", const=True)

    systemType: fhirtypes.String = Field(
        ...,
        alias="systemType",
        title="Type `String`",
        description="The standard that is used to operate and communicate",
    )
    systemType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_systemType", title="Extension field for ``systemType``."
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String`",
        description="The version of the standard that is used to operate and communicate",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class DeviceDefinitionUdiDeviceIdentifier(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Unique Device Identifier (UDI) Barcode string.
    Unique device identifier (UDI) assigned to device label or package.  Note
    that the Device may include multiple udiCarriers as it either may include
    just the udiCarrier for the jurisdiction it is sold, or for multiple
    jurisdictions it could have been sold.
    """

    resource_type = Field("DeviceDefinitionUdiDeviceIdentifier", const=True)

    deviceIdentifier: fhirtypes.String = Field(
        ...,
        alias="deviceIdentifier",
        title="Type `String`",
        description=(
            "The identifier that is to be associated with every Device that "
            "references this DeviceDefintiion for the issuer and jurisdication "
            "porvided in the DeviceDefinition.udiDeviceIdentifier"
        ),
    )
    deviceIdentifier__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_deviceIdentifier",
        title="Extension field for ``deviceIdentifier``.",
    )

    issuer: fhirtypes.Uri = Field(
        ...,
        alias="issuer",
        title="Type `Uri`",
        description="The organization that assigns the identifier algorithm",
    )
    issuer__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_issuer", title="Extension field for ``issuer``."
    )

    jurisdiction: fhirtypes.Uri = Field(
        ...,
        alias="jurisdiction",
        title="Type `Uri`",
        description="The jurisdiction to which the deviceIdentifier applies",
    )
    jurisdiction__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_jurisdiction", title="Extension field for ``jurisdiction``."
    )
