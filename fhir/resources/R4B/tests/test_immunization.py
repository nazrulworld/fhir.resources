# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Immunization
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import immunization
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_immunization_1(inst):
    assert inst.doseQuantity.code == "mg"
    assert (
        inst.doseQuantity.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert float(inst.doseQuantity.value) == float(5)
    assert inst.education[0].documentType == "253088698300010311120702"
    assert (
        inst.education[0].presentationDate
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2013-01-10"}
        ).valueDateTime
    )
    assert (
        inst.education[0].publicationDate
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2012-07-02"}
        ).valueDateTime
    )
    assert inst.encounter.reference == "Encounter/example"
    assert (
        inst.expirationDate
        == ExternalValidatorModel.model_validate({"valueDate": "2015-02-15"}).valueDate
    )
    assert inst.fundingSource.coding[0].code == "private"
    assert (
        inst.fundingSource.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/immunization-funding-source"
            }
        ).valueUri
    )
    assert inst.id == "example"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier[0].value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"
    assert inst.isSubpotent is True
    assert inst.location.reference == "Location/1"
    assert inst.lotNumber == "AAJN11K"
    assert inst.manufacturer.reference == "Organization/hl7"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.note[0].text == "Notes on adminstration of vaccine"
    assert (
        inst.occurrenceDateTime
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2013-01-10"}
        ).valueDateTime
    )
    assert inst.patient.reference == "Patient/example"
    assert inst.performer[0].actor.reference == "Practitioner/example"
    assert inst.performer[0].function.coding[0].code == "OP"
    assert (
        inst.performer[0].function.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v2-0443"}
        ).valueUri
    )
    assert inst.performer[1].actor.reference == "Practitioner/example"
    assert inst.performer[1].function.coding[0].code == "AP"
    assert (
        inst.performer[1].function.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v2-0443"}
        ).valueUri
    )
    assert inst.primarySource is True
    assert inst.programEligibility[0].coding[0].code == "ineligible"
    assert (
        inst.programEligibility[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/immunization-program-eligibility"
            }
        ).valueUri
    )
    assert inst.reasonCode[0].coding[0].code == "429060002"
    assert (
        inst.reasonCode[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.route.coding[0].code == "IM"
    assert inst.route.coding[0].display == "Injection, intramuscular"
    assert (
        inst.route.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministration"
            }
        ).valueUri
    )
    assert inst.site.coding[0].code == "LA"
    assert inst.site.coding[0].display == "left arm"
    assert (
        inst.site.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActSite"}
        ).valueUri
    )
    assert inst.status == "completed"
    assert inst.text.status == "generated"
    assert inst.vaccineCode.coding[0].code == "FLUVAX"
    assert (
        inst.vaccineCode.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:oid:1.2.36.1.2001.1005.17"}
        ).valueUri
    )
    assert inst.vaccineCode.text == "Fluvax (Influenza)"


def test_immunization_1(base_settings):
    """No. 1 tests collection for Immunization.
    Test File: immunization-example.json
    """
    filename = base_settings["unittest_data_dir"] / "immunization-example.json"
    inst = immunization.Immunization.model_validate_json(filename.read_bytes())
    assert "Immunization" == inst.get_resource_type()

    impl_immunization_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Immunization" == data["resourceType"]

    inst2 = immunization.Immunization(**data)
    impl_immunization_1(inst2)


def impl_immunization_2(inst):
    assert inst.id == "historical"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier[0].value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"
    assert inst.location.reference == "Location/1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.note[0].text == "Notes on adminstration of a historical vaccine"
    assert inst.occurrenceString == "January 2012"
    assert inst.patient.reference == "Patient/example"
    assert inst.primarySource is False
    assert inst.reportOrigin.coding[0].code == "record"
    assert (
        inst.reportOrigin.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/immunization-origin"}
        ).valueUri
    )
    assert inst.reportOrigin.text == "Written Record"
    assert inst.status == "completed"
    assert inst.text.status == "generated"
    assert inst.vaccineCode.coding[0].code == "GNFLU"
    assert (
        inst.vaccineCode.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:oid:1.2.36.1.2001.1005.17"}
        ).valueUri
    )
    assert inst.vaccineCode.text == "Influenza"


def test_immunization_2(base_settings):
    """No. 2 tests collection for Immunization.
    Test File: immunization-example-historical.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "immunization-example-historical.json"
    )
    inst = immunization.Immunization.model_validate_json(filename.read_bytes())
    assert "Immunization" == inst.get_resource_type()

    impl_immunization_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Immunization" == data["resourceType"]

    inst2 = immunization.Immunization(**data)
    impl_immunization_2(inst2)


def impl_immunization_3(inst):
    assert inst.doseQuantity.code == "mg"
    assert (
        inst.doseQuantity.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert float(inst.doseQuantity.value) == float(5)
    assert inst.encounter.reference == "Encounter/example"
    assert (
        inst.expirationDate
        == ExternalValidatorModel.model_validate({"valueDate": "2018-12-15"}).valueDate
    )
    assert inst.fundingSource.coding[0].code == "private"
    assert (
        inst.fundingSource.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/immunization-funding-source"
            }
        ).valueUri
    )
    assert inst.id == "protocol"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier[0].value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"
    assert inst.isSubpotent is False
    assert inst.location.reference == "Location/1"
    assert inst.lotNumber == "PT123F"
    assert inst.manufacturer.reference == "Organization/hl7"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert (
        inst.occurrenceDateTime
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2018-06-18"}
        ).valueDateTime
    )
    assert inst.patient.reference == "Patient/example"
    assert inst.performer[0].actor.reference == "Practitioner/example"
    assert inst.performer[0].function.coding[0].code == "OP"
    assert (
        inst.performer[0].function.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v2-0443"}
        ).valueUri
    )
    assert inst.performer[1].actor.reference == "Practitioner/example"
    assert inst.performer[1].function.coding[0].code == "AP"
    assert (
        inst.performer[1].function.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v2-0443"}
        ).valueUri
    )
    assert inst.primarySource is True
    assert inst.programEligibility[0].coding[0].code == "ineligible"
    assert (
        inst.programEligibility[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/immunization-program-eligibility"
            }
        ).valueUri
    )
    assert inst.protocolApplied[0].doseNumberPositiveInt == 1
    assert inst.protocolApplied[0].series == "2-dose"
    assert inst.protocolApplied[0].targetDisease[0].coding[0].code == "40468003"
    assert (
        inst.protocolApplied[0].targetDisease[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.protocolApplied[1].doseNumberPositiveInt == 2
    assert inst.protocolApplied[1].series == "3-dose"
    assert inst.protocolApplied[1].targetDisease[0].coding[0].code == "66071002"
    assert (
        inst.protocolApplied[1].targetDisease[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.route.coding[0].code == "IM"
    assert inst.route.coding[0].display == "Injection, intramuscular"
    assert (
        inst.route.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministration"
            }
        ).valueUri
    )
    assert inst.site.coding[0].code == "LA"
    assert inst.site.coding[0].display == "left arm"
    assert (
        inst.site.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActSite"}
        ).valueUri
    )
    assert inst.status == "completed"
    assert inst.text.status == "generated"
    assert inst.vaccineCode.coding[0].code == "104"
    assert (
        inst.vaccineCode.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/sid/cvx"}
        ).valueUri
    )
    assert inst.vaccineCode.text == "Twinrix (HepA/HepB)"


def test_immunization_3(base_settings):
    """No. 3 tests collection for Immunization.
    Test File: immunization-example-protocol.json
    """
    filename = base_settings["unittest_data_dir"] / "immunization-example-protocol.json"
    inst = immunization.Immunization.model_validate_json(filename.read_bytes())
    assert "Immunization" == inst.get_resource_type()

    impl_immunization_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Immunization" == data["resourceType"]

    inst2 = immunization.Immunization(**data)
    impl_immunization_3(inst2)


def impl_immunization_4(inst):
    assert inst.id == "notGiven"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert (
        inst.occurrenceDateTime
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2013-01-10"}
        ).valueDateTime
    )
    assert inst.patient.reference == "Patient/example"
    assert inst.primarySource is True
    assert inst.status == "not-done"
    assert inst.statusReason.coding[0].code == "MEDPREC"
    assert inst.statusReason.coding[0].display == "medical precaution"
    assert (
        inst.statusReason.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.text.status == "generated"
    assert inst.vaccineCode.coding[0].code == "01"
    assert inst.vaccineCode.coding[0].display == "DTP"
    assert (
        inst.vaccineCode.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/sid/cvx"}
        ).valueUri
    )


def test_immunization_4(base_settings):
    """No. 4 tests collection for Immunization.
    Test File: immunization-example-refused.json
    """
    filename = base_settings["unittest_data_dir"] / "immunization-example-refused.json"
    inst = immunization.Immunization.model_validate_json(filename.read_bytes())
    assert "Immunization" == inst.get_resource_type()

    impl_immunization_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Immunization" == data["resourceType"]

    inst2 = immunization.Immunization(**data)
    impl_immunization_4(inst2)


def impl_immunization_5(inst):
    assert inst.doseQuantity.code == "ml"
    assert (
        inst.doseQuantity.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert float(inst.doseQuantity.value) == float(0.5)
    assert inst.education[0].documentType == "253088698300010311120702"
    assert (
        inst.education[0].presentationDate
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2013-01-10"}
        ).valueDateTime
    )
    assert (
        inst.education[0].publicationDate
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2012-07-02"}
        ).valueDateTime
    )
    assert inst.encounter.reference == "Encounter/example"
    assert (
        inst.expirationDate
        == ExternalValidatorModel.model_validate({"valueDate": "2015-02-28"}).valueDate
    )
    assert inst.fundingSource.coding[0].code == "private"
    assert (
        inst.fundingSource.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/immunization-funding-source"
            }
        ).valueUri
    )
    assert inst.id == "subpotent"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier[0].value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"
    assert inst.isSubpotent is False
    assert inst.location.reference == "Location/1"
    assert inst.lotNumber == "AAJN11K"
    assert inst.manufacturer.reference == "Organization/hl7"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.note[0].text == "Notes on adminstration of vaccine"
    assert (
        inst.occurrenceDateTime
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2015-01-15"}
        ).valueDateTime
    )
    assert inst.patient.reference == "Patient/example"
    assert inst.performer[0].actor.reference == "Practitioner/example"
    assert inst.performer[0].function.coding[0].code == "OP"
    assert (
        inst.performer[0].function.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v2-0443"}
        ).valueUri
    )
    assert inst.performer[1].actor.reference == "Practitioner/example"
    assert inst.performer[1].function.coding[0].code == "AP"
    assert (
        inst.performer[1].function.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v2-0443"}
        ).valueUri
    )
    assert inst.primarySource is True
    assert inst.programEligibility[0].coding[0].code == "ineligible"
    assert (
        inst.programEligibility[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/immunization-program-eligibility"
            }
        ).valueUri
    )
    assert inst.route.coding[0].code == "IM"
    assert inst.route.coding[0].display == "Injection, intramuscular"
    assert (
        inst.route.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministration"
            }
        ).valueUri
    )
    assert inst.site.coding[0].code == "LT"
    assert inst.site.coding[0].display == "left thigh"
    assert (
        inst.site.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActSite"}
        ).valueUri
    )
    assert inst.status == "completed"
    assert inst.subpotentReason[0].coding[0].code == "partial"
    assert (
        inst.subpotentReason[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/immunization-subpotent-reason"
            }
        ).valueUri
    )
    assert inst.text.status == "generated"
    assert inst.vaccineCode.coding[0].code == "GNHEP"
    assert (
        inst.vaccineCode.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:oid:1.2.36.1.2001.1005.17"}
        ).valueUri
    )
    assert inst.vaccineCode.text == "Hepatitis B"


def test_immunization_5(base_settings):
    """No. 5 tests collection for Immunization.
    Test File: immunization-example-subpotent.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "immunization-example-subpotent.json"
    )
    inst = immunization.Immunization.model_validate_json(filename.read_bytes())
    assert "Immunization" == inst.get_resource_type()

    impl_immunization_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Immunization" == data["resourceType"]

    inst2 = immunization.Immunization(**data)
    impl_immunization_5(inst2)
