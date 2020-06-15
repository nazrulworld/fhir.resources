# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ImplementationGuide
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class ImplementationGuide(domainresource.DomainResource):
    """ A set of rules about how FHIR is used.
    A set of rules of how a particular interoperability or standards problem is
    solved - typically through the use of FHIR resources. This resource is used
    to gather all the parts of an implementation guide into a logical whole and
    to publish a computable definition of all the parts.
    """

    resource_type = Field("ImplementationGuide", const=True)

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
        description="Date last changed",
    )

    definition: fhirtypes.ImplementationGuideDefinitionType = Field(
        None,
        alias="definition",
        title="Type `ImplementationGuideDefinition` (represented as `dict` in JSON)",
        description="Information needed to build the IG",
    )

    dependsOn: ListType[fhirtypes.ImplementationGuideDependsOnType] = Field(
        None,
        alias="dependsOn",
        title=(
            "List of `ImplementationGuideDependsOn` items (represented as `dict` in"
            " JSON)"
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

    fhirVersion: ListType[fhirtypes.Code] = Field(
        ...,
        alias="fhirVersion",
        title="List of `Code` items (represented as `dict` in JSON)",
        description="FHIR Version(s) this Implementation Guide targets",
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

    license: fhirtypes.Code = Field(
        None,
        alias="license",
        title="Type `Code` (represented as `dict` in JSON)",
        description="SPDX license code for this IG (or not-open-source)",
    )

    manifest: fhirtypes.ImplementationGuideManifestType = Field(
        None,
        alias="manifest",
        title="Type `ImplementationGuideManifest` (represented as `dict` in JSON)",
        description="Information about an assembled IG",
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this implementation guide (computer friendly)",
    )

    packageId: fhirtypes.Id = Field(
        ...,
        alias="packageId",
        title="Type `Id` (represented as `dict` in JSON)",
        description="NPM Package name for IG",
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

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this implementation guide (human friendly)",
    )

    url: fhirtypes.Uri = Field(
        ...,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description=(
            "Canonical identifier for this implementation guide, represented as a "
            "URI (globally unique)"
        ),
    )

    useContext: ListType[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="List of `UsageContext` items (represented as `dict` in JSON)",
        description="The context that the content is intended to support",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String` (represented as `dict` in JSON)",
        description="Business version of the implementation guide",
    )


class ImplementationGuideDefinition(backboneelement.BackboneElement):
    """ Information needed to build the IG.
    The information needed by an IG publisher tool to publish the whole
    implementation guide.
    """

    resource_type = Field("ImplementationGuideDefinition", const=True)

    grouping: ListType[fhirtypes.ImplementationGuideDefinitionGroupingType] = Field(
        None,
        alias="grouping",
        title=(
            "List of `ImplementationGuideDefinitionGrouping` items (represented as "
            "`dict` in JSON)"
        ),
        description="Grouping used to present related resources in the IG",
    )

    page: fhirtypes.ImplementationGuideDefinitionPageType = Field(
        None,
        alias="page",
        title=(
            "Type `ImplementationGuideDefinitionPage` (represented as `dict` in "
            "JSON)"
        ),
        description="Page/Section in the Guide",
    )

    parameter: ListType[fhirtypes.ImplementationGuideDefinitionParameterType] = Field(
        None,
        alias="parameter",
        title=(
            "List of `ImplementationGuideDefinitionParameter` items (represented as"
            " `dict` in JSON)"
        ),
        description="Defines how IG is built by tools",
    )

    resource: ListType[fhirtypes.ImplementationGuideDefinitionResourceType] = Field(
        ...,
        alias="resource",
        title=(
            "List of `ImplementationGuideDefinitionResource` items (represented as "
            "`dict` in JSON)"
        ),
        description="Resource in the implementation guide",
    )

    template: ListType[fhirtypes.ImplementationGuideDefinitionTemplateType] = Field(
        None,
        alias="template",
        title=(
            "List of `ImplementationGuideDefinitionTemplate` items (represented as "
            "`dict` in JSON)"
        ),
        description="A template for building resources",
    )


class ImplementationGuideDefinitionGrouping(backboneelement.BackboneElement):
    """ Grouping used to present related resources in the IG.
    A logical group of resources. Logical groups can be used when building
    pages.
    """

    resource_type = Field("ImplementationGuideDefinitionGrouping", const=True)

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
        description="Descriptive name for the package",
    )


class ImplementationGuideDefinitionPage(backboneelement.BackboneElement):
    """ Page/Section in the Guide.
    A page / section in the implementation guide. The root page is the
    implementation guide home page.
    """

    resource_type = Field("ImplementationGuideDefinitionPage", const=True)

    generation: fhirtypes.Code = Field(
        ...,
        alias="generation",
        title="Type `Code` (represented as `dict` in JSON)",
        description="html | markdown | xml | generated",
    )

    nameReference: fhirtypes.ReferenceType = Field(
        None,
        alias="nameReference",
        title="Type `Reference` referencing `Binary` (represented as `dict` in JSON)",
        description="Where to find that page",
        one_of_many="name",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    nameUrl: fhirtypes.Url = Field(
        None,
        alias="nameUrl",
        title="Type `Url` (represented as `dict` in JSON)",
        description="Where to find that page",
        one_of_many="name",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    page: ListType[fhirtypes.ImplementationGuideDefinitionPageType] = Field(
        None,
        alias="page",
        title=(
            "List of `ImplementationGuideDefinitionPage` items (represented as "
            "`dict` in JSON)"
        ),
        description="Nested Pages / Sections",
    )

    title: fhirtypes.String = Field(
        ...,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="Short title shown for navigational assistance",
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
        one_of_many_fields = {"name": ["nameReference", "nameUrl"]}
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


class ImplementationGuideDefinitionParameter(backboneelement.BackboneElement):
    """ Defines how IG is built by tools.
    """

    resource_type = Field("ImplementationGuideDefinitionParameter", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "apply | path-resource | path-pages | path-tx-cache | expansion-"
            "parameter | rule-broken-links | generate-xml | generate-json | "
            "generate-turtle | html-template"
        ),
    )

    value: fhirtypes.String = Field(
        ...,
        alias="value",
        title="Type `String` (represented as `dict` in JSON)",
        description="Value for named type",
    )


class ImplementationGuideDefinitionResource(backboneelement.BackboneElement):
    """ Resource in the implementation guide.
    A resource that is part of the implementation guide. Conformance resources
    (value set, structure definition, capability statements etc.) are obvious
    candidates for inclusion, but any kind of resource can be included as an
    example resource.
    """

    resource_type = Field("ImplementationGuideDefinitionResource", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Reason why included in guide",
    )

    exampleBoolean: bool = Field(
        None,
        alias="exampleBoolean",
        title="Type `bool`",
        description="Is an example/What is this an example of?",
        one_of_many="example",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    exampleCanonical: fhirtypes.Canonical = Field(
        None,
        alias="exampleCanonical",
        title=(
            "Type `Canonical` referencing `StructureDefinition` (represented as "
            "`dict` in JSON)"
        ),
        description="Is an example/What is this an example of?",
        one_of_many="example",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fhirVersion: ListType[fhirtypes.Code] = Field(
        None,
        alias="fhirVersion",
        title="List of `Code` items (represented as `dict` in JSON)",
        description="Versions this applies to (if different to IG)",
    )

    groupingId: fhirtypes.Id = Field(
        None,
        alias="groupingId",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Grouping this is part of",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Human Name for the resource",
    )

    reference: fhirtypes.ReferenceType = Field(
        ...,
        alias="reference",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Location of the resource",
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
        one_of_many_fields = {"example": ["exampleBoolean", "exampleCanonical"]}
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


class ImplementationGuideDefinitionTemplate(backboneelement.BackboneElement):
    """ A template for building resources.
    """

    resource_type = Field("ImplementationGuideDefinitionTemplate", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Type of template specified",
    )

    scope: fhirtypes.String = Field(
        None,
        alias="scope",
        title="Type `String` (represented as `dict` in JSON)",
        description="The scope in which the template applies",
    )

    source: fhirtypes.String = Field(
        ...,
        alias="source",
        title="Type `String` (represented as `dict` in JSON)",
        description="The source location for the template",
    )


class ImplementationGuideDependsOn(backboneelement.BackboneElement):
    """ Another Implementation guide this depends on.
    Another implementation guide that this implementation depends on.
    Typically, an implementation guide uses value sets, profiles etc.defined in
    other implementation guides.
    """

    resource_type = Field("ImplementationGuideDependsOn", const=True)

    packageId: fhirtypes.Id = Field(
        None,
        alias="packageId",
        title="Type `Id` (represented as `dict` in JSON)",
        description="NPM Package name for IG this depends on",
    )

    uri: fhirtypes.Canonical = Field(
        ...,
        alias="uri",
        title=(
            "Type `Canonical` referencing `ImplementationGuide` (represented as "
            "`dict` in JSON)"
        ),
        description="Identity of the IG that this depends on",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String` (represented as `dict` in JSON)",
        description="Version of the IG",
    )


class ImplementationGuideGlobal(backboneelement.BackboneElement):
    """ Profiles that apply globally.
    A set of profiles that all resources covered by this implementation guide
    must conform to.
    """

    resource_type = Field("ImplementationGuideGlobal", const=True)

    profile: fhirtypes.Canonical = Field(
        ...,
        alias="profile",
        title=(
            "Type `Canonical` referencing `StructureDefinition` (represented as "
            "`dict` in JSON)"
        ),
        description="Profile that all resources must conform to",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Type this profile applies to",
    )


class ImplementationGuideManifest(backboneelement.BackboneElement):
    """ Information about an assembled IG.
    Information about an assembled implementation guide, created by the
    publication tooling.
    """

    resource_type = Field("ImplementationGuideManifest", const=True)

    image: ListType[fhirtypes.String] = Field(
        None,
        alias="image",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Image within the IG",
    )

    other: ListType[fhirtypes.String] = Field(
        None,
        alias="other",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Additional linkable file in IG",
    )

    page: ListType[fhirtypes.ImplementationGuideManifestPageType] = Field(
        None,
        alias="page",
        title=(
            "List of `ImplementationGuideManifestPage` items (represented as `dict`"
            " in JSON)"
        ),
        description="HTML page within the parent IG",
    )

    rendering: fhirtypes.Url = Field(
        None,
        alias="rendering",
        title="Type `Url` (represented as `dict` in JSON)",
        description="Location of rendered implementation guide",
    )

    resource: ListType[fhirtypes.ImplementationGuideManifestResourceType] = Field(
        ...,
        alias="resource",
        title=(
            "List of `ImplementationGuideManifestResource` items (represented as "
            "`dict` in JSON)"
        ),
        description="Resource in the implementation guide",
    )


class ImplementationGuideManifestPage(backboneelement.BackboneElement):
    """ HTML page within the parent IG.
    Information about a page within the IG.
    """

    resource_type = Field("ImplementationGuideManifestPage", const=True)

    anchor: ListType[fhirtypes.String] = Field(
        None,
        alias="anchor",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Anchor available on the page",
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="HTML page name",
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="Title of the page, for references",
    )


class ImplementationGuideManifestResource(backboneelement.BackboneElement):
    """ Resource in the implementation guide.
    A resource that is part of the implementation guide. Conformance resources
    (value set, structure definition, capability statements etc.) are obvious
    candidates for inclusion, but any kind of resource can be included as an
    example resource.
    """

    resource_type = Field("ImplementationGuideManifestResource", const=True)

    exampleBoolean: bool = Field(
        None,
        alias="exampleBoolean",
        title="Type `bool`",
        description="Is an example/What is this an example of?",
        one_of_many="example",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    exampleCanonical: fhirtypes.Canonical = Field(
        None,
        alias="exampleCanonical",
        title=(
            "Type `Canonical` referencing `StructureDefinition` (represented as "
            "`dict` in JSON)"
        ),
        description="Is an example/What is this an example of?",
        one_of_many="example",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    reference: fhirtypes.ReferenceType = Field(
        ...,
        alias="reference",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Location of the resource",
    )

    relativePath: fhirtypes.Url = Field(
        None,
        alias="relativePath",
        title="Type `Url` (represented as `dict` in JSON)",
        description="Relative path for page in IG",
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
        one_of_many_fields = {"example": ["exampleBoolean", "exampleCanonical"]}
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
