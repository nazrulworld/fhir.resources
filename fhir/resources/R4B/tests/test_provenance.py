# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Provenance
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import provenance
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_provenance_1(inst):
    assert inst.activity.coding[0].code == "AU"
    assert inst.activity.coding[0].display == "authenticated"
    assert (
        inst.activity.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-DocumentCompletion"}
        ).valueUri
    )
    assert inst.agent[0].type.coding[0].code == "VERF"
    assert (
        inst.agent[0].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/contractsignertypecodes"
            }
        ).valueUri
    )
    assert (
        inst.agent[0].who.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.agent[0].who.identifier.value == "mailto://hhd@ssa.gov"
    assert inst.id == "signature"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.reason[0].coding[0].code == "TREAT"
    assert inst.reason[0].coding[0].display == "treatment"
    assert (
        inst.reason[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert (
        inst.recorded
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2015-08-27T08:39:24+10:00"}
        ).valueInstant
    )
    assert (
        inst.signature[0].data
        == ExternalValidatorModel.model_validate(
            {"valueBase64Binary": "Li4u"}
        ).valueBase64Binary
    )
    assert inst.signature[0].sigFormat == "application/signature+xml"
    assert inst.signature[0].targetFormat == "application/fhir+xml"
    assert inst.signature[0].type[0].code == "1.2.840.10065.1.12.1.5"
    assert inst.signature[0].type[0].display == "Verification Signature"
    assert (
        inst.signature[0].type[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:iso-astm:E1762-95:2013"}
        ).valueUri
    )
    assert (
        inst.signature[0].when
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2015-08-27T08:39:24+10:00"}
        ).valueInstant
    )
    assert inst.signature[0].who.reference == "Practitioner/xcda-author"
    assert inst.target[0].reference == "DocumentReference/example"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">procedure record'
        " authored on 27-June 2015 by Harold Hippocrates, MD Content "
        "extracted from Referral received 26-June</div>"
    )
    assert inst.text.status == "generated"


def test_provenance_1(base_settings):
    """No. 1 tests collection for Provenance.
    Test File: provenance-example-sig.json
    """
    filename = base_settings["unittest_data_dir"] / "provenance-example-sig.json"
    inst = provenance.Provenance.model_validate_json(filename.read_bytes())
    assert "Provenance" == inst.get_resource_type()

    impl_provenance_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Provenance" == data["resourceType"]

    inst2 = provenance.Provenance(**data)
    impl_provenance_1(inst2)


def impl_provenance_2(inst):
    assert inst.agent[0].role[0].coding[0].code == "AUT"
    assert (
        inst.agent[0].role[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"}
        ).valueUri
    )
    assert inst.agent[0].who.reference == "Patient/72"
    assert inst.id == "consent-signature"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert (
        inst.recorded
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2016-05-26T00:41:10-04:00"}
        ).valueInstant
    )
    assert (
        inst.signature[0].data
        == ExternalValidatorModel.model_validate(
            {"valueBase64Binary": "dGhpcyBibG9iIGlzIHNuaXBwZWQ="}
        ).valueBase64Binary
    )
    assert inst.signature[0].sigFormat == "application/signature+xml"
    assert inst.signature[0].targetFormat == "application/fhir+xml"
    assert inst.signature[0].type[0].code == "1.2.840.10065.1.12.1.1"
    assert inst.signature[0].type[0].display == "Author's Signature"
    assert (
        inst.signature[0].type[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:iso-astm:E1762-95:2013"}
        ).valueUri
    )
    assert (
        inst.signature[0].when
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2016-05-26T00:41:10-04:00"}
        ).valueInstant
    )
    assert inst.signature[0].who.reference == "Patient/72"
    assert inst.target[0].reference == "Consent/consent-example-signature"
    assert inst.text.status == "generated"


def test_provenance_2(base_settings):
    """No. 2 tests collection for Provenance.
    Test File: provenance-consent-signature.json
    """
    filename = base_settings["unittest_data_dir"] / "provenance-consent-signature.json"
    inst = provenance.Provenance.model_validate_json(filename.read_bytes())
    assert "Provenance" == inst.get_resource_type()

    impl_provenance_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Provenance" == data["resourceType"]

    inst2 = provenance.Provenance(**data)
    impl_provenance_2(inst2)


def impl_provenance_3(inst):
    assert inst.agent[0].type.coding[0].code == "AUT"
    assert (
        inst.agent[0].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"}
        ).valueUri
    )
    assert inst.agent[0].who.reference == "Patient/example"
    assert inst.entity[0].role == "source"
    assert inst.entity[0].what.identifier.type.coding[0].code == "CWL"
    assert inst.entity[0].what.identifier.type.coding[0].display == "lobSTR"
    assert (
        inst.entity[0].what.identifier.type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://github.com/common-workflow-language/workflows"}
        ).valueUri
    )
    assert inst.entity[0].what.identifier.value == (
        "https://github.com/common-workflow-"
        "language/workflows/blob/master/workflows/lobSTR/lobSTR-"
        "workflow.cwl"
    )
    assert inst.id == "example-cwl"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert (
        inst.occurredPeriod.start
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2016-11-30"}
        ).valueDateTime
    )
    assert inst.reason[0].text == (
        "profiling Short Tandem Repeats (STRs) from high throughput " "sequencing data."
    )
    assert (
        inst.recorded
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2016-12-01T08:12:14+10:00"}
        ).valueInstant
    )
    assert inst.target[0].reference == "MolecularSequence/example-pgx-1"
    assert inst.text.status == "generated"


def test_provenance_3(base_settings):
    """No. 3 tests collection for Provenance.
    Test File: provenance-example-cwl.json
    """
    filename = base_settings["unittest_data_dir"] / "provenance-example-cwl.json"
    inst = provenance.Provenance.model_validate_json(filename.read_bytes())
    assert "Provenance" == inst.get_resource_type()

    impl_provenance_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Provenance" == data["resourceType"]

    inst2 = provenance.Provenance(**data)
    impl_provenance_3(inst2)


def impl_provenance_4(inst):
    assert inst.agent[0].type.coding[0].code == "AUT"
    assert (
        inst.agent[0].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"}
        ).valueUri
    )
    assert inst.agent[0].who.reference == "Practitioner/example"
    assert inst.entity[0].role == "source"
    assert inst.entity[0].what.identifier.type.coding[0].code == "biocompute"
    assert inst.entity[0].what.identifier.type.coding[0].display == "obj.1001"
    assert (
        inst.entity[0].what.identifier.type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://hive.biochemistry.gwu.edu"}
        ).valueUri
    )
    assert inst.entity[0].what.identifier.value == (
        "https://hive.biochemistry.gwu.edu/cgi-"
        "bin/prd/htscsrs/servlet.cgi?pageid=bcoexample_1"
    )
    assert inst.id == "example-biocompute-object"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert (
        inst.occurredPeriod.start
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2017-06-06"}
        ).valueDateTime
    )
    assert inst.reason[0].text == "antiviral resistance detection"
    assert (
        inst.recorded
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2016-06-09T08:12:14+10:00"}
        ).valueInstant
    )
    assert inst.target[0].reference == "MolecularSequence/example"
    assert inst.text.status == "generated"


def test_provenance_4(base_settings):
    """No. 4 tests collection for Provenance.
    Test File: provenance-example-biocompute-object.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "provenance-example-biocompute-object.json"
    )
    inst = provenance.Provenance.model_validate_json(filename.read_bytes())
    assert "Provenance" == inst.get_resource_type()

    impl_provenance_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Provenance" == data["resourceType"]

    inst2 = provenance.Provenance(**data)
    impl_provenance_4(inst2)


def impl_provenance_5(inst):
    assert inst.agent[0].type.coding[0].code == "AUT"
    assert (
        inst.agent[0].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"}
        ).valueUri
    )
    assert inst.agent[0].who.reference == "Practitioner/xcda-author"
    assert inst.agent[1].id == "a1"
    assert inst.agent[1].type.coding[0].code == "DEV"
    assert (
        inst.agent[1].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"}
        ).valueUri
    )
    assert inst.agent[1].who.reference == "Device/software"
    assert inst.entity[0].role == "source"
    assert inst.entity[0].what.display == "CDA Document in XDS repository"
    assert inst.entity[0].what.reference == "DocumentReference/example"
    assert inst.id == "example"
    assert inst.location.reference == "Location/1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert (
        inst.occurredPeriod.end
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2015-06-28"}
        ).valueDateTime
    )
    assert (
        inst.occurredPeriod.start
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2015-06-27"}
        ).valueDateTime
    )
    assert (
        inst.policy[0]
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://acme.com/fhir/Consent/25"}
        ).valueUri
    )
    assert inst.reason[0].coding[0].code == "3457005"
    assert inst.reason[0].coding[0].display == "Referral"
    assert (
        inst.reason[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert (
        inst.recorded
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2015-06-27T08:39:24+10:00"}
        ).valueInstant
    )
    assert inst.target[0].reference == "Procedure/example/_history/1"
    assert inst.text.status == "generated"


def test_provenance_5(base_settings):
    """No. 5 tests collection for Provenance.
    Test File: provenance-example.json
    """
    filename = base_settings["unittest_data_dir"] / "provenance-example.json"
    inst = provenance.Provenance.model_validate_json(filename.read_bytes())
    assert "Provenance" == inst.get_resource_type()

    impl_provenance_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Provenance" == data["resourceType"]

    inst2 = provenance.Provenance(**data)
    impl_provenance_5(inst2)
