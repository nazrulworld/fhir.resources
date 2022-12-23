# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ServiceRequest
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import servicerequest


def impl_servicerequest_1(inst):
    assert inst.asNeededCodeableConcept.text == "as needed to clear mucus"
    assert inst.authoredOn == fhirtypes.DateTime.validate("2017-02-01T17:23:07Z")
    assert inst.basedOn[0].reference == "CarePlan/gpvisit"
    assert inst.code.coding[0].code == "34431008"
    assert inst.code.coding[0].display == "Physiotherapy of chest (regime/therapy)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
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
    assert inst.reasonReference[0].reference == "#cystic-fibrosis"
    assert inst.relevantHistory[0].display == "Author's Signature"
    assert inst.relevantHistory[0].reference == "#signature"
    assert inst.requester.display == "Dr Adam Careful"
    assert inst.requester.reference == "Practitioner/example"
    assert inst.status == "completed"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_servicerequest_1(base_settings):
    """No. 1 tests collection for ServiceRequest.
    Test File: servicerequest-example2.json
    """
    filename = base_settings["unittest_data_dir"] / "servicerequest-example2.json"
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
    assert inst.authoredOn == fhirtypes.DateTime.validate("2017-02-01T17:23:07Z")
    assert inst.code.coding[0].code == "359962006"
    assert inst.code.coding[0].display == "Turning patient in bed (procedure)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
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
    assert inst.reasonReference[0].display == "Patient has a spinal fracture"
    assert inst.requester.display == "Dr Adam Careful"
    assert inst.requester.reference == "Practitioner/example"
    assert inst.status == "active"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_servicerequest_2(base_settings):
    """No. 2 tests collection for ServiceRequest.
    Test File: servicerequest-example3.json
    """
    filename = base_settings["unittest_data_dir"] / "servicerequest-example3.json"
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
    assert inst.code.coding[0].code == "LIPID"
    assert inst.code.coding[0].system == "http://acme.org/tests"
    assert inst.code.text == "Lipid Panel"
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
    assert inst.reasonCode[0].coding[0].code == "V173"
    assert inst.reasonCode[0].coding[0].display == "Fam hx-ischem heart dis"
    assert inst.reasonCode[0].coding[0].system == "http://hl7.org/fhir/sid/icd-9"
    assert inst.requester.reference == "Practitioner/example"
    assert inst.specimen[0].display == "Serum specimen"
    assert inst.specimen[0].reference == "#serum"
    assert inst.status == "active"
    assert inst.subject.reference == "Patient/example"
    assert inst.supportingInfo[0].display == "Fasting status"
    assert inst.supportingInfo[0].reference == "#fasting"
    assert inst.text.status == "generated"


def test_servicerequest_3(base_settings):
    """No. 3 tests collection for ServiceRequest.
    Test File: servicerequest-example-lipid.json
    """
    filename = base_settings["unittest_data_dir"] / "servicerequest-example-lipid.json"
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
    assert inst.authoredOn == fhirtypes.DateTime.validate("2017-03-05")
    assert inst.code.coding[0].code == "76164006"
    assert inst.code.coding[0].display == "Biopsy of colon (procedure)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "Biopsy of colon"
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


def test_servicerequest_4(base_settings):
    """No. 4 tests collection for ServiceRequest.
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

    impl_servicerequest_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ServiceRequest" == data["resourceType"]

    inst2 = servicerequest.ServiceRequest(**data)
    impl_servicerequest_4(inst2)


def impl_servicerequest_5(inst):
    assert inst.code.coding[0].code == "229115003"
    assert inst.code.coding[0].display == "Bench Press (regime/therapy)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
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
    assert inst.patientInstruction == (
        "Start with 30kg 10-15 repetitions for three sets and "
        "increase in increments of 5kg when you feel ready"
    )
    assert inst.status == "active"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_servicerequest_5(base_settings):
    """No. 5 tests collection for ServiceRequest.
    Test File: servicerequest-example4.json
    """
    filename = base_settings["unittest_data_dir"] / "servicerequest-example4.json"
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
    assert inst.authoredOn == fhirtypes.DateTime.validate("2016-08-16")
    assert inst.category[0].coding[0].code == "311401005"
    assert inst.category[0].coding[0].display == "Patient education (procedure)"
    assert inst.category[0].coding[0].system == "http://snomed.info/sct"
    assert inst.category[0].text == "Education"
    assert inst.code.coding[0].code == "48023004"
    assert (
        inst.code.coding[0].display
        == "Breast self-examination technique education (procedure)"
    )
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "Health education - breast examination"
    assert inst.id == "education"
    assert inst.intent == "order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.performer[0].display == "Pamela Educator, RN"
    assert inst.reasonCode[0].text == "early detection of breast mass"
    assert inst.requester.display == "Angela Care, MD"
    assert inst.status == "completed"
    assert inst.subject.display == "Jane Doe"
    assert inst.text.status == "generated"


def test_servicerequest_6(base_settings):
    """No. 6 tests collection for ServiceRequest.
    Test File: servicerequest-example-edu.json
    """
    filename = base_settings["unittest_data_dir"] / "servicerequest-example-edu.json"
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
    assert inst.authoredOn == fhirtypes.DateTime.validate("2018-02-20")
    assert inst.code.coding[0].code == "40617009"
    assert inst.code.coding[0].display == "Artificial respiration (procedure)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "Mechanical Ventilation"
    assert inst.id == "vent"
    assert inst.intent == "order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.orderDetail[0].coding[0].code == "243144002"
    assert (
        inst.orderDetail[0].coding[0].display
        == "Patient triggered inspiratory assistance (procedure)"
    )
    assert inst.orderDetail[0].coding[0].system == "http://snomed.info/sct"
    assert inst.orderDetail[0].text == "IPPB"
    assert inst.orderDetail[1].text == (
        " Initial Settings : Sens: -1 cm H20 Pressure 15 cm H2O "
        "moderate flow:  Monitor VS every 15 minutes x 4 at the start"
        " of mechanical ventilation, then routine for unit OR every 5"
        " hr"
    )
    assert inst.performer[0].display == "Dr Cecil Surgeon"
    assert inst.performer[0].reference == "Practitioner/example"
    assert inst.reasonCode[0].text == "chronic obstructive lung disease (COLD)"
    assert inst.requester.display == "Dr. Beverly Crusher"
    assert (
        inst.requester.reference == "Practitioner/3ad0687e-f477-468c-afd5-fcc2bf897809"
    )
    assert inst.status == "completed"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_servicerequest_7(base_settings):
    """No. 7 tests collection for ServiceRequest.
    Test File: servicerequest-example-ventilation.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "servicerequest-example-ventilation.json"
    )
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
    assert inst.authoredOn == fhirtypes.DateTime.validate("2017-03-05")
    assert inst.basedOn[0].display == "Maternity care plan"
    assert inst.basedOn[0].reference == "CarePlan/preg"
    assert inst.code.coding[0].code == "62013009"
    assert inst.code.coding[0].display == "Ambulating patient (procedure)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "Ambulation"
    assert inst.id == "ambulation"
    assert inst.identifier[0].value == "45678"
    assert inst.intent == "order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.reasonReference[0].display == "Blood Pressure"
    assert inst.reasonReference[0].reference == "Observation/blood-pressure"
    assert inst.requester.display == "Dr. Beverly Crusher"
    assert (
        inst.requester.reference == "Practitioner/3ad0687e-f477-468c-afd5-fcc2bf897809"
    )
    assert inst.status == "completed"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_servicerequest_8(base_settings):
    """No. 8 tests collection for ServiceRequest.
    Test File: servicerequest-example-ambulation.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "servicerequest-example-ambulation.json"
    )
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
    assert inst.authoredOn == fhirtypes.DateTime.validate("2016-09-20")
    assert inst.bodySite[0].coding[0].code == "36701003"
    assert inst.bodySite[0].coding[0].display == "Both knees (body structure)"
    assert inst.bodySite[0].coding[0].system == "http://snomed.info/sct"
    assert inst.bodySite[0].text == "Both knees"
    assert inst.category[0].coding[0].code == "386053000"
    assert inst.category[0].coding[0].display == "Evaluation procedure (procedure)"
    assert inst.category[0].coding[0].system == "http://snomed.info/sct"
    assert inst.category[0].text == "Evaluation"
    assert inst.code.coding[0].code == "710830005"
    assert (
        inst.code.coding[0].display
        == "Assessment of passive range of motion (procedure)"
    )
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "Assessment of passive range of motion"
    assert inst.id == "physical-therapy"
    assert inst.intent == "order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate("2016-09-27")
    assert inst.performer[0].display == "Paul Therapist, PT"
    assert (
        inst.reasonCode[0].text
        == "assessment of mobility limitations due to osteoarthritis"
    )
    assert inst.requester.display == "Ollie Ortho, MD"
    assert inst.status == "completed"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_servicerequest_9(base_settings):
    """No. 9 tests collection for ServiceRequest.
    Test File: servicerequest-example-pt.json
    """
    filename = base_settings["unittest_data_dir"] / "servicerequest-example-pt.json"
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
    assert inst.code.coding[0].code == "24627-2"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == "Chest CT"
    assert inst.id == "di"
    assert inst.intent == "original-order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate(
        "2013-05-08T09:33:27+07:00"
    )
    assert inst.reasonCode[0].text == "Check for metastatic disease"
    assert inst.requester.display == "Dr. Adam Careful"
    assert inst.requester.reference == "Practitioner/example"
    assert inst.status == "active"
    assert inst.subject.reference == "Patient/dicom"
    assert inst.text.status == "generated"


def test_servicerequest_10(base_settings):
    """No. 10 tests collection for ServiceRequest.
    Test File: servicerequest-example-di.json
    """
    filename = base_settings["unittest_data_dir"] / "servicerequest-example-di.json"
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
