# -*- coding: utf-8 -*-
from pydantic.datetime_parse import parse_date

from .. import fhirtypes  # noqa: F401
from .. import detectedissue


def test_DetectedIssue_1(base_settings):
    filename = (
        base_settings["unittest_data_dir"]
        / "detectedissue-example-allergy.canonical.json"
    )
    inst = detectedissue.DetectedIssue.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DetectedIssue" == inst.resource_type
    impl_DetectedIssue_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DetectedIssue" == data["resourceType"]

    inst2 = detectedissue.DetectedIssue(**data)
    impl_DetectedIssue_1(inst2)


def impl_DetectedIssue_1(inst):
    assert inst.id == "allergy"
    assert inst.text.div == "<div>[Put rendering here]</div>"
    assert inst.text.status == "generated"


def test_DetectedIssue_2(base_settings):
    filename = (
        base_settings["unittest_data_dir"] / "detectedissue-example-dup.canonical.json"
    )
    inst = detectedissue.DetectedIssue.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DetectedIssue" == inst.resource_type
    impl_DetectedIssue_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DetectedIssue" == data["resourceType"]

    inst2 = detectedissue.DetectedIssue(**data)
    impl_DetectedIssue_2(inst2)


def impl_DetectedIssue_2(inst):
    assert inst.author.reference == "Device/dsp"
    assert inst.category.coding[0].code == "DUPTHPY"
    assert inst.category.coding[0].display == "Duplicate Therapy Alert"
    assert inst.category.coding[0].system == "http://hl7.org/fhir/v3/ActCode"
    assert inst.date == parse_date("2013-05-08")
    assert inst.detail == "Similar test was performed within the past 14 days"
    assert inst.id == "duplicate"
    assert (
        inst.implicated[0].display
        == "Chest CT - ordered May 8, 2013 by Dr. Adam Careful"
    )
    assert inst.implicated[0].reference == "DiagnosticOrder/di"
    assert (
        inst.implicated[1].display
        == "Image 1 from Series 3: CT Images on Patient MINT (MINT1234) taken at 1-Jan 2011 01:20 AM"
    )
    assert inst.implicated[1].reference == "ImagingStudy/example"
    assert (
        inst.text.div
        == """<div>
      <p>Similar test was performed within the past 14 days</p>
      <ul>
        <li>
          <a href=\"DiagnosticOrder/id\">Chest CT - ordered May 8, 2013 by Dr. Adam Careful</a>
        </li>
        <li>
          <a href=\"ImagingStudy/example\">Image 1 from Series 3: CT Images on Patient MINT (MINT1234) taken at 1-Jan 2011 01:20 AM</a>
        </li>
      </ul>
    </div>"""
    )
    assert inst.text.status == "generated"


def test_DetectedIssue_3(base_settings):
    filename = (
        base_settings["unittest_data_dir"] / "detectedissue-example-lab.canonical.json"
    )
    inst = detectedissue.DetectedIssue.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DetectedIssue" == inst.resource_type
    impl_DetectedIssue_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DetectedIssue" == data["resourceType"]

    inst2 = detectedissue.DetectedIssue(**data)
    impl_DetectedIssue_3(inst2)


def impl_DetectedIssue_3(inst):
    assert inst.id == "lab"
    assert inst.text.div == "<div>[Put rendering here]</div>"
    assert inst.text.status == "generated"


def test_DetectedIssue_4(base_settings):
    filename = (
        base_settings["unittest_data_dir"] / "detectedissue-example.canonical.json"
    )
    inst = detectedissue.DetectedIssue.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DetectedIssue" == inst.resource_type
    impl_DetectedIssue_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DetectedIssue" == data["resourceType"]

    inst2 = detectedissue.DetectedIssue(**data)
    impl_DetectedIssue_4(inst2)


def impl_DetectedIssue_4(inst):
    assert inst.author.reference == "Device/dsp"
    assert inst.category.coding[0].code == "DRG"
    assert inst.category.coding[0].display == "Drug Interaction Alert"
    assert inst.category.coding[0].system == "http://hl7.org/fhir/v3/ActCode"
    assert inst.date == parse_date("2014-01-05")
    assert (
        inst.detail
        == "Risk of internal bleeding.  Those who take acetaminophen along with the widely used blood-thinning drug warfarin may face the risk of serious internal bleeding. People on warfarin who take acetaminophen for at least seven days in a row should be closely watched for bleeding."
    )
    assert inst.id == "ddi"
    assert (
        inst.implicated[0].display
        == "500 mg Acetaminophen tablet 1/day, PRN since 2010"
    )
    assert inst.implicated[0].reference == "MedicationStatement/tylenol"
    assert inst.implicated[1].display == "Warfarin 1 MG TAB prescribed Jan. 5, 2014"
    assert inst.implicated[1].reference == "MedicationOrder/warfarin"
    assert inst.mitigation[0].action.coding[0].code == "13"
    assert inst.mitigation[0].action.coding[0].display == "Stopped Concurrent Therapy"
    assert (
        inst.mitigation[0].action.coding[0].system == "http://hl7.org/fhir/v3/ActCode"
    )
    assert (
        inst.mitigation[0].action.text
        == "Asked patient to discontinue regular use of Tylenol and to consult with clinician if they need to resume to allow appropriate INR monitoring"
    )
    assert inst.mitigation[0].author.display == "Dr. Adam Careful"
    assert inst.mitigation[0].author.reference == "Practitioner/example"
    assert inst.mitigation[0].date == parse_date("2014-01-05")
    assert inst.severity == "high"
    assert (
        inst.text.div
        == """<div>
      <p><b>Severity: High</b> - Risk of internal bleeding</p>
      <p>Those who take acetaminophen along with the widely used blood-thinning drug warfarin may face the risk of serious internal bleeding. People on warfarin who take acetaminophen for at least seven days in a row should be closely watched for bleeding.</p>
      <ul>
        <li><a href=\"MedicationStatement/tylenol\">500 mg Acetaminophen tablet 1/day, PRN since 2010</a></li>
        <li><a href=\"MedicationOrder/warfarin\">Warfarin 1 MG TAB prescribed Jan. 5, 2014</a></li>
      </ul>
      <p>Mitigation: Jan 5, 2014 by Dr. Adam Careful: </p>
      <p>Asked patient to discontinue regular use of Tylenol and to consult with clinician if they need to resume to allow appropriate INR monitoring</p>
    </div>"""
    )
    assert inst.text.status == "generated"
