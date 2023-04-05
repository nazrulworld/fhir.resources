# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/TestScript
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


class TestScript(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Describes a set of tests.
    A structured set of tests against a FHIR server or client implementation to
    determine compliance against the FHIR specification.
    """

    resource_type = Field("TestScript", const=True)

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
            "A copyright statement relating to the test script and/or its contents."
            " Copyright statements are generally legal restrictions on the use and "
            "publishing of the test script."
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
            "The date (and optionally time) when the test script was last "
            "significantly changed. The date must change when the business version "
            "changes and it must change if the status code changes. In addition, it"
            " should change when the substantive content of the test script "
            "changes."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Natural language description of the test script",
        description=(
            "A free text natural language description of the test script from a "
            "consumer's perspective."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    destination: typing.List[fhirtypes.TestScriptDestinationType] = Field(
        None,
        alias="destination",
        title=(
            "An abstract server representing a destination or receiver in a message"
            " exchange"
        ),
        description=(
            "An abstract server used in operations within this test script in the "
            "destination element."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this test script is authored for "
            "testing purposes (or education/evaluation/marketing) and is not "
            "intended to be used for genuine usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    fixture: typing.List[fhirtypes.TestScriptFixtureType] = Field(
        None,
        alias="fixture",
        title="Fixture in the test script - by reference (uri)",
        description=(
            "Fixture in the test script - by reference (uri). All fixtures are "
            "required for the test script to execute."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Additional identifier for the test script",
        description=(
            "A formal identifier that is used to identify this test script when it "
            "is represented in other formats, or referenced in a specification, "
            "model, design or an instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for test script (if applicable)",
        description=(
            "A legal or geographic region in which the test script is intended to "
            "be used."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    metadata: fhirtypes.TestScriptMetadataType = Field(
        None,
        alias="metadata",
        title=(
            "Required capability that is assumed to function correctly on the FHIR "
            "server being tested"
        ),
        description=(
            "The required capability must exist and are assumed to function "
            "correctly on the FHIR server being tested."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name for this test script (computer friendly)",
        description=(
            "A natural language name identifying the test script. This name should "
            "be usable as an identifier for the module by machine processing "
            "applications such as code generation."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    origin: typing.List[fhirtypes.TestScriptOriginType] = Field(
        None,
        alias="origin",
        title=(
            "An abstract server representing a client or sender in a message "
            "exchange"
        ),
        description=(
            "An abstract server used in operations within this test script in the "
            "origin element."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    profile: typing.List[typing.Optional[fhirtypes.Canonical]] = Field(
        None,
        alias="profile",
        title="Reference of the validation profile",
        description="Reference to the profile to be used for validation.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureDefinition"],
    )
    profile__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_profile", title="Extension field for ``profile``.")

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher/steward (organization or individual)",
        description=(
            "The name of the organization or individual responsible for the release"
            " and ongoing maintenance of the test script."
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
        title="Why this test script is defined",
        description=(
            "Explanation of why this test script is needed and why it has been "
            "designed as it has."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    scope: typing.List[fhirtypes.TestScriptScopeType] = Field(
        None,
        alias="scope",
        title="Indication of the artifact(s) that are tested by this test case",
        description=(
            "The scope indicates a conformance artifact that is tested by the "
            "test(s) within this test case and the expectation of the test "
            "outcome(s) as well as the intended test phase inclusion."
        ),
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

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this test script. Enables tracking the life-cycle of the"
            " content."
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

    teardown: fhirtypes.TestScriptTeardownType = Field(
        None,
        alias="teardown",
        title="A series of required clean up steps",
        description=(
            "A series of operations required to clean up after all the tests are "
            "executed (successfully or otherwise)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    test: typing.List[fhirtypes.TestScriptTestType] = Field(
        None,
        alias="test",
        title="A test in this script",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Name for this test script (human friendly)",
        description="A short, descriptive, user-friendly title for the test script.",
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
            "Canonical identifier for this test script, represented as a URI "
            "(globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this test script when it is "
            "referenced in a specification, model, design or an instance; also "
            "called its canonical identifier. This SHOULD be globally unique and "
            "SHOULD be a literal address at which an authoritative instance of this"
            " test script is (or will be) published. This URL can be the target of "
            "a canonical reference. It SHALL remain the same when the test script "
            "is stored on different servers."
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
            "indexing and searching for appropriate test script instances."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    variable: typing.List[fhirtypes.TestScriptVariableType] = Field(
        None,
        alias="variable",
        title="Placeholder for evaluated elements",
        description=(
            "Variable is set based either on element value in response body or on "
            "header field value in the response headers."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the test script",
        description=(
            "The identifier that is used to identify this version of the test "
            "script when it is referenced in a specification, model, design or "
            "instance. This is an arbitrary value managed by the test script author"
            " and is not expected to be globally unique. For example, it might be a"
            " timestamp (e.g. yyyymmdd) if a managed version is not available. "
            "There is also no expectation that versions can be placed in a "
            "lexicographical sequence."
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
        ``TestScript`` according specification,
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
            "origin",
            "destination",
            "metadata",
            "scope",
            "fixture",
            "profile",
            "variable",
            "setup",
            "test",
            "teardown",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1245(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("name", "name__ext"), ("status", "status__ext")]
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
    def validate_one_of_many_1245(
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


class TestScriptDestination(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An abstract server representing a destination or receiver in a message
    exchange.
    An abstract server used in operations within this test script in the
    destination element.
    """

    resource_type = Field("TestScriptDestination", const=True)

    index: fhirtypes.Integer = Field(
        None,
        alias="index",
        title="The index of the abstract destination server starting at 1",
        description=(
            "Abstract name given to a destination server in this test script.  The "
            "name is provided as a number starting at 1."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    index__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_index", title="Extension field for ``index``."
    )

    profile: fhirtypes.CodingType = Field(
        ...,
        alias="profile",
        title=(
            "FHIR-Server | FHIR-SDC-FormManager | FHIR-SDC-FormReceiver | FHIR-SDC-"
            "FormProcessor"
        ),
        description="The type of destination profile the test system supports.",
        # if property is element of this resource.
        element_property=True,
    )

    url: fhirtypes.Url = Field(
        None,
        alias="url",
        title="The url path of the destination server",
        description=(
            "The explicit url path of the destination server used in this test "
            "script."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestScriptDestination`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "index", "profile", "url"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2393(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("index", "index__ext")]
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


class TestScriptFixture(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
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
        title="Whether or not to implicitly create the fixture during setup",
        description=(
            "Whether or not to implicitly create the fixture during setup. If true,"
            " the fixture is automatically created on each server being tested "
            "during setup, therefore no create operation is required for this "
            "fixture in the TestScript.setup section."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    autocreate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_autocreate", title="Extension field for ``autocreate``."
    )

    autodelete: bool = Field(
        None,
        alias="autodelete",
        title="Whether or not to implicitly delete the fixture during teardown",
        description=(
            "Whether or not to implicitly delete the fixture during teardown. If "
            "true, the fixture is automatically deleted on each server being tested"
            " during teardown, therefore no delete operation is required for this "
            "fixture in the TestScript.teardown section."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    autodelete__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_autodelete", title="Extension field for ``autodelete``."
    )

    resource: fhirtypes.ReferenceType = Field(
        None,
        alias="resource",
        title="Reference of the resource",
        description=(
            "Reference to the resource (containing the contents of the resource "
            "needed for operations). This is allowed to be a Parameters resource."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestScriptFixture`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "autocreate",
            "autodelete",
            "resource",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1973(
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
            ("autocreate", "autocreate__ext"),
            ("autodelete", "autodelete__ext"),
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


class TestScriptMetadata(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Required capability that is assumed to function correctly on the FHIR
    server being tested.
    The required capability must exist and are assumed to function correctly on
    the FHIR server being tested.
    """

    resource_type = Field("TestScriptMetadata", const=True)

    capability: typing.List[fhirtypes.TestScriptMetadataCapabilityType] = Field(
        ...,
        alias="capability",
        title=(
            "Capabilities  that are assumed to function correctly on the FHIR "
            "server being tested"
        ),
        description=(
            "Capabilities that must exist and are assumed to function correctly on "
            "the FHIR server being tested."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    link: typing.List[fhirtypes.TestScriptMetadataLinkType] = Field(
        None,
        alias="link",
        title="Links to the FHIR specification",
        description="A link to the FHIR specification that this test is covering.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestScriptMetadata`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "link", "capability"]


class TestScriptMetadataCapability(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Capabilities  that are assumed to function correctly on the FHIR server
    being tested.
    Capabilities that must exist and are assumed to function correctly on the
    FHIR server being tested.
    """

    resource_type = Field("TestScriptMetadataCapability", const=True)

    capabilities: fhirtypes.Canonical = Field(
        None,
        alias="capabilities",
        title="Required Capability Statement",
        description=(
            "Minimum capabilities required of server for test script to execute "
            "successfully.   If server does not meet at a minimum the referenced "
            "capability statement, then all tests in this script are skipped."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["CapabilityStatement"],
    )
    capabilities__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_capabilities", title="Extension field for ``capabilities``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="The expected capabilities of the server",
        description=(
            "Description of the capabilities that this test script is requiring the"
            " server to support."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    destination: fhirtypes.Integer = Field(
        None,
        alias="destination",
        title="Which server these requirements apply to",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    destination__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_destination", title="Extension field for ``destination``."
    )

    link: typing.List[typing.Optional[fhirtypes.Uri]] = Field(
        None,
        alias="link",
        title="Links to the FHIR specification",
        description=(
            "Links to the FHIR specification that describes this interaction and "
            "the resources involved in more detail."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    link__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_link", title="Extension field for ``link``.")

    origin: typing.List[typing.Optional[fhirtypes.Integer]] = Field(
        None,
        alias="origin",
        title="Which origin server these requirements apply to",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    origin__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_origin", title="Extension field for ``origin``.")

    required: bool = Field(
        None,
        alias="required",
        title="Are the capabilities required?",
        description=(
            "Whether or not the test execution will require the given capabilities "
            "of the server in order for this test script to execute."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    required__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_required", title="Extension field for ``required``."
    )

    validated: bool = Field(
        None,
        alias="validated",
        title="Are the capabilities validated?",
        description=(
            "Whether or not the test execution will validate the given capabilities"
            " of the server in order for this test script to execute."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    validated__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_validated", title="Extension field for ``validated``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestScriptMetadataCapability`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "required",
            "validated",
            "description",
            "origin",
            "destination",
            "link",
            "capabilities",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3077(
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
            ("capabilities", "capabilities__ext"),
            ("required", "required__ext"),
            ("validated", "validated__ext"),
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


class TestScriptMetadataLink(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Links to the FHIR specification.
    A link to the FHIR specification that this test is covering.
    """

    resource_type = Field("TestScriptMetadataLink", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Short description",
        description="Short description of the link.",
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="URL to the specification",
        description=(
            "URL to a particular requirement or feature within the FHIR "
            "specification."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestScriptMetadataLink`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "url", "description"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2435(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("url", "url__ext")]
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


class TestScriptOrigin(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An abstract server representing a client or sender in a message exchange.
    An abstract server used in operations within this test script in the origin
    element.
    """

    resource_type = Field("TestScriptOrigin", const=True)

    index: fhirtypes.Integer = Field(
        None,
        alias="index",
        title="The index of the abstract origin server starting at 1",
        description=(
            "Abstract name given to an origin server in this test script.  The name"
            " is provided as a number starting at 1."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    index__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_index", title="Extension field for ``index``."
    )

    profile: fhirtypes.CodingType = Field(
        ...,
        alias="profile",
        title="FHIR-Client | FHIR-SDC-FormFiller",
        description="The type of origin profile the test system supports.",
        # if property is element of this resource.
        element_property=True,
    )

    url: fhirtypes.Url = Field(
        None,
        alias="url",
        title="The url path of the origin server",
        description="The explicit url path of the origin server used in this test script.",
        # if property is element of this resource.
        element_property=True,
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestScriptOrigin`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "index", "profile", "url"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1855(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("index", "index__ext")]
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


class TestScriptScope(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Indication of the artifact(s) that are tested by this test case.
    The scope indicates a conformance artifact that is tested by the test(s)
    within this test case and the expectation of the test outcome(s) as well as
    the intended test phase inclusion.
    """

    resource_type = Field("TestScriptScope", const=True)

    artifact: fhirtypes.Canonical = Field(
        None,
        alias="artifact",
        title="The specific conformance artifact being tested",
        description=(
            "The specific conformance artifact being tested. The canonical "
            "reference can be version-specific."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )
    artifact__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_artifact", title="Extension field for ``artifact``."
    )

    conformance: fhirtypes.CodeableConceptType = Field(
        None,
        alias="conformance",
        title="required | optional | strict",
        description=(
            "The expectation of whether the test must pass for the system to be "
            "considered conformant with the artifact: required - all tests are "
            "expected to pass, optional - all test are expected to pass but non-"
            "pass status may be allowed, strict - all tests are expected to pass "
            "and warnings are treated as a failure."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    phase: fhirtypes.CodeableConceptType = Field(
        None,
        alias="phase",
        title="unit | integration | production",
        description=(
            "The phase of testing for this artifact: unit - development / "
            "implementation phase, integration - internal system to system phase, "
            "production - live system to system phase (Note, this may involve "
            "pii/phi data)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestScriptScope`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "artifact",
            "conformance",
            "phase",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1736(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("artifact", "artifact__ext")]
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


class TestScriptSetup(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A series of required setup operations before tests are executed.
    """

    resource_type = Field("TestScriptSetup", const=True)

    action: typing.List[fhirtypes.TestScriptSetupActionType] = Field(
        ...,
        alias="action",
        title="A setup operation or assert to perform",
        description="Action would contain either an operation or an assertion.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestScriptSetup`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "action"]


class TestScriptSetupAction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A setup operation or assert to perform.
    Action would contain either an operation or an assertion.
    """

    resource_type = Field("TestScriptSetupAction", const=True)

    assert_fhir: fhirtypes.TestScriptSetupActionAssertType = Field(
        None,
        alias="assert",
        title="The assertion to perform",
        description=(
            "Evaluates the results of previous operations to determine if the "
            "server under test behaves appropriately."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    operation: fhirtypes.TestScriptSetupActionOperationType = Field(
        None,
        alias="operation",
        title="The setup operation to perform",
        description="The operation to perform.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestScriptSetupAction`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "operation", "assert"]


class TestScriptSetupActionAssert(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
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
        title="The FHIRPath expression to evaluate against the source fixture",
        description=(
            "The FHIRPath expression for a specific value to evaluate against the "
            "source fixture. When compareToSourceId is defined, either "
            "compareToSourceExpression or compareToSourcePath must be defined, but "
            "not both."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    compareToSourceExpression__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_compareToSourceExpression",
        title="Extension field for ``compareToSourceExpression``.",
    )

    compareToSourceId: fhirtypes.String = Field(
        None,
        alias="compareToSourceId",
        title="Id of the source fixture to be evaluated",
        description=(
            "Id of the source fixture used as the contents to be evaluated by "
            'either the "source/expression" or "sourceId/path" definition.'
        ),
        # if property is element of this resource.
        element_property=True,
    )
    compareToSourceId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_compareToSourceId",
        title="Extension field for ``compareToSourceId``.",
    )

    compareToSourcePath: fhirtypes.String = Field(
        None,
        alias="compareToSourcePath",
        title="XPath or JSONPath expression to evaluate against the source fixture",
        description=(
            "XPath or JSONPath expression to evaluate against the source fixture. "
            "When compareToSourceId is defined, either compareToSourceExpression or"
            " compareToSourcePath must be defined, but not both."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    compareToSourcePath__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_compareToSourcePath",
        title="Extension field for ``compareToSourcePath``.",
    )

    contentType: fhirtypes.Code = Field(
        None,
        alias="contentType",
        title="Mime type to compare against the 'Content-Type' header",
        description=(
            "The mime-type contents to compare against the request or response "
            "message 'Content-Type' header."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    contentType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_contentType", title="Extension field for ``contentType``."
    )

    defaultManualCompletion: fhirtypes.Code = Field(
        None,
        alias="defaultManualCompletion",
        title="fail | pass | skip | stop",
        description="The default manual completion outcome applied to this assertion.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["fail", "pass", "skip", "stop"],
    )
    defaultManualCompletion__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultManualCompletion",
        title="Extension field for ``defaultManualCompletion``.",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Tracking/reporting assertion description",
        description=(
            "The description would be used by test engines for tracking and "
            "reporting purposes."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    direction: fhirtypes.Code = Field(
        None,
        alias="direction",
        title="response | request",
        description="The direction to use for the assertion.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["response", "request"],
    )
    direction__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_direction", title="Extension field for ``direction``."
    )

    expression: fhirtypes.String = Field(
        None,
        alias="expression",
        title="The FHIRPath expression to be evaluated",
        description=(
            "The FHIRPath expression to be evaluated against the request or "
            "response message contents - HTTP headers and payload."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_expression", title="Extension field for ``expression``."
    )

    headerField: fhirtypes.String = Field(
        None,
        alias="headerField",
        title="HTTP header field name",
        description="The HTTP header field name e.g. 'Location'.",
        # if property is element of this resource.
        element_property=True,
    )
    headerField__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_headerField", title="Extension field for ``headerField``."
    )

    label: fhirtypes.String = Field(
        None,
        alias="label",
        title="Tracking/logging assertion label",
        description="The label would be used for tracking/logging purposes by test engines.",
        # if property is element of this resource.
        element_property=True,
    )
    label__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_label", title="Extension field for ``label``."
    )

    minimumId: fhirtypes.String = Field(
        None,
        alias="minimumId",
        title="Fixture Id of minimum content resource",
        description=(
            "The ID of a fixture. Asserts that the response contains at a minimum "
            "the fixture specified by minimumId."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    minimumId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_minimumId", title="Extension field for ``minimumId``."
    )

    navigationLinks: bool = Field(
        None,
        alias="navigationLinks",
        title="Perform validation on navigation links?",
        description=(
            "Whether or not the test execution performs validation on the bundle "
            "navigation links."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    navigationLinks__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_navigationLinks", title="Extension field for ``navigationLinks``."
    )

    operator: fhirtypes.Code = Field(
        None,
        alias="operator",
        title=(
            "equals | notEquals | in | notIn | greaterThan | lessThan | empty | "
            "notEmpty | contains | notContains | eval | manualEval"
        ),
        description="The operator type defines the conditional behavior of the assert.",
        # if property is element of this resource.
        element_property=True,
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
            "eval",
            "manualEval",
        ],
    )
    operator__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_operator", title="Extension field for ``operator``."
    )

    path: fhirtypes.String = Field(
        None,
        alias="path",
        title="XPath or JSONPath expression",
        description=(
            "The XPath or JSONPath expression to be evaluated against the fixture "
            "representing the response received from server."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_path", title="Extension field for ``path``."
    )

    requestMethod: fhirtypes.Code = Field(
        None,
        alias="requestMethod",
        title="delete | get | options | patch | post | put | head",
        description=(
            "The request method or HTTP operation code to compare against that used"
            " by the client system under test."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["delete", "get", "options", "patch", "post", "put", "head"],
    )
    requestMethod__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_requestMethod", title="Extension field for ``requestMethod``."
    )

    requestURL: fhirtypes.String = Field(
        None,
        alias="requestURL",
        title="Request URL comparison value",
        description="The value to use in a comparison against the request URL path string.",
        # if property is element of this resource.
        element_property=True,
    )
    requestURL__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_requestURL", title="Extension field for ``requestURL``."
    )

    requirement: typing.List[
        fhirtypes.TestScriptSetupActionAssertRequirementType
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

    resource: fhirtypes.Uri = Field(
        None,
        alias="resource",
        title="Resource type",
        description="The type of the resource.  See the [resource list](resourcelist.html).",
        # if property is element of this resource.
        element_property=True,
    )
    resource__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_resource", title="Extension field for ``resource``."
    )

    response: fhirtypes.Code = Field(
        None,
        alias="response",
        title=(
            "continue | switchingProtocols | okay | created | accepted | "
            "nonAuthoritativeInformation | noContent | resetContent | "
            "partialContent | multipleChoices | movedPermanently | found | seeOther"
            " | notModified | useProxy | temporaryRedirect | permanentRedirect | "
            "badRequest | unauthorized | paymentRequired | forbidden | notFound | "
            "methodNotAllowed | notAcceptable | proxyAuthenticationRequired | "
            "requestTimeout | conflict | gone | lengthRequired | preconditionFailed"
            " | contentTooLarge | uriTooLong | unsupportedMediaType | "
            "rangeNotSatisfiable | expectationFailed | misdirectedRequest | "
            "unprocessableContent | upgradeRequired | internalServerError | "
            "notImplemented | badGateway | serviceUnavailable | gatewayTimeout | "
            "httpVersionNotSupported"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "continue",
            "switchingProtocols",
            "okay",
            "created",
            "accepted",
            "nonAuthoritativeInformation",
            "noContent",
            "resetContent",
            "partialContent",
            "multipleChoices",
            "movedPermanently",
            "found",
            "seeOther",
            "notModified",
            "useProxy",
            "temporaryRedirect",
            "permanentRedirect",
            "badRequest",
            "unauthorized",
            "paymentRequired",
            "forbidden",
            "notFound",
            "methodNotAllowed",
            "notAcceptable",
            "proxyAuthenticationRequired",
            "requestTimeout",
            "conflict",
            "gone",
            "lengthRequired",
            "preconditionFailed",
            "contentTooLarge",
            "uriTooLong",
            "unsupportedMediaType",
            "rangeNotSatisfiable",
            "expectationFailed",
            "misdirectedRequest",
            "unprocessableContent",
            "upgradeRequired",
            "internalServerError",
            "notImplemented",
            "badGateway",
            "serviceUnavailable",
            "gatewayTimeout",
            "httpVersionNotSupported",
        ],
    )
    response__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_response", title="Extension field for ``response``."
    )

    responseCode: fhirtypes.String = Field(
        None,
        alias="responseCode",
        title="HTTP response code to test",
        description="The value of the HTTP response code to be tested.",
        # if property is element of this resource.
        element_property=True,
    )
    responseCode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_responseCode", title="Extension field for ``responseCode``."
    )

    sourceId: fhirtypes.Id = Field(
        None,
        alias="sourceId",
        title="Fixture Id of source expression or headerField",
        description=(
            "Fixture to evaluate the XPath/JSONPath expression or the headerField  "
            "against."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    sourceId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sourceId", title="Extension field for ``sourceId``."
    )

    stopTestOnFail: bool = Field(
        None,
        alias="stopTestOnFail",
        title="If this assert fails, will the current test execution stop?",
        description=(
            "Whether or not the current test execution will stop on failure for "
            "this assert."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    stopTestOnFail__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_stopTestOnFail", title="Extension field for ``stopTestOnFail``."
    )

    validateProfileId: fhirtypes.Id = Field(
        None,
        alias="validateProfileId",
        title="Profile Id of validation profile reference",
        description="The ID of the Profile to validate against.",
        # if property is element of this resource.
        element_property=True,
    )
    validateProfileId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_validateProfileId",
        title="Extension field for ``validateProfileId``.",
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="The value to compare to",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )

    warningOnly: bool = Field(
        None,
        alias="warningOnly",
        title="Will this assert produce a warning only on error?",
        description=(
            "Whether or not the test execution will produce a warning only on error"
            " for this assert."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    warningOnly__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_warningOnly", title="Extension field for ``warningOnly``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestScriptSetupActionAssert`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "label",
            "description",
            "direction",
            "compareToSourceId",
            "compareToSourceExpression",
            "compareToSourcePath",
            "contentType",
            "defaultManualCompletion",
            "expression",
            "headerField",
            "minimumId",
            "navigationLinks",
            "operator",
            "path",
            "requestMethod",
            "requestURL",
            "resource",
            "response",
            "responseCode",
            "sourceId",
            "stopTestOnFail",
            "validateProfileId",
            "value",
            "warningOnly",
            "requirement",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3006(
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
            ("stopTestOnFail", "stopTestOnFail__ext"),
            ("warningOnly", "warningOnly__ext"),
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


class TestScriptSetupActionAssertRequirement(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Links or references to the testing requirements.
    Links or references providing traceability to the testing requirements for
    this assert.
    """

    resource_type = Field("TestScriptSetupActionAssertRequirement", const=True)

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
        ``TestScriptSetupActionAssertRequirement`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "linkUri", "linkCanonical"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_4175(
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


class TestScriptSetupActionOperation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The setup operation to perform.
    The operation to perform.
    """

    resource_type = Field("TestScriptSetupActionOperation", const=True)

    accept: fhirtypes.Code = Field(
        None,
        alias="accept",
        title="Mime type to accept in the payload of the response, with charset etc",
        description="The mime-type to use for RESTful operation in the 'Accept' header.",
        # if property is element of this resource.
        element_property=True,
    )
    accept__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_accept", title="Extension field for ``accept``."
    )

    contentType: fhirtypes.Code = Field(
        None,
        alias="contentType",
        title="Mime type of the request payload contents, with charset etc",
        description=(
            "The mime-type to use for RESTful operation in the 'Content-Type' "
            "header."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    contentType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_contentType", title="Extension field for ``contentType``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Tracking/reporting operation description",
        description=(
            "The description would be used by test engines for tracking and "
            "reporting purposes."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    destination: fhirtypes.Integer = Field(
        None,
        alias="destination",
        title="Server responding to the request",
        description=(
            "The server where the request message is destined for.  Must be one of "
            "the server numbers listed in TestScript.destination section."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    destination__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_destination", title="Extension field for ``destination``."
    )

    encodeRequestUrl: bool = Field(
        None,
        alias="encodeRequestUrl",
        title="Whether or not to send the request url in encoded format",
        description=(
            "Whether or not to implicitly send the request url in encoded format. "
            "The default is true to match the standard RESTful client behavior. Set"
            " to false when communicating with a server that does not support "
            "encoded url paths."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    encodeRequestUrl__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_encodeRequestUrl",
        title="Extension field for ``encodeRequestUrl``.",
    )

    label: fhirtypes.String = Field(
        None,
        alias="label",
        title="Tracking/logging operation label",
        description="The label would be used for tracking/logging purposes by test engines.",
        # if property is element of this resource.
        element_property=True,
    )
    label__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_label", title="Extension field for ``label``."
    )

    method: fhirtypes.Code = Field(
        None,
        alias="method",
        title="delete | get | options | patch | post | put | head",
        description=(
            "The HTTP method the test engine MUST use for this operation regardless"
            " of any other operation details."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["delete", "get", "options", "patch", "post", "put", "head"],
    )
    method__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_method", title="Extension field for ``method``."
    )

    origin: fhirtypes.Integer = Field(
        None,
        alias="origin",
        title="Server initiating the request",
        description=(
            "The server where the request message originates from.  Must be one of "
            "the server numbers listed in TestScript.origin section."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    origin__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_origin", title="Extension field for ``origin``."
    )

    params: fhirtypes.String = Field(
        None,
        alias="params",
        title="Explicitly defined path parameters",
        description=(
            "Path plus parameters after [type].  Used to set parts of the request "
            "URL explicitly."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    params__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_params", title="Extension field for ``params``."
    )

    requestHeader: typing.List[
        fhirtypes.TestScriptSetupActionOperationRequestHeaderType
    ] = Field(
        None,
        alias="requestHeader",
        title="Each operation can have one or more header elements",
        description="Header elements would be used to set HTTP headers.",
        # if property is element of this resource.
        element_property=True,
    )

    requestId: fhirtypes.Id = Field(
        None,
        alias="requestId",
        title="Fixture Id of mapped request",
        description="The fixture id (maybe new) to map to the request.",
        # if property is element of this resource.
        element_property=True,
    )
    requestId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_requestId", title="Extension field for ``requestId``."
    )

    resource: fhirtypes.Uri = Field(
        None,
        alias="resource",
        title="Resource type",
        description=(
            "The type of the FHIR resource. See the [resource "
            "list](resourcelist.html). Data type of uri is needed when non-HL7 "
            "artifacts are identified."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    resource__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_resource", title="Extension field for ``resource``."
    )

    responseId: fhirtypes.Id = Field(
        None,
        alias="responseId",
        title="Fixture Id of mapped response",
        description="The fixture id (maybe new) to map to the response.",
        # if property is element of this resource.
        element_property=True,
    )
    responseId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_responseId", title="Extension field for ``responseId``."
    )

    sourceId: fhirtypes.Id = Field(
        None,
        alias="sourceId",
        title="Fixture Id of body for PUT and POST requests",
        description="The id of the fixture used as the body of a PUT or POST request.",
        # if property is element of this resource.
        element_property=True,
    )
    sourceId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sourceId", title="Extension field for ``sourceId``."
    )

    targetId: fhirtypes.Id = Field(
        None,
        alias="targetId",
        title=(
            "Id of fixture used for extracting the [id],  [type], and [vid] for GET"
            " requests"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    targetId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_targetId", title="Extension field for ``targetId``."
    )

    type: fhirtypes.CodingType = Field(
        None,
        alias="type",
        title="The operation code type that will be executed",
        description="Server interaction or operation type.",
        # if property is element of this resource.
        element_property=True,
    )

    url: fhirtypes.String = Field(
        None,
        alias="url",
        title="Request URL",
        description="Complete request URL.",
        # if property is element of this resource.
        element_property=True,
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestScriptSetupActionOperation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "resource",
            "label",
            "description",
            "accept",
            "contentType",
            "destination",
            "encodeRequestUrl",
            "method",
            "origin",
            "params",
            "requestHeader",
            "requestId",
            "responseId",
            "sourceId",
            "targetId",
            "url",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3319(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("encodeRequestUrl", "encodeRequestUrl__ext")]
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


class TestScriptSetupActionOperationRequestHeader(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Each operation can have one or more header elements.
    Header elements would be used to set HTTP headers.
    """

    resource_type = Field("TestScriptSetupActionOperationRequestHeader", const=True)

    field: fhirtypes.String = Field(
        None,
        alias="field",
        title="HTTP header field name",
        description='The HTTP header field e.g. "Accept".',
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    field__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_field", title="Extension field for ``field``."
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="HTTP headerfield value",
        description='The value of the header e.g. "application/fhir+xml".',
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestScriptSetupActionOperationRequestHeader`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "field", "value"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_4653(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("field", "field__ext"), ("value", "value__ext")]
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


class TestScriptTeardown(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A series of required clean up steps.
    A series of operations required to clean up after all the tests are
    executed (successfully or otherwise).
    """

    resource_type = Field("TestScriptTeardown", const=True)

    action: typing.List[fhirtypes.TestScriptTeardownActionType] = Field(
        ...,
        alias="action",
        title="One or more teardown operations to perform",
        description="The teardown action will only contain an operation.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestScriptTeardown`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "action"]


class TestScriptTeardownAction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    One or more teardown operations to perform.
    The teardown action will only contain an operation.
    """

    resource_type = Field("TestScriptTeardownAction", const=True)

    operation: fhirtypes.TestScriptSetupActionOperationType = Field(
        ...,
        alias="operation",
        title="The teardown operation to perform",
        description="An operation would involve a REST request to a server.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestScriptTeardownAction`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "operation"]


class TestScriptTest(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A test in this script.
    """

    resource_type = Field("TestScriptTest", const=True)

    action: typing.List[fhirtypes.TestScriptTestActionType] = Field(
        ...,
        alias="action",
        title="A test operation or assert to perform",
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
        ``TestScriptTest`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "name", "description", "action"]


class TestScriptTestAction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A test operation or assert to perform.
    Action would contain either an operation or an assertion.
    """

    resource_type = Field("TestScriptTestAction", const=True)

    assert_fhir: fhirtypes.TestScriptSetupActionAssertType = Field(
        None,
        alias="assert",
        title="The setup assertion to perform",
        description=(
            "Evaluates the results of previous operations to determine if the "
            "server under test behaves appropriately."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    operation: fhirtypes.TestScriptSetupActionOperationType = Field(
        None,
        alias="operation",
        title="The setup operation to perform",
        description="An operation would involve a REST request to a server.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestScriptTestAction`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "operation", "assert"]


class TestScriptVariable(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
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
        title="Default, hard-coded, or user-defined value for this variable",
        description="A default, hard-coded, or user-defined value for this variable.",
        # if property is element of this resource.
        element_property=True,
    )
    defaultValue__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_defaultValue", title="Extension field for ``defaultValue``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Natural language description of the variable",
        description=(
            "A free text natural language description of the variable and its "
            "purpose."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    expression: fhirtypes.String = Field(
        None,
        alias="expression",
        title="The FHIRPath expression against the fixture body",
        description=(
            "The FHIRPath expression for a specific value to evaluate against the "
            "fixture body. When variables are defined, only one of either "
            "expression, headerField or path must be specified."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_expression", title="Extension field for ``expression``."
    )

    headerField: fhirtypes.String = Field(
        None,
        alias="headerField",
        title="HTTP header field name for source",
        description=(
            "Will be used to grab the HTTP header field value from the headers that"
            " sourceId is pointing to."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    headerField__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_headerField", title="Extension field for ``headerField``."
    )

    hint: fhirtypes.String = Field(
        None,
        alias="hint",
        title="Hint help text for default value to enter",
        description=(
            "Displayable text string with hint help information to the user when "
            "entering a default value."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    hint__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_hint", title="Extension field for ``hint``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Descriptive name for this variable",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    path: fhirtypes.String = Field(
        None,
        alias="path",
        title="XPath or JSONPath against the fixture body",
        description=(
            "XPath or JSONPath to evaluate against the fixture body.  When "
            "variables are defined, only one of either expression, headerField or "
            "path must be specified."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_path", title="Extension field for ``path``."
    )

    sourceId: fhirtypes.Id = Field(
        None,
        alias="sourceId",
        title="Fixture Id of source expression or headerField within this variable",
        description=(
            "Fixture to evaluate the XPath/JSONPath expression or the headerField  "
            "against within this variable."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    sourceId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sourceId", title="Extension field for ``sourceId``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TestScriptVariable`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "name",
            "defaultValue",
            "description",
            "expression",
            "headerField",
            "hint",
            "path",
            "sourceId",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2036(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("name", "name__ext")]
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
