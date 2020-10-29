# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Element
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
import typing

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

    extension: typing.List[fhirtypes.ExtensionType] = Field(
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
        # if property is element of this resource.
        element_property=True,
    )

    id: fhirtypes.String = Field(
        None,
        alias="id",
        title="Unique id for inter-element referencing",
        description=(
            "Unique id for the element within a resource (for internal references)."
            " This may be any string value that does not contain spaces."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    id__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_id", title="Extension field for ``id``."
    )
