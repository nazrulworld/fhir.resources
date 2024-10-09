from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Substance
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Substance(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A homogeneous material with a definite composition.
    """

    __resource_type__ = "Substance"

    category: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="category",
        title="What class/type of substance this is",
        description=(
            "A code that classifies the general type of substance.  This is used  "
            "for searching, sorting and display purposes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    code: fhirtypes.CodeableReferenceType = Field(  # type: ignore
        ...,
        alias="code",
        title="What substance this is",
        description="A code (or set of codes) that identify this substance.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["SubstanceDefinition"],
        },
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Textual description of the substance, comments",
        description=(
            "A description of the substance - its appearance, handling "
            "requirements, and other usage notes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    expiry: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="expiry",
        title="When no longer valid to use",
        description=(
            "When the substance is no longer valid to use. For some substances, a "
            "single arbitrary date is used for expiry."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    expiry__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_expiry", title="Extension field for ``expiry``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Unique identifier",
        description=(
            "Unique identifier for the substance. For an instance, an identifier "
            "associated with the package/container (usually a label affixed "
            "directly)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    ingredient: typing.List[fhirtypes.SubstanceIngredientType] | None = Field(  # type: ignore
        None,
        alias="ingredient",
        title="Composition information about the substance",
        description="A substance can be composed of other substances.",
        json_schema_extra={
            "element_property": True,
        },
    )

    instance: bool | None = Field(  # type: ignore
        None,
        alias="instance",
        title="Is this an instance of a substance or a kind of one",
        description=(
            "A boolean to indicate if this an instance of a substance or a kind of "
            "one (a definition)."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    instance__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_instance", title="Extension field for ``instance``."
    )

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="Amount of substance in the package",
        description="The amount of the substance.",
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="active | inactive | entered-in-error",
        description="A code to indicate if the substance is actively used.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["active", "inactive", "entered-in-error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
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
            "instance",
            "status",
            "category",
            "code",
            "description",
            "expiry",
            "quantity",
            "ingredient",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("instance", "instance__ext")]
        return required_fields


class SubstanceIngredient(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Composition information about the substance.
    A substance can be composed of other substances.
    """

    __resource_type__ = "SubstanceIngredient"

    quantity: fhirtypes.RatioType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="Optional amount (concentration)",
        description="The amount of the ingredient in the substance - a concentration ratio.",
        json_schema_extra={
            "element_property": True,
        },
    )

    substanceCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="substanceCodeableConcept",
        title="A component of the substance",
        description="Another substance that is a component of this substance.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e substance[x]
            "one_of_many": "substance",
            "one_of_many_required": True,
        },
    )

    substanceReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="substanceReference",
        title="A component of the substance",
        description="Another substance that is a component of this substance.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e substance[x]
            "one_of_many": "substance",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Substance"],
        },
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
            "substance": ["substanceCodeableConcept", "substanceReference"]
        }
        return one_of_many_fields
