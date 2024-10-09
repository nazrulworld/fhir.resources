from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Element
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
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
        title="Additional Content defined by implementations",
        description=(
            "May be used to represent additional information that is not part of "
            "the basic definition of the element. In order to make the use of "
            "extensions safe and manageable, there is a strict set of governance  "
            "applied to the definition and use of extensions. Though any "
            "implementer is allowed to define an extension, there is a set of "
            "requirements that SHALL be met as part of the definition of the "
            "extension."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    id: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="id",
        title="xml:id (or equivalent in JSON)",
        description=(
            "unique id for the element within a resource (for internal references)."
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
