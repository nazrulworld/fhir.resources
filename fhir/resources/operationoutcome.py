from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/OperationOutcome
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class OperationOutcome(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about the success/failure of an action.
    A collection of error, warning, or information messages that result from a
    system action.
    """

    __resource_type__ = "OperationOutcome"

    issue: typing.List[fhirtypes.OperationOutcomeIssueType] = Field(  # type: ignore
        ...,
        alias="issue",
        title="A single issue associated with the action",
        description=(
            "An error, warning, or information message that results from a system "
            "action."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``OperationOutcome`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "issue",
        ]


class OperationOutcomeIssue(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A single issue associated with the action.
    An error, warning, or information message that results from a system
    action.
    """

    __resource_type__ = "OperationOutcomeIssue"

    code: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Error or warning code",
        description=(
            "Describes the type of the issue. The system that creates an "
            "OperationOutcome SHALL choose the most applicable code from the "
            "IssueType value set, and may additional provide its own code for the "
            "error in the details element."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_code", title="Extension field for ``code``."
    )

    details: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="details",
        title="Additional details about the error",
        description=(
            "Additional details about the error. This may be a text description of "
            "the error or a system code that identifies the error."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    diagnostics: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="diagnostics",
        title="Additional diagnostic information about the issue",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    diagnostics__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_diagnostics", title="Extension field for ``diagnostics``."
    )

    expression: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="expression",
        title="FHIRPath of element(s) related to issue",
        description=(
            "A [simple subset of FHIRPath](fhirpath.html#simple) limited to element"
            " names, repetition indicators and the default child accessor that "
            "identifies one of the elements in the resource that caused this issue "
            "to be raised."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    expression__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_expression", title="Extension field for ``expression``."
    )

    location: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="location",
        title="Deprecated: Path of element(s) related to issue",
        description=(
            "This element is deprecated because it is XML specific. It is replaced "
            "by issue.expression, which is format independent, and simpler to "
            "parse.   For resource issues, this will be a simple XPath limited to "
            "element names, repetition indicators and the default child accessor "
            "that identifies one of the elements in the resource that caused this "
            'issue to be raised.  For HTTP errors, will be "http." + the parameter '
            "name."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    location__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_location", title="Extension field for ``location``."
    )

    severity: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="severity",
        title="fatal | error | warning | information | success",
        description=(
            "Indicates whether the issue indicates a variation from successful "
            "processing."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["fatal", "error", "warning", "information", "success"],
        },
    )
    severity__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_severity", title="Extension field for ``severity``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``OperationOutcomeIssue`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "severity",
            "code",
            "details",
            "diagnostics",
            "location",
            "expression",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("code", "code__ext"), ("severity", "severity__ext")]
        return required_fields
