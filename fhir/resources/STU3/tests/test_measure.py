# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Measure
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import measure


def impl_measure_1(inst):
    assert inst.date == fhirtypes.DateTime.validate("2015-03-08")
    assert inst.description == (
        "Exclusive breastfeeding measure of outcomes for exclusive "
        "breastmilk feeding of newborns."
    )
    assert inst.group[0].identifier.value == "Population Group 1"
    assert inst.group[0].population[0].code.coding[0].code == "initial-population"
    assert inst.group[0].population[0].criteria == "InitialPopulation1"
    assert (
        inst.group[0].population[0].identifier.value
        == "initial-population-1-identifier"
    )
    assert inst.group[0].population[1].code.coding[0].code == "denominator"
    assert inst.group[0].population[1].criteria == "Denominator1"
    assert inst.group[0].population[1].identifier.value == "denominator-1-identifier"
    assert inst.group[0].population[2].code.coding[0].code == "denominator-exclusions"
    assert inst.group[0].population[2].criteria == "DenominatorExclusions1"
    assert (
        inst.group[0].population[2].identifier.value
        == "denominator-exclusions-1-identifier"
    )
    assert inst.group[0].population[3].code.coding[0].code == "numerator"
    assert inst.group[0].population[3].criteria == "Numerator1"
    assert inst.group[0].population[3].identifier.value == "numerator-1-identifier"
    assert inst.group[1].identifier.value == "Population Group 2"
    assert inst.group[1].population[0].code.coding[0].code == "initial-population"
    assert inst.group[1].population[0].criteria == "InitialPopulation2"
    assert (
        inst.group[1].population[0].identifier.value
        == "initial-population-2-identifier"
    )
    assert inst.group[1].population[1].code.coding[0].code == "denominator"
    assert inst.group[1].population[1].criteria == "Denominator2"
    assert inst.group[1].population[1].identifier.value == "denominator-2-identifier"
    assert inst.group[1].population[2].code.coding[0].code == "denominator-exclusion"
    assert inst.group[1].population[2].criteria == "DenominatorExclusions2"
    assert (
        inst.group[1].population[2].identifier.value
        == "denominator-exclusions-2-identifier"
    )
    assert inst.group[1].population[3].code.coding[0].code == "numerator"
    assert inst.group[1].population[3].criteria == "Numerator2"
    assert inst.group[1].population[3].identifier.value == "numerator-2-identifier"
    assert inst.id == "measure-exclusive-breastfeeding"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "exclusive-breastfeeding-measure"
    assert inst.improvementNotation == "Improvement noted as an increase in the rate"
    assert (
        inst.library[0].reference == "Library/library-exclusive-breastfeeding-cqm-logic"
    )
    assert inst.purpose == (
        "Measure of newborns who were fed breast milk only since " "birth"
    )
    assert inst.relatedArtifact[0].citation == (
        "American Academy of Pediatrics. (2005). Section on "
        "Breastfeeding. Policy Statement:Breastfeeding and the Use of"
        " Human Milk. Pediatrics.115:496-506."
    )
    assert inst.relatedArtifact[0].type == "documentation"
    assert inst.relatedArtifact[1].type == "documentation"
    assert inst.relatedArtifact[2].type == "documentation"
    assert inst.relatedArtifact[3].type == "documentation"
    assert inst.relatedArtifact[4].type == "documentation"
    assert inst.relatedArtifact[5].type == "documentation"
    assert inst.relatedArtifact[6].citation == (
        "Kramer, M.S. & Kakuma, R. (2002).Optimal duration of "
        "exclusive breastfeeding. [107 refs] Cochrane Database of "
        "Systematic Reviews. (1):CD003517."
    )
    assert inst.relatedArtifact[6].type == "documentation"
    assert inst.relatedArtifact[7].citation == (
        "Petrova, A., Hegyi, T., & Mehta, R. (2007). Maternal "
        "race/ethnicity and one-month exclusive breastfeeding in "
        "association with the in-hospital feeding modality. "
        "Breastfeeding Medicine. 2(2):92-8."
    )
    assert inst.relatedArtifact[7].type == "documentation"
    assert inst.relatedArtifact[8].type == "documentation"
    assert inst.relatedArtifact[9].type == "documentation"
    assert inst.scoring.coding[0].code == "proportion"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Exclusive Breastfeeding Measure"
    assert inst.topic[0].text == "Exclusive Breastfeeding"
    assert inst.type[0].coding[0].code == "process"
    assert inst.version == "4.0.0"


def test_measure_1(base_settings):
    """No. 1 tests collection for Measure.
    Test File: measure-exclusive-breastfeeding.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "measure-exclusive-breastfeeding.json"
    )
    inst = measure.Measure.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Measure" == inst.resource_type

    impl_measure_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Measure" == data["resourceType"]

    inst2 = measure.Measure(**data)
    impl_measure_1(inst2)


def impl_measure_2(inst):
    assert inst.group[0].identifier.value == "Main"
    assert inst.group[0].population[0].code.coding[0].code == "initial-population"
    assert inst.group[0].population[0].criteria == "Initial Population"
    assert inst.group[0].population[1].code.coding[0].code == "denominator"
    assert inst.group[0].population[1].criteria == "Denominator"
    assert inst.group[0].population[2].code.coding[0].code == "numerator"
    assert inst.group[0].population[2].criteria == "Numerator"
    assert inst.id == "component-b-example"
    assert inst.scoring.coding[0].code == "proportion"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Screening for Depression"


def test_measure_2(base_settings):
    """No. 2 tests collection for Measure.
    Test File: measure-component-b-example.json
    """
    filename = base_settings["unittest_data_dir"] / "measure-component-b-example.json"
    inst = measure.Measure.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Measure" == inst.resource_type

    impl_measure_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Measure" == data["resourceType"]

    inst2 = measure.Measure(**data)
    impl_measure_2(inst2)


def impl_measure_3(inst):
    assert inst.date == fhirtypes.DateTime.validate("2014-03-08")
    assert inst.description == (
        "Exclusive breastfeeding measure of outcomes for exclusive "
        "breastmilk feeding of newborns."
    )
    assert inst.group[0].identifier.value == "Population Group 1"
    assert inst.group[0].population[0].code.coding[0].code == "initial-population"
    assert inst.group[0].population[0].criteria == "InitialPopulation1"
    assert (
        inst.group[0].population[0].identifier.value
        == "initial-population-1-identifier"
    )
    assert inst.group[0].population[1].code.coding[0].code == "denominator"
    assert inst.group[0].population[1].criteria == "Denominator1"
    assert inst.group[0].population[1].identifier.value == "denominator-1-identifier"
    assert inst.group[0].population[2].code.coding[0].code == "denominator-exclusions"
    assert inst.group[0].population[2].criteria == "DenominatorExclusions1"
    assert (
        inst.group[0].population[2].identifier.value
        == "denominator-exclusions-1-identifier"
    )
    assert inst.group[0].population[3].code.coding[0].code == "numerator"
    assert inst.group[0].population[3].criteria == "Numerator1"
    assert inst.group[0].population[3].identifier.value == "numerator-1-identifier"
    assert inst.group[1].identifier.value == "Population Group 2"
    assert inst.group[1].population[0].code.coding[0].code == "initial-population"
    assert inst.group[1].population[0].criteria == "InitialPopulation2"
    assert (
        inst.group[1].population[0].identifier.value
        == "initial-population-2-identifier"
    )
    assert inst.group[1].population[1].code.coding[0].code == "denominator"
    assert inst.group[1].population[1].criteria == "Denominator2"
    assert inst.group[1].population[1].identifier.value == "denominator-2-identifier"
    assert inst.group[1].population[2].code.coding[0].code == "denominator-exclusion"
    assert inst.group[1].population[2].criteria == "DenominatorExclusions2"
    assert (
        inst.group[1].population[2].identifier.value
        == "denominator-exclusions-2-identifier"
    )
    assert inst.group[1].population[3].code.coding[0].code == "numerator"
    assert inst.group[1].population[3].criteria == "Numerator2"
    assert inst.group[1].population[3].identifier.value == "numerator-2-identifier"
    assert inst.id == "measure-predecessor-example"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "exclusive-breastfeeding-measure"
    assert inst.improvementNotation == "Improvement noted as an increase in the rate"
    assert (
        inst.library[0].reference == "Library/library-exclusive-breastfeeding-cqm-logic"
    )
    assert inst.purpose == (
        "Measure of newborns who were fed breast milk only since " "birth"
    )
    assert inst.relatedArtifact[0].citation == (
        "American Academy of Pediatrics. (2005). Section on "
        "Breastfeeding. Policy Statement:Breastfeeding and the Use of"
        " Human Milk. Pediatrics.115:496-506."
    )
    assert inst.relatedArtifact[0].type == "documentation"
    assert inst.relatedArtifact[1].type == "documentation"
    assert inst.relatedArtifact[2].type == "documentation"
    assert inst.relatedArtifact[3].type == "documentation"
    assert inst.relatedArtifact[4].type == "documentation"
    assert inst.relatedArtifact[5].type == "documentation"
    assert inst.relatedArtifact[6].citation == (
        "Kramer, M.S. & Kakuma, R. (2002).Optimal duration of "
        "exclusive breastfeeding. [107 refs] Cochrane Database of "
        "Systematic Reviews. (1):CD003517."
    )
    assert inst.relatedArtifact[6].type == "documentation"
    assert inst.relatedArtifact[7].citation == (
        "Petrova, A., Hegyi, T., & Mehta, R. (2007). Maternal "
        "race/ethnicity and one-month exclusive breastfeeding in "
        "association with the in-hospital feeding modality. "
        "Breastfeeding Medicine. 2(2):92-8."
    )
    assert inst.relatedArtifact[7].type == "documentation"
    assert inst.relatedArtifact[8].type == "documentation"
    assert inst.relatedArtifact[9].type == "documentation"
    assert inst.scoring.coding[0].code == "proportion"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Exclusive Breastfeeding Measure"
    assert inst.topic[0].text == "Exclusive Breastfeeding"
    assert inst.type[0].coding[0].code == "process"
    assert inst.version == "3.0.1"


def test_measure_3(base_settings):
    """No. 3 tests collection for Measure.
    Test File: measure-predecessor-example.json
    """
    filename = base_settings["unittest_data_dir"] / "measure-predecessor-example.json"
    inst = measure.Measure.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Measure" == inst.resource_type

    impl_measure_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Measure" == data["resourceType"]

    inst2 = measure.Measure(**data)
    impl_measure_3(inst2)


def impl_measure_4(inst):
    assert inst.approvalDate == fhirtypes.Date.validate("2016-01-01")
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://www.ncqa.org/"
    assert inst.contributor[0].name == "National Committee for Quality Assurance"
    assert inst.contributor[0].type == "author"
    assert inst.date == fhirtypes.DateTime.validate("2017-03-10")
    assert inst.description == (
        "Percentage of children 3-18 years of age who were diagnosed "
        "with pharyngitis, ordered an antibiotic and received a group"
        " A streptococcus (strep) test for the episode."
    )
    assert inst.effectivePeriod.end == fhirtypes.DateTime.validate("2017-12-31")
    assert inst.effectivePeriod.start == fhirtypes.DateTime.validate("2017-01-01")
    assert inst.experimental is True
    assert inst.group[0].identifier.value == "CMS146-group-1"
    assert inst.group[0].population[0].code.coding[0].code == "initial-population"
    assert inst.group[0].population[0].criteria == "CMS146.InInitialPopulation"
    assert (
        inst.group[0].population[0].identifier.value == "initial-population-identifier"
    )
    assert inst.group[0].population[1].code.coding[0].code == "numerator"
    assert inst.group[0].population[1].criteria == "CMS146.InNumerator"
    assert inst.group[0].population[1].identifier.value == "numerator-identifier"
    assert inst.group[0].population[2].code.coding[0].code == "denominator"
    assert inst.group[0].population[2].criteria == "CMS146.InDenominator"
    assert inst.group[0].population[2].identifier.value == "denominator-identifier"
    assert inst.group[0].population[3].code.coding[0].code == "denominator-exclusion"
    assert inst.group[0].population[3].criteria == "CMS146.InDenominatorExclusions"
    assert (
        inst.group[0].population[3].identifier.value
        == "denominator-exclusions-identifier"
    )
    assert inst.group[0].stratifier[0].criteria == "CMS146.AgesUpToNine"
    assert inst.group[0].stratifier[0].identifier.value == "stratifier-ages-up-to-9"
    assert inst.group[0].stratifier[1].criteria == "CMS146.AgesTenPlus"
    assert inst.group[0].stratifier[1].identifier.value == "stratifier-ages-10-plus"
    assert inst.group[0].stratifier[2].identifier.value == "stratifier-ages-up-to-9"
    assert inst.group[0].stratifier[2].path == "Patient.gender"
    assert inst.guidance == (
        "This is an episode of care measure that examines all "
        "eligible episodes for the patient during the measurement "
        "period. If the patient has more than one episode, include "
        "all episodes in the measure"
    )
    assert inst.id == "measure-cms146-example"
    assert (
        inst.identifier[0].system
        == "http://hl7.org/fhir/cqi/ecqm/Measure/Identifier/cms"
    )
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "146"
    assert (
        inst.identifier[1].system
        == "http://hl7.org/fhir/cqi/ecqm/Measure/Identifier/nqf"
    )
    assert inst.identifier[1].use == "official"
    assert inst.identifier[1].value == "0002"
    assert inst.improvementNotation == "Higher score indicates better quality"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.lastReviewDate == fhirtypes.Date.validate("2016-09-01")
    assert inst.library[0].reference == "Library/library-cms146-example"
    assert inst.name == "CMS146"
    assert inst.publisher == "National Committee for Quality Assurance"
    assert inst.purpose == (
        "Measure of children with a group A streptococcus test in the"
        " 7-day period from 3 days prior through 3 days after the "
        "diagnosis of pharyngitis"
    )
    assert inst.relatedArtifact[0].citation == (
        "Linder, J.A., D.W. Bates, G.M. Lee, J.A. Finkelstein. 2005. "
        '"Antibiotic treatment of children with sore throat." JAMA '
        "294(18):2315-2322. "
    )
    assert inst.relatedArtifact[0].type == "documentation"
    assert inst.relatedArtifact[1].citation == (
        'Infectious Diseases Society of America. 2012. "Clinical '
        "Practice Guideline for the Diagnosis and Management of Group"
        ' A Streptococcal Pharyngitis: 2012 Update." '
    )
    assert inst.relatedArtifact[1].type == "documentation"
    assert inst.relatedArtifact[2].type == "documentation"
    assert inst.scoring.coding[0].code == "proportion"
    assert inst.status == "active"
    assert inst.supplementalData[0].identifier.value == "supplemental-data-gender"
    assert inst.supplementalData[0].path == "Patient.gender"
    assert inst.supplementalData[1].identifier.value == "supplemental-data-deceased"
    assert inst.supplementalData[1].path == "deceasedBoolean"
    assert inst.text.status == "additional"
    assert inst.title == "Appropriate Testing for Children with Pharyngitis"
    assert inst.topic[0].coding[0].code == "57024-2"
    assert inst.topic[0].coding[0].system == "http://hl7.org/fhir/c80-doc-typecodes"
    assert inst.type[0].coding[0].code == "process"
    assert inst.url == "http://hl7.org/fhir/Measure/measure-cms146-example"
    assert inst.useContext[0].code.code == "program"
    assert inst.useContext[0].valueCodeableConcept.text == "eligibile-provider"
    assert inst.version == "1.0.0"


def test_measure_4(base_settings):
    """No. 4 tests collection for Measure.
    Test File: measure-cms146-example.json
    """
    filename = base_settings["unittest_data_dir"] / "measure-cms146-example.json"
    inst = measure.Measure.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Measure" == inst.resource_type

    impl_measure_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Measure" == data["resourceType"]

    inst2 = measure.Measure(**data)
    impl_measure_4(inst2)


def impl_measure_5(inst):
    assert inst.group[0].identifier.value == "Main"
    assert inst.group[0].population[0].code.coding[0].code == "initial-population"
    assert inst.group[0].population[0].criteria == "Initial Population"
    assert inst.group[0].population[1].code.coding[0].code == "denominator"
    assert inst.group[0].population[1].criteria == "Denominator"
    assert inst.group[0].population[2].code.coding[0].code == "numerator"
    assert inst.group[0].population[2].criteria == "Numerator"
    assert inst.id == "component-a-example"
    assert inst.scoring.coding[0].code == "proportion"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Screening for Alcohol Misuse"


def test_measure_5(base_settings):
    """No. 5 tests collection for Measure.
    Test File: measure-component-a-example.json
    """
    filename = base_settings["unittest_data_dir"] / "measure-component-a-example.json"
    inst = measure.Measure.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Measure" == inst.resource_type

    impl_measure_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Measure" == data["resourceType"]

    inst2 = measure.Measure(**data)
    impl_measure_5(inst2)


def impl_measure_6(inst):
    assert inst.compositeScoring.coding[0].code == "opportunity"
    assert inst.id == "composite-example"
    assert inst.relatedArtifact[0].resource.reference == "Measure/component-a-example"
    assert inst.relatedArtifact[0].type == "composed-of"
    assert inst.relatedArtifact[1].resource.reference == "Measure/component-b-example"
    assert inst.relatedArtifact[1].type == "composed-of"
    assert inst.scoring.coding[0].code == "proportion"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Behavioral Assessment Composite Measure"


def test_measure_6(base_settings):
    """No. 6 tests collection for Measure.
    Test File: measure-composite-example.json
    """
    filename = base_settings["unittest_data_dir"] / "measure-composite-example.json"
    inst = measure.Measure.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Measure" == inst.resource_type

    impl_measure_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Measure" == data["resourceType"]

    inst2 = measure.Measure(**data)
    impl_measure_6(inst2)
