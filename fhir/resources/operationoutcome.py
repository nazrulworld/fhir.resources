# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/OperationOutcome
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType
from typing import Union

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class OperationOutcome(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about the success/failure of an action.
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A single issue associated with the action.
    An error, warning, or information message that results from a system
    action.
    """

    resource_type = Field("OperationOutcomeIssue", const=True)

    code: fhirtypes.Code = Field(
        ..., alias="code", title="Type `Code`", description="Error or warning code"
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
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
        title="Type `String`",
        description="Additional diagnostic information about the issue",
    )
    diagnostics__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_diagnostics", title="Extension field for ``diagnostics``."
    )

    expression: ListType[fhirtypes.String] = Field(
        None,
        alias="expression",
        title="List of `String` items",
        description="FHIRPath of element(s) related to issue",
    )
    expression__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_expression", title="Extension field for ``expression``.")

    location: ListType[fhirtypes.String] = Field(
        None,
        alias="location",
        title="List of `String` items",
        description="Deprecated: Path of element(s) related to issue",
    )
    location__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_location", title="Extension field for ``location``."
    )

    severity: fhirtypes.Code = Field(
        ...,
        alias="severity",
        title="Type `Code`",
        description="fatal | error | warning | information",
    )
    severity__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_severity", title="Extension field for ``severity``."
    )
