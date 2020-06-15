# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Consent
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Consent(domainresource.DomainResource):
    """ A healthcare consumer's  choices to permit or deny recipients or roles to
    perform actions for specific purposes and periods of time.
    A record of a healthcare consumer’s  choices, which permits or denies
    identified recipient(s) or recipient role(s) to perform one or more actions
    within a given policy context, for specific purposes and periods of time.
    """

    resource_type = Field("Consent", const=True)

    category: ListType[fhirtypes.CodeableConceptType] = Field(
        ...,
        alias="category",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Classification of the consent statement - for indexing/retrieval",
    )

    dateTime: fhirtypes.DateTime = Field(
        None,
        alias="dateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When this Consent was created or indexed",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Identifier for this record (external references)",
    )

    organization: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="organization",
        title=(
            "List of `Reference` items referencing `Organization` (represented as "
            "`dict` in JSON)"
        ),
        description="Custodian of the consent",
    )

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="Who the consent applies to",
    )

    performer: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="performer",
        title=(
            "List of `Reference` items referencing `Organization, Patient, "
            "Practitioner, RelatedPerson, PractitionerRole` (represented as `dict` "
            "in JSON)"
        ),
        description="Who is agreeing to the policy and rules",
    )

    policy: ListType[fhirtypes.ConsentPolicyType] = Field(
        None,
        alias="policy",
        title="List of `ConsentPolicy` items (represented as `dict` in JSON)",
        description="Policies covered by this consent",
    )

    policyRule: fhirtypes.CodeableConceptType = Field(
        None,
        alias="policyRule",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Regulation that this consents to",
    )

    provision: fhirtypes.ConsentProvisionType = Field(
        None,
        alias="provision",
        title="Type `ConsentProvision` (represented as `dict` in JSON)",
        description="Constraints to the base Consent.policyRule",
    )

    scope: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="scope",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Which of the four areas this resource covers (extensible)",
    )

    sourceAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="sourceAttachment",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="Source from which this consent is taken",
        one_of_many="source",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    sourceReference: fhirtypes.ReferenceType = Field(
        None,
        alias="sourceReference",
        title=(
            "Type `Reference` referencing `Consent, DocumentReference, Contract, "
            "QuestionnaireResponse` (represented as `dict` in JSON)"
        ),
        description="Source from which this consent is taken",
        one_of_many="source",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="draft | proposed | active | rejected | inactive | entered-in-error",
    )

    verification: ListType[fhirtypes.ConsentVerificationType] = Field(
        None,
        alias="verification",
        title="List of `ConsentVerification` items (represented as `dict` in JSON)",
        description="Consent Verified by patient or family",
    )

    @root_validator(pre=True)
    def validate_one_of_many(cls, values: Dict[str, Any]) -> Dict[str, Any]:
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
        one_of_many_fields = {"source": ["sourceAttachment", "sourceReference"]}
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


class ConsentPolicy(backboneelement.BackboneElement):
    """ Policies covered by this consent.
    The references to the policies that are included in this consent scope.
    Policies may be organizational, but are often defined jurisdictionally, or
    in law.
    """

    resource_type = Field("ConsentPolicy", const=True)

    authority: fhirtypes.Uri = Field(
        None,
        alias="authority",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Enforcement source for policy",
    )

    uri: fhirtypes.Uri = Field(
        None,
        alias="uri",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Specific policy covered by this consent",
    )


class ConsentProvision(backboneelement.BackboneElement):
    """ Constraints to the base Consent.policyRule.
    An exception to the base policy of this consent. An exception can be an
    addition or removal of access permissions.
    """

    resource_type = Field("ConsentProvision", const=True)

    action: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="action",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Actions controlled by this rule",
    )

    actor: ListType[fhirtypes.ConsentProvisionActorType] = Field(
        None,
        alias="actor",
        title="List of `ConsentProvisionActor` items (represented as `dict` in JSON)",
        description="Who|what controlled by this rule (or group, by role)",
    )

    class_fhir: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="class",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="e.g. Resource Type, Profile, CDA, etc.",
    )

    code: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="code",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="e.g. LOINC or SNOMED CT code, etc. in the content",
    )

    data: ListType[fhirtypes.ConsentProvisionDataType] = Field(
        None,
        alias="data",
        title="List of `ConsentProvisionData` items (represented as `dict` in JSON)",
        description="Data controlled by this rule",
    )

    dataPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="dataPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Timeframe for data controlled by this rule",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Timeframe for this rule",
    )

    provision: ListType[fhirtypes.ConsentProvisionType] = Field(
        None,
        alias="provision",
        title="List of `ConsentProvision` items (represented as `dict` in JSON)",
        description="Nested Exception Rules",
    )

    purpose: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="purpose",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="Context of activities covered by this rule",
    )

    securityLabel: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="securityLabel",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="Security Labels that define affected resources",
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="deny | permit",
    )


class ConsentProvisionActor(backboneelement.BackboneElement):
    """ Who|what controlled by this rule (or group, by role).
    Who or what is controlled by this rule. Use group to identify a set of
    actors by some property they share (e.g. 'admitting officers').
    """

    resource_type = Field("ConsentProvisionActor", const=True)

    reference: fhirtypes.ReferenceType = Field(
        ...,
        alias="reference",
        title=(
            "Type `Reference` referencing `Device, Group, CareTeam, Organization, "
            "Patient, Practitioner, RelatedPerson, PractitionerRole` (represented "
            "as `dict` in JSON)"
        ),
        description="Resource for the actor (or group, by role)",
    )

    role: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="role",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="How the actor is involved",
    )


class ConsentProvisionData(backboneelement.BackboneElement):
    """ Data controlled by this rule.
    The resources controlled by this rule if specific resources are referenced.
    """

    resource_type = Field("ConsentProvisionData", const=True)

    meaning: fhirtypes.Code = Field(
        ...,
        alias="meaning",
        title="Type `Code` (represented as `dict` in JSON)",
        description="instance | related | dependents | authoredby",
    )

    reference: fhirtypes.ReferenceType = Field(
        ...,
        alias="reference",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="The actual data reference",
    )


class ConsentVerification(backboneelement.BackboneElement):
    """ Consent Verified by patient or family.
    Whether a treatment instruction (e.g. artificial respiration yes or no) was
    verified with the patient, his/her family or another authorized person.
    """

    resource_type = Field("ConsentVerification", const=True)

    verificationDate: fhirtypes.DateTime = Field(
        None,
        alias="verificationDate",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When consent verified",
    )

    verified: bool = Field(
        ..., alias="verified", title="Type `bool`", description="Has been verified"
    )

    verifiedWith: fhirtypes.ReferenceType = Field(
        None,
        alias="verifiedWith",
        title=(
            "Type `Reference` referencing `Patient, RelatedPerson` (represented as "
            "`dict` in JSON)"
        ),
        description="Person who verified",
    )
