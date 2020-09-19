# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ConceptMap
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import fhirtypes
from .backboneelement import BackboneElement
from .domainresource import DomainResource


class ConceptMap(DomainResource):
    """A map from one set of concepts to one or more other concepts.

    A statement of relationships from one set of concepts to one or more other
    concepts - either code systems or data elements, or classes in class
    models.
    """

    resource_type = Field("ConceptMap", const=True)

    contact: ListType[fhirtypes.ConceptMapContactType] = Field(
        None,
        alias="contact",
        title="List of `ConceptMapContact` items (represented as `dict` in JSON).",
        description="Contact details of the publisher.",
    )

    copyright: fhirtypes.String = Field(
        None,
        alias="copyright",
        title="Type `str`.",
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
        description="Human language description of the concept map.",
    )

    element: ListType[fhirtypes.ConceptMapElementType] = Field(
        None,
        alias="element",
        title="List of `ConceptMapElement` items (represented as `dict` in JSON).",
        description="Mappings for a concept from the source set.",
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="Type `bool`.",
        description="If for testing purposes, not real usage.",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON).",
        description="Additional identifier for the concept map.",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`.",
        description="Informal name for this concept map.",
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

    sourceReference: fhirtypes.ReferenceType = Field(
        None,
        alias="sourceReference",
        title=(
            "Type `Reference` referencing `ValueSet, StructureDefinition`"
            " (represented as `dict` in JSON)."
        ),
        description="Identifies the source of the concepts which are being mapped.",
        one_of_many="source",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    sourceUri: fhirtypes.Uri = Field(
        None,
        alias="sourceUri",
        title="Type `Uri.",
        description="Identifies the source of the concepts which are being mapped.",
        one_of_many="source",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code.",
        description="draft | active | retired.",
    )

    targetReference: fhirtypes.ReferenceType = Field(
        None,
        alias="targetReference",
        title=(
            "Type `Reference` referencing `ValueSet, "
            "StructureDefinition` (represented as `dict` in JSON)."
        ),
        description="Provides context to the mappings.",
        one_of_many="target",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    targetUri: fhirtypes.Uri = Field(
        None,
        alias="targetUri",
        title="Type `Uri.",
        description="Provides context to the mappings.",
        one_of_many="target",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri.",
        description="Globally unique logical id for concept map.",
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
        title="Type `String.",
        description="Logical id for this version of the concept map.",
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


class ConceptMapContact(BackboneElement):
    """Contact details of the publisher.

    Contacts to assist a user in finding and communicating with the publisher.
    """

    resource_type = Field("ConceptMapContact", const=True)

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String.",
        description="Name of a individual to contact.",
    )
    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="List of `ContactPoint` items (represented as `dict` in JSON).",
        description="Contact details for individual or publisher.",
    )


class ConceptMapElement(BackboneElement):
    """Mappings for a concept from the source set.

    Mappings for an individual concept in the source to one or more concepts in
    the target.
    """

    resource_type = Field("ConceptMapElement", const=True)
    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Type `Code.",
        description="Identifies element being mapped.",
    )
    codeSystem: fhirtypes.Uri = Field(
        None,
        alias="codeSystem",
        title="Type `Uri.",
        description="Identifies element being mapped.",
    )

    target: ListType[fhirtypes.ConceptMapElementTargetType] = Field(
        None,
        alias="target",
        title="List of `ConceptMapElementTarget` items (represented as `dict` in JSON).",
        description="Concept in target system for element.",
    )


class ConceptMapElementTarget(BackboneElement):
    """Concept in target system for element.

    A concept from the target value set that this concept maps to.
    """

    resource_type = Field("ConceptMapElementTarget", const=True)
    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Type `Code.",
        description="Code that identifies the target element.",
    )
    codeSystem: fhirtypes.Uri = Field(
        None,
        alias="codeSystem",
        title="Type `Uri.",
        description="System of the target (if necessary).",
    )

    comments: fhirtypes.String = Field(
        None,
        alias="comments",
        title="Type `Str.",
        description="System of the target (if necessary).",
    )

    dependsOn: ListType[fhirtypes.ConceptMapElementTargetDependsOnType] = Field(
        None,
        alias="dependsOn",
        title=(
            "List of `ConceptMapElementTargetDependsOn` "
            "items (represented as `dict` in JSON)."
        ),
        description="Other elements required for this mapping (from context).",
    )

    equivalence: fhirtypes.Code = Field(
        None,
        alias="equivalence",
        title="Type `Code.",
        description=(
            "equivalent | equal | wider | subsumes | narrower | specializes |"
            "inexact | unmatched | disjoint."
        ),
    )
    product: ListType[fhirtypes.ConceptMapElementTargetDependsOnType] = Field(
        None,
        alias="dependsOn",
        title=(
            "List of `ConceptMapElementTargetDependsOn` "
            "items (represented as `dict` in JSON)."
        ),
        description="Other elements required for this mapping (from context).",
    )


class ConceptMapElementTargetDependsOn(BackboneElement):
    """Other elements required for this mapping (from context).

    A set of additional dependencies for this mapping to hold. This mapping is
    only applicable if the specified element can be resolved, and it has the
    specified value.
    """

    resource_type = Field("ConceptMapElementTargetDependsOn", const=True)

    code: fhirtypes.String = Field(
        None,
        alias="code",
        title="Type `String.",
        description="Value of the referenced element.",
    )
    codeSystem: fhirtypes.Uri = Field(
        None,
        alias="codeSystem",
        title="Type `Uri.",
        description="Code System (if necessary).",
    )
    element: fhirtypes.Uri = Field(
        None,
        alias="element",
        title="Type `Uri.",
        description="Reference to element/field/ValueSet mapping depends on.",
    )
