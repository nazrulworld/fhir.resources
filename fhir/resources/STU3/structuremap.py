# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/StructureMap
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


class StructureMap(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A Map of relationships between 2 structures that can be used to transform
    data.
    """

    resource_type = Field("StructureMap", const=True)

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
            "A copyright statement relating to the structure map and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the structure map."
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
            "The date  (and optionally time) when the structure map was published. "
            "The date must change if and when the business version changes and it "
            "must change if the status code changes. In addition, it should change "
            "when the substantive content of the structure map changes."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Natural language description of the structure map",
        description=(
            "A free text natural language description of the structure map from a "
            "consumer's perspective."
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
            "A boolean value to indicate that this structure map is authored for "
            "testing purposes (or education/evaluation/marketing), and is not "
            "intended to be used for genuine usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    group: typing.List[fhirtypes.StructureMapGroupType] = Field(
        ...,
        alias="group",
        title="Named sections for reader convenience",
        description=(
            "Organizes the mapping into managable chunks for human review/ease of "
            "maintenance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Additional identifier for the structure map",
        description=(
            "A formal identifier that is used to identify this structure map when "
            "it is represented in other formats, or referenced in a specification, "
            "model, design or an instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    import_fhir: typing.List[fhirtypes.Uri] = Field(
        None,
        alias="import",
        title="Other maps used by this map (canonical URLs)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    import__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_import", title="Extension field for ``import_fhir``.")

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for structure map (if applicable)",
        description=(
            "A legal or geographic region in which the structure map is intended to"
            " be used."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name for this structure map (computer friendly)",
        description=(
            "A natural language name identifying the structure map. This name "
            "should be usable as an identifier for the module by machine processing"
            " applications such as code generation."
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
            "structure map."
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
        title="Why this structure map is defined",
        description=(
            "Explaination of why this structure map is needed and why it has been "
            "designed as it has."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this structure map. Enables tracking the life-cycle of "
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

    structure: typing.List[fhirtypes.StructureMapStructureType] = Field(
        None,
        alias="structure",
        title="Structure Definition used by this map",
        description=(
            "A structure definition used by this map. The structure definition may "
            "describe instances that are converted, or the instances that are "
            "produced."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Name for this structure map (human friendly)",
        description="A short, descriptive, user-friendly title for the structure map.",
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Logical URI to reference this structure map (globally unique)",
        description=(
            "An absolute URI that is used to identify this structure map when it is"
            " referenced in a specification, model, design or an instance. This "
            "SHALL be a URL, SHOULD be globally unique, and SHOULD be an address at"
            " which this structure map is (or will be) published. The URL SHOULD "
            "include the major version of the structure map. For more information "
            "see [Technical and Business Versions](resource.html#versions)."
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
            "indexing and searching for appropriate structure map instances."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the structure map",
        description=(
            "The identifier that is used to identify this version of the structure "
            "map when it is referenced in a specification, model, design or "
            "instance. This is an arbitrary value managed by the structure map "
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

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``StructureMap`` according specification,
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
            "structure",
            "import",
            "group",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1458(
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
            ("name", "name__ext"),
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


class StructureMapGroup(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Named sections for reader convenience.
    Organizes the mapping into managable chunks for human review/ease of
    maintenance.
    """

    resource_type = Field("StructureMapGroup", const=True)

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Additional description/explaination for group",
        description=(
            "Additional supporting documentation that explains the purpose of the "
            "group and the types of mappings within it."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    extends: fhirtypes.Id = Field(
        None,
        alias="extends",
        title="Another group that this group adds rules to",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    extends__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_extends", title="Extension field for ``extends``."
    )

    input: typing.List[fhirtypes.StructureMapGroupInputType] = Field(
        ...,
        alias="input",
        title="Named instance provided when invoking the map",
        description=(
            "A name assigned to an instance of data. The instance must be provided "
            "when the mapping is invoked."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.Id = Field(
        None,
        alias="name",
        title="Human-readable label",
        description="A unique name for the group for the convenience of human readers.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    rule: typing.List[fhirtypes.StructureMapGroupRuleType] = Field(
        ...,
        alias="rule",
        title="Transform Rule from source to target",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    typeMode: fhirtypes.Code = Field(
        None,
        alias="typeMode",
        title="none | types | type-and-types",
        description=(
            "If this is the default rule set to apply for thie source type, or this"
            " combination of types."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["none", "types", "type-and-types"],
    )
    typeMode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_typeMode", title="Extension field for ``typeMode``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``StructureMapGroup`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "name",
            "extends",
            "typeMode",
            "documentation",
            "input",
            "rule",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1983(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("name", "name__ext"), ("typeMode", "typeMode__ext")]
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


class StructureMapGroupInput(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Named instance provided when invoking the map.
    A name assigned to an instance of data. The instance must be provided when
    the mapping is invoked.
    """

    resource_type = Field("StructureMapGroupInput", const=True)

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Documentation for this instance of data",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    mode: fhirtypes.Code = Field(
        None,
        alias="mode",
        title="source | target",
        description="Mode for this instance of data.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["source", "target"],
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_mode", title="Extension field for ``mode``."
    )

    name: fhirtypes.Id = Field(
        None,
        alias="name",
        title="Name for this instance of data",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    type: fhirtypes.String = Field(
        None,
        alias="type",
        title="Type for this instance of data",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``StructureMapGroupInput`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "name",
            "type",
            "mode",
            "documentation",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2515(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("mode", "mode__ext"), ("name", "name__ext")]
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


class StructureMapGroupRule(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Transform Rule from source to target.
    """

    resource_type = Field("StructureMapGroupRule", const=True)

    dependent: typing.List[fhirtypes.StructureMapGroupRuleDependentType] = Field(
        None,
        alias="dependent",
        title="Which other rules to apply in the context of this rule",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Documentation for this instance of data",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    name: fhirtypes.Id = Field(
        None,
        alias="name",
        title="Name of the rule for internal references",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    rule: typing.List[fhirtypes.StructureMapGroupRuleType] = Field(
        None,
        alias="rule",
        title="Rules contained in this rule",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    source: typing.List[fhirtypes.StructureMapGroupRuleSourceType] = Field(
        ...,
        alias="source",
        title="Source inputs to the mapping",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    target: typing.List[fhirtypes.StructureMapGroupRuleTargetType] = Field(
        None,
        alias="target",
        title="Content to create because of this mapping rule",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``StructureMapGroupRule`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "name",
            "source",
            "target",
            "rule",
            "dependent",
            "documentation",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2380(
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


class StructureMapGroupRuleDependent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Which other rules to apply in the context of this rule.
    """

    resource_type = Field("StructureMapGroupRuleDependent", const=True)

    name: fhirtypes.Id = Field(
        None,
        alias="name",
        title="Name of a rule or group to apply",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    variable: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="variable",
        title="Variable to pass to the rule or group",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    variable__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_variable", title="Extension field for ``variable``.")

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``StructureMapGroupRuleDependent`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "name", "variable"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3314(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("name", "name__ext"), ("variable", "variable__ext")]
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


class StructureMapGroupRuleSource(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Source inputs to the mapping.
    """

    resource_type = Field("StructureMapGroupRuleSource", const=True)

    check: fhirtypes.String = Field(
        None,
        alias="check",
        title=(
            "FHIRPath expression  - must be true or the mapping engine throws an "
            "error instead of completing"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    check__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_check", title="Extension field for ``check``."
    )

    condition: fhirtypes.String = Field(
        None,
        alias="condition",
        title="FHIRPath expression  - must be true or the rule does not apply",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    condition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_condition", title="Extension field for ``condition``."
    )

    context: fhirtypes.Id = Field(
        None,
        alias="context",
        title="Type or variable this rule applies to",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    context__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_context", title="Extension field for ``context``."
    )

    defaultValueAddress: fhirtypes.AddressType = Field(
        None,
        alias="defaultValueAddress",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueAge: fhirtypes.AgeType = Field(
        None,
        alias="defaultValueAge",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueAnnotation: fhirtypes.AnnotationType = Field(
        None,
        alias="defaultValueAnnotation",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="defaultValueAttachment",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueBase64Binary: fhirtypes.Base64Binary = Field(
        None,
        alias="defaultValueBase64Binary",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )
    defaultValueBase64Binary__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValueBase64Binary",
        title="Extension field for ``defaultValueBase64Binary``.",
    )

    defaultValueBoolean: bool = Field(
        None,
        alias="defaultValueBoolean",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )
    defaultValueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValueBoolean",
        title="Extension field for ``defaultValueBoolean``.",
    )

    defaultValueCode: fhirtypes.Code = Field(
        None,
        alias="defaultValueCode",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )
    defaultValueCode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValueCode",
        title="Extension field for ``defaultValueCode``.",
    )

    defaultValueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="defaultValueCodeableConcept",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueCoding: fhirtypes.CodingType = Field(
        None,
        alias="defaultValueCoding",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueContactPoint: fhirtypes.ContactPointType = Field(
        None,
        alias="defaultValueContactPoint",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueCount: fhirtypes.CountType = Field(
        None,
        alias="defaultValueCount",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueDate: fhirtypes.Date = Field(
        None,
        alias="defaultValueDate",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )
    defaultValueDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValueDate",
        title="Extension field for ``defaultValueDate``.",
    )

    defaultValueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="defaultValueDateTime",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )
    defaultValueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValueDateTime",
        title="Extension field for ``defaultValueDateTime``.",
    )

    defaultValueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="defaultValueDecimal",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )
    defaultValueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValueDecimal",
        title="Extension field for ``defaultValueDecimal``.",
    )

    defaultValueDistance: fhirtypes.DistanceType = Field(
        None,
        alias="defaultValueDistance",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueDuration: fhirtypes.DurationType = Field(
        None,
        alias="defaultValueDuration",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueHumanName: fhirtypes.HumanNameType = Field(
        None,
        alias="defaultValueHumanName",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueId: fhirtypes.Id = Field(
        None,
        alias="defaultValueId",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )
    defaultValueId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_defaultValueId", title="Extension field for ``defaultValueId``."
    )

    defaultValueIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="defaultValueIdentifier",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueInstant: fhirtypes.Instant = Field(
        None,
        alias="defaultValueInstant",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )
    defaultValueInstant__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValueInstant",
        title="Extension field for ``defaultValueInstant``.",
    )

    defaultValueInteger: fhirtypes.Integer = Field(
        None,
        alias="defaultValueInteger",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )
    defaultValueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValueInteger",
        title="Extension field for ``defaultValueInteger``.",
    )

    defaultValueMarkdown: fhirtypes.Markdown = Field(
        None,
        alias="defaultValueMarkdown",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )
    defaultValueMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValueMarkdown",
        title="Extension field for ``defaultValueMarkdown``.",
    )

    defaultValueMeta: fhirtypes.MetaType = Field(
        None,
        alias="defaultValueMeta",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueMoney: fhirtypes.MoneyType = Field(
        None,
        alias="defaultValueMoney",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueOid: fhirtypes.Oid = Field(
        None,
        alias="defaultValueOid",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )
    defaultValueOid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_defaultValueOid", title="Extension field for ``defaultValueOid``."
    )

    defaultValuePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="defaultValuePeriod",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValuePositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="defaultValuePositiveInt",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )
    defaultValuePositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValuePositiveInt",
        title="Extension field for ``defaultValuePositiveInt``.",
    )

    defaultValueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="defaultValueQuantity",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueRange: fhirtypes.RangeType = Field(
        None,
        alias="defaultValueRange",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueRatio: fhirtypes.RatioType = Field(
        None,
        alias="defaultValueRatio",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueReference: fhirtypes.ReferenceType = Field(
        None,
        alias="defaultValueReference",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueSampledData: fhirtypes.SampledDataType = Field(
        None,
        alias="defaultValueSampledData",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueSignature: fhirtypes.SignatureType = Field(
        None,
        alias="defaultValueSignature",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueString: fhirtypes.String = Field(
        None,
        alias="defaultValueString",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )
    defaultValueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValueString",
        title="Extension field for ``defaultValueString``.",
    )

    defaultValueTime: fhirtypes.Time = Field(
        None,
        alias="defaultValueTime",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )
    defaultValueTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValueTime",
        title="Extension field for ``defaultValueTime``.",
    )

    defaultValueTiming: fhirtypes.TimingType = Field(
        None,
        alias="defaultValueTiming",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="defaultValueUnsignedInt",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )
    defaultValueUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValueUnsignedInt",
        title="Extension field for ``defaultValueUnsignedInt``.",
    )

    defaultValueUri: fhirtypes.Uri = Field(
        None,
        alias="defaultValueUri",
        title="Default value if no value exists",
        description="A value to use if there is no existing value in the source object.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )
    defaultValueUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_defaultValueUri", title="Extension field for ``defaultValueUri``."
    )

    element: fhirtypes.String = Field(
        None,
        alias="element",
        title="Optional field for this source",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    element__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_element", title="Extension field for ``element``."
    )

    listMode: fhirtypes.Code = Field(
        None,
        alias="listMode",
        title="first | not_first | last | not_last | only_one",
        description="How to handle the list mode for this element.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["first", "not_first", "last", "not_last", "only_one"],
    )
    listMode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_listMode", title="Extension field for ``listMode``."
    )

    max: fhirtypes.String = Field(
        None,
        alias="max",
        title="Specified maximum cardinality (number or *)",
        description=(
            'Specified maximum cardinality for the element - a number or a "*". '
            "This is optional; if present, it acts an implicit check on the input "
            "content (* just serves as documentation; it's the default value)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    max__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_max", title="Extension field for ``max``."
    )

    min: fhirtypes.Integer = Field(
        None,
        alias="min",
        title="Specified minimum cardinality",
        description=(
            "Specified minimum cardinality for the element. This is optional; if "
            "present, it acts an implicit check on the input content."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    min__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_min", title="Extension field for ``min``."
    )

    type: fhirtypes.String = Field(
        None,
        alias="type",
        title="Rule only applies if source has this type",
        description=(
            "Specified type for the element. This works as a condition on the "
            "mapping - use for polymorphic elements."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    variable: fhirtypes.Id = Field(
        None,
        alias="variable",
        title="Named context for field, if a field is specified",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    variable__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_variable", title="Extension field for ``variable``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``StructureMapGroupRuleSource`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "context",
            "min",
            "max",
            "type",
            "defaultValueBase64Binary",
            "defaultValueBoolean",
            "defaultValueCode",
            "defaultValueDate",
            "defaultValueDateTime",
            "defaultValueDecimal",
            "defaultValueId",
            "defaultValueInstant",
            "defaultValueInteger",
            "defaultValueMarkdown",
            "defaultValueOid",
            "defaultValuePositiveInt",
            "defaultValueString",
            "defaultValueTime",
            "defaultValueUnsignedInt",
            "defaultValueUri",
            "defaultValueAddress",
            "defaultValueAge",
            "defaultValueAnnotation",
            "defaultValueAttachment",
            "defaultValueCodeableConcept",
            "defaultValueCoding",
            "defaultValueContactPoint",
            "defaultValueCount",
            "defaultValueDistance",
            "defaultValueDuration",
            "defaultValueHumanName",
            "defaultValueIdentifier",
            "defaultValueMoney",
            "defaultValuePeriod",
            "defaultValueQuantity",
            "defaultValueRange",
            "defaultValueRatio",
            "defaultValueReference",
            "defaultValueSampledData",
            "defaultValueSignature",
            "defaultValueTiming",
            "defaultValueMeta",
            "element",
            "listMode",
            "variable",
            "condition",
            "check",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3005(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("context", "context__ext")]
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
    def validate_one_of_many_3005(
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
            "defaultValue": [
                "defaultValueAddress",
                "defaultValueAge",
                "defaultValueAnnotation",
                "defaultValueAttachment",
                "defaultValueBase64Binary",
                "defaultValueBoolean",
                "defaultValueCode",
                "defaultValueCodeableConcept",
                "defaultValueCoding",
                "defaultValueContactPoint",
                "defaultValueCount",
                "defaultValueDate",
                "defaultValueDateTime",
                "defaultValueDecimal",
                "defaultValueDistance",
                "defaultValueDuration",
                "defaultValueHumanName",
                "defaultValueId",
                "defaultValueIdentifier",
                "defaultValueInstant",
                "defaultValueInteger",
                "defaultValueMarkdown",
                "defaultValueMeta",
                "defaultValueMoney",
                "defaultValueOid",
                "defaultValuePeriod",
                "defaultValuePositiveInt",
                "defaultValueQuantity",
                "defaultValueRange",
                "defaultValueRatio",
                "defaultValueReference",
                "defaultValueSampledData",
                "defaultValueSignature",
                "defaultValueString",
                "defaultValueTime",
                "defaultValueTiming",
                "defaultValueUnsignedInt",
                "defaultValueUri",
            ]
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


class StructureMapGroupRuleTarget(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Content to create because of this mapping rule.
    """

    resource_type = Field("StructureMapGroupRuleTarget", const=True)

    context: fhirtypes.Id = Field(
        None,
        alias="context",
        title="Type or variable this rule applies to",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    context__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_context", title="Extension field for ``context``."
    )

    contextType: fhirtypes.Code = Field(
        None,
        alias="contextType",
        title="type | variable",
        description="How to interpret the context.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["type", "variable"],
    )
    contextType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_contextType", title="Extension field for ``contextType``."
    )

    element: fhirtypes.String = Field(
        None,
        alias="element",
        title="Field to create in the context",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    element__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_element", title="Extension field for ``element``."
    )

    listMode: typing.List[fhirtypes.Code] = Field(
        None,
        alias="listMode",
        title="first | share | last | collate",
        description="If field is a list, how to manage the list.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["first", "share", "last", "collate"],
    )
    listMode__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_listMode", title="Extension field for ``listMode``.")

    listRuleId: fhirtypes.Id = Field(
        None,
        alias="listRuleId",
        title="Internal rule reference for shared list items",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    listRuleId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_listRuleId", title="Extension field for ``listRuleId``."
    )

    parameter: typing.List[fhirtypes.StructureMapGroupRuleTargetParameterType] = Field(
        None,
        alias="parameter",
        title="Parameters to the transform",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    transform: fhirtypes.Code = Field(
        None,
        alias="transform",
        title="create | copy +",
        description="How the data is copied / created.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["create", "copy", "+"],
    )
    transform__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_transform", title="Extension field for ``transform``."
    )

    variable: fhirtypes.Id = Field(
        None,
        alias="variable",
        title="Named context for field, if desired, and a field is specified",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    variable__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_variable", title="Extension field for ``variable``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``StructureMapGroupRuleTarget`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "context",
            "contextType",
            "element",
            "variable",
            "listMode",
            "listRuleId",
            "transform",
            "parameter",
        ]


class StructureMapGroupRuleTargetParameter(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Parameters to the transform.
    """

    resource_type = Field("StructureMapGroupRuleTargetParameter", const=True)

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="Parameter value - variable or literal",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="valueDecimal",
        title="Parameter value - variable or literal",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDecimal", title="Extension field for ``valueDecimal``."
    )

    valueId: fhirtypes.Id = Field(
        None,
        alias="valueId",
        title="Parameter value - variable or literal",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueId", title="Extension field for ``valueId``."
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="Parameter value - variable or literal",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueInteger", title="Extension field for ``valueInteger``."
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Parameter value - variable or literal",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``StructureMapGroupRuleTargetParameter`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "valueId",
            "valueString",
            "valueBoolean",
            "valueInteger",
            "valueDecimal",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3937(
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
            "value": [
                "valueBoolean",
                "valueDecimal",
                "valueId",
                "valueInteger",
                "valueString",
            ]
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


class StructureMapStructure(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Structure Definition used by this map.
    A structure definition used by this map. The structure definition may
    describe instances that are converted, or the instances that are produced.
    """

    resource_type = Field("StructureMapStructure", const=True)

    alias: fhirtypes.String = Field(
        None,
        alias="alias",
        title="Name for type in this map",
        description="The name used for this type in the map.",
        # if property is element of this resource.
        element_property=True,
    )
    alias__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_alias", title="Extension field for ``alias``."
    )

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Documentation on use of structure",
        description="Documentation that describes how the structure is used in the mapping.",
        # if property is element of this resource.
        element_property=True,
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    mode: fhirtypes.Code = Field(
        None,
        alias="mode",
        title="source | queried | target | produced",
        description="How the referenced structure is used in this mapping.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["source", "queried", "target", "produced"],
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_mode", title="Extension field for ``mode``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Canonical URL for structure definition",
        description="The canonical URL that identifies the structure.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``StructureMapStructure`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "url",
            "mode",
            "alias",
            "documentation",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2424(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("mode", "mode__ext"), ("url", "url__ext")]
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
