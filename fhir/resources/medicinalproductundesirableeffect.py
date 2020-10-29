# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductUndesirableEffect
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
import typing

from pydantic import Field

from . import domainresource, fhirtypes


class MedicinalProductUndesirableEffect(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    MedicinalProductUndesirableEffect.
    Describe the undesirable effects of the medicinal product.
    """

    resource_type = Field("MedicinalProductUndesirableEffect", const=True)

    classification: fhirtypes.CodeableConceptType = Field(
        None,
        alias="classification",
        title="Classification of the effect",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    frequencyOfOccurrence: fhirtypes.CodeableConceptType = Field(
        None,
        alias="frequencyOfOccurrence",
        title="The frequency of occurrence of the effect",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    population: typing.List[fhirtypes.PopulationType] = Field(
        None,
        alias="population",
        title="The population group to which this applies",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    subject: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="subject",
        title="The medication for which this is an indication",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicinalProduct", "Medication"],
    )

    symptomConditionEffect: fhirtypes.CodeableConceptType = Field(
        None,
        alias="symptomConditionEffect",
        title="The symptom, condition or undesirable effect",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
