# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MarketingStatus
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1 import Field

from . import backboneelement, fhirtypes


class MarketingStatus(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The marketing status describes the date when a medicinal product is
    actually put on the market or the date as of which it is no longer
    available.
    """

    resource_type = Field("MarketingStatus", const=True)

    country: fhirtypes.CodeableConceptType = Field(
        None,
        alias="country",
        title=(
            "The country in which the marketing authorisation has been granted "
            "shall be specified It should be specified using the ISO 3166 \u2011 1 "
            "alpha-2 code elements"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    dateRange: fhirtypes.PeriodType = Field(
        None,
        alias="dateRange",
        title=(
            "The date when the Medicinal Product is placed on the market by the "
            "Marketing Authorisation Holder (or where applicable, the "
            "manufacturer/distributor) in a country and/or jurisdiction shall be "
            "provided A complete date consisting of day, month and year shall be "
            "specified using the ISO 8601 date format NOTE \u201cPlaced on the market\u201d "
            "refers to the release of the Medicinal Product into the distribution "
            "chain"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    jurisdiction: fhirtypes.CodeableConceptType = Field(
        None,
        alias="jurisdiction",
        title=(
            "Where a Medicines Regulatory Agency has granted a marketing "
            "authorisation for which specific provisions within a jurisdiction "
            "apply, the jurisdiction can be specified using an appropriate "
            "controlled terminology The controlled term and the controlled term "
            "identifier shall be specified"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    restoreDate: fhirtypes.DateTime = Field(
        None,
        alias="restoreDate",
        title=(
            "The date when the Medicinal Product is placed on the market by the "
            "Marketing Authorisation Holder (or where applicable, the "
            "manufacturer/distributor) in a country and/or jurisdiction shall be "
            "provided A complete date consisting of day, month and year shall be "
            "specified using the ISO 8601 date format NOTE \u201cPlaced on the market\u201d "
            "refers to the release of the Medicinal Product into the distribution "
            "chain"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    restoreDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_restoreDate", title="Extension field for ``restoreDate``."
    )

    status: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="status",
        title=(
            "This attribute provides information on the status of the marketing of "
            "the medicinal product See ISO/TS 20443 for more information and "
            "examples"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MarketingStatus`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "country",
            "jurisdiction",
            "status",
            "dateRange",
            "restoreDate",
        ]
