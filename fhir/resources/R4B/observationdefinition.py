# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ObservationDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ObservationDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Definition of an observation.
    Set of definitional characteristics for a kind of observation or
    measurement produced or consumed by an orderable health care service.
    """

    resource_type = Field("ObservationDefinition", const=True)

    abnormalCodedValueSet: fhirtypes.ReferenceType = Field(
        None,
        alias="abnormalCodedValueSet",
        title=(
            "Value set of abnormal coded values for the observations conforming to "
            "this ObservationDefinition"
        ),
        description=(
            "The set of abnormal coded results for the observation conforming to "
            "this ObservationDefinition."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ValueSet"],
    )

    category: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="Category of observation",
        description="A code that classifies the general type of observation.",
        # if property is element of this resource.
        element_property=True,
    )

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Type of observation (code / type)",
        description=(
            "Describes what will be observed. Sometimes this is called the "
            'observation "name".'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    criticalCodedValueSet: fhirtypes.ReferenceType = Field(
        None,
        alias="criticalCodedValueSet",
        title=(
            "Value set of critical coded values for the observations conforming to "
            "this ObservationDefinition"
        ),
        description=(
            "The set of critical coded results for the observation conforming to "
            "this ObservationDefinition."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ValueSet"],
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier for this ObservationDefinition instance",
        description="A unique identifier assigned to this ObservationDefinition artifact.",
        # if property is element of this resource.
        element_property=True,
    )

    method: fhirtypes.CodeableConceptType = Field(
        None,
        alias="method",
        title="Method used to produce the observation",
        description="The method or technique used to perform the observation.",
        # if property is element of this resource.
        element_property=True,
    )

    multipleResultsAllowed: bool = Field(
        None,
        alias="multipleResultsAllowed",
        title="Multiple results allowed",
        description=(
            "Multiple results allowed for observations conforming to this "
            "ObservationDefinition."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    multipleResultsAllowed__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_multipleResultsAllowed",
        title="Extension field for ``multipleResultsAllowed``.",
    )

    normalCodedValueSet: fhirtypes.ReferenceType = Field(
        None,
        alias="normalCodedValueSet",
        title=(
            "Value set of normal coded values for the observations conforming to "
            "this ObservationDefinition"
        ),
        description=(
            "The set of normal coded results for the observations conforming to "
            "this ObservationDefinition."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ValueSet"],
    )

    permittedDataType: typing.List[typing.Optional[fhirtypes.Code]] = Field(
        None,
        alias="permittedDataType",
        title=(
            "Quantity | CodeableConcept | string | boolean | integer | Range | "
            "Ratio | SampledData | time | dateTime | Period"
        ),
        description=(
            "The data types allowed for the value element of the instance "
            "observations conforming to this ObservationDefinition."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "Quantity",
            "CodeableConcept",
            "string",
            "boolean",
            "integer",
            "Range",
            "Ratio",
            "SampledData",
            "time",
            "dateTime",
            "Period",
        ],
    )
    permittedDataType__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_permittedDataType",
        title="Extension field for ``permittedDataType``.",
    )

    preferredReportName: fhirtypes.String = Field(
        None,
        alias="preferredReportName",
        title="Preferred report name",
        description=(
            "The preferred name to be used when reporting the results of "
            "observations conforming to this ObservationDefinition."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    preferredReportName__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_preferredReportName",
        title="Extension field for ``preferredReportName``.",
    )

    qualifiedInterval: typing.List[
        fhirtypes.ObservationDefinitionQualifiedIntervalType
    ] = Field(
        None,
        alias="qualifiedInterval",
        title="Qualified range for continuous and ordinal observation results",
        description=(
            "Multiple  ranges of results qualified by different contexts for "
            "ordinal or continuous observations conforming to this "
            "ObservationDefinition."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    quantitativeDetails: fhirtypes.ObservationDefinitionQuantitativeDetailsType = Field(
        None,
        alias="quantitativeDetails",
        title="Characteristics of quantitative results",
        description="Characteristics for quantitative results of this observation.",
        # if property is element of this resource.
        element_property=True,
    )

    validCodedValueSet: fhirtypes.ReferenceType = Field(
        None,
        alias="validCodedValueSet",
        title=(
            "Value set of valid coded values for the observations conforming to "
            "this ObservationDefinition"
        ),
        description=(
            "The set of valid coded results for the observations  conforming to "
            "this ObservationDefinition."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ValueSet"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ObservationDefinition`` according specification,
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
            "category",
            "code",
            "identifier",
            "permittedDataType",
            "multipleResultsAllowed",
            "method",
            "preferredReportName",
            "quantitativeDetails",
            "qualifiedInterval",
            "validCodedValueSet",
            "normalCodedValueSet",
            "abnormalCodedValueSet",
            "criticalCodedValueSet",
        ]


class ObservationDefinitionQualifiedInterval(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Qualified range for continuous and ordinal observation results.
    Multiple  ranges of results qualified by different contexts for ordinal or
    continuous observations conforming to this ObservationDefinition.
    """

    resource_type = Field("ObservationDefinitionQualifiedInterval", const=True)

    age: fhirtypes.RangeType = Field(
        None,
        alias="age",
        title="Applicable age range, if relevant",
        description=(
            "The age at which this reference range is applicable. This is a "
            "neonatal age (e.g. number of weeks at term) if the meaning says so."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    appliesTo: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="appliesTo",
        title="Targetted population of the range",
        description=(
            "Codes to indicate the target population this reference range applies "
            "to."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    category: fhirtypes.Code = Field(
        None,
        alias="category",
        title="reference | critical | absolute",
        description=(
            "The category of interval of values for continuous or ordinal "
            "observations conforming to this ObservationDefinition."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["reference", "critical", "absolute"],
    )
    category__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_category", title="Extension field for ``category``."
    )

    condition: fhirtypes.String = Field(
        None,
        alias="condition",
        title="Condition associated with the reference range",
        description="Text based condition for which the reference range is valid.",
        # if property is element of this resource.
        element_property=True,
    )
    condition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_condition", title="Extension field for ``condition``."
    )

    context: fhirtypes.CodeableConceptType = Field(
        None,
        alias="context",
        title="Range context qualifier",
        description=(
            "Codes to indicate the health context the range applies to. For "
            "example, the normal or therapeutic range."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    gender: fhirtypes.Code = Field(
        None,
        alias="gender",
        title="male | female | other | unknown",
        description="Sex of the population the range applies to.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["male", "female", "other", "unknown"],
    )
    gender__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_gender", title="Extension field for ``gender``."
    )

    gestationalAge: fhirtypes.RangeType = Field(
        None,
        alias="gestationalAge",
        title="Applicable gestational age range, if relevant",
        description=(
            "The gestational age to which this reference range is applicable, in "
            "the context of pregnancy."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    range: fhirtypes.RangeType = Field(
        None,
        alias="range",
        title="The interval itself, for continuous or ordinal observations",
        description=(
            "The low and high values determining the interval. There may be only "
            "one of the two."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ObservationDefinitionQualifiedInterval`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "category",
            "range",
            "context",
            "appliesTo",
            "gender",
            "age",
            "gestationalAge",
            "condition",
        ]


class ObservationDefinitionQuantitativeDetails(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Characteristics of quantitative results.
    Characteristics for quantitative results of this observation.
    """

    resource_type = Field("ObservationDefinitionQuantitativeDetails", const=True)

    conversionFactor: fhirtypes.Decimal = Field(
        None,
        alias="conversionFactor",
        title="SI to Customary unit conversion factor",
        description=(
            "Factor for converting value expressed with SI unit to value expressed "
            "with customary unit."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    conversionFactor__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_conversionFactor",
        title="Extension field for ``conversionFactor``.",
    )

    customaryUnit: fhirtypes.CodeableConceptType = Field(
        None,
        alias="customaryUnit",
        title="Customary unit for quantitative results",
        description=(
            "Customary unit used to report quantitative results of observations "
            "conforming to this ObservationDefinition."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    decimalPrecision: fhirtypes.Integer = Field(
        None,
        alias="decimalPrecision",
        title="Decimal precision of observation quantitative results",
        description=(
            "Number of digits after decimal separator when the results of such "
            "observations are of type Quantity."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    decimalPrecision__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_decimalPrecision",
        title="Extension field for ``decimalPrecision``.",
    )

    unit: fhirtypes.CodeableConceptType = Field(
        None,
        alias="unit",
        title="SI unit for quantitative results",
        description=(
            "SI unit used to report quantitative results of observations conforming"
            " to this ObservationDefinition."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ObservationDefinitionQuantitativeDetails`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "customaryUnit",
            "unit",
            "conversionFactor",
            "decimalPrecision",
        ]
