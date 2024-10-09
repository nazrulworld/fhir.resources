from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Practitioner
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
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
    healthcare or related services.
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

    communication: typing.List[fhirtypes.PractitionerCommunicationType] | None = Field(  # type: ignore
        None,
        alias="communication",
        title="A language which may be used to communicate with the practitioner",
        description=(
            "A language which may be used to communicate with the practitioner, "
            "often for correspondence/administrative purposes.  The "
            "`PractitionerRole.communication` property should be used for "
            "publishing the languages that a practitioner is able to communicate "
            "with patients (on a per Organization/Role basis)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    deceasedBoolean: bool | None = Field(  # type: ignore
        None,
        alias="deceasedBoolean",
        title="Indicates if the practitioner is deceased or not",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e deceased[x]
            "one_of_many": "deceased",
            "one_of_many_required": False,
        },
    )
    deceasedBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_deceasedBoolean", title="Extension field for ``deceasedBoolean``."
    )

    deceasedDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="deceasedDateTime",
        title="Indicates if the practitioner is deceased or not",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e deceased[x]
            "one_of_many": "deceased",
            "one_of_many_required": False,
        },
    )
    deceasedDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_deceasedDateTime",
        title="Extension field for ``deceasedDateTime``.",
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
        title="An identifier for the person as this agent",
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
        title=(
            "Qualifications, certifications, accreditations, licenses, training, "
            "etc. pertaining to the provision of care"
        ),
        description=(
            "The official qualifications, certifications, accreditations, training,"
            " licenses (and other types of educations/skills/capabilities) that "
            "authorize or otherwise pertain to the provision of care by the "
            "practitioner.  For example, a medical license issued by a medical "
            "board of licensure authorizing the practitioner to practice medicine "
            "within a certain locality."
        ),
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
            "gender",
            "birthDate",
            "deceasedBoolean",
            "deceasedDateTime",
            "address",
            "photo",
            "qualification",
            "communication",
        ]

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {"deceased": ["deceasedBoolean", "deceasedDateTime"]}
        return one_of_many_fields


class PractitionerCommunication(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A language which may be used to communicate with the practitioner.
    A language which may be used to communicate with the practitioner, often
    for correspondence/administrative purposes.

    The `PractitionerRole.communication` property should be used for publishing
    the languages that a practitioner is able to communicate with patients (on
    a per Organization/Role basis).
    """

    __resource_type__ = "PractitionerCommunication"

    language: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="language",
        title="The language code used to communicate with the practitioner",
        description=(
            "The ISO-639-1 alpha 2 code in lower case for the language, optionally "
            "followed by a hyphen and the ISO-3166-1 alpha 2 code for the region in"
            ' upper case; e.g. "en" for English, or "en-US" for American English '
            'versus "en-AU" for Australian English.'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    preferred: bool | None = Field(  # type: ignore
        None,
        alias="preferred",
        title="Language preference indicator",
        description=(
            "Indicates whether or not the person prefers this language (over other "
            "languages he masters up a certain level)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    preferred__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_preferred", title="Extension field for ``preferred``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PractitionerCommunication`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "language", "preferred"]


class PractitionerQualification(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Qualifications, certifications, accreditations, licenses, training, etc.
    pertaining to the provision of care.
    The official qualifications, certifications, accreditations, training,
    licenses (and other types of educations/skills/capabilities) that authorize
    or otherwise pertain to the provision of care by the practitioner.

    For example, a medical license issued by a medical board of licensure
    authorizing the practitioner to practice medicine within a certain
    locality.
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
        description="An identifier that applies to this person's qualification.",
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
