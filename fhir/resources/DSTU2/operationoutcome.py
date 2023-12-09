# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/OperationOutcome
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic.v1 import Field

from . import fhirtypes
from .backboneelement import BackboneElement
from .domainresource import DomainResource


class OperationOutcome(DomainResource):
    """Information about the success/failure of an action.

    A collection of error, warning or information messages that result from a
    system action.
    """

    resource_type = Field("OperationOutcome", const=True)

    issue: ListType[fhirtypes.OperationOutcomeIssueType] = Field(
        None,
        alias="issue",
        title="List of `OperationOutcomeIssue` items (represented as `dict` in JSON).",
        description="A single issue associated with the action.",
    )


class OperationOutcomeIssue(BackboneElement):
    """A single issue associated with the action.

    An error, warning or information message that results from a system action.
    """

    resource_type = Field("OperationOutcomeIssue", const=True)

    code: fhirtypes.Code = Field(
        ..., alias="code", title="Type `Code`.", description="Error or warning code."
    )
    severity: fhirtypes.Code = Field(
        ...,
        alias="severity",
        title="Type `Code`.",
        description="fatal | error | warning | information.",
    )
    details: fhirtypes.CodeableConceptType = Field(
        None,
        alias="details",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Additional details about the error.",
    )

    diagnostics: fhirtypes.String = Field(
        None,
        alias="diagnostics",
        title="Type `String`.",
        description="Additional diagnostic information about the issue.",
    )

    location: ListType[fhirtypes.String] = Field(
        None,
        alias="location",
        title="List of `String` items.",
        description="XPath of element(s) related to issue.",
    )
