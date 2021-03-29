# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Substance
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Substance(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A homogeneous material with a definite composition.
    """

    resource_type = Field("Substance", const=True)

    category: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="What class/type of substance this is",
        description=(
            "A code that classifies the general type of substance.  This is used  "
            "for searching, sorting and display purposes."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="What substance this is",
        description="A code (or set of codes) that identify this substance.",
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Textual description of the substance, comments",
        description=(
            "A description of the substance - its appearance, handling "
            "requirements, and other usage notes."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Unique identifier",
        description="Unique identifier for the substance.",
        # if property is element of this resource.
        element_property=True,
    )

    ingredient: typing.List[fhirtypes.SubstanceIngredientType] = Field(
        None,
        alias="ingredient",
        title="Composition information about the substance",
        description="A substance can be composed of other substances.",
        # if property is element of this resource.
        element_property=True,
    )

    instance: typing.List[fhirtypes.SubstanceInstanceType] = Field(
        None,
        alias="instance",
        title="If this describes a specific package/container of the substance",
        description=(
            "Substance may be used to describe a kind of substance, or a specific "
            "package/container of the substance: an instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="active | inactive | entered-in-error",
        description="A code to indicate if the substance is actively used.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "inactive", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Substance`` according specification,
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
            "status",
            "category",
            "code",
            "description",
            "instance",
            "ingredient",
        ]


class SubstanceIngredient(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Composition information about the substance.
    A substance can be composed of other substances.
    """

    resource_type = Field("SubstanceIngredient", const=True)

    quantity: fhirtypes.RatioType = Field(
        None,
        alias="quantity",
        title="Optional amount (concentration)",
        description="The amount of the ingredient in the substance - a concentration ratio.",
        # if property is element of this resource.
        element_property=True,
    )

    substanceCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="substanceCodeableConcept",
        title="A component of the substance",
        description="Another substance that is a component of this substance.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e substance[x]
        one_of_many="substance",
        one_of_many_required=True,
    )

    substanceReference: fhirtypes.ReferenceType = Field(
        None,
        alias="substanceReference",
        title="A component of the substance",
        description="Another substance that is a component of this substance.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e substance[x]
        one_of_many="substance",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Substance"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceIngredient`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "quantity",
            "substanceCodeableConcept",
            "substanceReference",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2168(
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
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    If this describes a specific package/container of the substance.
    Substance may be used to describe a kind of substance, or a specific
    package/container of the substance: an instance.
    """

    resource_type = Field("SubstanceInstance", const=True)

    expiry: fhirtypes.DateTime = Field(
        None,
        alias="expiry",
        title="When no longer valid to use",
        description=(
            "When the substance is no longer valid to use. For some substances, a "
            "single arbitrary date is used for expiry."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    expiry__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_expiry", title="Extension field for ``expiry``."
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Identifier of the package/container",
        description=(
            "Identifier associated with the package/container (usually a label "
            "affixed directly)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Amount of substance in the package",
        description="The amount of the substance.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceInstance`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "identifier",
            "expiry",
            "quantity",
        ]
