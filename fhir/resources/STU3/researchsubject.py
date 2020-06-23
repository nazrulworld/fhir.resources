# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ResearchSubject
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic import Field

from . import domainresource, fhirtypes


class ResearchSubject(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Investigation to increase healthcare-related patient-independent knowledge.
    A process where a researcher or organization plans and then executes a
    series of steps intended to increase the field of healthcare-related
    knowledge.  This includes studies of safety, efficacy, comparative
    effectiveness and other information about medications, devices, therapies
    and other interventional and investigative techniques.  A ResearchStudy
    involves the gathering of information about human or animal subjects.
    """

    resource_type = Field("ResearchSubject", const=True)

    actualArm: fhirtypes.String = Field(
        None,
        alias="actualArm",
        title="Type `String`",
        description="What path was followed",
    )
    actualArm__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_actualArm", title="Extension field for ``actualArm``."
    )

    assignedArm: fhirtypes.String = Field(
        None,
        alias="assignedArm",
        title="Type `String`",
        description="What path should be followed",
    )
    assignedArm__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_assignedArm", title="Extension field for ``assignedArm``."
    )

    consent: fhirtypes.ReferenceType = Field(
        None,
        alias="consent",
        title="Type `Reference` referencing `Consent` (represented as `dict` in JSON)",
        description="Agreement to participate in study",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Business Identifier for research subject",
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
        title="Type `Code`",
        description="candidate | enrolled | active | suspended | withdrawn | completed",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
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
