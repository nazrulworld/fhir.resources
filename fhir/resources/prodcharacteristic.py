# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ProdCharacteristic
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, fhirtypes


class ProdCharacteristic(backboneelement.BackboneElement):
    """ The marketing status describes the date when a medicinal product is
    actually put on the market or the date as of which it is no longer
    available.
    """

    resource_type = Field("ProdCharacteristic", const=True)

    color: ListType[fhirtypes.String] = Field(
        None,
        alias="color",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Where applicable, the color can be specified An appropriate controlled vocabulary shall be used The term and the term identifier shall be used",
    )

    depth: fhirtypes.QuantityType = Field(
        None,
        alias="depth",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Where applicable, the depth can be specified using a numerical value and its unit of measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used",
    )

    externalDiameter: fhirtypes.QuantityType = Field(
        None,
        alias="externalDiameter",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Where applicable, the external diameter can be specified using a numerical value and its unit of measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used",
    )

    height: fhirtypes.QuantityType = Field(
        None,
        alias="height",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Where applicable, the height can be specified using a numerical value and its unit of measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used",
    )

    image: ListType[fhirtypes.AttachmentType] = Field(
        None,
        alias="image",
        title="List of `Attachment` items (represented as `dict` in JSON)",
        description="Where applicable, the image can be provided The format of the image attachment shall be specified by regional implementations",
    )

    imprint: ListType[fhirtypes.String] = Field(
        None,
        alias="imprint",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Where applicable, the imprint can be specified as text",
    )

    nominalVolume: fhirtypes.QuantityType = Field(
        None,
        alias="nominalVolume",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Where applicable, the nominal volume can be specified using a numerical value and its unit of measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used",
    )

    scoring: fhirtypes.CodeableConceptType = Field(
        None,
        alias="scoring",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Where applicable, the scoring can be specified An appropriate controlled vocabulary shall be used The term and the term identifier shall be used",
    )

    shape: fhirtypes.String = Field(
        None,
        alias="shape",
        title="Type `String` (represented as `dict` in JSON)",
        description="Where applicable, the shape can be specified An appropriate controlled vocabulary shall be used The term and the term identifier shall be used",
    )

    weight: fhirtypes.QuantityType = Field(
        None,
        alias="weight",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Where applicable, the weight can be specified using a numerical value and its unit of measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used",
    )

    width: fhirtypes.QuantityType = Field(
        None,
        alias="width",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Where applicable, the width can be specified using a numerical value and its unit of measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used",
    )
