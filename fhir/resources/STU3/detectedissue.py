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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Clinical issue with action.
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
        None, alias="date", title="Type `DateTime`", description="When identified"
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    detail: fhirtypes.String = Field(
        None,
        alias="detail",
        title="Type `String`",
        description="Description and context",
    )
    detail__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_detail", title="Extension field for ``detail``."
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
        None, alias="reference", title="Type `Uri`", description="Authority for issue"
    )
    reference__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_reference", title="Extension field for ``reference``."
    )

    severity: fhirtypes.Code = Field(
        None, alias="severity", title="Type `Code`", description="high | moderate | low"
    )
    severity__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_severity", title="Extension field for ``severity``."
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`",
        description="registered | preliminary | final | amended +",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )


class DetectedIssueMitigation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Step taken to address.
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
        None, alias="date", title="Type `DateTime`", description="Date committed"
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )
