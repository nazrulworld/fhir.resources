# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceComponent
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic.v1 import Field

from . import backboneelement, domainresource, fhirtypes


class DeviceComponent(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An instance of a medical-related component of a medical device.
    The characteristics, operational status and capabilities of a medical-
    related component of a medical device.
    """

    resource_type = Field("DeviceComponent", const=True)

    identifier: fhirtypes.IdentifierType = Field(
        ...,
        alias="identifier",
        title="Instance id assigned by the software stack",
        description=(
            "The locally assigned unique identification by the software. For "
            "example: handle ID."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    languageCode: fhirtypes.CodeableConceptType = Field(
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
        # if property is element of this resource.
        element_property=True,
    )

    lastSystemChange: fhirtypes.Instant = Field(
        None,
        alias="lastSystemChange",
        title="Recent system change timestamp",
        description=(
            "The timestamp for the most recent system change which includes device "
            "configuration or setting change."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    lastSystemChange__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_lastSystemChange",
        title="Extension field for ``lastSystemChange``.",
    )

    measurementPrinciple: fhirtypes.Code = Field(
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
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
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
    )
    measurementPrinciple__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_measurementPrinciple",
        title="Extension field for ``measurementPrinciple``.",
    )

    operationalStatus: typing.List[fhirtypes.CodeableConceptType] = Field(
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
        # if property is element of this resource.
        element_property=True,
    )

    parameterGroup: fhirtypes.CodeableConceptType = Field(
        None,
        alias="parameterGroup",
        title="Current supported parameter group",
        description=(
            "The parameter group supported by the current device component that is "
            "based on some nomenclature, e.g. cardiovascular."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    parent: fhirtypes.ReferenceType = Field(
        None,
        alias="parent",
        title="Parent resource link",
        description=(
            "The link to the parent resource. For example: Channel is linked to its"
            " VMD parent."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DeviceComponent"],
    )

    productionSpecification: typing.List[
        fhirtypes.DeviceComponentProductionSpecificationType
    ] = Field(
        None,
        alias="productionSpecification",
        title="Specification details such as Component Revisions, or Serial Numbers",
        description=(
            "The production specification such as component revision, serial "
            "number, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    source: fhirtypes.ReferenceType = Field(
        None,
        alias="source",
        title="Top-level device resource link",
        description=(
            "The link to the source Device that contains administrative device "
            "information such as manufacture, serial number, etc."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="What kind of component it is",
        description=(
            "The component type as defined in the object-oriented or metric "
            "nomenclature partition."
        ),
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("DeviceComponentProductionSpecification", const=True)

    componentId: fhirtypes.IdentifierType = Field(
        None,
        alias="componentId",
        title="Internal component unique identification",
        description=(
            "The internal component unique identification. This is a provision for "
            "manufacture specific standard components using a private OID. "
            "11073-10101 has a partition for private OID semantic that the "
            "manufacturer can make use of."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    productionSpec: fhirtypes.String = Field(
        None,
        alias="productionSpec",
        title="A printable string defining the component",
        description="The printable string defining the component.",
        # if property is element of this resource.
        element_property=True,
    )
    productionSpec__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_productionSpec", title="Extension field for ``productionSpec``."
    )

    specType: fhirtypes.CodeableConceptType = Field(
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
        # if property is element of this resource.
        element_property=True,
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
