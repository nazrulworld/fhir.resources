# -*- coding: utf-8 -*-
from pydantic.datetime_parse import parse_date, parse_datetime

from .. import fhirtypes  # noqa: F401
from .. import allergyintolerance


def test_AllergyIntolerance_1(base_settings):
    filename = (
        base_settings["unittest_data_dir"]
        / "allergyintolerance-example-refuted.canonical.json"
    )
    inst = allergyintolerance.AllergyIntolerance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "AllergyIntolerance" == inst.resource_type
    impl_AllergyIntolerance_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "AllergyIntolerance" == data["resourceType"]

    inst2 = allergyintolerance.AllergyIntolerance(**data)
    impl_AllergyIntolerance_1(inst2)


def impl_AllergyIntolerance_1(inst):
    assert inst.category == "food"
    assert (
        inst.extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/allergyintolerance-reasonRefuted"
    )
    assert inst.extension[0].valueCodeableConcept.coding[0].code == "MED"
    assert (
        inst.extension[0].valueCodeableConcept.coding[0].display
        == "Medical Status Altered"
    )
    assert (
        inst.extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/v3/ActReason"
    )
    assert inst.id == "allergyintolerance-example-refuted"
    assert inst.identifier[0].system == "http://acme.com/ids/patients/risks"
    assert inst.identifier[0].value == "49476534"
    assert inst.patient.reference == "Patient/example"
    assert inst.recordedDate == parse_datetime("2014-10-09T14:58:00+11:00")
    assert inst.recorder.reference == "Practitioner/example"
    assert inst.status == "refuted"
    assert inst.substance.coding[0].code == "227493005"
    assert inst.substance.coding[0].display == "Cashew nuts"
    assert inst.substance.coding[0].system == "http://snomed.info/sct"
    assert (
        inst.text.div
        == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: allergyintolerance-example-refuted</p><p><b>identifier</b>: 49476534</p><p><b>recordedDate</b>: 09/10/2014 2:58:00 PM</p><p><b>recorder</b>: <a>Practitioner/example</a></p><p><b>patient</b>: <a>Patient/example</a></p><p><b>substance</b>: Cashew nuts <span>(Details : {SNOMED CT code '227493005' = '227493005', given as 'Cashew nuts'})</span></p><p><b>status</b>: refuted</p><p><b>category</b>: food</p></div>"
    )
    assert inst.text.status == "generated"


def test_AllergyIntolerance_2(base_settings):
    filename = (
        base_settings["unittest_data_dir"] / "allergyintolerance-example.canonical.json"
    )
    inst = allergyintolerance.AllergyIntolerance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "AllergyIntolerance" == inst.resource_type
    impl_AllergyIntolerance_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "AllergyIntolerance" == data["resourceType"]

    inst2 = allergyintolerance.AllergyIntolerance(**data)
    impl_AllergyIntolerance_2(inst2)


def impl_AllergyIntolerance_2(inst):
    assert inst.category == "food"
    assert inst.criticality == "CRITH"
    assert inst.id == "allergyintolerance-example"
    assert inst.identifier[0].system == "http://acme.com/ids/patients/risks"
    assert inst.identifier[0].value == "49476534"
    assert inst.lastOccurence == "2012-06"
    assert inst.patient.reference == "Patient/example"
    assert inst.reaction[0].certainty == "confirmed"
    assert (
        inst.reaction[0].description
        == "Challenge Protocol. Severe Reaction to 1/8 cashew. Epinephrine administered"
    )
    assert inst.reaction[0].manifestation[0].coding[0].code == "39579001"
    assert (
        inst.reaction[0].manifestation[0].coding[0].display == "Anaphylactic reaction"
    )
    assert (
        inst.reaction[0].manifestation[0].coding[0].system == "http://snomed.info/sct"
    )
    assert inst.reaction[0].onset == parse_date("2012-06-12")
    assert inst.reaction[0].severity == "severe"
    assert inst.reaction[0].substance.coding[0].code == "C3214954"
    assert (
        inst.reaction[0].substance.coding[0].display
        == "cashew nut allergenic extract Injectable Product"
    )
    assert (
        inst.reaction[0].substance.coding[0].system
        == "http://www.nlm.nih.gov/research/umls/rxnorm"
    )
    assert inst.reaction[1].certainty == "likely"
    assert inst.reaction[1].manifestation[0].coding[0].code == "64305001"
    assert inst.reaction[1].manifestation[0].coding[0].display == "Urticaria"
    assert (
        inst.reaction[1].manifestation[0].coding[0].system == "http://snomed.info/sct"
    )
    assert inst.reaction[1].onset == "2004"
    assert inst.reaction[1].severity == "moderate"
    assert inst.recordedDate == parse_datetime("2014-10-09T14:58:00+11:00")
    assert inst.recorder.reference == "Practitioner/example"
    assert inst.status == "confirmed"
    assert inst.substance.coding[0].code == "227493005"
    assert inst.substance.coding[0].display == "Cashew nuts"
    assert inst.substance.coding[0].system == "http://snomed.info/sct"
    assert (
        inst.text.div
        == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: allergyintolerance-example</p><p><b>identifier</b>: 49476534</p><p><b>recordedDate</b>: 09/10/2014 2:58:00 PM</p><p><b>recorder</b>: <a>Practitioner/example</a></p><p><b>patient</b>: <a>Patient/example</a></p><p><b>substance</b>: Cashew nuts <span>(Details : {SNOMED CT code '227493005' = '227493005', given as 'Cashew nuts'})</span></p><p><b>status</b>: confirmed</p><p><b>criticality</b>: CRITH</p><p><b>type</b>: allergy</p><p><b>category</b>: food</p><p><b>lastOccurence</b>: 01/06/2012</p><blockquote><p><b>reaction</b></p><p><b>substance</b>: cashew nut allergenic extract Injectable Product <span>(Details : {RxNorm code 'C3214954' = '??', given as 'cashew nut allergenic extract Injectable Product'})</span></p><p><b>certainty</b>: confirmed</p><p><b>manifestation</b>: Anaphylactic reaction <span>(Details : {SNOMED CT code '39579001' = '39579001', given as 'Anaphylactic reaction'})</span></p><p><b>description</b>: Challenge Protocol. Severe Reaction to 1/8 cashew. Epinephrine administered</p><p><b>onset</b>: 12/06/2012</p><p><b>severity</b>: severe</p></blockquote><blockquote><p><b>reaction</b></p><p><b>certainty</b>: likely</p><p><b>manifestation</b>: Urticaria <span>(Details : {SNOMED CT code '64305001' = '64305001', given as 'Urticaria'})</span></p><p><b>onset</b>: 01/01/2004</p><p><b>severity</b>: moderate</p></blockquote></div>"
    )
    assert inst.text.status == "generated"
    assert inst.type == "allergy"


def test_AllergyIntolerance_3(base_settings):
    filename = (
        base_settings["unittest_data_dir"]
        / "allergyintolerance-fishallergy.canonical.json"
    )
    inst = allergyintolerance.AllergyIntolerance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "AllergyIntolerance" == inst.resource_type
    impl_AllergyIntolerance_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "AllergyIntolerance" == data["resourceType"]

    inst2 = allergyintolerance.AllergyIntolerance(**data)
    impl_AllergyIntolerance_3(inst2)


def impl_AllergyIntolerance_3(inst):
    assert inst.category == "food"
    assert inst.id == "fishallergy"
    assert inst.identifier[0].system == "http://acme.com/ids/patients/risks"
    assert inst.identifier[0].value == "49476535"
    assert inst.patient.reference == "Patient/example"
    assert inst.recordedDate == parse_datetime("2015-08-06T15:37:31-06:00")
    assert inst.recorder.reference == "Practitioner/example"
    assert inst.substance.coding[0].code == "227037002"
    assert inst.substance.coding[0].display == "Fish - dietary (substance)"
    assert inst.substance.coding[0].system == "http://snomed.info/sct"
    assert inst.substance.text == "Allergic to fresh fish. Tolerates canned fish"
    assert (
        inst.text.div
        == """<div>
      <p>allergy is to fresh fish. Tolerates canned fish</p>
      <p>recordedDate:2015-08-06T00:00:00-06:00</p>
      <p>substance:Fish - dietary (substance)</p>
    </div>"""
    )
    assert inst.text.status == "additional"


def test_AllergyIntolerance_4(base_settings):
    filename = (
        base_settings["unittest_data_dir"]
        / "allergyintolerance-medication.canonical.json"
    )
    inst = allergyintolerance.AllergyIntolerance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "AllergyIntolerance" == inst.resource_type
    impl_AllergyIntolerance_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "AllergyIntolerance" == data["resourceType"]

    inst2 = allergyintolerance.AllergyIntolerance(**data)
    impl_AllergyIntolerance_4(inst2)


def impl_AllergyIntolerance_4(inst):
    assert inst.category == "medication"
    assert inst.criticality == "CRITH"
    assert inst.id == "medication"
    assert inst.patient.reference == "Patient/example"
    assert inst.reaction[0].manifestation[0].coding[0].code == "247472004"
    assert inst.reaction[0].manifestation[0].coding[0].display == "Hives"
    assert (
        inst.reaction[0].manifestation[0].coding[0].system == "http://snomed.info/sct"
    )
    assert inst.recordedDate == parse_date("2010-03-01")
    assert inst.recorder.reference == "Practitioner/13"
    assert inst.status == "unconfirmed"
    assert inst.substance.coding[0].code == "314422"
    assert inst.substance.coding[0].display == "ALLERGENIC EXTRACT, PENICILLIN"
    assert (
        inst.substance.coding[0].system == "http://www.nlm.nih.gov/research/umls/rxnorm"
    )
    assert (
        inst.text.div
        == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: medication</p><p><b>recordedDate</b>: 01/03/2010</p><p><b>recorder</b>: <a>Practitioner/13</a></p><p><b>patient</b>: <a>Patient/example</a></p><p><b>substance</b>: ALLERGENIC EXTRACT, PENICILLIN <span>(Details : {RxNorm code '314422' = '??', given as 'ALLERGENIC EXTRACT, PENICILLIN'})</span></p><p><b>status</b>: unconfirmed</p><p><b>criticality</b>: CRITH</p><p><b>category</b>: medication</p><h3>Reactions</h3><table><tr><td>-</td><td><b>Manifestation</b></td></tr><tr><td>*</td><td>Hives <span>(Details : {SNOMED CT code '247472004' = '247472004', given as 'Hives'})</span></td></tr></table></div>"
    )
    assert inst.text.status == "generated"
