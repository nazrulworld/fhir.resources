from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ResearchStudy
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ResearchStudy(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Investigation to increase healthcare-related patient-independent knowledge.
    A process where a researcher or organization plans and then executes a
    series of steps intended to increase the field of healthcare-related
    knowledge.  This includes studies of safety, efficacy, comparative
    effectiveness and other information about medications, devices, therapies
    and other interventional and investigative techniques.  A ResearchStudy
    involves the gathering of information about human or animal subjects.
    """

    __resource_type__ = "ResearchStudy"

    arm: typing.List[fhirtypes.ResearchStudyArmType] | None = Field(  # type: ignore
        None,
        alias="arm",
        title="Defined path through the study for a subject",
        description=(
            "Describes an expected sequence of events for one of the participants "
            "of a study.  E.g. Exposure to drug A, wash-out, exposure to drug B, "
            "wash-out, follow-up."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    category: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="category",
        title="Classifications for the study",
        description=(
            "Codes categorizing the type of study such as investigational vs. "
            "observational, type of blinding, type of randomization, safety vs. "
            "efficacy, etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    contact: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        None,
        alias="contact",
        title="Contact details for the study",
        description=(
            "Contact details to assist a user in learning more about or engaging "
            "with the study."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="What this is study doing",
        description="A full description of how the study is being conducted.",
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    enrollment: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="enrollment",
        title="Inclusion & exclusion criteria",
        description=(
            "Reference to a Group that defines the criteria for and quantity of "
            'subjects participating in the study.  E.g. " 200 female Europeans '
            'between the ages of 20 and 45 with early onset diabetes".'
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Group"],
        },
    )

    focus: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="focus",
        title="Drugs, devices, conditions, etc. under study",
        description=(
            "The condition(s), medication(s), food(s), therapy(ies), device(s) or "
            "other concerns or interventions that the study is seeking to gain more"
            " information about."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business Identifier for study",
        description=(
            "Identifiers assigned to this research study by the sponsor or other "
            "systems."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="jurisdiction",
        title="Geographic region(s) for study",
        description=(
            "Indicates a country, state or other region where the study is taking "
            "place."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    keyword: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="keyword",
        title="Used to search for the study",
        description="Key terms to aid in searching for or filtering the study.",
        json_schema_extra={
            "element_property": True,
        },
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="note",
        title="Comments made about the event",
        description=(
            "Comments made about the event by the performer, subject or other "
            "participants."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    partOf: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="partOf",
        title="Part of larger study",
        description=(
            "A larger research study of which this particular study is a component "
            "or step."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ResearchStudy"],
        },
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="period",
        title="When the study began and ended",
        description=(
            "Identifies the start date and the expected (or actual, depending on "
            "status) end date for the study."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    principalInvestigator: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="principalInvestigator",
        title="The individual responsible for the study",
        description=(
            "Indicates the individual who has primary oversite of the execution of "
            "the study."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner"],
        },
    )

    protocol: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="protocol",
        title="Steps followed in executing study",
        description=(
            "The set of steps expected to be performed as part of the execution of "
            "the study."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["PlanDefinition"],
        },
    )

    reasonStopped: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="reasonStopped",
        title="Reason for terminating study early",
        description=(
            "A description and/or code explaining the premature termination of the "
            "study."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    relatedArtifact: typing.List[fhirtypes.RelatedArtifactType] | None = Field(  # type: ignore
        None,
        alias="relatedArtifact",
        title="References and dependencies",
        description="Citations, references and other related documents.",
        json_schema_extra={
            "element_property": True,
        },
    )

    site: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="site",
        title="Location involved in study execution",
        description=(
            "Clinic, hospital or other healthcare location that is participating in"
            " the study."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    sponsor: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="sponsor",
        title="Organization responsible for the study",
        description="The organization responsible for the execution of the study.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title=(
            "draft | in-progress | suspended | stopped | completed | entered-in-"
            "error"
        ),
        description="The current state of the study.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "draft",
                "in-progress",
                "suspended",
                "stopped",
                "completed",
                "entered-in-error",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Name for this study",
        description="A short, descriptive user-friendly label for the study.",
        json_schema_extra={
            "element_property": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ResearchStudy`` according specification,
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
            "title",
            "protocol",
            "partOf",
            "status",
            "category",
            "focus",
            "contact",
            "relatedArtifact",
            "keyword",
            "jurisdiction",
            "description",
            "enrollment",
            "period",
            "sponsor",
            "principalInvestigator",
            "site",
            "reasonStopped",
            "note",
            "arm",
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


class ResearchStudyArm(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Defined path through the study for a subject.
    Describes an expected sequence of events for one of the participants of a
    study.  E.g. Exposure to drug A, wash-out, exposure to drug B, wash-out,
    follow-up.
    """

    __resource_type__ = "ResearchStudyArm"

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Categorization of study arm",
        description=(
            "Categorization of study arm, e.g. experimental, active comparator, "
            "placebo comparater."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    description: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Short explanation of study path",
        description=(
            "A succinct description of the path through the study that would be "
            "followed by a subject adhering to this arm."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Label for study arm",
        description="Unique, human-readable label for this arm of the study.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ResearchStudyArm`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "name", "code", "description"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("name", "name__ext")]
        return required_fields
