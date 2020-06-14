# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductUndesirableEffect
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import domainresource, fhirtypes


class MedicinalProductUndesirableEffect(domainresource.DomainResource):
    """ MedicinalProductUndesirableEffect.
    Describe the undesirable effects of the medicinal product.
    """

    resource_type = Field("MedicinalProductUndesirableEffect", const=True)

    classification: fhirtypes.CodeableConceptType = Field(
        None,
        alias="classification",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Classification of the effect",
    )

    frequencyOfOccurrence: fhirtypes.CodeableConceptType = Field(
        None,
        alias="frequencyOfOccurrence",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The frequency of occurrence of the effect",
    )

    population: ListType[fhirtypes.PopulationType] = Field(
        None,
        alias="population",
        title="List of `Population` items (represented as `dict` in JSON)",
        description="The population group to which this applies",
    )

    subject: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="subject",
        title="List of `Reference` items referencing `MedicinalProduct, Medication` (represented as `dict` in JSON)",
        description="The medication for which this is an indication",
    )

    symptomConditionEffect: fhirtypes.CodeableConceptType = Field(
        None,
        alias="symptomConditionEffect",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The symptom, condition or undesirable effect",
    )
