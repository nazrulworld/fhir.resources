# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/RiskAssessment
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class RiskAssessment(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Potential outcomes for a subject with likelihood.
    An assessment of the likely outcome(s) for a patient or other subject as
    well as the likelihood of each outcome.
    """

    resource_type = Field("RiskAssessment", const=True)

    basedOn: fhirtypes.ReferenceType = Field(
        None,
        alias="basedOn",
        title="Request fulfilled by this assessment",
        description="A reference to the request that is fulfilled by this risk assessment.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    basis: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="basis",
        title="Information used in assessment",
        description=(
            "Indicates the source data considered as part of the assessment "
            "(FamilyHistory, Observations, Procedures, Conditions, etc.)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type of assessment",
        description="The type of the risk assessment performed.",
        # if property is element of this resource.
        element_property=True,
    )

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Comments on the risk assessment",
        description="Additional comments about the risk assessment.",
        # if property is element of this resource.
        element_property=True,
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    condition: fhirtypes.ReferenceType = Field(
        None,
        alias="condition",
        title="Condition assessed",
        description=(
            "For assessments or prognosis specific to a particular condition, "
            "indicates the condition being assessed."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Condition"],
    )

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title="Where was assessment performed?",
        description="The encounter where the assessment was performed.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter", "EpisodeOfCare"],
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Unique identifier for the assessment",
        description="Business identifier assigned to the risk assessment.",
        # if property is element of this resource.
        element_property=True,
    )

    method: fhirtypes.CodeableConceptType = Field(
        None,
        alias="method",
        title="Evaluation mechanism",
        description="The algorithm, process or mechanism used to evaluate the risk.",
        # if property is element of this resource.
        element_property=True,
    )

    mitigation: fhirtypes.String = Field(
        None,
        alias="mitigation",
        title="How to reduce risk",
        description=(
            "A description of the steps that might be taken to reduce the "
            "identified risk(s)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    mitigation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_mitigation", title="Extension field for ``mitigation``."
    )

    occurrenceDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurrenceDateTime",
        title="When was assessment made?",
        description="The date (and possibly time) the risk assessment was performed.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_occurrenceDateTime",
        title="Extension field for ``occurrenceDateTime``.",
    )

    occurrencePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="occurrencePeriod",
        title="When was assessment made?",
        description="The date (and possibly time) the risk assessment was performed.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )

    parent: fhirtypes.ReferenceType = Field(
        None,
        alias="parent",
        title="Part of this occurrence",
        description=(
            "A reference to a resource that this risk assessment is part of, such "
            "as a Procedure."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    performer: fhirtypes.ReferenceType = Field(
        None,
        alias="performer",
        title="Who did assessment?",
        description="The provider or software application that performed the assessment.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Device"],
    )

    prediction: typing.List[fhirtypes.RiskAssessmentPredictionType] = Field(
        None,
        alias="prediction",
        title="Outcome predicted",
        description="Describes the expected outcome for the subject.",
        # if property is element of this resource.
        element_property=True,
    )

    reasonCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reasonCodeableConcept",
        title="Why the assessment was necessary?",
        description="The reason the risk assessment was performed.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e reason[x]
        one_of_many="reason",
        one_of_many_required=False,
    )

    reasonReference: fhirtypes.ReferenceType = Field(
        None,
        alias="reasonReference",
        title="Why the assessment was necessary?",
        description="The reason the risk assessment was performed.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e reason[x]
        one_of_many="reason",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="registered | preliminary | final | amended +",
        description=(
            "The status of the RiskAssessment, using the same statuses as an "
            "Observation."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["registered", "preliminary", "final", "amended", "+"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Who/what does assessment apply to?",
        description="The patient or group the risk assessment applies to.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``RiskAssessment`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "identifier",
            "basedOn",
            "parent",
            "status",
            "method",
            "code",
            "subject",
            "context",
            "occurrenceDateTime",
            "occurrencePeriod",
            "condition",
            "performer",
            "reasonCodeableConcept",
            "reasonReference",
            "basis",
            "prediction",
            "mitigation",
            "comment",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1669(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1669(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "occurrence": ["occurrenceDateTime", "occurrencePeriod"],
            "reason": ["reasonCodeableConcept", "reasonReference"],
        }
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values


class RiskAssessmentPrediction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Outcome predicted.
    Describes the expected outcome for the subject.
    """

    resource_type = Field("RiskAssessmentPrediction", const=True)

    outcome: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="outcome",
        title="Possible outcome for the subject",
        description=(
            "One of the potential outcomes for the patient (e.g. remission, death,"
            "  a particular condition)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    probabilityDecimal: fhirtypes.Decimal = Field(
        None,
        alias="probabilityDecimal",
        title="Likelihood of specified outcome",
        description="How likely is the outcome (in the specified timeframe).",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e probability[x]
        one_of_many="probability",
        one_of_many_required=False,
    )
    probabilityDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_probabilityDecimal",
        title="Extension field for ``probabilityDecimal``.",
    )

    probabilityRange: fhirtypes.RangeType = Field(
        None,
        alias="probabilityRange",
        title="Likelihood of specified outcome",
        description="How likely is the outcome (in the specified timeframe).",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e probability[x]
        one_of_many="probability",
        one_of_many_required=False,
    )

    qualitativeRisk: fhirtypes.CodeableConceptType = Field(
        None,
        alias="qualitativeRisk",
        title="Likelihood of specified outcome as a qualitative value",
        description=(
            "How likely is the outcome (in the specified timeframe), expressed as a"
            " qualitative value (e.g. low, medium, high)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    rationale: fhirtypes.String = Field(
        None,
        alias="rationale",
        title="Explanation of prediction",
        description="Additional information explaining the basis for the prediction.",
        # if property is element of this resource.
        element_property=True,
    )
    rationale__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_rationale", title="Extension field for ``rationale``."
    )

    relativeRisk: fhirtypes.Decimal = Field(
        None,
        alias="relativeRisk",
        title="Relative likelihood",
        description=(
            "Indicates the risk for this particular subject (with their specific "
            "characteristics) divided by the risk of the population in general.  "
            "(Numbers greater than 1 = higher risk than the population, numbers "
            "less than 1 = lower risk.)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    relativeRisk__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_relativeRisk", title="Extension field for ``relativeRisk``."
    )

    whenPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="whenPeriod",
        title="Timeframe or age range",
        description=(
            "Indicates the period of time or age range of the subject to which the "
            "specified probability applies."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e when[x]
        one_of_many="when",
        one_of_many_required=False,
    )

    whenRange: fhirtypes.RangeType = Field(
        None,
        alias="whenRange",
        title="Timeframe or age range",
        description=(
            "Indicates the period of time or age range of the subject to which the "
            "specified probability applies."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e when[x]
        one_of_many="when",
        one_of_many_required=False,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``RiskAssessmentPrediction`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "outcome",
            "probabilityDecimal",
            "probabilityRange",
            "qualitativeRisk",
            "relativeRisk",
            "whenPeriod",
            "whenRange",
            "rationale",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2704(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "probability": ["probabilityDecimal", "probabilityRange"],
            "when": ["whenPeriod", "whenRange"],
        }
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values
