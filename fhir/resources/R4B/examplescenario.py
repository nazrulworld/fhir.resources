from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ExampleScenario
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ExampleScenario(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Example of workflow instance.
    """

    __resource_type__ = "ExampleScenario"

    actor: typing.List[fhirtypes.ExampleScenarioActorType] | None = Field(  # type: ignore
        None,
        alias="actor",
        title="Actor participating in the resource",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    contact: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        None,
        alias="contact",
        title="Contact details for the publisher",
        description=(
            "Contact details to assist a user in finding and communicating with the"
            " publisher."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    copyright: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the example scenario and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the example scenario."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the example scenario was "
            "published. The date must change when the business version changes and "
            "it must change if the status code changes. In addition, it should "
            "change when the substantive content of the example scenario changes. "
            "(e.g. the 'content logical definition')."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    experimental: bool | None = Field(  # type: ignore
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this example scenario is authored for"
            " testing purposes (or education/evaluation/marketing) and is not "
            "intended to be used for genuine usage."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Additional identifier for the example scenario",
        description=(
            "A formal identifier that is used to identify this example scenario "
            "when it is represented in other formats, or referenced in a "
            "specification, model, design or an instance."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    instance: typing.List[fhirtypes.ExampleScenarioInstanceType] | None = Field(  # type: ignore
        None,
        alias="instance",
        title="Each resource and each version that is present in the workflow",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for example scenario (if applicable)",
        description=(
            "A legal or geographic region in which the example scenario is intended"
            " to be used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name for this example scenario (computer friendly)",
        description=(
            "A natural language name identifying the example scenario. This name "
            "should be usable as an identifier for the module by machine processing"
            " applications such as code generation."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    process: typing.List[fhirtypes.ExampleScenarioProcessType] | None = Field(  # type: ignore
        None,
        alias="process",
        title="Each major process - a group of operations",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    publisher: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the organization or individual that published the example "
            "scenario."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="purpose",
        title="The purpose of the example, e.g. to illustrate a scenario",
        description=(
            "What the example scenario resource is created for. This should not be "
            "used to show the business purpose of the scenario itself, but the "
            "purpose of documenting a scenario."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this example scenario. Enables tracking the life-cycle "
            "of the content."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["draft", "active", "retired", "unknown"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    url: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="url",
        title=(
            "Canonical identifier for this example scenario, represented as a URI "
            "(globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this example scenario when it"
            " is referenced in a specification, model, design or an instance; also "
            "called its canonical identifier. This SHOULD be globally unique and "
            "SHOULD be a literal address at which at which an authoritative "
            "instance of this example scenario is (or will be) published. This URL "
            "can be the target of a canonical reference. It SHALL remain the same "
            "when the example scenario is stored on different servers."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_url", title="Extension field for ``url``."
    )

    useContext: typing.List[fhirtypes.UsageContextType] | None = Field(  # type: ignore
        None,
        alias="useContext",
        title="The context that the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These contexts may be general categories "
            "(gender, age, ...) or may be references to specific programs "
            "(insurance plans, studies, ...) and may be used to assist with "
            "indexing and searching for appropriate example scenario instances."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="Business version of the example scenario",
        description=(
            "The identifier that is used to identify this version of the example "
            "scenario when it is referenced in a specification, model, design or "
            "instance. This is an arbitrary value managed by the example scenario "
            "author and is not expected to be globally unique. For example, it "
            "might be a timestamp (e.g. yyyymmdd) if a managed version is not "
            "available. There is also no expectation that versions can be placed in"
            " a lexicographical sequence."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_version", title="Extension field for ``version``."
    )

    workflow: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="workflow",
        title="Another nested workflow",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ExampleScenario"],
        },
    )
    workflow__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_workflow", title="Extension field for ``workflow``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExampleScenario`` according specification,
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
            "status",
            "experimental",
            "date",
            "publisher",
            "contact",
            "useContext",
            "jurisdiction",
            "copyright",
            "purpose",
            "actor",
            "instance",
            "process",
            "workflow",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        return required_fields


class ExampleScenarioActor(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Actor participating in the resource.
    """

    __resource_type__ = "ExampleScenarioActor"

    actorId: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="actorId",
        title="ID or acronym of the actor",
        description="ID or acronym of actor.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    actorId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_actorId", title="Extension field for ``actorId``."
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="The description of the actor",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="The name of the actor as shown in the page",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="person | entity",
        description="The type of actor - person or system.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["person", "entity"],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExampleScenarioActor`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "actorId",
            "type",
            "name",
            "description",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("actorId", "actorId__ext"), ("type", "type__ext")]
        return required_fields


class ExampleScenarioInstance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Each resource and each version that is present in the workflow.
    """

    __resource_type__ = "ExampleScenarioInstance"

    containedInstance: typing.List[fhirtypes.ExampleScenarioInstanceContainedInstanceType] | None = Field(  # type: ignore
        None,
        alias="containedInstance",
        title="Resources contained in the instance",
        description=(
            "Resources contained in the instance (e.g. the observations contained "
            "in a bundle)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Human-friendly description of the resource instance",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="A short name for the resource instance",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    resourceId: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="resourceId",
        title="The id of the resource for referencing",
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    resourceId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_resourceId", title="Extension field for ``resourceId``."
    )

    resourceType: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="resourceType",
        title="The type of the resource",
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    resourceType__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_resourceType", title="Extension field for ``resourceType``."
    )

    version: typing.List[fhirtypes.ExampleScenarioInstanceVersionType] | None = Field(  # type: ignore
        None,
        alias="version",
        title="A specific version of the resource",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExampleScenarioInstance`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "resourceId",
            "resourceType",
            "name",
            "description",
            "version",
            "containedInstance",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("resourceId", "resourceId__ext"),
            ("resourceType", "resourceType__ext"),
        ]
        return required_fields


class ExampleScenarioInstanceContainedInstance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Resources contained in the instance.
    Resources contained in the instance (e.g. the observations contained in a
    bundle).
    """

    __resource_type__ = "ExampleScenarioInstanceContainedInstance"

    resourceId: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="resourceId",
        title="Each resource contained in the instance",
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    resourceId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_resourceId", title="Extension field for ``resourceId``."
    )

    versionId: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="versionId",
        title="A specific version of a resource contained in the instance",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    versionId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_versionId", title="Extension field for ``versionId``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExampleScenarioInstanceContainedInstance`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "resourceId", "versionId"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("resourceId", "resourceId__ext")]
        return required_fields


class ExampleScenarioInstanceVersion(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A specific version of the resource.
    """

    __resource_type__ = "ExampleScenarioInstanceVersion"

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="The description of the resource version",
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    versionId: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="versionId",
        title="The identifier of a specific version of a resource",
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    versionId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_versionId", title="Extension field for ``versionId``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExampleScenarioInstanceVersion`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "versionId", "description"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("description", "description__ext"),
            ("versionId", "versionId__ext"),
        ]
        return required_fields


class ExampleScenarioProcess(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Each major process - a group of operations.
    """

    __resource_type__ = "ExampleScenarioProcess"

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="A longer description of the group of operations",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    postConditions: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="postConditions",
        title="Description of final status after the process ends",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    postConditions__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_postConditions", title="Extension field for ``postConditions``."
    )

    preConditions: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="preConditions",
        title="Description of initial status before the process starts",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    preConditions__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_preConditions", title="Extension field for ``preConditions``."
    )

    step: typing.List[fhirtypes.ExampleScenarioProcessStepType] | None = Field(  # type: ignore
        None,
        alias="step",
        title="Each step of the process",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="The diagram title of the group of operations",
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExampleScenarioProcess`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "title",
            "description",
            "preConditions",
            "postConditions",
            "step",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("title", "title__ext")]
        return required_fields


class ExampleScenarioProcessStep(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Each step of the process.
    """

    __resource_type__ = "ExampleScenarioProcessStep"

    alternative: typing.List[fhirtypes.ExampleScenarioProcessStepAlternativeType] | None = Field(  # type: ignore
        None,
        alias="alternative",
        title="Alternate non-typical step action",
        description=(
            "Indicates an alternative step that can be taken instead of the "
            "operations on the base step in exceptional/atypical circumstances."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    operation: fhirtypes.ExampleScenarioProcessStepOperationType | None = Field(  # type: ignore
        None,
        alias="operation",
        title="Each interaction or action",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    pause: bool | None = Field(  # type: ignore
        None,
        alias="pause",
        title="If there is a pause in the flow",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    pause__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_pause", title="Extension field for ``pause``."
    )

    process: typing.List[fhirtypes.ExampleScenarioProcessType] | None = Field(  # type: ignore
        None,
        alias="process",
        title="Nested process",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExampleScenarioProcessStep`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "process",
            "pause",
            "operation",
            "alternative",
        ]


class ExampleScenarioProcessStepAlternative(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Alternate non-typical step action.
    Indicates an alternative step that can be taken instead of the operations
    on the base step in exceptional/atypical circumstances.
    """

    __resource_type__ = "ExampleScenarioProcessStepAlternative"

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="A human-readable description of each option",
        description=(
            "A human-readable description of the alternative explaining when the "
            "alternative should occur rather than the base step."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    step: typing.List[fhirtypes.ExampleScenarioProcessStepType] | None = Field(  # type: ignore
        None,
        alias="step",
        title="What happens in each alternative option",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Label for alternative",
        description=(
            "The label to display for the alternative that gives a sense of the "
            "circumstance in which the alternative should be invoked."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExampleScenarioProcessStepAlternative`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "title", "description", "step"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("title", "title__ext")]
        return required_fields


class ExampleScenarioProcessStepOperation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Each interaction or action.
    """

    __resource_type__ = "ExampleScenarioProcessStepOperation"

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="A comment to be inserted in the diagram",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    initiator: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="initiator",
        title="Who starts the transaction",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    initiator__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_initiator", title="Extension field for ``initiator``."
    )

    initiatorActive: bool | None = Field(  # type: ignore
        None,
        alias="initiatorActive",
        title="Whether the initiator is deactivated right after the transaction",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    initiatorActive__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_initiatorActive", title="Extension field for ``initiatorActive``."
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="The human-friendly name of the interaction",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    number: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="number",
        title="The sequential number of the interaction",
        description="The sequential number of the interaction, e.g. 1.2.5.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    number__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_number", title="Extension field for ``number``."
    )

    receiver: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="receiver",
        title="Who receives the transaction",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    receiver__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_receiver", title="Extension field for ``receiver``."
    )

    receiverActive: bool | None = Field(  # type: ignore
        None,
        alias="receiverActive",
        title="Whether the receiver is deactivated right after the transaction",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    receiverActive__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_receiverActive", title="Extension field for ``receiverActive``."
    )

    request: fhirtypes.ExampleScenarioInstanceContainedInstanceType | None = Field(  # type: ignore
        None,
        alias="request",
        title="Each resource instance used by the initiator",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    response: fhirtypes.ExampleScenarioInstanceContainedInstanceType | None = Field(  # type: ignore
        None,
        alias="response",
        title="Each resource instance used by the responder",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="type",
        title="The type of operation - CRUD",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExampleScenarioProcessStepOperation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "number",
            "type",
            "name",
            "initiator",
            "receiver",
            "description",
            "initiatorActive",
            "receiverActive",
            "request",
            "response",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("number", "number__ext")]
        return required_fields
