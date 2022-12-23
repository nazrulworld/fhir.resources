# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/TestScript
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import testscript


def impl_testscript_1(inst):
    assert inst.contact[0].name == "Support"
    assert inst.contact[0].telecom[0].system == "email"
    assert inst.contact[0].telecom[0].use == "work"
    assert inst.contact[0].telecom[0].value == "support@HL7.org"
    assert inst.copyright == "© HL7.org 2011+"
    assert inst.date == fhirtypes.DateTime.validate("2017-01-18")
    assert inst.destination[0].index == 1
    assert inst.destination[0].profile.code == "FHIR-Server"
    assert inst.destination[1].index == 2
    assert inst.destination[1].profile.code == "FHIR-Server"
    assert inst.experimental is True
    assert inst.id == "testscript-example-multisystem"
    assert inst.identifier.system == "urn:ietf:rfc:3986"
    assert inst.identifier.value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.9878"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America (the)"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert (
        inst.metadata.capability[0].capabilities
        == "http://hl7.org/fhir/CapabilityStatement/example"
    )
    assert inst.metadata.capability[0].description == "Patient Read Operation"
    assert inst.metadata.capability[0].destination == 1
    assert inst.metadata.capability[0].link[0] == "http://hl7.org/fhir/http.html#read"
    assert inst.metadata.capability[0].origin[0] == 1
    assert inst.metadata.capability[0].required is True
    assert inst.metadata.capability[0].validated is False
    assert (
        inst.metadata.capability[1].capabilities
        == "http://hl7.org/fhir/CapabilityStatement/example"
    )
    assert inst.metadata.capability[1].description == "Patient Read Operation"
    assert inst.metadata.capability[1].destination == 2
    assert inst.metadata.capability[1].link[0] == "http://hl7.org/fhir/http.html#read"
    assert inst.metadata.capability[1].origin[0] == 1
    assert inst.metadata.capability[1].required is True
    assert inst.metadata.capability[1].validated is False
    assert inst.metadata.link[0].description == (
        "Demographics and other administrative information about an "
        "individual or animal receiving care or other health-related "
        "services."
    )
    assert inst.metadata.link[0].url == "http://hl7.org/fhir/patient.html"
    assert inst.name == "testscript-example-multisystem"
    assert inst.origin[0].index == 1
    assert inst.origin[0].profile.code == "FHIR-Client"
    assert inst.publisher == "HL7"
    assert inst.purpose == "Patient Read Operation"
    assert inst.status == "draft"
    assert inst.test[0].action[0].operation.accept == "xml"
    assert inst.test[0].action[0].operation.contentType == "xml"
    assert inst.test[0].action[0].operation.description == (
        "Read a Patient from the first destination test system and "
        "perform basic validation."
    )
    assert inst.test[0].action[0].operation.destination == 1
    assert inst.test[0].action[0].operation.encodeRequestUrl is True
    assert inst.test[0].action[0].operation.origin == 1
    assert inst.test[0].action[0].operation.params == "/${Dest1PatientResourceId}"
    assert inst.test[0].action[0].operation.requestId == "request-read-patient-01"
    assert inst.test[0].action[0].operation.resource == "Patient"
    assert inst.test[0].action[0].operation.type.code == "read"
    assert inst.test[0].action[0].operation.type.system == (
        "http://terminology.hl7.org/CodeSystem/testscript-operation-" "codes"
    )
    assert inst.test[0].action[1].assert_fhir.description == (
        "Confirm that the request method GET was sent by the client "
        "system under test."
    )
    assert inst.test[0].action[1].assert_fhir.requestMethod == "get"
    assert inst.test[0].action[1].assert_fhir.warningOnly is False
    assert (
        inst.test[0].action[2].assert_fhir.description
        == "Confirm that the client requested an Accept of xml."
    )
    assert inst.test[0].action[2].assert_fhir.direction == "request"
    assert inst.test[0].action[2].assert_fhir.headerField == "Accept"
    assert inst.test[0].action[2].assert_fhir.operator == "contains"
    assert inst.test[0].action[2].assert_fhir.value == "xml"
    assert inst.test[0].action[2].assert_fhir.warningOnly is False
    assert (
        inst.test[0].action[3].assert_fhir.description
        == "Confirm that the returned HTTP status is 200(OK)."
    )
    assert inst.test[0].action[3].assert_fhir.direction == "response"
    assert inst.test[0].action[3].assert_fhir.response == "okay"
    assert inst.test[0].action[3].assert_fhir.warningOnly is False
    assert inst.test[0].action[4].assert_fhir.contentType == "xml"
    assert (
        inst.test[0].action[4].assert_fhir.description
        == "Confirm that the returned format is XML."
    )
    assert inst.test[0].action[4].assert_fhir.direction == "response"
    assert inst.test[0].action[4].assert_fhir.warningOnly is False
    assert (
        inst.test[0].action[5].assert_fhir.description
        == "Confirm that the returned resource type is Patient."
    )
    assert inst.test[0].action[5].assert_fhir.direction == "response"
    assert inst.test[0].action[5].assert_fhir.resource == "Patient"
    assert inst.test[0].action[5].assert_fhir.warningOnly is False
    assert inst.test[0].description == (
        "Read a Patient from the first destination test system using "
        "the user defined dynamic variable ${Dest1PatientResourceId}."
        " Perform basic validation."
    )
    assert inst.test[0].id == "01-ReadPatient-Destination1"
    assert inst.test[0].name == "ReadPatient-Destination1"
    assert inst.test[1].action[0].operation.accept == "xml"
    assert inst.test[1].action[0].operation.contentType == "xml"
    assert inst.test[1].action[0].operation.description == (
        "Read a Patient from the second destination test system and "
        "perform basic validation."
    )
    assert inst.test[1].action[0].operation.destination == 2
    assert inst.test[1].action[0].operation.encodeRequestUrl is True
    assert inst.test[1].action[0].operation.origin == 1
    assert inst.test[1].action[0].operation.params == "/${Dest2PatientResourceId}"
    assert inst.test[1].action[0].operation.requestHeader[0].field == "Accept-Charset"
    assert inst.test[1].action[0].operation.requestHeader[0].value == "utf-8"
    assert inst.test[1].action[0].operation.resource == "Patient"
    assert inst.test[1].action[0].operation.type.code == "read"
    assert inst.test[1].action[0].operation.type.system == (
        "http://terminology.hl7.org/CodeSystem/testscript-operation-" "codes"
    )
    assert (
        inst.test[1].action[1].assert_fhir.description
        == "Confirm that the client requested an Accept of xml."
    )
    assert inst.test[1].action[1].assert_fhir.direction == "request"
    assert inst.test[1].action[1].assert_fhir.headerField == "Accept"
    assert inst.test[1].action[1].assert_fhir.operator == "contains"
    assert inst.test[1].action[1].assert_fhir.value == "xml"
    assert inst.test[1].action[1].assert_fhir.warningOnly is False
    assert (
        inst.test[1].action[2].assert_fhir.description
        == "Confirm that the returned HTTP status is 200(OK)."
    )
    assert inst.test[1].action[2].assert_fhir.direction == "response"
    assert inst.test[1].action[2].assert_fhir.response == "okay"
    assert inst.test[1].action[2].assert_fhir.warningOnly is False
    assert inst.test[1].action[3].assert_fhir.contentType == "xml"
    assert (
        inst.test[1].action[3].assert_fhir.description
        == "Confirm that the returned format is XML."
    )
    assert inst.test[1].action[3].assert_fhir.direction == "response"
    assert inst.test[1].action[3].assert_fhir.warningOnly is False
    assert (
        inst.test[1].action[4].assert_fhir.description
        == "Confirm that the returned resource type is Patient."
    )
    assert inst.test[1].action[4].assert_fhir.direction == "response"
    assert inst.test[1].action[4].assert_fhir.resource == "Patient"
    assert inst.test[1].action[4].assert_fhir.warningOnly is False
    assert inst.test[1].description == (
        "Read a Patient from the second destination test system using"
        " the user defined dynamic variable "
        "${Dest2PatientResourceId}. Perform basic validation."
    )
    assert inst.test[1].id == "02-ReadPatient-Destination2"
    assert inst.test[1].name == "ReadPatient-Destination2"
    assert inst.text.status == "generated"
    assert inst.title == "Multisystem Test Script"
    assert inst.url == (
        "http://hl7.org/fhir/TestScript/testscript-example-" "multisystem"
    )
    assert inst.variable[0].defaultValue == "example"
    assert inst.variable[0].name == "Dest1PatientResourceId"
    assert inst.variable[1].defaultValue == "example"
    assert inst.variable[1].name == "Dest2PatientResourceId"
    assert inst.version == "1.0"


def test_testscript_1(base_settings):
    """No. 1 tests collection for TestScript.
    Test File: testscript-example-multisystem.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "testscript-example-multisystem.json"
    )
    inst = testscript.TestScript.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "TestScript" == inst.resource_type

    impl_testscript_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "TestScript" == data["resourceType"]

    inst2 = testscript.TestScript(**data)
    impl_testscript_1(inst2)


def impl_testscript_2(inst):
    assert inst.contact[0].name == "Support"
    assert inst.contact[0].telecom[0].system == "email"
    assert inst.contact[0].telecom[0].use == "work"
    assert inst.contact[0].telecom[0].value == "support@HL7.org"
    assert inst.copyright == "© HL7.org 2011+"
    assert inst.date == fhirtypes.DateTime.validate("2017-01-18")
    assert inst.experimental is True
    assert inst.fixture[0].autocreate is False
    assert inst.fixture[0].autodelete is False
    assert inst.fixture[0].id == "fixture-patient-create"
    assert inst.fixture[0].resource.display == "Peter Chalmers"
    assert inst.fixture[0].resource.reference == "Patient/example"
    assert inst.fixture[1].autocreate is False
    assert inst.fixture[1].autodelete is False
    assert inst.fixture[1].id == "fixture-patient-update"
    assert inst.fixture[1].resource.display == "Donald Duck"
    assert inst.fixture[1].resource.reference == "Patient/pat1"
    assert inst.id == "testscript-example-history"
    assert inst.identifier.system == "urn:ietf:rfc:3986"
    assert inst.identifier.value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.9877"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America (the)"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert (
        inst.metadata.capability[0].capabilities
        == "http://hl7.org/fhir/CapabilityStatement/example"
    )
    assert (
        inst.metadata.capability[0].description
        == "Patient Update, Delete and History (Instance) Operations"
    )
    assert inst.metadata.capability[0].link[0] == "http://hl7.org/fhir/http.html#update"
    assert inst.metadata.capability[0].link[1] == "http://hl7.org/fhir/http.html#delete"
    assert (
        inst.metadata.capability[0].link[2] == "http://hl7.org/fhir/http.html#history"
    )
    assert inst.metadata.capability[0].required is True
    assert inst.metadata.capability[0].validated is False
    assert inst.metadata.link[0].description == (
        "Demographics and other administrative information about an "
        "individual or animal receiving care or other health-related "
        "services."
    )
    assert inst.metadata.link[0].url == "http://hl7.org/fhir/patient.html"
    assert inst.name == "TestScript Example History"
    assert inst.profile[0].id == "bundle-profile"
    assert inst.profile[0].reference == "http://hl7.org/fhir/StructureDefinition/Bundle"
    assert inst.publisher == "HL7"
    assert inst.purpose == (
        "Patient (Conditional) Create, Update, Delete and History "
        "(Instance) Operations"
    )
    assert inst.setup.action[0].operation.accept == "json"
    assert inst.setup.action[0].operation.description == (
        "Execute a delete operation to insure the patient does not "
        "exist on the server."
    )
    assert inst.setup.action[0].operation.encodeRequestUrl is True
    assert inst.setup.action[0].operation.label == "SetupDeletePatient"
    assert inst.setup.action[0].operation.params == "/${createResourceId}"
    assert inst.setup.action[0].operation.resource == "Patient"
    assert inst.setup.action[0].operation.type.code == "delete"
    assert inst.setup.action[0].operation.type.system == (
        "http://terminology.hl7.org/CodeSystem/testscript-operation-" "codes"
    )
    assert inst.setup.action[1].assert_fhir.description == (
        "Confirm that the returned HTTP status is 200(OK) or 204(No " "Content)."
    )
    assert inst.setup.action[1].assert_fhir.direction == "response"
    assert inst.setup.action[1].assert_fhir.operator == "in"
    assert inst.setup.action[1].assert_fhir.responseCode == "200,204"
    assert inst.setup.action[1].assert_fhir.warningOnly is False
    assert inst.setup.action[2].operation.accept == "json"
    assert inst.setup.action[2].operation.contentType == "json"
    assert inst.setup.action[2].operation.description == (
        "Create patient resource on test server using the contents of"
        " fixture-patient-create"
    )
    assert inst.setup.action[2].operation.encodeRequestUrl is True
    assert inst.setup.action[2].operation.label == "SetupCreatePatient"
    assert inst.setup.action[2].operation.params == "/${createResourceId}"
    assert inst.setup.action[2].operation.resource == "Patient"
    assert inst.setup.action[2].operation.sourceId == "fixture-patient-create"
    assert inst.setup.action[2].operation.type.code == "update"
    assert inst.setup.action[2].operation.type.system == (
        "http://terminology.hl7.org/CodeSystem/testscript-operation-" "codes"
    )
    assert (
        inst.setup.action[3].assert_fhir.description
        == "Confirm that the returned HTTP status is 201(Created)."
    )
    assert inst.setup.action[3].assert_fhir.direction == "response"
    assert inst.setup.action[3].assert_fhir.responseCode == "201"
    assert inst.setup.action[3].assert_fhir.warningOnly is False
    assert inst.setup.action[4].operation.accept == "json"
    assert inst.setup.action[4].operation.contentType == "json"
    assert inst.setup.action[4].operation.description == (
        "Update patient resource on test server using the contents of"
        " fixture-patient-update"
    )
    assert inst.setup.action[4].operation.encodeRequestUrl is True
    assert inst.setup.action[4].operation.label == "SetupUpdatePatient"
    assert inst.setup.action[4].operation.params == "/${createResourceId}"
    assert inst.setup.action[4].operation.resource == "Patient"
    assert inst.setup.action[4].operation.sourceId == "fixture-patient-update"
    assert inst.setup.action[4].operation.type.code == "update"
    assert inst.setup.action[4].operation.type.system == (
        "http://terminology.hl7.org/CodeSystem/testscript-operation-" "codes"
    )
    assert (
        inst.setup.action[5].assert_fhir.description
        == "Confirm that the returned HTTP status is 200(OK)."
    )
    assert inst.setup.action[5].assert_fhir.direction == "response"
    assert inst.setup.action[5].assert_fhir.responseCode == "200"
    assert inst.setup.action[5].assert_fhir.warningOnly is False
    assert inst.status == "draft"
    assert inst.test[0].action[0].operation.accept == "json"
    assert inst.test[0].action[0].operation.contentType == "json"
    assert inst.test[0].action[0].operation.description == (
        "Get the Patient history on the test server using the id from"
        " fixture-patient-create."
    )
    assert inst.test[0].action[0].operation.encodeRequestUrl is True
    assert inst.test[0].action[0].operation.resource == "Patient"
    assert inst.test[0].action[0].operation.targetId == "fixture-patient-create"
    assert inst.test[0].action[0].operation.type.code == "history"
    assert inst.test[0].action[0].operation.type.system == (
        "http://terminology.hl7.org/CodeSystem/testscript-operation-" "codes"
    )
    assert (
        inst.test[0].action[1].assert_fhir.description
        == "Confirm that the returned HTTP status is 200(OK)."
    )
    assert inst.test[0].action[1].assert_fhir.direction == "response"
    assert inst.test[0].action[1].assert_fhir.response == "okay"
    assert inst.test[0].action[1].assert_fhir.warningOnly is False
    assert (
        inst.test[0].action[2].assert_fhir.description
        == "Confirm that the returned resource type is Bundle."
    )
    assert inst.test[0].action[2].assert_fhir.resource == "Bundle"
    assert inst.test[0].action[2].assert_fhir.warningOnly is False
    assert inst.test[0].action[3].assert_fhir.description == (
        "Confirm that the returned Bundle conforms to the base FHIR " "specification."
    )
    assert inst.test[0].action[3].assert_fhir.validateProfileId == "bundle-profile"
    assert inst.test[0].action[3].assert_fhir.warningOnly is False
    assert (
        inst.test[0].action[4].assert_fhir.description
        == "Confirm that the returned Bundle type equals 'history'."
    )
    assert inst.test[0].action[4].assert_fhir.operator == "equals"
    assert inst.test[0].action[4].assert_fhir.path == "fhir:Bundle/fhir:type/@value"
    assert inst.test[0].action[4].assert_fhir.value == "history"
    assert inst.test[0].action[4].assert_fhir.warningOnly is False
    assert (
        inst.test[0].description
        == "Get the history for a known Patient and validate response."
    )
    assert inst.test[0].id == "01-HistoryPatient"
    assert inst.test[0].name == "History Patient"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/TestScript/testscript-example-history"
    assert inst.variable[0].name == "createResourceId"
    assert inst.variable[0].path == "Patient/id"
    assert inst.variable[0].sourceId == "fixture-patient-create"
    assert inst.version == "1.0"


def test_testscript_2(base_settings):
    """No. 2 tests collection for TestScript.
    Test File: testscript-example-history.json
    """
    filename = base_settings["unittest_data_dir"] / "testscript-example-history.json"
    inst = testscript.TestScript.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "TestScript" == inst.resource_type

    impl_testscript_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "TestScript" == data["resourceType"]

    inst2 = testscript.TestScript(**data)
    impl_testscript_2(inst2)


def impl_testscript_3(inst):
    assert inst.contact[0].name == "Support"
    assert inst.contact[0].telecom[0].system == "email"
    assert inst.contact[0].telecom[0].use == "work"
    assert inst.contact[0].telecom[0].value == "support@HL7.org"
    assert inst.copyright == "© HL7.org 2011+"
    assert inst.date == fhirtypes.DateTime.validate("2017-01-18")
    assert inst.description == (
        "TestScript example resource with setup to delete if present "
        "and create a new instance of a Patient; and single test "
        "definition to update that Patient with various asserts."
    )
    assert inst.experimental is True
    assert inst.fixture[0].autocreate is False
    assert inst.fixture[0].autodelete is False
    assert inst.fixture[0].id == "fixture-patient-create"
    assert inst.fixture[0].resource.display == "Peter Chalmers"
    assert inst.fixture[0].resource.reference == "Patient/example"
    assert inst.fixture[1].autocreate is False
    assert inst.fixture[1].autodelete is False
    assert inst.fixture[1].id == "fixture-patient-update"
    assert inst.fixture[1].resource.display == "Donald Duck"
    assert inst.fixture[1].resource.reference == "Patient/pat1"
    assert inst.id == "testscript-example-update"
    assert inst.identifier.system == "urn:ietf:rfc:3986"
    assert inst.identifier.value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.9882"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America (the)"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert (
        inst.metadata.capability[0].capabilities
        == "http://hl7.org/fhir/CapabilityStatement/example"
    )
    assert (
        inst.metadata.capability[0].description
        == "Patient Update and Delete Operations"
    )
    assert inst.metadata.capability[0].link[0] == "http://hl7.org/fhir/http.html#update"
    assert inst.metadata.capability[0].link[1] == "http://hl7.org/fhir/http.html#delete"
    assert inst.metadata.capability[0].required is True
    assert inst.metadata.capability[0].validated is False
    assert inst.metadata.link[0].description == (
        "Demographics and other administrative information about an "
        "individual or animal receiving care or other health-related "
        "services."
    )
    assert inst.metadata.link[0].url == "http://hl7.org/fhir/patient.html"
    assert inst.name == "TestScript Example Update"
    assert inst.profile[0].id == "patient-profile"
    assert (
        inst.profile[0].reference == "http://hl7.org/fhir/StructureDefinition/Patient"
    )
    assert inst.publisher == "HL7"
    assert inst.purpose == "Patient (Conditional) Create, Update, Delete Operations"
    assert inst.setup.action[0].operation.accept == "xml"
    assert inst.setup.action[0].operation.description == (
        "Execute a delete operation to insure the patient does not "
        "exist on the server."
    )
    assert inst.setup.action[0].operation.encodeRequestUrl is True
    assert inst.setup.action[0].operation.label == "SetupDeletePatient"
    assert inst.setup.action[0].operation.params == "/${createResourceId}"
    assert inst.setup.action[0].operation.resource == "Patient"
    assert inst.setup.action[0].operation.type.code == "delete"
    assert inst.setup.action[0].operation.type.system == (
        "http://terminology.hl7.org/CodeSystem/testscript-operation-" "codes"
    )
    assert inst.setup.action[1].assert_fhir.description == (
        "Confirm that the returned HTTP status is 200(OK) or 204(No " "Content)."
    )
    assert inst.setup.action[1].assert_fhir.direction == "response"
    assert inst.setup.action[1].assert_fhir.operator == "in"
    assert inst.setup.action[1].assert_fhir.responseCode == "200,204"
    assert inst.setup.action[1].assert_fhir.warningOnly is False
    assert inst.setup.action[2].operation.accept == "xml"
    assert inst.setup.action[2].operation.contentType == "xml"
    assert inst.setup.action[2].operation.description == (
        "Create patient resource on test server using the contents of"
        " fixture-patient-create"
    )
    assert inst.setup.action[2].operation.encodeRequestUrl is True
    assert inst.setup.action[2].operation.label == "SetupCreatePatient"
    assert inst.setup.action[2].operation.params == "/${createResourceId}"
    assert inst.setup.action[2].operation.resource == "Patient"
    assert inst.setup.action[2].operation.sourceId == "fixture-patient-create"
    assert inst.setup.action[2].operation.type.code == "update"
    assert inst.setup.action[2].operation.type.system == (
        "http://terminology.hl7.org/CodeSystem/testscript-operation-" "codes"
    )
    assert (
        inst.setup.action[3].assert_fhir.description
        == "Confirm that the returned HTTP status is 201(Created)."
    )
    assert inst.setup.action[3].assert_fhir.direction == "response"
    assert inst.setup.action[3].assert_fhir.responseCode == "201"
    assert inst.setup.action[3].assert_fhir.warningOnly is False
    assert inst.status == "draft"
    assert inst.test[0].action[0].operation.accept == "xml"
    assert inst.test[0].action[0].operation.contentType == "xml"
    assert inst.test[0].action[0].operation.description == (
        "Update patient resource on test server using the contents of"
        " fixture-patient-update"
    )
    assert inst.test[0].action[0].operation.encodeRequestUrl is True
    assert inst.test[0].action[0].operation.label == "SetupUpdatePatient"
    assert inst.test[0].action[0].operation.params == "/${createResourceId}"
    assert inst.test[0].action[0].operation.resource == "Patient"
    assert inst.test[0].action[0].operation.sourceId == "fixture-patient-update"
    assert inst.test[0].action[0].operation.type.code == "update"
    assert inst.test[0].action[0].operation.type.system == (
        "http://terminology.hl7.org/CodeSystem/testscript-operation-" "codes"
    )
    assert (
        inst.test[0].action[1].assert_fhir.description
        == "Confirm that the returned HTTP status is 200(OK)."
    )
    assert inst.test[0].action[1].assert_fhir.response == "okay"
    assert inst.test[0].action[1].assert_fhir.warningOnly is False
    assert inst.test[0].action[2].assert_fhir.contentType == "xml"
    assert (
        inst.test[0].action[2].assert_fhir.description
        == "Confirm that the returned format is XML."
    )
    assert inst.test[0].action[2].assert_fhir.warningOnly is False
    assert inst.test[0].action[3].assert_fhir.description == (
        "Confirm that the returned HTTP Header Last-Modified is "
        "present. Warning only as the server might not support "
        "versioning."
    )
    assert inst.test[0].action[3].assert_fhir.headerField == "Last-Modified"
    assert inst.test[0].action[3].assert_fhir.operator == "notEmpty"
    assert inst.test[0].action[3].assert_fhir.warningOnly is True
    assert inst.test[0].description == "Update a Patient and validate response."
    assert inst.test[0].id == "01-UpdatePatient"
    assert inst.test[0].name == "Update Patient"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/TestScript/testscript-example-update"
    assert inst.variable[0].name == "createResourceId"
    assert inst.variable[0].path == "Patient/id"
    assert inst.variable[0].sourceId == "fixture-patient-create"
    assert inst.version == "1.0"


def test_testscript_3(base_settings):
    """No. 3 tests collection for TestScript.
    Test File: testscript-example-update.json
    """
    filename = base_settings["unittest_data_dir"] / "testscript-example-update.json"
    inst = testscript.TestScript.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "TestScript" == inst.resource_type

    impl_testscript_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "TestScript" == data["resourceType"]

    inst2 = testscript.TestScript(**data)
    impl_testscript_3(inst2)


def impl_testscript_4(inst):
    assert inst.contact[0].name == "Support"
    assert inst.contact[0].telecom[0].system == "email"
    assert inst.contact[0].telecom[0].use == "work"
    assert inst.contact[0].telecom[0].value == "support@HL7.org"
    assert inst.copyright == "© HL7.org 2011+"
    assert inst.date == fhirtypes.DateTime.validate("2017-01-18")
    assert inst.description == (
        "TestScript example resource with simple Patient search test."
        " The read tests will utilize user defined dynamic variables "
        "that will hold the Patient search parameter values."
    )
    assert inst.experimental is True
    assert inst.fixture[0].autocreate is False
    assert inst.fixture[0].autodelete is False
    assert inst.fixture[0].id == "fixture-patient-create"
    assert inst.fixture[0].resource.display == "Peter Chalmers"
    assert inst.fixture[0].resource.reference == "Patient/example"
    assert inst.id == "testscript-example-search"
    assert inst.identifier.system == "urn:ietf:rfc:3986"
    assert inst.identifier.value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.9881"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America (the)"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert (
        inst.metadata.capability[0].capabilities
        == "http://hl7.org/fhir/CapabilityStatement/example"
    )
    assert inst.metadata.capability[0].description == "Patient Search Operation"
    assert inst.metadata.capability[0].link[0] == "http://hl7.org/fhir/http.html#search"
    assert inst.metadata.capability[0].required is True
    assert inst.metadata.capability[0].validated is False
    assert inst.metadata.link[0].description == (
        "Demographics and other administrative information about an "
        "individual or animal receiving care or other health-related "
        "services."
    )
    assert inst.metadata.link[0].url == "http://hl7.org/fhir/patient.html"
    assert inst.name == "TestScript Example Search"
    assert inst.profile[0].id == "bundle-profile"
    assert inst.profile[0].reference == "http://hl7.org/fhir/StructureDefinition/Bundle"
    assert inst.publisher == "HL7"
    assert inst.purpose == "Patient Search Operation"
    assert inst.setup.action[0].operation.accept == "xml"
    assert (
        inst.setup.action[0].operation.description
        == "Test simple search to verify server support."
    )
    assert inst.setup.action[0].operation.encodeRequestUrl is True
    assert (
        inst.setup.action[0].operation.params
        == "?family=DONTEXPECTAMATCH&given=DONTEXPECTAMATCH"
    )
    assert inst.setup.action[0].operation.resource == "Patient"
    assert inst.setup.action[0].operation.type.code == "search"
    assert inst.setup.action[0].operation.type.system == (
        "http://terminology.hl7.org/CodeSystem/testscript-operation-" "codes"
    )
    assert inst.setup.action[1].assert_fhir.description == (
        "Confirm that the request url contains the family search " "parameter."
    )
    assert inst.setup.action[1].assert_fhir.direction == "request"
    assert inst.setup.action[1].assert_fhir.operator == "contains"
    assert inst.setup.action[1].assert_fhir.requestURL == "family"
    assert inst.setup.action[1].assert_fhir.warningOnly is False
    assert (
        inst.setup.action[2].assert_fhir.description
        == "Confirm that the returned HTTP status is 200(OK)."
    )
    assert inst.setup.action[2].assert_fhir.direction == "response"
    assert inst.setup.action[2].assert_fhir.responseCode == "200"
    assert inst.setup.action[2].assert_fhir.warningOnly is False
    assert (
        inst.setup.action[3].assert_fhir.description
        == "Confirm that the returned resource type is Bundle."
    )
    assert inst.setup.action[3].assert_fhir.resource == "Bundle"
    assert inst.setup.action[3].assert_fhir.warningOnly is False
    assert inst.setup.action[4].assert_fhir.description == (
        "Confirm that the returned Bundle correctly defines the " "navigation links."
    )
    assert inst.setup.action[4].assert_fhir.navigationLinks is True
    assert inst.setup.action[4].assert_fhir.warningOnly is False
    assert inst.status == "draft"
    assert inst.test[0].action[0].operation.accept == "xml"
    assert inst.test[0].action[0].operation.contentType == "xml"
    assert inst.test[0].action[0].operation.description == (
        "Create a Patient resource and capture the returned HTTP " "Header Location."
    )
    assert inst.test[0].action[0].operation.encodeRequestUrl is True
    assert inst.test[0].action[0].operation.resource == "Patient"
    assert inst.test[0].action[0].operation.responseId == "PatientCreateResponse"
    assert inst.test[0].action[0].operation.sourceId == "fixture-patient-create"
    assert inst.test[0].action[0].operation.type.code == "create"
    assert inst.test[0].action[0].operation.type.system == (
        "http://terminology.hl7.org/CodeSystem/testscript-operation-" "codes"
    )
    assert (
        inst.test[0].action[1].assert_fhir.description
        == "Confirm that the returned HTTP status is 201(Created)."
    )
    assert inst.test[0].action[1].assert_fhir.response == "created"
    assert inst.test[0].action[1].assert_fhir.warningOnly is False
    assert (
        inst.test[0].action[2].assert_fhir.description
        == "Confirm that the returned HTTP Header Location is present."
    )
    assert inst.test[0].action[2].assert_fhir.direction == "response"
    assert inst.test[0].action[2].assert_fhir.headerField == "Location"
    assert inst.test[0].action[2].assert_fhir.operator == "notEmpty"
    assert inst.test[0].action[2].assert_fhir.warningOnly is False
    assert inst.test[0].action[3].operation.accept == "xml"
    assert inst.test[0].action[3].operation.description == (
        "Read the created Patient using the captured Location URL " "value."
    )
    assert inst.test[0].action[3].operation.encodeRequestUrl is True
    assert inst.test[0].action[3].operation.type.code == "read"
    assert inst.test[0].action[3].operation.type.system == (
        "http://terminology.hl7.org/CodeSystem/testscript-operation-" "codes"
    )
    assert inst.test[0].action[3].operation.url == "${PatientCreateLocation}"
    assert (
        inst.test[0].action[4].assert_fhir.description
        == "Confirm that the returned HTTP status is 200(OK)."
    )
    assert inst.test[0].action[4].assert_fhir.response == "okay"
    assert inst.test[0].action[4].assert_fhir.warningOnly is False
    assert (
        inst.test[0].action[5].assert_fhir.description
        == "Confirm that the returned resource type is Patient."
    )
    assert inst.test[0].action[5].assert_fhir.resource == "Patient"
    assert inst.test[0].action[5].assert_fhir.warningOnly is False
    assert inst.test[0].description == (
        "Create a Patient resource and capture the returned HTTP "
        "Header Location. Then search for (read) that Patient using "
        "the Location URL value and validate the response."
    )
    assert inst.test[0].id == "01-PatientCreateSearch"
    assert inst.test[0].name == "Patient Create Search"
    assert inst.test[1].action[0].operation.accept == "xml"
    assert (
        inst.test[1].action[0].operation.description
        == "Search for Patient resources on the destination test system."
    )
    assert inst.test[1].action[0].operation.encodeRequestUrl is True
    assert inst.test[1].action[0].operation.params == (
        "?family=${PatientSearchFamilyName}&given=${PatientSearchGive" "nName}"
    )
    assert inst.test[1].action[0].operation.resource == "Patient"
    assert inst.test[1].action[0].operation.type.code == "search"
    assert inst.test[1].action[0].operation.type.system == (
        "http://terminology.hl7.org/CodeSystem/testscript-operation-" "codes"
    )
    assert (
        inst.test[1].action[1].assert_fhir.description
        == "Confirm that the returned HTTP status is 200(OK)."
    )
    assert inst.test[1].action[1].assert_fhir.response == "okay"
    assert inst.test[1].action[1].assert_fhir.warningOnly is False
    assert inst.test[1].action[2].assert_fhir.contentType == "xml"
    assert (
        inst.test[1].action[2].assert_fhir.description
        == "Confirm that the returned format is XML."
    )
    assert inst.test[1].action[2].assert_fhir.warningOnly is False
    assert (
        inst.test[1].action[3].assert_fhir.description
        == "Confirm that the returned resource type is Bundle."
    )
    assert inst.test[1].action[3].assert_fhir.resource == "Bundle"
    assert inst.test[1].action[3].assert_fhir.warningOnly is False
    assert inst.test[1].action[4].assert_fhir.description == (
        "Confirm that the returned Bundle conforms to the base FHIR " "specification."
    )
    assert inst.test[1].action[4].assert_fhir.validateProfileId == "bundle-profile"
    assert inst.test[1].action[4].assert_fhir.warningOnly is False
    assert (
        inst.test[1].action[5].assert_fhir.description
        == "Confirm that the returned Bundle type equals 'searchset'."
    )
    assert inst.test[1].action[5].assert_fhir.operator == "equals"
    assert inst.test[1].action[5].assert_fhir.path == "fhir:Bundle/fhir:type/@value"
    assert inst.test[1].action[5].assert_fhir.value == "searchset"
    assert inst.test[1].action[5].assert_fhir.warningOnly is False
    assert inst.test[1].action[6].assert_fhir.description == (
        "Confirm that the returned Bundle total is greater than or "
        "equal to the number of returned entries."
    )
    assert (
        inst.test[1].action[6].assert_fhir.expression
        == "Bundle.total.toInteger() >= entry.count()"
    )
    assert inst.test[1].action[6].assert_fhir.warningOnly is False
    assert inst.test[1].description == (
        "Search for Patient resources using the user defined dynamic "
        "variables ${PatientSearchFamilyName} and "
        "${PatientSearchGivenName} and validate response."
    )
    assert inst.test[1].id == "02-PatientSearchDynamic"
    assert inst.test[1].name == "Patient Search Dynamic"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/TestScript/testscript-example-search"
    assert inst.variable[0].headerField == "Location"
    assert inst.variable[0].name == "PatientCreateLocation"
    assert inst.variable[0].sourceId == "PatientCreateResponse"
    assert inst.variable[1].description == (
        "Enter patient search criteria for a known family name on the" " target system"
    )
    assert inst.variable[1].hint == "[Family name]"
    assert inst.variable[1].name == "PatientSearchFamilyName"
    assert inst.variable[2].description == (
        "Enter patient search criteria for a known given name on the " "target system"
    )
    assert inst.variable[2].hint == "[Given name]"
    assert inst.variable[2].name == "PatientSearchGivenName"
    assert (
        inst.variable[3].description
        == "Evaluate the returned Patient searchset Bundle.total value"
    )
    assert inst.variable[3].expression == "Bundle.total.toInteger()"
    assert inst.variable[3].name == "PatientSearchBundleTotal"
    assert inst.version == "1.0"


def test_testscript_4(base_settings):
    """No. 4 tests collection for TestScript.
    Test File: testscript-example-search.json
    """
    filename = base_settings["unittest_data_dir"] / "testscript-example-search.json"
    inst = testscript.TestScript.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "TestScript" == inst.resource_type

    impl_testscript_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "TestScript" == data["resourceType"]

    inst2 = testscript.TestScript(**data)
    impl_testscript_4(inst2)


def impl_testscript_5(inst):
    assert inst.contact[0].name == "Support"
    assert inst.contact[0].telecom[0].system == "email"
    assert inst.contact[0].telecom[0].use == "work"
    assert inst.contact[0].telecom[0].value == "support@HL7.org"
    assert inst.copyright == "© HL7.org 2011+"
    assert inst.date == fhirtypes.DateTime.validate("2017-01-18")
    assert inst.description == (
        "TestScript example resource with setup to delete if present "
        "and create a new instance of a Patient; and single test "
        "definition to read the created Patient with various asserts."
    )
    assert inst.experimental is True
    assert inst.fixture[0].autocreate is False
    assert inst.fixture[0].autodelete is False
    assert inst.fixture[0].id == "fixture-patient-create"
    assert inst.fixture[0].resource.display == "Peter Chalmers"
    assert inst.fixture[0].resource.reference == "Patient/example"
    assert inst.fixture[1].autocreate is False
    assert inst.fixture[1].autodelete is False
    assert inst.fixture[1].id == "fixture-patient-minimum"
    assert inst.fixture[1].resource.display == "Peter Chalmers (minimum)"
    assert inst.fixture[1].resource.reference == "Patient/example"
    assert inst.id == "testscript-example"
    assert inst.identifier.system == "urn:ietf:rfc:3986"
    assert inst.identifier.value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.9876"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America (the)"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert (
        inst.metadata.capability[0].capabilities
        == "http://hl7.org/fhir/CapabilityStatement/example"
    )
    assert (
        inst.metadata.capability[0].description
        == "Patient Update, Read and Delete Operations"
    )
    assert inst.metadata.capability[0].link[0] == "http://hl7.org/fhir/http.html#delete"
    assert inst.metadata.capability[0].link[1] == "http://hl7.org/fhir/http.html#read"
    assert inst.metadata.capability[0].link[2] == "http://hl7.org/fhir/http.html#update"
    assert inst.metadata.capability[0].required is True
    assert inst.metadata.capability[0].validated is False
    assert inst.metadata.link[0].description == (
        "Demographics and other administrative information about an "
        "individual or animal receiving care or other health-related "
        "services."
    )
    assert inst.metadata.link[0].url == "http://hl7.org/fhir/patient.html"
    assert inst.name == "TestScript Example"
    assert inst.profile[0].id == "patient-profile"
    assert (
        inst.profile[0].reference == "http://hl7.org/fhir/StructureDefinition/Patient"
    )
    assert inst.publisher == "HL7"
    assert inst.purpose == (
        "Patient Conditional Create (Update), Read and Delete " "Operations"
    )
    assert inst.setup.action[0].operation.accept == "json"
    assert inst.setup.action[0].operation.description == (
        "Execute a delete operation to insure the patient does not "
        "exist on the server."
    )
    assert inst.setup.action[0].operation.encodeRequestUrl is True
    assert inst.setup.action[0].operation.label == "SetupDeletePatient"
    assert inst.setup.action[0].operation.params == "/${createResourceId}"
    assert inst.setup.action[0].operation.resource == "Patient"
    assert inst.setup.action[0].operation.type.code == "delete"
    assert inst.setup.action[0].operation.type.system == (
        "http://terminology.hl7.org/CodeSystem/testscript-operation-" "codes"
    )
    assert inst.setup.action[1].assert_fhir.description == (
        "Confirm that the returned HTTP status is 200(OK) or 204(No " "Content)."
    )
    assert inst.setup.action[1].assert_fhir.direction == "response"
    assert inst.setup.action[1].assert_fhir.operator == "in"
    assert inst.setup.action[1].assert_fhir.responseCode == "200,204"
    assert inst.setup.action[1].assert_fhir.warningOnly is False
    assert inst.setup.action[2].operation.accept == "json"
    assert inst.setup.action[2].operation.contentType == "json"
    assert inst.setup.action[2].operation.description == (
        "Create patient resource on test server using the contents of"
        " fixture-patient-create"
    )
    assert inst.setup.action[2].operation.encodeRequestUrl is True
    assert inst.setup.action[2].operation.label == "SetupCreatePatient"
    assert inst.setup.action[2].operation.params == "/${createResourceId}"
    assert inst.setup.action[2].operation.resource == "Patient"
    assert inst.setup.action[2].operation.sourceId == "fixture-patient-create"
    assert inst.setup.action[2].operation.type.code == "update"
    assert inst.setup.action[2].operation.type.system == (
        "http://terminology.hl7.org/CodeSystem/testscript-operation-" "codes"
    )
    assert (
        inst.setup.action[3].assert_fhir.description
        == "Confirm that the returned HTTP status is 201(Created)."
    )
    assert inst.setup.action[3].assert_fhir.direction == "response"
    assert inst.setup.action[3].assert_fhir.responseCode == "201"
    assert inst.setup.action[3].assert_fhir.warningOnly is False
    assert inst.setup.action[4].operation.description == (
        "Read the created patient resource on the test server using "
        "the id from fixture-patient-create. Verify contents."
    )
    assert inst.setup.action[4].operation.encodeRequestUrl is True
    assert inst.setup.action[4].operation.resource == "Patient"
    assert inst.setup.action[4].operation.targetId == "fixture-patient-create"
    assert inst.setup.action[4].operation.type.code == "read"
    assert inst.setup.action[4].operation.type.system == (
        "http://terminology.hl7.org/CodeSystem/testscript-operation-" "codes"
    )
    assert (
        inst.setup.action[5].assert_fhir.description
        == "Confirm that the returned HTTP status is 200(OK)."
    )
    assert inst.setup.action[5].assert_fhir.direction == "response"
    assert inst.setup.action[5].assert_fhir.response == "okay"
    assert inst.setup.action[5].assert_fhir.warningOnly is False
    assert (
        inst.setup.action[6].assert_fhir.compareToSourceExpression
        == "Patient.name.first().family"
    )
    assert (
        inst.setup.action[6].assert_fhir.compareToSourceId == "fixture-patient-create"
    )
    assert inst.setup.action[6].assert_fhir.description == (
        "Confirm that the returned Patient contains the expected "
        "family name 'Chalmers'. Uses explicit compareToSourceId "
        "reference to fixture-patient-create used to create the "
        "Patient."
    )
    assert inst.setup.action[6].assert_fhir.operator == "equals"
    assert inst.setup.action[6].assert_fhir.warningOnly is False
    assert inst.status == "draft"
    assert inst.teardown.action[0].operation.description == (
        "Delete the patient resource on the test server using the id "
        "from fixture-patient-create."
    )
    assert inst.teardown.action[0].operation.encodeRequestUrl is True
    assert inst.teardown.action[0].operation.resource == "Patient"
    assert inst.teardown.action[0].operation.targetId == "fixture-patient-create"
    assert inst.teardown.action[0].operation.type.code == "delete"
    assert inst.teardown.action[0].operation.type.system == (
        "http://terminology.hl7.org/CodeSystem/testscript-operation-" "codes"
    )
    assert inst.test[0].action[0].operation.description == (
        "Read the patient resource on the test server using the id "
        "from fixture-patient-create. Prevent URL encoding of the "
        "request."
    )
    assert inst.test[0].action[0].operation.encodeRequestUrl is False
    assert inst.test[0].action[0].operation.resource == "Patient"
    assert inst.test[0].action[0].operation.responseId == "fixture-patient-read"
    assert inst.test[0].action[0].operation.targetId == "fixture-patient-create"
    assert inst.test[0].action[0].operation.type.code == "read"
    assert inst.test[0].action[0].operation.type.system == (
        "http://terminology.hl7.org/CodeSystem/testscript-operation-" "codes"
    )
    assert (
        inst.test[0].action[1].assert_fhir.description
        == "Confirm that the returned HTTP status is 200(OK)."
    )
    assert inst.test[0].action[1].assert_fhir.direction == "response"
    assert inst.test[0].action[1].assert_fhir.label == "01-ReadPatientOK"
    assert inst.test[0].action[1].assert_fhir.response == "okay"
    assert inst.test[0].action[1].assert_fhir.warningOnly is False
    assert inst.test[0].action[2].assert_fhir.description == (
        "Confirm that the returned HTTP Header Last-Modified is "
        "present. Warning only as the server might not support "
        "versioning."
    )
    assert inst.test[0].action[2].assert_fhir.direction == "response"
    assert inst.test[0].action[2].assert_fhir.headerField == "Last-Modified"
    assert inst.test[0].action[2].assert_fhir.operator == "notEmpty"
    assert inst.test[0].action[2].assert_fhir.warningOnly is True
    assert (
        inst.test[0].action[3].assert_fhir.description
        == "Confirm that the returned resource type is Patient."
    )
    assert inst.test[0].action[3].assert_fhir.resource == "Patient"
    assert inst.test[0].action[3].assert_fhir.warningOnly is False
    assert inst.test[0].action[4].assert_fhir.description == (
        "Confirm that the returned Patient conforms to the base FHIR " "specification."
    )
    assert inst.test[0].action[4].assert_fhir.validateProfileId == "patient-profile"
    assert inst.test[0].action[4].assert_fhir.warningOnly is False
    assert inst.test[0].action[5].assert_fhir.description == (
        "Confirm that the returned Patient contains the expected "
        "family name 'Chalmers'. Uses explicit sourceId reference to "
        "read responseId fixture."
    )
    assert inst.test[0].action[5].assert_fhir.operator == "equals"
    assert (
        inst.test[0].action[5].assert_fhir.path
        == "fhir:Patient/fhir:name/fhir:family/@value"
    )
    assert inst.test[0].action[5].assert_fhir.sourceId == "fixture-patient-read"
    assert inst.test[0].action[5].assert_fhir.value == "Chalmers"
    assert inst.test[0].action[5].assert_fhir.warningOnly is False
    assert inst.test[0].action[6].assert_fhir.description == (
        "Confirm that the returned Patient contains the expected "
        "given name 'Peter'. Uses explicit sourceId reference to read"
        " responseId fixture."
    )
    assert inst.test[0].action[6].assert_fhir.operator == "equals"
    assert (
        inst.test[0].action[6].assert_fhir.path
        == "fhir:Patient/fhir:name/fhir:given/@value"
    )
    assert inst.test[0].action[6].assert_fhir.sourceId == "fixture-patient-read"
    assert inst.test[0].action[6].assert_fhir.value == "Peter"
    assert inst.test[0].action[6].assert_fhir.warningOnly is False
    assert (
        inst.test[0].action[7].assert_fhir.compareToSourceId == "fixture-patient-create"
    )
    assert (
        inst.test[0].action[7].assert_fhir.compareToSourcePath
        == "fhir:Patient/fhir:name/fhir:family/@value"
    )
    assert inst.test[0].action[7].assert_fhir.operator == "equals"
    assert (
        inst.test[0].action[7].assert_fhir.path
        == "fhir:Patient/fhir:name/fhir:family/@value"
    )
    assert inst.test[0].action[7].assert_fhir.warningOnly is False
    assert (
        inst.test[0].action[8].assert_fhir.compareToSourceId == "fixture-patient-create"
    )
    assert (
        inst.test[0].action[8].assert_fhir.compareToSourcePath
        == "fhir:Patient/fhir:name/fhir:given/@value"
    )
    assert (
        inst.test[0].action[8].assert_fhir.path
        == "fhir:Patient/fhir:name/fhir:given/@value"
    )
    assert inst.test[0].action[8].assert_fhir.sourceId == "fixture-patient-read"
    assert inst.test[0].action[8].assert_fhir.warningOnly is False
    assert inst.test[0].action[9].assert_fhir.description == (
        "Confirm that the returned resource contains the expected "
        "retained elements and values. Warning only to provide users "
        "with reviewable results."
    )
    assert inst.test[0].action[9].assert_fhir.minimumId == "fixture-patient-minimum"
    assert inst.test[0].action[9].assert_fhir.warningOnly is True
    assert inst.test[0].description == "Read a Patient and validate response."
    assert inst.test[0].id == "01-ReadPatient"
    assert inst.test[0].name == "Read Patient"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/TestScript/testscript-example"
    assert inst.useContext[0].code.code == "focus"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueCodeableConcept.coding[0].code == "positive"
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/variant-state"
    )
    assert inst.variable[0].name == "createResourceId"
    assert inst.variable[0].path == "Patient/id"
    assert inst.variable[0].sourceId == "fixture-patient-create"
    assert inst.version == "1.0"


def test_testscript_5(base_settings):
    """No. 5 tests collection for TestScript.
    Test File: testscript-example.json
    """
    filename = base_settings["unittest_data_dir"] / "testscript-example.json"
    inst = testscript.TestScript.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "TestScript" == inst.resource_type

    impl_testscript_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "TestScript" == data["resourceType"]

    inst2 = testscript.TestScript(**data)
    impl_testscript_5(inst2)


def impl_testscript_6(inst):
    assert inst.contact[0].name == "Support"
    assert inst.contact[0].telecom[0].system == "email"
    assert inst.contact[0].telecom[0].use == "work"
    assert inst.contact[0].telecom[0].value == "support@HL7.org"
    assert inst.copyright == "© HL7.org 2011+"
    assert inst.date == fhirtypes.DateTime.validate("2017-01-18")
    assert inst.description == (
        "TestScript example resource with ported Sprinkler basic read"
        " tests R001, R002, R003, R004. The read tests will utilize "
        "user defined dynamic variables that will hold the Patient "
        "resource id values."
    )
    assert inst.experimental is True
    assert inst.id == "testscript-example-readtest"
    assert inst.identifier.system == "urn:ietf:rfc:3986"
    assert inst.identifier.value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.9879"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America (the)"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert (
        inst.metadata.capability[0].capabilities
        == "http://hl7.org/fhir/CapabilityStatement/example"
    )
    assert inst.metadata.capability[0].description == "Patient Read Operation"
    assert inst.metadata.capability[0].link[0] == "http://hl7.org/fhir/http.html#read"
    assert inst.metadata.capability[0].required is True
    assert inst.metadata.capability[0].validated is False
    assert inst.metadata.link[0].description == (
        "Demographics and other administrative information about an "
        "individual or animal receiving care or other health-related "
        "services."
    )
    assert inst.metadata.link[0].url == "http://hl7.org/fhir/patient.html"
    assert inst.name == "TestScript Example Read Test"
    assert inst.profile[0].id == "patient-profile"
    assert (
        inst.profile[0].reference == "http://hl7.org/fhir/StructureDefinition/Patient"
    )
    assert inst.publisher == "HL7"
    assert inst.purpose == "Patient Read Operation"
    assert inst.status == "draft"
    assert inst.test[0].action[0].operation.accept == "xml"
    assert inst.test[0].action[0].operation.description == (
        "Read the known Patient resource on the destination test "
        "system using the user defined dynamic variable "
        "${KnownPatientResourceId}."
    )
    assert inst.test[0].action[0].operation.encodeRequestUrl is True
    assert inst.test[0].action[0].operation.params == "/${KnownPatientResourceId}"
    assert inst.test[0].action[0].operation.resource == "Patient"
    assert inst.test[0].action[0].operation.type.code == "read"
    assert inst.test[0].action[0].operation.type.system == (
        "http://terminology.hl7.org/CodeSystem/testscript-operation-" "codes"
    )
    assert (
        inst.test[0].action[1].assert_fhir.description
        == "Confirm that the returned HTTP status is 200(OK)."
    )
    assert inst.test[0].action[1].assert_fhir.response == "okay"
    assert inst.test[0].action[1].assert_fhir.warningOnly is False
    assert inst.test[0].action[2].assert_fhir.contentType == "xml"
    assert (
        inst.test[0].action[2].assert_fhir.description
        == "Confirm that the returned format is XML."
    )
    assert inst.test[0].action[2].assert_fhir.warningOnly is False
    assert inst.test[0].action[3].assert_fhir.description == (
        "Confirm that the returned HTTP Header Last-Modified is "
        "present. Warning only as the server might not support "
        "versioning."
    )
    assert inst.test[0].action[3].assert_fhir.headerField == "Last-Modified"
    assert inst.test[0].action[3].assert_fhir.operator == "notEmpty"
    assert inst.test[0].action[3].assert_fhir.warningOnly is True
    assert (
        inst.test[0].action[4].assert_fhir.description
        == "Confirm that the returned resource type is Patient."
    )
    assert inst.test[0].action[4].assert_fhir.resource == "Patient"
    assert inst.test[0].action[4].assert_fhir.warningOnly is False
    assert inst.test[0].action[5].assert_fhir.description == (
        "Confirm that the returned Patient conforms to the base FHIR " "specification."
    )
    assert inst.test[0].action[5].assert_fhir.validateProfileId == "patient-profile"
    assert inst.test[0].action[5].assert_fhir.warningOnly is False
    assert inst.test[0].description == "Read a known Patient and validate response."
    assert inst.test[0].id == "R001"
    assert inst.test[0].name == "Sprinkler Read Test R001"
    assert inst.test[1].action[0].operation.accept == "xml"
    assert inst.test[1].action[0].operation.encodeRequestUrl is True
    assert inst.test[1].action[0].operation.params == "/1"
    assert inst.test[1].action[0].operation.resource == "Patient"
    assert inst.test[1].action[0].operation.type.code == "read"
    assert inst.test[1].action[0].operation.type.system == (
        "http://terminology.hl7.org/CodeSystem/testscript-operation-" "codes"
    )
    assert (
        inst.test[1].action[1].assert_fhir.description
        == "Confirm that the returned HTTP status is 404(Not Found)."
    )
    assert inst.test[1].action[1].assert_fhir.response == "notFound"
    assert inst.test[1].action[1].assert_fhir.warningOnly is False
    assert (
        inst.test[1].description
        == "Read an unknown Resource Type and validate response."
    )
    assert inst.test[1].id == "R002"
    assert inst.test[1].name == "Sprinkler Read Test R002"
    assert inst.test[2].action[0].operation.accept == "xml"
    assert inst.test[2].action[0].operation.description == (
        "Attempt to read the non-existing Patient resource on the "
        "destination test system using the user defined dynamic "
        "variable ${NonExistsPatientResourceId}."
    )
    assert inst.test[2].action[0].operation.encodeRequestUrl is True
    assert inst.test[2].action[0].operation.params == "/${NonExistsPatientResourceId}"
    assert inst.test[2].action[0].operation.resource == "Patient"
    assert inst.test[2].action[0].operation.type.code == "read"
    assert inst.test[2].action[0].operation.type.system == (
        "http://terminology.hl7.org/CodeSystem/testscript-operation-" "codes"
    )
    assert (
        inst.test[2].action[1].assert_fhir.description
        == "Confirm that the returned HTTP status is 404(Not Found)."
    )
    assert inst.test[2].action[1].assert_fhir.response == "notFound"
    assert inst.test[2].action[1].assert_fhir.warningOnly is False
    assert (
        inst.test[2].description
        == "Read a known, non-existing Patient and validate response."
    )
    assert inst.test[2].id == "R003"
    assert inst.test[2].name == "Sprinkler Read Test R003"
    assert inst.test[3].action[0].operation.accept == "xml"
    assert inst.test[3].action[0].operation.description == (
        "Attempt to read a Patient resource on the destination test "
        "system using known bad formatted resource id."
    )
    assert inst.test[3].action[0].operation.encodeRequestUrl is True
    assert inst.test[3].action[0].operation.params == "/ID-may-not-contain-CAPITALS"
    assert inst.test[3].action[0].operation.resource == "Patient"
    assert inst.test[3].action[0].operation.type.code == "read"
    assert inst.test[3].action[0].operation.type.system == (
        "http://terminology.hl7.org/CodeSystem/testscript-operation-" "codes"
    )
    assert (
        inst.test[3].action[1].assert_fhir.description
        == "Confirm that the returned HTTP status is 400(Bad Request)."
    )
    assert inst.test[3].action[1].assert_fhir.response == "bad"
    assert inst.test[3].action[1].assert_fhir.warningOnly is False
    assert inst.test[3].description == (
        "Read a Patient using a known bad formatted resource id and "
        "validate response."
    )
    assert inst.test[3].id == "R004"
    assert inst.test[3].name == "Sprinkler Read Test R004"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/TestScript/testscript-example-readtest"
    assert inst.variable[0].defaultValue == "example"
    assert inst.variable[0].name == "KnownPatientResourceId"
    assert inst.variable[1].defaultValue == "does-not-exist"
    assert inst.variable[1].name == "NonExistsPatientResourceId"
    assert inst.version == "1.0"


def test_testscript_6(base_settings):
    """No. 6 tests collection for TestScript.
    Test File: testscript-example-readtest.json
    """
    filename = base_settings["unittest_data_dir"] / "testscript-example-readtest.json"
    inst = testscript.TestScript.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "TestScript" == inst.resource_type

    impl_testscript_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "TestScript" == data["resourceType"]

    inst2 = testscript.TestScript(**data)
    impl_testscript_6(inst2)
