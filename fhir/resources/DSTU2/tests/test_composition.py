# -*- coding: utf-8 -*-
from datetime import datetime, timezone

from pydantic.datetime_parse import parse_date

from .. import fhirtypes  # noqa: F401
from .. import composition


def test_Composition_1(base_settings):
    filename = base_settings["unittest_data_dir"] / "composition-example.canonical.json"
    inst = composition.Composition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Composition" == inst.resource_type
    impl_Composition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Composition" == data["resourceType"]

    inst2 = composition.Composition(**data)
    impl_Composition_1(inst2)


def impl_Composition_1(inst):
    assert inst.attester[0].mode[0] == "legal"
    assert inst.attester[0].party.display == "Harold Hippocrates, MD"
    assert inst.attester[0].party.reference == "Practitioner/xcda-author"
    assert inst.attester[0].time == datetime(2012, 1, 4, 9, 10, 14, tzinfo=timezone.utc)
    assert inst.author[0].display == "Harold Hippocrates, MD"
    assert inst.author[0].reference == "Practitioner/xcda-author"
    assert inst.confidentiality == "N"
    assert inst.custodian.display == "Good Health Clinic"
    assert inst.custodian.reference == "Organization/2.16.840.1.113883.19.5"
    assert inst.date == datetime(2012, 1, 4, 9, 10, 14, tzinfo=timezone.utc)
    assert inst.encounter.reference == "Encounter/xcda"
    assert inst.event[0].code[0].coding[0].code == "HEALTHREC"
    assert inst.event[0].code[0].coding[0].display == "health record"
    assert inst.event[0].code[0].coding[0].system == "http://hl7.org/fhir/v3/ActCode"
    assert inst.event[0].detail[0].reference == "Observation/example"
    assert inst.event[0].period.end == parse_date("2012-11-12")
    assert inst.event[0].period.start == parse_date("2010-07-18")
    assert inst.id == "example"
    assert inst.identifier.system == "http://healthintersections.com.au/test"
    assert inst.identifier.value == "1"
    assert inst.section[0].code.coding[0].code == "11348-0"
    assert inst.section[0].code.coding[0].display == "History of past illness Narrative"
    assert inst.section[0].code.coding[0].system == "http://loinc.org"
    assert inst.section[0].entry[0].reference == "Condition/stroke"
    assert inst.section[0].entry[1].reference == "Condition/example"
    assert inst.section[0].entry[2].reference == "Condition/example2"
    assert inst.section[0].mode == "snapshot"
    assert inst.section[0].orderedBy.coding[0].code == "event-date"
    assert inst.section[0].orderedBy.coding[0].display == "Sorted by Event Date"
    assert (
        inst.section[0].orderedBy.coding[0].system == "http://hl7.org/fhir/list-order"
    )
    assert (
        inst.section[0].text.div
        == """<div>
				<table>
					<tr>
						<td>
							<b>Code</b>
						</td>
						<td>
							<b>Date</b>
						</td>
						<td>
							<b>Type</b>
						</td>
						<td>
							<b>BodySite</b>
						</td>
						<td>
							<b>Severity</b>
						</td>
					</tr>
					<tr>
						<td>Stroke</td>
						<td>2010-07-18</td>
						<td>Diagnosis</td>
						<td/>
						<td/>
					</tr>
					<tr>
						<td>Burnt Ear</td>
						<td>2012-05-24</td>
						<td>Diagnosis</td>
						<td>Left Ear</td>
						<td/>
					</tr>
					<tr>
						<td>Asthma</td>
						<td>2012-11-12</td>
						<td>Finding</td>
						<td/>
						<td>Mild</td>
					</tr>
				</table>
			</div>"""
    )
    assert inst.section[0].text.status == "generated"
    assert inst.section[0].title == "History of present illness"
    assert inst.section[1].code.coding[0].code == "10157-6"
    assert (
        inst.section[1].code.coding[0].display
        == "History of family member diseases Narrative"
    )
    assert inst.section[1].code.coding[0].system == "http://loinc.org"
    assert inst.section[1].emptyReason.coding[0].code == "withheld"
    assert inst.section[1].emptyReason.coding[0].display == "Information Withheld"
    assert (
        inst.section[1].emptyReason.coding[0].system
        == "http://hl7.org/fhir/list-empty-reason"
    )
    assert inst.section[1].mode == "snapshot"
    assert (
        inst.section[1].text.div
        == """<div>
			<p>History of family member diseases - not available</p>
			</div>"""
    )
    assert inst.section[1].text.status == "generated"
    assert inst.section[1].title == "History of family member diseases"
    assert inst.status == "final"
    assert inst.subject.display == "Henry Levin the 7th"
    assert inst.subject.reference == "Patient/xcda"
    assert (
        inst.text.div
        == """<div>
			<p>Consultation note for Henry Levin the 7th</p>
			<p>Managed by Good Health Clinic</p>
		</div>"""
    )
    assert inst.text.status == "generated"
    assert inst.title == "Consultation Note"
    assert inst.type.coding[0].code == "11488-4"
    assert inst.type.coding[0].display == "Consult note"
    assert inst.type.coding[0].system == "http://loinc.org"
