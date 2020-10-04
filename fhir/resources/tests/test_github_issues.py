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
    from fhir.resources import construct_fhir_element

    pat = construct_fhir_element(
        "Patient",
        {"resourceType": "Patient", "contained": [{"resourceType": "Patient"}]},
    )
    assert pat.contained[0].__class__ == pat.__class__
    assert pat.contained[0].resource_type == "Patient"
    assert pat.resource_type == "Patient"

    from fhir.resources.patient import Patient

    pat = Patient(resourceType="Patient", contained=[{"resourceType": "Patient"}])
    assert pat.contained[0].__class__ == pat.__class__
    assert pat.contained[0].resource_type == "Patient"
    assert pat.resource_type == "Patient"

    pat = Patient.parse_obj(
        {"resourceType": "Patient", "contained": [{"resourceType": "Patient"}]}
    )
    assert pat.contained[0].__class__ == pat.__class__
    assert pat.contained[0].resource_type == "Patient"
    assert pat.resource_type == "Patient"
