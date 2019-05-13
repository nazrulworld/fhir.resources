#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/TestScript) on 2019-05-13.
#  2019, SMART Health IT.


from . import domainresource

class TestScript(domainresource.DomainResource):
    """ Describes a set of tests.

    A structured set of tests against a FHIR server or client implementation to
    determine compliance against the FHIR specification.
    """

    resource_type = "TestScript"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """

        self.date = None
        """ Date last changed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.description = None
        """ Natural language description of the test script.
        Type `str`. """

        self.destination = None
        """ An abstract server representing a destination or receiver in a
        message exchange.
        List of `TestScriptDestination` items (represented as `dict` in JSON). """

        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """

        self.fixture = None
        """ Fixture in the test script - by reference (uri).
        List of `TestScriptFixture` items (represented as `dict` in JSON). """

        self.identifier = None
        """ Additional identifier for the test script.
        Type `Identifier` (represented as `dict` in JSON). """

        self.jurisdiction = None
        """ Intended jurisdiction for test script (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.metadata = None
        """ Required capability that is assumed to function correctly on the
        FHIR server being tested.
        Type `TestScriptMetadata` (represented as `dict` in JSON). """

        self.name = None
        """ Name for this test script (computer friendly).
        Type `str`. """

        self.origin = None
        """ An abstract server representing a client or sender in a message
        exchange.
        List of `TestScriptOrigin` items (represented as `dict` in JSON). """

        self.profile = None
        """ Reference of the validation profile.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """

        self.purpose = None
        """ Why this test script is defined.
        Type `str`. """

        self.setup = None
        """ A series of required setup operations before tests are executed.
        Type `TestScriptSetup` (represented as `dict` in JSON). """

        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """

        self.teardown = None
        """ A series of required clean up steps.
        Type `TestScriptTeardown` (represented as `dict` in JSON). """

        self.test = None
        """ A test in this script.
        List of `TestScriptTest` items (represented as `dict` in JSON). """

        self.title = None
        """ Name for this test script (human friendly).
        Type `str`. """

        self.url = None
        """ Canonical identifier for this test script, represented as a URI
        (globally unique).
        Type `str`. """

        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """

        self.variable = None
        """ Placeholder for evaluated elements.
        List of `TestScriptVariable` items (represented as `dict` in JSON). """

        self.version = None
        """ Business version of the test script.
        Type `str`. """

        super(TestScript, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(TestScript, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, "ContactDetail", True, None, False),
            ("copyright", "copyright", str, "markdown", False, None, False),
            ("date", "date", fhirdate.FHIRDate, "dateTime", False, None, False),
            ("description", "description", str, "markdown", False, None, False),
            ("destination", "destination", TestScriptDestination, "TestScriptDestination", True, None, False),
            ("experimental", "experimental", bool, "boolean", False, None, False),
            ("fixture", "fixture", TestScriptFixture, "TestScriptFixture", True, None, False),
            ("identifier", "identifier", identifier.Identifier, "Identifier", False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, "CodeableConcept", True, None, False),
            ("metadata", "metadata", TestScriptMetadata, "TestScriptMetadata", False, None, False),
            ("name", "name", str, "string", False, None, True),
            ("origin", "origin", TestScriptOrigin, "TestScriptOrigin", True, None, False),
            ("profile", "profile", fhirreference.FHIRReference, "Reference", True, None, False),
            ("publisher", "publisher", str, "string", False, None, False),
            ("purpose", "purpose", str, "markdown", False, None, False),
            ("setup", "setup", TestScriptSetup, "TestScriptSetup", False, None, False),
            ("status", "status", str, "code", False, None, True),
            ("teardown", "teardown", TestScriptTeardown, "TestScriptTeardown", False, None, False),
            ("test", "test", TestScriptTest, "TestScriptTest", True, None, False),
            ("title", "title", str, "string", False, None, False),
            ("url", "url", str, "uri", False, None, True),
            ("useContext", "useContext", usagecontext.UsageContext, "UsageContext", True, None, False),
            ("variable", "variable", TestScriptVariable, "TestScriptVariable", True, None, False),
            ("version", "version", str, "string", False, None, False),
        ])
        return js


from . import backboneelement

class TestScriptDestination(backboneelement.BackboneElement):
    """ An abstract server representing a destination or receiver in a message
    exchange.

    An abstract server used in operations within this test script in the
    destination element.
    """

    resource_type = "TestScriptDestination"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.index = None
        """ The index of the abstract destination server starting at 1.
        Type `int`. """

        self.profile = None
        """ FHIR-Server | FHIR-SDC-FormManager | FHIR-SDC-FormReceiver | FHIR-
        SDC-FormProcessor.
        Type `Coding` (represented as `dict` in JSON). """

        super(TestScriptDestination, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(TestScriptDestination, self).elementProperties()
        js.extend([
            ("index", "index", int, "integer", False, None, True),
            ("profile", "profile", coding.Coding, "Coding", False, None, True),
        ])
        return js


class TestScriptFixture(backboneelement.BackboneElement):
    """ Fixture in the test script - by reference (uri).

    Fixture in the test script - by reference (uri). All fixtures are required
    for the test script to execute.
    """

    resource_type = "TestScriptFixture"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.autocreate = None
        """ Whether or not to implicitly create the fixture during setup.
        Type `bool`. """

        self.autodelete = None
        """ Whether or not to implicitly delete the fixture during teardown.
        Type `bool`. """

        self.resource = None
        """ Reference of the resource.
        Type `FHIRReference` (represented as `dict` in JSON). """

        super(TestScriptFixture, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(TestScriptFixture, self).elementProperties()
        js.extend([
            ("autocreate", "autocreate", bool, "boolean", False, None, True),
            ("autodelete", "autodelete", bool, "boolean", False, None, True),
            ("resource", "resource", fhirreference.FHIRReference, "Reference", False, None, False),
        ])
        return js


class TestScriptMetadata(backboneelement.BackboneElement):
    """ Required capability that is assumed to function correctly on the FHIR
    server being tested.

    The required capability must exist and are assumed to function correctly on
    the FHIR server being tested.
    """

    resource_type = "TestScriptMetadata"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.capability = None
        """ Capabilities  that are assumed to function correctly on the FHIR
        server being tested.
        List of `TestScriptMetadataCapability` items (represented as `dict` in JSON). """

        self.link = None
        """ Links to the FHIR specification.
        List of `TestScriptMetadataLink` items (represented as `dict` in JSON). """

        super(TestScriptMetadata, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(TestScriptMetadata, self).elementProperties()
        js.extend([
            ("capability", "capability", TestScriptMetadataCapability, "TestScriptMetadataCapability", True, None, True),
            ("link", "link", TestScriptMetadataLink, "TestScriptMetadataLink", True, None, False),
        ])
        return js


class TestScriptMetadataCapability(backboneelement.BackboneElement):
    """ Capabilities  that are assumed to function correctly on the FHIR server
    being tested.

    Capabilities that must exist and are assumed to function correctly on the
    FHIR server being tested.
    """

    resource_type = "TestScriptMetadataCapability"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.capabilities = None
        """ Required Capability Statement.
        Type `str`. """

        self.description = None
        """ The expected capabilities of the server.
        Type `str`. """

        self.destination = None
        """ Which server these requirements apply to.
        Type `int`. """

        self.link = None
        """ Links to the FHIR specification.
        List of `str` items. """

        self.origin = None
        """ Which origin server these requirements apply to.
        List of `int` items. """

        self.required = None
        """ Are the capabilities required?.
        Type `bool`. """

        self.validated = None
        """ Are the capabilities validated?.
        Type `bool`. """

        super(TestScriptMetadataCapability, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(TestScriptMetadataCapability, self).elementProperties()
        js.extend([
            ("capabilities", "capabilities", str, "canonical", False, None, True),
            ("description", "description", str, "string", False, None, False),
            ("destination", "destination", int, "integer", False, None, False),
            ("link", "link", str, "uri", True, None, False),
            ("origin", "origin", int, "integer", True, None, False),
            ("required", "required", bool, "boolean", False, None, True),
            ("validated", "validated", bool, "boolean", False, None, True),
        ])
        return js


class TestScriptMetadataLink(backboneelement.BackboneElement):
    """ Links to the FHIR specification.

    A link to the FHIR specification that this test is covering.
    """

    resource_type = "TestScriptMetadataLink"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.description = None
        """ Short description.
        Type `str`. """

        self.url = None
        """ URL to the specification.
        Type `str`. """

        super(TestScriptMetadataLink, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(TestScriptMetadataLink, self).elementProperties()
        js.extend([
            ("description", "description", str, "string", False, None, False),
            ("url", "url", str, "uri", False, None, True),
        ])
        return js


class TestScriptOrigin(backboneelement.BackboneElement):
    """ An abstract server representing a client or sender in a message exchange.

    An abstract server used in operations within this test script in the origin
    element.
    """

    resource_type = "TestScriptOrigin"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.index = None
        """ The index of the abstract origin server starting at 1.
        Type `int`. """

        self.profile = None
        """ FHIR-Client | FHIR-SDC-FormFiller.
        Type `Coding` (represented as `dict` in JSON). """

        super(TestScriptOrigin, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(TestScriptOrigin, self).elementProperties()
        js.extend([
            ("index", "index", int, "integer", False, None, True),
            ("profile", "profile", coding.Coding, "Coding", False, None, True),
        ])
        return js


class TestScriptSetup(backboneelement.BackboneElement):
    """ A series of required setup operations before tests are executed.
    """

    resource_type = "TestScriptSetup"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.action = None
        """ A setup operation or assert to perform.
        List of `TestScriptSetupAction` items (represented as `dict` in JSON). """

        super(TestScriptSetup, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(TestScriptSetup, self).elementProperties()
        js.extend([
            ("action", "action", TestScriptSetupAction, "TestScriptSetupAction", True, None, True),
        ])
        return js


class TestScriptSetupAction(backboneelement.BackboneElement):
    """ A setup operation or assert to perform.

    Action would contain either an operation or an assertion.
    """

    resource_type = "TestScriptSetupAction"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.assert_fhir = None
        """ The assertion to perform.
        Type `TestScriptSetupActionAssert` (represented as `dict` in JSON). """

        self.operation = None
        """ The setup operation to perform.
        Type `TestScriptSetupActionOperation` (represented as `dict` in JSON). """

        super(TestScriptSetupAction, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(TestScriptSetupAction, self).elementProperties()
        js.extend([
            ("assert_fhir", "assert", TestScriptSetupActionAssert, "TestScriptSetupActionAssert", False, None, False),
            ("operation", "operation", TestScriptSetupActionOperation, "TestScriptSetupActionOperation", False, None, False),
        ])
        return js


class TestScriptSetupActionAssert(backboneelement.BackboneElement):
    """ The assertion to perform.

    Evaluates the results of previous operations to determine if the server
    under test behaves appropriately.
    """

    resource_type = "TestScriptSetupActionAssert"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.compareToSourceExpression = None
        """ The FHIRPath expression to evaluate against the source fixture.
        Type `str`. """

        self.compareToSourceId = None
        """ Id of the source fixture to be evaluated.
        Type `str`. """

        self.compareToSourcePath = None
        """ XPath or JSONPath expression to evaluate against the source fixture.
        Type `str`. """

        self.contentType = None
        """ Mime type to compare against the 'Content-Type' header.
        Type `str`. """

        self.description = None
        """ Tracking/reporting assertion description.
        Type `str`. """

        self.direction = None
        """ response | request.
        Type `str`. """

        self.expression = None
        """ The FHIRPath expression to be evaluated.
        Type `str`. """

        self.headerField = None
        """ HTTP header field name.
        Type `str`. """

        self.label = None
        """ Tracking/logging assertion label.
        Type `str`. """

        self.minimumId = None
        """ Fixture Id of minimum content resource.
        Type `str`. """

        self.navigationLinks = None
        """ Perform validation on navigation links?.
        Type `bool`. """

        self.operator = None
        """ equals | notEquals | in | notIn | greaterThan | lessThan | empty |
        notEmpty | contains | notContains | eval.
        Type `str`. """

        self.path = None
        """ XPath or JSONPath expression.
        Type `str`. """

        self.requestMethod = None
        """ delete | get | options | patch | post | put | head.
        Type `str`. """

        self.requestURL = None
        """ Request URL comparison value.
        Type `str`. """

        self.resource = None
        """ Resource type.
        Type `str`. """

        self.response = None
        """ okay | created | noContent | notModified | bad | forbidden |
        notFound | methodNotAllowed | conflict | gone | preconditionFailed
        | unprocessable.
        Type `str`. """

        self.responseCode = None
        """ HTTP response code to test.
        Type `str`. """

        self.sourceId = None
        """ Fixture Id of source expression or headerField.
        Type `str`. """

        self.validateProfileId = None
        """ Profile Id of validation profile reference.
        Type `str`. """

        self.value = None
        """ The value to compare to.
        Type `str`. """

        self.warningOnly = None
        """ Will this assert produce a warning only on error?.
        Type `bool`. """

        super(TestScriptSetupActionAssert, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(TestScriptSetupActionAssert, self).elementProperties()
        js.extend([
            ("compareToSourceExpression", "compareToSourceExpression", str, "string", False, None, False),
            ("compareToSourceId", "compareToSourceId", str, "string", False, None, False),
            ("compareToSourcePath", "compareToSourcePath", str, "string", False, None, False),
            ("contentType", "contentType", str, "code", False, None, False),
            ("description", "description", str, "string", False, None, False),
            ("direction", "direction", str, "code", False, None, False),
            ("expression", "expression", str, "string", False, None, False),
            ("headerField", "headerField", str, "string", False, None, False),
            ("label", "label", str, "string", False, None, False),
            ("minimumId", "minimumId", str, "string", False, None, False),
            ("navigationLinks", "navigationLinks", bool, "boolean", False, None, False),
            ("operator", "operator", str, "code", False, None, False),
            ("path", "path", str, "string", False, None, False),
            ("requestMethod", "requestMethod", str, "code", False, None, False),
            ("requestURL", "requestURL", str, "string", False, None, False),
            ("resource", "resource", str, "code", False, None, False),
            ("response", "response", str, "code", False, None, False),
            ("responseCode", "responseCode", str, "string", False, None, False),
            ("sourceId", "sourceId", str, "id", False, None, False),
            ("validateProfileId", "validateProfileId", str, "id", False, None, False),
            ("value", "value", str, "string", False, None, False),
            ("warningOnly", "warningOnly", bool, "boolean", False, None, True),
        ])
        return js


class TestScriptSetupActionOperation(backboneelement.BackboneElement):
    """ The setup operation to perform.

    The operation to perform.
    """

    resource_type = "TestScriptSetupActionOperation"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.accept = None
        """ Mime type to accept in the payload of the response, with charset
        etc..
        Type `str`. """

        self.contentType = None
        """ Mime type of the request payload contents, with charset etc..
        Type `str`. """

        self.description = None
        """ Tracking/reporting operation description.
        Type `str`. """

        self.destination = None
        """ Server responding to the request.
        Type `int`. """

        self.encodeRequestUrl = None
        """ Whether or not to send the request url in encoded format.
        Type `bool`. """

        self.label = None
        """ Tracking/logging operation label.
        Type `str`. """

        self.method = None
        """ delete | get | options | patch | post | put | head.
        Type `str`. """

        self.origin = None
        """ Server initiating the request.
        Type `int`. """

        self.params = None
        """ Explicitly defined path parameters.
        Type `str`. """

        self.requestHeader = None
        """ Each operation can have one or more header elements.
        List of `TestScriptSetupActionOperationRequestHeader` items (represented as `dict` in JSON). """

        self.requestId = None
        """ Fixture Id of mapped request.
        Type `str`. """

        self.resource = None
        """ Resource type.
        Type `str`. """

        self.responseId = None
        """ Fixture Id of mapped response.
        Type `str`. """

        self.sourceId = None
        """ Fixture Id of body for PUT and POST requests.
        Type `str`. """

        self.targetId = None
        """ Id of fixture used for extracting the [id],  [type], and [vid] for
        GET requests.
        Type `str`. """

        self.type = None
        """ The operation code type that will be executed.
        Type `Coding` (represented as `dict` in JSON). """

        self.url = None
        """ Request URL.
        Type `str`. """

        super(TestScriptSetupActionOperation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(TestScriptSetupActionOperation, self).elementProperties()
        js.extend([
            ("accept", "accept", str, "code", False, None, False),
            ("contentType", "contentType", str, "code", False, None, False),
            ("description", "description", str, "string", False, None, False),
            ("destination", "destination", int, "integer", False, None, False),
            ("encodeRequestUrl", "encodeRequestUrl", bool, "boolean", False, None, True),
            ("label", "label", str, "string", False, None, False),
            ("method", "method", str, "code", False, None, False),
            ("origin", "origin", int, "integer", False, None, False),
            ("params", "params", str, "string", False, None, False),
            ("requestHeader", "requestHeader", TestScriptSetupActionOperationRequestHeader, "TestScriptSetupActionOperationRequestHeader", True, None, False),
            ("requestId", "requestId", str, "id", False, None, False),
            ("resource", "resource", str, "code", False, None, False),
            ("responseId", "responseId", str, "id", False, None, False),
            ("sourceId", "sourceId", str, "id", False, None, False),
            ("targetId", "targetId", str, "id", False, None, False),
            ("type", "type", coding.Coding, "Coding", False, None, False),
            ("url", "url", str, "string", False, None, False),
        ])
        return js


class TestScriptSetupActionOperationRequestHeader(backboneelement.BackboneElement):
    """ Each operation can have one or more header elements.

    Header elements would be used to set HTTP headers.
    """

    resource_type = "TestScriptSetupActionOperationRequestHeader"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.field = None
        """ HTTP header field name.
        Type `str`. """

        self.value = None
        """ HTTP headerfield value.
        Type `str`. """

        super(TestScriptSetupActionOperationRequestHeader, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(TestScriptSetupActionOperationRequestHeader, self).elementProperties()
        js.extend([
            ("field", "field", str, "string", False, None, True),
            ("value", "value", str, "string", False, None, True),
        ])
        return js


class TestScriptTeardown(backboneelement.BackboneElement):
    """ A series of required clean up steps.

    A series of operations required to clean up after all the tests are
    executed (successfully or otherwise).
    """

    resource_type = "TestScriptTeardown"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.action = None
        """ One or more teardown operations to perform.
        List of `TestScriptTeardownAction` items (represented as `dict` in JSON). """

        super(TestScriptTeardown, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(TestScriptTeardown, self).elementProperties()
        js.extend([
            ("action", "action", TestScriptTeardownAction, "TestScriptTeardownAction", True, None, True),
        ])
        return js


class TestScriptTeardownAction(backboneelement.BackboneElement):
    """ One or more teardown operations to perform.

    The teardown action will only contain an operation.
    """

    resource_type = "TestScriptTeardownAction"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.operation = None
        """ The teardown operation to perform.
        Type `TestScriptSetupActionOperation` (represented as `dict` in JSON). """

        super(TestScriptTeardownAction, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(TestScriptTeardownAction, self).elementProperties()
        js.extend([
            ("operation", "operation", TestScriptSetupActionOperation, "TestScriptSetupActionOperation", False, None, True),
        ])
        return js


class TestScriptTest(backboneelement.BackboneElement):
    """ A test in this script.
    """

    resource_type = "TestScriptTest"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.action = None
        """ A test operation or assert to perform.
        List of `TestScriptTestAction` items (represented as `dict` in JSON). """

        self.description = None
        """ Tracking/reporting short description of the test.
        Type `str`. """

        self.name = None
        """ Tracking/logging name of this test.
        Type `str`. """

        super(TestScriptTest, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(TestScriptTest, self).elementProperties()
        js.extend([
            ("action", "action", TestScriptTestAction, "TestScriptTestAction", True, None, True),
            ("description", "description", str, "string", False, None, False),
            ("name", "name", str, "string", False, None, False),
        ])
        return js


class TestScriptTestAction(backboneelement.BackboneElement):
    """ A test operation or assert to perform.

    Action would contain either an operation or an assertion.
    """

    resource_type = "TestScriptTestAction"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.assert_fhir = None
        """ The setup assertion to perform.
        Type `TestScriptSetupActionAssert` (represented as `dict` in JSON). """

        self.operation = None
        """ The setup operation to perform.
        Type `TestScriptSetupActionOperation` (represented as `dict` in JSON). """

        super(TestScriptTestAction, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(TestScriptTestAction, self).elementProperties()
        js.extend([
            ("assert_fhir", "assert", TestScriptSetupActionAssert, "TestScriptSetupActionAssert", False, None, False),
            ("operation", "operation", TestScriptSetupActionOperation, "TestScriptSetupActionOperation", False, None, False),
        ])
        return js


class TestScriptVariable(backboneelement.BackboneElement):
    """ Placeholder for evaluated elements.

    Variable is set based either on element value in response body or on header
    field value in the response headers.
    """

    resource_type = "TestScriptVariable"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.defaultValue = None
        """ Default, hard-coded, or user-defined value for this variable.
        Type `str`. """

        self.description = None
        """ Natural language description of the variable.
        Type `str`. """

        self.expression = None
        """ The FHIRPath expression against the fixture body.
        Type `str`. """

        self.headerField = None
        """ HTTP header field name for source.
        Type `str`. """

        self.hint = None
        """ Hint help text for default value to enter.
        Type `str`. """

        self.name = None
        """ Descriptive name for this variable.
        Type `str`. """

        self.path = None
        """ XPath or JSONPath against the fixture body.
        Type `str`. """

        self.sourceId = None
        """ Fixture Id of source expression or headerField within this variable.
        Type `str`. """

        super(TestScriptVariable, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(TestScriptVariable, self).elementProperties()
        js.extend([
            ("defaultValue", "defaultValue", str, "string", False, None, False),
            ("description", "description", str, "string", False, None, False),
            ("expression", "expression", str, "string", False, None, False),
            ("headerField", "headerField", str, "string", False, None, False),
            ("hint", "hint", str, "string", False, None, False),
            ("name", "name", str, "string", False, None, True),
            ("path", "path", str, "string", False, None, False),
            ("sourceId", "sourceId", str, "id", False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
