# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/DSTU2/searchparameter.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic.v1 import Field

from . import domainresource, fhirtypes
from .backboneelement import BackboneElement


class SearchParameter(domainresource.DomainResource):
    """Search Parameter for a resource.

    A search parameter that defines a named search item that can
    be used to search/filter on a resource.
    """

    resource_type = Field("SearchParameter", const=True)

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri` items (represented as `dict` in JSON)",
        description="Absolute URL used to reference this search parameter",
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Informal name for this search parameter",
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired",
        description="The status of this search parameter definition.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired"],
        element_property=True,
    )

    experimental: fhirtypes.Boolean = Field(
        None,
        alias="experimental",
        title="Type `Boolean`",
        description="If for testing purposes, not real usage",
        element_property=True,
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of the publisher (Organization or individual)",
        element_property=True,
    )

    contact: ListType[fhirtypes.SearchParameterContactType] = Field(
        None,
        alias="contact",
        title="Type `SearchParameterContact` (represented as `dict` in JSON).",
        description="The channel on which to report matches to the criteria",
        element_property=True,
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Publication Date(/time)",
        description=(
            "The date (and optionally time) when the search parameter "
            "definition was published. The date must change when the business "
            "version changes, if it does, and it must change if the status code "
            "changes. In addition, it should change when the substantive content "
            "of the search parameter changes."
        ),
        element_property=True,
    )

    requirements: fhirtypes.String = Field(
        None,
        alias="requirements",
        title="Type `String` (represented as `dict` in JSON)",
        description="Why this search parameter is defined",
        element_property=True,
    )

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Type `Code` (represented as `dict` in JSON).",
        description="Code used in URL",
        element_property=True,
    )

    base: fhirtypes.Code = Field(
        None,
        alias="base",
        title="Type `Code` (represented as `dict` in JSON).",
        description="The resource type this search parameter applies to",
        element_property=True,
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON).",
        description="number | date | string | token | reference | composite | quantity | uri",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "number",
            "date",
            "string",
            "token",
            "reference",
            "composite",
            "quantity",
            "uri",
        ],
        element_property=True,
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Documentation for  search parameter",
        element_property=True,
    )

    xpath: fhirtypes.String = Field(
        None,
        alias="xpath",
        title="Type `String` (represented as `dict` in JSON)",
        description="XPath that extracts the values",
        element_property=True,
    )

    xpathUsage: fhirtypes.Code = Field(
        None,
        alias="xpathUsage",
        title="Type `Code` (represented as `dict` in JSON).",
        description="normal | phonetic | nearby | distance | other",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["normal", "phonetic", "nearby", "distance", "other"],
        element_property=True,
    )

    target: ListType[fhirtypes.Code] = Field(
        None,
        alias="target",
        title="List of Type `Code` (represented as `dict` in JSON).",
        description="Types of resource (if a resource reference)",
        element_property=True,
    )


class SearchParameterContact(BackboneElement):
    """Contact details of the publisher


    Contacts to assist a user in finding and communicating with the publisher.
    """

    resource_type = Field("SearchParameterContact", const=True)

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of a individual to contact",
        element_property=True,
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="List of `ContactPoint` items (represented as `dict` in JSON).",
        description="Contact details for individual or publisher.",
        element_property=True,
    )
