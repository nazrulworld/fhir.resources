from __future__ import annotations as _annotations

import typing

from fhir_core import fhirabstractmodel
from pydantic import Field, model_validator
from pydantic_core import PydanticCustomError

from . import fhirtypes

__author__ = "Md Nazrul Islam"
__email__ = "email2nazrul@gmail.com"


class FHIRPrimitiveExtension(fhirabstractmodel.FHIRAbstractModel):
    """@see: https://www.hl7.org/fhir/extensibility.html
    Extensibility feature for FHIR Primitive Data Types."""

    __resource_type__ = "FHIRPrimitiveExtension"

    id: typing.Optional[fhirtypes.StringType] = Field(
        None,
        alias="id",
        title="Type `String`",
        description="Unique id for inter-element referencing",
        # if property is element of this resource.
        json_schema_extra={"element_property": False},
    )

    extension: typing.Optional[typing.List[fhirtypes.ExtensionType]] = Field(  # type: ignore
        None,
        alias="extension",
        title="List of `Extension` items (represented as `dict` in JSON)",
        description="Additional content defined by implementations",
        # if property is element of this resource.
        json_schema_extra={"element_property": False},
    )

    @model_validator(mode="before")
    def validate_extension_or_fhir_comment_required(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """Conditional Required Validation"""
        extension = values.get("extension", None)
        fhir_comments = values.get("fhir_comments", None)

        if (
            values.get("id", None) is None
            and extension is None
            and fhir_comments is None
        ):
            raise PydanticCustomError(
                "model_validation_format",
                "One of field value is required.",
                {},
            )
        return values

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``FHIRPrimitiveExtension`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension"]
