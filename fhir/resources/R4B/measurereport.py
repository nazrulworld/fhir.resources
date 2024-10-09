from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/MeasureReport
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class MeasureReport(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Results of a measure evaluation.
    The MeasureReport resource contains the results of the calculation of a
    measure; and optionally a reference to the resources involved in that
    calculation.
    """

    __resource_type__ = "MeasureReport"

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="date",
        title="When the report was generated",
        description="The date this measure report was generated.",
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    evaluatedResource: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="evaluatedResource",
        title="What data was used to calculate the measure score",
        description=(
            "A reference to a Bundle containing the Resources that were used in the"
            " calculation of this measure."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    group: typing.List[fhirtypes.MeasureReportGroupType] | None = Field(  # type: ignore
        None,
        alias="group",
        title="Measure results for each group",
        description=(
            "The results of the calculation, one for each population group in the "
            "measure."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Additional identifier for the MeasureReport",
        description=(
            "A formal identifier that is used to identify this MeasureReport when "
            "it is represented in other formats or referenced in a specification, "
            "model, design or an instance."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    improvementNotation: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="improvementNotation",
        title="increase | decrease",
        description=(
            "Whether improvement in the measure is noted by an increase or decrease"
            " in the measure score."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    measure: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="measure",
        title="What measure was calculated",
        description="A reference to the Measure that was calculated to produce this report.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Measure"],
        },
    )
    measure__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_measure", title="Extension field for ``measure``."
    )

    period: fhirtypes.PeriodType = Field(  # type: ignore
        ...,
        alias="period",
        title="What period the report covers",
        description="The reporting period for which the report was calculated.",
        json_schema_extra={
            "element_property": True,
        },
    )

    reporter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="reporter",
        title="Who is reporting the data",
        description="The individual, location, or organization that is reporting the data.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Location",
                "Organization",
            ],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="complete | pending | error",
        description=(
            "The MeasureReport status. No data will be available until the "
            "MeasureReport status is complete."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["complete", "pending", "error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="subject",
        title="What individual(s) the report is for",
        description=(
            "Optional subject identifying the individual or individuals the report "
            "is for."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Patient",
                "Practitioner",
                "PractitionerRole",
                "Location",
                "Device",
                "RelatedPerson",
                "Group",
            ],
        },
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="individual | subject-list | summary | data-collection",
        description=(
            "The type of measure report. This may be an individual report, which "
            "provides the score for the measure for an individual member of the "
            "population; a subject-listing, which returns the list of members that "
            "meet the various criteria in the measure; a summary report, which "
            "returns a population count for each of the criteria in the measure; or"
            " a data-collection, which enables the MeasureReport to be used to "
            "exchange the data-of-interest for a quality measure."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["individual", "subject-list", "summary", "data-collection"],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
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
            "subject",
            "date",
            "reporter",
            "period",
            "improvementNotation",
            "group",
            "evaluatedResource",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("measure", "measure__ext"),
            ("status", "status__ext"),
            ("type", "type__ext"),
        ]
        return required_fields


class MeasureReportGroup(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Measure results for each group.
    The results of the calculation, one for each population group in the
    measure.
    """

    __resource_type__ = "MeasureReportGroup"

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Meaning of the group",
        description=(
            "The meaning of the population group as defined in the measure "
            "definition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    measureScore: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="measureScore",
        title="What score this group achieved",
        description=(
            "The measure score for this population group, calculated as appropriate"
            " for the measure type and scoring method, and based on the contents of"
            " the populations defined in the group."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    population: typing.List[fhirtypes.MeasureReportGroupPopulationType] | None = Field(  # type: ignore
        None,
        alias="population",
        title="The populations in the group",
        description=(
            "The populations that make up the population group, one for each type "
            "of population appropriate for the measure."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    stratifier: typing.List[fhirtypes.MeasureReportGroupStratifierType] | None = Field(  # type: ignore
        None,
        alias="stratifier",
        title="Stratification results",
        description=(
            "When a measure includes multiple stratifiers, there will be a "
            "stratifier group for each stratifier defined by the measure."
        ),
        json_schema_extra={
            "element_property": True,
        },
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
            "code",
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

    __resource_type__ = "MeasureReportGroupPopulation"

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title=(
            "initial-population | numerator | numerator-exclusion | denominator | "
            "denominator-exclusion | denominator-exception | measure-population | "
            "measure-population-exclusion | measure-observation"
        ),
        description="The type of the population.",
        json_schema_extra={
            "element_property": True,
        },
    )

    count: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="count",
        title="Size of the population",
        description="The number of members of the population.",
        json_schema_extra={
            "element_property": True,
        },
    )
    count__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_count", title="Extension field for ``count``."
    )

    subjectResults: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="subjectResults",
        title="For subject-list reports, the subject results in this population",
        description=(
            "This element refers to a List of subject level MeasureReport "
            "resources, one for each subject in this population."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["List"],
        },
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
            "code",
            "count",
            "subjectResults",
        ]


class MeasureReportGroupStratifier(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Stratification results.
    When a measure includes multiple stratifiers, there will be a stratifier
    group for each stratifier defined by the measure.
    """

    __resource_type__ = "MeasureReportGroupStratifier"

    code: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="code",
        title="What stratifier of the group",
        description="The meaning of this stratifier, as defined in the measure definition.",
        json_schema_extra={
            "element_property": True,
        },
    )

    stratum: typing.List[fhirtypes.MeasureReportGroupStratifierStratumType] | None = Field(  # type: ignore
        None,
        alias="stratum",
        title=(
            "Stratum results, one for each unique value, or set of values, in the "
            "stratifier, or stratifier components"
        ),
        description=(
            "This element contains the results for a single stratum within the "
            "stratifier. For example, when stratifying on administrative gender, "
            "there will be four strata, one for each possible gender value."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MeasureReportGroupStratifier`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "stratum"]


class MeasureReportGroupStratifierStratum(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Stratum results, one for each unique value, or set of values, in the
    stratifier, or stratifier components.
    This element contains the results for a single stratum within the
    stratifier. For example, when stratifying on administrative gender, there
    will be four strata, one for each possible gender value.
    """

    __resource_type__ = "MeasureReportGroupStratifierStratum"

    component: typing.List[fhirtypes.MeasureReportGroupStratifierStratumComponentType] | None = Field(  # type: ignore
        None,
        alias="component",
        title="Stratifier component values",
        description="A stratifier component value.",
        json_schema_extra={
            "element_property": True,
        },
    )

    measureScore: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="measureScore",
        title="What score this stratum achieved",
        description=(
            "The measure score for this stratum, calculated as appropriate for the "
            "measure type and scoring method, and based on only the members of this"
            " stratum."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    population: typing.List[fhirtypes.MeasureReportGroupStratifierStratumPopulationType] | None = Field(  # type: ignore
        None,
        alias="population",
        title="Population results in this stratum",
        description=(
            "The populations that make up the stratum, one for each type of "
            "population appropriate to the measure."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    value: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="value",
        title="The stratum value, e.g. male",
        description=(
            "The value for this stratum, expressed as a CodeableConcept. When "
            "defining stratifiers on complex values, the value must be rendered "
            "such that the value for each stratum within the stratifier is unique."
        ),
        json_schema_extra={
            "element_property": True,
        },
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
            "component",
            "population",
            "measureScore",
        ]


class MeasureReportGroupStratifierStratumComponent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Stratifier component values.
    A stratifier component value.
    """

    __resource_type__ = "MeasureReportGroupStratifierStratumComponent"

    code: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="code",
        title="What stratifier component of the group",
        description="The code for the stratum component value.",
        json_schema_extra={
            "element_property": True,
        },
    )

    value: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="value",
        title="The stratum component value, e.g. male",
        description="The stratum component value.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MeasureReportGroupStratifierStratumComponent`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "value"]


class MeasureReportGroupStratifierStratumPopulation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Population results in this stratum.
    The populations that make up the stratum, one for each type of population
    appropriate to the measure.
    """

    __resource_type__ = "MeasureReportGroupStratifierStratumPopulation"

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title=(
            "initial-population | numerator | numerator-exclusion | denominator | "
            "denominator-exclusion | denominator-exception | measure-population | "
            "measure-population-exclusion | measure-observation"
        ),
        description="The type of the population.",
        json_schema_extra={
            "element_property": True,
        },
    )

    count: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="count",
        title="Size of the population",
        description="The number of members of the population in this stratum.",
        json_schema_extra={
            "element_property": True,
        },
    )
    count__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_count", title="Extension field for ``count``."
    )

    subjectResults: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="subjectResults",
        title="For subject-list reports, the subject results in this population",
        description=(
            "This element refers to a List of subject level MeasureReport "
            "resources, one for each subject in this population in this stratum."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["List"],
        },
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
            "code",
            "count",
            "subjectResults",
        ]
