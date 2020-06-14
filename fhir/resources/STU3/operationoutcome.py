# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/OperationOutcome
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class OperationOutcome(domainresource.DomainResource):
    """ Information about the success/failure of an action.
    A collection of error, warning or information messages that result from a
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
    An error, warning or information message that results from a system action.
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
        description="Path of element(s) related to issue",
    )

    severity: fhirtypes.Code = Field(
        ...,
        alias="severity",
        title="Type `Code` (represented as `dict` in JSON)",
        description="fatal | error | warning | information",
    )
