# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/TestScript
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class TestScript(domainresource.DomainResource):
    """ Describes a set of tests.
    A structured set of tests against a FHIR server implementation to determine
    compliance against the FHIR specification.
    """

    resource_type = Field("TestScript", const=True)

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
        description="Date this was last changed",
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Natural language description of the test script",
    )

    destination: ListType[fhirtypes.TestScriptDestinationType] = Field(
        None,
        alias="destination",
        title="List of `TestScriptDestination` items (represented as `dict` in JSON)",
        description="An abstract server representing a destination or receiver in a message exchange",
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="Type `bool`",
        description="For testing purposes, not real usage",
    )

    fixture: ListType[fhirtypes.TestScriptFixtureType] = Field(
        None,
        alias="fixture",
        title="List of `TestScriptFixture` items (represented as `dict` in JSON)",
        description="Fixture in the test script - by reference (uri)",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Additional identifier for the test script",
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Intended jurisdiction for test script (if applicable)",
    )

    metadata: fhirtypes.TestScriptMetadataType = Field(
        None,
        alias="metadata",
        title="Type `TestScriptMetadata` (represented as `dict` in JSON)",
        description="Required capability that is assumed to function correctly on the FHIR server being tested",
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this test script (computer friendly)",
    )

    origin: ListType[fhirtypes.TestScriptOriginType] = Field(
        None,
        alias="origin",
        title="List of `TestScriptOrigin` items (represented as `dict` in JSON)",
        description="An abstract server representing a client or sender in a message exchange",
    )

    profile: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="profile",
        title="List of `Reference` items referencing `Resource` (represented as `dict` in JSON)",
        description="Reference of the validation profile",
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
        description="Why this test script is defined",
    )

    rule: ListType[fhirtypes.TestScriptRuleType] = Field(
        None,
        alias="rule",
        title="List of `TestScriptRule` items (represented as `dict` in JSON)",
        description="Assert rule used within the test script",
    )

    ruleset: ListType[fhirtypes.TestScriptRulesetType] = Field(
        None,
        alias="ruleset",
        title="List of `TestScriptRuleset` items (represented as `dict` in JSON)",
        description="Assert ruleset used within the test script",
    )

    setup: fhirtypes.TestScriptSetupType = Field(
        None,
        alias="setup",
        title="Type `TestScriptSetup` (represented as `dict` in JSON)",
        description="A series of required setup operations before tests are executed",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="draft | active | retired | unknown",
    )

    teardown: fhirtypes.TestScriptTeardownType = Field(
        None,
        alias="teardown",
        title="Type `TestScriptTeardown` (represented as `dict` in JSON)",
        description="A series of required clean up steps",
    )

    test: ListType[fhirtypes.TestScriptTestType] = Field(
        None,
        alias="test",
        title="List of `TestScriptTest` items (represented as `dict` in JSON)",
        description="A test in this script",
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this test script (human friendly)",
    )

    url: fhirtypes.Uri = Field(
        ...,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Logical URI to reference this test script (globally unique)",
    )

    useContext: ListType[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="List of `UsageContext` items (represented as `dict` in JSON)",
        description="Context the content is intended to support",
    )

    variable: ListType[fhirtypes.TestScriptVariableType] = Field(
        None,
        alias="variable",
        title="List of `TestScriptVariable` items (represented as `dict` in JSON)",
        description="Placeholder for evaluated elements",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String` (represented as `dict` in JSON)",
        description="Business version of the test script",
    )


class TestScriptDestination(backboneelement.BackboneElement):
    """ An abstract server representing a destination or receiver in a message
    exchange.
    An abstract server used in operations within this test script in the
    destination element.
    """

    resource_type = Field("TestScriptDestination", const=True)

    index: fhirtypes.Integer = Field(
        ...,
        alias="index",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="The index of the abstract destination server starting at 1",
    )

    profile: fhirtypes.CodingType = Field(
        ...,
        alias="profile",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="FHIR-Server | FHIR-SDC-FormManager | FHIR-SDC-FormReceiver | FHIR-SDC-FormProcessor",
    )


class TestScriptFixture(backboneelement.BackboneElement):
    """ Fixture in the test script - by reference (uri).
    Fixture in the test script - by reference (uri). All fixtures are required
    for the test script to execute.
    """

    resource_type = Field("TestScriptFixture", const=True)

    autocreate: bool = Field(
        None,
        alias="autocreate",
        title="Type `bool`",
        description="Whether or not to implicitly create the fixture during setup",
    )

    autodelete: bool = Field(
        None,
        alias="autodelete",
        title="Type `bool`",
        description="Whether or not to implicitly delete the fixture during teardown",
    )

    resource: fhirtypes.ReferenceType = Field(
        None,
        alias="resource",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="Reference of the resource",
    )


class TestScriptMetadata(backboneelement.BackboneElement):
    """ Required capability that is assumed to function correctly on the FHIR
    server being tested.
    The required capability must exist and are assumed to function correctly on
    the FHIR server being tested.
    """

    resource_type = Field("TestScriptMetadata", const=True)

    capability: ListType[fhirtypes.TestScriptMetadataCapabilityType] = Field(
        ...,
        alias="capability",
        title="List of `TestScriptMetadataCapability` items (represented as `dict` in JSON)",
        description="Capabilities  that are assumed to function correctly on the FHIR server being tested",
    )

    link: ListType[fhirtypes.TestScriptMetadataLinkType] = Field(
        None,
        alias="link",
        title="List of `TestScriptMetadataLink` items (represented as `dict` in JSON)",
        description="Links to the FHIR specification",
    )


class TestScriptMetadataCapability(backboneelement.BackboneElement):
    """ Capabilities  that are assumed to function correctly on the FHIR server
    being tested.
    Capabilities that must exist and are assumed to function correctly on the
    FHIR server being tested.
    """

    resource_type = Field("TestScriptMetadataCapability", const=True)

    capabilities: fhirtypes.ReferenceType = Field(
        ...,
        alias="capabilities",
        title="Type `Reference` referencing `CapabilityStatement` (represented as `dict` in JSON)",
        description="Required Capability Statement",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="The expected capabilities of the server",
    )

    destination: fhirtypes.Integer = Field(
        None,
        alias="destination",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Which server these requirements apply to",
    )

    link: ListType[fhirtypes.Uri] = Field(
        None,
        alias="link",
        title="List of `Uri` items (represented as `dict` in JSON)",
        description="Links to the FHIR specification",
    )

    origin: ListType[fhirtypes.Integer] = Field(
        None,
        alias="origin",
        title="List of `Integer` items (represented as `dict` in JSON)",
        description="Which origin server these requirements apply to",
    )

    required: bool = Field(
        None,
        alias="required",
        title="Type `bool`",
        description="Are the capabilities required?",
    )

    validated: bool = Field(
        None,
        alias="validated",
        title="Type `bool`",
        description="Are the capabilities validated?",
    )


class TestScriptMetadataLink(backboneelement.BackboneElement):
    """ Links to the FHIR specification.
    A link to the FHIR specification that this test is covering.
    """

    resource_type = Field("TestScriptMetadataLink", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Short description",
    )

    url: fhirtypes.Uri = Field(
        ...,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="URL to the specification",
    )


class TestScriptOrigin(backboneelement.BackboneElement):
    """ An abstract server representing a client or sender in a message exchange.
    An abstract server used in operations within this test script in the origin
    element.
    """

    resource_type = Field("TestScriptOrigin", const=True)

    index: fhirtypes.Integer = Field(
        ...,
        alias="index",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="The index of the abstract origin server starting at 1",
    )

    profile: fhirtypes.CodingType = Field(
        ...,
        alias="profile",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="FHIR-Client | FHIR-SDC-FormFiller",
    )


class TestScriptRule(backboneelement.BackboneElement):
    """ Assert rule used within the test script.
    Assert rule to be used in one or more asserts within the test script.
    """

    resource_type = Field("TestScriptRule", const=True)

    param: ListType[fhirtypes.TestScriptRuleParamType] = Field(
        None,
        alias="param",
        title="List of `TestScriptRuleParam` items (represented as `dict` in JSON)",
        description="Rule parameter template",
    )

    resource: fhirtypes.ReferenceType = Field(
        ...,
        alias="resource",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="Assert rule resource reference",
    )


class TestScriptRuleParam(backboneelement.BackboneElement):
    """ Rule parameter template.
    Each rule template can take one or more parameters for rule evaluation.
    """

    resource_type = Field("TestScriptRuleParam", const=True)

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Parameter name matching external assert rule parameter",
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="Type `String` (represented as `dict` in JSON)",
        description="Parameter value defined either explicitly or dynamically",
    )


class TestScriptRuleset(backboneelement.BackboneElement):
    """ Assert ruleset used within the test script.
    Contains one or more rules.  Offers a way to group rules so assertions
    could reference the group of rules and have them all applied.
    """

    resource_type = Field("TestScriptRuleset", const=True)

    resource: fhirtypes.ReferenceType = Field(
        ...,
        alias="resource",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="Assert ruleset resource reference",
    )

    rule: ListType[fhirtypes.TestScriptRulesetRuleType] = Field(
        ...,
        alias="rule",
        title="List of `TestScriptRulesetRule` items (represented as `dict` in JSON)",
        description="The referenced rule within the ruleset",
    )


class TestScriptRulesetRule(backboneelement.BackboneElement):
    """ The referenced rule within the ruleset.
    The referenced rule within the external ruleset template.
    """

    resource_type = Field("TestScriptRulesetRule", const=True)

    param: ListType[fhirtypes.TestScriptRulesetRuleParamType] = Field(
        None,
        alias="param",
        title="List of `TestScriptRulesetRuleParam` items (represented as `dict` in JSON)",
        description="Ruleset rule parameter template",
    )

    ruleId: fhirtypes.Id = Field(
        ...,
        alias="ruleId",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Id of referenced rule within the ruleset",
    )


class TestScriptRulesetRuleParam(backboneelement.BackboneElement):
    """ Ruleset rule parameter template.
    Each rule template can take one or more parameters for rule evaluation.
    """

    resource_type = Field("TestScriptRulesetRuleParam", const=True)

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Parameter name matching external assert ruleset rule parameter",
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="Type `String` (represented as `dict` in JSON)",
        description="Parameter value defined either explicitly or dynamically",
    )


class TestScriptSetup(backboneelement.BackboneElement):
    """ A series of required setup operations before tests are executed.
    """

    resource_type = Field("TestScriptSetup", const=True)

    action: ListType[fhirtypes.TestScriptSetupActionType] = Field(
        ...,
        alias="action",
        title="List of `TestScriptSetupAction` items (represented as `dict` in JSON)",
        description="A setup operation or assert to perform",
    )


class TestScriptSetupAction(backboneelement.BackboneElement):
    """ A setup operation or assert to perform.
    Action would contain either an operation or an assertion.
    """

    resource_type = Field("TestScriptSetupAction", const=True)

    assert_fhir: fhirtypes.TestScriptSetupActionAssertType = Field(
        None,
        alias="assert",
        title="Type `TestScriptSetupActionAssert` (represented as `dict` in JSON)",
        description="The assertion to perform",
    )

    operation: fhirtypes.TestScriptSetupActionOperationType = Field(
        None,
        alias="operation",
        title="Type `TestScriptSetupActionOperation` (represented as `dict` in JSON)",
        description="The setup operation to perform",
    )


class TestScriptSetupActionAssert(backboneelement.BackboneElement):
    """ The assertion to perform.
    Evaluates the results of previous operations to determine if the server
    under test behaves appropriately.
    """

    resource_type = Field("TestScriptSetupActionAssert", const=True)

    compareToSourceExpression: fhirtypes.String = Field(
        None,
        alias="compareToSourceExpression",
        title="Type `String` (represented as `dict` in JSON)",
        description="The fluentpath expression to evaluate against the source fixture",
    )

    compareToSourceId: fhirtypes.String = Field(
        None,
        alias="compareToSourceId",
        title="Type `String` (represented as `dict` in JSON)",
        description="Id of the source fixture to be evaluated",
    )

    compareToSourcePath: fhirtypes.String = Field(
        None,
        alias="compareToSourcePath",
        title="Type `String` (represented as `dict` in JSON)",
        description="XPath or JSONPath expression to evaluate against the source fixture",
    )

    contentType: fhirtypes.Code = Field(
        None,
        alias="contentType",
        title="Type `Code` (represented as `dict` in JSON)",
        description="xml | json | ttl | none",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Tracking/reporting assertion description",
    )

    direction: fhirtypes.Code = Field(
        None,
        alias="direction",
        title="Type `Code` (represented as `dict` in JSON)",
        description="response | request",
    )

    expression: fhirtypes.String = Field(
        None,
        alias="expression",
        title="Type `String` (represented as `dict` in JSON)",
        description="The fluentpath expression to be evaluated",
    )

    headerField: fhirtypes.String = Field(
        None,
        alias="headerField",
        title="Type `String` (represented as `dict` in JSON)",
        description="HTTP header field name",
    )

    label: fhirtypes.String = Field(
        None,
        alias="label",
        title="Type `String` (represented as `dict` in JSON)",
        description="Tracking/logging assertion label",
    )

    minimumId: fhirtypes.String = Field(
        None,
        alias="minimumId",
        title="Type `String` (represented as `dict` in JSON)",
        description="Fixture Id of minimum content resource",
    )

    navigationLinks: bool = Field(
        None,
        alias="navigationLinks",
        title="Type `bool`",
        description="Perform validation on navigation links?",
    )

    operator: fhirtypes.Code = Field(
        None,
        alias="operator",
        title="Type `Code` (represented as `dict` in JSON)",
        description="equals | notEquals | in | notIn | greaterThan | lessThan | empty | notEmpty | contains | notContains | eval",
    )

    path: fhirtypes.String = Field(
        None,
        alias="path",
        title="Type `String` (represented as `dict` in JSON)",
        description="XPath or JSONPath expression",
    )

    requestMethod: fhirtypes.Code = Field(
        None,
        alias="requestMethod",
        title="Type `Code` (represented as `dict` in JSON)",
        description="delete | get | options | patch | post | put",
    )

    requestURL: fhirtypes.String = Field(
        None,
        alias="requestURL",
        title="Type `String` (represented as `dict` in JSON)",
        description="Request URL comparison value",
    )

    resource: fhirtypes.Code = Field(
        None,
        alias="resource",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Resource type",
    )

    response: fhirtypes.Code = Field(
        None,
        alias="response",
        title="Type `Code` (represented as `dict` in JSON)",
        description="okay | created | noContent | notModified | bad | forbidden | notFound | methodNotAllowed | conflict | gone | preconditionFailed | unprocessable",
    )

    responseCode: fhirtypes.String = Field(
        None,
        alias="responseCode",
        title="Type `String` (represented as `dict` in JSON)",
        description="HTTP response code to test",
    )

    rule: fhirtypes.TestScriptSetupActionAssertRuleType = Field(
        None,
        alias="rule",
        title="Type `TestScriptSetupActionAssertRule` (represented as `dict` in JSON)",
        description="The reference to a TestScript.rule",
    )

    ruleset: fhirtypes.TestScriptSetupActionAssertRulesetType = Field(
        None,
        alias="ruleset",
        title="Type `TestScriptSetupActionAssertRuleset` (represented as `dict` in JSON)",
        description="The reference to a TestScript.ruleset",
    )

    sourceId: fhirtypes.Id = Field(
        None,
        alias="sourceId",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Fixture Id of source expression or headerField",
    )

    validateProfileId: fhirtypes.Id = Field(
        None,
        alias="validateProfileId",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Profile Id of validation profile reference",
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="Type `String` (represented as `dict` in JSON)",
        description="The value to compare to",
    )

    warningOnly: bool = Field(
        None,
        alias="warningOnly",
        title="Type `bool`",
        description="Will this assert produce a warning only on error?",
    )


class TestScriptSetupActionAssertRule(backboneelement.BackboneElement):
    """ The reference to a TestScript.rule.
    The TestScript.rule this assert will evaluate.
    """

    resource_type = Field("TestScriptSetupActionAssertRule", const=True)

    param: ListType[fhirtypes.TestScriptSetupActionAssertRuleParamType] = Field(
        None,
        alias="param",
        title="List of `TestScriptSetupActionAssertRuleParam` items (represented as `dict` in JSON)",
        description="Rule parameter template",
    )

    ruleId: fhirtypes.Id = Field(
        ...,
        alias="ruleId",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Id of the TestScript.rule",
    )


class TestScriptSetupActionAssertRuleParam(backboneelement.BackboneElement):
    """ Rule parameter template.
    Each rule template can take one or more parameters for rule evaluation.
    """

    resource_type = Field("TestScriptSetupActionAssertRuleParam", const=True)

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Parameter name matching external assert rule parameter",
    )

    value: fhirtypes.String = Field(
        ...,
        alias="value",
        title="Type `String` (represented as `dict` in JSON)",
        description="Parameter value defined either explicitly or dynamically",
    )


class TestScriptSetupActionAssertRuleset(backboneelement.BackboneElement):
    """ The reference to a TestScript.ruleset.
    The TestScript.ruleset this assert will evaluate.
    """

    resource_type = Field("TestScriptSetupActionAssertRuleset", const=True)

    rule: ListType[fhirtypes.TestScriptSetupActionAssertRulesetRuleType] = Field(
        None,
        alias="rule",
        title="List of `TestScriptSetupActionAssertRulesetRule` items (represented as `dict` in JSON)",
        description="The referenced rule within the ruleset",
    )

    rulesetId: fhirtypes.Id = Field(
        ...,
        alias="rulesetId",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Id of the TestScript.ruleset",
    )


class TestScriptSetupActionAssertRulesetRule(backboneelement.BackboneElement):
    """ The referenced rule within the ruleset.
    The referenced rule within the external ruleset template.
    """

    resource_type = Field("TestScriptSetupActionAssertRulesetRule", const=True)

    param: ListType[fhirtypes.TestScriptSetupActionAssertRulesetRuleParamType] = Field(
        None,
        alias="param",
        title="List of `TestScriptSetupActionAssertRulesetRuleParam` items (represented as `dict` in JSON)",
        description="Rule parameter template",
    )

    ruleId: fhirtypes.Id = Field(
        ...,
        alias="ruleId",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Id of referenced rule within the ruleset",
    )


class TestScriptSetupActionAssertRulesetRuleParam(backboneelement.BackboneElement):
    """ Rule parameter template.
    Each rule template can take one or more parameters for rule evaluation.
    """

    resource_type = Field("TestScriptSetupActionAssertRulesetRuleParam", const=True)

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Parameter name matching external assert ruleset rule parameter",
    )

    value: fhirtypes.String = Field(
        ...,
        alias="value",
        title="Type `String` (represented as `dict` in JSON)",
        description="Parameter value defined either explicitly or dynamically",
    )


class TestScriptSetupActionOperation(backboneelement.BackboneElement):
    """ The setup operation to perform.
    The operation to perform.
    """

    resource_type = Field("TestScriptSetupActionOperation", const=True)

    accept: fhirtypes.Code = Field(
        None,
        alias="accept",
        title="Type `Code` (represented as `dict` in JSON)",
        description="xml | json | ttl | none",
    )

    contentType: fhirtypes.Code = Field(
        None,
        alias="contentType",
        title="Type `Code` (represented as `dict` in JSON)",
        description="xml | json | ttl | none",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Tracking/reporting operation description",
    )

    destination: fhirtypes.Integer = Field(
        None,
        alias="destination",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Server responding to the request",
    )

    encodeRequestUrl: bool = Field(
        None,
        alias="encodeRequestUrl",
        title="Type `bool`",
        description="Whether or not to send the request url in encoded format",
    )

    label: fhirtypes.String = Field(
        None,
        alias="label",
        title="Type `String` (represented as `dict` in JSON)",
        description="Tracking/logging operation label",
    )

    origin: fhirtypes.Integer = Field(
        None,
        alias="origin",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Server initiating the request",
    )

    params: fhirtypes.String = Field(
        None,
        alias="params",
        title="Type `String` (represented as `dict` in JSON)",
        description="Explicitly defined path parameters",
    )

    requestHeader: ListType[
        fhirtypes.TestScriptSetupActionOperationRequestHeaderType
    ] = Field(
        None,
        alias="requestHeader",
        title="List of `TestScriptSetupActionOperationRequestHeader` items (represented as `dict` in JSON)",
        description="Each operation can have one or more header elements",
    )

    requestId: fhirtypes.Id = Field(
        None,
        alias="requestId",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Fixture Id of mapped request",
    )

    resource: fhirtypes.Code = Field(
        None,
        alias="resource",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Resource type",
    )

    responseId: fhirtypes.Id = Field(
        None,
        alias="responseId",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Fixture Id of mapped response",
    )

    sourceId: fhirtypes.Id = Field(
        None,
        alias="sourceId",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Fixture Id of body for PUT and POST requests",
    )

    targetId: fhirtypes.Id = Field(
        None,
        alias="targetId",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Id of fixture used for extracting the [id],  [type], and [vid] for GET requests",
    )

    type: fhirtypes.CodingType = Field(
        None,
        alias="type",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="The operation code type that will be executed",
    )

    url: fhirtypes.String = Field(
        None,
        alias="url",
        title="Type `String` (represented as `dict` in JSON)",
        description="Request URL",
    )


class TestScriptSetupActionOperationRequestHeader(backboneelement.BackboneElement):
    """ Each operation can have one or more header elements.
    Header elements would be used to set HTTP headers.
    """

    resource_type = Field("TestScriptSetupActionOperationRequestHeader", const=True)

    field: fhirtypes.String = Field(
        ...,
        alias="field",
        title="Type `String` (represented as `dict` in JSON)",
        description="HTTP header field name",
    )

    value: fhirtypes.String = Field(
        ...,
        alias="value",
        title="Type `String` (represented as `dict` in JSON)",
        description="HTTP headerfield value",
    )


class TestScriptTeardown(backboneelement.BackboneElement):
    """ A series of required clean up steps.
    A series of operations required to clean up after the all the tests are
    executed (successfully or otherwise).
    """

    resource_type = Field("TestScriptTeardown", const=True)

    action: ListType[fhirtypes.TestScriptTeardownActionType] = Field(
        ...,
        alias="action",
        title="List of `TestScriptTeardownAction` items (represented as `dict` in JSON)",
        description="One or more teardown operations to perform",
    )


class TestScriptTeardownAction(backboneelement.BackboneElement):
    """ One or more teardown operations to perform.
    The teardown action will only contain an operation.
    """

    resource_type = Field("TestScriptTeardownAction", const=True)

    operation: fhirtypes.TestScriptSetupActionOperationType = Field(
        ...,
        alias="operation",
        title="Type `TestScriptSetupActionOperation` (represented as `dict` in JSON)",
        description="The teardown operation to perform",
    )


class TestScriptTest(backboneelement.BackboneElement):
    """ A test in this script.
    """

    resource_type = Field("TestScriptTest", const=True)

    action: ListType[fhirtypes.TestScriptTestActionType] = Field(
        ...,
        alias="action",
        title="List of `TestScriptTestAction` items (represented as `dict` in JSON)",
        description="A test operation or assert to perform",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Tracking/reporting short description of the test",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Tracking/logging name of this test",
    )


class TestScriptTestAction(backboneelement.BackboneElement):
    """ A test operation or assert to perform.
    Action would contain either an operation or an assertion.
    """

    resource_type = Field("TestScriptTestAction", const=True)

    assert_fhir: fhirtypes.TestScriptSetupActionAssertType = Field(
        None,
        alias="assert",
        title="Type `TestScriptSetupActionAssert` (represented as `dict` in JSON)",
        description="The setup assertion to perform",
    )

    operation: fhirtypes.TestScriptSetupActionOperationType = Field(
        None,
        alias="operation",
        title="Type `TestScriptSetupActionOperation` (represented as `dict` in JSON)",
        description="The setup operation to perform",
    )


class TestScriptVariable(backboneelement.BackboneElement):
    """ Placeholder for evaluated elements.
    Variable is set based either on element value in response body or on header
    field value in the response headers.
    """

    resource_type = Field("TestScriptVariable", const=True)

    defaultValue: fhirtypes.String = Field(
        None,
        alias="defaultValue",
        title="Type `String` (represented as `dict` in JSON)",
        description="Default, hard-coded, or user-defined value for this variable",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Natural language description of the variable",
    )

    expression: fhirtypes.String = Field(
        None,
        alias="expression",
        title="Type `String` (represented as `dict` in JSON)",
        description="The fluentpath expression against the fixture body",
    )

    headerField: fhirtypes.String = Field(
        None,
        alias="headerField",
        title="Type `String` (represented as `dict` in JSON)",
        description="HTTP header field name for source",
    )

    hint: fhirtypes.String = Field(
        None,
        alias="hint",
        title="Type `String` (represented as `dict` in JSON)",
        description="Hint help text for default value to enter",
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Descriptive name for this variable",
    )

    path: fhirtypes.String = Field(
        None,
        alias="path",
        title="Type `String` (represented as `dict` in JSON)",
        description="XPath or JSONPath against the fixture body",
    )

    sourceId: fhirtypes.Id = Field(
        None,
        alias="sourceId",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Fixture Id of source expression or headerField within this variable",
    )
