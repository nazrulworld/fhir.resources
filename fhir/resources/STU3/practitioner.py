from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Practitioner
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Practitioner(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A person with a  formal responsibility in the provisioning of healthcare or
    related services.
    A person who is directly or indirectly involved in the provisioning of
    healthcare.
    """

    __resource_type__ = "Practitioner"

    active: bool | None = Field(  # type: ignore
        None,
        alias="active",
        title="Whether this practitioner's record is in active use",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_active", title="Extension field for ``active``."
    )

    address: typing.List[fhirtypes.AddressType] | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )

    birthDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="birthDate",
        title="The date  on which the practitioner was born",
        description="The date of birth for the practitioner.",
        json_schema_extra={
            "element_property": True,
        },
    )
    birthDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_birthDate", title="Extension field for ``birthDate``."
    )

    communication: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="communication",
        title="A language the practitioner is able to use in patient communication",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    gender: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="gender",
        title="male | female | other | unknown",
        description=(
            "Administrative Gender - the gender that the person is considered to "
            "have for administration and record keeping purposes."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["male", "female", "other", "unknown"],
        },
    )
    gender__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_gender", title="Extension field for ``gender``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="A identifier for the person as this agent",
        description="An identifier that applies to this person in this role.",
        json_schema_extra={
            "element_property": True,
        },
    )

    name: typing.List[fhirtypes.HumanNameType] | None = Field(  # type: ignore
        None,
        alias="name",
        title="The name(s) associated with the practitioner",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    photo: typing.List[fhirtypes.AttachmentType] | None = Field(  # type: ignore
        None,
        alias="photo",
        title="Image of the person",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    qualification: typing.List[fhirtypes.PractitionerQualificationType] | None = Field(  # type: ignore
        None,
        alias="qualification",
        title="Qualifications obtained by training and certification",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    telecom: typing.List[fhirtypes.ContactPointType] | None = Field(  # type: ignore
        None,
        alias="telecom",
        title="A contact detail for the practitioner (that apply to all roles)",
        description=(
            "A contact detail for the practitioner, e.g. a telephone number or an "
            "email address."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Practitioner`` according specification,
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
            "name",
            "telecom",
            "address",
            "gender",
            "birthDate",
            "photo",
            "qualification",
            "communication",
        ]


class PractitionerQualification(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Qualifications obtained by training and certification.
    """

    __resource_type__ = "PractitionerQualification"

    code: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="code",
        title="Coded representation of the qualification",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="An identifier for this qualification for the practitioner",
        description=(
            "An identifier that applies to this person's qualification in this " "role."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    issuer: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="issuer",
        title="Organization that regulates and issues the qualification",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="period",
        title="Period during which the qualification is valid",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PractitionerQualification`` according specification,
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
