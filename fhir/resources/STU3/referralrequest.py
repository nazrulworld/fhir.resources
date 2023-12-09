# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ReferralRequest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class ReferralRequest(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A request for referral or transfer of care.
    Used to record and send details about a request for referral service or
    transfer of a patient to the care of another provider or provider
    organization.
    """

    resource_type = Field("ReferralRequest", const=True)

    authoredOn: fhirtypes.DateTime = Field(
        None,
        alias="authoredOn",
        title="Date of creation/activation",
        description=(
            "Date/DateTime of creation for draft requests and date of activation "
            "for active requests."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    authoredOn__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_authoredOn", title="Extension field for ``authoredOn``."
    )

    basedOn: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="Request fulfilled by this request",
        description=(
            "Indicates any plans, proposals or orders that this request is intended"
            " to satisfy - in whole or in part."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ReferralRequest", "CarePlan", "ProcedureRequest"],
    )

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title="Originating encounter",
        description=(
            "The encounter at which the request for referral or transfer of care is"
            " initiated."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter", "EpisodeOfCare"],
    )

    definition: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="definition",
        title="Instantiates protocol or definition",
        description=(
            "A protocol, guideline, orderset or other definition that is adhered to"
            " in whole or in part by this request."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ActivityDefinition", "PlanDefinition"],
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="A textual description of the referral",
        description=(
            "The reason element gives a short description of why the referral is "
            "being made, the description expands on this to support a more complete"
            " clinical summary."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    groupIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="groupIdentifier",
        title="Composite request this is part of",
        description=(
            'The business identifier of the logical "grouping" request/order that '
            "this referral is a part of."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier",
        description=(
            "Business identifier that uniquely identifies the referral/care "
            "transfer request instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    intent: fhirtypes.Code = Field(
        None,
        alias="intent",
        title="proposal | plan | order",
        description=(
            'Distinguishes the "level" of authorization/demand implicit in this '
            "request."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["proposal", "plan", "order"],
    )
    intent__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_intent", title="Extension field for ``intent``."
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Comments made about referral request",
        description="Comments made about the referral request by any of the participants.",
        # if property is element of this resource.
        element_property=True,
    )

    occurrenceDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurrenceDateTime",
        title="When the service(s) requested in the referral should occur",
        description=(
            "The period of time within which the services identified in the "
            "referral/transfer of care is specified or required to occur."
        ),
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
        title="When the service(s) requested in the referral should occur",
        description=(
            "The period of time within which the services identified in the "
            "referral/transfer of care is specified or required to occur."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )

    priority: fhirtypes.Code = Field(
        None,
        alias="priority",
        title="Urgency of referral / transfer of care request",
        description=(
            "An indication of the urgency of referral (or where applicable the type"
            " of transfer of care) request."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_priority", title="Extension field for ``priority``."
    )

    reasonCode: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="Reason for referral / transfer of care request",
        description=(
            "Description of clinical condition indicating why referral/transfer of "
            "care is requested.  For example:  Pathological Anomalies, Disabled "
            "(physical or mental),  Behavioral Management."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    reasonReference: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title="Why is service needed?",
        description="Indicates another resource whose existence justifies this request.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Condition", "Observation"],
    )

    recipient: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="recipient",
        title="Receiver of referral / transfer of care request",
        description=(
            "The healthcare provider(s) or provider organization(s) who/which is to"
            " receive the referral/transfer of care request."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Organization", "HealthcareService"],
    )

    relevantHistory: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="relevantHistory",
        title="Key events in history of request",
        description=(
            "Links to Provenance records for past versions of this resource or "
            "fulfilling request or event resources that identify key state "
            "transitions or updates that are likely to be relevant to a user "
            "looking at the current version of the resource."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Provenance"],
    )

    replaces: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="replaces",
        title="Request(s) replaced by this request",
        description=(
            "Completed or terminated request(s) whose function is taken by this new"
            " request."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ReferralRequest"],
    )

    requester: fhirtypes.ReferralRequestRequesterType = Field(
        None,
        alias="requester",
        title="Who/what is requesting service",
        description=(
            "The individual who initiated the request and has responsibility for "
            "its activation."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    serviceRequested: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="serviceRequested",
        title="Actions requested as part of the referral",
        description=(
            "The service(s) that is/are requested to be provided to the patient.  "
            "For example: cardiac pacemaker insertion."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    specialty: fhirtypes.CodeableConceptType = Field(
        None,
        alias="specialty",
        title="The clinical specialty (discipline) that the referral is requested for",
        description=(
            "Indication of the clinical domain or discipline to which the referral "
            "or transfer of care request is sent.  For example: Cardiology "
            "Gastroenterology Diabetology."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title=(
            "draft | active | suspended | cancelled | completed | entered-in-error "
            "| unknown"
        ),
        description=(
            "The status of the authorization/intention reflected by the referral "
            "request record."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "draft",
            "active",
            "suspended",
            "cancelled",
            "completed",
            "entered-in-error",
            "unknown",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Patient referred to care or transfer",
        description=(
            "The patient who is the subject of a referral or transfer of care "
            "request."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group"],
    )

    supportingInfo: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingInfo",
        title="Additonal information to support referral or transfer of care request",
        description=(
            "Any additional (administrative, financial or clinical) information "
            "required to support request for referral or transfer of care.  For "
            "example: Presenting problems/chief complaints Medical History Family "
            "History Alerts Allergy/Intolerance and Adverse Reactions Medications "
            "Observations/Assessments (may include cognitive and fundtional "
            "assessments) Diagnostic Reports Care Plan."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Referral/Transition of care request type",
        description=(
            "An indication of the type of referral (or where applicable the type of"
            " transfer of care) request."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ReferralRequest`` according specification,
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
            "definition",
            "basedOn",
            "replaces",
            "groupIdentifier",
            "status",
            "intent",
            "type",
            "priority",
            "serviceRequested",
            "subject",
            "context",
            "occurrenceDateTime",
            "occurrencePeriod",
            "authoredOn",
            "requester",
            "specialty",
            "recipient",
            "reasonCode",
            "reasonReference",
            "description",
            "supportingInfo",
            "note",
            "relevantHistory",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1762(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("intent", "intent__ext"), ("status", "status__ext")]
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1762(
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
        one_of_many_fields = {"occurrence": ["occurrenceDateTime", "occurrencePeriod"]}
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


class ReferralRequestRequester(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who/what is requesting service.
    The individual who initiated the request and has responsibility for its
    activation.
    """

    resource_type = Field("ReferralRequestRequester", const=True)

    agent: fhirtypes.ReferenceType = Field(
        ...,
        alias="agent",
        title="Individual making the request",
        description="The device, practitioner, etc. who initiated the request.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "Organization",
            "Patient",
            "RelatedPerson",
            "Device",
        ],
    )

    onBehalfOf: fhirtypes.ReferenceType = Field(
        None,
        alias="onBehalfOf",
        title="Organization agent is acting for",
        description="The organization the device or practitioner was acting on behalf of.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ReferralRequestRequester`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "agent", "onBehalfOf"]
