# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/HumanName
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import element, fhirtypes


class HumanName(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Name of a human - parts and usage.
    A human's name with the ability to identify parts and usage.
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
        description="A full text representation of the name.",
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
