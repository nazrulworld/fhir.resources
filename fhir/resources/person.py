# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Person
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Person(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A generic person record.
    Demographics and administrative information about a person independent of a
    specific health-related context.
    """

    resource_type = Field("Person", const=True)

    active: bool = Field(
        None,
        alias="active",
        title="This person's record is in active use",
        description="Whether this person's record is in active use.",
        # if property is element of this resource.
        element_property=True,
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_active", title="Extension field for ``active``."
    )

    address: typing.List[fhirtypes.AddressType] = Field(
        None,
        alias="address",
        title="One or more addresses for the person",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    birthDate: fhirtypes.Date = Field(
        None,
        alias="birthDate",
        title="The date on which the person was born",
        description="The birth date for the person.",
        # if property is element of this resource.
        element_property=True,
    )
    birthDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_birthDate", title="Extension field for ``birthDate``."
    )

    communication: typing.List[fhirtypes.PersonCommunicationType] = Field(
        None,
        alias="communication",
        title=(
            "A language which may be used to communicate with the person about his "
            "or her health"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    deceasedBoolean: bool = Field(
        None,
        alias="deceasedBoolean",
        title="Indicates if the individual is deceased or not",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e deceased[x]
        one_of_many="deceased",
        one_of_many_required=False,
    )
    deceasedBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_deceasedBoolean", title="Extension field for ``deceasedBoolean``."
    )

    deceasedDateTime: fhirtypes.DateTime = Field(
        None,
        alias="deceasedDateTime",
        title="Indicates if the individual is deceased or not",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e deceased[x]
        one_of_many="deceased",
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
        title="male | female | other | unknown",
        description="Administrative Gender.",
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

    link: typing.List[fhirtypes.PersonLinkType] = Field(
        None,
        alias="link",
        title="Link to a resource that concerns the same actual person",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    managingOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="managingOrganization",
        title="The organization that is the custodian of the person record",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    maritalStatus: fhirtypes.CodeableConceptType = Field(
        None,
        alias="maritalStatus",
        title="Marital (civil) status of a person",
        description="This field contains a person's most recent marital (civil) status.",
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

    photo: typing.List[fhirtypes.AttachmentType] = Field(
        None,
        alias="photo",
        title="Image of the person",
        description=(
            "An image that can be displayed as a thumbnail of the person to enhance"
            " the identification of the individual."
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
        ``Person`` according specification,
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
            "photo",
            "communication",
            "managingOrganization",
            "link",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_821(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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


class PersonCommunication(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A language which may be used to communicate with the person about his or
    her health.
    """

    resource_type = Field("PersonCommunication", const=True)

    language: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="language",
        title=(
            "The language which can be used to communicate with the person about "
            "his or her health"
        ),
        description=(
            "The ISO-639-1 alpha 2 code in lower case for the language, optionally "
            "followed by a hyphen and the ISO-3166-1 alpha 2 code for the region in"
            ' upper case; e.g. "en" for English, or "en-US" for American English '
            'versus "en-AU" for Australian English.'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    preferred: bool = Field(
        None,
        alias="preferred",
        title="Language preference indicator",
        description=(
            "Indicates whether or not the person prefers this language (over other "
            "languages he masters up a certain level)."
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
        ``PersonCommunication`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "language", "preferred"]


class PersonLink(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Link to a resource that concerns the same actual person.
    """

    resource_type = Field("PersonLink", const=True)

    assurance: fhirtypes.Code = Field(
        None,
        alias="assurance",
        title="level1 | level2 | level3 | level4",
        description=(
            "Level of assurance that this link is associated with the target "
            "resource."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["level1", "level2", "level3", "level4"],
    )
    assurance__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_assurance", title="Extension field for ``assurance``."
    )

    target: fhirtypes.ReferenceType = Field(
        ...,
        alias="target",
        title="The resource to which this actual person is associated",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Practitioner", "RelatedPerson", "Person"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PersonLink`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "target", "assurance"]
