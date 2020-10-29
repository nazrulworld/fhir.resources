# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductInteraction
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
import typing

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class MedicinalProductInteraction(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    MedicinalProductInteraction.
    The interactions of the medicinal product with other medicinal products, or
    other forms of interactions.
    """

    resource_type = Field("MedicinalProductInteraction", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="The interaction described",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    effect: fhirtypes.CodeableConceptType = Field(
        None,
        alias="effect",
        title=(
            'The effect of the interaction, for example "reduced gastric absorption'
            ' of primary medication"'
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    incidence: fhirtypes.CodeableConceptType = Field(
        None,
        alias="incidence",
        title="The incidence of the interaction, e.g. theoretical, observed",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    interactant: typing.List[
        fhirtypes.MedicinalProductInteractionInteractantType
    ] = Field(
        None,
        alias="interactant",
        title="The specific medication, food or laboratory test that interacts",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    management: fhirtypes.CodeableConceptType = Field(
        None,
        alias="management",
        title="Actions for managing the interaction",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    subject: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="subject",
        title="The medication for which this is a described interaction",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicinalProduct", "Medication", "Substance"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title=(
            "The type of the interaction e.g. drug-drug interaction, drug-food "
            "interaction, drug-lab test interaction"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class MedicinalProductInteractionInteractant(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The specific medication, food or laboratory test that interacts.
    """

    resource_type = Field("MedicinalProductInteractionInteractant", const=True)

    itemCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="itemCodeableConcept",
        title="The specific medication, food or laboratory test that interacts",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e item[x]
        one_of_many="item",
        one_of_many_required=True,
    )

    itemReference: fhirtypes.ReferenceType = Field(
        None,
        alias="itemReference",
        title="The specific medication, food or laboratory test that interacts",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e item[x]
        one_of_many="item",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "MedicinalProduct",
            "Medication",
            "Substance",
            "ObservationDefinition",
        ],
    )

    @root_validator(pre=True)
    def validate_one_of_many(
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
        one_of_many_fields = {"item": ["itemCodeableConcept", "itemReference"]}
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
