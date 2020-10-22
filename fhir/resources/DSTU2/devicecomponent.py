# -*- coding: utf-8 -*-
"""
Profile: https://www.hl7.org/fhir/DSTU2/devicecomponent.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic import Field

from . import fhirtypes
from .backboneelement import BackboneElement
from .domainresource import DomainResource


class DeviceComponent(DomainResource):
    """An instance of a medical-related component of a medical device.

    Describes the characteristics, operational status and capabilities of a
    medical-related component of a medical device.
    """

    resource_type = "DeviceComponent"

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="What kind of component it is.",
    )

    identifier: fhirtypes.IdentifierType = Field(
        ...,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON).",
        description="Instance id assigned by the software stack.",
    )

    lastSystemChange: fhirtypes.Instant = Field(
        ...,
        alias="lastSystemChange",
        title="Type `Instant` (represented as `str` in JSON).",
        description="Recent system change timestamp.",
    )

    source: fhirtypes.ReferenceType = Field(
        None,
        alias="source",
        title="Type `Reference` referencing `Device` (represented as `dict` in JSON).",
        description="A source device of this component.",
        enum_reference_types=["Device"],
    )

    parent: fhirtypes.ReferenceType = Field(
        None,
        alias="parent",
        title="Type `Reference` referencing `DeviceComponent` (represented as `dict` in JSON).",
        description="Parent resource link.",
        enum_reference_types=["DeviceComponent"],
    )

    operationalStatus: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="operationalStatus",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="Component operational status.",
    )

    parameterGroup: fhirtypes.CodeableConceptType = Field(
        None,
        alias="parameterGroup",
        title="Type `CodeableConcept` (represented as `dict` in JSON). ",
        description="Current supported parameter group.",
    )

    measurementPrinciple: fhirtypes.Code = Field(
        None,
        alias="measurementPrinciple",
        title="Type `str`.",
        description=(
            "other | chemical | electrical | impedance | nuclear | optical | thermal | "
            "biological | mechanical | acoustical | manual+"
        ),
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

    productionSpecification: ListType[
        fhirtypes.DeviceComponentProductionSpecificationType
    ] = Field(
        None,
        alias="productSpecification",
        title=(
            "List of `DeviceComponentProductionSpecification` items "
            "(represented as `dict` in JSON)."
        ),
        description="Production specification of the component.",
    )

    languageCode: fhirtypes.CodeableConceptType = Field(
        None,
        alias="languageCode",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description=(
            "Language code for the human-readable text "
            "strings produced by the device."
        ),
    )


class DeviceComponentProductionSpecification(BackboneElement):
    """Production specification of the component.

    Describes the production specification such as component revision, serial
    number, etc.
    """

    resource_type = "DeviceComponentProductionSpecification"

    specType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="specType",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Specification type.",
    )

    componentId: fhirtypes.IdentifierType = Field(
        None,
        alias="componentId",
        title="Type `Identifier` (represented as `dict` in JSON).",
        description="Internal component unique identification.",
    )

    productionSpec: fhirtypes.String = Field(
        None,
        alias="productionSpec",
        title="Type `str`.",
        description="A printable string defining the component.",
    )
