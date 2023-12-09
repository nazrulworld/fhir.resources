# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Element
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic.v1 import Field

from . import fhirtypes
from .fhirabstractmodel import FHIRAbstractModel


class Element(FHIRAbstractModel):
    """Base for all elements.
    Base definition for all elements in a resource.
    """

    resource_type = Field("Element", const=True)

    extension: ListType[fhirtypes.ExtensionType] = Field(
        None,
        alias="extension",
        title="List of `Extension` items (represented as `dict` in JSON)",
        description="Additional Content defined by implementations",
    )

    id: fhirtypes.String = Field(
        None,
        alias="id",
        title="Type `String` (represented as `dict` in JSON)",
        description="xml:id (or equivalent in JSON)",
    )
