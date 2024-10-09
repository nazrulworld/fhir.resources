from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Permission
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Permission(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Access Rules.
    Permission resource holds access rules for a given data and context.
    """

    __resource_type__ = "Permission"

    asserter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="asserter",
        title="The person or entity that asserts the permission",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
                "CareTeam",
                "Patient",
                "RelatedPerson",
                "HealthcareService",
            ],
        },
    )

    combining: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="combining",
        title=(
            "deny-overrides | permit-overrides | ordered-deny-overrides | ordered-"
            "permit-overrides | deny-unless-permit | permit-unless-deny"
        ),
        description=(
            "Defines a procedure for arriving at an access decision given the set "
            "of rules."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "deny-overrides",
                "permit-overrides",
                "ordered-deny-overrides",
                "ordered-permit-overrides",
                "deny-unless-permit",
                "permit-unless-deny",
            ],
        },
    )
    combining__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_combining", title="Extension field for ``combining``."
    )

    date: typing.List[fhirtypes.DateTimeType | None] | None = Field(  # type: ignore
        None,
        alias="date",
        title="The date that permission was asserted",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    justification: fhirtypes.PermissionJustificationType | None = Field(  # type: ignore
        None,
        alias="justification",
        title="The asserted justification for using the data",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    rule: typing.List[fhirtypes.PermissionRuleType] | None = Field(  # type: ignore
        None,
        alias="rule",
        title="Constraints to the Permission",
        description="A set of rules.",
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="active | entered-in-error | draft | rejected",
        description="Status.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["active", "entered-in-error", "draft", "rejected"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    validity: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="validity",
        title="The period in which the permission is active",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Permission`` according specification,
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
            "status",
            "asserter",
            "date",
            "validity",
            "justification",
            "combining",
            "rule",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("combining", "combining__ext"), ("status", "status__ext")]
        return required_fields


class PermissionJustification(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The asserted justification for using the data.
    """

    __resource_type__ = "PermissionJustification"

    basis: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="basis",
        title="The regulatory grounds upon which this Permission builds",
        description=(
            "This would be a codeableconcept, or a coding, which can be constrained"
            " to , for example, the 6 grounds for processing in GDPR."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    evidence: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="evidence",
        title="Justifing rational",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PermissionJustification`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "basis", "evidence"]


class PermissionRule(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Constraints to the Permission.
    A set of rules.
    """

    __resource_type__ = "PermissionRule"

    activity: typing.List[fhirtypes.PermissionRuleActivityType] | None = Field(  # type: ignore
        None,
        alias="activity",
        title=(
            "A description or definition of which activities are allowed to be done"
            " on the data"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    data: typing.List[fhirtypes.PermissionRuleDataType] | None = Field(  # type: ignore
        None,
        alias="data",
        title=(
            "The selection criteria to identify data that is within scope of this "
            "provision"
        ),
        description=(
            "A description or definition of which activities are allowed to be done"
            " on the data."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    limit: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="limit",
        title="What limits apply to the use of the data",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="deny | permit",
        description=None,
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
        ``PermissionRule`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "data",
            "activity",
            "limit",
        ]


class PermissionRuleActivity(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A description or definition of which activities are allowed to be done on
    the data.
    """

    __resource_type__ = "PermissionRuleActivity"

    action: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="action",
        title="Actions controlled by this rule",
        description="Actions controlled by this Rule.",
        json_schema_extra={
            "element_property": True,
        },
    )

    actor: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="actor",
        title="Authorized actor(s)",
        description="The actor(s) authorized for the defined activity.",
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

    purpose: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="purpose",
        title="The purpose for which the permission is given",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PermissionRuleActivity`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "actor", "action", "purpose"]


class PermissionRuleData(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The selection criteria to identify data that is within scope of this
    provision.
    A description or definition of which activities are allowed to be done on
    the data.
    """

    __resource_type__ = "PermissionRuleData"

    expression: fhirtypes.ExpressionType | None = Field(  # type: ignore
        None,
        alias="expression",
        title="Expression identifying the data",
        description="Used when other data selection elements are insufficient.",
        json_schema_extra={
            "element_property": True,
        },
    )

    period: typing.List[fhirtypes.PeriodType] | None = Field(  # type: ignore
        None,
        alias="period",
        title="Timeframe encompasing data create/update",
        description=(
            "Clinical or Operational Relevant period of time that bounds the data "
            "controlled by this rule."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    resource: typing.List[fhirtypes.PermissionRuleDataResourceType] | None = Field(  # type: ignore
        None,
        alias="resource",
        title="Explicit FHIR Resource references",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    security: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        None,
        alias="security",
        title="Security tag code on .meta.security",
        description=(
            "The data in scope are those with the given codes present in that data "
            ".meta.security element."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PermissionRuleData`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "resource",
            "security",
            "period",
            "expression",
        ]


class PermissionRuleDataResource(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Explicit FHIR Resource references.
    """

    __resource_type__ = "PermissionRuleDataResource"

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
        ``PermissionRuleDataResource`` according specification,
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
