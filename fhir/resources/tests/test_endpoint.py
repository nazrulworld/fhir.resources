# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Endpoint
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import endpoint
from .fixtures import ExternalValidatorModel


def impl_endpoint_1(inst):
    assert (
        inst.address
        == ExternalValidatorModel.model_validate(
            {"valueUrl": "mailto:MARTIN.SMIETANKA@directnppes.com"}
        ).valueUrl
    )
    assert inst.connectionType[0].coding[0].code == "direct-project"
    assert inst.id == "direct-endpoint"
    assert inst.managingOrganization.reference == "Organization/f201"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.name == "MARTIN SMIETANKA"
    assert inst.payload[0].mimeType[0] == "text/x-hl7-text+xml"
    assert inst.payload[0].mimeType[1] == "application/fhir+xml"
    assert inst.payload[0].mimeType[2] == "application/fhir+json"
    assert (
        inst.payload[0].type[0].coding[0].code
        == "urn:hl7-org:sdwg:ccda-structuredBody:1.1"
    )
    assert (
        inst.payload[0].type[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:oid:1.3.6.1.4.1.19376.1.2.3"}
        ).valueUri
    )
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_endpoint_1(base_settings):
    """No. 1 tests collection for Endpoint.
    Test File: endpoint-example-direct.json
    """
    filename = base_settings["unittest_data_dir"] / "endpoint-example-direct.json"
    inst = endpoint.Endpoint.model_validate_json(filename.read_bytes())
    assert "Endpoint" == inst.get_resource_type()

    impl_endpoint_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Endpoint" == data["resourceType"]

    inst2 = endpoint.Endpoint(**data)
    impl_endpoint_1(inst2)


def impl_endpoint_2(inst):
    assert (
        inst.address
        == ExternalValidatorModel.model_validate(
            {"valueUrl": "https://pacs.hospital.org/wado-rs"}
        ).valueUrl
    )
    assert inst.connectionType[0].coding[0].code == "dicom-wado-rs"
    assert (
        inst.connectionType[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/endpoint-connection-type"
            }
        ).valueUri
    )
    assert inst.id == "example-wadors"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.name == "PACS Hospital DICOM WADO-RS endpoint"
    assert inst.payload[0].mimeType[0] == "application/dicom"
    assert inst.payload[0].type[0].text == "DICOM WADO-RS"
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_endpoint_2(base_settings):
    """No. 2 tests collection for Endpoint.
    Test File: endpoint-example-wadors.json
    """
    filename = base_settings["unittest_data_dir"] / "endpoint-example-wadors.json"
    inst = endpoint.Endpoint.model_validate_json(filename.read_bytes())
    assert "Endpoint" == inst.get_resource_type()

    impl_endpoint_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Endpoint" == data["resourceType"]

    inst2 = endpoint.Endpoint(**data)
    impl_endpoint_2(inst2)


def impl_endpoint_3(inst):
    assert (
        inst.address
        == ExternalValidatorModel.model_validate(
            {"valueUrl": "http://fhir3.healthintersections.com.au/open/CarePlan"}
        ).valueUrl
    )
    assert inst.connectionType[0].coding[0].code == "hl7-fhir-rest"
    assert (
        inst.connectionType[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/endpoint-connection-type"
            }
        ).valueUri
    )
    assert inst.contact[0].system == "email"
    assert inst.contact[0].use == "work"
    assert inst.contact[0].value == "endpointmanager@example.org"
    assert inst.description == (
        "The CarePlan hub provides a test/dev environment for testing" " submissions"
    )
    assert inst.environmentType[0].coding[0].code == "test"
    assert (
        inst.environmentType[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/endpoint-environment"}
        ).valueUri
    )
    assert inst.environmentType[1].coding[0].code == "dev"
    assert (
        inst.environmentType[1].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/endpoint-environment"}
        ).valueUri
    )
    assert inst.header[0] == "bearer-code BASGS534s4"
    assert inst.id == "example"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://example.org/enpoint-identifier"}
        ).valueUri
    )
    assert inst.identifier[0].value == "epcp12"
    assert inst.managingOrganization.reference == "Organization/hl7"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.name == "Health Intersections CarePlan Hub"
    assert inst.payload[0].mimeType[0] == "application/fhir+xml"
    assert inst.payload[0].type[0].coding[0].code == "CarePlan"
    assert (
        inst.payload[0].type[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/fhir-types"}
        ).valueUri
    )
    assert (
        inst.period.start
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2014-09-01"}
        ).valueDateTime
    )
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_endpoint_3(base_settings):
    """No. 3 tests collection for Endpoint.
    Test File: endpoint-example.json
    """
    filename = base_settings["unittest_data_dir"] / "endpoint-example.json"
    inst = endpoint.Endpoint.model_validate_json(filename.read_bytes())
    assert "Endpoint" == inst.get_resource_type()

    impl_endpoint_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Endpoint" == data["resourceType"]

    inst2 = endpoint.Endpoint(**data)
    impl_endpoint_3(inst2)
