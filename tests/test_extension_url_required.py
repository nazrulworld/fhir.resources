"""Tests for Extension.url required validation (issue #205)."""
import pytest
from pydantic import ValidationError


class TestExtensionUrlRequired:
    """Extension.url must be present per FHIR spec cardinality 1..1."""

    def test_r4b_extension_with_value_requires_url(self):
        """Extension with value[x] but no url should fail validation."""
        from fhir.resources.R4B.patient import Patient

        with pytest.raises(ValidationError, match="Extension.url is required"):
            Patient.model_validate(
                {
                    "resourceType": "Patient",
                    "extension": [{"valueCode": "F"}],
                }
            )

    def test_r5_extension_with_value_requires_url(self):
        """R5 Extension with value[x] but no url should fail validation."""
        from fhir.resources.patient import Patient

        with pytest.raises(ValidationError, match="Extension.url is required"):
            Patient.model_validate(
                {
                    "resourceType": "Patient",
                    "extension": [{"valueCode": "F"}],
                }
            )

    def test_stu3_extension_with_value_requires_url(self):
        """STU3 Extension with value[x] but no url should fail validation."""
        from fhir.resources.STU3.patient import Patient

        with pytest.raises(ValidationError, match="Extension.url is required"):
            Patient.model_validate(
                {
                    "resourceType": "Patient",
                    "extension": [{"valueCode": "F"}],
                }
            )

    def test_r4b_valid_extension_with_url(self):
        """Extension with url and value should pass."""
        from fhir.resources.R4B.patient import Patient

        p = Patient.model_validate(
            {
                "resourceType": "Patient",
                "extension": [
                    {"url": "http://example.com/ext", "valueCode": "F"}
                ],
            }
        )
        assert p.extension[0].url == "http://example.com/ext"
        assert p.extension[0].valueCode == "F"

    def test_r4b_extension_url_only(self):
        """Extension with only url (no value) should pass."""
        from fhir.resources.R4B.patient import Patient

        p = Patient.model_validate(
            {
                "resourceType": "Patient",
                "extension": [{"url": "http://example.com/ext"}],
            }
        )
        assert p.extension[0].url == "http://example.com/ext"

    def test_r4b_extension_nested_requires_url(self):
        """Extension with nested extensions but no url should fail."""
        from fhir.resources.R4B.patient import Patient

        with pytest.raises(ValidationError, match="Extension.url is required"):
            Patient.model_validate(
                {
                    "resourceType": "Patient",
                    "extension": [
                        {
                            "extension": [
                                {"url": "http://nested", "valueString": "test"}
                            ]
                        }
                    ],
                }
            )

    def test_r4b_value_string_requires_url(self):
        """Extension with valueString but no url should fail."""
        from fhir.resources.R4B.extension import Extension

        with pytest.raises(ValidationError, match="Extension.url is required"):
            Extension.model_validate({"valueString": "test"})
