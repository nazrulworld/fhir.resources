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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Physical entity which is the primary unit of interest in the study.
    A physical entity which is the primary unit of operational and/or
    administrative interest in a study.
    """

    resource_type = Field("ResearchSubject", const=True)

    actualArm: fhirtypes.String = Field(
        None,
        alias="actualArm",
        title="What path was followed",
        description=(
            "The name of the arm in the study the subject actually followed as part"
            " of this study."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    actualArm__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_actualArm", title="Extension field for ``actualArm``."
    )

    assignedArm: fhirtypes.String = Field(
        None,
        alias="assignedArm",
        title="What path should be followed",
        description=(
            "The name of the arm in the study the subject is expected to follow as "
            "part of this study."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    assignedArm__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_assignedArm", title="Extension field for ``assignedArm``."
    )

    consent: fhirtypes.ReferenceType = Field(
        None,
        alias="consent",
        title="Agreement to participate in study",
        description=(
            "A record of the patient's informed agreement to participate in the "
            "study."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Consent"],
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier for research subject in a study",
        description="Identifiers assigned to this research subject for a study.",
        # if property is element of this resource.
        element_property=True,
    )

    individual: fhirtypes.ReferenceType = Field(
        ...,
        alias="individual",
        title="Who is part of study",
        description="The record of the person or animal who is involved in the study.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Start and end of participation",
        description=(
            "The dates the subject began and ended their participation in the " "study."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title=(
            "candidate | eligible | follow-up | ineligible | not-registered | off-"
            "study | on-study | on-study-intervention | on-study-observation | "
            "pending-on-study | potential-candidate | screening | withdrawn"
        ),
        description="The current state of the subject.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "candidate",
            "eligible",
            "follow-up",
            "ineligible",
            "not-registered",
            "off-study",
            "on-study",
            "on-study-intervention",
            "on-study-observation",
            "pending-on-study",
            "potential-candidate",
            "screening",
            "withdrawn",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    study: fhirtypes.ReferenceType = Field(
        ...,
        alias="study",
        title="Study subject is part of",
        description="Reference to the study the subject is participating in.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ResearchStudy"],
    )
