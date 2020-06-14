# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/OperationOutcome
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class OperationOutcome(domainresource.DomainResource):
    """ Information about the success/failure of an action.
    A collection of error, warning, or information messages that result from a
    system action.
    """

    resource_type = Field("OperationOutcome", const=True)

    issue: ListType[fhirtypes.OperationOutcomeIssueType] = Field(
        ...,
        alias="issue",
        title="List of `OperationOutcomeIssue` items (represented as `dict` in JSON)",
        description="A single issue associated with the action",
    )


class OperationOutcomeIssue(backboneelement.BackboneElement):
    """ A single issue associated with the action.
    An error, warning, or information message that results from a system
    action.
    """

    resource_type = Field("OperationOutcomeIssue", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Error or warning code",
    )

    details: fhirtypes.CodeableConceptType = Field(
        None,
        alias="details",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Additional details about the error",
    )

    diagnostics: fhirtypes.String = Field(
        None,
        alias="diagnostics",
        title="Type `String` (represented as `dict` in JSON)",
        description="Additional diagnostic information about the issue",
    )

    expression: ListType[fhirtypes.String] = Field(
        None,
        alias="expression",
        title="List of `String` items (represented as `dict` in JSON)",
        description="FHIRPath of element(s) related to issue",
    )

    location: ListType[fhirtypes.String] = Field(
        None,
        alias="location",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Deprecated: Path of element(s) related to issue",
    )

    severity: fhirtypes.Code = Field(
        ...,
        alias="severity",
        title="Type `Code` (represented as `dict` in JSON)",
        description="fatal | error | warning | information",
    )
