# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Coverage
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic.v1 import Field

from . import backboneelement, domainresource, fhirtypes


class Coverage(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
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
        title="Plan Beneficiary",
        description=(
            "The party who benefits from the insurance coverage., the patient when "
            "services are provided."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    contract: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="contract",
        title="Contract details",
        description="The policy(s) which constitute this insurance coverage.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Contract"],
    )

    dependent: fhirtypes.String = Field(
        None,
        alias="dependent",
        title="Dependent number",
        description="A unique identifier for a dependent under the coverage.",
        # if property is element of this resource.
        element_property=True,
    )
    dependent__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_dependent", title="Extension field for ``dependent``."
    )

    grouping: fhirtypes.CoverageGroupingType = Field(
        None,
        alias="grouping",
        title="Additional coverage classifications",
        description=(
            "A suite of underwrite specific classifiers, for example may be used to"
            " identify a class of coverage or employer group, Policy, Plan."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="The primary coverage ID",
        description=(
            "The main (and possibly only) identifier for the coverage - often "
            "referred to as a Member Id, Certificate number, Personal Health Number"
            " or Case ID. May be constructed as the concatination of the "
            "Coverage.SubscriberID and the Coverage.dependant."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    network: fhirtypes.String = Field(
        None,
        alias="network",
        title="Insurer network",
        description=(
            "The insurer-specific identifier for the insurer-defined network of "
            "providers to which the beneficiary may seek treatment which will be "
            "covered at the 'in-network' rate, otherwise 'out of network' terms and"
            " conditions apply."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    network__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_network", title="Extension field for ``network``."
    )

    order: fhirtypes.PositiveInt = Field(
        None,
        alias="order",
        title="Relative order of the coverage",
        description=(
            "The order of applicability of this coverage relative to other "
            "coverages which are currently inforce. Note, there may be gaps in the "
            "numbering and this does not imply primary, secondard etc. as the "
            "specific positioning of coverages depends upon the episode of care."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    order__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_order", title="Extension field for ``order``."
    )

    payor: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="payor",
        title="Identifier for the plan or agreement issuer",
        description=(
            "The program or plan underwriter or payor including both insurance and "
            "non-insurance agreements, such as patient-pay agreements. May provide "
            "multiple identifiers such as insurance company identifier or business "
            "identifier (BIN number)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization", "Patient", "RelatedPerson"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Coverage start and end dates",
        description=(
            "Time period during which the coverage is in force. A missing start "
            "date indicates the start date isn't known, a missing end date means "
            "the coverage is continuing to be in force."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    policyHolder: fhirtypes.ReferenceType = Field(
        None,
        alias="policyHolder",
        title="Owner of the policy",
        description=(
            "The party who 'owns' the insurance policy,  may be an individual, "
            "corporation or the subscriber's employer."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "RelatedPerson", "Organization"],
    )

    relationship: fhirtypes.CodeableConceptType = Field(
        None,
        alias="relationship",
        title="Beneficiary relationship to the Subscriber",
        description="The relationship of beneficiary (patient) to the subscriber.",
        # if property is element of this resource.
        element_property=True,
    )

    sequence: fhirtypes.String = Field(
        None,
        alias="sequence",
        title="The plan instance or sequence counter",
        description=(
            "An optional counter for a particular instance of the identified "
            "coverage which increments upon each renewal."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="active | cancelled | draft | entered-in-error",
        description="The status of the resource instance.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "cancelled", "draft", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subscriber: fhirtypes.ReferenceType = Field(
        None,
        alias="subscriber",
        title="Subscriber to the policy",
        description=(
            "The party who has signed-up for or 'owns' the contractual relationship"
            " to the policy or to whom the benefit of the policy for services "
            "rendered to them or their family is due."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "RelatedPerson"],
    )

    subscriberId: fhirtypes.String = Field(
        None,
        alias="subscriberId",
        title="ID assigned to the Subscriber",
        description="The insurer assigned ID for the Subscriber.",
        # if property is element of this resource.
        element_property=True,
    )
    subscriberId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_subscriberId", title="Extension field for ``subscriberId``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type of coverage such as medical or accident",
        description=(
            "The type of coverage: social program, medical plan, accident coverage "
            "(workers compensation, auto), group health or payment by an individual"
            " or organization."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Coverage`` according specification,
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
            "type",
            "policyHolder",
            "subscriber",
            "subscriberId",
            "beneficiary",
            "relationship",
            "period",
            "payor",
            "grouping",
            "dependent",
            "sequence",
            "order",
            "network",
            "contract",
        ]


class CoverageGrouping(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
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
        title="Display text for the class",
        description="A short description for the class.",
        # if property is element of this resource.
        element_property=True,
    )
    classDisplay__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_classDisplay", title="Extension field for ``classDisplay``."
    )

    class_fhir: fhirtypes.String = Field(
        None,
        alias="class",
        title="An identifier for the class",
        description=(
            "Identifies a style or collective of coverage issues by the "
            "underwriter, for example may be used to identify a class of coverage "
            "such as a level of deductables or co-payment."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    class__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_class", title="Extension field for ``class_fhir``."
    )

    group: fhirtypes.String = Field(
        None,
        alias="group",
        title="An identifier for the group",
        description=(
            "Identifies a style or collective of coverage issued by the "
            "underwriter, for example may be used to identify an employer group. "
            "May also be referred to as a Policy or Group ID."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    group__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_group", title="Extension field for ``group``."
    )

    groupDisplay: fhirtypes.String = Field(
        None,
        alias="groupDisplay",
        title="Display text for an identifier for the group",
        description="A short description for the group.",
        # if property is element of this resource.
        element_property=True,
    )
    groupDisplay__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_groupDisplay", title="Extension field for ``groupDisplay``."
    )

    plan: fhirtypes.String = Field(
        None,
        alias="plan",
        title="An identifier for the plan",
        description=(
            "Identifies a style or collective of coverage issued by the "
            "underwriter, for example may be used to identify a collection of "
            "benefits provided to employees. May be referred to as a Section or "
            "Division ID."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    plan__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_plan", title="Extension field for ``plan``."
    )

    planDisplay: fhirtypes.String = Field(
        None,
        alias="planDisplay",
        title="Display text for the plan",
        description="A short description for the plan.",
        # if property is element of this resource.
        element_property=True,
    )
    planDisplay__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_planDisplay", title="Extension field for ``planDisplay``."
    )

    subClass: fhirtypes.String = Field(
        None,
        alias="subClass",
        title="An identifier for the subsection of the class",
        description=(
            "Identifies a sub-style or sub-collective of coverage issues by the "
            "underwriter, for example may be used to identify a subclass of "
            "coverage such as a sub-level of deductables or co-payment."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    subClass__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_subClass", title="Extension field for ``subClass``."
    )

    subClassDisplay: fhirtypes.String = Field(
        None,
        alias="subClassDisplay",
        title="Display text for the subsection of the subclass",
        description="A short description for the subclass.",
        # if property is element of this resource.
        element_property=True,
    )
    subClassDisplay__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_subClassDisplay", title="Extension field for ``subClassDisplay``."
    )

    subGroup: fhirtypes.String = Field(
        None,
        alias="subGroup",
        title="An identifier for the subsection of the group",
        description=(
            "Identifies a style or collective of coverage issued by the "
            "underwriter, for example may be used to identify a subset of an "
            "employer group."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    subGroup__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_subGroup", title="Extension field for ``subGroup``."
    )

    subGroupDisplay: fhirtypes.String = Field(
        None,
        alias="subGroupDisplay",
        title="Display text for the subsection of the group",
        description="A short description for the subgroup.",
        # if property is element of this resource.
        element_property=True,
    )
    subGroupDisplay__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_subGroupDisplay", title="Extension field for ``subGroupDisplay``."
    )

    subPlan: fhirtypes.String = Field(
        None,
        alias="subPlan",
        title="An identifier for the subsection of the plan",
        description=(
            "Identifies a sub-style or sub-collective of coverage issued by the "
            "underwriter, for example may be used to identify a subset of a "
            "collection of benefits provided to employees."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    subPlan__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_subPlan", title="Extension field for ``subPlan``."
    )

    subPlanDisplay: fhirtypes.String = Field(
        None,
        alias="subPlanDisplay",
        title="Display text for the subsection of the plan",
        description="A short description for the subplan.",
        # if property is element of this resource.
        element_property=True,
    )
    subPlanDisplay__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_subPlanDisplay", title="Extension field for ``subPlanDisplay``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CoverageGrouping`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "group",
            "groupDisplay",
            "subGroup",
            "subGroupDisplay",
            "plan",
            "planDisplay",
            "subPlan",
            "subPlanDisplay",
            "class",
            "classDisplay",
            "subClass",
            "subClassDisplay",
        ]
