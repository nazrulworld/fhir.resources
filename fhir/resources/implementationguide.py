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
from typing import Union

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class ImplementationGuide(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A set of rules about how FHIR is used.
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
        title="Type `Markdown`",
        description="Use and/or publishing restrictions",
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    date: fhirtypes.DateTime = Field(
        None, alias="date", title="Type `DateTime`", description="Date last changed"
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
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
        title="Type `Markdown`",
        description="Natural language description of the implementation guide",
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

    fhirVersion: ListType[fhirtypes.Code] = Field(
        ...,
        alias="fhirVersion",
        title="List of `Code` items",
        description="FHIR Version(s) this Implementation Guide targets",
    )
    fhirVersion__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_fhirVersion", title="Extension field for ``fhirVersion``.")

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
        title="Type `Code`",
        description="SPDX license code for this IG (or not-open-source)",
    )
    license__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_license", title="Extension field for ``license``."
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
        title="Type `String`",
        description="Name for this implementation guide (computer friendly)",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    packageId: fhirtypes.Id = Field(
        ..., alias="packageId", title="Type `Id`", description="NPM Package name for IG"
    )
    packageId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_packageId", title="Extension field for ``packageId``."
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
        description="Name for this implementation guide (human friendly)",
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.Uri = Field(
        ...,
        alias="url",
        title="Type `Uri`",
        description=(
            "Canonical identifier for this implementation guide, represented as a "
            "URI (globally unique)"
        ),
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
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
        title="Type `String`",
        description="Business version of the implementation guide",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class ImplementationGuideDefinition(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information needed to build the IG.
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Grouping used to present related resources in the IG.
    A logical group of resources. Logical groups can be used when building
    pages.
    """

    resource_type = Field("ImplementationGuideDefinitionGrouping", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Human readable text describing the package",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String`",
        description="Descriptive name for the package",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )


class ImplementationGuideDefinitionPage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Page/Section in the Guide.
    A page / section in the implementation guide. The root page is the
    implementation guide home page.
    """

    resource_type = Field("ImplementationGuideDefinitionPage", const=True)

    generation: fhirtypes.Code = Field(
        ...,
        alias="generation",
        title="Type `Code`",
        description="html | markdown | xml | generated",
    )
    generation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_generation", title="Extension field for ``generation``."
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
        title="Type `Url`",
        description="Where to find that page",
        one_of_many="name",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    nameUrl__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_nameUrl", title="Extension field for ``nameUrl``."
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
        title="Type `String`",
        description="Short title shown for navigational assistance",
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Defines how IG is built by tools.
    """

    resource_type = Field("ImplementationGuideDefinitionParameter", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Type `Code`",
        description=(
            "apply | path-resource | path-pages | path-tx-cache | expansion-"
            "parameter | rule-broken-links | generate-xml | generate-json | "
            "generate-turtle | html-template"
        ),
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    value: fhirtypes.String = Field(
        ..., alias="value", title="Type `String`", description="Value for named type"
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )


class ImplementationGuideDefinitionResource(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Resource in the implementation guide.
    A resource that is part of the implementation guide. Conformance resources
    (value set, structure definition, capability statements etc.) are obvious
    candidates for inclusion, but any kind of resource can be included as an
    example resource.
    """

    resource_type = Field("ImplementationGuideDefinitionResource", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Reason why included in guide",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    exampleBoolean: bool = Field(
        None,
        alias="exampleBoolean",
        title="Type `bool`",
        description="Is an example/What is this an example of?",
        one_of_many="example",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    exampleBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_exampleBoolean", title="Extension field for ``exampleBoolean``."
    )

    exampleCanonical: fhirtypes.Canonical = Field(
        None,
        alias="exampleCanonical",
        title="Type `Canonical` referencing `StructureDefinition`",
        description="Is an example/What is this an example of?",
        one_of_many="example",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    exampleCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_exampleCanonical",
        title="Extension field for ``exampleCanonical``.",
    )

    fhirVersion: ListType[fhirtypes.Code] = Field(
        None,
        alias="fhirVersion",
        title="List of `Code` items",
        description="Versions this applies to (if different to IG)",
    )
    fhirVersion__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_fhirVersion", title="Extension field for ``fhirVersion``.")

    groupingId: fhirtypes.Id = Field(
        None,
        alias="groupingId",
        title="Type `Id`",
        description="Grouping this is part of",
    )
    groupingId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_groupingId", title="Extension field for ``groupingId``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`",
        description="Human Name for the resource",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A template for building resources.
    """

    resource_type = Field("ImplementationGuideDefinitionTemplate", const=True)

    code: fhirtypes.Code = Field(
        ..., alias="code", title="Type `Code`", description="Type of template specified"
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    scope: fhirtypes.String = Field(
        None,
        alias="scope",
        title="Type `String`",
        description="The scope in which the template applies",
    )
    scope__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_scope", title="Extension field for ``scope``."
    )

    source: fhirtypes.String = Field(
        ...,
        alias="source",
        title="Type `String`",
        description="The source location for the template",
    )
    source__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_source", title="Extension field for ``source``."
    )


class ImplementationGuideDependsOn(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Another Implementation guide this depends on.
    Another implementation guide that this implementation depends on.
    Typically, an implementation guide uses value sets, profiles etc.defined in
    other implementation guides.
    """

    resource_type = Field("ImplementationGuideDependsOn", const=True)

    packageId: fhirtypes.Id = Field(
        None,
        alias="packageId",
        title="Type `Id`",
        description="NPM Package name for IG this depends on",
    )
    packageId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_packageId", title="Extension field for ``packageId``."
    )

    uri: fhirtypes.Canonical = Field(
        ...,
        alias="uri",
        title="Type `Canonical` referencing `ImplementationGuide`",
        description="Identity of the IG that this depends on",
    )
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_uri", title="Extension field for ``uri``."
    )

    version: fhirtypes.String = Field(
        None, alias="version", title="Type `String`", description="Version of the IG"
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class ImplementationGuideGlobal(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Profiles that apply globally.
    A set of profiles that all resources covered by this implementation guide
    must conform to.
    """

    resource_type = Field("ImplementationGuideGlobal", const=True)

    profile: fhirtypes.Canonical = Field(
        ...,
        alias="profile",
        title="Type `Canonical` referencing `StructureDefinition`",
        description="Profile that all resources must conform to",
    )
    profile__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_profile", title="Extension field for ``profile``."
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code`",
        description="Type this profile applies to",
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )


class ImplementationGuideManifest(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about an assembled IG.
    Information about an assembled implementation guide, created by the
    publication tooling.
    """

    resource_type = Field("ImplementationGuideManifest", const=True)

    image: ListType[fhirtypes.String] = Field(
        None,
        alias="image",
        title="List of `String` items",
        description="Image within the IG",
    )
    image__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_image", title="Extension field for ``image``."
    )

    other: ListType[fhirtypes.String] = Field(
        None,
        alias="other",
        title="List of `String` items",
        description="Additional linkable file in IG",
    )
    other__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_other", title="Extension field for ``other``."
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
        title="Type `Url`",
        description="Location of rendered implementation guide",
    )
    rendering__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_rendering", title="Extension field for ``rendering``."
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    HTML page within the parent IG.
    Information about a page within the IG.
    """

    resource_type = Field("ImplementationGuideManifestPage", const=True)

    anchor: ListType[fhirtypes.String] = Field(
        None,
        alias="anchor",
        title="List of `String` items",
        description="Anchor available on the page",
    )
    anchor__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_anchor", title="Extension field for ``anchor``."
    )

    name: fhirtypes.String = Field(
        ..., alias="name", title="Type `String`", description="HTML page name"
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String`",
        description="Title of the page, for references",
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )


class ImplementationGuideManifestResource(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Resource in the implementation guide.
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
    exampleBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_exampleBoolean", title="Extension field for ``exampleBoolean``."
    )

    exampleCanonical: fhirtypes.Canonical = Field(
        None,
        alias="exampleCanonical",
        title="Type `Canonical` referencing `StructureDefinition`",
        description="Is an example/What is this an example of?",
        one_of_many="example",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    exampleCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_exampleCanonical",
        title="Extension field for ``exampleCanonical``.",
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
        title="Type `Url`",
        description="Relative path for page in IG",
    )
    relativePath__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_relativePath", title="Extension field for ``relativePath``."
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
