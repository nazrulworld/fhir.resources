# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/HumanName
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import datatype, fhirtypes


class HumanName(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Name of a human or other living entity - parts and usage.
    A name, normally of a human, that can be used for other living entities
    (e.g. animals but not organizations) that have been assigned names by a
    human and may need the use of name parts or the need for usage information.
    """

    resource_type = Field("HumanName", const=True)

    family: fhirtypes.String = Field(
        None,
        alias="family",
        title="Family name (often called 'Surname')",
        description=(
            "The part of a name that links to the genealogy. In some cultures (e.g."
            " Eritrea) the family name of a son is the first name of his father."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    family__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_family", title="Extension field for ``family``."
    )

    given: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="given",
        title="Given names (not always 'first'). Includes middle names",
        description="Given name.",
        # if property is element of this resource.
        element_property=True,
    )
    given__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_given", title="Extension field for ``given``.")

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Time period when name was/is in use",
        description=(
            "Indicates the period of time when this name was valid for the named "
            "person."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    prefix: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="prefix",
        title="Parts that come before the name",
        description=(
            "Part of the name that is acquired as a title due to academic, legal, "
            "employment or nobility status, etc. and that appears at the start of "
            "the name."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    prefix__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_prefix", title="Extension field for ``prefix``.")

    suffix: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="suffix",
        title="Parts that come after the name",
        description=(
            "Part of the name that is acquired as a title due to academic, legal, "
            "employment or nobility status, etc. and that appears at the end of the"
            " name."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    suffix__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_suffix", title="Extension field for ``suffix``.")

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Text representation of the full name",
        description=(
            "Specifies the entire name as it should be displayed e.g. on an "
            "application UI. This may be provided instead of or as well as the "
            "specific parts."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )

    use: fhirtypes.Code = Field(
        None,
        alias="use",
        title="usual | official | temp | nickname | anonymous | old | maiden",
        description="Identifies the purpose for this name.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "usual",
            "official",
            "temp",
            "nickname",
            "anonymous",
            "old",
            "maiden",
        ],
    )
    use__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_use", title="Extension field for ``use``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``HumanName`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "use",
            "text",
            "family",
            "given",
            "prefix",
            "suffix",
            "period",
        ]
