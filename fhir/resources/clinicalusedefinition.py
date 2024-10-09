from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ClinicalUseDefinition
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ClinicalUseDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A single issue - either an indication, contraindication, interaction or an
    undesirable effect for a medicinal product, medication, device or procedure.
    """

    __resource_type__ = "ClinicalUseDefinition"

    category: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="category",
        title=(
            "A categorisation of the issue, primarily for dividing warnings into "
            'subject heading areas such as "Pregnancy", "Overdose"'
        ),
        description=(
            "A categorisation of the issue, primarily for dividing warnings into "
            'subject heading areas such as "Pregnancy and Lactation", "Overdose", '
            '"Effects on Ability to Drive and Use Machines".'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    contraindication: fhirtypes.ClinicalUseDefinitionContraindicationType | None = Field(  # type: ignore
        None,
        alias="contraindication",
        title="Specifics for when this is a contraindication",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business identifier for this issue",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    indication: fhirtypes.ClinicalUseDefinitionIndicationType | None = Field(  # type: ignore
        None,
        alias="indication",
        title="Specifics for when this is an indication",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    interaction: fhirtypes.ClinicalUseDefinitionInteractionType | None = Field(  # type: ignore
        None,
        alias="interaction",
        title="Specifics for when this is an interaction",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    library: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="library",
        title="Logic used by the clinical use definition",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Library"],
        },
    )
    library__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_library", title="Extension field for ``library``."
    )

    population: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="population",
        title="The population group to which this applies",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Group"],
        },
    )

    status: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="status",
        title="Whether this is a current issue or one that has been retired etc",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    subject: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="subject",
        title=(
            "The medication, product, substance, device, procedure etc. for which "
            "this is an indication"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "MedicinalProductDefinition",
                "Medication",
                "ActivityDefinition",
                "PlanDefinition",
                "Device",
                "DeviceDefinition",
                "Substance",
                "NutritionProduct",
                "BiologicallyDerivedProduct",
            ],
        },
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title=(
            "indication | contraindication | interaction | undesirable-effect | "
            "warning"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "indication",
                "contraindication",
                "interaction",
                "undesirable-effect",
                "warning",
            ],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    undesirableEffect: fhirtypes.ClinicalUseDefinitionUndesirableEffectType | None = Field(  # type: ignore
        None,
        alias="undesirableEffect",
        title="A possible negative outcome from the use of this treatment",
        description=(
            "Describe the possible undesirable effects (negative outcomes) from the"
            " use of the medicinal product as treatment."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    warning: fhirtypes.ClinicalUseDefinitionWarningType | None = Field(  # type: ignore
        None,
        alias="warning",
        title=(
            "Critical environmental, health or physical risks or hazards. For "
            "example 'Do not operate heavy machinery', 'May cause drowsiness'"
        ),
        description=(
            "A critical piece of information about environmental, health or "
            "physical risks or hazards that serve as caution to the user. For "
            "example 'Do not operate heavy machinery', 'May cause drowsiness', or "
            "'Get medical advice/attention if you feel unwell'."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClinicalUseDefinition`` according specification,
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
            "type",
            "category",
            "subject",
            "status",
            "contraindication",
            "indication",
            "interaction",
            "population",
            "library",
            "undesirableEffect",
            "warning",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("type", "type__ext")]
        return required_fields


class ClinicalUseDefinitionContraindication(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Specifics for when this is a contraindication.
    """

    __resource_type__ = "ClinicalUseDefinitionContraindication"

    applicability: fhirtypes.ExpressionType | None = Field(  # type: ignore
        None,
        alias="applicability",
        title=(
            "An expression that returns true or false, indicating whether the "
            "indication is applicable or not, after having applied its other "
            "elements"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    comorbidity: typing.List[fhirtypes.CodeableReferenceType] | None = Field(  # type: ignore
        None,
        alias="comorbidity",
        title="A comorbidity (concurrent condition) or coinfection",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ObservationDefinition"],
        },
    )

    diseaseStatus: fhirtypes.CodeableReferenceType | None = Field(  # type: ignore
        None,
        alias="diseaseStatus",
        title="The status of the disease or symptom for the contraindication",
        description=(
            "The status of the disease or symptom for the contraindication, for "
            'example "chronic" or "metastatic".'
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ObservationDefinition"],
        },
    )

    diseaseSymptomProcedure: fhirtypes.CodeableReferenceType | None = Field(  # type: ignore
        None,
        alias="diseaseSymptomProcedure",
        title=(
            "The situation that is being documented as contraindicating against "
            "this item"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ObservationDefinition"],
        },
    )

    indication: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="indication",
        title="The indication which this is a contraidication for",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ClinicalUseDefinition"],
        },
    )

    otherTherapy: typing.List[fhirtypes.ClinicalUseDefinitionContraindicationOtherTherapyType] | None = Field(  # type: ignore
        None,
        alias="otherTherapy",
        title=(
            "Information about use of the product in relation to other therapies "
            "described as part of the contraindication"
        ),
        description=(
            "Information about the use of the medicinal product in relation to "
            "other therapies described as part of the contraindication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClinicalUseDefinitionContraindication`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "diseaseSymptomProcedure",
            "diseaseStatus",
            "comorbidity",
            "indication",
            "applicability",
            "otherTherapy",
        ]


class ClinicalUseDefinitionContraindicationOtherTherapy(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about use of the product in relation to other therapies
    described as part of the contraindication.
    Information about the use of the medicinal product in relation to other
    therapies described as part of the contraindication.
    """

    __resource_type__ = "ClinicalUseDefinitionContraindicationOtherTherapy"

    relationshipType: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="relationshipType",
        title=(
            "The type of relationship between the product "
            "indication/contraindication and another therapy"
        ),
        description=(
            "The type of relationship between the medicinal product indication or "
            "contraindication and another therapy."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    treatment: fhirtypes.CodeableReferenceType = Field(  # type: ignore
        ...,
        alias="treatment",
        title=(
            "Reference to a specific medication, substance etc. as part of an "
            "indication or contraindication"
        ),
        description=(
            "Reference to a specific medication (active substance, medicinal "
            "product or class of products, biological, food etc.) as part of an "
            "indication or contraindication."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "MedicinalProductDefinition",
                "Medication",
                "Substance",
                "SubstanceDefinition",
                "NutritionProduct",
                "BiologicallyDerivedProduct",
                "ActivityDefinition",
            ],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClinicalUseDefinitionContraindicationOtherTherapy`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "relationshipType", "treatment"]


class ClinicalUseDefinitionIndication(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Specifics for when this is an indication.
    """

    __resource_type__ = "ClinicalUseDefinitionIndication"

    applicability: fhirtypes.ExpressionType | None = Field(  # type: ignore
        None,
        alias="applicability",
        title=(
            "An expression that returns true or false, indicating whether the "
            "indication is applicable or not, after having applied its other "
            "elements"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    comorbidity: typing.List[fhirtypes.CodeableReferenceType] | None = Field(  # type: ignore
        None,
        alias="comorbidity",
        title="A comorbidity or coinfection as part of the indication",
        description=(
            "A comorbidity (concurrent condition) or coinfection as part of the "
            "indication."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ObservationDefinition"],
        },
    )

    diseaseStatus: fhirtypes.CodeableReferenceType | None = Field(  # type: ignore
        None,
        alias="diseaseStatus",
        title="The status of the disease or symptom for the indication",
        description=(
            "The status of the disease or symptom for the indication, for example "
            '"chronic" or "metastatic".'
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ObservationDefinition"],
        },
    )

    diseaseSymptomProcedure: fhirtypes.CodeableReferenceType | None = Field(  # type: ignore
        None,
        alias="diseaseSymptomProcedure",
        title="The situation that is being documented as an indicaton for this item",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ObservationDefinition"],
        },
    )

    durationRange: fhirtypes.RangeType | None = Field(  # type: ignore
        None,
        alias="durationRange",
        title="Timing or duration information",
        description=(
            "Timing or duration information, that may be associated with use with "
            "the indicated condition e.g. Adult patients suffering from myocardial "
            "infarction (from a few days until less than 35 days), ischaemic stroke"
            " (from 7 days until less than 6 months)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e duration[x]
            "one_of_many": "duration",
            "one_of_many_required": False,
        },
    )

    durationString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="durationString",
        title="Timing or duration information",
        description=(
            "Timing or duration information, that may be associated with use with "
            "the indicated condition e.g. Adult patients suffering from myocardial "
            "infarction (from a few days until less than 35 days), ischaemic stroke"
            " (from 7 days until less than 6 months)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e duration[x]
            "one_of_many": "duration",
            "one_of_many_required": False,
        },
    )
    durationString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_durationString", title="Extension field for ``durationString``."
    )

    intendedEffect: fhirtypes.CodeableReferenceType | None = Field(  # type: ignore
        None,
        alias="intendedEffect",
        title="The intended effect, aim or strategy to be achieved",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ObservationDefinition"],
        },
    )

    otherTherapy: typing.List[fhirtypes.ClinicalUseDefinitionContraindicationOtherTherapyType] | None = Field(  # type: ignore
        None,
        alias="otherTherapy",
        title=(
            "The use of the medicinal product in relation to other therapies "
            "described as part of the indication"
        ),
        description=(
            "Information about the use of the medicinal product in relation to "
            "other therapies described as part of the indication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    undesirableEffect: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="undesirableEffect",
        title=(
            "An unwanted side effect or negative outcome of the subject of this "
            "resource when being used for this indication"
        ),
        description=(
            "An unwanted side effect or negative outcome that may happen if you use"
            " the drug (or other subject of this resource) for this indication."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ClinicalUseDefinition"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClinicalUseDefinitionIndication`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "diseaseSymptomProcedure",
            "diseaseStatus",
            "comorbidity",
            "intendedEffect",
            "durationRange",
            "durationString",
            "undesirableEffect",
            "applicability",
            "otherTherapy",
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
        one_of_many_fields = {"duration": ["durationRange", "durationString"]}
        return one_of_many_fields


class ClinicalUseDefinitionInteraction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Specifics for when this is an interaction.
    """

    __resource_type__ = "ClinicalUseDefinitionInteraction"

    effect: fhirtypes.CodeableReferenceType | None = Field(  # type: ignore
        None,
        alias="effect",
        title=(
            'The effect of the interaction, for example "reduced gastric absorption'
            ' of primary medication"'
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ObservationDefinition"],
        },
    )

    incidence: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="incidence",
        title="The incidence of the interaction, e.g. theoretical, observed",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    interactant: typing.List[fhirtypes.ClinicalUseDefinitionInteractionInteractantType] | None = Field(  # type: ignore
        None,
        alias="interactant",
        title=(
            "The specific medication, product, food etc. or laboratory test that "
            "interacts"
        ),
        description=(
            "The specific medication, product, food, substance etc. or laboratory "
            "test that interacts."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    management: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="management",
        title="Actions for managing the interaction",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title=(
            "The type of the interaction e.g. drug-drug interaction, drug-lab test "
            "interaction"
        ),
        description=(
            "The type of the interaction e.g. drug-drug interaction, drug-food "
            "interaction, drug-lab test interaction."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClinicalUseDefinitionInteraction`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "interactant",
            "type",
            "effect",
            "incidence",
            "management",
        ]


class ClinicalUseDefinitionInteractionInteractant(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The specific medication, product, food etc. or laboratory test that
    interacts.
    The specific medication, product, food, substance etc. or laboratory test
    that interacts.
    """

    __resource_type__ = "ClinicalUseDefinitionInteractionInteractant"

    itemCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="itemCodeableConcept",
        title=(
            "The specific medication, product, food etc. or laboratory test that "
            "interacts"
        ),
        description=(
            "The specific medication, product, food, substance etc. or laboratory "
            "test that interacts."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e item[x]
            "one_of_many": "item",
            "one_of_many_required": True,
        },
    )

    itemReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="itemReference",
        title=(
            "The specific medication, product, food etc. or laboratory test that "
            "interacts"
        ),
        description=(
            "The specific medication, product, food, substance etc. or laboratory "
            "test that interacts."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e item[x]
            "one_of_many": "item",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "MedicinalProductDefinition",
                "Medication",
                "Substance",
                "NutritionProduct",
                "BiologicallyDerivedProduct",
                "ObservationDefinition",
            ],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClinicalUseDefinitionInteractionInteractant`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "itemReference",
            "itemCodeableConcept",
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
        one_of_many_fields = {"item": ["itemCodeableConcept", "itemReference"]}
        return one_of_many_fields


class ClinicalUseDefinitionUndesirableEffect(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A possible negative outcome from the use of this treatment.
    Describe the possible undesirable effects (negative outcomes) from the use
    of the medicinal product as treatment.
    """

    __resource_type__ = "ClinicalUseDefinitionUndesirableEffect"

    classification: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="classification",
        title="High level classification of the effect",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    frequencyOfOccurrence: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="frequencyOfOccurrence",
        title="How often the effect is seen",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    symptomConditionEffect: fhirtypes.CodeableReferenceType | None = Field(  # type: ignore
        None,
        alias="symptomConditionEffect",
        title="The situation in which the undesirable effect may manifest",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ObservationDefinition"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClinicalUseDefinitionUndesirableEffect`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "symptomConditionEffect",
            "classification",
            "frequencyOfOccurrence",
        ]


class ClinicalUseDefinitionWarning(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Critical environmental, health or physical risks or hazards. For example
    'Do not operate heavy machinery', 'May cause drowsiness'.
    A critical piece of information about environmental, health or physical
    risks or hazards that serve as caution to the user. For example 'Do not
    operate heavy machinery', 'May cause drowsiness', or 'Get medical
    advice/attention if you feel unwell'.
    """

    __resource_type__ = "ClinicalUseDefinitionWarning"

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title="A coded or unformatted textual definition of this warning",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="A textual definition of this warning, with formatting",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClinicalUseDefinitionWarning`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "description", "code"]
