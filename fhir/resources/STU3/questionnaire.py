from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Questionnaire
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
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
            "An identifier for this question or group of questions in a particular "
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

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="date",
        title="Date this was last changed",
        description=(
            "The date  (and optionally time) when the questionnaire was published. "
            "The date must change if and when the business version changes and it "
            "must change if the status code changes. In addition, it should change "
            "when the substantive content of the questionnaire changes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
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
            "A boolean value to indicate that this questionnaire is authored for "
            "testing purposes (or education/evaluation/marketing), and is not "
            "intended to be used for genuine usage."
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
        title="Additional identifier for the questionnaire",
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
        title="When the questionnaire was last reviewed",
        description=(
            "The date on which the resource content was last reviewed. Review "
            "happens periodically after approval, but doesn't change the original "
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
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the individual or organization that published the "
            "questionnaire."
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
            "Explaination of why this questionnaire is needed and why it has been "
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
        description=(
            "The status of this questionnaire. Enables tracking the life-cycle of "
            "the content."
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
        title="Logical URI to reference this questionnaire (globally unique)",
        description=(
            "An absolute URI that is used to identify this questionnaire when it is"
            " referenced in a specification, model, design or an instance. This "
            "SHALL be a URL, SHOULD be globally unique, and SHOULD be an address at"
            " which this questionnaire is (or will be) published. The URL SHOULD "
            "include the major version of the questionnaire. For more information "
            "see [Technical and Business Versions](resource.html#versions)."
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
        title="Context the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These terms may be used to assist with "
            "indexing and searching for appropriate questionnaire instances."
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
            "name",
            "title",
            "status",
            "experimental",
            "date",
            "publisher",
            "description",
            "purpose",
            "approvalDate",
            "lastReviewDate",
            "effectivePeriod",
            "useContext",
            "jurisdiction",
            "contact",
            "copyright",
            "code",
            "subjectType",
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


class QuestionnaireItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Questions and sections within the Questionnaire.
    A particular question, question grouping or display text that is part of
    the questionnaire.
    """

    __resource_type__ = "QuestionnaireItem"

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
            "A reference to an [ElementDefinition](elementdefinition.html) that "
            "provides the details for the item. If a definition is provided, then "
            "the following element values can be inferred from the definition:   * "
            "code (ElementDefinition.code) * type (ElementDefinition.type) * "
            "required (ElementDefinition.min) * repeats (ElementDefinition.max) * "
            "maxLength (ElementDefinition.maxLength) * options "
            "(ElementDefinition.binding)  Any information provided in these "
            "elements on a Questionnaire Item overrides the information from the "
            "definition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_definition", title="Extension field for ``definition``."
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

    initialAttachment: fhirtypes.AttachmentType | None = Field(  # type: ignore
        None,
        alias="initialAttachment",
        title="Default value when item is first rendered",
        description=(
            "The value that should be defaulted when initially rendering the "
            "questionnaire for user input."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e initial[x]
            "one_of_many": "initial",
            "one_of_many_required": False,
        },
    )

    initialBoolean: bool | None = Field(  # type: ignore
        None,
        alias="initialBoolean",
        title="Default value when item is first rendered",
        description=(
            "The value that should be defaulted when initially rendering the "
            "questionnaire for user input."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e initial[x]
            "one_of_many": "initial",
            "one_of_many_required": False,
        },
    )
    initialBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_initialBoolean", title="Extension field for ``initialBoolean``."
    )

    initialCoding: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="initialCoding",
        title="Default value when item is first rendered",
        description=(
            "The value that should be defaulted when initially rendering the "
            "questionnaire for user input."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e initial[x]
            "one_of_many": "initial",
            "one_of_many_required": False,
        },
    )

    initialDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="initialDate",
        title="Default value when item is first rendered",
        description=(
            "The value that should be defaulted when initially rendering the "
            "questionnaire for user input."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e initial[x]
            "one_of_many": "initial",
            "one_of_many_required": False,
        },
    )
    initialDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_initialDate", title="Extension field for ``initialDate``."
    )

    initialDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="initialDateTime",
        title="Default value when item is first rendered",
        description=(
            "The value that should be defaulted when initially rendering the "
            "questionnaire for user input."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e initial[x]
            "one_of_many": "initial",
            "one_of_many_required": False,
        },
    )
    initialDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_initialDateTime", title="Extension field for ``initialDateTime``."
    )

    initialDecimal: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="initialDecimal",
        title="Default value when item is first rendered",
        description=(
            "The value that should be defaulted when initially rendering the "
            "questionnaire for user input."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e initial[x]
            "one_of_many": "initial",
            "one_of_many_required": False,
        },
    )
    initialDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_initialDecimal", title="Extension field for ``initialDecimal``."
    )

    initialInteger: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="initialInteger",
        title="Default value when item is first rendered",
        description=(
            "The value that should be defaulted when initially rendering the "
            "questionnaire for user input."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e initial[x]
            "one_of_many": "initial",
            "one_of_many_required": False,
        },
    )
    initialInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_initialInteger", title="Extension field for ``initialInteger``."
    )

    initialQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="initialQuantity",
        title="Default value when item is first rendered",
        description=(
            "The value that should be defaulted when initially rendering the "
            "questionnaire for user input."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e initial[x]
            "one_of_many": "initial",
            "one_of_many_required": False,
        },
    )

    initialReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="initialReference",
        title="Default value when item is first rendered",
        description=(
            "The value that should be defaulted when initially rendering the "
            "questionnaire for user input."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e initial[x]
            "one_of_many": "initial",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    initialString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="initialString",
        title="Default value when item is first rendered",
        description=(
            "The value that should be defaulted when initially rendering the "
            "questionnaire for user input."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e initial[x]
            "one_of_many": "initial",
            "one_of_many_required": False,
        },
    )
    initialString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_initialString", title="Extension field for ``initialString``."
    )

    initialTime: fhirtypes.TimeType | None = Field(  # type: ignore
        None,
        alias="initialTime",
        title="Default value when item is first rendered",
        description=(
            "The value that should be defaulted when initially rendering the "
            "questionnaire for user input."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e initial[x]
            "one_of_many": "initial",
            "one_of_many_required": False,
        },
    )
    initialTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_initialTime", title="Extension field for ``initialTime``."
    )

    initialUri: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="initialUri",
        title="Default value when item is first rendered",
        description=(
            "The value that should be defaulted when initially rendering the "
            "questionnaire for user input."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e initial[x]
            "one_of_many": "initial",
            "one_of_many_required": False,
        },
    )
    initialUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_initialUri", title="Extension field for ``initialUri``."
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
        title="No more than this many characters",
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

    option: typing.List[fhirtypes.QuestionnaireItemOptionType] | None = Field(  # type: ignore
        None,
        alias="option",
        title="Permitted answer",
        description='One of the permitted answers for a "choice" or "open-choice" question.',
        json_schema_extra={
            "element_property": True,
        },
    )

    options: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="options",
        title="Valueset containing permitted answers",
        description=(
            "A reference to a value set containing a list of codes representing "
            'permitted answers for a "choice" or "open-choice" question.'
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ValueSet"],
        },
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
            "An indication, if true, that the item may occur multiple times in the "
            "response, collecting multiple answers answers for questions or "
            "multiple sets of answers for groups."
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
            "(string, integer, coded choice, etc.)."
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
            "required",
            "repeats",
            "readOnly",
            "maxLength",
            "options",
            "option",
            "initialBoolean",
            "initialDecimal",
            "initialInteger",
            "initialDate",
            "initialDateTime",
            "initialTime",
            "initialString",
            "initialUri",
            "initialAttachment",
            "initialCoding",
            "initialQuantity",
            "initialReference",
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
            "initial": [
                "initialAttachment",
                "initialBoolean",
                "initialCoding",
                "initialDate",
                "initialDateTime",
                "initialDecimal",
                "initialInteger",
                "initialQuantity",
                "initialReference",
                "initialString",
                "initialTime",
                "initialUri",
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

    answerAttachment: fhirtypes.AttachmentType | None = Field(  # type: ignore
        None,
        alias="answerAttachment",
        title="Value question must have",
        description=(
            "An answer that the referenced question must match in order for the "
            "item to be enabled."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e answer[x]
            "one_of_many": "answer",
            "one_of_many_required": False,
        },
    )

    answerBoolean: bool | None = Field(  # type: ignore
        None,
        alias="answerBoolean",
        title="Value question must have",
        description=(
            "An answer that the referenced question must match in order for the "
            "item to be enabled."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e answer[x]
            "one_of_many": "answer",
            "one_of_many_required": False,
        },
    )
    answerBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_answerBoolean", title="Extension field for ``answerBoolean``."
    )

    answerCoding: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="answerCoding",
        title="Value question must have",
        description=(
            "An answer that the referenced question must match in order for the "
            "item to be enabled."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e answer[x]
            "one_of_many": "answer",
            "one_of_many_required": False,
        },
    )

    answerDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="answerDate",
        title="Value question must have",
        description=(
            "An answer that the referenced question must match in order for the "
            "item to be enabled."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e answer[x]
            "one_of_many": "answer",
            "one_of_many_required": False,
        },
    )
    answerDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_answerDate", title="Extension field for ``answerDate``."
    )

    answerDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="answerDateTime",
        title="Value question must have",
        description=(
            "An answer that the referenced question must match in order for the "
            "item to be enabled."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e answer[x]
            "one_of_many": "answer",
            "one_of_many_required": False,
        },
    )
    answerDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_answerDateTime", title="Extension field for ``answerDateTime``."
    )

    answerDecimal: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="answerDecimal",
        title="Value question must have",
        description=(
            "An answer that the referenced question must match in order for the "
            "item to be enabled."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e answer[x]
            "one_of_many": "answer",
            "one_of_many_required": False,
        },
    )
    answerDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_answerDecimal", title="Extension field for ``answerDecimal``."
    )

    answerInteger: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="answerInteger",
        title="Value question must have",
        description=(
            "An answer that the referenced question must match in order for the "
            "item to be enabled."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e answer[x]
            "one_of_many": "answer",
            "one_of_many_required": False,
        },
    )
    answerInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_answerInteger", title="Extension field for ``answerInteger``."
    )

    answerQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="answerQuantity",
        title="Value question must have",
        description=(
            "An answer that the referenced question must match in order for the "
            "item to be enabled."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e answer[x]
            "one_of_many": "answer",
            "one_of_many_required": False,
        },
    )

    answerReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="answerReference",
        title="Value question must have",
        description=(
            "An answer that the referenced question must match in order for the "
            "item to be enabled."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e answer[x]
            "one_of_many": "answer",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    answerString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="answerString",
        title="Value question must have",
        description=(
            "An answer that the referenced question must match in order for the "
            "item to be enabled."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e answer[x]
            "one_of_many": "answer",
            "one_of_many_required": False,
        },
    )
    answerString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_answerString", title="Extension field for ``answerString``."
    )

    answerTime: fhirtypes.TimeType | None = Field(  # type: ignore
        None,
        alias="answerTime",
        title="Value question must have",
        description=(
            "An answer that the referenced question must match in order for the "
            "item to be enabled."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e answer[x]
            "one_of_many": "answer",
            "one_of_many_required": False,
        },
    )
    answerTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_answerTime", title="Extension field for ``answerTime``."
    )

    answerUri: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="answerUri",
        title="Value question must have",
        description=(
            "An answer that the referenced question must match in order for the "
            "item to be enabled."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e answer[x]
            "one_of_many": "answer",
            "one_of_many_required": False,
        },
    )
    answerUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_answerUri", title="Extension field for ``answerUri``."
    )

    hasAnswer: bool | None = Field(  # type: ignore
        None,
        alias="hasAnswer",
        title="Enable when answered or not",
        description=(
            "An indication that this item should be enabled only if the specified "
            "question is answered (hasAnswer=true) or not answered "
            "(hasAnswer=false)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    hasAnswer__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_hasAnswer", title="Extension field for ``hasAnswer``."
    )

    question: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="question",
        title="Question that determines whether item is enabled",
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
            "hasAnswer",
            "answerBoolean",
            "answerDecimal",
            "answerInteger",
            "answerDate",
            "answerDateTime",
            "answerTime",
            "answerString",
            "answerUri",
            "answerAttachment",
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
        required_fields = [("question", "question__ext")]
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
                "answerAttachment",
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
                "answerUri",
            ]
        }
        return one_of_many_fields


class QuestionnaireItemOption(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Permitted answer.
    One of the permitted answers for a "choice" or "open-choice" question.
    """

    __resource_type__ = "QuestionnaireItemOption"

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
        ``QuestionnaireItemOption`` according specification,
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
                "valueString",
                "valueTime",
            ]
        }
        return one_of_many_fields
