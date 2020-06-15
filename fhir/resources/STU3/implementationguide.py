# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ImplementationGuide
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class ImplementationGuide(domainresource.DomainResource):
    """ A set of rules about how FHIR is used.
    A set of rules of how FHIR is used to solve a particular problem. This
    resource is used to gather all the parts of an implementation guide into a
    logical whole and to publish a computable definition of all the parts.
    """

    resource_type = Field("ImplementationGuide", const=True)

    binary: ListType[fhirtypes.Uri] = Field(
        None,
        alias="binary",
        title="List of `Uri` items (represented as `dict` in JSON)",
        description="Image, css, script, etc.",
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

    dependency: ListType[fhirtypes.ImplementationGuideDependencyType] = Field(
        None,
        alias="dependency",
        title=(
            "List of `ImplementationGuideDependency` items (represented as `dict` "
            "in JSON)"
        ),
        description="Another Implementation guide this depends on",
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Natural language description of the implementation guide",
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="Type `bool`",
        description="For testing purposes, not real usage",
    )

    fhirVersion: fhirtypes.Id = Field(
        None,
        alias="fhirVersion",
        title="Type `Id` (represented as `dict` in JSON)",
        description="FHIR Version this Implementation Guide targets",
    )

    global_fhir: ListType[fhirtypes.ImplementationGuideGlobalType] = Field(
        None,
        alias="global",
        title=(
            "List of `ImplementationGuideGlobal` items (represented as `dict` in "
            "JSON)"
        ),
        description="Profiles that apply globally",
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Intended jurisdiction for implementation guide (if applicable)",
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this implementation guide (computer friendly)",
    )

    package: ListType[fhirtypes.ImplementationGuidePackageType] = Field(
        None,
        alias="package",
        title=(
            "List of `ImplementationGuidePackage` items (represented as `dict` in "
            "JSON)"
        ),
        description="Group of resources as used in .page.package",
    )

    page: fhirtypes.ImplementationGuidePageType = Field(
        None,
        alias="page",
        title="Type `ImplementationGuidePage` (represented as `dict` in JSON)",
        description="Page/Section in the Guide",
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of the publisher (organization or individual)",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="draft | active | retired | unknown",
    )

    url: fhirtypes.Uri = Field(
        ...,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Logical URI to reference this implementation guide (globally unique)",
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
        description="Business version of the implementation guide",
    )


class ImplementationGuideDependency(backboneelement.BackboneElement):
    """ Another Implementation guide this depends on.
    Another implementation guide that this implementation depends on.
    Typically, an implementation guide uses value sets, profiles etc.defined in
    other implementation guides.
    """

    resource_type = Field("ImplementationGuideDependency", const=True)

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="reference | inclusion",
    )

    uri: fhirtypes.Uri = Field(
        ...,
        alias="uri",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Where to find dependency",
    )


class ImplementationGuideGlobal(backboneelement.BackboneElement):
    """ Profiles that apply globally.
    A set of profiles that all resources covered by this implementation guide
    must conform to.
    """

    resource_type = Field("ImplementationGuideGlobal", const=True)

    profile: fhirtypes.ReferenceType = Field(
        ...,
        alias="profile",
        title=(
            "Type `Reference` referencing `StructureDefinition` (represented as "
            "`dict` in JSON)"
        ),
        description="Profile that all resources must conform to",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Type this profiles applies to",
    )


class ImplementationGuidePackage(backboneelement.BackboneElement):
    """ Group of resources as used in .page.package.
    A logical group of resources. Logical groups can be used when building
    pages.
    """

    resource_type = Field("ImplementationGuidePackage", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Human readable text describing the package",
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name used .page.package",
    )

    resource: ListType[fhirtypes.ImplementationGuidePackageResourceType] = Field(
        ...,
        alias="resource",
        title=(
            "List of `ImplementationGuidePackageResource` items (represented as "
            "`dict` in JSON)"
        ),
        description="Resource in the implementation guide",
    )


class ImplementationGuidePackageResource(backboneelement.BackboneElement):
    """ Resource in the implementation guide.
    A resource that is part of the implementation guide. Conformance resources
    (value set, structure definition, capability statements etc.) are obvious
    candidates for inclusion, but any kind of resource can be included as an
    example resource.
    """

    resource_type = Field("ImplementationGuidePackageResource", const=True)

    acronym: fhirtypes.String = Field(
        None,
        alias="acronym",
        title="Type `String` (represented as `dict` in JSON)",
        description="Short code to identify the resource",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Reason why included in guide",
    )

    example: bool = Field(
        ...,
        alias="example",
        title="Type `bool`",
        description="If not an example, has its normal meaning",
    )

    exampleFor: fhirtypes.ReferenceType = Field(
        None,
        alias="exampleFor",
        title=(
            "Type `Reference` referencing `StructureDefinition` (represented as "
            "`dict` in JSON)"
        ),
        description="Resource this is an example of (if applicable)",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Human Name for the resource",
    )

    sourceReference: fhirtypes.ReferenceType = Field(
        None,
        alias="sourceReference",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Location of the resource",
        one_of_many="source",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    sourceUri: fhirtypes.Uri = Field(
        None,
        alias="sourceUri",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Location of the resource",
        one_of_many="source",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
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
        one_of_many_fields = {"source": ["sourceReference", "sourceUri"]}
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


class ImplementationGuidePage(backboneelement.BackboneElement):
    """ Page/Section in the Guide.
    A page / section in the implementation guide. The root page is the
    implementation guide home page.
    """

    resource_type = Field("ImplementationGuidePage", const=True)

    format: fhirtypes.Code = Field(
        None,
        alias="format",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Format of the page (e.g. html, markdown, etc.)",
    )

    kind: fhirtypes.Code = Field(
        ...,
        alias="kind",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "page | example | list | include | directory | dictionary | toc | "
            "resource"
        ),
    )

    package: ListType[fhirtypes.String] = Field(
        None,
        alias="package",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Name of package to include",
    )

    page: ListType[fhirtypes.ImplementationGuidePageType] = Field(
        None,
        alias="page",
        title=(
            "List of `ImplementationGuidePage` items (represented as `dict` in " "JSON)"
        ),
        description="Nested Pages / Sections",
    )

    source: fhirtypes.Uri = Field(
        ...,
        alias="source",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Where to find that page",
    )

    title: fhirtypes.String = Field(
        ...,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="Short title shown for navigational assistance",
    )

    type: ListType[fhirtypes.Code] = Field(
        None,
        alias="type",
        title="List of `Code` items (represented as `dict` in JSON)",
        description="Kind of resource to include in the list",
    )
