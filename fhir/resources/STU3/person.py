# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Person
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Person(domainresource.DomainResource):
    """ A generic person record.
    Demographics and administrative information about a person independent of a
    specific health-related context.
    """

    resource_type = Field("Person", const=True)

    active: bool = Field(
        None,
        alias="active",
        title="Type `bool`",
        description="This person\u0027s record is in active use",
    )

    address: ListType[fhirtypes.AddressType] = Field(
        None,
        alias="address",
        title="List of `Address` items (represented as `dict` in JSON)",
        description="One or more addresses for the person",
    )

    birthDate: fhirtypes.Date = Field(
        None,
        alias="birthDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="The date on which the person was born",
    )

    gender: fhirtypes.Code = Field(
        None,
        alias="gender",
        title="Type `Code` (represented as `dict` in JSON)",
        description="male | female | other | unknown",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="A human identifier for this person",
    )

    link: ListType[fhirtypes.PersonLinkType] = Field(
        None,
        alias="link",
        title="List of `PersonLink` items (represented as `dict` in JSON)",
        description="Link to a resource that concerns the same actual person",
    )

    managingOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="managingOrganization",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="The organization that is the custodian of the person record",
    )

    name: ListType[fhirtypes.HumanNameType] = Field(
        None,
        alias="name",
        title="List of `HumanName` items (represented as `dict` in JSON)",
        description="A name associated with the person",
    )

    photo: fhirtypes.AttachmentType = Field(
        None,
        alias="photo",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="Image of the person",
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="List of `ContactPoint` items (represented as `dict` in JSON)",
        description="A contact detail for the person",
    )


class PersonLink(backboneelement.BackboneElement):
    """ Link to a resource that concerns the same actual person.
    """

    resource_type = Field("PersonLink", const=True)

    assurance: fhirtypes.Code = Field(
        None,
        alias="assurance",
        title="Type `Code` (represented as `dict` in JSON)",
        description="level1 | level2 | level3 | level4",
    )

    target: fhirtypes.ReferenceType = Field(
        ...,
        alias="target",
        title=(
            "Type `Reference` referencing `Patient, Practitioner, RelatedPerson, "
            "Person` (represented as `dict` in JSON)"
        ),
        description="The resource to which this actual person is associated",
    )
