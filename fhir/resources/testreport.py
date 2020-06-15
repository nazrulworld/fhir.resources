# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/TestReport
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class TestReport(domainresource.DomainResource):
    """ Describes the results of a TestScript execution.
    A summary of information based on the results of executing a TestScript.
    """

    resource_type = Field("TestReport", const=True)

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="External identifier",
    )

    issued: fhirtypes.DateTime = Field(
        None,
        alias="issued",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When the TestScript was executed and this TestReport was generated",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Informal name of the executed TestScript",
    )

    participant: ListType[fhirtypes.TestReportParticipantType] = Field(
        None,
        alias="participant",
        title="List of `TestReportParticipant` items (represented as `dict` in JSON)",
        description=(
            "A participant in the test execution, either the execution engine, a "
            "client, or a server"
        ),
    )

    result: fhirtypes.Code = Field(
        ...,
        alias="result",
        title="Type `Code` (represented as `dict` in JSON)",
        description="pass | fail | pending",
    )

    score: fhirtypes.Decimal = Field(
        None,
        alias="score",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description=(
            "The final score (percentage of tests passed) resulting from the "
            "execution of the TestScript"
        ),
    )

    setup: fhirtypes.TestReportSetupType = Field(
        None,
        alias="setup",
        title="Type `TestReportSetup` (represented as `dict` in JSON)",
        description=(
            "The results of the series of required setup operations before the "
            "tests were executed"
        ),
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="completed | in-progress | waiting | stopped | entered-in-error",
    )

    teardown: fhirtypes.TestReportTeardownType = Field(
        None,
        alias="teardown",
        title="Type `TestReportTeardown` (represented as `dict` in JSON)",
        description="The results of running the series of required clean up steps",
    )

    test: ListType[fhirtypes.TestReportTestType] = Field(
        None,
        alias="test",
        title="List of `TestReportTest` items (represented as `dict` in JSON)",
        description="A test executed from the test script",
    )

    testScript: fhirtypes.ReferenceType = Field(
        ...,
        alias="testScript",
        title=(
            "Type `Reference` referencing `TestScript` (represented as `dict` in "
            "JSON)"
        ),
        description=(
            "Reference to the  version-specific TestScript that was executed to "
            "produce this TestReport"
        ),
    )

    tester: fhirtypes.String = Field(
        None,
        alias="tester",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of the tester producing this report (Organization or individual)",
    )


class TestReportParticipant(backboneelement.BackboneElement):
    """ A participant in the test execution, either the execution engine, a client,
    or a server.
    """

    resource_type = Field("TestReportParticipant", const=True)

    display: fhirtypes.String = Field(
        None,
        alias="display",
        title="Type `String` (represented as `dict` in JSON)",
        description="The display name of the participant",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="test-engine | client | server",
    )

    uri: fhirtypes.Uri = Field(
        ...,
        alias="uri",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="The uri of the participant. An absolute URL is preferred",
    )


class TestReportSetup(backboneelement.BackboneElement):
    """ The results of the series of required setup operations before the tests
    were executed.
    """

    resource_type = Field("TestReportSetup", const=True)

    action: ListType[fhirtypes.TestReportSetupActionType] = Field(
        ...,
        alias="action",
        title="List of `TestReportSetupAction` items (represented as `dict` in JSON)",
        description="A setup operation or assert that was executed",
    )


class TestReportSetupAction(backboneelement.BackboneElement):
    """ A setup operation or assert that was executed.
    Action would contain either an operation or an assertion.
    """

    resource_type = Field("TestReportSetupAction", const=True)

    assert_fhir: fhirtypes.TestReportSetupActionAssertType = Field(
        None,
        alias="assert",
        title="Type `TestReportSetupActionAssert` (represented as `dict` in JSON)",
        description="The assertion to perform",
    )

    operation: fhirtypes.TestReportSetupActionOperationType = Field(
        None,
        alias="operation",
        title="Type `TestReportSetupActionOperation` (represented as `dict` in JSON)",
        description="The operation to perform",
    )


class TestReportSetupActionAssert(backboneelement.BackboneElement):
    """ The assertion to perform.
    The results of the assertion performed on the previous operations.
    """

    resource_type = Field("TestReportSetupActionAssert", const=True)

    detail: fhirtypes.String = Field(
        None,
        alias="detail",
        title="Type `String` (represented as `dict` in JSON)",
        description="A link to further details on the result",
    )

    message: fhirtypes.Markdown = Field(
        None,
        alias="message",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="A message associated with the result",
    )

    result: fhirtypes.Code = Field(
        ...,
        alias="result",
        title="Type `Code` (represented as `dict` in JSON)",
        description="pass | skip | fail | warning | error",
    )


class TestReportSetupActionOperation(backboneelement.BackboneElement):
    """ The operation to perform.
    The operation performed.
    """

    resource_type = Field("TestReportSetupActionOperation", const=True)

    detail: fhirtypes.Uri = Field(
        None,
        alias="detail",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="A link to further details on the result",
    )

    message: fhirtypes.Markdown = Field(
        None,
        alias="message",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="A message associated with the result",
    )

    result: fhirtypes.Code = Field(
        ...,
        alias="result",
        title="Type `Code` (represented as `dict` in JSON)",
        description="pass | skip | fail | warning | error",
    )


class TestReportTeardown(backboneelement.BackboneElement):
    """ The results of running the series of required clean up steps.
    The results of the series of operations required to clean up after all the
    tests were executed (successfully or otherwise).
    """

    resource_type = Field("TestReportTeardown", const=True)

    action: ListType[fhirtypes.TestReportTeardownActionType] = Field(
        ...,
        alias="action",
        title=(
            "List of `TestReportTeardownAction` items (represented as `dict` in "
            "JSON)"
        ),
        description="One or more teardown operations performed",
    )


class TestReportTeardownAction(backboneelement.BackboneElement):
    """ One or more teardown operations performed.
    The teardown action will only contain an operation.
    """

    resource_type = Field("TestReportTeardownAction", const=True)

    operation: fhirtypes.TestReportSetupActionOperationType = Field(
        ...,
        alias="operation",
        title="Type `TestReportSetupActionOperation` (represented as `dict` in JSON)",
        description="The teardown operation performed",
    )


class TestReportTest(backboneelement.BackboneElement):
    """ A test executed from the test script.
    """

    resource_type = Field("TestReportTest", const=True)

    action: ListType[fhirtypes.TestReportTestActionType] = Field(
        ...,
        alias="action",
        title="List of `TestReportTestAction` items (represented as `dict` in JSON)",
        description="A test operation or assert that was performed",
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


class TestReportTestAction(backboneelement.BackboneElement):
    """ A test operation or assert that was performed.
    Action would contain either an operation or an assertion.
    """

    resource_type = Field("TestReportTestAction", const=True)

    assert_fhir: fhirtypes.TestReportSetupActionAssertType = Field(
        None,
        alias="assert",
        title="Type `TestReportSetupActionAssert` (represented as `dict` in JSON)",
        description="The assertion performed",
    )

    operation: fhirtypes.TestReportSetupActionOperationType = Field(
        None,
        alias="operation",
        title="Type `TestReportSetupActionOperation` (represented as `dict` in JSON)",
        description="The operation performed",
    )
