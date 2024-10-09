from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ConceptMap
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ConceptMap(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A map from one set of concepts to one or more other concepts.
    A statement of relationships from one set of concepts to one or more other
    concepts - either concepts in code systems, or data element/data element
    concepts, or classes in class models.
    """

    __resource_type__ = "ConceptMap"

    additionalAttribute: typing.List[fhirtypes.ConceptMapAdditionalAttributeType] | None = Field(  # type: ignore
        None,
        alias="additionalAttribute",
        title=(
            "Definition of an additional attribute to act as a data source or " "target"
        ),
        description=(
            "An additionalAttribute defines an additional data element found in the"
            " source or target data model where the data will come from or be "
            "mapped to. Some mappings are based on data in addition to the source "
            "data element, where codes in multiple fields are combined to a single "
            "field (or vice versa)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    approvalDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="approvalDate",
        title="When the ConceptMap was approved by publisher",
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

    author: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        None,
        alias="author",
        title="Who authored the ConceptMap",
        description=(
            "An individiual or organization primarily involved in the creation and "
            "maintenance of the ConceptMap."
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
            "A copyright statement relating to the concept map and/or its contents."
            " Copyright statements are generally legal restrictions on the use and "
            "publishing of the concept map."
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
            "The date  (and optionally time) when the concept map was last "
            "significantly changed. The date must change when the business version "
            "changes and it must change if the status code changes. In addition, it"
            " should change when the substantive content of the concept map "
            "changes."
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
        title="Natural language description of the concept map",
        description=(
            "A free text natural language description of the concept map from a "
            "consumer's perspective."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    editor: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        None,
        alias="editor",
        title="Who edited the ConceptMap",
        description=(
            "An individual or organization primarily responsible for internal "
            "coherence of the ConceptMap."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    effectivePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="effectivePeriod",
        title="When the ConceptMap is expected to be used",
        description=(
            "The period during which the ConceptMap content was or is planned to be"
            " in active use."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    endorser: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        None,
        alias="endorser",
        title="Who endorsed the ConceptMap",
        description=(
            "An individual or organization asserted by the publisher to be "
            "responsible for officially endorsing the ConceptMap for use in some "
            "setting."
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
            "A Boolean value to indicate that this concept map is authored for "
            "testing purposes (or education/evaluation/marketing) and is not "
            "intended to be used for genuine usage."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    group: typing.List[fhirtypes.ConceptMapGroupType] | None = Field(  # type: ignore
        None,
        alias="group",
        title="Same source and target systems",
        description="A group of mappings that all have the same source and target system.",
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Additional identifier for the concept map",
        description=(
            "A formal identifier that is used to identify this concept map when it "
            "is represented in other formats, or referenced in a specification, "
            "model, design or an instance."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for concept map (if applicable)",
        description=(
            "A legal or geographic region in which the concept map is intended to "
            "be used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    lastReviewDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="lastReviewDate",
        title="When the ConceptMap was last reviewed by the publisher",
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
        title="Name for this concept map (computer friendly)",
        description=(
            "A natural language name identifying the concept map. This name should "
            "be usable as an identifier for the module by machine processing "
            "applications such as code generation."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    property: typing.List[fhirtypes.ConceptMapPropertyType] | None = Field(  # type: ignore
        None,
        alias="property",
        title="Additional properties of the mapping",
        description=(
            "A property defines a slot through which additional information can be "
            "provided about a map from source -> target."
        ),
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
            " and ongoing maintenance of the concept map."
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
        title="Why this concept map is defined",
        description=(
            "Explanation of why this concept map is needed and why it has been "
            "designed as it has."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    relatedArtifact: typing.List[fhirtypes.RelatedArtifactType] | None = Field(  # type: ignore
        None,
        alias="relatedArtifact",
        title="Additional documentation, citations, etc",
        description=(
            "Related artifacts such as additional documentation, justification, "
            "dependencies, bibliographic references, and predecessor and successor "
            "artifacts."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reviewer: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        None,
        alias="reviewer",
        title="Who reviewed the ConceptMap",
        description=(
            "An individual or organization asserted by the publisher to be "
            "primarily responsible for review of some aspect of the ConceptMap."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    sourceScopeCanonical: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="sourceScopeCanonical",
        title="The source value set that contains the concepts that are being mapped",
        description=(
            "Identifier for the source value set that contains the concepts that "
            "are being mapped and provides context for the mappings.  Limits the "
            "scope of the map to source codes (ConceptMap.group.element code or "
            "valueSet) that are members of this value set."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e sourceScope[x]
            "one_of_many": "sourceScope",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ValueSet"],
        },
    )
    sourceScopeCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_sourceScopeCanonical",
        title="Extension field for ``sourceScopeCanonical``.",
    )

    sourceScopeUri: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="sourceScopeUri",
        title="The source value set that contains the concepts that are being mapped",
        description=(
            "Identifier for the source value set that contains the concepts that "
            "are being mapped and provides context for the mappings.  Limits the "
            "scope of the map to source codes (ConceptMap.group.element code or "
            "valueSet) that are members of this value set."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e sourceScope[x]
            "one_of_many": "sourceScope",
            "one_of_many_required": False,
        },
    )
    sourceScopeUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sourceScopeUri", title="Extension field for ``sourceScopeUri``."
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this concept map. Enables tracking the life-cycle of the"
            " content."
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

    targetScopeCanonical: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="targetScopeCanonical",
        title="The target value set which provides context for the mappings",
        description=(
            "Identifier for the target value set that provides important context "
            "about how the mapping choices are made.  Limits the scope of the map "
            "to target codes (ConceptMap.group.element.target code or valueSet) "
            "that are members of this value set."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e targetScope[x]
            "one_of_many": "targetScope",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ValueSet"],
        },
    )
    targetScopeCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_targetScopeCanonical",
        title="Extension field for ``targetScopeCanonical``.",
    )

    targetScopeUri: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="targetScopeUri",
        title="The target value set which provides context for the mappings",
        description=(
            "Identifier for the target value set that provides important context "
            "about how the mapping choices are made.  Limits the scope of the map "
            "to target codes (ConceptMap.group.element.target code or valueSet) "
            "that are members of this value set."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e targetScope[x]
            "one_of_many": "targetScope",
            "one_of_many_required": False,
        },
    )
    targetScopeUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_targetScopeUri", title="Extension field for ``targetScopeUri``."
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Name for this concept map (human friendly)",
        description="A short, descriptive, user-friendly title for the concept map.",
        json_schema_extra={
            "element_property": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    topic: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="topic",
        title="E.g. Education, Treatment, Assessment, etc",
        description=(
            "Descriptions related to the content of the ConceptMap. Topics provide "
            "a high-level categorization as well as keywords for the ConceptMap "
            "that can be useful for filtering and searching."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    url: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="url",
        title=(
            "Canonical identifier for this concept map, represented as a URI "
            "(globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this concept map when it is "
            "referenced in a specification, model, design or an instance; also "
            "called its canonical identifier. This SHOULD be globally unique and "
            "SHOULD be a literal address at which an authoritative instance of this"
            " concept map is (or will be) published. This URL can be the target of "
            "a canonical reference. It SHALL remain the same when the concept map "
            "is stored on different servers."
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
            "indexing and searching for appropriate concept map instances."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="Business version of the concept map",
        description=(
            "The identifier that is used to identify this version of the concept "
            "map when it is referenced in a specification, model, design or "
            "instance. This is an arbitrary value managed by the concept map author"
            " and is not expected to be globally unique. For example, it might be a"
            " timestamp (e.g. yyyymmdd) if a managed version is not available. "
            "There is also no expectation that versions can be placed in a "
            "lexicographical sequence."
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
            "Indicates the mechanism used to compare versions to determine which "
            "ConceptMap is more current."
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
            "Indicates the mechanism used to compare versions to determine which "
            "ConceptMap is more current."
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
        ``ConceptMap`` according specification,
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
            "topic",
            "author",
            "editor",
            "reviewer",
            "endorser",
            "relatedArtifact",
            "property",
            "additionalAttribute",
            "sourceScopeUri",
            "sourceScopeCanonical",
            "targetScopeUri",
            "targetScopeCanonical",
            "group",
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
            "sourceScope": ["sourceScopeCanonical", "sourceScopeUri"],
            "targetScope": ["targetScopeCanonical", "targetScopeUri"],
            "versionAlgorithm": ["versionAlgorithmCoding", "versionAlgorithmString"],
        }
        return one_of_many_fields


class ConceptMapAdditionalAttribute(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Definition of an additional attribute to act as a data source or target.
    An additionalAttribute defines an additional data element found in the
    source or target data model where the data will come from or be mapped to.
    Some mappings are based on data in addition to the source data element,
    where codes in multiple fields are combined to a single field (or vice
    versa).
    """

    __resource_type__ = "ConceptMapAdditionalAttribute"

    code: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Identifies this additional attribute through this resource",
        description=(
            "A code that is used to identify this additional data attribute. The "
            "code is used internally in "
            "ConceptMap.group.element.target.dependsOn.attribute and "
            "ConceptMap.group.element.target.product.attribute."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_code", title="Extension field for ``code``."
    )

    description: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="description",
        title=(
            "Why the additional attribute is defined, and/or what the data element "
            "it refers to is"
        ),
        description=(
            "A description of the additional attribute and/or the data element it "
            "refers to - why it is defined, and how the value might be used in "
            "mappings, and a discussion of issues associated with the use of the "
            "data element."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="code | Coding | string | boolean | Quantity",
        description=(
            "The type of the source data contained in this concept map for this "
            "data element."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["code", "Coding", "string", "boolean", "Quantity"],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    uri: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="uri",
        title="Formal identifier for the data element referred to in this attribte",
        description=(
            "Reference to the formal definition of the source/target data element. "
            "For elements defined by the FHIR specification, or using a FHIR "
            "logical model, the correct format is {canonical-url}#{element-id}."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_uri", title="Extension field for ``uri``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ConceptMapAdditionalAttribute`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "uri",
            "description",
            "type",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("code", "code__ext"), ("type", "type__ext")]
        return required_fields


class ConceptMapGroup(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Same source and target systems.
    A group of mappings that all have the same source and target system.
    """

    __resource_type__ = "ConceptMapGroup"

    element: typing.List[fhirtypes.ConceptMapGroupElementType] = Field(  # type: ignore
        ...,
        alias="element",
        title="Mappings for a concept from the source set",
        description=(
            "Mappings for an individual concept in the source to one or more "
            "concepts in the target."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    source: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="source",
        title="Source system where concepts to be mapped are defined",
        description=(
            "An absolute URI that identifies the source system where the concepts "
            "to be mapped are defined."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["CodeSystem"],
        },
    )
    source__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_source", title="Extension field for ``source``."
    )

    target: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="target",
        title="Target system that the concepts are to be mapped to",
        description=(
            "An absolute URI that identifies the target system that the concepts "
            "will be mapped to."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["CodeSystem"],
        },
    )
    target__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_target", title="Extension field for ``target``."
    )

    unmapped: fhirtypes.ConceptMapGroupUnmappedType | None = Field(  # type: ignore
        None,
        alias="unmapped",
        title=(
            "What to do when there is no mapping target for the source concept and "
            "ConceptMap.group.element.noMap is not true"
        ),
        description=(
            "What to do when there is no mapping to a target concept from the "
            "source concept and ConceptMap.group.element.noMap is not true. This "
            'provides the "default" to be applied when there is no target concept '
            "mapping specified or the expansion of "
            "ConceptMap.group.element.target.valueSet is empty."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ConceptMapGroup`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "source",
            "target",
            "element",
            "unmapped",
        ]


class ConceptMapGroupElement(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Mappings for a concept from the source set.
    Mappings for an individual concept in the source to one or more concepts in
    the target.
    """

    __resource_type__ = "ConceptMapGroupElement"

    code: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Identifies element being mapped",
        description="Identity (code or path) or the element/item being mapped.",
        json_schema_extra={
            "element_property": True,
        },
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_code", title="Extension field for ``code``."
    )

    display: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="display",
        title="Display for the code",
        description=(
            "The display for the code. The display is only provided to help editors"
            " when editing the concept map."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_display", title="Extension field for ``display``."
    )

    noMap: bool | None = Field(  # type: ignore
        None,
        alias="noMap",
        title="No mapping to a target concept for this source concept",
        description=(
            "If noMap = true this indicates that no mapping to a target concept "
            "exists for this source concept."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    noMap__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_noMap", title="Extension field for ``noMap``."
    )

    target: typing.List[fhirtypes.ConceptMapGroupElementTargetType] | None = Field(  # type: ignore
        None,
        alias="target",
        title="Concept in target system for element",
        description="A concept from the target value set that this concept maps to.",
        json_schema_extra={
            "element_property": True,
        },
    )

    valueSet: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="valueSet",
        title="Identifies the set of concepts being mapped",
        description=(
            "The set of concepts from the ConceptMap.group.source code system which"
            " are all being mapped to the target as part of this mapping rule."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ValueSet"],
        },
    )
    valueSet__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueSet", title="Extension field for ``valueSet``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ConceptMapGroupElement`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "display",
            "valueSet",
            "noMap",
            "target",
        ]


class ConceptMapGroupElementTarget(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Concept in target system for element.
    A concept from the target value set that this concept maps to.
    """

    __resource_type__ = "ConceptMapGroupElementTarget"

    code: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Code that identifies the target element",
        description="Identity (code or path) or the element/item that the map refers to.",
        json_schema_extra={
            "element_property": True,
        },
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_code", title="Extension field for ``code``."
    )

    comment: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="comment",
        title="Description of status/issues in mapping",
        description=(
            "A description of status/issues in mapping that conveys additional "
            "information not represented in  the structured data."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_comment", title="Extension field for ``comment``."
    )

    dependsOn: typing.List[fhirtypes.ConceptMapGroupElementTargetDependsOnType] | None = Field(  # type: ignore
        None,
        alias="dependsOn",
        title="Other properties required for this mapping",
        description=(
            "A set of additional dependencies for this mapping to hold. This "
            "mapping is only applicable if the specified data attribute can be "
            "resolved, and it has the specified value."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    display: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="display",
        title="Display for the code",
        description=(
            "The display for the code. The display is only provided to help editors"
            " when editing the concept map."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_display", title="Extension field for ``display``."
    )

    product: typing.List[fhirtypes.ConceptMapGroupElementTargetDependsOnType] | None = Field(  # type: ignore
        None,
        alias="product",
        title="Other data elements that this mapping also produces",
        description=(
            "Product is the output of a ConceptMap that provides additional values "
            "that go in other attributes / data elemnts of the target data."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    property: typing.List[fhirtypes.ConceptMapGroupElementTargetPropertyType] | None = Field(  # type: ignore
        None,
        alias="property",
        title="Property value for the source -> target mapping",
        description="A property value for this source -> target mapping.",
        json_schema_extra={
            "element_property": True,
        },
    )

    relationship: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="relationship",
        title=(
            "related-to | equivalent | source-is-narrower-than-target | source-is-"
            "broader-than-target | not-related-to"
        ),
        description=(
            "The relationship between the source and target concepts. The "
            "relationship is read from source to target (e.g. source-is-narrower-"
            "than-target)."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "related-to",
                "equivalent",
                "source-is-narrower-than-target",
                "source-is-broader-than-target",
                "not-related-to",
            ],
        },
    )
    relationship__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_relationship", title="Extension field for ``relationship``."
    )

    valueSet: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="valueSet",
        title="Identifies the set of target concepts",
        description=(
            "The set of concepts from the ConceptMap.group.target code system which"
            " are all being mapped to as part of this mapping rule. The effect of "
            "using this data element is the same as having multiple "
            "ConceptMap.group.element.target elements with one for each concept in "
            "the ConceptMap.group.element.target.valueSet value set."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ValueSet"],
        },
    )
    valueSet__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueSet", title="Extension field for ``valueSet``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ConceptMapGroupElementTarget`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "display",
            "valueSet",
            "relationship",
            "comment",
            "property",
            "dependsOn",
            "product",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("relationship", "relationship__ext")]
        return required_fields


class ConceptMapGroupElementTargetDependsOn(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Other properties required for this mapping.
    A set of additional dependencies for this mapping to hold. This mapping is
    only applicable if the specified data attribute can be resolved, and it has
    the specified value.
    """

    __resource_type__ = "ConceptMapGroupElementTargetDependsOn"

    attribute: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="attribute",
        title=(
            "A reference to a mapping attribute defined in "
            "ConceptMap.additionalAttribute"
        ),
        description=(
            "A reference to the additional attribute that holds a value the map "
            "depends on."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    attribute__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_attribute", title="Extension field for ``attribute``."
    )

    valueBoolean: bool | None = Field(  # type: ignore
        None,
        alias="valueBoolean",
        title="Value of the referenced data element",
        description="Data element value that the map depends on / produces.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCode: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="valueCode",
        title="Value of the referenced data element",
        description="Data element value that the map depends on / produces.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueCode__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueCode", title="Extension field for ``valueCode``."
    )

    valueCoding: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="valueCoding",
        title="Value of the referenced data element",
        description="Data element value that the map depends on / produces.",
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
        title="Value of the referenced data element",
        description="Data element value that the map depends on / produces.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueSet: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="valueSet",
        title="The mapping depends on a data element with a value from this value set",
        description=(
            "This mapping applies if the data element value is a code from this "
            "value set."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ValueSet"],
        },
    )
    valueSet__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueSet", title="Extension field for ``valueSet``."
    )

    valueString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="valueString",
        title="Value of the referenced data element",
        description="Data element value that the map depends on / produces.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ConceptMapGroupElementTargetDependsOn`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "attribute",
            "valueCode",
            "valueCoding",
            "valueString",
            "valueBoolean",
            "valueQuantity",
            "valueSet",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("attribute", "attribute__ext")]
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
            "value": [
                "valueBoolean",
                "valueCode",
                "valueCoding",
                "valueQuantity",
                "valueString",
            ]
        }
        return one_of_many_fields


class ConceptMapGroupElementTargetProperty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Property value for the source -> target mapping.
    A property value for this source -> target mapping.
    """

    __resource_type__ = "ConceptMapGroupElementTargetProperty"

    code: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Reference to ConceptMap.property.code",
        description="A reference to a mapping property defined in ConceptMap.property.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_code", title="Extension field for ``code``."
    )

    valueBoolean: bool | None = Field(  # type: ignore
        None,
        alias="valueBoolean",
        title="Value of the property for this concept",
        description=(
            "The value of this property. If the type chosen for this element is "
            "'code', then the property SHALL be defined in a ConceptMap.property "
            "element."
        ),
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

    valueCode: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="valueCode",
        title="Value of the property for this concept",
        description=(
            "The value of this property. If the type chosen for this element is "
            "'code', then the property SHALL be defined in a ConceptMap.property "
            "element."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueCode__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueCode", title="Extension field for ``valueCode``."
    )

    valueCoding: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="valueCoding",
        title="Value of the property for this concept",
        description=(
            "The value of this property. If the type chosen for this element is "
            "'code', then the property SHALL be defined in a ConceptMap.property "
            "element."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="valueDateTime",
        title="Value of the property for this concept",
        description=(
            "The value of this property. If the type chosen for this element is "
            "'code', then the property SHALL be defined in a ConceptMap.property "
            "element."
        ),
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
        title="Value of the property for this concept",
        description=(
            "The value of this property. If the type chosen for this element is "
            "'code', then the property SHALL be defined in a ConceptMap.property "
            "element."
        ),
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
        title="Value of the property for this concept",
        description=(
            "The value of this property. If the type chosen for this element is "
            "'code', then the property SHALL be defined in a ConceptMap.property "
            "element."
        ),
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
        title="Value of the property for this concept",
        description=(
            "The value of this property. If the type chosen for this element is "
            "'code', then the property SHALL be defined in a ConceptMap.property "
            "element."
        ),
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

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ConceptMapGroupElementTargetProperty`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "valueCoding",
            "valueString",
            "valueInteger",
            "valueBoolean",
            "valueDateTime",
            "valueDecimal",
            "valueCode",
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
        one_of_many_fields = {
            "value": [
                "valueBoolean",
                "valueCode",
                "valueCoding",
                "valueDateTime",
                "valueDecimal",
                "valueInteger",
                "valueString",
            ]
        }
        return one_of_many_fields


class ConceptMapGroupUnmapped(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What to do when there is no mapping target for the source concept and
    ConceptMap.group.element.noMap is not true.
    What to do when there is no mapping to a target concept from the source
    concept and ConceptMap.group.element.noMap is not true. This provides the
    "default" to be applied when there is no target concept mapping specified
    or the expansion of ConceptMap.group.element.target.valueSet is empty.
    """

    __resource_type__ = "ConceptMapGroupUnmapped"

    code: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Fixed code when mode = fixed",
        description=(
            "The fixed code to use when the mode = 'fixed'  - all unmapped codes "
            "are mapped to a single fixed code."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_code", title="Extension field for ``code``."
    )

    display: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="display",
        title="Display for the code",
        description=(
            "The display for the code. The display is only provided to help editors"
            " when editing the concept map."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_display", title="Extension field for ``display``."
    )

    mode: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="mode",
        title="use-source-code | fixed | other-map",
        description=(
            "Defines which action to take if there is no match for the source "
            "concept in the target system designated for the group. One of 3 "
            "actions are possible: use the unmapped source code (this is useful "
            "when doing a mapping between versions, and only a few codes have "
            "changed), use a fixed code (a default code), or alternatively, a "
            "reference to a different concept map can be provided (by canonical "
            "URL)."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["use-source-code", "fixed", "other-map"],
        },
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_mode", title="Extension field for ``mode``."
    )

    otherMap: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="otherMap",
        title=(
            "canonical reference to an additional ConceptMap to use for mapping if "
            "the source concept is unmapped"
        ),
        description=(
            "The canonical reference to an additional ConceptMap resource instance "
            "to use for mapping if this ConceptMap resource contains no matching "
            "mapping for the source concept."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ConceptMap"],
        },
    )
    otherMap__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_otherMap", title="Extension field for ``otherMap``."
    )

    relationship: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="relationship",
        title=(
            "related-to | equivalent | source-is-narrower-than-target | source-is-"
            "broader-than-target | not-related-to"
        ),
        description=(
            "The default relationship value to apply between the source and target "
            "concepts when the source code is unmapped and the mode is 'fixed' or "
            "'use-source-code'."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "related-to",
                "equivalent",
                "source-is-narrower-than-target",
                "source-is-broader-than-target",
                "not-related-to",
            ],
        },
    )
    relationship__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_relationship", title="Extension field for ``relationship``."
    )

    valueSet: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="valueSet",
        title="Fixed code set when mode = fixed",
        description=(
            "The set of fixed codes to use when the mode = 'fixed'  - all unmapped "
            "codes are mapped to each of the fixed codes."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ValueSet"],
        },
    )
    valueSet__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueSet", title="Extension field for ``valueSet``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ConceptMapGroupUnmapped`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "mode",
            "code",
            "display",
            "valueSet",
            "relationship",
            "otherMap",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("mode", "mode__ext")]
        return required_fields


class ConceptMapProperty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional properties of the mapping.
    A property defines a slot through which additional information can be
    provided about a map from source -> target.
    """

    __resource_type__ = "ConceptMapProperty"

    code: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="code",
        title=(
            "Identifies the property on the mappings, and when referred to in the "
            "$translate operation"
        ),
        description=(
            "A code that is used to identify the property. The code is used "
            "internally (in ConceptMap.group.element.target.property.code) and also"
            " in the $translate operation."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_code", title="Extension field for ``code``."
    )

    description: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Why the property is defined, and/or what it conveys",
        description=(
            "A description of the property - why it is defined, and how its value "
            "might be used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    system: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="system",
        title="The CodeSystem from which code values come",
        description=(
            "The CodeSystem that defines the codes from which values of type "
            "```code``` in property values."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["CodeSystem"],
        },
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_system", title="Extension field for ``system``."
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Coding | string | integer | boolean | dateTime | decimal | code",
        description="The type of the property value.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "Coding",
                "string",
                "integer",
                "boolean",
                "dateTime",
                "decimal",
                "code",
            ],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    uri: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="uri",
        title="Formal identifier for the property",
        description="Reference to the formal meaning of the property.",
        json_schema_extra={
            "element_property": True,
        },
    )
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_uri", title="Extension field for ``uri``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ConceptMapProperty`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "uri",
            "description",
            "type",
            "system",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("code", "code__ext"), ("type", "type__ext")]
        return required_fields
