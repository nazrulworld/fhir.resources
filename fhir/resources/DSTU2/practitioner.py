# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Practitioner
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic import Field

from . import fhirtypes
from .backboneelement import BackboneElement
from .domainresource import DomainResource


class Practitioner(DomainResource):
    """A person with a  formal responsibility in the provisioning of healthcare or
    related services.

    A person who is directly or indirectly involved in the provisioning of
    healthcare.
    """

    resource_type = Field("Practitioner", const=True)

    active: fhirtypes.Boolean = Field(
        None,
        alias="active",
        title="Type `Boolean`",
        description="Whether this practitioner's record is in active use.",
    )
    birthDate: fhirtypes.Date = Field(
        None,
        alias="birthDate",
        title="Type `Date`",
        description="The date  on which the practitioner was born.",
    )

    gender: fhirtypes.Code = Field(
        None,
        alias="gender",
        title="Type `Code`",
        description="male | female | other | unknown.",
    )

    name: fhirtypes.HumanNameType = Field(
        None,
        alias="name",
        title="Type `HumanName` (represented as `dict` in JSON).",
        description="A name associated with the person.",
    )

    address: ListType[fhirtypes.AddressType] = Field(
        None,
        alias="address",
        title="Type `Address` (represented as `dict` in JSON).",
        description="Where practitioner can be found/visited.",
    )

    communication: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="communication",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="A language the practitioner is able to use in patient communication.",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON).",
        description="A identifier for the person as this agent.",
    )
    photo: ListType[fhirtypes.AttachmentType] = Field(
        None,
        alias="photo",
        title="List of `Attachment` items (represented as `dict` in JSON).",
        description="Image of the person.",
    )

    practitionerRole: ListType[fhirtypes.PractitionerPractitionerRoleType] = Field(
        None,
        alias="practitionerRole",
        title="List of `PractitionerPractitionerRole` items (represented as `dict` in JSON).",
        description="Roles/organizations the practitioner is associated with.",
    )

    qualification: ListType[fhirtypes.PractitionerQualificationType] = Field(
        None,
        alias="qualification",
        title="List of `PractitionerQualification` items (represented as `dict` in JSON).",
        description="Qualifications obtained by training and certification.",
    )
    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="List of `ContactPoint` items (represented as `dict` in JSON).",
        description="A contact detail for the practitioner.",
    )


class PractitionerPractitionerRole(BackboneElement):
    """Roles/organizations the practitioner is associated with.

    The list of roles/organizations that the practitioner is associated with.
    """

    resource_type = Field("PractitionerPractitionerRole", const=True)

    healthcareService: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="healthcareService",
        title=(
            "List of `Reference` items referencing `HealthcareService`"
            " (represented as `dict` in JSON)."
        ),
        description=(
            "The list of healthcare services that this worker provides for this"
            "role's Organization/Location(s)."
        ),
    )

    location: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="location",
        title=(
            "List of `Reference` items referencing "
            "`Organization` (represented as `dict` in JSON)."
        ),
        description=("The location(s) at which this practitioner provides care."),
    )

    managingOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="managingOrganization",
        title="`Reference` referencing `Organization` (represented as `dict` in JSON).",
        description="Organization where the roles are performed.",
    )
    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON).",
        description=(
            "The period during which the practitioner "
            "is authorized to perform in these role(s)."
        ),
    )

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Roles which this practitioner may perform.",
    )

    specialty: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="specialty",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="Specific specialty of the practitioner.",
    )


class PractitionerQualification(BackboneElement):
    """Qualifications obtained by training and certification."""

    resource_type = Field("PractitionerQualification", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Coded representation of the qualification.",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON).",
        description="An identifier for this qualification for the practitioner.",
    )

    issuer: fhirtypes.ReferenceType = Field(
        None,
        alias="issuer",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON).",
        description="Organization that regulates and issues the qualification.",
    )
    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON).",
        description="Period during which the qualification is valid.",
    )
