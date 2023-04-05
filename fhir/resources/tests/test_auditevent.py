# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AuditEvent
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import auditevent


def impl_auditevent_1(inst):
    assert inst.action == "E"
    assert inst.agent[0].requestor is True
    assert inst.agent[0].type.coding[0].code == "humanuser"
    assert inst.agent[0].type.coding[0].display == "human user"
    assert inst.agent[0].type.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/extra-security-role-" "type"
    )
    assert inst.agent[0].who.display == "Grahame Grieve"
    assert inst.agent[0].who.identifier.value == "95"
    assert inst.agent[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/auditevent-" "AlternativeUserID"
    )
    assert inst.agent[1].extension[0].valueIdentifier.type.text == "process ID"
    assert inst.agent[1].extension[0].valueIdentifier.value == "6580"
    assert inst.agent[1].networkString == "Workstation1.ehr.familyclinic.com"
    assert inst.agent[1].requestor is False
    assert inst.agent[1].type.coding[0].code == "110153"
    assert inst.agent[1].type.coding[0].display == "Source Role ID"
    assert (
        inst.agent[1].type.coding[0].system
        == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.agent[1].who.identifier.system == "urn:oid:2.16.840.1.113883.4.2"
    assert inst.agent[1].who.identifier.value == "2.16.840.1.113883.4.2"
    assert inst.category[0].coding[0].code == "rest"
    assert inst.category[0].coding[0].display == "Restful Operation"
    assert (
        inst.category[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/audit-event-type"
    )
    assert inst.code.coding[0].code == "search"
    assert inst.code.coding[0].display == "search"
    assert inst.code.coding[0].system == "http://hl7.org/fhir/restful-interaction"
    assert inst.entity[0].query == bytes_validator(
        (
            "aHR0cDovL2ZoaXItZGV2LmhlYWx0aGludGVyc2VjdGlvbnMuY29tLmF1L29w"
            "ZW4vRW5jb3VudGVyP3BhcnRpY2lwYW50PTEz"
        )
    )
    assert inst.entity[0].role.coding[0].code == "24"
    assert inst.entity[0].role.coding[0].display == "Query"
    assert (
        inst.entity[0].role.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/object-role"
    )
    assert inst.id == "example-search"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.outcome.code.code == "0"
    assert inst.outcome.code.display == "Success"
    assert (
        inst.outcome.code.system
        == "http://terminology.hl7.org/CodeSystem/audit-event-outcome"
    )
    assert inst.recorded == fhirtypes.Instant.validate("2015-08-22T23:42:24Z")
    assert inst.source.observer.display == "hl7connect.healthintersections.com.au"
    assert inst.source.type[0].coding[0].code == "3"
    assert inst.source.type[0].coding[0].display == "Web Server"
    assert (
        inst.source.type[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/security-source-type"
    )
    assert inst.text.status == "extensions"


def test_auditevent_1(base_settings):
    """No. 1 tests collection for AuditEvent.
    Test File: audit-event-example-search.json
    """
    filename = base_settings["unittest_data_dir"] / "audit-event-example-search.json"
    inst = auditevent.AuditEvent.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "AuditEvent" == inst.resource_type

    impl_auditevent_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "AuditEvent" == data["resourceType"]

    inst2 = auditevent.AuditEvent(**data)
    impl_auditevent_1(inst2)


def impl_auditevent_2(inst):
    assert inst.action == "E"
    assert inst.agent[0].networkString == "127.0.0.1"
    assert inst.agent[0].requestor is True
    assert inst.agent[0].type.coding[0].code == "humanuser"
    assert inst.agent[0].type.coding[0].display == "human user"
    assert inst.agent[0].type.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/extra-security-role-" "type"
    )
    assert inst.agent[0].who.display == "Grahame Grieve"
    assert inst.agent[0].who.identifier.value == "95"
    assert inst.agent[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/auditevent-" "AlternativeUserID"
    )
    assert inst.agent[1].extension[0].valueIdentifier.type.text == "process ID"
    assert inst.agent[1].extension[0].valueIdentifier.value == "6580"
    assert inst.agent[1].networkString == "Workstation1.ehr.familyclinic.com"
    assert inst.agent[1].requestor is False
    assert inst.agent[1].type.coding[0].code == "110153"
    assert inst.agent[1].type.coding[0].display == "Source Role ID"
    assert (
        inst.agent[1].type.coding[0].system
        == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.agent[1].who.identifier.system == "urn:oid:2.16.840.1.113883.4.2"
    assert inst.agent[1].who.identifier.value == "2.16.840.1.113883.4.2"
    assert inst.category[0].coding[0].code == "110114"
    assert inst.category[0].coding[0].display == "User Authentication"
    assert (
        inst.category[0].coding[0].system
        == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.code.coding[0].code == "110123"
    assert inst.code.coding[0].display == "Logout"
    assert inst.code.coding[0].system == "http://dicom.nema.org/resources/ontology/DCM"
    assert inst.id == "example-logout"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.outcome.code.code == "0"
    assert inst.outcome.code.display == "Success"
    assert (
        inst.outcome.code.system
        == "http://terminology.hl7.org/CodeSystem/audit-event-outcome"
    )
    assert inst.recorded == fhirtypes.Instant.validate("2013-06-20T23:46:41Z")
    assert inst.source.observer.display == "Cloud"
    assert (
        inst.source.observer.identifier.value == "hl7connect.healthintersections.com.au"
    )
    assert inst.source.type[0].coding[0].code == "3"
    assert inst.source.type[0].coding[0].display == "Web Server"
    assert (
        inst.source.type[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/security-source-type"
    )
    assert inst.text.status == "extensions"


def test_auditevent_2(base_settings):
    """No. 2 tests collection for AuditEvent.
    Test File: audit-event-example-logout.json
    """
    filename = base_settings["unittest_data_dir"] / "audit-event-example-logout.json"
    inst = auditevent.AuditEvent.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "AuditEvent" == inst.resource_type

    impl_auditevent_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "AuditEvent" == data["resourceType"]

    inst2 = auditevent.AuditEvent(**data)
    impl_auditevent_2(inst2)


def impl_auditevent_3(inst):
    assert inst.action == "R"
    assert inst.agent[0].requestor is True
    assert inst.agent[0].type.coding[0].code == "humanuser"
    assert inst.agent[0].type.coding[0].display == "human user"
    assert inst.agent[0].type.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/extra-security-role-" "type"
    )
    assert inst.agent[0].who.identifier.value == "95"
    assert inst.agent[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/auditevent-" "AlternativeUserID"
    )
    assert inst.agent[1].extension[0].valueIdentifier.type.text == "process ID"
    assert inst.agent[1].extension[0].valueIdentifier.value == "6580"
    assert inst.agent[1].networkString == "Workstation1.ehr.familyclinic.com"
    assert inst.agent[1].requestor is False
    assert inst.agent[1].type.coding[0].code == "110153"
    assert inst.agent[1].type.coding[0].display == "Source Role ID"
    assert (
        inst.agent[1].type.coding[0].system
        == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.agent[1].who.identifier.system == "urn:oid:2.16.840.1.113883.4.2"
    assert inst.agent[1].who.identifier.value == "2.16.840.1.113883.4.2"
    assert inst.category[0].coding[0].code == "rest"
    assert inst.category[0].coding[0].display == "Restful Operation"
    assert (
        inst.category[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/audit-event-type"
    )
    assert inst.code.coding[0].code == "vread"
    assert inst.code.coding[0].display == "vread"
    assert inst.code.coding[0].system == "http://hl7.org/fhir/restful-interaction"
    assert inst.entity[0].role.coding[0].code == "1"
    assert inst.entity[0].role.coding[0].display == "Patient"
    assert (
        inst.entity[0].role.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/object-role"
    )
    assert inst.entity[0].what.reference == "Patient/example/_history/1"
    assert inst.id == "example-rest"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.outcome.code.code == "0"
    assert inst.outcome.code.display == "Success"
    assert (
        inst.outcome.code.system
        == "http://terminology.hl7.org/CodeSystem/audit-event-outcome"
    )
    assert inst.recorded == fhirtypes.Instant.validate("2013-06-20T23:42:24Z")
    assert (
        inst.source.observer.identifier.value == "hl7connect.healthintersections.com.au"
    )
    assert inst.source.type[0].coding[0].code == "3"
    assert inst.source.type[0].coding[0].display == "Web Server"
    assert (
        inst.source.type[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/security-source-type"
    )
    assert inst.text.status == "extensions"


def test_auditevent_3(base_settings):
    """No. 3 tests collection for AuditEvent.
    Test File: audit-event-example-vread.json
    """
    filename = base_settings["unittest_data_dir"] / "audit-event-example-vread.json"
    inst = auditevent.AuditEvent.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "AuditEvent" == inst.resource_type

    impl_auditevent_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "AuditEvent" == data["resourceType"]

    inst2 = auditevent.AuditEvent(**data)
    impl_auditevent_3(inst2)


def impl_auditevent_4(inst):
    assert inst.action == "C"
    assert (
        inst.agent[0].networkUri == "urn:ipv6:2001:0db8:85a3:0000:0000:8a2e:0370:7334"
    )
    assert inst.agent[0].requestor is False
    assert inst.agent[0].type.coding[0].code == "110153"
    assert inst.agent[0].type.coding[0].display == "Source Role ID"
    assert (
        inst.agent[0].type.coding[0].system
        == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.agent[0].who.display == "myMachine.example.org"
    assert inst.agent[1].networkUri == "http://server.example.com/fhir"
    assert inst.agent[1].requestor is False
    assert inst.agent[1].type.coding[0].code == "110152"
    assert inst.agent[1].type.coding[0].display == "Destination Role ID"
    assert (
        inst.agent[1].type.coding[0].system
        == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.agent[1].who.reference == "Device/example"
    assert inst.agent[2].requestor is True
    assert inst.agent[2].type.coding[0].code == "INF"
    assert inst.agent[2].type.coding[0].display == "Informant"
    assert (
        inst.agent[2].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"
    )
    assert inst.agent[2].who.display == "Betty Jones"
    assert inst.authorization[0].coding[0].code == "TREAT"
    assert (
        inst.authorization[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.basedOn[0].reference == "CarePlan/example"
    assert inst.category[0].coding[0].code == "create"
    assert inst.category[0].coding[0].display == "create"
    assert (
        inst.category[0].coding[0].system == "http://hl7.org/fhir/restful-interaction"
    )
    assert inst.code.coding[0].code == "rest"
    assert inst.code.coding[0].display == "Restful Operation"
    assert (
        inst.code.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/audit-event-type"
    )
    assert inst.encounter.reference == "Encounter/home"
    assert inst.entity[0].role.coding[0].code == "4"
    assert inst.entity[0].role.coding[0].display == "Domain Resource"
    assert (
        inst.entity[0].role.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/object-role"
    )
    assert inst.entity[0].what.reference == "List/example"
    assert inst.id == "example-advanced-create"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.occurredDateTime == fhirtypes.DateTime.validate(
        "2020-04-29T09:49:00.000Z"
    )
    assert inst.outcome.code.code == "0"
    assert inst.outcome.code.display == "Success"
    assert (
        inst.outcome.code.system
        == "http://terminology.hl7.org/CodeSystem/audit-event-outcome"
    )
    assert inst.patient.reference == "Patient/example"
    assert inst.recorded == fhirtypes.Instant.validate("2020-04-29T09:49:00.000Z")
    assert inst.severity == "informational"
    assert inst.source.observer.reference == "Device/example"
    assert inst.source.site.identifier.value == "http://server.example.com"
    assert inst.source.type[0].coding[0].code == "4"
    assert inst.source.type[0].coding[0].display == "Application Server"
    assert (
        inst.source.type[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/security-source-type"
    )
    assert inst.text.status == "generated"


def test_auditevent_4(base_settings):
    """No. 4 tests collection for AuditEvent.
    Test File: auditevent-example-advanced-create.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "auditevent-example-advanced-create.json"
    )
    inst = auditevent.AuditEvent.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "AuditEvent" == inst.resource_type

    impl_auditevent_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "AuditEvent" == data["resourceType"]

    inst2 = auditevent.AuditEvent(**data)
    impl_auditevent_4(inst2)


def impl_auditevent_5(inst):
    assert inst.action == "R"
    assert inst.agent[0].requestor is False
    assert inst.agent[0].type.coding[0].code == "110153"
    assert inst.agent[0].type.coding[0].display == "Source Role ID"
    assert (
        inst.agent[0].type.coding[0].system
        == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.agent[0].who.display == "ExportToMedia.app"
    assert inst.agent[1].requestor is True
    assert inst.agent[1].type.coding[0].code == "humanuser"
    assert inst.agent[1].type.coding[0].display == "human user"
    assert inst.agent[1].type.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/extra-security-role-" "type"
    )
    assert inst.agent[1].who.display == "Grahame Grieve"
    assert inst.agent[1].who.identifier.value == "95"
    assert inst.agent[2].requestor is False
    assert inst.agent[2].type.coding[0].code == "110154"
    assert inst.agent[2].type.coding[0].display == "Destination Media"
    assert (
        inst.agent[2].type.coding[0].system
        == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.agent[2].who.display == "Media title: Hello World"
    assert inst.category[0].coding[0].code == "110106"
    assert inst.category[0].coding[0].display == "Export"
    assert (
        inst.category[0].coding[0].system
        == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.code.coding[0].code == "ITI-32"
    assert inst.code.coding[0].display == "Distribute Document Set on Media"
    assert inst.code.coding[0].system == "urn:ihe:event-type-code"
    assert inst.entity[0].role.coding[0].code == "1"
    assert inst.entity[0].role.coding[0].display == "Patient"
    assert (
        inst.entity[0].role.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/object-role"
    )
    assert (
        inst.entity[0].what.identifier.value
        == "e3cdfc81a0d24bd^^^&2.16.840.1.113883.4.2&ISO"
    )
    assert inst.entity[1].role.coding[0].code == "20"
    assert inst.entity[1].role.coding[0].display == "Job"
    assert (
        inst.entity[1].role.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/object-role"
    )
    assert inst.entity[1].what.identifier.type.coding[0].code == "IHE XDS Metadata"
    assert (
        inst.entity[1].what.identifier.type.coding[0].display
        == "submission set classificationNode"
    )
    assert (
        inst.entity[1].what.identifier.type.coding[0].system
        == "urn:uuid:a54d6aa5-d40d-43f9-88c5-b4633d873bdd"
    )
    assert (
        inst.entity[1].what.identifier.value
        == "e3cdfc81a0d24bd^^^&2.16.840.1.113883.4.2&ISO"
    )
    assert inst.entity[2].what.reference == "DocumentReference/example"
    assert inst.id == "example-media"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.outcome.code.code == "0"
    assert inst.outcome.code.display == "Success"
    assert (
        inst.outcome.code.system
        == "http://terminology.hl7.org/CodeSystem/audit-event-outcome"
    )
    assert inst.recorded == fhirtypes.Instant.validate("2015-08-27T23:42:24Z")
    assert inst.source.observer.display == "Cloud"
    assert (
        inst.source.observer.identifier.value == "hl7connect.healthintersections.com.au"
    )
    assert inst.text.status == "generated"


def test_auditevent_5(base_settings):
    """No. 5 tests collection for AuditEvent.
    Test File: audit-event-example-media.json
    """
    filename = base_settings["unittest_data_dir"] / "audit-event-example-media.json"
    inst = auditevent.AuditEvent.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "AuditEvent" == inst.resource_type

    impl_auditevent_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "AuditEvent" == data["resourceType"]

    inst2 = auditevent.AuditEvent(**data)
    impl_auditevent_5(inst2)


def impl_auditevent_6(inst):
    assert inst.action == "C"
    assert inst.agent[0].requestor is True
    assert inst.agent[0].type.coding[0].code == "humanuser"
    assert inst.agent[0].type.coding[0].display == "human user"
    assert inst.agent[0].type.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/extra-security-role-" "type"
    )
    assert inst.agent[0].who.identifier.value == "95"
    assert inst.agent[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/auditevent-" "AlternativeUserID"
    )
    assert inst.agent[1].extension[0].valueIdentifier.type.text == "process ID"
    assert inst.agent[1].extension[0].valueIdentifier.value == "6580"
    assert inst.agent[1].networkString == "Workstation1.ehr.familyclinic.com"
    assert inst.agent[1].requestor is False
    assert inst.agent[1].type.coding[0].code == "110153"
    assert inst.agent[1].type.coding[0].display == "Source Role ID"
    assert (
        inst.agent[1].type.coding[0].system
        == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.agent[1].who.identifier.system == "urn:oid:2.16.840.1.113883.4.2"
    assert inst.agent[1].who.identifier.value == "2.16.840.1.113883.4.2"
    assert inst.category[0].coding[0].code == "rest"
    assert inst.category[0].coding[0].display == "Restful Operation"
    assert (
        inst.category[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/audit-event-type"
    )
    assert inst.code.coding[0].code == "create"
    assert inst.code.coding[0].display == "create"
    assert inst.code.coding[0].system == "http://hl7.org/fhir/restful-interaction"
    assert inst.entity[0].role.coding[0].code == "1"
    assert inst.entity[0].role.coding[0].display == "Patient"
    assert (
        inst.entity[0].role.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/object-role"
    )
    assert inst.entity[0].what.reference == "Patient/example/_history/1"
    assert inst.entity[1].role.coding[0].code == "21"
    assert inst.entity[1].role.coding[0].display == "Job Stream"
    assert (
        inst.entity[1].role.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/object-role"
    )
    assert inst.entity[1].what.identifier.system == "http://example.com/server"
    assert inst.entity[1].what.identifier.type.text == "TraceID"
    assert inst.entity[1].what.identifier.value == "6b507ee2d716780372c255df69ece653"
    assert inst.id == "example-rest-create-traceID"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.outcome.code.code == "0"
    assert inst.outcome.code.display == "Success"
    assert (
        inst.outcome.code.system
        == "http://terminology.hl7.org/CodeSystem/audit-event-outcome"
    )
    assert inst.recorded == fhirtypes.Instant.validate("2019-12-04T11:59:28.646+00:00")
    assert (
        inst.source.observer.identifier.value == "hl7connect.healthintersections.com.au"
    )
    assert inst.source.type[0].coding[0].code == "3"
    assert inst.source.type[0].coding[0].display == "Web Server"
    assert (
        inst.source.type[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/security-source-type"
    )
    assert inst.text.status == "extensions"


def test_auditevent_6(base_settings):
    """No. 6 tests collection for AuditEvent.
    Test File: audit-event-example-create-traceID.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "audit-event-example-create-traceID.json"
    )
    inst = auditevent.AuditEvent.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "AuditEvent" == inst.resource_type

    impl_auditevent_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "AuditEvent" == data["resourceType"]

    inst2 = auditevent.AuditEvent(**data)
    impl_auditevent_6(inst2)


def impl_auditevent_7(inst):
    assert inst.action == "E"
    assert inst.agent[0].requestor is True
    assert inst.agent[0].type.coding[0].code == "humanuser"
    assert inst.agent[0].type.coding[0].display == "human user"
    assert inst.agent[0].type.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/extra-security-role-" "type"
    )
    assert inst.agent[0].who.display == "Grahame Grieve"
    assert inst.agent[0].who.identifier.value == "95"
    assert inst.agent[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/auditevent-" "AlternativeUserID"
    )
    assert inst.agent[1].extension[0].valueIdentifier.type.text == "process ID"
    assert inst.agent[1].extension[0].valueIdentifier.value == "6580"
    assert inst.agent[1].networkString == "Workstation1.ehr.familyclinic.com"
    assert inst.agent[1].requestor is False
    assert inst.agent[1].type.coding[0].code == "110153"
    assert inst.agent[1].type.coding[0].display == "Source Role ID"
    assert (
        inst.agent[1].type.coding[0].system
        == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.agent[1].who.identifier.system == "urn:oid:2.16.840.1.113883.4.2"
    assert inst.agent[1].who.identifier.value == "2.16.840.1.113883.4.2"
    assert inst.category[0].coding[0].code == "110114"
    assert inst.category[0].coding[0].display == "User Authentication"
    assert (
        inst.category[0].coding[0].system
        == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.code.coding[0].code == "110122"
    assert inst.code.coding[0].display == "Login"
    assert inst.code.coding[0].system == "http://dicom.nema.org/resources/ontology/DCM"
    assert inst.id == "example-login"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.outcome.code.code == "0"
    assert inst.outcome.code.display == "Success"
    assert (
        inst.outcome.code.system
        == "http://terminology.hl7.org/CodeSystem/audit-event-outcome"
    )
    assert inst.recorded == fhirtypes.Instant.validate("2013-06-20T23:41:23Z")
    assert inst.source.observer.display == "Cloud"
    assert (
        inst.source.observer.identifier.value == "hl7connect.healthintersections.com.au"
    )
    assert inst.source.type[0].coding[0].code == "3"
    assert inst.source.type[0].coding[0].display == "Web Server"
    assert (
        inst.source.type[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/security-source-type"
    )
    assert inst.text.status == "extensions"


def test_auditevent_7(base_settings):
    """No. 7 tests collection for AuditEvent.
    Test File: audit-event-example-login.json
    """
    filename = base_settings["unittest_data_dir"] / "audit-event-example-login.json"
    inst = auditevent.AuditEvent.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "AuditEvent" == inst.resource_type

    impl_auditevent_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "AuditEvent" == data["resourceType"]

    inst2 = auditevent.AuditEvent(**data)
    impl_auditevent_7(inst2)


def impl_auditevent_8(inst):
    assert inst.action == "E"
    assert inst.agent[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/auditevent-" "AlternativeUserID"
    )
    assert inst.agent[0].extension[0].valueIdentifier.type.text == "process ID"
    assert inst.agent[0].extension[0].valueIdentifier.value == "6580"
    assert inst.agent[0].networkString == "Workstation1.ehr.familyclinic.com"
    assert inst.agent[0].requestor is False
    assert inst.agent[0].type.coding[0].code == "110153"
    assert inst.agent[0].type.coding[0].display == "Source Role ID"
    assert (
        inst.agent[0].type.coding[0].system
        == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.agent[0].who.identifier.system == "urn:oid:2.16.840.1.113883.4.2"
    assert inst.agent[0].who.identifier.value == "2.16.840.1.113883.4.2"
    assert inst.agent[1].requestor is True
    assert inst.agent[1].type.coding[0].code == "humanuser"
    assert inst.agent[1].type.coding[0].display == "human user"
    assert inst.agent[1].type.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/extra-security-role-" "type"
    )
    assert inst.agent[1].who.display == "Grahame Grieve"
    assert inst.agent[1].who.identifier.value == "95"
    assert inst.category[0].coding[0].code == "110112"
    assert inst.category[0].coding[0].display == "Query"
    assert (
        inst.category[0].coding[0].system
        == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.code.coding[0].code == "ITI-9"
    assert inst.code.coding[0].display == "PIX Query"
    assert inst.code.coding[0].system == "urn:oid:1.3.6.1.4.1.19376.1.2"
    assert inst.entity[0].role.coding[0].code == "1"
    assert inst.entity[0].role.coding[0].display == "Patient"
    assert (
        inst.entity[0].role.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/object-role"
    )
    assert (
        inst.entity[0].what.identifier.value
        == "e3cdfc81a0d24bd^^^&2.16.840.1.113883.4.2&ISO"
    )
    assert inst.entity[1].detail[0].type.coding[0].code == "MSH-10"
    assert inst.entity[1].detail[0].valueBase64Binary == bytes_validator(
        "MS4yLjg0MC4xMTQzNTAuMS4xMy4wLjEuNy4xLjE="
    )
    assert inst.entity[1].role.coding[0].code == "24"
    assert inst.entity[1].role.coding[0].display == "Query"
    assert (
        inst.entity[1].role.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/object-role"
    )
    assert inst.id == "example-pixQuery"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.outcome.code.code == "0"
    assert inst.outcome.code.display == "Success"
    assert (
        inst.outcome.code.system
        == "http://terminology.hl7.org/CodeSystem/audit-event-outcome"
    )
    assert inst.recorded == fhirtypes.Instant.validate("2015-08-26T23:42:24Z")
    assert inst.source.observer.display == "hl7connect.healthintersections.com.au"
    assert inst.text.status == "extensions"


def test_auditevent_8(base_settings):
    """No. 8 tests collection for AuditEvent.
    Test File: audit-event-example-pixQuery.json
    """
    filename = base_settings["unittest_data_dir"] / "audit-event-example-pixQuery.json"
    inst = auditevent.AuditEvent.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "AuditEvent" == inst.resource_type

    impl_auditevent_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "AuditEvent" == data["resourceType"]

    inst2 = auditevent.AuditEvent(**data)
    impl_auditevent_8(inst2)


def impl_auditevent_9(inst):
    assert inst.action == "E"
    assert inst.agent[0].requestor is False
    assert inst.agent[0].role[0].text == "Service User (Logon)"
    assert inst.agent[0].who.identifier.value == "Grahame"
    assert inst.agent[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/auditevent-" "AlternativeUserID"
    )
    assert inst.agent[1].extension[0].valueIdentifier.type.text == "process ID"
    assert inst.agent[1].extension[0].valueIdentifier.value == "6580"
    assert inst.agent[1].networkString == "Workstation1.ehr.familyclinic.com"
    assert inst.agent[1].requestor is False
    assert inst.agent[1].who.identifier.system == "urn:oid:2.16.840.1.113883.4.2"
    assert inst.agent[1].who.identifier.value == "2.16.840.1.113883.4.2"
    assert inst.category[0].coding[0].code == "110100"
    assert inst.category[0].coding[0].display == "Application Activity"
    assert (
        inst.category[0].coding[0].system
        == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.code.coding[0].code == "110120"
    assert inst.code.coding[0].display == "Application Start"
    assert inst.code.coding[0].system == "http://dicom.nema.org/resources/ontology/DCM"
    assert inst.entity[0].role.coding[0].code == "4"
    assert inst.entity[0].role.coding[0].display == "Domain Resource"
    assert (
        inst.entity[0].role.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/object-role"
    )
    assert inst.entity[0].what.identifier.type.coding[0].code == "SNO"
    assert (
        inst.entity[0].what.identifier.type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0203"
    )
    assert inst.entity[0].what.identifier.type.text == "Dell Serial Number"
    assert inst.entity[0].what.identifier.value == "ABCDEF"
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.outcome.code.code == "0"
    assert inst.outcome.code.display == "Success"
    assert (
        inst.outcome.code.system
        == "http://terminology.hl7.org/CodeSystem/audit-event-outcome"
    )
    assert inst.recorded == fhirtypes.Instant.validate("2012-10-25T22:04:27+11:00")
    assert inst.source.observer.display == "Grahame's Laptop"
    assert inst.source.type[0].coding[0].code == "110122"
    assert inst.source.type[0].coding[0].display == "Login"
    assert (
        inst.source.type[0].coding[0].system
        == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Application '
        "Start for under service login &quot;Grahame&quot; (id: "
        "Grahame's Test HL7Connect)</div>"
    )
    assert inst.text.status == "generated"


def test_auditevent_9(base_settings):
    """No. 9 tests collection for AuditEvent.
    Test File: auditevent-example.json
    """
    filename = base_settings["unittest_data_dir"] / "auditevent-example.json"
    inst = auditevent.AuditEvent.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "AuditEvent" == inst.resource_type

    impl_auditevent_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "AuditEvent" == data["resourceType"]

    inst2 = auditevent.AuditEvent(**data)
    impl_auditevent_9(inst2)


def impl_auditevent_10(inst):
    assert inst.action == "E"
    assert inst.agent[0].authorization[0].coding[0].code == "TREAT"
    assert (
        inst.agent[0].authorization[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.agent[0].requestor is True
    assert inst.agent[0].type.coding[0].code == "110152"
    assert inst.agent[0].type.coding[0].display == "Destination Role ID"
    assert (
        inst.agent[0].type.coding[0].system
        == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert (
        inst.agent[0].who.identifier.system
        == "https://github.com/synthetichealth/synthea"
    )
    assert inst.agent[0].who.identifier.value == "Org1"
    assert inst.code.coding[0].code == "110112"
    assert inst.code.coding[0].display == "Query"
    assert inst.code.coding[0].system == "http://dicom.nema.org/resources/ontology/DCM"
    assert inst.entity[0].role.coding[0].code == "4"
    assert inst.entity[0].role.coding[0].display == "Domain Resource"
    assert (
        inst.entity[0].role.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/object-role"
    )
    assert inst.entity[0].what.reference == "Consent/consent-example-basic"
    assert inst.id == "example-consent-permit-authz"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.outcome.code.code == "0"
    assert inst.outcome.code.display == "Success"
    assert (
        inst.outcome.code.system
        == "http://terminology.hl7.org/CodeSystem/audit-event-outcome"
    )
    assert inst.outcome.detail[0].text == "CONSENT_PERMIT"
    assert inst.patient.reference == "Patient/example"
    assert inst.recorded == fhirtypes.Instant.validate("2021-09-08T21:51:59.932Z")
    assert inst.source.observer.display == "LEAP Consent Decision Service"
    assert inst.source.type[0].coding[0].code == "4"
    assert inst.source.type[0].coding[0].display == "Application Server"
    assert (
        inst.source.type[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/security-source-type"
    )
    assert inst.text.status == "generated"


def test_auditevent_10(base_settings):
    """No. 10 tests collection for AuditEvent.
    Test File: auditevent-example-consent-authz.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "auditevent-example-consent-authz.json"
    )
    inst = auditevent.AuditEvent.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "AuditEvent" == inst.resource_type

    impl_auditevent_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "AuditEvent" == data["resourceType"]

    inst2 = auditevent.AuditEvent(**data)
    impl_auditevent_10(inst2)
