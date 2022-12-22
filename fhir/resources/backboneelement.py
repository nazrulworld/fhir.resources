# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/BackboneElement
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
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
        title="Extensions that cannot be ignored even if unrecognized",
        description=(
            "May be used to represent additional information that is not part of "
            "the basic definition of the element and that modifies the "
            "understanding of the element in which it is contained and/or the "
            "understanding of the containing element's descendants. Usually "
            "modifier elements provide negation or qualification. To make the use "
            "of extensions safe and manageable, there is a strict set of governance"
            " applied to the definition and use of extensions. Though any "
            "implementer can define an extension, there is a set of requirements "
            "that SHALL be met as part of the definition of the extension. "
            "Applications processing a resource are required to check for modifier "
            "extensions.  Modifier extensions SHALL NOT change the meaning of any "
            "elements on Resource or DomainResource (including cannot change the "
            "meaning of modifierExtension itself)."
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
