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
        title="List of `ExampleScenarioActor` items (represented as `dict` in JSON)",
        description="Actor participating in the resource",
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

    experimental: bool = Field(
        None,
        alias="experimental",
        title="Type `bool`",
        description="For testing purposes, not real usage",
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Additional identifier for the example scenario",
    )

    instance: ListType[fhirtypes.ExampleScenarioInstanceType] = Field(
        None,
        alias="instance",
        title=(
            "List of `ExampleScenarioInstance` items (represented as `dict` in " "JSON)"
        ),
        description="Each resource and each version that is present in the workflow",
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Intended jurisdiction for example scenario (if applicable)",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`",
        description="Name for this example scenario (computer friendly)",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    process: ListType[fhirtypes.ExampleScenarioProcessType] = Field(
        None,
        alias="process",
        title="List of `ExampleScenarioProcess` items (represented as `dict` in JSON)",
        description="Each major process - a group of operations",
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

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Type `Markdown`",
        description="The purpose of the example, e.g. to illustrate a scenario",
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
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

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri`",
        description=(
            "Canonical identifier for this example scenario, represented as a URI "
            "(globally unique)"
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
        description="Business version of the example scenario",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    workflow: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="workflow",
        title="List of `Canonical` items referencing `ExampleScenario`",
        description="Another nested workflow",
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
        title="Type `String`",
        description="ID or acronym of the actor",
    )
    actorId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_actorId", title="Extension field for ``actorId``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown`",
        description="The description of the actor",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`",
        description="The name of the actor as shown in the page",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    type: fhirtypes.Code = Field(
        ..., alias="type", title="Type `Code`", description="person | entity"
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
        title=(
            "List of `ExampleScenarioInstanceContainedInstance` items (represented "
            "as `dict` in JSON)"
        ),
        description="Resources contained in the instance",
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown`",
        description="Human-friendly description of the resource instance",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`",
        description="A short name for the resource instance",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    resourceId: fhirtypes.String = Field(
        ...,
        alias="resourceId",
        title="Type `String`",
        description="The id of the resource for referencing",
    )
    resourceId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_resourceId", title="Extension field for ``resourceId``."
    )

    resourceType: fhirtypes.Code = Field(
        ...,
        alias="resourceType",
        title="Type `Code`",
        description="The type of the resource",
    )
    resourceType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_resourceType", title="Extension field for ``resourceType``."
    )

    version: ListType[fhirtypes.ExampleScenarioInstanceVersionType] = Field(
        None,
        alias="version",
        title=(
            "List of `ExampleScenarioInstanceVersion` items (represented as `dict` "
            "in JSON)"
        ),
        description="A specific version of the resource",
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
        title="Type `String`",
        description="Each resource contained in the instance",
    )
    resourceId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_resourceId", title="Extension field for ``resourceId``."
    )

    versionId: fhirtypes.String = Field(
        None,
        alias="versionId",
        title="Type `String`",
        description="A specific version of a resource contained in the instance",
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
        title="Type `Markdown`",
        description="The description of the resource version",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    versionId: fhirtypes.String = Field(
        ...,
        alias="versionId",
        title="Type `String`",
        description="The identifier of a specific version of a resource",
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
        title="Type `Markdown`",
        description="A longer description of the group of operations",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    postConditions: fhirtypes.Markdown = Field(
        None,
        alias="postConditions",
        title="Type `Markdown`",
        description="Description of final status after the process ends",
    )
    postConditions__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_postConditions", title="Extension field for ``postConditions``."
    )

    preConditions: fhirtypes.Markdown = Field(
        None,
        alias="preConditions",
        title="Type `Markdown`",
        description="Description of initial status before the process starts",
    )
    preConditions__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_preConditions", title="Extension field for ``preConditions``."
    )

    step: ListType[fhirtypes.ExampleScenarioProcessStepType] = Field(
        None,
        alias="step",
        title=(
            "List of `ExampleScenarioProcessStep` items (represented as `dict` in "
            "JSON)"
        ),
        description="Each step of the process",
    )

    title: fhirtypes.String = Field(
        ...,
        alias="title",
        title="Type `String`",
        description="The diagram title of the group of operations",
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
        title=(
            "List of `ExampleScenarioProcessStepAlternative` items (represented as "
            "`dict` in JSON)"
        ),
        description="Alternate non-typical step action",
    )

    operation: fhirtypes.ExampleScenarioProcessStepOperationType = Field(
        None,
        alias="operation",
        title=(
            "Type `ExampleScenarioProcessStepOperation` (represented as `dict` in "
            "JSON)"
        ),
        description="Each interaction or action",
    )

    pause: bool = Field(
        None,
        alias="pause",
        title="Type `bool`",
        description="If there is a pause in the flow",
    )
    pause__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_pause", title="Extension field for ``pause``."
    )

    process: ListType[fhirtypes.ExampleScenarioProcessType] = Field(
        None,
        alias="process",
        title="List of `ExampleScenarioProcess` items (represented as `dict` in JSON)",
        description="Nested process",
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
        title="Type `Markdown`",
        description="A human-readable description of each option",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    step: ListType[fhirtypes.ExampleScenarioProcessStepType] = Field(
        None,
        alias="step",
        title=(
            "List of `ExampleScenarioProcessStep` items (represented as `dict` in "
            "JSON)"
        ),
        description="What happens in each alternative option",
    )

    title: fhirtypes.String = Field(
        ..., alias="title", title="Type `String`", description="Label for alternative"
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
        title="Type `Markdown`",
        description="A comment to be inserted in the diagram",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    initiator: fhirtypes.String = Field(
        None,
        alias="initiator",
        title="Type `String`",
        description="Who starts the transaction",
    )
    initiator__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_initiator", title="Extension field for ``initiator``."
    )

    initiatorActive: bool = Field(
        None,
        alias="initiatorActive",
        title="Type `bool`",
        description="Whether the initiator is deactivated right after the transaction",
    )
    initiatorActive__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_initiatorActive", title="Extension field for ``initiatorActive``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`",
        description="The human-friendly name of the interaction",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    number: fhirtypes.String = Field(
        ...,
        alias="number",
        title="Type `String`",
        description="The sequential number of the interaction",
    )
    number__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_number", title="Extension field for ``number``."
    )

    receiver: fhirtypes.String = Field(
        None,
        alias="receiver",
        title="Type `String`",
        description="Who receives the transaction",
    )
    receiver__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_receiver", title="Extension field for ``receiver``."
    )

    receiverActive: bool = Field(
        None,
        alias="receiverActive",
        title="Type `bool`",
        description="Whether the receiver is deactivated right after the transaction",
    )
    receiverActive__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_receiverActive", title="Extension field for ``receiverActive``."
    )

    request: fhirtypes.ExampleScenarioInstanceContainedInstanceType = Field(
        None,
        alias="request",
        title=(
            "Type `ExampleScenarioInstanceContainedInstance` (represented as `dict`"
            " in JSON)"
        ),
        description="Each resource instance used by the initiator",
    )

    response: fhirtypes.ExampleScenarioInstanceContainedInstanceType = Field(
        None,
        alias="response",
        title=(
            "Type `ExampleScenarioInstanceContainedInstance` (represented as `dict`"
            " in JSON)"
        ),
        description="Each resource instance used by the responder",
    )

    type: fhirtypes.String = Field(
        None,
        alias="type",
        title="Type `String`",
        description="The type of operation - CRUD",
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )
