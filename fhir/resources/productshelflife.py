# -*- coding: utf-8 -*-
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

    resource_type = Field("ProductShelfLife", const=True)

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Unique identifier for the packaged Medicinal Product",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    period: fhirtypes.QuantityType = Field(
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
        # if property is element of this resource.
        element_property=True,
    )

    specialPrecautionsForStorage: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="specialPrecautionsForStorage",
        title=(
            "Special precautions for storage, if any, can be specified using an "
            "appropriate controlled vocabulary The controlled term and the "
            "controlled term identifier shall be specified"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
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
        # if property is element of this resource.
        element_property=True,
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
