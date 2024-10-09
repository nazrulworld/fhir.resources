from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ConditionDefinition
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ConditionDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A definition of a condition.
    A definition of a condition and information relevant to managing it.
    """

    __resource_type__ = "ConditionDefinition"

    bodySite: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="bodySite",
        title="Anatomical location, if relevant",
        description="The anatomical location where this condition manifests itself.",
        json_schema_extra={
            "element_property": True,
        },
    )

    code: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="code",
        title="Identification of the condition, problem or diagnosis",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    contact: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        None,
        alias="contact",
        title="Contact details for the publisher",
        description=(
            "Contact details to assist a user in finding and communicating with the"
            " publisher."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the condition definition was last"
            " significantly changed. The date must change when the business version"
            " changes and it must change if the status code changes. In addition, "
            "it should change when the substantive content of the condition "
            "definition changes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    definition: typing.List[fhirtypes.UriType | None] | None = Field(  # type: ignore
        None,
        alias="definition",
        title="Formal Definition for the condition",
        description=(
            "Formal definitions of the condition. These may be references to "
            "ontologies, published clinical protocols or research papers."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    definition__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_definition", title="Extension field for ``definition``."
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Natural language description of the condition definition",
        description=(
            "A free text natural language description of the condition definition "
            "from a consumer's perspective."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    experimental: bool | None = Field(  # type: ignore
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this condition definition is authored"
            " for testing purposes (or education/evaluation/marketing) and is not "
            "intended to be used for genuine usage."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    hasBodySite: bool | None = Field(  # type: ignore
        None,
        alias="hasBodySite",
        title="Whether bodySite is appropriate",
        description="Whether bodySite is appropriate to collect for this condition.",
        json_schema_extra={
            "element_property": True,
        },
    )
    hasBodySite__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_hasBodySite", title="Extension field for ``hasBodySite``."
    )

    hasSeverity: bool | None = Field(  # type: ignore
        None,
        alias="hasSeverity",
        title="Whether Severity is appropriate",
        description="Whether Severity is appropriate to collect for this condition.",
        json_schema_extra={
            "element_property": True,
        },
    )
    hasSeverity__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_hasSeverity", title="Extension field for ``hasSeverity``."
    )

    hasStage: bool | None = Field(  # type: ignore
        None,
        alias="hasStage",
        title="Whether stage is appropriate",
        description="Whether stage is appropriate to collect for this condition.",
        json_schema_extra={
            "element_property": True,
        },
    )
    hasStage__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_hasStage", title="Extension field for ``hasStage``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Additional identifier for the condition definition",
        description=(
            "A formal identifier that is used to identify this condition definition"
            " when it is represented in other formats, or referenced in a "
            "specification, model, design or an instance."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for condition definition (if applicable)",
        description=(
            "A legal or geographic region in which the condition definition is "
            "intended to be used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    medication: typing.List[fhirtypes.ConditionDefinitionMedicationType] | None = Field(  # type: ignore
        None,
        alias="medication",
        title="Medications particularly relevant for this condition",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name for this condition definition (computer friendly)",
        description=(
            "A natural language name identifying the condition definition. This "
            "name should be usable as an identifier for the module by machine "
            "processing applications such as code generation."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    observation: typing.List[fhirtypes.ConditionDefinitionObservationType] | None = Field(  # type: ignore
        None,
        alias="observation",
        title="Observations particularly relevant to this condition",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    plan: typing.List[fhirtypes.ConditionDefinitionPlanType] | None = Field(  # type: ignore
        None,
        alias="plan",
        title="Plan that is appropriate",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    precondition: typing.List[fhirtypes.ConditionDefinitionPreconditionType] | None = Field(  # type: ignore
        None,
        alias="precondition",
        title="Observation that suggets this condition",
        description="An observation that suggests that this condition applies.",
        json_schema_extra={
            "element_property": True,
        },
    )

    publisher: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="publisher",
        title="Name of the publisher/steward (organization or individual)",
        description=(
            "The name of the organization or individual responsible for the release"
            " and ongoing maintenance of the condition definition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    questionnaire: typing.List[fhirtypes.ConditionDefinitionQuestionnaireType] | None = Field(  # type: ignore
        None,
        alias="questionnaire",
        title="Questionnaire for this condition",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    severity: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="severity",
        title="Subjective severity of condition",
        description=(
            "A subjective assessment of the severity of the condition as evaluated "
            "by the clinician."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    stage: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="stage",
        title="Stage/grade, usually assessed formally",
        description=(
            "Clinical stage or grade of a condition. May include formal severity "
            "assessments."
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
            "The status of this condition definition. Enables tracking the life-"
            "cycle of the content."
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

    subtitle: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="subtitle",
        title="Subordinate title of the event definition",
        description=(
            "An explanatory or alternate title for the event definition giving "
            "additional information about its content."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    subtitle__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_subtitle", title="Extension field for ``subtitle``."
    )

    team: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="team",
        title="Appropriate team for this condition",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["CareTeam"],
        },
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Name for this condition definition (human friendly)",
        description=(
            "A short, descriptive, user-friendly title for the condition " "definition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="url",
        title=(
            "Canonical identifier for this condition definition, represented as a "
            "URI (globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this condition definition "
            "when it is referenced in a specification, model, design or an "
            "instance; also called its canonical identifier. This SHOULD be "
            "globally unique and SHOULD be a literal address at which an "
            "authoritative instance of this condition definition is (or will be) "
            "published. This URL can be the target of a canonical reference. It "
            "SHALL remain the same when the condition definition is stored on "
            "different servers."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_url", title="Extension field for ``url``."
    )

    useContext: typing.List[fhirtypes.UsageContextType] | None = Field(  # type: ignore
        None,
        alias="useContext",
        title="The context that the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These contexts may be general categories "
            "(gender, age, ...) or may be references to specific programs "
            "(insurance plans, studies, ...) and may be used to assist with "
            "indexing and searching for appropriate condition definition instances."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="Business version of the condition definition",
        description=(
            "The identifier that is used to identify this version of the condition "
            "definition when it is referenced in a specification, model, design or "
            "instance. This is an arbitrary value managed by the condition "
            "definition author and is not expected to be globally unique. For "
            "example, it might be a timestamp (e.g. yyyymmdd) if a managed version "
            "is not available. There is also no expectation that versions can be "
            "placed in a lexicographical sequence."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_version", title="Extension field for ``version``."
    )

    versionAlgorithmCoding: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="versionAlgorithmCoding",
        title="How to compare versions",
        description=(
            "Indicates the mechanism used to compare versions to determine which is"
            " more current."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e versionAlgorithm[x]
            "one_of_many": "versionAlgorithm",
            "one_of_many_required": False,
        },
    )

    versionAlgorithmString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="versionAlgorithmString",
        title="How to compare versions",
        description=(
            "Indicates the mechanism used to compare versions to determine which is"
            " more current."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e versionAlgorithm[x]
            "one_of_many": "versionAlgorithm",
            "one_of_many_required": False,
        },
    )
    versionAlgorithmString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_versionAlgorithmString",
        title="Extension field for ``versionAlgorithmString``.",
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ConditionDefinition`` according specification,
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
            "url",
            "identifier",
            "version",
            "versionAlgorithmString",
            "versionAlgorithmCoding",
            "name",
            "title",
            "subtitle",
            "status",
            "experimental",
            "date",
            "publisher",
            "contact",
            "description",
            "useContext",
            "jurisdiction",
            "code",
            "severity",
            "bodySite",
            "stage",
            "hasSeverity",
            "hasBodySite",
            "hasStage",
            "definition",
            "observation",
            "medication",
            "precondition",
            "team",
            "questionnaire",
            "plan",
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
            "versionAlgorithm": ["versionAlgorithmCoding", "versionAlgorithmString"]
        }
        return one_of_many_fields


class ConditionDefinitionMedication(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Medications particularly relevant for this condition.
    """

    __resource_type__ = "ConditionDefinitionMedication"

    category: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="category",
        title="Category that is relevant",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Code for relevant Medication",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ConditionDefinitionMedication`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "category", "code"]


class ConditionDefinitionObservation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Observations particularly relevant to this condition.
    """

    __resource_type__ = "ConditionDefinitionObservation"

    category: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="category",
        title="Category that is relevant",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Code for relevant Observation",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ConditionDefinitionObservation`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "category", "code"]


class ConditionDefinitionPlan(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Plan that is appropriate.
    """

    __resource_type__ = "ConditionDefinitionPlan"

    reference: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="reference",
        title="The actual plan",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["PlanDefinition"],
        },
    )

    role: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="role",
        title="Use for the plan",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ConditionDefinitionPlan`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "role", "reference"]


class ConditionDefinitionPrecondition(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Observation that suggets this condition.
    An observation that suggests that this condition applies.
    """

    __resource_type__ = "ConditionDefinitionPrecondition"

    code: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="code",
        title="Code for relevant Observation",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="sensitive | specific",
        description="Kind of pre-condition.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["sensitive", "specific"],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="valueCodeableConcept",
        title="Value of Observation",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="valueQuantity",
        title="Value of Observation",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ConditionDefinitionPrecondition`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "code",
            "valueCodeableConcept",
            "valueQuantity",
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
        one_of_many_fields = {"value": ["valueCodeableConcept", "valueQuantity"]}
        return one_of_many_fields


class ConditionDefinitionQuestionnaire(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Questionnaire for this condition.
    """

    __resource_type__ = "ConditionDefinitionQuestionnaire"

    purpose: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="purpose",
        title="preadmit | diff-diagnosis | outcome",
        description="Use of the questionnaire.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["preadmit", "diff-diagnosis", "outcome"],
        },
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    reference: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="reference",
        title="Specific Questionnaire",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Questionnaire"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ConditionDefinitionQuestionnaire`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "purpose", "reference"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("purpose", "purpose__ext")]
        return required_fields
