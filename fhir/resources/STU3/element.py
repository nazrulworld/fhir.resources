# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Element
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import fhirabstractmodel, fhirtypes


class Element(fhirabstractmodel.FHIRAbstractModel):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Base for all elements.
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
        title="Type `String`",
        description="xml:id (or equivalent in JSON)",
    )
    id__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_id", title="Extension field for ``id``."
    )
