# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ReferralRequest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import referralrequest


def impl_referralrequest_1(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2014-02-14")
    assert inst.basedOn[0].display == (
        "ProcedureRequest for Myringotomy and insertion of tympanic " "ventilation tube"
    )
    assert inst.context.display == "Beverly Waver's encounter on 2014-02-14"
    assert (
        inst.definition[0].display
        == "Protocol for insertion of tympanic ventilation tube"
    )
    assert inst.description == (
        "In the past 2 years Beverly has had 6 instances of r) sided "
        "Otitis media. She is     falling behind her peers at school,"
        " and displaying some learning difficulties."
    )
    assert inst.groupIdentifier.value == "1234"
    assert inst.id == "example"
    assert inst.identifier[0].system == "http://orionhealth.com/fhir/apps/referralids"
    assert inst.identifier[0].value == "ret4421"
    assert inst.intent == "order"
    assert inst.occurrencePeriod.end == fhirtypes.DateTime.validate("2014-03-14")
    assert inst.priority == "routine"
    assert inst.reasonCode[0].text == "For consideration of Grommets"
    assert inst.recipient[0].display == "Dr Dave"
    assert (
        inst.recipient[0].reference
        == "https://fhir.orionhealth.com/blaze/fhir/Practitioner/76597"
    )
    assert inst.replaces[0].display == "prior ReferralRequest"
    assert inst.requester.agent.display == "Serena Shrink"
    assert (
        inst.requester.agent.reference
        == "https://fhir.orionhealth.com/blaze/fhir/Practitioner/77272"
    )
    assert inst.serviceRequested[0].coding[0].code == "172676009"
    assert (
        inst.serviceRequested[0].coding[0].display
        == "Myringotomy and insertion of tympanic ventilation tube"
    )
    assert inst.serviceRequested[0].coding[0].system == "http://snomed.info/sct"
    assert inst.serviceRequested[0].text == "Insertion of grommets"
    assert inst.specialty.coding[0].code == "ent"
    assert inst.specialty.coding[0].display == "ENT"
    assert (
        inst.specialty.coding[0].system
        == "http://orionhealth.com/fhir/apps/specialties"
    )
    assert inst.status == "active"
    assert inst.subject.display == "Beverly Weaver"
    assert (
        inst.subject.reference
        == "https://fhir.orionhealth.com/blaze/fhir/Patient/77662"
    )
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Referral to Dr '
        "Dave for Beverly weaver to have grommets inserted in her r) "
        "ear</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "103696004"
    assert inst.type.coding[0].display == "Patient referral to specialist"
    assert inst.type.coding[0].system == "http://snomed.info/sct"


def test_referralrequest_1(base_settings):
    """No. 1 tests collection for ReferralRequest.
    Test File: referralrequest-example.json
    """
    filename = base_settings["unittest_data_dir"] / "referralrequest-example.json"
    inst = referralrequest.ReferralRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ReferralRequest" == inst.resource_type

    impl_referralrequest_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ReferralRequest" == data["resourceType"]

    inst2 = referralrequest.ReferralRequest(**data)
    impl_referralrequest_1(inst2)
