# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ValueSet
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic.v1 import Field, root_validator

from . import fhirtypes
from .backboneelement import BackboneElement
from .domainresource import DomainResource


class ValueSet(DomainResource):
    """A set of codes drawn from one or more code systems.

    A value set specifies a set of codes drawn from one or more code systems.
    """

    resource_type = Field("ValueSet", const=True)

    codeSystem: fhirtypes.ValueSetCodeSystemType = Field(
        None,
        alias="codeSystem",
        title="Type `ValueSetCodeSystem` (represented as `dict` in JSON).",
        description="An inline code system, which is part of this value set.",
    )

    compose: fhirtypes.ValueSetComposeType = Field(
        None,
        alias="compose",
        title="Type `ValueSetCompose` (represented as `dict` in JSON).",
        description="When value set includes codes from elsewhere.",
    )
    contact: ListType[fhirtypes.ValueSetContactType] = Field(
        None,
        alias="contact",
        title="List of `ValueSetContact` items (represented as `dict` in JSON).",
        description="Contact details of the publisher.",
    )

    copyright: fhirtypes.String = Field(
        None,
        alias="copyright",
        title="Type `String`.",
        description="Use and/or publishing restrictions.",
    )
    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime`.",
        description="Date for given status.",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`.",
        description="Human language description of the value set.",
    )

    expansion: fhirtypes.ValueSetExpansionType = Field(
        None,
        alias="expansion",
        title="Type `ValueSetExpansion` (represented as `dict` in JSON).",
        description="Used when the value set is 'expanded'.",
    )

    experimental: fhirtypes.Boolean = Field(
        None,
        alias="experimental",
        title="Type `Boolean`.",
        description="If for testing purposes, not real usage.",
    )

    extensible: fhirtypes.Boolean = Field(
        None,
        alias="extensible",
        title="Type `Boolean`.",
        description="Whether this is intended to be used with an extensible binding.",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON).",
        description="Additional identifier for the value set (e.g. HL7 v2 / CDA).",
    )

    immutable: fhirtypes.Boolean = Field(
        None,
        alias="immutable",
        title="Type `Boolean`.",
        description=(
            "Indicates whether or not any change to the content logical"
            "definition may occur."
        ),
    )

    lockedDate: fhirtypes.Date = Field(
        None,
        alias="lockedDate",
        title="Type `Date`.",
        description="Fixed date for all referenced code systems and value sets.",
    )
    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`.",
        description="Informal name for this value set.",
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Type `String`.",
        description="Name of the publisher (organization or individual).",
    )

    requirements: fhirtypes.String = Field(
        None, alias="requirements", title="Type `String`.", description="Why needed."
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`.",
        description="draft | active | retired.",
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri`.",
        description="Globally unique logical identifier for  value set.",
    )

    useContext: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="useContext",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="Content intends to support these contexts.",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String`.",
        description="Logical identifier for this version of the value set.",
    )


class ValueSetCodeSystem(BackboneElement):
    """An inline code system, which is part of this value set.

    A definition of a code system, inlined into the value set (as a packaging
    convenience). Note that the inline code system may be used from other value
    sets by referring to its (codeSystem.system) directly.
    """

    resource_type = Field("ValueSetCodeSystem", const=True)

    caseSensitive: fhirtypes.Boolean = Field(
        None,
        alias="caseSensitive",
        title="Type `Boolean`.",
        description="If code comparison is case sensitive.",
    )

    concept: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="concept",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="Concepts in the code system.",
    )

    system: fhirtypes.Uri = Field(
        None,
        alias="system",
        title="Type `Uri`.",
        description="URI to identify the code system (e.g. in Coding.system).",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String`.",
        description="Version (for use in Coding.version).",
    )


class ValueSetCodeSystemConcept(BackboneElement):
    """Concepts in the code system.

    Concepts that are in the code system. The concept definitions are
    inherently hierarchical, but the definitions must be consulted to determine
    what the meaning of the hierarchical relationships are.
    """

    resource_type = Field("ValueSetCodeSystemConcept", const=True)

    abstract: fhirtypes.Boolean = Field(
        None,
        alias="abstract",
        title="Type `Boolean`.",
        description="If this code is not for use as a real concept.",
    )
    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Type `Code`.",
        description="Code that identifies concept.",
    )

    definition: fhirtypes.String = Field(
        None,
        alias="definition",
        title="Type `String`.",
        description="Formal definition.",
    )
    display: fhirtypes.String = Field(
        None,
        alias="display",
        title="Type `String`.",
        description="Text to display to the user.",
    )

    concept: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="concept",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="Child Concepts (is-a/contains/categorizes).",
    )
    designation: ListType[fhirtypes.ValueSetCodeSystemConceptDesignationType] = Field(
        None,
        alias="designation",
        title=(
            "List of `ValueSetCodeSystemConceptDesignation`"
            " items (represented as `dict` in JSON)."
        ),
        description="Additional representations for the concept.",
    )


class ValueSetCodeSystemConceptDesignation(BackboneElement):
    """Additional representations for the concept.

    Additional representations for the concept - other languages, aliases,
    specialized purposes, used for particular purposes, etc.
    """

    resource_type = Field("ValueSetCodeSystemConceptDesignation", const=True)

    language: fhirtypes.Code = Field(
        None,
        alias="language",
        title="Type `Code`.",
        description="Human language of the designation.",
    )
    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="Type `String`.",
        description="The text value for this designation.",
    )

    use: fhirtypes.CodingType = Field(
        None,
        alias="use",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Details how this designation would be used.",
    )


class ValueSetCompose(BackboneElement):
    """When value set includes codes from elsewhere.

    A set of criteria that provide the content logical definition of the value
    set by including or excluding codes from outside this value set.
    """

    resource_type = Field("ValueSetCompose", const=True)

    exclude: ListType[fhirtypes.ValueSetComposeIncludeType] = Field(
        None,
        alias="exclude",
        title="List of `ValueSetComposeInclude` items (represented as `dict` in JSON).",
        description="Explicitly exclude codes.",
    )

    import_fhir: ListType[fhirtypes.Uri] = Field(
        None,
        alias="import",
        title="List of `Uri` items.",
        description="Import the contents of another value set.",
    )

    include: ListType[fhirtypes.ValueSetComposeIncludeType] = Field(
        None,
        alias="include",
        title="List of `ValueSetComposeInclude` items (represented as `dict` in JSON).",
        description="Include one or more codes from a code system.",
    )


class ValueSetComposeInclude(BackboneElement):
    """Include one or more codes from a code system."""

    resource_type = Field("ValueSetComposeInclude", const=True)

    concept: ListType[fhirtypes.ValueSetComposeIncludeConceptType] = Field(
        None,
        alias="concept",
        title="List of `ValueSetComposeIncludeConcept` items (represented as `dict` in JSON).",
        description="A concept defined in the system.",
    )

    filter: ListType[fhirtypes.ValueSetComposeIncludeFilterType] = Field(
        None,
        alias="filter",
        title="List of `ValueSetComposeIncludeFilter` items (represented as `dict` in JSON).",
        description="Select codes/concepts by their properties (including relationships).",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String`.",
        description="Specific version of the code system referred to.",
    )
    system: fhirtypes.Uri = Field(
        None,
        alias="system",
        title="Type `Uri`.",
        description="The system the codes come from.",
    )


class ValueSetComposeIncludeConcept(BackboneElement):
    """A concept defined in the system.

    Specifies a concept to be included or excluded.
    """

    resource_type = Field("ValueSetComposeIncludeConcept", const=True)

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Type `Code`.",
        description="Code or expression from system.",
    )
    display: fhirtypes.String = Field(
        None,
        alias="display",
        title="Type `String`.",
        description="Test to display for this code for this value set.",
    )

    designation: ListType[fhirtypes.ValueSetCodeSystemConceptDesignationType] = Field(
        None,
        alias="designation",
        title=(
            "List of `ValueSetCodeSystemConceptDesignation` "
            "items (represented as `dict` in JSON)."
        ),
        description="Additional representations for this valueset.",
    )


class ValueSetComposeIncludeFilter(BackboneElement):
    """Select codes/concepts by their properties (including relationships).

    Select concepts by specify a matching criteria based on the properties
    (including relationships) defined by the system. If multiple filters are
    specified, they SHALL all be true.
    """

    resource_type = Field("ValueSetComposeIncludeFilter", const=True)

    op: fhirtypes.Code = Field(
        None,
        alias="op",
        title="Type `Code`.",
        description="= | is-a | is-not-a | regex | in | not-in.",
    )

    value: fhirtypes.Code = Field(
        None,
        alias="value",
        title="Type `Code`.",
        description="Code from the system, or regex criteria.",
    )

    property: fhirtypes.Code = Field(
        None,
        alias="property",
        title="Type `Code`.",
        description="A property defined by the code system.",
    )


class ValueSetContact(BackboneElement):
    """Contact details of the publisher.

    Contacts to assist a user in finding and communicating with the publisher.
    """

    resource_type = Field("ValueSetContact", const=True)

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`.",
        description="Name of an individual to contact.",
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="List of `ContactPoint` items (represented as `dict` in JSON).",
        description="Contact details for individual or publisher.",
    )


class ValueSetExpansion(BackboneElement):
    """Used when the value set is "expanded".

    A value set can also be "expanded", where the value set is turned into a
    simple collection of enumerated codes. This element holds the expansion, if
    it has been performed.
    """

    resource_type = Field("ValueSetExpansion", const=True)

    identifier: fhirtypes.Uri = Field(
        ...,
        alias="identifier",
        title="Type `Uri`.",
        description="Uniquely identifies this expansion.",
    )

    contains: ListType[fhirtypes.ValueSetExpansionContainsType] = Field(
        None,
        alias="contains",
        title="List of `ValueSetExpansionContains` items (represented as `dict` in JSON).",
        description="Contact details for individual or publisher.",
    )

    offset: fhirtypes.Integer = Field(
        None,
        alias="offset",
        title="Type `Integer`.",
        description="Offset at which this resource starts.",
    )
    timestamp: fhirtypes.DateTime = Field(
        None,
        alias="timestamp",
        title="Type `DateTime`.",
        description="Time ValueSet expansion happened.",
    )

    total: fhirtypes.Integer = Field(
        None,
        alias="total",
        title="Type `Integer`.",
        description="Total number of codes in the expansion.",
    )

    parameter: ListType[fhirtypes.ValueSetExpansionParameterType] = Field(
        None,
        alias="parameter",
        title="List of `ValueSetExpansionParameter` items (represented as `dict` in JSON).",
        description="Parameter that controlled the expansion process.",
    )


class ValueSetExpansionContains(BackboneElement):
    """Codes in the value set.

    The codes that are contained in the value set expansion.
    """

    resource_type = Field("ValueSetExpansionContains", const=True)

    abstract: fhirtypes.Boolean = Field(
        None,
        alias="abstract",
        title="Type `Boolean`.",
        description="If user cannot select this entry.",
    )

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Type `Code`.",
        description="Code - if blank, this is not a selectable code.",
    )

    display: fhirtypes.String = Field(
        None,
        alias="display",
        title="Type `String`.",
        description="User display for the concept.",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String`.",
        description="Version in which this code/display is defined.",
    )

    system: fhirtypes.Uri = Field(
        None,
        alias="system",
        title="Type `Uri`.",
        description=" System value for the code.",
    )

    contains: ListType[fhirtypes.ValueSetExpansionContainsType] = Field(
        None,
        alias="contains",
        title="List of `ValueSetExpansionContains` items (represented as `dict` in JSON).",
        description="Codes contained under this entry.",
    )


class ValueSetExpansionParameter(BackboneElement):
    """Parameter that controlled the expansion process.

    A parameter that controlled the expansion process. These parameters may be
    used by users of expanded value sets to check whether the expansion is
    suitable for a particular purpose, or to pick the correct expansion.
    """

    resource_type = Field("ValueSetExpansionParameter", const=True)

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="Type `bool`",
        description="Value of the named parameter.",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueCode: fhirtypes.Code = Field(
        None,
        alias="valueCode",
        title="Value of the named parameter.",
        description="Value of the named parameter.",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="valueDecimal",
        title="Type `Decimal`",
        description="Value of the named parameter.",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="Type `Integer`",
        description="Value of the named parameter.",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Type `String`",
        description="Value of the named parameter.",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueUri: fhirtypes.Uri = Field(
        None,
        alias="valueUri",
        title="Type `Uri`",
        description="Value of the named parameter.",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name as assigned by the server.",
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
