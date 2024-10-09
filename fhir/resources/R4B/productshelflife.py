from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ProductShelfLife
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, fhirtypes


class ProductShelfLife(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The shelf-life and storage information for a medicinal product item or
    container can be described using this class.
    """

    __resource_type__ = "ProductShelfLife"

    identifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Unique identifier for the packaged Medicinal Product",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    period: fhirtypes.QuantityType = Field(  # type: ignore
        ...,
        alias="period",
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
        },
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

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
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
            "identifier",
            "type",
            "period",
            "specialPrecautionsForStorage",
        ]
