from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Consent
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Consent(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A healthcare consumer's  or third party's choices to permit or deny
    recipients or roles to perform actions for specific purposes and periods of
    time.
    A record of a healthcare consumer’s  choices  or choices made on their
    behalf by a third party, which permits or denies identified recipient(s) or
    recipient role(s) to perform one or more actions within a given policy
    context, for specific purposes and periods of time.
    """

    __resource_type__ = "Consent"

    category: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="category",
        title="Classification of the consent statement - for indexing/retrieval",
        description=(
            "A classification of the type of consents found in the statement. This "
            "element supports indexing and retrieval of consent statements."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    controller: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="controller",
        title="Consent Enforcer",
        description="The actor that controls/enforces the access according to the consent.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "HealthcareService",
                "Organization",
                "Patient",
                "Practitioner",
            ],
        },
    )

    date: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="date",
        title="Fully executed date of the consent",
        description="Date the consent instance was agreed to.",
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    decision: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="decision",
        title="deny | permit",
        description="Action to take - permit or deny - as default.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["deny", "permit"],
        },
    )
    decision__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_decision", title="Extension field for ``decision``."
    )

    grantee: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="grantee",
        title="Who is agreeing to the policy and rules",
        description=(
            "The entity responsible for complying with the Consent Directive, "
            "including any obligations or limitations on authorizations and "
            "enforcement of prohibitions."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "CareTeam",
                "HealthcareService",
                "Organization",
                "Patient",
                "Practitioner",
                "RelatedPerson",
                "PractitionerRole",
            ],
        },
    )

    grantor: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="grantor",
        title="Who is granting rights according to the policy and rules",
        description=(
            "The entity responsible for granting the rights listed in a Consent "
            "Directive."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "CareTeam",
                "HealthcareService",
                "Organization",
                "Patient",
                "Practitioner",
                "RelatedPerson",
                "PractitionerRole",
            ],
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Identifier for this record (external references)",
        description="Unique identifier for this copy of the Consent Statement.",
        json_schema_extra={
            "element_property": True,
        },
    )

    manager: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="manager",
        title="Consent workflow management",
        description="The actor that manages the consent through its lifecycle.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "HealthcareService",
                "Organization",
                "Patient",
                "Practitioner",
            ],
        },
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="period",
        title="Effective period for this Consent",
        description=(
            "Effective period for this Consent Resource and all provisions unless "
            "specified in that provision."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    policyBasis: fhirtypes.ConsentPolicyBasisType | None = Field(  # type: ignore
        None,
        alias="policyBasis",
        title="Computable version of the backing policy",
        description=(
            "A Reference or URL used to uniquely identify the policy the "
            "organization will enforce for this Consent. This Reference or URL "
            "should be specific to the version of the policy and should be "
            "dereferencable to a computable policy of some form."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    policyText: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="policyText",
        title="Human Readable Policy",
        description=(
            "A Reference to the human readable policy explaining the basis for the "
            "Consent."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DocumentReference"],
        },
    )

    provision: typing.List[fhirtypes.ConsentProvisionType] | None = Field(  # type: ignore
        None,
        alias="provision",
        title="Constraints to the base Consent.policyRule/Consent.policy",
        description=(
            "An exception to the base policy of this consent. An exception can be "
            "an addition or removal of access permissions."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    regulatoryBasis: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="regulatoryBasis",
        title="Regulations establishing base Consent",
        description=(
            "A set of codes that indicate the regulatory basis (if any) that this "
            "consent supports."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    sourceAttachment: typing.List[fhirtypes.AttachmentType] | None = Field(  # type: ignore
        None,
        alias="sourceAttachment",
        title="Source from which this consent is taken",
        description=(
            "The source on which this consent statement is based. The source might "
            "be a scanned original paper form."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    sourceReference: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="sourceReference",
        title="Source from which this consent is taken",
        description=(
            "A reference to a consent that links back to such a source, a reference"
            " to a document repository (e.g. XDS) that stores the original consent "
            "document."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Consent",
                "DocumentReference",
                "Contract",
                "QuestionnaireResponse",
            ],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="draft | active | inactive | not-done | entered-in-error | unknown",
        description="Indicates the current state of this Consent resource.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "draft",
                "active",
                "inactive",
                "not-done",
                "entered-in-error",
                "unknown",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="subject",
        title="Who the consent applies to",
        description=(
            "The patient/healthcare practitioner or group of persons to whom this "
            "consent applies."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "Practitioner", "Group"],
        },
    )

    verification: typing.List[fhirtypes.ConsentVerificationType] | None = Field(  # type: ignore
        None,
        alias="verification",
        title="Consent Verified by patient or family",
        description=(
            "Whether a treatment instruction (e.g. artificial respiration: yes or "
            "no) was verified with the patient, his/her family or another "
            "authorized person."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Consent`` according specification,
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
            "category",
            "subject",
            "date",
            "period",
            "grantor",
            "grantee",
            "manager",
            "controller",
            "sourceAttachment",
            "sourceReference",
            "regulatoryBasis",
            "policyBasis",
            "policyText",
            "verification",
            "decision",
            "provision",
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


class ConsentPolicyBasis(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Computable version of the backing policy.
    A Reference or URL used to uniquely identify the policy the organization
    will enforce for this Consent. This Reference or URL should be specific to
    the version of the policy and should be dereferencable to a computable
    policy of some form.
    """

    __resource_type__ = "ConsentPolicyBasis"

    reference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="reference",
        title="Reference backing policy resource",
        description=(
            "A Reference that identifies the policy the organization will enforce "
            "for this Consent."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    url: fhirtypes.UrlType | None = Field(  # type: ignore
        None,
        alias="url",
        title="URL to a computable backing policy",
        description=(
            "A URL that links to a computable version of the policy the "
            "organization will enforce for this Consent."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_url", title="Extension field for ``url``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ConsentPolicyBasis`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "reference", "url"]


class ConsentProvision(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Constraints to the base Consent.policyRule/Consent.policy.
    An exception to the base policy of this consent. An exception can be an
    addition or removal of access permissions.
    """

    __resource_type__ = "ConsentProvision"

    action: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="action",
        title="Actions controlled by this provision",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    actor: typing.List[fhirtypes.ConsentProvisionActorType] | None = Field(  # type: ignore
        None,
        alias="actor",
        title="Who|what controlled by this provision (or group, by role)",
        description=(
            "Who or what is controlled by this provision. Use group to identify a "
            "set of actors by some property they share (e.g. 'admitting officers')."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    code: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="code",
        title="e.g. LOINC or SNOMED CT code, etc. in the content",
        description="If this code is found in an instance, then the provision applies.",
        json_schema_extra={
            "element_property": True,
        },
    )

    data: typing.List[fhirtypes.ConsentProvisionDataType] | None = Field(  # type: ignore
        None,
        alias="data",
        title="Data controlled by this provision",
        description=(
            "The resources controlled by this provision if specific resources are "
            "referenced."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    dataPeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="dataPeriod",
        title="Timeframe for data controlled by this provision",
        description=(
            "Clinical or Operational Relevant period of time that bounds the data "
            "controlled by this provision."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    documentType: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        None,
        alias="documentType",
        title="e.g. Resource Type, Profile, CDA, etc",
        description=(
            "The documentType(s) covered by this provision. The type can be a CDA "
            "document, or some other type that indicates what sort of information "
            "the consent relates to."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    expression: fhirtypes.ExpressionType | None = Field(  # type: ignore
        None,
        alias="expression",
        title="A computable expression of the consent",
        description=(
            "A computable (FHIRPath or other) definition of what is controlled by "
            "this consent."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="period",
        title="Timeframe for this provision",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    provision: typing.List[fhirtypes.ConsentProvisionType] | None = Field(  # type: ignore
        None,
        alias="provision",
        title="Nested Exception Provisions",
        description=(
            "Provisions which provide exceptions to the base provision or "
            "subprovisions."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    purpose: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        None,
        alias="purpose",
        title="Context of activities covered by this provision",
        description=(
            "The context of the activities a user is taking - why the user is "
            "accessing the data - that are controlled by this provision."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    resourceType: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        None,
        alias="resourceType",
        title="e.g. Resource Type, Profile, etc",
        description=(
            "The resourceType(s) covered by this provision. The type can be a FHIR "
            "resource type or a profile on a type that indicates what information "
            "the consent relates to."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    securityLabel: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        None,
        alias="securityLabel",
        title="Security Labels that define affected resources",
        description=(
            "A security label, comprised of 0..* security label fields (Privacy "
            "tags), which define which resources are controlled by this exception."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ConsentProvision`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "period",
            "actor",
            "action",
            "securityLabel",
            "purpose",
            "documentType",
            "resourceType",
            "code",
            "dataPeriod",
            "data",
            "expression",
            "provision",
        ]


class ConsentProvisionActor(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who|what controlled by this provision (or group, by role).
    Who or what is controlled by this provision. Use group to identify a set of
    actors by some property they share (e.g. 'admitting officers').
    """

    __resource_type__ = "ConsentProvisionActor"

    reference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="reference",
        title="Resource for the actor (or group, by role)",
        description=(
            "The resource that identifies the actor. To identify actors by type, "
            "use group to identify a set of actors by some property they share "
            "(e.g. 'admitting officers')."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Device",
                "Group",
                "CareTeam",
                "Organization",
                "Patient",
                "Practitioner",
                "RelatedPerson",
                "PractitionerRole",
            ],
        },
    )

    role: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="role",
        title="How the actor is involved",
        description=(
            "How the individual is involved in the resources content that is "
            "described in the exception."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ConsentProvisionActor`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "role", "reference"]


class ConsentProvisionData(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Data controlled by this provision.
    The resources controlled by this provision if specific resources are
    referenced.
    """

    __resource_type__ = "ConsentProvisionData"

    meaning: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="meaning",
        title="instance | related | dependents | authoredby",
        description=(
            "How the resource reference is interpreted when testing consent "
            "restrictions."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["instance", "related", "dependents", "authoredby"],
        },
    )
    meaning__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_meaning", title="Extension field for ``meaning``."
    )

    reference: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="reference",
        title="The actual data reference",
        description=(
            "A reference to a specific resource that defines which resources are "
            "covered by this consent."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ConsentProvisionData`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "meaning", "reference"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("meaning", "meaning__ext")]
        return required_fields


class ConsentVerification(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Consent Verified by patient or family.
    Whether a treatment instruction (e.g. artificial respiration: yes or no)
    was verified with the patient, his/her family or another authorized person.
    """

    __resource_type__ = "ConsentVerification"

    verificationDate: typing.List[fhirtypes.DateTimeType | None] | None = Field(  # type: ignore
        None,
        alias="verificationDate",
        title="When consent verified",
        description="Date(s) verification was collected.",
        json_schema_extra={
            "element_property": True,
        },
    )
    verificationDate__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_verificationDate",
        title="Extension field for ``verificationDate``.",
    )

    verificationType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="verificationType",
        title="Business case of verification",
        description=(
            "Extensible list of verification type starting with verification and "
            "re-validation."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    verified: bool | None = Field(  # type: ignore
        None,
        alias="verified",
        title="Has been verified",
        description="Has the instruction been verified.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    verified__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_verified", title="Extension field for ``verified``."
    )

    verifiedBy: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="verifiedBy",
        title="Person conducting verification",
        description=(
            "The person who conducted the verification/validation of the Grantor "
            "decision."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Organization",
                "Practitioner",
                "PractitionerRole",
            ],
        },
    )

    verifiedWith: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="verifiedWith",
        title="Person who verified",
        description=(
            "Who verified the instruction (Patient, Relative or other Authorized "
            "Person)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "RelatedPerson"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ConsentVerification`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "verified",
            "verificationType",
            "verifiedBy",
            "verifiedWith",
            "verificationDate",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("verified", "verified__ext")]
        return required_fields
