# -*- coding: utf-8 -*-
"""
Profile: https://www.hl7.org/fhir/DSTU2/enrollmentresponse.html
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import domainresource, fhirtypes


class EnrollmentResponse(domainresource.DomainResource):
    """
    EnrollmentResponse resource.
    This resource provides enrollment and plan details from the processing of
    an EnrollmentRequest resource.
    """

    resource_type = Field("EnrollmentResponse", const=True)

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier",
        description="The Response business identifier.",
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title="Claim reference",
        description="Original request resource reference.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["EnrollmentRequest"],
    )

    outcome: fhirtypes.Code = Field(
        None,
        alias="outcome",
        title="complete | error",
        description="Processing status: error, complete.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["complete", "error"],
    )

    disposition: fhirtypes.String = Field(
        None,
        alias="disposition",
        title="Disposition Message",
        description="A description of the status of the adjudication.",
    )

    ruleset: fhirtypes.CodingType = Field(
        None,
        alias="ruleset",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Resource version.",
    )

    originalRuleset: fhirtypes.CodingType = Field(
        None,
        alias="originalRuleset",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Original version.",
    )

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Creation date",
        description=(
            "The date when the enclosed suite of services were performed or "
            "completed."
        ),
    )

    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title="Insurer",
        description="The Insurer who produced this adjudicated response.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    requestProvider: fhirtypes.ReferenceType = Field(
        None,
        alias="requestProvider",
        title="Responsible practitioner",
        description=(
            "The practitioner who is responsible for the services rendered to the "
            "patient."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    requestOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="requestOrganization",
        title="Insurer",
        description="The Insurer who produced this adjudicated response.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )
