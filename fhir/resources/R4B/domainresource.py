# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DomainResource
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic.v1 import Field

from . import fhirtypes, resource


class DomainResource(resource.Resource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A resource with narrative, extensions, and contained resources.
    A resource that includes narrative, extensions, and contained resources.
    """

    resource_type = Field("DomainResource", const=True)

    contained: typing.List[fhirtypes.ResourceType] = Field(
        None,
        alias="contained",
        title="Contained, inline Resources",
        description=(
            "These resources do not have an independent existence apart from the "
            "resource that contains them - they cannot be identified independently,"
            " and nor can they have their own independent transaction scope."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    extension: typing.List[fhirtypes.ExtensionType] = Field(
        None,
        alias="extension",
        title="Additional content defined by implementations",
        description=(
            "May be used to represent additional information that is not part of "
            "the basic definition of the resource. To make the use of extensions "
            "safe and manageable, there is a strict set of governance  applied to "
            "the definition and use of extensions. Though any implementer can "
            "define an extension, there is a set of requirements that SHALL be met "
            "as part of the definition of the extension."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    modifierExtension: typing.List[fhirtypes.ExtensionType] = Field(
        None,
        alias="modifierExtension",
        title="Extensions that cannot be ignored",
        description=(
            "May be used to represent additional information that is not part of "
            "the basic definition of the resource and that modifies the "
            "understanding of the element that contains it and/or the understanding"
            " of the containing element's descendants. Usually modifier elements "
            "provide negation or qualification. To make the use of extensions safe "
            "and manageable, there is a strict set of governance applied to the "
            "definition and use of extensions. Though any implementer is allowed to"
            " define an extension, there is a set of requirements that SHALL be met"
            " as part of the definition of the extension. Applications processing a"
            " resource are required to check for modifier extensions.  Modifier "
            "extensions SHALL NOT change the meaning of any elements on Resource or"
            " DomainResource (including cannot change the meaning of "
            "modifierExtension itself)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    text: fhirtypes.NarrativeType = Field(
        None,
        alias="text",
        title="Text summary of the resource, for human interpretation",
        description=(
            "A human-readable narrative that contains a summary of the resource and"
            " can be used to represent the content of the resource to a human. The "
            "narrative need not encode all the structured data, but is required to "
            'contain sufficient detail to make it "clinically safe" for a human to '
            "just read the narrative. Resource definitions may define what content "
            "should be represented in the narrative to ensure clinical safety."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DomainResource`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
        ]
