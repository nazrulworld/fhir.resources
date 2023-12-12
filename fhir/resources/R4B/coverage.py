# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Coverage
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class Coverage(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Insurance or medical plan or a payment agreement.
    Financial instrument which may be used to reimburse or pay for health care
    products and services. Includes both insurance and self-payment.
    """

    resource_type = Field("Coverage", const=True)

    beneficiary: fhirtypes.ReferenceType = Field(
        ...,
        alias="beneficiary",
        title="Plan beneficiary",
        description=(
            "The party who benefits from the insurance coverage; the patient when "
            "products and/or services are provided."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    class_fhir: typing.List[fhirtypes.CoverageClassType] = Field(
        None,
        alias="class",
        title="Additional coverage classifications",
        description="A suite of underwriter specific classifiers.",
        # if property is element of this resource.
        element_property=True,
    )

    contract: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="contract",
        title="Contract details",
        description="The policy(s) which constitute this insurance coverage.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Contract"],
    )

    costToBeneficiary: typing.List[fhirtypes.CoverageCostToBeneficiaryType] = Field(
        None,
        alias="costToBeneficiary",
        title="Patient payments for services/products",
        description=(
            "A suite of codes indicating the cost category and associated amount "
            "which have been detailed in the policy and may have been  included on "
            "the health card."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    dependent: fhirtypes.String = Field(
        None,
        alias="dependent",
        title="Dependent number",
        description="A unique identifier for a dependent under the coverage.",
        # if property is element of this resource.
        element_property=True,
    )
    dependent__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_dependent", title="Extension field for ``dependent``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier for the coverage",
        description="A unique identifier assigned to this coverage.",
        # if property is element of this resource.
        element_property=True,
    )

    network: fhirtypes.String = Field(
        None,
        alias="network",
        title="Insurer network",
        description=(
            "The insurer-specific identifier for the insurer-defined network of "
            "providers to which the beneficiary may seek treatment which will be "
            "covered at the 'in-network' rate, otherwise 'out of network' terms and"
            " conditions apply."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    network__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_network", title="Extension field for ``network``."
    )

    order: fhirtypes.PositiveInt = Field(
        None,
        alias="order",
        title="Relative order of the coverage",
        description=(
            "The order of applicability of this coverage relative to other "
            "coverages which are currently in force. Note, there may be gaps in the"
            " numbering and this does not imply primary, secondary etc. as the "
            "specific positioning of coverages depends upon the episode of care."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    order__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_order", title="Extension field for ``order``."
    )

    payor: typing.List[fhirtypes.ReferenceType] = Field(
        ...,
        alias="payor",
        title="Issuer of the policy",
        description=(
            "The program or plan underwriter or payor including both insurance and "
            "non-insurance agreements, such as patient-pay agreements."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization", "Patient", "RelatedPerson"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Coverage start and end dates",
        description=(
            "Time period during which the coverage is in force. A missing start "
            "date indicates the start date isn't known, a missing end date means "
            "the coverage is continuing to be in force."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    policyHolder: fhirtypes.ReferenceType = Field(
        None,
        alias="policyHolder",
        title="Owner of the policy",
        description="The party who 'owns' the insurance policy.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "RelatedPerson", "Organization"],
    )

    relationship: fhirtypes.CodeableConceptType = Field(
        None,
        alias="relationship",
        title="Beneficiary relationship to the subscriber",
        description="The relationship of beneficiary (patient) to the subscriber.",
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="active | cancelled | draft | entered-in-error",
        description="The status of the resource instance.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "cancelled", "draft", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subrogation: bool = Field(
        None,
        alias="subrogation",
        title="Reimbursement to insurer",
        description=(
            "When 'subrogation=true' this insurance instance has been included not "
            "for adjudication but to provide insurers with the details to recover "
            "costs."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    subrogation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_subrogation", title="Extension field for ``subrogation``."
    )

    subscriber: fhirtypes.ReferenceType = Field(
        None,
        alias="subscriber",
        title="Subscriber to the policy",
        description=(
            "The party who has signed-up for or 'owns' the contractual relationship"
            " to the policy or to whom the benefit of the policy for services "
            "rendered to them or their family is due."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "RelatedPerson"],
    )

    subscriberId: fhirtypes.String = Field(
        None,
        alias="subscriberId",
        title="ID assigned to the subscriber",
        description="The insurer assigned ID for the Subscriber.",
        # if property is element of this resource.
        element_property=True,
    )
    subscriberId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_subscriberId", title="Extension field for ``subscriberId``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Coverage category such as medical or accident",
        description=(
            "The type of coverage: social program, medical plan, accident coverage "
            "(workers compensation, auto), group health or payment by an individual"
            " or organization."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Coverage`` according specification,
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
            "identifier",
            "status",
            "type",
            "policyHolder",
            "subscriber",
            "subscriberId",
            "beneficiary",
            "dependent",
            "relationship",
            "period",
            "payor",
            "class",
            "order",
            "network",
            "costToBeneficiary",
            "subrogation",
            "contract",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_980(
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


class CoverageClass(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional coverage classifications.
    A suite of underwriter specific classifiers.
    """

    resource_type = Field("CoverageClass", const=True)

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Human readable description of the type and value",
        description="A short description for the class.",
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type of class such as 'group' or 'plan'",
        description=(
            "The type of classification for which an insurer-specific class label "
            "or number and optional name is provided, for example may be used to "
            "identify a class of coverage or employer group, Policy, Plan."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="Value associated with the type",
        description=(
            "The alphanumeric string value associated with the insurer issued " "label."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CoverageClass`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "value", "name"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1496(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("value", "value__ext")]
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


class CoverageCostToBeneficiary(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Patient payments for services/products.
    A suite of codes indicating the cost category and associated amount which
    have been detailed in the policy and may have been  included on the health
    card.
    """

    resource_type = Field("CoverageCostToBeneficiary", const=True)

    exception: typing.List[fhirtypes.CoverageCostToBeneficiaryExceptionType] = Field(
        None,
        alias="exception",
        title="Exceptions for patient payments",
        description=(
            "A suite of codes indicating exceptions or reductions to patient costs "
            "and their effective periods."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Cost category",
        description="The category of patient centric costs associated with treatment.",
        # if property is element of this resource.
        element_property=True,
    )

    valueMoney: fhirtypes.MoneyType = Field(
        None,
        alias="valueMoney",
        title="The amount or percentage due from the beneficiary",
        description="The amount due from the patient for the cost category.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="The amount or percentage due from the beneficiary",
        description="The amount due from the patient for the cost category.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CoverageCostToBeneficiary`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "valueQuantity",
            "valueMoney",
            "exception",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2725(
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
        one_of_many_fields = {"value": ["valueMoney", "valueQuantity"]}
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


class CoverageCostToBeneficiaryException(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Exceptions for patient payments.
    A suite of codes indicating exceptions or reductions to patient costs and
    their effective periods.
    """

    resource_type = Field("CoverageCostToBeneficiaryException", const=True)

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="The effective period of the exception",
        description="The timeframe during when the exception is in force.",
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Exception category",
        description="The code for the specific exception.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CoverageCostToBeneficiaryException`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "period"]
