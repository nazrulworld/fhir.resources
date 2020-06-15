# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EnrollmentResponse
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import domainresource, fhirtypes


class EnrollmentResponse(domainresource.DomainResource):
    """ EnrollmentResponse resource.
    This resource provides enrollment and plan details from the processing of
    an EnrollmentRequest resource.
    """

    resource_type = Field("EnrollmentResponse", const=True)

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Creation date",
    )

    disposition: fhirtypes.String = Field(
        None,
        alias="disposition",
        title="Type `String` (represented as `dict` in JSON)",
        description="Disposition Message",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business Identifier",
    )

    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Insurer",
    )

    outcome: fhirtypes.Code = Field(
        None,
        alias="outcome",
        title="Type `Code` (represented as `dict` in JSON)",
        description="queued | complete | error | partial",
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title=(
            "Type `Reference` referencing `EnrollmentRequest` (represented as "
            "`dict` in JSON)"
        ),
        description="Claim reference",
    )

    requestProvider: fhirtypes.ReferenceType = Field(
        None,
        alias="requestProvider",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole, "
            "Organization` (represented as `dict` in JSON)"
        ),
        description="Responsible practitioner",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="active | cancelled | draft | entered-in-error",
    )
