# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Organization
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic.v1 import Field

from . import backboneelement, domainresource, fhirtypes


class Organization(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A grouping of people or organizations with a common purpose.
    A formally or informally recognized grouping of people or organizations
    formed for the purpose of achieving some form of collective action.
    Includes companies, institutions, corporations, departments, community
    groups, healthcare practice groups, etc.
    """

    resource_type = Field("Organization", const=True)

    active: bool = Field(
        None,
        alias="active",
        title="Whether the organization's record is still in active use",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_active", title="Extension field for ``active``."
    )

    address: typing.List[fhirtypes.AddressType] = Field(
        None,
        alias="address",
        title="An address for the organization",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    alias: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="alias",
        title=(
            "A list of\u00a0alternate names that the organization is known as, or was "
            "known as in the past"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    alias__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_alias", title="Extension field for ``alias``.")

    contact: typing.List[fhirtypes.OrganizationContactType] = Field(
        None,
        alias="contact",
        title="Contact for the organization for a certain purpose",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    endpoint: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="endpoint",
        title=(
            "Technical endpoints providing access to services operated for the "
            "organization"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Endpoint"],
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Identifies this organization  across multiple systems",
        description=(
            "Identifier for the organization that is used to identify the "
            "organization across multiple disparate systems."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name used for the organization",
        description="A name associated with the organization.",
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    partOf: fhirtypes.ReferenceType = Field(
        None,
        alias="partOf",
        title="The organization of which this organization forms a part",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    telecom: typing.List[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="A contact detail for the organization",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="Kind of organization",
        description="The kind(s) of organization that this is.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Organization`` according specification,
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
            "identifier",
            "active",
            "type",
            "name",
            "alias",
            "telecom",
            "address",
            "partOf",
            "contact",
            "endpoint",
        ]


class OrganizationContact(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Contact for the organization for a certain purpose.
    """

    resource_type = Field("OrganizationContact", const=True)

    address: fhirtypes.AddressType = Field(
        None,
        alias="address",
        title="Visiting or postal addresses for the contact",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.HumanNameType = Field(
        None,
        alias="name",
        title="A name associated with the contact",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    purpose: fhirtypes.CodeableConceptType = Field(
        None,
        alias="purpose",
        title="The type of contact",
        description="Indicates a purpose for which the contact can be reached.",
        # if property is element of this resource.
        element_property=True,
    )

    telecom: typing.List[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="Contact details (telephone, email, etc.)  for a contact",
        description=(
            "A contact detail (e.g. a telephone number or an email address) by "
            "which the party may be contacted."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``OrganizationContact`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "purpose",
            "name",
            "telecom",
            "address",
        ]
