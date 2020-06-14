# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceRequest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class DeviceRequest(domainresource.DomainResource):
    """ Medical device request.
    Represents a request for a patient to employ a medical device. The device
    may be an implantable device, or an external assistive device, such as a
    walker.
    """

    resource_type = Field("DeviceRequest", const=True)

    authoredOn: fhirtypes.DateTime = Field(
        None,
        alias="authoredOn",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When recorded",
    )

    basedOn: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="List of `Reference` items referencing `Resource` (represented as `dict` in JSON)",
        description="What request fulfills",
    )

    codeCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="codeCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Device requested",
        one_of_many="code",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    codeReference: fhirtypes.ReferenceType = Field(
        None,
        alias="codeReference",
        title="Type `Reference` referencing `Device` (represented as `dict` in JSON)",
        description="Device requested",
        one_of_many="code",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title="Type `Reference` referencing `Encounter, EpisodeOfCare` (represented as `dict` in JSON)",
        description="Encounter or Episode motivating request",
    )

    definition: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="definition",
        title="List of `Reference` items referencing `ActivityDefinition, PlanDefinition` (represented as `dict` in JSON)",
        description="Protocol or definition",
    )

    groupIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="groupIdentifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Identifier of composite request",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="External Request identifier",
    )

    intent: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="intent",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="proposal | plan | original-order | encoded | reflex-order",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Notes or comments",
    )

    occurrenceDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurrenceDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Desired time or schedule for use",
        one_of_many="occurrence",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    occurrencePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="occurrencePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Desired time or schedule for use",
        one_of_many="occurrence",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    occurrenceTiming: fhirtypes.TimingType = Field(
        None,
        alias="occurrenceTiming",
        title="Type `Timing` (represented as `dict` in JSON)",
        description="Desired time or schedule for use",
        one_of_many="occurrence",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    performer: fhirtypes.ReferenceType = Field(
        None,
        alias="performer",
        title="Type `Reference` referencing `Practitioner, Organization, Patient, Device, RelatedPerson, HealthcareService` (represented as `dict` in JSON)",
        description="Requested Filler",
    )

    performerType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="performerType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Fille role",
    )

    priorRequest: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="priorRequest",
        title="List of `Reference` items referencing `Resource` (represented as `dict` in JSON)",
        description="What request replaces",
    )

    priority: fhirtypes.Code = Field(
        None,
        alias="priority",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Indicates how quickly the {{title}} should be addressed with respect to other requests",
    )

    reasonCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Coded Reason for request",
    )

    reasonReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title="List of `Reference` items referencing `Resource` (represented as `dict` in JSON)",
        description="Linked Reason for request",
    )

    relevantHistory: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="relevantHistory",
        title="List of `Reference` items referencing `Provenance` (represented as `dict` in JSON)",
        description="Request provenance",
    )

    requester: fhirtypes.DeviceRequestRequesterType = Field(
        None,
        alias="requester",
        title="Type `DeviceRequestRequester` (represented as `dict` in JSON)",
        description="Who/what is requesting diagnostics",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="draft | active | suspended | completed | entered-in-error | cancelled",
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Type `Reference` referencing `Patient, Group, Location, Device` (represented as `dict` in JSON)",
        description="Focus of request",
    )

    supportingInfo: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingInfo",
        title="List of `Reference` items referencing `Resource` (represented as `dict` in JSON)",
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
            "code": ["codeCodeableConcept", "codeReference",],
            "occurrence": [
                "occurrenceDateTime",
                "occurrencePeriod",
                "occurrenceTiming",
            ],
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


class DeviceRequestRequester(backboneelement.BackboneElement):
    """ Who/what is requesting diagnostics.
    The individual who initiated the request and has responsibility for its
    activation.
    """

    resource_type = Field("DeviceRequestRequester", const=True)

    agent: fhirtypes.ReferenceType = Field(
        ...,
        alias="agent",
        title="Type `Reference` referencing `Device, Practitioner, Organization` (represented as `dict` in JSON)",
        description="Individual making the request",
    )

    onBehalfOf: fhirtypes.ReferenceType = Field(
        None,
        alias="onBehalfOf",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Organization agent is acting for",
    )
