# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Ingredient
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class Ingredient(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An ingredient of a manufactured item or pharmaceutical product.
    """

    resource_type = Field("Ingredient", const=True)

    allergenicIndicator: bool = Field(
        None,
        alias="allergenicIndicator",
        title="If the ingredient is a known or suspected allergen",
        description=(
            "If the ingredient is a known or suspected allergen. Note that this is "
            "a property of the substance, so if a reference to a "
            "SubstanceDefinition is used to decribe that (rather than just a code),"
            " the allergen information should go there, not here."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    allergenicIndicator__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_allergenicIndicator",
        title="Extension field for ``allergenicIndicator``.",
    )

    for_fhir: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="for",
        title="The product which this ingredient is a constituent part of",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "MedicinalProductDefinition",
            "AdministrableProductDefinition",
            "ManufacturedItemDefinition",
        ],
    )

    function: typing.List[fhirtypes.CodeableConceptType] = Field(
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
        # if property is element of this resource.
        element_property=True,
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="An identifier or code by which the ingredient can be referenced",
        description=(
            "The identifier(s) of this Ingredient that are assigned by business "
            "processes and/or used to refer to it when a direct URL reference to "
            "the resource itself is not appropriate."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    manufacturer: typing.List[fhirtypes.IngredientManufacturerType] = Field(
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
        # if property is element of this resource.
        element_property=True,
    )

    role: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="role",
        title="Purpose of the ingredient within the product, e.g. active, inactive",
        description=(
            "A classification of the ingredient identifying its purpose within the "
            "product, e.g. active, inactive."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this ingredient. Enables tracking the life-cycle of the "
            "content."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired", "unknown"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    substance: fhirtypes.IngredientSubstanceType = Field(
        ...,
        alias="substance",
        title="The substance that comprises this ingredient",
        description=None,
        # if property is element of this resource.
        element_property=True,
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
            "allergenicIndicator",
            "manufacturer",
            "substance",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1222(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


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

    resource_type = Field("IngredientManufacturer", const=True)

    manufacturer: fhirtypes.ReferenceType = Field(
        ...,
        alias="manufacturer",
        title="An organization that manufactures this ingredient",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    role: fhirtypes.Code = Field(
        None,
        alias="role",
        title="allowed | possible | actual",
        description=(
            "The way in which this manufacturer is associated with the ingredient. "
            "For example whether it is a possible one (others allowed), or an "
            "exclusive authorized one for this ingredient. Note that this is not "
            "the manufacturing process role."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["allowed", "possible", "actual"],
    )
    role__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    resource_type = Field("IngredientSubstance", const=True)

    code: fhirtypes.CodeableReferenceType = Field(
        ...,
        alias="code",
        title="A code or full resource that represents the ingredient substance",
        description="A code or full resource that represents the ingredient's substance.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SubstanceDefinition"],
    )

    strength: typing.List[fhirtypes.IngredientSubstanceStrengthType] = Field(
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
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("IngredientSubstanceStrength", const=True)

    concentrationRatio: fhirtypes.RatioType = Field(
        None,
        alias="concentrationRatio",
        title="The strength per unitary volume (or mass)",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e concentration[x]
        one_of_many="concentration",
        one_of_many_required=False,
    )

    concentrationRatioRange: fhirtypes.RatioRangeType = Field(
        None,
        alias="concentrationRatioRange",
        title="The strength per unitary volume (or mass)",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e concentration[x]
        one_of_many="concentration",
        one_of_many_required=False,
    )

    country: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="country",
        title="Where the strength range applies",
        description="The country or countries for which the strength range applies.",
        # if property is element of this resource.
        element_property=True,
    )

    measurementPoint: fhirtypes.String = Field(
        None,
        alias="measurementPoint",
        title="When strength is measured at a particular point or distance",
        description=(
            "For when strength is measured at a particular point or distance. There"
            " are products where strength is measured at a particular point. For "
            "example, the strength of the ingredient in some inhalers is measured "
            "at a particular position relative to the point of aerosolization."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    measurementPoint__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_measurementPoint",
        title="Extension field for ``measurementPoint``.",
    )

    presentationRatio: fhirtypes.RatioType = Field(
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e presentation[x]
        one_of_many="presentation",
        one_of_many_required=False,
    )

    presentationRatioRange: fhirtypes.RatioRangeType = Field(
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e presentation[x]
        one_of_many="presentation",
        one_of_many_required=False,
    )

    referenceStrength: typing.List[
        fhirtypes.IngredientSubstanceStrengthReferenceStrengthType
    ] = Field(
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
        # if property is element of this resource.
        element_property=True,
    )

    textConcentration: fhirtypes.String = Field(
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
        # if property is element of this resource.
        element_property=True,
    )
    textConcentration__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_textConcentration",
        title="Extension field for ``textConcentration``.",
    )

    textPresentation: fhirtypes.String = Field(
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
        # if property is element of this resource.
        element_property=True,
    )
    textPresentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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
            "textPresentation",
            "concentrationRatio",
            "concentrationRatioRange",
            "textConcentration",
            "measurementPoint",
            "country",
            "referenceStrength",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2993(
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
            "concentration": ["concentrationRatio", "concentrationRatioRange"],
            "presentation": ["presentationRatio", "presentationRatioRange"],
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

    resource_type = Field("IngredientSubstanceStrengthReferenceStrength", const=True)

    country: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="country",
        title="Where the strength range applies",
        description="The country or countries for which the strength range applies.",
        # if property is element of this resource.
        element_property=True,
    )

    measurementPoint: fhirtypes.String = Field(
        None,
        alias="measurementPoint",
        title="When strength is measured at a particular point or distance",
        description="For when strength is measured at a particular point or distance.",
        # if property is element of this resource.
        element_property=True,
    )
    measurementPoint__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_measurementPoint",
        title="Extension field for ``measurementPoint``.",
    )

    strengthRatio: fhirtypes.RatioType = Field(
        None,
        alias="strengthRatio",
        title="Strength expressed in terms of a reference substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e strength[x]
        one_of_many="strength",
        one_of_many_required=True,
    )

    strengthRatioRange: fhirtypes.RatioRangeType = Field(
        None,
        alias="strengthRatioRange",
        title="Strength expressed in terms of a reference substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e strength[x]
        one_of_many="strength",
        one_of_many_required=True,
    )

    substance: fhirtypes.CodeableReferenceType = Field(
        None,
        alias="substance",
        title="Relevant reference substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SubstanceDefinition"],
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
            "measurementPoint",
            "country",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_4751(
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
        one_of_many_fields = {"strength": ["strengthRatio", "strengthRatioRange"]}
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
