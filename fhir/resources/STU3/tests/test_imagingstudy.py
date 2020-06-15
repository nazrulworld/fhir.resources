# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ImagingStudy
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import imagingstudy


def impl_imagingstudy_1(inst):
    assert inst.accession.assigner.reference == "Organization/dicom-organization"
    assert inst.accession.type.coding[0].code == "ACSN"
    assert inst.accession.type.coding[0].system == "http://hl7.org/fhir/v2/0203"
    assert inst.accession.use == "usual"
    assert inst.accession.value == "W12342398"
    assert inst.availability == "ONLINE"
    assert inst.basedOn[0].reference == "ProcedureRequest/example"
    assert inst.context.reference == "Encounter/example"
    assert inst.description == "XR Wrist 3+ Views"
    assert inst.endpoint[0].reference == "Endpoint/example-wadors"
    assert inst.id == "example-xr"
    assert inst.identifier[0].assigner.reference == "Organization/dicom-organization"
    assert inst.identifier[0].use == "secondary"
    assert inst.identifier[0].value == "55551234"
    assert inst.interpreter[0].reference == "Practitioner/example"
    assert inst.modalityList[0].code == "DX"
    assert inst.modalityList[0].system == "http://dicom.nema.org/resources/ontology/DCM"
    assert inst.numberOfInstances == 2
    assert inst.numberOfSeries == 1
    assert inst.patient.reference == "Patient/dicom"
    assert inst.procedureCode[0].coding[0].code == "RPID2589"
    assert inst.procedureCode[0].coding[0].display == "XR Wrist 3+ Views"
    assert inst.procedureCode[0].coding[0].system == "http://www.radlex.org"
    assert inst.procedureCode[0].text == "XR Wrist 3+ Views"
    assert inst.procedureReference[0].reference == "Procedure/example"
    assert inst.reason.coding[0].code == "357009"
    assert (
        inst.reason.coding[0].display == "Closed fracture of trapezoidal bone of wrist"
    )
    assert inst.reason.coding[0].system == "http://snomed.info/sct"
    assert inst.referrer.reference == "Practitioner/example"
    assert inst.series[0].availability == "ONLINE"
    assert inst.series[0].bodySite.code == "T-15460"
    assert inst.series[0].bodySite.display == "Wrist Joint"
    assert inst.series[0].bodySite.system == "http://snomed.info/sct"
    assert inst.series[0].description == "XR Wrist 3+ Views"
    assert inst.series[0].endpoint[0].reference == "Endpoint/example-wadors"
    assert inst.series[0].instance[0].number == 1
    assert inst.series[0].instance[0].sopClass == "urn:oid:1.2.840.10008.5.1.4.1.1.2"
    assert inst.series[0].instance[0].title == "PA VIEW"
    assert inst.series[0].instance[0].uid == (
        "urn:oid:2.16.124.113543.6003.1154777499.30246.19789.35034300" "45.1.1"
    )
    assert inst.series[0].instance[1].number == 2
    assert inst.series[0].instance[1].sopClass == "urn:oid:1.2.840.10008.5.1.4.1.1.2"
    assert inst.series[0].instance[1].title == "LL VIEW"
    assert inst.series[0].instance[1].uid == (
        "urn:oid:2.16.124.113543.6003.1154777499.30246.19789.35034300" "45.1.2"
    )
    assert inst.series[0].laterality.code == "419161000"
    assert inst.series[0].laterality.display == "Unilateral left"
    assert inst.series[0].laterality.system == "http://snomed.info/sct"
    assert inst.series[0].modality.code == "DX"
    assert (
        inst.series[0].modality.system == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.series[0].number == 3
    assert inst.series[0].numberOfInstances == 2
    assert inst.series[0].performer[0].reference == "Practitioner/example"
    assert inst.series[0].started == fhirtypes.DateTime.validate(
        "2011-01-01T11:01:20+03:00"
    )
    assert inst.series[0].uid == (
        "urn:oid:2.16.124.113543.6003.1154777499.30246.19789.35034300" "45.1"
    )
    assert inst.started == fhirtypes.DateTime.validate("2017-01-01T11:01:20+03:00")
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">XR Wrist 3+ '
        "Views. John Smith (MRN: 09236). Accession: W12342398. "
        "Performed: 2017-01-01. 1 series, 2 images.</div>"
    )
    assert inst.text.status == "generated"
    assert inst.uid == (
        "urn:oid:2.16.124.113543.6003.1154777499.30246.19789.35034300" "46"
    )


def test_imagingstudy_1(base_settings):
    """No. 1 tests collection for ImagingStudy.
    Test File: imagingstudy-example-xr.json
    """
    filename = base_settings["unittest_data_dir"] / "imagingstudy-example-xr.json"
    inst = imagingstudy.ImagingStudy.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ImagingStudy" == inst.resource_type

    impl_imagingstudy_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ImagingStudy" == data["resourceType"]

    inst2 = imagingstudy.ImagingStudy(**data)
    impl_imagingstudy_1(inst2)


def impl_imagingstudy_2(inst):
    assert inst.id == "example"
    assert inst.numberOfInstances == 1
    assert inst.numberOfSeries == 1
    assert inst.patient.reference == "Patient/dicom"
    assert inst.series[0].bodySite.code == "67734004"
    assert inst.series[0].bodySite.display == "Upper Trunk Structure"
    assert inst.series[0].bodySite.system == "http://snomed.info/sct"
    assert inst.series[0].description == "CT Surview 180"
    assert inst.series[0].instance[0].number == 1
    assert inst.series[0].instance[0].sopClass == "urn:oid:1.2.840.10008.5.1.4.1.1.2"
    assert inst.series[0].instance[0].uid == (
        "urn:oid:2.16.124.113543.6003.189642796.63084.16748.259909290" "3"
    )
    assert inst.series[0].modality.code == "CT"
    assert (
        inst.series[0].modality.system == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.series[0].number == 3
    assert inst.series[0].numberOfInstances == 1
    assert inst.series[0].uid == (
        "urn:oid:2.16.124.113543.6003.2588828330.45298.17418.27238056" "30"
    )
    assert inst.started == fhirtypes.DateTime.validate("2011-01-01T11:01:20+03:00")
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">CT Chest.  John '
        "Smith (MRN: 09236). Accession: W12342398. Performed: "
        "2011-01-01. 3 series, 12 images.</div>"
    )
    assert inst.text.status == "generated"
    assert inst.uid == (
        "urn:oid:2.16.124.113543.6003.1154777499.30246.19789.35034300" "45"
    )


def test_imagingstudy_2(base_settings):
    """No. 2 tests collection for ImagingStudy.
    Test File: imagingstudy-example.json
    """
    filename = base_settings["unittest_data_dir"] / "imagingstudy-example.json"
    inst = imagingstudy.ImagingStudy.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ImagingStudy" == inst.resource_type

    impl_imagingstudy_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ImagingStudy" == data["resourceType"]

    inst2 = imagingstudy.ImagingStudy(**data)
    impl_imagingstudy_2(inst2)
