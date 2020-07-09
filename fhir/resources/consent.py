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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A healthcare consumer's  choices to permit or deny recipients or roles to
    perform actions for specific purposes and periods of time.
    A record of a healthcare consumer’s  choices, which permits or denies
    identified recipient(s) or recipient role(s) to perform one or more actions
    within a given policy context, for specific purposes and periods of time.
    """

    resource_type = Field("Consent", const=True)

    category: ListType[fhirtypes.CodeableConceptType] = Field(
        ...,
        alias="category",
        title="Classification of the consent statement - for indexing/retrieval",
        description=(
            "A classification of the type of consents found in the statement. This "
            "element supports indexing and retrieval of consent statements."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    dateTime: fhirtypes.DateTime = Field(
        None,
        alias="dateTime",
        title="When this Consent was created or indexed",
        description="When this  Consent was issued / created / indexed.",
        # if property is element of this resource.
        element_property=True,
    )
    dateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_dateTime", title="Extension field for ``dateTime``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Identifier for this record (external references)",
        description="Unique identifier for this copy of the Consent Statement.",
        # if property is element of this resource.
        element_property=True,
    )

    organization: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="organization",
        title="Custodian of the consent",
        description=(
            "The organization that manages the consent, and the framework within "
            "which it is executed."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="Who the consent applies to",
        description="The patient/healthcare consumer to whom this consent applies.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    performer: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="performer",
        title="Who is agreeing to the policy and rules",
        description=(
            "Either the Grantor, which is the entity responsible for granting the "
            "rights listed in a Consent Directive or the Grantee, which is the "
            "entity responsible for complying with the Consent Directive, including"
            " any obligations or limitations on authorizations and enforcement of "
            "prohibitions."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Organization",
            "Patient",
            "Practitioner",
            "RelatedPerson",
            "PractitionerRole",
        ],
    )

    policy: ListType[fhirtypes.ConsentPolicyType] = Field(
        None,
        alias="policy",
        title="Policies covered by this consent",
        description=(
            "The references to the policies that are included in this consent "
            "scope. Policies may be organizational, but are often defined "
            "jurisdictionally, or in law."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    policyRule: fhirtypes.CodeableConceptType = Field(
        None,
        alias="policyRule",
        title="Regulation that this consents to",
        description="A reference to the specific base computable regulation or policy.",
        # if property is element of this resource.
        element_property=True,
    )

    provision: fhirtypes.ConsentProvisionType = Field(
        None,
        alias="provision",
        title="Constraints to the base Consent.policyRule",
        description=(
            "An exception to the base policy of this consent. An exception can be "
            "an addition or removal of access permissions."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    scope: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="scope",
        title="Which of the four areas this resource covers (extensible)",
        description=(
            "A selector of the type of consent being presented: ADR, Privacy, "
            "Treatment, Research.  This list is now extensible."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    sourceAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="sourceAttachment",
        title="Source from which this consent is taken",
        description=(
            "The source on which this consent statement is based. The source might "
            "be a scanned original paper form, or a reference to a consent that "
            "links back to such a source, a reference to a document repository "
            "(e.g. XDS) that stores the original consent document."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e source[x]
        one_of_many="source",
        one_of_many_required=False,
    )

    sourceReference: fhirtypes.ReferenceType = Field(
        None,
        alias="sourceReference",
        title="Source from which this consent is taken",
        description=(
            "The source on which this consent statement is based. The source might "
            "be a scanned original paper form, or a reference to a consent that "
            "links back to such a source, a reference to a document repository "
            "(e.g. XDS) that stores the original consent document."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e source[x]
        one_of_many="source",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Consent",
            "DocumentReference",
            "Contract",
            "QuestionnaireResponse",
        ],
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="draft | proposed | active | rejected | inactive | entered-in-error",
        description="Indicates the current state of this consent.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "draft",
            "proposed",
            "active",
            "rejected",
            "inactive",
            "entered-in-error",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    verification: ListType[fhirtypes.ConsentVerificationType] = Field(
        None,
        alias="verification",
        title="Consent Verified by patient or family",
        description=(
            "Whether a treatment instruction (e.g. artificial respiration yes or "
            "no) was verified with the patient, his/her family or another "
            "authorized person."
        ),
        # if property is element of this resource.
        element_property=True,
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Policies covered by this consent.
    The references to the policies that are included in this consent scope.
    Policies may be organizational, but are often defined jurisdictionally, or
    in law.
    """

    resource_type = Field("ConsentPolicy", const=True)

    authority: fhirtypes.Uri = Field(
        None,
        alias="authority",
        title="Enforcement source for policy",
        description=(
            "Entity or Organization having regulatory jurisdiction or "
            "accountability for  enforcing policies pertaining to Consent "
            "Directives."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    authority__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_authority", title="Extension field for ``authority``."
    )

    uri: fhirtypes.Uri = Field(
        None,
        alias="uri",
        title="Specific policy covered by this consent",
        description=(
            "The references to the policies that are included in this consent "
            "scope. Policies may be organizational, but are often defined "
            "jurisdictionally, or in law."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_uri", title="Extension field for ``uri``."
    )


class ConsentProvision(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Constraints to the base Consent.policyRule.
    An exception to the base policy of this consent. An exception can be an
    addition or removal of access permissions.
    """

    resource_type = Field("ConsentProvision", const=True)

    action: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="action",
        title="Actions controlled by this rule",
        description="Actions controlled by this Rule.",
        # if property is element of this resource.
        element_property=True,
    )

    actor: ListType[fhirtypes.ConsentProvisionActorType] = Field(
        None,
        alias="actor",
        title="Who|what controlled by this rule (or group, by role)",
        description=(
            "Who or what is controlled by this rule. Use group to identify a set of"
            " actors by some property they share (e.g. 'admitting officers')."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    class_fhir: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="class",
        title="e.g. Resource Type, Profile, CDA, etc.",
        description=(
            "The class of information covered by this rule. The type can be a FHIR "
            "resource type, a profile on a type, or a CDA document, or some other "
            "type that indicates what sort of information the consent relates to."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    code: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="code",
        title="e.g. LOINC or SNOMED CT code, etc. in the content",
        description="If this code is found in an instance, then the rule applies.",
        # if property is element of this resource.
        element_property=True,
    )

    data: ListType[fhirtypes.ConsentProvisionDataType] = Field(
        None,
        alias="data",
        title="Data controlled by this rule",
        description=(
            "The resources controlled by this rule if specific resources are "
            "referenced."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    dataPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="dataPeriod",
        title="Timeframe for data controlled by this rule",
        description=(
            "Clinical or Operational Relevant period of time that bounds the data "
            "controlled by this rule."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Timeframe for this rule",
        description="The timeframe in this rule is valid.",
        # if property is element of this resource.
        element_property=True,
    )

    provision: ListType[fhirtypes.ConsentProvisionType] = Field(
        None,
        alias="provision",
        title="Nested Exception Rules",
        description="Rules which provide exceptions to the base rule or subrules.",
        # if property is element of this resource.
        element_property=True,
    )

    purpose: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="purpose",
        title="Context of activities covered by this rule",
        description=(
            "The context of the activities a user is taking - why the user is "
            "accessing the data - that are controlled by this rule."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    securityLabel: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="securityLabel",
        title="Security Labels that define affected resources",
        description=(
            "A security label, comprised of 0..* security label fields (Privacy "
            "tags), which define which resources are controlled by this exception."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="deny | permit",
        description=(
            "Action  to take - permit or deny - when the rule conditions are met.  "
            "Not permitted in root rule, required in all nested rules."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["deny", "permit"],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )


class ConsentProvisionActor(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who|what controlled by this rule (or group, by role).
    Who or what is controlled by this rule. Use group to identify a set of
    actors by some property they share (e.g. 'admitting officers').
    """

    resource_type = Field("ConsentProvisionActor", const=True)

    reference: fhirtypes.ReferenceType = Field(
        ...,
        alias="reference",
        title="Resource for the actor (or group, by role)",
        description=(
            "The resource that identifies the actor. To identify actors by type, "
            "use group to identify a set of actors by some property they share "
            "(e.g. 'admitting officers')."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Device",
            "Group",
            "CareTeam",
            "Organization",
            "Patient",
            "Practitioner",
            "RelatedPerson",
            "PractitionerRole",
        ],
    )

    role: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="role",
        title="How the actor is involved",
        description=(
            "How the individual is involved in the resources content that is "
            "described in the exception."
        ),
        # if property is element of this resource.
        element_property=True,
    )


class ConsentProvisionData(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Data controlled by this rule.
    The resources controlled by this rule if specific resources are referenced.
    """

    resource_type = Field("ConsentProvisionData", const=True)

    meaning: fhirtypes.Code = Field(
        ...,
        alias="meaning",
        title="instance | related | dependents | authoredby",
        description=(
            "How the resource reference is interpreted when testing consent "
            "restrictions."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["instance", "related", "dependents", "authoredby"],
    )
    meaning__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_meaning", title="Extension field for ``meaning``."
    )

    reference: fhirtypes.ReferenceType = Field(
        ...,
        alias="reference",
        title="The actual data reference",
        description=(
            "A reference to a specific resource that defines which resources are "
            "covered by this consent."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )


class ConsentVerification(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Consent Verified by patient or family.
    Whether a treatment instruction (e.g. artificial respiration yes or no) was
    verified with the patient, his/her family or another authorized person.
    """

    resource_type = Field("ConsentVerification", const=True)

    verificationDate: fhirtypes.DateTime = Field(
        None,
        alias="verificationDate",
        title="When consent verified",
        description="Date verification was collected.",
        # if property is element of this resource.
        element_property=True,
    )
    verificationDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_verificationDate",
        title="Extension field for ``verificationDate``.",
    )

    verified: bool = Field(
        ...,
        alias="verified",
        title="Has been verified",
        description="Has the instruction been verified.",
        # if property is element of this resource.
        element_property=True,
    )
    verified__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_verified", title="Extension field for ``verified``."
    )

    verifiedWith: fhirtypes.ReferenceType = Field(
        None,
        alias="verifiedWith",
        title="Person who verified",
        description=(
            "Who verified the instruction (Patient, Relative or other Authorized "
            "Person)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "RelatedPerson"],
    )
