# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ImplementationGuide
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class ImplementationGuide(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A set of rules about how FHIR is used.
    A set of rules of how a particular interoperability or standards problem is
    solved - typically through the use of FHIR resources. This resource is used
    to gather all the parts of an implementation guide into a logical whole and
    to publish a computable definition of all the parts.
    """

    resource_type = Field("ImplementationGuide", const=True)

    contact: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="Contact details for the publisher",
        description=(
            "Contact details to assist a user in finding and communicating with the"
            " publisher."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the implementation guide and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the implementation guide."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
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
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    definition: fhirtypes.ImplementationGuideDefinitionType = Field(
        None,
        alias="definition",
        title="Information needed to build the IG",
        description=(
            "The information needed by an IG publisher tool to publish the whole "
            "implementation guide."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    dependsOn: typing.List[fhirtypes.ImplementationGuideDependsOnType] = Field(
        None,
        alias="dependsOn",
        title="Another Implementation guide this depends on",
        description=(
            "Another implementation guide that this implementation depends on. "
            "Typically, an implementation guide uses value sets, profiles "
            "etc.defined in other implementation guides."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Natural language description of the implementation guide",
        description=(
            "A free text natural language description of the implementation guide "
            "from a consumer's perspective."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this implementation guide is authored"
            " for testing purposes (or education/evaluation/marketing) and is not "
            "intended to be used for genuine usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    fhirVersion: typing.List[typing.Optional[fhirtypes.Code]] = Field(
        None,
        alias="fhirVersion",
        title="FHIR Version(s) this Implementation Guide targets",
        description=(
            "The version(s) of the FHIR specification that this ImplementationGuide"
            " targets - e.g. describes how to use. The value of this element is the"
            " formal version of the specification, without the revision number, "
            "e.g. [publication].[major].[minor], which is 4.3.0 for this version."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    fhirVersion__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_fhirVersion", title="Extension field for ``fhirVersion``.")

    global_fhir: typing.List[fhirtypes.ImplementationGuideGlobalType] = Field(
        None,
        alias="global",
        title="Profiles that apply globally",
        description=(
            "A set of profiles that all resources covered by this implementation "
            "guide must conform to."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for implementation guide (if applicable)",
        description=(
            "A legal or geographic region in which the implementation guide is "
            "intended to be used."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    license: fhirtypes.Code = Field(
        None,
        alias="license",
        title="SPDX license code for this IG (or not-open-source)",
        description=(
            "The license that applies to this Implementation Guide, using an SPDX "
            "license code, or 'not-open-source'."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    license__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_license", title="Extension field for ``license``."
    )

    manifest: fhirtypes.ImplementationGuideManifestType = Field(
        None,
        alias="manifest",
        title="Information about an assembled IG",
        description=(
            "Information about an assembled implementation guide, created by the "
            "publication tooling."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name for this implementation guide (computer friendly)",
        description=(
            "A natural language name identifying the implementation guide. This "
            "name should be usable as an identifier for the module by machine "
            "processing applications such as code generation."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    packageId: fhirtypes.Id = Field(
        None,
        alias="packageId",
        title="NPM Package name for IG",
        description=(
            "The NPM package name for this Implementation Guide, used in the NPM "
            "package distribution, which is the primary mechanism by which FHIR "
            "based tooling manages IG dependencies. This value must be globally "
            "unique, and should be assigned with care."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    packageId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_packageId", title="Extension field for ``packageId``."
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the organization or individual that published the "
            "implementation guide."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this implementation guide. Enables tracking the life-"
            "cycle of the content."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired", "unknown"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Name for this implementation guide (human friendly)",
        description=(
            "A short, descriptive, user-friendly title for the implementation " "guide."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.Uri = Field(
        None,
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
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    useContext: typing.List[fhirtypes.UsageContextType] = Field(
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
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImplementationGuide`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "url",
            "version",
            "name",
            "title",
            "status",
            "experimental",
            "date",
            "publisher",
            "contact",
            "description",
            "useContext",
            "jurisdiction",
            "copyright",
            "packageId",
            "license",
            "fhirVersion",
            "dependsOn",
            "global",
            "definition",
            "manifest",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2146(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("fhirVersion", "fhirVersion__ext"),
            ("name", "name__ext"),
            ("packageId", "packageId__ext"),
            ("status", "status__ext"),
            ("url", "url__ext"),
        ]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class ImplementationGuideDefinition(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information needed to build the IG.
    The information needed by an IG publisher tool to publish the whole
    implementation guide.
    """

    resource_type = Field("ImplementationGuideDefinition", const=True)

    grouping: typing.List[fhirtypes.ImplementationGuideDefinitionGroupingType] = Field(
        None,
        alias="grouping",
        title="Grouping used to present related resources in the IG",
        description=(
            "A logical group of resources. Logical groups can be used when building"
            " pages."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    page: fhirtypes.ImplementationGuideDefinitionPageType = Field(
        None,
        alias="page",
        title="Page/Section in the Guide",
        description=(
            "A page / section in the implementation guide. The root page is the "
            "implementation guide home page."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    parameter: typing.List[
        fhirtypes.ImplementationGuideDefinitionParameterType
    ] = Field(
        None,
        alias="parameter",
        title="Defines how IG is built by tools",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    resource: typing.List[fhirtypes.ImplementationGuideDefinitionResourceType] = Field(
        ...,
        alias="resource",
        title="Resource in the implementation guide",
        description=(
            "A resource that is part of the implementation guide. Conformance "
            "resources (value set, structure definition, capability statements "
            "etc.) are obvious candidates for inclusion, but any kind of resource "
            "can be included as an example resource."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    template: typing.List[fhirtypes.ImplementationGuideDefinitionTemplateType] = Field(
        None,
        alias="template",
        title="A template for building resources",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImplementationGuideDefinition`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "grouping",
            "resource",
            "page",
            "parameter",
            "template",
        ]


class ImplementationGuideDefinitionGrouping(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
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
        title="Human readable text describing the package",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Descriptive name for the package",
        description=(
            "The human-readable title to display for the package of resources when "
            "rendering the implementation guide."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImplementationGuideDefinitionGrouping`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "name", "description"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_4024(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("name", "name__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class ImplementationGuideDefinitionPage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Page/Section in the Guide.
    A page / section in the implementation guide. The root page is the
    implementation guide home page.
    """

    resource_type = Field("ImplementationGuideDefinitionPage", const=True)

    generation: fhirtypes.Code = Field(
        None,
        alias="generation",
        title="html | markdown | xml | generated",
        description="A code that indicates how the page is generated.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["html", "markdown", "xml", "generated"],
    )
    generation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_generation", title="Extension field for ``generation``."
    )

    nameReference: fhirtypes.ReferenceType = Field(
        None,
        alias="nameReference",
        title="Where to find that page",
        description="The source address for the page.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e name[x]
        one_of_many="name",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Binary"],
    )

    nameUrl: fhirtypes.Url = Field(
        None,
        alias="nameUrl",
        title="Where to find that page",
        description="The source address for the page.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e name[x]
        one_of_many="name",
        one_of_many_required=True,
    )
    nameUrl__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_nameUrl", title="Extension field for ``nameUrl``."
    )

    page: typing.List[fhirtypes.ImplementationGuideDefinitionPageType] = Field(
        None,
        alias="page",
        title="Nested Pages / Sections",
        description="Nested Pages/Sections under this page.",
        # if property is element of this resource.
        element_property=True,
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Short title shown for navigational assistance",
        description=(
            "A short title used to represent this page in navigational structures "
            "such as table of contents, bread crumbs, etc."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImplementationGuideDefinitionPage`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "nameUrl",
            "nameReference",
            "title",
            "generation",
            "page",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3560(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("generation", "generation__ext"), ("title", "title__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3560(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Defines how IG is built by tools.
    """

    resource_type = Field("ImplementationGuideDefinitionParameter", const=True)

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title=(
            "apply | path-resource | path-pages | path-tx-cache | expansion-"
            "parameter | rule-broken-links | generate-xml | generate-json | "
            "generate-turtle | html-template"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "apply",
            "path-resource",
            "path-pages",
            "path-tx-cache",
            "expansion-parameter",
            "rule-broken-links",
            "generate-xml",
            "generate-json",
            "generate-turtle",
            "html-template",
        ],
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="Value for named type",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImplementationGuideDefinitionParameter`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "value"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_4121(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("code", "code__ext"), ("value", "value__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class ImplementationGuideDefinitionResource(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
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
        title="Reason why included in guide",
        description=(
            "A description of the reason that a resource has been included in the "
            "implementation guide."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    exampleBoolean: bool = Field(
        None,
        alias="exampleBoolean",
        title="Is an example/What is this an example of?",
        description=(
            "If true or a reference, indicates the resource is an example instance."
            "  If a reference is present, indicates that the example is an example "
            "of the specified profile."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )
    exampleBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_exampleBoolean", title="Extension field for ``exampleBoolean``."
    )

    exampleCanonical: fhirtypes.Canonical = Field(
        None,
        alias="exampleCanonical",
        title="Is an example/What is this an example of?",
        description=(
            "If true or a reference, indicates the resource is an example instance."
            "  If a reference is present, indicates that the example is an example "
            "of the specified profile."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureDefinition"],
    )
    exampleCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_exampleCanonical",
        title="Extension field for ``exampleCanonical``.",
    )

    fhirVersion: typing.List[typing.Optional[fhirtypes.Code]] = Field(
        None,
        alias="fhirVersion",
        title="Versions this applies to (if different to IG)",
        description=(
            "Indicates the FHIR Version(s) this artifact is intended to apply to. "
            "If no versions are specified, the resource is assumed to apply to all "
            "the versions stated in ImplementationGuide.fhirVersion."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    fhirVersion__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_fhirVersion", title="Extension field for ``fhirVersion``.")

    groupingId: fhirtypes.Id = Field(
        None,
        alias="groupingId",
        title="Grouping this is part of",
        description="Reference to the id of the grouping this resource appears in.",
        # if property is element of this resource.
        element_property=True,
    )
    groupingId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_groupingId", title="Extension field for ``groupingId``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Human Name for the resource",
        description=(
            "A human assigned name for the resource. All resources SHOULD have a "
            "name, but the name may be extracted from the resource (e.g. "
            "ValueSet.name)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    reference: fhirtypes.ReferenceType = Field(
        ...,
        alias="reference",
        title="Location of the resource",
        description="Where this resource is found.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImplementationGuideDefinitionResource`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "reference",
            "fhirVersion",
            "name",
            "description",
            "exampleBoolean",
            "exampleCanonical",
            "groupingId",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_4019(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A template for building resources.
    """

    resource_type = Field("ImplementationGuideDefinitionTemplate", const=True)

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Type of template specified",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    scope: fhirtypes.String = Field(
        None,
        alias="scope",
        title="The scope in which the template applies",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    scope__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_scope", title="Extension field for ``scope``."
    )

    source: fhirtypes.String = Field(
        None,
        alias="source",
        title="The source location for the template",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    source__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_source", title="Extension field for ``source``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImplementationGuideDefinitionTemplate`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "source", "scope"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_4007(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("code", "code__ext"), ("source", "source__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class ImplementationGuideDependsOn(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
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
        title="NPM Package name for IG this depends on",
        description=(
            "The NPM package name for the Implementation Guide that this IG depends"
            " on."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    packageId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_packageId", title="Extension field for ``packageId``."
    )

    uri: fhirtypes.Canonical = Field(
        None,
        alias="uri",
        title="Identity of the IG that this depends on",
        description="A canonical reference to the Implementation guide for the dependency.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ImplementationGuide"],
    )
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_uri", title="Extension field for ``uri``."
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Version of the IG",
        description=(
            "The version of the IG that is depended on, when the correct version is"
            " required to understand the IG correctly."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImplementationGuideDependsOn`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "uri", "packageId", "version"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3051(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("uri", "uri__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class ImplementationGuideGlobal(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Profiles that apply globally.
    A set of profiles that all resources covered by this implementation guide
    must conform to.
    """

    resource_type = Field("ImplementationGuideGlobal", const=True)

    profile: fhirtypes.Canonical = Field(
        None,
        alias="profile",
        title="Profile that all resources must conform to",
        description="A reference to the profile that all instances must conform to.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureDefinition"],
    )
    profile__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_profile", title="Extension field for ``profile``."
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="Type this profile applies to",
        description="The type of resource that all instances must conform to.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImplementationGuideGlobal`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "profile"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2746(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("profile", "profile__ext"), ("type", "type__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class ImplementationGuideManifest(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about an assembled IG.
    Information about an assembled implementation guide, created by the
    publication tooling.
    """

    resource_type = Field("ImplementationGuideManifest", const=True)

    image: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="image",
        title="Image within the IG",
        description="Indicates a relative path to an image that exists within the IG.",
        # if property is element of this resource.
        element_property=True,
    )
    image__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_image", title="Extension field for ``image``.")

    other: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="other",
        title="Additional linkable file in IG",
        description=(
            "Indicates the relative path of an additional non-page, non-image file "
            "that is part of the IG - e.g. zip, jar and similar files that could be"
            " the target of a hyperlink in a derived IG."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    other__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_other", title="Extension field for ``other``.")

    page: typing.List[fhirtypes.ImplementationGuideManifestPageType] = Field(
        None,
        alias="page",
        title="HTML page within the parent IG",
        description="Information about a page within the IG.",
        # if property is element of this resource.
        element_property=True,
    )

    rendering: fhirtypes.Url = Field(
        None,
        alias="rendering",
        title="Location of rendered implementation guide",
        description=(
            "A pointer to official web page, PDF or other rendering of the "
            "implementation guide."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    rendering__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_rendering", title="Extension field for ``rendering``."
    )

    resource: typing.List[fhirtypes.ImplementationGuideManifestResourceType] = Field(
        ...,
        alias="resource",
        title="Resource in the implementation guide",
        description=(
            "A resource that is part of the implementation guide. Conformance "
            "resources (value set, structure definition, capability statements "
            "etc.) are obvious candidates for inclusion, but any kind of resource "
            "can be included as an example resource."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImplementationGuideManifest`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "rendering",
            "resource",
            "page",
            "image",
            "other",
        ]


class ImplementationGuideManifestPage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    HTML page within the parent IG.
    Information about a page within the IG.
    """

    resource_type = Field("ImplementationGuideManifestPage", const=True)

    anchor: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="anchor",
        title="Anchor available on the page",
        description="The name of an anchor available on the page.",
        # if property is element of this resource.
        element_property=True,
    )
    anchor__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_anchor", title="Extension field for ``anchor``.")

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="HTML page name",
        description="Relative path to the page.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Title of the page, for references",
        description="Label for the page intended for human display.",
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImplementationGuideManifestPage`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "name", "title", "anchor"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3350(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("name", "name__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class ImplementationGuideManifestResource(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
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
        title="Is an example/What is this an example of?",
        description=(
            "If true or a reference, indicates the resource is an example instance."
            "  If a reference is present, indicates that the example is an example "
            "of the specified profile."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )
    exampleBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_exampleBoolean", title="Extension field for ``exampleBoolean``."
    )

    exampleCanonical: fhirtypes.Canonical = Field(
        None,
        alias="exampleCanonical",
        title="Is an example/What is this an example of?",
        description=(
            "If true or a reference, indicates the resource is an example instance."
            "  If a reference is present, indicates that the example is an example "
            "of the specified profile."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureDefinition"],
    )
    exampleCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_exampleCanonical",
        title="Extension field for ``exampleCanonical``.",
    )

    reference: fhirtypes.ReferenceType = Field(
        ...,
        alias="reference",
        title="Location of the resource",
        description="Where this resource is found.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    relativePath: fhirtypes.Url = Field(
        None,
        alias="relativePath",
        title="Relative path for page in IG",
        description="The relative path for primary page for this resource within the IG.",
        # if property is element of this resource.
        element_property=True,
    )
    relativePath__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_relativePath", title="Extension field for ``relativePath``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImplementationGuideManifestResource`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "reference",
            "exampleBoolean",
            "exampleCanonical",
            "relativePath",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3809(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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
