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

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class ValueSet(domainresource.DomainResource):
    """ A set of codes drawn from one or more code systems.
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
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Use and/or publishing restrictions",
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date this was last changed",
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Natural language description of the value set",
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

    extensible: bool = Field(
        None,
        alias="extensible",
        title="Type `bool`",
        description="Whether this is intended to be used with an extensible binding",
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

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Intended jurisdiction for value set (if applicable)",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this value set (computer friendly)",
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of the publisher (organization or individual)",
    )

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Why this value set is defined",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="draft | active | retired | unknown",
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this value set (human friendly)",
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Logical URI to reference this value set (globally unique)",
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
        title="Type `String` (represented as `dict` in JSON)",
        description="Business version of the value set",
    )


class ValueSetCompose(backboneelement.BackboneElement):
    """ Definition of the content of the value set (CLD).
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

    include: ListType[fhirtypes.ValueSetComposeIncludeType] = Field(
        ...,
        alias="include",
        title="List of `ValueSetComposeInclude` items (represented as `dict` in JSON)",
        description="Include one or more codes from a code system or other value set(s)",
    )

    lockedDate: fhirtypes.Date = Field(
        None,
        alias="lockedDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="Fixed date for version-less references (transitive)",
    )


class ValueSetComposeInclude(backboneelement.BackboneElement):
    """ Include one or more codes from a code system or other value set(s).
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
        title="Type `Uri` (represented as `dict` in JSON)",
        description="The system the codes come from",
    )

    valueSet: ListType[fhirtypes.Uri] = Field(
        None,
        alias="valueSet",
        title="List of `Uri` items (represented as `dict` in JSON)",
        description="Select only contents included in this value set",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String` (represented as `dict` in JSON)",
        description="Specific version of the code system referred to",
    )


class ValueSetComposeIncludeConcept(backboneelement.BackboneElement):
    """ A concept defined in the system.
    Specifies a concept to be included or excluded.
    """

    resource_type = Field("ValueSetComposeIncludeConcept", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Code or expression from system",
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
        title="Type `String` (represented as `dict` in JSON)",
        description="Text to display for this code for this value set in this valueset",
    )


class ValueSetComposeIncludeConceptDesignation(backboneelement.BackboneElement):
    """ Additional representations for this concept.
    Additional representations for this concept when used in this value set -
    other languages, aliases, specialized purposes, used for particular
    purposes, etc.
    """

    resource_type = Field("ValueSetComposeIncludeConceptDesignation", const=True)

    language: fhirtypes.Code = Field(
        None,
        alias="language",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Human language of the designation",
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
        title="Type `String` (represented as `dict` in JSON)",
        description="The text value for this designation",
    )


class ValueSetComposeIncludeFilter(backboneelement.BackboneElement):
    """ Select codes/concepts by their properties (including relationships).
    Select concepts by specify a matching criteria based on the properties
    (including relationships) defined by the system. If multiple filters are
    specified, they SHALL all be true.
    """

    resource_type = Field("ValueSetComposeIncludeFilter", const=True)

    op: fhirtypes.Code = Field(
        ...,
        alias="op",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "= | is-a | descendent-of | is-not-a | regex | in | not-in | "
            "generalizes | exists"
        ),
    )

    property: fhirtypes.Code = Field(
        ...,
        alias="property",
        title="Type `Code` (represented as `dict` in JSON)",
        description="A property defined by the code system",
    )

    value: fhirtypes.Code = Field(
        ...,
        alias="value",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Code from the system, or regex criteria, or boolean value for exists",
    )


class ValueSetExpansion(backboneelement.BackboneElement):
    """ Used when the value set is "expanded".
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
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Uniquely identifies this expansion",
    )

    offset: fhirtypes.Integer = Field(
        None,
        alias="offset",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Offset at which this resource starts",
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
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Time ValueSet expansion happened",
    )

    total: fhirtypes.Integer = Field(
        None,
        alias="total",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Total number of codes in the expansion",
    )


class ValueSetExpansionContains(backboneelement.BackboneElement):
    """ Codes in the value set.
    The codes that are contained in the value set expansion.
    """

    resource_type = Field("ValueSetExpansionContains", const=True)

    abstract: bool = Field(
        None,
        alias="abstract",
        title="Type `bool`",
        description="If user cannot select this entry",
    )

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Code - if blank, this is not a selectable code",
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
        title="Type `String` (represented as `dict` in JSON)",
        description="User display for the concept",
    )

    inactive: bool = Field(
        None,
        alias="inactive",
        title="Type `bool`",
        description="If concept is inactive in the code system",
    )

    system: fhirtypes.Uri = Field(
        None,
        alias="system",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="System value for the code",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String` (represented as `dict` in JSON)",
        description="Version in which this code/display is defined",
    )


class ValueSetExpansionParameter(backboneelement.BackboneElement):
    """ Parameter that controlled the expansion process.
    A parameter that controlled the expansion process. These parameters may be
    used by users of expanded value sets to check whether the expansion is
    suitable for a particular purpose, or to pick the correct expansion.
    """

    resource_type = Field("ValueSetExpansionParameter", const=True)

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name as assigned by the server",
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="Type `bool`",
        description="Value of the named parameter",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueCode: fhirtypes.Code = Field(
        None,
        alias="valueCode",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Value of the named parameter",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="valueDecimal",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Value of the named parameter",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Value of the named parameter",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Type `String` (represented as `dict` in JSON)",
        description="Value of the named parameter",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueUri: fhirtypes.Uri = Field(
        None,
        alias="valueUri",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Value of the named parameter",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
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
