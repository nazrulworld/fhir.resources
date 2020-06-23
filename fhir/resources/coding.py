# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Coding
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from pydantic import Field

from . import element, fhirtypes


class Coding(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A reference to a code defined by a terminology system.
    """

    resource_type = Field("Coding", const=True)

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Type `Code`",
        description="Symbol in syntax defined by the system",
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    display: fhirtypes.String = Field(
        None,
        alias="display",
        title="Type `String`",
        description="Representation defined by the system",
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_display", title="Extension field for ``display``."
    )

    system: fhirtypes.Uri = Field(
        None,
        alias="system",
        title="Type `Uri`",
        description="Identity of the terminology system",
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_system", title="Extension field for ``system``."
    )

    userSelected: bool = Field(
        None,
        alias="userSelected",
        title="Type `bool`",
        description="If this coding was chosen directly by the user",
    )
    userSelected__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_userSelected", title="Extension field for ``userSelected``."
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String`",
        description="Version of the system - if relevant",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )
