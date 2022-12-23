# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CatalogEntry
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class CatalogEntry(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An entry in a catalog.
    Catalog entries are wrappers that contextualize items included in a
    catalog.
    """

    resource_type = Field("CatalogEntry", const=True)

    additionalCharacteristic: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="additionalCharacteristic",
        title="Additional characteristics of the catalog entry",
        description="Used for examplefor Out of Formulary, or any specifics.",
        # if property is element of this resource.
        element_property=True,
    )

    additionalClassification: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="additionalClassification",
        title="Additional classification of the catalog entry",
        description="User for example for ATC classification, or.",
        # if property is element of this resource.
        element_property=True,
    )

    additionalIdentifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="additionalIdentifier",
        title=(
            "Any additional identifier(s) for the catalog item, in the same "
            "granularity or concept"
        ),
        description="Used in supporting related concepts, e.g. NDC to RxNorm.",
        # if property is element of this resource.
        element_property=True,
    )

    classification: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="classification",
        title="Classification (category or class) of the item entry",
        description="Classes of devices, or ATC for medication.",
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Unique identifier of the catalog item",
        description=(
            "Used in supporting different identifiers for the same product, e.g. "
            "manufacturer code and retailer code."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    lastUpdated: fhirtypes.DateTime = Field(
        None,
        alias="lastUpdated",
        title="When was this catalog last updated",
        description=(
            "Typically date of issue is different from the beginning of the "
            "validity. This can be used to see when an item was last updated."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    lastUpdated__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastUpdated", title="Extension field for ``lastUpdated``."
    )

    orderable: bool = Field(
        None,
        alias="orderable",
        title="Whether the entry represents an orderable item",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    orderable__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_orderable", title="Extension field for ``orderable``."
    )

    referencedItem: fhirtypes.ReferenceType = Field(
        ...,
        alias="referencedItem",
        title="The item that is being defined",
        description="The item in a catalog or definition.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Medication",
            "Device",
            "Organization",
            "Practitioner",
            "PractitionerRole",
            "HealthcareService",
            "ActivityDefinition",
            "PlanDefinition",
            "SpecimenDefinition",
            "ObservationDefinition",
            "Binary",
        ],
    )

    relatedEntry: typing.List[fhirtypes.CatalogEntryRelatedEntryType] = Field(
        None,
        alias="relatedEntry",
        title="An item that this catalog entry is related to",
        description=(
            "Used for example, to point to a substance, or to a device used to "
            "administer a medication."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "Used to support catalog exchange even for unsupported products, e.g. "
            "getting list of medications even if not prescribable."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired", "unknown"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="The type of item - medication, device, service, protocol or other",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    validTo: fhirtypes.DateTime = Field(
        None,
        alias="validTo",
        title="The date until which this catalog entry is expected to be active",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    validTo__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_validTo", title="Extension field for ``validTo``."
    )

    validityPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="validityPeriod",
        title="The time period in which this catalog entry is expected to be active",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CatalogEntry`` according specification,
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
            "type",
            "orderable",
            "referencedItem",
            "additionalIdentifier",
            "classification",
            "status",
            "validityPeriod",
            "validTo",
            "lastUpdated",
            "additionalCharacteristic",
            "additionalClassification",
            "relatedEntry",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1417(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("orderable", "orderable__ext")]
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


class CatalogEntryRelatedEntry(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An item that this catalog entry is related to.
    Used for example, to point to a substance, or to a device used to
    administer a medication.
    """

    resource_type = Field("CatalogEntryRelatedEntry", const=True)

    item: fhirtypes.ReferenceType = Field(
        ...,
        alias="item",
        title="The reference to the related item",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["CatalogEntry"],
    )

    relationtype: fhirtypes.Code = Field(
        None,
        alias="relationtype",
        title="triggers | is-replaced-by",
        description=(
            "The type of relation to the related item: child, parent, "
            "packageContent, containerPackage, usedIn, uses, requires, etc."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["triggers", "is-replaced-by"],
    )
    relationtype__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_relationtype", title="Extension field for ``relationtype``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CatalogEntryRelatedEntry`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "relationtype", "item"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2652(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("relationtype", "relationtype__ext")]
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
