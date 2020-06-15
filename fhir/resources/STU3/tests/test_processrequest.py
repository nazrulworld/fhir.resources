# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ProcessRequest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import processrequest


def impl_processrequest_1(inst):
    assert inst.action == "poll"
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.exclude[0] == "Communication"
    assert inst.exclude[1] == "PaymentReconciliation"
    assert inst.id == "1113"
    assert inst.identifier[0].system == "http://happyvalley.com/processrequest"
    assert inst.identifier[0].value == "113"
    assert inst.organization.reference == "Organization/1"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the Poll ProcessRequest</div>"
    )
    assert inst.text.status == "generated"


def test_processrequest_1(base_settings):
    """No. 1 tests collection for ProcessRequest.
    Test File: processrequest-example-poll-exclusive.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "processrequest-example-poll-exclusive.json"
    )
    inst = processrequest.ProcessRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ProcessRequest" == inst.resource_type

    impl_processrequest_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ProcessRequest" == data["resourceType"]

    inst2 = processrequest.ProcessRequest(**data)
    impl_processrequest_1(inst2)


def impl_processrequest_2(inst):
    assert inst.action == "poll"
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.id == "1115"
    assert (
        inst.identifier[0].system == "http://www.phr.com/patient/12345/processrequest"
    )
    assert inst.identifier[0].value == "115"
    assert inst.include[0] == "ExplanationOfBenefit"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the Poll ProcessRequest</div>"
    )
    assert inst.text.status == "generated"


def test_processrequest_2(base_settings):
    """No. 2 tests collection for ProcessRequest.
    Test File: processrequest-example-poll-eob.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "processrequest-example-poll-eob.json"
    )
    inst = processrequest.ProcessRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ProcessRequest" == inst.resource_type

    impl_processrequest_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ProcessRequest" == data["resourceType"]

    inst2 = processrequest.ProcessRequest(**data)
    impl_processrequest_2(inst2)


def impl_processrequest_3(inst):
    assert inst.action == "poll"
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.id == "1111"
    assert inst.identifier[0].system == "http://happyvalley.com/processrequest"
    assert inst.identifier[0].value == "111"
    assert inst.organization.reference == "Organization/1"
    assert inst.provider.identifier.system == "http://npid.org/providerid"
    assert inst.provider.identifier.value == "AF12345"
    assert inst.request.reference == "http://benefitco.com/oralhealthclaim/12345"
    assert inst.status == "active"
    assert inst.target.identifier.system == "http://ninsurers.org/payorid"
    assert inst.target.identifier.value == "WI12345"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the Poll ProcessRequest</div>"
    )
    assert inst.text.status == "generated"


def test_processrequest_3(base_settings):
    """No. 3 tests collection for ProcessRequest.
    Test File: processrequest-example-poll-specific.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "processrequest-example-poll-specific.json"
    )
    inst = processrequest.ProcessRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ProcessRequest" == inst.resource_type

    impl_processrequest_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ProcessRequest" == data["resourceType"]

    inst2 = processrequest.ProcessRequest(**data)
    impl_processrequest_3(inst2)


def impl_processrequest_4(inst):
    assert inst.action == "poll"
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.id == "1112"
    assert inst.identifier[0].system == "http://happyvalley.com/processrequest"
    assert inst.identifier[0].value == "112"
    assert inst.include[0] == "PaymentReconciliation"
    assert inst.organization.reference == "Organization/1"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the Poll ProcessRequest</div>"
    )
    assert inst.text.status == "generated"


def test_processrequest_4(base_settings):
    """No. 4 tests collection for ProcessRequest.
    Test File: processrequest-example-poll-inclusive.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "processrequest-example-poll-inclusive.json"
    )
    inst = processrequest.ProcessRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ProcessRequest" == inst.resource_type

    impl_processrequest_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ProcessRequest" == data["resourceType"]

    inst2 = processrequest.ProcessRequest(**data)
    impl_processrequest_4(inst2)


def impl_processrequest_5(inst):
    assert inst.action == "poll"
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.id == "1114"
    assert inst.identifier[0].system == "http://happyvalley.com/processrequest"
    assert inst.identifier[0].value == "114"
    assert inst.include[0] == "PaymentReconciliation"
    assert inst.organization.reference == "Organization/1"
    assert inst.period.end == fhirtypes.DateTime.validate("2014-08-20")
    assert inst.period.start == fhirtypes.DateTime.validate("2014-08-10")
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the Poll ProcessRequest</div>"
    )
    assert inst.text.status == "generated"


def test_processrequest_5(base_settings):
    """No. 5 tests collection for ProcessRequest.
    Test File: processrequest-example-poll-payrec.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "processrequest-example-poll-payrec.json"
    )
    inst = processrequest.ProcessRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ProcessRequest" == inst.resource_type

    impl_processrequest_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ProcessRequest" == data["resourceType"]

    inst2 = processrequest.ProcessRequest(**data)
    impl_processrequest_5(inst2)


def impl_processrequest_6(inst):
    assert inst.action == "poll"
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.id == "1110"
    assert inst.identifier[0].system == "http://happyvalley.com/processrequest"
    assert inst.identifier[0].value == "110"
    assert inst.organization.reference == "Organization/1"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the Poll ProcessRequest</div>"
    )
    assert inst.text.status == "generated"


def test_processrequest_6(base_settings):
    """No. 6 tests collection for ProcessRequest.
    Test File: processrequest-example.json
    """
    filename = base_settings["unittest_data_dir"] / "processrequest-example.json"
    inst = processrequest.ProcessRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ProcessRequest" == inst.resource_type

    impl_processrequest_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ProcessRequest" == data["resourceType"]

    inst2 = processrequest.ProcessRequest(**data)
    impl_processrequest_6(inst2)


def impl_processrequest_7(inst):
    assert inst.action == "cancel"
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.id == "87654"
    assert inst.identifier[0].system == "http://happyvalley.com/processrequest"
    assert inst.identifier[0].value == "76543"
    assert inst.nullify is False
    assert inst.organization.reference == "Organization/1"
    assert inst.request.reference == "http://BenefitsInc.com/fhir/claim/12345"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the Reversal ProcessRequest</div>"
    )
    assert inst.text.status == "generated"


def test_processrequest_7(base_settings):
    """No. 7 tests collection for ProcessRequest.
    Test File: processrequest-example-reverse.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "processrequest-example-reverse.json"
    )
    inst = processrequest.ProcessRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ProcessRequest" == inst.resource_type

    impl_processrequest_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ProcessRequest" == data["resourceType"]

    inst2 = processrequest.ProcessRequest(**data)
    impl_processrequest_7(inst2)


def impl_processrequest_8(inst):
    assert inst.action == "reprocess"
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.id == "44654"
    assert inst.identifier[0].system == "http://happyvalley.com/processrequest"
    assert inst.identifier[0].value == "44543"
    assert inst.item[0].sequenceLinkId == 1
    assert inst.organization.reference == "Organization/1"
    assert inst.reference == "ABC12345G"
    assert inst.request.reference == "http://BenefitsInc.com/fhir/claim/12345"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the ReProcess ProcessRequest resource.</div>"
    )
    assert inst.text.status == "generated"


def test_processrequest_8(base_settings):
    """No. 8 tests collection for ProcessRequest.
    Test File: processrequest-example-reprocess.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "processrequest-example-reprocess.json"
    )
    inst = processrequest.ProcessRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ProcessRequest" == inst.resource_type

    impl_processrequest_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ProcessRequest" == data["resourceType"]

    inst2 = processrequest.ProcessRequest(**data)
    impl_processrequest_8(inst2)


def impl_processrequest_9(inst):
    assert inst.action == "status"
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.id == "87655"
    assert inst.identifier[0].system == "http://happyvalley.com/processrequest"
    assert inst.identifier[0].value == "1776543"
    assert inst.organization.reference == "Organization/1"
    assert inst.request.reference == "http://happyvalley.com/claim/12345"
    assert inst.response.reference == "http://BenefitsInc.com/fhir/claimresponse/3500"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the Status ProcessRequest</div>"
    )
    assert inst.text.status == "generated"


def test_processrequest_9(base_settings):
    """No. 9 tests collection for ProcessRequest.
    Test File: processrequest-example-status.json
    """
    filename = base_settings["unittest_data_dir"] / "processrequest-example-status.json"
    inst = processrequest.ProcessRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ProcessRequest" == inst.resource_type

    impl_processrequest_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ProcessRequest" == data["resourceType"]

    inst2 = processrequest.ProcessRequest(**data)
    impl_processrequest_9(inst2)
