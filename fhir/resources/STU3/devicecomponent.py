# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceComponent
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class DeviceComponent(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
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
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Instance id assigned by the software stack",
    )

    languageCode: fhirtypes.CodeableConceptType = Field(
        None,
        alias="languageCode",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "Language code for the human-readable text strings produced by the "
            "device"
        ),
    )

    lastSystemChange: fhirtypes.Instant = Field(
        None,
        alias="lastSystemChange",
        title="Type `Instant`",
        description="Recent system change timestamp",
    )
    lastSystemChange__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_lastSystemChange",
        title="Extension field for ``lastSystemChange``.",
    )

    measurementPrinciple: fhirtypes.Code = Field(
        None,
        alias="measurementPrinciple",
        title="Type `Code`",
        description=(
            "other | chemical | electrical | impedance | nuclear | optical | "
            "thermal | biological | mechanical | acoustical | manual+"
        ),
    )
    measurementPrinciple__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_measurementPrinciple",
        title="Extension field for ``measurementPrinciple``.",
    )

    operationalStatus: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="operationalStatus",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description=(
            "Current operational status of the component, for example On, Off or "
            "Standby"
        ),
    )

    parameterGroup: fhirtypes.CodeableConceptType = Field(
        None,
        alias="parameterGroup",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Current supported parameter group",
    )

    parent: fhirtypes.ReferenceType = Field(
        None,
        alias="parent",
        title=(
            "Type `Reference` referencing `DeviceComponent` (represented as `dict` "
            "in JSON)"
        ),
        description="Parent resource link",
    )

    productionSpecification: ListType[
        fhirtypes.DeviceComponentProductionSpecificationType
    ] = Field(
        None,
        alias="productionSpecification",
        title=(
            "List of `DeviceComponentProductionSpecification` items (represented as"
            " `dict` in JSON)"
        ),
        description="Specification details such as Component Revisions, or Serial Numbers",
    )

    source: fhirtypes.ReferenceType = Field(
        None,
        alias="source",
        title="Type `Reference` referencing `Device` (represented as `dict` in JSON)",
        description="Top-level device resource link",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="What kind of component it is",
    )


class DeviceComponentProductionSpecification(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
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
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Internal component unique identification",
    )

    productionSpec: fhirtypes.String = Field(
        None,
        alias="productionSpec",
        title="Type `String`",
        description="A printable string defining the component",
    )
    productionSpec__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_productionSpec", title="Extension field for ``productionSpec``."
    )

    specType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="specType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "Type or kind of production specification, for example serial number or"
            " software revision"
        ),
    )
