# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/RelatedPerson
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic.v1 import Field

from . import backboneelement, domainresource, fhirtypes


class RelatedPerson(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A person that is related to a patient, but who is not a direct target of
    care.
    Information about a person that is involved in the care for a patient, but
    who is not the target of healthcare, nor has a formal responsibility in the
    care process.
    """

    resource_type = Field("RelatedPerson", const=True)

    active: bool = Field(
        None,
        alias="active",
        title="Whether this related person's record is in active use",
        description="Whether this related person record is in active use.",
        # if property is element of this resource.
        element_property=True,
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_active", title="Extension field for ``active``."
    )

    address: typing.List[fhirtypes.AddressType] = Field(
        None,
        alias="address",
        title="Address where the related person can be contacted or visited",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    birthDate: fhirtypes.Date = Field(
        None,
        alias="birthDate",
        title="The date on which the related person was born",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    birthDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_birthDate", title="Extension field for ``birthDate``."
    )

    communication: typing.List[fhirtypes.RelatedPersonCommunicationType] = Field(
        None,
        alias="communication",
        title=(
            "A language which may be used to communicate with about the patient's "
            "health"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    gender: fhirtypes.Code = Field(
        None,
        alias="gender",
        title="male | female | other | unknown",
        description=(
            "Administrative Gender - the gender that the person is considered to "
            "have for administration and record keeping purposes."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["male", "female", "other", "unknown"],
    )
    gender__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_gender", title="Extension field for ``gender``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="A human identifier for this person",
        description="Identifier for a person within a particular scope.",
        # if property is element of this resource.
        element_property=True,
    )

    name: typing.List[fhirtypes.HumanNameType] = Field(
        None,
        alias="name",
        title="A name associated with the person",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="The patient this person is related to",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Period of time that this relationship is considered valid",
        description=(
            "The period of time during which this relationship is or was active. If"
            " there are no dates defined, then the interval is unknown."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    photo: typing.List[fhirtypes.AttachmentType] = Field(
        None,
        alias="photo",
        title="Image of the person",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    relationship: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="relationship",
        title="The nature of the relationship",
        description=(
            "The nature of the relationship between a patient and the related "
            "person."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    telecom: typing.List[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="A contact detail for the person",
        description=(
            "A contact detail for the person, e.g. a telephone number or an email "
            "address."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``RelatedPerson`` according specification,
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
            "patient",
            "relationship",
            "name",
            "telecom",
            "gender",
            "birthDate",
            "address",
            "photo",
            "period",
            "communication",
        ]


class RelatedPersonCommunication(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A language which may be used to communicate with about the patient's health.
    """

    resource_type = Field("RelatedPersonCommunication", const=True)

    language: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="language",
        title=(
            "The language which can be used to communicate with the patient about "
            "his or her health"
        ),
        description=(
            "The ISO-639-1 alpha 2 code in lower case for the language, optionally "
            "followed by a hyphen and the ISO-3166-1 alpha 2 code for the region in"
            ' upper case; e.g. "en" for English, or "en-US" for American English '
            'versus "en-EN" for England English.'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    preferred: bool = Field(
        None,
        alias="preferred",
        title="Language preference indicator",
        description=(
            "Indicates whether or not the patient prefers this language (over other"
            " languages he masters up a certain level)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    preferred__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_preferred", title="Extension field for ``preferred``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``RelatedPersonCommunication`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "language", "preferred"]
