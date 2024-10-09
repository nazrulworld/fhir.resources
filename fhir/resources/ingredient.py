from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Ingredient
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Ingredient(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An ingredient of a manufactured item or pharmaceutical product.
    """

    __resource_type__ = "Ingredient"

    allergenicIndicator: bool | None = Field(  # type: ignore
        None,
        alias="allergenicIndicator",
        title="If the ingredient is a known or suspected allergen",
        description=(
            "If the ingredient is a known or suspected allergen. Note that this is "
            "a property of the substance, so if a reference to a "
            "SubstanceDefinition is used to decribe that (rather than just a code),"
            " the allergen information should go there, not here."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    allergenicIndicator__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_allergenicIndicator",
        title="Extension field for ``allergenicIndicator``.",
    )

    comment: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="comment",
        title=(
            "A place for providing any notes that are relevant to the component, "
            "e.g. removed during process, adjusted for loss on drying"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_comment", title="Extension field for ``comment``."
    )

    for_fhir: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="for",
        title="The product which this ingredient is a constituent part of",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "MedicinalProductDefinition",
                "AdministrableProductDefinition",
                "ManufacturedItemDefinition",
            ],
        },
    )

    function: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="function",
        title=(
            "Precise action within the drug product, e.g. antioxidant, alkalizing "
            "agent"
        ),
        description=(
            "A classification of the ingredient identifying its precise purpose(s) "
            "in the drug product. This extends the Ingredient.role to add more "
            "detail. Example: antioxidant, alkalizing agent."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    group: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="group",
        title=(
            "A classification of the ingredient according to where in the physical "
            "item it tends to be used, such the outer shell of a tablet, inner body"
            " or ink"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="An identifier or code by which the ingredient can be referenced",
        description=(
            "The identifier(s) of this Ingredient that are assigned by business "
            "processes and/or used to refer to it when a direct URL reference to "
            "the resource itself is not appropriate."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    manufacturer: typing.List[fhirtypes.IngredientManufacturerType] | None = Field(  # type: ignore
        None,
        alias="manufacturer",
        title="An organization that manufactures this ingredient",
        description=(
            "The organization(s) that manufacture this ingredient. Can be used to "
            "indicate:         1) Organizations we are aware of that manufacture "
            "this ingredient         2) Specific Manufacturer(s) currently being "
            "used         3) Set of organisations allowed to manufacture this "
            "ingredient for this product         Users must be clear on the "
            "application of context relevant to their use case."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    role: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="role",
        title="Purpose of the ingredient within the product, e.g. active, inactive",
        description=(
            "A classification of the ingredient identifying its purpose within the "
            "product, e.g. active, inactive."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this ingredient. Enables tracking the life-cycle of the "
            "content."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["draft", "active", "retired", "unknown"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    substance: fhirtypes.IngredientSubstanceType = Field(  # type: ignore
        ...,
        alias="substance",
        title="The substance that comprises this ingredient",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Ingredient`` according specification,
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
            "for",
            "role",
            "function",
            "group",
            "allergenicIndicator",
            "comment",
            "manufacturer",
            "substance",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        return required_fields


class IngredientManufacturer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An organization that manufactures this ingredient.
    The organization(s) that manufacture this ingredient. Can be used to
    indicate:         1) Organizations we are aware of that manufacture this
    ingredient         2) Specific Manufacturer(s) currently being used
    3) Set of organisations allowed to manufacture this ingredient for this
    product         Users must be clear on the application of context relevant
    to their use case.
    """

    __resource_type__ = "IngredientManufacturer"

    manufacturer: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="manufacturer",
        title="An organization that manufactures this ingredient",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    role: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="role",
        title="allowed | possible | actual",
        description=(
            "The way in which this manufacturer is associated with the ingredient. "
            "For example whether it is a possible one (others allowed), or an "
            "exclusive authorized one for this ingredient. Note that this is not "
            "the manufacturing process role."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["allowed", "possible", "actual"],
        },
    )
    role__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_role", title="Extension field for ``role``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``IngredientManufacturer`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "role", "manufacturer"]


class IngredientSubstance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The substance that comprises this ingredient.
    """

    __resource_type__ = "IngredientSubstance"

    code: fhirtypes.CodeableReferenceType = Field(  # type: ignore
        ...,
        alias="code",
        title="A code or full resource that represents the ingredient substance",
        description="A code or full resource that represents the ingredient's substance.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["SubstanceDefinition"],
        },
    )

    strength: typing.List[fhirtypes.IngredientSubstanceStrengthType] | None = Field(  # type: ignore
        None,
        alias="strength",
        title=(
            "The quantity of substance, per presentation, or per volume or mass, "
            "and type of quantity"
        ),
        description=(
            "The quantity of substance in the unit of presentation, or in the "
            "volume (or mass) of the single pharmaceutical product or manufactured "
            "item. The allowed repetitions do not represent different strengths, "
            "but are different representations - mathematically equivalent - of a "
            "single strength."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``IngredientSubstance`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "strength"]


class IngredientSubstanceStrength(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The quantity of substance, per presentation, or per volume or mass, and
    type of quantity.
    The quantity of substance in the unit of presentation, or in the volume (or
    mass) of the single pharmaceutical product or manufactured item. The
    allowed repetitions do not represent different strengths, but are different
    representations - mathematically equivalent - of a single strength.
    """

    __resource_type__ = "IngredientSubstanceStrength"

    basis: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="basis",
        title=(
            "A code that indicates if the strength is, for example, based on the "
            "ingredient substance as stated or on the substance base (when the "
            "ingredient is a salt)"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    concentrationCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="concentrationCodeableConcept",
        title="The strength per unitary volume (or mass)",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e concentration[x]
            "one_of_many": "concentration",
            "one_of_many_required": False,
        },
    )

    concentrationQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="concentrationQuantity",
        title="The strength per unitary volume (or mass)",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e concentration[x]
            "one_of_many": "concentration",
            "one_of_many_required": False,
        },
    )

    concentrationRatio: fhirtypes.RatioType | None = Field(  # type: ignore
        None,
        alias="concentrationRatio",
        title="The strength per unitary volume (or mass)",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e concentration[x]
            "one_of_many": "concentration",
            "one_of_many_required": False,
        },
    )

    concentrationRatioRange: fhirtypes.RatioRangeType | None = Field(  # type: ignore
        None,
        alias="concentrationRatioRange",
        title="The strength per unitary volume (or mass)",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e concentration[x]
            "one_of_many": "concentration",
            "one_of_many_required": False,
        },
    )

    country: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="country",
        title="Where the strength range applies",
        description="The country or countries for which the strength range applies.",
        json_schema_extra={
            "element_property": True,
        },
    )

    measurementPoint: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="measurementPoint",
        title="When strength is measured at a particular point or distance",
        description=(
            "For when strength is measured at a particular point or distance. There"
            " are products where strength is measured at a particular point. For "
            "example, the strength of the ingredient in some inhalers is measured "
            "at a particular position relative to the point of aerosolization."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    measurementPoint__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_measurementPoint",
        title="Extension field for ``measurementPoint``.",
    )

    presentationCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="presentationCodeableConcept",
        title="The quantity of substance in the unit of presentation",
        description=(
            "The quantity of substance in the unit of presentation, or in the "
            "volume (or mass) of the single pharmaceutical product or manufactured "
            "item. Unit of presentation refers to the quantity that the item occurs"
            " in e.g. a strength per tablet size, perhaps 'per 20mg' (the size of "
            "the tablet). It is not generally normalized as a unitary unit, which "
            "would be 'per mg')."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e presentation[x]
            "one_of_many": "presentation",
            "one_of_many_required": False,
        },
    )

    presentationQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="presentationQuantity",
        title="The quantity of substance in the unit of presentation",
        description=(
            "The quantity of substance in the unit of presentation, or in the "
            "volume (or mass) of the single pharmaceutical product or manufactured "
            "item. Unit of presentation refers to the quantity that the item occurs"
            " in e.g. a strength per tablet size, perhaps 'per 20mg' (the size of "
            "the tablet). It is not generally normalized as a unitary unit, which "
            "would be 'per mg')."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e presentation[x]
            "one_of_many": "presentation",
            "one_of_many_required": False,
        },
    )

    presentationRatio: fhirtypes.RatioType | None = Field(  # type: ignore
        None,
        alias="presentationRatio",
        title="The quantity of substance in the unit of presentation",
        description=(
            "The quantity of substance in the unit of presentation, or in the "
            "volume (or mass) of the single pharmaceutical product or manufactured "
            "item. Unit of presentation refers to the quantity that the item occurs"
            " in e.g. a strength per tablet size, perhaps 'per 20mg' (the size of "
            "the tablet). It is not generally normalized as a unitary unit, which "
            "would be 'per mg')."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e presentation[x]
            "one_of_many": "presentation",
            "one_of_many_required": False,
        },
    )

    presentationRatioRange: fhirtypes.RatioRangeType | None = Field(  # type: ignore
        None,
        alias="presentationRatioRange",
        title="The quantity of substance in the unit of presentation",
        description=(
            "The quantity of substance in the unit of presentation, or in the "
            "volume (or mass) of the single pharmaceutical product or manufactured "
            "item. Unit of presentation refers to the quantity that the item occurs"
            " in e.g. a strength per tablet size, perhaps 'per 20mg' (the size of "
            "the tablet). It is not generally normalized as a unitary unit, which "
            "would be 'per mg')."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e presentation[x]
            "one_of_many": "presentation",
            "one_of_many_required": False,
        },
    )

    referenceStrength: typing.List[fhirtypes.IngredientSubstanceStrengthReferenceStrengthType] | None = Field(  # type: ignore
        None,
        alias="referenceStrength",
        title="Strength expressed in terms of a reference substance",
        description=(
            "Strength expressed in terms of a reference substance. For when the "
            "ingredient strength is additionally expressed as equivalent to the "
            "strength of some other closely related substance (e.g. salt vs. base)."
            " Reference strength represents the strength (quantitative composition)"
            " of the active moiety of the active substance. There are situations "
            "when the active substance and active moiety are different, therefore "
            "both a strength and a reference strength are needed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    textConcentration: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="textConcentration",
        title=(
            "Text of either the whole concentration strength or a part of it (rest "
            "being in Strength.concentration as a ratio)"
        ),
        description=(
            "A textual represention of either the whole of the concentration "
            "strength or a part of it - with the rest being in "
            "Strength.concentration as a ratio."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    textConcentration__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_textConcentration",
        title="Extension field for ``textConcentration``.",
    )

    textPresentation: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="textPresentation",
        title=(
            "Text of either the whole presentation strength or a part of it (rest "
            "being in Strength.presentation as a ratio)"
        ),
        description=(
            "A textual represention of either the whole of the presentation "
            "strength or a part of it - with the rest being in "
            "Strength.presentation as a ratio."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    textPresentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_textPresentation",
        title="Extension field for ``textPresentation``.",
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``IngredientSubstanceStrength`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "presentationRatio",
            "presentationRatioRange",
            "presentationCodeableConcept",
            "presentationQuantity",
            "textPresentation",
            "concentrationRatio",
            "concentrationRatioRange",
            "concentrationCodeableConcept",
            "concentrationQuantity",
            "textConcentration",
            "basis",
            "measurementPoint",
            "country",
            "referenceStrength",
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
            "concentration": [
                "concentrationCodeableConcept",
                "concentrationQuantity",
                "concentrationRatio",
                "concentrationRatioRange",
            ],
            "presentation": [
                "presentationCodeableConcept",
                "presentationQuantity",
                "presentationRatio",
                "presentationRatioRange",
            ],
        }
        return one_of_many_fields


class IngredientSubstanceStrengthReferenceStrength(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Strength expressed in terms of a reference substance.
    Strength expressed in terms of a reference substance. For when the
    ingredient strength is additionally expressed as equivalent to the strength
    of some other closely related substance (e.g. salt vs. base). Reference
    strength represents the strength (quantitative composition) of the active
    moiety of the active substance. There are situations when the active
    substance and active moiety are different, therefore both a strength and a
    reference strength are needed.
    """

    __resource_type__ = "IngredientSubstanceStrengthReferenceStrength"

    country: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="country",
        title="Where the strength range applies",
        description="The country or countries for which the strength range applies.",
        json_schema_extra={
            "element_property": True,
        },
    )

    measurementPoint: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="measurementPoint",
        title="When strength is measured at a particular point or distance",
        description="For when strength is measured at a particular point or distance.",
        json_schema_extra={
            "element_property": True,
        },
    )
    measurementPoint__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_measurementPoint",
        title="Extension field for ``measurementPoint``.",
    )

    strengthQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="strengthQuantity",
        title="Strength expressed in terms of a reference substance",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e strength[x]
            "one_of_many": "strength",
            "one_of_many_required": True,
        },
    )

    strengthRatio: fhirtypes.RatioType | None = Field(  # type: ignore
        None,
        alias="strengthRatio",
        title="Strength expressed in terms of a reference substance",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e strength[x]
            "one_of_many": "strength",
            "one_of_many_required": True,
        },
    )

    strengthRatioRange: fhirtypes.RatioRangeType | None = Field(  # type: ignore
        None,
        alias="strengthRatioRange",
        title="Strength expressed in terms of a reference substance",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e strength[x]
            "one_of_many": "strength",
            "one_of_many_required": True,
        },
    )

    substance: fhirtypes.CodeableReferenceType = Field(  # type: ignore
        ...,
        alias="substance",
        title="Relevant reference substance",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["SubstanceDefinition"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``IngredientSubstanceStrengthReferenceStrength`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "substance",
            "strengthRatio",
            "strengthRatioRange",
            "strengthQuantity",
            "measurementPoint",
            "country",
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
            "strength": ["strengthQuantity", "strengthRatio", "strengthRatioRange"]
        }
        return one_of_many_fields
