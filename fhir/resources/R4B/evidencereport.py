from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/EvidenceReport
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class EvidenceReport(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A EvidenceReport.
    The EvidenceReport Resource is a specialized container for a collection of
    resources and codable concepts, adapted to support compositions of
    Evidence, EvidenceVariable, and Citation resources and related concepts.
    """

    __resource_type__ = "EvidenceReport"

    author: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        None,
        alias="author",
        title="Who authored the content",
        description=(
            "An individiual, organization, or device primarily involved in the "
            "creation and maintenance of the content."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    citeAsMarkdown: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="citeAsMarkdown",
        title="Citation for this report",
        description="Citation Resource or display of suggested citation for this report.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e citeAs[x]
            "one_of_many": "citeAs",
            "one_of_many_required": False,
        },
    )
    citeAsMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_citeAsMarkdown", title="Extension field for ``citeAsMarkdown``."
    )

    citeAsReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="citeAsReference",
        title="Citation for this report",
        description="Citation Resource or display of suggested citation for this report.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e citeAs[x]
            "one_of_many": "citeAs",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Citation"],
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

    editor: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        None,
        alias="editor",
        title="Who edited the content",
        description=(
            "An individiual, organization, or device primarily responsible for "
            "internal coherence of the content."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    endorser: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        None,
        alias="endorser",
        title="Who endorsed the content",
        description=(
            "An individiual, organization, or device responsible for officially "
            "endorsing the content for use in some setting."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Unique identifier for the evidence report",
        description=(
            "A formal identifier that is used to identify this EvidenceReport when "
            "it is represented in other formats, or referenced in a specification, "
            "model, design or an instance."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="note",
        title="Used for footnotes and annotations",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    publisher: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the organization or individual that published the evidence"
            " report."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    relatedArtifact: typing.List[fhirtypes.RelatedArtifactType] | None = Field(  # type: ignore
        None,
        alias="relatedArtifact",
        title="Link, description or reference to artifact associated with the report",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    relatedIdentifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="relatedIdentifier",
        title=(
            "Identifiers for articles that may relate to more than one evidence "
            "report"
        ),
        description=(
            "A formal identifier that is used to identify things closely related to"
            " this EvidenceReport."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    relatesTo: typing.List[fhirtypes.EvidenceReportRelatesToType] | None = Field(  # type: ignore
        None,
        alias="relatesTo",
        title="Relationships to other compositions/documents",
        description=(
            "Relationships that this composition has with other compositions or "
            "documents that already exist."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reviewer: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        None,
        alias="reviewer",
        title="Who reviewed the content",
        description=(
            "An individiual, organization, or device primarily responsible for "
            "review of some aspect of the content."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    section: typing.List[fhirtypes.EvidenceReportSectionType] | None = Field(  # type: ignore
        None,
        alias="section",
        title="Composition is broken into sections",
        description="The root of the sections that make up the composition.",
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this summary. Enables tracking the life-cycle of the "
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

    subject: fhirtypes.EvidenceReportSubjectType = Field(  # type: ignore
        ...,
        alias="subject",
        title="Focus of the report",
        description=(
            'Specifies the subject or focus of the report. Answers "What is this '
            'report about?".'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Kind of report",
        description=(
            "Specifies the kind of report, such as grouping of classifiers, search "
            "results, or human-compiled expression."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    url: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="url",
        title=(
            "Canonical identifier for this EvidenceReport, represented as a "
            "globally unique URI"
        ),
        description=(
            "An absolute URI that is used to identify this EvidenceReport when it "
            "is referenced in a specification, model, design or an instance; also "
            "called its canonical identifier. This SHOULD be globally unique and "
            "SHOULD be a literal address at which at which an authoritative "
            "instance of this summary is (or will be) published. This URL can be "
            "the target of a canonical reference. It SHALL remain the same when the"
            " summary is stored on different servers."
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
            "indexing and searching for appropriate evidence report instances."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EvidenceReport`` according specification,
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
            "status",
            "useContext",
            "identifier",
            "relatedIdentifier",
            "citeAsReference",
            "citeAsMarkdown",
            "type",
            "note",
            "relatedArtifact",
            "subject",
            "publisher",
            "contact",
            "author",
            "editor",
            "reviewer",
            "endorser",
            "relatesTo",
            "section",
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
        one_of_many_fields = {"citeAs": ["citeAsMarkdown", "citeAsReference"]}
        return one_of_many_fields


class EvidenceReportRelatesTo(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Relationships to other compositions/documents.
    Relationships that this composition has with other compositions or
    documents that already exist.
    """

    __resource_type__ = "EvidenceReportRelatesTo"

    code: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="code",
        title=(
            "replaces | amends | appends | transforms | replacedWith | amendedWith "
            "| appendedWith | transformedWith"
        ),
        description=(
            "The type of relationship that this composition has with anther "
            "composition or document."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "replaces",
                "amends",
                "appends",
                "transforms",
                "replacedWith",
                "amendedWith",
                "appendedWith",
                "transformedWith",
            ],
        },
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_code", title="Extension field for ``code``."
    )

    targetIdentifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="targetIdentifier",
        title="Target of the relationship",
        description="The target composition/document of this relationship.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e target[x]
            "one_of_many": "target",
            "one_of_many_required": True,
        },
    )

    targetReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="targetReference",
        title="Target of the relationship",
        description="The target composition/document of this relationship.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e target[x]
            "one_of_many": "target",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["EvidenceReport"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EvidenceReportRelatesTo`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "targetIdentifier",
            "targetReference",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("code", "code__ext")]
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
        one_of_many_fields = {"target": ["targetIdentifier", "targetReference"]}
        return one_of_many_fields


class EvidenceReportSection(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Composition is broken into sections.
    The root of the sections that make up the composition.
    """

    __resource_type__ = "EvidenceReportSection"

    author: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="author",
        title="Who and/or what authored the section",
        description=(
            "Identifies who is responsible for the information in this section, not"
            " necessarily who typed it in."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Person", "Device", "Group", "Organization"],
        },
    )

    emptyReason: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="emptyReason",
        title="Why the section is empty",
        description=(
            "If the section is empty, why the list is empty. An empty section "
            "typically has some text explaining the empty reason."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    entryClassifier: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="entryClassifier",
        title="Extensible classifiers as content",
        description="Specifies any type of classification of the evidence report.",
        json_schema_extra={
            "element_property": True,
        },
    )

    entryQuantity: typing.List[fhirtypes.QuantityType] | None = Field(  # type: ignore
        None,
        alias="entryQuantity",
        title="Quantity as content",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    entryReference: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="entryReference",
        title="Reference to resources as content",
        description=(
            "A reference to the actual resource from which the narrative in the "
            "section is derived."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    focus: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="focus",
        title="Classification of section (recommended)",
        description=(
            "A code identifying the kind of content contained within the section. "
            "This should be consistent with the section title."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    focusReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="focusReference",
        title="Classification of section by Resource",
        description=(
            "A definitional Resource identifying the kind of content contained "
            "within the section. This should be consistent with the section title."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    mode: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="mode",
        title="working | snapshot | changes",
        description=(
            "How the entry list was prepared - whether it is a working list that is"
            " suitable for being maintained on an ongoing basis, or if it "
            "represents a snapshot of a list of items from another source, or "
            "whether it is a prepared list where items may be marked as added, "
            "modified or deleted."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["working", "snapshot", "changes"],
        },
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_mode", title="Extension field for ``mode``."
    )

    orderedBy: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="orderedBy",
        title="Order of section entries",
        description="Specifies the order applied to the items in the section entries.",
        json_schema_extra={
            "element_property": True,
        },
    )

    section: typing.List[fhirtypes.EvidenceReportSectionType] | None = Field(  # type: ignore
        None,
        alias="section",
        title="Nested Section",
        description="A nested sub-section within this section.",
        json_schema_extra={
            "element_property": True,
        },
    )

    text: fhirtypes.NarrativeType | None = Field(  # type: ignore
        None,
        alias="text",
        title="Text summary of the section, for human interpretation",
        description=(
            "A human-readable narrative that contains the attested content of the "
            "section, used to represent the content of the resource to a human. The"
            " narrative need not encode all the structured data, but is peferred to"
            " contain sufficient detail to make it acceptable for a human to just "
            "read the narrative."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Label for section (e.g. for ToC)",
        description=(
            "The label for this particular section.  This will be part of the "
            "rendered content for the document, and is often used to build a table "
            "of contents."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EvidenceReportSection`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "title",
            "focus",
            "focusReference",
            "author",
            "text",
            "mode",
            "orderedBy",
            "entryClassifier",
            "entryReference",
            "entryQuantity",
            "emptyReason",
            "section",
        ]


class EvidenceReportSubject(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Focus of the report.
    Specifies the subject or focus of the report. Answers "What is this report
    about?".
    """

    __resource_type__ = "EvidenceReportSubject"

    characteristic: typing.List[fhirtypes.EvidenceReportSubjectCharacteristicType] | None = Field(  # type: ignore
        None,
        alias="characteristic",
        title="Characteristic",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="note",
        title="Footnotes and/or explanatory notes",
        description="Used for general notes and annotations not coded elsewhere.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EvidenceReportSubject`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "characteristic", "note"]


class EvidenceReportSubjectCharacteristic(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Characteristic.
    """

    __resource_type__ = "EvidenceReportSubjectCharacteristic"

    code: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="code",
        title="Characteristic code",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    exclude: bool | None = Field(  # type: ignore
        None,
        alias="exclude",
        title="Is used to express not the characteristic",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    exclude__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_exclude", title="Extension field for ``exclude``."
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="period",
        title="Timeframe for the characteristic",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    valueBoolean: bool | None = Field(  # type: ignore
        None,
        alias="valueBoolean",
        title="Characteristic value",
        description=None,
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

    valueCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="valueCodeableConcept",
        title="Characteristic value",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="valueQuantity",
        title="Characteristic value",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueRange: fhirtypes.RangeType | None = Field(  # type: ignore
        None,
        alias="valueRange",
        title="Characteristic value",
        description=None,
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
        title="Characteristic value",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EvidenceReportSubjectCharacteristic`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "valueReference",
            "valueCodeableConcept",
            "valueBoolean",
            "valueQuantity",
            "valueRange",
            "exclude",
            "period",
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
                "valueBoolean",
                "valueCodeableConcept",
                "valueQuantity",
                "valueRange",
                "valueReference",
            ]
        }
        return one_of_many_fields
