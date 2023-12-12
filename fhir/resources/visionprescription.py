# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/VisionPrescription
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


class VisionPrescription(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Prescription for vision correction products for a patient.
    An authorization for the provision of glasses and/or contact lenses to a
    patient.
    """

    resource_type = Field("VisionPrescription", const=True)

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Response creation date",
        description="The date this resource was created.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
    )

    dateWritten: fhirtypes.DateTime = Field(
        None,
        alias="dateWritten",
        title="When prescription was authorized",
        description="The date (and perhaps time) when the prescription was written.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    dateWritten__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_dateWritten", title="Extension field for ``dateWritten``."
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Created during encounter / admission / stay",
        description=(
            "A reference to a resource that identifies the particular occurrence of"
            " contact between patient and health care provider during which the "
            "prescription was issued."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier for vision prescription",
        description="A unique identifier assigned to this vision prescription.",
        # if property is element of this resource.
        element_property=True,
    )

    lensSpecification: typing.List[
        fhirtypes.VisionPrescriptionLensSpecificationType
    ] = Field(
        ...,
        alias="lensSpecification",
        title="Vision lens authorization",
        description=(
            "Contain the details of  the individual lens specifications and serves "
            "as the authorization for the fullfillment by certified professionals."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Who prescription is for",
        description=(
            "A resource reference to the person to whom the vision prescription "
            "applies."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    prescriber: fhirtypes.ReferenceType = Field(
        ...,
        alias="prescriber",
        title="Who authorized the vision prescription",
        description=(
            "The healthcare professional responsible for authorizing the "
            "prescription."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "PractitionerRole"],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="active | cancelled | draft | entered-in-error",
        description="The status of the resource instance.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "cancelled", "draft", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``VisionPrescription`` according specification,
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
            "status",
            "created",
            "patient",
            "encounter",
            "dateWritten",
            "prescriber",
            "lensSpecification",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2110(
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
            ("created", "created__ext"),
            ("dateWritten", "dateWritten__ext"),
            ("status", "status__ext"),
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


class VisionPrescriptionLensSpecification(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Vision lens authorization.
    Contain the details of  the individual lens specifications and serves as
    the authorization for the fullfillment by certified professionals.
    """

    resource_type = Field("VisionPrescriptionLensSpecification", const=True)

    add: fhirtypes.Decimal = Field(
        None,
        alias="add",
        title="Added power for multifocal levels",
        description=(
            "Power adjustment for multifocal lenses measured in dioptres (0.25 "
            "units)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    add__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_add", title="Extension field for ``add``."
    )

    axis: fhirtypes.Integer = Field(
        None,
        alias="axis",
        title="Lens meridian which contain no power for astigmatism",
        description="Adjustment for astigmatism measured in integer degrees.",
        # if property is element of this resource.
        element_property=True,
    )
    axis__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_axis", title="Extension field for ``axis``."
    )

    backCurve: fhirtypes.Decimal = Field(
        None,
        alias="backCurve",
        title="Contact lens back curvature",
        description="Back curvature measured in millimetres.",
        # if property is element of this resource.
        element_property=True,
    )
    backCurve__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_backCurve", title="Extension field for ``backCurve``."
    )

    brand: fhirtypes.String = Field(
        None,
        alias="brand",
        title="Brand required",
        description="Brand recommendations or restrictions.",
        # if property is element of this resource.
        element_property=True,
    )
    brand__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_brand", title="Extension field for ``brand``."
    )

    color: fhirtypes.String = Field(
        None,
        alias="color",
        title="Color required",
        description="Special color or pattern.",
        # if property is element of this resource.
        element_property=True,
    )
    color__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_color", title="Extension field for ``color``."
    )

    cylinder: fhirtypes.Decimal = Field(
        None,
        alias="cylinder",
        title="Lens power for astigmatism",
        description="Power adjustment for astigmatism measured in dioptres (0.25 units).",
        # if property is element of this resource.
        element_property=True,
    )
    cylinder__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_cylinder", title="Extension field for ``cylinder``."
    )

    diameter: fhirtypes.Decimal = Field(
        None,
        alias="diameter",
        title="Contact lens diameter",
        description="Contact lens diameter measured in millimetres.",
        # if property is element of this resource.
        element_property=True,
    )
    diameter__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_diameter", title="Extension field for ``diameter``."
    )

    duration: fhirtypes.QuantityType = Field(
        None,
        alias="duration",
        title="Lens wear duration",
        description="The recommended maximum wear period for the lens.",
        # if property is element of this resource.
        element_property=True,
    )

    eye: fhirtypes.Code = Field(
        None,
        alias="eye",
        title="right | left",
        description="The eye for which the lens specification applies.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["right", "left"],
    )
    eye__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_eye", title="Extension field for ``eye``."
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Notes for coatings",
        description="Notes for special requirements such as coatings and lens materials.",
        # if property is element of this resource.
        element_property=True,
    )

    power: fhirtypes.Decimal = Field(
        None,
        alias="power",
        title="Contact lens power",
        description="Contact lens power measured in dioptres (0.25 units).",
        # if property is element of this resource.
        element_property=True,
    )
    power__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_power", title="Extension field for ``power``."
    )

    prism: typing.List[fhirtypes.VisionPrescriptionLensSpecificationPrismType] = Field(
        None,
        alias="prism",
        title="Eye alignment compensation",
        description="Allows for adjustment on two axis.",
        # if property is element of this resource.
        element_property=True,
    )

    product: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="product",
        title="Product to be supplied",
        description=(
            "Identifies the type of vision correction product which is required for"
            " the patient."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    sphere: fhirtypes.Decimal = Field(
        None,
        alias="sphere",
        title="Power of the lens",
        description="Lens power measured in dioptres (0.25 units).",
        # if property is element of this resource.
        element_property=True,
    )
    sphere__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sphere", title="Extension field for ``sphere``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``VisionPrescriptionLensSpecification`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "product",
            "eye",
            "sphere",
            "cylinder",
            "axis",
            "prism",
            "add",
            "power",
            "backCurve",
            "diameter",
            "duration",
            "color",
            "brand",
            "note",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3857(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("eye", "eye__ext")]
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


class VisionPrescriptionLensSpecificationPrism(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Eye alignment compensation.
    Allows for adjustment on two axis.
    """

    resource_type = Field("VisionPrescriptionLensSpecificationPrism", const=True)

    amount: fhirtypes.Decimal = Field(
        None,
        alias="amount",
        title="Amount of adjustment",
        description="Amount of prism to compensate for eye alignment in fractional units.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    amount__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_amount", title="Extension field for ``amount``."
    )

    base: fhirtypes.Code = Field(
        None,
        alias="base",
        title="up | down | in | out",
        description="The relative base, or reference lens edge, for the prism.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["up", "down", "in", "out"],
    )
    base__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_base", title="Extension field for ``base``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``VisionPrescriptionLensSpecificationPrism`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "amount", "base"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_4379(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("amount", "amount__ext"), ("base", "base__ext")]
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
