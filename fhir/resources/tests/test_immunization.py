# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Immunization
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import immunization


def impl_immunization_1(inst):
    assert inst.doseQuantity.code == "mg"
    assert inst.doseQuantity.system == "http://unitsofmeasure.org"
    assert float(inst.doseQuantity.value) == float(5)
    assert inst.education[0].documentType == "253088698300010311120702"
    assert inst.education[0].presentationDate == fhirtypes.DateTime.validate(
        "2013-01-10"
    )
    assert inst.education[0].publicationDate == fhirtypes.DateTime.validate(
        "2012-07-02"
    )
    assert inst.encounter.reference == "Encounter/example"
    assert inst.expirationDate == fhirtypes.Date.validate("2015-02-15")
    assert inst.fundingSource.coding[0].code == "private"
    assert inst.fundingSource.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/immunization-funding-" "source"
    )
    assert inst.id == "example"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"
    assert inst.isSubpotent is True
    assert inst.location.reference == "Location/1"
    assert inst.lotNumber == "AAJN11K"
    assert inst.manufacturer.reference == "Organization/hl7"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.note[0].text == "Notes on adminstration of vaccine"
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate("2013-01-10")
    assert inst.patient.reference == "Patient/example"
    assert inst.performer[0].actor.reference == "Practitioner/example"
    assert inst.performer[0].function.coding[0].code == "OP"
    assert (
        inst.performer[0].function.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0443"
    )
    assert inst.performer[1].actor.reference == "Practitioner/example"
    assert inst.performer[1].function.coding[0].code == "AP"
    assert (
        inst.performer[1].function.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0443"
    )
    assert inst.primarySource is True
    assert inst.programEligibility[0].coding[0].code == "ineligible"
    assert inst.programEligibility[0].coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/immunization-program-" "eligibility"
    )
    assert inst.reasonCode[0].coding[0].code == "429060002"
    assert inst.reasonCode[0].coding[0].system == "http://snomed.info/sct"
    assert inst.route.coding[0].code == "IM"
    assert inst.route.coding[0].display == "Injection, intramuscular"
    assert inst.route.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministrati" "on"
    )
    assert inst.site.coding[0].code == "LA"
    assert inst.site.coding[0].display == "left arm"
    assert (
        inst.site.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActSite"
    )
    assert inst.status == "completed"
    assert inst.text.status == "generated"
    assert inst.vaccineCode.coding[0].code == "FLUVAX"
    assert inst.vaccineCode.coding[0].system == "urn:oid:1.2.36.1.2001.1005.17"
    assert inst.vaccineCode.text == "Fluvax (Influenza)"


def test_immunization_1(base_settings):
    """No. 1 tests collection for Immunization.
    Test File: immunization-example.json
    """
    filename = base_settings["unittest_data_dir"] / "immunization-example.json"
    inst = immunization.Immunization.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Immunization" == inst.resource_type

    impl_immunization_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Immunization" == data["resourceType"]

    inst2 = immunization.Immunization(**data)
    impl_immunization_1(inst2)


def impl_immunization_2(inst):
    assert inst.id == "historical"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"
    assert inst.location.reference == "Location/1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.note[0].text == "Notes on adminstration of a historical vaccine"
    assert inst.occurrenceString == "January 2012"
    assert inst.patient.reference == "Patient/example"
    assert inst.primarySource is False
    assert inst.reportOrigin.coding[0].code == "record"
    assert (
        inst.reportOrigin.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/immunization-origin"
    )
    assert inst.reportOrigin.text == "Written Record"
    assert inst.status == "completed"
    assert inst.text.status == "generated"
    assert inst.vaccineCode.coding[0].code == "GNFLU"
    assert inst.vaccineCode.coding[0].system == "urn:oid:1.2.36.1.2001.1005.17"
    assert inst.vaccineCode.text == "Influenza"


def test_immunization_2(base_settings):
    """No. 2 tests collection for Immunization.
    Test File: immunization-example-historical.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "immunization-example-historical.json"
    )
    inst = immunization.Immunization.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Immunization" == inst.resource_type

    impl_immunization_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Immunization" == data["resourceType"]

    inst2 = immunization.Immunization(**data)
    impl_immunization_2(inst2)


def impl_immunization_3(inst):
    assert inst.doseQuantity.code == "mg"
    assert inst.doseQuantity.system == "http://unitsofmeasure.org"
    assert float(inst.doseQuantity.value) == float(5)
    assert inst.encounter.reference == "Encounter/example"
    assert inst.expirationDate == fhirtypes.Date.validate("2018-12-15")
    assert inst.fundingSource.coding[0].code == "private"
    assert inst.fundingSource.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/immunization-funding-" "source"
    )
    assert inst.id == "protocol"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"
    assert inst.isSubpotent is False
    assert inst.location.reference == "Location/1"
    assert inst.lotNumber == "PT123F"
    assert inst.manufacturer.reference == "Organization/hl7"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate("2018-06-18")
    assert inst.patient.reference == "Patient/example"
    assert inst.performer[0].actor.reference == "Practitioner/example"
    assert inst.performer[0].function.coding[0].code == "OP"
    assert (
        inst.performer[0].function.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0443"
    )
    assert inst.performer[1].actor.reference == "Practitioner/example"
    assert inst.performer[1].function.coding[0].code == "AP"
    assert (
        inst.performer[1].function.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0443"
    )
    assert inst.primarySource is True
    assert inst.programEligibility[0].coding[0].code == "ineligible"
    assert inst.programEligibility[0].coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/immunization-program-" "eligibility"
    )
    assert inst.protocolApplied[0].doseNumberPositiveInt == 1
    assert inst.protocolApplied[0].series == "2-dose"
    assert inst.protocolApplied[0].targetDisease[0].coding[0].code == "40468003"
    assert (
        inst.protocolApplied[0].targetDisease[0].coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.protocolApplied[1].doseNumberPositiveInt == 2
    assert inst.protocolApplied[1].series == "3-dose"
    assert inst.protocolApplied[1].targetDisease[0].coding[0].code == "66071002"
    assert (
        inst.protocolApplied[1].targetDisease[0].coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.route.coding[0].code == "IM"
    assert inst.route.coding[0].display == "Injection, intramuscular"
    assert inst.route.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministrati" "on"
    )
    assert inst.site.coding[0].code == "LA"
    assert inst.site.coding[0].display == "left arm"
    assert (
        inst.site.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActSite"
    )
    assert inst.status == "completed"
    assert inst.text.status == "generated"
    assert inst.vaccineCode.coding[0].code == "104"
    assert inst.vaccineCode.coding[0].system == "http://hl7.org/fhir/sid/cvx"
    assert inst.vaccineCode.text == "Twinrix (HepA/HepB)"


def test_immunization_3(base_settings):
    """No. 3 tests collection for Immunization.
    Test File: immunization-example-protocol.json
    """
    filename = base_settings["unittest_data_dir"] / "immunization-example-protocol.json"
    inst = immunization.Immunization.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Immunization" == inst.resource_type

    impl_immunization_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Immunization" == data["resourceType"]

    inst2 = immunization.Immunization(**data)
    impl_immunization_3(inst2)


def impl_immunization_4(inst):
    assert inst.id == "notGiven"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate("2013-01-10")
    assert inst.patient.reference == "Patient/example"
    assert inst.primarySource is True
    assert inst.status == "not-done"
    assert inst.statusReason.coding[0].code == "MEDPREC"
    assert inst.statusReason.coding[0].display == "medical precaution"
    assert (
        inst.statusReason.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"
    assert inst.vaccineCode.coding[0].code == "01"
    assert inst.vaccineCode.coding[0].display == "DTP"
    assert inst.vaccineCode.coding[0].system == "http://hl7.org/fhir/sid/cvx"


def test_immunization_4(base_settings):
    """No. 4 tests collection for Immunization.
    Test File: immunization-example-refused.json
    """
    filename = base_settings["unittest_data_dir"] / "immunization-example-refused.json"
    inst = immunization.Immunization.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Immunization" == inst.resource_type

    impl_immunization_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Immunization" == data["resourceType"]

    inst2 = immunization.Immunization(**data)
    impl_immunization_4(inst2)


def impl_immunization_5(inst):
    assert inst.doseQuantity.code == "ml"
    assert inst.doseQuantity.system == "http://unitsofmeasure.org"
    assert float(inst.doseQuantity.value) == float(0.5)
    assert inst.education[0].documentType == "253088698300010311120702"
    assert inst.education[0].presentationDate == fhirtypes.DateTime.validate(
        "2013-01-10"
    )
    assert inst.education[0].publicationDate == fhirtypes.DateTime.validate(
        "2012-07-02"
    )
    assert inst.encounter.reference == "Encounter/example"
    assert inst.expirationDate == fhirtypes.Date.validate("2015-02-28")
    assert inst.fundingSource.coding[0].code == "private"
    assert inst.fundingSource.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/immunization-funding-" "source"
    )
    assert inst.id == "subpotent"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"
    assert inst.isSubpotent is False
    assert inst.location.reference == "Location/1"
    assert inst.lotNumber == "AAJN11K"
    assert inst.manufacturer.reference == "Organization/hl7"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.note[0].text == "Notes on adminstration of vaccine"
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate("2015-01-15")
    assert inst.patient.reference == "Patient/example"
    assert inst.performer[0].actor.reference == "Practitioner/example"
    assert inst.performer[0].function.coding[0].code == "OP"
    assert (
        inst.performer[0].function.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0443"
    )
    assert inst.performer[1].actor.reference == "Practitioner/example"
    assert inst.performer[1].function.coding[0].code == "AP"
    assert (
        inst.performer[1].function.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0443"
    )
    assert inst.primarySource is True
    assert inst.programEligibility[0].coding[0].code == "ineligible"
    assert inst.programEligibility[0].coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/immunization-program-" "eligibility"
    )
    assert inst.route.coding[0].code == "IM"
    assert inst.route.coding[0].display == "Injection, intramuscular"
    assert inst.route.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministrati" "on"
    )
    assert inst.site.coding[0].code == "LT"
    assert inst.site.coding[0].display == "left thigh"
    assert (
        inst.site.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActSite"
    )
    assert inst.status == "completed"
    assert inst.subpotentReason[0].coding[0].code == "partial"
    assert inst.subpotentReason[0].coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/immunization-" "subpotent-reason"
    )
    assert inst.text.status == "generated"
    assert inst.vaccineCode.coding[0].code == "GNHEP"
    assert inst.vaccineCode.coding[0].system == "urn:oid:1.2.36.1.2001.1005.17"
    assert inst.vaccineCode.text == "Hepatitis B"


def test_immunization_5(base_settings):
    """No. 5 tests collection for Immunization.
    Test File: immunization-example-subpotent.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "immunization-example-subpotent.json"
    )
    inst = immunization.Immunization.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Immunization" == inst.resource_type

    impl_immunization_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Immunization" == data["resourceType"]

    inst2 = immunization.Immunization(**data)
    impl_immunization_5(inst2)
