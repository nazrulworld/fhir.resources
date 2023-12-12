# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Citation
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

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
        title="When the citation record was approved by publisher",
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
        title="Who authored the citation record",
        description="Who authored or created the citation record.",
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
        title="Contact details for the publisher of the citation record",
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
            "Use and/or publishing restrictions for the citation record, not for "
            "the cited artifact"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    copyrightLabel: fhirtypes.String = Field(
        None,
        alias="copyrightLabel",
        title=(
            "Copyright holder and year(s) for the ciation record, not for the cited"
            " artifact"
        ),
        description=(
            "A short string (<50 characters), suitable for inclusion in a page "
            "footer that identifies the copyright holder, effective period, and "
            "optionally whether rights are resctricted. (e.g. 'All rights "
            "reserved', 'Some rights reserved')."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    copyrightLabel__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyrightLabel", title="Extension field for ``copyrightLabel``."
    )

    currentState: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="currentState",
        title="The status of the citation record",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date last changed",
        description=(
            "The date (and optionally time) when the citation record was last "
            "significantly changed. The date must change when the business version "
            "changes and it must change if the status code changes. In addition, it"
            " should change when the substantive content of the citation record "
            "changes."
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
        title="Who edited the citation record",
        description="Who edited or revised the citation record.",
        # if property is element of this resource.
        element_property=True,
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="When the citation record is expected to be used",
        description=(
            "The period during which the citation record content was or is planned "
            "to be in active use."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    endorser: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="endorser",
        title="Who endorsed the citation record",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this citation record is authored for "
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
        title="Identifier for the citation record itself",
        description=(
            "A formal identifier that is used to identify this citation record when"
            " it is represented in other formats, or referenced in a specification,"
            " model, design or an instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for citation record (if applicable)",
        description=(
            "A legal or geographic region in which the citation record is intended "
            "to be used."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    lastReviewDate: fhirtypes.Date = Field(
        None,
        alias="lastReviewDate",
        title="When the citation record was last reviewed by the publisher",
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
        title="Name for this citation record (computer friendly)",
        description=(
            "A natural language name identifying the citation record. This name "
            "should be usable as an identifier for the module by machine processing"
            " applications such as code generation."
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
            "The publisher of the citation record, not the publisher of the article"
            " or artifact being cited"
        ),
        description=(
            "The name of the organization or individual that published the citation"
            " record."
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

    relatedArtifact: typing.List[fhirtypes.RelatedArtifactType] = Field(
        None,
        alias="relatedArtifact",
        title="Artifact related to the citation record",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    reviewer: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="reviewer",
        title="Who reviewed the citation record",
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
        title="An effective date or period for a status of the citation record",
        description=(
            "The state or status of the citation record paired with an effective "
            "date or period for that state."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    summary: typing.List[fhirtypes.CitationSummaryType] = Field(
        None,
        alias="summary",
        title="A human-readable display of key concepts to represent the citation",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Name for this citation record (human friendly)",
        description="A short, descriptive, user-friendly title for the citation record.",
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
            "Canonical identifier for this citation record, represented as a "
            "globally unique URI"
        ),
        description=(
            "An absolute URI that is used to identify this citation record when it "
            "is referenced in a specification, model, design or an instance; also "
            "called its canonical identifier. This SHOULD be globally unique and "
            "SHOULD be a literal address at which an authoritative instance of this"
            " summary is (or will be) published. This URL can be the target of a "
            "canonical reference. It SHALL remain the same when the summary is "
            "stored on different servers."
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
        title="The context that the citation record content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These contexts may be general categories "
            "(gender, age, ...) or may be references to specific programs "
            "(insurance plans, studies, ...) and may be used to assist with "
            "indexing and searching for appropriate citation record instances."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the citation record",
        description=(
            "The identifier that is used to identify this version of the citation "
            "record when it is referenced in a specification, model, design or "
            "instance. This is an arbitrary value managed by the citation record "
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

    versionAlgorithmCoding: fhirtypes.CodingType = Field(
        None,
        alias="versionAlgorithmCoding",
        title="How to compare versions",
        description=(
            "Indicates the mechanism used to compare versions to determine which is"
            " more current."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e versionAlgorithm[x]
        one_of_many="versionAlgorithm",
        one_of_many_required=False,
    )

    versionAlgorithmString: fhirtypes.String = Field(
        None,
        alias="versionAlgorithmString",
        title="How to compare versions",
        description=(
            "Indicates the mechanism used to compare versions to determine which is"
            " more current."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e versionAlgorithm[x]
        one_of_many="versionAlgorithm",
        one_of_many_required=False,
    )
    versionAlgorithmString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_versionAlgorithmString",
        title="Extension field for ``versionAlgorithmString``.",
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
            "versionAlgorithmString",
            "versionAlgorithmCoding",
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
            "copyrightLabel",
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
            "relatedArtifact",
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1004(
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
            "versionAlgorithm": ["versionAlgorithmCoding", "versionAlgorithmString"]
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
        description=(
            "The abstract may be used to convey article-contained abstracts, "
            "externally-created abstracts, or other descriptive summaries."
        ),
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
        title="Unique identifier. May include DOI, PMID, PMCID, etc",
        description=(
            "A formal identifier that is used to identify the cited artifact when "
            "it is represented in other formats, or referenced in a specification, "
            "model, design or an instance."
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
        title=(
            "Identifier not unique to the cited artifact. May include trial "
            "registry identifiers"
        ),
        description=(
            "A formal identifier that is used to identify things closely related to"
            " the cited artifact."
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
        description=(
            "An effective date or period, historical or future, actual or expected,"
            " for a status of the cited artifact."
        ),
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
    The abstract may be used to convey article-contained abstracts, externally-
    created abstracts, or other descriptive summaries.
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
        description="Used to express the specific language of the abstract.",
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
        description="Used to express the reason for or classification of the abstract.",
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

    artifactAssessment: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="artifactAssessment",
        title="Complex or externally created classification",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ArtifactAssessment"],
    )

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
        ``CitationCitedArtifactClassification`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "classifier",
            "artifactAssessment",
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
        title="An individual entity named as a contributor",
        description=(
            "An individual entity named as a contributor, for example in the author"
            " list or contributor list."
        ),
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
            "separate data element for each list member"
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

    An individual entity named as a contributor.
    An individual entity named as a contributor, for example in the author list
    or contributor list.
    """

    resource_type = Field("CitationCitedArtifactContributorshipEntry", const=True)

    affiliation: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="affiliation",
        title="Organizational affiliation",
        description="Organization affiliated with the contributor.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization", "PractitionerRole"],
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

    contributor: fhirtypes.ReferenceType = Field(
        ...,
        alias="contributor",
        title="The identity of the individual contributor",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Organization"],
    )

    correspondingContact: bool = Field(
        None,
        alias="correspondingContact",
        title="Whether the contributor is the corresponding contributor for the role",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    correspondingContact__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_correspondingContact",
        title="Extension field for ``correspondingContact``.",
    )

    forenameInitials: fhirtypes.String = Field(
        None,
        alias="forenameInitials",
        title="For citation styles that use initials",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    forenameInitials__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_forenameInitials",
        title="Extension field for ``forenameInitials``.",
    )

    rankingOrder: fhirtypes.PositiveInt = Field(
        None,
        alias="rankingOrder",
        title="Ranked order of contribution",
        description=(
            "Provides a numerical ranking to represent the degree of "
            "contributorship relative to other contributors, such as 1 for first "
            "author and 2 for second author."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    rankingOrder__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_rankingOrder", title="Extension field for ``rankingOrder``."
    )

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="The role of the contributor (e.g. author, editor, reviewer, funder)",
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
            "contributor",
            "forenameInitials",
            "affiliation",
            "contributionType",
            "role",
            "contributionInstance",
            "correspondingContact",
            "rankingOrder",
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
        ``CitationCitedArtifactContributorshipEntryContributionInstance``
        according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "time"]


class CitationCitedArtifactContributorshipSummary(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Used to record a display of the author/contributor list without separate
    data element for each list member.
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
        description=(
            "The format for the display string, such as author last name with first"
            " letter capitalized followed by forename initials."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title=(
            "Such as author list, contributorship statement, funding statement, "
            "acknowledgements statement, or conflicts of interest statement"
        ),
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
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    articleDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_articleDate", title="Extension field for ``articleDate``."
    )

    citedMedium: fhirtypes.CodeableConceptType = Field(
        None,
        alias="citedMedium",
        title="Internet or Print",
        description=(
            'Describes the form of the medium cited. Common codes are "Internet" or'
            ' "Print". The CitedMedium value set has 6 codes. The codes internet, '
            "print, and offline-digital-storage are the common codes for a typical "
            "publication form, though internet and print are more common for study "
            "citations. Three additional codes (each appending one of the primary "
            'codes with "-without-issue" are used for situations when a study is '
            "published both within an issue (of a periodical release as commonly "
            "done for journals) AND is published separately from the issue (as "
            "commonly done with early online publication), to represent specific "
            "identification of the publication form not associated with the issue."
        ),
        # if property is element of this resource.
        element_property=True,
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

    issue: fhirtypes.String = Field(
        None,
        alias="issue",
        title=(
            "Issue, part or supplement of journal or other collection in which the "
            "article is published"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    issue__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_issue", title="Extension field for ``issue``."
    )

    language: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="language",
        title="Language(s) in which this form of the article is published",
        description=(
            "The language or languages in which this form of the article is "
            "published."
        ),
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
        description=(
            "Actual or approximate number of pages or screens. Distinct from "
            "reporting the page numbers."
        ),
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

    publicationDateSeason: fhirtypes.String = Field(
        None,
        alias="publicationDateSeason",
        title="Season in which the cited artifact was published",
        description="Spring, Summer, Fall/Autumn, Winter.",
        # if property is element of this resource.
        element_property=True,
    )
    publicationDateSeason__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_publicationDateSeason",
        title="Extension field for ``publicationDateSeason``.",
    )

    publicationDateText: fhirtypes.String = Field(
        None,
        alias="publicationDateText",
        title=(
            "Text representation of the date on which the issue of the cited "
            "artifact was published"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    publicationDateText__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_publicationDateText",
        title="Extension field for ``publicationDateText``.",
    )

    publishedIn: fhirtypes.CitationCitedArtifactPublicationFormPublishedInType = Field(
        None,
        alias="publishedIn",
        title="The collection the cited article or artifact is published in",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    volume: fhirtypes.String = Field(
        None,
        alias="volume",
        title=(
            "Volume number of journal or other collection in which the article is "
            "published"
        ),
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
        ``CitationCitedArtifactPublicationForm`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "publishedIn",
            "citedMedium",
            "volume",
            "issue",
            "articleDate",
            "publicationDateText",
            "publicationDateSeason",
            "lastRevisionDate",
            "language",
            "accessionNumber",
            "pageString",
            "firstPage",
            "lastPage",
            "pageCount",
            "copyright",
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
        title="Name of or resource describing the publisher",
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

    citation: fhirtypes.Markdown = Field(
        None,
        alias="citation",
        title="Bibliographic citation for the artifact",
        description=(
            "A bibliographic citation for the related artifact. This text SHOULD be"
            " formatted according to an accepted citation format."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    citation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_citation", title="Extension field for ``citation``."
    )

    classifier: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="classifier",
        title="Additional classifiers",
        description="Provides additional classifiers of the related artifact.",
        # if property is element of this resource.
        element_property=True,
    )

    display: fhirtypes.String = Field(
        None,
        alias="display",
        title="Brief description of the related artifact",
        description=(
            "A brief description of the document or knowledge resource being "
            "referenced, suitable for display to a consumer."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_display", title="Extension field for ``display``."
    )

    document: fhirtypes.AttachmentType = Field(
        None,
        alias="document",
        title="What document is being referenced",
        description=(
            "The document being referenced, represented as an attachment. Do not "
            "use this element if using the resource element to provide the "
            "canonical to the related artifact."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    label: fhirtypes.String = Field(
        None,
        alias="label",
        title="Short label",
        description=(
            "A short label that can be used to reference the related artifact from "
            "elsewhere in the containing artifact, such as a footnote index."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    label__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_label", title="Extension field for ``label``."
    )

    resource: fhirtypes.Canonical = Field(
        None,
        alias="resource",
        title="What artifact is being referenced",
        description=(
            "The related artifact, such as a library, value set, profile, or other "
            "knowledge resource."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    resource__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_resource", title="Extension field for ``resource``."
    )

    resourceReference: fhirtypes.ReferenceType = Field(
        None,
        alias="resourceReference",
        title="What artifact, if not a conformance resource",
        description=(
            "The related artifact, if the artifact is not a canonical resource, or "
            "a resource reference to a canonical resource."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title=(
            "documentation | justification | citation | predecessor | successor | "
            "derived-from | depends-on | composed-of | part-of | amends | amended-"
            "with | appends | appended-with | cites | cited-by | comments-on | "
            "comment-in | contains | contained-in | corrects | correction-in | "
            "replaces | replaced-with | retracts | retracted-by | signs | similar-"
            "to | supports | supported-with | transforms | transformed-into | "
            "transformed-with | documents | specification-of | created-with | cite-"
            "as | reprint | reprint-of"
        ),
        description="The type of relationship to the related artifact.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "documentation",
            "justification",
            "citation",
            "predecessor",
            "successor",
            "derived-from",
            "depends-on",
            "composed-of",
            "part-of",
            "amends",
            "amended-with",
            "appends",
            "appended-with",
            "cites",
            "cited-by",
            "comments-on",
            "comment-in",
            "contains",
            "contained-in",
            "corrects",
            "correction-in",
            "replaces",
            "replaced-with",
            "retracts",
            "retracted-by",
            "signs",
            "similar-to",
            "supports",
            "supported-with",
            "transforms",
            "transformed-into",
            "transformed-with",
            "documents",
            "specification-of",
            "created-with",
            "cite-as",
            "reprint",
            "reprint-of",
        ],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
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
            "type",
            "classifier",
            "label",
            "display",
            "citation",
            "document",
            "resource",
            "resourceReference",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3223(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("type", "type__ext")]
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


class CitationCitedArtifactStatusDate(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An effective date or period for a status of the cited artifact.
    An effective date or period, historical or future, actual or expected, for
    a status of the cited artifact.
    """

    resource_type = Field("CitationCitedArtifactStatusDate", const=True)

    activity: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="activity",
        title="Classification of the status",
        description="A definition of the status associated with a date or period.",
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
        description="Used to express the specific language of the title.",
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
        description="Used to express the reason for or classification of the title.",
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

    classifier: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="classifier",
        title="Code the reason for different URLs, e.g. abstract and full-text",
        description="A characterization of the object expected at the web location.",
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
        return ["id", "extension", "modifierExtension", "classifier", "url"]


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


class CitationStatusDate(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An effective date or period for a status of the citation record.
    The state or status of the citation record paired with an effective date or
    period for that state.
    """

    resource_type = Field("CitationStatusDate", const=True)

    activity: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="activity",
        title="Classification of the status",
        description=(
            "The state or status of the citation record (that will be paired with "
            "the period)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    actual: bool = Field(
        None,
        alias="actual",
        title="Either occurred or expected",
        description=(
            "Whether the status date is actual (has occurred) or expected "
            "(estimated or anticipated)."
        ),
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

    A human-readable display of key concepts to represent the citation.
    """

    resource_type = Field("CitationSummary", const=True)

    style: fhirtypes.CodeableConceptType = Field(
        None,
        alias="style",
        title="Format for display of the citation summary",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    text: fhirtypes.Markdown = Field(
        None,
        alias="text",
        title="The human-readable display of the citation summary",
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
