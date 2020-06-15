# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ServiceRequest
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import domainresource, fhirtypes


class ServiceRequest(domainresource.DomainResource):
    """ A request for a service to be performed.
    A record of a request for service such as diagnostic investigations,
    treatments, or operations to be performed.
    """

    resource_type = Field("ServiceRequest", const=True)

    asNeededBoolean: bool = Field(
        None,
        alias="asNeededBoolean",
        title="Type `bool`",
        description="Preconditions for service",
        one_of_many="asNeeded",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    asNeededCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="asNeededCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Preconditions for service",
        one_of_many="asNeeded",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    authoredOn: fhirtypes.DateTime = Field(
        None,
        alias="authoredOn",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date request signed",
    )

    basedOn: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title=(
            "List of `Reference` items referencing `CarePlan, ServiceRequest, "
            "MedicationRequest` (represented as `dict` in JSON)"
        ),
        description="What request fulfills",
    )

    bodySite: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="bodySite",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Location on Body",
    )

    category: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Classification of service",
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="What is being requested/ordered",
    )

    doNotPerform: bool = Field(
        None,
        alias="doNotPerform",
        title="Type `bool`",
        description="True if service/procedure should not be performed",
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title=(
            "Type `Reference` referencing `Encounter` (represented as `dict` in "
            "JSON)"
        ),
        description="Encounter in which the request was created",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Identifiers assigned to this order",
    )

    instantiatesCanonical: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="instantiatesCanonical",
        title=(
            "List of `Canonical` items referencing `ActivityDefinition, "
            "PlanDefinition` (represented as `dict` in JSON)"
        ),
        description="Instantiates FHIR protocol or definition",
    )

    instantiatesUri: ListType[fhirtypes.Uri] = Field(
        None,
        alias="instantiatesUri",
        title="List of `Uri` items (represented as `dict` in JSON)",
        description="Instantiates external protocol or definition",
    )

    insurance: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="insurance",
        title=(
            "List of `Reference` items referencing `Coverage, ClaimResponse` "
            "(represented as `dict` in JSON)"
        ),
        description="Associated insurance coverage",
    )

    intent: fhirtypes.Code = Field(
        ...,
        alias="intent",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "proposal | plan | directive | order | original-order | reflex-order | "
            "filler-order | instance-order | option"
        ),
    )

    locationCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="locationCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Requested location",
    )

    locationReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="locationReference",
        title=(
            "List of `Reference` items referencing `Location` (represented as "
            "`dict` in JSON)"
        ),
        description="Requested location",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Comments",
    )

    occurrenceDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurrenceDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When service should occur",
        one_of_many="occurrence",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    occurrencePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="occurrencePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When service should occur",
        one_of_many="occurrence",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    occurrenceTiming: fhirtypes.TimingType = Field(
        None,
        alias="occurrenceTiming",
        title="Type `Timing` (represented as `dict` in JSON)",
        description="When service should occur",
        one_of_many="occurrence",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    orderDetail: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="orderDetail",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Additional order information",
    )

    patientInstruction: fhirtypes.String = Field(
        None,
        alias="patientInstruction",
        title="Type `String` (represented as `dict` in JSON)",
        description="Patient or consumer-oriented instructions",
    )

    performer: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="performer",
        title=(
            "List of `Reference` items referencing `Practitioner, PractitionerRole,"
            " Organization, CareTeam, HealthcareService, Patient, Device, "
            "RelatedPerson` (represented as `dict` in JSON)"
        ),
        description="Requested performer",
    )

    performerType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="performerType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Performer role",
    )

    priority: fhirtypes.Code = Field(
        None,
        alias="priority",
        title="Type `Code` (represented as `dict` in JSON)",
        description="routine | urgent | asap | stat",
    )

    quantityQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantityQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Service amount",
        one_of_many="quantity",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    quantityRange: fhirtypes.RangeType = Field(
        None,
        alias="quantityRange",
        title="Type `Range` (represented as `dict` in JSON)",
        description="Service amount",
        one_of_many="quantity",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    quantityRatio: fhirtypes.RatioType = Field(
        None,
        alias="quantityRatio",
        title="Type `Ratio` (represented as `dict` in JSON)",
        description="Service amount",
        one_of_many="quantity",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    reasonCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Explanation/Justification for procedure or service",
    )

    reasonReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title=(
            "List of `Reference` items referencing `Condition, Observation, "
            "DiagnosticReport, DocumentReference` (represented as `dict` in JSON)"
        ),
        description="Explanation/Justification for service or service",
    )

    relevantHistory: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="relevantHistory",
        title=(
            "List of `Reference` items referencing `Provenance` (represented as "
            "`dict` in JSON)"
        ),
        description="Request provenance",
    )

    replaces: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="replaces",
        title=(
            "List of `Reference` items referencing `ServiceRequest` (represented as"
            " `dict` in JSON)"
        ),
        description="What request replaces",
    )

    requester: fhirtypes.ReferenceType = Field(
        None,
        alias="requester",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole, "
            "Organization, Patient, RelatedPerson, Device` (represented as `dict` "
            "in JSON)"
        ),
        description="Who/what is requesting service",
    )

    requisition: fhirtypes.IdentifierType = Field(
        None,
        alias="requisition",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Composite Request ID",
    )

    specimen: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="specimen",
        title=(
            "List of `Reference` items referencing `Specimen` (represented as "
            "`dict` in JSON)"
        ),
        description="Procedure Samples",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "draft | active | on-hold | revoked | completed | entered-in-error | "
            "unknown"
        ),
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title=(
            "Type `Reference` referencing `Patient, Group, Location, Device` "
            "(represented as `dict` in JSON)"
        ),
        description="Individual or Entity the service is ordered for",
    )

    supportingInfo: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingInfo",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="Additional clinical information",
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
            "asNeeded": ["asNeededBoolean", "asNeededCodeableConcept"],
            "occurrence": [
                "occurrenceDateTime",
                "occurrencePeriod",
                "occurrenceTiming",
            ],
            "quantity": ["quantityQuantity", "quantityRange", "quantityRatio"],
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
