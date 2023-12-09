# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Coding
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1 import Field

from . import element, fhirtypes


class Coding(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A reference to a code defined by a terminology system.
    """

    resource_type = Field("Coding", const=True)

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Symbol in syntax defined by the system",
        description=(
            "A symbol in syntax defined by the system. The symbol may be a "
            "predefined code or an expression in a syntax defined by the coding "
            "system (e.g. post-coordination)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    display: fhirtypes.String = Field(
        None,
        alias="display",
        title="Representation defined by the system",
        description=(
            "A representation of the meaning of the code in the system, following "
            "the rules of the system."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_display", title="Extension field for ``display``."
    )

    system: fhirtypes.Uri = Field(
        None,
        alias="system",
        title="Identity of the terminology system",
        description=(
            "The identification of the code system that defines the meaning of the "
            "symbol in the code."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_system", title="Extension field for ``system``."
    )

    userSelected: bool = Field(
        None,
        alias="userSelected",
        title="If this coding was chosen directly by the user",
        description=(
            "Indicates that this coding was chosen by a user directly - i.e. off a "
            "pick list of available items (codes or displays)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    userSelected__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_userSelected", title="Extension field for ``userSelected``."
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Version of the system - if relevant",
        description=(
            "The version of the code system which was used when choosing this code."
            " Note that a well-maintained code system does not need the version "
            "reported, because the meaning of codes is consistent across versions. "
            "However this cannot consistently be assured. and when the meaning is "
            "not guaranteed to be consistent, the version SHOULD be exchanged."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Coding`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "system",
            "version",
            "code",
            "display",
            "userSelected",
        ]
