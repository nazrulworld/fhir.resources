# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ProcedureRequest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import procedurerequest


def impl_procedurerequest_1(inst):
    assert inst.code.coding[0].code == "LIPID"
    assert inst.code.coding[0].system == "http://acme.org/tests"
    assert inst.code.text == "Lipid Panel"
    assert inst.contained[0].id == "fasting"
    assert inst.contained[1].id == "serum"
    assert inst.context.reference == "Encounter/example"
    assert inst.id == "lipid"
    assert inst.identifier[0].system == "urn:oid:1.3.4.5.6.7"
    assert inst.identifier[0].type.coding[0].code == "PLAC"
    assert (
        inst.identifier[0].type.coding[0].system
        == "http://hl7.org/fhir/identifier-type"
    )
    assert inst.identifier[0].type.text == "Placer"
    assert inst.identifier[0].value == "2345234234234"
    assert inst.intent == "original-order"
    assert inst.note[0].text == "patient is afraid of needles"
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate(
        "2013-05-02T16:16:00-07:00"
    )
    assert inst.performer.reference == "Practitioner/f202"
    assert inst.reasonCode[0].coding[0].code == "V173"
    assert inst.reasonCode[0].coding[0].display == "Fam hx-ischem heart dis"
    assert inst.reasonCode[0].coding[0].system == "http://hl7.org/fhir/sid/icd-9"
    assert inst.requester.agent.reference == "Practitioner/example"
    assert inst.requester.onBehalfOf.reference == "Organization/f001"
    assert inst.specimen[0].display == "Serum specimen"
    assert inst.specimen[0].reference == "#serum"
    assert inst.status == "active"
    assert inst.subject.reference == "Patient/example"
    assert inst.supportingInfo[0].display == "Fasting status"
    assert inst.supportingInfo[0].reference == "#fasting"
    assert inst.text.status == "generated"


def test_procedurerequest_1(base_settings):
    """No. 1 tests collection for ProcedureRequest.
    Test File: procedurerequest-example-lipid.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "procedurerequest-example-lipid.json"
    )
    inst = procedurerequest.ProcedureRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ProcedureRequest" == inst.resource_type

    impl_procedurerequest_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ProcedureRequest" == data["resourceType"]

    inst2 = procedurerequest.ProcedureRequest(**data)
    impl_procedurerequest_1(inst2)


def impl_procedurerequest_2(inst):
    assert inst.code.coding[0].code == "229115003"
    assert inst.code.coding[0].display == "Bench Press (regime/therapy) "
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "benchpress"
    assert inst.intent == "plan"
    assert inst.note[0].text == (
        "Start with 30kg and increase in increments of 5kg when you " "feel ready"
    )
    assert inst.occurrenceTiming.repeat.count == 20
    assert inst.occurrenceTiming.repeat.countMax == 30
    assert inst.occurrenceTiming.repeat.frequency == 3
    assert float(inst.occurrenceTiming.repeat.period) == float(1)
    assert inst.occurrenceTiming.repeat.periodUnit == "wk"
    assert inst.status == "active"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_procedurerequest_2(base_settings):
    """No. 2 tests collection for ProcedureRequest.
    Test File: procedurerequest-example4.json
    """
    filename = base_settings["unittest_data_dir"] / "procedurerequest-example4.json"
    inst = procedurerequest.ProcedureRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ProcedureRequest" == inst.resource_type

    impl_procedurerequest_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ProcedureRequest" == data["resourceType"]

    inst2 = procedurerequest.ProcedureRequest(**data)
    impl_procedurerequest_2(inst2)


def impl_procedurerequest_3(inst):
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
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.performer.display == "Pamela Educator, RN"
    assert inst.reasonCode[0].text == "early detection of breast mass"
    assert inst.requester.agent.display == "Angela Care, MD"
    assert inst.status == "completed"
    assert inst.subject.display == "Jane Doe"
    assert inst.text.status == "generated"


def test_procedurerequest_3(base_settings):
    """No. 3 tests collection for ProcedureRequest.
    Test File: procedurerequest-example-edu.json
    """
    filename = base_settings["unittest_data_dir"] / "procedurerequest-example-edu.json"
    inst = procedurerequest.ProcedureRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ProcedureRequest" == inst.resource_type

    impl_procedurerequest_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ProcedureRequest" == data["resourceType"]

    inst2 = procedurerequest.ProcedureRequest(**data)
    impl_procedurerequest_3(inst2)


def impl_procedurerequest_4(inst):
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
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate("2016-09-27")
    assert inst.performer.display == "Paul Therapist, PT"
    assert (
        inst.reasonCode[0].text
        == "assessment of mobility limitations due to osteoarthritis"
    )
    assert inst.requester.agent.display == "Ollie Ortho, MD"
    assert inst.requester.onBehalfOf.display == "Sawbones Orthopedic Clinic"
    assert inst.status == "completed"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_procedurerequest_4(base_settings):
    """No. 4 tests collection for ProcedureRequest.
    Test File: procedurerequest-example-pt.json
    """
    filename = base_settings["unittest_data_dir"] / "procedurerequest-example-pt.json"
    inst = procedurerequest.ProcedureRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ProcedureRequest" == inst.resource_type

    impl_procedurerequest_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ProcedureRequest" == data["resourceType"]

    inst2 = procedurerequest.ProcedureRequest(**data)
    impl_procedurerequest_4(inst2)


def impl_procedurerequest_5(inst):
    assert inst.code.coding[0].code == "49874-1"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == "ABCB4 gene mutation analysis"
    assert inst.context.reference == "Encounter/example"
    assert inst.id == "og-example1"
    assert inst.intent == "original-order"
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate(
        "2014-05-12T16:16:00-07:00"
    )
    assert inst.performer.reference == "Practitioner/example"
    assert inst.requester.agent.reference == "Practitioner/example"
    assert inst.status == "active"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_procedurerequest_5(base_settings):
    """No. 5 tests collection for ProcedureRequest.
    Test File: procedurerequest-genetics-example-1.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "procedurerequest-genetics-example-1.json"
    )
    inst = procedurerequest.ProcedureRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ProcedureRequest" == inst.resource_type

    impl_procedurerequest_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ProcedureRequest" == data["resourceType"]

    inst2 = procedurerequest.ProcedureRequest(**data)
    impl_procedurerequest_5(inst2)


def impl_procedurerequest_6(inst):
    assert inst.code.coding[0].code == "24627-2"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == "Chest CT"
    assert inst.id == "di"
    assert inst.intent == "original-order"
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate(
        "2013-05-08T09:33:27+07:00"
    )
    assert inst.reasonCode[0].text == "Check for metastatic disease"
    assert inst.requester.agent.display == "Dr. Adam Careful"
    assert inst.requester.agent.reference == "Practitioner/example"
    assert inst.status == "active"
    assert inst.subject.reference == "Patient/dicom"
    assert inst.text.status == "generated"


def test_procedurerequest_6(base_settings):
    """No. 6 tests collection for ProcedureRequest.
    Test File: procedurerequest-example-di.json
    """
    filename = base_settings["unittest_data_dir"] / "procedurerequest-example-di.json"
    inst = procedurerequest.ProcedureRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ProcedureRequest" == inst.resource_type

    impl_procedurerequest_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ProcedureRequest" == data["resourceType"]

    inst2 = procedurerequest.ProcedureRequest(**data)
    impl_procedurerequest_6(inst2)


def impl_procedurerequest_7(inst):
    assert inst.basedOn[0].display == "Original Request"
    assert inst.bodySite[0].coding[0].display == "Right arm"
    assert inst.bodySite[0].text == "Right arm"
    assert inst.code.coding[0].code == "35542-0"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == "Peanut IgG"
    assert inst.definition[0].display == "Protocol for alergies"
    assert inst.id == "subrequest"
    assert inst.intent == "instance-order"
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate(
        "2013-05-08T09:33:27+07:00"
    )
    assert inst.performerType.coding[0].display == "Qualified nurse"
    assert inst.performerType.text == "Nurse"
    assert inst.priority == "routine"
    assert inst.reasonCode[0].text == "Check for Peanut Allergy"
    assert inst.replaces[0].display == "Previous allergy test"
    assert inst.requester.agent.display == "Dr. Adam Careful"
    assert inst.requester.agent.reference == "Practitioner/example"
    assert inst.requisition.value == "A13848392"
    assert inst.status == "active"
    assert inst.subject.reference == "Patient/dicom"
    assert inst.text.status == "generated"


def test_procedurerequest_7(base_settings):
    """No. 7 tests collection for ProcedureRequest.
    Test File: procedurerequest-example-subrequest.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "procedurerequest-example-subrequest.json"
    )
    inst = procedurerequest.ProcedureRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ProcedureRequest" == inst.resource_type

    impl_procedurerequest_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ProcedureRequest" == data["resourceType"]

    inst2 = procedurerequest.ProcedureRequest(**data)
    impl_procedurerequest_7(inst2)


def impl_procedurerequest_8(inst):
    assert inst.asNeededCodeableConcept.text == "as needed to clear mucus"
    assert inst.authoredOn == fhirtypes.DateTime.validate("2017-02-01T17:23:07Z")
    assert inst.basedOn[0].reference == "CarePlan/gpvisit"
    assert inst.code.coding[0].code == "34431008"
    assert inst.code.coding[0].display == "Physiotherapy of chest (regime/therapy) "
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.contained[0].id == "signature"
    assert inst.contained[1].id == "cystic-fibrosis"
    assert inst.id == "physiotherapy"
    assert inst.identifier[0].system == "http://goodhealth.org/placer-ids"
    assert inst.identifier[0].type.coding[0].code == "PLAC"
    assert inst.identifier[0].type.coding[0].display == "Placer Identifier"
    assert (
        inst.identifier[0].type.coding[0].system
        == "http://hl7.org/fhir/identifier-type"
    )
    assert inst.identifier[0].type.text == "Placer"
    assert inst.identifier[0].value == "20170201-0001"
    assert inst.intent == "order"
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
    assert inst.requester.agent.display == "Dr Adam Careful"
    assert inst.requester.agent.reference == "Practitioner/example"
    assert inst.requester.onBehalfOf.display == "Good Health Clinic"
    assert inst.requester.onBehalfOf.reference == "Organization/2"
    assert inst.status == "completed"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_procedurerequest_8(base_settings):
    """No. 8 tests collection for ProcedureRequest.
    Test File: procedurerequest-example2.json
    """
    filename = base_settings["unittest_data_dir"] / "procedurerequest-example2.json"
    inst = procedurerequest.ProcedureRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ProcedureRequest" == inst.resource_type

    impl_procedurerequest_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ProcedureRequest" == data["resourceType"]

    inst2 = procedurerequest.ProcedureRequest(**data)
    impl_procedurerequest_8(inst2)


def impl_procedurerequest_9(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2017-02-01T17:23:07Z")
    assert inst.code.coding[0].code == "359962006"
    assert inst.code.coding[0].display == "Turning patient in bed (procedure)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.doNotPerform is True
    assert inst.id == "do-not-turn"
    assert inst.identifier[0].system == "http://goodhealth.org/placer-ids"
    assert inst.identifier[0].value == "20170201-0002"
    assert inst.intent == "order"
    assert inst.priority == "stat"
    assert inst.reasonReference[0].display == "Patient has a spinal fracture"
    assert inst.requester.agent.display == "Dr Adam Careful"
    assert inst.requester.agent.reference == "Practitioner/example"
    assert inst.status == "active"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_procedurerequest_9(base_settings):
    """No. 9 tests collection for ProcedureRequest.
    Test File: procedurerequest-example3.json
    """
    filename = base_settings["unittest_data_dir"] / "procedurerequest-example3.json"
    inst = procedurerequest.ProcedureRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ProcedureRequest" == inst.resource_type

    impl_procedurerequest_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ProcedureRequest" == data["resourceType"]

    inst2 = procedurerequest.ProcedureRequest(**data)
    impl_procedurerequest_9(inst2)


def impl_procedurerequest_10(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2017-03-05")
    assert inst.basedOn[0].display == "Maternity care plan"
    assert inst.basedOn[0].reference == "CarePlan/preg"
    assert inst.code.coding[0].code == "62013009"
    assert inst.code.coding[0].display == "Ambulating patient (procedure)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "Ambulation"
    assert inst.definition[0].display == "Protocol for hypertension during pregnancy"
    assert inst.id == "ambulation"
    assert inst.identifier[0].value == "45678"
    assert inst.intent == "order"
    assert inst.reasonReference[0].display == "Blood Pressure"
    assert inst.reasonReference[0].reference == "Observation/blood-pressure"
    assert inst.requester.agent.display == "Dr. Beverly Crusher"
    assert (
        inst.requester.agent.reference
        == "Practitioner/3ad0687e-f477-468c-afd5-fcc2bf897809"
    )
    assert inst.status == "completed"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_procedurerequest_10(base_settings):
    """No. 10 tests collection for ProcedureRequest.
    Test File: procedurerequest-example-ambulation.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "procedurerequest-example-ambulation.json"
    )
    inst = procedurerequest.ProcedureRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ProcedureRequest" == inst.resource_type

    impl_procedurerequest_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ProcedureRequest" == data["resourceType"]

    inst2 = procedurerequest.ProcedureRequest(**data)
    impl_procedurerequest_10(inst2)
