# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DetectedIssue
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class DetectedIssue(domainresource.DomainResource):
    """ Clinical issue with action.
    Indicates an actual or potential clinical issue with or between one or more
    active or proposed clinical actions for a patient; e.g. Drug-drug
    interaction, Ineffective treatment frequency, Procedure-condition conflict,
    etc.
    """

    resource_type = Field("DetectedIssue", const=True)

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title=(
            "Type `Reference` referencing `Practitioner, Device` (represented as "
            "`dict` in JSON)"
        ),
        description="The provider or device that identified the issue",
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Issue Category, e.g. drug-drug, duplicate therapy, etc.",
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When identified",
    )

    detail: fhirtypes.String = Field(
        None,
        alias="detail",
        title="Type `String` (represented as `dict` in JSON)",
        description="Description and context",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Unique id for the detected issue",
    )

    implicated: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="implicated",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="Problem resource",
    )

    mitigation: ListType[fhirtypes.DetectedIssueMitigationType] = Field(
        None,
        alias="mitigation",
        title=(
            "List of `DetectedIssueMitigation` items (represented as `dict` in " "JSON)"
        ),
        description="Step taken to address",
    )

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="Associated patient",
    )

    reference: fhirtypes.Uri = Field(
        None,
        alias="reference",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Authority for issue",
    )

    severity: fhirtypes.Code = Field(
        None,
        alias="severity",
        title="Type `Code` (represented as `dict` in JSON)",
        description="high | moderate | low",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="registered | preliminary | final | amended +",
    )


class DetectedIssueMitigation(backboneelement.BackboneElement):
    """ Step taken to address.
    Indicates an action that has been taken or is committed to to reduce or
    eliminate the likelihood of the risk identified by the detected issue from
    manifesting.  Can also reflect an observation of known mitigating factors
    that may reduce/eliminate the need for any action.
    """

    resource_type = Field("DetectedIssueMitigation", const=True)

    action: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="action",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="What mitigation?",
    )

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title=(
            "Type `Reference` referencing `Practitioner` (represented as `dict` in "
            "JSON)"
        ),
        description="Who is committing?",
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date committed",
    )
