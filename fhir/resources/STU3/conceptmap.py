# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ConceptMap
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class ConceptMap(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A map from one set of concepts to one or more other concepts.
    A statement of relationships from one set of concepts to one or more other
    concepts - either code systems or data elements, or classes in class
    models.
    """

    resource_type = Field("ConceptMap", const=True)

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
        description="Natural language description of the concept map",
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

    group: ListType[fhirtypes.ConceptMapGroupType] = Field(
        None,
        alias="group",
        title="List of `ConceptMapGroup` items (represented as `dict` in JSON)",
        description="Same source and target systems",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Additional identifier for the concept map",
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Intended jurisdiction for concept map (if applicable)",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`",
        description="Name for this concept map (computer friendly)",
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
        description="Why this concept map is defined",
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    sourceReference: fhirtypes.ReferenceType = Field(
        None,
        alias="sourceReference",
        title=(
            "Type `Reference` referencing `ValueSet` (represented as `dict` in " "JSON)"
        ),
        description="Identifies the source of the concepts which are being mapped",
        one_of_many="source",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    sourceUri: fhirtypes.Uri = Field(
        None,
        alias="sourceUri",
        title="Type `Uri`",
        description="Identifies the source of the concepts which are being mapped",
        one_of_many="source",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    sourceUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sourceUri", title="Extension field for ``sourceUri``."
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

    targetReference: fhirtypes.ReferenceType = Field(
        None,
        alias="targetReference",
        title=(
            "Type `Reference` referencing `ValueSet` (represented as `dict` in " "JSON)"
        ),
        description="Provides context to the mappings",
        one_of_many="target",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    targetUri: fhirtypes.Uri = Field(
        None,
        alias="targetUri",
        title="Type `Uri`",
        description="Provides context to the mappings",
        one_of_many="target",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    targetUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_targetUri", title="Extension field for ``targetUri``."
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String`",
        description="Name for this concept map (human friendly)",
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri`",
        description="Logical URI to reference this concept map (globally unique)",
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
        description="Business version of the concept map",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
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
            "source": ["sourceReference", "sourceUri"],
            "target": ["targetReference", "targetUri"],
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


class ConceptMapGroup(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Same source and target systems.
    A group of mappings that all have the same source and target system.
    """

    resource_type = Field("ConceptMapGroup", const=True)

    element: ListType[fhirtypes.ConceptMapGroupElementType] = Field(
        ...,
        alias="element",
        title="List of `ConceptMapGroupElement` items (represented as `dict` in JSON)",
        description="Mappings for a concept from the source set",
    )

    source: fhirtypes.Uri = Field(
        None,
        alias="source",
        title="Type `Uri`",
        description="Code System (if value set crosses code systems)",
    )
    source__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_source", title="Extension field for ``source``."
    )

    sourceVersion: fhirtypes.String = Field(
        None,
        alias="sourceVersion",
        title="Type `String`",
        description="Specific version of the  code system",
    )
    sourceVersion__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sourceVersion", title="Extension field for ``sourceVersion``."
    )

    target: fhirtypes.Uri = Field(
        None,
        alias="target",
        title="Type `Uri`",
        description="System of the target (if necessary)",
    )
    target__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_target", title="Extension field for ``target``."
    )

    targetVersion: fhirtypes.String = Field(
        None,
        alias="targetVersion",
        title="Type `String`",
        description="Specific version of the  code system",
    )
    targetVersion__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_targetVersion", title="Extension field for ``targetVersion``."
    )

    unmapped: fhirtypes.ConceptMapGroupUnmappedType = Field(
        None,
        alias="unmapped",
        title="Type `ConceptMapGroupUnmapped` (represented as `dict` in JSON)",
        description="When no match in the mappings",
    )


class ConceptMapGroupElement(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Mappings for a concept from the source set.
    Mappings for an individual concept in the source to one or more concepts in
    the target.
    """

    resource_type = Field("ConceptMapGroupElement", const=True)

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Type `Code`",
        description="Identifies element being mapped",
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    display: fhirtypes.String = Field(
        None, alias="display", title="Type `String`", description="Display for the code"
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_display", title="Extension field for ``display``."
    )

    target: ListType[fhirtypes.ConceptMapGroupElementTargetType] = Field(
        None,
        alias="target",
        title=(
            "List of `ConceptMapGroupElementTarget` items (represented as `dict` in"
            " JSON)"
        ),
        description="Concept in target system for element",
    )


class ConceptMapGroupElementTarget(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Concept in target system for element.
    A concept from the target value set that this concept maps to.
    """

    resource_type = Field("ConceptMapGroupElementTarget", const=True)

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Type `Code`",
        description="Code that identifies the target element",
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Type `String`",
        description="Description of status/issues in mapping",
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    dependsOn: ListType[fhirtypes.ConceptMapGroupElementTargetDependsOnType] = Field(
        None,
        alias="dependsOn",
        title=(
            "List of `ConceptMapGroupElementTargetDependsOn` items (represented as "
            "`dict` in JSON)"
        ),
        description="Other elements required for this mapping (from context)",
    )

    display: fhirtypes.String = Field(
        None, alias="display", title="Type `String`", description="Display for the code"
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_display", title="Extension field for ``display``."
    )

    equivalence: fhirtypes.Code = Field(
        None,
        alias="equivalence",
        title="Type `Code`",
        description=(
            "relatedto | equivalent | equal | wider | subsumes | narrower | "
            "specializes | inexact | unmatched | disjoint"
        ),
    )
    equivalence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_equivalence", title="Extension field for ``equivalence``."
    )

    product: ListType[fhirtypes.ConceptMapGroupElementTargetDependsOnType] = Field(
        None,
        alias="product",
        title=(
            "List of `ConceptMapGroupElementTargetDependsOn` items (represented as "
            "`dict` in JSON)"
        ),
        description="Other concepts that this mapping also produces",
    )


class ConceptMapGroupElementTargetDependsOn(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Other elements required for this mapping (from context).
    A set of additional dependencies for this mapping to hold. This mapping is
    only applicable if the specified element can be resolved, and it has the
    specified value.
    """

    resource_type = Field("ConceptMapGroupElementTargetDependsOn", const=True)

    code: fhirtypes.String = Field(
        ...,
        alias="code",
        title="Type `String`",
        description="Value of the referenced element",
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    display: fhirtypes.String = Field(
        None, alias="display", title="Type `String`", description="Display for the code"
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_display", title="Extension field for ``display``."
    )

    property: fhirtypes.Uri = Field(
        ...,
        alias="property",
        title="Type `Uri`",
        description="Reference to property mapping depends on",
    )
    property__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_property", title="Extension field for ``property``."
    )

    system: fhirtypes.Uri = Field(
        None,
        alias="system",
        title="Type `Uri`",
        description="Code System (if necessary)",
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_system", title="Extension field for ``system``."
    )


class ConceptMapGroupUnmapped(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    When no match in the mappings.
    What to do when there is no match in the mappings in the group.
    """

    resource_type = Field("ConceptMapGroupUnmapped", const=True)

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Type `Code`",
        description="Fixed code when mode = fixed",
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    display: fhirtypes.String = Field(
        None, alias="display", title="Type `String`", description="Display for the code"
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_display", title="Extension field for ``display``."
    )

    mode: fhirtypes.Code = Field(
        ...,
        alias="mode",
        title="Type `Code`",
        description="provided | fixed | other-map",
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_mode", title="Extension field for ``mode``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri`",
        description="Canonical URL for other concept map",
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )
