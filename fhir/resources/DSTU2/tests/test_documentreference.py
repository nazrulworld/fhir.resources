# -*- coding: utf-8 -*-
from pydantic.datetime_parse import parse_datetime

from .. import fhirtypes  # noqa: F401
from .. import documentreference


def test_DocumentReference_1(base_settings):
    filename = (
        base_settings["unittest_data_dir"] / "documentreference-example.canonical.json"
    )
    inst = documentreference.DocumentReference.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DocumentReference" == inst.resource_type
    impl_DocumentReference_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DocumentReference" == data["resourceType"]

    inst2 = documentreference.DocumentReference(**data)
    impl_DocumentReference_1(inst2)


def impl_DocumentReference_1(inst):
    assert inst.authenticator.reference == "Organization/organization-example"
    assert inst.author[0].reference == "Practitioner/xcda1"
    assert inst.author[1].reference == "#a2"
    assert inst.contained[0].id == "a2"
    assert inst.contained[0].name.family[0] == "Smitty"
    assert inst.contained[0].name.given[0] == "Gerald"
    assert (
        inst.contained[0].practitionerRole[0].managingOrganization.display
        == "Cleveland Clinic"
    )
    assert inst.contained[0].practitionerRole[0].role.text == "Attending"
    assert inst.contained[0].practitionerRole[0].specialty[0].text == "Orthopedic"
    assert inst.content[0].attachment.contentType == "application/hl7-v3+xml"
    assert inst.content[0].attachment.hash == b"2jmj7l5rSw0yVb/vlWAYkK/YBwk="
    assert inst.content[0].attachment.language == "en-US"
    assert inst.content[0].attachment.size == 3654
    assert (
        inst.content[0].attachment.url
        == "http://example.org/xds/mhd/Binary/07a6483f-732b-461e-86b6-edb665c45510"
    )
    assert inst.content[0].format[0].code == "urn:ihe:pcc:handp:2008"
    assert inst.content[0].format[0].display == "History and Physical Specification"
    assert inst.content[0].format[0].system == "urn:oid:1.3.6.1.4.1.19376.1.2.3"
    assert inst.context.encounter.reference == "Encounter/xcda"
    assert inst.context.event[0].coding[0].code == "T-D8200"
    assert inst.context.event[0].coding[0].display == "Arm"
    assert (
        inst.context.event[0].coding[0].system
        == "http://ihe.net/xds/connectathon/eventCodes"
    )
    assert inst.context.facilityType.coding[0].code == "Outpatient"
    assert inst.context.facilityType.coding[0].display == "Outpatient"
    assert (
        inst.context.facilityType.coding[0].system
        == "http://www.ihe.net/xds/connectathon/healthcareFacilityTypeCodes"
    )
    assert inst.context.period.end == parse_datetime("2004-12-23T08:01:00+11:00")
    assert inst.context.period.start == parse_datetime("2004-12-23T08:00:00+11:00")
    assert inst.context.practiceSetting.coding[0].code == "General Medicine"
    assert inst.context.practiceSetting.coding[0].display == "General Medicine"
    assert (
        inst.context.practiceSetting.coding[0].system
        == "http://www.ihe.net/xds/connectathon/practiceSettingCodes"
    )
    assert inst.context.related[0].identifier.system == "urn:ietf:rfc:3986"
    assert (
        inst.context.related[0].identifier.value
        == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.2345"
    )
    assert inst.context.related[0].ref.reference == "Patient/xcda"
    assert inst.context.sourcePatientInfo.reference == "Patient/xcda"
    assert inst.created == parse_datetime("2005-12-24T09:35:00+11:00")
    assert inst.custodian.reference == "Organization/organization-example"
    assert inst.description == "Physical"
    assert inst.docStatus.coding[0].code == "preliminary"
    assert inst.docStatus.coding[0].display == "preliminary"
    assert inst.docStatus.coding[0].system == "http://hl7.org/fhir/composition-status"
    assert inst.id == "example"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"
    assert inst.indexed == parse_datetime("2005-12-24T09:43:41+11:00")
    assert inst.masterIdentifier.system == "urn:ietf:rfc:3986"
    assert inst.masterIdentifier.value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7"
    assert inst.relatesTo[0].code == "appends"
    assert inst.relatesTo[0].target.reference == "DocumentReference/example"
    assert inst.securityLabel[0].coding[0].code == "V"
    assert inst.securityLabel[0].coding[0].display == "very restricted"
    assert (
        inst.securityLabel[0].coding[0].system
        == "http://hl7.org/fhir/v3/Confidentiality"
    )
    assert inst.status == "current"
    assert inst.subject.reference == "Patient/xcda"
    assert (
        inst.text.div
        == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: example</p><p><b>contained</b>: </p><p><b>masterIdentifier</b>: urn:oid:1.3.6.1.4.1.21367.2005.3.7</p><p><b>identifier</b>: urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234</p><p><b>subject</b>: <a>Patient/xcda</a></p><p><b>type</b>: Outpatient Note <span>(Details : {LOINC code '34108-1' = 'Outpatient Note', given as 'Outpatient Note'})</span></p><p><b>class</b>: History and Physical <span>(Details : {http://ihe.net/xds/connectathon/classCodes code 'History and Physical' = '??', given as 'History and Physical'})</span></p><p><b>author</b>: <a>Practitioner/xcda1</a>, id: a2; Gerald Smitty </p><p><b>custodian</b>: <a>Organization/organization-example</a></p><p><b>authenticator</b>: <a>Organization/organization-example</a></p><p><b>created</b>: 24/12/2005 9:35:00 AM</p><p><b>indexed</b>: 24/12/2005 9:43:41 AM</p><p><b>status</b>: current</p><p><b>docStatus</b>: preliminary <span>(Details : {http://hl7.org/fhir/composition-status code 'preliminary' = 'Preliminary', given as 'preliminary'})</span></p><h3>RelatesTos</h3><table><tr><td>-</td><td><b>Code</b></td><td><b>Target</b></td></tr><tr><td>*</td><td>appends</td><td><a>DocumentReference/example</a></td></tr></table><p><b>description</b>: Physical</p><p><b>securityLabel</b>: very restricted <span>(Details : {http://hl7.org/fhir/v3/Confidentiality code 'V' = 'very restricted', given as 'very restricted'})</span></p><h3>Contents</h3><table><tr><td>-</td><td><b>Attachment</b></td><td><b>Format</b></td></tr><tr><td>*</td><td/><td>History and Physical Specification (Details: urn:oid:1.3.6.1.4.1.19376.1.2.3 code urn:ihe:pcc:handp:2008 = '??', stated as 'History and Physical Specification')</td></tr></table><blockquote><p><b>context</b></p><p><b>encounter</b>: <a>Encounter/xcda</a></p><p><b>event</b>: Arm <span>(Details : {http://ihe.net/xds/connectathon/eventCodes code 'T-D8200' = '??', given as 'Arm'})</span></p><p><b>period</b>: 23/12/2004 8:00:00 AM --&gt; 23/12/2004 8:01:00 AM</p><p><b>facilityType</b>: Outpatient <span>(Details : {http://www.ihe.net/xds/connectathon/healthcareFacilityTypeCodes code 'Outpatient' = '??', given as 'Outpatient'})</span></p><p><b>practiceSetting</b>: General Medicine <span>(Details : {http://www.ihe.net/xds/connectathon/practiceSettingCodes code 'General Medicine' = '??', given as 'General Medicine'})</span></p><p><b>sourcePatientInfo</b>: <a>Patient/xcda</a></p><h3>Relateds</h3><table><tr><td>-</td><td><b>Identifier</b></td><td><b>Ref</b></td></tr><tr><td>*</td><td>urn:oid:1.3.6.1.4.1.21367.2005.3.7.2345</td><td><a>Patient/xcda</a></td></tr></table></blockquote></div>"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "34108-1"
    assert inst.type.coding[0].display == "Outpatient Note"
    assert inst.type.coding[0].system == "http://loinc.org"
