# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Substance
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Substance(domainresource.DomainResource):
    """ A homogeneous material with a definite composition.
    """

    resource_type = Field("Substance", const=True)

    category: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="What class/type of substance this is",
    )

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="What substance this is",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Textual description of the substance, comments",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Unique identifier",
    )

    ingredient: ListType[fhirtypes.SubstanceIngredientType] = Field(
        None,
        alias="ingredient",
        title="List of `SubstanceIngredient` items (represented as `dict` in JSON)",
        description="Composition information about the substance",
    )

    instance: ListType[fhirtypes.SubstanceInstanceType] = Field(
        None,
        alias="instance",
        title="List of `SubstanceInstance` items (represented as `dict` in JSON)",
        description="If this describes a specific package/container of the substance",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="active | inactive | entered-in-error",
    )


class SubstanceIngredient(backboneelement.BackboneElement):
    """ Composition information about the substance.
    A substance can be composed of other substances.
    """

    resource_type = Field("SubstanceIngredient", const=True)

    quantity: fhirtypes.RatioType = Field(
        None,
        alias="quantity",
        title="Type `Ratio` (represented as `dict` in JSON)",
        description="Optional amount (concentration)",
    )

    substanceCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="substanceCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="A component of the substance",
        one_of_many="substance",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    substanceReference: fhirtypes.ReferenceType = Field(
        None,
        alias="substanceReference",
        title=(
            "Type `Reference` referencing `Substance` (represented as `dict` in "
            "JSON)"
        ),
        description="A component of the substance",
        one_of_many="substance",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
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
            "substance": ["substanceCodeableConcept", "substanceReference"]
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


class SubstanceInstance(backboneelement.BackboneElement):
    """ If this describes a specific package/container of the substance.
    Substance may be used to describe a kind of substance, or a specific
    package/container of the substance: an instance.
    """

    resource_type = Field("SubstanceInstance", const=True)

    expiry: fhirtypes.DateTime = Field(
        None,
        alias="expiry",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When no longer valid to use",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Identifier of the package/container",
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Amount of substance in the package",
    )
