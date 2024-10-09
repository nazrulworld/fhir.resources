from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/UsageContext
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import element, fhirtypes


class UsageContext(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Describes the context of use for a conformance or knowledge resource.
    Specifies clinical/business/etc metadata that can be used to retrieve,
    index and/or categorize an artifact. This metadata can either be specific
    to the applicable population (e.g., age category, DRG) or the specific
    context of care (e.g., venue, care setting, provider of care).
    """

    __resource_type__ = "UsageContext"

    code: fhirtypes.CodingType = Field(  # type: ignore
        ...,
        alias="code",
        title="Type of context being specified",
        description=(
            "A code that identifies the type of context being specified by this "
            "usage context."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="valueCodeableConcept",
        title="Value that defines the context",
        description=(
            "A value that defines the context specified in this context of use. The"
            " interpretation of the value is defined by the code."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="valueQuantity",
        title="Value that defines the context",
        description=(
            "A value that defines the context specified in this context of use. The"
            " interpretation of the value is defined by the code."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueRange: fhirtypes.RangeType | None = Field(  # type: ignore
        None,
        alias="valueRange",
        title="Value that defines the context",
        description=(
            "A value that defines the context specified in this context of use. The"
            " interpretation of the value is defined by the code."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``UsageContext`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "code",
            "valueCodeableConcept",
            "valueQuantity",
            "valueRange",
        ]

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "value": ["valueCodeableConcept", "valueQuantity", "valueRange"]
        }
        return one_of_many_fields
