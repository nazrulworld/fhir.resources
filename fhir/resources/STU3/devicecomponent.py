from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceComponent
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class DeviceComponent(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An instance of a medical-related component of a medical device.
    The characteristics, operational status and capabilities of a medical-
    related component of a medical device.
    """

    __resource_type__ = "DeviceComponent"

    identifier: fhirtypes.IdentifierType = Field(  # type: ignore
        ...,
        alias="identifier",
        title="Instance id assigned by the software stack",
        description=(
            "The locally assigned unique identification by the software. For "
            "example: handle ID."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    languageCode: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="languageCode",
        title=(
            "Language code for the human-readable text strings produced by the "
            "device"
        ),
        description=(
            "The language code for the human-readable text string produced by the "
            "device. This language code will follow the IETF language tag. Example:"
            " en-US."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    lastSystemChange: fhirtypes.InstantType | None = Field(  # type: ignore
        None,
        alias="lastSystemChange",
        title="Recent system change timestamp",
        description=(
            "The timestamp for the most recent system change which includes device "
            "configuration or setting change."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    lastSystemChange__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_lastSystemChange",
        title="Extension field for ``lastSystemChange``.",
    )

    measurementPrinciple: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="measurementPrinciple",
        title=(
            "other | chemical | electrical | impedance | nuclear | optical | "
            "thermal | biological | mechanical | acoustical | manual+"
        ),
        description=(
            "The physical principle of the measurement. For example: thermal, "
            "chemical, acoustical, etc."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "other",
                "chemical",
                "electrical",
                "impedance",
                "nuclear",
                "optical",
                "thermal",
                "biological",
                "mechanical",
                "acoustical",
                "manual+",
            ],
        },
    )
    measurementPrinciple__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_measurementPrinciple",
        title="Extension field for ``measurementPrinciple``.",
    )

    operationalStatus: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="operationalStatus",
        title=(
            "Current operational status of the component, for example On, Off or "
            "Standby"
        ),
        description=(
            "The current operational status of the device. For example: On, Off, "
            "Standby, etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    parameterGroup: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="parameterGroup",
        title="Current supported parameter group",
        description=(
            "The parameter group supported by the current device component that is "
            "based on some nomenclature, e.g. cardiovascular."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    parent: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="parent",
        title="Parent resource link",
        description=(
            "The link to the parent resource. For example: Channel is linked to its"
            " VMD parent."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DeviceComponent"],
        },
    )

    productionSpecification: typing.List[fhirtypes.DeviceComponentProductionSpecificationType] | None = Field(  # type: ignore
        None,
        alias="productionSpecification",
        title="Specification details such as Component Revisions, or Serial Numbers",
        description=(
            "The production specification such as component revision, serial "
            "number, etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    source: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="source",
        title="Top-level device resource link",
        description=(
            "The link to the source Device that contains administrative device "
            "information such as manufacture, serial number, etc."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Device"],
        },
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="What kind of component it is",
        description=(
            "The component type as defined in the object-oriented or metric "
            "nomenclature partition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceComponent`` according specification,
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
            "lastSystemChange",
            "source",
            "parent",
            "operationalStatus",
            "parameterGroup",
            "measurementPrinciple",
            "productionSpecification",
            "languageCode",
        ]


class DeviceComponentProductionSpecification(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Specification details such as Component Revisions, or Serial Numbers.
    The production specification such as component revision, serial number,
    etc.
    """

    __resource_type__ = "DeviceComponentProductionSpecification"

    componentId: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="componentId",
        title="Internal component unique identification",
        description=(
            "The internal component unique identification. This is a provision for "
            "manufacture specific standard components using a private OID. "
            "11073-10101 has a partition for private OID semantic that the "
            "manufacturer can make use of."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    productionSpec: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="productionSpec",
        title="A printable string defining the component",
        description="The printable string defining the component.",
        json_schema_extra={
            "element_property": True,
        },
    )
    productionSpec__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_productionSpec", title="Extension field for ``productionSpec``."
    )

    specType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="specType",
        title=(
            "Type or kind of production specification, for example serial number or"
            " software revision"
        ),
        description=(
            "The specification type, such as, serial number, part number, hardware "
            "revision, software revision, etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceComponentProductionSpecification`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "specType",
            "componentId",
            "productionSpec",
        ]
