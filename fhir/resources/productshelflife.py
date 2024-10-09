from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ProductShelfLife
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backbonetype, fhirtypes


class ProductShelfLife(backbonetype.BackboneType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The shelf-life and storage information for a medicinal product item or
    container can be described using this class.
    """

    __resource_type__ = "ProductShelfLife"

    periodDuration: fhirtypes.DurationType | None = Field(  # type: ignore
        None,
        alias="periodDuration",
        title=(
            "The shelf life time period can be specified using a numerical value "
            "for the period of time and its unit of time measurement The unit of "
            "measurement shall be specified in accordance with ISO 11240 and the "
            "resulting terminology The symbol and the symbol identifier shall be "
            "used"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e period[x]
            "one_of_many": "period",
            "one_of_many_required": False,
        },
    )

    periodString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="periodString",
        title=(
            "The shelf life time period can be specified using a numerical value "
            "for the period of time and its unit of time measurement The unit of "
            "measurement shall be specified in accordance with ISO 11240 and the "
            "resulting terminology The symbol and the symbol identifier shall be "
            "used"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e period[x]
            "one_of_many": "period",
            "one_of_many_required": False,
        },
    )
    periodString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_periodString", title="Extension field for ``periodString``."
    )

    specialPrecautionsForStorage: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="specialPrecautionsForStorage",
        title=(
            "Special precautions for storage, if any, can be specified using an "
            "appropriate controlled vocabulary The controlled term and the "
            "controlled term identifier shall be specified"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title=(
            "This describes the shelf life, taking into account various scenarios "
            "such as shelf life of the packaged Medicinal Product itself, shelf "
            "life after transformation where necessary and shelf life after the "
            "first opening of a bottle, etc. The shelf life type shall be specified"
            " using an appropriate controlled vocabulary The controlled term and "
            "the controlled term identifier shall be specified"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ProductShelfLife`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "periodDuration",
            "periodString",
            "specialPrecautionsForStorage",
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
        one_of_many_fields = {"period": ["periodDuration", "periodString"]}
        return one_of_many_fields
