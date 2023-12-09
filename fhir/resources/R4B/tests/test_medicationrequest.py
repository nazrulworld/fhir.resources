# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationRequest
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import medicationrequest


def impl_medicationrequest_1(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2015-01-15")
    assert inst.dispenseRequest.expectedSupplyDuration.code == "d"
    assert (
        inst.dispenseRequest.expectedSupplyDuration.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dispenseRequest.expectedSupplyDuration.unit == "days"
    assert float(inst.dispenseRequest.expectedSupplyDuration.value) == float(30)
    assert inst.dispenseRequest.numberOfRepeatsAllowed == 3
    assert inst.dispenseRequest.quantity.code == "mL"
    assert inst.dispenseRequest.quantity.system == "http://unitsofmeasure.org"
    assert inst.dispenseRequest.quantity.unit == "mL"
    assert float(inst.dispenseRequest.quantity.value) == float(30)
    assert inst.dispenseRequest.validityPeriod.end == fhirtypes.DateTime.validate(
        "2016-01-15"
    )
    assert inst.dispenseRequest.validityPeriod.start == fhirtypes.DateTime.validate(
        "2015-01-15"
    )
    assert inst.dosageInstruction[0].additionalInstruction[0].text == "Shake Well"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "ORINHL"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "ea"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        1
    )
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == "Use two sprays twice daily"
    assert inst.dosageInstruction[0].timing.repeat.frequency == 2
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.id == "medrx0326"
    assert inst.identifier[0].system == "http://www.bmc.nl/portal/prescriptions"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345689"
    assert inst.intent == "order"
    assert inst.medicationCodeableConcept.coding[0].code == "746763"
    assert (
        inst.medicationCodeableConcept.coding[0].display
        == "Proventil HFA 90mcg/actuat metered dose inhaler, 200 actuat"
    )
    assert (
        inst.medicationCodeableConcept.coding[0].system
        == "http://www.nlm.nih.gov/research/umls/rxnorm"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.requester.display == "Patrick Pump"
    assert inst.requester.reference == "Practitioner/f007"
    assert inst.status == "on-hold"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.substitution.allowedBoolean is True
    assert inst.substitution.reason.coding[0].code == "FP"
    assert inst.substitution.reason.coding[0].display == "formulary policy"
    assert (
        inst.substitution.reason.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_medicationrequest_1(base_settings):
    """No. 1 tests collection for MedicationRequest.
    Test File: medicationrequest0326.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationrequest0326.json"
    inst = medicationrequest.MedicationRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationRequest" == inst.resource_type

    impl_medicationrequest_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationRequest" == data["resourceType"]

    inst2 = medicationrequest.MedicationRequest(**data)
    impl_medicationrequest_1(inst2)


def impl_medicationrequest_2(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2015-01-15")
    assert inst.contained[0].id == "med0305"
    assert inst.dispenseRequest.expectedSupplyDuration.code == "d"
    assert (
        inst.dispenseRequest.expectedSupplyDuration.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dispenseRequest.expectedSupplyDuration.unit == "days"
    assert float(inst.dispenseRequest.expectedSupplyDuration.value) == float(30)
    assert inst.dispenseRequest.numberOfRepeatsAllowed == 1
    assert inst.dispenseRequest.quantity.code == "mL"
    assert inst.dispenseRequest.quantity.system == "http://unitsofmeasure.org"
    assert inst.dispenseRequest.quantity.unit == "mL"
    assert float(inst.dispenseRequest.quantity.value) == float(10)
    assert inst.dispenseRequest.validityPeriod.end == fhirtypes.DateTime.validate(
        "2016-01-15"
    )
    assert inst.dispenseRequest.validityPeriod.start == fhirtypes.DateTime.validate(
        "2015-01-15"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "OPDROP"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "OPDROP"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        1
    )
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].method.coding[0].code == "421538008"
    assert (
        inst.dosageInstruction[0].method.coding[0].display
        == "Instill - dosing instruction imperative (qualifier value)"
    )
    assert inst.dosageInstruction[0].method.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].route.coding[0].code == "54485002"
    assert (
        inst.dosageInstruction[0].route.coding[0].display
        == "Ophthalmic route (qualifier value)"
    )
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == "Instil one drop in each eye twice daily"
    assert inst.dosageInstruction[0].timing.repeat.frequency == 2
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.encounter.display == "encounter who leads to this prescription"
    assert inst.encounter.reference == "Encounter/f002"
    assert inst.id == "medrx0330"
    assert inst.identifier[0].system == "http://www.bmc.nl/portal/prescriptions"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345689"
    assert inst.intent == "order"
    assert inst.medicationReference.reference == "#med0305"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.requester.display == "Patrick Pump"
    assert inst.requester.reference == "Practitioner/f007"
    assert inst.status == "active"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.substitution.allowedBoolean is False
    assert inst.substitution.reason.coding[0].code == "FP"
    assert inst.substitution.reason.coding[0].display == "formulary policy"
    assert (
        inst.substitution.reason.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_medicationrequest_2(base_settings):
    """No. 2 tests collection for MedicationRequest.
    Test File: medicationrequest0330.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationrequest0330.json"
    inst = medicationrequest.MedicationRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationRequest" == inst.resource_type

    impl_medicationrequest_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationRequest" == data["resourceType"]

    inst2 = medicationrequest.MedicationRequest(**data)
    impl_medicationrequest_2(inst2)


def impl_medicationrequest_3(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2015-01-15")
    assert inst.contained[0].id == "med0309"
    assert inst.dosageInstruction[0].additionalInstruction[0].text == "Take at bedtime"
    assert (
        inst.dosageInstruction[0].asNeededCodeableConcept.coding[0].code == "32914008"
    )
    assert (
        inst.dosageInstruction[0].asNeededCodeableConcept.coding[0].display
        == "Restless Legs"
    )
    assert (
        inst.dosageInstruction[0].asNeededCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseRange.high.code == "TAB"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseRange.high.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseRange.high.unit == "TAB"
    assert float(
        inst.dosageInstruction[0].doseAndRate[0].doseRange.high.value
    ) == float(2)
    assert inst.dosageInstruction[0].doseAndRate[0].doseRange.low.code == "TAB"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseRange.low.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseRange.low.unit == "TAB"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseRange.low.value) == float(
        1
    )
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].route.coding[0].code == "26643006"
    assert inst.dosageInstruction[0].route.coding[0].display == "Oral Route"
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == (
        "Take 1-2 tablets once daily at bedtime as needed for " "restless legs"
    )
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.encounter.display == "encounter who leads to this prescription"
    assert inst.encounter.reference == "Encounter/f001"
    assert inst.id == "medrx0310"
    assert inst.identifier[0].system == "http://www.bmc.nl/portal/prescriptions"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345689"
    assert inst.intent == "order"
    assert inst.medicationReference.reference == "#med0309"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.requester.display == "Patrick Pump"
    assert inst.requester.reference == "Practitioner/f007"
    assert inst.status == "active"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationrequest_3(base_settings):
    """No. 3 tests collection for MedicationRequest.
    Test File: medicationrequest0310.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationrequest0310.json"
    inst = medicationrequest.MedicationRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationRequest" == inst.resource_type

    impl_medicationrequest_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationRequest" == data["resourceType"]

    inst2 = medicationrequest.MedicationRequest(**data)
    impl_medicationrequest_3(inst2)


def impl_medicationrequest_4(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2015-01-15")
    assert inst.contained[0].id == "med0304"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "mg"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "mg"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        6
    )
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].route.coding[0].code == "26643006"
    assert (
        inst.dosageInstruction[0].route.coding[0].display
        == "Oral route (qualifier value)"
    )
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == (
        "6 mg PO daily for remission induction; adjust dosage to "
        "white blood cell (WBC) count.  With hold treatment if WBC is"
        " less than 15,000/µL; resume when WBC is greater than "
        "50,000/µL"
    )
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.id == "medrx0306"
    assert inst.identifier[0].system == "http://www.bmc.nl/portal/prescriptions"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345689"
    assert inst.intent == "order"
    assert inst.medicationReference.display == "Myleran 2mg tablet"
    assert inst.medicationReference.reference == "#med0304"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.reasonCode[0].coding[0].code == "92818009"
    assert inst.reasonCode[0].coding[0].display == "Chronic myeloid Leukemia (disorder)"
    assert inst.reasonCode[0].coding[0].system == "http://snomed.info/sct"
    assert inst.requester.display == "Patrick Pump"
    assert inst.requester.reference == "Practitioner/f007"
    assert inst.status == "active"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationrequest_4(base_settings):
    """No. 4 tests collection for MedicationRequest.
    Test File: medicationrequest0306.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationrequest0306.json"
    inst = medicationrequest.MedicationRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationRequest" == inst.resource_type

    impl_medicationrequest_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationRequest" == data["resourceType"]

    inst2 = medicationrequest.MedicationRequest(**data)
    impl_medicationrequest_4(inst2)


def impl_medicationrequest_5(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2015-01-15")
    assert inst.contained[0].id == "med0308"
    assert inst.dispenseRequest.expectedSupplyDuration.code == "d"
    assert (
        inst.dispenseRequest.expectedSupplyDuration.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dispenseRequest.expectedSupplyDuration.unit == "days"
    assert float(inst.dispenseRequest.expectedSupplyDuration.value) == float(10)
    assert inst.dispenseRequest.quantity.code == "TAB"
    assert (
        inst.dispenseRequest.quantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.dispenseRequest.quantity.unit == "TAB"
    assert float(inst.dispenseRequest.quantity.value) == float(30)
    assert inst.dispenseRequest.validityPeriod.end == fhirtypes.DateTime.validate(
        "2016-01-15"
    )
    assert inst.dispenseRequest.validityPeriod.start == fhirtypes.DateTime.validate(
        "2015-01-15"
    )
    assert (
        inst.dosageInstruction[0].additionalInstruction[0].coding[0].code == "418914006"
    )
    assert inst.dosageInstruction[0].additionalInstruction[0].coding[0].display == (
        "Warning. May cause drowsiness. If affected do not drive or "
        "operate machinery. Avoid alcoholic drink (qualifier value)"
    )
    assert (
        inst.dosageInstruction[0].additionalInstruction[0].coding[0].system
        == "http://snomed.info/sct"
    )
    assert (
        inst.dosageInstruction[0].asNeededCodeableConcept.coding[0].code == "203082005"
    )
    assert (
        inst.dosageInstruction[0].asNeededCodeableConcept.coding[0].display
        == "Fibromyalgia (disorder)"
    )
    assert (
        inst.dosageInstruction[0].asNeededCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "TAB"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "TAB"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        1
    )
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].route.coding[0].code == "26643006"
    assert inst.dosageInstruction[0].route.coding[0].display == "Oral Route"
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert (
        inst.dosageInstruction[0].text == "1 tablet every four hours as needed for pain"
    )
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(4)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "h"
    assert inst.encounter.display == "encounter who leads to this prescription"
    assert inst.encounter.reference == "Encounter/f001"
    assert inst.id == "medrx0307"
    assert inst.identifier[0].system == "http://www.bmc.nl/portal/prescriptions"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345689"
    assert inst.intent == "order"
    assert inst.medicationReference.reference == "#med0308"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.requester.display == "Patrick Pump"
    assert inst.requester.reference == "Practitioner/f007"
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.substitution.allowedBoolean is True
    assert inst.substitution.reason.coding[0].code == "FP"
    assert inst.substitution.reason.coding[0].display == "formulary policy"
    assert (
        inst.substitution.reason.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_medicationrequest_5(base_settings):
    """No. 5 tests collection for MedicationRequest.
    Test File: medicationrequest0307.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationrequest0307.json"
    inst = medicationrequest.MedicationRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationRequest" == inst.resource_type

    impl_medicationrequest_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationRequest" == data["resourceType"]

    inst2 = medicationrequest.MedicationRequest(**data)
    impl_medicationrequest_5(inst2)


def impl_medicationrequest_6(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2015-01-15")
    assert inst.contained[0].id == "med0350"
    assert inst.dispenseRequest.expectedSupplyDuration.code == "d"
    assert (
        inst.dispenseRequest.expectedSupplyDuration.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dispenseRequest.expectedSupplyDuration.unit == "days"
    assert float(inst.dispenseRequest.expectedSupplyDuration.value) == float(30)
    assert inst.dispenseRequest.numberOfRepeatsAllowed == 3
    assert inst.dispenseRequest.quantity.code == "TAB"
    assert (
        inst.dispenseRequest.quantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.dispenseRequest.quantity.unit == "TAB"
    assert float(inst.dispenseRequest.quantity.value) == float(30)
    assert inst.dispenseRequest.validityPeriod.end == fhirtypes.DateTime.validate(
        "2016-01-15"
    )
    assert inst.dispenseRequest.validityPeriod.start == fhirtypes.DateTime.validate(
        "2015-01-15"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "mg"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "mg"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        7
    )
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == "7mg once daily"
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.id == "medrx0331"
    assert inst.identifier[0].system == "http://www.bmc.nl/portal/prescriptions"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345689"
    assert inst.intent == "order"
    assert inst.medicationReference.reference == "#med0350"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.requester.display == "Patrick Pump"
    assert inst.requester.reference == "Practitioner/f007"
    assert inst.status == "active"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.substitution.allowedBoolean is True
    assert inst.substitution.reason.coding[0].code == "FP"
    assert inst.substitution.reason.coding[0].display == "formulary policy"
    assert (
        inst.substitution.reason.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_medicationrequest_6(base_settings):
    """No. 6 tests collection for MedicationRequest.
    Test File: medicationrequest0331.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationrequest0331.json"
    inst = medicationrequest.MedicationRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationRequest" == inst.resource_type

    impl_medicationrequest_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationRequest" == data["resourceType"]

    inst2 = medicationrequest.MedicationRequest(**data)
    impl_medicationrequest_6(inst2)


def impl_medicationrequest_7(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2015-01-15")
    assert inst.dispenseRequest.expectedSupplyDuration.code == "d"
    assert (
        inst.dispenseRequest.expectedSupplyDuration.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dispenseRequest.expectedSupplyDuration.unit == "days"
    assert float(inst.dispenseRequest.expectedSupplyDuration.value) == float(14)
    assert inst.dispenseRequest.quantity.code == "PATCH"
    assert (
        inst.dispenseRequest.quantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.dispenseRequest.quantity.unit == "patch"
    assert float(inst.dispenseRequest.quantity.value) == float(6)
    assert inst.dispenseRequest.validityPeriod.end == fhirtypes.DateTime.validate(
        "2016-01-15"
    )
    assert inst.dispenseRequest.validityPeriod.start == fhirtypes.DateTime.validate(
        "2015-01-15"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "PATCH"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "patch"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        1
    )
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == "apply one patch three times per week"
    assert inst.dosageInstruction[0].timing.repeat.frequency == 3
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "wk"
    assert inst.id == "medrx0327"
    assert inst.identifier[0].system == "http://www.bmc.nl/portal/prescriptions"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345689"
    assert inst.intent == "order"
    assert inst.medicationCodeableConcept.coding[0].code == "333919005"
    assert (
        inst.medicationCodeableConcept.coding[0].display
        == "Fentanyl 25micrograms/hour patch (product)"
    )
    assert inst.medicationCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.requester.display == "Patrick Pump"
    assert inst.requester.reference == "Practitioner/f007"
    assert inst.status == "active"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationrequest_7(base_settings):
    """No. 7 tests collection for MedicationRequest.
    Test File: medicationrequest0327.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationrequest0327.json"
    inst = medicationrequest.MedicationRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationRequest" == inst.resource_type

    impl_medicationrequest_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationRequest" == data["resourceType"]

    inst2 = medicationrequest.MedicationRequest(**data)
    impl_medicationrequest_7(inst2)


def impl_medicationrequest_8(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2015-01-15")
    assert inst.contained[0].id == "med0306"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "mg/kg"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "mg/kg"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        1.8
    )
    assert inst.dosageInstruction[0].doseAndRate[0].rateRatio.denominator.code == "min"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].rateRatio.denominator.system
        == "http://unitsofmeasure.org"
    )
    assert float(
        inst.dosageInstruction[0].doseAndRate[0].rateRatio.denominator.value
    ) == float(20)
    assert inst.dosageInstruction[0].doseAndRate[0].rateRatio.numerator.code == "mg/kg"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].rateRatio.numerator.system
        == "http://unitsofmeasure.org"
    )
    assert float(
        inst.dosageInstruction[0].doseAndRate[0].rateRatio.numerator.value
    ) == float(1.8)
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].maxDosePerLifetime.code == "mg"
    assert (
        inst.dosageInstruction[0].maxDosePerLifetime.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dosageInstruction[0].maxDosePerLifetime.unit == "mg"
    assert float(inst.dosageInstruction[0].maxDosePerLifetime.value) == float(400)
    assert inst.dosageInstruction[0].route.coding[0].code == "255560000"
    assert inst.dosageInstruction[0].route.coding[0].display == "Intravenous"
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == (
        "1.8 mg/kg IV infusion over 20 minutes every 3 weeks for 16 " "cycles"
    )
    assert inst.dosageInstruction[0].timing.repeat.count == 16
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(3)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "wk"
    assert inst.encounter.display == "encounter who leads to this prescription"
    assert inst.encounter.reference == "Encounter/f001"
    assert inst.id == "medrx0316"
    assert inst.identifier[0].system == "http://www.bmc.nl/portal/prescriptions"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345689"
    assert inst.instantiatesUri[0] == (
        "http://www.bccancer.bc.ca/chemotherapy-protocols-"
        "site/Documents/Lymphoma-"
        "Myeloma/ULYBRENTUX%20Protocol_1Jun2017.pdf"
    )
    assert inst.intent == "order"
    assert inst.medicationReference.reference == "#med0306"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.requester.display == "Patrick Pump"
    assert inst.requester.reference == "Practitioner/f007"
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationrequest_8(base_settings):
    """No. 8 tests collection for MedicationRequest.
    Test File: medicationrequest0316.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationrequest0316.json"
    inst = medicationrequest.MedicationRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationRequest" == inst.resource_type

    impl_medicationrequest_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationRequest" == data["resourceType"]

    inst2 = medicationrequest.MedicationRequest(**data)
    impl_medicationrequest_8(inst2)


def impl_medicationrequest_9(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2015-01-15")
    assert inst.dispenseRequest.expectedSupplyDuration.code == "d"
    assert (
        inst.dispenseRequest.expectedSupplyDuration.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dispenseRequest.expectedSupplyDuration.unit == "days"
    assert float(inst.dispenseRequest.expectedSupplyDuration.value) == float(30)
    assert inst.dispenseRequest.numberOfRepeatsAllowed == 6
    assert inst.dispenseRequest.quantity.code == "mL"
    assert inst.dispenseRequest.quantity.system == "http://unitsofmeasure.org"
    assert inst.dispenseRequest.quantity.unit == "mL"
    assert float(inst.dispenseRequest.quantity.value) == float(10)
    assert inst.dispenseRequest.validityPeriod.end == fhirtypes.DateTime.validate(
        "2016-01-15"
    )
    assert inst.dispenseRequest.validityPeriod.start == fhirtypes.DateTime.validate(
        "2015-01-15"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "U"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "U"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        20
    )
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].route.coding[0].code == "263887005"
    assert (
        inst.dosageInstruction[0].route.coding[0].display
        == "Subcutaneous (qualifier value)"
    )
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == "20 Units SC three times daily"
    assert inst.dosageInstruction[0].timing.repeat.frequency == 3
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.id == "medrx0320"
    assert inst.identifier[0].system == "http://www.bmc.nl/portal/prescriptions"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345689"
    assert inst.intent == "order"
    assert inst.medicationCodeableConcept.coding[0].code == "285018"
    assert (
        inst.medicationCodeableConcept.coding[0].display
        == "Lantus 100 unit/ml injectable solution"
    )
    assert (
        inst.medicationCodeableConcept.coding[0].system
        == "http://www.nlm.nih.gov/research/umls/rxnorm"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.reasonCode[0].coding[0].code == "473189005"
    assert (
        inst.reasonCode[0].coding[0].display
        == "On subcutaneous insulin for diabetes mellitus (finding)"
    )
    assert inst.reasonCode[0].coding[0].system == "http://snomed.info/sct"
    assert inst.requester.display == "Patrick Pump"
    assert inst.requester.reference == "Practitioner/f007"
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationrequest_9(base_settings):
    """No. 9 tests collection for MedicationRequest.
    Test File: medicationrequest0320.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationrequest0320.json"
    inst = medicationrequest.MedicationRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationRequest" == inst.resource_type

    impl_medicationrequest_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationRequest" == data["resourceType"]

    inst2 = medicationrequest.MedicationRequest(**data)
    impl_medicationrequest_9(inst2)


def impl_medicationrequest_10(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2015-01-15")
    assert inst.contained[0].id == "med0336"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].rateQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].rateQuantity.unit == "ug/kg/min"
    assert float(inst.dosageInstruction[0].doseAndRate[0].rateQuantity.value) == float(
        4
    )
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].route.coding[0].code == "47625008"
    assert (
        inst.dosageInstruction[0].route.coding[0].display
        == "Intravenous route (qualifier value)"
    )
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == "Dopamine 4mcg/kg/min"
    assert float(inst.dosageInstruction[0].timing.repeat.duration) == float(33.33)
    assert inst.dosageInstruction[0].timing.repeat.durationUnit == "h"
    assert inst.id == "medrx0336"
    assert inst.identifier[0].system == "http://www.bmc.nl/portal/prescriptions"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345689"
    assert inst.intent == "order"
    assert inst.medicationReference.display == "Dopamine 400mg in 500mL D5W"
    assert inst.medicationReference.reference == "#med0336"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.requester.display == "Patrick Pump"
    assert inst.requester.reference == "Practitioner/f007"
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.supportingInformation[0].reference == "Observation/example"
    assert inst.text.status == "generated"


def test_medicationrequest_10(base_settings):
    """No. 10 tests collection for MedicationRequest.
    Test File: medicationrequest0336.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationrequest0336.json"
    inst = medicationrequest.MedicationRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationRequest" == inst.resource_type

    impl_medicationrequest_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationRequest" == data["resourceType"]

    inst2 = medicationrequest.MedicationRequest(**data)
    impl_medicationrequest_10(inst2)
