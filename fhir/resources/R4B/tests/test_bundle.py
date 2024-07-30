# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Bundle
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import bundle
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_bundle_1(inst):
    assert (
        inst.entry[0].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:uuid:d195d9b8-6f78-4d71-9d22-3c1a923bfea5"}
        ).valueUri
    )
    assert inst.entry[0].request.method == "GET"
    assert (
        inst.entry[0].request.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "Subscription/123/$status"}
        ).valueUri
    )
    assert inst.entry[0].resource.id == "d195d9b8-6f78-4d71-9d22-3c1a923bfea5"
    assert inst.entry[0].response.status == "200"
    assert (
        inst.entry[1].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://example.org/FHIR/R4/Encounter/2"}
        ).valueUri
    )
    assert inst.entry[1].request.method == "PUT"
    assert (
        inst.entry[1].request.url
        == ExternalValidatorModel.model_validate({"valueUri": "Encounter/2"}).valueUri
    )
    assert inst.entry[1].resource.id == "2"
    assert (
        inst.entry[1].resource.meta.lastUpdated
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2019-08-07T10:49:22Z"}
        ).valueInstant
    )
    assert inst.entry[1].resource.meta.versionId == "1"
    assert inst.entry[1].response.status == "201"
    assert inst.id == "00b99077-2bda-436e-98cc-a4f65d6c2fe0"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert (
        inst.timestamp
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2020-04-17T10:24:13.1882432-05:00"}
        ).valueInstant
    )
    assert inst.type == "history"


def test_bundle_1(base_settings):
    """No. 1 tests collection for Bundle.
    Test File: notification-full-resource.json
    """
    filename = base_settings["unittest_data_dir"] / "notification-full-resource.json"
    inst = bundle.Bundle.model_validate_json(filename.read_bytes())
    assert "Bundle" == inst.get_resource_type()

    impl_bundle_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_1(inst2)


def impl_bundle_2(inst):
    assert (
        inst.entry[0].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:uuid:2866af9c-137d-4458-a8a9-eeeec0ce5583"}
        ).valueUri
    )
    assert inst.entry[0].resource.id == "warning"
    assert inst.entry[0].search.mode == "outcome"
    assert inst.id == "bundle-search-warning"
    assert inst.link[0].relation == "self"
    assert (
        inst.link[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "https://example.org/fhir/Observation?patient.identifier=http://example.com/fhir/identifier/mrn|123456"
            }
        ).valueUri
    )
    assert (
        inst.meta.lastUpdated
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2017-03-14T08:23:30+11:00"}
        ).valueInstant
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.total == 0
    assert inst.type == "searchset"


def test_bundle_2(base_settings):
    """No. 2 tests collection for Bundle.
    Test File: bundle-search-warning.json
    """
    filename = base_settings["unittest_data_dir"] / "bundle-search-warning.json"
    inst = bundle.Bundle.model_validate_json(filename.read_bytes())
    assert "Bundle" == inst.get_resource_type()

    impl_bundle_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_2(inst2)


def impl_bundle_3(inst):
    assert (
        inst.entry[0].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:uuid:dd431176-7bcf-455e-8a0c-50cb15d6263f"}
        ).valueUri
    )
    assert inst.entry[0].request.method == "GET"
    assert (
        inst.entry[0].request.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "Subscription/123/$events"}
        ).valueUri
    )
    assert inst.entry[0].resource.id == "dd431176-7bcf-455e-8a0c-50cb15d6263f"
    assert inst.entry[0].response.status == "200"
    assert (
        inst.entry[1].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://example.org/FHIR/R4B/Encounter/1"}
        ).valueUri
    )
    assert inst.entry[1].request.method == "PUT"
    assert (
        inst.entry[1].request.url
        == ExternalValidatorModel.model_validate({"valueUri": "Encounter/1"}).valueUri
    )
    assert inst.entry[1].response.status == "201"
    assert (
        inst.entry[2].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://example.org/FHIR/R4B/Encounter/2"}
        ).valueUri
    )
    assert inst.entry[2].request.method == "PUT"
    assert (
        inst.entry[2].request.url
        == ExternalValidatorModel.model_validate({"valueUri": "Encounter/2"}).valueUri
    )
    assert inst.entry[2].response.status == "201"
    assert inst.id == "155141d4-7601-46f7-a82b-b8443bcf9883"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert (
        inst.timestamp
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2020-04-17T10:24:13.1882432-05:00"}
        ).valueInstant
    )
    assert inst.type == "history"


def test_bundle_3(base_settings):
    """No. 3 tests collection for Bundle.
    Test File: notification-id-only-query.json
    """
    filename = base_settings["unittest_data_dir"] / "notification-id-only-query.json"
    inst = bundle.Bundle.model_validate_json(filename.read_bytes())
    assert "Bundle" == inst.get_resource_type()

    impl_bundle_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_3(inst2)


def impl_bundle_4(inst):
    assert (
        inst.entry[0].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://example.com/base/DiagnosticReport/f202"}
        ).valueUri
    )
    assert inst.entry[0].resource.id == "f202"
    assert (
        inst.entry[1].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://example.com/base/ServiceRequest/req"}
        ).valueUri
    )
    assert inst.entry[1].resource.id == "req"
    assert inst.id == "f202"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.type == "collection"


def test_bundle_4(base_settings):
    """No. 4 tests collection for Bundle.
    Test File: diagnosticreport-example-f202-bloodculture.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "diagnosticreport-example-f202-bloodculture.json"
    )
    inst = bundle.Bundle.model_validate_json(filename.read_bytes())
    assert "Bundle" == inst.get_resource_type()

    impl_bundle_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_4(inst2)


def impl_bundle_5(inst):
    assert (
        inst.entry[0].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:uuid:a5b053d4-2603-446f-ae86-f5853ac09334"}
        ).valueUri
    )
    assert inst.entry[0].request.method == "GET"
    assert (
        inst.entry[0].request.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "Subscription/123/$status"}
        ).valueUri
    )
    assert inst.entry[0].resource.id == "a5b053d4-2603-446f-ae86-f5853ac09334"
    assert inst.entry[0].response.status == "200"
    assert inst.id == "3d20ea4b-90dc-4d0d-b15a-c7a893389401"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert (
        inst.timestamp
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2020-04-17T10:24:13.1882432-05:00"}
        ).valueInstant
    )
    assert inst.type == "history"


def test_bundle_5(base_settings):
    """No. 5 tests collection for Bundle.
    Test File: notification-heartbeat.json
    """
    filename = base_settings["unittest_data_dir"] / "notification-heartbeat.json"
    inst = bundle.Bundle.model_validate_json(filename.read_bytes())
    assert "Bundle" == inst.get_resource_type()

    impl_bundle_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_5(inst2)


def impl_bundle_6(inst):
    assert (
        inst.entry[0].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:uuid:d9d296d8-5afd-42e1-a0ce-3344e0e003ed"}
        ).valueUri
    )
    assert inst.entry[0].resource.id == "caf609cf-c3a7-4be3-a3aa-356b9bb69d4f"
    assert (
        inst.entry[1].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:uuid:03f9aa7d-b395-47b9-84e0-053678b6e4e3"}
        ).valueUri
    )
    assert inst.entry[1].resource.id == "03f9aa7d-b395-47b9-84e0-053678b6e4e3"
    assert (
        inst.entry[2].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://acme.com/ehr/fhir/Patient/pat1"}
        ).valueUri
    )
    assert inst.entry[2].resource.id == "pat1"
    assert (
        inst.entry[3].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://acme.com/ehr/fhir/Patient/pat12"}
        ).valueUri
    )
    assert inst.entry[3].resource.id == "pat2"
    assert inst.id == "3a0707d3-549e-4467-b8b8-5a2ab3800efe"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert (
        inst.timestamp
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2015-07-14T11:15:33+10:00"}
        ).valueInstant
    )
    assert inst.type == "message"


def test_bundle_6(base_settings):
    """No. 6 tests collection for Bundle.
    Test File: message-response-link.json
    """
    filename = base_settings["unittest_data_dir"] / "message-response-link.json"
    inst = bundle.Bundle.model_validate_json(filename.read_bytes())
    assert "Bundle" == inst.get_resource_type()

    impl_bundle_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_6(inst2)


def impl_bundle_7(inst):
    assert (
        inst.entry[0].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:uuid:3fdc72f4-a11d-4a9d-9260-a9f745779e1d"}
        ).valueUri
    )
    assert inst.entry[0].request.method == "POST"
    assert (
        inst.entry[0].request.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "DocumentReference"}
        ).valueUri
    )
    assert (
        inst.entry[0].resource.meta.lastUpdated
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2013-07-01T13:11:33Z"}
        ).valueInstant
    )
    assert (
        inst.entry[1].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://localhost:9556/svc/fhir/Patient/a2"}
        ).valueUri
    )
    assert (
        inst.entry[1].request.ifNoneExist
        == "Patient?identifier=http://acme.org/xds/patients!89765a87b"
    )
    assert inst.entry[1].request.method == "POST"
    assert (
        inst.entry[1].request.url
        == ExternalValidatorModel.model_validate({"valueUri": "Patient"}).valueUri
    )
    assert inst.entry[1].resource.id == "a2"
    assert (
        inst.entry[1].resource.meta.lastUpdated
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2013-07-01T13:11:33Z"}
        ).valueInstant
    )
    assert (
        inst.entry[2].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://localhost:9556/svc/fhir/Practitioner/a3"}
        ).valueUri
    )
    assert inst.entry[2].request.method == "POST"
    assert (
        inst.entry[2].request.url
        == ExternalValidatorModel.model_validate({"valueUri": "Practitioner"}).valueUri
    )
    assert inst.entry[2].resource.id == "a3"
    assert (
        inst.entry[2].resource.meta.lastUpdated
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2013-07-01T13:11:33Z"}
        ).valueInstant
    )
    assert (
        inst.entry[3].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://localhost:9556/svc/fhir/Practitioner/a4"}
        ).valueUri
    )
    assert inst.entry[3].request.method == "POST"
    assert (
        inst.entry[3].request.url
        == ExternalValidatorModel.model_validate({"valueUri": "Practitioner"}).valueUri
    )
    assert inst.entry[3].resource.id == "a4"
    assert (
        inst.entry[3].resource.meta.lastUpdated
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2013-07-01T13:11:33Z"}
        ).valueInstant
    )
    assert (
        inst.entry[4].fullUrl
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://localhost:9556/svc/fhir/Binary/1e404af3-077f-4bee-b7a6-a9be97e1ce32"
            }
        ).valueUri
    )
    assert inst.entry[4].request.method == "POST"
    assert (
        inst.entry[4].request.url
        == ExternalValidatorModel.model_validate({"valueUri": "Binary"}).valueUri
    )
    assert inst.entry[4].resource.id == "1e404af3-077f-4bee-b7a6-a9be97e1ce32"
    assert (
        inst.entry[4].resource.meta.lastUpdated
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2013-07-01T13:11:33Z"}
        ).valueInstant
    )
    assert inst.id == "xds"
    assert (
        inst.meta.lastUpdated
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2013-07-01T13:11:33Z"}
        ).valueInstant
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.type == "transaction"


def test_bundle_7(base_settings):
    """No. 7 tests collection for Bundle.
    Test File: xds-example.json
    """
    filename = base_settings["unittest_data_dir"] / "xds-example.json"
    inst = bundle.Bundle.model_validate_json(filename.read_bytes())
    assert "Bundle" == inst.get_resource_type()

    impl_bundle_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_7(inst2)


def impl_bundle_8(inst):
    assert (
        inst.entry[0].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/DomainResource-text"}
        ).valueUri
    )
    assert inst.entry[0].resource.id == "DomainResource-text"
    assert (
        inst.entry[1].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Resource-content"}
        ).valueUri
    )
    assert inst.entry[1].resource.id == "Resource-content"
    assert (
        inst.entry[2].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Resource-filter"}
        ).valueUri
    )
    assert inst.entry[2].resource.id == "Resource-filter"
    assert (
        inst.entry[3].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Resource-has"}
        ).valueUri
    )
    assert inst.entry[3].resource.id == "Resource-has"
    assert (
        inst.entry[4].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Resource-id"}
        ).valueUri
    )
    assert inst.entry[4].resource.id == "Resource-id"
    assert (
        inst.entry[5].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Resource-lastUpdated"}
        ).valueUri
    )
    assert inst.entry[5].resource.id == "Resource-lastUpdated"
    assert (
        inst.entry[6].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Resource-list"}
        ).valueUri
    )
    assert inst.entry[6].resource.id == "Resource-list"
    assert (
        inst.entry[7].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Resource-profile"}
        ).valueUri
    )
    assert inst.entry[7].resource.id == "Resource-profile"
    assert (
        inst.entry[8].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Resource-query"}
        ).valueUri
    )
    assert inst.entry[8].resource.id == "Resource-query"
    assert (
        inst.entry[9].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Resource-security"}
        ).valueUri
    )
    assert inst.entry[9].resource.id == "Resource-security"
    assert inst.id == "searchParams"
    assert (
        inst.meta.lastUpdated
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2022-05-28T12:47:40.239+10:00"}
        ).valueInstant
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.type == "collection"


def test_bundle_8(base_settings):
    """No. 8 tests collection for Bundle.
    Test File: search-parameters.json
    """
    filename = base_settings["unittest_data_dir"] / "search-parameters.json"
    inst = bundle.Bundle.model_validate_json(filename.read_bytes())
    assert "Bundle" == inst.get_resource_type()

    impl_bundle_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_8(inst2)


def impl_bundle_9(inst):
    assert (
        inst.entry[0].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:uuid:267b18ce-3d37-4581-9baa-6fada338038b"}
        ).valueUri
    )
    assert inst.entry[0].resource.id == "267b18ce-3d37-4581-9baa-6fada338038b"
    assert (
        inst.entry[1].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://acme.com/ehr/fhir/Patient/pat1"}
        ).valueUri
    )
    assert inst.entry[1].resource.id == "pat1"
    assert (
        inst.entry[2].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://acme.com/ehr/fhir/Patient/pat12"}
        ).valueUri
    )
    assert inst.entry[2].resource.id == "pat2"
    assert inst.id == "10bb101f-a121-4264-a920-67be9cb82c74"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert (
        inst.timestamp
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2015-07-14T11:15:33+10:00"}
        ).valueInstant
    )
    assert inst.type == "message"


def test_bundle_9(base_settings):
    """No. 9 tests collection for Bundle.
    Test File: message-request-link.json
    """
    filename = base_settings["unittest_data_dir"] / "message-request-link.json"
    inst = bundle.Bundle.model_validate_json(filename.read_bytes())
    assert "Bundle" == inst.get_resource_type()

    impl_bundle_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_9(inst2)


def impl_bundle_10(inst):
    assert (
        inst.entry[0].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/tx-sct"}
        ).valueUri
    )
    assert inst.entry[0].resource.id == "tx-sct"
    assert (
        inst.entry[1].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/tx-rxnorm"}
        ).valueUri
    )
    assert inst.entry[1].resource.id == "tx-rxnorm"
    assert (
        inst.entry[2].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/tx-loinc"}
        ).valueUri
    )
    assert inst.entry[2].resource.id == "tx-loinc"
    assert (
        inst.entry[3].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/tx-ucum"}
        ).valueUri
    )
    assert inst.entry[3].resource.id == "tx-ucum"
    assert (
        inst.entry[4].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/tx-nci"}
        ).valueUri
    )
    assert inst.entry[4].resource.id == "tx-nci"
    assert (
        inst.entry[5].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/tx-cpt"}
        ).valueUri
    )
    assert inst.entry[5].resource.id == "tx-cpt"
    assert (
        inst.entry[6].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/tx-ndf-rt"}
        ).valueUri
    )
    assert inst.entry[6].resource.id == "tx-ndf-rt"
    assert (
        inst.entry[7].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/tx-unii"}
        ).valueUri
    )
    assert inst.entry[7].resource.id == "tx-unii"
    assert (
        inst.entry[8].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/tx-ndc"}
        ).valueUri
    )
    assert inst.entry[8].resource.id == "tx-ndc"
    assert (
        inst.entry[9].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/tx-cvx"}
        ).valueUri
    )
    assert inst.entry[9].resource.id == "tx-cvx"
    assert inst.id == "terminologies"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.type == "collection"


def test_bundle_10(base_settings):
    """No. 10 tests collection for Bundle.
    Test File: namingsystem-terminologies.json
    """
    filename = base_settings["unittest_data_dir"] / "namingsystem-terminologies.json"
    inst = bundle.Bundle.model_validate_json(filename.read_bytes())
    assert "Bundle" == inst.get_resource_type()

    impl_bundle_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_10(inst2)
