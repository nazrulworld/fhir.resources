# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Endpoint
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import endpoint


def impl_endpoint_1(inst):
    assert inst.address == "https://pacs.hospital.org/IHEInvokeImageDisplay"
    assert inst.connectionType.code == "ihe-iid"
    assert inst.connectionType.system == (
        "http://terminology.hl7.org/CodeSystem/endpoint-connection-" "type"
    )
    assert inst.id == "example-iid"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name == "PACS Hospital Invoke Image Display endpoint"
    assert inst.payloadType[0].text == "DICOM IID"
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_endpoint_1(base_settings):
    """No. 1 tests collection for Endpoint.
    Test File: endpoint-example-iid.json
    """
    filename = base_settings["unittest_data_dir"] / "endpoint-example-iid.json"
    inst = endpoint.Endpoint.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Endpoint" == inst.resource_type

    impl_endpoint_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Endpoint" == data["resourceType"]

    inst2 = endpoint.Endpoint(**data)
    impl_endpoint_1(inst2)


def impl_endpoint_2(inst):
    assert inst.address == "mailto:MARTIN.SMIETANKA@directnppes.com"
    assert inst.connectionType.code == "direct-project"
    assert inst.id == "direct-endpoint"
    assert inst.managingOrganization.reference == "Organization/299"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name == "MARTIN SMIETANKA"
    assert (
        inst.payloadType[0].coding[0].code == "urn:hl7-org:sdwg:ccda-structuredBody:1.1"
    )
    assert inst.payloadType[0].coding[0].system == "urn:oid:1.3.6.1.4.1.19376.1.2.3"
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_endpoint_2(base_settings):
    """No. 2 tests collection for Endpoint.
    Test File: endpoint-example-direct.json
    """
    filename = base_settings["unittest_data_dir"] / "endpoint-example-direct.json"
    inst = endpoint.Endpoint.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Endpoint" == inst.resource_type

    impl_endpoint_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Endpoint" == data["resourceType"]

    inst2 = endpoint.Endpoint(**data)
    impl_endpoint_2(inst2)


def impl_endpoint_3(inst):
    assert inst.address == "https://pacs.hospital.org/wado-rs"
    assert inst.connectionType.code == "dicom-wado-rs"
    assert inst.connectionType.system == (
        "http://terminology.hl7.org/CodeSystem/endpoint-connection-" "type"
    )
    assert inst.id == "example-wadors"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name == "PACS Hospital DICOM WADO-RS endpoint"
    assert inst.payloadMimeType[0] == "application/dicom"
    assert inst.payloadType[0].text == "DICOM WADO-RS"
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_endpoint_3(base_settings):
    """No. 3 tests collection for Endpoint.
    Test File: endpoint-example-wadors.json
    """
    filename = base_settings["unittest_data_dir"] / "endpoint-example-wadors.json"
    inst = endpoint.Endpoint.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Endpoint" == inst.resource_type

    impl_endpoint_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Endpoint" == data["resourceType"]

    inst2 = endpoint.Endpoint(**data)
    impl_endpoint_3(inst2)


def impl_endpoint_4(inst):
    assert inst.address == "http://fhir3.healthintersections.com.au/open/CarePlan"
    assert inst.connectionType.code == "hl7-fhir-rest"
    assert inst.connectionType.system == (
        "http://terminology.hl7.org/CodeSystem/endpoint-connection-" "type"
    )
    assert inst.contact[0].system == "email"
    assert inst.contact[0].use == "work"
    assert inst.contact[0].value == "endpointmanager@example.org"
    assert inst.header[0] == "bearer-code BASGS534s4"
    assert inst.id == "example"
    assert inst.identifier[0].system == "http://example.org/enpoint-identifier"
    assert inst.identifier[0].value == "epcp12"
    assert inst.managingOrganization.reference == "Organization/hl7"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name == "Health Intersections CarePlan Hub"
    assert inst.payloadMimeType[0] == "application/fhir+xml"
    assert inst.payloadType[0].coding[0].code == "CarePlan"
    assert inst.payloadType[0].coding[0].system == "http://hl7.org/fhir/resource-types"
    assert inst.period.start == fhirtypes.DateTime.validate("2014-09-01")
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_endpoint_4(base_settings):
    """No. 4 tests collection for Endpoint.
    Test File: endpoint-example.json
    """
    filename = base_settings["unittest_data_dir"] / "endpoint-example.json"
    inst = endpoint.Endpoint.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Endpoint" == inst.resource_type

    impl_endpoint_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Endpoint" == data["resourceType"]

    inst2 = endpoint.Endpoint(**data)
    impl_endpoint_4(inst2)
