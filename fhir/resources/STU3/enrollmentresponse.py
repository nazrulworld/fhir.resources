# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EnrollmentResponse
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import domainresource, fhirtypes


class EnrollmentResponse(domainresource.DomainResource):
    """ EnrollmentResponse resource.
    This resource provides enrollment and plan details from the processing of
    an Enrollment resource.
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
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Insurer",
    )

    outcome: fhirtypes.CodeableConceptType = Field(
        None,
        alias="outcome",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="complete | error | partial",
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title="Type `Reference` referencing `EnrollmentRequest` (represented as `dict` in JSON)",
        description="Claim reference",
    )

    requestOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="requestOrganization",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Responsible organization",
    )

    requestProvider: fhirtypes.ReferenceType = Field(
        None,
        alias="requestProvider",
        title="Type `Reference` referencing `Practitioner` (represented as `dict` in JSON)",
        description="Responsible practitioner",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="active | cancelled | draft | entered-in-error",
    )
