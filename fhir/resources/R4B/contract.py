from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Contract
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Contract(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Legal Agreement.
    Legally enforceable, formally recorded unilateral or bilateral directive
    i.e., a policy or agreement.
    """

    __resource_type__ = "Contract"

    alias: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="alias",
        title="Acronym or short name",
        description=(
            "Alternative representation of the title for this Contract definition, "
            "derivative, or instance in any legal state., e.g., a domain specific "
            "contract number related to legislation."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    alias__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_alias", title="Extension field for ``alias``."
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

    author: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="author",
        title="Source of Contract",
        description=(
            "The individual or organization that authored the Contract definition, "
            "derivative, or instance in any legal state."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Patient",
                "Practitioner",
                "PractitionerRole",
                "Organization",
            ],
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

    contentDefinition: fhirtypes.ContractContentDefinitionType | None = Field(  # type: ignore
        None,
        alias="contentDefinition",
        title="Contract precursor content",
        description=(
            "Precusory content developed with a focus and intent of supporting the "
            "formation a Contract instance, which may be associated with and "
            "transformable into a Contract."
        ),
        json_schema_extra={
            "element_property": True,
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

    domain: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="domain",
        title=(
            "A sphere of control governed by an authoritative jurisdiction, "
            "organization, or person"
        ),
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

    expirationType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="expirationType",
        title="Contract cessation cause",
        description=(
            "Event resulting in discontinuation or termination of this Contract "
            "instance by one or more parties to the contract."
        ),
        json_schema_extra={
            "element_property": True,
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

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Contract number",
        description=(
            "Unique identifier for this Contract or a derivative that references a "
            "Source Contract."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    instantiatesCanonical: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="instantiatesCanonical",
        title="Source Contract Definition",
        description=(
            "The URL pointing to a FHIR-defined Contract Definition that is adhered"
            " to in whole or part by this Contract."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Contract"],
        },
    )

    instantiatesUri: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="instantiatesUri",
        title="External Contract Definition",
        description=(
            "The URL pointing to an externally maintained definition that is "
            "adhered to in whole or in part by this Contract."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    instantiatesUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_instantiatesUri", title="Extension field for ``instantiatesUri``."
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

    legalState: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="legalState",
        title="Negotiation status",
        description=(
            "Legal states of the formation of a legal instrument, which is a "
            "formally executed written document that can be formally attributed to "
            "its author, records and formally expresses a legally enforceable act, "
            "process, or contractual duty, obligation, or right, and therefore "
            "evidences that act, process, or agreement."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    legallyBindingAttachment: fhirtypes.AttachmentType | None = Field(  # type: ignore
        None,
        alias="legallyBindingAttachment",
        title="Binding Contract",
        description=(
            "Legally binding Contract: This is the signed and legally recognized "
            'representation of the Contract, which is considered the "source of '
            'truth" and which would be the basis for legal action related to '
            "enforcement of this Contract."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e legallyBinding[x]
            "one_of_many": "legallyBinding",
            "one_of_many_required": False,
        },
    )

    legallyBindingReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="legallyBindingReference",
        title="Binding Contract",
        description=(
            "Legally binding Contract: This is the signed and legally recognized "
            'representation of the Contract, which is considered the "source of '
            'truth" and which would be the basis for legal action related to '
            "enforcement of this Contract."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e legallyBinding[x]
            "one_of_many": "legallyBinding",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Composition",
                "DocumentReference",
                "QuestionnaireResponse",
                "Contract",
            ],
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Computer friendly designation",
        description=(
            "A natural language name identifying this Contract definition, "
            "derivative, or instance in any legal state. Provides additional "
            "information about its content. This name should be usable as an "
            "identifier for the module by machine processing applications such as "
            "code generation."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    relevantHistory: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="relevantHistory",
        title="Key event in Contract History",
        description=(
            "Links to Provenance records for past versions of this Contract "
            "definition, derivative, or instance, which identify key state "
            "transitions or updates that are likely to be relevant to a user "
            "looking at the current version of the Contract.  The Provence.entity "
            "indicates the target that was changed in the update. "
            "http://build.fhir.org/provenance-definitions.html#Provenance.entity."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Provenance"],
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

    scope: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="scope",
        title="Range of Legal Concerns",
        description=(
            "A selector of legal concerns for this Contract definition, derivative,"
            " or instance in any legal state."
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

    site: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="site",
        title="Specific Location",
        description="Sites in which the contract is complied with,  exercised, or in force.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
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
            "Sub-category for the Contract that distinguishes the kinds of systems "
            "that would be interested in the Contract within the context of the "
            "Contract's scope."
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

    subtitle: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="subtitle",
        title="Subordinate Friendly name",
        description=(
            "An explanatory or alternate user-friendly title for this Contract "
            "definition, derivative, or instance in any legal state.t giving "
            "additional information about its content."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    subtitle__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_subtitle", title="Extension field for ``subtitle``."
    )

    supportingInfo: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="supportingInfo",
        title="Extra Information",
        description=(
            "Information that may be needed by/relevant to the performer in their "
            "execution of this term action."
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

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Human Friendly name",
        description=(
            "A short, descriptive, user-friendly title for this Contract "
            "definition, derivative, or instance in any legal state.t giving "
            "additional information about its content."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    topicCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="topicCodeableConcept",
        title="Focus of contract interest",
        description=(
            "Narrows the range of legal concerns to focus on the achievement of "
            "specific contractual objectives."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e topic[x]
            "one_of_many": "topic",
            "one_of_many_required": False,
        },
    )

    topicReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="topicReference",
        title="Focus of contract interest",
        description=(
            "Narrows the range of legal concerns to focus on the achievement of "
            "specific contractual objectives."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e topic[x]
            "one_of_many": "topic",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Legal instrument category",
        description=(
            "A high-level category for the legal instrument, whether constructed as"
            " a Contract definition, derivative, or instance in any legal state.  "
            "Provides additional information about its content within the context "
            "of the Contract's scope to distinguish the kinds of systems that would"
            " be interested in the contract."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    url: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="url",
        title="Basal definition",
        description=(
            "Canonical identifier for this contract, represented as a URI (globally"
            " unique)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_url", title="Extension field for ``url``."
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="Business edition",
        description=(
            "An edition identifier used for business purposes to label business "
            "significant variants."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_version", title="Extension field for ``version``."
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
            "url",
            "version",
            "status",
            "legalState",
            "instantiatesCanonical",
            "instantiatesUri",
            "contentDerivative",
            "issued",
            "applies",
            "expirationType",
            "subject",
            "authority",
            "domain",
            "site",
            "name",
            "title",
            "subtitle",
            "alias",
            "author",
            "scope",
            "topicCodeableConcept",
            "topicReference",
            "type",
            "subType",
            "contentDefinition",
            "term",
            "supportingInfo",
            "relevantHistory",
            "signer",
            "friendly",
            "legal",
            "rule",
            "legallyBindingAttachment",
            "legallyBindingReference",
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
        one_of_many_fields = {
            "legallyBinding": ["legallyBindingAttachment", "legallyBindingReference"],
            "topic": ["topicCodeableConcept", "topicReference"],
        }
        return one_of_many_fields


class ContractContentDefinition(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Contract precursor content.
    Precusory content developed with a focus and intent of supporting the
    formation a Contract instance, which may be associated with and
    transformable into a Contract.
    """

    __resource_type__ = "ContractContentDefinition"

    copyright: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="copyright",
        title="Publication Ownership",
        description=(
            "A copyright statement relating to Contract precursor content. "
            "Copyright statements are generally legal restrictions on the use and "
            "publishing of the Contract precursor content."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    publicationDate: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="publicationDate",
        title="When published",
        description=(
            "The date (and optionally time) when the contract was published. The "
            "date must change when the business version changes and it must change "
            "if the status code changes. In addition, it should change when the "
            "substantive content of the contract changes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    publicationDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_publicationDate", title="Extension field for ``publicationDate``."
    )

    publicationStatus: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="publicationStatus",
        title=(
            "amended | appended | cancelled | disputed | entered-in-error | "
            "executable | executed | negotiable | offered | policy | rejected | "
            "renewed | revoked | resolved | terminated"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
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
    publicationStatus__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_publicationStatus",
        title="Extension field for ``publicationStatus``.",
    )

    publisher: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="publisher",
        title="Publisher Entity",
        description=(
            "The  individual or organization that published the Contract precursor "
            "content."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
            ],
        },
    )

    subType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="subType",
        title="Detailed Content Type Definition",
        description="Detailed Precusory content type.",
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Content structure and use",
        description=(
            "Precusory content structure and use, i.e., a boilerplate, template, "
            "application for a contract such as an insurance policy or benefits "
            "under a program, e.g., workers compensation."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ContractContentDefinition`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "subType",
            "publisher",
            "publicationDate",
            "publicationStatus",
            "copyright",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("publicationStatus", "publicationStatus__ext")]
        return required_fields


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
                "PractitionerRole",
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

    action: typing.List[fhirtypes.ContractTermActionType] | None = Field(  # type: ignore
        None,
        alias="action",
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
        title="Contract Term Effective Time",
        description=(
            "Relevant time or time-period when this Contract Provision is "
            "applicable."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    asset: typing.List[fhirtypes.ContractTermAssetType] | None = Field(  # type: ignore
        None,
        alias="asset",
        title="Contract Term Asset List",
        description=None,
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

    offer: fhirtypes.ContractTermOfferType = Field(  # type: ignore
        ...,
        alias="offer",
        title="Context of the Contract term",
        description=(
            "The matter of concern in the context of this provision of the " "agrement."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    securityLabel: typing.List[fhirtypes.ContractTermSecurityLabelType] | None = Field(  # type: ignore
        None,
        alias="securityLabel",
        title="Protection for the Term",
        description=(
            "Security labels that protect the handling of information about the "
            "term and its elements, which may be specifically identified.."
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
            "A specialized legal clause or condition based on overarching contract "
            "type."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    text: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="text",
        title="Term Statement",
        description="Statement of a provision in a policy or a contract.",
        json_schema_extra={
            "element_property": True,
        },
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_text", title="Extension field for ``text``."
    )

    topicCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="topicCodeableConcept",
        title="Term Concern",
        description="The entity that the term applies to.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e topic[x]
            "one_of_many": "topic",
            "one_of_many_required": False,
        },
    )

    topicReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="topicReference",
        title="Term Concern",
        description="The entity that the term applies to.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e topic[x]
            "one_of_many": "topic",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Contract Term Type or Form",
        description=(
            "A legal clause or condition contained within a contract that requires "
            "one or both parties to perform a particular requirement by some "
            "specified time or prevents one or both parties from performing a "
            "particular requirement by some specified time."
        ),
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
            "topicCodeableConcept",
            "topicReference",
            "type",
            "subType",
            "text",
            "securityLabel",
            "offer",
            "asset",
            "action",
            "group",
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
        one_of_many_fields = {"topic": ["topicCodeableConcept", "topicReference"]}
        return one_of_many_fields


class ContractTermAction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Entity being ascribed responsibility.
    An actor taking a role in an activity for which it can be assigned some
    degree of responsibility for the activity taking place.
    """

    __resource_type__ = "ContractTermAction"

    context: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="context",
        title="Episode associated with action",
        description=(
            "Encounter or Episode with primary association to specified term "
            "activity."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter", "EpisodeOfCare"],
        },
    )

    contextLinkId: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="contextLinkId",
        title="Pointer to specific item",
        description=(
            "Id [identifier??] of the clause or question text related to the "
            "requester of this action in the referenced form or "
            "QuestionnaireResponse."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    contextLinkId__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_contextLinkId", title="Extension field for ``contextLinkId``."
    )

    doNotPerform: bool | None = Field(  # type: ignore
        None,
        alias="doNotPerform",
        title="True if the term prohibits the  action",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    doNotPerform__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_doNotPerform", title="Extension field for ``doNotPerform``."
    )

    intent: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="intent",
        title="Purpose for the Contract Term Action",
        description=(
            "Reason or purpose for the action stipulated by this Contract " "Provision."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    linkId: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="linkId",
        title="Pointer to specific item",
        description=(
            "Id [identifier??] of the clause or question text related to this "
            "action in the referenced form or QuestionnaireResponse."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    linkId__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_linkId", title="Extension field for ``linkId``."
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="note",
        title="Comments about the action",
        description=(
            "Comments made about the term action made by the requester, performer, "
            "subject or other participants."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    occurrenceDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="occurrenceDateTime",
        title="When action happens",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e occurrence[x]
            "one_of_many": "occurrence",
            "one_of_many_required": False,
        },
    )
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_occurrenceDateTime",
        title="Extension field for ``occurrenceDateTime``.",
    )

    occurrencePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="occurrencePeriod",
        title="When action happens",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e occurrence[x]
            "one_of_many": "occurrence",
            "one_of_many_required": False,
        },
    )

    occurrenceTiming: fhirtypes.TimingType | None = Field(  # type: ignore
        None,
        alias="occurrenceTiming",
        title="When action happens",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e occurrence[x]
            "one_of_many": "occurrence",
            "one_of_many_required": False,
        },
    )

    performer: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="performer",
        title="Actor that wil execute (or not) the action",
        description=(
            "Indicates who or what is being asked to perform (or not perform) the "
            "ction."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "RelatedPerson",
                "Patient",
                "Practitioner",
                "PractitionerRole",
                "CareTeam",
                "Device",
                "Substance",
                "Organization",
                "Location",
            ],
        },
    )

    performerLinkId: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="performerLinkId",
        title="Pointer to specific item",
        description=(
            "Id [identifier??] of the clause or question text related to the reason"
            " type or reference of this  action in the referenced form or "
            "QuestionnaireResponse."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    performerLinkId__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_performerLinkId", title="Extension field for ``performerLinkId``."
    )

    performerRole: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="performerRole",
        title="Competency of the performer",
        description=(
            "The type of role or competency of an individual desired or required to"
            " perform or not perform the action."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    performerType: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="performerType",
        title="Kind of service performer",
        description=(
            "The type of individual that is desired or required to perform or not "
            "perform the action."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reason: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="reason",
        title="Why action is to be performed",
        description=(
            "Describes why the action is to be performed or not performed in "
            "textual form."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    reason__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_reason", title="Extension field for ``reason``."
    )

    reasonCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="reasonCode",
        title="Why is action (not) needed?",
        description=(
            "Rationale for the action to be performed or not performed. Describes "
            "why the action is permitted or prohibited."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reasonLinkId: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="reasonLinkId",
        title="Pointer to specific item",
        description=(
            "Id [identifier??] of the clause or question text related to the reason"
            " type or reference of this  action in the referenced form or "
            "QuestionnaireResponse."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    reasonLinkId__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_reasonLinkId", title="Extension field for ``reasonLinkId``."
    )

    reasonReference: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="reasonReference",
        title="Why is action (not) needed?",
        description=(
            "Indicates another resource whose existence justifies permitting or not"
            " permitting this action."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Condition",
                "Observation",
                "DiagnosticReport",
                "DocumentReference",
                "Questionnaire",
                "QuestionnaireResponse",
            ],
        },
    )

    requester: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="requester",
        title="Who asked for action",
        description=(
            "Who or what initiated the action and has responsibility for its "
            "activation."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Patient",
                "RelatedPerson",
                "Practitioner",
                "PractitionerRole",
                "Device",
                "Group",
                "Organization",
            ],
        },
    )

    requesterLinkId: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="requesterLinkId",
        title="Pointer to specific item",
        description=(
            "Id [identifier??] of the clause or question text related to the "
            "requester of this action in the referenced form or "
            "QuestionnaireResponse."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    requesterLinkId__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_requesterLinkId", title="Extension field for ``requesterLinkId``."
    )

    securityLabelNumber: typing.List[fhirtypes.UnsignedIntType | None] | None = Field(  # type: ignore
        None,
        alias="securityLabelNumber",
        title="Action restriction numbers",
        description="Security labels that protects the action.",
        json_schema_extra={
            "element_property": True,
        },
    )
    securityLabelNumber__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_securityLabelNumber",
        title="Extension field for ``securityLabelNumber``.",
    )

    status: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="status",
        title="State of the action",
        description="Current state of the term action.",
        json_schema_extra={
            "element_property": True,
        },
    )

    subject: typing.List[fhirtypes.ContractTermActionSubjectType] | None = Field(  # type: ignore
        None,
        alias="subject",
        title="Entity of the action",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Type or form of the action",
        description=(
            "Activity or service obligation to be done or not done, performed or "
            "not performed, effectuated or not by this Contract term."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ContractTermAction`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "doNotPerform",
            "type",
            "subject",
            "intent",
            "linkId",
            "status",
            "context",
            "contextLinkId",
            "occurrenceDateTime",
            "occurrencePeriod",
            "occurrenceTiming",
            "requester",
            "requesterLinkId",
            "performerType",
            "performerRole",
            "performer",
            "performerLinkId",
            "reasonCode",
            "reasonReference",
            "reason",
            "reasonLinkId",
            "note",
            "securityLabelNumber",
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
        one_of_many_fields = {
            "occurrence": ["occurrenceDateTime", "occurrencePeriod", "occurrenceTiming"]
        }
        return one_of_many_fields


class ContractTermActionSubject(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Entity of the action.
    """

    __resource_type__ = "ContractTermActionSubject"

    reference: typing.List[fhirtypes.ReferenceType] = Field(  # type: ignore
        ...,
        alias="reference",
        title="Entity of the action",
        description="The entity the action is performed or not performed on or for.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Patient",
                "RelatedPerson",
                "Practitioner",
                "PractitionerRole",
                "Device",
                "Group",
                "Organization",
            ],
        },
    )

    role: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
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
        ``ContractTermActionSubject`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "reference", "role"]


class ContractTermAsset(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Contract Term Asset List.
    """

    __resource_type__ = "ContractTermAsset"

    answer: typing.List[fhirtypes.ContractTermOfferAnswerType] | None = Field(  # type: ignore
        None,
        alias="answer",
        title="Response to assets",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    condition: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="condition",
        title="Quality desctiption of asset",
        description=(
            "Description of the quality and completeness of the asset that imay be "
            "a factor in its valuation."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    condition__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_condition", title="Extension field for ``condition``."
    )

    context: typing.List[fhirtypes.ContractTermAssetContextType] | None = Field(  # type: ignore
        None,
        alias="context",
        title="Circumstance of the asset",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    linkId: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="linkId",
        title="Pointer to asset text",
        description=(
            "Id [identifier??] of the clause or question text about the asset in "
            "the referenced form or QuestionnaireResponse."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    linkId__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_linkId", title="Extension field for ``linkId``."
    )

    period: typing.List[fhirtypes.PeriodType] | None = Field(  # type: ignore
        None,
        alias="period",
        title="Time period of the asset",
        description="Asset relevant contractual time period.",
        json_schema_extra={
            "element_property": True,
        },
    )

    periodType: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="periodType",
        title="Asset availability types",
        description="Type of Asset availability for use or ownership.",
        json_schema_extra={
            "element_property": True,
        },
    )

    relationship: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="relationship",
        title="Kinship of the asset",
        description=(
            "Specifies the applicability of the term to an asset resource instance,"
            " and instances it refers to orinstances that refer to it, and/or are "
            "owned by the offeree."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    scope: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="scope",
        title="Range of asset",
        description="Differentiates the kind of the asset .",
        json_schema_extra={
            "element_property": True,
        },
    )

    securityLabelNumber: typing.List[fhirtypes.UnsignedIntType | None] | None = Field(  # type: ignore
        None,
        alias="securityLabelNumber",
        title="Asset restriction numbers",
        description="Security labels that protects the asset.",
        json_schema_extra={
            "element_property": True,
        },
    )
    securityLabelNumber__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_securityLabelNumber",
        title="Extension field for ``securityLabelNumber``.",
    )

    subtype: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="subtype",
        title="Asset sub-category",
        description="May be a subtype or part of an offered asset.",
        json_schema_extra={
            "element_property": True,
        },
    )

    text: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="text",
        title="Asset clause or question text",
        description=(
            "Clause or question text (Prose Object) concerning the asset in a "
            "linked form, such as a QuestionnaireResponse used in the formation of "
            "the contract."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_text", title="Extension field for ``text``."
    )

    type: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="type",
        title="Asset category",
        description="Target entity type about which the term may be concerned.",
        json_schema_extra={
            "element_property": True,
        },
    )

    typeReference: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="typeReference",
        title="Associated entities",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    usePeriod: typing.List[fhirtypes.PeriodType] | None = Field(  # type: ignore
        None,
        alias="usePeriod",
        title="Time period",
        description="Time period of asset use.",
        json_schema_extra={
            "element_property": True,
        },
    )

    valuedItem: typing.List[fhirtypes.ContractTermAssetValuedItemType] | None = Field(  # type: ignore
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
        ``ContractTermAsset`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "scope",
            "type",
            "typeReference",
            "subtype",
            "relationship",
            "context",
            "condition",
            "periodType",
            "period",
            "usePeriod",
            "text",
            "linkId",
            "answer",
            "securityLabelNumber",
            "valuedItem",
        ]


class ContractTermAssetContext(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Circumstance of the asset.
    """

    __resource_type__ = "ContractTermAssetContext"

    code: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="code",
        title="Codeable asset context",
        description=(
            "Coded representation of the context generally or of the Referenced "
            "entity, such as the asset holder type or location."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="reference",
        title="Creator,custodian or owner",
        description=(
            "Asset context reference may include the creator, custodian, or owning "
            "Person or Organization (e.g., bank, repository),  location held, e.g.,"
            " building,  jurisdiction."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    text: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="text",
        title="Context description",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_text", title="Extension field for ``text``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ContractTermAssetContext`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "reference", "code", "text"]


class ContractTermAssetValuedItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Contract Valued Item List.
    """

    __resource_type__ = "ContractTermAssetValuedItem"

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

    linkId: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="linkId",
        title="Pointer to specific item",
        description=(
            "Id  of the clause or question text related to the context of this "
            "valuedItem in the referenced form or QuestionnaireResponse."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    linkId__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_linkId", title="Extension field for ``linkId``."
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

    payment: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="payment",
        title="Terms of valuation",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    payment__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_payment", title="Extension field for ``payment``."
    )

    paymentDate: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="paymentDate",
        title="When payment is due",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    paymentDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_paymentDate", title="Extension field for ``paymentDate``."
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

    recipient: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="recipient",
        title="Who will receive payment",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Organization",
                "Patient",
                "Practitioner",
                "PractitionerRole",
                "RelatedPerson",
            ],
        },
    )

    responsible: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="responsible",
        title="Who will make payment",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Organization",
                "Patient",
                "Practitioner",
                "PractitionerRole",
                "RelatedPerson",
            ],
        },
    )

    securityLabelNumber: typing.List[fhirtypes.UnsignedIntType | None] | None = Field(  # type: ignore
        None,
        alias="securityLabelNumber",
        title="Security Labels that define affected terms",
        description=(
            "A set of security labels that define which terms are controlled by "
            "this condition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    securityLabelNumber__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_securityLabelNumber",
        title="Extension field for ``securityLabelNumber``.",
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
        ``ContractTermAssetValuedItem`` according specification,
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
            "payment",
            "paymentDate",
            "responsible",
            "recipient",
            "linkId",
            "securityLabelNumber",
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


class ContractTermOffer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Context of the Contract term.
    The matter of concern in the context of this provision of the agrement.
    """

    __resource_type__ = "ContractTermOffer"

    answer: typing.List[fhirtypes.ContractTermOfferAnswerType] | None = Field(  # type: ignore
        None,
        alias="answer",
        title="Response to offer text",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    decision: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="decision",
        title="Accepting party choice",
        description=(
            "Type of choice made by accepting party with respect to an offer made "
            "by an offeror/ grantee."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    decisionMode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="decisionMode",
        title="How decision is conveyed",
        description="How the decision about a Contract was conveyed.",
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Offer business ID",
        description="Unique identifier for this particular Contract Provision.",
        json_schema_extra={
            "element_property": True,
        },
    )

    linkId: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="linkId",
        title="Pointer to text",
        description=(
            "The id of the clause or question text of the offer in the referenced "
            "questionnaire/response."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    linkId__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_linkId", title="Extension field for ``linkId``."
    )

    party: typing.List[fhirtypes.ContractTermOfferPartyType] | None = Field(  # type: ignore
        None,
        alias="party",
        title="Offer Recipient",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    securityLabelNumber: typing.List[fhirtypes.UnsignedIntType | None] | None = Field(  # type: ignore
        None,
        alias="securityLabelNumber",
        title="Offer restriction numbers",
        description="Security labels that protects the offer.",
        json_schema_extra={
            "element_property": True,
        },
    )
    securityLabelNumber__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_securityLabelNumber",
        title="Extension field for ``securityLabelNumber``.",
    )

    text: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="text",
        title="Human readable offer text",
        description="Human readable form of this Contract Offer.",
        json_schema_extra={
            "element_property": True,
        },
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_text", title="Extension field for ``text``."
    )

    topic: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="topic",
        title="Negotiable offer asset",
        description=(
            "The owner of an asset has the residual control rights over the asset: "
            "the right to decide all usages of the asset in any way not "
            "inconsistent with a prior contract, custom, or law (Hart, 1995, p. "
            "30)."
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
        title="Contract Offer Type or Form",
        description=(
            "Type of Contract Provision such as specific requirements, purposes for"
            " actions, obligations, prohibitions, e.g. life time maximum benefit."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ContractTermOffer`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "identifier",
            "party",
            "topic",
            "type",
            "decision",
            "decisionMode",
            "answer",
            "text",
            "linkId",
            "securityLabelNumber",
        ]


class ContractTermOfferAnswer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Response to offer text.
    """

    __resource_type__ = "ContractTermOfferAnswer"

    valueAttachment: fhirtypes.AttachmentType | None = Field(  # type: ignore
        None,
        alias="valueAttachment",
        title="The actual answer response",
        description=(
            "Response to an offer clause or question text,  which enables selection"
            " of values to be agreed to, e.g., the period of participation, the "
            "date of occupancy of a rental, warrently duration, or whether "
            "biospecimen may be used for further research."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueBoolean: bool | None = Field(  # type: ignore
        None,
        alias="valueBoolean",
        title="The actual answer response",
        description=(
            "Response to an offer clause or question text,  which enables selection"
            " of values to be agreed to, e.g., the period of participation, the "
            "date of occupancy of a rental, warrently duration, or whether "
            "biospecimen may be used for further research."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCoding: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="valueCoding",
        title="The actual answer response",
        description=(
            "Response to an offer clause or question text,  which enables selection"
            " of values to be agreed to, e.g., the period of participation, the "
            "date of occupancy of a rental, warrently duration, or whether "
            "biospecimen may be used for further research."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="valueDate",
        title="The actual answer response",
        description=(
            "Response to an offer clause or question text,  which enables selection"
            " of values to be agreed to, e.g., the period of participation, the "
            "date of occupancy of a rental, warrently duration, or whether "
            "biospecimen may be used for further research."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueDate", title="Extension field for ``valueDate``."
    )

    valueDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="valueDateTime",
        title="The actual answer response",
        description=(
            "Response to an offer clause or question text,  which enables selection"
            " of values to be agreed to, e.g., the period of participation, the "
            "date of occupancy of a rental, warrently duration, or whether "
            "biospecimen may be used for further research."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueDateTime", title="Extension field for ``valueDateTime``."
    )

    valueDecimal: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="valueDecimal",
        title="The actual answer response",
        description=(
            "Response to an offer clause or question text,  which enables selection"
            " of values to be agreed to, e.g., the period of participation, the "
            "date of occupancy of a rental, warrently duration, or whether "
            "biospecimen may be used for further research."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueDecimal", title="Extension field for ``valueDecimal``."
    )

    valueInteger: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="valueInteger",
        title="The actual answer response",
        description=(
            "Response to an offer clause or question text,  which enables selection"
            " of values to be agreed to, e.g., the period of participation, the "
            "date of occupancy of a rental, warrently duration, or whether "
            "biospecimen may be used for further research."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueInteger", title="Extension field for ``valueInteger``."
    )

    valueQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="valueQuantity",
        title="The actual answer response",
        description=(
            "Response to an offer clause or question text,  which enables selection"
            " of values to be agreed to, e.g., the period of participation, the "
            "date of occupancy of a rental, warrently duration, or whether "
            "biospecimen may be used for further research."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="valueReference",
        title="The actual answer response",
        description=(
            "Response to an offer clause or question text,  which enables selection"
            " of values to be agreed to, e.g., the period of participation, the "
            "date of occupancy of a rental, warrently duration, or whether "
            "biospecimen may be used for further research."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    valueString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="valueString",
        title="The actual answer response",
        description=(
            "Response to an offer clause or question text,  which enables selection"
            " of values to be agreed to, e.g., the period of participation, the "
            "date of occupancy of a rental, warrently duration, or whether "
            "biospecimen may be used for further research."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    valueTime: fhirtypes.TimeType | None = Field(  # type: ignore
        None,
        alias="valueTime",
        title="The actual answer response",
        description=(
            "Response to an offer clause or question text,  which enables selection"
            " of values to be agreed to, e.g., the period of participation, the "
            "date of occupancy of a rental, warrently duration, or whether "
            "biospecimen may be used for further research."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueTime", title="Extension field for ``valueTime``."
    )

    valueUri: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="valueUri",
        title="The actual answer response",
        description=(
            "Response to an offer clause or question text,  which enables selection"
            " of values to be agreed to, e.g., the period of participation, the "
            "date of occupancy of a rental, warrently duration, or whether "
            "biospecimen may be used for further research."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueUri", title="Extension field for ``valueUri``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ContractTermOfferAnswer`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "valueBoolean",
            "valueDecimal",
            "valueInteger",
            "valueDate",
            "valueDateTime",
            "valueTime",
            "valueString",
            "valueUri",
            "valueAttachment",
            "valueCoding",
            "valueQuantity",
            "valueReference",
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
        one_of_many_fields = {
            "value": [
                "valueAttachment",
                "valueBoolean",
                "valueCoding",
                "valueDate",
                "valueDateTime",
                "valueDecimal",
                "valueInteger",
                "valueQuantity",
                "valueReference",
                "valueString",
                "valueTime",
                "valueUri",
            ]
        }
        return one_of_many_fields


class ContractTermOfferParty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Offer Recipient.
    """

    __resource_type__ = "ContractTermOfferParty"

    reference: typing.List[fhirtypes.ReferenceType] = Field(  # type: ignore
        ...,
        alias="reference",
        title="Referenced entity",
        description="Participant in the offer.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Patient",
                "RelatedPerson",
                "Practitioner",
                "PractitionerRole",
                "Device",
                "Group",
                "Organization",
            ],
        },
    )

    role: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="role",
        title="Participant engagement type",
        description="How the party participates in the offer.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ContractTermOfferParty`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "reference", "role"]


class ContractTermSecurityLabel(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Protection for the Term.
    Security labels that protect the handling of information about the term and
    its elements, which may be specifically identified..
    """

    __resource_type__ = "ContractTermSecurityLabel"

    category: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        None,
        alias="category",
        title="Applicable Policy",
        description=(
            "Security label privacy tag that species the applicable privacy and "
            "security policies governing this term and/or term elements."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    classification: fhirtypes.CodingType = Field(  # type: ignore
        ...,
        alias="classification",
        title="Confidentiality Protection",
        description=(
            "Security label privacy tag that species the level of confidentiality "
            "protection required for this term and/or term elements."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    control: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        None,
        alias="control",
        title="Handling Instructions",
        description=(
            "Security label privacy tag that species the manner in which term "
            "and/or term elements are to be protected."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    number: typing.List[fhirtypes.UnsignedIntType | None] | None = Field(  # type: ignore
        None,
        alias="number",
        title="Link to Security Labels",
        description=(
            "Number used to link this term or term element to the applicable "
            "Security Label."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    number__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_number", title="Extension field for ``number``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ContractTermSecurityLabel`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "number",
            "classification",
            "category",
            "control",
        ]
