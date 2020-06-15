# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MarketingStatus
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from pydantic import Field

from . import backboneelement, fhirtypes


class MarketingStatus(backboneelement.BackboneElement):
    """ The marketing status describes the date when a medicinal product is
    actually put on the market or the date as of which it is no longer
    available.
    """

    resource_type = Field("MarketingStatus", const=True)

    country: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="country",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "The country in which the marketing authorisation has been granted "
            "shall be specified It should be specified using the ISO 3166 \u2011 1 "
            "alpha-2 code elements"
        ),
    )

    dateRange: fhirtypes.PeriodType = Field(
        ...,
        alias="dateRange",
        title="Type `Period` (represented as `dict` in JSON)",
        description=(
            "The date when the Medicinal Product is placed on the market by the "
            "Marketing Authorisation Holder (or where applicable, the "
            "manufacturer/distributor) in a country and/or jurisdiction shall be "
            "provided A complete date consisting of day, month and year shall be "
            "specified using the ISO 8601 date format NOTE \u201cPlaced on the market\u201d "
            "refers to the release of the Medicinal Product into the distribution "
            "chain"
        ),
    )

    jurisdiction: fhirtypes.CodeableConceptType = Field(
        None,
        alias="jurisdiction",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "Where a Medicines Regulatory Agency has granted a marketing "
            "authorisation for which specific provisions within a jurisdiction "
            "apply, the jurisdiction can be specified using an appropriate "
            "controlled terminology The controlled term and the controlled term "
            "identifier shall be specified"
        ),
    )

    restoreDate: fhirtypes.DateTime = Field(
        None,
        alias="restoreDate",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description=(
            "The date when the Medicinal Product is placed on the market by the "
            "Marketing Authorisation Holder (or where applicable, the "
            "manufacturer/distributor) in a country and/or jurisdiction shall be "
            "provided A complete date consisting of day, month and year shall be "
            "specified using the ISO 8601 date format NOTE \u201cPlaced on the market\u201d "
            "refers to the release of the Medicinal Product into the distribution "
            "chain"
        ),
    )

    status: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="status",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "This attribute provides information on the status of the marketing of "
            "the medicinal product See ISO/TS 20443 for more information and "
            "examples"
        ),
    )
