# -*- coding: utf-8 -*-
"""
Profile: https://www.hl7.org/fhir/DSTU2/implementationguide.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic.v1 import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class ImplementationGuide(domainresource.DomainResource):
    """A set of rules about how FHIR is used.

    A set of rules of how a particular interoperability or standards problem is
    solved - typically through the use of FHIR resources. This resource is used
    to gather all the parts of an implementation guide into a logical whole and
    to publish a computable definition of all the parts.
    """

    resource_type = Field("ImplementationGuide", const=True)

    binary: ListType[fhirtypes.Uri] = Field(
        None,
        alias="binary",
        title="List of `uri` items.",
        description="Image, css, script, etc..",
    )

    contact: ListType[fhirtypes.ImplementationGuideContactType] = Field(
        None,
        alias="contact",
        title="Contact details for the publisher",
        description=(
            "Contact details to assist a user in finding and communicating with the"
            " publisher."
        ),
    )

    copyright: fhirtypes.String = Field(
        None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the implementation guide and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the implementation guide."
        ),
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the implementation guide was "
            "published. The date must change when the business version changes and "
            "it must change if the status code changes. In addition, it should "
            "change when the substantive content of the implementation guide "
            "changes."
        ),
    )

    dependency: ListType[fhirtypes.ImplementationGuideDependencyType] = Field(
        None,
        alias="dependency",
        title="Another Implementation guide this depends on",
        description=(
            "Another implementation guide that this implementation depends on. "
            "Typically, an implementation guide uses value sets, profiles "
            "etc.defined in other implementation guides."
        ),
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Natural language description of the implementation guide",
        description=(
            "A free text natural language description of the implementation guide "
            "from a consumer's perspective."
        ),
    )

    experimental: fhirtypes.Boolean = Field(
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this implementation guide is authored"
            " for testing purposes (or education/evaluation/marketing) and is not "
            "intended to be used for genuine usage."
        ),
    )

    fhirVersion: fhirtypes.Id = Field(
        None,
        alias="fhirVersion",
        title="FHIR Version this Implementation Guide targets",
        description=(
            "The version(s) of the FHIR specification that this ImplementationGuide"
            " targets - e.g. describes how to use. The value of this element is the"
            " formal version of the specification, without the revision number, "
            "e.g. [publication].[major].[minor], which is 4.0.1. for this version."
        ),
    )

    global_fhir: ListType[fhirtypes.ImplementationGuideGlobalType] = Field(
        None,
        alias="global",
        title="Profiles that apply globally",
        description=(
            "A set of profiles that all resources covered by this implementation "
            "guide must conform to."
        ),
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Name for this implementation guide (computer friendly)",
        description=(
            "A natural language name identifying the implementation guide. This "
            "name should be usable as an identifier for the module by machine "
            "processing applications such as code generation."
        ),
    )

    package: ListType[fhirtypes.ImplementationGuidePackageType] = Field(
        ...,
        alias="package",
        title="List of `ImplementationGuidePackage` items (represented as `dict` in JSON).",
        description="Group of resources as used in .page.package.",
    )

    page: fhirtypes.ImplementationGuidePageType = Field(
        ...,
        alias="page",
        title="Type `ImplementationGuidePage` (represented as `dict` in JSON).",
        description="Page/Section in the Guide.",
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the organization or individual that published the "
            "implementation guide."
        ),
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="draft | active | retired",
        description=(
            "The status of this implementation guide. Enables tracking the life-"
            "cycle of the content."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired"],
    )

    url: fhirtypes.Uri = Field(
        ...,
        alias="url",
        title=(
            "Canonical identifier for this implementation guide, represented as a "
            "URI (globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this implementation guide "
            "when it is referenced in a specification, model, design or an "
            "instance; also called its canonical identifier. This SHOULD be "
            "globally unique and SHOULD be a literal address at which at which an "
            "authoritative instance of this implementation guide is (or will be) "
            "published. This URL can be the target of a canonical reference. It "
            "SHALL remain the same when the implementation guide is stored on "
            "different servers."
        ),
    )

    useContext: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="useContext",
        title="The context that the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These contexts may be general categories "
            "(gender, age, ...) or may be references to specific programs "
            "(insurance plans, studies, ...) and may be used to assist with "
            "indexing and searching for appropriate implementation guide instances."
        ),
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the implementation guide",
        description=(
            "The identifier that is used to identify this version of the "
            "implementation guide when it is referenced in a specification, model, "
            "design or instance. This is an arbitrary value managed by the "
            "implementation guide author and is not expected to be globally unique."
            " For example, it might be a timestamp (e.g. yyyymmdd) if a managed "
            "version is not available. There is also no expectation that versions "
            "can be placed in a lexicographical sequence."
        ),
    )


class ImplementationGuideContact(backboneelement.BackboneElement):
    """Contact details of the publisher.

    Contacts to assist a user in finding and communicating with the publisher.
    """

    resource_type = Field("ImplementationGuideContact", const=True)

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `str`.",
        description="Name of a individual to contact.",
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="List of `ContactPoint` items (represented as `dict` in JSON).",
        description="Contact details for individual or publisher.",
    )


class ImplementationGuideDependency(backboneelement.BackboneElement):
    """Another Implementation guide this depends on.

    Another implementation guide that this implementation depends on.
    Typically, an implementation guide uses value sets, profiles etc.defined in
    other implementation guides.
    """

    resource_type = Field("ImplementationGuideDependsOn", const=True)

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `str`.",
        description="reference | inclusion.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["reference", "inclusion"],
    )

    uri: fhirtypes.Uri = Field(
        ...,
        alias="uri",
        title="Identity of the IG that this depends on",
        description="A canonical reference to the Implementation guide for the dependency.",
    )


class ImplementationGuideGlobal(backboneelement.BackboneElement):
    """Profiles that apply globally.

    A set of profiles that all resources covered by this implementation guide
    must conform to.
    """

    resource_type = Field("ImplementationGuideGlobal", const=True)

    profile: fhirtypes.ReferenceType = Field(
        ...,
        alias="profile",
        title="Profile that all resources must conform to",
        description="A reference to the profile that all instances must conform to.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureDefinition"],
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type this profile applies to",
        description="The type of resource that all instances must conform to.",
    )


class ImplementationGuidePackage(backboneelement.BackboneElement):
    """Group of resources as used in .page.package.

    A logical group of resources. Logical groups can be used when building
    pages.
    """

    resource_type = Field("ImplementationGuidePackage", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `str`.",
        description="Human readable text describing the package.",
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `str`.",
        description="Name used .page.package.",
    )

    resource: ListType[fhirtypes.ImplementationGuidePackageResourceType] = Field(
        ...,
        alias="resource",
        title=(
            "List of `ImplementationGuidePackageResource` items (represented as `dict` "
            "in JSON)."
        ),
        description="Resource in the implementation guide.",
    )


class ImplementationGuidePackageResource(backboneelement.BackboneElement):
    """Resource in the implementation guide.

    A resource that is part of the implementation guide. Conformance resources
    (value set, structure definition, conformance statements etc.) are obvious
    candidates for inclusion, but any kind of resource can be included as an
    example resource.
    """

    resource_type = Field("ImplementationGuidePackageResource", const=True)

    acronym: fhirtypes.String = Field(
        None,
        alias="acronym",
        title="Type `str`.",
        description="Short code to identify the resource.",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `str`.",
        description="Reason why included in guide.",
    )

    exampleFor: fhirtypes.ReferenceType = Field(
        None,
        alias="exampleFor",
        title=(
            "Type `Reference` referencing `StructureDefinition` (represented as `dict` "
            "in JSON)."
        ),
        description="Resource this is an example of (if applicable).",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureDefinition"],
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `str`.",
        description="Human Name for the resource.",
    )

    purpose: fhirtypes.Code = Field(
        ...,
        alias="purpose",
        title="Type `str`.",
        description=(
            "example | terminology | profile | extension | dictionary | logical."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "example",
            "terminology",
            "profile",
            "extension",
            "dictionary",
            "logical",
        ],
    )

    sourceReference: fhirtypes.ReferenceType = Field(
        None,
        alias="sourceReference",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON).",
        description="Location of the resource.",
        # Choice of Data Types. i.e timing[x]
        one_of_many="source",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    sourceUri: fhirtypes.Uri = Field(
        None,
        alias="sourceUri",
        title="Type `str`.",
        description="Location of the resource.",
        # Choice of Data Types. i.e timing[x]
        one_of_many="source",
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
        one_of_many_fields = {
            "source": ["sourceReference", "sourceUri"],
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


class ImplementationGuidePage(backboneelement.BackboneElement):
    """Page/Section in the Guide.

    A page / section in the implementation guide. The root page is the
    implementation guide home page.
    """

    resource_type = Field("ImplementationGuidePage", const=True)

    format: fhirtypes.Code = Field(
        None,
        alias="format",
        title="Type `str`.",
        description="Format of the page (e.g. html, markdown, etc.).",
    )

    kind: fhirtypes.Code = Field(
        ...,
        alias="kind",
        title="Type `str`.",
        description=(
            "page | example | list | include | directory | dictionary | toc | resource."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "page",
            "example",
            "list",
            "include",
            "directory",
            "dictionary",
            "toc",
            "resource",
        ],
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `str`.",
        description="Short name shown for navigational assistance.",
    )

    package: ListType[fhirtypes.String] = Field(
        None,
        alias="package",
        title="List of `str` items.",
        description="Name of package to include.",
    )

    page: ListType[fhirtypes.ImplementationGuidePageType] = Field(
        None,
        alias="page",
        title=(
            "List of `ImplementationGuidePage` items (represented as `dict` in JSON)."
        ),
        description="Nested Pages / Sections.",
    )

    source: fhirtypes.Uri = Field(
        ...,
        alias="source",
        title="Type `Uri`.",
        description="Where to find that page.",
    )

    type: ListType[fhirtypes.Code] = Field(
        None,
        alias="type",
        title="List of `Code` items.",
        description="Kind of resource to include in the list.",
    )
