from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Consent
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Consent(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A healthcare consumer's  choices to permit or deny recipients or roles to
    perform actions for specific purposes and periods of time.
    A record of a healthcare consumer’s  choices, which permits or denies
    identified recipient(s) or recipient role(s) to perform one or more actions
    within a given policy context, for specific purposes and periods of time.
    """

    __resource_type__ = "Consent"

    category: typing.List[fhirtypes.CodeableConceptType] = Field(  # type: ignore
        ...,
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

    dateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="dateTime",
        title="When this Consent was created or indexed",
        description="When this  Consent was issued / created / indexed.",
        json_schema_extra={
            "element_property": True,
        },
    )
    dateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_dateTime", title="Extension field for ``dateTime``."
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

    organization: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="organization",
        title="Custodian of the consent",
        description=(
            "The organization that manages the consent, and the framework within "
            "which it is executed."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    patient: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="patient",
        title="Who the consent applies to",
        description="The patient/healthcare consumer to whom this consent applies.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient"],
        },
    )

    performer: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Organization",
                "Patient",
                "Practitioner",
                "RelatedPerson",
                "PractitionerRole",
            ],
        },
    )

    policy: typing.List[fhirtypes.ConsentPolicyType] | None = Field(  # type: ignore
        None,
        alias="policy",
        title="Policies covered by this consent",
        description=(
            "The references to the policies that are included in this consent "
            "scope. Policies may be organizational, but are often defined "
            "jurisdictionally, or in law."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    policyRule: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="policyRule",
        title="Regulation that this consents to",
        description="A reference to the specific base computable regulation or policy.",
        json_schema_extra={
            "element_property": True,
        },
    )

    provision: fhirtypes.ConsentProvisionType | None = Field(  # type: ignore
        None,
        alias="provision",
        title="Constraints to the base Consent.policyRule",
        description=(
            "An exception to the base policy of this consent. An exception can be "
            "an addition or removal of access permissions."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    scope: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="scope",
        title="Which of the four areas this resource covers (extensible)",
        description=(
            "A selector of the type of consent being presented: ADR, Privacy, "
            "Treatment, Research.  This list is now extensible."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    sourceAttachment: fhirtypes.AttachmentType | None = Field(  # type: ignore
        None,
        alias="sourceAttachment",
        title="Source from which this consent is taken",
        description=(
            "The source on which this consent statement is based. The source might "
            "be a scanned original paper form, or a reference to a consent that "
            "links back to such a source, a reference to a document repository "
            "(e.g. XDS) that stores the original consent document."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e source[x]
            "one_of_many": "source",
            "one_of_many_required": False,
        },
    )

    sourceReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="sourceReference",
        title="Source from which this consent is taken",
        description=(
            "The source on which this consent statement is based. The source might "
            "be a scanned original paper form, or a reference to a consent that "
            "links back to such a source, a reference to a document repository "
            "(e.g. XDS) that stores the original consent document."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e source[x]
            "one_of_many": "source",
            "one_of_many_required": False,
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
        title="draft | proposed | active | rejected | inactive | entered-in-error",
        description="Indicates the current state of this consent.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "draft",
                "proposed",
                "active",
                "rejected",
                "inactive",
                "entered-in-error",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    verification: typing.List[fhirtypes.ConsentVerificationType] | None = Field(  # type: ignore
        None,
        alias="verification",
        title="Consent Verified by patient or family",
        description=(
            "Whether a treatment instruction (e.g. artificial respiration yes or "
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
            "scope",
            "category",
            "patient",
            "dateTime",
            "performer",
            "organization",
            "sourceAttachment",
            "sourceReference",
            "policy",
            "policyRule",
            "verification",
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

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
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
        return one_of_many_fields


class ConsentPolicy(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Policies covered by this consent.
    The references to the policies that are included in this consent scope.
    Policies may be organizational, but are often defined jurisdictionally, or
    in law.
    """

    __resource_type__ = "ConsentPolicy"

    authority: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="authority",
        title="Enforcement source for policy",
        description=(
            "Entity or Organization having regulatory jurisdiction or "
            "accountability for  enforcing policies pertaining to Consent "
            "Directives."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    authority__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_authority", title="Extension field for ``authority``."
    )

    uri: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="uri",
        title="Specific policy covered by this consent",
        description=(
            "The references to the policies that are included in this consent "
            "scope. Policies may be organizational, but are often defined "
            "jurisdictionally, or in law."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_uri", title="Extension field for ``uri``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ConsentPolicy`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "authority", "uri"]


class ConsentProvision(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Constraints to the base Consent.policyRule.
    An exception to the base policy of this consent. An exception can be an
    addition or removal of access permissions.
    """

    __resource_type__ = "ConsentProvision"

    action: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="action",
        title="Actions controlled by this rule",
        description="Actions controlled by this Rule.",
        json_schema_extra={
            "element_property": True,
        },
    )

    actor: typing.List[fhirtypes.ConsentProvisionActorType] | None = Field(  # type: ignore
        None,
        alias="actor",
        title="Who|what controlled by this rule (or group, by role)",
        description=(
            "Who or what is controlled by this rule. Use group to identify a set of"
            " actors by some property they share (e.g. 'admitting officers')."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    class_fhir: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        None,
        alias="class",
        title="e.g. Resource Type, Profile, CDA, etc.",
        description=(
            "The class of information covered by this rule. The type can be a FHIR "
            "resource type, a profile on a type, or a CDA document, or some other "
            "type that indicates what sort of information the consent relates to."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    code: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="code",
        title="e.g. LOINC or SNOMED CT code, etc. in the content",
        description="If this code is found in an instance, then the rule applies.",
        json_schema_extra={
            "element_property": True,
        },
    )

    data: typing.List[fhirtypes.ConsentProvisionDataType] | None = Field(  # type: ignore
        None,
        alias="data",
        title="Data controlled by this rule",
        description=(
            "The resources controlled by this rule if specific resources are "
            "referenced."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    dataPeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="dataPeriod",
        title="Timeframe for data controlled by this rule",
        description=(
            "Clinical or Operational Relevant period of time that bounds the data "
            "controlled by this rule."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="period",
        title="Timeframe for this rule",
        description="The timeframe in this rule is valid.",
        json_schema_extra={
            "element_property": True,
        },
    )

    provision: typing.List[fhirtypes.ConsentProvisionType] | None = Field(  # type: ignore
        None,
        alias="provision",
        title="Nested Exception Rules",
        description="Rules which provide exceptions to the base rule or subrules.",
        json_schema_extra={
            "element_property": True,
        },
    )

    purpose: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        None,
        alias="purpose",
        title="Context of activities covered by this rule",
        description=(
            "The context of the activities a user is taking - why the user is "
            "accessing the data - that are controlled by this rule."
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

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="deny | permit",
        description=(
            "Action  to take - permit or deny - when the rule conditions are met.  "
            "Not permitted in root rule, required in all nested rules."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["deny", "permit"],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
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
            "type",
            "period",
            "actor",
            "action",
            "securityLabel",
            "purpose",
            "class",
            "code",
            "dataPeriod",
            "data",
            "provision",
        ]


class ConsentProvisionActor(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who|what controlled by this rule (or group, by role).
    Who or what is controlled by this rule. Use group to identify a set of
    actors by some property they share (e.g. 'admitting officers').
    """

    __resource_type__ = "ConsentProvisionActor"

    reference: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
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

    role: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
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

    Data controlled by this rule.
    The resources controlled by this rule if specific resources are referenced.
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
    Whether a treatment instruction (e.g. artificial respiration yes or no) was
    verified with the patient, his/her family or another authorized person.
    """

    __resource_type__ = "ConsentVerification"

    verificationDate: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="verificationDate",
        title="When consent verified",
        description="Date verification was collected.",
        json_schema_extra={
            "element_property": True,
        },
    )
    verificationDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_verificationDate",
        title="Extension field for ``verificationDate``.",
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
