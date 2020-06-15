# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MeasureReport
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class MeasureReport(domainresource.DomainResource):
    """ Results of a measure evaluation.
    The MeasureReport resource contains the results of the calculation of a
    measure; and optionally a reference to the resources involved in that
    calculation.
    """

    resource_type = Field("MeasureReport", const=True)

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When the report was generated",
    )

    evaluatedResource: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="evaluatedResource",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="What data was used to calculate the measure score",
    )

    group: ListType[fhirtypes.MeasureReportGroupType] = Field(
        None,
        alias="group",
        title="List of `MeasureReportGroup` items (represented as `dict` in JSON)",
        description="Measure results for each group",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Additional identifier for the MeasureReport",
    )

    improvementNotation: fhirtypes.CodeableConceptType = Field(
        None,
        alias="improvementNotation",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="increase | decrease",
    )

    measure: fhirtypes.Canonical = Field(
        ...,
        alias="measure",
        title="Type `Canonical` referencing `Measure` (represented as `dict` in JSON)",
        description="What measure was calculated",
    )

    period: fhirtypes.PeriodType = Field(
        ...,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="What period the report covers",
    )

    reporter: fhirtypes.ReferenceType = Field(
        None,
        alias="reporter",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole, "
            "Location, Organization` (represented as `dict` in JSON)"
        ),
        description="Who is reporting the data",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="complete | pending | error",
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title=(
            "Type `Reference` referencing `Patient, Practitioner, PractitionerRole,"
            " Location, Device, RelatedPerson, Group` (represented as `dict` in "
            "JSON)"
        ),
        description="What individual(s) the report is for",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="individual | subject-list | summary | data-collection",
    )


class MeasureReportGroup(backboneelement.BackboneElement):
    """ Measure results for each group.
    The results of the calculation, one for each population group in the
    measure.
    """

    resource_type = Field("MeasureReportGroup", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Meaning of the group",
    )

    measureScore: fhirtypes.QuantityType = Field(
        None,
        alias="measureScore",
        title="Type `Quantity` (represented as `dict` in JSON)",
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
            "measure-population-exclusion | measure-observation"
        ),
    )

    count: fhirtypes.Integer = Field(
        None,
        alias="count",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Size of the population",
    )

    subjectResults: fhirtypes.ReferenceType = Field(
        None,
        alias="subjectResults",
        title="Type `Reference` referencing `List` (represented as `dict` in JSON)",
        description="For subject-list reports, the subject results in this population",
    )


class MeasureReportGroupStratifier(backboneelement.BackboneElement):
    """ Stratification results.
    When a measure includes multiple stratifiers, there will be a stratifier
    group for each stratifier defined by the measure.
    """

    resource_type = Field("MeasureReportGroupStratifier", const=True)

    code: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="code",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="What stratifier of the group",
    )

    stratum: ListType[fhirtypes.MeasureReportGroupStratifierStratumType] = Field(
        None,
        alias="stratum",
        title=(
            "List of `MeasureReportGroupStratifierStratum` items (represented as "
            "`dict` in JSON)"
        ),
        description=(
            "Stratum results, one for each unique value, or set of values, in the "
            "stratifier, or stratifier components"
        ),
    )


class MeasureReportGroupStratifierStratum(backboneelement.BackboneElement):
    """ Stratum results, one for each unique value, or set of values, in the
    stratifier, or stratifier components.
    This element contains the results for a single stratum within the
    stratifier. For example, when stratifying on administrative gender, there
    will be four strata, one for each possible gender value.
    """

    resource_type = Field("MeasureReportGroupStratifierStratum", const=True)

    component: ListType[
        fhirtypes.MeasureReportGroupStratifierStratumComponentType
    ] = Field(
        None,
        alias="component",
        title=(
            "List of `MeasureReportGroupStratifierStratumComponent` items "
            "(represented as `dict` in JSON)"
        ),
        description="Stratifier component values",
    )

    measureScore: fhirtypes.QuantityType = Field(
        None,
        alias="measureScore",
        title="Type `Quantity` (represented as `dict` in JSON)",
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

    value: fhirtypes.CodeableConceptType = Field(
        None,
        alias="value",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The stratum value, e.g. male",
    )


class MeasureReportGroupStratifierStratumComponent(backboneelement.BackboneElement):
    """ Stratifier component values.
    A stratifier component value.
    """

    resource_type = Field("MeasureReportGroupStratifierStratumComponent", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="What stratifier component of the group",
    )

    value: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="value",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The stratum component value, e.g. male",
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
            "measure-population-exclusion | measure-observation"
        ),
    )

    count: fhirtypes.Integer = Field(
        None,
        alias="count",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Size of the population",
    )

    subjectResults: fhirtypes.ReferenceType = Field(
        None,
        alias="subjectResults",
        title="Type `Reference` referencing `List` (represented as `dict` in JSON)",
        description="For subject-list reports, the subject results in this population",
    )
