# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Citation
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pathlib import Path

from .. import citation
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


def impl_citation_1(inst):
    assert inst.citedArtifact.abstract[0].language.coding[0].code == "en"
    assert inst.citedArtifact.abstract[0].language.coding[0].display == "English"
    assert (
        inst.citedArtifact.abstract[0].language.coding[0].system
        == ExternalValidatorModel(valueUri="urn:ietf:bcp:47").valueUri
    )
    assert inst.citedArtifact.abstract[0].type.coding[0].code == "primary-human-use"
    assert inst.citedArtifact.abstract[0].type.coding[0].display == "Primary human use"
    assert (
        inst.citedArtifact.abstract[0].type.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/cited-artifact-abstract-type"
        ).valueUri
    )
    assert (
        inst.citedArtifact.classification[0].classifier[0].coding[0].code
        == "knowledge-artifact-type"
    )
    assert (
        inst.citedArtifact.classification[0].classifier[0].coding[0].display
        == "Knowledge Artifact Type"
    )
    assert (
        inst.citedArtifact.classification[0].classifier[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/cited-artifact-classification-type"
        ).valueUri
    )
    assert (
        inst.citedArtifact.classification[0].classifier[1].coding[0].code == "D064886"
    )
    assert (
        inst.citedArtifact.classification[0].classifier[1].coding[0].display
        == "Dataset"
    )
    assert (
        inst.citedArtifact.classification[0].classifier[1].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/citation-artifact-classifier"
        ).valueUri
    )
    assert (
        inst.citedArtifact.classification[0].classifier[1].coding[0].version == "5.0.0"
    )
    assert (
        inst.citedArtifact.classification[1].classifier[0].coding[0].code
        == "EFO_0004327"
    )
    assert (
        inst.citedArtifact.classification[1].classifier[0].coding[0].display
        == "electrocardiography"
    )
    assert (
        inst.citedArtifact.classification[1].classifier[0].coding[0].system
        == ExternalValidatorModel(valueUri="http://www.ebi.ac.uk/efo").valueUri
    )
    assert inst.citedArtifact.classification[1].classifier[0].text == "ecg"
    assert inst.citedArtifact.classification[1].type.text == "topic"
    assert (
        inst.citedArtifact.classification[2].classifier[0].coding[0].code == "FMA_63919"
    )
    assert (
        inst.citedArtifact.classification[2].classifier[0].coding[0].display == "foetus"
    )
    assert (
        inst.citedArtifact.classification[2].classifier[0].coding[0].system
        == ExternalValidatorModel(valueUri="http://purl.obolibrary.org/obo").valueUri
    )
    assert inst.citedArtifact.classification[2].classifier[0].text == "foetus"
    assert inst.citedArtifact.classification[2].type.text == "topic"
    assert inst.citedArtifact.classification[3].classifier[0].text == "pwd"
    assert inst.citedArtifact.classification[3].type.text == "topic"
    assert inst.citedArtifact.classification[4].classifier[0].text == "doppler"
    assert inst.citedArtifact.classification[4].type.text == "topic"
    assert inst.citedArtifact.classification[5].classifier[0].text == "foetal ecg"
    assert inst.citedArtifact.classification[5].type.text == "topic"
    assert inst.citedArtifact.classification[6].classifier[0].text == "maternal ecg"
    assert inst.citedArtifact.classification[6].type.text == "topic"
    assert inst.citedArtifact.classification[7].classifier[0].text == "pwd envelope"
    assert inst.citedArtifact.classification[7].type.text == "topic"
    assert inst.citedArtifact.classification[8].classifier[0].text == "non-invasive"
    assert inst.citedArtifact.classification[8].type.text == "topic"
    assert (
        inst.citedArtifact.classification[9].classifier[0].coding[0].code == "394579002"
    )
    assert (
        inst.citedArtifact.classification[9].classifier[0].coding[0].display
        == "Cardiology (qualifier value)"
    )
    assert (
        inst.citedArtifact.classification[9].classifier[0].coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.citedArtifact.classification[9].classifier[0].text == "cardiology"
    assert inst.citedArtifact.classification[9].type.text == "topic"
    assert (
        inst.citedArtifact.contributorship.summary[0].source.text
        == "copied-from-article"
    )
    assert (
        inst.citedArtifact.contributorship.summary[0].type.coding[0].code
        == "author-string"
    )
    assert (
        inst.citedArtifact.contributorship.summary[0].type.coding[0].display
        == "Author string"
    )
    assert (
        inst.citedArtifact.contributorship.summary[0].type.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/contributor-summary-type"
        ).valueUri
    )
    assert (
        inst.citedArtifact.contributorship.summary[0].type.coding[0].version == "5.0.0"
    )
    assert inst.citedArtifact.contributorship.summary[0].value == (
        "Danilo Pani, Eleonora Sulas, Monica Urru, Reza Sameni, Luigi"
        " Raffo, Roberto Tumbarello"
    )
    assert (
        inst.citedArtifact.contributorship.summary[1].source.text
        == "copied-from-article"
    )
    assert inst.citedArtifact.contributorship.summary[1].type.text == "acknowledgements"
    assert (
        inst.citedArtifact.dateAccessed
        == ExternalValidatorModel(valueDateTime="2021-03-17").valueDateTime
    )
    assert (
        inst.citedArtifact.identifier[0].system
        == ExternalValidatorModel(valueUri="https://doi.org").valueUri
    )
    assert inst.citedArtifact.identifier[0].value == "10.13026/c4n5-3b04"
    assert (
        inst.citedArtifact.publicationForm[0].articleDate
        == ExternalValidatorModel(valueDateTime="2020-11-12").valueDateTime
    )
    assert inst.citedArtifact.publicationForm[0].copyright == (
        "https://physionet.org/content/ninfea/view-license/1.0.0/ and"
        " https://physionet.org/content/ninfea/1.0.0/LICENSE.txt"
    )
    assert inst.citedArtifact.publicationForm[0].language[0].coding[0].code == "en"
    assert (
        inst.citedArtifact.publicationForm[0].language[0].coding[0].display == "English"
    )
    assert (
        inst.citedArtifact.publicationForm[0].language[0].coding[0].system
        == ExternalValidatorModel(valueUri="urn:ietf:bcp:47").valueUri
    )
    assert (
        inst.citedArtifact.publicationForm[0].language[0].coding[0].version == "4.0.1"
    )
    assert (
        inst.citedArtifact.publicationForm[0].publishedIn.publisher.display
        == "MIT Laboratory for Computational Physiology"
    )
    assert inst.citedArtifact.publicationForm[0].publishedIn.title == "PhysioNet"
    assert (
        inst.citedArtifact.publicationForm[0].publishedIn.type.coding[0].code
        == "D019991"
    )
    assert (
        inst.citedArtifact.publicationForm[0].publishedIn.type.coding[0].display
        == "Database"
    )
    assert (
        inst.citedArtifact.publicationForm[0].publishedIn.type.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/published-in-type"
        ).valueUri
    )
    assert (
        inst.citedArtifact.publicationForm[0].publishedIn.type.coding[0].version
        == "5.0.0"
    )
    assert (
        inst.citedArtifact.relatedIdentifier[0].system
        == ExternalValidatorModel(valueUri="https://doi.org").valueUri
    )
    assert inst.citedArtifact.relatedIdentifier[0].value == "10.1038/s41597-021-00811-3"
    assert inst.citedArtifact.relatesTo[0].classifier[0].text == "original publication"
    assert (
        inst.citedArtifact.relatesTo[0].document.url
        == ExternalValidatorModel(
            valueUrl="https://doi.org/10.1038/s41597-021-00811-3"
        ).valueUrl
    )
    assert inst.citedArtifact.relatesTo[0].type == "derived-from"
    assert inst.citedArtifact.relatesTo[1].classifier[0].text == "ontology"
    assert inst.citedArtifact.relatesTo[1].display == "Experimental Factor Ontology"
    assert (
        inst.citedArtifact.relatesTo[1].document.url
        == ExternalValidatorModel(
            valueUrl="http://data.bioontology.org/ontologies/EFO"
        ).valueUrl
    )
    assert inst.citedArtifact.relatesTo[1].type == "depends-on"
    assert inst.citedArtifact.title[0].language.coding[0].code == "en"
    assert inst.citedArtifact.title[0].language.coding[0].display == "English"
    assert (
        inst.citedArtifact.title[0].language.coding[0].system
        == ExternalValidatorModel(valueUri="urn:ietf:bcp:47").valueUri
    )
    assert inst.citedArtifact.title[0].language.coding[0].version == "4.0.1"
    assert inst.citedArtifact.title[0].text == (
        "NInFEA: Non-Invasive Multimodal Foetal ECG-Doppler Dataset "
        "for Antenatal Cardiology Research"
    )
    assert inst.citedArtifact.title[0].type[0].text == "primary-human-use"
    assert inst.citedArtifact.version.value == "1.0.0"
    assert inst.citedArtifact.webLocation[0].classifier[0].coding[0].code == "webpage"
    assert (
        inst.citedArtifact.webLocation[0].classifier[0].coding[0].display == "Webpage"
    )
    assert (
        inst.citedArtifact.webLocation[0].classifier[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/artifact-url-classifier"
        ).valueUri
    )
    assert inst.citedArtifact.webLocation[0].classifier[0].coding[0].version == "5.0.0"
    assert (
        inst.citedArtifact.webLocation[0].url
        == ExternalValidatorModel(
            valueUri="https://physionet.org/content/ninfea/1.0.0/"
        ).valueUri
    )
    assert inst.citedArtifact.webLocation[1].classifier[0].coding[0].code == "doi-based"
    assert (
        inst.citedArtifact.webLocation[1].classifier[0].coding[0].display == "DOI Based"
    )
    assert (
        inst.citedArtifact.webLocation[1].classifier[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/artifact-url-classifier"
        ).valueUri
    )
    assert inst.citedArtifact.webLocation[1].classifier[0].coding[0].version == "5.0.0"
    assert (
        inst.citedArtifact.webLocation[1].url
        == ExternalValidatorModel(
            valueUri="https://doi.org/10.13026/c4n5-3b04"
        ).valueUri
    )
    assert inst.citedArtifact.webLocation[2].classifier[0].coding[0].code == "doi-based"
    assert (
        inst.citedArtifact.webLocation[2].classifier[0].coding[0].display == "DOI Based"
    )
    assert (
        inst.citedArtifact.webLocation[2].classifier[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/artifact-url-classifier"
        ).valueUri
    )
    assert inst.citedArtifact.webLocation[2].classifier[0].coding[0].version == "5.0.0"
    assert (
        inst.citedArtifact.webLocation[2].classifier[0].text == "original publication"
    )
    assert (
        inst.citedArtifact.webLocation[2].url
        == ExternalValidatorModel(
            valueUri="https://doi.org/10.1038/s41597-021-00811-3"
        ).valueUri
    )
    assert (
        inst.citedArtifact.webLocation[3].classifier[0].coding[0].code
        == "compressed-file"
    )
    assert (
        inst.citedArtifact.webLocation[3].classifier[0].coding[0].display
        == "Compressed file"
    )
    assert (
        inst.citedArtifact.webLocation[3].classifier[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/artifact-url-classifier"
        ).valueUri
    )
    assert inst.citedArtifact.webLocation[3].classifier[0].coding[0].version == "5.0.0"
    assert (
        inst.citedArtifact.webLocation[3].url
        == ExternalValidatorModel(
            valueUri="https://physionet.org/static/published-projects/ninfea/ninfea-non-invasive-multimodal-foetal-ecg-doppler-dataset-for-antenatal-cardiology-research-1.0.0.zip"
        ).valueUri
    )
    assert inst.citedArtifact.webLocation[4].classifier[0].text == "DOI-for-metadata"
    assert (
        inst.citedArtifact.webLocation[4].url
        == ExternalValidatorModel(
            valueUri="https://doi.org/10.6084/m9.figshare.13283492"
        ).valueUri
    )
    assert inst.contact[0].telecom[0].system == "email"
    assert inst.contact[0].telecom[0].value == "support@computablepublishing.com"
    assert inst.copyright == "https://creativecommons.org/licenses/by-nc-sa/4.0/"
    assert (
        inst.date
        == ExternalValidatorModel(
            valueDateTime="2021-09-24T10:41:01.740Z"
        ).valueDateTime
    )
    assert inst.description == "A citation of a dataset"
    assert inst.id == "citation-example-research-doi"
    assert inst.identifier[0].assigner.display == "Computable Publishing LLC"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(valueUri="https://fevir.net").valueUri
    )
    assert inst.identifier[0].type.text == "FEvIR Object Identifier"
    assert inst.identifier[0].value == "60"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.name == "NInFEACitation"
    assert inst.publisher == "Computable Publishing LLC"
    assert inst.status == "active"
    assert inst.summary[0].style.text == "as reported on PhysioNet"
    assert inst.summary[1].style.coding[0].code == "comppub"
    assert inst.summary[1].style.coding[0].display == "Computable Publishing"
    assert (
        inst.summary[1].style.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/ValueSet/citation-summary-style"
        ).valueUri
    )
    assert inst.text.status == "generated"
    assert inst.title == "NInFEA Citation"


def test_citation_1(base_settings):
    """No. 1 tests collection for Citation.
    Test File: citation-example-research-doi.json
    """
    filename = base_settings["unittest_data_dir"] / "citation-example-research-doi.json"
    inst = citation.Citation.model_validate_json(Path(filename).read_bytes())
    assert "Citation" == inst.get_resource_type()

    impl_citation_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Citation" == data["resourceType"]

    inst2 = citation.Citation(**data)
    impl_citation_1(inst2)
