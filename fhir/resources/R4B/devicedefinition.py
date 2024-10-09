from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class DeviceDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An instance of a medical-related component of a medical device.
    The characteristics, operational status and capabilities of a medical-
    related component of a medical device.
    """

    __resource_type__ = "DeviceDefinition"

    capability: typing.List[fhirtypes.DeviceDefinitionCapabilityType] | None = Field(  # type: ignore
        None,
        alias="capability",
        title="Device capabilities",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

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

    deviceName: typing.List[fhirtypes.DeviceDefinitionDeviceNameType] | None = Field(  # type: ignore
        None,
        alias="deviceName",
        title="A name given to the device to identify it",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Instance identifier",
        description=(
            "Unique instance identifiers assigned to a device by the software, "
            "manufacturers, other organizations or owners. For example: handle ID."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    languageCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="languageCode",
        title=(
            "Language code for the human-readable text strings produced by the "
            "device (all supported)"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    manufacturerReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="manufacturerReference",
        title="Name of device manufacturer",
        description="A name of the manufacturer.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e manufacturer[x]
            "one_of_many": "manufacturer",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    manufacturerString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="manufacturerString",
        title="Name of device manufacturer",
        description="A name of the manufacturer.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e manufacturer[x]
            "one_of_many": "manufacturer",
            "one_of_many_required": False,
        },
    )
    manufacturerString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_manufacturerString",
        title="Extension field for ``manufacturerString``.",
    )

    material: typing.List[fhirtypes.DeviceDefinitionMaterialType] | None = Field(  # type: ignore
        None,
        alias="material",
        title="A substance used to create the material(s) of which the device is made",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    modelNumber: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="modelNumber",
        title="The model number for the device",
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

    onlineInformation: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="onlineInformation",
        title="Access to on-line information",
        description="Access to on-line information about the device.",
        json_schema_extra={
            "element_property": True,
        },
    )
    onlineInformation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_onlineInformation",
        title="Extension field for ``onlineInformation``.",
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

    parentDevice: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="parentDevice",
        title="The parent device it can be part of",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DeviceDefinition"],
        },
    )

    physicalCharacteristics: fhirtypes.ProdCharacteristicType | None = Field(  # type: ignore
        None,
        alias="physicalCharacteristics",
        title="Dimensions, color etc.",
        description="Dimensions, color etc.",
        json_schema_extra={
            "element_property": True,
        },
    )

    property: typing.List[fhirtypes.DeviceDefinitionPropertyType] | None = Field(  # type: ignore
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

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title=(
            "The quantity of the device present in the packaging (e.g. the number "
            "of devices present in a pack, or the number of devices in the same "
            "package of the medicinal product)"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    safety: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="safety",
        title="Safety characteristics of the device",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    shelfLifeStorage: typing.List[fhirtypes.ProductShelfLifeType] | None = Field(  # type: ignore
        None,
        alias="shelfLifeStorage",
        title="Shelf Life and storage information",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    specialization: typing.List[fhirtypes.DeviceDefinitionSpecializationType] | None = Field(  # type: ignore
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

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="What kind of device or device system this is",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    udiDeviceIdentifier: typing.List[fhirtypes.DeviceDefinitionUdiDeviceIdentifierType] | None = Field(  # type: ignore
        None,
        alias="udiDeviceIdentifier",
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

    version: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="version",
        title="Available versions",
        description="The available versions of the device, e.g., software versions.",
        json_schema_extra={
            "element_property": True,
        },
    )
    version__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_version", title="Extension field for ``version``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceDefinition`` according specification,
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
            "udiDeviceIdentifier",
            "manufacturerString",
            "manufacturerReference",
            "deviceName",
            "modelNumber",
            "type",
            "specialization",
            "version",
            "safety",
            "shelfLifeStorage",
            "physicalCharacteristics",
            "languageCode",
            "capability",
            "property",
            "owner",
            "contact",
            "url",
            "onlineInformation",
            "note",
            "quantity",
            "parentDevice",
            "material",
        ]

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
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
        return one_of_many_fields


class DeviceDefinitionCapability(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Device capabilities.
    """

    __resource_type__ = "DeviceDefinitionCapability"

    description: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="description",
        title="Description of capability",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Type of capability",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceDefinitionCapability`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "description"]


class DeviceDefinitionDeviceName(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A name given to the device to identify it.
    """

    __resource_type__ = "DeviceDefinitionDeviceName"

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="The name of the device",
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
        ``DeviceDefinitionDeviceName`` according specification,
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


class DeviceDefinitionMaterial(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A substance used to create the material(s) of which the device is made.
    """

    __resource_type__ = "DeviceDefinitionMaterial"

    allergenicIndicator: bool | None = Field(  # type: ignore
        None,
        alias="allergenicIndicator",
        title="Whether the substance is a known or suspected allergen",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    allergenicIndicator__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_allergenicIndicator",
        title="Extension field for ``allergenicIndicator``.",
    )

    alternate: bool | None = Field(  # type: ignore
        None,
        alias="alternate",
        title="Indicates an alternative material of the device",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    alternate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_alternate", title="Extension field for ``alternate``."
    )

    substance: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="substance",
        title="The substance",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceDefinitionMaterial`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "substance",
            "alternate",
            "allergenicIndicator",
        ]


class DeviceDefinitionProperty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The actual configuration settings of a device as it actually operates,
    e.g., regulation status, time properties.
    """

    __resource_type__ = "DeviceDefinitionProperty"

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
        ``DeviceDefinitionProperty`` according specification,
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


class DeviceDefinitionSpecialization(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The capabilities supported on a  device, the standards to which the device
    conforms for a particular purpose, and used for the communication.
    """

    __resource_type__ = "DeviceDefinitionSpecialization"

    systemType: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="systemType",
        title="The standard that is used to operate and communicate",
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    systemType__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_systemType", title="Extension field for ``systemType``."
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
        ``DeviceDefinitionSpecialization`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "systemType", "version"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("systemType", "systemType__ext")]
        return required_fields


class DeviceDefinitionUdiDeviceIdentifier(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Unique Device Identifier (UDI) Barcode string.
    Unique device identifier (UDI) assigned to device label or package.  Note
    that the Device may include multiple udiCarriers as it either may include
    just the udiCarrier for the jurisdiction it is sold, or for multiple
    jurisdictions it could have been sold.
    """

    __resource_type__ = "DeviceDefinitionUdiDeviceIdentifier"

    deviceIdentifier: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="deviceIdentifier",
        title=(
            "The identifier that is to be associated with every Device that "
            "references this DeviceDefintiion for the issuer and jurisdication "
            "porvided in the DeviceDefinition.udiDeviceIdentifier"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    deviceIdentifier__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_deviceIdentifier",
        title="Extension field for ``deviceIdentifier``.",
    )

    issuer: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="issuer",
        title="The organization that assigns the identifier algorithm",
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    issuer__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_issuer", title="Extension field for ``issuer``."
    )

    jurisdiction: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="jurisdiction",
        title="The jurisdiction to which the deviceIdentifier applies",
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    jurisdiction__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_jurisdiction", title="Extension field for ``jurisdiction``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceDefinitionUdiDeviceIdentifier`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "deviceIdentifier",
            "issuer",
            "jurisdiction",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("deviceIdentifier", "deviceIdentifier__ext"),
            ("issuer", "issuer__ext"),
            ("jurisdiction", "jurisdiction__ext"),
        ]
        return required_fields
