# -*- coding: utf-8 -*-
"""
Profile: https://www.hl7.org/fhir/DSTU2/detectedissue.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class DetectedIssue(domainresource.DomainResource):
    """Clinical issue with action.

    Indicates an actual or potential clinical issue with or between one or more
    active or proposed clinical actions for a patient; e.g. Drug-drug
    interaction, Ineffective treatment frequency, Procedure-condition conflict,
    etc.
    """

    resource_type = Field("DetectedIssue", const=True)

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title="The provider or device that identified the issue",
        description=(
            "Individual or device responsible for the issue being raised.  For "
            "example, a decision support application or a pharmacist conducting a "
            "medication review."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Device"],
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Issue Category, e.g. drug-drug, duplicate therapy, etc.",
        description="Identifies the general type of issue identified.",
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="When identified",
        description=(
            "The date or date-time when the detected issue was initially identified."
        ),
    )

    detail: fhirtypes.String = Field(
        None,
        alias="detail",
        title="Description and context",
        description="A textual explanation of the detected issue.",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Unique id for the detected issue",
        description="Business identifier associated with the detected issue record.",
    )

    implicated: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="implicated",
        title="Problem resource",
        description=(
            "Indicates the resource representing the current activity or proposed "
            "activity that is potentially problematic."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    mitigation: ListType[fhirtypes.DetectedIssueMitigationType] = Field(
        None,
        alias="mitigation",
        title="Step taken to address",
        description=(
            "Indicates an action that has been taken or is committed to reduce or "
            "eliminate the likelihood of the risk identified by the detected issue "
            "from manifesting.  Can also reflect an observation of known mitigating"
            " factors that may reduce/eliminate the need for any action."
        ),
    )

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="Associated patient",
        description=(
            "Indicates the patient whose record the detected issue is associated "
            "with."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    reference: fhirtypes.Uri = Field(
        None,
        alias="reference",
        title="Authority for issue",
        description=(
            "The literature, knowledge-base or similar reference that describes the"
            " propensity for the detected issue identified."
        ),
    )

    severity: fhirtypes.Code = Field(
        None,
        alias="severity",
        title="high | moderate | low",
        description=(
            "Indicates the degree of importance associated with the identified "
            "issue based on the potential impact on the patient."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["high", "moderate", "low"],
    )


class DetectedIssueMitigation(backboneelement.BackboneElement):
    """Step taken to address.

    Indicates an action that has been taken or is committed to reduce or
    eliminate the likelihood of the risk identified by the detected issue from
    manifesting.  Can also reflect an observation of known mitigating factors
    that may reduce/eliminate the need for any action.
    """

    resource_type = Field("DetectedIssueMitigation", const=True)

    action: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="action",
        title="What mitigation?",
        description=(
            "Describes the action that was taken or the observation that was made "
            "that reduces/eliminates the risk associated with the identified issue."
        ),
    )

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title="Who is committing?",
        description=(
            "Identifies the practitioner who determined the mitigation and takes "
            "responsibility for the mitigation step occurring."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date committed",
        description="Indicates when the mitigating action was documented.",
    )
