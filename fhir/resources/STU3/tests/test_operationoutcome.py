# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/OperationOutcome
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import operationoutcome


def impl_operationoutcome_1(inst):
    assert inst.id == "validationfail"
    assert inst.issue[0].code == "structure"
    assert (
        inst.issue[0].details.text
        == 'Error parsing resource XML (Unknown Content "label"'
    )
    assert inst.issue[0].expression[0] == "Patient.identifier"
    assert inst.issue[0].location[0] == "/f:Patient/f:identifier"
    assert inst.issue[0].severity == "error"
    assert inst.text.status == "generated"


def test_operationoutcome_1(base_settings):
    """No. 1 tests collection for OperationOutcome.
    Test File: operationoutcome-example-validationfail.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "operationoutcome-example-validationfail.json"
    )
    inst = operationoutcome.OperationOutcome.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationOutcome" == inst.resource_type

    impl_operationoutcome_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationOutcome" == data["resourceType"]

    inst2 = operationoutcome.OperationOutcome(**data)
    impl_operationoutcome_1(inst2)


def impl_operationoutcome_2(inst):
    assert inst.id == "break-the-glass"
    assert inst.issue[0].code == "suppressed"
    assert inst.issue[0].details.coding[0].code == "ETREAT"
    assert inst.issue[0].details.coding[0].display == "Emergency Treatment"
    assert inst.issue[0].details.coding[0].system == "http://hl7.org/fhir/v3/ActReason"
    assert inst.issue[0].details.text == (
        "Additional information may be available using the Break-The-" "Glass Protocol"
    )
    assert inst.issue[0].severity == "information"
    assert inst.text.status == "generated"


def test_operationoutcome_2(base_settings):
    """No. 2 tests collection for OperationOutcome.
    Test File: operationoutcome-example-break-the-glass.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "operationoutcome-example-break-the-glass.json"
    )
    inst = operationoutcome.OperationOutcome.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationOutcome" == inst.resource_type

    impl_operationoutcome_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationOutcome" == data["resourceType"]

    inst2 = operationoutcome.OperationOutcome(**data)
    impl_operationoutcome_2(inst2)


def impl_operationoutcome_3(inst):
    assert inst.id == "searchfail"
    assert inst.issue[0].code == "code-invalid"
    assert inst.issue[0].details.text == (
        'The "name" parameter has the modifier "exact" which is '
        "not supported by this server"
    )
    assert inst.issue[0].location[0] == "http.name:exact"
    assert inst.issue[0].severity == "fatal"
    assert inst.text.status == "generated"


def test_operationoutcome_3(base_settings):
    """No. 3 tests collection for OperationOutcome.
    Test File: operationoutcome-example-searchfail.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operationoutcome-example-searchfail.json"
    )
    inst = operationoutcome.OperationOutcome.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationOutcome" == inst.resource_type

    impl_operationoutcome_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationOutcome" == data["resourceType"]

    inst2 = operationoutcome.OperationOutcome(**data)
    impl_operationoutcome_3(inst2)


def impl_operationoutcome_4(inst):
    assert inst.id == "exception"
    assert inst.issue[0].code == "exception"
    assert inst.issue[0].details.text == "SQL Link Communication Error (dbx = 34234)"
    assert inst.issue[0].severity == "error"
    assert inst.text.status == "additional"


def test_operationoutcome_4(base_settings):
    """No. 4 tests collection for OperationOutcome.
    Test File: operationoutcome-example-exception.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operationoutcome-example-exception.json"
    )
    inst = operationoutcome.OperationOutcome.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationOutcome" == inst.resource_type

    impl_operationoutcome_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationOutcome" == data["resourceType"]

    inst2 = operationoutcome.OperationOutcome(**data)
    impl_operationoutcome_4(inst2)


def impl_operationoutcome_5(inst):
    assert inst.id == "101"
    assert inst.issue[0].code == "code-invalid"
    assert (
        inst.issue[0].details.text
        == 'The code "W" is not known and not legal in this context'
    )
    assert (
        inst.issue[0].diagnostics
        == "Acme.Interop.FHIRProcessors.Patient.processGender line 2453"
    )
    assert inst.issue[0].expression[0] == "Person.gender"
    assert inst.issue[0].location[0] == "/f:Person/f:gender"
    assert inst.issue[0].severity == "error"
    assert inst.text.status == "additional"


def test_operationoutcome_5(base_settings):
    """No. 5 tests collection for OperationOutcome.
    Test File: operationoutcome-example.json
    """
    filename = base_settings["unittest_data_dir"] / "operationoutcome-example.json"
    inst = operationoutcome.OperationOutcome.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationOutcome" == inst.resource_type

    impl_operationoutcome_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationOutcome" == data["resourceType"]

    inst2 = operationoutcome.OperationOutcome(**data)
    impl_operationoutcome_5(inst2)


def impl_operationoutcome_6(inst):
    assert inst.id == "allok"
    assert inst.issue[0].code == "informational"
    assert inst.issue[0].details.text == "All OK"
    assert inst.issue[0].severity == "information"
    assert inst.text.status == "additional"


def test_operationoutcome_6(base_settings):
    """No. 6 tests collection for OperationOutcome.
    Test File: operationoutcome-example-allok.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operationoutcome-example-allok.json"
    )
    inst = operationoutcome.OperationOutcome.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationOutcome" == inst.resource_type

    impl_operationoutcome_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationOutcome" == data["resourceType"]

    inst2 = operationoutcome.OperationOutcome(**data)
    impl_operationoutcome_6(inst2)
