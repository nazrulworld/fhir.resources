from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ServiceRequest
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import domainresource, fhirtypes


class ServiceRequest(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A request for a service to be performed.
    A record of a request for service such as diagnostic investigations,
    treatments, or operations to be performed.
    """

    __resource_type__ = "ServiceRequest"

    asNeededBoolean: bool | None = Field(  # type: ignore
        None,
        alias="asNeededBoolean",
        title="Preconditions for service",
        description=(
            "If a CodeableConcept is present, it indicates the pre-condition for "
            'performing the service.  For example "pain", "on flare-up", etc.'
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e asNeeded[x]
            "one_of_many": "asNeeded",
            "one_of_many_required": False,
        },
    )
    asNeededBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_asNeededBoolean", title="Extension field for ``asNeededBoolean``."
    )

    asNeededCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="asNeededCodeableConcept",
        title="Preconditions for service",
        description=(
            "If a CodeableConcept is present, it indicates the pre-condition for "
            'performing the service.  For example "pain", "on flare-up", etc.'
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e asNeeded[x]
            "one_of_many": "asNeeded",
            "one_of_many_required": False,
        },
    )

    authoredOn: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="authoredOn",
        title="Date request signed",
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
            "enum_reference_types": ["CarePlan", "ServiceRequest", "MedicationRequest"],
        },
    )

    bodySite: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="bodySite",
        title="Location on Body",
        description=(
            "Anatomic location where the procedure should be performed. This is the"
            " target site."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    category: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="category",
        title="Classification of service",
        description=(
            "A code that classifies the service for searching, sorting and display "
            'purposes (e.g. "Surgical Procedure").'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title="What is being requested/ordered",
        description=(
            "A code that identifies a particular service (i.e., procedure, "
            "diagnostic investigation, or panel of investigations) that have been "
            "requested."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    doNotPerform: bool | None = Field(  # type: ignore
        None,
        alias="doNotPerform",
        title="True if service/procedure should not be performed",
        description=(
            "Set this to true if the record is saying that the service/procedure "
            "should NOT be performed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    doNotPerform__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_doNotPerform", title="Extension field for ``doNotPerform``."
    )

    encounter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="encounter",
        title="Encounter in which the request was created",
        description=(
            "An encounter that provides additional information about the healthcare"
            " context in which this request is made."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter"],
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Identifiers assigned to this order",
        description=(
            "Identifiers assigned to this order instance by the orderer and/or the "
            "receiver and/or order fulfiller."
        ),
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
            "ServiceRequest."
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
            " this ServiceRequest."
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
            "determinations that may be needed for delivering the requested "
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

    locationCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="locationCode",
        title="Requested location",
        description=(
            "The preferred location(s) where the procedure should actually happen "
            "in coded or free text form. E.g. at home or nursing day care center."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    locationReference: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="locationReference",
        title="Requested location",
        description=(
            "A reference to the the preferred location(s) where the procedure "
            "should actually happen. E.g. at home or nursing day care center."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="note",
        title="Comments",
        description=(
            "Any other notes and comments made about the service request. For "
            "example, internal billing notes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    occurrenceDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="occurrenceDateTime",
        title="When service should occur",
        description="The date/time at which the requested service should occur.",
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
        title="When service should occur",
        description="The date/time at which the requested service should occur.",
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
        title="When service should occur",
        description="The date/time at which the requested service should occur.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e occurrence[x]
            "one_of_many": "occurrence",
            "one_of_many_required": False,
        },
    )

    orderDetail: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="orderDetail",
        title="Additional order information",
        description=(
            "Additional details and instructions about the how the services are to "
            "be delivered.   For example, and order for a urinary catheter may have"
            " an order detail for an external or indwelling catheter, or an order "
            "for a bandage may require additional instructions specifying how the "
            "bandage should be applied."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    patientInstruction: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="patientInstruction",
        title="Patient or consumer-oriented instructions",
        description="Instructions in terms that are understood by the patient or consumer.",
        json_schema_extra={
            "element_property": True,
        },
    )
    patientInstruction__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_patientInstruction",
        title="Extension field for ``patientInstruction``.",
    )

    performer: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="performer",
        title="Requested performer",
        description=(
            "The desired performer for doing the requested service.  For example, "
            "the surgeon, dermatopathologist, endoscopist, etc."
        ),
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
        title="Performer role",
        description="Desired type of performer for doing the requested service.",
        json_schema_extra={
            "element_property": True,
        },
    )

    priority: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="priority",
        title="routine | urgent | asap | stat",
        description=(
            "Indicates how quickly the ServiceRequest should be addressed with "
            "respect to other requests."
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

    quantityQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantityQuantity",
        title="Service amount",
        description=(
            "An amount of service being requested which can be a quantity ( for "
            "example $1,500 home modification), a ratio ( for example, 20 half day "
            "visits per month), or a range (2.0 to 1.8 Gy per fraction)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e quantity[x]
            "one_of_many": "quantity",
            "one_of_many_required": False,
        },
    )

    quantityRange: fhirtypes.RangeType | None = Field(  # type: ignore
        None,
        alias="quantityRange",
        title="Service amount",
        description=(
            "An amount of service being requested which can be a quantity ( for "
            "example $1,500 home modification), a ratio ( for example, 20 half day "
            "visits per month), or a range (2.0 to 1.8 Gy per fraction)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e quantity[x]
            "one_of_many": "quantity",
            "one_of_many_required": False,
        },
    )

    quantityRatio: fhirtypes.RatioType | None = Field(  # type: ignore
        None,
        alias="quantityRatio",
        title="Service amount",
        description=(
            "An amount of service being requested which can be a quantity ( for "
            "example $1,500 home modification), a ratio ( for example, 20 half day "
            "visits per month), or a range (2.0 to 1.8 Gy per fraction)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e quantity[x]
            "one_of_many": "quantity",
            "one_of_many_required": False,
        },
    )

    reasonCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="reasonCode",
        title="Explanation/Justification for procedure or service",
        description=(
            "An explanation or justification for why this service is being "
            "requested in coded or textual form.   This is often for billing "
            "purposes.  May relate to the resources referred to in "
            "`supportingInfo`."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reasonReference: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="reasonReference",
        title="Explanation/Justification for service or service",
        description=(
            "Indicates another resource that provides a justification for why this "
            "service is being requested.   May relate to the resources referred to "
            "in `supportingInfo`."
        ),
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

    replaces: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="replaces",
        title="What request replaces",
        description=(
            "The request takes the place of the referenced completed or terminated "
            "request(s)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ServiceRequest"],
        },
    )

    requester: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="requester",
        title="Who/what is requesting service",
        description=(
            "The individual who initiated the request and has responsibility for "
            "its activation."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
                "Patient",
                "RelatedPerson",
                "Device",
            ],
        },
    )

    requisition: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="requisition",
        title="Composite Request ID",
        description=(
            "A shared identifier common to all service requests that were "
            "authorized more or less simultaneously by a single author, "
            "representing the composite or group identifier."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    specimen: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="specimen",
        title="Procedure Samples",
        description="One or more specimens that the laboratory procedure will use.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Specimen"],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title=(
            "draft | active | on-hold | revoked | completed | entered-in-error | "
            "unknown"
        ),
        description="The status of the order.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
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
        title="Individual or Entity the service is ordered for",
        description=(
            "On whom or what the service is to be performed. This is usually a "
            "human patient, but can also be requested on animals, groups of humans "
            "or animals, devices such as dialysis machines, or even locations "
            "(typically for environmental scans)."
        ),
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
            "Additional clinical information about the patient or specimen that may"
            " influence the services or their interpretations.     This information"
            " includes diagnosis, clinical findings and other observations.  In "
            'laboratory ordering these are typically referred to as "ask at order '
            'entry questions (AOEs)".  This includes observations explicitly '
            "requested by the producer (filler) to provide context or supporting "
            "information needed to complete the order. For example,  reporting the "
            "amount of inspired oxygen for blood gas measurements."
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
        ``ServiceRequest`` according specification,
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
            "replaces",
            "requisition",
            "status",
            "intent",
            "category",
            "priority",
            "doNotPerform",
            "code",
            "orderDetail",
            "quantityQuantity",
            "quantityRatio",
            "quantityRange",
            "subject",
            "encounter",
            "occurrenceDateTime",
            "occurrencePeriod",
            "occurrenceTiming",
            "asNeededBoolean",
            "asNeededCodeableConcept",
            "authoredOn",
            "requester",
            "performerType",
            "performer",
            "locationCode",
            "locationReference",
            "reasonCode",
            "reasonReference",
            "insurance",
            "supportingInfo",
            "specimen",
            "bodySite",
            "note",
            "patientInstruction",
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
        required_fields = [("intent", "intent__ext"), ("status", "status__ext")]
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
            "asNeeded": ["asNeededBoolean", "asNeededCodeableConcept"],
            "occurrence": [
                "occurrenceDateTime",
                "occurrencePeriod",
                "occurrenceTiming",
            ],
            "quantity": ["quantityQuantity", "quantityRange", "quantityRatio"],
        }
        return one_of_many_fields
