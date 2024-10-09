from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/NutritionOrder
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class NutritionOrder(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Diet, formula or nutritional supplement request.
    A request to supply a diet, formula feeding (enteral) or oral nutritional
    supplement to a patient/resident.
    """

    __resource_type__ = "NutritionOrder"

    allergyIntolerance: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="allergyIntolerance",
        title=(
            "List of the patient's food and nutrition-related allergies and "
            "intolerances"
        ),
        description=(
            "A link to a record of allergies or intolerances  which should be "
            "included in the nutrition order."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["AllergyIntolerance"],
        },
    )

    dateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="dateTime",
        title="Date and time the nutrition order was requested",
        description="The date and time that this nutrition order was requested.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    dateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_dateTime", title="Extension field for ``dateTime``."
    )

    encounter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="encounter",
        title="The encounter associated with this nutrition order",
        description=(
            "An encounter that provides additional information about the healthcare"
            " context in which this request is made."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter"],
        },
    )

    enteralFormula: fhirtypes.NutritionOrderEnteralFormulaType | None = Field(  # type: ignore
        None,
        alias="enteralFormula",
        title="Enteral formula components",
        description=(
            "Feeding provided through the gastrointestinal tract via a tube, "
            "catheter, or stoma that delivers nutrition distal to the oral cavity."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    excludeFoodModifier: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="excludeFoodModifier",
        title=(
            "Order-specific modifier about the type of food that should not be " "given"
        ),
        description=(
            "This modifier is used to convey order-specific modifiers about the "
            "type of food that should NOT be given. These can be derived from "
            "patient allergies, intolerances, or preferences such as No Red Meat, "
            "No Soy or No Wheat or  Gluten-Free.  While it should not be necessary "
            "to repeat allergy or intolerance information captured in the "
            "referenced AllergyIntolerance resource in the excludeFoodModifier, "
            "this element may be used to convey additional specificity related to "
            "foods that should be eliminated from the patient\u2019s diet for any "
            "reason.  This modifier applies to the entire nutrition order inclusive"
            " of the oral diet, nutritional supplements and enteral formula "
            "feedings."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    foodPreferenceModifier: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="foodPreferenceModifier",
        title="Order-specific modifier about the type of food that should be given",
        description=(
            "This modifier is used to convey order-specific modifiers about the "
            "type of food that should be given. These can be derived from patient "
            "allergies, intolerances, or preferences such as Halal, Vegan or "
            "Kosher. This modifier applies to the entire nutrition order inclusive "
            "of the oral diet, nutritional supplements and enteral formula "
            "feedings."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Identifiers assigned to this order",
        description=(
            "Identifiers assigned to this order by the order sender or by the order"
            " receiver."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    oralDiet: fhirtypes.NutritionOrderOralDietType | None = Field(  # type: ignore
        None,
        alias="oralDiet",
        title="Oral diet components",
        description="Diet given orally in contrast to enteral (tube) feeding.",
        json_schema_extra={
            "element_property": True,
        },
    )

    orderer: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="orderer",
        title="Who ordered the diet, formula or nutritional supplement",
        description=(
            "The practitioner that holds legal responsibility for ordering the "
            "diet, nutritional supplement, or formula feedings."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner"],
        },
    )

    patient: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="patient",
        title="The person who requires the diet, formula or nutritional supplement",
        description=(
            "The person (patient) who needs the nutrition order for an oral diet, "
            "nutritional supplement and/or enteral or formula feeding."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient"],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title=(
            "proposed | draft | planned | requested | active | on-hold | completed "
            "| cancelled | entered-in-error"
        ),
        description="The workflow status of the nutrition order/request.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "proposed",
                "draft",
                "planned",
                "requested",
                "active",
                "on-hold",
                "completed",
                "cancelled",
                "entered-in-error",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    supplement: typing.List[fhirtypes.NutritionOrderSupplementType] | None = Field(  # type: ignore
        None,
        alias="supplement",
        title="Supplement components",
        description=(
            "Oral nutritional products given in order to add further nutritional "
            "value to the patient's diet."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``NutritionOrder`` according specification,
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
            "patient",
            "encounter",
            "dateTime",
            "orderer",
            "allergyIntolerance",
            "foodPreferenceModifier",
            "excludeFoodModifier",
            "oralDiet",
            "supplement",
            "enteralFormula",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("dateTime", "dateTime__ext")]
        return required_fields


class NutritionOrderEnteralFormula(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Enteral formula components.
    Feeding provided through the gastrointestinal tract via a tube, catheter,
    or stoma that delivers nutrition distal to the oral cavity.
    """

    __resource_type__ = "NutritionOrderEnteralFormula"

    additiveProductName: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="additiveProductName",
        title="Product or brand name of the modular additive",
        description=(
            "The product or brand name of the type of modular component to be added"
            " to the formula."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    additiveProductName__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_additiveProductName",
        title="Extension field for ``additiveProductName``.",
    )

    additiveType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="additiveType",
        title="Type of modular component to add to the feeding",
        description=(
            "Indicates the type of modular component such as protein, carbohydrate,"
            " fat or fiber to be provided in addition to or mixed with the base "
            "formula."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    administration: typing.List[fhirtypes.NutritionOrderEnteralFormulaAdministrationType] | None = Field(  # type: ignore
        None,
        alias="administration",
        title="Formula feeding instruction as structured data",
        description=(
            "Formula administration instructions as structured data.  This "
            "repeating structure allows for changing the administration rate or "
            "volume over time for both bolus and continuous feeding.  An example of"
            " this would be an instruction to increase the rate of continuous "
            "feeding every 2 hours."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    administrationInstruction: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="administrationInstruction",
        title="Formula feeding instructions expressed as text",
        description=(
            "Free text formula administration, feeding instructions or additional "
            "instructions or information."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    administrationInstruction__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_administrationInstruction",
        title="Extension field for ``administrationInstruction``.",
    )

    baseFormulaProductName: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="baseFormulaProductName",
        title="Product or brand name of the enteral or infant formula",
        description=(
            "The product or brand name of the enteral or infant formula product "
            'such as "ACME Adult Standard Formula".'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    baseFormulaProductName__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_baseFormulaProductName",
        title="Extension field for ``baseFormulaProductName``.",
    )

    baseFormulaType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="baseFormulaType",
        title="Type of enteral or infant formula",
        description=(
            "The type of enteral or infant formula such as an adult standard "
            "formula with fiber or a soy-based infant formula."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    caloricDensity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="caloricDensity",
        title="Amount of energy per specified volume that is required",
        description=(
            "The amount of energy (calories) that the formula should provide per "
            "specified volume, typically per mL or fluid oz.  For example, an "
            "infant may require a formula that provides 24 calories per fluid ounce"
            " or an adult may require an enteral formula that provides 1.5 "
            "calorie/mL."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    maxVolumeToDeliver: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="maxVolumeToDeliver",
        title="Upper limit on formula volume per unit of time",
        description=(
            "The maximum total quantity of formula that may be administered to a "
            "subject over the period of time, e.g. 1440 mL over 24 hours."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    routeofAdministration: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="routeofAdministration",
        title="How the formula should enter the patient's gastrointestinal tract",
        description=(
            "The route or physiological path of administration into the patient's "
            "gastrointestinal  tract for purposes of providing the formula feeding,"
            " e.g. nasogastric tube."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``NutritionOrderEnteralFormula`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "baseFormulaType",
            "baseFormulaProductName",
            "additiveType",
            "additiveProductName",
            "caloricDensity",
            "routeofAdministration",
            "administration",
            "maxVolumeToDeliver",
            "administrationInstruction",
        ]


class NutritionOrderEnteralFormulaAdministration(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Formula feeding instruction as structured data.
    Formula administration instructions as structured data.  This repeating
    structure allows for changing the administration rate or volume over time
    for both bolus and continuous feeding.  An example of this would be an
    instruction to increase the rate of continuous feeding every 2 hours.
    """

    __resource_type__ = "NutritionOrderEnteralFormulaAdministration"

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="The volume of formula to provide",
        description=(
            "The volume of formula to provide to the patient per the specified "
            "administration schedule."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    rateQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="rateQuantity",
        title="Speed with which the formula is provided per period of time",
        description=(
            "The rate of administration of formula via a feeding pump, e.g. 60 mL "
            "per hour, according to the specified schedule."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e rate[x]
            "one_of_many": "rate",
            "one_of_many_required": False,
        },
    )

    rateRatio: fhirtypes.RatioType | None = Field(  # type: ignore
        None,
        alias="rateRatio",
        title="Speed with which the formula is provided per period of time",
        description=(
            "The rate of administration of formula via a feeding pump, e.g. 60 mL "
            "per hour, according to the specified schedule."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e rate[x]
            "one_of_many": "rate",
            "one_of_many_required": False,
        },
    )

    schedule: fhirtypes.TimingType | None = Field(  # type: ignore
        None,
        alias="schedule",
        title="Scheduled frequency of enteral feeding",
        description=(
            "The time period and frequency at which the enteral formula should be "
            "delivered to the patient."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``NutritionOrderEnteralFormulaAdministration`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "schedule",
            "quantity",
            "rateQuantity",
            "rateRatio",
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
        one_of_many_fields = {"rate": ["rateQuantity", "rateRatio"]}
        return one_of_many_fields


class NutritionOrderOralDiet(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Oral diet components.
    Diet given orally in contrast to enteral (tube) feeding.
    """

    __resource_type__ = "NutritionOrderOralDiet"

    fluidConsistencyType: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="fluidConsistencyType",
        title="The required consistency of fluids and liquids provided to the patient",
        description=(
            "The required consistency (e.g. honey-thick, nectar-thick, thin, "
            "thickened.) of liquids or fluids served to the patient."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    instruction: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="instruction",
        title="Instructions or additional information about the oral diet",
        description=(
            "Free text or additional instructions or information pertaining to the "
            "oral diet."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    instruction__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_instruction", title="Extension field for ``instruction``."
    )

    nutrient: typing.List[fhirtypes.NutritionOrderOralDietNutrientType] | None = Field(  # type: ignore
        None,
        alias="nutrient",
        title="Required  nutrient modifications",
        description=(
            "Class that defines the quantity and type of nutrient modifications "
            "(for example carbohydrate, fiber or sodium) required for the oral "
            "diet."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    schedule: typing.List[fhirtypes.TimingType] | None = Field(  # type: ignore
        None,
        alias="schedule",
        title="Scheduled frequency of diet",
        description=(
            "The time period and frequency at which the diet should be given.  The "
            "diet should be given for the combination of all schedules if more than"
            " one schedule is present."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    texture: typing.List[fhirtypes.NutritionOrderOralDietTextureType] | None = Field(  # type: ignore
        None,
        alias="texture",
        title="Required  texture modifications",
        description=(
            "Class that describes any texture modifications required for the "
            "patient to safely consume various types of solid foods."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    type: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="type",
        title=(
            "Type of oral diet or diet restrictions that describe what can be "
            "consumed orally"
        ),
        description=(
            "The kind of diet or dietary restriction such as fiber restricted diet "
            "or diabetic diet."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``NutritionOrderOralDiet`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "schedule",
            "nutrient",
            "texture",
            "fluidConsistencyType",
            "instruction",
        ]


class NutritionOrderOralDietNutrient(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Required  nutrient modifications.
    Class that defines the quantity and type of nutrient modifications (for
    example carbohydrate, fiber or sodium) required for the oral diet.
    """

    __resource_type__ = "NutritionOrderOralDietNutrient"

    amount: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="amount",
        title="Quantity of the specified nutrient",
        description="The quantity of the specified nutrient to include in diet.",
        json_schema_extra={
            "element_property": True,
        },
    )

    modifier: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="modifier",
        title="Type of nutrient that is being modified",
        description="The nutrient that is being modified such as carbohydrate or sodium.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``NutritionOrderOralDietNutrient`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "modifier", "amount"]


class NutritionOrderOralDietTexture(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Required  texture modifications.
    Class that describes any texture modifications required for the patient to
    safely consume various types of solid foods.
    """

    __resource_type__ = "NutritionOrderOralDietTexture"

    foodType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="foodType",
        title=(
            "Concepts that are used to identify an entity that is ingested for "
            "nutritional purposes"
        ),
        description=(
            "The food type(s) (e.g. meats, all foods)  that the texture "
            "modification applies to.  This could be all foods types."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    modifier: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="modifier",
        title="Code to indicate how to alter the texture of the foods, e.g. pureed",
        description=(
            "Any texture modifications (for solid foods) that should be made, e.g. "
            "easy to chew, chopped, ground, and pureed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``NutritionOrderOralDietTexture`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "modifier", "foodType"]


class NutritionOrderSupplement(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Supplement components.
    Oral nutritional products given in order to add further nutritional value
    to the patient's diet.
    """

    __resource_type__ = "NutritionOrderSupplement"

    instruction: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="instruction",
        title="Instructions or additional information about the oral supplement",
        description=(
            "Free text or additional instructions or information pertaining to the "
            "oral supplement."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    instruction__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_instruction", title="Extension field for ``instruction``."
    )

    productName: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="productName",
        title="Product or brand name of the nutritional supplement",
        description=(
            'The product or brand name of the nutritional supplement such as "Acme '
            'Protein Shake".'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    productName__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_productName", title="Extension field for ``productName``."
    )

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="Amount of the nutritional supplement",
        description="The amount of the nutritional supplement to be given.",
        json_schema_extra={
            "element_property": True,
        },
    )

    schedule: typing.List[fhirtypes.TimingType] | None = Field(  # type: ignore
        None,
        alias="schedule",
        title="Scheduled frequency of supplement",
        description=(
            "The time period and frequency at which the supplement(s) should be "
            "given.  The supplement should be given for the combination of all "
            "schedules if more than one schedule is present."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Type of supplement product requested",
        description=(
            "The kind of nutritional supplement product required such as a high "
            "protein or pediatric clear liquid supplement."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``NutritionOrderSupplement`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "productName",
            "schedule",
            "quantity",
            "instruction",
        ]
