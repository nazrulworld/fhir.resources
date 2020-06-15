# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ResearchStudy
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ResearchStudy(domainresource.DomainResource):
    """ Investigation to increase healthcare-related patient-independent knowledge.
    A process where a researcher or organization plans and then executes a
    series of steps intended to increase the field of healthcare-related
    knowledge.  This includes studies of safety, efficacy, comparative
    effectiveness and other information about medications, devices, therapies
    and other interventional and investigative techniques.  A ResearchStudy
    involves the gathering of information about human or animal subjects.
    """

    resource_type = Field("ResearchStudy", const=True)

    arm: ListType[fhirtypes.ResearchStudyArmType] = Field(
        None,
        alias="arm",
        title="List of `ResearchStudyArm` items (represented as `dict` in JSON)",
        description="Defined path through the study for a subject",
    )

    category: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Classifications for the study",
    )

    condition: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="condition",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Condition being studied",
    )

    contact: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Contact details for the study",
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="What this is study doing",
    )

    enrollment: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="enrollment",
        title=(
            "List of `Reference` items referencing `Group` (represented as `dict` "
            "in JSON)"
        ),
        description="Inclusion \u0026 exclusion criteria",
    )

    focus: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="focus",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Drugs, devices, etc. under study",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business Identifier for study",
    )

    keyword: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="keyword",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Used to search for the study",
    )

    location: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="location",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Geographic region(s) for study",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Comments made about the study",
    )

    objective: ListType[fhirtypes.ResearchStudyObjectiveType] = Field(
        None,
        alias="objective",
        title="List of `ResearchStudyObjective` items (represented as `dict` in JSON)",
        description="A goal for the study",
    )

    partOf: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title=(
            "List of `Reference` items referencing `ResearchStudy` (represented as "
            "`dict` in JSON)"
        ),
        description="Part of larger study",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When the study began and ended",
    )

    phase: fhirtypes.CodeableConceptType = Field(
        None,
        alias="phase",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "n-a | early-phase-1 | phase-1 | phase-1-phase-2 | phase-2 | "
            "phase-2-phase-3 | phase-3 | phase-4"
        ),
    )

    primaryPurposeType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="primaryPurposeType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "treatment | prevention | diagnostic | supportive-care | screening | "
            "health-services-research | basic-science | device-feasibility"
        ),
    )

    principalInvestigator: fhirtypes.ReferenceType = Field(
        None,
        alias="principalInvestigator",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole` "
            "(represented as `dict` in JSON)"
        ),
        description="Researcher who oversees multiple aspects of the study",
    )

    protocol: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="protocol",
        title=(
            "List of `Reference` items referencing `PlanDefinition` (represented as"
            " `dict` in JSON)"
        ),
        description="Steps followed in executing study",
    )

    reasonStopped: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reasonStopped",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "accrual-goal-met | closed-due-to-toxicity | closed-due-to-lack-of-"
            "study-progress | temporarily-closed-per-study-design"
        ),
    )

    relatedArtifact: ListType[fhirtypes.RelatedArtifactType] = Field(
        None,
        alias="relatedArtifact",
        title="List of `RelatedArtifact` items (represented as `dict` in JSON)",
        description="References and dependencies",
    )

    site: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="site",
        title=(
            "List of `Reference` items referencing `Location` (represented as "
            "`dict` in JSON)"
        ),
        description="Facility where study activities are conducted",
    )

    sponsor: fhirtypes.ReferenceType = Field(
        None,
        alias="sponsor",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Organization that initiates and is legally responsible for the study",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "active | administratively-completed | approved | closed-to-accrual | "
            "closed-to-accrual-and-intervention | completed | disapproved | in-"
            "review | temporarily-closed-to-accrual | temporarily-closed-to-"
            "accrual-and-intervention | withdrawn"
        ),
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this study",
    )


class ResearchStudyArm(backboneelement.BackboneElement):
    """ Defined path through the study for a subject.
    Describes an expected sequence of events for one of the participants of a
    study.  E.g. Exposure to drug A, wash-out, exposure to drug B, wash-out,
    follow-up.
    """

    resource_type = Field("ResearchStudyArm", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Short explanation of study path",
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Label for study arm",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Categorization of study arm",
    )


class ResearchStudyObjective(backboneelement.BackboneElement):
    """ A goal for the study.
    A goal that the study is aiming to achieve in terms of a scientific
    question to be answered by the analysis of data collected during the study.
    """

    resource_type = Field("ResearchStudyObjective", const=True)

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Label for the objective",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="primary | secondary | exploratory",
    )
