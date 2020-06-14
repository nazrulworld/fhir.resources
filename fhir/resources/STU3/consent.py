# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Consent
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Consent(domainresource.DomainResource):
    """ A healthcare consumer's policy choices to permits or denies recipients or
    roles to perform actions for specific purposes and periods of time.
    A record of a healthcare consumer’s policy choices, which permits or denies
    identified recipient(s) or recipient role(s) to perform one or more actions
    within a given policy context, for specific purposes and periods of time.
    """

    resource_type = Field("Consent", const=True)

    action: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="action",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Actions controlled by this consent",
    )

    actor: ListType[fhirtypes.ConsentActorType] = Field(
        None,
        alias="actor",
        title="List of `ConsentActor` items (represented as `dict` in JSON)",
        description="Who|what controlled by this consent (or group, by role)",
    )

    category: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Classification of the consent statement - for indexing/retrieval",
    )

    consentingParty: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="consentingParty",
        title="List of `Reference` items referencing `Organization, Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON)",
        description="Who is agreeing to the policy and exceptions",
    )

    data: ListType[fhirtypes.ConsentDataType] = Field(
        None,
        alias="data",
        title="List of `ConsentData` items (represented as `dict` in JSON)",
        description="Data controlled by this consent",
    )

    dataPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="dataPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Timeframe for data controlled by this consent",
    )

    dateTime: fhirtypes.DateTime = Field(
        None,
        alias="dateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When this Consent was created or indexed",
    )

    except_fhir: ListType[fhirtypes.ConsentExceptType] = Field(
        None,
        alias="except",
        title="List of `ConsentExcept` items (represented as `dict` in JSON)",
        description="Additional rule -  addition or removal of permissions",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Identifier for this record (external references)",
    )

    organization: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="organization",
        title="List of `Reference` items referencing `Organization` (represented as `dict` in JSON)",
        description="Custodian of the consent",
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="Who the consent applies to",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Period that this consent applies",
    )

    policy: ListType[fhirtypes.ConsentPolicyType] = Field(
        None,
        alias="policy",
        title="List of `ConsentPolicy` items (represented as `dict` in JSON)",
        description="Policies covered by this consent",
    )

    policyRule: fhirtypes.Uri = Field(
        None,
        alias="policyRule",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Policy that this consents to",
    )

    purpose: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="purpose",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="Context of activities for which the agreement is made",
    )

    securityLabel: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="securityLabel",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="Security Labels that define affected resources",
    )

    sourceAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="sourceAttachment",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="Source from which this consent is taken",
        one_of_many="source",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    sourceIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="sourceIdentifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Source from which this consent is taken",
        one_of_many="source",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    sourceReference: fhirtypes.ReferenceType = Field(
        None,
        alias="sourceReference",
        title="Type `Reference` referencing `Consent, DocumentReference, Contract, QuestionnaireResponse` (represented as `dict` in JSON)",
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
        one_of_many_fields = {
            "source": ["sourceAttachment", "sourceIdentifier", "sourceReference",],
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


class ConsentActor(backboneelement.BackboneElement):
    """ Who|what controlled by this consent (or group, by role).
    Who or what is controlled by this consent. Use group to identify a set of
    actors by some property they share (e.g. 'admitting officers').
    """

    resource_type = Field("ConsentActor", const=True)

    reference: fhirtypes.ReferenceType = Field(
        ...,
        alias="reference",
        title="Type `Reference` referencing `Device, Group, CareTeam, Organization, Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON)",
        description="Resource for the actor (or group, by role)",
    )

    role: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="role",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="How the actor is involved",
    )


class ConsentData(backboneelement.BackboneElement):
    """ Data controlled by this consent.
    The resources controlled by this consent, if specific resources are
    referenced.
    """

    resource_type = Field("ConsentData", const=True)

    meaning: fhirtypes.Code = Field(
        ...,
        alias="meaning",
        title="Type `Code` (represented as `dict` in JSON)",
        description="instance | related | dependents | authoredby",
    )

    reference: fhirtypes.ReferenceType = Field(
        ...,
        alias="reference",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="The actual data reference",
    )


class ConsentExcept(backboneelement.BackboneElement):
    """ Additional rule -  addition or removal of permissions.
    An exception to the base policy of this consent. An exception can be an
    addition or removal of access permissions.
    """

    resource_type = Field("ConsentExcept", const=True)

    action: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="action",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Actions controlled by this exception",
    )

    actor: ListType[fhirtypes.ConsentExceptActorType] = Field(
        None,
        alias="actor",
        title="List of `ConsentExceptActor` items (represented as `dict` in JSON)",
        description="Who|what controlled by this exception (or group, by role)",
    )

    class_fhir: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="class",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="e.g. Resource Type, Profile, or CDA etc",
    )

    code: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="code",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="e.g. LOINC or SNOMED CT code, etc in the content",
    )

    data: ListType[fhirtypes.ConsentExceptDataType] = Field(
        None,
        alias="data",
        title="List of `ConsentExceptData` items (represented as `dict` in JSON)",
        description="Data controlled by this exception",
    )

    dataPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="dataPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Timeframe for data controlled by this exception",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Timeframe for this exception",
    )

    purpose: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="purpose",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="Context of activities covered by this exception",
    )

    securityLabel: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="securityLabel",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="Security Labels that define affected resources",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="deny | permit",
    )


class ConsentExceptActor(backboneelement.BackboneElement):
    """ Who|what controlled by this exception (or group, by role).
    Who or what is controlled by this Exception. Use group to identify a set of
    actors by some property they share (e.g. 'admitting officers').
    """

    resource_type = Field("ConsentExceptActor", const=True)

    reference: fhirtypes.ReferenceType = Field(
        ...,
        alias="reference",
        title="Type `Reference` referencing `Device, Group, CareTeam, Organization, Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON)",
        description="Resource for the actor (or group, by role)",
    )

    role: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="role",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="How the actor is involved",
    )


class ConsentExceptData(backboneelement.BackboneElement):
    """ Data controlled by this exception.
    The resources controlled by this exception, if specific resources are
    referenced.
    """

    resource_type = Field("ConsentExceptData", const=True)

    meaning: fhirtypes.Code = Field(
        ...,
        alias="meaning",
        title="Type `Code` (represented as `dict` in JSON)",
        description="instance | related | dependents | authoredby",
    )

    reference: fhirtypes.ReferenceType = Field(
        ...,
        alias="reference",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="The actual data reference",
    )


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
