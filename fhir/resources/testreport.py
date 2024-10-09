from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/TestReport
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class TestReport(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Describes the results of a TestScript execution.
    A summary of information based on the results of executing a TestScript.
    """

    __resource_type__ = "TestReport"

    identifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="External identifier",
        description=(
            "Identifier for the TestReport assigned for external purposes outside "
            "the context of FHIR."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    issued: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="issued",
        title="When the TestScript was executed and this TestReport was generated",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    issued__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_issued", title="Extension field for ``issued``."
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Informal name of the executed TestReport",
        description="A free text natural language name identifying the executed TestReport.",
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    participant: typing.List[fhirtypes.TestReportParticipantType] | None = Field(  # type: ignore
        None,
        alias="participant",
        title=(
            "A participant in the test execution, either the execution engine, a "
            "client, or a server"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    result: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="result",
        title="pass | fail | pending",
        description="The overall result from the execution of the TestScript.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["pass", "fail", "pending"],
        },
    )
    result__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_result", title="Extension field for ``result``."
    )

    score: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="score",
        title=(
            "The final score (percentage of tests passed) resulting from the "
            "execution of the TestScript"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    score__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_score", title="Extension field for ``score``."
    )

    setup: fhirtypes.TestReportSetupType | None = Field(  # type: ignore
        None,
        alias="setup",
        title=(
            "The results of the series of required setup operations before the "
            "tests were executed"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="completed | in-progress | waiting | stopped | entered-in-error",
        description="The current state of this test report.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "completed",
                "in-progress",
                "waiting",
                "stopped",
                "entered-in-error",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    teardown: fhirtypes.TestReportTeardownType | None = Field(  # type: ignore
        None,
        alias="teardown",
        title="The results of running the series of required clean up steps",
        description=(
            "The results of the series of operations required to clean up after all"
            " the tests were executed (successfully or otherwise)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    test: typing.List[fhirtypes.TestReportTestType] | None = Field(  # type: ignore
        None,
        alias="test",
        title="A test executed from the test script",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    testScript: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="testScript",
        title=(
            "Canonical URL to the  version-specific TestScript that was executed to"
            " produce this TestReport"
        ),
        description=(
            "Ideally this is an absolute URL that is used to identify the version-"
            "specific TestScript that was executed, matching the `TestScript.url`."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["TestScript"],
        },
    )
    testScript__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_testScript", title="Extension field for ``testScript``."
    )

    tester: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="tester",
        title="Name of the tester producing this report (Organization or individual)",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    tester__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_tester", title="Extension field for ``tester``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestReport`` according specification,
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
            "identifier",
            "name",
            "status",
            "testScript",
            "result",
            "score",
            "tester",
            "issued",
            "participant",
            "setup",
            "test",
            "teardown",
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
            ("result", "result__ext"),
            ("status", "status__ext"),
            ("testScript", "testScript__ext"),
        ]
        return required_fields


class TestReportParticipant(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A participant in the test execution, either the execution engine, a client,
    or a server.
    """

    __resource_type__ = "TestReportParticipant"

    display: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="display",
        title="The display name of the participant",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_display", title="Extension field for ``display``."
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="test-engine | client | server",
        description="The type of participant.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["test-engine", "client", "server"],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    uri: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="uri",
        title="The uri of the participant. An absolute URL is preferred",
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_uri", title="Extension field for ``uri``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestReportParticipant`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "uri", "display"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("type", "type__ext"), ("uri", "uri__ext")]
        return required_fields


class TestReportSetup(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The results of the series of required setup operations before the tests
    were executed.
    """

    __resource_type__ = "TestReportSetup"

    action: typing.List[fhirtypes.TestReportSetupActionType] = Field(  # type: ignore
        ...,
        alias="action",
        title="A setup operation or assert that was executed",
        description="Action would contain either an operation or an assertion.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestReportSetup`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "action"]


class TestReportSetupAction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A setup operation or assert that was executed.
    Action would contain either an operation or an assertion.
    """

    __resource_type__ = "TestReportSetupAction"

    assert_fhir: fhirtypes.TestReportSetupActionAssertType | None = Field(  # type: ignore
        None,
        alias="assert",
        title="The assertion to perform",
        description="The results of the assertion performed on the previous operations.",
        json_schema_extra={
            "element_property": True,
        },
    )

    operation: fhirtypes.TestReportSetupActionOperationType | None = Field(  # type: ignore
        None,
        alias="operation",
        title="The operation to perform",
        description="The operation performed.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestReportSetupAction`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "operation", "assert"]


class TestReportSetupActionAssert(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The assertion to perform.
    The results of the assertion performed on the previous operations.
    """

    __resource_type__ = "TestReportSetupActionAssert"

    detail: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="detail",
        title="A link to further details on the result",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    detail__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_detail", title="Extension field for ``detail``."
    )

    message: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="message",
        title="A message associated with the result",
        description="An explanatory message associated with the result.",
        json_schema_extra={
            "element_property": True,
        },
    )
    message__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_message", title="Extension field for ``message``."
    )

    requirement: typing.List[fhirtypes.TestReportSetupActionAssertRequirementType] | None = Field(  # type: ignore
        None,
        alias="requirement",
        title="Links or references to the testing requirements",
        description=(
            "Links or references providing traceability to the testing requirements"
            " for this assert."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    result: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="result",
        title="pass | skip | fail | warning | error",
        description="The result of this assertion.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["pass", "skip", "fail", "warning", "error"],
        },
    )
    result__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_result", title="Extension field for ``result``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestReportSetupActionAssert`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "result",
            "message",
            "detail",
            "requirement",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("result", "result__ext")]
        return required_fields


class TestReportSetupActionAssertRequirement(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Links or references to the testing requirements.
    Links or references providing traceability to the testing requirements for
    this assert.
    """

    __resource_type__ = "TestReportSetupActionAssertRequirement"

    linkCanonical: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="linkCanonical",
        title="Link or reference to the testing requirement",
        description=(
            "Link or reference providing traceability to the testing requirement "
            "for this test."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e link[x]
            "one_of_many": "link",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Requirements"],
        },
    )
    linkCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_linkCanonical", title="Extension field for ``linkCanonical``."
    )

    linkUri: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="linkUri",
        title="Link or reference to the testing requirement",
        description=(
            "Link or reference providing traceability to the testing requirement "
            "for this test."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e link[x]
            "one_of_many": "link",
            "one_of_many_required": False,
        },
    )
    linkUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_linkUri", title="Extension field for ``linkUri``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestReportSetupActionAssertRequirement`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "linkUri", "linkCanonical"]

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
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
        one_of_many_fields = {"link": ["linkCanonical", "linkUri"]}
        return one_of_many_fields


class TestReportSetupActionOperation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The operation to perform.
    The operation performed.
    """

    __resource_type__ = "TestReportSetupActionOperation"

    detail: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="detail",
        title="A link to further details on the result",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    detail__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_detail", title="Extension field for ``detail``."
    )

    message: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="message",
        title="A message associated with the result",
        description="An explanatory message associated with the result.",
        json_schema_extra={
            "element_property": True,
        },
    )
    message__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_message", title="Extension field for ``message``."
    )

    result: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="result",
        title="pass | skip | fail | warning | error",
        description="The result of this operation.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["pass", "skip", "fail", "warning", "error"],
        },
    )
    result__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_result", title="Extension field for ``result``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestReportSetupActionOperation`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "result", "message", "detail"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("result", "result__ext")]
        return required_fields


class TestReportTeardown(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The results of running the series of required clean up steps.
    The results of the series of operations required to clean up after all the
    tests were executed (successfully or otherwise).
    """

    __resource_type__ = "TestReportTeardown"

    action: typing.List[fhirtypes.TestReportTeardownActionType] = Field(  # type: ignore
        ...,
        alias="action",
        title="One or more teardown operations performed",
        description="The teardown action will only contain an operation.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestReportTeardown`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "action"]


class TestReportTeardownAction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    One or more teardown operations performed.
    The teardown action will only contain an operation.
    """

    __resource_type__ = "TestReportTeardownAction"

    operation: fhirtypes.TestReportSetupActionOperationType = Field(  # type: ignore
        ...,
        alias="operation",
        title="The teardown operation performed",
        description="An operation would involve a REST request to a server.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestReportTeardownAction`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "operation"]


class TestReportTest(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A test executed from the test script.
    """

    __resource_type__ = "TestReportTest"

    action: typing.List[fhirtypes.TestReportTestActionType] = Field(  # type: ignore
        ...,
        alias="action",
        title="A test operation or assert that was performed",
        description="Action would contain either an operation or an assertion.",
        json_schema_extra={
            "element_property": True,
        },
    )

    description: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Tracking/reporting short description of the test",
        description=(
            "A short description of the test used by test engines for tracking and "
            "reporting purposes."
        ),
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
        title="Tracking/logging name of this test",
        description=(
            "The name of this test used for tracking/logging purposes by test "
            "engines."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestReportTest`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "name", "description", "action"]


class TestReportTestAction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A test operation or assert that was performed.
    Action would contain either an operation or an assertion.
    """

    __resource_type__ = "TestReportTestAction"

    assert_fhir: fhirtypes.TestReportSetupActionAssertType | None = Field(  # type: ignore
        None,
        alias="assert",
        title="The assertion performed",
        description="The results of the assertion performed on the previous operations.",
        json_schema_extra={
            "element_property": True,
        },
    )

    operation: fhirtypes.TestReportSetupActionOperationType | None = Field(  # type: ignore
        None,
        alias="operation",
        title="The operation performed",
        description="An operation would involve a REST request to a server.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestReportTestAction`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "operation", "assert"]
