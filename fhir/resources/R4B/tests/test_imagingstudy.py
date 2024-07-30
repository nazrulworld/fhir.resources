# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ImagingStudy
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import imagingstudy
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_imagingstudy_1(inst):
    assert inst.basedOn[0].reference == "ServiceRequest/example"
    assert inst.encounter.reference == "Encounter/example"
    assert inst.endpoint[0].reference == "Endpoint/example-wadors"
    assert inst.id == "example-xr"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate({"valueUri": "urn:dicom:uid"}).valueUri
    )
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == (
        "urn:oid:2.16.124.113543.6003.1154777499.30246.19789.35034300" "46"
    )
    assert inst.identifier[1].assigner.reference == "Organization/dicom-organization"
    assert inst.identifier[1].type.coding[0].code == "ACSN"
    assert (
        inst.identifier[1].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v2-0203"}
        ).valueUri
    )
    assert inst.identifier[1].use == "usual"
    assert inst.identifier[1].value == "W12342398"
    assert inst.identifier[2].assigner.reference == "Organization/dicom-organization"
    assert inst.identifier[2].use == "secondary"
    assert inst.identifier[2].value == "55551234"
    assert inst.interpreter[0].reference == "Practitioner/example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.modality[0].code == "DX"
    assert (
        inst.modality[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://dicom.nema.org/resources/ontology/DCM"}
        ).valueUri
    )
    assert inst.note[0].text == "XR Wrist 3+ Views"
    assert inst.numberOfInstances == 2
    assert inst.numberOfSeries == 1
    assert inst.procedureCode[0].coding[0].code == "RPID2589"
    assert inst.procedureCode[0].coding[0].display == "XR Wrist 3+ Views"
    assert (
        inst.procedureCode[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.radlex.org"}
        ).valueUri
    )
    assert inst.procedureCode[0].text == "XR Wrist 3+ Views"
    assert inst.procedureReference.reference == "Procedure/example"
    assert inst.reasonCode[0].coding[0].code == "357009"
    assert (
        inst.reasonCode[0].coding[0].display
        == "Closed fracture of trapezoidal bone of wrist"
    )
    assert (
        inst.reasonCode[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.referrer.reference == "Practitioner/example"
    assert inst.series[0].bodySite.code == "T-15460"
    assert inst.series[0].bodySite.display == "Wrist Joint"
    assert (
        inst.series[0].bodySite.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.series[0].description == "XR Wrist 3+ Views"
    assert inst.series[0].endpoint[0].reference == "Endpoint/example-wadors"
    assert inst.series[0].instance[0].number == 1
    assert (
        inst.series[0].instance[0].sopClass.code == "urn:oid:1.2.840.10008.5.1.4.1.1.2"
    )
    assert (
        inst.series[0].instance[0].sopClass.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.series[0].instance[0].title == "PA VIEW"
    assert (
        inst.series[0].instance[0].uid
        == "2.16.124.113543.6003.1154777499.30246.19789.3503430045.1.1"
    )
    assert inst.series[0].instance[1].number == 2
    assert (
        inst.series[0].instance[1].sopClass.code == "urn:oid:1.2.840.10008.5.1.4.1.1.2"
    )
    assert (
        inst.series[0].instance[1].sopClass.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.series[0].instance[1].title == "LL VIEW"
    assert (
        inst.series[0].instance[1].uid
        == "2.16.124.113543.6003.1154777499.30246.19789.3503430045.1.2"
    )
    assert inst.series[0].laterality.code == "419161000"
    assert inst.series[0].laterality.display == "Unilateral left"
    assert (
        inst.series[0].laterality.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.series[0].modality.code == "DX"
    assert (
        inst.series[0].modality.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://dicom.nema.org/resources/ontology/DCM"}
        ).valueUri
    )
    assert inst.series[0].number == 3
    assert inst.series[0].numberOfInstances == 2
    assert inst.series[0].performer[0].actor.reference == "Practitioner/example"
    assert inst.series[0].performer[0].function.coding[0].code == "PRF"
    assert (
        inst.series[0].performer[0].function.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"}
        ).valueUri
    )
    assert (
        inst.series[0].started
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2011-01-01T11:01:20+03:00"}
        ).valueDateTime
    )
    assert (
        inst.series[0].uid == "2.16.124.113543.6003.1154777499.30246.19789.3503430045.1"
    )
    assert (
        inst.started
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2017-01-01T11:01:20+03:00"}
        ).valueDateTime
    )
    assert inst.status == "available"
    assert inst.subject.reference == "Patient/dicom"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">XR Wrist 3+ '
        "Views. John Smith (MRN: 09236). Accession: W12342398. "
        "Performed: 2017-01-01. 1 series, 2 images.</div>"
    )
    assert inst.text.status == "generated"


def test_imagingstudy_1(base_settings):
    """No. 1 tests collection for ImagingStudy.
    Test File: imagingstudy-example-xr.json
    """
    filename = base_settings["unittest_data_dir"] / "imagingstudy-example-xr.json"
    inst = imagingstudy.ImagingStudy.model_validate_json(filename.read_bytes())
    assert "ImagingStudy" == inst.get_resource_type()

    impl_imagingstudy_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ImagingStudy" == data["resourceType"]

    inst2 = imagingstudy.ImagingStudy(**data)
    impl_imagingstudy_1(inst2)


def impl_imagingstudy_2(inst):
    assert inst.id == "example"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate({"valueUri": "urn:dicom:uid"}).valueUri
    )
    assert inst.identifier[0].value == (
        "urn:oid:2.16.124.113543.6003.1154777499.30246.19789.35034300" "45"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.numberOfInstances == 1
    assert inst.numberOfSeries == 1
    assert inst.series[0].bodySite.code == "67734004"
    assert inst.series[0].bodySite.display == "Upper Trunk Structure"
    assert (
        inst.series[0].bodySite.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.series[0].description == "CT Surview 180"
    assert inst.series[0].instance[0].number == 1
    assert (
        inst.series[0].instance[0].sopClass.code == "urn:oid:1.2.840.10008.5.1.4.1.1.2"
    )
    assert (
        inst.series[0].instance[0].sopClass.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert (
        inst.series[0].instance[0].uid
        == "2.16.124.113543.6003.189642796.63084.16748.2599092903"
    )
    assert inst.series[0].modality.code == "CT"
    assert (
        inst.series[0].modality.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://dicom.nema.org/resources/ontology/DCM"}
        ).valueUri
    )
    assert inst.series[0].number == 3
    assert inst.series[0].numberOfInstances == 1
    assert (
        inst.series[0].uid == "2.16.124.113543.6003.2588828330.45298.17418.2723805630"
    )
    assert (
        inst.started
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2011-01-01T11:01:20+03:00"}
        ).valueDateTime
    )
    assert inst.status == "available"
    assert inst.subject.reference == "Patient/dicom"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">CT Chest.  John '
        "Smith (MRN: 09236). Accession: W12342398. Performed: "
        "2011-01-01. 3 series, 12 images.</div>"
    )
    assert inst.text.status == "generated"


def test_imagingstudy_2(base_settings):
    """No. 2 tests collection for ImagingStudy.
    Test File: imagingstudy-example.json
    """
    filename = base_settings["unittest_data_dir"] / "imagingstudy-example.json"
    inst = imagingstudy.ImagingStudy.model_validate_json(filename.read_bytes())
    assert "ImagingStudy" == inst.get_resource_type()

    impl_imagingstudy_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ImagingStudy" == data["resourceType"]

    inst2 = imagingstudy.ImagingStudy(**data)
    impl_imagingstudy_2(inst2)
