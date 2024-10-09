from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Device
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
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

    availabilityStatus: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="availabilityStatus",
        title="lost | damaged | destroyed | available",
        description="The availability of the device.",
        json_schema_extra={
            "element_property": True,
        },
    )

    biologicalSourceEvent: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="biologicalSourceEvent",
        title=(
            "An identifier that supports traceability to the event during which "
            "material in this product from one or more biological entities was "
            "obtained or pooled"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    category: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="category",
        title="Indicates a high-level grouping of the device",
        description="Devices may be associated with one or more categories.",
        json_schema_extra={
            "element_property": True,
        },
    )

    conformsTo: typing.List[fhirtypes.DeviceConformsToType] | None = Field(  # type: ignore
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

    cycle: fhirtypes.CountType | None = Field(  # type: ignore
        None,
        alias="cycle",
        title=(
            "The series of occurrences that repeats during the operation of the "
            "device"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    definition: fhirtypes.CodeableReferenceType | None = Field(  # type: ignore
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

    displayName: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="displayName",
        title="The name used to display by default when the device is referenced",
        description=(
            "The name used to display by default when the device is referenced. "
            "Based on intent of use by the resource creator, this may reflect one "
            "of the names in Device.name, or may be another simple name."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    displayName__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_displayName", title="Extension field for ``displayName``."
    )

    duration: fhirtypes.DurationType | None = Field(  # type: ignore
        None,
        alias="duration",
        title=(
            "A measurement of time during the device's operation (e.g., days, "
            "hours, mins, etc.)"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    endpoint: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="endpoint",
        title=(
            "Technical endpoints providing access to electronic services provided "
            "by the device"
        ),
        description=(
            "Technical endpoints providing access to services provided by the "
            "device defined at this resource."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Endpoint"],
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

    gateway: typing.List[fhirtypes.CodeableReferenceType] | None = Field(  # type: ignore
        None,
        alias="gateway",
        title=(
            "Linked device acting as a communication/data collector, translator or "
            "controller"
        ),
        description=(
            "The linked device acting as a communication controller, data "
            "collector, translator, or concentrator for the current device (e.g., "
            "mobile phone application that relays a blood pressure device's data)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Device"],
        },
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
        description=(
            "A name of the manufacturer or entity legally responsible for the "
            "device."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    manufacturer__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_manufacturer", title="Extension field for ``manufacturer``."
    )

    mode: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="mode",
        title="The designated condition for performing a task",
        description="The designated condition for performing a task with the device.",
        json_schema_extra={
            "element_property": True,
        },
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

    name: typing.List[fhirtypes.DeviceNameType] | None = Field(  # type: ignore
        None,
        alias="name",
        title=(
            "The name or names of the device as known to the manufacturer and/or "
            "patient"
        ),
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
        title=(
            "The higher level or encompassing device that this device is a logical "
            "part of"
        ),
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

    property: typing.List[fhirtypes.DevicePropertyType] | None = Field(  # type: ignore
        None,
        alias="property",
        title=(
            "Inherent, essentially fixed, characteristics of the device.  e.g., "
            "time properties, size, material, etc."
        ),
        description=(
            "Static or essentially fixed characteristics or features of the device "
            "(e.g., time or timing attributes, resolution, accuracy, intended use "
            "or instructions for use, and physical attributes) that are not "
            "otherwise captured in more specific attributes."
        ),
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

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="active | inactive | entered-in-error",
        description=(
            "The Device record status. This is not the status of the device like "
            "availability."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["active", "inactive", "entered-in-error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    type: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="type",
        title="The kind or type of device",
        description=(
            "The kind or type of device. A device instance may have more than one "
            "type - in which case those are the types that apply to the specific "
            "instance of the device."
        ),
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
            "displayName",
            "definition",
            "udiCarrier",
            "status",
            "availabilityStatus",
            "biologicalSourceEvent",
            "manufacturer",
            "manufactureDate",
            "expirationDate",
            "lotNumber",
            "serialNumber",
            "name",
            "modelNumber",
            "partNumber",
            "category",
            "type",
            "version",
            "conformsTo",
            "property",
            "mode",
            "cycle",
            "duration",
            "owner",
            "contact",
            "location",
            "url",
            "endpoint",
            "gateway",
            "note",
            "safety",
            "parent",
        ]


class DeviceConformsTo(backboneelement.BackboneElement):
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

    __resource_type__ = "DeviceConformsTo"

    category: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="category",
        title=(
            "Describes the common type of the standard, specification, or formal "
            "guidance.  communication | performance | measurement"
        ),
        description="Describes the type of the standard, specification, or formal guidance.",
        json_schema_extra={
            "element_property": True,
        },
    )

    specification: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="specification",
        title=(
            "Identifies the standard, specification, or formal guidance that the "
            "device adheres to"
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

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="Specific form or variant of the standard",
        description=(
            "Identifies the specific form or variant of the standard, "
            "specification, or formal guidance. This may be a 'version number', "
            "release, document edition, publication year, or other label."
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
        ``DeviceConformsTo`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "category",
            "specification",
            "version",
        ]


class DeviceName(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The name or names of the device as known to the manufacturer and/or patient.
    This represents the manufacturer's name of the device as provided by the
    device, from a UDI label, or by a person describing the Device.  This
    typically would be used when a person provides the name(s) or when the
    device represents one of the names available from DeviceDefinition.
    """

    __resource_type__ = "DeviceName"

    display: bool | None = Field(  # type: ignore
        None,
        alias="display",
        title="The preferred device name",
        description="Indicates the default or preferred name to be displayed.",
        json_schema_extra={
            "element_property": True,
        },
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_display", title="Extension field for ``display``."
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="registered-name | user-friendly-name | patient-reported-name",
        description=(
            "Indicates the kind of name. RegisteredName | UserFriendlyName | "
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

    value: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="value",
        title="The term that names the device",
        description="The actual name that identifies the device.",
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
        ``DeviceName`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "value", "type", "display"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("type", "type__ext"), ("value", "value__ext")]
        return required_fields


class DeviceProperty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Inherent, essentially fixed, characteristics of the device.  e.g., time
    properties, size, material, etc..
    Static or essentially fixed characteristics or features of the device
    (e.g., time or timing attributes, resolution, accuracy, intended use or
    instructions for use, and physical attributes) that are not otherwise
    captured in more specific attributes.
    """

    __resource_type__ = "DeviceProperty"

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Code that specifies the property being represented",
        description=(
            "Code that specifies the property, such as resolution, color, size, "
            "being represented."
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
        ``DeviceProperty`` according specification,
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
            "element_required": True,
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
        title=(
            "barcode | rfid | manual | card | self-reported | electronic-"
            "transmission | unknown"
        ),
        description="A coded entry to indicate how the data was entered.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "barcode",
                "rfid",
                "manual",
                "card",
                "self-reported",
                "electronic-transmission",
                "unknown",
            ],
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
            "Organization that is charged with issuing UDIs for devices. For "
            "example, the US FDA issuers include:  1) GS1: "
            "http://hl7.org/fhir/NamingSystem/gs1-di,  2) HIBCC: "
            "http://hl7.org/fhir/NamingSystem/hibcc-diI,  3) ICCBBA for blood "
            "containers: http://hl7.org/fhir/NamingSystem/iccbba-blood-di,  4) "
            "ICCBA for other devices: http://hl7.org/fhir/NamingSystem/iccbba-"
            "other-di # Informationsstelle f\u00fcr Arzneispezialit\u00e4ten (IFA GmbH) (EU "
            "only): http://hl7.org/fhir/NamingSystem/ifa-gmbh-di."
        ),
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
        title="Regional UDI authority",
        description=(
            "The identity of the authoritative source for UDI generation within a "
            "jurisdiction. All UDIs are globally unique within a single namespace "
            "with the appropriate repository uri as the system. For example, UDIs "
            "of devices managed in the U.S. by the FDA, the value is "
            "http://hl7.org/fhir/NamingSystem/us-fda-udi or in the European Union "
            "by the European Commission http://hl7.org/fhir/NamingSystem/eu-ec-udi."
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
        ]
        return required_fields


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
        title=(
            "The hardware or software module of the device to which the version "
            "applies"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    installDate: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="installDate",
        title="The date the version was installed on the device",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    installDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_installDate", title="Extension field for ``installDate``."
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
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "component",
            "installDate",
            "value",
        ]

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
