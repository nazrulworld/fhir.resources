# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Permission
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class Permission(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Access Rules.
    Permission resource holds access rules for a given data and context.
    """

    resource_type = Field("Permission", const=True)

    asserter: fhirtypes.ReferenceType = Field(
        None,
        alias="asserter",
        title="The person or entity that asserts the permission",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "Organization",
            "CareTeam",
            "Patient",
            "RelatedPerson",
            "HealthcareService",
        ],
    )

    combining: fhirtypes.Code = Field(
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
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "deny-overrides",
            "permit-overrides",
            "ordered-deny-overrides",
            "ordered-permit-overrides",
            "deny-unless-permit",
            "permit-unless-deny",
        ],
    )
    combining__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_combining", title="Extension field for ``combining``."
    )

    date: typing.List[typing.Optional[fhirtypes.DateTime]] = Field(
        None,
        alias="date",
        title="The date that permission was asserted",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_date", title="Extension field for ``date``.")

    justification: fhirtypes.PermissionJustificationType = Field(
        None,
        alias="justification",
        title="The asserted justification for using the data",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    rule: typing.List[fhirtypes.PermissionRuleType] = Field(
        None,
        alias="rule",
        title="Constraints to the Permission",
        description="A set of rules.",
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="active | entered-in-error | draft | rejected",
        description="Status.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "entered-in-error", "draft", "rejected"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    validity: fhirtypes.PeriodType = Field(
        None,
        alias="validity",
        title="The period in which the permission is active",
        description=None,
        # if property is element of this resource.
        element_property=True,
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1255(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("combining", "combining__ext"), ("status", "status__ext")]
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


class PermissionJustification(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The asserted justification for using the data.
    """

    resource_type = Field("PermissionJustification", const=True)

    basis: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="basis",
        title="The regulatory grounds upon which this Permission builds",
        description=(
            "This would be a codeableconcept, or a coding, which can be constrained"
            " to , for example, the 6 grounds for processing in GDPR."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    evidence: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="evidence",
        title="Justifing rational",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
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

    resource_type = Field("PermissionRule", const=True)

    activity: typing.List[fhirtypes.PermissionRuleActivityType] = Field(
        None,
        alias="activity",
        title=(
            "A description or definition of which activities are allowed to be done"
            " on the data"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    data: typing.List[fhirtypes.PermissionRuleDataType] = Field(
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
        # if property is element of this resource.
        element_property=True,
    )

    limit: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="limit",
        title="What limits apply to the use of the data",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="deny | permit",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["deny", "permit"],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    resource_type = Field("PermissionRuleActivity", const=True)

    action: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="action",
        title="Actions controlled by this rule",
        description="Actions controlled by this Rule.",
        # if property is element of this resource.
        element_property=True,
    )

    actor: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="actor",
        title="Authorized actor(s)",
        description="The actor(s) authorized for the defined activity.",
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

    purpose: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="purpose",
        title="The purpose for which the permission is given",
        description=None,
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("PermissionRuleData", const=True)

    expression: fhirtypes.ExpressionType = Field(
        None,
        alias="expression",
        title="Expression identifying the data",
        description="Used when other data selection elements are insufficient.",
        # if property is element of this resource.
        element_property=True,
    )

    period: typing.List[fhirtypes.PeriodType] = Field(
        None,
        alias="period",
        title="Timeframe encompasing data create/update",
        description=(
            "Clinical or Operational Relevant period of time that bounds the data "
            "controlled by this rule."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    resource: typing.List[fhirtypes.PermissionRuleDataResourceType] = Field(
        None,
        alias="resource",
        title="Explicit FHIR Resource references",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    security: typing.List[fhirtypes.CodingType] = Field(
        None,
        alias="security",
        title="Security tag code on .meta.security",
        description=(
            "The data in scope are those with the given codes present in that data "
            ".meta.security element."
        ),
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("PermissionRuleDataResource", const=True)

    meaning: fhirtypes.Code = Field(
        None,
        alias="meaning",
        title="instance | related | dependents | authoredby",
        description=(
            "How the resource reference is interpreted when testing consent "
            "restrictions."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
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

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PermissionRuleDataResource`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "meaning", "reference"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2872(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("meaning", "meaning__ext")]
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
