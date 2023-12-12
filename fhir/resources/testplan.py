# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/TestPlan
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class TestPlan(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Description of intented testing.
    A plan for executing testing on an artifact or specifications.
    """

    resource_type = Field("TestPlan", const=True)

    category: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="The category of the Test Plan - can be acceptance, unit, performance",
        description=(
            "The category of the Test Plan - can be acceptance, unit, performance, "
            "etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    contact: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="Contact details for the publisher",
        description=(
            "Contact details to assist a user in finding and communicating with the"
            " publisher."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the test plan and/or its contents. "
            "Copyright statements are generally legal restrictions on the use and "
            "publishing of the test plan. The short copyright declaration (e.g. (c)"
            " '2015+ xyz organization' should be sent in the copyrightLabel "
            "element."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    copyrightLabel: fhirtypes.String = Field(
        None,
        alias="copyrightLabel",
        title="Copyright holder and year(s)",
        description=(
            "A short string (<50 characters), suitable for inclusion in a page "
            "footer that identifies the copyright holder, effective period, and "
            "optionally whether rights are resctricted. (e.g. 'All rights "
            "reserved', 'Some rights reserved')."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    copyrightLabel__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyrightLabel", title="Extension field for ``copyrightLabel``."
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date last changed",
        description=(
            "The date (and optionally time) when the test plan was last "
            "significantly changed. The date must change when the business version "
            "changes and it must change if the status code changes. In addition, it"
            " should change when the substantive content of the test plan changes."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    dependency: typing.List[fhirtypes.TestPlanDependencyType] = Field(
        None,
        alias="dependency",
        title=(
            "The required criteria to execute the test plan - e.g. preconditions, "
            "previous tests"
        ),
        description=(
            "The required criteria to execute the test plan - e.g. preconditions, "
            "previous tests..."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Natural language description of the test plan",
        description=(
            "A free text natural language description of the test plan from a "
            "consumer's perspective."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    exitCriteria: fhirtypes.Markdown = Field(
        None,
        alias="exitCriteria",
        title=(
            "The threshold or criteria for the test plan to be considered "
            "successfully executed - narrative"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    exitCriteria__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_exitCriteria", title="Extension field for ``exitCriteria``."
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this test plan is authored for "
            "testing purposes (or education/evaluation/marketing) and is not "
            "intended to be used for genuine usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier identifier for the test plan",
        description=(
            "A formal identifier that is used to identify this test plan when it is"
            " represented in other formats, or referenced in a specification, "
            "model, design or an instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction where the test plan applies (if applicable)",
        description=(
            "A legal or geographic region in which the test plan is intended to be "
            "used."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name for this test plan (computer friendly)",
        description=(
            "A natural language name identifying the test plan. This name should be"
            " usable as an identifier for the module by machine processing "
            "applications such as code generation."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher/steward (organization or individual)",
        description=(
            "The name of the organization or individual responsible for the release"
            " and ongoing maintenance of the test plan."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Why this test plan is defined",
        description=(
            "Explanation of why this test plan is needed and why it has been "
            "designed as it has."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    scope: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="scope",
        title=(
            "What is being tested with this Test Plan - a conformance resource, or "
            "narrative criteria, or an external reference"
        ),
        description=(
            "What is being tested with this Test Plan - a conformance resource, or "
            "narrative criteria, or an external reference..."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this test plan. Enables tracking the life-cycle of the "
            "content."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired", "unknown"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    testCase: typing.List[fhirtypes.TestPlanTestCaseType] = Field(
        None,
        alias="testCase",
        title="The test cases that constitute this plan",
        description=(
            "The individual test cases that are part of this plan, when they they "
            "are made explicit."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    testTools: fhirtypes.Markdown = Field(
        None,
        alias="testTools",
        title=(
            "A description of test tools to be used in the test plan - narrative "
            "for now"
        ),
        description="A description of test tools to be used in the test plan.",
        # if property is element of this resource.
        element_property=True,
    )
    testTools__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_testTools", title="Extension field for ``testTools``."
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Name for this test plan (human friendly)",
        description="A short, descriptive, user-friendly title for the test plan.",
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title=(
            "Canonical identifier for this test plan, represented as a URI "
            "(globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this test plan when it is "
            "referenced in a specification, model, design or an instance; also "
            "called its canonical identifier. This SHOULD be globally unique and "
            "SHOULD be a literal address at which an authoritative instance of this"
            " test plan is (or will be) published. This URL can be the target of a "
            "canonical reference. It SHALL remain the same when the test plan is "
            "stored on different servers."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    useContext: typing.List[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="The context that the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These contexts may be general categories "
            "(gender, age, ...) or may be references to specific programs "
            "(insurance plans, studies, ...) and may be used to assist with "
            "indexing and searching for appropriate test plan instances."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the test plan",
        description=(
            "The identifier that is used to identify this version of the test plan "
            "when it is referenced in a specification, model, design or instance.  "
            "This is an arbitrary value managed by the test plan author and is not "
            "expected to be globally unique. For example, it might be a timestamp "
            "(e.g. yyyymmdd) if a managed version is not available. There is also "
            "no expectation that versions can be placed in a lexicographical "
            "sequence."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    versionAlgorithmCoding: fhirtypes.CodingType = Field(
        None,
        alias="versionAlgorithmCoding",
        title="How to compare versions",
        description=(
            "Indicates the mechanism used to compare versions to determine which is"
            " more current."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e versionAlgorithm[x]
        one_of_many="versionAlgorithm",
        one_of_many_required=False,
    )

    versionAlgorithmString: fhirtypes.String = Field(
        None,
        alias="versionAlgorithmString",
        title="How to compare versions",
        description=(
            "Indicates the mechanism used to compare versions to determine which is"
            " more current."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e versionAlgorithm[x]
        one_of_many="versionAlgorithm",
        one_of_many_required=False,
    )
    versionAlgorithmString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_versionAlgorithmString",
        title="Extension field for ``versionAlgorithmString``.",
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestPlan`` according specification,
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
            "url",
            "identifier",
            "version",
            "versionAlgorithmString",
            "versionAlgorithmCoding",
            "name",
            "title",
            "status",
            "experimental",
            "date",
            "publisher",
            "contact",
            "description",
            "useContext",
            "jurisdiction",
            "purpose",
            "copyright",
            "copyrightLabel",
            "category",
            "scope",
            "testTools",
            "dependency",
            "exitCriteria",
            "testCase",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1005(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1005(
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
        one_of_many_fields = {
            "versionAlgorithm": ["versionAlgorithmCoding", "versionAlgorithmString"]
        }
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


class TestPlanDependency(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The required criteria to execute the test plan - e.g. preconditions,
    previous tests.
    The required criteria to execute the test plan - e.g. preconditions,
    previous tests...
    """

    resource_type = Field("TestPlanDependency", const=True)

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Description of the dependency criterium",
        description=(
            "A textual description of the criterium - what is needed for the "
            "dependency to be considered met."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    predecessor: fhirtypes.ReferenceType = Field(
        None,
        alias="predecessor",
        title="Link to predecessor test plans",
        description=(
            "Predecessor test plans - those that are expected to be successfully "
            "performed as a dependency for the execution of this test plan."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestPlanDependency`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "description", "predecessor"]


class TestPlanTestCase(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The test cases that constitute this plan.
    The individual test cases that are part of this plan, when they they are
    made explicit.
    """

    resource_type = Field("TestPlanTestCase", const=True)

    assertion: typing.List[fhirtypes.TestPlanTestCaseAssertionType] = Field(
        None,
        alias="assertion",
        title="Test assertions or expectations",
        description=(
            "The test assertions - the expectations of test results from the "
            "execution of the test case."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    dependency: typing.List[fhirtypes.TestPlanTestCaseDependencyType] = Field(
        None,
        alias="dependency",
        title="Required criteria to execute the test case",
        description=(
            "The required criteria to execute the test case - e.g. preconditions, "
            "previous tests."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    scope: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="scope",
        title="The scope or artifact covered by the case",
        description=(
            "The scope or artifact covered by the case, when the individual test "
            "case is associated with a testable artifact."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    sequence: fhirtypes.Integer = Field(
        None,
        alias="sequence",
        title="Sequence of test case in the test plan",
        description=(
            "Sequence of test case - an ordinal number that indicates the order for"
            " the present test case in the test plan."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    testData: typing.List[fhirtypes.TestPlanTestCaseTestDataType] = Field(
        None,
        alias="testData",
        title="The test data used in the test case",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    testRun: typing.List[fhirtypes.TestPlanTestCaseTestRunType] = Field(
        None,
        alias="testRun",
        title="The actual test to be executed",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestPlanTestCase`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "scope",
            "dependency",
            "testRun",
            "testData",
            "assertion",
        ]


class TestPlanTestCaseAssertion(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Test assertions or expectations.
    The test assertions - the expectations of test results from the execution
    of the test case.
    """

    resource_type = Field("TestPlanTestCaseAssertion", const=True)

    object: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="object",
        title="The focus or object of the assertion",
        description="The focus or object of the assertion i.e. a resource.",
        # if property is element of this resource.
        element_property=True,
    )

    result: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="result",
        title="The actual result assertion",
        description=(
            "The test assertion - the expected outcome from the test case " "execution."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="Assertion type - for example 'informative' or 'required' ",
        description=(
            "The test assertion type - this can be used to group assertions as "
            "'required' or 'optional', or can be used for other classification of "
            "the assertion."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestPlanTestCaseAssertion`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "object", "result"]


class TestPlanTestCaseDependency(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Required criteria to execute the test case.
    The required criteria to execute the test case - e.g. preconditions,
    previous tests.
    """

    resource_type = Field("TestPlanTestCaseDependency", const=True)

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Description of the criteria",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    predecessor: fhirtypes.ReferenceType = Field(
        None,
        alias="predecessor",
        title="Link to predecessor test plans",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestPlanTestCaseDependency`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "description", "predecessor"]


class TestPlanTestCaseTestData(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The test data used in the test case.
    """

    resource_type = Field("TestPlanTestCaseTestData", const=True)

    content: fhirtypes.ReferenceType = Field(
        None,
        alias="content",
        title="The actual test resources when they exist",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    sourceReference: fhirtypes.ReferenceType = Field(
        None,
        alias="sourceReference",
        title=(
            "Pointer to a definition of test resources - narrative or structured "
            "e.g. synthetic data generation, etc"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e source[x]
        one_of_many="source",
        one_of_many_required=False,
    )

    sourceString: fhirtypes.String = Field(
        None,
        alias="sourceString",
        title=(
            "Pointer to a definition of test resources - narrative or structured "
            "e.g. synthetic data generation, etc"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e source[x]
        one_of_many="source",
        one_of_many_required=False,
    )
    sourceString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sourceString", title="Extension field for ``sourceString``."
    )

    type: fhirtypes.CodingType = Field(
        ...,
        alias="type",
        title="The type of test data description, e.g. 'synthea'",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestPlanTestCaseTestData`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "content",
            "sourceString",
            "sourceReference",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2582(
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
        one_of_many_fields = {"source": ["sourceReference", "sourceString"]}
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


class TestPlanTestCaseTestRun(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The actual test to be executed.
    """

    resource_type = Field("TestPlanTestCaseTestRun", const=True)

    narrative: fhirtypes.Markdown = Field(
        None,
        alias="narrative",
        title="The narrative description of the tests",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    narrative__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_narrative", title="Extension field for ``narrative``."
    )

    script: fhirtypes.TestPlanTestCaseTestRunScriptType = Field(
        None,
        alias="script",
        title=(
            "The test cases in a structured language e.g. gherkin, Postman, or FHIR"
            " TestScript"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestPlanTestCaseTestRun`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "narrative", "script"]


class TestPlanTestCaseTestRunScript(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The test cases in a structured language e.g. gherkin, Postman, or FHIR
    TestScript.
    """

    resource_type = Field("TestPlanTestCaseTestRunScript", const=True)

    language: fhirtypes.CodeableConceptType = Field(
        None,
        alias="language",
        title="The language for the test cases e.g. 'gherkin', 'testscript'",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    sourceReference: fhirtypes.ReferenceType = Field(
        None,
        alias="sourceReference",
        title=(
            "The actual content of the cases - references to TestScripts or "
            "externally defined content"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e source[x]
        one_of_many="source",
        one_of_many_required=False,
    )

    sourceString: fhirtypes.String = Field(
        None,
        alias="sourceString",
        title=(
            "The actual content of the cases - references to TestScripts or "
            "externally defined content"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e source[x]
        one_of_many="source",
        one_of_many_required=False,
    )
    sourceString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sourceString", title="Extension field for ``sourceString``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestPlanTestCaseTestRunScript`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "language",
            "sourceString",
            "sourceReference",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3161(
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
        one_of_many_fields = {"source": ["sourceReference", "sourceString"]}
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
