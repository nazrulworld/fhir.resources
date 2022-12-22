# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/GuidanceResponse
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import domainresource, fhirtypes


class GuidanceResponse(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The formal response to a guidance request.
    A guidance response is the formal response to a guidance request, including
    any output parameters returned by the evaluation, as well as the
    description of any proposed actions to be taken.
    """

    resource_type = Field("GuidanceResponse", const=True)

    dataRequirement: typing.List[fhirtypes.DataRequirementType] = Field(
        None,
        alias="dataRequirement",
        title="Additional required data",
        description=(
            "If the evaluation could not be completed due to lack of information, "
            "or additional information would potentially result in a more accurate "
            "response, this element will a description of the data required in "
            "order to proceed with the evaluation. A subsequent request to the "
            "service should include this data."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Encounter during which the response was returned",
        description=(
            "The encounter during which this response was created or to which the "
            "creation of this record is tightly associated."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    evaluationMessage: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="evaluationMessage",
        title="Messages resulting from the evaluation of the artifact or artifacts",
        description=(
            "Messages resulting from the evaluation of the artifact or artifacts. "
            "As part of evaluating the request, the engine may produce "
            "informational or warning messages. These messages will be provided by "
            "this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["OperationOutcome"],
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier",
        description=(
            "Allows a service to provide  unique, business identifiers for the "
            "response."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    moduleCanonical: fhirtypes.Canonical = Field(
        None,
        alias="moduleCanonical",
        title="What guidance was requested",
        description=(
            "An identifier, CodeableConcept or canonical reference to the guidance "
            "that was requested."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e module[x]
        one_of_many="module",
        one_of_many_required=True,
    )
    moduleCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_moduleCanonical", title="Extension field for ``moduleCanonical``."
    )

    moduleCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="moduleCodeableConcept",
        title="What guidance was requested",
        description=(
            "An identifier, CodeableConcept or canonical reference to the guidance "
            "that was requested."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e module[x]
        one_of_many="module",
        one_of_many_required=True,
    )

    moduleUri: fhirtypes.Uri = Field(
        None,
        alias="moduleUri",
        title="What guidance was requested",
        description=(
            "An identifier, CodeableConcept or canonical reference to the guidance "
            "that was requested."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e module[x]
        one_of_many="module",
        one_of_many_required=True,
    )
    moduleUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_moduleUri", title="Extension field for ``moduleUri``."
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Additional notes about the response",
        description=(
            "Provides a mechanism to communicate additional information about the "
            "response."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    occurrenceDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurrenceDateTime",
        title="When the guidance response was processed",
        description="Indicates when the guidance response was processed.",
        # if property is element of this resource.
        element_property=True,
    )
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_occurrenceDateTime",
        title="Extension field for ``occurrenceDateTime``.",
    )

    outputParameters: fhirtypes.ReferenceType = Field(
        None,
        alias="outputParameters",
        title="The output parameters of the evaluation, if any",
        description=(
            "The output parameters of the evaluation, if any. Many modules will "
            "result in the return of specific resources such as procedure or "
            "communication requests that are returned as part of the operation "
            "result. However, modules may define specific outputs that would be "
            "returned as the result of the evaluation, and these would be returned "
            "in this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Parameters"],
    )

    performer: fhirtypes.ReferenceType = Field(
        None,
        alias="performer",
        title="Device returning the guidance",
        description="Provides a reference to the device that performed the guidance.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device"],
    )

    reasonCode: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="Why guidance is needed",
        description=(
            "Describes the reason for the guidance response in coded or textual "
            "form."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    reasonReference: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title="Why guidance is needed",
        description=(
            "Indicates the reason the request was initiated. This is typically "
            "provided as a parameter to the evaluation and echoed by the service, "
            "although for some use cases, such as subscription- or event-based "
            "scenarios, it may provide an indication of the cause for the response."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Condition",
            "Observation",
            "DiagnosticReport",
            "DocumentReference",
        ],
    )

    requestIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="requestIdentifier",
        title="The identifier of the request associated with this response, if any",
        description=(
            "The identifier of the request associated with this response. If an "
            "identifier was given as part of the request, it will be reproduced "
            "here to enable the requester to more easily identify the response in a"
            " multi-request scenario."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    result: fhirtypes.ReferenceType = Field(
        None,
        alias="result",
        title="Proposed actions, if any",
        description="The actions, if any, produced by the evaluation of the artifact.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["CarePlan", "RequestGroup"],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title=(
            "success | data-requested | data-required | in-progress | failure | "
            "entered-in-error"
        ),
        description=(
            "The status of the response. If the evaluation is completed "
            "successfully, the status will indicate success. However, in order to "
            "complete the evaluation, the engine may require more information. In "
            "this case, the status will be data-required, and the response will "
            "contain a description of the additional required information. If the "
            "evaluation completed successfully, but the engine determines that a "
            "potentially more accurate response could be provided if more data was "
            "available, the status will be data-requested, and the response will "
            "contain a description of the additional requested information."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "success",
            "data-requested",
            "data-required",
            "in-progress",
            "failure",
            "entered-in-error",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Patient the request was performed for",
        description="The patient for which the request was processed.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``GuidanceResponse`` according specification,
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
            "requestIdentifier",
            "identifier",
            "moduleUri",
            "moduleCanonical",
            "moduleCodeableConcept",
            "status",
            "subject",
            "encounter",
            "occurrenceDateTime",
            "performer",
            "reasonCode",
            "reasonReference",
            "note",
            "evaluationMessage",
            "outputParameters",
            "result",
            "dataRequirement",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1819(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1819(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "module": ["moduleCanonical", "moduleCodeableConcept", "moduleUri"]
        }
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values
