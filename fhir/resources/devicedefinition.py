from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceDefinition
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
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

    chargeItem: typing.List[fhirtypes.DeviceDefinitionChargeItemType] | None = Field(  # type: ignore
        None,
        alias="chargeItem",
        title="Billing code or reference associated with the device",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    classification: typing.List[fhirtypes.DeviceDefinitionClassificationType] | None = Field(  # type: ignore
        None,
        alias="classification",
        title="What kind of device or device system this is",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    conformsTo: typing.List[fhirtypes.DeviceDefinitionConformsToType] | None = Field(  # type: ignore
        None,
        alias="conformsTo",
        title=(
            "Identifies the standards, specifications, or formal guidances for the "
            "capabilities supported by the device"
        ),
        description=(
            "Identifies the standards, specifications, or formal guidances for the "
            "capabilities supported by the device. The device may be certified as "
            "conformant to these specifications e.g., communication, performance, "
            "process, measurement, or specialization standards."
        ),
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

    correctiveAction: fhirtypes.DeviceDefinitionCorrectiveActionType | None = Field(  # type: ignore
        None,
        alias="correctiveAction",
        title="Tracking of latest field safety corrective action",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Additional information to describe the device",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    deviceName: typing.List[fhirtypes.DeviceDefinitionDeviceNameType] | None = Field(  # type: ignore
        None,
        alias="deviceName",
        title="The name or names of the device as given by the manufacturer",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    guideline: fhirtypes.DeviceDefinitionGuidelineType | None = Field(  # type: ignore
        None,
        alias="guideline",
        title=(
            "Information aimed at providing directions for the usage of this model "
            "of device"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    hasPart: typing.List[fhirtypes.DeviceDefinitionHasPartType] | None = Field(  # type: ignore
        None,
        alias="hasPart",
        title="A device, part of the current one",
        description="A device that is part (for example a component) of the present device.",
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
            "manufacturers, other organizations or owners. For example: handle ID. "
            "The identifier is typically valued if the udiDeviceIdentifier, "
            "partNumber or modelNumber is not valued and represents a different "
            "type of identifier.  However, it is permissible to still include those"
            " identifiers in DeviceDefinition.identifier with the appropriate "
            "identifier.type."
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

    link: typing.List[fhirtypes.DeviceDefinitionLinkType] | None = Field(  # type: ignore
        None,
        alias="link",
        title=(
            "An associated device, attached to, used with, communicating with or "
            "linking a previous or new device model to the focal device"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    manufacturer: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="manufacturer",
        title="Name of device manufacturer",
        description=(
            "A name of the manufacturer  or legal representative e.g. labeler. "
            "Whether this is the actual manufacturer or the labeler or responsible "
            "depends on implementation and jurisdiction."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
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
        title=(
            "The catalog or model number for the device for example as defined by "
            "the manufacturer"
        ),
        description=(
            "The model number for the device for example as defined by the "
            "manufacturer or labeler, or other agency."
        ),
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

    packaging: typing.List[fhirtypes.DeviceDefinitionPackagingType] | None = Field(  # type: ignore
        None,
        alias="packaging",
        title=(
            "Information about the packaging of the device, i.e. how the device is "
            "packaged"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
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

    productionIdentifierInUDI: typing.List[fhirtypes.CodeType | None] | None = Field(  # type: ignore
        None,
        alias="productionIdentifierInUDI",
        title=(
            "lot-number | manufactured-date | serial-number | expiration-date | "
            "biological-source | software-version"
        ),
        description=(
            "Indicates the production identifier(s) that are expected to appear in "
            "the UDI carrier on the device label."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "lot-number",
                "manufactured-date",
                "serial-number",
                "expiration-date",
                "biological-source",
                "software-version",
            ],
        },
    )
    productionIdentifierInUDI__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_productionIdentifierInUDI",
        title="Extension field for ``productionIdentifierInUDI``.",
    )

    property: typing.List[fhirtypes.DeviceDefinitionPropertyType] | None = Field(  # type: ignore
        None,
        alias="property",
        title=(
            "Inherent, essentially fixed, characteristics of this kind of device, "
            "e.g., time properties, size, etc"
        ),
        description=(
            "Static or essentially fixed characteristics or features of this kind "
            "of device that are otherwise not captured in more specific attributes,"
            " e.g., time or timing attributes, resolution, accuracy, and physical "
            "attributes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    regulatoryIdentifier: typing.List[fhirtypes.DeviceDefinitionRegulatoryIdentifierType] | None = Field(  # type: ignore
        None,
        alias="regulatoryIdentifier",
        title="Regulatory identifier(s) associated with this device",
        description=(
            "Identifier associated with the regulatory documentation (certificates,"
            " technical documentation, post-market surveillance documentation and "
            "reports) of a set of device models sharing the same intended purpose, "
            "risk class and essential design and manufacturing characteristics. One"
            " example is the Basic UDI-DI in Europe."
        ),
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

    version: typing.List[fhirtypes.DeviceDefinitionVersionType] | None = Field(  # type: ignore
        None,
        alias="version",
        title="The version of the device or software",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
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
            "description",
            "identifier",
            "udiDeviceIdentifier",
            "regulatoryIdentifier",
            "partNumber",
            "manufacturer",
            "deviceName",
            "modelNumber",
            "classification",
            "conformsTo",
            "hasPart",
            "packaging",
            "version",
            "safety",
            "shelfLifeStorage",
            "languageCode",
            "property",
            "owner",
            "contact",
            "link",
            "note",
            "material",
            "productionIdentifierInUDI",
            "guideline",
            "correctiveAction",
            "chargeItem",
        ]


class DeviceDefinitionChargeItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Billing code or reference associated with the device.
    """

    __resource_type__ = "DeviceDefinitionChargeItem"

    chargeItemCode: fhirtypes.CodeableReferenceType = Field(  # type: ignore
        ...,
        alias="chargeItemCode",
        title="The code or reference for the charge item",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ChargeItemDefinition"],
        },
    )

    count: fhirtypes.QuantityType = Field(  # type: ignore
        ...,
        alias="count",
        title="Coefficient applicable to the billing code",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    effectivePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="effectivePeriod",
        title="A specific time period in which this charge item applies",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    useContext: typing.List[fhirtypes.UsageContextType] | None = Field(  # type: ignore
        None,
        alias="useContext",
        title="The context to which this charge item applies",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceDefinitionChargeItem`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "chargeItemCode",
            "count",
            "effectivePeriod",
            "useContext",
        ]


class DeviceDefinitionClassification(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What kind of device or device system this is.
    """

    __resource_type__ = "DeviceDefinitionClassification"

    justification: typing.List[fhirtypes.RelatedArtifactType] | None = Field(  # type: ignore
        None,
        alias="justification",
        title="Further information qualifying this classification of the device model",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="A classification or risk class of the device model",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceDefinitionClassification`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "justification"]


class DeviceDefinitionConformsTo(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Identifies the standards, specifications, or formal guidances for the
    capabilities supported by the device.
    Identifies the standards, specifications, or formal guidances for the
    capabilities supported by the device. The device may be certified as
    conformant to these specifications e.g., communication, performance,
    process, measurement, or specialization standards.
    """

    __resource_type__ = "DeviceDefinitionConformsTo"

    category: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="category",
        title=(
            "Describes the common type of the standard, specification, or formal "
            "guidance"
        ),
        description="Describes the type of the standard, specification, or formal guidance.",
        json_schema_extra={
            "element_property": True,
        },
    )

    source: typing.List[fhirtypes.RelatedArtifactType] | None = Field(  # type: ignore
        None,
        alias="source",
        title=(
            "Standard, regulation, certification, or guidance website, document, or"
            " other publication, or similar, supporting the conformance"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    specification: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="specification",
        title=(
            "Identifies the standard, specification, or formal guidance that the "
            "device adheres to the Device Specification type"
        ),
        description=(
            "Code that identifies the specific standard, specification, protocol, "
            "formal guidance, regulation, legislation, or certification scheme to "
            "which the device adheres."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    version: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="version",
        title=(
            "The specific form or variant of the standard, specification or formal "
            "guidance"
        ),
        description=(
            "Identifies the specific form or variant of the standard, "
            "specification, or formal guidance. This may be a 'version number', "
            "release, document edition, publication year, or other label."
        ),
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
        ``DeviceDefinitionConformsTo`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "category",
            "specification",
            "version",
            "source",
        ]


class DeviceDefinitionCorrectiveAction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Tracking of latest field safety corrective action.
    """

    __resource_type__ = "DeviceDefinitionCorrectiveAction"

    period: fhirtypes.PeriodType = Field(  # type: ignore
        ...,
        alias="period",
        title="Start and end dates of the  corrective action",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    recall: bool | None = Field(  # type: ignore
        None,
        alias="recall",
        title="Whether the corrective action was a recall",
        description="Whether the last corrective action known for this device was a recall.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    recall__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_recall", title="Extension field for ``recall``."
    )

    scope: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="scope",
        title="model | lot-numbers | serial-numbers",
        description=(
            "The scope of the corrective action - whether the action targeted all "
            "units of a given device model, or only a specific set of batches "
            "identified by lot numbers, or individually identified devices "
            "identified by the serial name."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["model", "lot-numbers", "serial-numbers"],
        },
    )
    scope__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_scope", title="Extension field for ``scope``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceDefinitionCorrectiveAction`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "recall", "scope", "period"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("recall", "recall__ext")]
        return required_fields


class DeviceDefinitionDeviceName(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The name or names of the device as given by the manufacturer.
    """

    __resource_type__ = "DeviceDefinitionDeviceName"

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="A name that is used to refer to the device",
        description=(
            "A human-friendly name that is used to refer to the device - depending "
            "on the type, it can be the brand name, the common name or alias, or "
            "other."
        ),
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
        title="registered-name | user-friendly-name | patient-reported-name",
        description=(
            "The type of deviceName. RegisteredName | UserFriendlyName | "
            "PatientReportedName."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "registered-name",
                "user-friendly-name",
                "patient-reported-name",
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


class DeviceDefinitionGuideline(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information aimed at providing directions for the usage of this model of
    device.
    """

    __resource_type__ = "DeviceDefinitionGuideline"

    contraindication: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="contraindication",
        title=(
            "A specific situation when a device should not be used because it may "
            "cause harm"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    indication: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="indication",
        title="A clinical condition for which the device was designed to be used",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    intendedUse: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="intendedUse",
        title=(
            "A description of the general purpose or medical use of the device or "
            "its function"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    intendedUse__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_intendedUse", title="Extension field for ``intendedUse``."
    )

    relatedArtifact: typing.List[fhirtypes.RelatedArtifactType] | None = Field(  # type: ignore
        None,
        alias="relatedArtifact",
        title="A source of information or reference for this guideline",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    usageInstruction: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="usageInstruction",
        title=(
            "Detailed written and visual directions for the user on how to use the "
            "device"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    usageInstruction__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_usageInstruction",
        title="Extension field for ``usageInstruction``.",
    )

    useContext: typing.List[fhirtypes.UsageContextType] | None = Field(  # type: ignore
        None,
        alias="useContext",
        title="The circumstances that form the setting for using the device",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    warning: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="warning",
        title=(
            "Specific hazard alert information that a user needs to know before "
            "using the device"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceDefinitionGuideline`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "useContext",
            "usageInstruction",
            "relatedArtifact",
            "indication",
            "contraindication",
            "warning",
            "intendedUse",
        ]


class DeviceDefinitionHasPart(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A device, part of the current one.
    A device that is part (for example a component) of the present device.
    """

    __resource_type__ = "DeviceDefinitionHasPart"

    count: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="count",
        title="Number of occurrences of the part",
        description="Number of instances of the component device in the current device.",
        json_schema_extra={
            "element_property": True,
        },
    )
    count__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_count", title="Extension field for ``count``."
    )

    reference: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="reference",
        title="Reference to the part",
        description="Reference to the device that is part of the current device.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DeviceDefinition"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceDefinitionHasPart`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "reference", "count"]


class DeviceDefinitionLink(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An associated device, attached to, used with, communicating with or linking
    a previous or new device model to the focal device.
    """

    __resource_type__ = "DeviceDefinitionLink"

    relatedDevice: fhirtypes.CodeableReferenceType = Field(  # type: ignore
        ...,
        alias="relatedDevice",
        title="A reference to the linked device",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DeviceDefinition"],
        },
    )

    relation: fhirtypes.CodingType = Field(  # type: ignore
        ...,
        alias="relation",
        title=(
            "The type indicates the relationship of the related device to the "
            "device instance"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceDefinitionLink`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "relation", "relatedDevice"]


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
        title=(
            "A relevant substance that the device contains, may contain, or is made"
            " of"
        ),
        description=(
            "A substance that the device contains, may contain, or is made of - for"
            " example latex - to be used to determine patient compatibility. This "
            "is not intended to represent the composition of the device, only the "
            "clinically relevant materials."
        ),
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


class DeviceDefinitionPackaging(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about the packaging of the device, i.e. how the device is
    packaged.
    """

    __resource_type__ = "DeviceDefinitionPackaging"

    count: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="count",
        title="The number of items contained in the package (devices or sub-packages)",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    count__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_count", title="Extension field for ``count``."
    )

    distributor: typing.List[fhirtypes.DeviceDefinitionPackagingDistributorType] | None = Field(  # type: ignore
        None,
        alias="distributor",
        title="An organization that distributes the packaged device",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business identifier of the packaged medication",
        description="The business identifier of the packaged medication.",
        json_schema_extra={
            "element_property": True,
        },
    )

    packaging: typing.List[fhirtypes.DeviceDefinitionPackagingType] | None = Field(  # type: ignore
        None,
        alias="packaging",
        title="Allows packages within packages",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="A code that defines the specific type of packaging",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    udiDeviceIdentifier: typing.List[fhirtypes.DeviceDefinitionUdiDeviceIdentifierType] | None = Field(  # type: ignore
        None,
        alias="udiDeviceIdentifier",
        title="Unique Device Identifier (UDI) Barcode string on the packaging",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceDefinitionPackaging`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "identifier",
            "type",
            "count",
            "distributor",
            "udiDeviceIdentifier",
            "packaging",
        ]


class DeviceDefinitionPackagingDistributor(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An organization that distributes the packaged device.
    """

    __resource_type__ = "DeviceDefinitionPackagingDistributor"

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Distributor's human-readable name",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    organizationReference: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="organizationReference",
        title="Distributor as an Organization resource",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceDefinitionPackagingDistributor`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "name", "organizationReference"]


class DeviceDefinitionProperty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Inherent, essentially fixed, characteristics of this kind of device, e.g.,
    time properties, size, etc.
    Static or essentially fixed characteristics or features of this kind of
    device that are otherwise not captured in more specific attributes, e.g.,
    time or timing attributes, resolution, accuracy, and physical attributes.
    """

    __resource_type__ = "DeviceDefinitionProperty"

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Code that specifies the property being represented",
        description=(
            "Code that specifies the property such as a resolution or color being "
            "represented."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    valueAttachment: fhirtypes.AttachmentType | None = Field(  # type: ignore
        None,
        alias="valueAttachment",
        title="Value of the property",
        description=(
            "The value of the property specified by the associated property.type "
            "code."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueBoolean: bool | None = Field(  # type: ignore
        None,
        alias="valueBoolean",
        title="Value of the property",
        description=(
            "The value of the property specified by the associated property.type "
            "code."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="valueCodeableConcept",
        title="Value of the property",
        description=(
            "The value of the property specified by the associated property.type "
            "code."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueInteger: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="valueInteger",
        title="Value of the property",
        description=(
            "The value of the property specified by the associated property.type "
            "code."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueInteger", title="Extension field for ``valueInteger``."
    )

    valueQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="valueQuantity",
        title="Value of the property",
        description=(
            "The value of the property specified by the associated property.type "
            "code."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueRange: fhirtypes.RangeType | None = Field(  # type: ignore
        None,
        alias="valueRange",
        title="Value of the property",
        description=(
            "The value of the property specified by the associated property.type "
            "code."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="valueString",
        title="Value of the property",
        description=(
            "The value of the property specified by the associated property.type "
            "code."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueString", title="Extension field for ``valueString``."
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
            "valueCodeableConcept",
            "valueString",
            "valueBoolean",
            "valueInteger",
            "valueRange",
            "valueAttachment",
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
            "value": [
                "valueAttachment",
                "valueBoolean",
                "valueCodeableConcept",
                "valueInteger",
                "valueQuantity",
                "valueRange",
                "valueString",
            ]
        }
        return one_of_many_fields


class DeviceDefinitionRegulatoryIdentifier(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Regulatory identifier(s) associated with this device.
    Identifier associated with the regulatory documentation (certificates,
    technical documentation, post-market surveillance documentation and
    reports) of a set of device models sharing the same intended purpose, risk
    class and essential design and manufacturing characteristics. One example
    is the Basic UDI-DI in Europe.
    """

    __resource_type__ = "DeviceDefinitionRegulatoryIdentifier"

    deviceIdentifier: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="deviceIdentifier",
        title="The identifier itself",
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
        title="The organization that issued this identifier",
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

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="basic | master | license",
        description="The type of identifier itself.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["basic", "master", "license"],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceDefinitionRegulatoryIdentifier`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
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
            ("type", "type__ext"),
        ]
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
            "references this DeviceDefintiion for the issuer and jurisdiction "
            "provided in the DeviceDefinition.udiDeviceIdentifier"
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

    marketDistribution: typing.List[fhirtypes.DeviceDefinitionUdiDeviceIdentifierMarketDistributionType] | None = Field(  # type: ignore
        None,
        alias="marketDistribution",
        title="Indicates whether and when the device is available on the market",
        description="Indicates where and when the device is available on the market.",
        json_schema_extra={
            "element_property": True,
        },
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
            "marketDistribution",
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


class DeviceDefinitionUdiDeviceIdentifierMarketDistribution(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Indicates whether and when the device is available on the market.
    Indicates where and when the device is available on the market.
    """

    __resource_type__ = "DeviceDefinitionUdiDeviceIdentifierMarketDistribution"

    marketPeriod: fhirtypes.PeriodType = Field(  # type: ignore
        ...,
        alias="marketPeriod",
        title="Begin and end dates for the commercial distribution of the device",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    subJurisdiction: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="subJurisdiction",
        title="National state or territory where the device is commercialized",
        description=(
            "National state or territory to which the marketDistribution recers, "
            "typically where the device is commercialized."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    subJurisdiction__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_subJurisdiction", title="Extension field for ``subJurisdiction``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceDefinitionUdiDeviceIdentifierMarketDistribution`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "marketPeriod",
            "subJurisdiction",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("subJurisdiction", "subJurisdiction__ext")]
        return required_fields


class DeviceDefinitionVersion(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The version of the device or software.
    """

    __resource_type__ = "DeviceDefinitionVersion"

    component: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="component",
        title=(
            "The hardware or software module of the device to which the version "
            "applies"
        ),
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
        ``DeviceDefinitionVersion`` according specification,
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
