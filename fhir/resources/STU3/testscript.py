# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/TestScript
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType
from typing import Union

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class TestScript(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Describes a set of tests.
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
        title="Type `Markdown`",
        description="Use and/or publishing restrictions",
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime`",
        description="Date this was last changed",
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown`",
        description="Natural language description of the test script",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    destination: ListType[fhirtypes.TestScriptDestinationType] = Field(
        None,
        alias="destination",
        title="List of `TestScriptDestination` items (represented as `dict` in JSON)",
        description=(
            "An abstract server representing a destination or receiver in a message"
            " exchange"
        ),
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
        description=(
            "Required capability that is assumed to function correctly on the FHIR "
            "server being tested"
        ),
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String`",
        description="Name for this test script (computer friendly)",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    origin: ListType[fhirtypes.TestScriptOriginType] = Field(
        None,
        alias="origin",
        title="List of `TestScriptOrigin` items (represented as `dict` in JSON)",
        description=(
            "An abstract server representing a client or sender in a message "
            "exchange"
        ),
    )

    profile: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="profile",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="Reference of the validation profile",
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
        description="Why this test script is defined",
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
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
        title="Type `Code`",
        description="draft | active | retired | unknown",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
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
        title="Type `String`",
        description="Name for this test script (human friendly)",
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.Uri = Field(
        ...,
        alias="url",
        title="Type `Uri`",
        description="Logical URI to reference this test script (globally unique)",
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
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
        title="Type `String`",
        description="Business version of the test script",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class TestScriptDestination(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An abstract server representing a destination or receiver in a message
    exchange.
    An abstract server used in operations within this test script in the
    destination element.
    """

    resource_type = Field("TestScriptDestination", const=True)

    index: fhirtypes.Integer = Field(
        ...,
        alias="index",
        title="Type `Integer`",
        description="The index of the abstract destination server starting at 1",
    )
    index__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_index", title="Extension field for ``index``."
    )

    profile: fhirtypes.CodingType = Field(
        ...,
        alias="profile",
        title="Type `Coding` (represented as `dict` in JSON)",
        description=(
            "FHIR-Server | FHIR-SDC-FormManager | FHIR-SDC-FormReceiver | FHIR-SDC-"
            "FormProcessor"
        ),
    )


class TestScriptFixture(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Fixture in the test script - by reference (uri).
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
    autocreate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_autocreate", title="Extension field for ``autocreate``."
    )

    autodelete: bool = Field(
        None,
        alias="autodelete",
        title="Type `bool`",
        description="Whether or not to implicitly delete the fixture during teardown",
    )
    autodelete__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_autodelete", title="Extension field for ``autodelete``."
    )

    resource: fhirtypes.ReferenceType = Field(
        None,
        alias="resource",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Reference of the resource",
    )


class TestScriptMetadata(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Required capability that is assumed to function correctly on the FHIR
    server being tested.
    The required capability must exist and are assumed to function correctly on
    the FHIR server being tested.
    """

    resource_type = Field("TestScriptMetadata", const=True)

    capability: ListType[fhirtypes.TestScriptMetadataCapabilityType] = Field(
        ...,
        alias="capability",
        title=(
            "List of `TestScriptMetadataCapability` items (represented as `dict` in"
            " JSON)"
        ),
        description=(
            "Capabilities  that are assumed to function correctly on the FHIR "
            "server being tested"
        ),
    )

    link: ListType[fhirtypes.TestScriptMetadataLinkType] = Field(
        None,
        alias="link",
        title="List of `TestScriptMetadataLink` items (represented as `dict` in JSON)",
        description="Links to the FHIR specification",
    )


class TestScriptMetadataCapability(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Capabilities  that are assumed to function correctly on the FHIR server
    being tested.
    Capabilities that must exist and are assumed to function correctly on the
    FHIR server being tested.
    """

    resource_type = Field("TestScriptMetadataCapability", const=True)

    capabilities: fhirtypes.ReferenceType = Field(
        ...,
        alias="capabilities",
        title=(
            "Type `Reference` referencing `CapabilityStatement` (represented as "
            "`dict` in JSON)"
        ),
        description="Required Capability Statement",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="The expected capabilities of the server",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    destination: fhirtypes.Integer = Field(
        None,
        alias="destination",
        title="Type `Integer`",
        description="Which server these requirements apply to",
    )
    destination__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_destination", title="Extension field for ``destination``."
    )

    link: ListType[fhirtypes.Uri] = Field(
        None,
        alias="link",
        title="List of `Uri` items",
        description="Links to the FHIR specification",
    )
    link__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_link", title="Extension field for ``link``."
    )

    origin: ListType[fhirtypes.Integer] = Field(
        None,
        alias="origin",
        title="List of `Integer` items",
        description="Which origin server these requirements apply to",
    )
    origin__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_origin", title="Extension field for ``origin``."
    )

    required: bool = Field(
        None,
        alias="required",
        title="Type `bool`",
        description="Are the capabilities required?",
    )
    required__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_required", title="Extension field for ``required``."
    )

    validated: bool = Field(
        None,
        alias="validated",
        title="Type `bool`",
        description="Are the capabilities validated?",
    )
    validated__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_validated", title="Extension field for ``validated``."
    )


class TestScriptMetadataLink(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Links to the FHIR specification.
    A link to the FHIR specification that this test is covering.
    """

    resource_type = Field("TestScriptMetadataLink", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Short description",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    url: fhirtypes.Uri = Field(
        ..., alias="url", title="Type `Uri`", description="URL to the specification"
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )


class TestScriptOrigin(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An abstract server representing a client or sender in a message exchange.
    An abstract server used in operations within this test script in the origin
    element.
    """

    resource_type = Field("TestScriptOrigin", const=True)

    index: fhirtypes.Integer = Field(
        ...,
        alias="index",
        title="Type `Integer`",
        description="The index of the abstract origin server starting at 1",
    )
    index__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_index", title="Extension field for ``index``."
    )

    profile: fhirtypes.CodingType = Field(
        ...,
        alias="profile",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="FHIR-Client | FHIR-SDC-FormFiller",
    )


class TestScriptRule(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Assert rule used within the test script.
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
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Assert rule resource reference",
    )


class TestScriptRuleParam(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Rule parameter template.
    Each rule template can take one or more parameters for rule evaluation.
    """

    resource_type = Field("TestScriptRuleParam", const=True)

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String`",
        description="Parameter name matching external assert rule parameter",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="Type `String`",
        description="Parameter value defined either explicitly or dynamically",
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )


class TestScriptRuleset(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Assert ruleset used within the test script.
    Contains one or more rules.  Offers a way to group rules so assertions
    could reference the group of rules and have them all applied.
    """

    resource_type = Field("TestScriptRuleset", const=True)

    resource: fhirtypes.ReferenceType = Field(
        ...,
        alias="resource",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Assert ruleset resource reference",
    )

    rule: ListType[fhirtypes.TestScriptRulesetRuleType] = Field(
        ...,
        alias="rule",
        title="List of `TestScriptRulesetRule` items (represented as `dict` in JSON)",
        description="The referenced rule within the ruleset",
    )


class TestScriptRulesetRule(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The referenced rule within the ruleset.
    The referenced rule within the external ruleset template.
    """

    resource_type = Field("TestScriptRulesetRule", const=True)

    param: ListType[fhirtypes.TestScriptRulesetRuleParamType] = Field(
        None,
        alias="param",
        title=(
            "List of `TestScriptRulesetRuleParam` items (represented as `dict` in "
            "JSON)"
        ),
        description="Ruleset rule parameter template",
    )

    ruleId: fhirtypes.Id = Field(
        ...,
        alias="ruleId",
        title="Type `Id`",
        description="Id of referenced rule within the ruleset",
    )
    ruleId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_ruleId", title="Extension field for ``ruleId``."
    )


class TestScriptRulesetRuleParam(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Ruleset rule parameter template.
    Each rule template can take one or more parameters for rule evaluation.
    """

    resource_type = Field("TestScriptRulesetRuleParam", const=True)

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String`",
        description="Parameter name matching external assert ruleset rule parameter",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="Type `String`",
        description="Parameter value defined either explicitly or dynamically",
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )


class TestScriptSetup(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A series of required setup operations before tests are executed.
    """

    resource_type = Field("TestScriptSetup", const=True)

    action: ListType[fhirtypes.TestScriptSetupActionType] = Field(
        ...,
        alias="action",
        title="List of `TestScriptSetupAction` items (represented as `dict` in JSON)",
        description="A setup operation or assert to perform",
    )


class TestScriptSetupAction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A setup operation or assert to perform.
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The assertion to perform.
    Evaluates the results of previous operations to determine if the server
    under test behaves appropriately.
    """

    resource_type = Field("TestScriptSetupActionAssert", const=True)

    compareToSourceExpression: fhirtypes.String = Field(
        None,
        alias="compareToSourceExpression",
        title="Type `String`",
        description="The fluentpath expression to evaluate against the source fixture",
    )
    compareToSourceExpression__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_compareToSourceExpression",
        title="Extension field for ``compareToSourceExpression``.",
    )

    compareToSourceId: fhirtypes.String = Field(
        None,
        alias="compareToSourceId",
        title="Type `String`",
        description="Id of the source fixture to be evaluated",
    )
    compareToSourceId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_compareToSourceId",
        title="Extension field for ``compareToSourceId``.",
    )

    compareToSourcePath: fhirtypes.String = Field(
        None,
        alias="compareToSourcePath",
        title="Type `String`",
        description="XPath or JSONPath expression to evaluate against the source fixture",
    )
    compareToSourcePath__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_compareToSourcePath",
        title="Extension field for ``compareToSourcePath``.",
    )

    contentType: fhirtypes.Code = Field(
        None,
        alias="contentType",
        title="Type `Code`",
        description="xml | json | ttl | none",
    )
    contentType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_contentType", title="Extension field for ``contentType``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Tracking/reporting assertion description",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    direction: fhirtypes.Code = Field(
        None, alias="direction", title="Type `Code`", description="response | request"
    )
    direction__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_direction", title="Extension field for ``direction``."
    )

    expression: fhirtypes.String = Field(
        None,
        alias="expression",
        title="Type `String`",
        description="The fluentpath expression to be evaluated",
    )
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_expression", title="Extension field for ``expression``."
    )

    headerField: fhirtypes.String = Field(
        None,
        alias="headerField",
        title="Type `String`",
        description="HTTP header field name",
    )
    headerField__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_headerField", title="Extension field for ``headerField``."
    )

    label: fhirtypes.String = Field(
        None,
        alias="label",
        title="Type `String`",
        description="Tracking/logging assertion label",
    )
    label__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_label", title="Extension field for ``label``."
    )

    minimumId: fhirtypes.String = Field(
        None,
        alias="minimumId",
        title="Type `String`",
        description="Fixture Id of minimum content resource",
    )
    minimumId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_minimumId", title="Extension field for ``minimumId``."
    )

    navigationLinks: bool = Field(
        None,
        alias="navigationLinks",
        title="Type `bool`",
        description="Perform validation on navigation links?",
    )
    navigationLinks__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_navigationLinks", title="Extension field for ``navigationLinks``."
    )

    operator: fhirtypes.Code = Field(
        None,
        alias="operator",
        title="Type `Code`",
        description=(
            "equals | notEquals | in | notIn | greaterThan | lessThan | empty | "
            "notEmpty | contains | notContains | eval"
        ),
    )
    operator__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_operator", title="Extension field for ``operator``."
    )

    path: fhirtypes.String = Field(
        None,
        alias="path",
        title="Type `String`",
        description="XPath or JSONPath expression",
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_path", title="Extension field for ``path``."
    )

    requestMethod: fhirtypes.Code = Field(
        None,
        alias="requestMethod",
        title="Type `Code`",
        description="delete | get | options | patch | post | put",
    )
    requestMethod__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_requestMethod", title="Extension field for ``requestMethod``."
    )

    requestURL: fhirtypes.String = Field(
        None,
        alias="requestURL",
        title="Type `String`",
        description="Request URL comparison value",
    )
    requestURL__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_requestURL", title="Extension field for ``requestURL``."
    )

    resource: fhirtypes.Code = Field(
        None, alias="resource", title="Type `Code`", description="Resource type"
    )
    resource__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_resource", title="Extension field for ``resource``."
    )

    response: fhirtypes.Code = Field(
        None,
        alias="response",
        title="Type `Code`",
        description=(
            "okay | created | noContent | notModified | bad | forbidden | notFound "
            "| methodNotAllowed | conflict | gone | preconditionFailed | "
            "unprocessable"
        ),
    )
    response__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_response", title="Extension field for ``response``."
    )

    responseCode: fhirtypes.String = Field(
        None,
        alias="responseCode",
        title="Type `String`",
        description="HTTP response code to test",
    )
    responseCode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_responseCode", title="Extension field for ``responseCode``."
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
        title=(
            "Type `TestScriptSetupActionAssertRuleset` (represented as `dict` in "
            "JSON)"
        ),
        description="The reference to a TestScript.ruleset",
    )

    sourceId: fhirtypes.Id = Field(
        None,
        alias="sourceId",
        title="Type `Id`",
        description="Fixture Id of source expression or headerField",
    )
    sourceId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sourceId", title="Extension field for ``sourceId``."
    )

    validateProfileId: fhirtypes.Id = Field(
        None,
        alias="validateProfileId",
        title="Type `Id`",
        description="Profile Id of validation profile reference",
    )
    validateProfileId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_validateProfileId",
        title="Extension field for ``validateProfileId``.",
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="Type `String`",
        description="The value to compare to",
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )

    warningOnly: bool = Field(
        None,
        alias="warningOnly",
        title="Type `bool`",
        description="Will this assert produce a warning only on error?",
    )
    warningOnly__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_warningOnly", title="Extension field for ``warningOnly``."
    )


class TestScriptSetupActionAssertRule(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The reference to a TestScript.rule.
    The TestScript.rule this assert will evaluate.
    """

    resource_type = Field("TestScriptSetupActionAssertRule", const=True)

    param: ListType[fhirtypes.TestScriptSetupActionAssertRuleParamType] = Field(
        None,
        alias="param",
        title=(
            "List of `TestScriptSetupActionAssertRuleParam` items (represented as "
            "`dict` in JSON)"
        ),
        description="Rule parameter template",
    )

    ruleId: fhirtypes.Id = Field(
        ..., alias="ruleId", title="Type `Id`", description="Id of the TestScript.rule"
    )
    ruleId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_ruleId", title="Extension field for ``ruleId``."
    )


class TestScriptSetupActionAssertRuleParam(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Rule parameter template.
    Each rule template can take one or more parameters for rule evaluation.
    """

    resource_type = Field("TestScriptSetupActionAssertRuleParam", const=True)

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String`",
        description="Parameter name matching external assert rule parameter",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    value: fhirtypes.String = Field(
        ...,
        alias="value",
        title="Type `String`",
        description="Parameter value defined either explicitly or dynamically",
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )


class TestScriptSetupActionAssertRuleset(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The reference to a TestScript.ruleset.
    The TestScript.ruleset this assert will evaluate.
    """

    resource_type = Field("TestScriptSetupActionAssertRuleset", const=True)

    rule: ListType[fhirtypes.TestScriptSetupActionAssertRulesetRuleType] = Field(
        None,
        alias="rule",
        title=(
            "List of `TestScriptSetupActionAssertRulesetRule` items (represented as"
            " `dict` in JSON)"
        ),
        description="The referenced rule within the ruleset",
    )

    rulesetId: fhirtypes.Id = Field(
        ...,
        alias="rulesetId",
        title="Type `Id`",
        description="Id of the TestScript.ruleset",
    )
    rulesetId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_rulesetId", title="Extension field for ``rulesetId``."
    )


class TestScriptSetupActionAssertRulesetRule(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The referenced rule within the ruleset.
    The referenced rule within the external ruleset template.
    """

    resource_type = Field("TestScriptSetupActionAssertRulesetRule", const=True)

    param: ListType[fhirtypes.TestScriptSetupActionAssertRulesetRuleParamType] = Field(
        None,
        alias="param",
        title=(
            "List of `TestScriptSetupActionAssertRulesetRuleParam` items "
            "(represented as `dict` in JSON)"
        ),
        description="Rule parameter template",
    )

    ruleId: fhirtypes.Id = Field(
        ...,
        alias="ruleId",
        title="Type `Id`",
        description="Id of referenced rule within the ruleset",
    )
    ruleId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_ruleId", title="Extension field for ``ruleId``."
    )


class TestScriptSetupActionAssertRulesetRuleParam(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Rule parameter template.
    Each rule template can take one or more parameters for rule evaluation.
    """

    resource_type = Field("TestScriptSetupActionAssertRulesetRuleParam", const=True)

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String`",
        description="Parameter name matching external assert ruleset rule parameter",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    value: fhirtypes.String = Field(
        ...,
        alias="value",
        title="Type `String`",
        description="Parameter value defined either explicitly or dynamically",
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )


class TestScriptSetupActionOperation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The setup operation to perform.
    The operation to perform.
    """

    resource_type = Field("TestScriptSetupActionOperation", const=True)

    accept: fhirtypes.Code = Field(
        None, alias="accept", title="Type `Code`", description="xml | json | ttl | none"
    )
    accept__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_accept", title="Extension field for ``accept``."
    )

    contentType: fhirtypes.Code = Field(
        None,
        alias="contentType",
        title="Type `Code`",
        description="xml | json | ttl | none",
    )
    contentType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_contentType", title="Extension field for ``contentType``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Tracking/reporting operation description",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    destination: fhirtypes.Integer = Field(
        None,
        alias="destination",
        title="Type `Integer`",
        description="Server responding to the request",
    )
    destination__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_destination", title="Extension field for ``destination``."
    )

    encodeRequestUrl: bool = Field(
        None,
        alias="encodeRequestUrl",
        title="Type `bool`",
        description="Whether or not to send the request url in encoded format",
    )
    encodeRequestUrl__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_encodeRequestUrl",
        title="Extension field for ``encodeRequestUrl``.",
    )

    label: fhirtypes.String = Field(
        None,
        alias="label",
        title="Type `String`",
        description="Tracking/logging operation label",
    )
    label__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_label", title="Extension field for ``label``."
    )

    origin: fhirtypes.Integer = Field(
        None,
        alias="origin",
        title="Type `Integer`",
        description="Server initiating the request",
    )
    origin__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_origin", title="Extension field for ``origin``."
    )

    params: fhirtypes.String = Field(
        None,
        alias="params",
        title="Type `String`",
        description="Explicitly defined path parameters",
    )
    params__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_params", title="Extension field for ``params``."
    )

    requestHeader: ListType[
        fhirtypes.TestScriptSetupActionOperationRequestHeaderType
    ] = Field(
        None,
        alias="requestHeader",
        title=(
            "List of `TestScriptSetupActionOperationRequestHeader` items "
            "(represented as `dict` in JSON)"
        ),
        description="Each operation can have one or more header elements",
    )

    requestId: fhirtypes.Id = Field(
        None,
        alias="requestId",
        title="Type `Id`",
        description="Fixture Id of mapped request",
    )
    requestId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_requestId", title="Extension field for ``requestId``."
    )

    resource: fhirtypes.Code = Field(
        None, alias="resource", title="Type `Code`", description="Resource type"
    )
    resource__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_resource", title="Extension field for ``resource``."
    )

    responseId: fhirtypes.Id = Field(
        None,
        alias="responseId",
        title="Type `Id`",
        description="Fixture Id of mapped response",
    )
    responseId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_responseId", title="Extension field for ``responseId``."
    )

    sourceId: fhirtypes.Id = Field(
        None,
        alias="sourceId",
        title="Type `Id`",
        description="Fixture Id of body for PUT and POST requests",
    )
    sourceId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sourceId", title="Extension field for ``sourceId``."
    )

    targetId: fhirtypes.Id = Field(
        None,
        alias="targetId",
        title="Type `Id`",
        description=(
            "Id of fixture used for extracting the [id],  [type], and [vid] for GET"
            " requests"
        ),
    )
    targetId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_targetId", title="Extension field for ``targetId``."
    )

    type: fhirtypes.CodingType = Field(
        None,
        alias="type",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="The operation code type that will be executed",
    )

    url: fhirtypes.String = Field(
        None, alias="url", title="Type `String`", description="Request URL"
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )


class TestScriptSetupActionOperationRequestHeader(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Each operation can have one or more header elements.
    Header elements would be used to set HTTP headers.
    """

    resource_type = Field("TestScriptSetupActionOperationRequestHeader", const=True)

    field: fhirtypes.String = Field(
        ..., alias="field", title="Type `String`", description="HTTP header field name"
    )
    field__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_field", title="Extension field for ``field``."
    )

    value: fhirtypes.String = Field(
        ..., alias="value", title="Type `String`", description="HTTP headerfield value"
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )


class TestScriptTeardown(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A series of required clean up steps.
    A series of operations required to clean up after the all the tests are
    executed (successfully or otherwise).
    """

    resource_type = Field("TestScriptTeardown", const=True)

    action: ListType[fhirtypes.TestScriptTeardownActionType] = Field(
        ...,
        alias="action",
        title=(
            "List of `TestScriptTeardownAction` items (represented as `dict` in "
            "JSON)"
        ),
        description="One or more teardown operations to perform",
    )


class TestScriptTeardownAction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    One or more teardown operations to perform.
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A test in this script.
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
        title="Type `String`",
        description="Tracking/reporting short description of the test",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`",
        description="Tracking/logging name of this test",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )


class TestScriptTestAction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A test operation or assert to perform.
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Placeholder for evaluated elements.
    Variable is set based either on element value in response body or on header
    field value in the response headers.
    """

    resource_type = Field("TestScriptVariable", const=True)

    defaultValue: fhirtypes.String = Field(
        None,
        alias="defaultValue",
        title="Type `String`",
        description="Default, hard-coded, or user-defined value for this variable",
    )
    defaultValue__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_defaultValue", title="Extension field for ``defaultValue``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Natural language description of the variable",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    expression: fhirtypes.String = Field(
        None,
        alias="expression",
        title="Type `String`",
        description="The fluentpath expression against the fixture body",
    )
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_expression", title="Extension field for ``expression``."
    )

    headerField: fhirtypes.String = Field(
        None,
        alias="headerField",
        title="Type `String`",
        description="HTTP header field name for source",
    )
    headerField__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_headerField", title="Extension field for ``headerField``."
    )

    hint: fhirtypes.String = Field(
        None,
        alias="hint",
        title="Type `String`",
        description="Hint help text for default value to enter",
    )
    hint__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_hint", title="Extension field for ``hint``."
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String`",
        description="Descriptive name for this variable",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    path: fhirtypes.String = Field(
        None,
        alias="path",
        title="Type `String`",
        description="XPath or JSONPath against the fixture body",
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_path", title="Extension field for ``path``."
    )

    sourceId: fhirtypes.Id = Field(
        None,
        alias="sourceId",
        title="Type `Id`",
        description="Fixture Id of source expression or headerField within this variable",
    )
    sourceId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sourceId", title="Extension field for ``sourceId``."
    )
