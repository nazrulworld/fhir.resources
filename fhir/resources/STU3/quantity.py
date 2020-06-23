# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SimpleQuantity
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic import Field

from . import element, fhirtypes


class Quantity(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A measured or measurable amount.
    A measured amount (or an amount that can potentially be measured). Note
    that measured amounts include amounts that are not precisely quantified,
    including amounts involving arbitrary units and floating currencies.
    """

    resource_type = Field("Quantity", const=True)

    code: fhirtypes.Code = Field(
        None, alias="code", title="Type `Code`", description="Coded form of the unit"
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    comparator: fhirtypes.Code = Field(
        None,
        alias="comparator",
        title="Type `Code`",
        description="\u003c | \u003c= | \u003e= | \u003e - how to understand the value",
    )
    comparator__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comparator", title="Extension field for ``comparator``."
    )

    system: fhirtypes.Uri = Field(
        None,
        alias="system",
        title="Type `Uri`",
        description="System that defines coded unit form",
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_system", title="Extension field for ``system``."
    )

    unit: fhirtypes.String = Field(
        None, alias="unit", title="Type `String`", description="Unit representation"
    )
    unit__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_unit", title="Extension field for ``unit``."
    )

    value: fhirtypes.Decimal = Field(
        None,
        alias="value",
        title="Type `Decimal`",
        description="Numerical value (with implicit precision)",
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )
