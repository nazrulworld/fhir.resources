from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/CatalogEntry
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class CatalogEntry(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An entry in a catalog.
    Catalog entries are wrappers that contextualize items included in a
    catalog.
    """

    __resource_type__ = "CatalogEntry"

    additionalCharacteristic: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="additionalCharacteristic",
        title="Additional characteristics of the catalog entry",
        description="Used for examplefor Out of Formulary, or any specifics.",
        json_schema_extra={
            "element_property": True,
        },
    )

    additionalClassification: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="additionalClassification",
        title="Additional classification of the catalog entry",
        description="User for example for ATC classification, or.",
        json_schema_extra={
            "element_property": True,
        },
    )

    additionalIdentifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="additionalIdentifier",
        title=(
            "Any additional identifier(s) for the catalog item, in the same "
            "granularity or concept"
        ),
        description="Used in supporting related concepts, e.g. NDC to RxNorm.",
        json_schema_extra={
            "element_property": True,
        },
    )

    classification: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="classification",
        title="Classification (category or class) of the item entry",
        description="Classes of devices, or ATC for medication.",
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Unique identifier of the catalog item",
        description=(
            "Used in supporting different identifiers for the same product, e.g. "
            "manufacturer code and retailer code."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    lastUpdated: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="lastUpdated",
        title="When was this catalog last updated",
        description=(
            "Typically date of issue is different from the beginning of the "
            "validity. This can be used to see when an item was last updated."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    lastUpdated__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_lastUpdated", title="Extension field for ``lastUpdated``."
    )

    orderable: bool | None = Field(  # type: ignore
        None,
        alias="orderable",
        title="Whether the entry represents an orderable item",
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    orderable__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_orderable", title="Extension field for ``orderable``."
    )

    referencedItem: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="referencedItem",
        title="The item that is being defined",
        description="The item in a catalog or definition.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
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
        },
    )

    relatedEntry: typing.List[fhirtypes.CatalogEntryRelatedEntryType] | None = Field(  # type: ignore
        None,
        alias="relatedEntry",
        title="An item that this catalog entry is related to",
        description=(
            "Used for example, to point to a substance, or to a device used to "
            "administer a medication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "Used to support catalog exchange even for unsupported products, e.g. "
            "getting list of medications even if not prescribable."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["draft", "active", "retired", "unknown"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="The type of item - medication, device, service, protocol or other",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    validTo: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="validTo",
        title="The date until which this catalog entry is expected to be active",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    validTo__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_validTo", title="Extension field for ``validTo``."
    )

    validityPeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="validityPeriod",
        title="The time period in which this catalog entry is expected to be active",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
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

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("orderable", "orderable__ext")]
        return required_fields


class CatalogEntryRelatedEntry(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An item that this catalog entry is related to.
    Used for example, to point to a substance, or to a device used to
    administer a medication.
    """

    __resource_type__ = "CatalogEntryRelatedEntry"

    item: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="item",
        title="The reference to the related item",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["CatalogEntry"],
        },
    )

    relationtype: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="relationtype",
        title="triggers | is-replaced-by",
        description=(
            "The type of relation to the related item: child, parent, "
            "packageContent, containerPackage, usedIn, uses, requires, etc."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["triggers", "is-replaced-by"],
        },
    )
    relationtype__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_relationtype", title="Extension field for ``relationtype``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CatalogEntryRelatedEntry`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "relationtype", "item"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("relationtype", "relationtype__ext")]
        return required_fields
