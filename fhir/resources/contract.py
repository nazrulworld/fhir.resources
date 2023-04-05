# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Contract
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class Contract(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Legal Agreement.
    Legally enforceable, formally recorded unilateral or bilateral directive
    i.e., a policy or agreement.
    """

    resource_type = Field("Contract", const=True)

    alias: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="alias",
        title="Acronym or short name",
        description=(
            "Alternative representation of the title for this Contract definition, "
            "derivative, or instance in any legal state., e.g., a domain specific "
            "contract number related to legislation."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    alias__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_alias", title="Extension field for ``alias``.")

    applies: fhirtypes.PeriodType = Field(
        None,
        alias="applies",
        title="Effective time",
        description="Relevant time or time-period when this Contract is applicable.",
        # if property is element of this resource.
        element_property=True,
    )

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title="Source of Contract",
        description=(
            "The individual or organization that authored the Contract definition, "
            "derivative, or instance in any legal state."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "Practitioner",
            "PractitionerRole",
            "Organization",
        ],
    )

    authority: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="authority",
        title="Authority under which this Contract has standing",
        description=(
            "A formally or informally recognized grouping of people, principals, "
            "organizations, or jurisdictions formed for the purpose of achieving "
            "some form of collective action such as the promulgation, "
            "administration and enforcement of contracts and policies."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    contentDefinition: fhirtypes.ContractContentDefinitionType = Field(
        None,
        alias="contentDefinition",
        title="Contract precursor content",
        description=(
            "Precusory content developed with a focus and intent of supporting the "
            "formation a Contract instance, which may be associated with and "
            "transformable into a Contract."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    contentDerivative: fhirtypes.CodeableConceptType = Field(
        None,
        alias="contentDerivative",
        title="Content derived from the basal information",
        description=(
            "The minimal content derived from the basal information source at a "
            "specific stage in its lifecycle."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    domain: typing.List[fhirtypes.ReferenceType] = Field(
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
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    expirationType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="expirationType",
        title="Contract cessation cause",
        description=(
            "Event resulting in discontinuation or termination of this Contract "
            "instance by one or more parties to the contract."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    friendly: typing.List[fhirtypes.ContractFriendlyType] = Field(
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
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Contract number",
        description=(
            "Unique identifier for this Contract or a derivative that references a "
            "Source Contract."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    instantiatesCanonical: fhirtypes.ReferenceType = Field(
        None,
        alias="instantiatesCanonical",
        title="Source Contract Definition",
        description=(
            "The URL pointing to a FHIR-defined Contract Definition that is adhered"
            " to in whole or part by this Contract."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Contract"],
    )

    instantiatesUri: fhirtypes.Uri = Field(
        None,
        alias="instantiatesUri",
        title="External Contract Definition",
        description=(
            "The URL pointing to an externally maintained definition that is "
            "adhered to in whole or in part by this Contract."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    instantiatesUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_instantiatesUri", title="Extension field for ``instantiatesUri``."
    )

    issued: fhirtypes.DateTime = Field(
        None,
        alias="issued",
        title="When this Contract was issued",
        description="When this  Contract was issued.",
        # if property is element of this resource.
        element_property=True,
    )
    issued__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_issued", title="Extension field for ``issued``."
    )

    legal: typing.List[fhirtypes.ContractLegalType] = Field(
        None,
        alias="legal",
        title="Contract Legal Language",
        description="List of Legal expressions or representations of this Contract.",
        # if property is element of this resource.
        element_property=True,
    )

    legalState: fhirtypes.CodeableConceptType = Field(
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
        # if property is element of this resource.
        element_property=True,
    )

    legallyBindingAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="legallyBindingAttachment",
        title="Binding Contract",
        description=(
            "Legally binding Contract: This is the signed and legally recognized "
            'representation of the Contract, which is considered the "source of '
            'truth" and which would be the basis for legal action related to '
            "enforcement of this Contract."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e legallyBinding[x]
        one_of_many="legallyBinding",
        one_of_many_required=False,
    )

    legallyBindingReference: fhirtypes.ReferenceType = Field(
        None,
        alias="legallyBindingReference",
        title="Binding Contract",
        description=(
            "Legally binding Contract: This is the signed and legally recognized "
            'representation of the Contract, which is considered the "source of '
            'truth" and which would be the basis for legal action related to '
            "enforcement of this Contract."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e legallyBinding[x]
        one_of_many="legallyBinding",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Composition",
            "DocumentReference",
            "QuestionnaireResponse",
            "Contract",
        ],
    )

    name: fhirtypes.String = Field(
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
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    relevantHistory: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="relevantHistory",
        title="Key event in Contract History",
        description=(
            "Links to Provenance records for past versions of this Contract "
            "definition, derivative, or instance, which identify key state "
            "transitions or updates that are likely to be relevant to a user "
            "looking at the current version of the Contract.  The Provenance.entity"
            " indicates the target that was changed in the update (see "
            "[Provenance.entity](provenance-definitions.html#Provenance.entity))."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Provenance"],
    )

    rule: typing.List[fhirtypes.ContractRuleType] = Field(
        None,
        alias="rule",
        title="Computable Contract Language",
        description=(
            "List of Computable Policy Rule Language Representations of this "
            "Contract."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    scope: fhirtypes.CodeableConceptType = Field(
        None,
        alias="scope",
        title="Range of Legal Concerns",
        description=(
            "A selector of legal concerns for this Contract definition, derivative,"
            " or instance in any legal state."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    signer: typing.List[fhirtypes.ContractSignerType] = Field(
        None,
        alias="signer",
        title="Contract Signatory",
        description=(
            "Parties with legal standing in the Contract, including the principal "
            "parties, the grantor(s) and grantee(s), which are any person or "
            "organization bound by the contract, and any ancillary parties, which "
            "facilitate the execution of the contract such as a notary or witness."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    site: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="site",
        title="Specific Location",
        description="Sites in which the contract is complied with,  exercised, or in force.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title=(
            "amended | appended | cancelled | disputed | entered-in-error | "
            "executable +"
        ),
        description="The status of the resource instance.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "amended",
            "appended",
            "cancelled",
            "disputed",
            "entered-in-error",
            "executable",
            "+",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subType: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="subType",
        title="Subtype within the context of type",
        description=(
            "Sub-category for the Contract that distinguishes the kinds of systems "
            "that would be interested in the Contract within the context of the "
            "Contract's scope."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    subject: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="subject",
        title="Contract Target Entity",
        description=(
            "The target entity impacted by or of interest to parties to the "
            "agreement."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    subtitle: fhirtypes.String = Field(
        None,
        alias="subtitle",
        title="Subordinate Friendly name",
        description=(
            "A more detailed or qualifying explanatory or alternate user-friendly "
            "title for this Contract definition, derivative, or instance in any "
            "legal state."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    subtitle__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_subtitle", title="Extension field for ``subtitle``."
    )

    supportingInfo: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingInfo",
        title="Extra Information",
        description=(
            "Information that may be needed by/relevant to the performer in their "
            "execution of this term action."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    term: typing.List[fhirtypes.ContractTermType] = Field(
        None,
        alias="term",
        title="Contract Term List",
        description=(
            "One or more Contract Provisions, which may be related and conveyed as "
            "a group, and may contain nested groups."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Human Friendly name",
        description=(
            "A short, descriptive, user-friendly title for this Contract "
            "definition, derivative, or instance in any legal state."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    topicCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="topicCodeableConcept",
        title="Focus of contract interest",
        description=(
            "Narrows the range of legal concerns to focus on the achievement of "
            "specific contractual objectives."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e topic[x]
        one_of_many="topic",
        one_of_many_required=False,
    )

    topicReference: fhirtypes.ReferenceType = Field(
        None,
        alias="topicReference",
        title="Focus of contract interest",
        description=(
            "Narrows the range of legal concerns to focus on the achievement of "
            "specific contractual objectives."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e topic[x]
        one_of_many="topic",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    type: fhirtypes.CodeableConceptType = Field(
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
        # if property is element of this resource.
        element_property=True,
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Basal definition",
        description=(
            "Canonical identifier for this contract, represented as a URI (globally"
            " unique)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business edition",
        description=(
            "An edition identifier used for business purposes to label business "
            "significant variants."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1013(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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


class ContractContentDefinition(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Contract precursor content.
    Precusory content developed with a focus and intent of supporting the
    formation a Contract instance, which may be associated with and
    transformable into a Contract.
    """

    resource_type = Field("ContractContentDefinition", const=True)

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Publication Ownership",
        description=(
            "A copyright statement relating to Contract precursor content. "
            "Copyright statements are generally legal restrictions on the use and "
            "publishing of the Contract precursor content."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    publicationDate: fhirtypes.DateTime = Field(
        None,
        alias="publicationDate",
        title="When published",
        description=(
            "The date (and optionally time) when the contract was last "
            "significantly changed. The date must change when the business version "
            "changes and it must change if the status code changes. In addition, it"
            " should change when the substantive content of the contract changes."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    publicationDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publicationDate", title="Extension field for ``publicationDate``."
    )

    publicationStatus: fhirtypes.Code = Field(
        None,
        alias="publicationStatus",
        title=(
            "amended | appended | cancelled | disputed | entered-in-error | "
            "executable +"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "amended",
            "appended",
            "cancelled",
            "disputed",
            "entered-in-error",
            "executable",
            "+",
        ],
    )
    publicationStatus__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_publicationStatus",
        title="Extension field for ``publicationStatus``.",
    )

    publisher: fhirtypes.ReferenceType = Field(
        None,
        alias="publisher",
        title="Publisher Entity",
        description=(
            "The  individual or organization that published the Contract precursor "
            "content."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "PractitionerRole", "Organization"],
    )

    subType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="subType",
        title="Detailed Content Type Definition",
        description="Detailed Precusory content type.",
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Content structure and use",
        description=(
            "Precusory content structure and use, i.e., a boilerplate, template, "
            "application for a contract such as an insurance policy or benefits "
            "under a program, e.g., workers compensation."
        ),
        # if property is element of this resource.
        element_property=True,
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2771(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("publicationStatus", "publicationStatus__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


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

    resource_type = Field("ContractFriendly", const=True)

    contentAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="contentAttachment",
        title="Easily comprehended representation of this Contract",
        description=(
            "Human readable rendering of this Contract in a format and "
            "representation intended to enhance comprehension and ensure "
            "understandability."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e content[x]
        one_of_many="content",
        one_of_many_required=True,
    )

    contentReference: fhirtypes.ReferenceType = Field(
        None,
        alias="contentReference",
        title="Easily comprehended representation of this Contract",
        description=(
            "Human readable rendering of this Contract in a format and "
            "representation intended to enhance comprehension and ensure "
            "understandability."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e content[x]
        one_of_many="content",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Composition",
            "DocumentReference",
            "QuestionnaireResponse",
        ],
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1847(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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


class ContractLegal(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Contract Legal Language.
    List of Legal expressions or representations of this Contract.
    """

    resource_type = Field("ContractLegal", const=True)

    contentAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="contentAttachment",
        title="Contract Legal Text",
        description="Contract legal text in human renderable form.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e content[x]
        one_of_many="content",
        one_of_many_required=True,
    )

    contentReference: fhirtypes.ReferenceType = Field(
        None,
        alias="contentReference",
        title="Contract Legal Text",
        description="Contract legal text in human renderable form.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e content[x]
        one_of_many="content",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Composition",
            "DocumentReference",
            "QuestionnaireResponse",
        ],
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1490(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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


class ContractRule(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Computable Contract Language.
    List of Computable Policy Rule Language Representations of this Contract.
    """

    resource_type = Field("ContractRule", const=True)

    contentAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="contentAttachment",
        title="Computable Contract Rules",
        description=(
            "Computable Contract conveyed using a policy rule language (e.g. XACML,"
            " DKAL, SecPal)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e content[x]
        one_of_many="content",
        one_of_many_required=True,
    )

    contentReference: fhirtypes.ReferenceType = Field(
        None,
        alias="contentReference",
        title="Computable Contract Rules",
        description=(
            "Computable Contract conveyed using a policy rule language (e.g. XACML,"
            " DKAL, SecPal)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e content[x]
        one_of_many="content",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1406(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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

    resource_type = Field("ContractSigner", const=True)

    party: fhirtypes.ReferenceType = Field(
        ...,
        alias="party",
        title="Contract Signatory Party",
        description="Party which is a signator to this Contract.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Organization",
            "Patient",
            "Practitioner",
            "PractitionerRole",
            "RelatedPerson",
        ],
    )

    signature: typing.List[fhirtypes.SignatureType] = Field(
        ...,
        alias="signature",
        title="Contract Documentation Signature",
        description="Legally binding Contract DSIG signature contents in Base64.",
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodingType = Field(
        ...,
        alias="type",
        title="Contract Signatory Role",
        description="Role of this Contract signer, e.g. notary, grantee.",
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("ContractTerm", const=True)

    action: typing.List[fhirtypes.ContractTermActionType] = Field(
        None,
        alias="action",
        title="Entity being ascribed responsibility",
        description=(
            "An actor taking a role in an activity for which it can be assigned "
            "some degree of responsibility for the activity taking place."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    applies: fhirtypes.PeriodType = Field(
        None,
        alias="applies",
        title="Contract Term Effective Time",
        description=(
            "Relevant time or time-period when this Contract Provision is "
            "applicable."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    asset: typing.List[fhirtypes.ContractTermAssetType] = Field(
        None,
        alias="asset",
        title="Contract Term Asset List",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    group: typing.List[fhirtypes.ContractTermType] = Field(
        None,
        alias="group",
        title="Nested Contract Term Group",
        description="Nested group of Contract Provisions.",
        # if property is element of this resource.
        element_property=True,
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Contract Term Number",
        description="Unique identifier for this particular Contract Provision.",
        # if property is element of this resource.
        element_property=True,
    )

    issued: fhirtypes.DateTime = Field(
        None,
        alias="issued",
        title="Contract Term Issue Date Time",
        description="When this Contract Provision was issued.",
        # if property is element of this resource.
        element_property=True,
    )
    issued__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_issued", title="Extension field for ``issued``."
    )

    offer: fhirtypes.ContractTermOfferType = Field(
        ...,
        alias="offer",
        title="Context of the Contract term",
        description=(
            "The matter of concern in the context of this provision of the " "agrement."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    securityLabel: typing.List[fhirtypes.ContractTermSecurityLabelType] = Field(
        None,
        alias="securityLabel",
        title="Protection for the Term",
        description=(
            "Security labels that protect the handling of information about the "
            "term and its elements, which may be specifically identified."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    subType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="subType",
        title="Contract Term Type specific classification",
        description=(
            "A specialized legal clause or condition based on overarching contract "
            "type."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Term Statement",
        description="Statement of a provision in a policy or a contract.",
        # if property is element of this resource.
        element_property=True,
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )

    topicCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="topicCodeableConcept",
        title="Term Concern",
        description="The entity that the term applies to.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e topic[x]
        one_of_many="topic",
        one_of_many_required=False,
    )

    topicReference: fhirtypes.ReferenceType = Field(
        None,
        alias="topicReference",
        title="Term Concern",
        description="The entity that the term applies to.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e topic[x]
        one_of_many="topic",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Contract Term Type or Form",
        description=(
            "A legal clause or condition contained within a contract that requires "
            "one or both parties to perform a particular requirement by some "
            "specified time or prevents one or both parties from performing a "
            "particular requirement by some specified time."
        ),
        # if property is element of this resource.
        element_property=True,
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1414(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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


class ContractTermAction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Entity being ascribed responsibility.
    An actor taking a role in an activity for which it can be assigned some
    degree of responsibility for the activity taking place.
    """

    resource_type = Field("ContractTermAction", const=True)

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title="Episode associated with action",
        description=(
            "Encounter or Episode with primary association to the specified term "
            "activity."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter", "EpisodeOfCare"],
    )

    contextLinkId: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="contextLinkId",
        title="Pointer to specific item",
        description=(
            "Id [identifier??] of the clause or question text related to the "
            "requester of this action in the referenced form or "
            "QuestionnaireResponse."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    contextLinkId__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_contextLinkId", title="Extension field for ``contextLinkId``."
    )

    doNotPerform: bool = Field(
        None,
        alias="doNotPerform",
        title="True if the term prohibits the  action",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    doNotPerform__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_doNotPerform", title="Extension field for ``doNotPerform``."
    )

    intent: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="intent",
        title="Purpose for the Contract Term Action",
        description=(
            "Reason or purpose for the action stipulated by this Contract " "Provision."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    linkId: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="linkId",
        title="Pointer to specific item",
        description=(
            "Id [identifier??] of the clause or question text related to this "
            "action in the referenced form or QuestionnaireResponse."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    linkId__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_linkId", title="Extension field for ``linkId``.")

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Comments about the action",
        description=(
            "Comments made about the term action made by the requester, performer, "
            "subject or other participants."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    occurrenceDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurrenceDateTime",
        title="When action happens",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_occurrenceDateTime",
        title="Extension field for ``occurrenceDateTime``.",
    )

    occurrencePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="occurrencePeriod",
        title="When action happens",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )

    occurrenceTiming: fhirtypes.TimingType = Field(
        None,
        alias="occurrenceTiming",
        title="When action happens",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )

    performer: fhirtypes.ReferenceType = Field(
        None,
        alias="performer",
        title="Actor that wil execute (or not) the action",
        description=(
            "Indicates who or what is being asked to perform (or not perform) the "
            "ction."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
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
    )

    performerLinkId: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="performerLinkId",
        title="Pointer to specific item",
        description=(
            "Id [identifier??] of the clause or question text related to the reason"
            " type or reference of this  action in the referenced form or "
            "QuestionnaireResponse."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    performerLinkId__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_performerLinkId", title="Extension field for ``performerLinkId``."
    )

    performerRole: fhirtypes.CodeableConceptType = Field(
        None,
        alias="performerRole",
        title="Competency of the performer",
        description=(
            "The type of role or competency of an individual desired or required to"
            " perform or not perform the action."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    performerType: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="performerType",
        title="Kind of service performer",
        description=(
            "The type of individual that is desired or required to perform or not "
            "perform the action."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    reason: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="reason",
        title="Why is action (not) needed?",
        description=(
            "Rationale for the action to be performed or not performed. Describes "
            "why the action is permitted or prohibited. Either a coded concept, or "
            "another resource whose existence justifies permitting or not "
            "permitting this action."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Condition",
            "Observation",
            "DiagnosticReport",
            "DocumentReference",
            "Questionnaire",
            "QuestionnaireResponse",
        ],
    )

    reasonLinkId: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="reasonLinkId",
        title="Pointer to specific item",
        description=(
            "Id [identifier??] of the clause or question text related to the reason"
            " type or reference of this  action in the referenced form or "
            "QuestionnaireResponse."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    reasonLinkId__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_reasonLinkId", title="Extension field for ``reasonLinkId``."
    )

    requester: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="requester",
        title="Who asked for action",
        description=(
            "Who or what initiated the action and has responsibility for its "
            "activation."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "RelatedPerson",
            "Practitioner",
            "PractitionerRole",
            "Device",
            "Group",
            "Organization",
        ],
    )

    requesterLinkId: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="requesterLinkId",
        title="Pointer to specific item",
        description=(
            "Id [identifier??] of the clause or question text related to the "
            "requester of this action in the referenced form or "
            "QuestionnaireResponse."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    requesterLinkId__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_requesterLinkId", title="Extension field for ``requesterLinkId``."
    )

    securityLabelNumber: typing.List[typing.Optional[fhirtypes.UnsignedInt]] = Field(
        None,
        alias="securityLabelNumber",
        title="Action restriction numbers",
        description="Security labels that protects the action.",
        # if property is element of this resource.
        element_property=True,
    )
    securityLabelNumber__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_securityLabelNumber",
        title="Extension field for ``securityLabelNumber``.",
    )

    status: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="status",
        title="State of the action",
        description="Current state of the term action.",
        # if property is element of this resource.
        element_property=True,
    )

    subject: typing.List[fhirtypes.ContractTermActionSubjectType] = Field(
        None,
        alias="subject",
        title="Entity of the action",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type or form of the action",
        description=(
            "Activity or service obligation to be done or not done, performed or "
            "not performed, effectuated or not by this Contract term."
        ),
        # if property is element of this resource.
        element_property=True,
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
            "reason",
            "reasonLinkId",
            "note",
            "securityLabelNumber",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2021(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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


class ContractTermActionSubject(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Entity of the action.
    """

    resource_type = Field("ContractTermActionSubject", const=True)

    reference: typing.List[fhirtypes.ReferenceType] = Field(
        ...,
        alias="reference",
        title="Entity of the action",
        description="The entity the action is performed or not performed on or for.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "RelatedPerson",
            "Practitioner",
            "PractitionerRole",
            "Device",
            "Group",
            "Organization",
        ],
    )

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="Role type of the agent",
        description="Role type of agent assigned roles in this Contract.",
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("ContractTermAsset", const=True)

    answer: typing.List[fhirtypes.ContractTermOfferAnswerType] = Field(
        None,
        alias="answer",
        title="Response to assets",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    condition: fhirtypes.String = Field(
        None,
        alias="condition",
        title="Quality desctiption of asset",
        description=(
            "Description of the quality and completeness of the asset that may be a"
            " factor in its valuation."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    condition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_condition", title="Extension field for ``condition``."
    )

    context: typing.List[fhirtypes.ContractTermAssetContextType] = Field(
        None,
        alias="context",
        title="Circumstance of the asset",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    linkId: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="linkId",
        title="Pointer to asset text",
        description=(
            "Id [identifier??] of the clause or question text about the asset in "
            "the referenced form or QuestionnaireResponse."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    linkId__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_linkId", title="Extension field for ``linkId``.")

    period: typing.List[fhirtypes.PeriodType] = Field(
        None,
        alias="period",
        title="Time period of the asset",
        description="Asset relevant contractual time period.",
        # if property is element of this resource.
        element_property=True,
    )

    periodType: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="periodType",
        title="Asset availability types",
        description="Type of Asset availability for use or ownership.",
        # if property is element of this resource.
        element_property=True,
    )

    relationship: fhirtypes.CodingType = Field(
        None,
        alias="relationship",
        title="Kinship of the asset",
        description=(
            "Specifies the applicability of the term to an asset resource instance,"
            " and instances it refers to or instances that refer to it, and/or are "
            "owned by the offeree."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    scope: fhirtypes.CodeableConceptType = Field(
        None,
        alias="scope",
        title="Range of asset",
        description="Differentiates the kind of the asset .",
        # if property is element of this resource.
        element_property=True,
    )

    securityLabelNumber: typing.List[typing.Optional[fhirtypes.UnsignedInt]] = Field(
        None,
        alias="securityLabelNumber",
        title="Asset restriction numbers",
        description="Security labels that protects the asset.",
        # if property is element of this resource.
        element_property=True,
    )
    securityLabelNumber__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_securityLabelNumber",
        title="Extension field for ``securityLabelNumber``.",
    )

    subtype: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="subtype",
        title="Asset sub-category",
        description="May be a subtype or part of an offered asset.",
        # if property is element of this resource.
        element_property=True,
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Asset clause or question text",
        description=(
            "Clause or question text (Prose Object) concerning the asset in a "
            "linked form, such as a QuestionnaireResponse used in the formation of "
            "the contract."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )

    type: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="Asset category",
        description="Target entity type about which the term may be concerned.",
        # if property is element of this resource.
        element_property=True,
    )

    typeReference: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="typeReference",
        title="Associated entities",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    usePeriod: typing.List[fhirtypes.PeriodType] = Field(
        None,
        alias="usePeriod",
        title="Time period",
        description="Time period of asset use.",
        # if property is element of this resource.
        element_property=True,
    )

    valuedItem: typing.List[fhirtypes.ContractTermAssetValuedItemType] = Field(
        None,
        alias="valuedItem",
        title="Contract Valued Item List",
        description=None,
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("ContractTermAssetContext", const=True)

    code: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="code",
        title="Codeable asset context",
        description=(
            "Coded representation of the context generally or of the Referenced "
            "entity, such as the asset holder type or location."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    reference: fhirtypes.ReferenceType = Field(
        None,
        alias="reference",
        title="Creator,custodian or owner",
        description=(
            "Asset context reference may include the creator, custodian, or owning "
            "Person or Organization (e.g., bank, repository),  location held, e.g.,"
            " building,  jurisdiction."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Context description",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    resource_type = Field("ContractTermAssetValuedItem", const=True)

    effectiveTime: fhirtypes.DateTime = Field(
        None,
        alias="effectiveTime",
        title="Contract Valued Item Effective Tiem",
        description=(
            "Indicates the time during which this Contract ValuedItem information "
            "is effective."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    effectiveTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_effectiveTime", title="Extension field for ``effectiveTime``."
    )

    entityCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="entityCodeableConcept",
        title="Contract Valued Item Type",
        description="Specific type of Contract Valued Item that may be priced.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e entity[x]
        one_of_many="entity",
        one_of_many_required=False,
    )

    entityReference: fhirtypes.ReferenceType = Field(
        None,
        alias="entityReference",
        title="Contract Valued Item Type",
        description="Specific type of Contract Valued Item that may be priced.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e entity[x]
        one_of_many="entity",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    factor: fhirtypes.Decimal = Field(
        None,
        alias="factor",
        title="Contract Valued Item Price Scaling Factor",
        description=(
            "A real number that represents a multiplier used in determining the "
            "overall value of the Contract Valued Item delivered. The concept of a "
            "Factor allows for a discount or surcharge multiplier to be applied to "
            "a monetary amount."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_factor", title="Extension field for ``factor``."
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Contract Valued Item Number",
        description="Identifies a Contract Valued Item instance.",
        # if property is element of this resource.
        element_property=True,
    )

    linkId: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="linkId",
        title="Pointer to specific item",
        description=(
            "Id  of the clause or question text related to the context of this "
            "valuedItem in the referenced form or QuestionnaireResponse."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    linkId__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_linkId", title="Extension field for ``linkId``.")

    net: fhirtypes.MoneyType = Field(
        None,
        alias="net",
        title="Total Contract Valued Item Value",
        description=(
            "Expresses the product of the Contract Valued Item unitQuantity and the"
            " unitPriceAmt. For example, the formula: unit Quantity * unit Price "
            "(Cost per Point) * factor Number  * points = net Amount. Quantity, "
            "factor and points are assumed to be 1 if not supplied."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    payment: fhirtypes.String = Field(
        None,
        alias="payment",
        title="Terms of valuation",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    payment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_payment", title="Extension field for ``payment``."
    )

    paymentDate: fhirtypes.DateTime = Field(
        None,
        alias="paymentDate",
        title="When payment is due",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    paymentDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_paymentDate", title="Extension field for ``paymentDate``."
    )

    points: fhirtypes.Decimal = Field(
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
        # if property is element of this resource.
        element_property=True,
    )
    points__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_points", title="Extension field for ``points``."
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Count of Contract Valued Items",
        description=(
            "Specifies the units by which the Contract Valued Item is measured or "
            "counted, and quantifies the countable or measurable Contract Valued "
            "Item instances."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    recipient: fhirtypes.ReferenceType = Field(
        None,
        alias="recipient",
        title="Who will receive payment",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Organization",
            "Patient",
            "Practitioner",
            "PractitionerRole",
            "RelatedPerson",
        ],
    )

    responsible: fhirtypes.ReferenceType = Field(
        None,
        alias="responsible",
        title="Who will make payment",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Organization",
            "Patient",
            "Practitioner",
            "PractitionerRole",
            "RelatedPerson",
        ],
    )

    securityLabelNumber: typing.List[typing.Optional[fhirtypes.UnsignedInt]] = Field(
        None,
        alias="securityLabelNumber",
        title="Security Labels that define affected terms",
        description=(
            "A set of security labels that define which terms are controlled by "
            "this condition."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    securityLabelNumber__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_securityLabelNumber",
        title="Extension field for ``securityLabelNumber``.",
    )

    unitPrice: fhirtypes.MoneyType = Field(
        None,
        alias="unitPrice",
        title="Contract Valued Item fee, charge, or cost",
        description="A Contract Valued Item unit valuation measure.",
        # if property is element of this resource.
        element_property=True,
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2934(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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


class ContractTermOffer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Context of the Contract term.
    The matter of concern in the context of this provision of the agrement.
    """

    resource_type = Field("ContractTermOffer", const=True)

    answer: typing.List[fhirtypes.ContractTermOfferAnswerType] = Field(
        None,
        alias="answer",
        title="Response to offer text",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    decision: fhirtypes.CodeableConceptType = Field(
        None,
        alias="decision",
        title="Accepting party choice",
        description=(
            "Type of choice made by accepting party with respect to an offer made "
            "by an offeror/ grantee."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    decisionMode: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="decisionMode",
        title="How decision is conveyed",
        description="How the decision about a Contract was conveyed.",
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Offer business ID",
        description="Unique identifier for this particular Contract Provision.",
        # if property is element of this resource.
        element_property=True,
    )

    linkId: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="linkId",
        title="Pointer to text",
        description=(
            "The id of the clause or question text of the offer in the referenced "
            "questionnaire/response."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    linkId__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_linkId", title="Extension field for ``linkId``.")

    party: typing.List[fhirtypes.ContractTermOfferPartyType] = Field(
        None,
        alias="party",
        title="Offer Recipient",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    securityLabelNumber: typing.List[typing.Optional[fhirtypes.UnsignedInt]] = Field(
        None,
        alias="securityLabelNumber",
        title="Offer restriction numbers",
        description="Security labels that protects the offer.",
        # if property is element of this resource.
        element_property=True,
    )
    securityLabelNumber__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_securityLabelNumber",
        title="Extension field for ``securityLabelNumber``.",
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Human readable offer text",
        description="Human readable form of this Contract Offer.",
        # if property is element of this resource.
        element_property=True,
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )

    topic: fhirtypes.ReferenceType = Field(
        None,
        alias="topic",
        title="Negotiable offer asset",
        description=(
            "The owner of an asset has the residual control rights over the asset: "
            "the right to decide all usages of the asset in any way not "
            "inconsistent with a prior contract, custom, or law (Hart, 1995, p. "
            "30)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Contract Offer Type or Form",
        description=(
            "Type of Contract Provision such as specific requirements, purposes for"
            " actions, obligations, prohibitions, e.g. life time maximum benefit."
        ),
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("ContractTermOfferAnswer", const=True)

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="The actual answer response",
        description=(
            "Response to an offer clause or question text,  which enables selection"
            " of values to be agreed to, e.g., the period of participation, the "
            "date of occupancy of a rental, warranty duration, or whether "
            "biospecimen may be used for further research."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="The actual answer response",
        description=(
            "Response to an offer clause or question text,  which enables selection"
            " of values to be agreed to, e.g., the period of participation, the "
            "date of occupancy of a rental, warranty duration, or whether "
            "biospecimen may be used for further research."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCoding: fhirtypes.CodingType = Field(
        None,
        alias="valueCoding",
        title="The actual answer response",
        description=(
            "Response to an offer clause or question text,  which enables selection"
            " of values to be agreed to, e.g., the period of participation, the "
            "date of occupancy of a rental, warranty duration, or whether "
            "biospecimen may be used for further research."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueDate: fhirtypes.Date = Field(
        None,
        alias="valueDate",
        title="The actual answer response",
        description=(
            "Response to an offer clause or question text,  which enables selection"
            " of values to be agreed to, e.g., the period of participation, the "
            "date of occupancy of a rental, warranty duration, or whether "
            "biospecimen may be used for further research."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDate", title="Extension field for ``valueDate``."
    )

    valueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="valueDateTime",
        title="The actual answer response",
        description=(
            "Response to an offer clause or question text,  which enables selection"
            " of values to be agreed to, e.g., the period of participation, the "
            "date of occupancy of a rental, warranty duration, or whether "
            "biospecimen may be used for further research."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDateTime", title="Extension field for ``valueDateTime``."
    )

    valueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="valueDecimal",
        title="The actual answer response",
        description=(
            "Response to an offer clause or question text,  which enables selection"
            " of values to be agreed to, e.g., the period of participation, the "
            "date of occupancy of a rental, warranty duration, or whether "
            "biospecimen may be used for further research."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDecimal", title="Extension field for ``valueDecimal``."
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="The actual answer response",
        description=(
            "Response to an offer clause or question text,  which enables selection"
            " of values to be agreed to, e.g., the period of participation, the "
            "date of occupancy of a rental, warranty duration, or whether "
            "biospecimen may be used for further research."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueInteger", title="Extension field for ``valueInteger``."
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="The actual answer response",
        description=(
            "Response to an offer clause or question text,  which enables selection"
            " of values to be agreed to, e.g., the period of participation, the "
            "date of occupancy of a rental, warranty duration, or whether "
            "biospecimen may be used for further research."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueReference",
        title="The actual answer response",
        description=(
            "Response to an offer clause or question text,  which enables selection"
            " of values to be agreed to, e.g., the period of participation, the "
            "date of occupancy of a rental, warranty duration, or whether "
            "biospecimen may be used for further research."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="The actual answer response",
        description=(
            "Response to an offer clause or question text,  which enables selection"
            " of values to be agreed to, e.g., the period of participation, the "
            "date of occupancy of a rental, warranty duration, or whether "
            "biospecimen may be used for further research."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    valueTime: fhirtypes.Time = Field(
        None,
        alias="valueTime",
        title="The actual answer response",
        description=(
            "Response to an offer clause or question text,  which enables selection"
            " of values to be agreed to, e.g., the period of participation, the "
            "date of occupancy of a rental, warranty duration, or whether "
            "biospecimen may be used for further research."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueTime", title="Extension field for ``valueTime``."
    )

    valueUri: fhirtypes.Uri = Field(
        None,
        alias="valueUri",
        title="The actual answer response",
        description=(
            "Response to an offer clause or question text,  which enables selection"
            " of values to be agreed to, e.g., the period of participation, the "
            "date of occupancy of a rental, warranty duration, or whether "
            "biospecimen may be used for further research."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2541(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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


class ContractTermOfferParty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Offer Recipient.
    """

    resource_type = Field("ContractTermOfferParty", const=True)

    reference: typing.List[fhirtypes.ReferenceType] = Field(
        ...,
        alias="reference",
        title="Referenced entity",
        description="Participant in the offer.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "RelatedPerson",
            "Practitioner",
            "PractitionerRole",
            "Device",
            "Group",
            "Organization",
        ],
    )

    role: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="role",
        title="Participant engagement type",
        description="How the party participates in the offer.",
        # if property is element of this resource.
        element_property=True,
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
    its elements, which may be specifically identified.
    """

    resource_type = Field("ContractTermSecurityLabel", const=True)

    category: typing.List[fhirtypes.CodingType] = Field(
        None,
        alias="category",
        title="Applicable Policy",
        description=(
            "Security label privacy tag that specifies the applicable privacy and "
            "security policies governing this term and/or term elements."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    classification: fhirtypes.CodingType = Field(
        ...,
        alias="classification",
        title="Confidentiality Protection",
        description=(
            "Security label privacy tag that specifies the level of confidentiality"
            " protection required for this term and/or term elements."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    control: typing.List[fhirtypes.CodingType] = Field(
        None,
        alias="control",
        title="Handling Instructions",
        description=(
            "Security label privacy tag that specifies the manner in which term "
            "and/or term elements are to be protected."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    number: typing.List[typing.Optional[fhirtypes.UnsignedInt]] = Field(
        None,
        alias="number",
        title="Link to Security Labels",
        description=(
            "Number used to link this term or term element to the applicable "
            "Security Label."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    number__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_number", title="Extension field for ``number``.")

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
