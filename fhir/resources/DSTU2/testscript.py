# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/DSTU2/testscript.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic.v1 import Field

from . import domainresource, fhirtypes
from .backboneelement import BackboneElement


class TestScript(domainresource.DomainResource):
    """Describes a set of tests



    TestScript is a resource that specifies a suite of tests against a FHIR
    server implementation to determine compliance against the FHIR specification.
    """

    resource_type = Field("TestScript", const=True)

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Absolute URL used to reference this TestScript",
        description=(
            "An absolute URL that is used to identify this Test Script. "
            "This SHALL be a URL, SHOULD be globally unique, "
            "and SHOULD be an address at which this Test "
            "Script is (or will be) published."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String` (represented as `dict` in JSON)",
        description="Logical id for this version of the TestScript",
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Informal name for this TestScript",
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON).",
        description="draft | active | retired",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities,
        # read official FHIR documentation.
        enum_values=["draft", "active", "retired"],
        element_property=True,
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="External identifier",
        description=(
            "Identifier for the TestScript assigned for external "
            "purposes outside the context of FHIR."
        ),
        element_property=True,
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="If for testing purposes, not real usage",
        description=(
            "This TestScript was authored for testing purposes "
            "(or education/evaluation/marketing), and is not intended "
            "to be used for genuine usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of the publisher (Organization or individual)",
        element_property=True,
    )

    contact: ListType[fhirtypes.TestScriptContactType] = Field(
        None,
        alias="contact",
        title="Contact details of the publisher",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date for this version of the TestScript",
        description=(
            "The date this version of the test script was published. "
            "The date must change when the business version changes, "
            "if it does, and it must change if the status code changes. "
            "In addition, it should change when the substantive content "
            "of the test cases change."
        ),
        element_property=True,
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Natural language description of the TestScript",
        element_property=True,
    )

    useContext: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="useContext",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Content intends to support these contexts",
        element_property=True,
    )

    requirements: fhirtypes.String = Field(
        None,
        alias="requirements",
        title="Type `String` (represented as `dict` in JSON)",
        description="Scope and Usage this Test Script is for",
        element_property=True,
    )

    copyright: fhirtypes.String = Field(
        None,
        alias="copyright",
        title="Type `String` (represented as `dict` in JSON)",
        description="Use and/or publishing restrictions",
        element_property=True,
    )

    metadata: ListType[fhirtypes.TestScriptMetadataType] = Field(
        None,
        alias="metadata",
        title=(
            "Required capability that is assumed to function "
            "correctly on the FHIR server being tested"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    multiserver: bool = Field(
        None,
        alias="multiserver",
        title="Whether or not the tests apply to more than one FHIR server",
        description=(
            "If the tests apply to more than one FHIR server "
            "(e.g. cross-server interoperability tests) then multiserver=true."
            " Defaults to false if value is unspecified."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    fixture: ListType[fhirtypes.TestScriptFixtureType] = Field(
        None,
        alias="fixture",
        title="Fixture in the test script - by reference (uri)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    profile: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="profile",
        title="Type 'Reference' referencing 'Any'  (represented as 'dict' in JSON).",
        description="Reference of the validation profile",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Any"],
        element_property=True,
    )

    variable: ListType[fhirtypes.TestScriptVariableType] = Field(
        None,
        alias="variable",
        title="Placeholder for evaluated elements",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    setup: fhirtypes.TestScriptSetupType = Field(
        None,
        alias="setup",
        title="A series of required setup operations before tests are executed",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    test: ListType[fhirtypes.TestScriptTestType] = Field(
        None,
        alias="test",
        title="A test in this script",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    teardown: fhirtypes.TestScriptTeardownType = Field(
        None,
        alias="teardown",
        title="A series of required clean up steps",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class TestScriptContact(BackboneElement):
    """Contact details of the publisher

    Contacts to assist a user in finding and communicating with the publisher.
    """

    resource_type = Field("TestScriptContact", const=True)

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of a individual to contact",
        element_property=True,
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="Contact details for individual or publisher",
        description=(
            "Contact details for individual "
            "(if a name was provided) or the publisher."
        ),
        element_property=True,
    )


class TestScriptMetadata(BackboneElement):
    """Required capability that is assumed to function correctly on the FHIR
    server being tested

    The required capability must exist and are assumed to function correctly
    on the FHIR server being tested.
    """

    resource_type = Field("TestScriptMetadata", const=True)

    link: ListType[fhirtypes.TestScriptMetadataLinkType] = Field(
        None,
        alias="link",
        title="Links to the FHIR specification",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    capability: ListType[fhirtypes.TestScriptMetadataCapabilityType] = Field(
        None,
        alias="capability",
        title=(
            "Capabilities  that are assumed to function "
            "correctly on the FHIR server being tested"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class TestScriptFixture(BackboneElement):
    """Fixture in the test script - by reference (uri)

    Fixture in the test script - by reference (uri).
    All fixtures are required for the test script to execute.
    """

    resource_type = Field("TestScriptFixture", const=True)

    autocreate: bool = Field(
        None,
        alias="autocreate",
        title="Whether or not to implicitly create the fixture during setup",
        description=(
            "Whether or not to implicitly create the fixture during setup. "
            "If true, the fixture is automatically created on each server being "
            "tested during setup, therefore no create operation is required for "
            "this fixture in the TestScript.setup section."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    autodelete: bool = Field(
        None,
        alias="autodelete",
        title="Whether or not to implicitly delete the fixture during teardown",
        description=(
            "Whether or not to implicitly delete the fixture during "
            "teardown If true, the fixture is automatically deleted on "
            "each server being tested during teardown, therefore no delete "
            "operation is required for this fixture in the TestScript.teardown section."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    resource: fhirtypes.ReferenceType = Field(
        None,
        alias="resource",
        title="Type 'Reference' referencing 'Any'  (represented as 'dict' in JSON).",
        description="Reference of the resource",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Any"],
        element_property=True,
    )


class TestScriptVariable(BackboneElement):
    """Placeholder for evaluated elements

    Variable is set based either on element value in response body or on header
     field value in the response headers.
    """

    resource_type = Field("TestScriptVariable", const=True)

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Descriptive name for this variable",
        element_property=True,
    )

    headerField: fhirtypes.String = Field(
        None,
        alias="headerField",
        title="Type `String` (represented as `dict` in JSON)",
        description="HTTP header field name for source",
        element_property=True,
    )

    path: fhirtypes.String = Field(
        None,
        alias="path",
        title="Type `String` (represented as `dict` in JSON)",
        description="XPath or JSONPath against the fixture body",
        element_property=True,
    )

    sourceId: fhirtypes.Id = Field(
        None,
        alias="sourceId",
        title="Fixture Id of source expression or headerField within this variable",
        description=(
            "Fixture to evaluate the XPath/JSONPath expression "
            "or the headerField against within this variable."
        ),
        # if property is element of this resource.
        element_property=True,
    )


class TestScriptSetup(BackboneElement):
    """A series of required setup operations before tests are executed

    A series of required setup operations before tests are executed.
    """

    resource_type = Field("TestScriptSetup", const=True)

    metadata: fhirtypes.TestScriptMetadataType = Field(
        None,
        alias="metadata",
        title=(
            "Capabilities that are assumed to function correctly "
            "on the FHIR server being tested"
        ),
        description=(
            "Capabilities that must exist and are assumed to function "
            "correctly on the FHIR server being tested."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    action: ListType[fhirtypes.TestScriptSetupActionType] = Field(
        None,
        alias="action",
        title="A setup operation or assert to perform",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class TestScriptTest(BackboneElement):
    """A test in this script



    A test in this script.
    """

    resource_type = Field("TestScriptTest", const=True)

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Tracking/logging name of this test",
        element_property=True,
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Tracking/reporting short description of the test",
        element_property=True,
    )

    metadata: fhirtypes.TestScriptMetadataType = Field(
        None,
        alias="metadata",
        title=(
            "Capabilities that are assumed to function "
            "correctly on the FHIR server being tested"
        ),
        description=(
            "Capabilities that must exist and are assumed to "
            "function correctly on the FHIR server being tested."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    action: ListType[fhirtypes.TestScriptTestActionType] = Field(
        None,
        alias="action",
        title="A test operation or assert to perform",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class TestScriptTeardown(BackboneElement):
    """A series of required clean up steps

    A series of operations required to clean up after the all the tests
    are executed (successfully or otherwise).
    """

    resource_type = Field("TestScriptTeardown", const=True)

    action: ListType[fhirtypes.TestScriptTeardownActionType] = Field(
        None,
        alias="action",
        title="One or more teardown operations to perform",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class TestScriptMetadataLink(BackboneElement):
    """Links to the FHIR specification

    A link to the FHIR specification that this test is covering.
    """

    resource_type = Field("TestScriptMetadataLink", const=True)

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="URL to the specification",
        description="URL to a particular requirement or feature within the FHIR specification.",
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Short description",
        element_property=True,
    )


class TestScriptMetadataCapability(BackboneElement):
    """Capabilities that are assumed to function correctly on
    the FHIR server being tested

    Capabilities that must exist and are assumed to function
    correctly on the FHIR server being tested.
    """

    resource_type = Field("TestScriptMetadataCapability", const=True)

    required: bool = Field(
        None,
        alias="required",
        title="Are the capabilities required?",
        description=(
            "Whether or not the test execution will require the given "
            "capabilities of the server in order for this test script to execute."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    validated: bool = Field(
        None,
        alias="validated",
        title="Are the capabilities validated?",
        description=(
            "Whether or not the test execution will validate the given "
            "capabilities of the server in order for this test script to execute."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="The expected capabilities of the server",
        element_property=True,
    )

    destination: fhirtypes.Integer = Field(
        None,
        alias="destination",
        title="Which server these requirements apply to",
        description="Which server these requirements apply to.",
        # if property is element of this resource.
        element_property=True,
    )

    link: ListType[fhirtypes.Uri] = Field(
        None,
        alias="link",
        title="Links to the FHIR specification",
        description=(
            "Links to the FHIR specification that describes this "
            "interaction and the resources involved in more detail."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    conformance: fhirtypes.ReferenceType = Field(
        None,
        alias="conformance",
        title="Type 'Reference' referencing 'Conformance'  (represented as 'dict' in JSON).",
        description="Required Conformance",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Conformance"],
        element_property=True,
    )


class TestScriptSetupAction(BackboneElement):
    """A setup operation or assert to perform


    Action would contain either an operation or an assertion.
    """

    resource_type = Field("TestScriptSetupAction", const=True)

    operation: fhirtypes.TestScriptSetupActionOperationType = Field(
        None,
        alias="operation",
        title="A setup operation or assert to perform",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    assert_fhir: fhirtypes.TestScriptSetupActionAssertType = Field(
        None,
        alias="assert",
        title="The assertion to perform",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class TestScriptTestAction(BackboneElement):
    """A test operation or assert to perform


    Action would contain either an operation or an assertion.
    """

    resource_type = Field("TestScriptTestAction", const=True)

    operation: fhirtypes.TestScriptSetupActionOperationType = Field(
        None,
        alias="operation",
        title="The setup operation to perform",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    assert_fhir: fhirtypes.TestScriptSetupActionAssertType = Field(
        None,
        alias="assert",
        title="The setup assertion to perform",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class TestScriptTeardownAction(BackboneElement):
    """One or more teardown operations to perform


    The teardown action will only contain an operation.
    """

    resource_type = Field("TestScriptTeardownAction", const=True)

    operation: fhirtypes.TestScriptSetupActionOperationType = Field(
        None,
        alias="operation",
        title="The teardown operation to perform",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class TestScriptSetupActionOperation(BackboneElement):
    """The setup operation to perform


    The operation to perform.
    """

    resource_type = Field("TestScriptSetupActionOperation", const=True)

    type: fhirtypes.CodingType = Field(
        None,
        alias="type",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="The setup operation type that will be executed",
        element_property=True,
    )

    resource: fhirtypes.Code = Field(
        None,
        alias="resource",
        title="Resource type",
        description=(
            "The type of the resource. See "
            "http://hl7-fhir.github.io/resourcelist.html."
        ),
        element_property=True,
    )

    label: fhirtypes.String = Field(
        None,
        alias="label",
        title="Tracking/logging operation label",
        description="The label would be used for tracking/logging purposes by test engines.",
        element_property=True,
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Tracking/reporting operation description",
        description=(
            "The description would be used by test engines "
            "for tracking and reporting purposes."
        ),
        element_property=True,
    )

    accept: fhirtypes.Code = Field(
        None,
        alias="accept",
        title=(
            "The content-type or mime-type to use for RESTful "
            "operation in the 'Accept' header."
        ),
        description="xml | json",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities,
        # read official FHIR documentation.
        enum_values=["xml", "json"],
        element_property=True,
    )

    contentType: fhirtypes.Code = Field(
        None,
        alias="contentType",
        title=(
            "The content-type or mime-type to use for RESTful "
            "operation in the 'Content-Type' header."
        ),
        description="xml | json",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities,
        # read official FHIR documentation.
        enum_values=["xml", "json"],
        element_property=True,
    )

    destination: fhirtypes.Integer = Field(
        None,
        alias="destination",
        title="Which server to perform the operation on",
        description="Which server to perform the operation on.",
        # if property is element of this resource.
        element_property=True,
    )

    encodeRequestUrl: bool = Field(
        None,
        alias="encodeRequestUrl",
        title="Whether or not to send the request url in encoded format",
        description=(
            "Whether or not to implicitly send the request url in "
            "encoded format. The default is true to match the standard "
            "RESTful client behavior. Set to false when communicating "
            "with a server that does not support encoded url paths."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    params: fhirtypes.String = Field(
        None,
        alias="params",
        title="Explicitly defined path parameters",
        description=(
            "Path plus parameters after [type]. "
            "Used to set parts of the request URL explicitly."
        ),
        element_property=True,
    )

    requestHeader: fhirtypes.TestScriptSetupActionOperationRequestHeaderType = Field(  # noqa: B950
        None,
        alias="requestHeader",
        title="Each operation can have one ore more header elements",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    responseId: fhirtypes.Id = Field(
        None,
        alias="responseId",
        title="Fixture Id of mapped response",
        description="The fixture id (maybe new) to map to the response.",
        # if property is element of this resource.
        element_property=True,
    )

    sourceId: fhirtypes.Id = Field(
        None,
        alias="sourceId",
        title="Fixture Id of body for PUT and POST requests",
        description="The id of the fixture used as the body of a PUT or POST request.",
        # if property is element of this resource.
        element_property=True,
    )

    targetId: fhirtypes.Id = Field(
        None,
        alias="targetId",
        title=(
            "Id of fixture used for extracting the [id],  "
            "[type], and [vid] for GET requests"
        ),
        description=(
            "Id of fixture used for extracting the [id], "
            "[type], and [vid] for GET requests."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    url: fhirtypes.String = Field(
        None,
        alias="url",
        title="Request URL",
        description="Complete request URL.",
        element_property=True,
    )


class TestScriptSetupActionAssert(BackboneElement):
    """The assertion to perform

    Evaluates the results of previous operations to determine
    if the server under test behaves appropriately.
    """

    resource_type = Field("TestScriptSetupActionAssert", const=True)

    label: fhirtypes.String = Field(
        None,
        alias="label",
        title="Tracking/logging assertion label",
        description="The label would be used for tracking/logging purposes by test engines.",
        element_property=True,
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Tracking/reporting assertion description",
        description=(
            "The description would be used by test "
            "engines for tracking and reporting purposes."
        ),
        element_property=True,
    )

    direction: fhirtypes.Code = Field(
        None,
        alias="direction",
        title="The direction to use for the assertion.",
        description="response | request",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["response", "request"],
        element_property=True,
    )

    compareToSourceId: fhirtypes.String = Field(
        None,
        alias="compareToSourceId",
        title="Id of fixture used to compare the 'sourceId/path' evaluations to",
        description="Id of fixture used to compare the 'sourceId/path' evaluations to.",
        element_property=True,
    )

    compareToSourcePath: fhirtypes.String = Field(
        None,
        alias="compareToSourcePath",
        title=(
            "XPath or JSONPath expression against fixture used "
            "to compare the 'sourceId/path' evaluations to"
        ),
        description=(
            "XPath or JSONPath expression against fixture used "
            "to compare the 'sourceId/path' evaluations to."
        ),
        element_property=True,
    )

    contentType: fhirtypes.Code = Field(
        None,
        alias="contentType",
        title=(
            "The content-type or mime-type to use for RESTful "
            "operation in the 'Content-Type' header."
        ),
        description="xml | json",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["xml", "json"],
        element_property=True,
    )

    headerField: fhirtypes.String = Field(
        None,
        alias="headerField",
        title="HTTP header field name",
        description="The HTTP header field name e.g. 'Location'.",
        element_property=True,
    )

    minimumId: fhirtypes.String = Field(
        None,
        alias="minimumId",
        title="Fixture Id of minimum content resource",
        description=(
            "The ID of a fixture. Asserts that the response contains "
            "at a minimumId the fixture specified by minimumId."
        ),
        element_property=True,
    )

    navigationLinks: bool = Field(
        None,
        alias="navigationLinks",
        title="Perform validation on navigation links?",
        description=(
            "Whether or not the test execution performs "
            "validation on the bundle navigation links."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    operator: fhirtypes.Code = Field(
        None,
        alias="operator",
        title="The operator type.",
        description=(
            "equals | notEquals | in | notIn | greaterThan | "
            "lessThan | empty | notEmpty | contains | notContains"
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "equals",
            "notEquals",
            "in",
            "notIn",
            "greaterThan",
            "lessThan",
            "empty",
            "notEmpty",
            "contains",
            "notContains",
        ],
        element_property=True,
    )

    path: fhirtypes.String = Field(
        None,
        alias="path",
        title="XPath or JSONPath expression",
        description=(
            "The XPath or JSONPath expression to be evaluated against "
            "the fixture representing the response received from server."
        ),
        element_property=True,
    )

    resource: fhirtypes.Code = Field(
        None,
        alias="resource",
        title="Resource type",
        description=(
            "The type of the resource. See "
            "http://hl7-fhir.github.io/resourcelist.html."
        ),
        element_property=True,
    )

    response: fhirtypes.Code = Field(
        None,
        alias="response",
        title="Response type",
        description=(
            "okay | created | noContent | notModified | bad | "
            "forbidden | notFound | methodNotAllowed | conflict | "
            "gone | preconditionFailed | unprocessable"
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "okay",
            "created",
            "noContent",
            "notModified",
            "bad",
            "forbidden",
            "notFound",
            "methodNotAllowed",
            "conflict",
            "gone",
            "preconditionFailed",
            "unprocessable",
        ],
        element_property=True,
    )

    responseCode: fhirtypes.String = Field(
        None,
        alias="responseCode",
        title="HTTP response code to test",
        description="The value of the HTTP response code to be tested.",
        element_property=True,
    )

    sourceId: fhirtypes.Id = Field(
        None,
        alias="sourceId",
        title="Fixture Id of source expression or headerField",
        description=(
            "Fixture to evaluate the XPath/JSONPath "
            "expression or the headerField against."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    validateProfileId: fhirtypes.Id = Field(
        None,
        alias="validateProfileId",
        title="Profile Id of validation profile reference",
        description="The ID of the Profile to validate against.",
        # if property is element of this resource.
        element_property=True,
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="The value to compare to",
        description="The value to compare to.",
        element_property=True,
    )

    warningOnly: bool = Field(
        None,
        alias="warningOnly",
        title="Will this assert produce a warning only on error?",
        description=(
            "Whether or not the test execution will produce a warning "
            "only on error for this assert."
        ),
        # if property is element of this resource.
        element_property=True,
    )


class TestScriptSetupActionOperationRequestHeader(BackboneElement):
    """Each operation can have one ore more header elements


    Header elements would be used to set HTTP headers.
    """

    resource_type = Field("TestScriptSetupActionOperationRequestHeader", const=True)

    field: fhirtypes.String = Field(
        None,
        alias="field",
        title="HTTP header field name",
        description="The HTTP header field e.g. 'Accept'.",
        element_property=True,
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="HTTP headerfield value",
        description="The value of the header e.g. 'application/xml'.",
        element_property=True,
    )
