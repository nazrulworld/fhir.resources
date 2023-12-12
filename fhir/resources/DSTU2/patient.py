# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Patient
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic.v1 import Field, root_validator

from . import fhirtypes
from .backboneelement import BackboneElement
from .domainresource import DomainResource


class Patient(DomainResource):
    """Information about an individual or animal receiving health care services.

    Demographics and other administrative information about an individual or
    animal receiving care or other health-related services.
    """

    resource_type = Field("Patient", const=True)

    active: fhirtypes.Boolean = Field(
        None,
        alias="active",
        title="Type `bool`.",
        description="Whether this patient's record is in active use.",
    )
    address: ListType[fhirtypes.AddressType] = Field(
        None,
        alias="address",
        title="List of `Address` items (represented as `dict` in JSON).",
        description="Addresses for the individual.",
    )
    animal: fhirtypes.PatientAnimalType = Field(
        None,
        alias="animal",
        title="Type `PatientAnimal` (represented as `dict` in JSON).",
        description="This patient is known to be an animal (non-human).",
    )

    birthDate: fhirtypes.Date = Field(
        None,
        alias="birthDate",
        title="Type `Date`.",
        description="The date of birth for the individual.",
    )

    careProvider: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="careProvider",
        title=(
            "List of `Reference` items referencing"
            " `Organization, Practitioner` (represented as `dict` in JSON)."
        ),
        description="Patient's nominated primary care provider.",
    )
    communication: ListType[fhirtypes.PatientCommunicationType] = Field(
        None,
        alias="communication",
        title=("List of `PatientCommunication` items (represented as `dict` in JSON)."),
        description=(
            "A list of Languages which may be used to "
            "communicate with the patient about his or her health."
        ),
    )

    contact: ListType[fhirtypes.PatientContactType] = Field(
        None,
        alias="contact",
        title=("List of `PatientContact` items (represented as `dict` in JSON)."),
        description=(
            "A contact party (e.g. guardian, partner, friend) for the patient."
        ),
    )

    deceasedBoolean: fhirtypes.Boolean = Field(
        None,
        alias="deceasedBoolean",
        title="Type `bool`.",
        description="Indicates if the individual is deceased or not.",
        one_of_many="deceased",  # Choice of Data Types. i.e deceased[x]
        one_of_many_required=False,
    )
    deceasedDateTime: fhirtypes.DateTime = Field(
        None,
        alias="deceasedDateTime",
        title="Type `DateTime`.",
        description="Indicates if the individual is deceased or not.",
        one_of_many="deceased",  # Choice of Data Types. i.e deceased[x]
        one_of_many_required=False,
    )

    gender: fhirtypes.Code = Field(
        None,
        alias="gender",
        title="Type `Code`.",
        description="male | female | other | unknown.",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON).",
        description="An identifier for this patient.",
    )
    link: ListType[fhirtypes.PatientLinkType] = Field(
        None,
        alias="link",
        title="List of `PatientLink` items (represented as `dict` in JSON).",
        description="Link to another patient resource that concerns the same actual person.",
    )

    managingOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="managingOrganization",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON).",
        description="Organization that is the custodian of the patient record.",
    )

    maritalStatus: fhirtypes.CodeableConceptType = Field(
        None,
        alias="maritalStatus",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Marital (civil) status of a patient.",
    )

    multipleBirthBoolean: fhirtypes.Boolean = Field(
        None,
        alias="multipleBirthBoolean",
        title="Type `Boolean`.",
        description="Whether patient is part of a multiple birth.",
        one_of_many="multiple",  # Choice of Data Types. i.e deceased[x]
        one_of_many_required=False,
    )

    multipleBirthInteger: fhirtypes.Integer = Field(
        None,
        alias="multipleBirthInteger",
        title="Type `Integer`.",
        description="Whether patient is part of a multiple birth.",
        one_of_many="multiple",  # Choice of Data Types. i.e deceased[x]
        one_of_many_required=False,
    )

    name: ListType[fhirtypes.HumanNameType] = Field(
        None,
        alias="name",
        title="List of `HumanName` items (represented as `dict` in JSON).",
        description="A name associated with the patient.",
    )

    photo: ListType[fhirtypes.AttachmentType] = Field(
        None,
        alias="photo",
        title="List of `Attachment` items (represented as `dict` in JSON).",
        description="Image of the patient.",
    )
    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="List of `ContactPoint` items (represented as `dict` in JSON).",
        description="A contact detail for the individual.",
    )

    @root_validator(pre=True)
    def validate_one_of_many(cls, values: Dict[str, Any]) -> Dict[str, Any]:
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
            "multiple": ["multipleBirthBoolean", "multipleBirthInteger"],
            "deceased": ["deceasedBoolean", "deceasedDateTime"],
        }
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values


class PatientAnimal(BackboneElement):
    """This patient is known to be an animal (non-human).

    This patient is known to be an animal.
    """

    resource_type = Field("PatientAnimal", const=True)

    breed: fhirtypes.CodeableConceptType = Field(
        None,
        alias="breed",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="E.g. Poodle, Angus.",
    )

    genderStatus: fhirtypes.CodeableConceptType = Field(
        None,
        alias="genderStatus",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="E.g. Neutered, Intact.",
    )

    species: fhirtypes.CodeableConceptType = Field(
        None,
        alias="species",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="E.g. Dog, Cow.",
    )


class PatientCommunication(BackboneElement):
    """A list of Languages which may be used to communicate with the patient about
    his or her health.

    Languages which may be used to communicate with the patient about his or
    her health.
    """

    resource_type = Field("PatientCommunication", const=True)

    language: fhirtypes.CodeableConceptType = Field(
        None,
        alias="language",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description=(
            "The language which can be used to communicate with the patient"
            "about his or her health."
        ),
    )

    preferred: fhirtypes.Boolean = Field(
        None,
        alias="preferred",
        title="Type `Boolean`.",
        description="Language preference indicator.",
    )


class PatientContact(BackboneElement):
    """A contact party (e.g. guardian, partner, friend) for the patient."""

    resource_type = Field("PatientContact", const=True)

    address: fhirtypes.AddressType = Field(
        None,
        alias="address",
        title="Type `Address` (represented as `dict` in JSON).",
        description=("Address for the contact person."),
    )

    gender: fhirtypes.Code = Field(
        None,
        alias="gender",
        title="Type `Code`.",
        description="male | female | other | unknown.",
    )

    name: fhirtypes.HumanNameType = Field(
        None,
        alias="name",
        title="Type `HumanName` (represented as `dict` in JSON).",
        description="A name associated with the contact person.",
    )
    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON).",
        description="Organization that is associated with the contact.",
    )

    period: fhirtypes.ReferenceType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON).",
        description=(
            "The period during which this contact person or organization is"
            "valid to be contacted relating to this patient."
        ),
    )

    relationship: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="relationship",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="The kind of relationship.",
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="List of `ContactPoint` items (represented as `dict` in JSON).",
        description="A contact detail for the person.",
    )


class PatientLink(BackboneElement):
    """Link to another patient resource that concerns the same actual person.

    Link to another patient resource that concerns the same actual patient.
    """

    resource_type = Field("PatientLink", const=True)

    other: fhirtypes.ReferenceType = Field(
        ...,
        alias="other",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON).",
        description="The other patient resource that the link refers to.",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code`.",
        description="replace | refer | seealso - type of link.",
    )
