# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EpisodeOfCare
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


class EpisodeOfCare(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An association of a Patient with an Organization and  Healthcare
    Provider(s) for a period of time that the Organization assumes some level
    of responsibility.
    An association between a patient and an organization / healthcare
    provider(s) during which time encounters may occur. The managing
    organization assumes a level of responsibility for the patient during this
    time.
    """

    resource_type = Field("EpisodeOfCare", const=True)

    account: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="account",
        title=(
            "The set of accounts that may be used for billing for this " "EpisodeOfCare"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Account"],
    )

    careManager: fhirtypes.ReferenceType = Field(
        None,
        alias="careManager",
        title="Care manager/care coordinator for the patient",
        description=(
            "The practitioner that is the care manager/care coordinator for this "
            "patient."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "PractitionerRole"],
    )

    careTeam: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="careTeam",
        title="Other practitioners facilitating this episode of care",
        description=(
            "The list of practitioners that may be facilitating this episode of "
            "care for specific purposes."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["CareTeam"],
    )

    diagnosis: typing.List[fhirtypes.EpisodeOfCareDiagnosisType] = Field(
        None,
        alias="diagnosis",
        title=(
            "The list of medical conditions that were addressed during the episode "
            "of care"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier(s) relevant for this EpisodeOfCare",
        description=(
            "The EpisodeOfCare may be known by different identifiers for different "
            "contexts of use, such as when an external agency is tracking the "
            "Episode for funding purposes."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    managingOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="managingOrganization",
        title="Organization that assumes responsibility for care coordination",
        description=(
            "The organization that has assumed the specific responsibilities for "
            "care coordination, care delivery, or other services for the specified "
            "duration."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="The patient who is the focus of this episode of care",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Interval during responsibility is assumed",
        description=(
            "The interval during which the managing organization assumes the "
            "defined responsibility."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    reason: typing.List[fhirtypes.EpisodeOfCareReasonType] = Field(
        None,
        alias="reason",
        title=(
            "The list of medical reasons that are expected to be addressed during "
            "the episode of care"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    referralRequest: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="referralRequest",
        title="Originating Referral Request(s)",
        description=(
            "Referral Request(s) that are fulfilled by this EpisodeOfCare, incoming"
            " referrals."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ServiceRequest"],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title=(
            "planned | waitlist | active | onhold | finished | cancelled | entered-"
            "in-error"
        ),
        description="planned | waitlist | active | onhold | finished | cancelled.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "planned",
            "waitlist",
            "active",
            "onhold",
            "finished",
            "cancelled",
            "entered-in-error",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    statusHistory: typing.List[fhirtypes.EpisodeOfCareStatusHistoryType] = Field(
        None,
        alias="statusHistory",
        title=(
            "Past list of status codes (the current status may be included to cover"
            " the start date of the status)"
        ),
        description=(
            "The history of statuses that the EpisodeOfCare has been through "
            "(without requiring processing the history of the resource)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="Type/class  - e.g. specialist referral, disease management",
        description=(
            "A classification of the type of episode of care; e.g. specialist "
            "referral, disease management, type of funded care."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EpisodeOfCare`` according specification,
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
            "statusHistory",
            "type",
            "reason",
            "diagnosis",
            "patient",
            "managingOrganization",
            "period",
            "referralRequest",
            "careManager",
            "careTeam",
            "account",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1443(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
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


class EpisodeOfCareDiagnosis(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The list of medical conditions that were addressed during the episode of
    care.
    """

    resource_type = Field("EpisodeOfCareDiagnosis", const=True)

    condition: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="condition",
        title="The medical condition that was addressed during the episode of care",
        description=(
            "The medical condition that was addressed during the episode of care, "
            "expressed as a text, code or a reference to another resource."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Condition"],
    )

    use: fhirtypes.CodeableConceptType = Field(
        None,
        alias="use",
        title=(
            "Role that this diagnosis has within the episode of care (e.g. "
            "admission, billing, discharge \u2026)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EpisodeOfCareDiagnosis`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "condition", "use"]


class EpisodeOfCareReason(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The list of medical reasons that are expected to be addressed during the
    episode of care.
    """

    resource_type = Field("EpisodeOfCareReason", const=True)

    use: fhirtypes.CodeableConceptType = Field(
        None,
        alias="use",
        title="What the reason value should be used for/as",
        description=(
            "What the reason value should be used as e.g. Chief Complaint, Health "
            "Concern, Health Maintenance (including screening)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    value: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="value",
        title="Medical reason to be addressed",
        description=(
            "The medical reason that is expected to be addressed during the episode"
            " of care, expressed as a text, code or a reference to another "
            "resource."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Condition",
            "Procedure",
            "Observation",
            "HealthcareService",
        ],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EpisodeOfCareReason`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "use", "value"]


class EpisodeOfCareStatusHistory(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Past list of status codes (the current status may be included to cover the
    start date of the status).
    The history of statuses that the EpisodeOfCare has been through (without
    requiring processing the history of the resource).
    """

    resource_type = Field("EpisodeOfCareStatusHistory", const=True)

    period: fhirtypes.PeriodType = Field(
        ...,
        alias="period",
        title="Duration the EpisodeOfCare was in the specified status",
        description="The period during this EpisodeOfCare that the specific status applied.",
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title=(
            "planned | waitlist | active | onhold | finished | cancelled | entered-"
            "in-error"
        ),
        description="planned | waitlist | active | onhold | finished | cancelled.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "planned",
            "waitlist",
            "active",
            "onhold",
            "finished",
            "cancelled",
            "entered-in-error",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EpisodeOfCareStatusHistory`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "status", "period"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2861(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
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
