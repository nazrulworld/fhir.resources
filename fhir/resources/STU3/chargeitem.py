from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ChargeItem
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ChargeItem(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Item containing charge code(s) associated with the provision of healthcare
    provider products.
    The resource ChargeItem describes the provision of healthcare provider
    products for a certain patient, therefore referring not only to the
    product, but containing in addition details of the provision, like date,
    time, amounts and participating organizations and persons. Main Usage of
    the ChargeItem is to enable the billing process and internal cost
    allocation.
    """

    __resource_type__ = "ChargeItem"

    account: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="account",
        title="Account to place this charge",
        description="Account into which this ChargeItems belongs.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Account"],
        },
    )

    bodysite: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="bodysite",
        title="Anatomical location, if relevant",
        description="The anatomical location where the related service has been applied.",
        json_schema_extra={
            "element_property": True,
        },
    )

    code: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="code",
        title="A code that identifies the charge, like a billing code",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    context: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="context",
        title="Encounter / Episode associated with event",
        description=(
            "The encounter or episode of care that establishes the context for this"
            " event."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter", "EpisodeOfCare"],
        },
    )

    definition: typing.List[fhirtypes.UriType | None] | None = Field(  # type: ignore
        None,
        alias="definition",
        title="Defining information about the code of this charge item",
        description=(
            "References the source of pricing information, rules of application for"
            " the code this ChargeItem uses."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    definition__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_definition", title="Extension field for ``definition``."
    )

    enteredDate: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="enteredDate",
        title="Date the charge item was entered",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    enteredDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_enteredDate", title="Extension field for ``enteredDate``."
    )

    enterer: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="enterer",
        title="Individual who was entering",
        description="The device, practitioner, etc. who entered the charge item.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "Organization",
                "Patient",
                "Device",
                "RelatedPerson",
            ],
        },
    )

    factorOverride: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="factorOverride",
        title="Factor overriding the associated rules",
        description=(
            "Factor overriding the factor determined by the rules associated with "
            "the code."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    factorOverride__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_factorOverride", title="Extension field for ``factorOverride``."
    )

    identifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business Identifier for item",
        description="Identifiers assigned to this event performer or other systems.",
        json_schema_extra={
            "element_property": True,
        },
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="note",
        title="Comments made about the ChargeItem",
        description=(
            "Comments made about the event by the performer, subject or other "
            "participants."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    occurrenceDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="occurrenceDateTime",
        title="When the charged service was applied",
        description="Date/time(s) or duration when the charged service was applied.",
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
        title="When the charged service was applied",
        description="Date/time(s) or duration when the charged service was applied.",
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
        title="When the charged service was applied",
        description="Date/time(s) or duration when the charged service was applied.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e occurrence[x]
            "one_of_many": "occurrence",
            "one_of_many_required": False,
        },
    )

    overrideReason: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="overrideReason",
        title="Reason for overriding the list price/factor",
        description=(
            "If the list price or the rule based factor associated with the code is"
            " overridden, this attribute can capture a text to indicate the  reason"
            " for this action."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    overrideReason__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_overrideReason", title="Extension field for ``overrideReason``."
    )

    partOf: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="partOf",
        title="Part of referenced ChargeItem",
        description=(
            "ChargeItems can be grouped to larger ChargeItems covering the whole "
            "set."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ChargeItem"],
        },
    )

    participant: typing.List[fhirtypes.ChargeItemParticipantType] | None = Field(  # type: ignore
        None,
        alias="participant",
        title="Who performed charged service",
        description=(
            "Indicates who or what performed or participated in the charged " "service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    performingOrganization: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="performingOrganization",
        title="Organization providing the charged sevice",
        description="The organization requesting the service.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    priceOverride: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="priceOverride",
        title="Price overriding the associated rules",
        description=(
            "Total price of the charge overriding the list price associated with "
            "the code."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="Quantity of which the charge item has been serviced",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    reason: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="reason",
        title="Why was the charged  service rendered?",
        description="Describes why the event occurred in coded or textual form.",
        json_schema_extra={
            "element_property": True,
        },
    )

    requestingOrganization: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="requestingOrganization",
        title="Organization requesting the charged service",
        description="The organization performing the service.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    service: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="service",
        title="Which rendered service is being charged?",
        description="Indicated the rendered service that caused this charge.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "DiagnosticReport",
                "ImagingStudy",
                "Immunization",
                "MedicationAdministration",
                "MedicationDispense",
                "Observation",
                "Procedure",
                "SupplyDelivery",
            ],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title=(
            "planned | billable | not-billable | aborted | billed | entered-in-"
            "error | unknown"
        ),
        description="The current state of the ChargeItem.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "planned",
                "billable",
                "not-billable",
                "aborted",
                "billed",
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
        title="Individual service was done for/to",
        description=(
            "The individual or set of individuals the action is being or was "
            "performed on."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "Group"],
        },
    )

    supportingInformation: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="supportingInformation",
        title="Further information supporting the this charge",
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
        ``ChargeItem`` according specification,
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
            "status",
            "partOf",
            "code",
            "subject",
            "context",
            "occurrenceDateTime",
            "occurrencePeriod",
            "occurrenceTiming",
            "participant",
            "performingOrganization",
            "requestingOrganization",
            "quantity",
            "bodysite",
            "factorOverride",
            "priceOverride",
            "overrideReason",
            "enterer",
            "enteredDate",
            "reason",
            "service",
            "account",
            "note",
            "supportingInformation",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
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
            "occurrence": ["occurrenceDateTime", "occurrencePeriod", "occurrenceTiming"]
        }
        return one_of_many_fields


class ChargeItemParticipant(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who performed charged service.
    Indicates who or what performed or participated in the charged service.
    """

    __resource_type__ = "ChargeItemParticipant"

    actor: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="actor",
        title="Individual who was performing",
        description=(
            "The device, practitioner, etc. who performed or participated in the "
            "service."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "Organization",
                "Patient",
                "Device",
                "RelatedPerson",
            ],
        },
    )

    role: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="role",
        title="What type of performance was done",
        description=(
            "Describes the type of performance or participation(e.g. primary "
            "surgeon, anaesthesiologiest, etc.)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ChargeItemParticipant`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "role", "actor"]
