from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/SampledData
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import datatype, fhirtypes


class SampledData(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A series of measurements taken by a device.
    A series of measurements taken by a device, with upper and lower limits.
    There may be more than one dimension in the data.
    """

    __resource_type__ = "SampledData"

    codeMap: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="codeMap",
        title="Defines the codes used in the data",
        description="Reference to ConceptMap that defines the codes used in the data.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ConceptMap"],
        },
    )
    codeMap__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_codeMap", title="Extension field for ``codeMap``."
    )

    data: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="data",
        title='Decimal values with spaces, or "E" | "U" | "L", or another code',
        description=(
            "A series of data points which are decimal values or codes separated by"
            ' a single space (character u20). The special codes "E" (error), "L" '
            '(below detection limit) and "U" (above detection limit) are also '
            "defined for used in place of decimal values."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    data__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_data", title="Extension field for ``data``."
    )

    dimensions: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="dimensions",
        title="Number of sample points at each time point",
        description=(
            "The number of sample points at each time point. If this value is "
            "greater than one, then the dimensions will be interlaced - all the "
            "sample points for a point in time will be recorded at once."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    dimensions__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_dimensions", title="Extension field for ``dimensions``."
    )

    factor: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="factor",
        title="Multiply data by this before adding to origin",
        description=(
            "A correction factor that is applied to the sampled data points before "
            "they are added to the origin."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_factor", title="Extension field for ``factor``."
    )

    interval: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="interval",
        title="Number of intervalUnits between samples",
        description=(
            "Amount of intervalUnits between samples, e.g. milliseconds for time-"
            "based sampling."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    interval__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_interval", title="Extension field for ``interval``."
    )

    intervalUnit: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="intervalUnit",
        title="The measurement unit of the interval between samples",
        description="The measurement unit in which the sample interval is expressed.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    intervalUnit__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_intervalUnit", title="Extension field for ``intervalUnit``."
    )

    lowerLimit: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="lowerLimit",
        title="Lower limit of detection",
        description=(
            "The lower limit of detection of the measured points. This is needed if"
            ' any of the data points have the value "L" (lower than detection '
            "limit)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    lowerLimit__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_lowerLimit", title="Extension field for ``lowerLimit``."
    )

    offsets: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="offsets",
        title="Offsets, typically in time, at which data values were taken",
        description=(
            "A series of data points which are decimal values separated by a single"
            " space (character u20).  The units in which the offsets are expressed "
            "are found in intervalUnit.  The absolute point at which the "
            "measurements begin SHALL be conveyed outside the scope of this "
            "datatype, e.g. Observation.effectiveDateTime for a timing offset."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    offsets__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_offsets", title="Extension field for ``offsets``."
    )

    origin: fhirtypes.QuantityType = Field(  # type: ignore
        ...,
        alias="origin",
        title="Zero value and units",
        description=(
            "The base quantity that a measured value of zero represents. In "
            "addition, this provides the units of the entire measurement series."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    upperLimit: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="upperLimit",
        title="Upper limit of detection",
        description=(
            "The upper limit of detection of the measured points. This is needed if"
            ' any of the data points have the value "U" (higher than detection '
            "limit)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    upperLimit__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_upperLimit", title="Extension field for ``upperLimit``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SampledData`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "origin",
            "interval",
            "intervalUnit",
            "factor",
            "lowerLimit",
            "upperLimit",
            "dimensions",
            "codeMap",
            "offsets",
            "data",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("dimensions", "dimensions__ext"),
            ("intervalUnit", "intervalUnit__ext"),
        ]
        return required_fields
