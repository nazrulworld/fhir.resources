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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Insurance or medical plan or a payment agreement.
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
        None, alias="dependent", title="Type `String`", description="Dependent number"
    )
    dependent__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_dependent", title="Extension field for ``dependent``."
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
        None, alias="network", title="Type `String`", description="Insurer network"
    )
    network__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_network", title="Extension field for ``network``."
    )

    order: fhirtypes.PositiveInt = Field(
        None,
        alias="order",
        title="Type `PositiveInt`",
        description="Relative order of the coverage",
    )
    order__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_order", title="Extension field for ``order``."
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
        title="Type `String`",
        description="The plan instance or sequence counter",
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code`",
        description="active | cancelled | draft | entered-in-error",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
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
        title="Type `String`",
        description="ID assigned to the Subscriber",
    )
    subscriberId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_subscriberId", title="Extension field for ``subscriberId``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of coverage such as medical or accident",
    )


class CoverageGrouping(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional coverage classifications.
    A suite of underwrite specific classifiers, for example may be used to
    identify a class of coverage or employer group, Policy, Plan.
    """

    resource_type = Field("CoverageGrouping", const=True)

    classDisplay: fhirtypes.String = Field(
        None,
        alias="classDisplay",
        title="Type `String`",
        description="Display text for the class",
    )
    classDisplay__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_classDisplay", title="Extension field for ``classDisplay``."
    )

    class_fhir: fhirtypes.String = Field(
        None,
        alias="class",
        title="Type `String`",
        description="An identifier for the class",
    )
    class__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_class", title="Extension field for ``class_fhir``."
    )

    group: fhirtypes.String = Field(
        None,
        alias="group",
        title="Type `String`",
        description="An identifier for the group",
    )
    group__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_group", title="Extension field for ``group``."
    )

    groupDisplay: fhirtypes.String = Field(
        None,
        alias="groupDisplay",
        title="Type `String`",
        description="Display text for an identifier for the group",
    )
    groupDisplay__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_groupDisplay", title="Extension field for ``groupDisplay``."
    )

    plan: fhirtypes.String = Field(
        None,
        alias="plan",
        title="Type `String`",
        description="An identifier for the plan",
    )
    plan__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_plan", title="Extension field for ``plan``."
    )

    planDisplay: fhirtypes.String = Field(
        None,
        alias="planDisplay",
        title="Type `String`",
        description="Display text for the plan",
    )
    planDisplay__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_planDisplay", title="Extension field for ``planDisplay``."
    )

    subClass: fhirtypes.String = Field(
        None,
        alias="subClass",
        title="Type `String`",
        description="An identifier for the subsection of the class",
    )
    subClass__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_subClass", title="Extension field for ``subClass``."
    )

    subClassDisplay: fhirtypes.String = Field(
        None,
        alias="subClassDisplay",
        title="Type `String`",
        description="Display text for the subsection of the subclass",
    )
    subClassDisplay__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_subClassDisplay", title="Extension field for ``subClassDisplay``."
    )

    subGroup: fhirtypes.String = Field(
        None,
        alias="subGroup",
        title="Type `String`",
        description="An identifier for the subsection of the group",
    )
    subGroup__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_subGroup", title="Extension field for ``subGroup``."
    )

    subGroupDisplay: fhirtypes.String = Field(
        None,
        alias="subGroupDisplay",
        title="Type `String`",
        description="Display text for the subsection of the group",
    )
    subGroupDisplay__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_subGroupDisplay", title="Extension field for ``subGroupDisplay``."
    )

    subPlan: fhirtypes.String = Field(
        None,
        alias="subPlan",
        title="Type `String`",
        description="An identifier for the subsection of the plan",
    )
    subPlan__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_subPlan", title="Extension field for ``subPlan``."
    )

    subPlanDisplay: fhirtypes.String = Field(
        None,
        alias="subPlanDisplay",
        title="Type `String`",
        description="Display text for the subsection of the plan",
    )
    subPlanDisplay__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_subPlanDisplay", title="Extension field for ``subPlanDisplay``."
    )
