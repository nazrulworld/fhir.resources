# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ServiceDefinition
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import servicedefinition


def impl_servicedefinition_1(inst):
    assert inst.dataRequirement[0].mustSupport[0] == "gender"
    assert inst.dataRequirement[0].mustSupport[1] == "birthDate"
    assert inst.dataRequirement[0].type == "Patient"
    assert inst.dataRequirement[1].type == "Condition"
    assert inst.dataRequirement[2].type == "MedicationStatement"
    assert inst.date == fhirtypes.DateTime.validate("2016-07-05")
    assert inst.description == (
        "The InfoButton specification defines a mechanism for "
        "retrieving relevant clinical context based a particular set "
        "of search criteria.."
    )
    assert inst.id == "infobutton"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "infobutton"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "InfoButton Module"
    assert inst.topic[0].text == "InfoButton Module"
    assert inst.topic[1].text == "InfoButton"
    assert inst.version == "1.0.0"


def test_servicedefinition_1(base_settings):
    """No. 1 tests collection for ServiceDefinition.
    Test File: servicedefinition-infobutton.json
    """
    filename = base_settings["unittest_data_dir"] / "servicedefinition-infobutton.json"
    inst = servicedefinition.ServiceDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ServiceDefinition" == inst.resource_type

    impl_servicedefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ServiceDefinition" == data["resourceType"]

    inst2 = servicedefinition.ServiceDefinition(**data)
    impl_servicedefinition_1(inst2)


def impl_servicedefinition_2(inst):
    assert inst.date == fhirtypes.DateTime.validate("2015-07-22")
    assert inst.description == (
        "Guideline appropriate ordering is used to assess "
        "appropriateness of an order given a patient, a proposed "
        "order, and a set of clinical indications."
    )
    assert inst.id == "example"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "guildeline-appropriate-ordering"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Guideline Appropriate Ordering Module"
    assert inst.topic[0].text == "Guideline Appropriate Ordering"
    assert inst.topic[1].text == "Appropriate Use Criteria"
    assert inst.version == "1.0.0"


def test_servicedefinition_2(base_settings):
    """No. 2 tests collection for ServiceDefinition.
    Test File: servicedefinition-example.json
    """
    filename = base_settings["unittest_data_dir"] / "servicedefinition-example.json"
    inst = servicedefinition.ServiceDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ServiceDefinition" == inst.resource_type

    impl_servicedefinition_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ServiceDefinition" == data["resourceType"]

    inst2 = servicedefinition.ServiceDefinition(**data)
    impl_servicedefinition_2(inst2)
