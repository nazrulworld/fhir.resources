# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductAuthorization
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import medicinalproductauthorization


def impl_medicinalproductauthorization_1(inst):
    assert inst.country[0].coding[0].code == "EU"
    assert inst.country[0].coding[0].system == "http://ema.europa.eu/example/country"
    assert inst.dataExclusivityPeriod.end == fhirtypes.DateTime.validate(
        "2020-08-15T11:15:33+10:00"
    )
    assert inst.dataExclusivityPeriod.start == fhirtypes.DateTime.validate(
        "2010-08-15T11:15:33+10:00"
    )
    assert inst.dateOfFirstAuthorization == fhirtypes.DateTime.validate(
        "2010-08-15T11:15:33+10:00"
    )
    assert inst.holder.reference == "Organization/example"
    assert inst.id == "example"
    assert (
        inst.identifier[0].system
        == "http://ema.europa.eu/example/marketingAuthorisationNumber"
    )
    assert inst.identifier[0].value == "EU/1/11/999/001"
    assert inst.internationalBirthDate == fhirtypes.DateTime.validate(
        "2010-08-15T11:15:33+10:00"
    )
    assert inst.jurisdictionalAuthorization[0].country.coding[0].code == "NO"
    assert (
        inst.jurisdictionalAuthorization[0].country.coding[0].system
        == "http://ema.europa.eu/example/countryCode"
    )
    assert inst.jurisdictionalAuthorization[0].id == "1"
    assert (
        inst.jurisdictionalAuthorization[0].identifier[0].system
        == "http://ema.europa.eu/example/marketingauthorisationnumber"
    )
    assert inst.jurisdictionalAuthorization[0].identifier[0].value == "123-456-789"
    assert inst.jurisdictionalAuthorization[1].country.coding[0].code == "NO"
    assert (
        inst.jurisdictionalAuthorization[1].country.coding[0].system
        == "http://ema.europa.eu/example/countryCode"
    )
    assert inst.jurisdictionalAuthorization[1].id == "2"
    assert (
        inst.jurisdictionalAuthorization[1].identifier[0].system
        == "http://ema.europa.eu/example/marketingauthorisationnumber"
    )
    assert inst.jurisdictionalAuthorization[1].identifier[0].value == "123-456-123"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.procedure.application[0].dateDateTime == fhirtypes.DateTime.validate(
        "2015-08-01T11:15:33+10:00"
    )
    assert (
        inst.procedure.application[0].identifier.system
        == "http://ema.europa.eu/example/applicationidentifier-number"
    )
    assert inst.procedure.application[0].identifier.value == "IA38G"
    assert (
        inst.procedure.application[0].type.coding[0].code
        == "GroupTypeIAVariationNotification"
    )
    assert inst.procedure.application[0].type.coding[0].system == (
        "http://ema.europa.eu/example/marketingAuthorisationApplicati" "onType"
    )
    assert inst.procedure.datePeriod.end == fhirtypes.DateTime.validate(
        "2015-08-21T11:15:33+10:00"
    )
    assert inst.procedure.datePeriod.start == fhirtypes.DateTime.validate(
        "2015-08-02T11:15:33+10:00"
    )
    assert (
        inst.procedure.identifier.system
        == "http://ema.europa.eu/example/procedureidentifier-number"
    )
    assert inst.procedure.identifier.value == "EMEA/H/C/009999/IA/0099/G"
    assert inst.procedure.type.coding[0].code == "VariationTypeIA"
    assert inst.procedure.type.coding[0].system == (
        "http://ema.europa.eu/example/marketingAuthorisationProcedure" "Type"
    )
    assert inst.regulator.reference == "Organization/example"
    assert inst.status.coding[0].code == "active"
    assert (
        inst.status.coding[0].system
        == "http://ema.europa.eu/example/authorisationstatus"
    )
    assert inst.statusDate == fhirtypes.DateTime.validate("2015-01-14T11:15:33+10:00")
    assert inst.text.status == "generated"
    assert inst.validityPeriod.end == fhirtypes.DateTime.validate(
        "2020-05-20T11:15:33+10:00"
    )
    assert inst.validityPeriod.start == fhirtypes.DateTime.validate(
        "2015-08-16T11:15:33+10:00"
    )


def test_medicinalproductauthorization_1(base_settings):
    """No. 1 tests collection for MedicinalProductAuthorization.
    Test File: medicinalproductauthorization-example.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "medicinalproductauthorization-example.json"
    )
    inst = medicinalproductauthorization.MedicinalProductAuthorization.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicinalProductAuthorization" == inst.resource_type

    impl_medicinalproductauthorization_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicinalProductAuthorization" == data["resourceType"]

    inst2 = medicinalproductauthorization.MedicinalProductAuthorization(**data)
    impl_medicinalproductauthorization_1(inst2)
