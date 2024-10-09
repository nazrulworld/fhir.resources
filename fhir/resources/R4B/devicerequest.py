from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceRequest
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class DeviceRequest(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Medical device request.
    Represents a request for a patient to employ a medical device. The device
    may be an implantable device, or an external assistive device, such as a
    walker.
    """

    __resource_type__ = "DeviceRequest"

    authoredOn: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="authoredOn",
        title="When recorded",
        description="When the request transitioned to being actionable.",
        json_schema_extra={
            "element_property": True,
        },
    )
    authoredOn__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_authoredOn", title="Extension field for ``authoredOn``."
    )

    basedOn: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="basedOn",
        title="What request fulfills",
        description="Plan/proposal/order fulfilled by this request.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    codeCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="codeCodeableConcept",
        title="Device requested",
        description="The details of the device to be used.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e code[x]
            "one_of_many": "code",
            "one_of_many_required": True,
        },
    )

    codeReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="codeReference",
        title="Device requested",
        description="The details of the device to be used.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e code[x]
            "one_of_many": "code",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Device"],
        },
    )

    encounter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="encounter",
        title="Encounter motivating request",
        description=(
            "An encounter that provides additional context in which this request is"
            " made."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter"],
        },
    )

    groupIdentifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="groupIdentifier",
        title="Identifier of composite request",
        description="Composite request this is part of.",
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="External Request identifier",
        description="Identifiers assigned to this order by the orderer or by the receiver.",
        json_schema_extra={
            "element_property": True,
        },
    )

    instantiatesCanonical: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="instantiatesCanonical",
        title="Instantiates FHIR protocol or definition",
        description=(
            "The URL pointing to a FHIR-defined protocol, guideline, orderset or "
            "other definition that is adhered to in whole or in part by this "
            "DeviceRequest."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ActivityDefinition", "PlanDefinition"],
        },
    )
    instantiatesCanonical__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_instantiatesCanonical",
        title="Extension field for ``instantiatesCanonical``.",
    )

    instantiatesUri: typing.List[fhirtypes.UriType | None] | None = Field(  # type: ignore
        None,
        alias="instantiatesUri",
        title="Instantiates external protocol or definition",
        description=(
            "The URL pointing to an externally maintained protocol, guideline, "
            "orderset or other definition that is adhered to in whole or in part by"
            " this DeviceRequest."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    instantiatesUri__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_instantiatesUri", title="Extension field for ``instantiatesUri``."
    )

    insurance: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="insurance",
        title="Associated insurance coverage",
        description=(
            "Insurance plans, coverage extensions, pre-authorizations and/or pre-"
            "determinations that may be required for delivering the requested "
            "service."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Coverage", "ClaimResponse"],
        },
    )

    intent: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="intent",
        title=(
            "proposal | plan | directive | order | original-order | reflex-order | "
            "filler-order | instance-order | option"
        ),
        description=(
            "Whether the request is a proposal, plan, an original order or a reflex"
            " order."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "proposal",
                "plan",
                "directive",
                "order",
                "original-order",
                "reflex-order",
                "filler-order",
                "instance-order",
                "option",
            ],
        },
    )
    intent__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_intent", title="Extension field for ``intent``."
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="note",
        title="Notes or comments",
        description=(
            "Details about this request that were not represented at all or "
            "sufficiently in one of the attributes provided in a class. These may "
            "include for example a comment, an instruction, or a note associated "
            "with the statement."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    occurrenceDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="occurrenceDateTime",
        title="Desired time or schedule for use",
        description=(
            "The timing schedule for the use of the device. The Schedule data type "
            'allows many different expressions, for example. "Every 8 hours"; '
            '"Three times a day"; "1/2 an hour before breakfast for 10 days from '
            '23-Dec 2011:"; "15 Oct 2013, 17 Oct 2013 and 1 Nov 2013".'
        ),
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
        title="Desired time or schedule for use",
        description=(
            "The timing schedule for the use of the device. The Schedule data type "
            'allows many different expressions, for example. "Every 8 hours"; '
            '"Three times a day"; "1/2 an hour before breakfast for 10 days from '
            '23-Dec 2011:"; "15 Oct 2013, 17 Oct 2013 and 1 Nov 2013".'
        ),
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
        title="Desired time or schedule for use",
        description=(
            "The timing schedule for the use of the device. The Schedule data type "
            'allows many different expressions, for example. "Every 8 hours"; '
            '"Three times a day"; "1/2 an hour before breakfast for 10 days from '
            '23-Dec 2011:"; "15 Oct 2013, 17 Oct 2013 and 1 Nov 2013".'
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e occurrence[x]
            "one_of_many": "occurrence",
            "one_of_many_required": False,
        },
    )

    parameter: typing.List[fhirtypes.DeviceRequestParameterType] | None = Field(  # type: ignore
        None,
        alias="parameter",
        title="Device details",
        description=(
            "Specific parameters for the ordered item.  For example, the prism "
            "value for lenses."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    performer: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="performer",
        title="Requested Filler",
        description="The desired performer for doing the diagnostic testing.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
                "CareTeam",
                "HealthcareService",
                "Patient",
                "Device",
                "RelatedPerson",
            ],
        },
    )

    performerType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="performerType",
        title="Filler role",
        description="Desired type of performer for doing the diagnostic testing.",
        json_schema_extra={
            "element_property": True,
        },
    )

    priorRequest: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="priorRequest",
        title="What request replaces",
        description=(
            "The request takes the place of the referenced completed or terminated "
            "request(s)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    priority: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="priority",
        title="routine | urgent | asap | stat",
        description=(
            "Indicates how quickly the {{title}} should be addressed with respect "
            "to other requests."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["routine", "urgent", "asap", "stat"],
        },
    )
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_priority", title="Extension field for ``priority``."
    )

    reasonCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="reasonCode",
        title="Coded Reason for request",
        description="Reason or justification for the use of this device.",
        json_schema_extra={
            "element_property": True,
        },
    )

    reasonReference: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="reasonReference",
        title="Linked Reason for request",
        description="Reason or justification for the use of this device.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Condition",
                "Observation",
                "DiagnosticReport",
                "DocumentReference",
            ],
        },
    )

    relevantHistory: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="relevantHistory",
        title="Request provenance",
        description="Key events in the history of the request.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Provenance"],
        },
    )

    requester: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="requester",
        title="Who/what is requesting diagnostics",
        description=(
            "The individual who initiated the request and has responsibility for "
            "its activation."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Device",
                "Practitioner",
                "PractitionerRole",
                "Organization",
            ],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title=(
            "draft | active | on-hold | revoked | completed | entered-in-error | "
            "unknown"
        ),
        description="The status of the request.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "draft",
                "active",
                "on-hold",
                "revoked",
                "completed",
                "entered-in-error",
                "unknown",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="subject",
        title="Focus of request",
        description="The patient who will use the device.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "Group", "Location", "Device"],
        },
    )

    supportingInfo: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="supportingInfo",
        title="Additional clinical information",
        description=(
            "Additional clinical information about the patient that may influence "
            "the request fulfilment.  For example, this may include where on the "
            "subject's body the device will be used (i.e. the target site)."
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
        ``DeviceRequest`` according specification,
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
            "instantiatesCanonical",
            "instantiatesUri",
            "basedOn",
            "priorRequest",
            "groupIdentifier",
            "status",
            "intent",
            "priority",
            "codeReference",
            "codeCodeableConcept",
            "parameter",
            "subject",
            "encounter",
            "occurrenceDateTime",
            "occurrencePeriod",
            "occurrenceTiming",
            "authoredOn",
            "requester",
            "performerType",
            "performer",
            "reasonCode",
            "reasonReference",
            "insurance",
            "supportingInfo",
            "note",
            "relevantHistory",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("intent", "intent__ext")]
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
        one_of_many_fields = {
            "code": ["codeCodeableConcept", "codeReference"],
            "occurrence": [
                "occurrenceDateTime",
                "occurrencePeriod",
                "occurrenceTiming",
            ],
        }
        return one_of_many_fields


class DeviceRequestParameter(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Device details.
    Specific parameters for the ordered item.  For example, the prism value for
    lenses.
    """

    __resource_type__ = "DeviceRequestParameter"

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Device detail",
        description="A code or string that identifies the device detail being asserted.",
        json_schema_extra={
            "element_property": True,
        },
    )

    valueBoolean: bool | None = Field(  # type: ignore
        None,
        alias="valueBoolean",
        title="Value of detail",
        description="The value of the device detail.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="valueCodeableConcept",
        title="Value of detail",
        description="The value of the device detail.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="valueQuantity",
        title="Value of detail",
        description="The value of the device detail.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueRange: fhirtypes.RangeType | None = Field(  # type: ignore
        None,
        alias="valueRange",
        title="Value of detail",
        description="The value of the device detail.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceRequestParameter`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "valueCodeableConcept",
            "valueQuantity",
            "valueRange",
            "valueBoolean",
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
                "valueBoolean",
                "valueCodeableConcept",
                "valueQuantity",
                "valueRange",
            ]
        }
        return one_of_many_fields
