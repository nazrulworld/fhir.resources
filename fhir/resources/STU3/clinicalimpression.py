# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ClinicalImpression
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


class ClinicalImpression(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A clinical assessment performed when planning treatments and management
    strategies for a patient.
    A record of a clinical assessment performed to determine what problem(s)
    may affect the patient and before planning the treatments or management
    strategies that are best to manage a patient's condition. Assessments are
    often 1:1 with a clinical consultation / encounter,  but this varies
    greatly depending on the clinical workflow. This resource is called
    "ClinicalImpression" rather than "ClinicalAssessment" to avoid confusion
    with the recording of assessment tools such as Apgar score.
    """

    resource_type = Field("ClinicalImpression", const=True)

    action: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="action",
        title="Action taken as part of assessment procedure",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "ReferralRequest",
            "ProcedureRequest",
            "Procedure",
            "MedicationRequest",
            "Appointment",
        ],
    )

    assessor: fhirtypes.ReferenceType = Field(
        None,
        alias="assessor",
        title="The clinician performing the assessment",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Kind of assessment performed",
        description="Categorizes the type of clinical assessment performed.",
        # if property is element of this resource.
        element_property=True,
    )

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title="Encounter or Episode created from",
        description=(
            "The encounter or episode of care this impression was created as part "
            "of."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter", "EpisodeOfCare"],
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="When the assessment was documented",
        description="Indicates when the documentation of the assessment was complete.",
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Why/how the assessment was performed",
        description=(
            "A summary of the context and/or cause of the assessment - why / where "
            "was it performed, and what patient events/status prompted it."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    effectiveDateTime: fhirtypes.DateTime = Field(
        None,
        alias="effectiveDateTime",
        title="Time of assessment",
        description="The point in time or period over which the subject was assessed.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e effective[x]
        one_of_many="effective",
        one_of_many_required=False,
    )
    effectiveDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_effectiveDateTime",
        title="Extension field for ``effectiveDateTime``.",
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="Time of assessment",
        description="The point in time or period over which the subject was assessed.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e effective[x]
        one_of_many="effective",
        one_of_many_required=False,
    )

    finding: typing.List[fhirtypes.ClinicalImpressionFindingType] = Field(
        None,
        alias="finding",
        title="Possible or likely findings and diagnoses",
        description=(
            "Specific findings or diagnoses that was considered likely or relevant "
            "to ongoing treatment."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier",
        description=(
            "A unique identifier assigned to the clinical impression that remains "
            "consistent regardless of what server the impression is stored on."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    investigation: typing.List[fhirtypes.ClinicalImpressionInvestigationType] = Field(
        None,
        alias="investigation",
        title="One or more sets of investigations (signs, symptions, etc.)",
        description=(
            "One or more sets of investigations (signs, symptions, etc.). The "
            "actual grouping of investigations vary greatly depending on the type "
            "and context of the assessment. These investigations may include data "
            "generated during the assessment process, or data previously generated "
            "and recorded that is pertinent to the outcomes."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Comments made about the ClinicalImpression",
        description=(
            "Commentary about the impression, typically recorded after the "
            "impression itself was made, though supplemental notes by the original "
            "author could also appear."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    previous: fhirtypes.ReferenceType = Field(
        None,
        alias="previous",
        title="Reference to last assessment",
        description=(
            "A reference to the last assesment that was conducted bon this patient."
            " Assessments are often/usually ongoing in nature; a care provider "
            "(practitioner or team) will make new assessments on an ongoing basis "
            "as new data arises or the patient's conditions changes."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ClinicalImpression"],
    )

    problem: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="problem",
        title="Relevant impressions of patient state",
        description="This a list of the relevant problems/conditions for a patient.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Condition", "AllergyIntolerance"],
    )

    prognosisCodeableConcept: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="prognosisCodeableConcept",
        title="Estimate of likely outcome",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    prognosisReference: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="prognosisReference",
        title="RiskAssessment expressing likely outcome",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["RiskAssessment"],
    )

    protocol: typing.List[fhirtypes.Uri] = Field(
        None,
        alias="protocol",
        title="Clinical Protocol followed",
        description=(
            "Reference to a specific published clinical protocol that was followed "
            "during this assessment, and/or that provides evidence in support of "
            "the diagnosis."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    protocol__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_protocol", title="Extension field for ``protocol``.")

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | completed | entered-in-error",
        description="Identifies the workflow status of the assessment.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "completed", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Patient or group assessed",
        description="The patient or group of individuals assessed as part of this record.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group"],
    )

    summary: fhirtypes.String = Field(
        None,
        alias="summary",
        title="Summary of the assessment",
        description="A text summary of the investigations and the diagnosis.",
        # if property is element of this resource.
        element_property=True,
    )
    summary__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_summary", title="Extension field for ``summary``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClinicalImpression`` according specification,
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
            "status",
            "code",
            "description",
            "subject",
            "context",
            "effectiveDateTime",
            "effectivePeriod",
            "date",
            "assessor",
            "previous",
            "problem",
            "investigation",
            "protocol",
            "summary",
            "finding",
            "prognosisCodeableConcept",
            "prognosisReference",
            "action",
            "note",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2041(
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
    def validate_one_of_many_2041(
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
        one_of_many_fields = {"effective": ["effectiveDateTime", "effectivePeriod"]}
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


class ClinicalImpressionFinding(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Possible or likely findings and diagnoses.
    Specific findings or diagnoses that was considered likely or relevant to
    ongoing treatment.
    """

    resource_type = Field("ClinicalImpressionFinding", const=True)

    basis: fhirtypes.String = Field(
        None,
        alias="basis",
        title="Which investigations support finding",
        description="Which investigations support finding or diagnosis.",
        # if property is element of this resource.
        element_property=True,
    )
    basis__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_basis", title="Extension field for ``basis``."
    )

    itemCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="itemCodeableConcept",
        title="What was found",
        description=(
            "Specific text, code or reference for finding or diagnosis, which may "
            "include ruled-out or resolved conditions."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e item[x]
        one_of_many="item",
        one_of_many_required=True,
    )

    itemReference: fhirtypes.ReferenceType = Field(
        None,
        alias="itemReference",
        title="What was found",
        description=(
            "Specific text, code or reference for finding or diagnosis, which may "
            "include ruled-out or resolved conditions."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e item[x]
        one_of_many="item",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Condition", "Observation"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClinicalImpressionFinding`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "itemCodeableConcept",
            "itemReference",
            "itemReference",
            "basis",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2737(
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
        one_of_many_fields = {"item": ["itemCodeableConcept", "itemReference"]}
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


class ClinicalImpressionInvestigation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    One or more sets of investigations (signs, symptions, etc.).
    One or more sets of investigations (signs, symptions, etc.). The actual
    grouping of investigations vary greatly depending on the type and context
    of the assessment. These investigations may include data generated during
    the assessment process, or data previously generated and recorded that is
    pertinent to the outcomes.
    """

    resource_type = Field("ClinicalImpressionInvestigation", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="A name/code for the set",
        description=(
            'A name/code for the group ("set") of investigations. Typically, this '
            'will be something like "signs", "symptoms", "clinical", "diagnostic", '
            "but the list is not constrained, and others such groups such as "
            "(exposure|family|travel|nutitirional) history may be used."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    item: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="item",
        title="Record of a specific investigation",
        description="A record of a specific investigation that was undertaken.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Observation",
            "QuestionnaireResponse",
            "FamilyMemberHistory",
            "DiagnosticReport",
            "RiskAssessment",
            "ImagingStudy",
        ],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClinicalImpressionInvestigation`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "item"]
