# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AuditEvent
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import auditevent


def impl_auditevent_1(inst):
    assert inst.action == "E"
    assert inst.agent[0].altId == "601847123"
    assert inst.agent[0].name == "Grahame Grieve"
    assert inst.agent[0].requestor is True
    assert inst.agent[0].type.coding[0].code == "humanuser"
    assert inst.agent[0].type.coding[0].display == "human user"
    assert inst.agent[0].type.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/extra-security-role-" "type"
    )
    assert inst.agent[0].who.identifier.value == "95"
    assert inst.agent[1].altId == "6580"
    assert inst.agent[1].network.address == "Workstation1.ehr.familyclinic.com"
    assert inst.agent[1].network.type == "1"
    assert inst.agent[1].requestor is False
    assert inst.agent[1].type.coding[0].code == "110153"
    assert inst.agent[1].type.coding[0].display == "Source Role ID"
    assert (
        inst.agent[1].type.coding[0].system
        == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.agent[1].who.identifier.system == "urn:oid:2.16.840.1.113883.4.2"
    assert inst.agent[1].who.identifier.value == "2.16.840.1.113883.4.2"
    assert inst.entity[0].query == bytes_validator(
        (
            "aHR0cDovL2ZoaXItZGV2LmhlYWx0aGludGVyc2VjdGlvbnMuY29tLmF1L29w"
            "ZW4vRW5jb3VudGVyP3BhcnRpY2lwYW50PTEz"
        )
    )
    assert inst.entity[0].role.code == "24"
    assert inst.entity[0].role.display == "Query"
    assert (
        inst.entity[0].role.system
        == "http://terminology.hl7.org/CodeSystem/object-role"
    )
    assert inst.entity[0].type.code == "2"
    assert inst.entity[0].type.display == "System Object"
    assert (
        inst.entity[0].type.system
        == "http://terminology.hl7.org/CodeSystem/audit-entity-type"
    )
    assert inst.id == "example-search"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.outcome == "0"
    assert inst.recorded == fhirtypes.Instant.validate("2015-08-22T23:42:24Z")
    assert inst.source.observer.display == "hl7connect.healthintersections.com.au"
    assert inst.source.site == "Cloud"
    assert inst.source.type[0].code == "3"
    assert inst.source.type[0].display == "Web Server"
    assert (
        inst.source.type[0].system
        == "http://terminology.hl7.org/CodeSystem/security-source-type"
    )
    assert inst.subtype[0].code == "search"
    assert inst.subtype[0].display == "search"
    assert inst.subtype[0].system == "http://hl7.org/fhir/restful-interaction"
    assert inst.text.status == "generated"
    assert inst.type.code == "rest"
    assert inst.type.display == "Restful Operation"
    assert inst.type.system == "http://terminology.hl7.org/CodeSystem/audit-event-type"


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
    assert inst.agent[0].altId == "601847123"
    assert inst.agent[0].name == "Grahame Grieve"
    assert inst.agent[0].network.address == "127.0.0.1"
    assert inst.agent[0].network.type == "2"
    assert inst.agent[0].requestor is True
    assert inst.agent[0].type.coding[0].code == "humanuser"
    assert inst.agent[0].type.coding[0].display == "human user"
    assert inst.agent[0].type.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/extra-security-role-" "type"
    )
    assert inst.agent[0].who.identifier.value == "95"
    assert inst.agent[1].altId == "6580"
    assert inst.agent[1].network.address == "Workstation1.ehr.familyclinic.com"
    assert inst.agent[1].network.type == "1"
    assert inst.agent[1].requestor is False
    assert inst.agent[1].type.coding[0].code == "110153"
    assert inst.agent[1].type.coding[0].display == "Source Role ID"
    assert (
        inst.agent[1].type.coding[0].system
        == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.agent[1].who.identifier.system == "urn:oid:2.16.840.1.113883.4.2"
    assert inst.agent[1].who.identifier.value == "2.16.840.1.113883.4.2"
    assert inst.id == "example-logout"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.outcome == "0"
    assert inst.recorded == fhirtypes.Instant.validate("2013-06-20T23:46:41Z")
    assert (
        inst.source.observer.identifier.value == "hl7connect.healthintersections.com.au"
    )
    assert inst.source.site == "Cloud"
    assert inst.source.type[0].code == "3"
    assert inst.source.type[0].display == "Web Server"
    assert (
        inst.source.type[0].system
        == "http://terminology.hl7.org/CodeSystem/security-source-type"
    )
    assert inst.subtype[0].code == "110123"
    assert inst.subtype[0].display == "Logout"
    assert inst.subtype[0].system == "http://dicom.nema.org/resources/ontology/DCM"
    assert inst.text.status == "generated"
    assert inst.type.code == "110114"
    assert inst.type.display == "User Authentication"
    assert inst.type.system == "http://dicom.nema.org/resources/ontology/DCM"


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
    assert inst.agent[0].altId == "601847123"
    assert inst.agent[0].name == "Grahame Grieve"
    assert inst.agent[0].requestor is True
    assert inst.agent[0].type.coding[0].code == "humanuser"
    assert inst.agent[0].type.coding[0].display == "human user"
    assert inst.agent[0].type.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/extra-security-role-" "type"
    )
    assert inst.agent[0].who.identifier.value == "95"
    assert inst.agent[1].altId == "6580"
    assert inst.agent[1].network.address == "Workstation1.ehr.familyclinic.com"
    assert inst.agent[1].network.type == "1"
    assert inst.agent[1].requestor is False
    assert inst.agent[1].type.coding[0].code == "110153"
    assert inst.agent[1].type.coding[0].display == "Source Role ID"
    assert (
        inst.agent[1].type.coding[0].system
        == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.agent[1].who.identifier.system == "urn:oid:2.16.840.1.113883.4.2"
    assert inst.agent[1].who.identifier.value == "2.16.840.1.113883.4.2"
    assert inst.entity[0].lifecycle.code == "6"
    assert inst.entity[0].lifecycle.display == "Access / Use"
    assert (
        inst.entity[0].lifecycle.system
        == "http://terminology.hl7.org/CodeSystem/dicom-audit-lifecycle"
    )
    assert inst.entity[0].type.code == "2"
    assert inst.entity[0].type.display == "System Object"
    assert (
        inst.entity[0].type.system
        == "http://terminology.hl7.org/CodeSystem/audit-entity-type"
    )
    assert inst.entity[0].what.reference == "Patient/example/_history/1"
    assert inst.id == "example-rest"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.outcome == "0"
    assert inst.recorded == fhirtypes.Instant.validate("2013-06-20T23:42:24Z")
    assert (
        inst.source.observer.identifier.value == "hl7connect.healthintersections.com.au"
    )
    assert inst.source.site == "Cloud"
    assert inst.source.type[0].code == "3"
    assert inst.source.type[0].display == "Web Server"
    assert (
        inst.source.type[0].system
        == "http://terminology.hl7.org/CodeSystem/security-source-type"
    )
    assert inst.subtype[0].code == "vread"
    assert inst.subtype[0].display == "vread"
    assert inst.subtype[0].system == "http://hl7.org/fhir/restful-interaction"
    assert inst.text.status == "generated"
    assert inst.type.code == "rest"
    assert inst.type.display == "Restful Operation"
    assert inst.type.system == "http://terminology.hl7.org/CodeSystem/audit-event-type"


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
    assert inst.action == "R"
    assert inst.agent[0].requestor is False
    assert inst.agent[0].type.coding[0].code == "110153"
    assert inst.agent[0].type.coding[0].display == "Source Role ID"
    assert (
        inst.agent[0].type.coding[0].system
        == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.agent[0].who.display == "ExportToMedia.app"
    assert inst.agent[1].altId == "601847123"
    assert inst.agent[1].name == "Grahame Grieve"
    assert inst.agent[1].requestor is True
    assert inst.agent[1].type.coding[0].code == "humanuser"
    assert inst.agent[1].type.coding[0].display == "human user"
    assert inst.agent[1].type.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/extra-security-role-" "type"
    )
    assert inst.agent[1].who.identifier.value == "95"
    assert inst.agent[2].media.code == "110033"
    assert inst.agent[2].media.display == "DVD"
    assert inst.agent[2].media.system == "http://dicom.nema.org/resources/ontology/DCM"
    assert inst.agent[2].name == "Media title: Hello World"
    assert inst.agent[2].requestor is False
    assert inst.agent[2].type.coding[0].code == "110154"
    assert inst.agent[2].type.coding[0].display == "Destination Media"
    assert (
        inst.agent[2].type.coding[0].system
        == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.entity[0].role.code == "1"
    assert inst.entity[0].role.display == "Patient"
    assert (
        inst.entity[0].role.system
        == "http://terminology.hl7.org/CodeSystem/object-role"
    )
    assert inst.entity[0].type.code == "1"
    assert inst.entity[0].type.display == "Person"
    assert (
        inst.entity[0].type.system
        == "http://terminology.hl7.org/CodeSystem/audit-entity-type"
    )
    assert (
        inst.entity[0].what.identifier.value
        == "e3cdfc81a0d24bd^^^&2.16.840.1.113883.4.2&ISO"
    )
    assert inst.entity[1].role.code == "20"
    assert inst.entity[1].role.display == "Job"
    assert (
        inst.entity[1].role.system
        == "http://terminology.hl7.org/CodeSystem/object-role"
    )
    assert inst.entity[1].type.code == "2"
    assert inst.entity[1].type.display == "System Object"
    assert (
        inst.entity[1].type.system
        == "http://terminology.hl7.org/CodeSystem/audit-entity-type"
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
    assert inst.entity[2].type.code == "2"
    assert inst.entity[2].type.display == "System Object"
    assert (
        inst.entity[2].type.system
        == "http://terminology.hl7.org/CodeSystem/audit-entity-type"
    )
    assert inst.entity[2].what.reference == "DocumentManifest/example"
    assert inst.id == "example-media"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.outcome == "0"
    assert inst.recorded == fhirtypes.Instant.validate("2015-08-27T23:42:24Z")
    assert inst.source.observer.display == "hl7connect.healthintersections.com.au"
    assert inst.subtype[0].code == "ITI-32"
    assert inst.subtype[0].display == "Distribute Document Set on Media"
    assert inst.subtype[0].system == "urn:oid:1.3.6.1.4.1.19376.1.2"
    assert inst.text.status == "generated"
    assert inst.type.code == "110106"
    assert inst.type.display == "Export"
    assert inst.type.system == "http://dicom.nema.org/resources/ontology/DCM"


def test_auditevent_4(base_settings):
    """No. 4 tests collection for AuditEvent.
    Test File: audit-event-example-media.json
    """
    filename = base_settings["unittest_data_dir"] / "audit-event-example-media.json"
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
    assert inst.action == "E"
    assert inst.agent[0].altId == "601847123"
    assert inst.agent[0].name == "Grahame Grieve"
    assert inst.agent[0].network.address == "127.0.0.1"
    assert inst.agent[0].network.type == "2"
    assert inst.agent[0].requestor is True
    assert inst.agent[0].type.coding[0].code == "humanuser"
    assert inst.agent[0].type.coding[0].display == "human user"
    assert inst.agent[0].type.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/extra-security-role-" "type"
    )
    assert inst.agent[0].who.identifier.value == "95"
    assert inst.agent[1].altId == "6580"
    assert inst.agent[1].network.address == "Workstation1.ehr.familyclinic.com"
    assert inst.agent[1].network.type == "1"
    assert inst.agent[1].requestor is False
    assert inst.agent[1].type.coding[0].code == "110153"
    assert inst.agent[1].type.coding[0].display == "Source Role ID"
    assert (
        inst.agent[1].type.coding[0].system
        == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.agent[1].who.identifier.system == "urn:oid:2.16.840.1.113883.4.2"
    assert inst.agent[1].who.identifier.value == "2.16.840.1.113883.4.2"
    assert inst.id == "example-login"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.outcome == "0"
    assert inst.recorded == fhirtypes.Instant.validate("2013-06-20T23:41:23Z")
    assert (
        inst.source.observer.identifier.value == "hl7connect.healthintersections.com.au"
    )
    assert inst.source.site == "Cloud"
    assert inst.source.type[0].code == "3"
    assert inst.source.type[0].display == "Web Server"
    assert (
        inst.source.type[0].system
        == "http://terminology.hl7.org/CodeSystem/security-source-type"
    )
    assert inst.subtype[0].code == "110122"
    assert inst.subtype[0].display == "Login"
    assert inst.subtype[0].system == "http://dicom.nema.org/resources/ontology/DCM"
    assert inst.text.status == "generated"
    assert inst.type.code == "110114"
    assert inst.type.display == "User Authentication"
    assert inst.type.system == "http://dicom.nema.org/resources/ontology/DCM"


def test_auditevent_5(base_settings):
    """No. 5 tests collection for AuditEvent.
    Test File: audit-event-example-login.json
    """
    filename = base_settings["unittest_data_dir"] / "audit-event-example-login.json"
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
    assert inst.action == "E"
    assert inst.agent[0].altId == "6580"
    assert inst.agent[0].network.address == "Workstation1.ehr.familyclinic.com"
    assert inst.agent[0].network.type == "1"
    assert inst.agent[0].requestor is False
    assert inst.agent[0].type.coding[0].code == "110153"
    assert inst.agent[0].type.coding[0].display == "Source Role ID"
    assert (
        inst.agent[0].type.coding[0].system
        == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.agent[0].who.identifier.system == "urn:oid:2.16.840.1.113883.4.2"
    assert inst.agent[0].who.identifier.value == "2.16.840.1.113883.4.2"
    assert inst.agent[1].altId == "601847123"
    assert inst.agent[1].name == "Grahame Grieve"
    assert inst.agent[1].requestor is True
    assert inst.agent[1].type.coding[0].code == "humanuser"
    assert inst.agent[1].type.coding[0].display == "human user"
    assert inst.agent[1].type.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/extra-security-role-" "type"
    )
    assert inst.agent[1].who.identifier.value == "95"
    assert inst.entity[0].role.code == "1"
    assert inst.entity[0].role.display == "Patient"
    assert (
        inst.entity[0].role.system
        == "http://terminology.hl7.org/CodeSystem/object-role"
    )
    assert inst.entity[0].type.code == "1"
    assert inst.entity[0].type.display == "Person"
    assert (
        inst.entity[0].type.system
        == "http://terminology.hl7.org/CodeSystem/audit-entity-type"
    )
    assert (
        inst.entity[0].what.identifier.value
        == "e3cdfc81a0d24bd^^^&2.16.840.1.113883.4.2&ISO"
    )
    assert inst.entity[1].detail[0].type == "MSH-10"
    assert inst.entity[1].detail[0].valueBase64Binary == bytes_validator(
        "MS4yLjg0MC4xMTQzNTAuMS4xMy4wLjEuNy4xLjE="
    )
    assert inst.entity[1].role.code == "24"
    assert inst.entity[1].role.display == "Query"
    assert (
        inst.entity[1].role.system
        == "http://terminology.hl7.org/CodeSystem/object-role"
    )
    assert inst.entity[1].type.code == "2"
    assert inst.entity[1].type.display == "System Object"
    assert (
        inst.entity[1].type.system
        == "http://terminology.hl7.org/CodeSystem/audit-entity-type"
    )
    assert inst.id == "example-pixQuery"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.outcome == "0"
    assert inst.recorded == fhirtypes.Instant.validate("2015-08-26T23:42:24Z")
    assert inst.source.observer.display == "hl7connect.healthintersections.com.au"
    assert inst.subtype[0].code == "ITI-9"
    assert inst.subtype[0].display == "PIX Query"
    assert inst.subtype[0].system == "urn:oid:1.3.6.1.4.1.19376.1.2"
    assert inst.text.status == "generated"
    assert inst.type.code == "110112"
    assert inst.type.display == "Query"
    assert inst.type.system == "http://dicom.nema.org/resources/ontology/DCM"


def test_auditevent_6(base_settings):
    """No. 6 tests collection for AuditEvent.
    Test File: audit-event-example-pixQuery.json
    """
    filename = base_settings["unittest_data_dir"] / "audit-event-example-pixQuery.json"
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
    assert inst.agent[0].network.address == "127.0.0.1"
    assert inst.agent[0].network.type == "2"
    assert inst.agent[0].requestor is False
    assert inst.agent[0].role[0].text == "Service User (Logon)"
    assert inst.agent[0].type.coding[0].code == "humanuser"
    assert inst.agent[0].type.coding[0].display == "human user"
    assert inst.agent[0].type.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/extra-security-role-" "type"
    )
    assert inst.agent[0].who.identifier.value == "Grahame"
    assert inst.agent[1].altId == "6580"
    assert inst.agent[1].network.address == "Workstation1.ehr.familyclinic.com"
    assert inst.agent[1].network.type == "1"
    assert inst.agent[1].requestor is False
    assert inst.agent[1].type.coding[0].code == "110153"
    assert inst.agent[1].type.coding[0].display == "Source Role ID"
    assert (
        inst.agent[1].type.coding[0].system
        == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.agent[1].who.identifier.system == "urn:oid:2.16.840.1.113883.4.2"
    assert inst.agent[1].who.identifier.value == "2.16.840.1.113883.4.2"
    assert inst.entity[0].lifecycle.code == "6"
    assert inst.entity[0].lifecycle.display == "Access / Use"
    assert (
        inst.entity[0].lifecycle.system
        == "http://terminology.hl7.org/CodeSystem/dicom-audit-lifecycle"
    )
    assert inst.entity[0].name == "Grahame's Laptop"
    assert inst.entity[0].role.code == "4"
    assert inst.entity[0].role.display == "Domain Resource"
    assert (
        inst.entity[0].role.system
        == "http://terminology.hl7.org/CodeSystem/object-role"
    )
    assert inst.entity[0].type.code == "4"
    assert inst.entity[0].type.display == "Other"
    assert (
        inst.entity[0].type.system
        == "http://terminology.hl7.org/CodeSystem/audit-entity-type"
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
    assert inst.outcome == "0"
    assert inst.recorded == fhirtypes.Instant.validate("2012-10-25T22:04:27+11:00")
    assert inst.source.observer.display == "Grahame's Laptop"
    assert inst.source.site == "Development"
    assert inst.source.type[0].code == "110122"
    assert inst.source.type[0].display == "Login"
    assert inst.source.type[0].system == "http://dicom.nema.org/resources/ontology/DCM"
    assert inst.subtype[0].code == "110120"
    assert inst.subtype[0].display == "Application Start"
    assert inst.subtype[0].system == "http://dicom.nema.org/resources/ontology/DCM"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Application '
        "Start for under service login &quot;Grahame&quot; (id: "
        "Grahame's Test HL7Connect)</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type.code == "110100"
    assert inst.type.display == "Application Activity"
    assert inst.type.system == "http://dicom.nema.org/resources/ontology/DCM"


def test_auditevent_7(base_settings):
    """No. 7 tests collection for AuditEvent.
    Test File: auditevent-example.json
    """
    filename = base_settings["unittest_data_dir"] / "auditevent-example.json"
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
    assert inst.action == "R"
    assert inst.agent[0].altId == "notMe"
    assert inst.agent[0].location.reference == "Location/1"
    assert inst.agent[0].name == "That guy everyone wishes would be caught"
    assert inst.agent[0].network.address == "custodian.net"
    assert inst.agent[0].network.type == "1"
    assert inst.agent[0].policy[0] == "http://consent.com/yes"
    assert inst.agent[0].requestor is True
    assert inst.agent[0].type.coding[0].code == "110153"
    assert inst.agent[0].type.coding[0].display == "Source Role ID"
    assert (
        inst.agent[0].type.coding[0].system
        == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.agent[0].who.identifier.value == "SomeIdiot@nowhere"
    assert inst.agent[1].network.address == "marketing.land"
    assert inst.agent[1].network.type == "1"
    assert inst.agent[1].purposeOfUse[0].coding[0].code == "HMARKT"
    assert inst.agent[1].purposeOfUse[0].coding[0].display == "healthcare marketing"
    assert (
        inst.agent[1].purposeOfUse[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.agent[1].requestor is False
    assert inst.agent[1].type.coding[0].code == "110152"
    assert inst.agent[1].type.coding[0].display == "Destination Role ID"
    assert (
        inst.agent[1].type.coding[0].system
        == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.agent[1].who.display == "Where"
    assert inst.agent[1].who.reference == "Practitioner/example"
    assert inst.entity[0].role.code == "1"
    assert inst.entity[0].role.display == "Patient"
    assert (
        inst.entity[0].role.system
        == "http://terminology.hl7.org/CodeSystem/object-role"
    )
    assert inst.entity[0].type.code == "1"
    assert inst.entity[0].type.display == "Person"
    assert (
        inst.entity[0].type.system
        == "http://terminology.hl7.org/CodeSystem/audit-entity-type"
    )
    assert inst.entity[0].what.reference == "Patient/example"
    assert inst.entity[1].description == "data about Everthing important"
    assert inst.entity[1].lifecycle.code == "11"
    assert inst.entity[1].lifecycle.display == "Disclosure"
    assert (
        inst.entity[1].lifecycle.system
        == "http://terminology.hl7.org/CodeSystem/dicom-audit-lifecycle"
    )
    assert inst.entity[1].name == "Namne of What"
    assert inst.entity[1].role.code == "4"
    assert inst.entity[1].role.display == "Domain Resource"
    assert (
        inst.entity[1].role.system
        == "http://terminology.hl7.org/CodeSystem/object-role"
    )
    assert inst.entity[1].securityLabel[0].code == "V"
    assert inst.entity[1].securityLabel[0].display == "very restricted"
    assert (
        inst.entity[1].securityLabel[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-Confidentiality"
    )
    assert inst.entity[1].securityLabel[1].code == "STD"
    assert (
        inst.entity[1].securityLabel[1].display
        == "sexually transmitted disease information sensitivity"
    )
    assert (
        inst.entity[1].securityLabel[1].system
        == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )
    assert inst.entity[1].securityLabel[2].code == "DELAU"
    assert inst.entity[1].securityLabel[2].display == "delete after use"
    assert (
        inst.entity[1].securityLabel[2].system
        == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )
    assert inst.entity[1].type.code == "2"
    assert inst.entity[1].type.display == "System Object"
    assert (
        inst.entity[1].type.system
        == "http://terminology.hl7.org/CodeSystem/audit-entity-type"
    )
    assert inst.entity[1].what.identifier.value == "What.id"
    assert inst.entity[1].what.reference == "Patient/example/_history/1"
    assert inst.id == "example-disclosure"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.outcome == "0"
    assert inst.outcomeDesc == "Successful  Disclosure"
    assert inst.purposeOfEvent[0].coding[0].code == "HMARKT"
    assert inst.purposeOfEvent[0].coding[0].display == "healthcare marketing"
    assert (
        inst.purposeOfEvent[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.recorded == fhirtypes.Instant.validate("2013-09-22T00:08:00Z")
    assert (
        inst.source.observer.display == "Watchers Accounting of Disclosures Application"
    )
    assert inst.source.site == "Watcher"
    assert inst.source.type[0].code == "4"
    assert inst.source.type[0].display == "Application Server"
    assert (
        inst.source.type[0].system
        == "http://terminology.hl7.org/CodeSystem/security-source-type"
    )
    assert inst.subtype[0].code == "Disclosure"
    assert inst.subtype[0].display == "HIPAA disclosure"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Disclosure by '
        "some idiot, for marketing reasons, to places unknown, of a "
        "Poor Sap, data about Everthing important.</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type.code == "110106"
    assert inst.type.display == "Export"
    assert inst.type.system == "http://dicom.nema.org/resources/ontology/DCM"


def test_auditevent_8(base_settings):
    """No. 8 tests collection for AuditEvent.
    Test File: auditevent-example-disclosure.json
    """
    filename = base_settings["unittest_data_dir"] / "auditevent-example-disclosure.json"
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
    assert inst.action == "C"
    assert inst.agent[0].altId == "601847123"
    assert inst.agent[0].name == "Grahame Grieve"
    assert inst.agent[0].requestor is True
    assert inst.agent[0].type.coding[0].code == "humanuser"
    assert inst.agent[0].type.coding[0].display == "human user"
    assert inst.agent[0].type.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/extra-security-role-" "type"
    )
    assert inst.agent[0].who.identifier.value == "95"
    assert inst.agent[1].altId == "6580"
    assert inst.agent[1].network.address == "Workstation1.ehr.familyclinic.com"
    assert inst.agent[1].network.type == "1"
    assert inst.agent[1].requestor is False
    assert inst.agent[1].type.coding[0].code == "110153"
    assert inst.agent[1].type.coding[0].display == "Source Role ID"
    assert (
        inst.agent[1].type.coding[0].system
        == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.agent[1].who.identifier.system == "urn:oid:2.16.840.1.113883.4.2"
    assert inst.agent[1].who.identifier.value == "2.16.840.1.113883.4.2"
    assert inst.contained[0].id == "o1"
    assert inst.entity[0].detail[0].type == "requested transaction"
    assert inst.entity[0].detail[0].valueString == "http POST ....."
    assert inst.entity[0].type.code == "2"
    assert inst.entity[0].type.display == "System Object"
    assert (
        inst.entity[0].type.system
        == "http://terminology.hl7.org/CodeSystem/audit-entity-type"
    )
    assert inst.entity[1].description == "transaction failed"
    assert inst.entity[1].type.code == "OperationOutcome"
    assert inst.entity[1].type.display == "OperationOutcome"
    assert inst.entity[1].type.system == "http://hl7.org/fhir/resource-types"
    assert inst.entity[1].what.reference == "#o1"
    assert inst.id == "example-error"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.outcome == "8"
    assert inst.outcomeDesc == (
        "Invalid request to create an Operation resource on the " "Patient endpoint."
    )
    assert inst.recorded == fhirtypes.Instant.validate("2017-09-07T23:42:24Z")
    assert (
        inst.source.observer.identifier.value == "hl7connect.healthintersections.com.au"
    )
    assert inst.source.site == "Cloud"
    assert inst.source.type[0].code == "3"
    assert inst.source.type[0].display == "Web Server"
    assert (
        inst.source.type[0].system
        == "http://terminology.hl7.org/CodeSystem/security-source-type"
    )
    assert inst.subtype[0].code == "create"
    assert inst.subtype[0].display == "create"
    assert inst.subtype[0].system == "http://hl7.org/fhir/restful-interaction"
    assert inst.text.status == "generated"
    assert inst.type.code == "rest"
    assert inst.type.display == "Restful Operation"
    assert inst.type.system == "http://terminology.hl7.org/CodeSystem/audit-event-type"


def test_auditevent_9(base_settings):
    """No. 9 tests collection for AuditEvent.
    Test File: auditevent-example-error.json
    """
    filename = base_settings["unittest_data_dir"] / "auditevent-example-error.json"
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
