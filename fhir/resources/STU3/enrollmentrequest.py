# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EnrollmentRequest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import domainresource, fhirtypes


class EnrollmentRequest(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Enrollment request.
    This resource provides the insurance enrollment details to the insurer
    regarding a specified coverage.
    """

    resource_type = Field("EnrollmentRequest", const=True)

    coverage: fhirtypes.ReferenceType = Field(
        None,
        alias="coverage",
        title=(
            "Type `Reference` referencing `Coverage` (represented as `dict` in " "JSON)"
        ),
        description="Insurance information",
    )

    created: fhirtypes.DateTime = Field(
        None, alias="created", title="Type `DateTime`", description="Creation date"
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business Identifier",
    )

    insurer: fhirtypes.ReferenceType = Field(
        None,
        alias="insurer",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Target",
    )

    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Responsible organization",
    )

    provider: fhirtypes.ReferenceType = Field(
        None,
        alias="provider",
        title=(
            "Type `Reference` referencing `Practitioner` (represented as `dict` in "
            "JSON)"
        ),
        description="Responsible practitioner",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code`",
        description="active | cancelled | draft | entered-in-error",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="The subject of the Products and Services",
    )
