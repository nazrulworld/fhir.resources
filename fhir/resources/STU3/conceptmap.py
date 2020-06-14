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
    """ A map from one set of concepts to one or more other concepts.
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
        description="Natural language description of the concept map",
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="Type `bool`",
        description="For testing purposes, not real usage",
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
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this concept map (computer friendly)",
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
        description="Why this concept map is defined",
    )

    sourceReference: fhirtypes.ReferenceType = Field(
        None,
        alias="sourceReference",
        title="Type `Reference` referencing `ValueSet` (represented as `dict` in JSON)",
        description="Identifies the source of the concepts which are being mapped",
        one_of_many="source",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    sourceUri: fhirtypes.Uri = Field(
        None,
        alias="sourceUri",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Identifies the source of the concepts which are being mapped",
        one_of_many="source",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="draft | active | retired | unknown",
    )

    targetReference: fhirtypes.ReferenceType = Field(
        None,
        alias="targetReference",
        title="Type `Reference` referencing `ValueSet` (represented as `dict` in JSON)",
        description="Provides context to the mappings",
        one_of_many="target",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    targetUri: fhirtypes.Uri = Field(
        None,
        alias="targetUri",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Provides context to the mappings",
        one_of_many="target",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this concept map (human friendly)",
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Logical URI to reference this concept map (globally unique)",
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
        description="Business version of the concept map",
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
            "source": ["sourceReference", "sourceUri",],
            "target": ["targetReference", "targetUri",],
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
    """ Same source and target systems.
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
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Code System (if value set crosses code systems)",
    )

    sourceVersion: fhirtypes.String = Field(
        None,
        alias="sourceVersion",
        title="Type `String` (represented as `dict` in JSON)",
        description="Specific version of the  code system",
    )

    target: fhirtypes.Uri = Field(
        None,
        alias="target",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="System of the target (if necessary)",
    )

    targetVersion: fhirtypes.String = Field(
        None,
        alias="targetVersion",
        title="Type `String` (represented as `dict` in JSON)",
        description="Specific version of the  code system",
    )

    unmapped: fhirtypes.ConceptMapGroupUnmappedType = Field(
        None,
        alias="unmapped",
        title="Type `ConceptMapGroupUnmapped` (represented as `dict` in JSON)",
        description="When no match in the mappings",
    )


class ConceptMapGroupElement(backboneelement.BackboneElement):
    """ Mappings for a concept from the source set.
    Mappings for an individual concept in the source to one or more concepts in
    the target.
    """

    resource_type = Field("ConceptMapGroupElement", const=True)

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Identifies element being mapped",
    )

    display: fhirtypes.String = Field(
        None,
        alias="display",
        title="Type `String` (represented as `dict` in JSON)",
        description="Display for the code",
    )

    target: ListType[fhirtypes.ConceptMapGroupElementTargetType] = Field(
        None,
        alias="target",
        title="List of `ConceptMapGroupElementTarget` items (represented as `dict` in JSON)",
        description="Concept in target system for element",
    )


class ConceptMapGroupElementTarget(backboneelement.BackboneElement):
    """ Concept in target system for element.
    A concept from the target value set that this concept maps to.
    """

    resource_type = Field("ConceptMapGroupElementTarget", const=True)

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Code that identifies the target element",
    )

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Type `String` (represented as `dict` in JSON)",
        description="Description of status/issues in mapping",
    )

    dependsOn: ListType[fhirtypes.ConceptMapGroupElementTargetDependsOnType] = Field(
        None,
        alias="dependsOn",
        title="List of `ConceptMapGroupElementTargetDependsOn` items (represented as `dict` in JSON)",
        description="Other elements required for this mapping (from context)",
    )

    display: fhirtypes.String = Field(
        None,
        alias="display",
        title="Type `String` (represented as `dict` in JSON)",
        description="Display for the code",
    )

    equivalence: fhirtypes.Code = Field(
        None,
        alias="equivalence",
        title="Type `Code` (represented as `dict` in JSON)",
        description="relatedto | equivalent | equal | wider | subsumes | narrower | specializes | inexact | unmatched | disjoint",
    )

    product: ListType[fhirtypes.ConceptMapGroupElementTargetDependsOnType] = Field(
        None,
        alias="product",
        title="List of `ConceptMapGroupElementTargetDependsOn` items (represented as `dict` in JSON)",
        description="Other concepts that this mapping also produces",
    )


class ConceptMapGroupElementTargetDependsOn(backboneelement.BackboneElement):
    """ Other elements required for this mapping (from context).
    A set of additional dependencies for this mapping to hold. This mapping is
    only applicable if the specified element can be resolved, and it has the
    specified value.
    """

    resource_type = Field("ConceptMapGroupElementTargetDependsOn", const=True)

    code: fhirtypes.String = Field(
        ...,
        alias="code",
        title="Type `String` (represented as `dict` in JSON)",
        description="Value of the referenced element",
    )

    display: fhirtypes.String = Field(
        None,
        alias="display",
        title="Type `String` (represented as `dict` in JSON)",
        description="Display for the code",
    )

    property: fhirtypes.Uri = Field(
        ...,
        alias="property",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Reference to property mapping depends on",
    )

    system: fhirtypes.Uri = Field(
        None,
        alias="system",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Code System (if necessary)",
    )


class ConceptMapGroupUnmapped(backboneelement.BackboneElement):
    """ When no match in the mappings.
    What to do when there is no match in the mappings in the group.
    """

    resource_type = Field("ConceptMapGroupUnmapped", const=True)

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Fixed code when mode = fixed",
    )

    display: fhirtypes.String = Field(
        None,
        alias="display",
        title="Type `String` (represented as `dict` in JSON)",
        description="Display for the code",
    )

    mode: fhirtypes.Code = Field(
        ...,
        alias="mode",
        title="Type `Code` (represented as `dict` in JSON)",
        description="provided | fixed | other-map",
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Canonical URL for other concept map",
    )
