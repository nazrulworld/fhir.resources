from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Coding
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic import Field

from . import element, fhirtypes


class Coding(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A reference to a code defined by a terminology system.
    """

    __resource_type__ = "Coding"

    code: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Symbol in syntax defined by the system",
        description=(
            "A symbol in syntax defined by the system. The symbol may be a "
            "predefined code or an expression in a syntax defined by the coding "
            "system (e.g. post-coordination)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_code", title="Extension field for ``code``."
    )

    display: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="display",
        title="Representation defined by the system",
        description=(
            "A representation of the meaning of the code in the system, following "
            "the rules of the system."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_display", title="Extension field for ``display``."
    )

    system: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="system",
        title="Identity of the terminology system",
        description=(
            "The identification of the code system that defines the meaning of the "
            "symbol in the code."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_system", title="Extension field for ``system``."
    )

    userSelected: bool | None = Field(  # type: ignore
        None,
        alias="userSelected",
        title="If this coding was chosen directly by the user",
        description=(
            "Indicates that this coding was chosen by a user directly - e.g. off a "
            "pick list of available items (codes or displays)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    userSelected__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_userSelected", title="Extension field for ``userSelected``."
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="Version of the system - if relevant",
        description=(
            "The version of the code system which was used when choosing this code."
            " Note that a well-maintained code system does not need the version "
            "reported, because the meaning of codes is consistent across versions. "
            "However this cannot consistently be assured, and when the meaning is "
            "not guaranteed to be consistent, the version SHOULD be exchanged."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
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
