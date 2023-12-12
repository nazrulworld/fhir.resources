# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SimpleQuantity
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1 import Field

from . import element, fhirtypes


class Quantity(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A measured or measurable amount.
    A measured amount (or an amount that can potentially be measured). Note
    that measured amounts include amounts that are not precisely quantified,
    including amounts involving arbitrary units and floating currencies.
    """

    resource_type = Field("Quantity", const=True)

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Coded form of the unit",
        description=(
            "A computer processable form of the unit in some unit representation "
            "system."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    comparator: fhirtypes.Code = Field(
        None,
        alias="comparator",
        title="< | <= | >= | > - how to understand the value",
        description=(
            "How the value should be understood and represented - whether the "
            "actual value is greater or less than the stated value due to "
            'measurement issues; e.g. if the comparator is "<" , then the real '
            "value is < stated value."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["\u003c", "\u003c=", "\u003e=", "\u003e"],
    )
    comparator__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comparator", title="Extension field for ``comparator``."
    )

    system: fhirtypes.Uri = Field(
        None,
        alias="system",
        title="System that defines coded unit form",
        description=(
            "The identification of the system that provides the coded form of the "
            "unit."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_system", title="Extension field for ``system``."
    )

    unit: fhirtypes.String = Field(
        None,
        alias="unit",
        title="Unit representation",
        description="A human-readable form of the unit.",
        # if property is element of this resource.
        element_property=True,
    )
    unit__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_unit", title="Extension field for ``unit``."
    )

    value: fhirtypes.Decimal = Field(
        None,
        alias="value",
        title="Numerical value (with implicit precision)",
        description=(
            "The value of the measured amount. The value includes an implicit "
            "precision in the presentation of the value."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Quantity`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "value", "comparator", "unit", "system", "code"]
