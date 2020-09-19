# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Organization
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic import Field

from . import fhirtypes
from .backboneelement import BackboneElement
from .domainresource import DomainResource


class Organization(DomainResource):
    """A grouping of people or organizations with a common purpose.

    A formally or informally recognized grouping of people or organizations
    formed for the purpose of achieving some form of collective action.
    Includes companies, institutions, corporations, departments, community
    groups, healthcare practice groups, etc.
    """

    resource_type = Field("Organization", const=True)

    active: bool = Field(
        None,
        alias="active",
        title="Type `bool`.",
        description="Whether the organization's record is still in active use.",
    )
    address: ListType[fhirtypes.AddressType] = Field(
        None,
        alias="address",
        title="List of `Address` items (represented as `dict` in JSON).",
        description="An address for the organization.",
    )

    contact: ListType[fhirtypes.OrganizationContactType] = Field(
        None,
        alias="contact",
        title="List of `OrganizationContact` items (represented as `dict` in JSON).",
        description="Contact for the organization for a certain purpose.",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON).",
        description="Identifies this organization  across multiple systems.",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`.",
        description="Name used for the organization.",
    )
    partOf: fhirtypes.ReferenceType = Field(
        None,
        alias="partOf",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON).",
        description="The organization of which this organization forms a part.",
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="List of `ContactPoint` items (represented as `dict` in JSON).",
        description="A contact detail for the organization.",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Kind of organization.",
    )


class OrganizationContact(BackboneElement):
    """Contact for the organization for a certain purpose."""

    resource_type = Field("OrganizationContact", const=True)

    address: fhirtypes.AddressType = Field(
        None,
        alias="address",
        title="Type `Address` (represented as `dict` in JSON).",
        description="Visiting or postal addresses for the contact.",
    )

    name: fhirtypes.HumanNameType = Field(
        None,
        alias="name",
        title="Type `HumanName` (represented as `dict` in JSON).",
        description="A name associated with the contact.",
    )

    purpose: fhirtypes.CodeableConceptType = Field(
        None,
        alias="purpose",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="The type of contact.",
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="List of `ContactPoint` items (represented as `dict` in JSON).",
        description="Contact details (telephone, email, etc.)  for a contact.",
    )
