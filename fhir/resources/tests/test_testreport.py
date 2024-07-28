# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/TestReport
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import testreport
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


def impl_testreport_1(inst):
    assert inst.id == "testreport-example"
    assert (
        inst.identifier.system
        == ExternalValidatorModel(valueUri="urn:ietf:rfc:3986").valueUri
    )
    assert inst.identifier.value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.9878"
    assert (
        inst.issued
        == ExternalValidatorModel(
            valueDateTime="2016-10-07T08:25:34-05:00"
        ).valueDateTime
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.name == "TestReport Example for TestScript Example"
    assert inst.participant[0].display == "Crucible"
    assert inst.participant[0].type == "test-engine"
    assert (
        inst.participant[0].uri
        == ExternalValidatorModel(valueUri="http://projectcrucible.org").valueUri
    )
    assert inst.participant[1].display == "HealthIntersections STU3"
    assert inst.participant[1].type == "server"
    assert (
        inst.participant[1].uri
        == ExternalValidatorModel(
            valueUri="http://fhir3.healthintersections.com.au/open"
        ).valueUri
    )
    assert inst.result == "pass"
    assert float(inst.score) == float(100.0)
    assert (
        inst.setup.action[0].operation.detail
        == ExternalValidatorModel(
            valueUri="http://projectcrucible.org/permalink/1"
        ).valueUri
    )
    assert inst.setup.action[0].operation.message == "DELETE Patient"
    assert inst.setup.action[0].operation.result == "pass"
    assert (
        inst.setup.action[1].assert_fhir.detail
        == "http://projectcrucible.org/permalink/1"
    )
    assert inst.setup.action[1].assert_fhir.message == "HTTP 204"
    assert inst.setup.action[1].assert_fhir.result == "pass"
    assert (
        inst.setup.action[2].operation.detail
        == ExternalValidatorModel(
            valueUri="http://projectcrucible.org/permalink/1"
        ).valueUri
    )
    assert (
        inst.setup.action[2].operation.message == "POST Patient/fixture-patient-create"
    )
    assert inst.setup.action[2].operation.result == "pass"
    assert (
        inst.setup.action[3].assert_fhir.detail
        == "http://projectcrucible.org/permalink/1"
    )
    assert inst.setup.action[3].assert_fhir.message == "HTTP 201"
    assert inst.setup.action[3].assert_fhir.result == "pass"
    assert inst.status == "completed"
    assert (
        inst.teardown.action[0].operation.detail
        == ExternalValidatorModel(
            valueUri="http://projectcrucible.org/permalink/3"
        ).valueUri
    )
    assert (
        inst.teardown.action[0].operation.message
        == "DELETE Patient/fixture-patient-create."
    )
    assert inst.teardown.action[0].operation.result == "pass"
    assert inst.testScript == "http://example.com/TestScript/testscript-example"
    assert (
        inst.test[0].action[0].operation.detail
        == ExternalValidatorModel(
            valueUri="http://projectcrucible.org/permalink/2"
        ).valueUri
    )
    assert (
        inst.test[0].action[0].operation.message == "GET Patient/fixture-patient-create"
    )
    assert inst.test[0].action[0].operation.result == "pass"
    assert (
        inst.test[0].action[1].assert_fhir.detail
        == "http://projectcrucible.org/permalink/2"
    )
    assert inst.test[0].action[1].assert_fhir.message == "HTTP 200"
    assert inst.test[0].action[1].assert_fhir.result == "pass"
    assert (
        inst.test[0].action[2].assert_fhir.detail
        == "http://projectcrucible.org/permalink/2"
    )
    assert inst.test[0].action[2].assert_fhir.message == "Last-Modified Present"
    assert inst.test[0].action[2].assert_fhir.result == "pass"
    assert (
        inst.test[0].action[3].assert_fhir.detail
        == "http://projectcrucible.org/permalink/2"
    )
    assert inst.test[0].action[3].assert_fhir.message == "Response is Patient"
    assert inst.test[0].action[3].assert_fhir.result == "pass"
    assert (
        inst.test[0].action[4].assert_fhir.detail
        == "http://projectcrucible.org/permalink/2"
    )
    assert inst.test[0].action[4].assert_fhir.message == "Response validates"
    assert inst.test[0].action[4].assert_fhir.result == "pass"
    assert (
        inst.test[0].action[5].assert_fhir.detail
        == "http://projectcrucible.org/permalink/2"
    )
    assert (
        inst.test[0].action[5].assert_fhir.message == "Patient.name.family 'Chalmers'"
    )
    assert inst.test[0].action[5].assert_fhir.result == "pass"
    assert (
        inst.test[0].action[6].assert_fhir.detail
        == "http://projectcrucible.org/permalink/2"
    )
    assert inst.test[0].action[6].assert_fhir.message == "Patient.name.given 'Peter'"
    assert inst.test[0].action[6].assert_fhir.result == "pass"
    assert (
        inst.test[0].action[7].assert_fhir.detail
        == "http://projectcrucible.org/permalink/2"
    )
    assert (
        inst.test[0].action[7].assert_fhir.message == "Patient.name.family 'Chalmers'"
    )
    assert inst.test[0].action[7].assert_fhir.result == "pass"
    assert (
        inst.test[0].action[8].assert_fhir.detail
        == "http://projectcrucible.org/permalink/2"
    )
    assert (
        inst.test[0].action[8].assert_fhir.message == "Patient.name.family 'Chalmers'"
    )
    assert inst.test[0].action[8].assert_fhir.result == "pass"
    assert (
        inst.test[0].action[9].assert_fhir.detail
        == "http://projectcrucible.org/permalink/2"
    )
    assert inst.test[0].action[9].assert_fhir.message == "Patient expected values."
    assert inst.test[0].action[9].assert_fhir.result == "pass"
    assert inst.test[0].description == "Read a Patient and validate response."
    assert inst.test[0].id == "01-ReadPatient"
    assert inst.test[0].name == "Read Patient"
    assert inst.tester == "HL7 Execution Engine"
    assert inst.text.status == "generated"


def test_testreport_1(base_settings):
    """No. 1 tests collection for TestReport.
    Test File: testreport-example.json
    """
    filename = base_settings["unittest_data_dir"] / "testreport-example.json"
    inst = testreport.TestReport.model_validate_json(filename.read_bytes())
    assert "TestReport" == inst.get_resource_type()

    impl_testreport_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "TestReport" == data["resourceType"]

    inst2 = testreport.TestReport(**data)
    impl_testreport_1(inst2)
