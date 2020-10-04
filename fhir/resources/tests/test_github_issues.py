from fhir.resources import construct_fhir_element
from fhir.resources.patient import Patient


def test_issue_28():
    """Running the following code:
    from fhir.resources import construct_fhir_element
    d = {'resourceType': 'Patient', 'contained':[{'resourceType': 'Patient'}]}
    construct_fhir_element('Patient', d)
    end up changing the value of d to {'resourceType': 'Patient', 'contained': [{}]}

    I would expect it to not change the given object. Moreover, because it doesn't
    delete resourceType from the outter dictionary, I assume this behavior is not expected.
    Is it on purpose?
    Thanks,
    Itay"""
    data = {"resourceType": "Patient", "contained": [{"resourceType": "Patient"}]}
    construct_fhir_element(
        "Patient",
        data,
    )
    # should not change data
    assert data == {
        "resourceType": "Patient",
        "contained": [{"resourceType": "Patient"}],
    }

    data = {"resourceType": "Patient", "contained": [{"resourceType": "Patient"}]}
    Patient.parse_obj(data)

    # should not change data
    assert data == {
        "resourceType": "Patient",
        "contained": [{"resourceType": "Patient"}],
    }

    data = {"resourceType": "Patient", "contained": [{"resourceType": "Patient"}]}
    Patient(**data)
    # should not change data
    assert data == {
        "resourceType": "Patient",
        "contained": [{"resourceType": "Patient"}],
    }
