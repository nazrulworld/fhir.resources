# -*- coding: utf-8 -*-
from datetime import datetime, timezone

from .. import fhirtypes  # noqa: F401
from .. import appointment


def test_Appointment_1(base_settings):
    filename = (
        base_settings["unittest_data_dir"]
        / "appointment-example-request.canonical.json"
    )
    inst = appointment.Appointment.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Appointment" == inst.resource_type
    impl_Appointment_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Appointment" == data["resourceType"]

    inst2 = appointment.Appointment(**data)
    impl_Appointment_1(inst2)


def impl_Appointment_1(inst):
    assert (
        inst.comment
        == "Further expand on the results of the MRI and determine the next actions that may be appropriate."
    )
    assert inst.description == "Discussion on the results of your recent MRI"
    assert inst.id == "examplereq"
    assert (
        inst.identifier[0].system == "http://example.org/sampleappointment-identifier"
    )
    assert inst.identifier[0].value == "123"
    assert inst.minutesDuration == 15
    assert inst.participant[0].actor.display == "Peter James Chalmers"
    assert inst.participant[0].actor.reference == "Patient/example"
    assert inst.participant[0].required == "required"
    assert inst.participant[0].status == "needs-action"
    assert inst.participant[1].required == "required"
    assert inst.participant[1].status == "needs-action"
    assert inst.participant[1].type[0].coding[0].code == "attending"
    assert inst.participant[2].actor.display == "South Wing, second floor"
    assert inst.participant[2].actor.reference == "Location/1"
    assert inst.participant[2].required == "required"
    assert inst.participant[2].status == "accepted"
    assert inst.priority == 5
    assert inst.reason.text == "Clinical Review"
    assert inst.slot[0].reference == "Slot/example"
    assert inst.status == "proposed"
    assert inst.text.div == "<div>Brian MRI results discussion</div>"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "52"
    assert inst.type.coding[0].display == "General Discussion"


def test_Appointment_2(base_settings):
    filename = base_settings["unittest_data_dir"] / "appointment-example.canonical.json"
    inst = appointment.Appointment.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Appointment" == inst.resource_type
    impl_Appointment_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Appointment" == data["resourceType"]

    inst2 = appointment.Appointment(**data)
    impl_Appointment_2(inst2)


def impl_Appointment_2(inst):
    assert (
        inst.comment
        == "Further expand on the results of the MRI and determine the next actions that may be appropriate."
    )
    assert inst.description == "Discussion on the results of your recent MRI"
    assert inst.end == datetime(2013, 12, 10, 11, 00, 00, tzinfo=timezone.utc)
    assert inst.id == "example"
    assert inst.participant[0].actor.display == "Peter James Chalmers"
    assert inst.participant[0].actor.reference == "Patient/example"
    assert inst.participant[0].required == "required"
    assert inst.participant[0].status == "accepted"
    assert inst.participant[1].actor.display == "Dr Adam Careful"
    assert inst.participant[1].actor.reference == "Practitioner/example"
    assert inst.participant[1].required == "required"
    assert inst.participant[1].status == "accepted"
    assert inst.participant[1].type[0].coding[0].code == "attending"
    assert inst.participant[2].actor.display == "South Wing, second floor"
    assert inst.participant[2].actor.reference == "Location/1"
    assert inst.participant[2].required == "required"
    assert inst.participant[2].status == "accepted"
    assert inst.priority == 5
    assert inst.start == datetime(2013, 12, 10, 9, 00, 00, tzinfo=timezone.utc)
    assert inst.status == "booked"
    assert inst.text.div == "<div>Brian MRI results discussion</div>"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "52"
    assert inst.type.coding[0].display == "General Discussion"


def test_Appointment_3(base_settings):
    filename = (
        base_settings["unittest_data_dir"]
        / "appointment-example2doctors.canonical.json"
    )
    inst = appointment.Appointment.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Appointment" == inst.resource_type
    impl_Appointment_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Appointment" == data["resourceType"]

    inst2 = appointment.Appointment(**data)
    impl_Appointment_3(inst2)


def impl_Appointment_3(inst):
    assert (
        inst.comment
        == "Clarify the results of the MRI to ensure context of test was correct"
    )
    assert inst.description == "Discussion about Peter Chalmers MRI results"
    assert inst.end == datetime(2013, 12, 9, 11, 00, 00, tzinfo=timezone.utc)
    assert inst.id == "2docs"
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
    assert inst.start == datetime(2013, 12, 9, 9, 00, 00, tzinfo=timezone.utc)
    assert inst.status == "booked"
    assert inst.text.div == "<div>Brian MRI results discussion</div>"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "52"
    assert inst.type.coding[0].display == "General Discussion"
