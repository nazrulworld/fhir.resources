# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ExampleScenario
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ExampleScenario(domainresource.DomainResource):
    """ Example of workflow instance.
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
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Use and/or publishing restrictions",
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date last changed",
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="Type `bool`",
        description="For testing purposes, not real usage",
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
        title="List of `ExampleScenarioInstance` items (represented as `dict` in JSON)",
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
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this example scenario (computer friendly)",
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
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of the publisher (organization or individual)",
    )

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="The purpose of the example, e.g. to illustrate a scenario",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="draft | active | retired | unknown",
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Canonical identifier for this example scenario, represented as a URI (globally unique)",
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
        description="Business version of the example scenario",
    )

    workflow: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="workflow",
        title="List of `Canonical` items referencing `ExampleScenario` (represented as `dict` in JSON)",
        description="Another nested workflow",
    )


class ExampleScenarioActor(backboneelement.BackboneElement):
    """ Actor participating in the resource.
    """

    resource_type = Field("ExampleScenarioActor", const=True)

    actorId: fhirtypes.String = Field(
        ...,
        alias="actorId",
        title="Type `String` (represented as `dict` in JSON)",
        description="ID or acronym of the actor",
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="The description of the actor",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="The name of the actor as shown in the page",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="person | entity",
    )


class ExampleScenarioInstance(backboneelement.BackboneElement):
    """ Each resource and each version that is present in the workflow.
    """

    resource_type = Field("ExampleScenarioInstance", const=True)

    containedInstance: ListType[
        fhirtypes.ExampleScenarioInstanceContainedInstanceType
    ] = Field(
        None,
        alias="containedInstance",
        title="List of `ExampleScenarioInstanceContainedInstance` items (represented as `dict` in JSON)",
        description="Resources contained in the instance",
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Human-friendly description of the resource instance",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="A short name for the resource instance",
    )

    resourceId: fhirtypes.String = Field(
        ...,
        alias="resourceId",
        title="Type `String` (represented as `dict` in JSON)",
        description="The id of the resource for referencing",
    )

    resourceType: fhirtypes.Code = Field(
        ...,
        alias="resourceType",
        title="Type `Code` (represented as `dict` in JSON)",
        description="The type of the resource",
    )

    version: ListType[fhirtypes.ExampleScenarioInstanceVersionType] = Field(
        None,
        alias="version",
        title="List of `ExampleScenarioInstanceVersion` items (represented as `dict` in JSON)",
        description="A specific version of the resource",
    )


class ExampleScenarioInstanceContainedInstance(backboneelement.BackboneElement):
    """ Resources contained in the instance.
    Resources contained in the instance (e.g. the observations contained in a
    bundle).
    """

    resource_type = Field("ExampleScenarioInstanceContainedInstance", const=True)

    resourceId: fhirtypes.String = Field(
        ...,
        alias="resourceId",
        title="Type `String` (represented as `dict` in JSON)",
        description="Each resource contained in the instance",
    )

    versionId: fhirtypes.String = Field(
        None,
        alias="versionId",
        title="Type `String` (represented as `dict` in JSON)",
        description="A specific version of a resource contained in the instance",
    )


class ExampleScenarioInstanceVersion(backboneelement.BackboneElement):
    """ A specific version of the resource.
    """

    resource_type = Field("ExampleScenarioInstanceVersion", const=True)

    description: fhirtypes.Markdown = Field(
        ...,
        alias="description",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="The description of the resource version",
    )

    versionId: fhirtypes.String = Field(
        ...,
        alias="versionId",
        title="Type `String` (represented as `dict` in JSON)",
        description="The identifier of a specific version of a resource",
    )


class ExampleScenarioProcess(backboneelement.BackboneElement):
    """ Each major process - a group of operations.
    """

    resource_type = Field("ExampleScenarioProcess", const=True)

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="A longer description of the group of operations",
    )

    postConditions: fhirtypes.Markdown = Field(
        None,
        alias="postConditions",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Description of final status after the process ends",
    )

    preConditions: fhirtypes.Markdown = Field(
        None,
        alias="preConditions",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Description of initial status before the process starts",
    )

    step: ListType[fhirtypes.ExampleScenarioProcessStepType] = Field(
        None,
        alias="step",
        title="List of `ExampleScenarioProcessStep` items (represented as `dict` in JSON)",
        description="Each step of the process",
    )

    title: fhirtypes.String = Field(
        ...,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="The diagram title of the group of operations",
    )


class ExampleScenarioProcessStep(backboneelement.BackboneElement):
    """ Each step of the process.
    """

    resource_type = Field("ExampleScenarioProcessStep", const=True)

    alternative: ListType[fhirtypes.ExampleScenarioProcessStepAlternativeType] = Field(
        None,
        alias="alternative",
        title="List of `ExampleScenarioProcessStepAlternative` items (represented as `dict` in JSON)",
        description="Alternate non-typical step action",
    )

    operation: fhirtypes.ExampleScenarioProcessStepOperationType = Field(
        None,
        alias="operation",
        title="Type `ExampleScenarioProcessStepOperation` (represented as `dict` in JSON)",
        description="Each interaction or action",
    )

    pause: bool = Field(
        None,
        alias="pause",
        title="Type `bool`",
        description="If there is a pause in the flow",
    )

    process: ListType[fhirtypes.ExampleScenarioProcessType] = Field(
        None,
        alias="process",
        title="List of `ExampleScenarioProcess` items (represented as `dict` in JSON)",
        description="Nested process",
    )


class ExampleScenarioProcessStepAlternative(backboneelement.BackboneElement):
    """ Alternate non-typical step action.
    Indicates an alternative step that can be taken instead of the operations
    on the base step in exceptional/atypical circumstances.
    """

    resource_type = Field("ExampleScenarioProcessStepAlternative", const=True)

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="A human-readable description of each option",
    )

    step: ListType[fhirtypes.ExampleScenarioProcessStepType] = Field(
        None,
        alias="step",
        title="List of `ExampleScenarioProcessStep` items (represented as `dict` in JSON)",
        description="What happens in each alternative option",
    )

    title: fhirtypes.String = Field(
        ...,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="Label for alternative",
    )


class ExampleScenarioProcessStepOperation(backboneelement.BackboneElement):
    """ Each interaction or action.
    """

    resource_type = Field("ExampleScenarioProcessStepOperation", const=True)

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="A comment to be inserted in the diagram",
    )

    initiator: fhirtypes.String = Field(
        None,
        alias="initiator",
        title="Type `String` (represented as `dict` in JSON)",
        description="Who starts the transaction",
    )

    initiatorActive: bool = Field(
        None,
        alias="initiatorActive",
        title="Type `bool`",
        description="Whether the initiator is deactivated right after the transaction",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="The human-friendly name of the interaction",
    )

    number: fhirtypes.String = Field(
        ...,
        alias="number",
        title="Type `String` (represented as `dict` in JSON)",
        description="The sequential number of the interaction",
    )

    receiver: fhirtypes.String = Field(
        None,
        alias="receiver",
        title="Type `String` (represented as `dict` in JSON)",
        description="Who receives the transaction",
    )

    receiverActive: bool = Field(
        None,
        alias="receiverActive",
        title="Type `bool`",
        description="Whether the receiver is deactivated right after the transaction",
    )

    request: fhirtypes.ExampleScenarioInstanceContainedInstanceType = Field(
        None,
        alias="request",
        title="Type `ExampleScenarioInstanceContainedInstance` (represented as `dict` in JSON)",
        description="Each resource instance used by the initiator",
    )

    response: fhirtypes.ExampleScenarioInstanceContainedInstanceType = Field(
        None,
        alias="response",
        title="Type `ExampleScenarioInstanceContainedInstance` (represented as `dict` in JSON)",
        description="Each resource instance used by the responder",
    )

    type: fhirtypes.String = Field(
        None,
        alias="type",
        title="Type `String` (represented as `dict` in JSON)",
        description="The type of operation - CRUD",
    )
