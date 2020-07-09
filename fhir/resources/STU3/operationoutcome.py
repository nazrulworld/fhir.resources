# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/OperationOutcome
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
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
    A collection of error, warning or information messages that result from a
    system action.
    """

    resource_type = Field("OperationOutcome", const=True)

    issue: ListType[fhirtypes.OperationOutcomeIssueType] = Field(
        ...,
        alias="issue",
        title="A single issue associated with the action",
        description=(
            "An error, warning or information message that results from a system "
            "action."
        ),
        # if property is element of this resource.
        element_property=True,
    )


class OperationOutcomeIssue(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A single issue associated with the action.
    An error, warning or information message that results from a system action.
    """

    resource_type = Field("OperationOutcomeIssue", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Error or warning code",
        description=(
            "Describes the type of the issue. The system that creates an "
            "OperationOutcome SHALL choose the most applicable code from the "
            "IssueType value set, and may additional provide its own code for the "
            "error in the details element."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    details: fhirtypes.CodeableConceptType = Field(
        None,
        alias="details",
        title="Additional details about the error",
        description=(
            "Additional details about the error. This may be a text description of "
            "the error, or a system code that identifies the error."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    diagnostics: fhirtypes.String = Field(
        None,
        alias="diagnostics",
        title="Additional diagnostic information about the issue",
        description=(
            "Additional diagnostic information about the issue.  Typically, this "
            "may be a description of how a value is erroneous, or a stack dump to "
            "help trace the issue."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    diagnostics__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_diagnostics", title="Extension field for ``diagnostics``."
    )

    expression: ListType[fhirtypes.String] = Field(
        None,
        alias="expression",
        title="FHIRPath of element(s) related to issue",
        description=(
            "A simple FHIRPath limited to element names, repetition indicators and "
            "the default child access that identifies one of the elements in the "
            "resource that caused this issue to be raised."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    expression__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_expression", title="Extension field for ``expression``.")

    location: ListType[fhirtypes.String] = Field(
        None,
        alias="location",
        title="Path of element(s) related to issue",
        description=(
            "For resource issues, this will be a simple XPath limited to element "
            "names, repetition indicators and the default child access that "
            "identifies one of the elements in the resource that caused this issue "
            'to be raised.  For HTTP errors, will be "http." + the parameter name.'
        ),
        # if property is element of this resource.
        element_property=True,
    )
    location__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_location", title="Extension field for ``location``."
    )

    severity: fhirtypes.Code = Field(
        ...,
        alias="severity",
        title="fatal | error | warning | information",
        description=(
            "Indicates whether the issue indicates a variation from successful "
            "processing."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["fatal", "error", "warning", "information"],
    )
    severity__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_severity", title="Extension field for ``severity``."
    )
