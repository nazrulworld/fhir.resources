import importlib
import inspect
import pkgutil

import pytest
from fhir_core.fhirabstractmodel import FHIRAbstractModel

import fhir.resources.STU3 as stu3
from fhir.resources.STU3.condition import Condition
from fhir.resources.STU3.provenance import Provenance


def _stu3_model_classes():
    for module_info in pkgutil.iter_modules(stu3.__path__):
        if module_info.ispkg or module_info.name == "fhirtypes":
            continue
        module = importlib.import_module(f"{stu3.__name__}.{module_info.name}")
        for _, klass in inspect.getmembers(module, inspect.isclass):
            if klass.__module__ == module.__name__ and issubclass(
                klass, FHIRAbstractModel
            ):
                yield klass


@pytest.mark.parametrize("method", ["elements_sequence", "summary_elements_sequence"])
def test_stu3_element_sequences_have_no_duplicates(method):
    duplicated = {}
    for klass in _stu3_model_classes():
        names = getattr(klass, method)()
        repeated = sorted({name for name in names if names.count(name) > 1})
        if repeated:
            duplicated[klass.__name__] = repeated
    assert duplicated == {}


def test_stu3_annotation_author_reference_written_once_in_xml():
    condition = Condition.model_validate(
        {
            "resourceType": "Condition",
            "subject": {"reference": "Patient/1"},
            "note": [
                {
                    "authorReference": {"reference": "Practitioner/1"},
                    "text": "checked",
                }
            ],
        }
    )
    xml_bytes = condition.model_dump_xml()
    assert xml_bytes.count(b"<authorReference>") == 1


def test_stu3_provenance_agent_who_reference_written_once_in_xml():
    provenance = Provenance.model_validate(
        {
            "resourceType": "Provenance",
            "target": [{"reference": "Patient/1"}],
            "recorded": "2017-01-01T00:00:00Z",
            "agent": [
                {
                    "whoReference": {"reference": "Practitioner/1"},
                    "onBehalfOfReference": {"reference": "Organization/1"},
                }
            ],
        }
    )
    xml_bytes = provenance.model_dump_xml()
    assert xml_bytes.count(b"<whoReference>") == 1
    assert xml_bytes.count(b"<onBehalfOfReference>") == 1
