# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Contract
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Contract(domainresource.DomainResource):
    """ Legal Agreement.
    Legally enforceable, formally recorded unilateral or bilateral directive
    i.e., a policy or agreement.
    """

    resource_type = Field("Contract", const=True)

    alias: ListType[fhirtypes.String] = Field(
        None,
        alias="alias",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Acronym or short name",
    )

    applies: fhirtypes.PeriodType = Field(
        None,
        alias="applies",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Effective time",
    )

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title=(
            "Type `Reference` referencing `Patient, Practitioner, PractitionerRole,"
            " Organization` (represented as `dict` in JSON)"
        ),
        description="Source of Contract",
    )

    authority: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="authority",
        title=(
            "List of `Reference` items referencing `Organization` (represented as "
            "`dict` in JSON)"
        ),
        description="Authority under which this Contract has standing",
    )

    contentDefinition: fhirtypes.ContractContentDefinitionType = Field(
        None,
        alias="contentDefinition",
        title="Type `ContractContentDefinition` (represented as `dict` in JSON)",
        description="Contract precursor content",
    )

    contentDerivative: fhirtypes.CodeableConceptType = Field(
        None,
        alias="contentDerivative",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Content derived from the basal information",
    )

    domain: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="domain",
        title=(
            "List of `Reference` items referencing `Location` (represented as "
            "`dict` in JSON)"
        ),
        description=(
            "A sphere of control governed by an authoritative jurisdiction, "
            "organization, or person"
        ),
    )

    expirationType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="expirationType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Contract cessation cause",
    )

    friendly: ListType[fhirtypes.ContractFriendlyType] = Field(
        None,
        alias="friendly",
        title="List of `ContractFriendly` items (represented as `dict` in JSON)",
        description="Contract Friendly Language",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Contract number",
    )

    instantiatesCanonical: fhirtypes.ReferenceType = Field(
        None,
        alias="instantiatesCanonical",
        title=(
            "Type `Reference` referencing `Contract` (represented as `dict` in " "JSON)"
        ),
        description="Source Contract Definition",
    )

    instantiatesUri: fhirtypes.Uri = Field(
        None,
        alias="instantiatesUri",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="External Contract Definition",
    )

    issued: fhirtypes.DateTime = Field(
        None,
        alias="issued",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When this Contract was issued",
    )

    legal: ListType[fhirtypes.ContractLegalType] = Field(
        None,
        alias="legal",
        title="List of `ContractLegal` items (represented as `dict` in JSON)",
        description="Contract Legal Language",
    )

    legalState: fhirtypes.CodeableConceptType = Field(
        None,
        alias="legalState",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Negotiation status",
    )

    legallyBindingAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="legallyBindingAttachment",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="Binding Contract",
        one_of_many="legallyBinding",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    legallyBindingReference: fhirtypes.ReferenceType = Field(
        None,
        alias="legallyBindingReference",
        title=(
            "Type `Reference` referencing `Composition, DocumentReference, "
            "QuestionnaireResponse, Contract` (represented as `dict` in JSON)"
        ),
        description="Binding Contract",
        one_of_many="legallyBinding",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Computer friendly designation",
    )

    relevantHistory: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="relevantHistory",
        title=(
            "List of `Reference` items referencing `Provenance` (represented as "
            "`dict` in JSON)"
        ),
        description="Key event in Contract History",
    )

    rule: ListType[fhirtypes.ContractRuleType] = Field(
        None,
        alias="rule",
        title="List of `ContractRule` items (represented as `dict` in JSON)",
        description="Computable Contract Language",
    )

    scope: fhirtypes.CodeableConceptType = Field(
        None,
        alias="scope",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Range of Legal Concerns",
    )

    signer: ListType[fhirtypes.ContractSignerType] = Field(
        None,
        alias="signer",
        title="List of `ContractSigner` items (represented as `dict` in JSON)",
        description="Contract Signatory",
    )

    site: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="site",
        title=(
            "List of `Reference` items referencing `Location` (represented as "
            "`dict` in JSON)"
        ),
        description="Specific Location",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "amended | appended | cancelled | disputed | entered-in-error | "
            "executable | executed | negotiable | offered | policy | rejected | "
            "renewed | revoked | resolved | terminated"
        ),
    )

    subType: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="subType",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Subtype within the context of type",
    )

    subject: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="subject",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="Contract Target Entity",
    )

    subtitle: fhirtypes.String = Field(
        None,
        alias="subtitle",
        title="Type `String` (represented as `dict` in JSON)",
        description="Subordinate Friendly name",
    )

    supportingInfo: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingInfo",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="Extra Information",
    )

    term: ListType[fhirtypes.ContractTermType] = Field(
        None,
        alias="term",
        title="List of `ContractTerm` items (represented as `dict` in JSON)",
        description="Contract Term List",
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="Human Friendly name",
    )

    topicCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="topicCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Focus of contract interest",
        one_of_many="topic",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    topicReference: fhirtypes.ReferenceType = Field(
        None,
        alias="topicReference",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Focus of contract interest",
        one_of_many="topic",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Legal instrument category",
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Basal definition",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String` (represented as `dict` in JSON)",
        description="Business edition",
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
    """ Contract precursor content.
    Precusory content developed with a focus and intent of supporting the
    formation a Contract instance, which may be associated with and
    transformable into a Contract.
    """

    resource_type = Field("ContractContentDefinition", const=True)

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Publication Ownership",
    )

    publicationDate: fhirtypes.DateTime = Field(
        None,
        alias="publicationDate",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When published",
    )

    publicationStatus: fhirtypes.Code = Field(
        ...,
        alias="publicationStatus",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "amended | appended | cancelled | disputed | entered-in-error | "
            "executable | executed | negotiable | offered | policy | rejected | "
            "renewed | revoked | resolved | terminated"
        ),
    )

    publisher: fhirtypes.ReferenceType = Field(
        None,
        alias="publisher",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole, "
            "Organization` (represented as `dict` in JSON)"
        ),
        description="Publisher Entity",
    )

    subType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="subType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Detailed Content Type Definition",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Content structure and use",
    )


class ContractFriendly(backboneelement.BackboneElement):
    """ Contract Friendly Language.
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
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="Easily comprehended representation of this Contract",
        one_of_many="content",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    contentReference: fhirtypes.ReferenceType = Field(
        None,
        alias="contentReference",
        title=(
            "Type `Reference` referencing `Composition, DocumentReference, "
            "QuestionnaireResponse` (represented as `dict` in JSON)"
        ),
        description="Easily comprehended representation of this Contract",
        one_of_many="content",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
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
    """ Contract Legal Language.
    List of Legal expressions or representations of this Contract.
    """

    resource_type = Field("ContractLegal", const=True)

    contentAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="contentAttachment",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="Contract Legal Text",
        one_of_many="content",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    contentReference: fhirtypes.ReferenceType = Field(
        None,
        alias="contentReference",
        title=(
            "Type `Reference` referencing `Composition, DocumentReference, "
            "QuestionnaireResponse` (represented as `dict` in JSON)"
        ),
        description="Contract Legal Text",
        one_of_many="content",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
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
    """ Computable Contract Language.
    List of Computable Policy Rule Language Representations of this Contract.
    """

    resource_type = Field("ContractRule", const=True)

    contentAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="contentAttachment",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="Computable Contract Rules",
        one_of_many="content",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    contentReference: fhirtypes.ReferenceType = Field(
        None,
        alias="contentReference",
        title=(
            "Type `Reference` referencing `DocumentReference` (represented as "
            "`dict` in JSON)"
        ),
        description="Computable Contract Rules",
        one_of_many="content",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
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
    """ Contract Signatory.
    Parties with legal standing in the Contract, including the principal
    parties, the grantor(s) and grantee(s), which are any person or
    organization bound by the contract, and any ancillary parties, which
    facilitate the execution of the contract such as a notary or witness.
    """

    resource_type = Field("ContractSigner", const=True)

    party: fhirtypes.ReferenceType = Field(
        ...,
        alias="party",
        title=(
            "Type `Reference` referencing `Organization, Patient, Practitioner, "
            "PractitionerRole, RelatedPerson` (represented as `dict` in JSON)"
        ),
        description="Contract Signatory Party",
    )

    signature: ListType[fhirtypes.SignatureType] = Field(
        ...,
        alias="signature",
        title="List of `Signature` items (represented as `dict` in JSON)",
        description="Contract Documentation Signature",
    )

    type: fhirtypes.CodingType = Field(
        ...,
        alias="type",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Contract Signatory Role",
    )


class ContractTerm(backboneelement.BackboneElement):
    """ Contract Term List.
    One or more Contract Provisions, which may be related and conveyed as a
    group, and may contain nested groups.
    """

    resource_type = Field("ContractTerm", const=True)

    action: ListType[fhirtypes.ContractTermActionType] = Field(
        None,
        alias="action",
        title="List of `ContractTermAction` items (represented as `dict` in JSON)",
        description="Entity being ascribed responsibility",
    )

    applies: fhirtypes.PeriodType = Field(
        None,
        alias="applies",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Contract Term Effective Time",
    )

    asset: ListType[fhirtypes.ContractTermAssetType] = Field(
        None,
        alias="asset",
        title="List of `ContractTermAsset` items (represented as `dict` in JSON)",
        description="Contract Term Asset List",
    )

    group: ListType[fhirtypes.ContractTermType] = Field(
        None,
        alias="group",
        title="List of `ContractTerm` items (represented as `dict` in JSON)",
        description="Nested Contract Term Group",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Contract Term Number",
    )

    issued: fhirtypes.DateTime = Field(
        None,
        alias="issued",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Contract Term Issue Date Time",
    )

    offer: fhirtypes.ContractTermOfferType = Field(
        ...,
        alias="offer",
        title="Type `ContractTermOffer` (represented as `dict` in JSON)",
        description="Context of the Contract term",
    )

    securityLabel: ListType[fhirtypes.ContractTermSecurityLabelType] = Field(
        None,
        alias="securityLabel",
        title=(
            "List of `ContractTermSecurityLabel` items (represented as `dict` in "
            "JSON)"
        ),
        description="Protection for the Term",
    )

    subType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="subType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Contract Term Type specific classification",
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Type `String` (represented as `dict` in JSON)",
        description="Term Statement",
    )

    topicCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="topicCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Term Concern",
        one_of_many="topic",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    topicReference: fhirtypes.ReferenceType = Field(
        None,
        alias="topicReference",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Term Concern",
        one_of_many="topic",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Contract Term Type or Form",
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
    """ Entity being ascribed responsibility.
    An actor taking a role in an activity for which it can be assigned some
    degree of responsibility for the activity taking place.
    """

    resource_type = Field("ContractTermAction", const=True)

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title=(
            "Type `Reference` referencing `Encounter, EpisodeOfCare` (represented "
            "as `dict` in JSON)"
        ),
        description="Episode associated with action",
    )

    contextLinkId: ListType[fhirtypes.String] = Field(
        None,
        alias="contextLinkId",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Pointer to specific item",
    )

    doNotPerform: bool = Field(
        None,
        alias="doNotPerform",
        title="Type `bool`",
        description="True if the term prohibits the  action",
    )

    intent: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="intent",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Purpose for the Contract Term Action",
    )

    linkId: ListType[fhirtypes.String] = Field(
        None,
        alias="linkId",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Pointer to specific item",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Comments about the action",
    )

    occurrenceDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurrenceDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When action happens",
        one_of_many="occurrence",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    occurrencePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="occurrencePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When action happens",
        one_of_many="occurrence",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    occurrenceTiming: fhirtypes.TimingType = Field(
        None,
        alias="occurrenceTiming",
        title="Type `Timing` (represented as `dict` in JSON)",
        description="When action happens",
        one_of_many="occurrence",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    performer: fhirtypes.ReferenceType = Field(
        None,
        alias="performer",
        title=(
            "Type `Reference` referencing `RelatedPerson, Patient, Practitioner, "
            "PractitionerRole, CareTeam, Device, Substance, Organization, Location`"
            " (represented as `dict` in JSON)"
        ),
        description="Actor that wil execute (or not) the action",
    )

    performerLinkId: ListType[fhirtypes.String] = Field(
        None,
        alias="performerLinkId",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Pointer to specific item",
    )

    performerRole: fhirtypes.CodeableConceptType = Field(
        None,
        alias="performerRole",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Competency of the performer",
    )

    performerType: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="performerType",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Kind of service performer",
    )

    reason: ListType[fhirtypes.String] = Field(
        None,
        alias="reason",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Why action is to be performed",
    )

    reasonCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Why is action (not) needed?",
    )

    reasonLinkId: ListType[fhirtypes.String] = Field(
        None,
        alias="reasonLinkId",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Pointer to specific item",
    )

    reasonReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title=(
            "List of `Reference` items referencing `Condition, Observation, "
            "DiagnosticReport, DocumentReference, Questionnaire, "
            "QuestionnaireResponse` (represented as `dict` in JSON)"
        ),
        description="Why is action (not) needed?",
    )

    requester: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="requester",
        title=(
            "List of `Reference` items referencing `Patient, RelatedPerson, "
            "Practitioner, PractitionerRole, Device, Group, Organization` "
            "(represented as `dict` in JSON)"
        ),
        description="Who asked for action",
    )

    requesterLinkId: ListType[fhirtypes.String] = Field(
        None,
        alias="requesterLinkId",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Pointer to specific item",
    )

    securityLabelNumber: ListType[fhirtypes.UnsignedInt] = Field(
        None,
        alias="securityLabelNumber",
        title="List of `UnsignedInt` items (represented as `dict` in JSON)",
        description="Action restriction numbers",
    )

    status: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="status",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="State of the action",
    )

    subject: ListType[fhirtypes.ContractTermActionSubjectType] = Field(
        None,
        alias="subject",
        title=(
            "List of `ContractTermActionSubject` items (represented as `dict` in "
            "JSON)"
        ),
        description="Entity of the action",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type or form of the action",
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
    """ Entity of the action.
    """

    resource_type = Field("ContractTermActionSubject", const=True)

    reference: ListType[fhirtypes.ReferenceType] = Field(
        ...,
        alias="reference",
        title=(
            "List of `Reference` items referencing `Patient, RelatedPerson, "
            "Practitioner, PractitionerRole, Device, Group, Organization` "
            "(represented as `dict` in JSON)"
        ),
        description="Entity of the action",
    )

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Role type of the agent",
    )


class ContractTermAsset(backboneelement.BackboneElement):
    """ Contract Term Asset List.
    """

    resource_type = Field("ContractTermAsset", const=True)

    answer: ListType[fhirtypes.ContractTermOfferAnswerType] = Field(
        None,
        alias="answer",
        title=(
            "List of `ContractTermOfferAnswer` items (represented as `dict` in " "JSON)"
        ),
        description="Response to assets",
    )

    condition: fhirtypes.String = Field(
        None,
        alias="condition",
        title="Type `String` (represented as `dict` in JSON)",
        description="Quality desctiption of asset",
    )

    context: ListType[fhirtypes.ContractTermAssetContextType] = Field(
        None,
        alias="context",
        title=(
            "List of `ContractTermAssetContext` items (represented as `dict` in "
            "JSON)"
        ),
        description="Circumstance of the asset",
    )

    linkId: ListType[fhirtypes.String] = Field(
        None,
        alias="linkId",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Pointer to asset text",
    )

    period: ListType[fhirtypes.PeriodType] = Field(
        None,
        alias="period",
        title="List of `Period` items (represented as `dict` in JSON)",
        description="Time period of the asset",
    )

    periodType: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="periodType",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Asset availability types",
    )

    relationship: fhirtypes.CodingType = Field(
        None,
        alias="relationship",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Kinship of the asset",
    )

    scope: fhirtypes.CodeableConceptType = Field(
        None,
        alias="scope",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Range of asset",
    )

    securityLabelNumber: ListType[fhirtypes.UnsignedInt] = Field(
        None,
        alias="securityLabelNumber",
        title="List of `UnsignedInt` items (represented as `dict` in JSON)",
        description="Asset restriction numbers",
    )

    subtype: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="subtype",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Asset sub-category",
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Type `String` (represented as `dict` in JSON)",
        description="Asset clause or question text",
    )

    type: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Asset category",
    )

    typeReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="typeReference",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="Associated entities",
    )

    usePeriod: ListType[fhirtypes.PeriodType] = Field(
        None,
        alias="usePeriod",
        title="List of `Period` items (represented as `dict` in JSON)",
        description="Time period",
    )

    valuedItem: ListType[fhirtypes.ContractTermAssetValuedItemType] = Field(
        None,
        alias="valuedItem",
        title=(
            "List of `ContractTermAssetValuedItem` items (represented as `dict` in "
            "JSON)"
        ),
        description="Contract Valued Item List",
    )


class ContractTermAssetContext(backboneelement.BackboneElement):
    """ Circumstance of the asset.
    """

    resource_type = Field("ContractTermAssetContext", const=True)

    code: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="code",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Codeable asset context",
    )

    reference: fhirtypes.ReferenceType = Field(
        None,
        alias="reference",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Creator,custodian or owner",
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Type `String` (represented as `dict` in JSON)",
        description="Context description",
    )


class ContractTermAssetValuedItem(backboneelement.BackboneElement):
    """ Contract Valued Item List.
    """

    resource_type = Field("ContractTermAssetValuedItem", const=True)

    effectiveTime: fhirtypes.DateTime = Field(
        None,
        alias="effectiveTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Contract Valued Item Effective Tiem",
    )

    entityCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="entityCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Contract Valued Item Type",
        one_of_many="entity",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    entityReference: fhirtypes.ReferenceType = Field(
        None,
        alias="entityReference",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Contract Valued Item Type",
        one_of_many="entity",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    factor: fhirtypes.Decimal = Field(
        None,
        alias="factor",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Contract Valued Item Price Scaling Factor",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Contract Valued Item Number",
    )

    linkId: ListType[fhirtypes.String] = Field(
        None,
        alias="linkId",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Pointer to specific item",
    )

    net: fhirtypes.MoneyType = Field(
        None,
        alias="net",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Total Contract Valued Item Value",
    )

    payment: fhirtypes.String = Field(
        None,
        alias="payment",
        title="Type `String` (represented as `dict` in JSON)",
        description="Terms of valuation",
    )

    paymentDate: fhirtypes.DateTime = Field(
        None,
        alias="paymentDate",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When payment is due",
    )

    points: fhirtypes.Decimal = Field(
        None,
        alias="points",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Contract Valued Item Difficulty Scaling Factor",
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Count of Contract Valued Items",
    )

    recipient: fhirtypes.ReferenceType = Field(
        None,
        alias="recipient",
        title=(
            "Type `Reference` referencing `Organization, Patient, Practitioner, "
            "PractitionerRole, RelatedPerson` (represented as `dict` in JSON)"
        ),
        description="Who will receive payment",
    )

    responsible: fhirtypes.ReferenceType = Field(
        None,
        alias="responsible",
        title=(
            "Type `Reference` referencing `Organization, Patient, Practitioner, "
            "PractitionerRole, RelatedPerson` (represented as `dict` in JSON)"
        ),
        description="Who will make payment",
    )

    securityLabelNumber: ListType[fhirtypes.UnsignedInt] = Field(
        None,
        alias="securityLabelNumber",
        title="List of `UnsignedInt` items (represented as `dict` in JSON)",
        description="Security Labels that define affected terms",
    )

    unitPrice: fhirtypes.MoneyType = Field(
        None,
        alias="unitPrice",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Contract Valued Item fee, charge, or cost",
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
    """ Context of the Contract term.
    The matter of concern in the context of this provision of the agrement.
    """

    resource_type = Field("ContractTermOffer", const=True)

    answer: ListType[fhirtypes.ContractTermOfferAnswerType] = Field(
        None,
        alias="answer",
        title=(
            "List of `ContractTermOfferAnswer` items (represented as `dict` in " "JSON)"
        ),
        description="Response to offer text",
    )

    decision: fhirtypes.CodeableConceptType = Field(
        None,
        alias="decision",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Accepting party choice",
    )

    decisionMode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="decisionMode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="How decision is conveyed",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Offer business ID",
    )

    linkId: ListType[fhirtypes.String] = Field(
        None,
        alias="linkId",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Pointer to text",
    )

    party: ListType[fhirtypes.ContractTermOfferPartyType] = Field(
        None,
        alias="party",
        title="List of `ContractTermOfferParty` items (represented as `dict` in JSON)",
        description="Offer Recipient",
    )

    securityLabelNumber: ListType[fhirtypes.UnsignedInt] = Field(
        None,
        alias="securityLabelNumber",
        title="List of `UnsignedInt` items (represented as `dict` in JSON)",
        description="Offer restriction numbers",
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Type `String` (represented as `dict` in JSON)",
        description="Human readable offer text",
    )

    topic: fhirtypes.ReferenceType = Field(
        None,
        alias="topic",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Negotiable offer asset",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Contract Offer Type or Form",
    )


class ContractTermOfferAnswer(backboneelement.BackboneElement):
    """ Response to offer text.
    """

    resource_type = Field("ContractTermOfferAnswer", const=True)

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="The actual answer response",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="Type `bool`",
        description="The actual answer response",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueCoding: fhirtypes.CodingType = Field(
        None,
        alias="valueCoding",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="The actual answer response",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueDate: fhirtypes.Date = Field(
        None,
        alias="valueDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="The actual answer response",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="valueDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="The actual answer response",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="valueDecimal",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="The actual answer response",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="The actual answer response",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="The actual answer response",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueReference",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="The actual answer response",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Type `String` (represented as `dict` in JSON)",
        description="The actual answer response",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueTime: fhirtypes.Time = Field(
        None,
        alias="valueTime",
        title="Type `Time` (represented as `dict` in JSON)",
        description="The actual answer response",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueUri: fhirtypes.Uri = Field(
        None,
        alias="valueUri",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="The actual answer response",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
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
    """ Offer Recipient.
    """

    resource_type = Field("ContractTermOfferParty", const=True)

    reference: ListType[fhirtypes.ReferenceType] = Field(
        ...,
        alias="reference",
        title=(
            "List of `Reference` items referencing `Patient, RelatedPerson, "
            "Practitioner, PractitionerRole, Device, Group, Organization` "
            "(represented as `dict` in JSON)"
        ),
        description="Referenced entity",
    )

    role: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="role",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Participant engagement type",
    )


class ContractTermSecurityLabel(backboneelement.BackboneElement):
    """ Protection for the Term.
    Security labels that protect the handling of information about the term and
    its elements, which may be specifically identified..
    """

    resource_type = Field("ContractTermSecurityLabel", const=True)

    category: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="category",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="Applicable Policy",
    )

    classification: fhirtypes.CodingType = Field(
        ...,
        alias="classification",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Confidentiality Protection",
    )

    control: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="control",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="Handling Instructions",
    )

    number: ListType[fhirtypes.UnsignedInt] = Field(
        None,
        alias="number",
        title="List of `UnsignedInt` items (represented as `dict` in JSON)",
        description="Link to Security Labels",
    )
