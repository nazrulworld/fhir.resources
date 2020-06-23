# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ProductShelfLife
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, fhirtypes


class ProductShelfLife(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The shelf-life and storage information for a medicinal product item or
    container can be described using this class.
    """

    resource_type = Field("ProductShelfLife", const=True)

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Unique identifier for the packaged Medicinal Product",
    )

    period: fhirtypes.QuantityType = Field(
        ...,
        alias="period",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description=(
            "The shelf life time period can be specified using a numerical value "
            "for the period of time and its unit of time measurement The unit of "
            "measurement shall be specified in accordance with ISO 11240 and the "
            "resulting terminology The symbol and the symbol identifier shall be "
            "used"
        ),
    )

    specialPrecautionsForStorage: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="specialPrecautionsForStorage",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description=(
            "Special precautions for storage, if any, can be specified using an "
            "appropriate controlled vocabulary The controlled term and the "
            "controlled term identifier shall be specified"
        ),
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "This describes the shelf life, taking into account various scenarios "
            "such as shelf life of the packaged Medicinal Product itself, shelf "
            "life after transformation where necessary and shelf life after the "
            "first opening of a bottle, etc. The shelf life type shall be specified"
            " using an appropriate controlled vocabulary The controlled term and "
            "the controlled term identifier shall be specified"
        ),
    )
