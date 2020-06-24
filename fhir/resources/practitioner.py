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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A person with a  formal responsibility in the provisioning of healthcare or
    related services.
    A person who is directly or indirectly involved in the provisioning of
    healthcare.
    """

    resource_type = Field("Practitioner", const=True)

    active: bool = Field(
        None,
        alias="active",
        title="Whether this practitioner's record is in active use",
        description=None,
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_active", title="Extension field for ``active``."
    )

    address: ListType[fhirtypes.AddressType] = Field(
        None,
        alias="address",
        title=(
            "Address(es) of the practitioner that are not role specific (typically "
            "home address)"
        ),
        description=(
            "Address(es) of the practitioner that are not role specific (typically "
            "home address).  Work addresses are not typically entered in this "
            "property as they are usually role dependent."
        ),
    )

    birthDate: fhirtypes.Date = Field(
        None,
        alias="birthDate",
        title="The date  on which the practitioner was born",
        description="The date of birth for the practitioner.",
    )
    birthDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_birthDate", title="Extension field for ``birthDate``."
    )

    communication: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="communication",
        title="A language the practitioner can use in patient communication",
        description=None,
    )

    gender: fhirtypes.Code = Field(
        None,
        alias="gender",
        title="male | female | other | unknown",
        description=(
            "Administrative Gender - the gender that the person is considered to "
            "have for administration and record keeping purposes."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["male", "female", "other", "unknown"],
    )
    gender__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_gender", title="Extension field for ``gender``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="An identifier for the person as this agent",
        description="An identifier that applies to this person in this role.",
    )

    name: ListType[fhirtypes.HumanNameType] = Field(
        None,
        alias="name",
        title="The name(s) associated with the practitioner",
        description=None,
    )

    photo: ListType[fhirtypes.AttachmentType] = Field(
        None, alias="photo", title="Image of the person", description=None,
    )

    qualification: ListType[fhirtypes.PractitionerQualificationType] = Field(
        None,
        alias="qualification",
        title=(
            "Certification, licenses, or training pertaining to the provision of "
            "care"
        ),
        description=(
            "The official certifications, training, and licenses that authorize or "
            "otherwise pertain to the provision of care by the practitioner.  For "
            "example, a medical license issued by a medical board authorizing the "
            "practitioner to practice medicine within a certian locality."
        ),
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="A contact detail for the practitioner (that apply to all roles)",
        description=(
            "A contact detail for the practitioner, e.g. a telephone number or an "
            "email address."
        ),
    )


class PractitionerQualification(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Certification, licenses, or training pertaining to the provision of care.
    The official certifications, training, and licenses that authorize or
    otherwise pertain to the provision of care by the practitioner.  For
    example, a medical license issued by a medical board authorizing the
    practitioner to practice medicine within a certian locality.
    """

    resource_type = Field("PractitionerQualification", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Coded representation of the qualification",
        description=None,
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="An identifier for this qualification for the practitioner",
        description=(
            "An identifier that applies to this person's qualification in this " "role."
        ),
    )

    issuer: fhirtypes.ReferenceType = Field(
        None,
        alias="issuer",
        title="Organization that regulates and issues the qualification",
        description=None,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Period during which the qualification is valid",
        description=None,
    )
