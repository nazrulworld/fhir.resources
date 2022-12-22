# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/RegulatedAuthorization
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import regulatedauthorization


def impl_regulatedauthorization_1(inst):
    assert inst.holder.display == "EquiliDrugCo Holdings Inc."
    assert inst.holder.reference == "Organization/EqlidrugCo"
    assert inst.id == "basic-drug-auth"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.regulator.display == "FDA"
    assert inst.regulator.reference == "Organization/FDA"
    assert inst.status.coding[0].code == "active"
    assert inst.statusDate == fhirtypes.DateTime.validate("2016-01-01")
    assert inst.subject[0].reference == "MedicinalProductDefinition/equilidem"
    assert inst.text.status == "generated"
    assert inst.type.text == "Regulatory Drug Marketing Approval"


def test_regulatedauthorization_1(base_settings):
    """No. 1 tests collection for RegulatedAuthorization.
    Test File: regulatedauthorization-example-basic-drug-auth.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "regulatedauthorization-example-basic-drug-auth.json"
    )
    inst = regulatedauthorization.RegulatedAuthorization.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "RegulatedAuthorization" == inst.resource_type

    impl_regulatedauthorization_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "RegulatedAuthorization" == data["resourceType"]

    inst2 = regulatedauthorization.RegulatedAuthorization(**data)
    impl_regulatedauthorization_1(inst2)


def impl_regulatedauthorization_2(inst):
    assert inst.case.application[0].dateDateTime == fhirtypes.DateTime.validate(
        "2015-08-01"
    )
    assert (
        inst.case.application[0].identifier.system
        == "http://ema.europa.eu/example/applicationidentifier-number"
    )
    assert inst.case.application[0].identifier.value == "IA38G"
    assert (
        inst.case.application[0].type.coding[0].code
        == "GroupTypeIAVariationNotification"
    )
    assert inst.case.application[0].type.coding[0].system == (
        "http://ema.europa.eu/example/marketingAuthorisationApplicati" "onType"
    )
    assert inst.case.application[1].dateDateTime == fhirtypes.DateTime.validate(
        "2014-09-01"
    )
    assert (
        inst.case.application[1].identifier.system
        == "http://ema.europa.eu/example/applicationidentifier-number"
    )
    assert inst.case.application[1].identifier.value == "IA38F"
    assert (
        inst.case.application[1].type.coding[0].code
        == "GroupTypeIAVariationNotification"
    )
    assert inst.case.application[1].type.coding[0].system == (
        "http://ema.europa.eu/example/marketingAuthorisationApplicati" "onType"
    )
    assert inst.case.datePeriod.end == fhirtypes.DateTime.validate("2015-08-21")
    assert inst.case.datePeriod.start == fhirtypes.DateTime.validate("2014-09-02")
    assert (
        inst.case.identifier.system
        == "http://ema.europa.eu/example/procedureidentifier-number"
    )
    assert inst.case.identifier.value == "EMEA/H/C/009999/IA/0099/G"
    assert inst.case.type.coding[0].code == "VariationTypeIA"
    assert inst.case.type.coding[0].system == (
        "http://ema.europa.eu/example/marketingAuthorisationProcedure" "Type"
    )
    assert inst.holder.reference == "Organization/example"
    assert inst.id == "example"
    assert (
        inst.identifier[0].system
        == "http://ema.europa.eu/example/marketingAuthorisationNumber"
    )
    assert inst.identifier[0].value == "EU/1/11/999/001"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.region[0].coding[0].code == "EU"
    assert inst.region[0].coding[0].system == "http://ema.europa.eu/example/country"
    assert inst.regulator.reference == "Organization/example"
    assert inst.status.coding[0].code == "active"
    assert (
        inst.status.coding[0].system
        == "http://ema.europa.eu/example/authorisationstatus"
    )
    assert inst.statusDate == fhirtypes.DateTime.validate("2015-01-14")
    assert inst.text.status == "generated"
    assert inst.validityPeriod.end == fhirtypes.DateTime.validate("2020-05-20")
    assert inst.validityPeriod.start == fhirtypes.DateTime.validate("2014-09-03")


def test_regulatedauthorization_2(base_settings):
    """No. 2 tests collection for RegulatedAuthorization.
    Test File: regulatedauthorization-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "regulatedauthorization-example.json"
    )
    inst = regulatedauthorization.RegulatedAuthorization.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "RegulatedAuthorization" == inst.resource_type

    impl_regulatedauthorization_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "RegulatedAuthorization" == data["resourceType"]

    inst2 = regulatedauthorization.RegulatedAuthorization(**data)
    impl_regulatedauthorization_2(inst2)
