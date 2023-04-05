# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ServiceRequest
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import servicerequest


def impl_servicerequest_1(inst):
    assert inst.code.concept.coding[0].code == "3981005"
    assert (
        inst.code.concept.coding[0].display
        == "Carrier detection, molecular genetics (procedure)"
    )
    assert inst.code.concept.coding[0].system == "http://snomed.info/sct"
    assert inst.encounter.reference == "Encounter/denovoEncounter"
    assert inst.id == "genomicServiceRequest"
    assert (
        inst.identifier[0].system
        == "http://www.somesystemabc.net/identifiers/serviceRequests"
    )
    assert inst.identifier[0].type.coding[0].code == "LACSN"
    assert (
        inst.identifier[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0203"
    )
    assert inst.identifier[0].type.text == "Laboratory Accession ID"
    assert inst.identifier[0].value == "111111111"
    assert inst.intent == "plan"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "active"
    assert inst.subject.reference == "Patient/denovoChild"
    assert inst.text.status == "generated"


def test_servicerequest_1(base_settings):
    """No. 1 tests collection for ServiceRequest.
    Test File: ServiceRequest-genomicServiceRequest.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "ServiceRequest-genomicServiceRequest.json"
    )
    inst = servicerequest.ServiceRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ServiceRequest" == inst.resource_type

    impl_servicerequest_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ServiceRequest" == data["resourceType"]

    inst2 = servicerequest.ServiceRequest(**data)
    impl_servicerequest_1(inst2)


def impl_servicerequest_2(inst):
    assert inst.asNeededCodeableConcept.text == "as needed to clear mucus"
    assert inst.authoredOn == fhirtypes.DateTime.validate("2017-02-01T17:23:07Z")
    assert inst.basedOn[0].reference == "CarePlan/gpvisit"
    assert inst.code.concept.coding[0].code == "34431008"
    assert (
        inst.code.concept.coding[0].display == "Physiotherapy of chest (regime/therapy)"
    )
    assert inst.code.concept.coding[0].system == "http://snomed.info/sct"
    assert inst.contained[0].id == "signature"
    assert inst.contained[1].id == "cystic-fibrosis"
    assert inst.id == "physiotherapy"
    assert inst.identifier[0].system == "http://goodhealth.org/placer-ids"
    assert inst.identifier[0].type.coding[0].code == "PLAC"
    assert inst.identifier[0].type.coding[0].display == "Placer Identifier"
    assert (
        inst.identifier[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0203"
    )
    assert inst.identifier[0].type.text == "Placer"
    assert inst.identifier[0].value == "20170201-0001"
    assert inst.intent == "order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert float(inst.occurrenceTiming.repeat.duration) == float(15)
    assert float(inst.occurrenceTiming.repeat.durationMax) == float(25)
    assert inst.occurrenceTiming.repeat.durationUnit == "min"
    assert inst.occurrenceTiming.repeat.frequency == 1
    assert inst.occurrenceTiming.repeat.frequencyMax == 4
    assert float(inst.occurrenceTiming.repeat.period) == float(1)
    assert inst.occurrenceTiming.repeat.periodUnit == "d"
    assert inst.reason[0].reference.reference == "#cystic-fibrosis"
    assert inst.relevantHistory[0].display == "Author's Signature"
    assert inst.relevantHistory[0].reference == "#signature"
    assert inst.requester.display == "Dr Adam Careful"
    assert inst.requester.reference == "Practitioner/example"
    assert inst.status == "completed"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_servicerequest_2(base_settings):
    """No. 2 tests collection for ServiceRequest.
    Test File: servicerequest-example2.json
    """
    filename = base_settings["unittest_data_dir"] / "servicerequest-example2.json"
    inst = servicerequest.ServiceRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ServiceRequest" == inst.resource_type

    impl_servicerequest_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ServiceRequest" == data["resourceType"]

    inst2 = servicerequest.ServiceRequest(**data)
    impl_servicerequest_2(inst2)


def impl_servicerequest_3(inst):
    assert inst.code.concept.coding[0].code == "3981005"
    assert (
        inst.code.concept.coding[0].display
        == "Carrier detection, molecular genetics (procedure)"
    )
    assert inst.code.concept.coding[0].system == "http://snomed.info/sct"
    assert inst.encounter.reference == "Encounter/denovoEncounter"
    assert inst.id == "genomicSRMother"
    assert (
        inst.identifier[0].system
        == "http://www.somesystemabc.net/identifiers/serviceRequests"
    )
    assert inst.identifier[0].type.coding[0].code == "LACSN"
    assert (
        inst.identifier[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0203"
    )
    assert inst.identifier[0].type.text == "Laboratory Accession ID"
    assert inst.identifier[0].value == "111111116"
    assert inst.intent == "plan"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "active"
    assert inst.subject.reference == "Patient/mother"
    assert inst.text.status == "generated"


def test_servicerequest_3(base_settings):
    """No. 3 tests collection for ServiceRequest.
    Test File: ServiceRequest-genomicSRMother.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "ServiceRequest-genomicSRMother.json"
    )
    inst = servicerequest.ServiceRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ServiceRequest" == inst.resource_type

    impl_servicerequest_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ServiceRequest" == data["resourceType"]

    inst2 = servicerequest.ServiceRequest(**data)
    impl_servicerequest_3(inst2)


def impl_servicerequest_4(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2017-02-01T17:23:07Z")
    assert inst.code.concept.coding[0].code == "359962006"
    assert inst.code.concept.coding[0].display == "Turning patient in bed (procedure)"
    assert inst.code.concept.coding[0].system == "http://snomed.info/sct"
    assert inst.doNotPerform is True
    assert inst.id == "do-not-turn"
    assert inst.identifier[0].system == "http://goodhealth.org/placer-ids"
    assert inst.identifier[0].value == "20170201-0002"
    assert inst.intent == "order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.priority == "stat"
    assert inst.reason[0].reference.display == "Patient has a spinal fracture"
    assert inst.requester.display == "Dr Adam Careful"
    assert inst.requester.reference == "Practitioner/example"
    assert inst.status == "active"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_servicerequest_4(base_settings):
    """No. 4 tests collection for ServiceRequest.
    Test File: servicerequest-example3.json
    """
    filename = base_settings["unittest_data_dir"] / "servicerequest-example3.json"
    inst = servicerequest.ServiceRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ServiceRequest" == inst.resource_type

    impl_servicerequest_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ServiceRequest" == data["resourceType"]

    inst2 = servicerequest.ServiceRequest(**data)
    impl_servicerequest_4(inst2)


def impl_servicerequest_5(inst):
    assert inst.code.concept.coding[0].code == "LIPID"
    assert inst.code.concept.coding[0].system == "http://acme.org/tests"
    assert inst.code.concept.text == "Lipid Panel"
    assert inst.contained[0].id == "fasting"
    assert inst.contained[1].id == "serum"
    assert inst.encounter.reference == "Encounter/example"
    assert inst.id == "lipid"
    assert inst.identifier[0].system == "urn:oid:1.3.4.5.6.7"
    assert inst.identifier[0].type.coding[0].code == "PLAC"
    assert (
        inst.identifier[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0203"
    )
    assert inst.identifier[0].type.text == "Placer"
    assert inst.identifier[0].value == "2345234234234"
    assert inst.intent == "original-order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.note[0].text == "patient is afraid of needles"
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate(
        "2013-05-02T16:16:00-07:00"
    )
    assert inst.performer[0].reference == "Practitioner/f202"
    assert inst.reason[0].concept.coding[0].code == "V173"
    assert inst.reason[0].concept.coding[0].display == "Fam hx-ischem heart dis"
    assert inst.reason[0].concept.coding[0].system == "http://hl7.org/fhir/sid/icd-9"
    assert inst.requester.reference == "Practitioner/example"
    assert inst.specimen[0].display == "Serum specimen"
    assert inst.specimen[0].reference == "#serum"
    assert inst.status == "active"
    assert inst.subject.reference == "Patient/example"
    assert inst.supportingInfo[0].reference.display == "Fasting status"
    assert inst.supportingInfo[0].reference.reference == "#fasting"
    assert inst.text.status == "generated"


def test_servicerequest_5(base_settings):
    """No. 5 tests collection for ServiceRequest.
    Test File: servicerequest-example-lipid.json
    """
    filename = base_settings["unittest_data_dir"] / "servicerequest-example-lipid.json"
    inst = servicerequest.ServiceRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ServiceRequest" == inst.resource_type

    impl_servicerequest_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ServiceRequest" == data["resourceType"]

    inst2 = servicerequest.ServiceRequest(**data)
    impl_servicerequest_5(inst2)


def impl_servicerequest_6(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2017-03-05")
    assert inst.code.concept.coding[0].code == "76164006"
    assert inst.code.concept.coding[0].display == "Biopsy of colon (procedure)"
    assert inst.code.concept.coding[0].system == "http://snomed.info/sct"
    assert inst.code.concept.text == "Biopsy of colon"
    assert inst.id == "colon-biopsy"
    assert inst.identifier[0].value == "12345"
    assert inst.intent == "order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].display == "Dr Adam Careful"
    assert inst.performer[0].reference == "Practitioner/example"
    assert inst.requester.display == "Dr. Beverly Crusher"
    assert (
        inst.requester.reference == "Practitioner/3ad0687e-f477-468c-afd5-fcc2bf897809"
    )
    assert inst.requisition.system == "http://bumc.org/requisitions"
    assert inst.requisition.value == "req12345"
    assert inst.status == "completed"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_servicerequest_6(base_settings):
    """No. 6 tests collection for ServiceRequest.
    Test File: servicerequest-example-colonoscopy-bx.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "servicerequest-example-colonoscopy-bx.json"
    )
    inst = servicerequest.ServiceRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ServiceRequest" == inst.resource_type

    impl_servicerequest_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ServiceRequest" == data["resourceType"]

    inst2 = servicerequest.ServiceRequest(**data)
    impl_servicerequest_6(inst2)


def impl_servicerequest_7(inst):
    assert inst.code.concept.coding[0].code == "229115003"
    assert inst.code.concept.coding[0].display == "Bench Press (regime/therapy)"
    assert inst.code.concept.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "benchpress"
    assert inst.intent == "plan"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.occurrenceTiming.repeat.count == 20
    assert inst.occurrenceTiming.repeat.countMax == 30
    assert inst.occurrenceTiming.repeat.frequency == 3
    assert float(inst.occurrenceTiming.repeat.period) == float(1)
    assert inst.occurrenceTiming.repeat.periodUnit == "wk"
    assert inst.patientInstruction[0].instructionMarkdown == (
        "Start with 30kg 10-15 repetitions for three sets and "
        "increase in increments of 5kg when you feel ready"
    )
    assert inst.status == "active"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_servicerequest_7(base_settings):
    """No. 7 tests collection for ServiceRequest.
    Test File: servicerequest-example4.json
    """
    filename = base_settings["unittest_data_dir"] / "servicerequest-example4.json"
    inst = servicerequest.ServiceRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ServiceRequest" == inst.resource_type

    impl_servicerequest_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ServiceRequest" == data["resourceType"]

    inst2 = servicerequest.ServiceRequest(**data)
    impl_servicerequest_7(inst2)


def impl_servicerequest_8(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2016-08-16")
    assert inst.category[0].coding[0].code == "311401005"
    assert inst.category[0].coding[0].display == "Patient education (procedure)"
    assert inst.category[0].coding[0].system == "http://snomed.info/sct"
    assert inst.category[0].text == "Education"
    assert inst.code.concept.coding[0].code == "48023004"
    assert (
        inst.code.concept.coding[0].display
        == "Breast self-examination technique education (procedure)"
    )
    assert inst.code.concept.coding[0].system == "http://snomed.info/sct"
    assert inst.code.concept.text == "Health education - breast examination"
    assert inst.id == "education"
    assert inst.intent == "order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.performer[0].display == "Pamela Educator, RN"
    assert inst.reason[0].concept.text == "early detection of breast mass"
    assert inst.requester.display == "Angela Care, MD"
    assert inst.status == "completed"
    assert inst.subject.display == "Jane Doe"
    assert inst.text.status == "generated"


def test_servicerequest_8(base_settings):
    """No. 8 tests collection for ServiceRequest.
    Test File: servicerequest-example-edu.json
    """
    filename = base_settings["unittest_data_dir"] / "servicerequest-example-edu.json"
    inst = servicerequest.ServiceRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ServiceRequest" == inst.resource_type

    impl_servicerequest_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ServiceRequest" == data["resourceType"]

    inst2 = servicerequest.ServiceRequest(**data)
    impl_servicerequest_8(inst2)


def impl_servicerequest_9(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2018-02-20")
    assert inst.code.concept.coding[0].code == "40617009"
    assert inst.code.concept.coding[0].display == "Artificial respiration (procedure)"
    assert inst.code.concept.coding[0].system == "http://snomed.info/sct"
    assert inst.code.concept.text == "Mechanical Ventilation"
    assert inst.id == "vent"
    assert inst.intent == "order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].display == "Dr Cecil Surgeon"
    assert inst.performer[0].reference == "Practitioner/example"
    assert inst.reason[0].concept.text == "chronic obstructive lung disease (COLD)"
    assert inst.requester.display == "Dr. Beverly Crusher"
    assert (
        inst.requester.reference == "Practitioner/3ad0687e-f477-468c-afd5-fcc2bf897809"
    )
    assert inst.status == "completed"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_servicerequest_9(base_settings):
    """No. 9 tests collection for ServiceRequest.
    Test File: servicerequest-example-ventilation.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "servicerequest-example-ventilation.json"
    )
    inst = servicerequest.ServiceRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ServiceRequest" == inst.resource_type

    impl_servicerequest_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ServiceRequest" == data["resourceType"]

    inst2 = servicerequest.ServiceRequest(**data)
    impl_servicerequest_9(inst2)


def impl_servicerequest_10(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2017-03-05")
    assert inst.basedOn[0].display == "Maternity care plan"
    assert inst.basedOn[0].reference == "CarePlan/preg"
    assert inst.code.concept.coding[0].code == "62013009"
    assert inst.code.concept.coding[0].display == "Ambulating patient (procedure)"
    assert inst.code.concept.coding[0].system == "http://snomed.info/sct"
    assert inst.code.concept.text == "Ambulation"
    assert inst.id == "ambulation"
    assert inst.identifier[0].value == "45678"
    assert inst.intent == "order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.reason[0].reference.display == "Blood Pressure"
    assert inst.reason[0].reference.reference == "Observation/blood-pressure"
    assert inst.requester.display == "Dr. Beverly Crusher"
    assert (
        inst.requester.reference == "Practitioner/3ad0687e-f477-468c-afd5-fcc2bf897809"
    )
    assert inst.status == "completed"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_servicerequest_10(base_settings):
    """No. 10 tests collection for ServiceRequest.
    Test File: servicerequest-example-ambulation.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "servicerequest-example-ambulation.json"
    )
    inst = servicerequest.ServiceRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ServiceRequest" == inst.resource_type

    impl_servicerequest_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ServiceRequest" == data["resourceType"]

    inst2 = servicerequest.ServiceRequest(**data)
    impl_servicerequest_10(inst2)
