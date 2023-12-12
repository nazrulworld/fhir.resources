# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Requirements
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class Requirements(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A set of requirements - features of systems that are necessary.
    A set of requirements - a list of features or behaviors of designed systems
    that are necessary to achieve organizational or regulatory goals.
    """

    resource_type = Field("Requirements", const=True)

    actor: typing.List[typing.Optional[fhirtypes.Canonical]] = Field(
        None,
        alias="actor",
        title="Actor for these requirements",
        description="An actor these requirements are in regard to.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ActorDefinition"],
    )
    actor__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_actor", title="Extension field for ``actor``.")

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
            "A copyright statement relating to the Requirements and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the Requirements."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    copyrightLabel: fhirtypes.String = Field(
        None,
        alias="copyrightLabel",
        title="Copyright holder and year(s)",
        description=(
            "A short string (<50 characters), suitable for inclusion in a page "
            "footer that identifies the copyright holder, effective period, and "
            "optionally whether rights are resctricted. (e.g. 'All rights "
            "reserved', 'Some rights reserved')."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    copyrightLabel__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyrightLabel", title="Extension field for ``copyrightLabel``."
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the Requirements was published. "
            "The date must change when the business version changes and it must "
            "change if the status code changes. In addition, it should change when "
            "the substantive content of the Requirements changes."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    derivedFrom: typing.List[typing.Optional[fhirtypes.Canonical]] = Field(
        None,
        alias="derivedFrom",
        title="Other set of Requirements this builds on",
        description=(
            "Another set of Requirements that this set of Requirements builds on "
            "and updates."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Requirements"],
    )
    derivedFrom__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_derivedFrom", title="Extension field for ``derivedFrom``.")

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Natural language description of the requirements",
        description="A free text natural language description of the requirements.",
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
            "A Boolean value to indicate that this Requirements is authored for "
            "testing purposes (or education/evaluation/marketing) and is not "
            "intended to be used for genuine usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Additional identifier for the Requirements (business identifier)",
        description=(
            "A formal identifier that is used to identify this Requirements when it"
            " is represented in other formats, or referenced in a specification, "
            "model, design or an instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for Requirements (if applicable)",
        description=(
            "A legal or geographic region in which the Requirements is intended to "
            "be used."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name for this Requirements (computer friendly)",
        description=(
            "A natural language name identifying the Requirements. This name should"
            " be usable as an identifier for the module by machine processing "
            "applications such as code generation."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher/steward (organization or individual)",
        description=(
            "The name of the organization or individual responsible for the release"
            " and ongoing maintenance of the Requirements."
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
        title="Why this Requirements is defined",
        description=(
            "Explanation of why this Requirements is needed and why it has been "
            "designed as it has."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    reference: typing.List[typing.Optional[fhirtypes.Url]] = Field(
        None,
        alias="reference",
        title=(
            "External artifact (rule/document etc. that) created this set of "
            "requirements"
        ),
        description=(
            "A reference to another artifact that created this set of requirements."
            " This could be a Profile, etc., or external regulation, or business "
            "requirements expressed elsewhere."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    reference__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_reference", title="Extension field for ``reference``.")

    statement: typing.List[fhirtypes.RequirementsStatementType] = Field(
        None,
        alias="statement",
        title="Actual statement as markdown",
        description="The actual statement of requirement, in markdown format.",
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this Requirements. Enables tracking the life-cycle of "
            "the content."
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
        title="Name for this Requirements (human friendly)",
        description="A short, descriptive, user-friendly title for the Requirements.",
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
            "Canonical identifier for this Requirements, represented as a URI "
            "(globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this Requirements when it is "
            "referenced in a specification, model, design or an instance; also "
            "called its canonical identifier. This SHOULD be globally unique and "
            "SHOULD be a literal address at which an authoritative instance of this"
            " Requirements is (or will be) published. This URL can be the target of"
            " a canonical reference. It SHALL remain the same when the Requirements"
            " is stored on different servers."
        ),
        # if property is element of this resource.
        element_property=True,
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
            "indexing and searching for appropriate Requirements instances."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the Requirements",
        description=(
            "The identifier that is used to identify this version of the "
            "Requirements when it is referenced in a specification, model, design "
            "or instance. This is an arbitrary value managed by the Requirements "
            "author and is not expected to be globally unique. For example, it "
            "might be a timestamp (e.g. yyyymmdd) if a managed version is not "
            "available. There is also no expectation that versions can be placed in"
            " a lexicographical sequence."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    versionAlgorithmCoding: fhirtypes.CodingType = Field(
        None,
        alias="versionAlgorithmCoding",
        title="How to compare versions",
        description=(
            "Indicates the mechanism used to compare versions to determine which is"
            " more current."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e versionAlgorithm[x]
        one_of_many="versionAlgorithm",
        one_of_many_required=False,
    )

    versionAlgorithmString: fhirtypes.String = Field(
        None,
        alias="versionAlgorithmString",
        title="How to compare versions",
        description=(
            "Indicates the mechanism used to compare versions to determine which is"
            " more current."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e versionAlgorithm[x]
        one_of_many="versionAlgorithm",
        one_of_many_required=False,
    )
    versionAlgorithmString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_versionAlgorithmString",
        title="Extension field for ``versionAlgorithmString``.",
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Requirements`` according specification,
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
            "versionAlgorithmString",
            "versionAlgorithmCoding",
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
            "copyrightLabel",
            "derivedFrom",
            "reference",
            "actor",
            "statement",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1481(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
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
    def validate_one_of_many_1481(
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
        one_of_many_fields = {
            "versionAlgorithm": ["versionAlgorithmCoding", "versionAlgorithmString"]
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


class RequirementsStatement(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Actual statement as markdown.
    The actual statement of requirement, in markdown format.
    """

    resource_type = Field("RequirementsStatement", const=True)

    conditionality: bool = Field(
        None,
        alias="conditionality",
        title="Set to true if requirements statement is conditional",
        description=(
            "This boolean flag is set to true of the text of the requirement is "
            "conditional on something e.g. it includes lanauage like 'if x then y'."
            " This conditionality flag is introduced for purposes of filtering and "
            "colour highlighting etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    conditionality__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_conditionality", title="Extension field for ``conditionality``."
    )

    conformance: typing.List[typing.Optional[fhirtypes.Code]] = Field(
        None,
        alias="conformance",
        title="SHALL | SHOULD | MAY | SHOULD-NOT",
        description="A short human usable label for this statement.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["SHALL", "SHOULD", "MAY", "SHOULD-NOT"],
    )
    conformance__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_conformance", title="Extension field for ``conformance``.")

    derivedFrom: fhirtypes.String = Field(
        None,
        alias="derivedFrom",
        title="Another statement this clarifies/restricts ([url#]key)",
        description=(
            "Another statement on one of the requirements that this requirement "
            "clarifies or restricts."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    derivedFrom__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_derivedFrom", title="Extension field for ``derivedFrom``."
    )

    key: fhirtypes.Id = Field(
        None,
        alias="key",
        title="Key that identifies this statement",
        description="Key that identifies this statement (unique within this resource).",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    key__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_key", title="Extension field for ``key``."
    )

    label: fhirtypes.String = Field(
        None,
        alias="label",
        title="Short Human label for this statement",
        description="A short human usable label for this statement.",
        # if property is element of this resource.
        element_property=True,
    )
    label__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_label", title="Extension field for ``label``."
    )

    parent: fhirtypes.String = Field(
        None,
        alias="parent",
        title="A larger requirement that this requirement helps to refine and enable",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    parent__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_parent", title="Extension field for ``parent``."
    )

    reference: typing.List[typing.Optional[fhirtypes.Url]] = Field(
        None,
        alias="reference",
        title="External artifact (rule/document etc. that) created this requirement",
        description=(
            "A reference to another artifact that created this requirement. This "
            "could be a Profile, etc., or external regulation, or business "
            "requirements expressed elsewhere."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    reference__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_reference", title="Extension field for ``reference``.")

    requirement: fhirtypes.Markdown = Field(
        None,
        alias="requirement",
        title="The actual requirement",
        description="The actual requirement for human consumption.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    requirement__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_requirement", title="Extension field for ``requirement``."
    )

    satisfiedBy: typing.List[typing.Optional[fhirtypes.Url]] = Field(
        None,
        alias="satisfiedBy",
        title="Design artifact that satisfies this requirement",
        description=(
            "A reference to another artifact that satisfies this requirement. This "
            "could be a Profile, extension, or an element in one of those, or a "
            "CapabilityStatement, OperationDefinition, SearchParameter, "
            "CodeSystem(/code), ValueSet, Libary etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    satisfiedBy__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_satisfiedBy", title="Extension field for ``satisfiedBy``.")

    source: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="source",
        title="Who asked for this statement",
        description=(
            "Who asked for this statement to be a requirement. By default, it's "
            "assumed that the publisher knows who it is if it matters."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "CareTeam",
            "Device",
            "Group",
            "HealthcareService",
            "Organization",
            "Patient",
            "Practitioner",
            "PractitionerRole",
            "RelatedPerson",
        ],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``RequirementsStatement`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "key",
            "label",
            "conformance",
            "conditionality",
            "requirement",
            "derivedFrom",
            "parent",
            "satisfiedBy",
            "reference",
            "source",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2431(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("key", "key__ext"), ("requirement", "requirement__ext")]
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
