# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceDefinition
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class DeviceDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An instance of a medical-related component of a medical device.
    The characteristics, operational status and capabilities of a medical-
    related component of a medical device.
    """

    resource_type = Field("DeviceDefinition", const=True)

    chargeItem: typing.List[fhirtypes.DeviceDefinitionChargeItemType] = Field(
        None,
        alias="chargeItem",
        title="Billing code or reference associated with the device",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    classification: typing.List[fhirtypes.DeviceDefinitionClassificationType] = Field(
        None,
        alias="classification",
        title="What kind of device or device system this is",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    conformsTo: typing.List[fhirtypes.DeviceDefinitionConformsToType] = Field(
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
        # if property is element of this resource.
        element_property=True,
    )

    contact: typing.List[fhirtypes.ContactPointType] = Field(
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

    correctiveAction: fhirtypes.DeviceDefinitionCorrectiveActionType = Field(
        None,
        alias="correctiveAction",
        title="Tracking of latest field safety corrective action",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Additional information to describe the device",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    deviceName: typing.List[fhirtypes.DeviceDefinitionDeviceNameType] = Field(
        None,
        alias="deviceName",
        title="The name or names of the device as given by the manufacturer",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    guideline: fhirtypes.DeviceDefinitionGuidelineType = Field(
        None,
        alias="guideline",
        title=(
            "Information aimed at providing directions for the usage of this model "
            "of device"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    hasPart: typing.List[fhirtypes.DeviceDefinitionHasPartType] = Field(
        None,
        alias="hasPart",
        title="A device, part of the current one",
        description="A device that is part (for example a component) of the present device.",
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
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
        # if property is element of this resource.
        element_property=True,
    )

    languageCode: typing.List[fhirtypes.CodeableConceptType] = Field(
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

    link: typing.List[fhirtypes.DeviceDefinitionLinkType] = Field(
        None,
        alias="link",
        title=(
            "An associated device, attached to, used with, communicating with or "
            "linking a previous or new device model to the focal device"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    manufacturer: fhirtypes.ReferenceType = Field(
        None,
        alias="manufacturer",
        title="Name of device manufacturer",
        description=(
            "A name of the manufacturer  or legal representative e.g. labeler. "
            "Whether this is the actual manufacturer or the labeler or responsible "
            "depends on implementation and jurisdiction."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    material: typing.List[fhirtypes.DeviceDefinitionMaterialType] = Field(
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
        title=(
            "The catalog or model number for the device for example as defined by "
            "the manufacturer"
        ),
        description=(
            "The model number for the device for example as defined by the "
            "manufacturer or labeler, or other agency."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    modelNumber__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_modelNumber", title="Extension field for ``modelNumber``."
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
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

    packaging: typing.List[fhirtypes.DeviceDefinitionPackagingType] = Field(
        None,
        alias="packaging",
        title=(
            "Information about the packaging of the device, i.e. how the device is "
            "packaged"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    partNumber: fhirtypes.String = Field(
        None,
        alias="partNumber",
        title="The part number or catalog number of the device",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    partNumber__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_partNumber", title="Extension field for ``partNumber``."
    )

    productionIdentifierInUDI: typing.List[typing.Optional[fhirtypes.Code]] = Field(
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
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "lot-number",
            "manufactured-date",
            "serial-number",
            "expiration-date",
            "biological-source",
            "software-version",
        ],
    )
    productionIdentifierInUDI__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_productionIdentifierInUDI",
        title="Extension field for ``productionIdentifierInUDI``.",
    )

    property: typing.List[fhirtypes.DeviceDefinitionPropertyType] = Field(
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
        # if property is element of this resource.
        element_property=True,
    )

    regulatoryIdentifier: typing.List[
        fhirtypes.DeviceDefinitionRegulatoryIdentifierType
    ] = Field(
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
        # if property is element of this resource.
        element_property=True,
    )

    safety: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="safety",
        title="Safety characteristics of the device",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    shelfLifeStorage: typing.List[fhirtypes.ProductShelfLifeType] = Field(
        None,
        alias="shelfLifeStorage",
        title="Shelf Life and storage information",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    udiDeviceIdentifier: typing.List[
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

    version: typing.List[fhirtypes.DeviceDefinitionVersionType] = Field(
        None,
        alias="version",
        title="The version of the device or software",
        description=None,
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("DeviceDefinitionChargeItem", const=True)

    chargeItemCode: fhirtypes.CodeableReferenceType = Field(
        ...,
        alias="chargeItemCode",
        title="The code or reference for the charge item",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ChargeItemDefinition"],
    )

    count: fhirtypes.QuantityType = Field(
        ...,
        alias="count",
        title="Coefficient applicable to the billing code",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="A specific time period in which this charge item applies",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    useContext: typing.List[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="The context to which this charge item applies",
        description=None,
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("DeviceDefinitionClassification", const=True)

    justification: typing.List[fhirtypes.RelatedArtifactType] = Field(
        None,
        alias="justification",
        title="Further information qualifying this classification of the device model",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="A classification or risk class of the device model",
        description=None,
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("DeviceDefinitionConformsTo", const=True)

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title=(
            "Describes the common type of the standard, specification, or formal "
            "guidance"
        ),
        description="Describes the type of the standard, specification, or formal guidance.",
        # if property is element of this resource.
        element_property=True,
    )

    source: typing.List[fhirtypes.RelatedArtifactType] = Field(
        None,
        alias="source",
        title=(
            "Standard, regulation, certification, or guidance website, document, or"
            " other publication, or similar, supporting the conformance"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    specification: fhirtypes.CodeableConceptType = Field(
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
        # if property is element of this resource.
        element_property=True,
    )

    version: typing.List[typing.Optional[fhirtypes.String]] = Field(
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
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_version", title="Extension field for ``version``.")

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

    resource_type = Field("DeviceDefinitionCorrectiveAction", const=True)

    period: fhirtypes.PeriodType = Field(
        ...,
        alias="period",
        title="Start and end dates of the  corrective action",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    recall: bool = Field(
        None,
        alias="recall",
        title="Whether the corrective action was a recall",
        description="Whether the last corrective action known for this device was a recall.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    recall__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_recall", title="Extension field for ``recall``."
    )

    scope: fhirtypes.Code = Field(
        None,
        alias="scope",
        title="model | lot-numbers | serial-numbers",
        description=(
            "The scope of the corrective action - whether the action targeted all "
            "units of a given device model, or only a specific set of batches "
            "identified by lot numbers, or individually identified devices "
            "identified by the serial name."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["model", "lot-numbers", "serial-numbers"],
    )
    scope__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_scope", title="Extension field for ``scope``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceDefinitionCorrectiveAction`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "recall", "scope", "period"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3455(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("recall", "recall__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class DeviceDefinitionDeviceName(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The name or names of the device as given by the manufacturer.
    """

    resource_type = Field("DeviceDefinitionDeviceName", const=True)

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="A name that is used to refer to the device",
        description=(
            "A human-friendly name that is used to refer to the device - depending "
            "on the type, it can be the brand name, the common name or alias, or "
            "other."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="registered-name | user-friendly-name | patient-reported-name",
        description=(
            "The type of deviceName. RegisteredName | UserFriendlyName | "
            "PatientReportedName."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["registered-name", "user-friendly-name", "patient-reported-name"],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceDefinitionDeviceName`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "name", "type"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2771(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("name", "name__ext"), ("type", "type__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class DeviceDefinitionGuideline(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information aimed at providing directions for the usage of this model of
    device.
    """

    resource_type = Field("DeviceDefinitionGuideline", const=True)

    contraindication: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="contraindication",
        title=(
            "A specific situation when a device should not be used because it may "
            "cause harm"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    indication: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="indication",
        title="A clinical condition for which the device was designed to be used",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    intendedUse: fhirtypes.String = Field(
        None,
        alias="intendedUse",
        title=(
            "A description of the general purpose or medical use of the device or "
            "its function"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    intendedUse__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_intendedUse", title="Extension field for ``intendedUse``."
    )

    relatedArtifact: typing.List[fhirtypes.RelatedArtifactType] = Field(
        None,
        alias="relatedArtifact",
        title="A source of information or reference for this guideline",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    usageInstruction: fhirtypes.Markdown = Field(
        None,
        alias="usageInstruction",
        title=(
            "Detailed written and visual directions for the user on how to use the "
            "device"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    usageInstruction__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_usageInstruction",
        title="Extension field for ``usageInstruction``.",
    )

    useContext: typing.List[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="The circumstances that form the setting for using the device",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    warning: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="warning",
        title=(
            "Specific hazard alert information that a user needs to know before "
            "using the device"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("DeviceDefinitionHasPart", const=True)

    count: fhirtypes.Integer = Field(
        None,
        alias="count",
        title="Number of occurrences of the part",
        description="Number of instances of the component device in the current device.",
        # if property is element of this resource.
        element_property=True,
    )
    count__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_count", title="Extension field for ``count``."
    )

    reference: fhirtypes.ReferenceType = Field(
        ...,
        alias="reference",
        title="Reference to the part",
        description="Reference to the device that is part of the current device.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DeviceDefinition"],
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

    resource_type = Field("DeviceDefinitionLink", const=True)

    relatedDevice: fhirtypes.CodeableReferenceType = Field(
        ...,
        alias="relatedDevice",
        title="A reference to the linked device",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DeviceDefinition"],
    )

    relation: fhirtypes.CodingType = Field(
        ...,
        alias="relation",
        title=(
            "The type indicates the relationship of the related device to the "
            "device instance"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("DeviceDefinitionPackaging", const=True)

    count: fhirtypes.Integer = Field(
        None,
        alias="count",
        title="The number of items contained in the package (devices or sub-packages)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    count__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_count", title="Extension field for ``count``."
    )

    distributor: typing.List[
        fhirtypes.DeviceDefinitionPackagingDistributorType
    ] = Field(
        None,
        alias="distributor",
        title="An organization that distributes the packaged device",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Business identifier of the packaged medication",
        description="The business identifier of the packaged medication.",
        # if property is element of this resource.
        element_property=True,
    )

    packaging: typing.List[fhirtypes.DeviceDefinitionPackagingType] = Field(
        None,
        alias="packaging",
        title="Allows packages within packages",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="A code that defines the specific type of packaging",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    udiDeviceIdentifier: typing.List[
        fhirtypes.DeviceDefinitionUdiDeviceIdentifierType
    ] = Field(
        None,
        alias="udiDeviceIdentifier",
        title="Unique Device Identifier (UDI) Barcode string on the packaging",
        description=None,
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("DeviceDefinitionPackagingDistributor", const=True)

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Distributor's human-readable name",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    organizationReference: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="organizationReference",
        title="Distributor as an Organization resource",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
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

    resource_type = Field("DeviceDefinitionProperty", const=True)

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Code that specifies the property being represented",
        description=(
            "Code that specifies the property such as a resolution or color being "
            "represented."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="Value of the property",
        description=(
            "The value of the property specified by the associated property.type "
            "code."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="Value of the property",
        description=(
            "The value of the property specified by the associated property.type "
            "code."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="valueCodeableConcept",
        title="Value of the property",
        description=(
            "The value of the property specified by the associated property.type "
            "code."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="Value of the property",
        description=(
            "The value of the property specified by the associated property.type "
            "code."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueInteger", title="Extension field for ``valueInteger``."
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="Value of the property",
        description=(
            "The value of the property specified by the associated property.type "
            "code."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueRange: fhirtypes.RangeType = Field(
        None,
        alias="valueRange",
        title="Value of the property",
        description=(
            "The value of the property specified by the associated property.type "
            "code."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Value of the property",
        description=(
            "The value of the property specified by the associated property.type "
            "code."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2683(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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

    resource_type = Field("DeviceDefinitionRegulatoryIdentifier", const=True)

    deviceIdentifier: fhirtypes.String = Field(
        None,
        alias="deviceIdentifier",
        title="The identifier itself",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    deviceIdentifier__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_deviceIdentifier",
        title="Extension field for ``deviceIdentifier``.",
    )

    issuer: fhirtypes.Uri = Field(
        None,
        alias="issuer",
        title="The organization that issued this identifier",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    issuer__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_issuer", title="Extension field for ``issuer``."
    )

    jurisdiction: fhirtypes.Uri = Field(
        None,
        alias="jurisdiction",
        title="The jurisdiction to which the deviceIdentifier applies",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    jurisdiction__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_jurisdiction", title="Extension field for ``jurisdiction``."
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="basic | master | license",
        description="The type of identifier itself.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["basic", "master", "license"],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3904(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


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

    resource_type = Field("DeviceDefinitionUdiDeviceIdentifier", const=True)

    deviceIdentifier: fhirtypes.String = Field(
        None,
        alias="deviceIdentifier",
        title=(
            "The identifier that is to be associated with every Device that "
            "references this DeviceDefintiion for the issuer and jurisdiction "
            "provided in the DeviceDefinition.udiDeviceIdentifier"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    deviceIdentifier__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_deviceIdentifier",
        title="Extension field for ``deviceIdentifier``.",
    )

    issuer: fhirtypes.Uri = Field(
        None,
        alias="issuer",
        title="The organization that assigns the identifier algorithm",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    issuer__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_issuer", title="Extension field for ``issuer``."
    )

    jurisdiction: fhirtypes.Uri = Field(
        None,
        alias="jurisdiction",
        title="The jurisdiction to which the deviceIdentifier applies",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    jurisdiction__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_jurisdiction", title="Extension field for ``jurisdiction``."
    )

    marketDistribution: typing.List[
        fhirtypes.DeviceDefinitionUdiDeviceIdentifierMarketDistributionType
    ] = Field(
        None,
        alias="marketDistribution",
        title="Indicates whether and when the device is available on the market",
        description="Indicates where and when the device is available on the market.",
        # if property is element of this resource.
        element_property=True,
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3716(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class DeviceDefinitionUdiDeviceIdentifierMarketDistribution(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Indicates whether and when the device is available on the market.
    Indicates where and when the device is available on the market.
    """

    resource_type = Field(
        "DeviceDefinitionUdiDeviceIdentifierMarketDistribution", const=True
    )

    marketPeriod: fhirtypes.PeriodType = Field(
        ...,
        alias="marketPeriod",
        title="Begin and end dates for the commercial distribution of the device",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    subJurisdiction: fhirtypes.Uri = Field(
        None,
        alias="subJurisdiction",
        title="National state or territory where the device is commercialized",
        description=(
            "National state or territory to which the marketDistribution recers, "
            "typically where the device is commercialized."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    subJurisdiction__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_5604(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("subJurisdiction", "subJurisdiction__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class DeviceDefinitionVersion(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The version of the device or software.
    """

    resource_type = Field("DeviceDefinitionVersion", const=True)

    component: fhirtypes.IdentifierType = Field(
        None,
        alias="component",
        title=(
            "The hardware or software module of the device to which the version "
            "applies"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="The type of the device version, e.g. manufacturer, approved, internal",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="The version text",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceDefinitionVersion`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "component", "value"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2545(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("value", "value__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values
