# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Coding
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic import Field

from . import element, fhirtypes


class Coding(element.Element):
    """ A reference to a code defined by a terminology system.
    """

    resource_type = Field("Coding", const=True)

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Symbol in syntax defined by the system",
    )

    display: fhirtypes.String = Field(
        None,
        alias="display",
        title="Type `String` (represented as `dict` in JSON)",
        description="Representation defined by the system",
    )

    system: fhirtypes.Uri = Field(
        None,
        alias="system",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Identity of the terminology system",
    )

    userSelected: bool = Field(
        None,
        alias="userSelected",
        title="Type `bool`",
        description="If this coding was chosen directly by the user",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String` (represented as `dict` in JSON)",
        description="Version of the system - if relevant",
    )
