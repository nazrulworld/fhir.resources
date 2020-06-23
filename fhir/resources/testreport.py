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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Describes the results of a TestScript execution.
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
        title="Type `DateTime`",
        description="When the TestScript was executed and this TestReport was generated",
    )
    issued__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_issued", title="Extension field for ``issued``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`",
        description="Informal name of the executed TestScript",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
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
        ..., alias="result", title="Type `Code`", description="pass | fail | pending"
    )
    result__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_result", title="Extension field for ``result``."
    )

    score: fhirtypes.Decimal = Field(
        None,
        alias="score",
        title="Type `Decimal`",
        description=(
            "The final score (percentage of tests passed) resulting from the "
            "execution of the TestScript"
        ),
    )
    score__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_score", title="Extension field for ``score``."
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
        title="Type `Code`",
        description="completed | in-progress | waiting | stopped | entered-in-error",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
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
        title="Type `String`",
        description="Name of the tester producing this report (Organization or individual)",
    )
    tester__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_tester", title="Extension field for ``tester``."
    )


class TestReportParticipant(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A participant in the test execution, either the execution engine, a client,
    or a server.
    """

    resource_type = Field("TestReportParticipant", const=True)

    display: fhirtypes.String = Field(
        None,
        alias="display",
        title="Type `String`",
        description="The display name of the participant",
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_display", title="Extension field for ``display``."
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code`",
        description="test-engine | client | server",
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    uri: fhirtypes.Uri = Field(
        ...,
        alias="uri",
        title="Type `Uri`",
        description="The uri of the participant. An absolute URL is preferred",
    )
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_uri", title="Extension field for ``uri``."
    )


class TestReportSetup(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The results of the series of required setup operations before the tests
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A setup operation or assert that was executed.
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The assertion to perform.
    The results of the assertion performed on the previous operations.
    """

    resource_type = Field("TestReportSetupActionAssert", const=True)

    detail: fhirtypes.String = Field(
        None,
        alias="detail",
        title="Type `String`",
        description="A link to further details on the result",
    )
    detail__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_detail", title="Extension field for ``detail``."
    )

    message: fhirtypes.Markdown = Field(
        None,
        alias="message",
        title="Type `Markdown`",
        description="A message associated with the result",
    )
    message__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_message", title="Extension field for ``message``."
    )

    result: fhirtypes.Code = Field(
        ...,
        alias="result",
        title="Type `Code`",
        description="pass | skip | fail | warning | error",
    )
    result__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_result", title="Extension field for ``result``."
    )


class TestReportSetupActionOperation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The operation to perform.
    The operation performed.
    """

    resource_type = Field("TestReportSetupActionOperation", const=True)

    detail: fhirtypes.Uri = Field(
        None,
        alias="detail",
        title="Type `Uri`",
        description="A link to further details on the result",
    )
    detail__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_detail", title="Extension field for ``detail``."
    )

    message: fhirtypes.Markdown = Field(
        None,
        alias="message",
        title="Type `Markdown`",
        description="A message associated with the result",
    )
    message__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_message", title="Extension field for ``message``."
    )

    result: fhirtypes.Code = Field(
        ...,
        alias="result",
        title="Type `Code`",
        description="pass | skip | fail | warning | error",
    )
    result__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_result", title="Extension field for ``result``."
    )


class TestReportTeardown(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The results of running the series of required clean up steps.
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    One or more teardown operations performed.
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A test executed from the test script.
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


class TestReportTestAction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A test operation or assert that was performed.
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
