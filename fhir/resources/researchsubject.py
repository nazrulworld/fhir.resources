# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ResearchSubject
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class ResearchSubject(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Participant or object which is the recipient of investigative activities in
    a study.
    A ResearchSubject is a participant or object which is the recipient of
    investigative activities in a research study.
    """

    resource_type = Field("ResearchSubject", const=True)

    actualComparisonGroup: fhirtypes.Id = Field(
        None,
        alias="actualComparisonGroup",
        title="What path was followed",
        description=(
            "The name of the arm in the study the subject actually followed as part"
            " of this study."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    actualComparisonGroup__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_actualComparisonGroup",
        title="Extension field for ``actualComparisonGroup``.",
    )

    assignedComparisonGroup: fhirtypes.Id = Field(
        None,
        alias="assignedComparisonGroup",
        title="What path should be followed",
        description=(
            "The name of the arm in the study the subject is expected to follow as "
            "part of this study."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    assignedComparisonGroup__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_assignedComparisonGroup",
        title="Extension field for ``assignedComparisonGroup``.",
    )

    consent: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="consent",
        title="Agreement to participate in study",
        description=(
            "A record of the patient's informed agreement to participate in the "
            "study."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Consent"],
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier for research subject in a study",
        description="Identifiers assigned to this research subject for a study.",
        # if property is element of this resource.
        element_property=True,
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Start and end of participation",
        description=(
            "The dates the subject began and ended their participation in the " "study."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    progress: typing.List[fhirtypes.ResearchSubjectProgressType] = Field(
        None,
        alias="progress",
        title="Subject status",
        description=(
            "The current state (status) of the subject and resons for status change"
            " where appropriate."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description="The publication state of the resource (not of the subject).",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired", "unknown"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    study: fhirtypes.ReferenceType = Field(
        ...,
        alias="study",
        title="Study subject is part of",
        description="Reference to the study the subject is participating in.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ResearchStudy"],
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Who or what is part of study",
        description=(
            "The record of the person, animal or other entity involved in the " "study."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "Group",
            "Specimen",
            "Device",
            "Medication",
            "Substance",
            "BiologicallyDerivedProduct",
        ],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ResearchSubject`` according specification,
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
            "progress",
            "period",
            "study",
            "subject",
            "assignedComparisonGroup",
            "actualComparisonGroup",
            "consent",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1731(
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


class ResearchSubjectProgress(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Subject status.
    The current state (status) of the subject and resons for status change
    where appropriate.
    """

    resource_type = Field("ResearchSubjectProgress", const=True)

    endDate: fhirtypes.DateTime = Field(
        None,
        alias="endDate",
        title="State change date",
        description="The date when the state ended.",
        # if property is element of this resource.
        element_property=True,
    )
    endDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_endDate", title="Extension field for ``endDate``."
    )

    milestone: fhirtypes.CodeableConceptType = Field(
        None,
        alias="milestone",
        title="SignedUp | Screened | Randomized",
        description="The milestones the subject has passed through.",
        # if property is element of this resource.
        element_property=True,
    )

    reason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reason",
        title="State change reason",
        description=(
            "The reason for the state change.  If coded it should follow the formal"
            " subject state model."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    startDate: fhirtypes.DateTime = Field(
        None,
        alias="startDate",
        title="State change date",
        description="The date when the new status started.",
        # if property is element of this resource.
        element_property=True,
    )
    startDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_startDate", title="Extension field for ``startDate``."
    )

    subjectState: fhirtypes.CodeableConceptType = Field(
        None,
        alias="subjectState",
        title=(
            "candidate | eligible | follow-up | ineligible | not-registered | off-"
            "study | on-study | on-study-intervention | on-study-observation | "
            "pending-on-study | potential-candidate | screening | withdrawn"
        ),
        description="The current state of the subject.",
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="state | milestone",
        description=(
            "Identifies the aspect of the subject's journey that the state refers "
            "to."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ResearchSubjectProgress`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "subjectState",
            "milestone",
            "reason",
            "startDate",
            "endDate",
        ]
