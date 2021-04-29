# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MeasureReport
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class MeasureReport(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Results of a measure evaluation.
    The MeasureReport resource contains the results of evaluating a measure.
    """

    resource_type = Field("MeasureReport", const=True)

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="When the report was generated",
        description="The date this measure report was generated.",
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    evaluatedResources: fhirtypes.ReferenceType = Field(
        None,
        alias="evaluatedResources",
        title="What data was evaluated to produce the measure score",
        description=(
            "A reference to a Bundle containing the Resources that were used in the"
            " evaluation of this report."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Bundle"],
    )

    group: typing.List[fhirtypes.MeasureReportGroupType] = Field(
        None,
        alias="group",
        title="Measure results for each group",
        description=(
            "The results of the calculation, one for each population group in the "
            "measure."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Additional identifier for the Report",
        description=(
            "A formal identifier that is used to identify this report when it is "
            "represented in other formats, or referenced in a specification, model,"
            " design or an instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    measure: fhirtypes.ReferenceType = Field(
        ...,
        alias="measure",
        title="What measure was evaluated",
        description="A reference to the Measure that was evaluated to produce this report.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Measure"],
    )

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="What patient the report is for",
        description="Optional Patient if the report was requested for a single patient.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    period: fhirtypes.PeriodType = Field(
        ...,
        alias="period",
        title="What period the report covers",
        description="The reporting period for which the report was calculated.",
        # if property is element of this resource.
        element_property=True,
    )

    reportingOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="reportingOrganization",
        title="Who is reporting the data",
        description="Reporting Organization.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="complete | pending | error",
        description=(
            "The report status. No data will be available until the report status "
            "is complete."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["complete", "pending", "error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="individual | patient-list | summary",
        description=(
            "The type of measure report. This may be an individual report, which "
            "provides a single patient's score for the measure; a patient listing, "
            "which returns the list of patients that meet the various criteria in "
            "the measure; or a summary report, which returns a population count for"
            " each of the criteria in the measure."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["individual", "patient-list", "summary"],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MeasureReport`` according specification,
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
            "measure",
            "patient",
            "date",
            "reportingOrganization",
            "period",
            "group",
            "evaluatedResources",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1551(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext"), ("type", "type__ext")]
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


class MeasureReportGroup(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Measure results for each group.
    The results of the calculation, one for each population group in the
    measure.
    """

    resource_type = Field("MeasureReportGroup", const=True)

    identifier: fhirtypes.IdentifierType = Field(
        ...,
        alias="identifier",
        title="What group of the measure",
        description=(
            "The identifier of the population group as defined in the measure "
            "definition."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    measureScore: fhirtypes.Decimal = Field(
        None,
        alias="measureScore",
        title="What score this group achieved",
        description=(
            "The measure score for this population group, calculated as appropriate"
            " for the measure type and scoring method, and based on the contents of"
            " the populations defined in the group."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    measureScore__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_measureScore", title="Extension field for ``measureScore``."
    )

    population: typing.List[fhirtypes.MeasureReportGroupPopulationType] = Field(
        None,
        alias="population",
        title="The populations in the group",
        description=(
            "The populations that make up the population group, one for each type "
            "of population appropriate for the measure."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    stratifier: typing.List[fhirtypes.MeasureReportGroupStratifierType] = Field(
        None,
        alias="stratifier",
        title="Stratification results",
        description=(
            "When a measure includes multiple stratifiers, there will be a "
            "stratifier group for each stratifier defined by the measure."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MeasureReportGroup`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "identifier",
            "population",
            "measureScore",
            "stratifier",
        ]


class MeasureReportGroupPopulation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The populations in the group.
    The populations that make up the population group, one for each type of
    population appropriate for the measure.
    """

    resource_type = Field("MeasureReportGroupPopulation", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title=(
            "initial-population | numerator | numerator-exclusion | denominator | "
            "denominator-exclusion | denominator-exception | measure-population | "
            "measure-population-exclusion | measure-score"
        ),
        description="The type of the population.",
        # if property is element of this resource.
        element_property=True,
    )

    count: fhirtypes.Integer = Field(
        None,
        alias="count",
        title="Size of the population",
        description="The number of members of the population.",
        # if property is element of this resource.
        element_property=True,
    )
    count__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_count", title="Extension field for ``count``."
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Population identifier as defined in the measure",
        description=(
            "The identifier of the population being reported, as defined by the "
            "population element of the measure."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    patients: fhirtypes.ReferenceType = Field(
        None,
        alias="patients",
        title="For patient-list reports, the patients in this population",
        description=(
            "This element refers to a List of patient level MeasureReport "
            "resources, one for each patient in this population."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["List"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MeasureReportGroupPopulation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "identifier",
            "code",
            "count",
            "patients",
        ]


class MeasureReportGroupStratifier(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Stratification results.
    When a measure includes multiple stratifiers, there will be a stratifier
    group for each stratifier defined by the measure.
    """

    resource_type = Field("MeasureReportGroupStratifier", const=True)

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="What stratifier of the group",
        description=(
            "The identifier of this stratifier, as defined in the measure "
            "definition."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    stratum: typing.List[fhirtypes.MeasureReportGroupStratifierStratumType] = Field(
        None,
        alias="stratum",
        title="Stratum results, one for each unique value in the stratifier",
        description=(
            "This element contains the results for a single stratum within the "
            "stratifier. For example, when stratifying on administrative gender, "
            "there will be four strata, one for each possible gender value."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MeasureReportGroupStratifier`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "identifier", "stratum"]


class MeasureReportGroupStratifierStratum(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Stratum results, one for each unique value in the stratifier.
    This element contains the results for a single stratum within the
    stratifier. For example, when stratifying on administrative gender, there
    will be four strata, one for each possible gender value.
    """

    resource_type = Field("MeasureReportGroupStratifierStratum", const=True)

    measureScore: fhirtypes.Decimal = Field(
        None,
        alias="measureScore",
        title="What score this stratum achieved",
        description=(
            "The measure score for this stratum, calculated as appropriate for the "
            "measure type and scoring method, and based on only the members of this"
            " stratum."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    measureScore__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_measureScore", title="Extension field for ``measureScore``."
    )

    population: typing.List[
        fhirtypes.MeasureReportGroupStratifierStratumPopulationType
    ] = Field(
        None,
        alias="population",
        title="Population results in this stratum",
        description=(
            "The populations that make up the stratum, one for each type of "
            "population appropriate to the measure."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="The stratum value, e.g. male",
        description=(
            "The value for this stratum, expressed as a string. When defining "
            "stratifiers on complex values, the value must be rendered such that "
            "the value for each stratum within the stratifier is unique."
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
        ``MeasureReportGroupStratifierStratum`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "value",
            "population",
            "measureScore",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3874(
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


class MeasureReportGroupStratifierStratumPopulation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Population results in this stratum.
    The populations that make up the stratum, one for each type of population
    appropriate to the measure.
    """

    resource_type = Field("MeasureReportGroupStratifierStratumPopulation", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title=(
            "initial-population | numerator | numerator-exclusion | denominator | "
            "denominator-exclusion | denominator-exception | measure-population | "
            "measure-population-exclusion | measure-score"
        ),
        description="The type of the population.",
        # if property is element of this resource.
        element_property=True,
    )

    count: fhirtypes.Integer = Field(
        None,
        alias="count",
        title="Size of the population",
        description="The number of members of the population in this stratum.",
        # if property is element of this resource.
        element_property=True,
    )
    count__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_count", title="Extension field for ``count``."
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Population identifier as defined in the measure",
        description=(
            "The identifier of the population being reported, as defined by the "
            "population element of the measure."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    patients: fhirtypes.ReferenceType = Field(
        None,
        alias="patients",
        title="For patient-list reports, the patients in this population",
        description=(
            "This element refers to a List of patient level MeasureReport "
            "resources, one for each patient in this population in this stratum."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["List"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MeasureReportGroupStratifierStratumPopulation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "identifier",
            "code",
            "count",
            "patients",
        ]
