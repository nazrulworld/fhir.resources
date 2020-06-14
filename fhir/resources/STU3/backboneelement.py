# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/BackboneElement
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import element, fhirtypes


class BackboneElement(element.Element):
    """ Base for elements defined inside a resource.
    Base definition for all elements that are defined inside a resource - but
    not those in a data type.
    """

    resource_type = Field("BackboneElement", const=True)

    modifierExtension: ListType[fhirtypes.ExtensionType] = Field(
        None,
        alias="modifierExtension",
        title="List of `Extension` items (represented as `dict` in JSON)",
        description="Extensions that cannot be ignored",
    )
