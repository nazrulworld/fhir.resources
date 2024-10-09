from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ConceptMap
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
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
    concepts - either code systems or data elements, or classes in class
    models.
    """

    __resource_type__ = "ConceptMap"

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

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="date",
        title="Date this was last changed",
        description=(
            "The date  (and optionally time) when the concept map was published. "
            "The date must change if and when the business version changes and it "
            "must change if the status code changes. In addition, it should change "
            "when the substantive content of the concept map changes."
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

    experimental: bool | None = Field(  # type: ignore
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A boolean value to indicate that this concept map is authored for "
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

    group: typing.List[fhirtypes.ConceptMapGroupType] | None = Field(  # type: ignore
        None,
        alias="group",
        title="Same source and target systems",
        description="A group of mappings that all have the same source and target system.",
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
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

    publisher: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the individual or organization that published the concept "
            "map."
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
            "Explaination of why this concept map is needed and why it has been "
            "designed as it has."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    sourceReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="sourceReference",
        title="Identifies the source of the concepts which are being mapped",
        description=(
            "The source value set that specifies the concepts that are being " "mapped."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e source[x]
            "one_of_many": "source",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ValueSet"],
        },
    )

    sourceUri: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="sourceUri",
        title="Identifies the source of the concepts which are being mapped",
        description=(
            "The source value set that specifies the concepts that are being " "mapped."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e source[x]
            "one_of_many": "source",
            "one_of_many_required": False,
        },
    )
    sourceUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sourceUri", title="Extension field for ``sourceUri``."
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

    targetReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="targetReference",
        title="Provides context to the mappings",
        description=(
            "The target value set provides context to the mappings. Note that the "
            "mapping is made between concepts, not between value sets, but the "
            "value set provides important context about how the concept mapping "
            "choices are made."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e target[x]
            "one_of_many": "target",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ValueSet"],
        },
    )

    targetUri: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="targetUri",
        title="Provides context to the mappings",
        description=(
            "The target value set provides context to the mappings. Note that the "
            "mapping is made between concepts, not between value sets, but the "
            "value set provides important context about how the concept mapping "
            "choices are made."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e target[x]
            "one_of_many": "target",
            "one_of_many_required": False,
        },
    )
    targetUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_targetUri", title="Extension field for ``targetUri``."
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

    url: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="url",
        title="Logical URI to reference this concept map (globally unique)",
        description=(
            "An absolute URI that is used to identify this concept map when it is "
            "referenced in a specification, model, design or an instance. This "
            "SHALL be a URL, SHOULD be globally unique, and SHOULD be an address at"
            " which this concept map is (or will be) published. The URL SHOULD "
            "include the major version of the concept map. For more information see"
            " [Technical and Business Versions](resource.html#versions)."
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
            "sourceUri",
            "sourceReference",
            "targetUri",
            "targetReference",
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
            "source": ["sourceReference", "sourceUri"],
            "target": ["targetReference", "targetUri"],
        }
        return one_of_many_fields


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

    source: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="source",
        title="Code System (if value set crosses code systems)",
        description=(
            "An absolute URI that identifies the Code System (if the source is a "
            "value set that crosses more than one code system)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    source__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_source", title="Extension field for ``source``."
    )

    sourceVersion: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="sourceVersion",
        title="Specific version of the  code system",
        description=(
            "The specific version of the code system, as determined by the code "
            "system authority."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    sourceVersion__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sourceVersion", title="Extension field for ``sourceVersion``."
    )

    target: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="target",
        title="System of the target (if necessary)",
        description=(
            "An absolute URI that identifies the code system of the target code (if"
            " the target is a value set that cross code systems)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    target__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_target", title="Extension field for ``target``."
    )

    targetVersion: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="targetVersion",
        title="Specific version of the  code system",
        description=(
            "The specific version of the code system, as determined by the code "
            "system authority."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    targetVersion__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_targetVersion", title="Extension field for ``targetVersion``."
    )

    unmapped: fhirtypes.ConceptMapGroupUnmappedType | None = Field(  # type: ignore
        None,
        alias="unmapped",
        title="When no match in the mappings",
        description="What to do when there is no match in the mappings in the group.",
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
            "sourceVersion",
            "target",
            "targetVersion",
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

    target: typing.List[fhirtypes.ConceptMapGroupElementTargetType] | None = Field(  # type: ignore
        None,
        alias="target",
        title="Concept in target system for element",
        description="A concept from the target value set that this concept maps to.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ConceptMapGroupElement`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "display", "target"]


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
        title="Other elements required for this mapping (from context)",
        description=(
            "A set of additional dependencies for this mapping to hold. This "
            "mapping is only applicable if the specified element can be resolved, "
            "and it has the specified value."
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

    equivalence: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="equivalence",
        title=(
            "relatedto | equivalent | equal | wider | subsumes | narrower | "
            "specializes | inexact | unmatched | disjoint"
        ),
        description=(
            "The equivalence between the source and target concepts (counting for "
            "the dependencies and products). The equivalence is read from target to"
            " source (e.g. the target is 'wider' than the source)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "relatedto",
                "equivalent",
                "equal",
                "wider",
                "subsumes",
                "narrower",
                "specializes",
                "inexact",
                "unmatched",
                "disjoint",
            ],
        },
    )
    equivalence__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_equivalence", title="Extension field for ``equivalence``."
    )

    product: typing.List[fhirtypes.ConceptMapGroupElementTargetDependsOnType] | None = Field(  # type: ignore
        None,
        alias="product",
        title="Other concepts that this mapping also produces",
        description=(
            "A set of additional outcomes from this mapping to other elements. To "
            "properly execute this mapping, the specified element must be mapped to"
            " some data element or source that is in context. The mapping may still"
            " be useful without a place for the additional data elements, but the "
            "equivalence cannot be relied on."
        ),
        json_schema_extra={
            "element_property": True,
        },
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
            "equivalence",
            "comment",
            "dependsOn",
            "product",
        ]


class ConceptMapGroupElementTargetDependsOn(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Other elements required for this mapping (from context).
    A set of additional dependencies for this mapping to hold. This mapping is
    only applicable if the specified element can be resolved, and it has the
    specified value.
    """

    __resource_type__ = "ConceptMapGroupElementTargetDependsOn"

    code: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Value of the referenced element",
        description=(
            "Identity (code or path) or the element/item/ValueSet that the map "
            "depends on / refers to."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
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

    property: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="property",
        title="Reference to property mapping depends on",
        description=(
            "A reference to an element that holds a coded value that corresponds to"
            " a code system property. The idea is that the information model "
            "carries an element somwhere that is labeled to correspond with a code "
            "system property."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    property__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_property", title="Extension field for ``property``."
    )

    system: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="system",
        title="Code System (if necessary)",
        description=(
            "An absolute URI that identifies the code system of the dependency code"
            " (if the source/dependency is a value set that crosses code systems)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_system", title="Extension field for ``system``."
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
            "property",
            "system",
            "code",
            "display",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("code", "code__ext"), ("property", "property__ext")]
        return required_fields


class ConceptMapGroupUnmapped(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    When no match in the mappings.
    What to do when there is no match in the mappings in the group.
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
        title="provided | fixed | other-map",
        description=(
            "Defines which action to take if there is no match in the group. One of"
            " 3 actions is possible: use the unmapped code (this is useful when "
            "doing a mapping between versions, and only a few codes have changed), "
            "use a fixed code (a default code), or alternatively, a reference to a "
            "different concept map can be provided (by canonical URL)."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["provided", "fixed", "other-map"],
        },
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_mode", title="Extension field for ``mode``."
    )

    url: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="url",
        title="Canonical URL for other concept map",
        description="The canonical URL of the map to use if this map contains no mapping.",
        json_schema_extra={
            "element_property": True,
        },
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_url", title="Extension field for ``url``."
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
            "url",
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
