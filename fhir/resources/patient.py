# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Patient
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Patient(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about an individual or animal receiving health care services.
    Demographics and other administrative information about an individual or
    animal receiving care or other health-related services.
    """

    resource_type = Field("Patient", const=True)

    active: bool = Field(
        None,
        alias="active",
        title="Type `bool`",
        description="Whether this patient\u0027s record is in active use",
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_active", title="Extension field for ``active``."
    )

    address: ListType[fhirtypes.AddressType] = Field(
        None,
        alias="address",
        title="List of `Address` items (represented as `dict` in JSON)",
        description="An address for the individual",
    )

    birthDate: fhirtypes.Date = Field(
        None,
        alias="birthDate",
        title="Type `Date`",
        description="The date of birth for the individual",
    )
    birthDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_birthDate", title="Extension field for ``birthDate``."
    )

    communication: ListType[fhirtypes.PatientCommunicationType] = Field(
        None,
        alias="communication",
        title="List of `PatientCommunication` items (represented as `dict` in JSON)",
        description=(
            "A language which may be used to communicate with the patient about his"
            " or her health"
        ),
    )

    contact: ListType[fhirtypes.PatientContactType] = Field(
        None,
        alias="contact",
        title="List of `PatientContact` items (represented as `dict` in JSON)",
        description="A contact party (e.g. guardian, partner, friend) for the patient",
    )

    deceasedBoolean: bool = Field(
        None,
        alias="deceasedBoolean",
        title="Type `bool`",
        description="Indicates if the individual is deceased or not",
        one_of_many="deceased",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    deceasedBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_deceasedBoolean", title="Extension field for ``deceasedBoolean``."
    )

    deceasedDateTime: fhirtypes.DateTime = Field(
        None,
        alias="deceasedDateTime",
        title="Type `DateTime`",
        description="Indicates if the individual is deceased or not",
        one_of_many="deceased",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    deceasedDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_deceasedDateTime",
        title="Extension field for ``deceasedDateTime``.",
    )

    gender: fhirtypes.Code = Field(
        None,
        alias="gender",
        title="Type `Code`",
        description="male | female | other | unknown",
    )
    gender__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_gender", title="Extension field for ``gender``."
    )

    generalPractitioner: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="generalPractitioner",
        title=(
            "List of `Reference` items referencing `Organization, Practitioner, "
            "PractitionerRole` (represented as `dict` in JSON)"
        ),
        description="Patient\u0027s nominated primary care provider",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="An identifier for this patient",
    )

    link: ListType[fhirtypes.PatientLinkType] = Field(
        None,
        alias="link",
        title="List of `PatientLink` items (represented as `dict` in JSON)",
        description="Link to another patient resource that concerns the same actual person",
    )

    managingOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="managingOrganization",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Organization that is the custodian of the patient record",
    )

    maritalStatus: fhirtypes.CodeableConceptType = Field(
        None,
        alias="maritalStatus",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Marital (civil) status of a patient",
    )

    multipleBirthBoolean: bool = Field(
        None,
        alias="multipleBirthBoolean",
        title="Type `bool`",
        description="Whether patient is part of a multiple birth",
        one_of_many="multipleBirth",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    multipleBirthBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_multipleBirthBoolean",
        title="Extension field for ``multipleBirthBoolean``.",
    )

    multipleBirthInteger: fhirtypes.Integer = Field(
        None,
        alias="multipleBirthInteger",
        title="Type `Integer`",
        description="Whether patient is part of a multiple birth",
        one_of_many="multipleBirth",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    multipleBirthInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_multipleBirthInteger",
        title="Extension field for ``multipleBirthInteger``.",
    )

    name: ListType[fhirtypes.HumanNameType] = Field(
        None,
        alias="name",
        title="List of `HumanName` items (represented as `dict` in JSON)",
        description="A name associated with the patient",
    )

    photo: ListType[fhirtypes.AttachmentType] = Field(
        None,
        alias="photo",
        title="List of `Attachment` items (represented as `dict` in JSON)",
        description="Image of the patient",
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="List of `ContactPoint` items (represented as `dict` in JSON)",
        description="A contact detail for the individual",
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
            "deceased": ["deceasedBoolean", "deceasedDateTime"],
            "multipleBirth": ["multipleBirthBoolean", "multipleBirthInteger"],
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


class PatientCommunication(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A language which may be used to communicate with the patient about his or
    her health.
    """

    resource_type = Field("PatientCommunication", const=True)

    language: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="language",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "The language which can be used to communicate with the patient about "
            "his or her health"
        ),
    )

    preferred: bool = Field(
        None,
        alias="preferred",
        title="Type `bool`",
        description="Language preference indicator",
    )
    preferred__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_preferred", title="Extension field for ``preferred``."
    )


class PatientContact(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A contact party (e.g. guardian, partner, friend) for the patient.
    """

    resource_type = Field("PatientContact", const=True)

    address: fhirtypes.AddressType = Field(
        None,
        alias="address",
        title="Type `Address` (represented as `dict` in JSON)",
        description="Address for the contact person",
    )

    gender: fhirtypes.Code = Field(
        None,
        alias="gender",
        title="Type `Code`",
        description="male | female | other | unknown",
    )
    gender__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_gender", title="Extension field for ``gender``."
    )

    name: fhirtypes.HumanNameType = Field(
        None,
        alias="name",
        title="Type `HumanName` (represented as `dict` in JSON)",
        description="A name associated with the contact person",
    )

    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Organization that is associated with the contact",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description=(
            "The period during which this contact person or organization is valid "
            "to be contacted relating to this patient"
        ),
    )

    relationship: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="relationship",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="The kind of relationship",
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="List of `ContactPoint` items (represented as `dict` in JSON)",
        description="A contact detail for the person",
    )


class PatientLink(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Link to another patient resource that concerns the same actual person.
    Link to another patient resource that concerns the same actual patient.
    """

    resource_type = Field("PatientLink", const=True)

    other: fhirtypes.ReferenceType = Field(
        ...,
        alias="other",
        title=(
            "Type `Reference` referencing `Patient, RelatedPerson` (represented as "
            "`dict` in JSON)"
        ),
        description="The other patient or related person resource that the link refers to",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code`",
        description="replaced-by | replaces | refer | seealso",
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )
