# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CodeSystem
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


class CodeSystem(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A set of codes drawn from one or more code systems.
    A code system resource specifies a set of codes drawn from one or more code
    systems.
    """

    resource_type = Field("CodeSystem", const=True)

    caseSensitive: bool = Field(
        None,
        alias="caseSensitive",
        title="Type `bool`",
        description="If code comparison is case sensitive",
    )
    caseSensitive__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_caseSensitive", title="Extension field for ``caseSensitive``."
    )

    compositional: bool = Field(
        None,
        alias="compositional",
        title="Type `bool`",
        description="If code system defines a post-composition grammar",
    )
    compositional__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_compositional", title="Extension field for ``compositional``."
    )

    concept: ListType[fhirtypes.CodeSystemConceptType] = Field(
        None,
        alias="concept",
        title="List of `CodeSystemConcept` items (represented as `dict` in JSON)",
        description="Concepts in the code system",
    )

    contact: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Contact details for the publisher",
    )

    content: fhirtypes.Code = Field(
        ...,
        alias="content",
        title="Type `Code`",
        description="not-present | example | fragment | complete",
    )
    content__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_content", title="Extension field for ``content``."
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

    count: fhirtypes.UnsignedInt = Field(
        None,
        alias="count",
        title="Type `UnsignedInt`",
        description="Total concepts in the code system",
    )
    count__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_count", title="Extension field for ``count``."
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
        description="Natural language description of the code system",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
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

    filter: ListType[fhirtypes.CodeSystemFilterType] = Field(
        None,
        alias="filter",
        title="List of `CodeSystemFilter` items (represented as `dict` in JSON)",
        description="Filter that can be used in a value set",
    )

    hierarchyMeaning: fhirtypes.Code = Field(
        None,
        alias="hierarchyMeaning",
        title="Type `Code`",
        description="grouped-by | is-a | part-of | classified-with",
    )
    hierarchyMeaning__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_hierarchyMeaning",
        title="Extension field for ``hierarchyMeaning``.",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Additional identifier for the code system",
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Intended jurisdiction for code system (if applicable)",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`",
        description="Name for this code system (computer friendly)",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    property: ListType[fhirtypes.CodeSystemPropertyType] = Field(
        None,
        alias="property",
        title="List of `CodeSystemProperty` items (represented as `dict` in JSON)",
        description="Additional information supplied about each concept",
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
        description="Why this code system is defined",
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
        description="Name for this code system (human friendly)",
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri`",
        description=(
            "Logical URI to reference this code system (globally unique) "
            "(Coding.system)"
        ),
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

    valueSet: fhirtypes.Uri = Field(
        None,
        alias="valueSet",
        title="Type `Uri`",
        description="Canonical URL for value set with entire code system",
    )
    valueSet__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueSet", title="Extension field for ``valueSet``."
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String`",
        description="Business version of the code system (Coding.version)",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    versionNeeded: bool = Field(
        None,
        alias="versionNeeded",
        title="Type `bool`",
        description="If definitions are not stable",
    )
    versionNeeded__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_versionNeeded", title="Extension field for ``versionNeeded``."
    )


class CodeSystemConcept(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Concepts in the code system.
    Concepts that are in the code system. The concept definitions are
    inherently hierarchical, but the definitions must be consulted to determine
    what the meaning of the hierarchical relationships are.
    """

    resource_type = Field("CodeSystemConcept", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Type `Code`",
        description="Code that identifies concept",
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    concept: ListType[fhirtypes.CodeSystemConceptType] = Field(
        None,
        alias="concept",
        title="List of `CodeSystemConcept` items (represented as `dict` in JSON)",
        description="Child Concepts (is-a/contains/categorizes)",
    )

    definition: fhirtypes.String = Field(
        None, alias="definition", title="Type `String`", description="Formal definition"
    )
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_definition", title="Extension field for ``definition``."
    )

    designation: ListType[fhirtypes.CodeSystemConceptDesignationType] = Field(
        None,
        alias="designation",
        title=(
            "List of `CodeSystemConceptDesignation` items (represented as `dict` in"
            " JSON)"
        ),
        description="Additional representations for the concept",
    )

    display: fhirtypes.String = Field(
        None,
        alias="display",
        title="Type `String`",
        description="Text to display to the user",
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_display", title="Extension field for ``display``."
    )

    property: ListType[fhirtypes.CodeSystemConceptPropertyType] = Field(
        None,
        alias="property",
        title=(
            "List of `CodeSystemConceptProperty` items (represented as `dict` in "
            "JSON)"
        ),
        description="Property value for the concept",
    )


class CodeSystemConceptDesignation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional representations for the concept.
    Additional representations for the concept - other languages, aliases,
    specialized purposes, used for particular purposes, etc.
    """

    resource_type = Field("CodeSystemConceptDesignation", const=True)

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


class CodeSystemConceptProperty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Property value for the concept.
    A property value for this concept.
    """

    resource_type = Field("CodeSystemConceptProperty", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Type `Code`",
        description="Reference to CodeSystem.property.code",
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="Type `bool`",
        description="Value of the property for this concept",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCode: fhirtypes.Code = Field(
        None,
        alias="valueCode",
        title="Type `Code`",
        description="Value of the property for this concept",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueCode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueCode", title="Extension field for ``valueCode``."
    )

    valueCoding: fhirtypes.CodingType = Field(
        None,
        alias="valueCoding",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Value of the property for this concept",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="valueDateTime",
        title="Type `DateTime`",
        description="Value of the property for this concept",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDateTime", title="Extension field for ``valueDateTime``."
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="Type `Integer`",
        description="Value of the property for this concept",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueInteger", title="Extension field for ``valueInteger``."
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Type `String`",
        description="Value of the property for this concept",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueString", title="Extension field for ``valueString``."
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
                "valueCoding",
                "valueDateTime",
                "valueInteger",
                "valueString",
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


class CodeSystemFilter(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Filter that can be used in a value set.
    A filter that can be used in a value set compose statement when selecting
    concepts using a filter.
    """

    resource_type = Field("CodeSystemFilter", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Type `Code`",
        description="Code that identifies the filter",
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="How or why the filter is used",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    operator: ListType[fhirtypes.Code] = Field(
        ...,
        alias="operator",
        title="List of `Code` items",
        description="Operators that can be used with filter",
    )
    operator__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_operator", title="Extension field for ``operator``."
    )

    value: fhirtypes.String = Field(
        ...,
        alias="value",
        title="Type `String`",
        description="What to use for the value",
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )


class CodeSystemProperty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional information supplied about each concept.
    A property defines an additional slot through which additional information
    can be provided about a concept.
    """

    resource_type = Field("CodeSystemProperty", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Type `Code`",
        description=(
            "Identifies the property on the concepts, and when referred to in "
            "operations"
        ),
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Why the property is defined, and/or what it conveys",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code`",
        description="code | Coding | string | integer | boolean | dateTime",
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    uri: fhirtypes.Uri = Field(
        None,
        alias="uri",
        title="Type `Uri`",
        description="Formal identifier for the property",
    )
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_uri", title="Extension field for ``uri``."
    )
