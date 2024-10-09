from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Contract
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Contract(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Legal Agreement.
    A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.
    """

    __resource_type__ = "Contract"

    action: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="action",
        title="Action stipulated by this Contract",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    actionReason: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="actionReason",
        title="Rationale for the stiplulated action",
        description="Reason for action stipulated by this Contract.",
        json_schema_extra={
            "element_property": True,
        },
    )

    agent: typing.List[fhirtypes.ContractAgentType] | None = Field(  # type: ignore
        None,
        alias="agent",
        title="Entity being ascribed responsibility",
        description=(
            "An actor taking a role in an activity for which it can be assigned "
            "some degree of responsibility for the activity taking place."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    applies: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="applies",
        title="Effective time",
        description="Relevant time or time-period when this Contract is applicable.",
        json_schema_extra={
            "element_property": True,
        },
    )

    authority: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="authority",
        title="Authority under which this Contract has standing",
        description=(
            "A formally or informally recognized grouping of people, principals, "
            "organizations, or jurisdictions formed for the purpose of achieving "
            "some form of collective action such as the promulgation, "
            "administration and enforcement of contracts and policies."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    bindingAttachment: fhirtypes.AttachmentType | None = Field(  # type: ignore
        None,
        alias="bindingAttachment",
        title="Binding Contract",
        description=(
            "Legally binding Contract: This is the signed and legally recognized "
            'representation of the Contract, which is considered the "source of '
            'truth" and which would be the basis for legal action related to '
            "enforcement of this Contract."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e binding[x]
            "one_of_many": "binding",
            "one_of_many_required": False,
        },
    )

    bindingReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="bindingReference",
        title="Binding Contract",
        description=(
            "Legally binding Contract: This is the signed and legally recognized "
            'representation of the Contract, which is considered the "source of '
            'truth" and which would be the basis for legal action related to '
            "enforcement of this Contract."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e binding[x]
            "one_of_many": "binding",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Composition",
                "DocumentReference",
                "QuestionnaireResponse",
            ],
        },
    )

    contentDerivative: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="contentDerivative",
        title="Content derived from the basal information",
        description=(
            "The minimal content derived from the basal information source at a "
            "specific stage in its lifecycle."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    decisionType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="decisionType",
        title="Decision by Grantor",
        description=(
            "The type of decision made by a grantor with respect to an offer made "
            "by a grantee."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    domain: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="domain",
        title="Domain in which this Contract applies",
        description=(
            "Recognized governance framework or system operating with a "
            "circumscribed scope in accordance with specified principles, policies,"
            " processes or procedures for managing rights, actions, or behaviors of"
            " parties or principals relative to resources."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    friendly: typing.List[fhirtypes.ContractFriendlyType] | None = Field(  # type: ignore
        None,
        alias="friendly",
        title="Contract Friendly Language",
        description=(
            'The "patient friendly language" versionof the Contract in whole or in '
            'parts. "Patient friendly language" means the representation of the '
            "Contract and Contract Provisions in a manner that is readily "
            "accessible and understandable by a layperson in accordance with best "
            "practices for communication styles that ensure that those agreeing to "
            "or signing the Contract understand the roles, actions, obligations, "
            "responsibilities, and implication of the agreement."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Contract number",
        description="Unique identifier for this Contract.",
        json_schema_extra={
            "element_property": True,
        },
    )

    issued: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="issued",
        title="When this Contract was issued",
        description="When this  Contract was issued.",
        json_schema_extra={
            "element_property": True,
        },
    )
    issued__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_issued", title="Extension field for ``issued``."
    )

    legal: typing.List[fhirtypes.ContractLegalType] | None = Field(  # type: ignore
        None,
        alias="legal",
        title="Contract Legal Language",
        description="List of Legal expressions or representations of this Contract.",
        json_schema_extra={
            "element_property": True,
        },
    )

    rule: typing.List[fhirtypes.ContractRuleType] | None = Field(  # type: ignore
        None,
        alias="rule",
        title="Computable Contract Language",
        description=(
            "List of Computable Policy Rule Language Representations of this "
            "Contract."
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
            "A set of security labels that define which resources are controlled by"
            " this consent. If more than one label is specified, all resources must"
            " have all the specified labels."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    signer: typing.List[fhirtypes.ContractSignerType] | None = Field(  # type: ignore
        None,
        alias="signer",
        title="Contract Signatory",
        description=(
            "Parties with legal standing in the Contract, including the principal "
            "parties, the grantor(s) and grantee(s), which are any person or "
            "organization bound by the contract, and any ancillary parties, which "
            "facilitate the execution of the contract such as a notary or witness."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title=(
            "amended | appended | cancelled | disputed | entered-in-error | "
            "executable | executed | negotiable | offered | policy | rejected | "
            "renewed | revoked | resolved | terminated"
        ),
        description="The status of the resource instance.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "amended",
                "appended",
                "cancelled",
                "disputed",
                "entered-in-error",
                "executable",
                "executed",
                "negotiable",
                "offered",
                "policy",
                "rejected",
                "renewed",
                "revoked",
                "resolved",
                "terminated",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    subType: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="subType",
        title="Subtype within the context of type",
        description=(
            "More specific type or specialization of an overarching or more general"
            " contract such as auto insurance, home owner  insurance, prenupial "
            "agreement, Advanced-Directive, or privacy consent."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    subject: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="subject",
        title="Contract Target Entity",
        description=(
            "The target entity impacted by or of interest to parties to the "
            "agreement."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    term: typing.List[fhirtypes.ContractTermType] | None = Field(  # type: ignore
        None,
        alias="term",
        title="Contract Term List",
        description=(
            "One or more Contract Provisions, which may be related and conveyed as "
            "a group, and may contain nested groups."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    topic: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="topic",
        title="Context of the Contract",
        description="The matter of concern in the context of this agreement.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Type or form",
        description=(
            "Type of Contract such as an insurance policy, real estate contract, a "
            "will, power of attorny, Privacy or Security policy , trust framework "
            "agreement, etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    valuedItem: typing.List[fhirtypes.ContractValuedItemType] | None = Field(  # type: ignore
        None,
        alias="valuedItem",
        title="Contract Valued Item List",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Contract`` according specification,
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
            "issued",
            "applies",
            "subject",
            "topic",
            "authority",
            "domain",
            "type",
            "subType",
            "action",
            "actionReason",
            "decisionType",
            "contentDerivative",
            "securityLabel",
            "agent",
            "signer",
            "valuedItem",
            "term",
            "bindingAttachment",
            "bindingReference",
            "bindingReference",
            "bindingReference",
            "friendly",
            "legal",
            "rule",
        ]

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
        one_of_many_fields = {"binding": ["bindingAttachment", "bindingReference"]}
        return one_of_many_fields


class ContractAgent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Entity being ascribed responsibility.
    An actor taking a role in an activity for which it can be assigned some
    degree of responsibility for the activity taking place.
    """

    __resource_type__ = "ContractAgent"

    actor: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="actor",
        title="Contract Agent Type",
        description="Who or what parties are assigned roles in this Contract.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Contract",
                "Device",
                "Group",
                "Location",
                "Organization",
                "Patient",
                "Practitioner",
                "RelatedPerson",
                "Substance",
            ],
        },
    )

    role: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="role",
        title="Role type of the agent",
        description="Role type of agent assigned roles in this Contract.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ContractAgent`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "actor", "role"]


class ContractFriendly(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Contract Friendly Language.
    The "patient friendly language" versionof the Contract in whole or in
    parts. "Patient friendly language" means the representation of the Contract
    and Contract Provisions in a manner that is readily accessible and
    understandable by a layperson in accordance with best practices for
    communication styles that ensure that those agreeing to or signing the
    Contract understand the roles, actions, obligations, responsibilities, and
    implication of the agreement.
    """

    __resource_type__ = "ContractFriendly"

    contentAttachment: fhirtypes.AttachmentType | None = Field(  # type: ignore
        None,
        alias="contentAttachment",
        title="Easily comprehended representation of this Contract",
        description=(
            "Human readable rendering of this Contract in a format and "
            "representation intended to enhance comprehension and ensure "
            "understandability."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e content[x]
            "one_of_many": "content",
            "one_of_many_required": True,
        },
    )

    contentReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="contentReference",
        title="Easily comprehended representation of this Contract",
        description=(
            "Human readable rendering of this Contract in a format and "
            "representation intended to enhance comprehension and ensure "
            "understandability."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e content[x]
            "one_of_many": "content",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Composition",
                "DocumentReference",
                "QuestionnaireResponse",
            ],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ContractFriendly`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "contentAttachment",
            "contentReference",
            "contentReference",
            "contentReference",
        ]

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
        one_of_many_fields = {"content": ["contentAttachment", "contentReference"]}
        return one_of_many_fields


class ContractLegal(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Contract Legal Language.
    List of Legal expressions or representations of this Contract.
    """

    __resource_type__ = "ContractLegal"

    contentAttachment: fhirtypes.AttachmentType | None = Field(  # type: ignore
        None,
        alias="contentAttachment",
        title="Contract Legal Text",
        description="Contract legal text in human renderable form.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e content[x]
            "one_of_many": "content",
            "one_of_many_required": True,
        },
    )

    contentReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="contentReference",
        title="Contract Legal Text",
        description="Contract legal text in human renderable form.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e content[x]
            "one_of_many": "content",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Composition",
                "DocumentReference",
                "QuestionnaireResponse",
            ],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ContractLegal`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "contentAttachment",
            "contentReference",
            "contentReference",
            "contentReference",
        ]

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
        one_of_many_fields = {"content": ["contentAttachment", "contentReference"]}
        return one_of_many_fields


class ContractRule(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Computable Contract Language.
    List of Computable Policy Rule Language Representations of this Contract.
    """

    __resource_type__ = "ContractRule"

    contentAttachment: fhirtypes.AttachmentType | None = Field(  # type: ignore
        None,
        alias="contentAttachment",
        title="Computable Contract Rules",
        description=(
            "Computable Contract conveyed using a policy rule language (e.g. XACML,"
            " DKAL, SecPal)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e content[x]
            "one_of_many": "content",
            "one_of_many_required": True,
        },
    )

    contentReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="contentReference",
        title="Computable Contract Rules",
        description=(
            "Computable Contract conveyed using a policy rule language (e.g. XACML,"
            " DKAL, SecPal)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e content[x]
            "one_of_many": "content",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DocumentReference"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ContractRule`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "contentAttachment",
            "contentReference",
        ]

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
        one_of_many_fields = {"content": ["contentAttachment", "contentReference"]}
        return one_of_many_fields


class ContractSigner(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Contract Signatory.
    Parties with legal standing in the Contract, including the principal
    parties, the grantor(s) and grantee(s), which are any person or
    organization bound by the contract, and any ancillary parties, which
    facilitate the execution of the contract such as a notary or witness.
    """

    __resource_type__ = "ContractSigner"

    party: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="party",
        title="Contract Signatory Party",
        description="Party which is a signator to this Contract.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Organization",
                "Patient",
                "Practitioner",
                "RelatedPerson",
            ],
        },
    )

    signature: typing.List[fhirtypes.SignatureType] = Field(  # type: ignore
        ...,
        alias="signature",
        title="Contract Documentation Signature",
        description="Legally binding Contract DSIG signature contents in Base64.",
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodingType = Field(  # type: ignore
        ...,
        alias="type",
        title="Contract Signatory Role",
        description="Role of this Contract signer, e.g. notary, grantee.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ContractSigner`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "party", "signature"]


class ContractTerm(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Contract Term List.
    One or more Contract Provisions, which may be related and conveyed as a
    group, and may contain nested groups.
    """

    __resource_type__ = "ContractTerm"

    action: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="action",
        title="Contract Term Activity",
        description="Action stipulated by this Contract Provision.",
        json_schema_extra={
            "element_property": True,
        },
    )

    actionReason: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="actionReason",
        title="Purpose for the Contract Term Action",
        description=(
            "Reason or purpose for the action stipulated by this Contract " "Provision."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    agent: typing.List[fhirtypes.ContractTermAgentType] | None = Field(  # type: ignore
        None,
        alias="agent",
        title="Contract Term Agent List",
        description=(
            "An actor taking a role in an activity for which it can be assigned "
            "some degree of responsibility for the activity taking place."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    applies: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="applies",
        title="Contract Term Effective Time",
        description=(
            "Relevant time or time-period when this Contract Provision is "
            "applicable."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    group: typing.List[fhirtypes.ContractTermType] | None = Field(  # type: ignore
        None,
        alias="group",
        title="Nested Contract Term Group",
        description="Nested group of Contract Provisions.",
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Contract Term Number",
        description="Unique identifier for this particular Contract Provision.",
        json_schema_extra={
            "element_property": True,
        },
    )

    issued: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="issued",
        title="Contract Term Issue Date Time",
        description="When this Contract Provision was issued.",
        json_schema_extra={
            "element_property": True,
        },
    )
    issued__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_issued", title="Extension field for ``issued``."
    )

    securityLabel: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        None,
        alias="securityLabel",
        title="Security Labels that define affected terms",
        description=(
            "A set of security labels that define which terms are controlled by "
            "this condition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    subType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="subType",
        title="Contract Term Type specific classification",
        description=(
            "Subtype of this Contract Provision, e.g. life time maximum payment for"
            " a contract term for specific valued item, e.g. disability payment."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    text: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="text",
        title="Human readable Contract term text",
        description="Human readable form of this Contract Provision.",
        json_schema_extra={
            "element_property": True,
        },
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_text", title="Extension field for ``text``."
    )

    topic: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="topic",
        title="Context of the Contract term",
        description=(
            "The matter of concern in the context of this provision of the " "agrement."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Contract Term Type or Form",
        description=(
            "Type of Contract Provision such as specific requirements, purposes for"
            " actions, obligations, prohibitions, e.g. life time maximum benefit."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    valuedItem: typing.List[fhirtypes.ContractTermValuedItemType] | None = Field(  # type: ignore
        None,
        alias="valuedItem",
        title="Contract Term Valued Item List",
        description="Contract Provision Valued Item List.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ContractTerm`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "identifier",
            "issued",
            "applies",
            "type",
            "subType",
            "topic",
            "action",
            "actionReason",
            "securityLabel",
            "agent",
            "text",
            "valuedItem",
            "group",
        ]


class ContractTermAgent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Contract Term Agent List.
    An actor taking a role in an activity for which it can be assigned some
    degree of responsibility for the activity taking place.
    """

    __resource_type__ = "ContractTermAgent"

    actor: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="actor",
        title="Contract Term Agent Subject",
        description="The agent assigned a role in this Contract Provision.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Contract",
                "Device",
                "Group",
                "Location",
                "Organization",
                "Patient",
                "Practitioner",
                "RelatedPerson",
                "Substance",
            ],
        },
    )

    role: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="role",
        title="Type of the Contract Term Agent",
        description=(
            "Role played by the agent assigned this role in the execution of this "
            "Contract Provision."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ContractTermAgent`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "actor", "role"]


class ContractTermValuedItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Contract Term Valued Item List.
    Contract Provision Valued Item List.
    """

    __resource_type__ = "ContractTermValuedItem"

    effectiveTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="effectiveTime",
        title="Contract Term Valued Item Effective Tiem",
        description=(
            "Indicates the time during which this Contract Term ValuedItem "
            "information is effective."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    effectiveTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_effectiveTime", title="Extension field for ``effectiveTime``."
    )

    entityCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="entityCodeableConcept",
        title="Contract Term Valued Item Type",
        description="Specific type of Contract Provision Valued Item that may be priced.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e entity[x]
            "one_of_many": "entity",
            "one_of_many_required": False,
        },
    )

    entityReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="entityReference",
        title="Contract Term Valued Item Type",
        description="Specific type of Contract Provision Valued Item that may be priced.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e entity[x]
            "one_of_many": "entity",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    factor: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="factor",
        title="Contract Term Valued Item Price Scaling Factor",
        description=(
            "A real number that represents a multiplier used in determining the "
            "overall value of the Contract Provision Valued Item delivered. The "
            "concept of a Factor allows for a discount or surcharge multiplier to "
            "be applied to a monetary amount."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_factor", title="Extension field for ``factor``."
    )

    identifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Contract Term Valued Item Number",
        description="Identifies a Contract Provision Valued Item instance.",
        json_schema_extra={
            "element_property": True,
        },
    )

    net: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="net",
        title="Total Contract Term Valued Item Value",
        description=(
            "Expresses the product of the Contract Provision Valued Item "
            "unitQuantity and the unitPriceAmt. For example, the formula: unit "
            "Quantity * unit Price (Cost per Point) * factor Number  * points = net"
            " Amount. Quantity, factor and points are assumed to be 1 if not "
            "supplied."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    points: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="points",
        title="Contract Term Valued Item Difficulty Scaling Factor",
        description=(
            "An amount that expresses the weighting (based on difficulty, cost "
            "and/or resource intensiveness) associated with the Contract Provision "
            "Valued Item delivered. The concept of Points allows for assignment of "
            "point values for a Contract ProvisionValued Item, such that a monetary"
            " amount can be assigned to each point."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    points__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_points", title="Extension field for ``points``."
    )

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="Contract Term Valued Item Count",
        description=(
            "Specifies the units by which the Contract Provision Valued Item is "
            "measured or counted, and quantifies the countable or measurable "
            "Contract Term Valued Item instances."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    unitPrice: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="unitPrice",
        title="Contract Term Valued Item fee, charge, or cost",
        description="A Contract Provision Valued Item unit valuation measure.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ContractTermValuedItem`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "entityCodeableConcept",
            "entityReference",
            "identifier",
            "effectiveTime",
            "quantity",
            "unitPrice",
            "factor",
            "points",
            "net",
        ]

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
        one_of_many_fields = {"entity": ["entityCodeableConcept", "entityReference"]}
        return one_of_many_fields


class ContractValuedItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Contract Valued Item List.
    """

    __resource_type__ = "ContractValuedItem"

    effectiveTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="effectiveTime",
        title="Contract Valued Item Effective Tiem",
        description=(
            "Indicates the time during which this Contract ValuedItem information "
            "is effective."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    effectiveTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_effectiveTime", title="Extension field for ``effectiveTime``."
    )

    entityCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="entityCodeableConcept",
        title="Contract Valued Item Type",
        description="Specific type of Contract Valued Item that may be priced.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e entity[x]
            "one_of_many": "entity",
            "one_of_many_required": False,
        },
    )

    entityReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="entityReference",
        title="Contract Valued Item Type",
        description="Specific type of Contract Valued Item that may be priced.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e entity[x]
            "one_of_many": "entity",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    factor: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="factor",
        title="Contract Valued Item Price Scaling Factor",
        description=(
            "A real number that represents a multiplier used in determining the "
            "overall value of the Contract Valued Item delivered. The concept of a "
            "Factor allows for a discount or surcharge multiplier to be applied to "
            "a monetary amount."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_factor", title="Extension field for ``factor``."
    )

    identifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Contract Valued Item Number",
        description="Identifies a Contract Valued Item instance.",
        json_schema_extra={
            "element_property": True,
        },
    )

    net: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="net",
        title="Total Contract Valued Item Value",
        description=(
            "Expresses the product of the Contract Valued Item unitQuantity and the"
            " unitPriceAmt. For example, the formula: unit Quantity * unit Price "
            "(Cost per Point) * factor Number  * points = net Amount. Quantity, "
            "factor and points are assumed to be 1 if not supplied."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    points: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="points",
        title="Contract Valued Item Difficulty Scaling Factor",
        description=(
            "An amount that expresses the weighting (based on difficulty, cost "
            "and/or resource intensiveness) associated with the Contract Valued "
            "Item delivered. The concept of Points allows for assignment of point "
            "values for a Contract Valued Item, such that a monetary amount can be "
            "assigned to each point."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    points__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_points", title="Extension field for ``points``."
    )

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="Count of Contract Valued Items",
        description=(
            "Specifies the units by which the Contract Valued Item is measured or "
            "counted, and quantifies the countable or measurable Contract Valued "
            "Item instances."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    unitPrice: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="unitPrice",
        title="Contract Valued Item fee, charge, or cost",
        description="A Contract Valued Item unit valuation measure.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ContractValuedItem`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "entityCodeableConcept",
            "entityReference",
            "identifier",
            "effectiveTime",
            "quantity",
            "unitPrice",
            "factor",
            "points",
            "net",
        ]

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
        one_of_many_fields = {"entity": ["entityCodeableConcept", "entityReference"]}
        return one_of_many_fields
