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
        title="Device capabilities",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    contact: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="contact",
        title="Details for human/organization for support",
        description=(
            "Contact details for an organization or a particular human that is "
            "responsible for the device."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    deviceName: ListType[fhirtypes.DeviceDefinitionDeviceNameType] = Field(
        None,
        alias="deviceName",
        title="A name given to the device to identify it",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Instance identifier",
        description=(
            "Unique instance identifiers assigned to a device by the software, "
            "manufacturers, other organizations or owners. For example: handle ID."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    languageCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="languageCode",
        title=(
            "Language code for the human-readable text strings produced by the "
            "device (all supported)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    manufacturerReference: fhirtypes.ReferenceType = Field(
        None,
        alias="manufacturerReference",
        title="Name of device manufacturer",
        description="A name of the manufacturer.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e manufacturer[x]
        one_of_many="manufacturer",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    manufacturerString: fhirtypes.String = Field(
        None,
        alias="manufacturerString",
        title="Name of device manufacturer",
        description="A name of the manufacturer.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e manufacturer[x]
        one_of_many="manufacturer",
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
        title="A substance used to create the material(s) of which the device is made",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    modelNumber: fhirtypes.String = Field(
        None,
        alias="modelNumber",
        title="The model number for the device",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    modelNumber__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_modelNumber", title="Extension field for ``modelNumber``."
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Device notes and comments",
        description=(
            "Descriptive information, usage information or implantation information"
            " that is not captured in an existing element."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    onlineInformation: fhirtypes.Uri = Field(
        None,
        alias="onlineInformation",
        title="Access to on-line information",
        description="Access to on-line information about the device.",
        # if property is element of this resource.
        element_property=True,
    )
    onlineInformation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_onlineInformation",
        title="Extension field for ``onlineInformation``.",
    )

    owner: fhirtypes.ReferenceType = Field(
        None,
        alias="owner",
        title="Organization responsible for device",
        description=(
            "An organization that is responsible for the provision and ongoing "
            "maintenance of the device."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    parentDevice: fhirtypes.ReferenceType = Field(
        None,
        alias="parentDevice",
        title="The parent device it can be part of",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DeviceDefinition"],
    )

    physicalCharacteristics: fhirtypes.ProdCharacteristicType = Field(
        None,
        alias="physicalCharacteristics",
        title="Dimensions, color etc.",
        description="Dimensions, color etc.",
        # if property is element of this resource.
        element_property=True,
    )

    property: ListType[fhirtypes.DeviceDefinitionPropertyType] = Field(
        None,
        alias="property",
        title=(
            "The actual configuration settings of a device as it actually operates,"
            " e.g., regulation status, time properties"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title=(
            "The quantity of the device present in the packaging (e.g. the number "
            "of devices present in a pack, or the number of devices in the same "
            "package of the medicinal product)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    safety: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="safety",
        title="Safety characteristics of the device",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    shelfLifeStorage: ListType[fhirtypes.ProductShelfLifeType] = Field(
        None,
        alias="shelfLifeStorage",
        title="Shelf Life and storage information",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    specialization: ListType[fhirtypes.DeviceDefinitionSpecializationType] = Field(
        None,
        alias="specialization",
        title=(
            "The capabilities supported on a  device, the standards to which the "
            "device conforms for a particular purpose, and used for the "
            "communication"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="What kind of device or device system this is",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    udiDeviceIdentifier: ListType[
        fhirtypes.DeviceDefinitionUdiDeviceIdentifierType
    ] = Field(
        None,
        alias="udiDeviceIdentifier",
        title="Unique Device Identifier (UDI) Barcode string",
        description=(
            "Unique device identifier (UDI) assigned to device label or package.  "
            "Note that the Device may include multiple udiCarriers as it either may"
            " include just the udiCarrier for the jurisdiction it is sold, or for "
            "multiple jurisdictions it could have been sold."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Network address to contact device",
        description="A network address on which the device may be contacted directly.",
        # if property is element of this resource.
        element_property=True,
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    version: ListType[fhirtypes.String] = Field(
        None,
        alias="version",
        title="Available versions",
        description="The available versions of the device, e.g., software versions.",
        # if property is element of this resource.
        element_property=True,
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
        title="Description of capability",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type of capability",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class DeviceDefinitionDeviceName(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A name given to the device to identify it.
    """

    resource_type = Field("DeviceDefinitionDeviceName", const=True)

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="The name of the device",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title=(
            "udi-label-name | user-friendly-name | patient-reported-name | "
            "manufacturer-name | model-name | other"
        ),
        description=(
            "The type of deviceName. UDILabelName | UserFriendlyName | "
            "PatientReportedName | ManufactureDeviceName | ModelName."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "udi-label-name",
            "user-friendly-name",
            "patient-reported-name",
            "manufacturer-name",
            "model-name",
            "other",
        ],
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
        title="Whether the substance is a known or suspected allergen",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    allergenicIndicator__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_allergenicIndicator",
        title="Extension field for ``allergenicIndicator``.",
    )

    alternate: bool = Field(
        None,
        alias="alternate",
        title="Indicates an alternative material of the device",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    alternate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_alternate", title="Extension field for ``alternate``."
    )

    substance: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="substance",
        title="The substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
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
        title=(
            "Code that specifies the property DeviceDefinitionPropetyCode "
            "(Extensible)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    valueCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="valueCode",
        title="Property value as a code, e.g., NTP4 (synced to NTP)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    valueQuantity: ListType[fhirtypes.QuantityType] = Field(
        None,
        alias="valueQuantity",
        title="Property value as a quantity",
        description=None,
        # if property is element of this resource.
        element_property=True,
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
        title="The standard that is used to operate and communicate",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    systemType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_systemType", title="Extension field for ``systemType``."
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="The version of the standard that is used to operate and communicate",
        description=None,
        # if property is element of this resource.
        element_property=True,
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
        title=(
            "The identifier that is to be associated with every Device that "
            "references this DeviceDefintiion for the issuer and jurisdication "
            "porvided in the DeviceDefinition.udiDeviceIdentifier"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    deviceIdentifier__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_deviceIdentifier",
        title="Extension field for ``deviceIdentifier``.",
    )

    issuer: fhirtypes.Uri = Field(
        ...,
        alias="issuer",
        title="The organization that assigns the identifier algorithm",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    issuer__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_issuer", title="Extension field for ``issuer``."
    )

    jurisdiction: fhirtypes.Uri = Field(
        ...,
        alias="jurisdiction",
        title="The jurisdiction to which the deviceIdentifier applies",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    jurisdiction__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_jurisdiction", title="Extension field for ``jurisdiction``."
    )
