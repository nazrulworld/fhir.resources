# -*- coding: utf-8 -*-
"""see: https://www.hl7.org/fhir/extensibility.html
Extensibility feature for FHIR Primitive Data Types.
"""
__author__ = "Md Nazrul Islam<email2nazrul>"

from typing import List as ListType

from pydantic import Field

from . import fhirabstractmodel, fhirtypes


class FHIRPrimitiveExtension(fhirabstractmodel.FHIRAbstractModel):
    """"""

    resource_type = Field("FHIRPrimitiveExtension", const=True)

    id: fhirtypes.String = Field(
        None,
        alias="id",
        title="Type `String`",
        description="Unique id for inter-element referencing",
    )

    extension: ListType[fhirtypes.ExtensionType] = Field(
        ...,
        alias="extension",
        title="List of `Extension` items (represented as `dict` in JSON)",
        description="Additional content defined by implementations",
    )
