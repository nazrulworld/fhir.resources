# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Contract
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Contract(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Legal Agreement.
    A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.
    """

    resource_type = Field("Contract", const=True)

    action: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="action",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Action stipulated by this Contract",
    )

    actionReason: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="actionReason",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Rationale for the stiplulated action",
    )

    agent: ListType[fhirtypes.ContractAgentType] = Field(
        None,
        alias="agent",
        title="List of `ContractAgent` items (represented as `dict` in JSON)",
        description="Entity being ascribed responsibility",
    )

    applies: fhirtypes.PeriodType = Field(
        None,
        alias="applies",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Effective time",
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

    bindingAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="bindingAttachment",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="Binding Contract",
        one_of_many="binding",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    bindingReference: fhirtypes.ReferenceType = Field(
        None,
        alias="bindingReference",
        title=(
            "Type `Reference` referencing `Composition, DocumentReference, "
            "QuestionnaireResponse` (represented as `dict` in JSON)"
        ),
        description="Binding Contract",
        one_of_many="binding",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    contentDerivative: fhirtypes.CodeableConceptType = Field(
        None,
        alias="contentDerivative",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Content derived from the basal information",
    )

    decisionType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="decisionType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Decision by Grantor",
    )

    domain: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="domain",
        title=(
            "List of `Reference` items referencing `Location` (represented as "
            "`dict` in JSON)"
        ),
        description="Domain in which this Contract applies",
    )

    friendly: ListType[fhirtypes.ContractFriendlyType] = Field(
        None,
        alias="friendly",
        title="List of `ContractFriendly` items (represented as `dict` in JSON)",
        description="Contract Friendly Language",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Contract number",
    )

    issued: fhirtypes.DateTime = Field(
        None,
        alias="issued",
        title="Type `DateTime`",
        description="When this Contract was issued",
    )
    issued__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_issued", title="Extension field for ``issued``."
    )

    legal: ListType[fhirtypes.ContractLegalType] = Field(
        None,
        alias="legal",
        title="List of `ContractLegal` items (represented as `dict` in JSON)",
        description="Contract Legal Language",
    )

    rule: ListType[fhirtypes.ContractRuleType] = Field(
        None,
        alias="rule",
        title="List of `ContractRule` items (represented as `dict` in JSON)",
        description="Computable Contract Language",
    )

    securityLabel: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="securityLabel",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="Security Labels that define affected resources",
    )

    signer: ListType[fhirtypes.ContractSignerType] = Field(
        None,
        alias="signer",
        title="List of `ContractSigner` items (represented as `dict` in JSON)",
        description="Contract Signatory",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code`",
        description=(
            "amended | appended | cancelled | disputed | entered-in-error | "
            "executable | executed | negotiable | offered | policy | rejected | "
            "renewed | revoked | resolved | terminated"
        ),
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
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

    term: ListType[fhirtypes.ContractTermType] = Field(
        None,
        alias="term",
        title="List of `ContractTerm` items (represented as `dict` in JSON)",
        description="Contract Term List",
    )

    topic: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="topic",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="Context of the Contract",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type or form",
    )

    valuedItem: ListType[fhirtypes.ContractValuedItemType] = Field(
        None,
        alias="valuedItem",
        title="List of `ContractValuedItem` items (represented as `dict` in JSON)",
        description="Contract Valued Item List",
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
        one_of_many_fields = {"binding": ["bindingAttachment", "bindingReference"]}
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


class ContractAgent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Entity being ascribed responsibility.
    An actor taking a role in an activity for which it can be assigned some
    degree of responsibility for the activity taking place.
    """

    resource_type = Field("ContractAgent", const=True)

    actor: fhirtypes.ReferenceType = Field(
        ...,
        alias="actor",
        title=(
            "Type `Reference` referencing `Contract, Device, Group, Location, "
            "Organization, Patient, Practitioner, RelatedPerson, Substance` "
            "(represented as `dict` in JSON)"
        ),
        description="Contract Agent Type",
    )

    role: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="role",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Role type of the agent",
    )


class ContractFriendly(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Contract Legal Language.
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Computable Contract Language.
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
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
        title=(
            "Type `Reference` referencing `Organization, Patient, Practitioner, "
            "RelatedPerson` (represented as `dict` in JSON)"
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Contract Term List.
    One or more Contract Provisions, which may be related and conveyed as a
    group, and may contain nested groups.
    """

    resource_type = Field("ContractTerm", const=True)

    action: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="action",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Contract Term Activity",
    )

    actionReason: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="actionReason",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Purpose for the Contract Term Action",
    )

    agent: ListType[fhirtypes.ContractTermAgentType] = Field(
        None,
        alias="agent",
        title="List of `ContractTermAgent` items (represented as `dict` in JSON)",
        description="Contract Term Agent List",
    )

    applies: fhirtypes.PeriodType = Field(
        None,
        alias="applies",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Contract Term Effective Time",
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
        title="Type `DateTime`",
        description="Contract Term Issue Date Time",
    )
    issued__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_issued", title="Extension field for ``issued``."
    )

    securityLabel: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="securityLabel",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="Security Labels that define affected terms",
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
        title="Type `String`",
        description="Human readable Contract term text",
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )

    topic: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="topic",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="Context of the Contract term",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Contract Term Type or Form",
    )

    valuedItem: ListType[fhirtypes.ContractTermValuedItemType] = Field(
        None,
        alias="valuedItem",
        title="List of `ContractTermValuedItem` items (represented as `dict` in JSON)",
        description="Contract Term Valued Item List",
    )


class ContractTermAgent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Contract Term Agent List.
    An actor taking a role in an activity for which it can be assigned some
    degree of responsibility for the activity taking place.
    """

    resource_type = Field("ContractTermAgent", const=True)

    actor: fhirtypes.ReferenceType = Field(
        ...,
        alias="actor",
        title=(
            "Type `Reference` referencing `Contract, Device, Group, Location, "
            "Organization, Patient, Practitioner, RelatedPerson, Substance` "
            "(represented as `dict` in JSON)"
        ),
        description="Contract Term Agent Subject",
    )

    role: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="role",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Type of the Contract Term Agent",
    )


class ContractTermValuedItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Contract Term Valued Item List.
    Contract Provision Valued Item List.
    """

    resource_type = Field("ContractTermValuedItem", const=True)

    effectiveTime: fhirtypes.DateTime = Field(
        None,
        alias="effectiveTime",
        title="Type `DateTime`",
        description="Contract Term Valued Item Effective Tiem",
    )
    effectiveTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_effectiveTime", title="Extension field for ``effectiveTime``."
    )

    entityCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="entityCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Contract Term Valued Item Type",
        one_of_many="entity",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    entityReference: fhirtypes.ReferenceType = Field(
        None,
        alias="entityReference",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Contract Term Valued Item Type",
        one_of_many="entity",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    factor: fhirtypes.Decimal = Field(
        None,
        alias="factor",
        title="Type `Decimal`",
        description="Contract Term Valued Item Price Scaling Factor",
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_factor", title="Extension field for ``factor``."
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Contract Term Valued Item Number",
    )

    net: fhirtypes.MoneyType = Field(
        None,
        alias="net",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Total Contract Term Valued Item Value",
    )

    points: fhirtypes.Decimal = Field(
        None,
        alias="points",
        title="Type `Decimal`",
        description="Contract Term Valued Item Difficulty Scaling Factor",
    )
    points__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_points", title="Extension field for ``points``."
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Contract Term Valued Item Count",
    )

    unitPrice: fhirtypes.MoneyType = Field(
        None,
        alias="unitPrice",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Contract Term Valued Item fee, charge, or cost",
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


class ContractValuedItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Contract Valued Item List.
    """

    resource_type = Field("ContractValuedItem", const=True)

    effectiveTime: fhirtypes.DateTime = Field(
        None,
        alias="effectiveTime",
        title="Type `DateTime`",
        description="Contract Valued Item Effective Tiem",
    )
    effectiveTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_effectiveTime", title="Extension field for ``effectiveTime``."
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
        title="Type `Decimal`",
        description="Contract Valued Item Price Scaling Factor",
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_factor", title="Extension field for ``factor``."
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Contract Valued Item Number",
    )

    net: fhirtypes.MoneyType = Field(
        None,
        alias="net",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Total Contract Valued Item Value",
    )

    points: fhirtypes.Decimal = Field(
        None,
        alias="points",
        title="Type `Decimal`",
        description="Contract Valued Item Difficulty Scaling Factor",
    )
    points__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_points", title="Extension field for ``points``."
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Count of Contract Valued Items",
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
