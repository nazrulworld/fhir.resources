# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ValueSet
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType
from typing import Union

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class ValueSet(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A set of codes drawn from one or more code systems.
    A value set specifies a set of codes drawn from one or more code systems.
    """

    resource_type = Field("ValueSet", const=True)

    compose: fhirtypes.ValueSetComposeType = Field(
        None,
        alias="compose",
        title="Type `ValueSetCompose` (represented as `dict` in JSON)",
        description="Definition of the content of the value set (CLD)",
    )

    contact: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Contact details for the publisher",
    )

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Type `Markdown`",
        description="Use and/or publishing restrictions",
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime`",
        description="Date this was last changed",
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown`",
        description="Natural language description of the value set",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    expansion: fhirtypes.ValueSetExpansionType = Field(
        None,
        alias="expansion",
        title="Type `ValueSetExpansion` (represented as `dict` in JSON)",
        description='Used when the value set is "expanded"',
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="Type `bool`",
        description="For testing purposes, not real usage",
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    extensible: bool = Field(
        None,
        alias="extensible",
        title="Type `bool`",
        description="Whether this is intended to be used with an extensible binding",
    )
    extensible__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_extensible", title="Extension field for ``extensible``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Additional identifier for the value set",
    )

    immutable: bool = Field(
        None,
        alias="immutable",
        title="Type `bool`",
        description=(
            "Indicates whether or not any change to the content logical definition "
            "may occur"
        ),
    )
    immutable__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_immutable", title="Extension field for ``immutable``."
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Intended jurisdiction for value set (if applicable)",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`",
        description="Name for this value set (computer friendly)",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Type `String`",
        description="Name of the publisher (organization or individual)",
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Type `Markdown`",
        description="Why this value set is defined",
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`",
        description="draft | active | retired | unknown",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String`",
        description="Name for this value set (human friendly)",
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri`",
        description="Logical URI to reference this value set (globally unique)",
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    useContext: ListType[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="List of `UsageContext` items (represented as `dict` in JSON)",
        description="Context the content is intended to support",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String`",
        description="Business version of the value set",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class ValueSetCompose(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Definition of the content of the value set (CLD).
    A set of criteria that define the content logical definition of the value
    set by including or excluding codes from outside this value set. This I
    also known as the "Content Logical Definition" (CLD).
    """

    resource_type = Field("ValueSetCompose", const=True)

    exclude: ListType[fhirtypes.ValueSetComposeIncludeType] = Field(
        None,
        alias="exclude",
        title="List of `ValueSetComposeInclude` items (represented as `dict` in JSON)",
        description="Explicitly exclude codes from a code system or other value sets",
    )

    inactive: bool = Field(
        None,
        alias="inactive",
        title="Type `bool`",
        description="Whether inactive codes are in the value set",
    )
    inactive__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_inactive", title="Extension field for ``inactive``."
    )

    include: ListType[fhirtypes.ValueSetComposeIncludeType] = Field(
        ...,
        alias="include",
        title="List of `ValueSetComposeInclude` items (represented as `dict` in JSON)",
        description="Include one or more codes from a code system or other value set(s)",
    )

    lockedDate: fhirtypes.Date = Field(
        None,
        alias="lockedDate",
        title="Type `Date`",
        description="Fixed date for version-less references (transitive)",
    )
    lockedDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lockedDate", title="Extension field for ``lockedDate``."
    )


class ValueSetComposeInclude(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Include one or more codes from a code system or other value set(s).
    """

    resource_type = Field("ValueSetComposeInclude", const=True)

    concept: ListType[fhirtypes.ValueSetComposeIncludeConceptType] = Field(
        None,
        alias="concept",
        title=(
            "List of `ValueSetComposeIncludeConcept` items (represented as `dict` "
            "in JSON)"
        ),
        description="A concept defined in the system",
    )

    filter: ListType[fhirtypes.ValueSetComposeIncludeFilterType] = Field(
        None,
        alias="filter",
        title=(
            "List of `ValueSetComposeIncludeFilter` items (represented as `dict` in"
            " JSON)"
        ),
        description="Select codes/concepts by their properties (including relationships)",
    )

    system: fhirtypes.Uri = Field(
        None,
        alias="system",
        title="Type `Uri`",
        description="The system the codes come from",
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_system", title="Extension field for ``system``."
    )

    valueSet: ListType[fhirtypes.Uri] = Field(
        None,
        alias="valueSet",
        title="List of `Uri` items",
        description="Select only contents included in this value set",
    )
    valueSet__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_valueSet", title="Extension field for ``valueSet``."
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String`",
        description="Specific version of the code system referred to",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class ValueSetComposeIncludeConcept(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A concept defined in the system.
    Specifies a concept to be included or excluded.
    """

    resource_type = Field("ValueSetComposeIncludeConcept", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Type `Code`",
        description="Code or expression from system",
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    designation: ListType[
        fhirtypes.ValueSetComposeIncludeConceptDesignationType
    ] = Field(
        None,
        alias="designation",
        title=(
            "List of `ValueSetComposeIncludeConceptDesignation` items (represented "
            "as `dict` in JSON)"
        ),
        description="Additional representations for this concept",
    )

    display: fhirtypes.String = Field(
        None,
        alias="display",
        title="Type `String`",
        description="Text to display for this code for this value set in this valueset",
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_display", title="Extension field for ``display``."
    )


class ValueSetComposeIncludeConceptDesignation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional representations for this concept.
    Additional representations for this concept when used in this value set -
    other languages, aliases, specialized purposes, used for particular
    purposes, etc.
    """

    resource_type = Field("ValueSetComposeIncludeConceptDesignation", const=True)

    language: fhirtypes.Code = Field(
        None,
        alias="language",
        title="Type `Code`",
        description="Human language of the designation",
    )
    language__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_language", title="Extension field for ``language``."
    )

    use: fhirtypes.CodingType = Field(
        None,
        alias="use",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Details how this designation would be used",
    )

    value: fhirtypes.String = Field(
        ...,
        alias="value",
        title="Type `String`",
        description="The text value for this designation",
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )


class ValueSetComposeIncludeFilter(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Select codes/concepts by their properties (including relationships).
    Select concepts by specify a matching criteria based on the properties
    (including relationships) defined by the system. If multiple filters are
    specified, they SHALL all be true.
    """

    resource_type = Field("ValueSetComposeIncludeFilter", const=True)

    op: fhirtypes.Code = Field(
        ...,
        alias="op",
        title="Type `Code`",
        description=(
            "= | is-a | descendent-of | is-not-a | regex | in | not-in | "
            "generalizes | exists"
        ),
    )
    op__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_op", title="Extension field for ``op``."
    )

    property: fhirtypes.Code = Field(
        ...,
        alias="property",
        title="Type `Code`",
        description="A property defined by the code system",
    )
    property__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_property", title="Extension field for ``property``."
    )

    value: fhirtypes.Code = Field(
        ...,
        alias="value",
        title="Type `Code`",
        description="Code from the system, or regex criteria, or boolean value for exists",
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )


class ValueSetExpansion(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Used when the value set is "expanded".
    A value set can also be "expanded", where the value set is turned into a
    simple collection of enumerated codes. This element holds the expansion, if
    it has been performed.
    """

    resource_type = Field("ValueSetExpansion", const=True)

    contains: ListType[fhirtypes.ValueSetExpansionContainsType] = Field(
        None,
        alias="contains",
        title=(
            "List of `ValueSetExpansionContains` items (represented as `dict` in "
            "JSON)"
        ),
        description="Codes in the value set",
    )

    identifier: fhirtypes.Uri = Field(
        ...,
        alias="identifier",
        title="Type `Uri`",
        description="Uniquely identifies this expansion",
    )
    identifier__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_identifier", title="Extension field for ``identifier``."
    )

    offset: fhirtypes.Integer = Field(
        None,
        alias="offset",
        title="Type `Integer`",
        description="Offset at which this resource starts",
    )
    offset__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_offset", title="Extension field for ``offset``."
    )

    parameter: ListType[fhirtypes.ValueSetExpansionParameterType] = Field(
        None,
        alias="parameter",
        title=(
            "List of `ValueSetExpansionParameter` items (represented as `dict` in "
            "JSON)"
        ),
        description="Parameter that controlled the expansion process",
    )

    timestamp: fhirtypes.DateTime = Field(
        ...,
        alias="timestamp",
        title="Type `DateTime`",
        description="Time ValueSet expansion happened",
    )
    timestamp__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_timestamp", title="Extension field for ``timestamp``."
    )

    total: fhirtypes.Integer = Field(
        None,
        alias="total",
        title="Type `Integer`",
        description="Total number of codes in the expansion",
    )
    total__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_total", title="Extension field for ``total``."
    )


class ValueSetExpansionContains(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Codes in the value set.
    The codes that are contained in the value set expansion.
    """

    resource_type = Field("ValueSetExpansionContains", const=True)

    abstract: bool = Field(
        None,
        alias="abstract",
        title="Type `bool`",
        description="If user cannot select this entry",
    )
    abstract__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_abstract", title="Extension field for ``abstract``."
    )

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Type `Code`",
        description="Code - if blank, this is not a selectable code",
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    contains: ListType[fhirtypes.ValueSetExpansionContainsType] = Field(
        None,
        alias="contains",
        title=(
            "List of `ValueSetExpansionContains` items (represented as `dict` in "
            "JSON)"
        ),
        description="Codes contained under this entry",
    )

    designation: ListType[
        fhirtypes.ValueSetComposeIncludeConceptDesignationType
    ] = Field(
        None,
        alias="designation",
        title=(
            "List of `ValueSetComposeIncludeConceptDesignation` items (represented "
            "as `dict` in JSON)"
        ),
        description="Additional representations for this item",
    )

    display: fhirtypes.String = Field(
        None,
        alias="display",
        title="Type `String`",
        description="User display for the concept",
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_display", title="Extension field for ``display``."
    )

    inactive: bool = Field(
        None,
        alias="inactive",
        title="Type `bool`",
        description="If concept is inactive in the code system",
    )
    inactive__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_inactive", title="Extension field for ``inactive``."
    )

    system: fhirtypes.Uri = Field(
        None,
        alias="system",
        title="Type `Uri`",
        description="System value for the code",
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_system", title="Extension field for ``system``."
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String`",
        description="Version in which this code/display is defined",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class ValueSetExpansionParameter(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Parameter that controlled the expansion process.
    A parameter that controlled the expansion process. These parameters may be
    used by users of expanded value sets to check whether the expansion is
    suitable for a particular purpose, or to pick the correct expansion.
    """

    resource_type = Field("ValueSetExpansionParameter", const=True)

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String`",
        description="Name as assigned by the server",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="Type `bool`",
        description="Value of the named parameter",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCode: fhirtypes.Code = Field(
        None,
        alias="valueCode",
        title="Type `Code`",
        description="Value of the named parameter",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueCode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueCode", title="Extension field for ``valueCode``."
    )

    valueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="valueDecimal",
        title="Type `Decimal`",
        description="Value of the named parameter",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDecimal", title="Extension field for ``valueDecimal``."
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="Type `Integer`",
        description="Value of the named parameter",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueInteger", title="Extension field for ``valueInteger``."
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Type `String`",
        description="Value of the named parameter",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    valueUri: fhirtypes.Uri = Field(
        None,
        alias="valueUri",
        title="Type `Uri`",
        description="Value of the named parameter",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueUri", title="Extension field for ``valueUri``."
    )

    @root_validator(pre=True)
    def validate_one_of_many(cls, values: Dict[str, Any]) -> Dict[str, Any]:
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
