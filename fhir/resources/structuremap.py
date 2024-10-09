from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/StructureMap
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class StructureMap(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A Map of relationships between 2 structures that can be used to transform
    data.
    """

    __resource_type__ = "StructureMap"

    const: typing.List[fhirtypes.StructureMapConstType] | None = Field(  # type: ignore
        None,
        alias="const",
        title="Definition of the constant value used in the map rules",
        description="Definition of a constant value used in the map rules.",
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
            "A copyright statement relating to the structure map and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the structure map."
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
            "The date  (and optionally time) when the structure map was last "
            "significantly changed. The date must change when the business version "
            "changes and it must change if the status code changes. In addition, it"
            " should change when the substantive content of the structure map "
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
        title="Natural language description of the structure map",
        description=(
            "A free text natural language description of the structure map from a "
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
            "A Boolean value to indicate that this structure map is authored for "
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

    group: typing.List[fhirtypes.StructureMapGroupType] = Field(  # type: ignore
        ...,
        alias="group",
        title="Named sections for reader convenience",
        description=(
            "Organizes the mapping into managable chunks for human review/ease of "
            "maintenance."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Additional identifier for the structure map",
        description=(
            "A formal identifier that is used to identify this structure map when "
            "it is represented in other formats, or referenced in a specification, "
            "model, design or an instance."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    import_fhir: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="import",
        title="Other maps used by this map (canonical URLs)",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["StructureMap"],
        },
    )
    import__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_import", title="Extension field for ``import_fhir``."
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for structure map (if applicable)",
        description=(
            "A legal or geographic region in which the structure map is intended to"
            " be used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name for this structure map (computer friendly)",
        description=(
            "A natural language name identifying the structure map. This name "
            "should be usable as an identifier for the module by machine processing"
            " applications such as code generation."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
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
            " and ongoing maintenance of the structure map."
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
        title="Why this structure map is defined",
        description=(
            "Explanation of why this structure map is needed and why it has been "
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
            "The status of this structure map. Enables tracking the life-cycle of "
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

    structure: typing.List[fhirtypes.StructureMapStructureType] | None = Field(  # type: ignore
        None,
        alias="structure",
        title="Structure Definition used by this map",
        description=(
            "A structure definition used by this map. The structure definition may "
            "describe instances that are converted, or the instances that are "
            "produced."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Name for this structure map (human friendly)",
        description="A short, descriptive, user-friendly title for the structure map.",
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
            "Canonical identifier for this structure map, represented as a URI "
            "(globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this structure map when it is"
            " referenced in a specification, model, design or an instance; also "
            "called its canonical identifier. This SHOULD be globally unique and "
            "SHOULD be a literal address at which an authoritative instance of this"
            " structure map is (or will be) published. This URL can be the target "
            "of a canonical reference. It SHALL remain the same when the structure "
            "map is stored on different servers."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
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
            "indexing and searching for appropriate structure map instances."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="Business version of the structure map",
        description=(
            "The identifier that is used to identify this version of the structure "
            "map when it is referenced in a specification, model, design or "
            "instance. This is an arbitrary value managed by the structure map "
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
        ``StructureMap`` according specification,
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
            "structure",
            "import",
            "const",
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
        required_fields = [
            ("name", "name__ext"),
            ("status", "status__ext"),
            ("url", "url__ext"),
        ]
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


class StructureMapConst(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Definition of the constant value used in the map rules.
    Definition of a constant value used in the map rules.
    """

    __resource_type__ = "StructureMapConst"

    name: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Constant name",
        description="Other maps used by this map (canonical URLs).",
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    value: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="value",
        title="FHIRPath exression - value of the constant",
        description="A FHIRPath expression that is the value of this variable.",
        json_schema_extra={
            "element_property": True,
        },
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``StructureMapConst`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "name", "value"]


class StructureMapGroup(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Named sections for reader convenience.
    Organizes the mapping into managable chunks for human review/ease of
    maintenance.
    """

    __resource_type__ = "StructureMapGroup"

    documentation: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="documentation",
        title="Additional description/explanation for group",
        description=(
            "Additional supporting documentation that explains the purpose of the "
            "group and the types of mappings within it."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    extends: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="extends",
        title="Another group that this group adds rules to",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    extends__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_extends", title="Extension field for ``extends``."
    )

    input: typing.List[fhirtypes.StructureMapGroupInputType] = Field(  # type: ignore
        ...,
        alias="input",
        title="Named instance provided when invoking the map",
        description=(
            "A name assigned to an instance of data. The instance must be provided "
            "when the mapping is invoked."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    name: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Human-readable label",
        description="A unique name for the group for the convenience of human readers.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    rule: typing.List[fhirtypes.StructureMapGroupRuleType] | None = Field(  # type: ignore
        None,
        alias="rule",
        title="Transform Rule from source to target",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    typeMode: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="typeMode",
        title="types | type-and-types",
        description=(
            "If this is the default rule set to apply for the source type or this "
            "combination of types."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["types", "type-and-types"],
        },
    )
    typeMode__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_typeMode", title="Extension field for ``typeMode``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``StructureMapGroup`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "name",
            "extends",
            "typeMode",
            "documentation",
            "input",
            "rule",
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


class StructureMapGroupInput(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Named instance provided when invoking the map.
    A name assigned to an instance of data. The instance must be provided when
    the mapping is invoked.
    """

    __resource_type__ = "StructureMapGroupInput"

    documentation: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="documentation",
        title="Documentation for this instance of data",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    mode: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="mode",
        title="source | target",
        description="Mode for this instance of data.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["source", "target"],
        },
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_mode", title="Extension field for ``mode``."
    )

    name: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name for this instance of data",
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    type: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Type for this instance of data",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``StructureMapGroupInput`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "name",
            "type",
            "mode",
            "documentation",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("mode", "mode__ext"), ("name", "name__ext")]
        return required_fields


class StructureMapGroupRule(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Transform Rule from source to target.
    """

    __resource_type__ = "StructureMapGroupRule"

    dependent: typing.List[fhirtypes.StructureMapGroupRuleDependentType] | None = Field(  # type: ignore
        None,
        alias="dependent",
        title="Which other rules to apply in the context of this rule",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    documentation: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="documentation",
        title="Documentation for this instance of data",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    name: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name of the rule for internal references",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    rule: typing.List[fhirtypes.StructureMapGroupRuleType] | None = Field(  # type: ignore
        None,
        alias="rule",
        title="Rules contained in this rule",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    source: typing.List[fhirtypes.StructureMapGroupRuleSourceType] = Field(  # type: ignore
        ...,
        alias="source",
        title="Source inputs to the mapping",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    target: typing.List[fhirtypes.StructureMapGroupRuleTargetType] | None = Field(  # type: ignore
        None,
        alias="target",
        title="Content to create because of this mapping rule",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``StructureMapGroupRule`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "name",
            "source",
            "target",
            "rule",
            "dependent",
            "documentation",
        ]


class StructureMapGroupRuleDependent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Which other rules to apply in the context of this rule.
    """

    __resource_type__ = "StructureMapGroupRuleDependent"

    name: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name of a rule or group to apply",
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    parameter: typing.List[fhirtypes.StructureMapGroupRuleTargetParameterType] = Field(  # type: ignore
        ...,
        alias="parameter",
        title="Parameter to pass to the rule or group",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``StructureMapGroupRuleDependent`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "name", "parameter"]

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


class StructureMapGroupRuleSource(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Source inputs to the mapping.
    """

    __resource_type__ = "StructureMapGroupRuleSource"

    check: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="check",
        title=(
            "FHIRPath expression  - must be true or the mapping engine throws an "
            "error instead of completing"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    check__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_check", title="Extension field for ``check``."
    )

    condition: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="condition",
        title="FHIRPath expression  - must be true or the rule does not apply",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    condition__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_condition", title="Extension field for ``condition``."
    )

    context: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="context",
        title="Type or variable this rule applies to",
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    context__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_context", title="Extension field for ``context``."
    )

    defaultValue: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="defaultValue",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
        },
    )
    defaultValue__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_defaultValue", title="Extension field for ``defaultValue``."
    )

    element: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="element",
        title="Optional field for this source",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    element__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_element", title="Extension field for ``element``."
    )

    listMode: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="listMode",
        title="first | not_first | last | not_last | only_one",
        description="How to handle the list mode for this element.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["first", "not_first", "last", "not_last", "only_one"],
        },
    )
    listMode__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_listMode", title="Extension field for ``listMode``."
    )

    logMessage: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="logMessage",
        title="Message to put in log if source exists (FHIRPath)",
        description=(
            "A FHIRPath expression which specifies a message to put in the "
            "transform log when content matching the source rule is found."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    logMessage__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_logMessage", title="Extension field for ``logMessage``."
    )

    max: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="max",
        title="Specified maximum cardinality (number or *)",
        description=(
            'Specified maximum cardinality for the element - a number or a "*". '
            "This is optional; if present, it acts an implicit check on the input "
            "content (* just serves as documentation; it's the default value)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    max__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_max", title="Extension field for ``max``."
    )

    min: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="min",
        title="Specified minimum cardinality",
        description=(
            "Specified minimum cardinality for the element. This is optional; if "
            "present, it acts an implicit check on the input content."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    min__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_min", title="Extension field for ``min``."
    )

    type: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Rule only applies if source has this type",
        description=(
            "Specified type for the element. This works as a condition on the "
            "mapping - use for polymorphic elements."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    variable: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="variable",
        title="Named context for field, if a field is specified",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    variable__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_variable", title="Extension field for ``variable``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``StructureMapGroupRuleSource`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "context",
            "min",
            "max",
            "type",
            "defaultValue",
            "element",
            "listMode",
            "variable",
            "condition",
            "check",
            "logMessage",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("context", "context__ext")]
        return required_fields


class StructureMapGroupRuleTarget(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Content to create because of this mapping rule.
    """

    __resource_type__ = "StructureMapGroupRuleTarget"

    context: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="context",
        title="Variable this rule applies to",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    context__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_context", title="Extension field for ``context``."
    )

    element: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="element",
        title="Field to create in the context",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    element__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_element", title="Extension field for ``element``."
    )

    listMode: typing.List[fhirtypes.CodeType | None] | None = Field(  # type: ignore
        None,
        alias="listMode",
        title="first | share | last | single",
        description="If field is a list, how to manage the list.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["first", "share", "last", "single"],
        },
    )
    listMode__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_listMode", title="Extension field for ``listMode``."
    )

    listRuleId: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="listRuleId",
        title="Internal rule reference for shared list items",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    listRuleId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_listRuleId", title="Extension field for ``listRuleId``."
    )

    parameter: typing.List[fhirtypes.StructureMapGroupRuleTargetParameterType] | None = Field(  # type: ignore
        None,
        alias="parameter",
        title="Parameters to the transform",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    transform: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="transform",
        title="create | copy +",
        description="How the data is copied / created.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["create", "copy", "+"],
        },
    )
    transform__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_transform", title="Extension field for ``transform``."
    )

    variable: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="variable",
        title="Named context for field, if desired, and a field is specified",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    variable__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_variable", title="Extension field for ``variable``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``StructureMapGroupRuleTarget`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "context",
            "element",
            "variable",
            "listMode",
            "listRuleId",
            "transform",
            "parameter",
        ]


class StructureMapGroupRuleTargetParameter(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Parameters to the transform.
    """

    __resource_type__ = "StructureMapGroupRuleTargetParameter"

    valueBoolean: bool | None = Field(  # type: ignore
        None,
        alias="valueBoolean",
        title="Parameter value - variable or literal",
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

    valueDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="valueDate",
        title="Parameter value - variable or literal",
        description=None,
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
        title="Parameter value - variable or literal",
        description=None,
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
        title="Parameter value - variable or literal",
        description=None,
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

    valueId: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="valueId",
        title="Parameter value - variable or literal",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueId", title="Extension field for ``valueId``."
    )

    valueInteger: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="valueInteger",
        title="Parameter value - variable or literal",
        description=None,
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
        title="Parameter value - variable or literal",
        description=None,
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
        title="Parameter value - variable or literal",
        description=None,
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
        ``StructureMapGroupRuleTargetParameter`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "valueId",
            "valueString",
            "valueBoolean",
            "valueInteger",
            "valueDecimal",
            "valueDate",
            "valueTime",
            "valueDateTime",
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
                "valueDate",
                "valueDateTime",
                "valueDecimal",
                "valueId",
                "valueInteger",
                "valueString",
                "valueTime",
            ]
        }
        return one_of_many_fields


class StructureMapStructure(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Structure Definition used by this map.
    A structure definition used by this map. The structure definition may
    describe instances that are converted, or the instances that are produced.
    """

    __resource_type__ = "StructureMapStructure"

    alias: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="alias",
        title="Name for type in this map",
        description="The name used for this type in the map.",
        json_schema_extra={
            "element_property": True,
        },
    )
    alias__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_alias", title="Extension field for ``alias``."
    )

    documentation: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="documentation",
        title="Documentation on use of structure",
        description="Documentation that describes how the structure is used in the mapping.",
        json_schema_extra={
            "element_property": True,
        },
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    mode: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="mode",
        title="source | queried | target | produced",
        description="How the referenced structure is used in this mapping.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["source", "queried", "target", "produced"],
        },
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_mode", title="Extension field for ``mode``."
    )

    url: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="url",
        title="Canonical reference to structure definition",
        description="The canonical reference to the structure.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["StructureDefinition"],
        },
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_url", title="Extension field for ``url``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``StructureMapStructure`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "url",
            "mode",
            "alias",
            "documentation",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("mode", "mode__ext"), ("url", "url__ext")]
        return required_fields
