import pydantic
import pytest

from fhir.resources.observation import Observation

__author__ = "Shristi Shetty"

BASE = {
    "resourceType": "Observation",
    "status": "final",
    "code": {"text": "x"},
}


@pytest.mark.parametrize(
    "field, value",
    [
        ("effectiveDateTime", "2016-12-31T23:59:60Z"),
        ("effectiveInstant", "2016-12-31T23:59:60Z"),
        ("issued", "2016-12-31T23:59:60.500+00:00"),
        ("valueTime", "23:59:60"),
    ],
)
def test_leap_second_is_accepted_and_preserved(field, value):
    """Leap seconds (23:59:60) must validate, see #212.

    fhir-core 1.1.12 keeps the original string, as Python datetime
    cannot hold second 60, matching how partial dates are kept.
    """
    obs = Observation.model_validate({**BASE, field: value})
    assert obs.model_dump()[field] == value
    assert value in obs.model_dump_json()


def test_leap_second_control_59_still_valid():
    obs = Observation.model_validate(
        {**BASE, "effectiveDateTime": "2016-12-31T23:59:59Z"}
    )
    assert obs.effectiveDateTime is not None


def test_second_61_still_rejected():
    with pytest.raises(pydantic.ValidationError):
        Observation.model_validate(
            {**BASE, "effectiveDateTime": "2016-12-31T23:59:61Z"}
        )
