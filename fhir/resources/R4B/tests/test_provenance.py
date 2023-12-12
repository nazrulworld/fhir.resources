# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Provenance
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import provenance


def impl_provenance_1(inst):
    assert inst.activity.coding[0].code == "AU"
    assert inst.activity.coding[0].display == "authenticated"
    assert (
        inst.activity.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-DocumentCompletion"
    )
    assert inst.agent[0].type.coding[0].code == "VERF"
    assert inst.agent[0].type.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/contractsignertypecode" "s"
    )
    assert inst.agent[0].who.identifier.system == "urn:ietf:rfc:3986"
    assert inst.agent[0].who.identifier.value == "mailto://hhd@ssa.gov"
    assert inst.id == "signature"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.reason[0].coding[0].code == "TREAT"
    assert inst.reason[0].coding[0].display == "treatment"
    assert (
        inst.reason[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.recorded == fhirtypes.Instant.validate("2015-08-27T08:39:24+10:00")
    assert inst.signature[0].data == bytes_validator("Li4u")
    assert inst.signature[0].sigFormat == "application/signature+xml"
    assert inst.signature[0].targetFormat == "application/fhir+xml"
    assert inst.signature[0].type[0].code == "1.2.840.10065.1.12.1.5"
    assert inst.signature[0].type[0].display == "Verification Signature"
    assert inst.signature[0].type[0].system == "urn:iso-astm:E1762-95:2013"
    assert inst.signature[0].when == fhirtypes.Instant.validate(
        "2015-08-27T08:39:24+10:00"
    )
    assert inst.signature[0].who.reference == "Practitioner/xcda-author"
    assert inst.target[0].reference == "DocumentReference/example"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">procedure record'
        " authored on 27-June 2015 by Harold Hippocrates, MD Content "
        "extracted from Referral received 26-June</div>"
    )
    assert inst.text.status == "generated"


def test_provenance_1(base_settings):
    """No. 1 tests collection for Provenance.
    Test File: provenance-example-sig.json
    """
    filename = base_settings["unittest_data_dir"] / "provenance-example-sig.json"
    inst = provenance.Provenance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Provenance" == inst.resource_type

    impl_provenance_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Provenance" == data["resourceType"]

    inst2 = provenance.Provenance(**data)
    impl_provenance_1(inst2)


def impl_provenance_2(inst):
    assert inst.agent[0].role[0].coding[0].code == "AUT"
    assert (
        inst.agent[0].role[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"
    )
    assert inst.agent[0].who.reference == "Patient/72"
    assert inst.id == "consent-signature"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.recorded == fhirtypes.Instant.validate("2016-05-26T00:41:10-04:00")
    assert inst.signature[0].data == bytes_validator("dGhpcyBibG9iIGlzIHNuaXBwZWQ=")
    assert inst.signature[0].sigFormat == "application/signature+xml"
    assert inst.signature[0].targetFormat == "application/fhir+xml"
    assert inst.signature[0].type[0].code == "1.2.840.10065.1.12.1.1"
    assert inst.signature[0].type[0].display == "Author's Signature"
    assert inst.signature[0].type[0].system == "urn:iso-astm:E1762-95:2013"
    assert inst.signature[0].when == fhirtypes.Instant.validate(
        "2016-05-26T00:41:10-04:00"
    )
    assert inst.signature[0].who.reference == "Patient/72"
    assert inst.target[0].reference == "Consent/consent-example-signature"
    assert inst.text.status == "generated"


def test_provenance_2(base_settings):
    """No. 2 tests collection for Provenance.
    Test File: provenance-consent-signature.json
    """
    filename = base_settings["unittest_data_dir"] / "provenance-consent-signature.json"
    inst = provenance.Provenance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Provenance" == inst.resource_type

    impl_provenance_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Provenance" == data["resourceType"]

    inst2 = provenance.Provenance(**data)
    impl_provenance_2(inst2)


def impl_provenance_3(inst):
    assert inst.agent[0].type.coding[0].code == "AUT"
    assert (
        inst.agent[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"
    )
    assert inst.agent[0].who.reference == "Patient/example"
    assert inst.entity[0].role == "source"
    assert inst.entity[0].what.identifier.type.coding[0].code == "CWL"
    assert inst.entity[0].what.identifier.type.coding[0].display == "lobSTR"
    assert (
        inst.entity[0].what.identifier.type.coding[0].system
        == "https://github.com/common-workflow-language/workflows"
    )
    assert inst.entity[0].what.identifier.value == (
        "https://github.com/common-workflow-"
        "language/workflows/blob/master/workflows/lobSTR/lobSTR-"
        "workflow.cwl"
    )
    assert inst.id == "example-cwl"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.occurredPeriod.start == fhirtypes.DateTime.validate("2016-11-30")
    assert inst.reason[0].text == (
        "profiling Short Tandem Repeats (STRs) from high throughput " "sequencing data."
    )
    assert inst.recorded == fhirtypes.Instant.validate("2016-12-01T08:12:14+10:00")
    assert inst.target[0].reference == "MolecularSequence/example-pgx-1"
    assert inst.text.status == "generated"


def test_provenance_3(base_settings):
    """No. 3 tests collection for Provenance.
    Test File: provenance-example-cwl.json
    """
    filename = base_settings["unittest_data_dir"] / "provenance-example-cwl.json"
    inst = provenance.Provenance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Provenance" == inst.resource_type

    impl_provenance_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Provenance" == data["resourceType"]

    inst2 = provenance.Provenance(**data)
    impl_provenance_3(inst2)


def impl_provenance_4(inst):
    assert inst.agent[0].type.coding[0].code == "AUT"
    assert (
        inst.agent[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"
    )
    assert inst.agent[0].who.reference == "Practitioner/example"
    assert inst.entity[0].role == "source"
    assert inst.entity[0].what.identifier.type.coding[0].code == "biocompute"
    assert inst.entity[0].what.identifier.type.coding[0].display == "obj.1001"
    assert (
        inst.entity[0].what.identifier.type.coding[0].system
        == "https://hive.biochemistry.gwu.edu"
    )
    assert inst.entity[0].what.identifier.value == (
        "https://hive.biochemistry.gwu.edu/cgi-"
        "bin/prd/htscsrs/servlet.cgi?pageid=bcoexample_1"
    )
    assert inst.id == "example-biocompute-object"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.occurredPeriod.start == fhirtypes.DateTime.validate("2017-06-06")
    assert inst.reason[0].text == "antiviral resistance detection"
    assert inst.recorded == fhirtypes.Instant.validate("2016-06-09T08:12:14+10:00")
    assert inst.target[0].reference == "MolecularSequence/example"
    assert inst.text.status == "generated"


def test_provenance_4(base_settings):
    """No. 4 tests collection for Provenance.
    Test File: provenance-example-biocompute-object.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "provenance-example-biocompute-object.json"
    )
    inst = provenance.Provenance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Provenance" == inst.resource_type

    impl_provenance_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Provenance" == data["resourceType"]

    inst2 = provenance.Provenance(**data)
    impl_provenance_4(inst2)


def impl_provenance_5(inst):
    assert inst.agent[0].type.coding[0].code == "AUT"
    assert (
        inst.agent[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"
    )
    assert inst.agent[0].who.reference == "Practitioner/xcda-author"
    assert inst.agent[1].id == "a1"
    assert inst.agent[1].type.coding[0].code == "DEV"
    assert (
        inst.agent[1].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"
    )
    assert inst.agent[1].who.reference == "Device/software"
    assert inst.entity[0].role == "source"
    assert inst.entity[0].what.display == "CDA Document in XDS repository"
    assert inst.entity[0].what.reference == "DocumentReference/example"
    assert inst.id == "example"
    assert inst.location.reference == "Location/1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.occurredPeriod.end == fhirtypes.DateTime.validate("2015-06-28")
    assert inst.occurredPeriod.start == fhirtypes.DateTime.validate("2015-06-27")
    assert inst.policy[0] == "http://acme.com/fhir/Consent/25"
    assert inst.reason[0].coding[0].code == "3457005"
    assert inst.reason[0].coding[0].display == "Referral"
    assert inst.reason[0].coding[0].system == "http://snomed.info/sct"
    assert inst.recorded == fhirtypes.Instant.validate("2015-06-27T08:39:24+10:00")
    assert inst.target[0].reference == "Procedure/example/_history/1"
    assert inst.text.status == "generated"


def test_provenance_5(base_settings):
    """No. 5 tests collection for Provenance.
    Test File: provenance-example.json
    """
    filename = base_settings["unittest_data_dir"] / "provenance-example.json"
    inst = provenance.Provenance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Provenance" == inst.resource_type

    impl_provenance_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Provenance" == data["resourceType"]

    inst2 = provenance.Provenance(**data)
    impl_provenance_5(inst2)
