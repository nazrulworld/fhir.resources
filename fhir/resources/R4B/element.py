from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Element
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from fhir_core import fhirabstractmodel
from pydantic import Field

from . import fhirtypes


class Element(fhirabstractmodel.FHIRAbstractModel):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Base for all elements.
    Base definition for all elements in a resource.
    """

    __resource_type__ = "Element"

    extension: typing.List[fhirtypes.ExtensionType] | None = Field(  # type: ignore
        None,
        alias="extension",
        title="Additional content defined by implementations",
        description=(
            "May be used to represent additional information that is not part of "
            "the basic definition of the element. To make the use of extensions "
            "safe and manageable, there is a strict set of governance  applied to "
            "the definition and use of extensions. Though any implementer can "
            "define an extension, there is a set of requirements that SHALL be met "
            "as part of the definition of the extension."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    id: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="id",
        title="Unique id for inter-element referencing",
        description=(
            "Unique id for the element within a resource (for internal references)."
            " This may be any string value that does not contain spaces."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Element`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension"]
