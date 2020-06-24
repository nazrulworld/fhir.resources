# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ExampleScenario
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType
from typing import Union

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ExampleScenario(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Example of workflow instance.
    """

    resource_type = Field("ExampleScenario", const=True)

    actor: ListType[fhirtypes.ExampleScenarioActorType] = Field(
        None,
        alias="actor",
        title="Actor participating in the resource",
        description=None,
    )

    contact: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="Contact details for the publisher",
        description=(
            "Contact details to assist a user in finding and communicating with the"
            " publisher."
        ),
    )

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the example scenario and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the example scenario."
        ),
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    date: fhirtypes.DateTime = Field(
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
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this example scenario is authored for"
            " testing purposes (or education/evaluation/marketing) and is not "
            "intended to be used for genuine usage."
        ),
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Additional identifier for the example scenario",
        description=(
            "A formal identifier that is used to identify this example scenario "
            "when it is represented in other formats, or referenced in a "
            "specification, model, design or an instance."
        ),
    )

    instance: ListType[fhirtypes.ExampleScenarioInstanceType] = Field(
        None,
        alias="instance",
        title="Each resource and each version that is present in the workflow",
        description=None,
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for example scenario (if applicable)",
        description=(
            "A legal or geographic region in which the example scenario is intended"
            " to be used."
        ),
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name for this example scenario (computer friendly)",
        description=(
            "A natural language name identifying the example scenario. This name "
            "should be usable as an identifier for the module by machine processing"
            " applications such as code generation."
        ),
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    process: ListType[fhirtypes.ExampleScenarioProcessType] = Field(
        None,
        alias="process",
        title="Each major process - a group of operations",
        description=None,
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the organization or individual that published the example "
            "scenario."
        ),
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="The purpose of the example, e.g. to illustrate a scenario",
        description=(
            "What the example scenario resource is created for. This should not be "
            "used to show the business purpose of the scenario itself, but the "
            "purpose of documenting a scenario."
        ),
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this example scenario. Enables tracking the life-cycle "
            "of the content."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired", "unknown"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    url: fhirtypes.Uri = Field(
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
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    useContext: ListType[fhirtypes.UsageContextType] = Field(
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
    )

    version: fhirtypes.String = Field(
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
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    workflow: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="workflow",
        title="Another nested workflow",
        description=None,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ExampleScenario"],
    )
    workflow__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_workflow", title="Extension field for ``workflow``."
    )


class ExampleScenarioActor(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Actor participating in the resource.
    """

    resource_type = Field("ExampleScenarioActor", const=True)

    actorId: fhirtypes.String = Field(
        ...,
        alias="actorId",
        title="ID or acronym of the actor",
        description="ID or acronym of actor.",
    )
    actorId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_actorId", title="Extension field for ``actorId``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="The description of the actor",
        description=None,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="The name of the actor as shown in the page",
        description=None,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="person | entity",
        description="The type of actor - person or system.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["person", "entity"],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )


class ExampleScenarioInstance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Each resource and each version that is present in the workflow.
    """

    resource_type = Field("ExampleScenarioInstance", const=True)

    containedInstance: ListType[
        fhirtypes.ExampleScenarioInstanceContainedInstanceType
    ] = Field(
        None,
        alias="containedInstance",
        title="Resources contained in the instance",
        description=(
            "Resources contained in the instance (e.g. the observations contained "
            "in a bundle)."
        ),
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Human-friendly description of the resource instance",
        description=None,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="A short name for the resource instance",
        description=None,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    resourceId: fhirtypes.String = Field(
        ...,
        alias="resourceId",
        title="The id of the resource for referencing",
        description=None,
    )
    resourceId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_resourceId", title="Extension field for ``resourceId``."
    )

    resourceType: fhirtypes.Code = Field(
        ..., alias="resourceType", title="The type of the resource", description=None,
    )
    resourceType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_resourceType", title="Extension field for ``resourceType``."
    )

    version: ListType[fhirtypes.ExampleScenarioInstanceVersionType] = Field(
        None,
        alias="version",
        title="A specific version of the resource",
        description=None,
    )


class ExampleScenarioInstanceContainedInstance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Resources contained in the instance.
    Resources contained in the instance (e.g. the observations contained in a
    bundle).
    """

    resource_type = Field("ExampleScenarioInstanceContainedInstance", const=True)

    resourceId: fhirtypes.String = Field(
        ...,
        alias="resourceId",
        title="Each resource contained in the instance",
        description=None,
    )
    resourceId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_resourceId", title="Extension field for ``resourceId``."
    )

    versionId: fhirtypes.String = Field(
        None,
        alias="versionId",
        title="A specific version of a resource contained in the instance",
        description=None,
    )
    versionId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_versionId", title="Extension field for ``versionId``."
    )


class ExampleScenarioInstanceVersion(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A specific version of the resource.
    """

    resource_type = Field("ExampleScenarioInstanceVersion", const=True)

    description: fhirtypes.Markdown = Field(
        ...,
        alias="description",
        title="The description of the resource version",
        description=None,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    versionId: fhirtypes.String = Field(
        ...,
        alias="versionId",
        title="The identifier of a specific version of a resource",
        description=None,
    )
    versionId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_versionId", title="Extension field for ``versionId``."
    )


class ExampleScenarioProcess(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Each major process - a group of operations.
    """

    resource_type = Field("ExampleScenarioProcess", const=True)

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="A longer description of the group of operations",
        description=None,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    postConditions: fhirtypes.Markdown = Field(
        None,
        alias="postConditions",
        title="Description of final status after the process ends",
        description=None,
    )
    postConditions__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_postConditions", title="Extension field for ``postConditions``."
    )

    preConditions: fhirtypes.Markdown = Field(
        None,
        alias="preConditions",
        title="Description of initial status before the process starts",
        description=None,
    )
    preConditions__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_preConditions", title="Extension field for ``preConditions``."
    )

    step: ListType[fhirtypes.ExampleScenarioProcessStepType] = Field(
        None, alias="step", title="Each step of the process", description=None,
    )

    title: fhirtypes.String = Field(
        ...,
        alias="title",
        title="The diagram title of the group of operations",
        description=None,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )


class ExampleScenarioProcessStep(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Each step of the process.
    """

    resource_type = Field("ExampleScenarioProcessStep", const=True)

    alternative: ListType[fhirtypes.ExampleScenarioProcessStepAlternativeType] = Field(
        None,
        alias="alternative",
        title="Alternate non-typical step action",
        description=(
            "Indicates an alternative step that can be taken instead of the "
            "operations on the base step in exceptional/atypical circumstances."
        ),
    )

    operation: fhirtypes.ExampleScenarioProcessStepOperationType = Field(
        None, alias="operation", title="Each interaction or action", description=None,
    )

    pause: bool = Field(
        None, alias="pause", title="If there is a pause in the flow", description=None,
    )
    pause__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_pause", title="Extension field for ``pause``."
    )

    process: ListType[fhirtypes.ExampleScenarioProcessType] = Field(
        None, alias="process", title="Nested process", description=None,
    )


class ExampleScenarioProcessStepAlternative(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Alternate non-typical step action.
    Indicates an alternative step that can be taken instead of the operations
    on the base step in exceptional/atypical circumstances.
    """

    resource_type = Field("ExampleScenarioProcessStepAlternative", const=True)

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="A human-readable description of each option",
        description=(
            "A human-readable description of the alternative explaining when the "
            "alternative should occur rather than the base step."
        ),
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    step: ListType[fhirtypes.ExampleScenarioProcessStepType] = Field(
        None,
        alias="step",
        title="What happens in each alternative option",
        description=None,
    )

    title: fhirtypes.String = Field(
        ...,
        alias="title",
        title="Label for alternative",
        description=(
            "The label to display for the alternative that gives a sense of the "
            "circumstance in which the alternative should be invoked."
        ),
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )


class ExampleScenarioProcessStepOperation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Each interaction or action.
    """

    resource_type = Field("ExampleScenarioProcessStepOperation", const=True)

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="A comment to be inserted in the diagram",
        description=None,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    initiator: fhirtypes.String = Field(
        None, alias="initiator", title="Who starts the transaction", description=None,
    )
    initiator__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_initiator", title="Extension field for ``initiator``."
    )

    initiatorActive: bool = Field(
        None,
        alias="initiatorActive",
        title="Whether the initiator is deactivated right after the transaction",
        description=None,
    )
    initiatorActive__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_initiatorActive", title="Extension field for ``initiatorActive``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="The human-friendly name of the interaction",
        description=None,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    number: fhirtypes.String = Field(
        ...,
        alias="number",
        title="The sequential number of the interaction",
        description="The sequential number of the interaction, e.g. 1.2.5.",
    )
    number__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_number", title="Extension field for ``number``."
    )

    receiver: fhirtypes.String = Field(
        None, alias="receiver", title="Who receives the transaction", description=None,
    )
    receiver__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_receiver", title="Extension field for ``receiver``."
    )

    receiverActive: bool = Field(
        None,
        alias="receiverActive",
        title="Whether the receiver is deactivated right after the transaction",
        description=None,
    )
    receiverActive__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_receiverActive", title="Extension field for ``receiverActive``."
    )

    request: fhirtypes.ExampleScenarioInstanceContainedInstanceType = Field(
        None,
        alias="request",
        title="Each resource instance used by the initiator",
        description=None,
    )

    response: fhirtypes.ExampleScenarioInstanceContainedInstanceType = Field(
        None,
        alias="response",
        title="Each resource instance used by the responder",
        description=None,
    )

    type: fhirtypes.String = Field(
        None, alias="type", title="The type of operation - CRUD", description=None,
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )
