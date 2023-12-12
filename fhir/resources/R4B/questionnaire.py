# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Questionnaire
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

    resource_type = Field("Questionnaire", const=True)

    approvalDate: fhirtypes.Date = Field(
        None,
        alias="approvalDate",
        title="When the questionnaire was approved by publisher",
        description=(
            "The date on which the resource content was approved by the publisher. "
            "Approval happens once when the content is officially approved for "
            "usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_approvalDate", title="Extension field for ``approvalDate``."
    )

    code: typing.List[fhirtypes.CodingType] = Field(
        None,
        alias="code",
        title="Concept that represents the overall questionnaire",
        description=(
            "An identifier for this question or group of questions in a particular "
            "terminology such as LOINC."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    contact: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="Contact details for the publisher",
        description=(
            "Contact details to assist a user in finding and communicating with the"
            " publisher."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the questionnaire and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the questionnaire."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the questionnaire was published. "
            "The date must change when the business version changes and it must "
            "change if the status code changes. In addition, it should change when "
            "the substantive content of the questionnaire changes."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    derivedFrom: typing.List[typing.Optional[fhirtypes.Canonical]] = Field(
        None,
        alias="derivedFrom",
        title="Instantiates protocol or definition",
        description="The URL of a Questionnaire that this Questionnaire is based on.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Questionnaire"],
    )
    derivedFrom__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_derivedFrom", title="Extension field for ``derivedFrom``.")

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Natural language description of the questionnaire",
        description=(
            "A free text natural language description of the questionnaire from a "
            "consumer's perspective."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="When the questionnaire is expected to be used",
        description=(
            "The period during which the questionnaire content was or is planned to"
            " be in active use."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this questionnaire is authored for "
            "testing purposes (or education/evaluation/marketing) and is not "
            "intended to be used for genuine usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Additional identifier for the questionnaire",
        description=(
            "A formal identifier that is used to identify this questionnaire when "
            "it is represented in other formats, or referenced in a specification, "
            "model, design or an instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    item: typing.List[fhirtypes.QuestionnaireItemType] = Field(
        None,
        alias="item",
        title="Questions and sections within the Questionnaire",
        description=(
            "A particular question, question grouping or display text that is part "
            "of the questionnaire."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for questionnaire (if applicable)",
        description=(
            "A legal or geographic region in which the questionnaire is intended to"
            " be used."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    lastReviewDate: fhirtypes.Date = Field(
        None,
        alias="lastReviewDate",
        title="When the questionnaire was last reviewed",
        description=(
            "The date on which the resource content was last reviewed. Review "
            "happens periodically after approval but does not change the original "
            "approval date."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastReviewDate", title="Extension field for ``lastReviewDate``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name for this questionnaire (computer friendly)",
        description=(
            "A natural language name identifying the questionnaire. This name "
            "should be usable as an identifier for the module by machine processing"
            " applications such as code generation."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the organization or individual that published the "
            "questionnaire."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Why this questionnaire is defined",
        description=(
            "Explanation of why this questionnaire is needed and why it has been "
            "designed as it has."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this questionnaire. Enables tracking the life-cycle of "
            "the content."
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

    subjectType: typing.List[typing.Optional[fhirtypes.Code]] = Field(
        None,
        alias="subjectType",
        title="Resource that can be subject of QuestionnaireResponse",
        description=(
            "The types of subjects that can be the subject of responses created for"
            " the questionnaire."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    subjectType__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_subjectType", title="Extension field for ``subjectType``.")

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Name for this questionnaire (human friendly)",
        description="A short, descriptive, user-friendly title for the questionnaire.",
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title=(
            "Canonical identifier for this questionnaire, represented as a URI "
            "(globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this questionnaire when it is"
            " referenced in a specification, model, design or an instance; also "
            "called its canonical identifier. This SHOULD be globally unique and "
            "SHOULD be a literal address at which at which an authoritative "
            "instance of this questionnaire is (or will be) published. This URL can"
            " be the target of a canonical reference. It SHALL remain the same when"
            " the questionnaire is stored on different servers."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    useContext: typing.List[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="The context that the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These contexts may be general categories "
            "(gender, age, ...) or may be references to specific programs "
            "(insurance plans, studies, ...) and may be used to assist with "
            "indexing and searching for appropriate questionnaire instances."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.String = Field(
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
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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
            "approvalDate",
            "lastReviewDate",
            "effectivePeriod",
            "code",
            "item",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1565(
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


class QuestionnaireItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Questions and sections within the Questionnaire.
    A particular question, question grouping or display text that is part of
    the questionnaire.
    """

    resource_type = Field("QuestionnaireItem", const=True)

    answerOption: typing.List[fhirtypes.QuestionnaireItemAnswerOptionType] = Field(
        None,
        alias="answerOption",
        title="Permitted answer",
        description='One of the permitted answers for a "choice" or "open-choice" question.',
        # if property is element of this resource.
        element_property=True,
    )

    answerValueSet: fhirtypes.Canonical = Field(
        None,
        alias="answerValueSet",
        title="Valueset containing permitted answers",
        description=(
            "A reference to a value set containing a list of codes representing "
            'permitted answers for a "choice" or "open-choice" question.'
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ValueSet"],
    )
    answerValueSet__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_answerValueSet", title="Extension field for ``answerValueSet``."
    )

    code: typing.List[fhirtypes.CodingType] = Field(
        None,
        alias="code",
        title="Corresponding concept for this item in a terminology",
        description=(
            "A terminology code that corresponds to this group or question (e.g. a "
            "code from LOINC, which defines many questions and answers)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    definition: fhirtypes.Uri = Field(
        None,
        alias="definition",
        title="ElementDefinition - details for the item",
        description=(
            "This element is a URI that refers to an "
            "[ElementDefinition](elementdefinition.html) that provides information "
            "about this item, including information that might otherwise be "
            "included in the instance of the Questionnaire resource. A detailed "
            "description of the construction of the URI is shown in Comments, "
            "below. If this element is present then the following element values "
            "MAY be derived from the Element Definition if the corresponding "
            "elements of this Questionnaire resource instance have no value:  * "
            "code (ElementDefinition.code)  * type (ElementDefinition.type)  * "
            "required (ElementDefinition.min)  * repeats (ElementDefinition.max)  *"
            " maxLength (ElementDefinition.maxLength)  * answerValueSet "
            "(ElementDefinition.binding) * options (ElementDefinition.binding)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_definition", title="Extension field for ``definition``."
    )

    enableBehavior: fhirtypes.Code = Field(
        None,
        alias="enableBehavior",
        title="all | any",
        description=(
            "Controls how multiple enableWhen values are interpreted -  whether all"
            " or any must be true."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["all", "any"],
    )
    enableBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_enableBehavior", title="Extension field for ``enableBehavior``."
    )

    enableWhen: typing.List[fhirtypes.QuestionnaireItemEnableWhenType] = Field(
        None,
        alias="enableWhen",
        title="Only allow data when",
        description=(
            "A constraint indicating that this item should only be enabled "
            "(displayed/allow answers to be captured) when the specified condition "
            "is true."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    initial: typing.List[fhirtypes.QuestionnaireItemInitialType] = Field(
        None,
        alias="initial",
        title="Initial value(s) when item is first rendered",
        description=(
            "One or more values that should be pre-populated in the answer when "
            "initially rendering the questionnaire for user input."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    item: typing.List[fhirtypes.QuestionnaireItemType] = Field(
        None,
        alias="item",
        title="Nested questionnaire items",
        description=(
            "Text, questions and other groups to be nested beneath a question or "
            "group."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    linkId: fhirtypes.String = Field(
        None,
        alias="linkId",
        title="Unique id for item in questionnaire",
        description=(
            "An identifier that is unique within the Questionnaire allowing linkage"
            " to the equivalent item in a QuestionnaireResponse resource."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_linkId", title="Extension field for ``linkId``."
    )

    maxLength: fhirtypes.Integer = Field(
        None,
        alias="maxLength",
        title="No more than this many characters",
        description=(
            "The maximum number of characters that are permitted in the answer to "
            'be considered a "valid" QuestionnaireResponse.'
        ),
        # if property is element of this resource.
        element_property=True,
    )
    maxLength__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_maxLength", title="Extension field for ``maxLength``."
    )

    prefix: fhirtypes.String = Field(
        None,
        alias="prefix",
        title='E.g. "1(a)", "2.5.3"',
        description=(
            "A short label for a particular group, question or set of display text "
            "within the questionnaire used for reference by the individual "
            "completing the questionnaire."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    prefix__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_prefix", title="Extension field for ``prefix``."
    )

    readOnly: bool = Field(
        None,
        alias="readOnly",
        title="Don't allow human editing",
        description=(
            "An indication, when true, that the value cannot be changed by a human "
            "respondent to the Questionnaire."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    readOnly__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_readOnly", title="Extension field for ``readOnly``."
    )

    repeats: bool = Field(
        None,
        alias="repeats",
        title="Whether the item may repeat",
        description=(
            "An indication, if true, that the item may occur multiple times in the "
            "response, collecting multiple answers for questions or multiple sets "
            "of answers for groups."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    repeats__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_repeats", title="Extension field for ``repeats``."
    )

    required: bool = Field(
        None,
        alias="required",
        title="Whether the item must be included in data results",
        description=(
            'An indication, if true, that the item must be present in a "completed"'
            " QuestionnaireResponse.  If false, the item may be skipped when "
            "answering the questionnaire."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    required__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_required", title="Extension field for ``required``."
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Primary text for the item",
        description=(
            "The name of a section, the text of a question or text content for a "
            "display item."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="group | display | boolean | decimal | integer | date | dateTime +",
        description=(
            "The type of questionnaire item this is - whether text for display, a "
            "grouping of other items or a particular type of data to be captured "
            "(string, integer, coded choice, etc.)."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "group",
            "display",
            "boolean",
            "decimal",
            "integer",
            "date",
            "dateTime",
            "+",
        ],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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
            "required",
            "repeats",
            "readOnly",
            "maxLength",
            "answerValueSet",
            "answerOption",
            "initial",
            "item",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1972(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("linkId", "linkId__ext"), ("type", "type__ext")]
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


class QuestionnaireItemAnswerOption(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Permitted answer.
    One of the permitted answers for a "choice" or "open-choice" question.
    """

    resource_type = Field("QuestionnaireItemAnswerOption", const=True)

    initialSelected: bool = Field(
        None,
        alias="initialSelected",
        title="Whether option is selected by default",
        description=(
            "Indicates whether the answer value is selected when the list of "
            "possible answers is initially shown."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    initialSelected__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_initialSelected", title="Extension field for ``initialSelected``."
    )

    valueCoding: fhirtypes.CodingType = Field(
        None,
        alias="valueCoding",
        title="Answer value",
        description="A potential answer that's allowed as the answer to this question.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueDate: fhirtypes.Date = Field(
        None,
        alias="valueDate",
        title="Answer value",
        description="A potential answer that's allowed as the answer to this question.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDate", title="Extension field for ``valueDate``."
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="Answer value",
        description="A potential answer that's allowed as the answer to this question.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueInteger", title="Extension field for ``valueInteger``."
    )

    valueReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueReference",
        title="Answer value",
        description="A potential answer that's allowed as the answer to this question.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Answer value",
        description="A potential answer that's allowed as the answer to this question.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    valueTime: fhirtypes.Time = Field(
        None,
        alias="valueTime",
        title="Answer value",
        description="A potential answer that's allowed as the answer to this question.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3230(
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
            "value": [
                "valueCoding",
                "valueDate",
                "valueInteger",
                "valueReference",
                "valueString",
                "valueTime",
            ]
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


class QuestionnaireItemEnableWhen(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Only allow data when.
    A constraint indicating that this item should only be enabled
    (displayed/allow answers to be captured) when the specified condition is
    true.
    """

    resource_type = Field("QuestionnaireItemEnableWhen", const=True)

    answerBoolean: bool = Field(
        None,
        alias="answerBoolean",
        title="Value for question comparison based on operator",
        description=(
            "A value that the referenced question is tested using the specified "
            "operator in order for the item to be enabled."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e answer[x]
        one_of_many="answer",
        one_of_many_required=True,
    )
    answerBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_answerBoolean", title="Extension field for ``answerBoolean``."
    )

    answerCoding: fhirtypes.CodingType = Field(
        None,
        alias="answerCoding",
        title="Value for question comparison based on operator",
        description=(
            "A value that the referenced question is tested using the specified "
            "operator in order for the item to be enabled."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e answer[x]
        one_of_many="answer",
        one_of_many_required=True,
    )

    answerDate: fhirtypes.Date = Field(
        None,
        alias="answerDate",
        title="Value for question comparison based on operator",
        description=(
            "A value that the referenced question is tested using the specified "
            "operator in order for the item to be enabled."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e answer[x]
        one_of_many="answer",
        one_of_many_required=True,
    )
    answerDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_answerDate", title="Extension field for ``answerDate``."
    )

    answerDateTime: fhirtypes.DateTime = Field(
        None,
        alias="answerDateTime",
        title="Value for question comparison based on operator",
        description=(
            "A value that the referenced question is tested using the specified "
            "operator in order for the item to be enabled."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e answer[x]
        one_of_many="answer",
        one_of_many_required=True,
    )
    answerDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_answerDateTime", title="Extension field for ``answerDateTime``."
    )

    answerDecimal: fhirtypes.Decimal = Field(
        None,
        alias="answerDecimal",
        title="Value for question comparison based on operator",
        description=(
            "A value that the referenced question is tested using the specified "
            "operator in order for the item to be enabled."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e answer[x]
        one_of_many="answer",
        one_of_many_required=True,
    )
    answerDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_answerDecimal", title="Extension field for ``answerDecimal``."
    )

    answerInteger: fhirtypes.Integer = Field(
        None,
        alias="answerInteger",
        title="Value for question comparison based on operator",
        description=(
            "A value that the referenced question is tested using the specified "
            "operator in order for the item to be enabled."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e answer[x]
        one_of_many="answer",
        one_of_many_required=True,
    )
    answerInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_answerInteger", title="Extension field for ``answerInteger``."
    )

    answerQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="answerQuantity",
        title="Value for question comparison based on operator",
        description=(
            "A value that the referenced question is tested using the specified "
            "operator in order for the item to be enabled."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e answer[x]
        one_of_many="answer",
        one_of_many_required=True,
    )

    answerReference: fhirtypes.ReferenceType = Field(
        None,
        alias="answerReference",
        title="Value for question comparison based on operator",
        description=(
            "A value that the referenced question is tested using the specified "
            "operator in order for the item to be enabled."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e answer[x]
        one_of_many="answer",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    answerString: fhirtypes.String = Field(
        None,
        alias="answerString",
        title="Value for question comparison based on operator",
        description=(
            "A value that the referenced question is tested using the specified "
            "operator in order for the item to be enabled."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e answer[x]
        one_of_many="answer",
        one_of_many_required=True,
    )
    answerString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_answerString", title="Extension field for ``answerString``."
    )

    answerTime: fhirtypes.Time = Field(
        None,
        alias="answerTime",
        title="Value for question comparison based on operator",
        description=(
            "A value that the referenced question is tested using the specified "
            "operator in order for the item to be enabled."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e answer[x]
        one_of_many="answer",
        one_of_many_required=True,
    )
    answerTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_answerTime", title="Extension field for ``answerTime``."
    )

    operator: fhirtypes.Code = Field(
        None,
        alias="operator",
        title="exists | = | != | > | < | >= | <=",
        description="Specifies the criteria by which the question is enabled.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["exists", "=", "!=", "\u003e", "\u003c", "\u003e=", "\u003c="],
    )
    operator__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_operator", title="Extension field for ``operator``."
    )

    question: fhirtypes.String = Field(
        None,
        alias="question",
        title="Question that determines whether item is enabled",
        description=(
            "The linkId for the question whose answer (or lack of answer) governs "
            "whether this item is enabled."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    question__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2958(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("operator", "operator__ext"), ("question", "question__ext")]
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2958(
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


class QuestionnaireItemInitial(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Initial value(s) when item is first rendered.
    One or more values that should be pre-populated in the answer when
    initially rendering the questionnaire for user input.
    """

    resource_type = Field("QuestionnaireItemInitial", const=True)

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="Actual value for initializing the question",
        description="The actual value to for an initial answer.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="Actual value for initializing the question",
        description="The actual value to for an initial answer.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCoding: fhirtypes.CodingType = Field(
        None,
        alias="valueCoding",
        title="Actual value for initializing the question",
        description="The actual value to for an initial answer.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueDate: fhirtypes.Date = Field(
        None,
        alias="valueDate",
        title="Actual value for initializing the question",
        description="The actual value to for an initial answer.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDate", title="Extension field for ``valueDate``."
    )

    valueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="valueDateTime",
        title="Actual value for initializing the question",
        description="The actual value to for an initial answer.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDateTime", title="Extension field for ``valueDateTime``."
    )

    valueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="valueDecimal",
        title="Actual value for initializing the question",
        description="The actual value to for an initial answer.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDecimal", title="Extension field for ``valueDecimal``."
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="Actual value for initializing the question",
        description="The actual value to for an initial answer.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueInteger", title="Extension field for ``valueInteger``."
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="Actual value for initializing the question",
        description="The actual value to for an initial answer.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueReference",
        title="Actual value for initializing the question",
        description="The actual value to for an initial answer.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Actual value for initializing the question",
        description="The actual value to for an initial answer.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    valueTime: fhirtypes.Time = Field(
        None,
        alias="valueTime",
        title="Actual value for initializing the question",
        description="The actual value to for an initial answer.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueTime", title="Extension field for ``valueTime``."
    )

    valueUri: fhirtypes.Uri = Field(
        None,
        alias="valueUri",
        title="Actual value for initializing the question",
        description="The actual value to for an initial answer.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2685(
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
