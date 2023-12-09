# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SampledData
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import element, fhirtypes


class SampledData(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A series of measurements taken by a device.
    A series of measurements taken by a device, with upper and lower limits.
    There may be more than one dimension in the data.
    """

    resource_type = Field("SampledData", const=True)

    data: fhirtypes.String = Field(
        None,
        alias="data",
        title='Decimal values with spaces, or "E" | "U" | "L"',
        description=(
            "A series of data points which are decimal values separated by a single"
            ' space (character u20). The special values "E" (error), "L" (below '
            'detection limit) and "U" (above detection limit) can also be used in '
            "place of a decimal value."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    data__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_data", title="Extension field for ``data``."
    )

    dimensions: fhirtypes.PositiveInt = Field(
        None,
        alias="dimensions",
        title="Number of sample points at each time point",
        description=(
            "The number of sample points at each time point. If this value is "
            "greater than one, then the dimensions will be interlaced - all the "
            "sample points for a point in time will be recorded at once."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    dimensions__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_dimensions", title="Extension field for ``dimensions``."
    )

    factor: fhirtypes.Decimal = Field(
        None,
        alias="factor",
        title="Multiply data by this before adding to origin",
        description=(
            "A correction factor that is applied to the sampled data points before "
            "they are added to the origin."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_factor", title="Extension field for ``factor``."
    )

    lowerLimit: fhirtypes.Decimal = Field(
        None,
        alias="lowerLimit",
        title="Lower limit of detection",
        description=(
            "The lower limit of detection of the measured points. This is needed if"
            ' any of the data points have the value "L" (lower than detection '
            "limit)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    lowerLimit__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lowerLimit", title="Extension field for ``lowerLimit``."
    )

    origin: fhirtypes.QuantityType = Field(
        ...,
        alias="origin",
        title="Zero value and units",
        description=(
            "The base quantity that a measured value of zero represents. In "
            "addition, this provides the units of the entire measurement series."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    period: fhirtypes.Decimal = Field(
        None,
        alias="period",
        title="Number of milliseconds between samples",
        description="The length of time between sampling times, measured in milliseconds.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    period__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_period", title="Extension field for ``period``."
    )

    upperLimit: fhirtypes.Decimal = Field(
        None,
        alias="upperLimit",
        title="Upper limit of detection",
        description=(
            "The upper limit of detection of the measured points. This is needed if"
            ' any of the data points have the value "U" (higher than detection '
            "limit)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    upperLimit__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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
            "period",
            "factor",
            "lowerLimit",
            "upperLimit",
            "dimensions",
            "data",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1268(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("data", "data__ext"),
            ("dimensions", "dimensions__ext"),
            ("period", "period__ext"),
        ]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values
