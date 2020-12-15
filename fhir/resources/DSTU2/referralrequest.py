# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/DSTU2/referralrequest.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic import Field

from . import domainresource, fhirtypes


class ReferralRequest(domainresource.DomainResource):
    """A request for referral or transfer of care

    Used to record and send details about a request for referral service or
    transfer of a patient to the care of another provider or provider organization.
    """

    resource_type = Field("ReferralRequest", const=True)

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON).",
        description="draft | requested | active | cancelled | accepted | rejected | completed",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "draft",
            "requested",
            "active",
            "cancelled",
            "accepted",
            "rejected",
            "completed",
        ],
        element_property=True,
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier",
        description="The workflow status of the referral or transfer of care request.",
        element_property=True,
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date of creation/activation",
        description=(
            "Date/DateTime of creation for draft requests "
            "and date of activation for active requests."
        ),
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Referral/Transition of care request type",
        element_property=True,
    )

    specialty: fhirtypes.CodeableConceptType = Field(
        None,
        alias="specialty",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="The clinical specialty (discipline) that the referral is requested for",
        element_property=True,
    )

    priority: fhirtypes.CodeableConceptType = Field(
        None,
        alias="priority",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Urgency of referral / transfer of care request",
        element_property=True,
    )

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="Type 'Reference' referencing 'Patient'  (represented as 'dict' in JSON).",
        description="Patient referred to care or transfer",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
        element_property=True,
    )

    requester: fhirtypes.ReferenceType = Field(
        None,
        alias="requester",
        title=(
            "Type 'Reference' referencing 'Practitioner', 'Organization' and "
            "'Patient'  (represented as 'dict' in JSON)."
        ),
        description="Requester of referral / transfer of care",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Organization", "Patient"],
        element_property=True,
    )

    recipient: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="recipient",
        title=(
            "Type 'Reference' referencing 'Practitioner' and 'Organization'"
            "  (represented as 'dict' in JSON)."
        ),
        description="Receiver of referral / transfer of care request",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Organization"],
        element_property=True,
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Type 'Reference' referencing 'Encounter'  (represented as 'dict' in JSON).",
        description="Originating encounter",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
        element_property=True,
    )

    dateSent: fhirtypes.DateTime = Field(
        None,
        alias="dateSent",
        title="Date referral/transfer of care request is sent",
        description=(
            "Date/DateTime the request for referral or transfer "
            "of care is sent by the author."
        ),
        element_property=True,
    )

    reason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reason",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Reason for referral / transfer of care request",
        element_property=True,
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="A textual description of the referral",
        element_property=True,
    )

    serviceRequested: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="serviceRequested",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Actions requested as part of the referral",
        element_property=True,
    )

    supportingInformation: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingInformation",
        title="Type 'Reference' referencing 'Any'  (represented as 'dict' in JSON).",
        description="Additonal information to support referral or transfer of care request",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Any"],
        element_property=True,
    )

    fulfillmentTime: fhirtypes.PeriodType = Field(
        None,
        alias="fulfillmentTime",
        title="Requested service(s) fulfillment time",
        description=(
            "The period of time within which the services identified in the "
            "referral/transfer of care is specified or required to occur."
        ),
        # if property is element of this resource.
        element_property=True,
    )
