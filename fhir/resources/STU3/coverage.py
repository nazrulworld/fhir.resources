# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Coverage
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Coverage(domainresource.DomainResource):
    """ Insurance or medical plan or a payment agreement.
    Financial instrument which may be used to reimburse or pay for health care
    products and services.
    """

    resource_type = Field("Coverage", const=True)

    beneficiary: fhirtypes.ReferenceType = Field(
        None,
        alias="beneficiary",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="Plan Beneficiary",
    )

    contract: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="contract",
        title=(
            "List of `Reference` items referencing `Contract` (represented as "
            "`dict` in JSON)"
        ),
        description="Contract details",
    )

    dependent: fhirtypes.String = Field(
        None,
        alias="dependent",
        title="Type `String` (represented as `dict` in JSON)",
        description="Dependent number",
    )

    grouping: fhirtypes.CoverageGroupingType = Field(
        None,
        alias="grouping",
        title="Type `CoverageGrouping` (represented as `dict` in JSON)",
        description="Additional coverage classifications",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="The primary coverage ID",
    )

    network: fhirtypes.String = Field(
        None,
        alias="network",
        title="Type `String` (represented as `dict` in JSON)",
        description="Insurer network",
    )

    order: fhirtypes.PositiveInt = Field(
        None,
        alias="order",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Relative order of the coverage",
    )

    payor: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="payor",
        title=(
            "List of `Reference` items referencing `Organization, Patient, "
            "RelatedPerson` (represented as `dict` in JSON)"
        ),
        description="Identifier for the plan or agreement issuer",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Coverage start and end dates",
    )

    policyHolder: fhirtypes.ReferenceType = Field(
        None,
        alias="policyHolder",
        title=(
            "Type `Reference` referencing `Patient, RelatedPerson, Organization` "
            "(represented as `dict` in JSON)"
        ),
        description="Owner of the policy",
    )

    relationship: fhirtypes.CodeableConceptType = Field(
        None,
        alias="relationship",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Beneficiary relationship to the Subscriber",
    )

    sequence: fhirtypes.String = Field(
        None,
        alias="sequence",
        title="Type `String` (represented as `dict` in JSON)",
        description="The plan instance or sequence counter",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="active | cancelled | draft | entered-in-error",
    )

    subscriber: fhirtypes.ReferenceType = Field(
        None,
        alias="subscriber",
        title=(
            "Type `Reference` referencing `Patient, RelatedPerson` (represented as "
            "`dict` in JSON)"
        ),
        description="Subscriber to the policy",
    )

    subscriberId: fhirtypes.String = Field(
        None,
        alias="subscriberId",
        title="Type `String` (represented as `dict` in JSON)",
        description="ID assigned to the Subscriber",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of coverage such as medical or accident",
    )


class CoverageGrouping(backboneelement.BackboneElement):
    """ Additional coverage classifications.
    A suite of underwrite specific classifiers, for example may be used to
    identify a class of coverage or employer group, Policy, Plan.
    """

    resource_type = Field("CoverageGrouping", const=True)

    classDisplay: fhirtypes.String = Field(
        None,
        alias="classDisplay",
        title="Type `String` (represented as `dict` in JSON)",
        description="Display text for the class",
    )

    class_fhir: fhirtypes.String = Field(
        None,
        alias="class",
        title="Type `String` (represented as `dict` in JSON)",
        description="An identifier for the class",
    )

    group: fhirtypes.String = Field(
        None,
        alias="group",
        title="Type `String` (represented as `dict` in JSON)",
        description="An identifier for the group",
    )

    groupDisplay: fhirtypes.String = Field(
        None,
        alias="groupDisplay",
        title="Type `String` (represented as `dict` in JSON)",
        description="Display text for an identifier for the group",
    )

    plan: fhirtypes.String = Field(
        None,
        alias="plan",
        title="Type `String` (represented as `dict` in JSON)",
        description="An identifier for the plan",
    )

    planDisplay: fhirtypes.String = Field(
        None,
        alias="planDisplay",
        title="Type `String` (represented as `dict` in JSON)",
        description="Display text for the plan",
    )

    subClass: fhirtypes.String = Field(
        None,
        alias="subClass",
        title="Type `String` (represented as `dict` in JSON)",
        description="An identifier for the subsection of the class",
    )

    subClassDisplay: fhirtypes.String = Field(
        None,
        alias="subClassDisplay",
        title="Type `String` (represented as `dict` in JSON)",
        description="Display text for the subsection of the subclass",
    )

    subGroup: fhirtypes.String = Field(
        None,
        alias="subGroup",
        title="Type `String` (represented as `dict` in JSON)",
        description="An identifier for the subsection of the group",
    )

    subGroupDisplay: fhirtypes.String = Field(
        None,
        alias="subGroupDisplay",
        title="Type `String` (represented as `dict` in JSON)",
        description="Display text for the subsection of the group",
    )

    subPlan: fhirtypes.String = Field(
        None,
        alias="subPlan",
        title="Type `String` (represented as `dict` in JSON)",
        description="An identifier for the subsection of the plan",
    )

    subPlanDisplay: fhirtypes.String = Field(
        None,
        alias="subPlanDisplay",
        title="Type `String` (represented as `dict` in JSON)",
        description="Display text for the subsection of the plan",
    )
