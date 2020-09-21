# -*- coding: utf-8 -*-
"""
Profile: https://www.hl7.org/fhir/DSTU2/explanationofbenefit.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic import Field

from . import domainresource, fhirtypes


class ExplanationOfBenefit(domainresource.DomainResource):
    """Explanation of Benefit resource.

    This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """

    resource_type = Field("ExplanationOfBenefit", const=True)

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Response creation date",
        description="The date this resource was created.",
    )

    disposition: fhirtypes.String = Field(
        None,
        alias="disposition",
        title="Disposition Message",
        description="A human readable description of the status of the adjudication.",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier for the resource",
        description="A unique identifier assigned to this explanation of benefit.",
    )

    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON).",
        description="Insurer.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    originalRuleset: fhirtypes.CodingType = Field(
        None,
        alias="originalRuleset",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Original version.",
    )

    outcome: fhirtypes.Code = Field(
        None,
        alias="outcome",
        title="complete | error",
        description=(
            "The outcome of the claim, predetermination, or preauthorization "
            "processing."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["complete", "error"],
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title="Type `Reference` referencing `Claim` (represented as `dict` in JSON).",
        description="Claim reference.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Claim"],
    )

    requestOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="requestOrganization",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)."
        ),
        description="Responsible organization.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    requestProvider: fhirtypes.ReferenceType = Field(
        None,
        alias="requestProvider",
        title="Type `Reference` referencing `Practitioner` (represented as `dict` in JSON).",
        description="Responsible practitioner.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    ruleset: fhirtypes.CodingType = Field(
        None,
        alias="ruleset",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Resource version.",
    )
