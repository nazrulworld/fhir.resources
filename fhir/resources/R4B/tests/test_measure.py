# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Measure
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
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
    assert inst.experimental is True
    assert inst.group[0].id == "PopulationGroup1"
    assert inst.group[0].population[0].code.coding[0].code == "initial-population"
    assert inst.group[0].population[0].criteria.expression == "InitialPopulation1"
    assert inst.group[0].population[0].criteria.language == "text/cql"
    assert inst.group[0].population[1].code.coding[0].code == "denominator"
    assert inst.group[0].population[1].criteria.expression == "Denominator1"
    assert inst.group[0].population[1].criteria.language == "text/cql"
    assert inst.group[0].population[2].code.coding[0].code == "denominator-exclusions"
    assert inst.group[0].population[2].criteria.expression == "DenominatorExclusions1"
    assert inst.group[0].population[2].criteria.language == "text/cql"
    assert inst.group[0].population[3].code.coding[0].code == "numerator"
    assert inst.group[0].population[3].criteria.expression == "Numerator1"
    assert inst.group[0].population[3].criteria.language == "text/cql"
    assert inst.group[1].id == "PopulationGroup2"
    assert inst.group[1].population[0].code.coding[0].code == "initial-population"
    assert inst.group[1].population[0].criteria.expression == "InitialPopulation2"
    assert inst.group[1].population[0].criteria.language == "text/cql"
    assert inst.group[1].population[1].code.coding[0].code == "denominator"
    assert inst.group[1].population[1].criteria.expression == "Denominator2"
    assert inst.group[1].population[1].criteria.language == "text/cql"
    assert inst.group[1].population[2].code.coding[0].code == "denominator-exclusion"
    assert inst.group[1].population[2].criteria.expression == "DenominatorExclusions2"
    assert inst.group[1].population[2].criteria.language == "text/cql"
    assert inst.group[1].population[3].code.coding[0].code == "numerator"
    assert inst.group[1].population[3].criteria.expression == "Numerator2"
    assert inst.group[1].population[3].criteria.language == "text/cql"
    assert inst.id == "measure-exclusive-breastfeeding"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "exclusive-breastfeeding-measure"
    assert inst.improvementNotation.coding[0].code == "increase"
    assert inst.improvementNotation.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/measure-improvement-" "notation"
    )
    assert inst.library[0] == (
        "http://example.org/fhir/Library/library-exclusive-" "breastfeeding-cqm-logic"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
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
    assert inst.version == "4.3.0"


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
    assert inst.experimental is True
    assert inst.group[0].id == "Main"
    assert inst.group[0].population[0].code.coding[0].code == "initial-population"
    assert inst.group[0].population[0].criteria.expression == "Initial Population"
    assert inst.group[0].population[0].criteria.language == "text/cql"
    assert inst.group[0].population[1].code.coding[0].code == "denominator"
    assert inst.group[0].population[1].criteria.expression == "Denominator"
    assert inst.group[0].population[1].criteria.language == "text/cql"
    assert inst.group[0].population[2].code.coding[0].code == "numerator"
    assert inst.group[0].population[2].criteria.expression == "Numerator"
    assert inst.group[0].population[2].criteria.language == "text/cql"
    assert inst.id == "component-b-example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
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
    assert inst.experimental is True
    assert inst.group[0].id == "PopulationGroup1"
    assert inst.group[0].population[0].code.coding[0].code == "initial-population"
    assert inst.group[0].population[0].criteria.expression == "InitialPopulation1"
    assert inst.group[0].population[0].criteria.language == "text/cql"
    assert inst.group[0].population[1].code.coding[0].code == "denominator"
    assert inst.group[0].population[1].criteria.expression == "Denominator1"
    assert inst.group[0].population[1].criteria.language == "text/cql"
    assert inst.group[0].population[2].code.coding[0].code == "denominator-exclusions"
    assert inst.group[0].population[2].criteria.expression == "DenominatorExclusions1"
    assert inst.group[0].population[2].criteria.language == "text/cql"
    assert inst.group[0].population[3].code.coding[0].code == "numerator"
    assert inst.group[0].population[3].criteria.expression == "Numerator1"
    assert inst.group[0].population[3].criteria.language == "text/cql"
    assert inst.group[1].id == "PopulationGroup2"
    assert inst.group[1].population[0].code.coding[0].code == "initial-population"
    assert inst.group[1].population[0].criteria.expression == "InitialPopulation2"
    assert inst.group[1].population[0].criteria.language == "text/cql"
    assert inst.group[1].population[1].code.coding[0].code == "denominator"
    assert inst.group[1].population[1].criteria.expression == "Denominator2"
    assert inst.group[1].population[1].criteria.language == "text/cql"
    assert inst.group[1].population[2].code.coding[0].code == "denominator-exclusion"
    assert inst.group[1].population[2].criteria.expression == "DenominatorExclusions2"
    assert inst.group[1].population[2].criteria.language == "text/cql"
    assert inst.group[1].population[3].code.coding[0].code == "numerator"
    assert inst.group[1].population[3].criteria.expression == "Numerator2"
    assert inst.group[1].population[3].criteria.language == "text/cql"
    assert inst.id == "measure-predecessor-example"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "exclusive-breastfeeding-measure"
    assert inst.improvementNotation.coding[0].code == "increase"
    assert inst.improvementNotation.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/measure-improvement-" "notation"
    )
    assert inst.library[0] == (
        "http://example.org/fhir/Library/library-exclusive-" "breastfeeding-cqm-logic"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
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
    assert inst.version == "4.3.0"


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
    assert inst.date == fhirtypes.DateTime.validate("2018-03-08")
    assert inst.experimental is True
    assert inst.group[0].code.coding[0].code == "QRPH_ADX_ART1_N"
    assert inst.group[0].code.coding[0].system == "http://ihe.net/qrph/adx/"
    assert inst.group[0].description == (
        "Number of adults and children newly enrolled on "
        "antiretroviral therapy (ART) in the reporting period"
    )
    assert inst.group[0].population[0].code.text == "cohort"
    assert inst.group[0].population[0].criteria.expression == (
        "Newly enrolled on antiretroviral therapy (ART) during " "measurement period"
    )
    assert inst.group[0].population[0].criteria.language == "text/cql"
    assert inst.group[0].stratifier[0].code.coding[0].code == "AGE_GROUP:SEX"
    assert (
        inst.group[0].stratifier[0].code.coding[0].system == "http://ihe.net/qrph/adx/"
    )
    assert inst.group[0].stratifier[0].criteria.expression == "Age Group/Sex"
    assert inst.group[0].stratifier[0].criteria.language == "text/cql"
    assert inst.group[1].code.coding[0].code == "QRPH_ADX_ART1_N_PREG_BF"
    assert inst.group[1].code.coding[0].system == "http://ihe.net/qrph/adx/"
    assert inst.group[1].description == (
        "Number of adults and children newly enrolled on ART in the "
        "reporting period_pregnant and breastfeeding"
    )
    assert inst.group[1].population[0].code.text == "cohort"
    assert inst.group[1].population[0].criteria.expression == (
        "Newly enrolled on antiretroviral therapy (ART) during "
        "measurement period (pregnant and breastfeeding)"
    )
    assert inst.group[1].population[0].criteria.language == "text/cql"
    assert inst.group[1].stratifier[0].code.coding[0].code == "PREG_BF"
    assert (
        inst.group[1].stratifier[0].code.coding[0].system == "http://ihe.net/qrph/adx/"
    )
    assert inst.group[1].stratifier[0].criteria.expression == "Pregnant/Breastfeeding"
    assert inst.group[1].stratifier[0].criteria.language == "text/cql"
    assert inst.group[2].code.coding[0].code == "QRPH_ADX_ART3_N"
    assert inst.group[2].code.coding[0].system == "http://ihe.net/qrph/adx/"
    assert inst.group[2].description == (
        "Number of adults and children currently receiving "
        "antiretroviral therapy (ART)"
    )
    assert inst.group[2].population[0].code.text == "cohort"
    assert inst.group[2].population[0].criteria.expression == (
        "Receiving antiretroviral therapy (ART) during measurement " "period"
    )
    assert inst.group[2].population[0].criteria.language == "text/cql"
    assert inst.group[3].code.coding[0].code == "QRPH_ADX_ART5_N"
    assert inst.group[3].code.coding[0].system == "http://ihe.net/qrph/adx/"
    assert inst.group[3].description == (
        "Number of adults and children who are still on treatment at "
        "12 months after initiating ART"
    )
    assert inst.group[3].population[0].code.text == "cohort"
    assert inst.group[3].population[0].criteria.expression == (
        "Receiving antiretroviral therapy (ART) at 12 months after " "initiating"
    )
    assert inst.group[3].population[0].criteria.language == "text/cql"
    assert inst.group[3].stratifier[0].component[0].code.coding[0].code == "AGE_GROUP"
    assert (
        inst.group[3].stratifier[0].component[0].code.coding[0].system
        == "http://ihe.net/qrph/adx/"
    )
    assert inst.group[3].stratifier[0].component[0].criteria.expression == "Age Group"
    assert inst.group[3].stratifier[0].component[0].criteria.language == "text/cql"
    assert inst.group[3].stratifier[0].component[1].code.coding[0].code == "SEX"
    assert (
        inst.group[3].stratifier[0].component[1].code.coding[0].system
        == "http://ihe.net/qrph/adx/"
    )
    assert inst.group[3].stratifier[0].component[1].criteria.expression == "Sex"
    assert inst.group[3].stratifier[0].component[1].criteria.language == "text/cql"
    assert inst.group[4].code.coding[0].code == "QRPH_ADX_ART5_N_PREG_BF"
    assert inst.group[4].code.coding[0].system == "http://ihe.net/qrph/adx/"
    assert inst.group[4].description == (
        "Number of adults and children who are still on treatment at "
        "12 months after initiating ART-pregnant and breastfeeding"
    )
    assert inst.group[4].population[0].code.text == "cohort"
    assert inst.group[4].population[0].criteria.expression == (
        "Receiving antiretroviral therapy (ART) at 12 months after "
        "initiating (pregnant and breastfeeding)"
    )
    assert inst.group[4].population[0].criteria.language == "text/cql"
    assert inst.group[4].stratifier[0].code.coding[0].code == "PREG_BF"
    assert (
        inst.group[4].stratifier[0].code.coding[0].system == "http://ihe.net/qrph/adx/"
    )
    assert inst.group[4].stratifier[0].criteria.expression == "Pregnant/Breastfeeding"
    assert inst.group[4].stratifier[0].criteria.language == "text/cql"
    assert inst.group[5].code.coding[0].code == "QRPH_ADX_ART5_D"
    assert inst.group[5].code.coding[0].system == "http://ihe.net/qrph/adx/"
    assert inst.group[5].description == (
        "Number of adults and children who initiated ART in the 12 "
        "months prior to the beginning of the reporting period"
    )
    assert inst.group[5].population[0].code.text == "cohort"
    assert inst.group[5].population[0].criteria.expression == (
        "Initiated antiretroviral therapy (ART) in the 12 months "
        "prior to measurement period"
    )
    assert inst.group[5].population[0].criteria.language == "text/cql"
    assert inst.group[5].stratifier[0].code.coding[0].code == "AGE_GROUP:SEX"
    assert (
        inst.group[5].stratifier[0].code.coding[0].system == "http://ihe.net/qrph/adx/"
    )
    assert inst.group[5].stratifier[0].criteria.expression == "Age Group/Sex"
    assert inst.group[5].stratifier[0].criteria.language == "text/cql"
    assert inst.group[6].code.coding[0].code == "QRPH_ADX_MTCT1_D"
    assert inst.group[6].code.coding[0].system == "http://ihe.net/qrph/adx/"
    assert inst.group[6].description == (
        "Number of pregnant women who attended ANC or had a facility-"
        "based delivery in the reporting period"
    )
    assert inst.group[6].population[0].code.text == "cohort"
    assert inst.group[6].population[0].criteria.expression == (
        "Antenatal Care Visit or Live Birth during the Measurement " "Period"
    )
    assert inst.group[6].population[0].criteria.language == "text/cql"
    assert inst.group[6].stratifier[0].code.coding[0].code == "PMTCT_HIV_STATUS"
    assert (
        inst.group[6].stratifier[0].code.coding[0].system == "http://ihe.net/qrph/adx/"
    )
    assert inst.group[6].stratifier[0].criteria.expression == "PMTCT HIV Status"
    assert inst.group[6].stratifier[0].criteria.language == "text/cql"
    assert inst.group[7].code.coding[0].code == "QRPH_ADX_MTCT2_D"
    assert inst.group[7].code.coding[0].system == "http://ihe.net/qrph/adx/"
    assert inst.group[7].description == (
        "Number of HIV positive pregnant women who attended ANC or "
        "had a facility-based delivery within the reporting period"
    )
    assert inst.group[7].population[0].code.text == "cohort"
    assert inst.group[7].population[0].criteria.expression == (
        "Antenatal Care Visit or Live Birth during Measurement Period" " (HIV Positive)"
    )
    assert inst.group[7].population[0].criteria.language == "text/cql"
    assert inst.group[8].code.coding[0].code == "QRPH_ADX_MTCT2_N"
    assert inst.group[8].code.coding[0].system == "http://ihe.net/qrph/adx/"
    assert inst.group[8].description == (
        "Number of HIV-positive pregnant women who received ART to "
        "reduce the risk of mother-to-child-transmission during "
        "pregnancy"
    )
    assert inst.group[8].population[0].code.text == "cohort"
    assert inst.group[8].population[0].criteria.expression == (
        "HIV-positive, pregnant, and receiving antiretroviral therapy"
        " (ART) to reduce the risk of mother-to-child-transmission "
        "during pregnancy"
    )
    assert inst.group[8].population[0].criteria.language == "text/cql"
    assert inst.group[8].stratifier[0].code.coding[0].code == "PMTCT_ART_STATUS"
    assert (
        inst.group[8].stratifier[0].code.coding[0].system == "http://ihe.net/qrph/adx/"
    )
    assert inst.group[8].stratifier[0].criteria.expression == "PMTCT ART Status"
    assert inst.group[8].stratifier[0].criteria.language == "text/cql"
    assert inst.group[9].code.coding[0].code == "QRPH_ADX_VLS3_N"
    assert inst.group[9].code.coding[0].system == "http://ihe.net/qrph/adx/"
    assert inst.group[9].description == (
        "Number of people living with HIV and on ART who have a "
        "suppressed viral load results (<1000 copies/mL)"
    )
    assert inst.group[9].population[0].code.text == "cohort"
    assert inst.group[9].population[0].criteria.expression == (
        "Living with HIV and on ART with suppressed viral load "
        "results (<1000 copies/mL)"
    )
    assert inst.group[9].population[0].criteria.language == "text/cql"
    assert inst.group[9].stratifier[0].code.coding[0].code == "AGE_GROUP:SEX"
    assert (
        inst.group[9].stratifier[0].code.coding[0].system == "http://ihe.net/qrph/adx/"
    )
    assert inst.group[9].stratifier[0].criteria.expression == "Age Group/Sex"
    assert inst.group[9].stratifier[0].criteria.language == "text/cql"
    assert inst.id == "hiv-indicators"
    assert inst.identifier[0].system == "http://ohie.org/Measure/"
    assert inst.identifier[0].value == "hiv-indicators"
    assert inst.library[0] == "http://ohie.org/Library/hiv-indicators"
    assert inst.name == "HIV"
    assert inst.publisher == "Open HIE"
    assert (
        inst.relatedArtifact[0].document.url
        == "http://wiki.ihe.net/index.php/Aggregate_Data_Exchange_-_HIV"
    )
    assert inst.relatedArtifact[0].type == "derived-from"
    assert (
        inst.relatedArtifact[0].url
        == "http://wiki.ihe.net/index.php/Aggregate_Data_Exchange_-_HIV"
    )
    assert inst.scoring.coding[0].code == "cohort"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "HIV Indicators"
    assert inst.url == "http://ohie.org/Measure/hiv-indicators"
    assert inst.version == "0.0.0"


def test_measure_4(base_settings):
    """No. 4 tests collection for Measure.
    Test File: measure-hiv-indicators.json
    """
    filename = base_settings["unittest_data_dir"] / "measure-hiv-indicators.json"
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
    assert inst.approvalDate == fhirtypes.Date.validate("2016-01-01")
    assert inst.author[0].name == "National Committee for Quality Assurance"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://www.ncqa.org/"
    assert inst.date == fhirtypes.DateTime.validate("2017-03-10")
    assert inst.description == (
        "Percentage of children 3-18 years of age who were diagnosed "
        "with pharyngitis, ordered an antibiotic and received a group"
        " A streptococcus (strep) test for the episode."
    )
    assert inst.effectivePeriod.end == fhirtypes.DateTime.validate("2017-12-31")
    assert inst.effectivePeriod.start == fhirtypes.DateTime.validate("2017-01-01")
    assert inst.experimental is True
    assert inst.group[0].id == "CMS146-group-1"
    assert inst.group[0].population[0].code.coding[0].code == "initial-population"
    assert (
        inst.group[0].population[0].code.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/measure-population"
    )
    assert inst.group[0].population[0].criteria.expression == "CMS146.InitialPopulation"
    assert inst.group[0].population[0].criteria.language == "text/cql"
    assert inst.group[0].population[1].code.coding[0].code == "numerator"
    assert (
        inst.group[0].population[1].code.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/measure-population"
    )
    assert inst.group[0].population[1].criteria.expression == "CMS146.Numerator"
    assert inst.group[0].population[1].criteria.language == "text/cql"
    assert inst.group[0].population[2].code.coding[0].code == "denominator"
    assert (
        inst.group[0].population[2].code.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/measure-population"
    )
    assert inst.group[0].population[2].criteria.expression == "CMS146.Denominator"
    assert inst.group[0].population[2].criteria.language == "text/cql"
    assert inst.group[0].population[3].code.coding[0].code == "denominator-exclusion"
    assert (
        inst.group[0].population[3].code.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/measure-population"
    )
    assert (
        inst.group[0].population[3].criteria.expression == "CMS146.DenominatorExclusion"
    )
    assert inst.group[0].population[3].criteria.language == "text/cql"
    assert inst.group[0].stratifier[0].code.text == "stratifier-ages-up-to-9"
    assert inst.group[0].stratifier[0].criteria.expression == "CMS146.AgesUpToNine"
    assert inst.group[0].stratifier[0].criteria.language == "text/cql"
    assert inst.group[0].stratifier[1].code.text == "stratifier-ages-10-plus"
    assert inst.group[0].stratifier[1].criteria.expression == "CMS146.AgesTenPlus"
    assert inst.group[0].stratifier[1].criteria.language == "text/cql"
    assert inst.group[0].stratifier[2].code.text == "stratifier-gender"
    assert inst.group[0].stratifier[2].criteria.expression == "Patient.gender"
    assert inst.group[0].stratifier[2].criteria.language == "text/fhirpath"
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
    assert inst.improvementNotation.coding[0].code == "increase"
    assert inst.improvementNotation.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/measure-improvement-" "notation"
    )
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.lastReviewDate == fhirtypes.Date.validate("2016-09-01")
    assert inst.library[0] == "http://hl7.org/fhir/Library/library-cms146-example"
    assert inst.name == "CMS146"
    assert inst.publisher == "National Committee for Quality Assurance"
    assert inst.purpose == (
        "Measure of children with a group A streptococcus test in the"
        " 7-day period from 3 days prior through 3 days after the "
        "diagnosis of pharyngitis"
    )
    assert inst.relatedArtifact[0].citation == (
        "Linder, J.A., D.W. Bates, G.M. Lee, J.A. Finkelstein. 2005. "
        "_Antibiotic treatment of children with sore throat._ JAMA "
        "294(18):2315-2322."
    )
    assert inst.relatedArtifact[0].type == "documentation"
    assert inst.relatedArtifact[1].citation == (
        "Infectious Diseases Society of America. 2012. _Clinical "
        "Practice Guideline for the Diagnosis and Management of Group"
        " A Streptococcal Pharyngitis: 2012 Update._"
    )
    assert inst.relatedArtifact[1].type == "documentation"
    assert inst.relatedArtifact[2].type == "documentation"
    assert inst.scoring.coding[0].code == "proportion"
    assert (
        inst.scoring.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/measure-scoring"
    )
    assert inst.status == "active"
    assert inst.supplementalData[0].code.text == "supplemental-data-gender"
    assert inst.supplementalData[0].criteria.expression == "Patient.gender"
    assert inst.supplementalData[0].criteria.language == "text/fhirpath"
    assert inst.supplementalData[1].code.text == "supplemental-data-deceased"
    assert inst.supplementalData[1].criteria.expression == "deceasedBoolean"
    assert inst.supplementalData[1].criteria.language == "text/fhirpath"
    assert inst.text.status == "additional"
    assert inst.title == "Appropriate Testing for Children with Pharyngitis"
    assert inst.topic[0].coding[0].code == "57024-2"
    assert inst.topic[0].coding[0].system == "http://loinc.org"
    assert inst.type[0].coding[0].code == "process"
    assert (
        inst.type[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/measure-type"
    )
    assert inst.url == "http://hl7.org/fhir/Measure/measure-cms146-example"
    assert inst.useContext[0].code.code == "program"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueCodeableConcept.text == "eligibile-provider"
    assert inst.useContext[1].code.code == "age"
    assert (
        inst.useContext[1].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[1].valueRange.high.unit == "a"
    assert float(inst.useContext[1].valueRange.high.value) == float(18)
    assert inst.useContext[1].valueRange.low.unit == "a"
    assert float(inst.useContext[1].valueRange.low.value) == float(3)
    assert inst.version == "1.0.0"


def test_measure_5(base_settings):
    """No. 5 tests collection for Measure.
    Test File: measure-cms146-example.json
    """
    filename = base_settings["unittest_data_dir"] / "measure-cms146-example.json"
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
    assert inst.experimental is True
    assert inst.group[0].id == "Main"
    assert inst.group[0].population[0].code.coding[0].code == "initial-population"
    assert inst.group[0].population[0].criteria.expression == "Initial Population"
    assert inst.group[0].population[0].criteria.language == "text/cql"
    assert inst.group[0].population[1].code.coding[0].code == "denominator"
    assert inst.group[0].population[1].criteria.expression == "Denominator"
    assert inst.group[0].population[1].criteria.language == "text/cql"
    assert inst.group[0].population[2].code.coding[0].code == "numerator"
    assert inst.group[0].population[2].criteria.expression == "Numerator"
    assert inst.group[0].population[2].criteria.language == "text/cql"
    assert inst.id == "component-a-example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.scoring.coding[0].code == "proportion"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Screening for Alcohol Misuse"


def test_measure_6(base_settings):
    """No. 6 tests collection for Measure.
    Test File: measure-component-a-example.json
    """
    filename = base_settings["unittest_data_dir"] / "measure-component-a-example.json"
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


def impl_measure_7(inst):
    assert inst.compositeScoring.coding[0].code == "opportunity"
    assert inst.experimental is True
    assert inst.id == "composite-example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert (
        inst.relatedArtifact[0].resource
        == "http://example.org/fhir/Measure/component-a-example"
    )
    assert inst.relatedArtifact[0].type == "composed-of"
    assert (
        inst.relatedArtifact[1].resource
        == "http://example.org/fhir/Measure/component-b-example"
    )
    assert inst.relatedArtifact[1].type == "composed-of"
    assert inst.scoring.coding[0].code == "proportion"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Behavioral Assessment Composite Measure"


def test_measure_7(base_settings):
    """No. 7 tests collection for Measure.
    Test File: measure-composite-example.json
    """
    filename = base_settings["unittest_data_dir"] / "measure-composite-example.json"
    inst = measure.Measure.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Measure" == inst.resource_type

    impl_measure_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Measure" == data["resourceType"]

    inst2 = measure.Measure(**data)
    impl_measure_7(inst2)
