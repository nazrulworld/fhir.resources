# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ResearchSubject
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import domainresource, fhirtypes


class ResearchSubject(domainresource.DomainResource):
    """ Physical entity which is the primary unit of interest in the study.
    A physical entity which is the primary unit of operational and/or
    administrative interest in a study.
    """

    resource_type = Field("ResearchSubject", const=True)

    actualArm: fhirtypes.String = Field(
        None,
        alias="actualArm",
        title="Type `String` (represented as `dict` in JSON)",
        description="What path was followed",
    )

    assignedArm: fhirtypes.String = Field(
        None,
        alias="assignedArm",
        title="Type `String` (represented as `dict` in JSON)",
        description="What path should be followed",
    )

    consent: fhirtypes.ReferenceType = Field(
        None,
        alias="consent",
        title="Type `Reference` referencing `Consent` (represented as `dict` in JSON)",
        description="Agreement to participate in study",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business Identifier for research subject in a study",
    )

    individual: fhirtypes.ReferenceType = Field(
        ...,
        alias="individual",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="Who is part of study",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Start and end of participation",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "candidate | eligible | follow-up | ineligible | not-registered | off-"
            "study | on-study | on-study-intervention | on-study-observation | "
            "pending-on-study | potential-candidate | screening | withdrawn"
        ),
    )

    study: fhirtypes.ReferenceType = Field(
        ...,
        alias="study",
        title=(
            "Type `Reference` referencing `ResearchStudy` (represented as `dict` in"
            " JSON)"
        ),
        description="Study subject is part of",
    )
