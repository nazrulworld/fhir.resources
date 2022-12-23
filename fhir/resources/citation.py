# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Citation
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class Citation(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A description of identification, location, or contributorship of a
    publication (article or artifact).
    The Citation Resource enables reference to any knowledge artifact for
    purposes of identification and attribution. The Citation Resource supports
    existing reference structures and developing publication practices such as
    versioning, expressing complex contributorship roles, and referencing
    computable resources.
    """

    resource_type = Field("Citation", const=True)

    approvalDate: fhirtypes.Date = Field(
        None,
        alias="approvalDate",
        title="When the citation was approved by publisher",
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

    author: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="author",
        title="Who authored the Citation",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    citedArtifact: fhirtypes.CitationCitedArtifactType = Field(
        None,
        alias="citedArtifact",
        title="The article or artifact being described",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    classification: typing.List[fhirtypes.CitationClassificationType] = Field(
        None,
        alias="classification",
        title="The assignment to an organizing scheme",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    contact: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="Contact details for the publisher of the Citation Resource",
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
        title=(
            "Use and/or publishing restrictions for the Citation, not for the cited"
            " artifact"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    currentState: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="currentState",
        title="The status of the citation",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the citation was published. The "
            "date must change when the business version changes and it must change "
            "if the status code changes. In addition, it should change when the "
            "substantive content of the citation changes."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Natural language description of the citation",
        description=(
            "A free text natural language description of the citation from a "
            "consumer's perspective."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    editor: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="editor",
        title="Who edited the Citation",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="When the citation is expected to be used",
        description=(
            "The period during which the citation content was or is planned to be "
            "in active use."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    endorser: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="endorser",
        title="Who endorsed the Citation",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this citation is authored for testing"
            " purposes (or education/evaluation/marketing) and is not intended to "
            "be used for genuine usage."
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
        title="Identifier for the Citation resource itself",
        description=(
            "A formal identifier that is used to identify this citation when it is "
            "represented in other formats, or referenced in a specification, model,"
            " design or an instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for citation (if applicable)",
        description=(
            "A legal or geographic region in which the citation is intended to be "
            "used."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    lastReviewDate: fhirtypes.Date = Field(
        None,
        alias="lastReviewDate",
        title="When the citation was last reviewed",
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
        title="Name for this citation (computer friendly)",
        description=(
            "A natural language name identifying the citation. This name should be "
            "usable as an identifier for the module by machine processing "
            "applications such as code generation."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Used for general notes and annotations not coded elsewhere",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title=(
            "The publisher of the Citation, not the publisher of the article or "
            "artifact being cited"
        ),
        description=(
            "The name of the organization or individual that published the " "citation."
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
        title="Why this citation is defined",
        description=(
            "Explanation of why this citation is needed and why it has been "
            "designed as it has."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    relatesTo: typing.List[fhirtypes.CitationRelatesToType] = Field(
        None,
        alias="relatesTo",
        title="Artifact related to the Citation Resource",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    reviewer: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="reviewer",
        title="Who reviewed the Citation",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this summary. Enables tracking the life-cycle of the "
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

    statusDate: typing.List[fhirtypes.CitationStatusDateType] = Field(
        None,
        alias="statusDate",
        title="An effective date or period for a status of the citation",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    summary: typing.List[fhirtypes.CitationSummaryType] = Field(
        None,
        alias="summary",
        title="A human-readable display of the citation",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Name for this citation (human friendly)",
        description="A short, descriptive, user-friendly title for the citation.",
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
            "Canonical identifier for this citation, represented as a globally "
            "unique URI"
        ),
        description=(
            "An absolute URI that is used to identify this citation when it is "
            "referenced in a specification, model, design or an instance; also "
            "called its canonical identifier. This SHOULD be globally unique and "
            "SHOULD be a literal address at which at which an authoritative "
            "instance of this summary is (or will be) published. This URL can be "
            "the target of a canonical reference. It SHALL remain the same when the"
            " summary is stored on different servers."
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
        title="The context that the Citation Resource content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These contexts may be general categories "
            "(gender, age, ...) or may be references to specific programs "
            "(insurance plans, studies, ...) and may be used to assist with "
            "indexing and searching for appropriate citation instances."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the citation",
        description=(
            "The identifier that is used to identify this version of the citation "
            "when it is referenced in a specification, model, design or instance. "
            "This is an arbitrary value managed by the citation author and is not "
            "expected to be globally unique. For example, it might be a timestamp "
            "(e.g. yyyymmdd) if a managed version is not available. There is also "
            "no expectation that versions can be placed in a lexicographical "
            "sequence."
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
        ``Citation`` according specification,
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
            "contact",
            "description",
            "useContext",
            "jurisdiction",
            "purpose",
            "copyright",
            "approvalDate",
            "lastReviewDate",
            "effectivePeriod",
            "author",
            "editor",
            "reviewer",
            "endorser",
            "summary",
            "classification",
            "note",
            "currentState",
            "statusDate",
            "relatesTo",
            "citedArtifact",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1004(
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


class CitationCitedArtifact(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The article or artifact being described.
    """

    resource_type = Field("CitationCitedArtifact", const=True)

    abstract: typing.List[fhirtypes.CitationCitedArtifactAbstractType] = Field(
        None,
        alias="abstract",
        title="Summary of the article or artifact",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    classification: typing.List[
        fhirtypes.CitationCitedArtifactClassificationType
    ] = Field(
        None,
        alias="classification",
        title="The assignment to an organizing scheme",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    contributorship: fhirtypes.CitationCitedArtifactContributorshipType = Field(
        None,
        alias="contributorship",
        title="Attribution of authors and other contributors",
        description=(
            "This element is used to list authors and other contributors, their "
            "contact information, specific contributions, and summary statements."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    currentState: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="currentState",
        title="The status of the cited artifact",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    dateAccessed: fhirtypes.DateTime = Field(
        None,
        alias="dateAccessed",
        title="When the cited artifact was accessed",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    dateAccessed__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_dateAccessed", title="Extension field for ``dateAccessed``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="May include DOI, PMID, PMCID, etc.",
        description=(
            "A formal identifier that is used to identify this citation when it is "
            "represented in other formats, or referenced in a specification, model,"
            " design or an instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Any additional information or content for the article or artifact",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    part: fhirtypes.CitationCitedArtifactPartType = Field(
        None,
        alias="part",
        title="The component of the article or artifact",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    publicationForm: typing.List[
        fhirtypes.CitationCitedArtifactPublicationFormType
    ] = Field(
        None,
        alias="publicationForm",
        title=(
            "If multiple, used to represent alternative forms of the article that "
            "are not separate citations"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    relatedIdentifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="relatedIdentifier",
        title="May include trial registry identifiers",
        description=(
            "A formal identifier that is used to identify things closely related to"
            " this citation."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    relatesTo: typing.List[fhirtypes.CitationCitedArtifactRelatesToType] = Field(
        None,
        alias="relatesTo",
        title="The artifact related to the cited artifact",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    statusDate: typing.List[fhirtypes.CitationCitedArtifactStatusDateType] = Field(
        None,
        alias="statusDate",
        title="An effective date or period for a status of the cited artifact",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    title: typing.List[fhirtypes.CitationCitedArtifactTitleType] = Field(
        None,
        alias="title",
        title="The title details of the article or artifact",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.CitationCitedArtifactVersionType = Field(
        None,
        alias="version",
        title="The defined version of the cited artifact",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    webLocation: typing.List[fhirtypes.CitationCitedArtifactWebLocationType] = Field(
        None,
        alias="webLocation",
        title="Used for any URL for the article or artifact cited",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CitationCitedArtifact`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "identifier",
            "relatedIdentifier",
            "dateAccessed",
            "version",
            "currentState",
            "statusDate",
            "title",
            "abstract",
            "part",
            "relatesTo",
            "publicationForm",
            "webLocation",
            "classification",
            "contributorship",
            "note",
        ]


class CitationCitedArtifactAbstract(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Summary of the article or artifact.
    """

    resource_type = Field("CitationCitedArtifactAbstract", const=True)

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Copyright notice for the abstract",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    language: fhirtypes.CodeableConceptType = Field(
        None,
        alias="language",
        title="Used to express the specific language",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    text: fhirtypes.Markdown = Field(
        None,
        alias="text",
        title="Abstract content",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="The kind of abstract",
        description="Used to express the reason or specific aspect for the abstract.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CitationCitedArtifactAbstract`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "language",
            "text",
            "copyright",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3133(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("text", "text__ext")]
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


class CitationCitedArtifactClassification(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The assignment to an organizing scheme.
    """

    resource_type = Field("CitationCitedArtifactClassification", const=True)

    classifier: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="classifier",
        title="The specific classification value",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="The kind of classifier (e.g. publication type, keyword)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    whoClassified: fhirtypes.CitationCitedArtifactClassificationWhoClassifiedType = Field(
        None,
        alias="whoClassified",
        title="Provenance and copyright of classification",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CitationCitedArtifactClassification`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "classifier",
            "whoClassified",
        ]


class CitationCitedArtifactClassificationWhoClassified(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Provenance and copyright of classification.
    """

    resource_type = Field(
        "CitationCitedArtifactClassificationWhoClassified", const=True
    )

    classifierCopyright: fhirtypes.String = Field(
        None,
        alias="classifierCopyright",
        title="Rights management statement for the classification",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    classifierCopyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_classifierCopyright",
        title="Extension field for ``classifierCopyright``.",
    )

    freeToShare: bool = Field(
        None,
        alias="freeToShare",
        title="Acceptable to re-use the classification",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    freeToShare__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_freeToShare", title="Extension field for ``freeToShare``."
    )

    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title="Organization who created the classification",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    person: fhirtypes.ReferenceType = Field(
        None,
        alias="person",
        title="Person who created the classification",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Person", "Practitioner"],
    )

    publisher: fhirtypes.ReferenceType = Field(
        None,
        alias="publisher",
        title=(
            "The publisher of the classification, not the publisher of the article "
            "or artifact being cited"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CitationCitedArtifactClassificationWhoClassified`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "person",
            "organization",
            "publisher",
            "classifierCopyright",
            "freeToShare",
        ]


class CitationCitedArtifactContributorship(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Attribution of authors and other contributors.
    This element is used to list authors and other contributors, their contact
    information, specific contributions, and summary statements.
    """

    resource_type = Field("CitationCitedArtifactContributorship", const=True)

    complete: bool = Field(
        None,
        alias="complete",
        title="Indicates if the list includes all authors and/or contributors",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    complete__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_complete", title="Extension field for ``complete``."
    )

    entry: typing.List[fhirtypes.CitationCitedArtifactContributorshipEntryType] = Field(
        None,
        alias="entry",
        title="An individual entity named in the list",
        description="An individual entity named in the author list or contributor list.",
        # if property is element of this resource.
        element_property=True,
    )

    summary: typing.List[
        fhirtypes.CitationCitedArtifactContributorshipSummaryType
    ] = Field(
        None,
        alias="summary",
        title=(
            "Used to record a display of the author/contributor list without "
            "separate coding for each list member"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CitationCitedArtifactContributorship`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "complete", "entry", "summary"]


class CitationCitedArtifactContributorshipEntry(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An individual entity named in the list.
    An individual entity named in the author list or contributor list.
    """

    resource_type = Field("CitationCitedArtifactContributorshipEntry", const=True)

    address: typing.List[fhirtypes.AddressType] = Field(
        None,
        alias="address",
        title="Physical mailing address",
        description="Physical mailing address for the author or contributor.",
        # if property is element of this resource.
        element_property=True,
    )

    affiliationInfo: typing.List[
        fhirtypes.CitationCitedArtifactContributorshipEntryAffiliationInfoType
    ] = Field(
        None,
        alias="affiliationInfo",
        title="Organizational affiliation",
        description="Organization affiliated with the entity.",
        # if property is element of this resource.
        element_property=True,
    )

    collectiveName: fhirtypes.String = Field(
        None,
        alias="collectiveName",
        title="Used for collective or corporate name as an author",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    collectiveName__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_collectiveName", title="Extension field for ``collectiveName``."
    )

    contributionInstance: typing.List[
        fhirtypes.CitationCitedArtifactContributorshipEntryContributionInstanceType
    ] = Field(
        None,
        alias="contributionInstance",
        title="Contributions with accounting for time or number",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    contributionType: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="contributionType",
        title="The specific contribution",
        description=(
            "This element identifies the specific nature of an individual\u2019s "
            "contribution with respect to the cited work."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    correspondingContact: bool = Field(
        None,
        alias="correspondingContact",
        title=(
            "Indication of which contributor is the corresponding contributor for "
            "the role"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    correspondingContact__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_correspondingContact",
        title="Extension field for ``correspondingContact``.",
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Author identifier, eg ORCID",
        description="Unique person identifier.",
        # if property is element of this resource.
        element_property=True,
    )

    initials: fhirtypes.String = Field(
        None,
        alias="initials",
        title="Initials for forename",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    initials__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_initials", title="Extension field for ``initials``."
    )

    listOrder: fhirtypes.PositiveInt = Field(
        None,
        alias="listOrder",
        title="Used to code order of authors",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    listOrder__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_listOrder", title="Extension field for ``listOrder``."
    )

    name: fhirtypes.HumanNameType = Field(
        None,
        alias="name",
        title="A name associated with the person",
        description="A name associated with the individual.",
        # if property is element of this resource.
        element_property=True,
    )

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="The role of the contributor (e.g. author, editor, reviewer)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    telecom: typing.List[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="Email or telephone contact methods for the author or contributor",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CitationCitedArtifactContributorshipEntry`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "name",
            "initials",
            "collectiveName",
            "identifier",
            "affiliationInfo",
            "address",
            "telecom",
            "contributionType",
            "role",
            "contributionInstance",
            "correspondingContact",
            "listOrder",
        ]


class CitationCitedArtifactContributorshipEntryAffiliationInfo(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Organizational affiliation.
    Organization affiliated with the entity.
    """

    resource_type = Field(
        "CitationCitedArtifactContributorshipEntryAffiliationInfo", const=True
    )

    affiliation: fhirtypes.String = Field(
        None,
        alias="affiliation",
        title="Display for the organization",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    affiliation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_affiliation", title="Extension field for ``affiliation``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Identifier for the organization",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    role: fhirtypes.String = Field(
        None,
        alias="role",
        title="Role within the organization, such as professional title",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    role__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_role", title="Extension field for ``role``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CitationCitedArtifactContributorshipEntryAffiliationInfo`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "affiliation",
            "role",
            "identifier",
        ]


class CitationCitedArtifactContributorshipEntryContributionInstance(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Contributions with accounting for time or number.
    """

    resource_type = Field(
        "CitationCitedArtifactContributorshipEntryContributionInstance", const=True
    )

    time: fhirtypes.DateTime = Field(
        None,
        alias="time",
        title="The time that the contribution was made",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    time__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_time", title="Extension field for ``time``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="The specific contribution",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CitationCitedArtifactContributorship
        EntryContributionInstance`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "time"]


class CitationCitedArtifactContributorshipSummary(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Used to record a display of the author/contributor list without separate
    coding for each list member.
    """

    resource_type = Field("CitationCitedArtifactContributorshipSummary", const=True)

    source: fhirtypes.CodeableConceptType = Field(
        None,
        alias="source",
        title="Used to code the producer or rule for creating the display string",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    style: fhirtypes.CodeableConceptType = Field(
        None,
        alias="style",
        title="The format for the display string",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Either authorList or contributorshipStatement",
        description=(
            "Used most commonly to express an author list or a contributorship "
            "statement."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    value: fhirtypes.Markdown = Field(
        None,
        alias="value",
        title=(
            "The display string for the author list, contributor list, or "
            "contributorship statement"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CitationCitedArtifactContributorshipSummary`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "style",
            "source",
            "value",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_4683(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("value", "value__ext")]
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


class CitationCitedArtifactPart(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The component of the article or artifact.
    """

    resource_type = Field("CitationCitedArtifactPart", const=True)

    baseCitation: fhirtypes.ReferenceType = Field(
        None,
        alias="baseCitation",
        title="The citation for the full article or artifact",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Citation"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="The kind of component",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="The specification of the component",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CitationCitedArtifactPart`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "value", "baseCitation"]


class CitationCitedArtifactPublicationForm(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    If multiple, used to represent alternative forms of the article that are
    not separate citations.
    """

    resource_type = Field("CitationCitedArtifactPublicationForm", const=True)

    accessionNumber: fhirtypes.String = Field(
        None,
        alias="accessionNumber",
        title="Entry number or identifier for inclusion in a database",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    accessionNumber__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_accessionNumber", title="Extension field for ``accessionNumber``."
    )

    articleDate: fhirtypes.DateTime = Field(
        None,
        alias="articleDate",
        title=(
            "The date the article was added to the database, or the date the "
            "article was released"
        ),
        description=(
            "The date the article was added to the database, or the date the "
            "article was released (which may differ from the journal issue "
            "publication date)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    articleDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_articleDate", title="Extension field for ``articleDate``."
    )

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Copyright notice for the full article or artifact",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    firstPage: fhirtypes.String = Field(
        None,
        alias="firstPage",
        title="Used for isolated representation of first page",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    firstPage__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_firstPage", title="Extension field for ``firstPage``."
    )

    language: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="language",
        title="Language in which this form of the article is published",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    lastPage: fhirtypes.String = Field(
        None,
        alias="lastPage",
        title="Used for isolated representation of last page",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    lastPage__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastPage", title="Extension field for ``lastPage``."
    )

    lastRevisionDate: fhirtypes.DateTime = Field(
        None,
        alias="lastRevisionDate",
        title="The date the article was last revised or updated in the database",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    lastRevisionDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_lastRevisionDate",
        title="Extension field for ``lastRevisionDate``.",
    )

    pageCount: fhirtypes.String = Field(
        None,
        alias="pageCount",
        title="Number of pages or screens",
        description="Actual or approximate number of pages or screens.",
        # if property is element of this resource.
        element_property=True,
    )
    pageCount__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_pageCount", title="Extension field for ``pageCount``."
    )

    pageString: fhirtypes.String = Field(
        None,
        alias="pageString",
        title="Used for full display of pagination",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    pageString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_pageString", title="Extension field for ``pageString``."
    )

    periodicRelease: fhirtypes.CitationCitedArtifactPublicationFormPeriodicReleaseType = Field(
        None,
        alias="periodicRelease",
        title="The specific issue in which the cited article resides",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    publishedIn: fhirtypes.CitationCitedArtifactPublicationFormPublishedInType = Field(
        None,
        alias="publishedIn",
        title="The collection the cited article or artifact is published in",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CitationCitedArtifactPublicationForm`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "publishedIn",
            "periodicRelease",
            "articleDate",
            "lastRevisionDate",
            "language",
            "accessionNumber",
            "pageString",
            "firstPage",
            "lastPage",
            "pageCount",
            "copyright",
        ]


class CitationCitedArtifactPublicationFormPeriodicRelease(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The specific issue in which the cited article resides.
    """

    resource_type = Field(
        "CitationCitedArtifactPublicationFormPeriodicRelease", const=True
    )

    citedMedium: fhirtypes.CodeableConceptType = Field(
        None,
        alias="citedMedium",
        title="Internet or Print",
        description=(
            'Describes the form of the medium cited. Common codes are "Internet" or'
            ' "Print".'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    dateOfPublication: fhirtypes.CitationCitedArtifactPublicationFormPeriodicReleaseDateOfPublicationType = Field(  # noqa: B950
        None,
        alias="dateOfPublication",
        title="Defining the date on which the issue of the journal was published",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    issue: fhirtypes.String = Field(
        None,
        alias="issue",
        title="Issue, part or supplement of journal in which the article is published",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    issue__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_issue", title="Extension field for ``issue``."
    )

    volume: fhirtypes.String = Field(
        None,
        alias="volume",
        title="Volume number of journal in which the article is published",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    volume__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_volume", title="Extension field for ``volume``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CitationCitedArtifactPublicationFormPeriodicRelease`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "citedMedium",
            "volume",
            "issue",
            "dateOfPublication",
        ]


class CitationCitedArtifactPublicationFormPeriodicReleaseDateOfPublication(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Defining the date on which the issue of the journal was published.
    """

    resource_type = Field(
        "CitationCitedArtifactPublicationFormPeriodicReleaseDateOfPublication",
        const=True,
    )

    date: fhirtypes.Date = Field(
        None,
        alias="date",
        title="Date on which the issue of the journal was published",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    day: fhirtypes.String = Field(
        None,
        alias="day",
        title="Day on which the issue of the journal was published",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    day__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_day", title="Extension field for ``day``."
    )

    month: fhirtypes.String = Field(
        None,
        alias="month",
        title="Month on which the issue of the journal was published",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    month__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_month", title="Extension field for ``month``."
    )

    season: fhirtypes.String = Field(
        None,
        alias="season",
        title="Season on which the issue of the journal was published",
        description="Spring, Summer, Fall/Autumn, Winter.",
        # if property is element of this resource.
        element_property=True,
    )
    season__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_season", title="Extension field for ``season``."
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title=(
            "Text representation of the date of which the issue of the journal was "
            "published"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )

    year: fhirtypes.String = Field(
        None,
        alias="year",
        title="Year on which the issue of the journal was published",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    year__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_year", title="Extension field for ``year``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CitationCitedArtifactPublication
        FormPeriodicReleaseDateOfPublication`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "date",
            "year",
            "month",
            "day",
            "season",
            "text",
        ]


class CitationCitedArtifactPublicationFormPublishedIn(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The collection the cited article or artifact is published in.
    """

    resource_type = Field("CitationCitedArtifactPublicationFormPublishedIn", const=True)

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title=(
            "Journal identifiers include ISSN, ISO Abbreviation and NLMuniqueID; "
            "Book identifiers include ISBN"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    publisher: fhirtypes.ReferenceType = Field(
        None,
        alias="publisher",
        title="Name of the publisher",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    publisherLocation: fhirtypes.String = Field(
        None,
        alias="publisherLocation",
        title="Geographic location of the publisher",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    publisherLocation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_publisherLocation",
        title="Extension field for ``publisherLocation``.",
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Name of the database or title of the book or journal",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Kind of container (e.g. Periodical, database, or book)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CitationCitedArtifactPublicationFormPublishedIn`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "identifier",
            "title",
            "publisher",
            "publisherLocation",
        ]


class CitationCitedArtifactRelatesTo(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The artifact related to the cited artifact.
    """

    resource_type = Field("CitationCitedArtifactRelatesTo", const=True)

    relationshipType: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="relationshipType",
        title="How the cited artifact relates to the target artifact",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    targetAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="targetAttachment",
        title="The article or artifact that the cited artifact is related to",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e target[x]
        one_of_many="target",
        one_of_many_required=True,
    )

    targetClassifier: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="targetClassifier",
        title="The clasification of the related artifact",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    targetIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="targetIdentifier",
        title="The article or artifact that the cited artifact is related to",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e target[x]
        one_of_many="target",
        one_of_many_required=True,
    )

    targetReference: fhirtypes.ReferenceType = Field(
        None,
        alias="targetReference",
        title="The article or artifact that the cited artifact is related to",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e target[x]
        one_of_many="target",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    targetUri: fhirtypes.Uri = Field(
        None,
        alias="targetUri",
        title="The article or artifact that the cited artifact is related to",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e target[x]
        one_of_many="target",
        one_of_many_required=True,
    )
    targetUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_targetUri", title="Extension field for ``targetUri``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CitationCitedArtifactRelatesTo`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "relationshipType",
            "targetClassifier",
            "targetUri",
            "targetIdentifier",
            "targetReference",
            "targetAttachment",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3223(
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
            "target": [
                "targetAttachment",
                "targetIdentifier",
                "targetReference",
                "targetUri",
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


class CitationCitedArtifactStatusDate(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An effective date or period for a status of the cited artifact.
    """

    resource_type = Field("CitationCitedArtifactStatusDate", const=True)

    activity: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="activity",
        title="Classification of the status",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    actual: bool = Field(
        None,
        alias="actual",
        title="Either occurred or expected",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    actual__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_actual", title="Extension field for ``actual``."
    )

    period: fhirtypes.PeriodType = Field(
        ...,
        alias="period",
        title="When the status started and/or ended",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CitationCitedArtifactStatusDate`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "activity", "actual", "period"]


class CitationCitedArtifactTitle(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The title details of the article or artifact.
    """

    resource_type = Field("CitationCitedArtifactTitle", const=True)

    language: fhirtypes.CodeableConceptType = Field(
        None,
        alias="language",
        title="Used to express the specific language",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    text: fhirtypes.Markdown = Field(
        None,
        alias="text",
        title="The title of the article or artifact",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )

    type: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="The kind of title",
        description="Used to express the reason or specific aspect for the title.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CitationCitedArtifactTitle`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "language", "text"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2812(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("text", "text__ext")]
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


class CitationCitedArtifactVersion(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The defined version of the cited artifact.
    """

    resource_type = Field("CitationCitedArtifactVersion", const=True)

    baseCitation: fhirtypes.ReferenceType = Field(
        None,
        alias="baseCitation",
        title="Citation for the main version of the cited artifact",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Citation"],
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="The version number or other version identifier",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CitationCitedArtifactVersion`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "value", "baseCitation"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3049(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("value", "value__ext")]
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


class CitationCitedArtifactWebLocation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Used for any URL for the article or artifact cited.
    """

    resource_type = Field("CitationCitedArtifactWebLocation", const=True)

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Code the reason for different URLs, e.g. abstract and full-text",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="The specific URL",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CitationCitedArtifactWebLocation`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "url"]


class CitationClassification(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The assignment to an organizing scheme.
    """

    resource_type = Field("CitationClassification", const=True)

    classifier: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="classifier",
        title="The specific classification value",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="The kind of classifier (e.g. publication type, keyword)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CitationClassification`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "classifier"]


class CitationRelatesTo(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Artifact related to the Citation Resource.
    """

    resource_type = Field("CitationRelatesTo", const=True)

    relationshipType: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="relationshipType",
        title="How the Citation resource relates to the target artifact",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    targetAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="targetAttachment",
        title="The article or artifact that the Citation Resource is related to",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e target[x]
        one_of_many="target",
        one_of_many_required=True,
    )

    targetClassifier: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="targetClassifier",
        title="The clasification of the related artifact",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    targetIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="targetIdentifier",
        title="The article or artifact that the Citation Resource is related to",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e target[x]
        one_of_many="target",
        one_of_many_required=True,
    )

    targetReference: fhirtypes.ReferenceType = Field(
        None,
        alias="targetReference",
        title="The article or artifact that the Citation Resource is related to",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e target[x]
        one_of_many="target",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    targetUri: fhirtypes.Uri = Field(
        None,
        alias="targetUri",
        title="The article or artifact that the Citation Resource is related to",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e target[x]
        one_of_many="target",
        one_of_many_required=True,
    )
    targetUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_targetUri", title="Extension field for ``targetUri``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CitationRelatesTo`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "relationshipType",
            "targetClassifier",
            "targetUri",
            "targetIdentifier",
            "targetReference",
            "targetAttachment",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1920(
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
            "target": [
                "targetAttachment",
                "targetIdentifier",
                "targetReference",
                "targetUri",
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


class CitationStatusDate(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An effective date or period for a status of the citation.
    """

    resource_type = Field("CitationStatusDate", const=True)

    activity: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="activity",
        title="Classification of the status",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    actual: bool = Field(
        None,
        alias="actual",
        title="Either occurred or expected",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    actual__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_actual", title="Extension field for ``actual``."
    )

    period: fhirtypes.PeriodType = Field(
        ...,
        alias="period",
        title="When the status started and/or ended",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CitationStatusDate`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "activity", "actual", "period"]


class CitationSummary(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A human-readable display of the citation.
    """

    resource_type = Field("CitationSummary", const=True)

    style: fhirtypes.CodeableConceptType = Field(
        None,
        alias="style",
        title="Format for display of the citation",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    text: fhirtypes.Markdown = Field(
        None,
        alias="text",
        title="The human-readable display of the citation",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CitationSummary`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "style", "text"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1765(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("text", "text__ext")]
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
