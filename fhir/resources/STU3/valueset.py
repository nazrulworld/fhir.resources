from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ValueSet
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ValueSet(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A set of codes drawn from one or more code systems.
    A value set specifies a set of codes drawn from one or more code systems.
    """

    __resource_type__ = "ValueSet"

    compose: fhirtypes.ValueSetComposeType | None = Field(  # type: ignore
        None,
        alias="compose",
        title="Definition of the content of the value set (CLD)",
        description=(
            "A set of criteria that define the content logical definition of the "
            "value set by including or excluding codes from outside this value set."
            ' This I also known as the "Content Logical Definition" (CLD).'
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
            "A copyright statement relating to the value set and/or its contents. "
            "Copyright statements are generally legal restrictions on the use and "
            "publishing of the value set."
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
            "The date  (and optionally time) when the value set was published. The "
            "date must change if and when the business version changes and it must "
            "change if the status code changes. In addition, it should change when "
            "the substantive content of the value set changes. (e.g. the 'content "
            "logical definition')."
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
        title="Natural language description of the value set",
        description=(
            "A free text natural language description of the value set from a "
            "consumer's perspective."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    expansion: fhirtypes.ValueSetExpansionType | None = Field(  # type: ignore
        None,
        alias="expansion",
        title='Used when the value set is "expanded"',
        description=(
            'A value set can also be "expanded", where the value set is turned into'
            " a simple collection of enumerated codes. This element holds the "
            "expansion, if it has been performed."
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
            "A boolean value to indicate that this value set is authored for "
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

    extensible: bool | None = Field(  # type: ignore
        None,
        alias="extensible",
        title="Whether this is intended to be used with an extensible binding",
        description="Whether this is intended to be used with an extensible binding or not.",
        json_schema_extra={
            "element_property": True,
        },
    )
    extensible__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_extensible", title="Extension field for ``extensible``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Additional identifier for the value set",
        description=(
            "A formal identifier that is used to identify this value set when it is"
            " represented in other formats, or referenced in a specification, "
            "model, design or an instance."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    immutable: bool | None = Field(  # type: ignore
        None,
        alias="immutable",
        title=(
            "Indicates whether or not any change to the content logical definition "
            "may occur"
        ),
        description=(
            "If this is set to 'true', then no new versions of the content logical "
            "definition can be created.  Note: Other metadata might still change."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    immutable__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_immutable", title="Extension field for ``immutable``."
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for value set (if applicable)",
        description=(
            "A legal or geographic region in which the value set is intended to be "
            "used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name for this value set (computer friendly)",
        description=(
            "A natural language name identifying the value set. This name should be"
            " usable as an identifier for the module by machine processing "
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
            "The name of the individual or organization that published the value "
            "set."
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
        title="Why this value set is defined",
        description=(
            "Explaination of why this value set is needed and why it has been "
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
            "The status of this value set. Enables tracking the life-cycle of the "
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

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Name for this value set (human friendly)",
        description="A short, descriptive, user-friendly title for the value set.",
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
        title="Logical URI to reference this value set (globally unique)",
        description=(
            "An absolute URI that is used to identify this value set when it is "
            "referenced in a specification, model, design or an instance. This "
            "SHALL be a URL, SHOULD be globally unique, and SHOULD be an address at"
            " which this value set is (or will be) published. The URL SHOULD "
            "include the major version of the value set. For more information see "
            "[Technical and Business Versions](resource.html#versions)."
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
            "indexing and searching for appropriate value set instances."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="Business version of the value set",
        description=(
            "The identifier that is used to identify this version of the value set "
            "when it is referenced in a specification, model, design or instance. "
            "This is an arbitrary value managed by the value set author and is not "
            "expected to be globally unique. For example, it might be a timestamp "
            "(e.g. yyyymmdd) if a managed version is not available. There is also "
            "no expectation that versions can be placed in a lexicographical "
            "sequence."
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
        ``ValueSet`` according specification,
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
            "immutable",
            "purpose",
            "copyright",
            "extensible",
            "compose",
            "expansion",
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


class ValueSetCompose(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Definition of the content of the value set (CLD).
    A set of criteria that define the content logical definition of the value
    set by including or excluding codes from outside this value set. This I
    also known as the "Content Logical Definition" (CLD).
    """

    __resource_type__ = "ValueSetCompose"

    exclude: typing.List[fhirtypes.ValueSetComposeIncludeType] | None = Field(  # type: ignore
        None,
        alias="exclude",
        title="Explicitly exclude codes from a code system or other value sets",
        description=(
            "Exclude one or more codes from the value set based on code system "
            "filters and/or other value sets."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    inactive: bool | None = Field(  # type: ignore
        None,
        alias="inactive",
        title="Whether inactive codes are in the value set",
        description=(
            "Whether inactive codes - codes that are not approved for current use -"
            " are in the value set. If inactive = true, inactive codes are to be "
            "included in the expansion, if inactive = false, the inactive codes "
            "will not be included in the expansion. If absent, the behavior is "
            "determined by the implementation, or by the applicable "
            "ExpansionProfile (but generally, inactive codes would be expected to "
            "be included)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    inactive__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_inactive", title="Extension field for ``inactive``."
    )

    include: typing.List[fhirtypes.ValueSetComposeIncludeType] = Field(  # type: ignore
        ...,
        alias="include",
        title="Include one or more codes from a code system or other value set(s)",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    lockedDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="lockedDate",
        title="Fixed date for version-less references (transitive)",
        description=(
            "If a locked date is defined, then the Content Logical Definition must "
            "be evaluated using the current version as of the locked date for "
            "referenced code system(s) and value set instances where "
            "ValueSet.compose.include.version is not defined."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    lockedDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_lockedDate", title="Extension field for ``lockedDate``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ValueSetCompose`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "lockedDate",
            "inactive",
            "include",
            "exclude",
        ]


class ValueSetComposeInclude(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Include one or more codes from a code system or other value set(s).
    """

    __resource_type__ = "ValueSetComposeInclude"

    concept: typing.List[fhirtypes.ValueSetComposeIncludeConceptType] | None = Field(  # type: ignore
        None,
        alias="concept",
        title="A concept defined in the system",
        description="Specifies a concept to be included or excluded.",
        json_schema_extra={
            "element_property": True,
        },
    )

    filter: typing.List[fhirtypes.ValueSetComposeIncludeFilterType] | None = Field(  # type: ignore
        None,
        alias="filter",
        title="Select codes/concepts by their properties (including relationships)",
        description=(
            "Select concepts by specify a matching criteria based on the properties"
            " (including relationships) defined by the system. If multiple filters "
            "are specified, they SHALL all be true."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    system: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="system",
        title="The system the codes come from",
        description=(
            "An absolute URI which is the code system from which the selected codes"
            " come from."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_system", title="Extension field for ``system``."
    )

    valueSet: typing.List[fhirtypes.UriType | None] | None = Field(  # type: ignore
        None,
        alias="valueSet",
        title="Select only contents included in this value set",
        description=(
            "Selects concepts found in this value set. This is an absolute URI that"
            " is a reference to ValueSet.url."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    valueSet__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_valueSet", title="Extension field for ``valueSet``."
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="Specific version of the code system referred to",
        description="The version of the code system that the codes are selected from.",
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
        ``ValueSetComposeInclude`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "system",
            "version",
            "concept",
            "filter",
            "valueSet",
        ]


class ValueSetComposeIncludeConcept(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A concept defined in the system.
    Specifies a concept to be included or excluded.
    """

    __resource_type__ = "ValueSetComposeIncludeConcept"

    code: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Code or expression from system",
        description="Specifies a code for the concept to be included or excluded.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_code", title="Extension field for ``code``."
    )

    designation: typing.List[fhirtypes.ValueSetComposeIncludeConceptDesignationType] | None = Field(  # type: ignore
        None,
        alias="designation",
        title="Additional representations for this concept",
        description=(
            "Additional representations for this concept when used in this value "
            "set - other languages, aliases, specialized purposes, used for "
            "particular purposes, etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    display: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="display",
        title="Text to display for this code for this value set in this valueset",
        description=(
            "The text to display to the user for this concept in the context of "
            "this valueset. If no display is provided, then applications using the "
            "value set use the display specified for the code by the system."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_display", title="Extension field for ``display``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ValueSetComposeIncludeConcept`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "display",
            "designation",
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


class ValueSetComposeIncludeConceptDesignation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional representations for this concept.
    Additional representations for this concept when used in this value set -
    other languages, aliases, specialized purposes, used for particular
    purposes, etc.
    """

    __resource_type__ = "ValueSetComposeIncludeConceptDesignation"

    language: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="language",
        title="Human language of the designation",
        description="The language this designation is defined for.",
        json_schema_extra={
            "element_property": True,
        },
    )
    language__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_language", title="Extension field for ``language``."
    )

    use: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="use",
        title="Details how this designation would be used",
        description="A code that details how this designation would be used.",
        json_schema_extra={
            "element_property": True,
        },
    )

    value: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="value",
        title="The text value for this designation",
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ValueSetComposeIncludeConceptDesignation`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "language", "use", "value"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("value", "value__ext")]
        return required_fields


class ValueSetComposeIncludeFilter(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Select codes/concepts by their properties (including relationships).
    Select concepts by specify a matching criteria based on the properties
    (including relationships) defined by the system. If multiple filters are
    specified, they SHALL all be true.
    """

    __resource_type__ = "ValueSetComposeIncludeFilter"

    op: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="op",
        title=(
            "= | is-a | descendent-of | is-not-a | regex | in | not-in | "
            "generalizes | exists"
        ),
        description="The kind of operation to perform as a part of the filter criteria.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "=",
                "is-a",
                "descendent-of",
                "is-not-a",
                "regex",
                "in",
                "not-in",
                "generalizes",
                "exists",
            ],
        },
    )
    op__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_op", title="Extension field for ``op``."
    )

    property: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="property",
        title="A property defined by the code system",
        description="A code that identifies a property defined in the code system.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    property__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_property", title="Extension field for ``property``."
    )

    value: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="value",
        title="Code from the system, or regex criteria, or boolean value for exists",
        description=(
            "The match value may be either a code defined by the system, or a "
            "string value, which is a regex match on the literal string of the "
            "property value when the operation is 'regex', or one of the values "
            "(true and false), when the operation is 'exists'."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ValueSetComposeIncludeFilter`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "property", "op", "value"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("op", "op__ext"),
            ("property", "property__ext"),
            ("value", "value__ext"),
        ]
        return required_fields


class ValueSetExpansion(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Used when the value set is "expanded".
    A value set can also be "expanded", where the value set is turned into a
    simple collection of enumerated codes. This element holds the expansion, if
    it has been performed.
    """

    __resource_type__ = "ValueSetExpansion"

    contains: typing.List[fhirtypes.ValueSetExpansionContainsType] | None = Field(  # type: ignore
        None,
        alias="contains",
        title="Codes in the value set",
        description="The codes that are contained in the value set expansion.",
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Uniquely identifies this expansion",
        description=(
            "An identifier that uniquely identifies this expansion of the valueset."
            " Systems may re-use the same identifier as long as the expansion and "
            "the definition remain the same, but are not required to do so."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    identifier__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_identifier", title="Extension field for ``identifier``."
    )

    offset: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="offset",
        title="Offset at which this resource starts",
        description=(
            "If paging is being used, the offset at which this resource starts.  "
            "I.e. this resource is a partial view into the expansion. If paging is "
            "not being used, this element SHALL not be present."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    offset__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_offset", title="Extension field for ``offset``."
    )

    parameter: typing.List[fhirtypes.ValueSetExpansionParameterType] | None = Field(  # type: ignore
        None,
        alias="parameter",
        title="Parameter that controlled the expansion process",
        description=(
            "A parameter that controlled the expansion process. These parameters "
            "may be used by users of expanded value sets to check whether the "
            "expansion is suitable for a particular purpose, or to pick the correct"
            " expansion."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    timestamp: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="timestamp",
        title="Time ValueSet expansion happened",
        description="The time at which the expansion was produced by the expanding system.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    timestamp__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_timestamp", title="Extension field for ``timestamp``."
    )

    total: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="total",
        title="Total number of codes in the expansion",
        description=(
            "The total number of concepts in the expansion. If the number of "
            "concept nodes in this resource is less than the stated number, then "
            "the server can return more using the offset parameter."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    total__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_total", title="Extension field for ``total``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ValueSetExpansion`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "identifier",
            "timestamp",
            "total",
            "offset",
            "parameter",
            "contains",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("identifier", "identifier__ext"),
            ("timestamp", "timestamp__ext"),
        ]
        return required_fields


class ValueSetExpansionContains(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Codes in the value set.
    The codes that are contained in the value set expansion.
    """

    __resource_type__ = "ValueSetExpansionContains"

    abstract: bool | None = Field(  # type: ignore
        None,
        alias="abstract",
        title="If user cannot select this entry",
        description=(
            "If true, this entry is included in the expansion for navigational "
            "purposes, and the user cannot select the code directly as a proper "
            "value."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    abstract__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_abstract", title="Extension field for ``abstract``."
    )

    code: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Code - if blank, this is not a selectable code",
        description=(
            "The code for this item in the expansion hierarchy. If this code is "
            "missing the entry in the hierarchy is a place holder (abstract) and "
            "does not represent a valid code in the value set."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_code", title="Extension field for ``code``."
    )

    contains: typing.List[fhirtypes.ValueSetExpansionContainsType] | None = Field(  # type: ignore
        None,
        alias="contains",
        title="Codes contained under this entry",
        description="Other codes and entries contained under this entry in the hierarchy.",
        json_schema_extra={
            "element_property": True,
        },
    )

    designation: typing.List[fhirtypes.ValueSetComposeIncludeConceptDesignationType] | None = Field(  # type: ignore
        None,
        alias="designation",
        title="Additional representations for this item",
        description=(
            "Additional representations for this item - other languages, aliases, "
            "specialized purposes, used for particular purposes, etc. These are "
            "relevant when the conditions of the expansion do not fix to a single "
            "correct representation."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    display: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="display",
        title="User display for the concept",
        description="The recommended display for this item in the expansion.",
        json_schema_extra={
            "element_property": True,
        },
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_display", title="Extension field for ``display``."
    )

    inactive: bool | None = Field(  # type: ignore
        None,
        alias="inactive",
        title="If concept is inactive in the code system",
        description=(
            "If the concept is inactive in the code system that defines it. "
            "Inactive codes are those that are no longer to be used, but are "
            "maintained by the code system for understanding legacy data."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    inactive__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_inactive", title="Extension field for ``inactive``."
    )

    system: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="system",
        title="System value for the code",
        description=(
            "An absolute URI which is the code system in which the code for this "
            "item in the expansion is defined."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_system", title="Extension field for ``system``."
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="Version in which this code/display is defined",
        description=(
            "The version of this code system that defined this code and/or display."
            " This should only be used with code systems that do not enforce "
            "concept permanence."
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
        ``ValueSetExpansionContains`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "system",
            "abstract",
            "inactive",
            "version",
            "code",
            "display",
            "designation",
            "contains",
        ]


class ValueSetExpansionParameter(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Parameter that controlled the expansion process.
    A parameter that controlled the expansion process. These parameters may be
    used by users of expanded value sets to check whether the expansion is
    suitable for a particular purpose, or to pick the correct expansion.
    """

    __resource_type__ = "ValueSetExpansionParameter"

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name as assigned by the server",
        description="The name of the parameter.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    valueBoolean: bool | None = Field(  # type: ignore
        None,
        alias="valueBoolean",
        title="Value of the named parameter",
        description="The value of the parameter.",
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
        title="Value of the named parameter",
        description="The value of the parameter.",
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

    valueDecimal: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="valueDecimal",
        title="Value of the named parameter",
        description="The value of the parameter.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueDecimal", title="Extension field for ``valueDecimal``."
    )

    valueInteger: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="valueInteger",
        title="Value of the named parameter",
        description="The value of the parameter.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueInteger", title="Extension field for ``valueInteger``."
    )

    valueString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="valueString",
        title="Value of the named parameter",
        description="The value of the parameter.",
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

    valueUri: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="valueUri",
        title="Value of the named parameter",
        description="The value of the parameter.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueUri", title="Extension field for ``valueUri``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ValueSetExpansionParameter`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "name",
            "valueString",
            "valueBoolean",
            "valueInteger",
            "valueDecimal",
            "valueUri",
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
        required_fields = [("name", "name__ext")]
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
                "valueDecimal",
                "valueInteger",
                "valueString",
                "valueUri",
            ]
        }
        return one_of_many_fields
