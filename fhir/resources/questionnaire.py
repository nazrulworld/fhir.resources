from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Questionnaire
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Questionnaire(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A structured set of questions.
    A structured set of questions intended to guide the collection of answers
    from end-users. Questionnaires provide detailed control over order,
    presentation, phraseology and grouping to allow coherent, consistent data
    collection.
    """

    __resource_type__ = "Questionnaire"

    approvalDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="approvalDate",
        title="When the questionnaire was approved by publisher",
        description=(
            "The date on which the resource content was approved by the publisher. "
            "Approval happens once when the content is officially approved for "
            "usage."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_approvalDate", title="Extension field for ``approvalDate``."
    )

    code: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        None,
        alias="code",
        title="Concept that represents the overall questionnaire",
        description=(
            "An identifier for this collection of questions in a particular "
            "terminology such as LOINC."
        ),
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

    copyright: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the questionnaire and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the questionnaire."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    copyrightLabel: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="copyrightLabel",
        title="Copyright holder and year(s)",
        description=(
            "A short string (<50 characters), suitable for inclusion in a page "
            "footer that identifies the copyright holder, effective period, and "
            "optionally whether rights are resctricted. (e.g. 'All rights "
            "reserved', 'Some rights reserved')."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    copyrightLabel__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_copyrightLabel", title="Extension field for ``copyrightLabel``."
    )

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the questionnaire was last "
            "significantly changed. The date must change when the business version "
            "changes and it must change if the status code changes. In addition, it"
            " should change when the substantive content of the questionnaire "
            "changes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    derivedFrom: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="derivedFrom",
        title="Based on Questionnaire",
        description="The URL of a Questionnaire that this Questionnaire is based on.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Questionnaire"],
        },
    )
    derivedFrom__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_derivedFrom", title="Extension field for ``derivedFrom``."
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Natural language description of the questionnaire",
        description=(
            "A free text natural language description of the questionnaire from a "
            "consumer's perspective."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    effectivePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="effectivePeriod",
        title="When the questionnaire is expected to be used",
        description=(
            "The period during which the questionnaire content was or is planned to"
            " be in active use."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    experimental: bool | None = Field(  # type: ignore
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this questionnaire is authored for "
            "testing purposes (or education/evaluation/marketing) and is not "
            "intended for genuine usage."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business identifier for questionnaire",
        description=(
            "A formal identifier that is used to identify this questionnaire when "
            "it is represented in other formats, or referenced in a specification, "
            "model, design or an instance."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    item: typing.List[fhirtypes.QuestionnaireItemType] | None = Field(  # type: ignore
        None,
        alias="item",
        title="Questions and sections within the Questionnaire",
        description=(
            "A particular question, question grouping or display text that is part "
            "of the questionnaire."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for questionnaire (if applicable)",
        description=(
            "A legal or geographic region in which the questionnaire is intended to"
            " be used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    lastReviewDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="lastReviewDate",
        title="When the questionnaire was last reviewed by the publisher",
        description=(
            "The date on which the resource content was last reviewed. Review "
            "happens periodically after approval but does not change the original "
            "approval date."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_lastReviewDate", title="Extension field for ``lastReviewDate``."
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name for this questionnaire (computer friendly)",
        description=(
            "A natural language name identifying the questionnaire. This name "
            "should be usable as an identifier for the module by machine processing"
            " applications such as code generation."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    publisher: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="publisher",
        title="Name of the publisher/steward (organization or individual)",
        description=(
            "The name of the organization or individual responsible for the release"
            " and ongoing maintenance of the questionnaire."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="purpose",
        title="Why this questionnaire is defined",
        description=(
            "Explanation of why this questionnaire is needed and why it has been "
            "designed as it has."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description="The current state of this questionnaire.",
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

    subjectType: typing.List[fhirtypes.CodeType | None] | None = Field(  # type: ignore
        None,
        alias="subjectType",
        title="Resource that can be subject of QuestionnaireResponse",
        description=(
            "The types of subjects that can be the subject of responses created for"
            " the questionnaire."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    subjectType__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_subjectType", title="Extension field for ``subjectType``."
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Name for this questionnaire (human friendly)",
        description="A short, descriptive, user-friendly title for the questionnaire.",
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
            "Canonical identifier for this questionnaire, represented as an "
            "absolute URI (globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this questionnaire when it is"
            " referenced in a specification, model, design or an instance; also "
            "called its canonical identifier. This SHOULD be globally unique and "
            "SHOULD be a literal address at which an authoritative instance of this"
            " questionnaire is (or will be) published. This URL can be the target "
            "of a canonical reference. It SHALL remain the same when the "
            "questionnaire is stored on different servers."
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
            "indexing and searching for appropriate questionnaires."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="Business version of the questionnaire",
        description=(
            "The identifier that is used to identify this version of the "
            "questionnaire when it is referenced in a specification, model, design "
            "or instance. This is an arbitrary value managed by the questionnaire "
            "author and is not expected to be globally unique. For example, it "
            "might be a timestamp (e.g. yyyymmdd) if a managed version is not "
            "available. There is also no expectation that versions can be placed in"
            " a lexicographical sequence."
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
        ``Questionnaire`` according specification,
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
            "derivedFrom",
            "status",
            "experimental",
            "subjectType",
            "date",
            "publisher",
            "contact",
            "description",
            "useContext",
            "jurisdiction",
            "purpose",
            "copyright",
            "copyrightLabel",
            "approvalDate",
            "lastReviewDate",
            "effectivePeriod",
            "code",
            "item",
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


class QuestionnaireItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Questions and sections within the Questionnaire.
    A particular question, question grouping or display text that is part of
    the questionnaire.
    """

    __resource_type__ = "QuestionnaireItem"

    answerConstraint: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="answerConstraint",
        title="optionsOnly | optionsOrType | optionsOrString",
        description=(
            "For items that have a defined set of allowed answers (via answerOption"
            " or answerValueSet), indicates whether values *other* than those "
            "specified can be selected."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["optionsOnly", "optionsOrType", "optionsOrString"],
        },
    )
    answerConstraint__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_answerConstraint",
        title="Extension field for ``answerConstraint``.",
    )

    answerOption: typing.List[fhirtypes.QuestionnaireItemAnswerOptionType] | None = Field(  # type: ignore
        None,
        alias="answerOption",
        title="Permitted answer",
        description="One of the permitted answers for the question.",
        json_schema_extra={
            "element_property": True,
        },
    )

    answerValueSet: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="answerValueSet",
        title="ValueSet containing permitted answers",
        description=(
            "A reference to a value set containing a list of values representing "
            "permitted answers for a question."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ValueSet"],
        },
    )
    answerValueSet__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_answerValueSet", title="Extension field for ``answerValueSet``."
    )

    code: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        None,
        alias="code",
        title="Corresponding concept for this item in a terminology",
        description=(
            "A terminology code that corresponds to this group or question (e.g. a "
            "code from LOINC, which defines many questions and answers)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    definition: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="definition",
        title="ElementDefinition - details for the item",
        description=(
            "This element is a URI that refers to an "
            "[ElementDefinition](elementdefinition.html) or to an "
            "[ObservationDefinition](observationdefinition.html) that provides "
            "information about this item, including information that might "
            "otherwise be included in the instance of the Questionnaire resource. A"
            " detailed description of the construction of the URI is shown in "
            "[Comments](questionnaire.html#definition), below."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_definition", title="Extension field for ``definition``."
    )

    disabledDisplay: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="disabledDisplay",
        title="hidden | protected",
        description=(
            "Indicates if and how items that are disabled (because enableWhen "
            "evaluates to 'false') should be displayed."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["hidden", "protected"],
        },
    )
    disabledDisplay__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_disabledDisplay", title="Extension field for ``disabledDisplay``."
    )

    enableBehavior: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="enableBehavior",
        title="all | any",
        description=(
            "Controls how multiple enableWhen values are interpreted -  whether all"
            " or any must be true."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["all", "any"],
        },
    )
    enableBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_enableBehavior", title="Extension field for ``enableBehavior``."
    )

    enableWhen: typing.List[fhirtypes.QuestionnaireItemEnableWhenType] | None = Field(  # type: ignore
        None,
        alias="enableWhen",
        title="Only allow data when",
        description=(
            "A constraint indicating that this item should only be enabled "
            "(displayed/allow answers to be captured) when the specified condition "
            "is true."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    initial: typing.List[fhirtypes.QuestionnaireItemInitialType] | None = Field(  # type: ignore
        None,
        alias="initial",
        title="Initial value(s) when item is first rendered",
        description=(
            "One or more values that should be pre-populated in the answer when "
            "initially rendering the questionnaire for user input."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    item: typing.List[fhirtypes.QuestionnaireItemType] | None = Field(  # type: ignore
        None,
        alias="item",
        title="Nested questionnaire items",
        description=(
            "Text, questions and other groups to be nested beneath a question or "
            "group."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    linkId: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="linkId",
        title="Unique id for item in questionnaire",
        description=(
            "An identifier that is unique within the Questionnaire allowing linkage"
            " to the equivalent item in a QuestionnaireResponse resource."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_linkId", title="Extension field for ``linkId``."
    )

    maxLength: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="maxLength",
        title="No more than these many characters",
        description=(
            "The maximum number of characters that are permitted in the answer to "
            'be considered a "valid" QuestionnaireResponse.'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    maxLength__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_maxLength", title="Extension field for ``maxLength``."
    )

    prefix: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="prefix",
        title='E.g. "1(a)", "2.5.3"',
        description=(
            "A short label for a particular group, question or set of display text "
            "within the questionnaire used for reference by the individual "
            "completing the questionnaire."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    prefix__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_prefix", title="Extension field for ``prefix``."
    )

    readOnly: bool | None = Field(  # type: ignore
        None,
        alias="readOnly",
        title="Don't allow human editing",
        description=(
            "An indication, when true, that the value cannot be changed by a human "
            "respondent to the Questionnaire."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    readOnly__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_readOnly", title="Extension field for ``readOnly``."
    )

    repeats: bool | None = Field(  # type: ignore
        None,
        alias="repeats",
        title="Whether the item may repeat",
        description=(
            "An indication, if true, that a QuestionnaireResponse for this item may"
            " include multiple answers associated with a single instance of this "
            "item (for question-type items) or multiple repetitions of the item "
            "(for group-type items)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    repeats__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_repeats", title="Extension field for ``repeats``."
    )

    required: bool | None = Field(  # type: ignore
        None,
        alias="required",
        title="Whether the item must be included in data results",
        description=(
            'An indication, if true, that the item must be present in a "completed"'
            " QuestionnaireResponse.  If false, the item may be skipped when "
            "answering the questionnaire."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    required__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_required", title="Extension field for ``required``."
    )

    text: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="text",
        title="Primary text for the item",
        description=(
            "The name of a section, the text of a question or text content for a "
            "display item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_text", title="Extension field for ``text``."
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="group | display | boolean | decimal | integer | date | dateTime +",
        description=(
            "The type of questionnaire item this is - whether text for display, a "
            "grouping of other items or a particular type of data to be captured "
            "(string, integer, Coding, etc.)."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "group",
                "display",
                "boolean",
                "decimal",
                "integer",
                "date",
                "dateTime",
                "+",
            ],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``QuestionnaireItem`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "linkId",
            "definition",
            "code",
            "prefix",
            "text",
            "type",
            "enableWhen",
            "enableBehavior",
            "disabledDisplay",
            "required",
            "repeats",
            "readOnly",
            "maxLength",
            "answerConstraint",
            "answerValueSet",
            "answerOption",
            "initial",
            "item",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("linkId", "linkId__ext"), ("type", "type__ext")]
        return required_fields


class QuestionnaireItemAnswerOption(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Permitted answer.
    One of the permitted answers for the question.
    """

    __resource_type__ = "QuestionnaireItemAnswerOption"

    initialSelected: bool | None = Field(  # type: ignore
        None,
        alias="initialSelected",
        title="Whether option is selected by default",
        description=(
            "Indicates whether the answer value is selected when the list of "
            "possible answers is initially shown."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    initialSelected__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_initialSelected", title="Extension field for ``initialSelected``."
    )

    valueCoding: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="valueCoding",
        title="Answer value",
        description="A potential answer that's allowed as the answer to this question.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="valueDate",
        title="Answer value",
        description="A potential answer that's allowed as the answer to this question.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueDate", title="Extension field for ``valueDate``."
    )

    valueInteger: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="valueInteger",
        title="Answer value",
        description="A potential answer that's allowed as the answer to this question.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueInteger", title="Extension field for ``valueInteger``."
    )

    valueReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="valueReference",
        title="Answer value",
        description="A potential answer that's allowed as the answer to this question.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    valueString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="valueString",
        title="Answer value",
        description="A potential answer that's allowed as the answer to this question.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    valueTime: fhirtypes.TimeType | None = Field(  # type: ignore
        None,
        alias="valueTime",
        title="Answer value",
        description="A potential answer that's allowed as the answer to this question.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueTime", title="Extension field for ``valueTime``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``QuestionnaireItemAnswerOption`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "valueInteger",
            "valueDate",
            "valueTime",
            "valueString",
            "valueCoding",
            "valueReference",
            "initialSelected",
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
            "value": [
                "valueCoding",
                "valueDate",
                "valueInteger",
                "valueReference",
                "valueString",
                "valueTime",
            ]
        }
        return one_of_many_fields


class QuestionnaireItemEnableWhen(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Only allow data when.
    A constraint indicating that this item should only be enabled
    (displayed/allow answers to be captured) when the specified condition is
    true.
    """

    __resource_type__ = "QuestionnaireItemEnableWhen"

    answerBoolean: bool | None = Field(  # type: ignore
        None,
        alias="answerBoolean",
        title="Value for question comparison based on operator",
        description=(
            "A value that the referenced question is tested using the specified "
            "operator in order for the item to be enabled.  If there are multiple "
            "answers, a match on any of the answers suffices.  If different "
            "behavior is desired (all must match, at least 2 must match, etc.), "
            "consider using the enableWhenExpression extension."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e answer[x]
            "one_of_many": "answer",
            "one_of_many_required": True,
        },
    )
    answerBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_answerBoolean", title="Extension field for ``answerBoolean``."
    )

    answerCoding: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="answerCoding",
        title="Value for question comparison based on operator",
        description=(
            "A value that the referenced question is tested using the specified "
            "operator in order for the item to be enabled.  If there are multiple "
            "answers, a match on any of the answers suffices.  If different "
            "behavior is desired (all must match, at least 2 must match, etc.), "
            "consider using the enableWhenExpression extension."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e answer[x]
            "one_of_many": "answer",
            "one_of_many_required": True,
        },
    )

    answerDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="answerDate",
        title="Value for question comparison based on operator",
        description=(
            "A value that the referenced question is tested using the specified "
            "operator in order for the item to be enabled.  If there are multiple "
            "answers, a match on any of the answers suffices.  If different "
            "behavior is desired (all must match, at least 2 must match, etc.), "
            "consider using the enableWhenExpression extension."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e answer[x]
            "one_of_many": "answer",
            "one_of_many_required": True,
        },
    )
    answerDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_answerDate", title="Extension field for ``answerDate``."
    )

    answerDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="answerDateTime",
        title="Value for question comparison based on operator",
        description=(
            "A value that the referenced question is tested using the specified "
            "operator in order for the item to be enabled.  If there are multiple "
            "answers, a match on any of the answers suffices.  If different "
            "behavior is desired (all must match, at least 2 must match, etc.), "
            "consider using the enableWhenExpression extension."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e answer[x]
            "one_of_many": "answer",
            "one_of_many_required": True,
        },
    )
    answerDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_answerDateTime", title="Extension field for ``answerDateTime``."
    )

    answerDecimal: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="answerDecimal",
        title="Value for question comparison based on operator",
        description=(
            "A value that the referenced question is tested using the specified "
            "operator in order for the item to be enabled.  If there are multiple "
            "answers, a match on any of the answers suffices.  If different "
            "behavior is desired (all must match, at least 2 must match, etc.), "
            "consider using the enableWhenExpression extension."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e answer[x]
            "one_of_many": "answer",
            "one_of_many_required": True,
        },
    )
    answerDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_answerDecimal", title="Extension field for ``answerDecimal``."
    )

    answerInteger: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="answerInteger",
        title="Value for question comparison based on operator",
        description=(
            "A value that the referenced question is tested using the specified "
            "operator in order for the item to be enabled.  If there are multiple "
            "answers, a match on any of the answers suffices.  If different "
            "behavior is desired (all must match, at least 2 must match, etc.), "
            "consider using the enableWhenExpression extension."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e answer[x]
            "one_of_many": "answer",
            "one_of_many_required": True,
        },
    )
    answerInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_answerInteger", title="Extension field for ``answerInteger``."
    )

    answerQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="answerQuantity",
        title="Value for question comparison based on operator",
        description=(
            "A value that the referenced question is tested using the specified "
            "operator in order for the item to be enabled.  If there are multiple "
            "answers, a match on any of the answers suffices.  If different "
            "behavior is desired (all must match, at least 2 must match, etc.), "
            "consider using the enableWhenExpression extension."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e answer[x]
            "one_of_many": "answer",
            "one_of_many_required": True,
        },
    )

    answerReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="answerReference",
        title="Value for question comparison based on operator",
        description=(
            "A value that the referenced question is tested using the specified "
            "operator in order for the item to be enabled.  If there are multiple "
            "answers, a match on any of the answers suffices.  If different "
            "behavior is desired (all must match, at least 2 must match, etc.), "
            "consider using the enableWhenExpression extension."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e answer[x]
            "one_of_many": "answer",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    answerString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="answerString",
        title="Value for question comparison based on operator",
        description=(
            "A value that the referenced question is tested using the specified "
            "operator in order for the item to be enabled.  If there are multiple "
            "answers, a match on any of the answers suffices.  If different "
            "behavior is desired (all must match, at least 2 must match, etc.), "
            "consider using the enableWhenExpression extension."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e answer[x]
            "one_of_many": "answer",
            "one_of_many_required": True,
        },
    )
    answerString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_answerString", title="Extension field for ``answerString``."
    )

    answerTime: fhirtypes.TimeType | None = Field(  # type: ignore
        None,
        alias="answerTime",
        title="Value for question comparison based on operator",
        description=(
            "A value that the referenced question is tested using the specified "
            "operator in order for the item to be enabled.  If there are multiple "
            "answers, a match on any of the answers suffices.  If different "
            "behavior is desired (all must match, at least 2 must match, etc.), "
            "consider using the enableWhenExpression extension."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e answer[x]
            "one_of_many": "answer",
            "one_of_many_required": True,
        },
    )
    answerTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_answerTime", title="Extension field for ``answerTime``."
    )

    operator: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="operator",
        title="exists | = | != | > | < | >= | <=",
        description="Specifies the criteria by which the question is enabled.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "exists",
                "=",
                "!=",
                "\u003e",
                "\u003c",
                "\u003e=",
                "\u003c=",
            ],
        },
    )
    operator__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_operator", title="Extension field for ``operator``."
    )

    question: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="question",
        title=(
            "The linkId of question that determines whether item is " "enabled/disabled"
        ),
        description=(
            "The linkId for the question whose answer (or lack of answer) governs "
            "whether this item is enabled."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    question__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_question", title="Extension field for ``question``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``QuestionnaireItemEnableWhen`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "question",
            "operator",
            "answerBoolean",
            "answerDecimal",
            "answerInteger",
            "answerDate",
            "answerDateTime",
            "answerTime",
            "answerString",
            "answerCoding",
            "answerQuantity",
            "answerReference",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("operator", "operator__ext"), ("question", "question__ext")]
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
            "answer": [
                "answerBoolean",
                "answerCoding",
                "answerDate",
                "answerDateTime",
                "answerDecimal",
                "answerInteger",
                "answerQuantity",
                "answerReference",
                "answerString",
                "answerTime",
            ]
        }
        return one_of_many_fields


class QuestionnaireItemInitial(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Initial value(s) when item is first rendered.
    One or more values that should be pre-populated in the answer when
    initially rendering the questionnaire for user input.
    """

    __resource_type__ = "QuestionnaireItemInitial"

    valueAttachment: fhirtypes.AttachmentType | None = Field(  # type: ignore
        None,
        alias="valueAttachment",
        title="Actual value for initializing the question",
        description="The actual value to for an initial answer.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueBoolean: bool | None = Field(  # type: ignore
        None,
        alias="valueBoolean",
        title="Actual value for initializing the question",
        description="The actual value to for an initial answer.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCoding: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="valueCoding",
        title="Actual value for initializing the question",
        description="The actual value to for an initial answer.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="valueDate",
        title="Actual value for initializing the question",
        description="The actual value to for an initial answer.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueDate", title="Extension field for ``valueDate``."
    )

    valueDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="valueDateTime",
        title="Actual value for initializing the question",
        description="The actual value to for an initial answer.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueDateTime", title="Extension field for ``valueDateTime``."
    )

    valueDecimal: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="valueDecimal",
        title="Actual value for initializing the question",
        description="The actual value to for an initial answer.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueDecimal", title="Extension field for ``valueDecimal``."
    )

    valueInteger: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="valueInteger",
        title="Actual value for initializing the question",
        description="The actual value to for an initial answer.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueInteger", title="Extension field for ``valueInteger``."
    )

    valueQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="valueQuantity",
        title="Actual value for initializing the question",
        description="The actual value to for an initial answer.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="valueReference",
        title="Actual value for initializing the question",
        description="The actual value to for an initial answer.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    valueString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="valueString",
        title="Actual value for initializing the question",
        description="The actual value to for an initial answer.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    valueTime: fhirtypes.TimeType | None = Field(  # type: ignore
        None,
        alias="valueTime",
        title="Actual value for initializing the question",
        description="The actual value to for an initial answer.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueTime", title="Extension field for ``valueTime``."
    )

    valueUri: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="valueUri",
        title="Actual value for initializing the question",
        description="The actual value to for an initial answer.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueUri", title="Extension field for ``valueUri``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``QuestionnaireItemInitial`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "valueBoolean",
            "valueDecimal",
            "valueInteger",
            "valueDate",
            "valueDateTime",
            "valueTime",
            "valueString",
            "valueUri",
            "valueAttachment",
            "valueCoding",
            "valueQuantity",
            "valueReference",
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
            "value": [
                "valueAttachment",
                "valueBoolean",
                "valueCoding",
                "valueDate",
                "valueDateTime",
                "valueDecimal",
                "valueInteger",
                "valueQuantity",
                "valueReference",
                "valueString",
                "valueTime",
                "valueUri",
            ]
        }
        return one_of_many_fields
