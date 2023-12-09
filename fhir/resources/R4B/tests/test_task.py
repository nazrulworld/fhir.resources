# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Task
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import task


def impl_task_1(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2016-10-31T08:25:05+10:00")
    assert inst.basedOn[0].display == "General Wellness Careplan"
    assert inst.businessStatus.text == "test completed and posted"
    assert inst.code.text == "Lipid Panel"
    assert inst.description == (
        "Create order for getting specimen, Set up inhouse testing,  "
        "generate order for any sendouts and submit with specimen"
    )
    assert inst.encounter.display == "Example In-Patient Encounter"
    assert inst.encounter.reference == "Encounter/example"
    assert inst.executionPeriod.end == fhirtypes.DateTime.validate(
        "2016-10-31T18:45:05+10:00"
    )
    assert inst.executionPeriod.start == fhirtypes.DateTime.validate(
        "2016-10-31T08:25:05+10:00"
    )
    assert inst.focus.display == "Lipid Panel Request"
    assert inst.focus.reference == "ServiceRequest/lipid"
    assert inst.for_fhir.display == "Peter James Chalmers"
    assert inst.for_fhir.reference == "Patient/example"
    assert inst.groupIdentifier.system == "http:/goodhealth.org/accession/identifiers"
    assert inst.groupIdentifier.use == "official"
    assert inst.groupIdentifier.value == "G20170201-001"
    assert inst.id == "example6"
    assert inst.identifier[0].system == "http:/goodhealth.org/identifiers"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "20170201-001"
    assert inst.intent == "order"
    assert inst.lastModified == fhirtypes.DateTime.validate("2016-10-31T18:45:05+10:00")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.output[0].type.text == "DiagnosticReport generated"
    assert inst.output[0].valueReference.reference == "DiagnosticReport/lipids"
    assert inst.output[1].type.text == "collected specimen"
    assert inst.output[1].valueReference.reference == "Specimen/101"
    assert inst.owner.display == "Clinical Laboratory @ Acme Hospital"
    assert inst.owner.reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.performerType[0].coding[0].code == "performer"
    assert inst.performerType[0].coding[0].display == "Performer"
    assert (
        inst.performerType[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/task-performer-type"
    )
    assert inst.performerType[0].text == "Performer"
    assert inst.priority == "routine"
    assert inst.reasonCode.text == (
        "The Task.reason should only be included if there is no "
        "Task.focus or if it differs from the reason indicated on the"
        " focus"
    )
    assert inst.requester.display == "Dr Adam Careful"
    assert inst.requester.reference == "Practitioner/example"
    assert inst.restriction.period.end == fhirtypes.DateTime.validate(
        "2016-11-02T09:45:05+10:00"
    )
    assert inst.restriction.repetitions == 1
    assert inst.status == "completed"
    assert inst.text.status == "generated"


def test_task_1(base_settings):
    """No. 1 tests collection for Task.
    Test File: task-example6.json
    """
    filename = base_settings["unittest_data_dir"] / "task-example6.json"
    inst = task.Task.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Task" == inst.resource_type

    impl_task_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Task" == data["resourceType"]

    inst2 = task.Task(**data)
    impl_task_1(inst2)


def impl_task_2(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2018-10-12T08:25:05+10:00")
    assert inst.code.coding[0].code == "poll"
    assert (
        inst.code.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/financialtaskcode"
    )
    assert inst.id == "fm-example2"
    assert inst.identifier[0].system == "http:/happyvalley.com/task"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "20181012-005"
    assert inst.input[0].type.coding[0].code == "include"
    assert (
        inst.input[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/financialtaskinputtype"
    )
    assert inst.input[0].valueCode == "ClaimResponse"
    assert inst.input[1].type.coding[0].code == "period"
    assert (
        inst.input[1].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/financialtaskinputtype"
    )
    assert inst.input[1].valuePeriod.end == fhirtypes.DateTime.validate("2018-10-12")
    assert inst.input[1].valuePeriod.start == fhirtypes.DateTime.validate("2018-10-01")
    assert inst.intent == "order"
    assert inst.lastModified == fhirtypes.DateTime.validate("2018-10-12T08:25:05+10:00")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.owner.identifier.system == "http://nationalinsurers.com/identifiers"
    assert inst.owner.identifier.value == "12345"
    assert inst.priority == "stat"
    assert inst.requester.display == "Happy Valley Clinic"
    assert inst.requester.reference == "Organization/example"
    assert inst.status == "requested"
    assert inst.text.status == "generated"


def test_task_2(base_settings):
    """No. 2 tests collection for Task.
    Test File: task-example-fm-poll.json
    """
    filename = base_settings["unittest_data_dir"] / "task-example-fm-poll.json"
    inst = task.Task.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Task" == inst.resource_type

    impl_task_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Task" == data["resourceType"]

    inst2 = task.Task(**data)
    impl_task_2(inst2)


def impl_task_3(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2016-10-31T08:25:05+10:00")
    assert inst.basedOn[0].display == "General Wellness Careplan"
    assert inst.businessStatus.text == "waiting for specimen"
    assert inst.code.text == "Lipid Panel"
    assert inst.contained[0].id == "signature"
    assert inst.description == (
        "Create order for getting specimen, Set up inhouse testing,  "
        "generate order for any sendouts and submit with specimen"
    )
    assert inst.encounter.display == "Example In-Patient Encounter"
    assert inst.encounter.reference == "Encounter/example"
    assert inst.executionPeriod.start == fhirtypes.DateTime.validate(
        "2016-10-31T08:25:05+10:00"
    )
    assert inst.focus.display == "Lipid Panel Request"
    assert inst.focus.reference == "ServiceRequest/lipid"
    assert inst.for_fhir.display == "Peter James Chalmers"
    assert inst.for_fhir.reference == "Patient/example"
    assert inst.groupIdentifier.system == "http:/goodhealth.org/accession/identifiers"
    assert inst.groupIdentifier.use == "official"
    assert inst.groupIdentifier.value == "G20170201-001"
    assert inst.id == "example1"
    assert inst.identifier[0].system == "http:/goodhealth.org/identifiers"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "20170201-001"
    assert inst.intent == "order"
    assert inst.lastModified == fhirtypes.DateTime.validate("2016-10-31T09:45:05+10:00")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.owner.display == "Clinical Laboratory @ Acme Hospital"
    assert inst.owner.reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.performerType[0].coding[0].code == "performer"
    assert inst.performerType[0].coding[0].display == "Performer"
    assert (
        inst.performerType[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/task-performer-type"
    )
    assert inst.performerType[0].text == "Performer"
    assert inst.priority == "routine"
    assert inst.reasonCode.text == (
        "The Task.reason should only be included if there is no "
        "Task.focus or if it differs from the reason indicated on the"
        " focus"
    )
    assert inst.relevantHistory[0].display == "Author's Signature"
    assert inst.relevantHistory[0].reference == "#signature"
    assert inst.requester.display == "Dr Adam Careful"
    assert inst.requester.reference == "Practitioner/example"
    assert inst.restriction.period.end == fhirtypes.DateTime.validate(
        "2016-11-02T09:45:05+10:00"
    )
    assert inst.restriction.repetitions == 1
    assert inst.status == "in-progress"
    assert inst.text.status == "generated"


def test_task_3(base_settings):
    """No. 3 tests collection for Task.
    Test File: task-example1.json
    """
    filename = base_settings["unittest_data_dir"] / "task-example1.json"
    inst = task.Task.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Task" == inst.resource_type

    impl_task_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Task" == data["resourceType"]

    inst2 = task.Task(**data)
    impl_task_3(inst2)


def impl_task_4(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2018-10-04T08:25:05+10:00")
    assert inst.code.coding[0].code == "reprocess"
    assert (
        inst.code.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/financialtaskcode"
    )
    assert inst.focus.identifier.system == "http://happyvalley.com/claim"
    assert inst.focus.identifier.value == "1501"
    assert inst.id == "fm-example4"
    assert inst.identifier[0].system == "http:/happyvalley.com/task"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "20181012-006"
    assert inst.input[0].type.coding[0].code == "origresponse"
    assert (
        inst.input[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/financialtaskinputtype"
    )
    assert (
        inst.input[0].valueReference.identifier.system
        == "http://nationalinsurers.com/claimresponse"
    )
    assert inst.input[0].valueReference.identifier.value == "CR201810040001234"
    assert inst.input[1].type.coding[0].code == "reference"
    assert (
        inst.input[1].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/financialtaskinputtype"
    )
    assert inst.input[1].valueString == "BR12345"
    assert inst.input[2].type.coding[0].code == "item"
    assert (
        inst.input[2].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/financialtaskinputtype"
    )
    assert inst.input[2].valuePositiveInt == 2
    assert inst.input[3].type.coding[0].code == "item"
    assert (
        inst.input[3].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/financialtaskinputtype"
    )
    assert inst.input[3].valuePositiveInt == 3
    assert inst.intent == "order"
    assert inst.lastModified == fhirtypes.DateTime.validate("2018-10-04T08:25:05+10:00")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.owner.identifier.system == "http://nationalinsurers.com/identifiers"
    assert inst.owner.identifier.value == "12345"
    assert inst.priority == "stat"
    assert inst.requester.display == "Happy Valley Clinic"
    assert inst.requester.reference == "Organization/example"
    assert inst.status == "requested"
    assert inst.text.status == "generated"


def test_task_4(base_settings):
    """No. 4 tests collection for Task.
    Test File: task-example-fm-reprocess.json
    """
    filename = base_settings["unittest_data_dir"] / "task-example-fm-reprocess.json"
    inst = task.Task.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Task" == inst.resource_type

    impl_task_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Task" == data["resourceType"]

    inst2 = task.Task(**data)
    impl_task_4(inst2)


def impl_task_5(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2016-03-10T22:39:32-04:00")
    assert inst.code.text == "Refill Request"
    assert inst.focus.reference == "MedicationRequest/medrx002"
    assert inst.for_fhir.reference == "Patient/f001"
    assert inst.id == "example3"
    assert inst.intent == "order"
    assert inst.lastModified == fhirtypes.DateTime.validate("2016-03-10T22:39:32-04:00")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.owner.reference == "Practitioner/example"
    assert inst.requester.reference == "Patient/example"
    assert inst.status == "draft"
    assert inst.text.status == "generated"


def test_task_5(base_settings):
    """No. 5 tests collection for Task.
    Test File: task-example3.json
    """
    filename = base_settings["unittest_data_dir"] / "task-example3.json"
    inst = task.Task.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Task" == inst.resource_type

    impl_task_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Task" == data["resourceType"]

    inst2 = task.Task(**data)
    impl_task_5(inst2)


def impl_task_6(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2018-10-04T08:25:05+10:00")
    assert inst.code.coding[0].code == "status"
    assert (
        inst.code.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/financialtaskcode"
    )
    assert inst.focus.identifier.system == "http://happyvalley.com/claim"
    assert inst.focus.identifier.value == "1500"
    assert inst.id == "fm-example6"
    assert inst.identifier[0].system == "http:/happyvalley.com/task"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "20181012-001"
    assert inst.identifier[1].system == "http://nationalinsurers.com/identifiers/12345"
    assert inst.identifier[1].use == "official"
    assert inst.identifier[1].value == "123GB5674"
    assert inst.intent == "order"
    assert inst.lastModified == fhirtypes.DateTime.validate("2018-10-04T08:25:05+10:00")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.output[0].type.coding[0].code == "status"
    assert (
        inst.output[0].type.coding[0].system
        == "http://hl7.org/financial-taskoutputtype"
    )
    assert inst.output[0].valueCode == "complete"
    assert inst.owner.identifier.system == "http://nationalinsurers.com/identifiers"
    assert inst.owner.identifier.value == "12345"
    assert inst.priority == "stat"
    assert inst.requester.display == "Happy Valley Clinic"
    assert inst.requester.reference == "Organization/example"
    assert inst.status == "completed"
    assert inst.text.status == "generated"


def test_task_6(base_settings):
    """No. 6 tests collection for Task.
    Test File: task-example-fm-status-resp.json
    """
    filename = base_settings["unittest_data_dir"] / "task-example-fm-status-resp.json"
    inst = task.Task.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Task" == inst.resource_type

    impl_task_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Task" == data["resourceType"]

    inst2 = task.Task(**data)
    impl_task_6(inst2)


def impl_task_7(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2016-10-31T08:45:05+10:00")
    assert inst.businessStatus.text == "waiting for patient"
    assert inst.code.text == "Specimen Collection"
    assert inst.encounter.display == "Example In-Patient Encounter"
    assert inst.encounter.reference == "Encounter/example"
    assert inst.executionPeriod.start == fhirtypes.DateTime.validate(
        "2016-10-31T08:45:05+10:00"
    )
    assert inst.focus.display == "BloodDraw ServiceRequest"
    assert inst.for_fhir.display == "Peter James Chalmers"
    assert inst.for_fhir.reference == "Patient/example"
    assert inst.groupIdentifier.system == "http:/goodhealth.org/accession/identifiers"
    assert inst.groupIdentifier.use == "official"
    assert inst.groupIdentifier.value == "G20170201-001"
    assert inst.id == "example2"
    assert inst.identifier[0].system == "http:/goodhealth.org/identifiers"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "20170201-002"
    assert inst.intent == "filler-order"
    assert inst.lastModified == fhirtypes.DateTime.validate("2016-10-31T09:45:05+10:00")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.owner.display == "Clinical Laboratory @ Acme Hospital"
    assert inst.owner.reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.partOf[0].display == "Lipid Panel"
    assert inst.partOf[0].reference == "Task/example1"
    assert inst.performerType[0].coding[0].code == "performer"
    assert inst.performerType[0].coding[0].display == "Performer"
    assert (
        inst.performerType[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/task-performer-type"
    )
    assert inst.performerType[0].text == "Performer"
    assert inst.priority == "routine"
    assert inst.requester.display == "Clinical Laboratory @ Acme Hospital"
    assert (
        inst.requester.reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    )
    assert inst.restriction.period.end == fhirtypes.DateTime.validate(
        "2016-11-01T09:45:05+10:00"
    )
    assert inst.restriction.repetitions == 1
    assert inst.status == "accepted"
    assert inst.text.status == "generated"


def test_task_7(base_settings):
    """No. 7 tests collection for Task.
    Test File: task-example2.json
    """
    filename = base_settings["unittest_data_dir"] / "task-example2.json"
    inst = task.Task.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Task" == inst.resource_type

    impl_task_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Task" == data["resourceType"]

    inst2 = task.Task(**data)
    impl_task_7(inst2)


def impl_task_8(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2018-10-04T08:25:05+10:00")
    assert inst.code.coding[0].code == "release"
    assert (
        inst.code.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/financialtaskcode"
    )
    assert inst.focus.identifier.system == "http://happyvalley.com/claim"
    assert inst.focus.identifier.value == "1501"
    assert inst.id == "fm-example3"
    assert inst.identifier[0].system == "http:/happyvalley.com/task"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "20181012-001"
    assert inst.input[0].type.coding[0].code == "origresponse"
    assert (
        inst.input[0].type.coding[0].system == "http://hl7.org/financial-taskinputtype"
    )
    assert (
        inst.input[0].valueReference.identifier.system
        == "http://nationalinsurers.com/claimresponse"
    )
    assert inst.input[0].valueReference.identifier.value == "CR201810040001234"
    assert inst.intent == "order"
    assert inst.lastModified == fhirtypes.DateTime.validate("2018-10-04T08:25:05+10:00")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.owner.identifier.system == "http://nationalinsurers.com/identifiers"
    assert inst.owner.identifier.value == "12345"
    assert inst.priority == "stat"
    assert inst.requester.display == "Happy Valley Clinic"
    assert inst.requester.reference == "Organization/example"
    assert inst.status == "requested"
    assert inst.text.status == "generated"


def test_task_8(base_settings):
    """No. 8 tests collection for Task.
    Test File: task-example-fm-release.json
    """
    filename = base_settings["unittest_data_dir"] / "task-example-fm-release.json"
    inst = task.Task.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Task" == inst.resource_type

    impl_task_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Task" == data["resourceType"]

    inst2 = task.Task(**data)
    impl_task_8(inst2)


def impl_task_9(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2018-10-04T08:25:05+10:00")
    assert inst.code.coding[0].code == "cancel"
    assert (
        inst.code.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/financialtaskcode"
    )
    assert inst.focus.identifier.system == "http://happyvalley.com/claim"
    assert inst.focus.identifier.value == "1500"
    assert inst.id == "fm-example1"
    assert inst.identifier[0].system == "http:/happyvalley.com/task"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "20181012-001"
    assert inst.intent == "order"
    assert inst.lastModified == fhirtypes.DateTime.validate("2018-10-04T08:25:05+10:00")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.owner.identifier.system == "http://nationalinsurers.com/identifiers"
    assert inst.owner.identifier.value == "12345"
    assert inst.priority == "stat"
    assert inst.requester.display == "Happy Valley Clinic"
    assert inst.requester.reference == "Organization/example"
    assert inst.status == "requested"
    assert inst.text.status == "generated"


def test_task_9(base_settings):
    """No. 9 tests collection for Task.
    Test File: task-example-fm-cancel.json
    """
    filename = base_settings["unittest_data_dir"] / "task-example-fm-cancel.json"
    inst = task.Task.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Task" == inst.resource_type

    impl_task_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Task" == data["resourceType"]

    inst2 = task.Task(**data)
    impl_task_9(inst2)


def impl_task_10(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2016-10-31T08:25:05+10:00")
    assert inst.basedOn[0].display == "General Wellness Careplan"
    assert inst.businessStatus.text == "specimen received, test in progress"
    assert inst.code.text == "Lipid Panel"
    assert inst.description == (
        "Create order for getting specimen, Set up inhouse testing,  "
        "generate order for any sendouts and submit with specimen"
    )
    assert inst.encounter.display == "Example In-Patient Encounter"
    assert inst.encounter.reference == "Encounter/example"
    assert inst.executionPeriod.start == fhirtypes.DateTime.validate(
        "2016-10-31T08:25:05+10:00"
    )
    assert inst.focus.display == "Lipid Panel Request"
    assert inst.focus.reference == "ServiceRequest/lipid"
    assert inst.for_fhir.display == "Peter James Chalmers"
    assert inst.for_fhir.reference == "Patient/example"
    assert inst.groupIdentifier.system == "http:/goodhealth.org/accession/identifiers"
    assert inst.groupIdentifier.use == "official"
    assert inst.groupIdentifier.value == "G20170201-001"
    assert inst.id == "example5"
    assert inst.identifier[0].system == "http:/goodhealth.org/identifiers"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "20170201-001"
    assert inst.intent == "order"
    assert inst.lastModified == fhirtypes.DateTime.validate("2016-10-31T16:45:05+10:00")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.output[0].type.text == "collected specimen"
    assert inst.output[0].valueReference.reference == "Specimen/101"
    assert inst.owner.display == "Clinical Laboratory @ Acme Hospital"
    assert inst.owner.reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.performerType[0].coding[0].code == "performer"
    assert inst.performerType[0].coding[0].display == "Performer"
    assert (
        inst.performerType[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/task-performer-type"
    )
    assert inst.performerType[0].text == "Performer"
    assert inst.priority == "routine"
    assert inst.reasonCode.text == (
        "The Task.reason should only be included if there is no "
        "Task.focus or if it differs from the reason indicated on the"
        " focus"
    )
    assert inst.requester.display == "Dr Adam Careful"
    assert inst.requester.reference == "Practitioner/example"
    assert inst.restriction.period.end == fhirtypes.DateTime.validate(
        "2016-11-02T09:45:05+10:00"
    )
    assert inst.restriction.repetitions == 1
    assert inst.status == "in-progress"
    assert inst.text.status == "generated"


def test_task_10(base_settings):
    """No. 10 tests collection for Task.
    Test File: task-example5.json
    """
    filename = base_settings["unittest_data_dir"] / "task-example5.json"
    inst = task.Task.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Task" == inst.resource_type

    impl_task_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Task" == data["resourceType"]

    inst2 = task.Task(**data)
    impl_task_10(inst2)
