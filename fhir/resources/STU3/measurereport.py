# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MeasureReport
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class MeasureReport(domainresource.DomainResource):
    """ Results of a measure evaluation.
    The MeasureReport resource contains the results of evaluating a measure.
    """

    resource_type = Field("MeasureReport", const=True)

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When the report was generated",
    )

    evaluatedResources: fhirtypes.ReferenceType = Field(
        None,
        alias="evaluatedResources",
        title="Type `Reference` referencing `Bundle` (represented as `dict` in JSON)",
        description="What data was evaluated to produce the measure score",
    )

    group: ListType[fhirtypes.MeasureReportGroupType] = Field(
        None,
        alias="group",
        title="List of `MeasureReportGroup` items (represented as `dict` in JSON)",
        description="Measure results for each group",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Additional identifier for the Report",
    )

    measure: fhirtypes.ReferenceType = Field(
        ...,
        alias="measure",
        title="Type `Reference` referencing `Measure` (represented as `dict` in JSON)",
        description="What measure was evaluated",
    )

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="What patient the report is for",
    )

    period: fhirtypes.PeriodType = Field(
        ...,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="What period the report covers",
    )

    reportingOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="reportingOrganization",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Who is reporting the data",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="complete | pending | error",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="individual | patient-list | summary",
    )


class MeasureReportGroup(backboneelement.BackboneElement):
    """ Measure results for each group.
    The results of the calculation, one for each population group in the
    measure.
    """

    resource_type = Field("MeasureReportGroup", const=True)

    identifier: fhirtypes.IdentifierType = Field(
        ...,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="What group of the measure",
    )

    measureScore: fhirtypes.Decimal = Field(
        None,
        alias="measureScore",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="What score this group achieved",
    )

    population: ListType[fhirtypes.MeasureReportGroupPopulationType] = Field(
        None,
        alias="population",
        title=(
            "List of `MeasureReportGroupPopulation` items (represented as `dict` in"
            " JSON)"
        ),
        description="The populations in the group",
    )

    stratifier: ListType[fhirtypes.MeasureReportGroupStratifierType] = Field(
        None,
        alias="stratifier",
        title=(
            "List of `MeasureReportGroupStratifier` items (represented as `dict` in"
            " JSON)"
        ),
        description="Stratification results",
    )


class MeasureReportGroupPopulation(backboneelement.BackboneElement):
    """ The populations in the group.
    The populations that make up the population group, one for each type of
    population appropriate for the measure.
    """

    resource_type = Field("MeasureReportGroupPopulation", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "initial-population | numerator | numerator-exclusion | denominator | "
            "denominator-exclusion | denominator-exception | measure-population | "
            "measure-population-exclusion | measure-score"
        ),
    )

    count: fhirtypes.Integer = Field(
        None,
        alias="count",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Size of the population",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Population identifier as defined in the measure",
    )

    patients: fhirtypes.ReferenceType = Field(
        None,
        alias="patients",
        title="Type `Reference` referencing `List` (represented as `dict` in JSON)",
        description="For patient-list reports, the patients in this population",
    )


class MeasureReportGroupStratifier(backboneelement.BackboneElement):
    """ Stratification results.
    When a measure includes multiple stratifiers, there will be a stratifier
    group for each stratifier defined by the measure.
    """

    resource_type = Field("MeasureReportGroupStratifier", const=True)

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="What stratifier of the group",
    )

    stratum: ListType[fhirtypes.MeasureReportGroupStratifierStratumType] = Field(
        None,
        alias="stratum",
        title=(
            "List of `MeasureReportGroupStratifierStratum` items (represented as "
            "`dict` in JSON)"
        ),
        description="Stratum results, one for each unique value in the stratifier",
    )


class MeasureReportGroupStratifierStratum(backboneelement.BackboneElement):
    """ Stratum results, one for each unique value in the stratifier.
    This element contains the results for a single stratum within the
    stratifier. For example, when stratifying on administrative gender, there
    will be four strata, one for each possible gender value.
    """

    resource_type = Field("MeasureReportGroupStratifierStratum", const=True)

    measureScore: fhirtypes.Decimal = Field(
        None,
        alias="measureScore",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="What score this stratum achieved",
    )

    population: ListType[
        fhirtypes.MeasureReportGroupStratifierStratumPopulationType
    ] = Field(
        None,
        alias="population",
        title=(
            "List of `MeasureReportGroupStratifierStratumPopulation` items "
            "(represented as `dict` in JSON)"
        ),
        description="Population results in this stratum",
    )

    value: fhirtypes.String = Field(
        ...,
        alias="value",
        title="Type `String` (represented as `dict` in JSON)",
        description="The stratum value, e.g. male",
    )


class MeasureReportGroupStratifierStratumPopulation(backboneelement.BackboneElement):
    """ Population results in this stratum.
    The populations that make up the stratum, one for each type of population
    appropriate to the measure.
    """

    resource_type = Field("MeasureReportGroupStratifierStratumPopulation", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "initial-population | numerator | numerator-exclusion | denominator | "
            "denominator-exclusion | denominator-exception | measure-population | "
            "measure-population-exclusion | measure-score"
        ),
    )

    count: fhirtypes.Integer = Field(
        None,
        alias="count",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Size of the population",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Population identifier as defined in the measure",
    )

    patients: fhirtypes.ReferenceType = Field(
        None,
        alias="patients",
        title="Type `Reference` referencing `List` (represented as `dict` in JSON)",
        description="For patient-list reports, the patients in this population",
    )
