# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/BackboneElement
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import element, fhirtypes


class BackboneElement(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Base for elements defined inside a resource.
    Base definition for all elements that are defined inside a resource - but
    not those in a data type.
    """

    resource_type = Field("BackboneElement", const=True)

    modifierExtension: typing.List[fhirtypes.ExtensionType] = Field(
        None,
        alias="modifierExtension",
        title="Extensions that cannot be ignored",
        description=(
            "May be used to represent additional information that is not part of "
            "the basic definition of the element, and that modifies the "
            "understanding of the element that contains it. Usually modifier "
            "elements provide negation or qualification. In order to make the use "
            "of extensions safe and manageable, there is a strict set of governance"
            " applied to the definition and use of extensions. Though any "
            "implementer is allowed to define an extension, there is a set of "
            "requirements that SHALL be met as part of the definition of the "
            "extension. Applications processing a resource are required to check "
            "for modifier extensions."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BackboneElement`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension"]
