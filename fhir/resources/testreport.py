# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/TestReport
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class TestReport(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Describes the results of a TestScript execution.
    A summary of information based on the results of executing a TestScript.
    """

    resource_type = Field("TestReport", const=True)

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="External identifier",
        description=(
            "Identifier for the TestReport assigned for external purposes outside "
            "the context of FHIR."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    issued: fhirtypes.DateTime = Field(
        None,
        alias="issued",
        title="When the TestScript was executed and this TestReport was generated",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    issued__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_issued", title="Extension field for ``issued``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Informal name of the executed TestReport",
        description="A free text natural language name identifying the executed TestReport.",
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    participant: typing.List[fhirtypes.TestReportParticipantType] = Field(
        None,
        alias="participant",
        title=(
            "A participant in the test execution, either the execution engine, a "
            "client, or a server"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    result: fhirtypes.Code = Field(
        None,
        alias="result",
        title="pass | fail | pending",
        description="The overall result from the execution of the TestScript.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["pass", "fail", "pending"],
    )
    result__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_result", title="Extension field for ``result``."
    )

    score: fhirtypes.Decimal = Field(
        None,
        alias="score",
        title=(
            "The final score (percentage of tests passed) resulting from the "
            "execution of the TestScript"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    score__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_score", title="Extension field for ``score``."
    )

    setup: fhirtypes.TestReportSetupType = Field(
        None,
        alias="setup",
        title=(
            "The results of the series of required setup operations before the "
            "tests were executed"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="completed | in-progress | waiting | stopped | entered-in-error",
        description="The current state of this test report.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "completed",
            "in-progress",
            "waiting",
            "stopped",
            "entered-in-error",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    teardown: fhirtypes.TestReportTeardownType = Field(
        None,
        alias="teardown",
        title="The results of running the series of required clean up steps",
        description=(
            "The results of the series of operations required to clean up after all"
            " the tests were executed (successfully or otherwise)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    test: typing.List[fhirtypes.TestReportTestType] = Field(
        None,
        alias="test",
        title="A test executed from the test script",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    testScript: fhirtypes.Canonical = Field(
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
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["TestScript"],
    )
    testScript__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_testScript", title="Extension field for ``testScript``."
    )

    tester: fhirtypes.String = Field(
        None,
        alias="tester",
        title="Name of the tester producing this report (Organization or individual)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    tester__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1252(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class TestReportParticipant(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A participant in the test execution, either the execution engine, a client,
    or a server.
    """

    resource_type = Field("TestReportParticipant", const=True)

    display: fhirtypes.String = Field(
        None,
        alias="display",
        title="The display name of the participant",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_display", title="Extension field for ``display``."
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="test-engine | client | server",
        description="The type of participant.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["test-engine", "client", "server"],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    uri: fhirtypes.Uri = Field(
        None,
        alias="uri",
        title="The uri of the participant. An absolute URL is preferred",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_uri", title="Extension field for ``uri``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestReportParticipant`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "uri", "display"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2403(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("type", "type__ext"), ("uri", "uri__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class TestReportSetup(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The results of the series of required setup operations before the tests
    were executed.
    """

    resource_type = Field("TestReportSetup", const=True)

    action: typing.List[fhirtypes.TestReportSetupActionType] = Field(
        ...,
        alias="action",
        title="A setup operation or assert that was executed",
        description="Action would contain either an operation or an assertion.",
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("TestReportSetupAction", const=True)

    assert_fhir: fhirtypes.TestReportSetupActionAssertType = Field(
        None,
        alias="assert",
        title="The assertion to perform",
        description="The results of the assertion performed on the previous operations.",
        # if property is element of this resource.
        element_property=True,
    )

    operation: fhirtypes.TestReportSetupActionOperationType = Field(
        None,
        alias="operation",
        title="The operation to perform",
        description="The operation performed.",
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("TestReportSetupActionAssert", const=True)

    detail: fhirtypes.String = Field(
        None,
        alias="detail",
        title="A link to further details on the result",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    detail__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_detail", title="Extension field for ``detail``."
    )

    message: fhirtypes.Markdown = Field(
        None,
        alias="message",
        title="A message associated with the result",
        description="An explanatory message associated with the result.",
        # if property is element of this resource.
        element_property=True,
    )
    message__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_message", title="Extension field for ``message``."
    )

    requirement: typing.List[
        fhirtypes.TestReportSetupActionAssertRequirementType
    ] = Field(
        None,
        alias="requirement",
        title="Links or references to the testing requirements",
        description=(
            "Links or references providing traceability to the testing requirements"
            " for this assert."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    result: fhirtypes.Code = Field(
        None,
        alias="result",
        title="pass | skip | fail | warning | error",
        description="The result of this assertion.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["pass", "skip", "fail", "warning", "error"],
    )
    result__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3013(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("result", "result__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class TestReportSetupActionAssertRequirement(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Links or references to the testing requirements.
    Links or references providing traceability to the testing requirements for
    this assert.
    """

    resource_type = Field("TestReportSetupActionAssertRequirement", const=True)

    linkCanonical: fhirtypes.Canonical = Field(
        None,
        alias="linkCanonical",
        title="Link or reference to the testing requirement",
        description=(
            "Link or reference providing traceability to the testing requirement "
            "for this test."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e link[x]
        one_of_many="link",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Requirements"],
    )
    linkCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_linkCanonical", title="Extension field for ``linkCanonical``."
    )

    linkUri: fhirtypes.Uri = Field(
        None,
        alias="linkUri",
        title="Link or reference to the testing requirement",
        description=(
            "Link or reference providing traceability to the testing requirement "
            "for this test."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e link[x]
        one_of_many="link",
        one_of_many_required=False,
    )
    linkUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_linkUri", title="Extension field for ``linkUri``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestReportSetupActionAssertRequirement`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "linkUri", "linkCanonical"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_4182(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values


class TestReportSetupActionOperation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The operation to perform.
    The operation performed.
    """

    resource_type = Field("TestReportSetupActionOperation", const=True)

    detail: fhirtypes.Uri = Field(
        None,
        alias="detail",
        title="A link to further details on the result",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    detail__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_detail", title="Extension field for ``detail``."
    )

    message: fhirtypes.Markdown = Field(
        None,
        alias="message",
        title="A message associated with the result",
        description="An explanatory message associated with the result.",
        # if property is element of this resource.
        element_property=True,
    )
    message__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_message", title="Extension field for ``message``."
    )

    result: fhirtypes.Code = Field(
        None,
        alias="result",
        title="pass | skip | fail | warning | error",
        description="The result of this operation.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["pass", "skip", "fail", "warning", "error"],
    )
    result__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_result", title="Extension field for ``result``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestReportSetupActionOperation`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "result", "message", "detail"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3326(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("result", "result__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class TestReportTeardown(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The results of running the series of required clean up steps.
    The results of the series of operations required to clean up after all the
    tests were executed (successfully or otherwise).
    """

    resource_type = Field("TestReportTeardown", const=True)

    action: typing.List[fhirtypes.TestReportTeardownActionType] = Field(
        ...,
        alias="action",
        title="One or more teardown operations performed",
        description="The teardown action will only contain an operation.",
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("TestReportTeardownAction", const=True)

    operation: fhirtypes.TestReportSetupActionOperationType = Field(
        ...,
        alias="operation",
        title="The teardown operation performed",
        description="An operation would involve a REST request to a server.",
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("TestReportTest", const=True)

    action: typing.List[fhirtypes.TestReportTestActionType] = Field(
        ...,
        alias="action",
        title="A test operation or assert that was performed",
        description="Action would contain either an operation or an assertion.",
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Tracking/reporting short description of the test",
        description=(
            "A short description of the test used by test engines for tracking and "
            "reporting purposes."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Tracking/logging name of this test",
        description=(
            "The name of this test used for tracking/logging purposes by test "
            "engines."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    resource_type = Field("TestReportTestAction", const=True)

    assert_fhir: fhirtypes.TestReportSetupActionAssertType = Field(
        None,
        alias="assert",
        title="The assertion performed",
        description="The results of the assertion performed on the previous operations.",
        # if property is element of this resource.
        element_property=True,
    )

    operation: fhirtypes.TestReportSetupActionOperationType = Field(
        None,
        alias="operation",
        title="The operation performed",
        description="An operation would involve a REST request to a server.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestReportTestAction`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "operation", "assert"]
