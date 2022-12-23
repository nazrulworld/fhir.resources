# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Population
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field, root_validator

from . import backboneelement, fhirtypes


class Population(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A definition of a set of people that apply to some clinically related
    context, for example people contraindicated for a certain medication.
    A populatioof people with some set of grouping criteria.
    """

    resource_type = Field("Population", const=True)

    ageCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="ageCodeableConcept",
        title="The age of the specific population",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e age[x]
        one_of_many="age",
        one_of_many_required=False,
    )

    ageRange: fhirtypes.RangeType = Field(
        None,
        alias="ageRange",
        title="The age of the specific population",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e age[x]
        one_of_many="age",
        one_of_many_required=False,
    )

    gender: fhirtypes.CodeableConceptType = Field(
        None,
        alias="gender",
        title="The gender of the specific population",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    physiologicalCondition: fhirtypes.CodeableConceptType = Field(
        None,
        alias="physiologicalCondition",
        title=(
            "The existing physiological conditions of the specific population to "
            "which this applies"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    race: fhirtypes.CodeableConceptType = Field(
        None,
        alias="race",
        title="Race of the specific population",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Population`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "ageRange",
            "ageCodeableConcept",
            "gender",
            "race",
            "physiologicalCondition",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1257(
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
        one_of_many_fields = {"age": ["ageCodeableConcept", "ageRange"]}
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
