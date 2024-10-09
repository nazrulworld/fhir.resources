from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ResearchSubject
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

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

    __resource_type__ = "ResearchSubject"

    actualComparisonGroup: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="actualComparisonGroup",
        title="What path was followed",
        description=(
            "The name of the arm in the study the subject actually followed as part"
            " of this study."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    actualComparisonGroup__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_actualComparisonGroup",
        title="Extension field for ``actualComparisonGroup``.",
    )

    assignedComparisonGroup: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="assignedComparisonGroup",
        title="What path should be followed",
        description=(
            "The name of the arm in the study the subject is expected to follow as "
            "part of this study."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    assignedComparisonGroup__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_assignedComparisonGroup",
        title="Extension field for ``assignedComparisonGroup``.",
    )

    consent: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="consent",
        title="Agreement to participate in study",
        description=(
            "A record of the patient's informed agreement to participate in the "
            "study."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Consent"],
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business Identifier for research subject in a study",
        description="Identifiers assigned to this research subject for a study.",
        json_schema_extra={
            "element_property": True,
        },
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="period",
        title="Start and end of participation",
        description=(
            "The dates the subject began and ended their participation in the " "study."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    progress: typing.List[fhirtypes.ResearchSubjectProgressType] | None = Field(  # type: ignore
        None,
        alias="progress",
        title="Subject status",
        description=(
            "The current state (status) of the subject and resons for status change"
            " where appropriate."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description="The publication state of the resource (not of the subject).",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["draft", "active", "retired", "unknown"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    study: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="study",
        title="Study subject is part of",
        description="Reference to the study the subject is participating in.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ResearchStudy"],
        },
    )

    subject: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="subject",
        title="Who or what is part of study",
        description=(
            "The record of the person, animal or other entity involved in the " "study."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Patient",
                "Group",
                "Specimen",
                "Device",
                "Medication",
                "Substance",
                "BiologicallyDerivedProduct",
            ],
        },
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

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        return required_fields


class ResearchSubjectProgress(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Subject status.
    The current state (status) of the subject and resons for status change
    where appropriate.
    """

    __resource_type__ = "ResearchSubjectProgress"

    endDate: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="endDate",
        title="State change date",
        description="The date when the state ended.",
        json_schema_extra={
            "element_property": True,
        },
    )
    endDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_endDate", title="Extension field for ``endDate``."
    )

    milestone: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="milestone",
        title="SignedUp | Screened | Randomized",
        description="The milestones the subject has passed through.",
        json_schema_extra={
            "element_property": True,
        },
    )

    reason: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="reason",
        title="State change reason",
        description=(
            "The reason for the state change.  If coded it should follow the formal"
            " subject state model."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    startDate: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="startDate",
        title="State change date",
        description="The date when the new status started.",
        json_schema_extra={
            "element_property": True,
        },
    )
    startDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_startDate", title="Extension field for ``startDate``."
    )

    subjectState: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="subjectState",
        title=(
            "candidate | eligible | follow-up | ineligible | not-registered | off-"
            "study | on-study | on-study-intervention | on-study-observation | "
            "pending-on-study | potential-candidate | screening | withdrawn"
        ),
        description="The current state of the subject.",
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="state | milestone",
        description=(
            "Identifies the aspect of the subject's journey that the state refers "
            "to."
        ),
        json_schema_extra={
            "element_property": True,
        },
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
