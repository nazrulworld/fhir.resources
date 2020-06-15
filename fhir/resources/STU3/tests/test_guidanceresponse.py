# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/GuidanceResponse
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import guidanceresponse


def impl_guidanceresponse_1(inst):
    assert inst.contained[0].id == "outputParameters1"
    assert inst.context.reference == "Encounter/example"
    assert inst.id == "example"
    assert inst.identifier.system == "http://example.org"
    assert inst.identifier.value == "guidanceResponse1"
    assert inst.module.reference == "ServiceDefinition/example"
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate(
        "2017-03-10T16:02:00Z"
    )
    assert inst.outputParameters.reference == "#outputParameters1"
    assert inst.performer.reference == "Device/software"
    assert (
        inst.reasonCodeableConcept.text == "Guideline Appropriate Ordering Assessment"
    )
    assert inst.requestId == "guidanceRequest1"
    assert inst.status == "success"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_guidanceresponse_1(base_settings):
    """No. 1 tests collection for GuidanceResponse.
    Test File: guidanceresponse-example.json
    """
    filename = base_settings["unittest_data_dir"] / "guidanceresponse-example.json"
    inst = guidanceresponse.GuidanceResponse.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "GuidanceResponse" == inst.resource_type

    impl_guidanceresponse_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "GuidanceResponse" == data["resourceType"]

    inst2 = guidanceresponse.GuidanceResponse(**data)
    impl_guidanceresponse_1(inst2)
