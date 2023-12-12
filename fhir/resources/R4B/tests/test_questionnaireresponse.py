# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/QuestionnaireResponse
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import questionnaireresponse


def impl_questionnaireresponse_1(inst):
    assert inst.author.reference == "#questauth"
    assert inst.authored == fhirtypes.DateTime.validate("2013-02-19T14:15:00-05:00")
    assert inst.basedOn[0].reference == "#order"
    assert inst.contained[0].id == "patsub"
    assert inst.contained[1].id == "order"
    assert inst.contained[2].id == "questauth"
    assert inst.encounter.reference == "Encounter/example"
    assert inst.id == "3141"
    assert (
        inst.identifier.system
        == "http://example.org/fhir/NamingSystem/questionnaire-ids"
    )
    assert inst.identifier.value == "Q12349876"
    assert (
        inst.item[0].item[0].answer[0].item[0].item[0].answer[0].valueCoding.code == "1"
    )
    assert (
        inst.item[0].item[0].answer[0].item[0].item[0].answer[0].valueCoding.system
        == "http://cancer.questionnaire.org/system/code/yesno"
    )
    assert inst.item[0].item[0].answer[0].item[0].item[0].linkId == "1.1.1.1"
    assert (
        inst.item[0].item[0].answer[0].item[0].item[1].answer[0].valueCoding.code == "1"
    )
    assert (
        inst.item[0].item[0].answer[0].item[0].item[1].answer[0].valueCoding.system
        == "http://cancer.questionnaire.org/system/code/yesno"
    )
    assert inst.item[0].item[0].answer[0].item[0].item[1].linkId == "1.1.1.2"
    assert (
        inst.item[0].item[0].answer[0].item[0].item[2].answer[0].valueCoding.code == "0"
    )
    assert (
        inst.item[0].item[0].answer[0].item[0].item[2].answer[0].valueCoding.system
        == "http://cancer.questionnaire.org/system/code/yesno"
    )
    assert inst.item[0].item[0].answer[0].item[0].item[2].linkId == "1.1.1.3"
    assert inst.item[0].item[0].answer[0].item[0].linkId == "1.1.1"
    assert inst.item[0].item[0].answer[0].valueCoding.code == "1"
    assert inst.item[0].item[0].answer[0].valueCoding.display == "Yes"
    assert (
        inst.item[0].item[0].answer[0].valueCoding.system
        == "http://cancer.questionnaire.org/system/code/yesno"
    )
    assert inst.item[0].item[0].linkId == "1.1"
    assert inst.item[0].linkId == "1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.partOf[0].reference == "Procedure/f201"
    assert inst.status == "completed"
    assert inst.subject.reference == "#patsub"
    assert inst.text.status == "generated"


def test_questionnaireresponse_1(base_settings):
    """No. 1 tests collection for QuestionnaireResponse.
    Test File: questionnaireresponse-example.json
    """
    filename = base_settings["unittest_data_dir"] / "questionnaireresponse-example.json"
    inst = questionnaireresponse.QuestionnaireResponse.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "QuestionnaireResponse" == inst.resource_type

    impl_questionnaireresponse_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "QuestionnaireResponse" == data["resourceType"]

    inst2 = questionnaireresponse.QuestionnaireResponse(**data)
    impl_questionnaireresponse_1(inst2)


def impl_questionnaireresponse_2(inst):
    assert inst.authored == fhirtypes.DateTime.validate("2008-01-17")
    assert inst.id == "ussg-fht-answers"
    assert inst.item[0].item[0].answer[0].valueDate == fhirtypes.Date.validate(
        "2008-01-17"
    )
    assert inst.item[0].item[0].linkId == "0.1"
    assert inst.item[0].item[0].text == "Date Done"
    assert inst.item[0].linkId == "0"
    assert inst.item[1].definition == "http://loinc.org/fhir/DataElement/54126-8"
    assert inst.item[1].item[0].item[0].answer[0].valueString == "Annie Proband"
    assert (
        inst.item[1].item[0].item[0].definition
        == "http://loinc.org/fhir/DataElement/54125-0"
    )
    assert inst.item[1].item[0].item[0].linkId == "1.1.1"
    assert inst.item[1].item[0].item[0].text == "Name"
    assert inst.item[1].item[0].item[1].answer[0].valueCoding.code == "LA3-6"
    assert inst.item[1].item[0].item[1].answer[0].valueCoding.display == "Female"
    assert (
        inst.item[1].item[0].item[1].answer[0].valueCoding.system == "http://loinc.org"
    )
    assert (
        inst.item[1].item[0].item[1].definition
        == "http://loinc.org/fhir/DataElement/54131-8"
    )
    assert inst.item[1].item[0].item[1].linkId == "1.1.2"
    assert inst.item[1].item[0].item[1].text == "Gender"
    assert inst.item[1].item[0].item[2].answer[0].valueDate == fhirtypes.Date.validate(
        "1966-04-04"
    )
    assert (
        inst.item[1].item[0].item[2].definition
        == "http://loinc.org/fhir/DataElement/21112-8"
    )
    assert inst.item[1].item[0].item[2].linkId == "1.1.3"
    assert inst.item[1].item[0].item[2].text == "Date of Birth"
    assert inst.item[1].item[0].item[3].answer[0].valueCoding.code == "LA32-8"
    assert inst.item[1].item[0].item[3].answer[0].valueCoding.display == "No"
    assert (
        inst.item[1].item[0].item[3].answer[0].valueCoding.system == "http://loinc.org"
    )
    assert (
        inst.item[1].item[0].item[3].definition
        == "http://loinc.org/fhir/DataElement/54132-6"
    )
    assert inst.item[1].item[0].item[3].linkId == "1.1.4"
    assert inst.item[1].item[0].item[3].text == "Were you born a twin?"
    assert inst.item[1].item[0].item[4].answer[0].valueCoding.code == "LA32-8"
    assert inst.item[1].item[0].item[4].answer[0].valueCoding.display == "No"
    assert (
        inst.item[1].item[0].item[4].answer[0].valueCoding.system == "http://loinc.org"
    )
    assert (
        inst.item[1].item[0].item[4].definition
        == "http://loinc.org/fhir/DataElement/54128-4"
    )
    assert inst.item[1].item[0].item[4].linkId == "1.1.5"
    assert inst.item[1].item[0].item[4].text == "Were you adopted?"
    assert inst.item[1].item[0].item[5].answer[0].valueCoding.code == "LA32-8"
    assert inst.item[1].item[0].item[5].answer[0].valueCoding.display == "No"
    assert (
        inst.item[1].item[0].item[5].answer[0].valueCoding.system == "http://loinc.org"
    )
    assert (
        inst.item[1].item[0].item[5].definition
        == "http://loinc.org/fhir/DataElement/54135-9"
    )
    assert inst.item[1].item[0].item[5].linkId == "1.1.6"
    assert inst.item[1].item[0].item[5].text == (
        "Are your parents related to each other in any way other than" " marriage?"
    )
    assert (
        inst.item[1]
        .item[0]
        .item[6]
        .answer[0]
        .item[0]
        .item[0]
        .answer[0]
        .valueCoding.code
        == "[in_i]"
    )
    assert (
        inst.item[1]
        .item[0]
        .item[6]
        .answer[0]
        .item[0]
        .item[0]
        .answer[0]
        .valueCoding.display
        == "inches"
    )
    assert (
        inst.item[1]
        .item[0]
        .item[6]
        .answer[0]
        .item[0]
        .item[0]
        .answer[0]
        .valueCoding.system
        == "http://unitsofmeasure.org"
    )
    assert inst.item[1].item[0].item[6].answer[0].item[0].item[0].linkId == "1.1.7.1.1"
    assert inst.item[1].item[0].item[6].answer[0].item[0].item[0].text == "Units"
    assert inst.item[1].item[0].item[6].answer[0].item[0].linkId == "1.1.7.1"
    assert float(inst.item[1].item[0].item[6].answer[0].valueDecimal) == float(63)
    assert (
        inst.item[1].item[0].item[6].definition
        == "http://loinc.org/fhir/DataElement/8302-2"
    )
    assert inst.item[1].item[0].item[6].linkId == "1.1.7"
    assert inst.item[1].item[0].item[6].text == "Height"
    assert (
        inst.item[1]
        .item[0]
        .item[7]
        .answer[0]
        .item[0]
        .item[0]
        .answer[0]
        .valueCoding.code
        == "[lb_av]"
    )
    assert (
        inst.item[1]
        .item[0]
        .item[7]
        .answer[0]
        .item[0]
        .item[0]
        .answer[0]
        .valueCoding.display
        == "pounds"
    )
    assert (
        inst.item[1]
        .item[0]
        .item[7]
        .answer[0]
        .item[0]
        .item[0]
        .answer[0]
        .valueCoding.system
        == "http://unitsofmeasure.org"
    )
    assert inst.item[1].item[0].item[7].answer[0].item[0].item[0].linkId == "1.1.8.1.1"
    assert inst.item[1].item[0].item[7].answer[0].item[0].item[0].text == "Units"
    assert inst.item[1].item[0].item[7].answer[0].item[0].linkId == "1.1.8.1"
    assert float(inst.item[1].item[0].item[7].answer[0].valueDecimal) == float(127)
    assert (
        inst.item[1].item[0].item[7].definition
        == "http://loinc.org/fhir/DataElement/29463-7"
    )
    assert inst.item[1].item[0].item[7].linkId == "1.1.8"
    assert inst.item[1].item[0].item[7].text == "Weight"
    assert float(inst.item[1].item[0].item[8].answer[0].valueDecimal) == float(22.5)
    assert (
        inst.item[1].item[0].item[8].definition
        == "http://loinc.org/fhir/DataElement/39156-5"
    )
    assert inst.item[1].item[0].item[8].linkId == "1.1.9"
    assert inst.item[1].item[0].item[8].text == "Body mass index (BMI) [Ratio]"
    assert inst.item[1].item[0].item[9].answer[0].valueCoding.code == "LA4457-3"
    assert inst.item[1].item[0].item[9].answer[0].valueCoding.display == "White"
    assert (
        inst.item[1].item[0].item[9].answer[0].valueCoding.system == "http://loinc.org"
    )
    assert (
        inst.item[1].item[0].item[9].definition
        == "http://loinc.org/fhir/DataElement/54134-2"
    )
    assert inst.item[1].item[0].item[9].linkId == "1.1.10"
    assert inst.item[1].item[0].item[9].text == "Race"
    assert inst.item[1].item[0].linkId == "1.1"
    assert inst.item[1].linkId == "1"
    assert inst.item[1].text == "Your health information"
    assert inst.item[2].definition == "http://loinc.org/fhir/DataElement/54114-4"
    assert inst.item[2].item[0].item[0].answer[0].valueCoding.code == "LA10405-1"
    assert inst.item[2].item[0].item[0].answer[0].valueCoding.display == "Daughter"
    assert (
        inst.item[2].item[0].item[0].answer[0].valueCoding.system == "http://loinc.org"
    )
    assert (
        inst.item[2].item[0].item[0].definition
        == "http://loinc.org/fhir/DataElement/54136-7"
    )
    assert inst.item[2].item[0].item[0].linkId == "2.1.1.1"
    assert inst.item[2].item[0].item[0].text == "Relationship to you"
    assert inst.item[2].item[0].item[1].answer[0].valueString == "Susan"
    assert (
        inst.item[2].item[0].item[1].definition
        == "http://loinc.org/fhir/DataElement/54138-3"
    )
    assert inst.item[2].item[0].item[1].linkId == "2.1.1.2"
    assert inst.item[2].item[0].item[1].text == "Name"
    assert inst.item[2].item[0].item[2].answer[0].valueCoding.code == "LA3-6"
    assert inst.item[2].item[0].item[2].answer[0].valueCoding.display == "Female"
    assert (
        inst.item[2].item[0].item[2].answer[0].valueCoding.system == "http://loinc.org"
    )
    assert (
        inst.item[2].item[0].item[2].definition
        == "http://loinc.org/fhir/DataElement/54123-5"
    )
    assert inst.item[2].item[0].item[2].linkId == "2.1.1.3"
    assert inst.item[2].item[0].item[2].text == "Gender"
    assert float(
        inst.item[2].item[0].item[3].answer[0].item[0].item[0].answer[0].valueDecimal
    ) == float(17)
    assert (
        inst.item[2].item[0].item[3].answer[0].item[0].item[0].definition
        == "http://loinc.org/fhir/DataElement/54141-7"
    )
    assert (
        inst.item[2].item[0].item[3].answer[0].item[0].item[0].linkId == "2.1.1.4.2.2"
    )
    assert inst.item[2].item[0].item[3].answer[0].item[0].item[0].text == "Age"
    assert inst.item[2].item[0].item[3].answer[0].item[0].linkId == "2.1.1.4.2"
    assert inst.item[2].item[0].item[3].answer[0].valueCoding.code == "LA33-6"
    assert inst.item[2].item[0].item[3].answer[0].valueCoding.display == "Yes"
    assert (
        inst.item[2].item[0].item[3].answer[0].valueCoding.system == "http://loinc.org"
    )
    assert (
        inst.item[2].item[0].item[3].definition
        == "http://loinc.org/fhir/DataElement/54139-1"
    )
    assert inst.item[2].item[0].item[3].linkId == "2.1.1.4"
    assert inst.item[2].item[0].item[3].text == "Living?"
    assert inst.item[2].item[0].item[4].answer[0].valueCoding.code == "LA32-8"
    assert inst.item[2].item[0].item[4].answer[0].valueCoding.display == "No"
    assert (
        inst.item[2].item[0].item[4].answer[0].valueCoding.system == "http://loinc.org"
    )
    assert (
        inst.item[2].item[0].item[4].definition
        == "http://loinc.org/fhir/DataElement/54121-9"
    )
    assert inst.item[2].item[0].item[4].linkId == "2.1.1.5"
    assert inst.item[2].item[0].item[4].text == "Was this person born a twin?"
    assert inst.item[2].item[0].item[5].answer[0].valueCoding.code == "LA32-8"
    assert inst.item[2].item[0].item[5].answer[0].valueCoding.display == "No"
    assert (
        inst.item[2].item[0].item[5].answer[0].valueCoding.system == "http://loinc.org"
    )
    assert (
        inst.item[2].item[0].item[5].definition
        == "http://loinc.org/fhir/DataElement/54122-7"
    )
    assert inst.item[2].item[0].item[5].linkId == "2.1.1.6"
    assert inst.item[2].item[0].item[5].text == "Was this person adopted?"
    assert inst.item[2].item[0].linkId == "2.1"
    assert (
        inst.item[2].item[1].item[0].item[0].answer[0].valueCoding.code == "LA10415-0"
    )
    assert (
        inst.item[2].item[1].item[0].item[0].answer[0].valueCoding.display == "Brother"
    )
    assert (
        inst.item[2].item[1].item[0].item[0].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[1].item[0].item[0].definition
        == "http://loinc.org/fhir/DataElement/54136-7"
    )
    assert inst.item[2].item[1].item[0].item[0].linkId == "2.1.1.1"
    assert inst.item[2].item[1].item[0].item[0].text == "Relationship to you"
    assert inst.item[2].item[1].item[0].item[1].answer[0].valueString == "Brian"
    assert (
        inst.item[2].item[1].item[0].item[1].definition
        == "http://loinc.org/fhir/DataElement/54138-3"
    )
    assert inst.item[2].item[1].item[0].item[1].linkId == "2.1.1.2"
    assert inst.item[2].item[1].item[0].item[1].text == "Name"
    assert inst.item[2].item[1].item[0].item[2].answer[0].valueCoding.code == "LA2-8"
    assert inst.item[2].item[1].item[0].item[2].answer[0].valueCoding.display == "Male"
    assert (
        inst.item[2].item[1].item[0].item[2].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[1].item[0].item[2].definition
        == "http://loinc.org/fhir/DataElement/54123-5"
    )
    assert inst.item[2].item[1].item[0].item[2].linkId == "2.1.1.3"
    assert inst.item[2].item[1].item[0].item[2].text == "Gender"
    assert float(
        inst.item[2]
        .item[1]
        .item[0]
        .item[3]
        .answer[0]
        .item[0]
        .item[0]
        .answer[0]
        .valueDecimal
    ) == float(32)
    assert (
        inst.item[2].item[1].item[0].item[3].answer[0].item[0].item[0].definition
        == "http://loinc.org/fhir/DataElement/54141-7"
    )
    assert (
        inst.item[2].item[1].item[0].item[3].answer[0].item[0].item[0].linkId
        == "2.1.1.4.2.2"
    )
    assert inst.item[2].item[1].item[0].item[3].answer[0].item[0].item[0].text == "Age"
    assert inst.item[2].item[1].item[0].item[3].answer[0].item[0].linkId == "2.1.1.4.2"
    assert inst.item[2].item[1].item[0].item[3].answer[0].valueCoding.code == "LA33-6"
    assert inst.item[2].item[1].item[0].item[3].answer[0].valueCoding.display == "Yes"
    assert (
        inst.item[2].item[1].item[0].item[3].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[1].item[0].item[3].definition
        == "http://loinc.org/fhir/DataElement/54139-1"
    )
    assert inst.item[2].item[1].item[0].item[3].linkId == "2.1.1.4"
    assert inst.item[2].item[1].item[0].item[3].text == "Living?"
    assert inst.item[2].item[1].item[0].item[4].answer[0].valueCoding.code == "LA32-8"
    assert inst.item[2].item[1].item[0].item[4].answer[0].valueCoding.display == "No"
    assert (
        inst.item[2].item[1].item[0].item[4].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[1].item[0].item[4].definition
        == "http://loinc.org/fhir/DataElement/54121-9"
    )
    assert inst.item[2].item[1].item[0].item[4].linkId == "2.1.1.5"
    assert inst.item[2].item[1].item[0].item[4].text == "Was this person born a twin?"
    assert inst.item[2].item[1].item[0].item[5].answer[0].valueCoding.code == "LA32-8"
    assert inst.item[2].item[1].item[0].item[5].answer[0].valueCoding.display == "No"
    assert (
        inst.item[2].item[1].item[0].item[5].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[1].item[0].item[5].definition
        == "http://loinc.org/fhir/DataElement/54122-7"
    )
    assert inst.item[2].item[1].item[0].item[5].linkId == "2.1.1.6"
    assert inst.item[2].item[1].item[0].item[5].text == "Was this person adopted?"
    assert inst.item[2].item[1].item[0].linkId == "2.1.1"
    assert (
        inst.item[2].item[1].item[1].item[0].answer[0].valueCoding.code == "LA10550-4"
    )
    assert (
        inst.item[2].item[1].item[1].item[0].answer[0].valueCoding.display
        == "-- Other Cancer"
    )
    assert (
        inst.item[2].item[1].item[1].item[0].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert inst.item[2].item[1].item[1].item[0].linkId == "2.1.2.1"
    assert inst.item[2].item[1].item[1].item[0].text == "Disease or Condition"
    assert (
        inst.item[2].item[1].item[1].item[1].answer[0].valueCoding.code == "LA10397-0"
    )
    assert inst.item[2].item[1].item[1].item[1].answer[0].valueCoding.display == "30-39"
    assert (
        inst.item[2].item[1].item[1].item[1].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert inst.item[2].item[1].item[1].item[1].linkId == "2.1.2.2"
    assert inst.item[2].item[1].item[1].item[1].text == "Age at Diagnosis"
    assert inst.item[2].item[1].item[1].linkId == "2.1.2"
    assert (
        inst.item[2].item[1].item[1].text == "This family member's history of disease"
    )
    assert inst.item[2].item[1].linkId == "2.1"
    assert (
        inst.item[2].item[2].item[0].item[0].answer[0].valueCoding.code == "LA10418-4"
    )
    assert (
        inst.item[2].item[2].item[0].item[0].answer[0].valueCoding.display == "Sister"
    )
    assert (
        inst.item[2].item[2].item[0].item[0].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[2].item[0].item[0].definition
        == "http://loinc.org/fhir/DataElement/54136-7"
    )
    assert inst.item[2].item[2].item[0].item[0].linkId == "2.1.1.1"
    assert inst.item[2].item[2].item[0].item[0].text == "Relationship to you"
    assert inst.item[2].item[2].item[0].item[1].answer[0].valueString == "Janet"
    assert (
        inst.item[2].item[2].item[0].item[1].definition
        == "http://loinc.org/fhir/DataElement/54138-3"
    )
    assert inst.item[2].item[2].item[0].item[1].linkId == "2.1.1.2"
    assert inst.item[2].item[2].item[0].item[1].text == "Name"
    assert inst.item[2].item[2].item[0].item[2].answer[0].valueCoding.code == "LA3-6"
    assert (
        inst.item[2].item[2].item[0].item[2].answer[0].valueCoding.display == "Female"
    )
    assert (
        inst.item[2].item[2].item[0].item[2].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[2].item[0].item[2].definition
        == "http://loinc.org/fhir/DataElement/54123-5"
    )
    assert inst.item[2].item[2].item[0].item[2].linkId == "2.1.1.3"
    assert inst.item[2].item[2].item[0].item[2].text == "Gender"
    assert float(
        inst.item[2]
        .item[2]
        .item[0]
        .item[3]
        .answer[0]
        .item[0]
        .item[0]
        .answer[0]
        .valueDecimal
    ) == float(36)
    assert (
        inst.item[2].item[2].item[0].item[3].answer[0].item[0].item[0].definition
        == "http://loinc.org/fhir/DataElement/54141-7"
    )
    assert (
        inst.item[2].item[2].item[0].item[3].answer[0].item[0].item[0].linkId
        == "2.1.1.4.2.2"
    )
    assert inst.item[2].item[2].item[0].item[3].answer[0].item[0].item[0].text == "Age"
    assert inst.item[2].item[2].item[0].item[3].answer[0].item[0].linkId == "2.1.1.4.2"
    assert inst.item[2].item[2].item[0].item[3].answer[0].valueCoding.code == "LA33-6"
    assert inst.item[2].item[2].item[0].item[3].answer[0].valueCoding.display == "Yes"
    assert (
        inst.item[2].item[2].item[0].item[3].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[2].item[0].item[3].definition
        == "http://loinc.org/fhir/DataElement/54139-1"
    )
    assert inst.item[2].item[2].item[0].item[3].linkId == "2.1.1.4"
    assert inst.item[2].item[2].item[0].item[3].text == "Living?"
    assert inst.item[2].item[2].item[0].item[4].answer[0].valueCoding.code == "LA32-8"
    assert inst.item[2].item[2].item[0].item[4].answer[0].valueCoding.display == "No"
    assert (
        inst.item[2].item[2].item[0].item[4].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[2].item[0].item[4].definition
        == "http://loinc.org/fhir/DataElement/54121-9"
    )
    assert inst.item[2].item[2].item[0].item[4].linkId == "2.1.1.5"
    assert inst.item[2].item[2].item[0].item[4].text == "Was this person born a twin?"
    assert inst.item[2].item[2].item[0].item[5].answer[0].valueCoding.code == "LA32-8"
    assert inst.item[2].item[2].item[0].item[5].answer[0].valueCoding.display == "No"
    assert (
        inst.item[2].item[2].item[0].item[5].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[2].item[0].item[5].definition
        == "http://loinc.org/fhir/DataElement/54122-7"
    )
    assert inst.item[2].item[2].item[0].item[5].linkId == "2.1.1.6"
    assert inst.item[2].item[2].item[0].item[5].text == "Was this person adopted?"
    assert inst.item[2].item[2].item[0].linkId == "2.1.1"
    assert (
        inst.item[2].item[2].item[1].item[0].answer[0].valueCoding.code == "LA10536-3"
    )
    assert (
        inst.item[2].item[2].item[1].item[0].answer[0].valueCoding.display
        == "-- Breast Cancer"
    )
    assert (
        inst.item[2].item[2].item[1].item[0].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert inst.item[2].item[2].item[1].item[0].linkId == "2.1.2.1"
    assert inst.item[2].item[2].item[1].item[0].text == "Disease or Condition"
    assert (
        inst.item[2].item[2].item[1].item[1].answer[0].valueCoding.code == "LA10397-0"
    )
    assert inst.item[2].item[2].item[1].item[1].answer[0].valueCoding.display == "30-39"
    assert (
        inst.item[2].item[2].item[1].item[1].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert inst.item[2].item[2].item[1].item[1].linkId == "2.1.2.2"
    assert inst.item[2].item[2].item[1].item[1].text == "Age at Diagnosis"
    assert inst.item[2].item[2].item[1].linkId == "2.1.2"
    assert (
        inst.item[2].item[2].item[1].text == "This family member's history of disease"
    )
    assert inst.item[2].item[2].linkId == "2.1"
    assert (
        inst.item[2].item[3].item[0].item[0].answer[0].valueCoding.code == "LA10419-2"
    )
    assert (
        inst.item[2].item[3].item[0].item[0].answer[0].valueCoding.display == "Nephew"
    )
    assert (
        inst.item[2].item[3].item[0].item[0].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[3].item[0].item[0].definition
        == "http://loinc.org/fhir/DataElement/54136-7"
    )
    assert inst.item[2].item[3].item[0].item[0].linkId == "2.1.1.1"
    assert inst.item[2].item[3].item[0].item[0].text == "Relationship to you"
    assert inst.item[2].item[3].item[0].item[1].answer[0].valueString == "Ian"
    assert (
        inst.item[2].item[3].item[0].item[1].definition
        == "http://loinc.org/fhir/DataElement/54138-3"
    )
    assert inst.item[2].item[3].item[0].item[1].linkId == "2.1.1.2"
    assert inst.item[2].item[3].item[0].item[1].text == "Name"
    assert inst.item[2].item[3].item[0].item[2].answer[0].valueCoding.code == "LA2-8"
    assert inst.item[2].item[3].item[0].item[2].answer[0].valueCoding.display == "Male"
    assert (
        inst.item[2].item[3].item[0].item[2].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[3].item[0].item[2].definition
        == "http://loinc.org/fhir/DataElement/54123-5"
    )
    assert inst.item[2].item[3].item[0].item[2].linkId == "2.1.1.3"
    assert inst.item[2].item[3].item[0].item[2].text == "Gender"
    assert float(
        inst.item[2]
        .item[3]
        .item[0]
        .item[3]
        .answer[0]
        .item[0]
        .item[0]
        .answer[0]
        .valueDecimal
    ) == float(16)
    assert (
        inst.item[2].item[3].item[0].item[3].answer[0].item[0].item[0].definition
        == "http://loinc.org/fhir/DataElement/54141-7"
    )
    assert (
        inst.item[2].item[3].item[0].item[3].answer[0].item[0].item[0].linkId
        == "2.1.1.4.2.2"
    )
    assert inst.item[2].item[3].item[0].item[3].answer[0].item[0].item[0].text == "Age"
    assert inst.item[2].item[3].item[0].item[3].answer[0].item[0].linkId == "2.1.1.4.2"
    assert inst.item[2].item[3].item[0].item[3].answer[0].valueCoding.code == "LA33-6"
    assert inst.item[2].item[3].item[0].item[3].answer[0].valueCoding.display == "Yes"
    assert (
        inst.item[2].item[3].item[0].item[3].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[3].item[0].item[3].definition
        == "http://loinc.org/fhir/DataElement/54139-1"
    )
    assert inst.item[2].item[3].item[0].item[3].linkId == "2.1.1.4"
    assert inst.item[2].item[3].item[0].item[3].text == "Living?"
    assert inst.item[2].item[3].item[0].item[4].answer[0].valueCoding.code == "LA32-8"
    assert inst.item[2].item[3].item[0].item[4].answer[0].valueCoding.display == "No"
    assert (
        inst.item[2].item[3].item[0].item[4].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[3].item[0].item[4].definition
        == "http://loinc.org/fhir/DataElement/54121-9"
    )
    assert inst.item[2].item[3].item[0].item[4].linkId == "2.1.1.5"
    assert inst.item[2].item[3].item[0].item[4].text == "Was this person born a twin?"
    assert inst.item[2].item[3].item[0].item[5].answer[0].valueCoding.code == "LA32-8"
    assert inst.item[2].item[3].item[0].item[5].answer[0].valueCoding.display == "No"
    assert (
        inst.item[2].item[3].item[0].item[5].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[3].item[0].item[5].definition
        == "http://loinc.org/fhir/DataElement/54122-7"
    )
    assert inst.item[2].item[3].item[0].item[5].linkId == "2.1.1.6"
    assert inst.item[2].item[3].item[0].item[5].text == "Was this person adopted?"
    assert inst.item[2].item[3].item[0].linkId == "2.1.1"
    assert inst.item[2].item[3].linkId == "2.1"
    assert (
        inst.item[2].item[4].item[0].item[0].answer[0].valueCoding.code == "LA10420-0"
    )
    assert inst.item[2].item[4].item[0].item[0].answer[0].valueCoding.display == "Niece"
    assert (
        inst.item[2].item[4].item[0].item[0].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[4].item[0].item[0].definition
        == "http://loinc.org/fhir/DataElement/54136-7"
    )
    assert inst.item[2].item[4].item[0].item[0].linkId == "2.1.1.1"
    assert inst.item[2].item[4].item[0].item[0].text == "Relationship to you"
    assert inst.item[2].item[4].item[0].item[1].answer[0].valueString == "Helen"
    assert (
        inst.item[2].item[4].item[0].item[1].definition
        == "http://loinc.org/fhir/DataElement/54138-3"
    )
    assert inst.item[2].item[4].item[0].item[1].linkId == "2.1.1.2"
    assert inst.item[2].item[4].item[0].item[1].text == "Name"
    assert inst.item[2].item[4].item[0].item[2].answer[0].valueCoding.code == "LA3-6"
    assert (
        inst.item[2].item[4].item[0].item[2].answer[0].valueCoding.display == "Female"
    )
    assert (
        inst.item[2].item[4].item[0].item[2].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[4].item[0].item[2].definition
        == "http://loinc.org/fhir/DataElement/54123-5"
    )
    assert inst.item[2].item[4].item[0].item[2].linkId == "2.1.1.3"
    assert inst.item[2].item[4].item[0].item[2].text == "Gender"
    assert float(
        inst.item[2]
        .item[4]
        .item[0]
        .item[3]
        .answer[0]
        .item[0]
        .item[0]
        .answer[0]
        .valueDecimal
    ) == float(15)
    assert (
        inst.item[2].item[4].item[0].item[3].answer[0].item[0].item[0].definition
        == "http://loinc.org/fhir/DataElement/54141-7"
    )
    assert (
        inst.item[2].item[4].item[0].item[3].answer[0].item[0].item[0].linkId
        == "2.1.1.4.2.2"
    )
    assert inst.item[2].item[4].item[0].item[3].answer[0].item[0].item[0].text == "Age"
    assert inst.item[2].item[4].item[0].item[3].answer[0].item[0].linkId == "2.1.1.4.2"
    assert inst.item[2].item[4].item[0].item[3].answer[0].valueCoding.code == "LA33-6"
    assert inst.item[2].item[4].item[0].item[3].answer[0].valueCoding.display == "Yes"
    assert (
        inst.item[2].item[4].item[0].item[3].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[4].item[0].item[3].definition
        == "http://loinc.org/fhir/DataElement/54139-1"
    )
    assert inst.item[2].item[4].item[0].item[3].linkId == "2.1.1.4"
    assert inst.item[2].item[4].item[0].item[3].text == "Living?"
    assert inst.item[2].item[4].item[0].item[4].answer[0].valueCoding.code == "LA32-8"
    assert inst.item[2].item[4].item[0].item[4].answer[0].valueCoding.display == "No"
    assert (
        inst.item[2].item[4].item[0].item[4].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[4].item[0].item[4].definition
        == "http://loinc.org/fhir/DataElement/54121-9"
    )
    assert inst.item[2].item[4].item[0].item[4].linkId == "2.1.1.5"
    assert inst.item[2].item[4].item[0].item[4].text == "Was this person born a twin?"
    assert inst.item[2].item[4].item[0].item[5].answer[0].valueCoding.code == "LA32-8"
    assert inst.item[2].item[4].item[0].item[5].answer[0].valueCoding.display == "No"
    assert (
        inst.item[2].item[4].item[0].item[5].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[4].item[0].item[5].definition
        == "http://loinc.org/fhir/DataElement/54122-7"
    )
    assert inst.item[2].item[4].item[0].item[5].linkId == "2.1.1.6"
    assert inst.item[2].item[4].item[0].item[5].text == "Was this person adopted?"
    assert inst.item[2].item[4].item[0].linkId == "2.1.1"
    assert inst.item[2].item[4].linkId == "2.1"
    assert (
        inst.item[2].item[5].item[0].item[0].answer[0].valueCoding.code == "LA10416-8"
    )
    assert (
        inst.item[2].item[5].item[0].item[0].answer[0].valueCoding.display == "Father"
    )
    assert (
        inst.item[2].item[5].item[0].item[0].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[5].item[0].item[0].definition
        == "http://loinc.org/fhir/DataElement/54136-7"
    )
    assert inst.item[2].item[5].item[0].item[0].linkId == "2.1.1.1"
    assert inst.item[2].item[5].item[0].item[0].text == "Relationship to you"
    assert inst.item[2].item[5].item[0].item[1].answer[0].valueString == "Donald"
    assert (
        inst.item[2].item[5].item[0].item[1].definition
        == "http://loinc.org/fhir/DataElement/54138-3"
    )
    assert inst.item[2].item[5].item[0].item[1].linkId == "2.1.1.2"
    assert inst.item[2].item[5].item[0].item[1].text == "Name"
    assert inst.item[2].item[5].item[0].item[2].answer[0].valueCoding.code == "LA2-8"
    assert inst.item[2].item[5].item[0].item[2].answer[0].valueCoding.display == "Male"
    assert (
        inst.item[2].item[5].item[0].item[2].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[5].item[0].item[2].definition
        == "http://loinc.org/fhir/DataElement/54123-5"
    )
    assert inst.item[2].item[5].item[0].item[2].linkId == "2.1.1.3"
    assert inst.item[2].item[5].item[0].item[2].text == "Gender"
    assert float(
        inst.item[2]
        .item[5]
        .item[0]
        .item[3]
        .answer[0]
        .item[0]
        .item[0]
        .answer[0]
        .valueDecimal
    ) == float(52)
    assert (
        inst.item[2].item[5].item[0].item[3].answer[0].item[0].item[0].definition
        == "http://loinc.org/fhir/DataElement/54141-7"
    )
    assert (
        inst.item[2].item[5].item[0].item[3].answer[0].item[0].item[0].linkId
        == "2.1.1.4.2.2"
    )
    assert inst.item[2].item[5].item[0].item[3].answer[0].item[0].item[0].text == "Age"
    assert inst.item[2].item[5].item[0].item[3].answer[0].item[0].linkId == "2.1.1.4.2"
    assert inst.item[2].item[5].item[0].item[3].answer[0].valueCoding.code == "LA33-6"
    assert inst.item[2].item[5].item[0].item[3].answer[0].valueCoding.display == "Yes"
    assert (
        inst.item[2].item[5].item[0].item[3].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[5].item[0].item[3].definition
        == "http://loinc.org/fhir/DataElement/54139-1"
    )
    assert inst.item[2].item[5].item[0].item[3].linkId == "2.1.1.4"
    assert inst.item[2].item[5].item[0].item[3].text == "Living?"
    assert inst.item[2].item[5].item[0].item[4].answer[0].valueCoding.code == "LA32-8"
    assert inst.item[2].item[5].item[0].item[4].answer[0].valueCoding.display == "No"
    assert (
        inst.item[2].item[5].item[0].item[4].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[5].item[0].item[4].definition
        == "http://loinc.org/fhir/DataElement/54121-9"
    )
    assert inst.item[2].item[5].item[0].item[4].linkId == "2.1.1.5"
    assert inst.item[2].item[5].item[0].item[4].text == "Was this person born a twin?"
    assert inst.item[2].item[5].item[0].item[5].answer[0].valueCoding.code == "LA32-8"
    assert inst.item[2].item[5].item[0].item[5].answer[0].valueCoding.display == "No"
    assert (
        inst.item[2].item[5].item[0].item[5].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[5].item[0].item[5].definition
        == "http://loinc.org/fhir/DataElement/54122-7"
    )
    assert inst.item[2].item[5].item[0].item[5].linkId == "2.1.1.6"
    assert inst.item[2].item[5].item[0].item[5].text == "Was this person adopted?"
    assert inst.item[2].item[5].item[0].linkId == "2.1.1"
    assert inst.item[2].item[5].linkId == "2.1"
    assert (
        inst.item[2].item[6].item[0].item[0].answer[0].valueCoding.code == "LA10425-9"
    )
    assert (
        inst.item[2].item[6].item[0].item[0].answer[0].valueCoding.display
        == "Paternal Uncle"
    )
    assert (
        inst.item[2].item[6].item[0].item[0].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[6].item[0].item[0].definition
        == "http://loinc.org/fhir/DataElement/54136-7"
    )
    assert inst.item[2].item[6].item[0].item[0].linkId == "2.1.1.1"
    assert inst.item[2].item[6].item[0].item[0].text == "Relationship to you"
    assert inst.item[2].item[6].item[0].item[1].answer[0].valueString == "Eric"
    assert (
        inst.item[2].item[6].item[0].item[1].definition
        == "http://loinc.org/fhir/DataElement/54138-3"
    )
    assert inst.item[2].item[6].item[0].item[1].linkId == "2.1.1.2"
    assert inst.item[2].item[6].item[0].item[1].text == "Name"
    assert inst.item[2].item[6].item[0].item[2].answer[0].valueCoding.code == "LA2-8"
    assert inst.item[2].item[6].item[0].item[2].answer[0].valueCoding.display == "Male"
    assert (
        inst.item[2].item[6].item[0].item[2].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[6].item[0].item[2].definition
        == "http://loinc.org/fhir/DataElement/54123-5"
    )
    assert inst.item[2].item[6].item[0].item[2].linkId == "2.1.1.3"
    assert inst.item[2].item[6].item[0].item[2].text == "Gender"
    assert float(
        inst.item[2]
        .item[6]
        .item[0]
        .item[3]
        .answer[0]
        .item[0]
        .item[0]
        .answer[0]
        .valueDecimal
    ) == float(56)
    assert (
        inst.item[2].item[6].item[0].item[3].answer[0].item[0].item[0].definition
        == "http://loinc.org/fhir/DataElement/54141-7"
    )
    assert (
        inst.item[2].item[6].item[0].item[3].answer[0].item[0].item[0].linkId
        == "2.1.1.4.2.2"
    )
    assert inst.item[2].item[6].item[0].item[3].answer[0].item[0].item[0].text == "Age"
    assert inst.item[2].item[6].item[0].item[3].answer[0].item[0].linkId == "2.1.1.4.2"
    assert inst.item[2].item[6].item[0].item[3].answer[0].valueCoding.code == "LA33-6"
    assert inst.item[2].item[6].item[0].item[3].answer[0].valueCoding.display == "Yes"
    assert (
        inst.item[2].item[6].item[0].item[3].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[6].item[0].item[3].definition
        == "http://loinc.org/fhir/DataElement/54139-1"
    )
    assert inst.item[2].item[6].item[0].item[3].linkId == "2.1.1.4"
    assert inst.item[2].item[6].item[0].item[3].text == "Living?"
    assert inst.item[2].item[6].item[0].item[4].answer[0].valueCoding.code == "LA32-8"
    assert inst.item[2].item[6].item[0].item[4].answer[0].valueCoding.display == "No"
    assert (
        inst.item[2].item[6].item[0].item[4].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[6].item[0].item[4].definition
        == "http://loinc.org/fhir/DataElement/54121-9"
    )
    assert inst.item[2].item[6].item[0].item[4].linkId == "2.1.1.5"
    assert inst.item[2].item[6].item[0].item[4].text == "Was this person born a twin?"
    assert inst.item[2].item[6].item[0].item[5].answer[0].valueCoding.code == "LA32-8"
    assert inst.item[2].item[6].item[0].item[5].answer[0].valueCoding.display == "No"
    assert (
        inst.item[2].item[6].item[0].item[5].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[6].item[0].item[5].definition
        == "http://loinc.org/fhir/DataElement/54122-7"
    )
    assert inst.item[2].item[6].item[0].item[5].linkId == "2.1.1.6"
    assert inst.item[2].item[6].item[0].item[5].text == "Was this person adopted?"
    assert inst.item[2].item[6].item[0].linkId == "2.1.1"
    assert inst.item[2].item[6].linkId == "2.1"
    assert (
        inst.item[2].item[7].item[0].item[0].answer[0].valueCoding.code == "LA10421-8"
    )
    assert (
        inst.item[2].item[7].item[0].item[0].answer[0].valueCoding.display
        == "Paternal Aunt"
    )
    assert (
        inst.item[2].item[7].item[0].item[0].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[7].item[0].item[0].definition
        == "http://loinc.org/fhir/DataElement/54136-7"
    )
    assert inst.item[2].item[7].item[0].item[0].linkId == "2.1.1.1"
    assert inst.item[2].item[7].item[0].item[0].text == "Relationship to you"
    assert inst.item[2].item[7].item[0].item[1].answer[0].valueString == "Fiona"
    assert (
        inst.item[2].item[7].item[0].item[1].definition
        == "http://loinc.org/fhir/DataElement/54138-3"
    )
    assert inst.item[2].item[7].item[0].item[1].linkId == "2.1.1.2"
    assert inst.item[2].item[7].item[0].item[1].text == "Name"
    assert inst.item[2].item[7].item[0].item[2].answer[0].valueCoding.code == "LA3-6"
    assert (
        inst.item[2].item[7].item[0].item[2].answer[0].valueCoding.display == "Female"
    )
    assert (
        inst.item[2].item[7].item[0].item[2].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[7].item[0].item[2].definition
        == "http://loinc.org/fhir/DataElement/54123-5"
    )
    assert inst.item[2].item[7].item[0].item[2].linkId == "2.1.1.3"
    assert inst.item[2].item[7].item[0].item[2].text == "Gender"
    assert float(
        inst.item[2]
        .item[7]
        .item[0]
        .item[3]
        .answer[0]
        .item[0]
        .item[0]
        .answer[0]
        .valueDecimal
    ) == float(57)
    assert (
        inst.item[2].item[7].item[0].item[3].answer[0].item[0].item[0].definition
        == "http://loinc.org/fhir/DataElement/54141-7"
    )
    assert (
        inst.item[2].item[7].item[0].item[3].answer[0].item[0].item[0].linkId
        == "2.1.1.4.2.2"
    )
    assert inst.item[2].item[7].item[0].item[3].answer[0].item[0].item[0].text == "Age"
    assert inst.item[2].item[7].item[0].item[3].answer[0].item[0].linkId == "2.1.1.4.2"
    assert inst.item[2].item[7].item[0].item[3].answer[0].valueCoding.code == "LA33-6"
    assert inst.item[2].item[7].item[0].item[3].answer[0].valueCoding.display == "Yes"
    assert (
        inst.item[2].item[7].item[0].item[3].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[7].item[0].item[3].definition
        == "http://loinc.org/fhir/DataElement/54139-1"
    )
    assert inst.item[2].item[7].item[0].item[3].linkId == "2.1.1.4"
    assert inst.item[2].item[7].item[0].item[3].text == "Living?"
    assert inst.item[2].item[7].item[0].item[4].answer[0].valueCoding.code == "LA32-8"
    assert inst.item[2].item[7].item[0].item[4].answer[0].valueCoding.display == "No"
    assert (
        inst.item[2].item[7].item[0].item[4].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[7].item[0].item[4].definition
        == "http://loinc.org/fhir/DataElement/54121-9"
    )
    assert inst.item[2].item[7].item[0].item[4].linkId == "2.1.1.5"
    assert inst.item[2].item[7].item[0].item[4].text == "Was this person born a twin?"
    assert inst.item[2].item[7].item[0].item[5].answer[0].valueCoding.code == "LA32-8"
    assert inst.item[2].item[7].item[0].item[5].answer[0].valueCoding.display == "No"
    assert (
        inst.item[2].item[7].item[0].item[5].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[7].item[0].item[5].definition
        == "http://loinc.org/fhir/DataElement/54122-7"
    )
    assert inst.item[2].item[7].item[0].item[5].linkId == "2.1.1.6"
    assert inst.item[2].item[7].item[0].item[5].text == "Was this person adopted?"
    assert inst.item[2].item[7].item[0].linkId == "2.1.1"
    assert (
        inst.item[2].item[7].item[1].item[0].answer[0].valueCoding.code == "LA10543-9"
    )
    assert (
        inst.item[2].item[7].item[1].item[0].answer[0].valueCoding.display
        == "-- Skin Cancer"
    )
    assert (
        inst.item[2].item[7].item[1].item[0].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert inst.item[2].item[7].item[1].item[0].linkId == "2.1.2.1"
    assert inst.item[2].item[7].item[1].item[0].text == "Disease or Condition"
    assert inst.item[2].item[7].item[1].linkId == "2.1.2"
    assert (
        inst.item[2].item[7].item[1].text == "This family member's history of disease"
    )
    assert inst.item[2].item[7].linkId == "2.1"
    assert (
        inst.item[2].item[8].item[0].item[0].answer[0].valueCoding.code == "LA10423-4"
    )
    assert (
        inst.item[2].item[8].item[0].item[0].answer[0].valueCoding.display
        == "Paternal Grandfather"
    )
    assert (
        inst.item[2].item[8].item[0].item[0].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[8].item[0].item[0].definition
        == "http://loinc.org/fhir/DataElement/54136-7"
    )
    assert inst.item[2].item[8].item[0].item[0].linkId == "2.1.1.1"
    assert inst.item[2].item[8].item[0].item[0].text == "Relationship to you"
    assert inst.item[2].item[8].item[0].item[1].answer[0].valueString == "Bob"
    assert (
        inst.item[2].item[8].item[0].item[1].definition
        == "http://loinc.org/fhir/DataElement/54138-3"
    )
    assert inst.item[2].item[8].item[0].item[1].linkId == "2.1.1.2"
    assert inst.item[2].item[8].item[0].item[1].text == "Name"
    assert inst.item[2].item[8].item[0].item[2].answer[0].valueCoding.code == "LA2-8"
    assert inst.item[2].item[8].item[0].item[2].answer[0].valueCoding.display == "Male"
    assert (
        inst.item[2].item[8].item[0].item[2].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[8].item[0].item[2].definition
        == "http://loinc.org/fhir/DataElement/54123-5"
    )
    assert inst.item[2].item[8].item[0].item[2].linkId == "2.1.1.3"
    assert inst.item[2].item[8].item[0].item[2].text == "Gender"
    assert (
        inst.item[2]
        .item[8]
        .item[0]
        .item[3]
        .answer[0]
        .item[0]
        .item[0]
        .answer[0]
        .valueCoding.code
        == "LA10537-1"
    )
    assert (
        inst.item[2]
        .item[8]
        .item[0]
        .item[3]
        .answer[0]
        .item[0]
        .item[0]
        .answer[0]
        .valueCoding.display
        == "-- Colon Cancer"
    )
    assert (
        inst.item[2]
        .item[8]
        .item[0]
        .item[3]
        .answer[0]
        .item[0]
        .item[0]
        .answer[0]
        .valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[8].item[0].item[3].answer[0].item[0].item[0].definition
        == "http://loinc.org/fhir/DataElement/54112-8"
    )
    assert (
        inst.item[2].item[8].item[0].item[3].answer[0].item[0].item[0].linkId
        == "2.1.1.4.1.1"
    )
    assert (
        inst.item[2].item[8].item[0].item[3].answer[0].item[0].item[0].text
        == "Cause of Death"
    )
    assert (
        inst.item[2]
        .item[8]
        .item[0]
        .item[3]
        .answer[0]
        .item[0]
        .item[1]
        .answer[0]
        .valueCoding.code
        == "LA10400-2"
    )
    assert (
        inst.item[2]
        .item[8]
        .item[0]
        .item[3]
        .answer[0]
        .item[0]
        .item[1]
        .answer[0]
        .valueCoding.display
        == "OVER 60"
    )
    assert (
        inst.item[2]
        .item[8]
        .item[0]
        .item[3]
        .answer[0]
        .item[0]
        .item[1]
        .answer[0]
        .valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[8].item[0].item[3].answer[0].item[0].item[1].definition
        == "http://loinc.org/fhir/DataElement/54113-6"
    )
    assert (
        inst.item[2].item[8].item[0].item[3].answer[0].item[0].item[1].linkId
        == "2.1.1.4.1.2"
    )
    assert (
        inst.item[2].item[8].item[0].item[3].answer[0].item[0].item[1].text
        == "Age at Death"
    )
    assert inst.item[2].item[8].item[0].item[3].answer[0].item[0].linkId == "2.1.1.4.1"
    assert inst.item[2].item[8].item[0].item[3].answer[0].valueCoding.code == "LA32-8"
    assert inst.item[2].item[8].item[0].item[3].answer[0].valueCoding.display == "No"
    assert (
        inst.item[2].item[8].item[0].item[3].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[8].item[0].item[3].definition
        == "http://loinc.org/fhir/DataElement/54139-1"
    )
    assert inst.item[2].item[8].item[0].item[3].linkId == "2.1.1.4"
    assert inst.item[2].item[8].item[0].item[3].text == "Living?"
    assert inst.item[2].item[8].item[0].item[4].answer[0].valueCoding.code == "LA32-8"
    assert inst.item[2].item[8].item[0].item[4].answer[0].valueCoding.display == "No"
    assert (
        inst.item[2].item[8].item[0].item[4].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[8].item[0].item[4].definition
        == "http://loinc.org/fhir/DataElement/54121-9"
    )
    assert inst.item[2].item[8].item[0].item[4].linkId == "2.1.1.5"
    assert inst.item[2].item[8].item[0].item[4].text == "Was this person born a twin?"
    assert inst.item[2].item[8].item[0].item[5].answer[0].valueCoding.code == "LA32-8"
    assert inst.item[2].item[8].item[0].item[5].answer[0].valueCoding.display == "No"
    assert (
        inst.item[2].item[8].item[0].item[5].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[8].item[0].item[5].definition
        == "http://loinc.org/fhir/DataElement/54122-7"
    )
    assert inst.item[2].item[8].item[0].item[5].linkId == "2.1.1.6"
    assert inst.item[2].item[8].item[0].item[5].text == "Was this person adopted?"
    assert inst.item[2].item[8].item[0].linkId == "2.1.1"
    assert (
        inst.item[2].item[8].item[1].item[0].answer[0].valueCoding.code == "LA10537-1"
    )
    assert (
        inst.item[2].item[8].item[1].item[0].answer[0].valueCoding.display
        == "-- Colon Cancer"
    )
    assert (
        inst.item[2].item[8].item[1].item[0].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert inst.item[2].item[8].item[1].item[0].linkId == "2.1.2.1"
    assert inst.item[2].item[8].item[1].item[0].text == "Disease or Condition"
    assert (
        inst.item[2].item[8].item[1].item[1].answer[0].valueCoding.code == "LA10400-2"
    )
    assert (
        inst.item[2].item[8].item[1].item[1].answer[0].valueCoding.display == "OVER 60"
    )
    assert (
        inst.item[2].item[8].item[1].item[1].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert inst.item[2].item[8].item[1].item[1].linkId == "2.1.2.2"
    assert inst.item[2].item[8].item[1].item[1].text == "Age at Diagnosis"
    assert inst.item[2].item[8].item[1].linkId == "2.1.2"
    assert (
        inst.item[2].item[8].item[1].text == "This family member's history of disease"
    )
    assert inst.item[2].item[8].linkId == "2.1"
    assert (
        inst.item[2].item[9].item[0].item[0].answer[0].valueCoding.code == "LA10424-2"
    )
    assert (
        inst.item[2].item[9].item[0].item[0].answer[0].valueCoding.display
        == "Paternal Grandmother"
    )
    assert (
        inst.item[2].item[9].item[0].item[0].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[9].item[0].item[0].definition
        == "http://loinc.org/fhir/DataElement/54136-7"
    )
    assert inst.item[2].item[9].item[0].item[0].linkId == "2.1.1.1"
    assert inst.item[2].item[9].item[0].item[0].text == "Relationship to you"
    assert inst.item[2].item[9].item[0].item[1].answer[0].valueString == "Claire"
    assert (
        inst.item[2].item[9].item[0].item[1].definition
        == "http://loinc.org/fhir/DataElement/54138-3"
    )
    assert inst.item[2].item[9].item[0].item[1].linkId == "2.1.1.2"
    assert inst.item[2].item[9].item[0].item[1].text == "Name"
    assert inst.item[2].item[9].item[0].item[2].answer[0].valueCoding.code == "LA3-6"
    assert (
        inst.item[2].item[9].item[0].item[2].answer[0].valueCoding.display == "Female"
    )
    assert (
        inst.item[2].item[9].item[0].item[2].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[9].item[0].item[2].definition
        == "http://loinc.org/fhir/DataElement/54123-5"
    )
    assert inst.item[2].item[9].item[0].item[2].linkId == "2.1.1.3"
    assert inst.item[2].item[9].item[0].item[2].text == "Gender"
    assert (
        inst.item[2]
        .item[9]
        .item[0]
        .item[3]
        .answer[0]
        .item[0]
        .item[0]
        .answer[0]
        .item[0]
        .answer[0]
        .valueString
        == "Lou Gehrigs"
    )
    assert (
        inst.item[2]
        .item[9]
        .item[0]
        .item[3]
        .answer[0]
        .item[0]
        .item[0]
        .answer[0]
        .item[0]
        .linkId
        == "2.1.1.4.1.1.1"
    )
    assert (
        inst.item[2]
        .item[9]
        .item[0]
        .item[3]
        .answer[0]
        .item[0]
        .item[0]
        .answer[0]
        .item[0]
        .text
        == "Please specify"
    )
    assert (
        inst.item[2]
        .item[9]
        .item[0]
        .item[3]
        .answer[0]
        .item[0]
        .item[0]
        .answer[0]
        .valueCoding.code
        == "LA10589-2"
    )
    assert (
        inst.item[2]
        .item[9]
        .item[0]
        .item[3]
        .answer[0]
        .item[0]
        .item[0]
        .answer[0]
        .valueCoding.display
        == "-- Other/Unexpected"
    )
    assert (
        inst.item[2]
        .item[9]
        .item[0]
        .item[3]
        .answer[0]
        .item[0]
        .item[0]
        .answer[0]
        .valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[9].item[0].item[3].answer[0].item[0].item[0].definition
        == "http://loinc.org/fhir/DataElement/54112-8"
    )
    assert (
        inst.item[2].item[9].item[0].item[3].answer[0].item[0].item[0].linkId
        == "2.1.1.4.1.1"
    )
    assert (
        inst.item[2].item[9].item[0].item[3].answer[0].item[0].item[0].text
        == "Cause of Death"
    )
    assert (
        inst.item[2]
        .item[9]
        .item[0]
        .item[3]
        .answer[0]
        .item[0]
        .item[1]
        .answer[0]
        .valueCoding.code
        == "LA10400-2"
    )
    assert (
        inst.item[2]
        .item[9]
        .item[0]
        .item[3]
        .answer[0]
        .item[0]
        .item[1]
        .answer[0]
        .valueCoding.display
        == "OVER 60"
    )
    assert (
        inst.item[2]
        .item[9]
        .item[0]
        .item[3]
        .answer[0]
        .item[0]
        .item[1]
        .answer[0]
        .valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[9].item[0].item[3].answer[0].item[0].item[1].definition
        == "http://loinc.org/fhir/DataElement/54113-6"
    )
    assert (
        inst.item[2].item[9].item[0].item[3].answer[0].item[0].item[1].linkId
        == "2.1.1.4.1.2"
    )
    assert (
        inst.item[2].item[9].item[0].item[3].answer[0].item[0].item[1].text
        == "Age at Death"
    )
    assert inst.item[2].item[9].item[0].item[3].answer[0].item[0].linkId == "2.1.1.4.1"
    assert inst.item[2].item[9].item[0].item[3].answer[0].valueCoding.code == "LA32-8"
    assert inst.item[2].item[9].item[0].item[3].answer[0].valueCoding.display == "No"
    assert (
        inst.item[2].item[9].item[0].item[3].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[9].item[0].item[3].definition
        == "http://loinc.org/fhir/DataElement/54139-1"
    )
    assert inst.item[2].item[9].item[0].item[3].linkId == "2.1.1.4"
    assert inst.item[2].item[9].item[0].item[3].text == "Living?"
    assert inst.item[2].item[9].item[0].item[4].answer[0].valueCoding.code == "LA32-8"
    assert inst.item[2].item[9].item[0].item[4].answer[0].valueCoding.display == "No"
    assert (
        inst.item[2].item[9].item[0].item[4].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[9].item[0].item[4].definition
        == "http://loinc.org/fhir/DataElement/54121-9"
    )
    assert inst.item[2].item[9].item[0].item[4].linkId == "2.1.1.5"
    assert inst.item[2].item[9].item[0].item[4].text == "Was this person born a twin?"
    assert inst.item[2].item[9].item[0].item[5].answer[0].valueCoding.code == "LA32-8"
    assert inst.item[2].item[9].item[0].item[5].answer[0].valueCoding.display == "No"
    assert (
        inst.item[2].item[9].item[0].item[5].answer[0].valueCoding.system
        == "http://loinc.org"
    )
    assert (
        inst.item[2].item[9].item[0].item[5].definition
        == "http://loinc.org/fhir/DataElement/54122-7"
    )
    assert inst.item[2].item[9].item[0].item[5].linkId == "2.1.1.6"
    assert inst.item[2].item[9].item[0].item[5].text == "Was this person adopted?"
    assert inst.item[2].item[9].item[0].linkId == "2.1.1"
    assert inst.item[2].item[9].linkId == "2.1"
    assert inst.item[2].linkId == "2"
    assert inst.item[2].text == "Family member health information"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.questionnaire == "http://hl7.org/fhir/Questionnaire/ussg-fht"
    assert inst.status == "in-progress"
    assert inst.subject.reference == "http://hl7.org/fhir/Patient/proband"
    assert inst.subject.type == "Patient"
    assert inst.text.status == "generated"


def test_questionnaireresponse_2(base_settings):
    """No. 2 tests collection for QuestionnaireResponse.
    Test File: questionnaireresponse-example-ussg-fht-answers.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "questionnaireresponse-example-ussg-fht-answers.json"
    )
    inst = questionnaireresponse.QuestionnaireResponse.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "QuestionnaireResponse" == inst.resource_type

    impl_questionnaireresponse_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "QuestionnaireResponse" == data["resourceType"]

    inst2 = questionnaireresponse.QuestionnaireResponse(**data)
    impl_questionnaireresponse_2(inst2)


def impl_questionnaireresponse_3(inst):
    assert inst.author.reference == "Practitioner/f201"
    assert inst.authored == fhirtypes.DateTime.validate("2013-06-18T00:00:00+01:00")
    assert inst.id == "f201"
    assert inst.item[0].item[0].answer[0].valueString == "I am allergic to house dust"
    assert inst.item[0].item[0].linkId == "1.1"
    assert inst.item[0].item[0].text == "Do you have allergies?"
    assert inst.item[0].linkId == "1"
    assert inst.item[1].item[0].answer[0].valueString == "Male"
    assert inst.item[1].item[0].linkId == "2.1"
    assert inst.item[1].item[0].text == "What is your gender?"
    assert inst.item[1].item[1].answer[0].valueDate == fhirtypes.Date.validate(
        "1960-03-13"
    )
    assert inst.item[1].item[1].linkId == "2.2"
    assert inst.item[1].item[1].text == "What is your date of birth?"
    assert inst.item[1].item[2].answer[0].valueString == "The Netherlands"
    assert inst.item[1].item[2].linkId == "2.3"
    assert inst.item[1].item[2].text == "What is your country of birth?"
    assert inst.item[1].item[3].answer[0].valueString == "married"
    assert inst.item[1].item[3].linkId == "2.4"
    assert inst.item[1].item[3].text == "What is your marital status?"
    assert inst.item[1].linkId == "2"
    assert inst.item[1].text == "General questions"
    assert inst.item[2].item[0].answer[0].valueString == "No"
    assert inst.item[2].item[0].linkId == "3.1"
    assert inst.item[2].item[0].text == "Do you smoke?"
    assert inst.item[2].item[1].answer[0].valueString == "No, but I used to drink"
    assert inst.item[2].item[1].linkId == "3.2"
    assert inst.item[2].item[1].text == "Do you drink alchohol?"
    assert inst.item[2].linkId == "3"
    assert inst.item[2].text == "Intoxications"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.source.reference == "Practitioner/f201"
    assert inst.status == "completed"
    assert inst.subject.display == "Roel"
    assert inst.subject.reference == "Patient/f201"
    assert inst.text.status == "generated"


def test_questionnaireresponse_3(base_settings):
    """No. 3 tests collection for QuestionnaireResponse.
    Test File: questionnaireresponse-example-f201-lifelines.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "questionnaireresponse-example-f201-lifelines.json"
    )
    inst = questionnaireresponse.QuestionnaireResponse.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "QuestionnaireResponse" == inst.resource_type

    impl_questionnaireresponse_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "QuestionnaireResponse" == data["resourceType"]

    inst2 = questionnaireresponse.QuestionnaireResponse(**data)
    impl_questionnaireresponse_3(inst2)


def impl_questionnaireresponse_4(inst):
    assert inst.author.reference == "http://hl7.org/fhir/Practitioner/example"
    assert inst.author.type == "Practitioner"
    assert inst.authored == fhirtypes.DateTime.validate("2013-02-19T14:15:00+10:00")
    assert inst.id == "bb"
    assert inst.item[0].item[0].item[0].answer[0].valueString == "Cathy Jones"
    assert inst.item[0].item[0].item[0].linkId == "nameOfChild"
    assert inst.item[0].item[0].item[0].text == "Name of child"
    assert inst.item[0].item[0].item[1].answer[0].valueCoding.code == "f"
    assert inst.item[0].item[0].item[1].linkId == "sex"
    assert inst.item[0].item[0].item[1].text == "Sex"
    assert inst.item[0].item[0].linkId == "group"
    assert float(inst.item[0].item[1].item[0].answer[0].valueDecimal) == float(3.25)
    assert inst.item[0].item[1].item[0].linkId == "birthWeight"
    assert inst.item[0].item[1].item[0].text == "Birth weight (kg)"
    assert float(inst.item[0].item[1].item[1].answer[0].valueDecimal) == float(44.3)
    assert inst.item[0].item[1].item[1].linkId == "birthLength"
    assert inst.item[0].item[1].item[1].text == "Birth length (cm)"
    assert inst.item[0].item[1].item[2].answer[0].item[0].item[0].answer[
        0
    ].valueDate == fhirtypes.Date.validate("1972-11-30")
    assert (
        inst.item[0].item[1].item[2].answer[0].item[0].item[0].linkId == "vitaminKDose1"
    )
    assert inst.item[0].item[1].item[2].answer[0].item[0].item[0].text == "1st dose"
    assert inst.item[0].item[1].item[2].answer[0].item[0].item[1].answer[
        0
    ].valueDate == fhirtypes.Date.validate("1972-12-11")
    assert (
        inst.item[0].item[1].item[2].answer[0].item[0].item[1].linkId == "vitaminKDose2"
    )
    assert inst.item[0].item[1].item[2].answer[0].item[0].item[1].text == "2nd dose"
    assert inst.item[0].item[1].item[2].answer[0].item[0].linkId == "vitaminKgivenDoses"
    assert inst.item[0].item[1].item[2].answer[0].valueCoding.code == "INJECTION"
    assert inst.item[0].item[1].item[2].linkId == "vitaminKgiven"
    assert inst.item[0].item[1].item[2].text == "Vitamin K given"
    assert inst.item[0].item[1].item[3].answer[0].item[0].answer[
        0
    ].valueDate == fhirtypes.Date.validate("1972-12-04")
    assert inst.item[0].item[1].item[3].answer[0].item[0].linkId == "hepBgivenDate"
    assert inst.item[0].item[1].item[3].answer[0].item[0].text == "Date given"
    assert inst.item[0].item[1].item[3].answer[0].valueBoolean is True
    assert inst.item[0].item[1].item[3].linkId == "hepBgiven"
    assert inst.item[0].item[1].item[3].text == "Hep B given y / n"
    assert (
        inst.item[0].item[1].item[4].answer[0].valueString
        == "Already able to speak Chinese"
    )
    assert inst.item[0].item[1].item[4].linkId == "abnormalitiesAtBirth"
    assert inst.item[0].item[1].item[4].text == "Abnormalities noted at birth"
    assert inst.item[0].item[1].linkId == "neonatalInformation"
    assert inst.item[0].item[1].text == "Neonatal Information"
    assert inst.item[0].linkId == "birthDetails"
    assert inst.item[0].text == "Birth details - To be completed by health professional"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "completed"
    assert inst.subject.reference == "http://hl7.org/fhir/Patient/1"
    assert inst.subject.type == "Patient"
    assert inst.text.status == "generated"


def test_questionnaireresponse_4(base_settings):
    """No. 4 tests collection for QuestionnaireResponse.
    Test File: questionnaireresponse-example-bluebook.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "questionnaireresponse-example-bluebook.json"
    )
    inst = questionnaireresponse.QuestionnaireResponse.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "QuestionnaireResponse" == inst.resource_type

    impl_questionnaireresponse_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "QuestionnaireResponse" == data["resourceType"]

    inst2 = questionnaireresponse.QuestionnaireResponse(**data)
    impl_questionnaireresponse_4(inst2)


def impl_questionnaireresponse_5(inst):
    assert inst.authored == fhirtypes.DateTime.validate("2014-12-11T04:44:16Z")
    assert inst.id == "gcs"
    assert inst.item[0].answer[0].valueCoding.code == "LA6560-2"
    assert inst.item[0].answer[0].valueCoding.display == "Confused"
    assert (
        inst.item[0].answer[0].valueCoding.extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/ordinalValue"
    )
    assert float(inst.item[0].answer[0].valueCoding.extension[0].valueDecimal) == float(
        4
    )
    assert inst.item[0].answer[0].valueCoding.system == "http://loinc.org"
    assert inst.item[0].linkId == "1.1"
    assert inst.item[1].answer[0].valueCoding.code == "LA6566-9"
    assert inst.item[1].answer[0].valueCoding.display == "Localizing pain"
    assert (
        inst.item[1].answer[0].valueCoding.extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/ordinalValue"
    )
    assert float(inst.item[1].answer[0].valueCoding.extension[0].valueDecimal) == float(
        5
    )
    assert inst.item[1].answer[0].valueCoding.system == "http://loinc.org"
    assert inst.item[1].linkId == "1.2"
    assert inst.item[2].answer[0].valueCoding.code == "LA6556-0"
    assert inst.item[2].answer[0].valueCoding.display == "Eyes open spontaneously"
    assert (
        inst.item[2].answer[0].valueCoding.extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/ordinalValue"
    )
    assert float(inst.item[2].answer[0].valueCoding.extension[0].valueDecimal) == float(
        4
    )
    assert inst.item[2].answer[0].valueCoding.system == "http://loinc.org"
    assert inst.item[2].linkId == "1.3"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.questionnaire == "http://hl7.org/fhir/Questionnaire/gcs"
    assert inst.source.reference == "Practitioner/f007"
    assert inst.status == "completed"
    assert inst.subject.display == "Peter James Chalmers"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_questionnaireresponse_5(base_settings):
    """No. 5 tests collection for QuestionnaireResponse.
    Test File: questionnaireresponse-example-gcs.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "questionnaireresponse-example-gcs.json"
    )
    inst = questionnaireresponse.QuestionnaireResponse.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "QuestionnaireResponse" == inst.resource_type

    impl_questionnaireresponse_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "QuestionnaireResponse" == data["resourceType"]

    inst2 = questionnaireresponse.QuestionnaireResponse(**data)
    impl_questionnaireresponse_5(inst2)
