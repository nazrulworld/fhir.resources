from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/StructureMap
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
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

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="date",
        title="Date this was last changed",
        description=(
            "The date  (and optionally time) when the structure map was published. "
            "The date must change if and when the business version changes and it "
            "must change if the status code changes. In addition, it should change "
            "when the substantive content of the structure map changes."
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
            "A boolean value to indicate that this structure map is authored for "
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

    import_fhir: typing.List[fhirtypes.UriType | None] | None = Field(  # type: ignore
        None,
        alias="import",
        title="Other maps used by this map (canonical URLs)",
        description=None,
        json_schema_extra={
            "element_property": True,
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
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the individual or organization that published the "
            "structure map."
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
            "Explaination of why this structure map is needed and why it has been "
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
        title="Logical URI to reference this structure map (globally unique)",
        description=(
            "An absolute URI that is used to identify this structure map when it is"
            " referenced in a specification, model, design or an instance. This "
            "SHALL be a URL, SHOULD be globally unique, and SHOULD be an address at"
            " which this structure map is (or will be) published. The URL SHOULD "
            "include the major version of the structure map. For more information "
            "see [Technical and Business Versions](resource.html#versions)."
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
        title="Context the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These terms may be used to assist with "
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
            "structure",
            "import",
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
        title="Additional description/explaination for group",
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

    rule: typing.List[fhirtypes.StructureMapGroupRuleType] = Field(  # type: ignore
        ...,
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
        title="none | types | type-and-types",
        description=(
            "If this is the default rule set to apply for thie source type, or this"
            " combination of types."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["none", "types", "type-and-types"],
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
        required_fields = [("name", "name__ext"), ("typeMode", "typeMode__ext")]
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
            "element_required": True,
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

    variable: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="variable",
        title="Variable to pass to the rule or group",
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    variable__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_variable", title="Extension field for ``variable``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``StructureMapGroupRuleDependent`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "name", "variable"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("name", "name__ext"), ("variable", "variable__ext")]
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

    defaultValueAddress: fhirtypes.AddressType | None = Field(  # type: ignore
        None,
        alias="defaultValueAddress",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )

    defaultValueAge: fhirtypes.AgeType | None = Field(  # type: ignore
        None,
        alias="defaultValueAge",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )

    defaultValueAnnotation: fhirtypes.AnnotationType | None = Field(  # type: ignore
        None,
        alias="defaultValueAnnotation",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )

    defaultValueAttachment: fhirtypes.AttachmentType | None = Field(  # type: ignore
        None,
        alias="defaultValueAttachment",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )

    defaultValueBase64Binary: fhirtypes.Base64BinaryType | None = Field(  # type: ignore
        None,
        alias="defaultValueBase64Binary",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )
    defaultValueBase64Binary__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_defaultValueBase64Binary",
        title="Extension field for ``defaultValueBase64Binary``.",
    )

    defaultValueBoolean: bool | None = Field(  # type: ignore
        None,
        alias="defaultValueBoolean",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )
    defaultValueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_defaultValueBoolean",
        title="Extension field for ``defaultValueBoolean``.",
    )

    defaultValueCode: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="defaultValueCode",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )
    defaultValueCode__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_defaultValueCode",
        title="Extension field for ``defaultValueCode``.",
    )

    defaultValueCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="defaultValueCodeableConcept",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )

    defaultValueCoding: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="defaultValueCoding",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )

    defaultValueContactPoint: fhirtypes.ContactPointType | None = Field(  # type: ignore
        None,
        alias="defaultValueContactPoint",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )

    defaultValueCount: fhirtypes.CountType | None = Field(  # type: ignore
        None,
        alias="defaultValueCount",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )

    defaultValueDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="defaultValueDate",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )
    defaultValueDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_defaultValueDate",
        title="Extension field for ``defaultValueDate``.",
    )

    defaultValueDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="defaultValueDateTime",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )
    defaultValueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_defaultValueDateTime",
        title="Extension field for ``defaultValueDateTime``.",
    )

    defaultValueDecimal: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="defaultValueDecimal",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )
    defaultValueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_defaultValueDecimal",
        title="Extension field for ``defaultValueDecimal``.",
    )

    defaultValueDistance: fhirtypes.DistanceType | None = Field(  # type: ignore
        None,
        alias="defaultValueDistance",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )

    defaultValueDuration: fhirtypes.DurationType | None = Field(  # type: ignore
        None,
        alias="defaultValueDuration",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )

    defaultValueHumanName: fhirtypes.HumanNameType | None = Field(  # type: ignore
        None,
        alias="defaultValueHumanName",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )

    defaultValueId: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="defaultValueId",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )
    defaultValueId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_defaultValueId", title="Extension field for ``defaultValueId``."
    )

    defaultValueIdentifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="defaultValueIdentifier",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )

    defaultValueInstant: fhirtypes.InstantType | None = Field(  # type: ignore
        None,
        alias="defaultValueInstant",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )
    defaultValueInstant__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_defaultValueInstant",
        title="Extension field for ``defaultValueInstant``.",
    )

    defaultValueInteger: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="defaultValueInteger",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )
    defaultValueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_defaultValueInteger",
        title="Extension field for ``defaultValueInteger``.",
    )

    defaultValueMarkdown: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="defaultValueMarkdown",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )
    defaultValueMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_defaultValueMarkdown",
        title="Extension field for ``defaultValueMarkdown``.",
    )

    defaultValueMeta: fhirtypes.MetaType | None = Field(  # type: ignore
        None,
        alias="defaultValueMeta",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )

    defaultValueMoney: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="defaultValueMoney",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )

    defaultValueOid: fhirtypes.OidType | None = Field(  # type: ignore
        None,
        alias="defaultValueOid",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )
    defaultValueOid__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_defaultValueOid", title="Extension field for ``defaultValueOid``."
    )

    defaultValuePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="defaultValuePeriod",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )

    defaultValuePositiveInt: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="defaultValuePositiveInt",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )
    defaultValuePositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_defaultValuePositiveInt",
        title="Extension field for ``defaultValuePositiveInt``.",
    )

    defaultValueQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="defaultValueQuantity",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )

    defaultValueRange: fhirtypes.RangeType | None = Field(  # type: ignore
        None,
        alias="defaultValueRange",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )

    defaultValueRatio: fhirtypes.RatioType | None = Field(  # type: ignore
        None,
        alias="defaultValueRatio",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )

    defaultValueReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="defaultValueReference",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )

    defaultValueSampledData: fhirtypes.SampledDataType | None = Field(  # type: ignore
        None,
        alias="defaultValueSampledData",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )

    defaultValueSignature: fhirtypes.SignatureType | None = Field(  # type: ignore
        None,
        alias="defaultValueSignature",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )

    defaultValueString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="defaultValueString",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )
    defaultValueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_defaultValueString",
        title="Extension field for ``defaultValueString``.",
    )

    defaultValueTime: fhirtypes.TimeType | None = Field(  # type: ignore
        None,
        alias="defaultValueTime",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )
    defaultValueTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_defaultValueTime",
        title="Extension field for ``defaultValueTime``.",
    )

    defaultValueTiming: fhirtypes.TimingType | None = Field(  # type: ignore
        None,
        alias="defaultValueTiming",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )

    defaultValueUnsignedInt: fhirtypes.UnsignedIntType | None = Field(  # type: ignore
        None,
        alias="defaultValueUnsignedInt",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )
    defaultValueUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_defaultValueUnsignedInt",
        title="Extension field for ``defaultValueUnsignedInt``.",
    )

    defaultValueUri: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="defaultValueUri",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e defaultValue[x]
            "one_of_many": "defaultValue",
            "one_of_many_required": False,
        },
    )
    defaultValueUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_defaultValueUri", title="Extension field for ``defaultValueUri``."
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
            "defaultValueBase64Binary",
            "defaultValueBoolean",
            "defaultValueCode",
            "defaultValueDate",
            "defaultValueDateTime",
            "defaultValueDecimal",
            "defaultValueId",
            "defaultValueInstant",
            "defaultValueInteger",
            "defaultValueMarkdown",
            "defaultValueOid",
            "defaultValuePositiveInt",
            "defaultValueString",
            "defaultValueTime",
            "defaultValueUnsignedInt",
            "defaultValueUri",
            "defaultValueAddress",
            "defaultValueAge",
            "defaultValueAnnotation",
            "defaultValueAttachment",
            "defaultValueCodeableConcept",
            "defaultValueCoding",
            "defaultValueContactPoint",
            "defaultValueCount",
            "defaultValueDistance",
            "defaultValueDuration",
            "defaultValueHumanName",
            "defaultValueIdentifier",
            "defaultValueMoney",
            "defaultValuePeriod",
            "defaultValueQuantity",
            "defaultValueRange",
            "defaultValueRatio",
            "defaultValueReference",
            "defaultValueSampledData",
            "defaultValueSignature",
            "defaultValueTiming",
            "defaultValueMeta",
            "element",
            "listMode",
            "variable",
            "condition",
            "check",
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
            "defaultValue": [
                "defaultValueAddress",
                "defaultValueAge",
                "defaultValueAnnotation",
                "defaultValueAttachment",
                "defaultValueBase64Binary",
                "defaultValueBoolean",
                "defaultValueCode",
                "defaultValueCodeableConcept",
                "defaultValueCoding",
                "defaultValueContactPoint",
                "defaultValueCount",
                "defaultValueDate",
                "defaultValueDateTime",
                "defaultValueDecimal",
                "defaultValueDistance",
                "defaultValueDuration",
                "defaultValueHumanName",
                "defaultValueId",
                "defaultValueIdentifier",
                "defaultValueInstant",
                "defaultValueInteger",
                "defaultValueMarkdown",
                "defaultValueMeta",
                "defaultValueMoney",
                "defaultValueOid",
                "defaultValuePeriod",
                "defaultValuePositiveInt",
                "defaultValueQuantity",
                "defaultValueRange",
                "defaultValueRatio",
                "defaultValueReference",
                "defaultValueSampledData",
                "defaultValueSignature",
                "defaultValueString",
                "defaultValueTime",
                "defaultValueTiming",
                "defaultValueUnsignedInt",
                "defaultValueUri",
            ]
        }
        return one_of_many_fields


class StructureMapGroupRuleTarget(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Content to create because of this mapping rule.
    """

    __resource_type__ = "StructureMapGroupRuleTarget"

    context: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="context",
        title="Type or variable this rule applies to",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    context__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_context", title="Extension field for ``context``."
    )

    contextType: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="contextType",
        title="type | variable",
        description="How to interpret the context.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["type", "variable"],
        },
    )
    contextType__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_contextType", title="Extension field for ``contextType``."
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
        title="first | share | last | collate",
        description="If field is a list, how to manage the list.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["first", "share", "last", "collate"],
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
            "contextType",
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
                "valueDecimal",
                "valueId",
                "valueInteger",
                "valueString",
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

    url: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="url",
        title="Canonical URL for structure definition",
        description="The canonical URL that identifies the structure.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
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
