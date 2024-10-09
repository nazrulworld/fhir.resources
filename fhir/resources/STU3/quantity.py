from __future__ import annotations as _annotations

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
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A measured or measurable amount.
    A measured amount (or an amount that can potentially be measured). Note
    that measured amounts include amounts that are not precisely quantified,
    including amounts involving arbitrary units and floating currencies.
    """

    __resource_type__ = "Quantity"

    code: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Coded form of the unit",
        description=(
            "A computer processable form of the unit in some unit representation "
            "system."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_code", title="Extension field for ``code``."
    )

    comparator: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="comparator",
        title="< | <= | >= | > - how to understand the value",
        description=(
            "How the value should be understood and represented - whether the "
            "actual value is greater or less than the stated value due to "
            'measurement issues; e.g. if the comparator is "<" , then the real '
            "value is < stated value."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    comparator__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_comparator", title="Extension field for ``comparator``."
    )

    system: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="system",
        title="System that defines coded unit form",
        description=(
            "The identification of the system that provides the coded form of the "
            "unit."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_system", title="Extension field for ``system``."
    )

    unit: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="unit",
        title="Unit representation",
        description="A human-readable form of the unit.",
        json_schema_extra={
            "element_property": True,
        },
    )
    unit__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_unit", title="Extension field for ``unit``."
    )

    value: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="value",
        title="Numerical value (with implicit precision)",
        description=(
            "The value of the measured amount. The value includes an implicit "
            "precision in the presentation of the value."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Quantity`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "value", "comparator", "unit", "system", "code"]
