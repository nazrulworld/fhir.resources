# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Appointment
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import appointment
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_appointment_1(inst):
    assert inst.appointmentType.coding[0].code == "FOLLOWUP"
    assert (
        inst.appointmentType.coding[0].display
        == "A follow up visit from a previous appointment"
    )
    assert (
        inst.appointmentType.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v2-0276"}
        ).valueUri
    )
    assert inst.basedOn[0].reference == "ServiceRequest/myringotomy"
    assert inst.comment == (
        "Further expand on the results of the MRI and determine the "
        "next actions that may be appropriate."
    )
    assert (
        inst.created
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2013-10-10"}
        ).valueDateTime
    )
    assert inst.description == "Discussion on the results of your recent MRI"
    assert (
        inst.end
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2013-12-10T11:00:00Z"}
        ).valueInstant
    )
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.participant[0].actor.display == "Peter James Chalmers"
    assert inst.participant[0].actor.reference == "Patient/example"
    assert inst.participant[0].required == "required"
    assert inst.participant[0].status == "accepted"
    assert inst.participant[1].actor.display == "Dr Adam Careful"
    assert inst.participant[1].actor.reference == "Practitioner/example"
    assert inst.participant[1].required == "required"
    assert inst.participant[1].status == "accepted"
    assert inst.participant[1].type[0].coding[0].code == "ATND"
    assert (
        inst.participant[1].type[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"}
        ).valueUri
    )
    assert inst.participant[2].actor.display == "South Wing, second floor"
    assert inst.participant[2].actor.reference == "Location/1"
    assert inst.participant[2].required == "required"
    assert inst.participant[2].status == "accepted"
    assert inst.priority == 5
    assert inst.reasonReference[0].display == "Severe burn of left ear"
    assert inst.reasonReference[0].reference == "Condition/example"
    assert inst.serviceCategory[0].coding[0].code == "gp"
    assert inst.serviceCategory[0].coding[0].display == "General Practice"
    assert (
        inst.serviceCategory[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://example.org/service-category"}
        ).valueUri
    )
    assert inst.serviceType[0].coding[0].code == "52"
    assert inst.serviceType[0].coding[0].display == "General Discussion"
    assert inst.specialty[0].coding[0].code == "394814009"
    assert inst.specialty[0].coding[0].display == "General practice"
    assert (
        inst.specialty[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert (
        inst.start
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2013-12-10T09:00:00Z"}
        ).valueInstant
    )
    assert inst.status == "booked"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Brian MRI '
        "results discussion</div>"
    )
    assert inst.text.status == "generated"


def test_appointment_1(base_settings):
    """No. 1 tests collection for Appointment.
    Test File: appointment-example.json
    """
    filename = base_settings["unittest_data_dir"] / "appointment-example.json"
    inst = appointment.Appointment.model_validate_json(filename.read_bytes())
    assert "Appointment" == inst.get_resource_type()

    impl_appointment_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Appointment" == data["resourceType"]

    inst2 = appointment.Appointment(**data)
    impl_appointment_1(inst2)


def impl_appointment_2(inst):
    assert inst.appointmentType.coding[0].code == "WALKIN"
    assert (
        inst.appointmentType.coding[0].display
        == "A previously unscheduled walk-in visit"
    )
    assert (
        inst.appointmentType.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v2-0276"}
        ).valueUri
    )
    assert inst.comment == (
        "Further expand on the results of the MRI and determine the "
        "next actions that may be appropriate."
    )
    assert (
        inst.created
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2015-12-02"}
        ).valueDateTime
    )
    assert inst.description == "Discussion on the results of your recent MRI"
    assert inst.id == "examplereq"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://example.org/sampleappointment-identifier"}
        ).valueUri
    )
    assert inst.identifier[0].value == "123"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.minutesDuration == 15
    assert inst.participant[0].actor.display == "Peter James Chalmers"
    assert inst.participant[0].actor.reference == "Patient/example"
    assert inst.participant[0].required == "required"
    assert inst.participant[0].status == "needs-action"
    assert inst.participant[1].required == "required"
    assert inst.participant[1].status == "needs-action"
    assert inst.participant[1].type[0].coding[0].code == "ATND"
    assert (
        inst.participant[1].type[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"}
        ).valueUri
    )
    assert inst.participant[2].actor.display == "South Wing, second floor"
    assert inst.participant[2].actor.reference == "Location/1"
    assert inst.participant[2].required == "required"
    assert inst.participant[2].status == "accepted"
    assert inst.priority == 5
    assert inst.reasonCode[0].coding[0].code == "413095006"
    assert (
        inst.reasonCode[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.reasonCode[0].text == "Clinical Review"
    assert (
        inst.requestedPeriod[0].end
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2016-06-09"}
        ).valueDateTime
    )
    assert (
        inst.requestedPeriod[0].start
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2016-06-02"}
        ).valueDateTime
    )
    assert inst.serviceCategory[0].coding[0].code == "gp"
    assert inst.serviceCategory[0].coding[0].display == "General Practice"
    assert (
        inst.serviceCategory[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://example.org/service-category"}
        ).valueUri
    )
    assert inst.slot[0].reference == "Slot/example"
    assert inst.specialty[0].coding[0].code == "394814009"
    assert inst.specialty[0].coding[0].display == "General practice"
    assert (
        inst.specialty[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.status == "proposed"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Brian MRI '
        "results discussion</div>"
    )
    assert inst.text.status == "generated"


def test_appointment_2(base_settings):
    """No. 2 tests collection for Appointment.
    Test File: appointment-example-request.json
    """
    filename = base_settings["unittest_data_dir"] / "appointment-example-request.json"
    inst = appointment.Appointment.model_validate_json(filename.read_bytes())
    assert "Appointment" == inst.get_resource_type()

    impl_appointment_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Appointment" == data["resourceType"]

    inst2 = appointment.Appointment(**data)
    impl_appointment_2(inst2)


def impl_appointment_3(inst):
    assert inst.appointmentType.coding[0].code == "WALKIN"
    assert (
        inst.appointmentType.coding[0].display
        == "A previously unscheduled walk-in visit"
    )
    assert (
        inst.appointmentType.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v2-0276"}
        ).valueUri
    )
    assert inst.comment == (
        "Clarify the results of the MRI to ensure context of test was" " correct"
    )
    assert inst.description == "Discussion about Peter Chalmers MRI results"
    assert (
        inst.end
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2013-12-09T11:00:00Z"}
        ).valueInstant
    )
    assert inst.id == "2docs"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.participant[0].actor.display == "Peter James Chalmers"
    assert inst.participant[0].actor.reference == "Patient/example"
    assert inst.participant[0].required == "information-only"
    assert inst.participant[0].status == "accepted"
    assert inst.participant[1].actor.display == "Dr Adam Careful"
    assert inst.participant[1].actor.reference == "Practitioner/example"
    assert inst.participant[1].required == "required"
    assert inst.participant[1].status == "accepted"
    assert inst.participant[2].actor.display == "Luigi Maas"
    assert inst.participant[2].actor.reference == "Practitioner/f202"
    assert inst.participant[2].required == "required"
    assert inst.participant[2].status == "accepted"
    assert inst.participant[3].actor.display == "Phone Call"
    assert inst.participant[3].required == "information-only"
    assert inst.participant[3].status == "accepted"
    assert inst.priority == 5
    assert inst.serviceCategory[0].coding[0].code == "gp"
    assert inst.serviceCategory[0].coding[0].display == "General Practice"
    assert (
        inst.serviceCategory[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://example.org/service-category"}
        ).valueUri
    )
    assert inst.serviceType[0].coding[0].code == "52"
    assert inst.serviceType[0].coding[0].display == "General Discussion"
    assert inst.specialty[0].coding[0].code == "394814009"
    assert inst.specialty[0].coding[0].display == "General practice"
    assert (
        inst.specialty[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert (
        inst.start
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2013-12-09T09:00:00Z"}
        ).valueInstant
    )
    assert inst.status == "booked"
    assert inst.supportingInformation[0].reference == "DiagnosticReport/ultrasound"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Brian MRI '
        "results discussion</div>"
    )
    assert inst.text.status == "generated"


def test_appointment_3(base_settings):
    """No. 3 tests collection for Appointment.
    Test File: appointment-example2doctors.json
    """
    filename = base_settings["unittest_data_dir"] / "appointment-example2doctors.json"
    inst = appointment.Appointment.model_validate_json(filename.read_bytes())
    assert "Appointment" == inst.get_resource_type()

    impl_appointment_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Appointment" == data["resourceType"]

    inst2 = appointment.Appointment(**data)
    impl_appointment_3(inst2)
