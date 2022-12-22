# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ProdCharacteristic
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, fhirtypes


class ProdCharacteristic(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The marketing status describes the date when a medicinal product is
    actually put on the market or the date as of which it is no longer
    available.
    """

    resource_type = Field("ProdCharacteristic", const=True)

    color: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="color",
        title=(
            "Where applicable, the color can be specified An appropriate controlled"
            " vocabulary shall be used The term and the term identifier shall be "
            "used"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    color__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_color", title="Extension field for ``color``.")

    depth: fhirtypes.QuantityType = Field(
        None,
        alias="depth",
        title=(
            "Where applicable, the depth can be specified using a numerical value "
            "and its unit of measurement The unit of measurement shall be specified"
            " in accordance with ISO 11240 and the resulting terminology The symbol"
            " and the symbol identifier shall be used"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    externalDiameter: fhirtypes.QuantityType = Field(
        None,
        alias="externalDiameter",
        title=(
            "Where applicable, the external diameter can be specified using a "
            "numerical value and its unit of measurement The unit of measurement "
            "shall be specified in accordance with ISO 11240 and the resulting "
            "terminology The symbol and the symbol identifier shall be used"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    height: fhirtypes.QuantityType = Field(
        None,
        alias="height",
        title=(
            "Where applicable, the height can be specified using a numerical value "
            "and its unit of measurement The unit of measurement shall be specified"
            " in accordance with ISO 11240 and the resulting terminology The symbol"
            " and the symbol identifier shall be used"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    image: typing.List[fhirtypes.AttachmentType] = Field(
        None,
        alias="image",
        title=(
            "Where applicable, the image can be provided The format of the image "
            "attachment shall be specified by regional implementations"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    imprint: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="imprint",
        title="Where applicable, the imprint can be specified as text",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    imprint__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_imprint", title="Extension field for ``imprint``.")

    nominalVolume: fhirtypes.QuantityType = Field(
        None,
        alias="nominalVolume",
        title=(
            "Where applicable, the nominal volume can be specified using a "
            "numerical value and its unit of measurement The unit of measurement "
            "shall be specified in accordance with ISO 11240 and the resulting "
            "terminology The symbol and the symbol identifier shall be used"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    scoring: fhirtypes.CodeableConceptType = Field(
        None,
        alias="scoring",
        title=(
            "Where applicable, the scoring can be specified An appropriate "
            "controlled vocabulary shall be used The term and the term identifier "
            "shall be used"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    shape: fhirtypes.String = Field(
        None,
        alias="shape",
        title=(
            "Where applicable, the shape can be specified An appropriate controlled"
            " vocabulary shall be used The term and the term identifier shall be "
            "used"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    shape__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_shape", title="Extension field for ``shape``."
    )

    weight: fhirtypes.QuantityType = Field(
        None,
        alias="weight",
        title=(
            "Where applicable, the weight can be specified using a numerical value "
            "and its unit of measurement The unit of measurement shall be specified"
            " in accordance with ISO 11240 and the resulting terminology The symbol"
            " and the symbol identifier shall be used"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    width: fhirtypes.QuantityType = Field(
        None,
        alias="width",
        title=(
            "Where applicable, the width can be specified using a numerical value "
            "and its unit of measurement The unit of measurement shall be specified"
            " in accordance with ISO 11240 and the resulting terminology The symbol"
            " and the symbol identifier shall be used"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ProdCharacteristic`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "height",
            "width",
            "depth",
            "weight",
            "nominalVolume",
            "externalDiameter",
            "shape",
            "color",
            "imprint",
            "image",
            "scoring",
        ]
