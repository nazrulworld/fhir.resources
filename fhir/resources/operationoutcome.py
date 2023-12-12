# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/OperationOutcome
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class OperationOutcome(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about the success/failure of an action.
    A collection of error, warning, or information messages that result from a
    system action.
    """

    resource_type = Field("OperationOutcome", const=True)

    issue: typing.List[fhirtypes.OperationOutcomeIssueType] = Field(
        ...,
        alias="issue",
        title="A single issue associated with the action",
        description=(
            "An error, warning, or information message that results from a system "
            "action."
        ),
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("OperationOutcomeIssue", const=True)

    code: fhirtypes.Code = Field(
        None,
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
        element_required=True,
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
            "the error or a system code that identifies the error."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    diagnostics: fhirtypes.String = Field(
        None,
        alias="diagnostics",
        title="Additional diagnostic information about the issue",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    diagnostics__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_diagnostics", title="Extension field for ``diagnostics``."
    )

    expression: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="expression",
        title="FHIRPath of element(s) related to issue",
        description=(
            "A [simple subset of FHIRPath](fhirpath.html#simple) limited to element"
            " names, repetition indicators and the default child accessor that "
            "identifies one of the elements in the resource that caused this issue "
            "to be raised."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    expression__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_expression", title="Extension field for ``expression``.")

    location: typing.List[typing.Optional[fhirtypes.String]] = Field(
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
        # if property is element of this resource.
        element_property=True,
    )
    location__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_location", title="Extension field for ``location``.")

    severity: fhirtypes.Code = Field(
        None,
        alias="severity",
        title="fatal | error | warning | information | success",
        description=(
            "Indicates whether the issue indicates a variation from successful "
            "processing."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["fatal", "error", "warning", "information", "success"],
    )
    severity__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2378(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("code", "code__ext"), ("severity", "severity__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values
