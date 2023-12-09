# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/StructureDefinition
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class StructureDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Structural Definition.
    A definition of a FHIR structure. This resource is used to describe the
    underlying resources, data types defined in FHIR, and also for describing
    extensions and constraints on resources and data types.
    """

    resource_type = Field("StructureDefinition", const=True)

    abstract: bool = Field(
        None,
        alias="abstract",
        title="Whether the structure is abstract",
        description=(
            "Whether structure this definition describes is abstract or not  - that"
            " is, whether the structure is not intended to be instantiated. For "
            "Resources and Data types, abstract types will never be exchanged  "
            "between systems."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    abstract__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_abstract", title="Extension field for ``abstract``."
    )

    baseDefinition: fhirtypes.Uri = Field(
        None,
        alias="baseDefinition",
        title="Definition that this type is constrained/specialized from",
        description=(
            "An absolute URI that is the base structure from which this type is "
            "derived, either by specialization or constraint."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    baseDefinition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_baseDefinition", title="Extension field for ``baseDefinition``."
    )

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

    context: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="context",
        title="Where the extension can be used in instances",
        description=(
            "Identifies the types of resource or data type elements to which the "
            "extension can be applied."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    context__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_context", title="Extension field for ``context``.")

    contextInvariant: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="contextInvariant",
        title="FHIRPath invariants - when the extension can be used",
        description=(
            "A set of rules as Fluent Invariants about when the extension can be "
            "used (e.g. co-occurrence variants for the extension)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    contextInvariant__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_contextInvariant",
        title="Extension field for ``contextInvariant``.",
    )

    contextType: fhirtypes.Code = Field(
        None,
        alias="contextType",
        title="resource | datatype | extension",
        description=(
            "If this is an extension, Identifies the context within FHIR resources "
            "where the extension can be used."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["resource", "datatype", "extension"],
    )
    contextType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_contextType", title="Extension field for ``contextType``."
    )

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the structure definition and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the structure definition."
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
        title="Date this was last changed",
        description=(
            "The date  (and optionally time) when the structure definition was "
            "published. The date must change if and when the business version "
            "changes and it must change if the status code changes. In addition, it"
            " should change when the substantive content of the structure "
            "definition changes."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    derivation: fhirtypes.Code = Field(
        None,
        alias="derivation",
        title="specialization | constraint - How relates to base definition",
        description="How the type relates to the baseDefinition.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["specialization", "constraint"],
    )
    derivation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_derivation", title="Extension field for ``derivation``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Natural language description of the structure definition",
        description=(
            "A free text natural language description of the structure definition "
            "from a consumer's perspective."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    differential: fhirtypes.StructureDefinitionDifferentialType = Field(
        None,
        alias="differential",
        title="Differential view of the structure",
        description=(
            "A differential view is expressed relative to the base "
            "StructureDefinition - a statement of differences that it applies."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A boolean value to indicate that this structure definition is authored"
            " for testing purposes (or education/evaluation/marketing), and is not "
            "intended to be used for genuine usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    fhirVersion: fhirtypes.Id = Field(
        None,
        alias="fhirVersion",
        title="FHIR Version this StructureDefinition targets",
        description=(
            "The version of the FHIR specification on which this "
            "StructureDefinition is based - this is the formal version of the "
            "specification, without the revision number, e.g. "
            "[publication].[major].[minor], which is 3.0.2 for this version."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    fhirVersion__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fhirVersion", title="Extension field for ``fhirVersion``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Additional identifier for the structure definition",
        description=(
            "A formal identifier that is used to identify this structure definition"
            " when it is represented in other formats, or referenced in a "
            "specification, model, design or an instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for structure definition (if applicable)",
        description=(
            "A legal or geographic region in which the structure definition is "
            "intended to be used."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    keyword: typing.List[fhirtypes.CodingType] = Field(
        None,
        alias="keyword",
        title="Assist with indexing and finding",
        description=(
            "A set of key words or terms from external terminologies that may be "
            "used to assist with indexing and searching of templates."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    kind: fhirtypes.Code = Field(
        None,
        alias="kind",
        title="primitive-type | complex-type | resource | logical",
        description="Defines the kind of structure that this definition is describing.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["primitive-type", "complex-type", "resource", "logical"],
    )
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_kind", title="Extension field for ``kind``."
    )

    mapping: typing.List[fhirtypes.StructureDefinitionMappingType] = Field(
        None,
        alias="mapping",
        title="External specification that the content is mapped to",
        description="An external specification that the content is mapped to.",
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name for this structure definition (computer friendly)",
        description=(
            "A natural language name identifying the structure definition. This "
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

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the individual or organization that published the "
            "structure definition."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Why this structure definition is defined",
        description=(
            "Explaination of why this structure definition is needed and why it has"
            " been designed as it has."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    snapshot: fhirtypes.StructureDefinitionSnapshotType = Field(
        None,
        alias="snapshot",
        title="Snapshot view of the structure",
        description=(
            "A snapshot view is expressed in a stand alone form that can be used "
            "and interpreted without considering the base StructureDefinition."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this structure definition. Enables tracking the life-"
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
        title="Name for this structure definition (human friendly)",
        description=(
            "A short, descriptive, user-friendly title for the structure " "definition."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="Type defined or constrained by this structure",
        description=(
            "The type this structure describes. If the derivation kind is "
            "'specialization' then this is the master definition for a type, and "
            "there is always one of these (a data type, an extension, a resource, "
            "including abstract ones). Otherwise the structure definition is a "
            "constraint on the stated type (and in this case, the type cannot be an"
            " abstract type)."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Logical URI to reference this structure definition (globally unique)",
        description=(
            "An absolute URI that is used to identify this structure definition "
            "when it is referenced in a specification, model, design or an "
            "instance. This SHALL be a URL, SHOULD be globally unique, and SHOULD "
            "be an address at which this structure definition is (or will be) "
            "published. The URL SHOULD include the major version of the structure "
            "definition. For more information see [Technical and Business "
            "Versions](resource.html#versions)."
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
        title="Context the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These terms may be used to assist with "
            "indexing and searching for appropriate structure definition instances."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the structure definition",
        description=(
            "The identifier that is used to identify this version of the structure "
            "definition when it is referenced in a specification, model, design or "
            "instance. This is an arbitrary value managed by the structure "
            "definition author and is not expected to be globally unique. For "
            "example, it might be a timestamp (e.g. yyyymmdd) if a managed version "
            "is not available. There is also no expectation that versions can be "
            "placed in a lexicographical sequence."
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
        ``StructureDefinition`` according specification,
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
            "identifier",
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
            "purpose",
            "copyright",
            "keyword",
            "fhirVersion",
            "mapping",
            "kind",
            "abstract",
            "contextType",
            "context",
            "contextInvariant",
            "type",
            "baseDefinition",
            "derivation",
            "snapshot",
            "differential",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2203(
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
            ("abstract", "abstract__ext"),
            ("kind", "kind__ext"),
            ("name", "name__ext"),
            ("status", "status__ext"),
            ("type", "type__ext"),
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


class StructureDefinitionDifferential(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Differential view of the structure.
    A differential view is expressed relative to the base StructureDefinition -
    a statement of differences that it applies.
    """

    resource_type = Field("StructureDefinitionDifferential", const=True)

    element: typing.List[fhirtypes.ElementDefinitionType] = Field(
        ...,
        alias="element",
        title="Definition of elements in the resource (if no StructureDefinition)",
        description="Captures constraints on each element within the resource.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``StructureDefinitionDifferential`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "element"]


class StructureDefinitionMapping(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    External specification that the content is mapped to.
    An external specification that the content is mapped to.
    """

    resource_type = Field("StructureDefinitionMapping", const=True)

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Versions, Issues, Scope limitations etc.",
        description=(
            "Comments about this mapping, including version notes, issues, scope "
            "limitations, and other important notes for usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    identity: fhirtypes.Id = Field(
        None,
        alias="identity",
        title="Internal id when this mapping is used",
        description=(
            "An Internal id that is used to identify this mapping set when specific"
            " mappings are made."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    identity__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_identity", title="Extension field for ``identity``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Names what this mapping refers to",
        description="A name for the specification that is being mapped to.",
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    uri: fhirtypes.Uri = Field(
        None,
        alias="uri",
        title="Identifies what this mapping refers to",
        description=(
            "An absolute URI that identifies the specification that this mapping is"
            " expressed to."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_uri", title="Extension field for ``uri``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``StructureDefinitionMapping`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "identity",
            "uri",
            "name",
            "comment",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2912(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("identity", "identity__ext")]
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


class StructureDefinitionSnapshot(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Snapshot view of the structure.
    A snapshot view is expressed in a stand alone form that can be used and
    interpreted without considering the base StructureDefinition.
    """

    resource_type = Field("StructureDefinitionSnapshot", const=True)

    element: typing.List[fhirtypes.ElementDefinitionType] = Field(
        ...,
        alias="element",
        title="Definition of elements in the resource (if no StructureDefinition)",
        description="Captures constraints on each element within the resource.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``StructureDefinitionSnapshot`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "element"]
