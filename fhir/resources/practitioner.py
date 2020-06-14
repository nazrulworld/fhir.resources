# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Practitioner
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Practitioner(domainresource.DomainResource):
    """ A person with a  formal responsibility in the provisioning of healthcare or
    related services.
    A person who is directly or indirectly involved in the provisioning of
    healthcare.
    """

    resource_type = Field("Practitioner", const=True)

    active: bool = Field(
        None,
        alias="active",
        title="Type `bool`",
        description="Whether this practitioner\u0027s record is in active use",
    )

    address: ListType[fhirtypes.AddressType] = Field(
        None,
        alias="address",
        title="List of `Address` items (represented as `dict` in JSON)",
        description="Address(es) of the practitioner that are not role specific (typically home address)",
    )

    birthDate: fhirtypes.Date = Field(
        None,
        alias="birthDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="The date  on which the practitioner was born",
    )

    communication: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="communication",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="A language the practitioner can use in patient communication",
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
        description="An identifier for the person as this agent",
    )

    name: ListType[fhirtypes.HumanNameType] = Field(
        None,
        alias="name",
        title="List of `HumanName` items (represented as `dict` in JSON)",
        description="The name(s) associated with the practitioner",
    )

    photo: ListType[fhirtypes.AttachmentType] = Field(
        None,
        alias="photo",
        title="List of `Attachment` items (represented as `dict` in JSON)",
        description="Image of the person",
    )

    qualification: ListType[fhirtypes.PractitionerQualificationType] = Field(
        None,
        alias="qualification",
        title="List of `PractitionerQualification` items (represented as `dict` in JSON)",
        description="Certification, licenses, or training pertaining to the provision of care",
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="List of `ContactPoint` items (represented as `dict` in JSON)",
        description="A contact detail for the practitioner (that apply to all roles)",
    )


class PractitionerQualification(backboneelement.BackboneElement):
    """ Certification, licenses, or training pertaining to the provision of care.
    The official certifications, training, and licenses that authorize or
    otherwise pertain to the provision of care by the practitioner.  For
    example, a medical license issued by a medical board authorizing the
    practitioner to practice medicine within a certian locality.
    """

    resource_type = Field("PractitionerQualification", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Coded representation of the qualification",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="An identifier for this qualification for the practitioner",
    )

    issuer: fhirtypes.ReferenceType = Field(
        None,
        alias="issuer",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Organization that regulates and issues the qualification",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Period during which the qualification is valid",
    )
