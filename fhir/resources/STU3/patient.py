from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Patient
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Patient(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about an individual or animal receiving health care services.
    Demographics and other administrative information about an individual or
    animal receiving care or other health-related services.
    """

    __resource_type__ = "Patient"

    active: bool | None = Field(  # type: ignore
        None,
        alias="active",
        title="Whether this patient's record is in active use",
        description="Whether this patient record is in active use.",
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
        title="Addresses for the individual",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    animal: fhirtypes.PatientAnimalType | None = Field(  # type: ignore
        None,
        alias="animal",
        title="This patient is known to be an animal (non-human)",
        description="This patient is known to be an animal.",
        json_schema_extra={
            "element_property": True,
        },
    )

    birthDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="birthDate",
        title="The date of birth for the individual",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    birthDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_birthDate", title="Extension field for ``birthDate``."
    )

    communication: typing.List[fhirtypes.PatientCommunicationType] | None = Field(  # type: ignore
        None,
        alias="communication",
        title=(
            "A list of Languages which may be used to communicate with the patient "
            "about his or her health"
        ),
        description=(
            "Languages which may be used to communicate with the patient about his "
            "or her health."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    contact: typing.List[fhirtypes.PatientContactType] | None = Field(  # type: ignore
        None,
        alias="contact",
        title="A contact party (e.g. guardian, partner, friend) for the patient",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    deceasedBoolean: bool | None = Field(  # type: ignore
        None,
        alias="deceasedBoolean",
        title="Indicates if the individual is deceased or not",
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
        title="Indicates if the individual is deceased or not",
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
            "Administrative Gender - the gender that the patient is considered to "
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

    generalPractitioner: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="generalPractitioner",
        title="Patient's nominated primary care provider",
        description="Patient's nominated care provider.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization", "Practitioner"],
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="An identifier for this patient",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    link: typing.List[fhirtypes.PatientLinkType] | None = Field(  # type: ignore
        None,
        alias="link",
        title="Link to another patient resource that concerns the same actual person",
        description=(
            "Link to another patient resource that concerns the same actual " "patient."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    managingOrganization: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="managingOrganization",
        title="Organization that is the custodian of the patient record",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    maritalStatus: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="maritalStatus",
        title="Marital (civil) status of a patient",
        description="This field contains a patient's most recent marital (civil) status.",
        json_schema_extra={
            "element_property": True,
        },
    )

    multipleBirthBoolean: bool | None = Field(  # type: ignore
        None,
        alias="multipleBirthBoolean",
        title="Whether patient is part of a multiple birth",
        description=(
            "Indicates whether the patient is part of a multiple (bool) or "
            "indicates the actual birth order (integer)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e multipleBirth[x]
            "one_of_many": "multipleBirth",
            "one_of_many_required": False,
        },
    )
    multipleBirthBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_multipleBirthBoolean",
        title="Extension field for ``multipleBirthBoolean``.",
    )

    multipleBirthInteger: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="multipleBirthInteger",
        title="Whether patient is part of a multiple birth",
        description=(
            "Indicates whether the patient is part of a multiple (bool) or "
            "indicates the actual birth order (integer)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e multipleBirth[x]
            "one_of_many": "multipleBirth",
            "one_of_many_required": False,
        },
    )
    multipleBirthInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_multipleBirthInteger",
        title="Extension field for ``multipleBirthInteger``.",
    )

    name: typing.List[fhirtypes.HumanNameType] | None = Field(  # type: ignore
        None,
        alias="name",
        title="A name associated with the patient",
        description="A name associated with the individual.",
        json_schema_extra={
            "element_property": True,
        },
    )

    photo: typing.List[fhirtypes.AttachmentType] | None = Field(  # type: ignore
        None,
        alias="photo",
        title="Image of the patient",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    telecom: typing.List[fhirtypes.ContactPointType] | None = Field(  # type: ignore
        None,
        alias="telecom",
        title="A contact detail for the individual",
        description=(
            "A contact detail (e.g. a telephone number or an email address) by "
            "which the individual may be contacted."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Patient`` according specification,
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
            "maritalStatus",
            "multipleBirthBoolean",
            "multipleBirthInteger",
            "photo",
            "contact",
            "animal",
            "communication",
            "generalPractitioner",
            "managingOrganization",
            "link",
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
        one_of_many_fields = {
            "deceased": ["deceasedBoolean", "deceasedDateTime"],
            "multipleBirth": ["multipleBirthBoolean", "multipleBirthInteger"],
        }
        return one_of_many_fields


class PatientAnimal(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    This patient is known to be an animal (non-human).
    This patient is known to be an animal.
    """

    __resource_type__ = "PatientAnimal"

    breed: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="breed",
        title="E.g. Poodle, Angus",
        description="Identifies the detailed categorization of the kind of animal.",
        json_schema_extra={
            "element_property": True,
        },
    )

    genderStatus: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="genderStatus",
        title="E.g. Neutered, Intact",
        description="Indicates the current state of the animal's reproductive organs.",
        json_schema_extra={
            "element_property": True,
        },
    )

    species: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="species",
        title="E.g. Dog, Cow",
        description=(
            "Identifies the high level taxonomic categorization of the kind of "
            "animal."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PatientAnimal`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "species",
            "breed",
            "genderStatus",
        ]


class PatientCommunication(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A list of Languages which may be used to communicate with the patient about
    his or her health.
    Languages which may be used to communicate with the patient about his or
    her health.
    """

    __resource_type__ = "PatientCommunication"

    language: fhirtypes.CodeableConceptType = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )

    preferred: bool | None = Field(  # type: ignore
        None,
        alias="preferred",
        title="Language preference indicator",
        description=(
            "Indicates whether or not the patient prefers this language (over other"
            " languages he masters up a certain level)."
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
        ``PatientCommunication`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "language", "preferred"]


class PatientContact(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A contact party (e.g. guardian, partner, friend) for the patient.
    """

    __resource_type__ = "PatientContact"

    address: fhirtypes.AddressType | None = Field(  # type: ignore
        None,
        alias="address",
        title="Address for the contact person",
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
            "Administrative Gender - the gender that the contact person is "
            "considered to have for administration and record keeping purposes."
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

    name: fhirtypes.HumanNameType | None = Field(  # type: ignore
        None,
        alias="name",
        title="A name associated with the contact person",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    organization: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="organization",
        title="Organization that is associated with the contact",
        description=(
            "Organization on behalf of which the contact is acting or for which the"
            " contact is working."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="period",
        title=(
            "The period during which this contact person or organization is valid "
            "to be contacted relating to this patient"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    relationship: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="relationship",
        title="The kind of relationship",
        description=(
            "The nature of the relationship between the patient and the contact "
            "person."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    telecom: typing.List[fhirtypes.ContactPointType] | None = Field(  # type: ignore
        None,
        alias="telecom",
        title="A contact detail for the person",
        description=(
            "A contact detail for the person, e.g. a telephone number or an email "
            "address."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PatientContact`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "relationship",
            "name",
            "telecom",
            "address",
            "gender",
            "organization",
            "period",
        ]


class PatientLink(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Link to another patient resource that concerns the same actual person.
    Link to another patient resource that concerns the same actual patient.
    """

    __resource_type__ = "PatientLink"

    other: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="other",
        title="The other patient or related person resource that the link refers to",
        description="The other patient resource that the link refers to.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "RelatedPerson"],
        },
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="replaced-by | replaces | refer | seealso - type of link",
        description=(
            "The type of link between this patient resource and another patient "
            "resource."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["replaced-by", "replaces", "refer", "seealso"],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PatientLink`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "other", "type"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("type", "type__ext")]
        return required_fields
