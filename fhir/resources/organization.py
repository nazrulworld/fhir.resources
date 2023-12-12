# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Organization
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
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
    groups, healthcare practice groups, payer/insurer, etc.
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

    alias: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="alias",
        title=(
            "A list of alternate names that the organization is known as, or was "
            "known as in the past"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    alias__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_alias", title="Extension field for ``alias``.")

    contact: typing.List[fhirtypes.ExtendedContactDetailType] = Field(
        None,
        alias="contact",
        title="Official contact details for the Organization",
        description=(
            "The contact details of communication devices available relevant to the"
            " specific Organization. This can include addresses, phone numbers, fax"
            " numbers, mobile numbers, email addresses and web sites."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title=(
            "Additional details about the Organization that could be displayed as "
            "further information to identify the Organization beyond its name"
        ),
        description=(
            "Description of the organization, which helps provide additional "
            "general context on the organization to ensure that the correct "
            "organization is selected."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
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

    qualification: typing.List[fhirtypes.OrganizationQualificationType] = Field(
        None,
        alias="qualification",
        title=(
            "Qualifications, certifications, accreditations, licenses, training, "
            "etc. pertaining to the provision of care"
        ),
        description=(
            "The official certifications, accreditations, training, designations "
            "and licenses that authorize and/or otherwise endorse the provision of "
            "care by the organization.  For example, an approval to provide a type "
            "of services issued by a certifying body (such as the US Joint "
            "Commission) to an organization."
        ),
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
            "description",
            "contact",
            "partOf",
            "endpoint",
            "qualification",
        ]


class OrganizationQualification(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Qualifications, certifications, accreditations, licenses, training, etc.
    pertaining to the provision of care.
    The official certifications, accreditations, training, designations and
    licenses that authorize and/or otherwise endorse the provision of care by
    the organization.

    For example, an approval to provide a type of services issued by a
    certifying body (such as the US Joint Commission) to an organization.
    """

    resource_type = Field("OrganizationQualification", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Coded representation of the qualification",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="An identifier for this qualification for the organization",
        description="An identifier allocated to this qualification for this organization.",
        # if property is element of this resource.
        element_property=True,
    )

    issuer: fhirtypes.ReferenceType = Field(
        None,
        alias="issuer",
        title="Organization that regulates and issues the qualification",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Period during which the qualification is valid",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``OrganizationQualification`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "identifier",
            "code",
            "period",
            "issuer",
        ]
