# -*- coding: utf-8 -*-
"""
Profile: https://www.hl7.org/fhir/DSTU2/dataelement.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic.v1 import Field

from . import fhirtypes
from .domainresource import DomainResource


class DataElement(DomainResource):
    """Resource data element.

    The formal description of a single piece of information that can be
    gathered and reported.
    """

    resource_type = Field("DataElement", const=True)

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Globally unique logical id for data element.",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON).",
        description="Logical id to reference this data element.",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `str`.",
        description="Logical id for this version of the data element.",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `str`.",
        description="Descriptive label for this element definition.",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="draft | active | retired",
        description="",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired"],
    )

    experimental: fhirtypes.Boolean = Field(
        None,
        alias="experimental",
        title="Type `bool`.",
        description="If for testing purposes, not real usage.",
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Type `str`.",
        description="Name of the publisher (Organization or individual).",
    )

    contact: ListType[fhirtypes.DataElementContactType] = Field(
        None,
        alias="contact",
        title="List of `DataElementContact` items (represented as `dict` in JSON).",
        description="Contact details of the publisher.",
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime` (represented as `str` in JSON).",
        description="Date for this version of the data element.",
    )

    useContext: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="useContext",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="Content intends to support these contexts.",
    )

    copyright: fhirtypes.String = Field(
        None,
        alias="copyright",
        title="Type `str`.",
        description="Use and/or publishing restrictions.",
    )

    stringency: fhirtypes.Code = Field(
        None,
        alias="stringency",
        title="Type `str`.",
        description=(
            "comparable | fully-specified | equivalent "
            "| convertable | scaleable | flexible."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "comparable",
            "fully-specified",
            "equivalent",
            "convertable",
            "scaleable",
            "flexible",
        ],
    )

    mapping: ListType[fhirtypes.DataElementMappingType] = Field(
        None,
        alias="mapping",
        title="List of `DataElementMapping` items (represented as `dict` in JSON).",
        description="External specification mapped to.",
    )

    element: ListType[fhirtypes.ElementDefinitionType] = Field(
        ...,
        alias="element",
        title="List of `ElementDefinition` items (represented as `dict` in JSON).",
        description="Definition of element.",
    )


class DataElementContact(DomainResource):
    """Contact details of the publisher.

    Contacts to assist a user in finding and communicating with the publisher.
    """

    resource_type = Field("DataElementContact", const=True)

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `str`.",
        description="Name of a individual to contact.",
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="List of `ContactPoint` items (represented as `dict` in JSON).",
        description="Contact details for individual or publisher.",
    )


class DataElementMapping(DomainResource):
    """External specification mapped to.

    Identifies a specification (other than a terminology) that the elements
    which make up the DataElement have some correspondence with.
    """

    resource_type = Field("DataElementMapping", const=True)

    identity: fhirtypes.Id = Field(
        ...,
        alias="identity",
        title="Type `str`.",
        description="Internal id when this mapping is used.",
    )

    uri: fhirtypes.Uri = Field(
        None,
        alias="uri",
        title="Type `str`.",
        description="Identifies what this mapping refers to.",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `str`.",
        description="Names what this mapping refers to.",
    )

    comments: fhirtypes.String = Field(
        None,
        alias="comments",
        title="Type `str`.",
        description="Versions, Issues, Scope limitations etc..",
    )
