# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductPharmaceutical
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class MedicinalProductPharmaceutical(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A pharmaceutical product described in terms of its composition and dose
    form.
    """

    resource_type = Field("MedicinalProductPharmaceutical", const=True)

    administrableDoseForm: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="administrableDoseForm",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The administrable dose form, after necessary reconstitution",
    )

    characteristics: ListType[
        fhirtypes.MedicinalProductPharmaceuticalCharacteristicsType
    ] = Field(
        None,
        alias="characteristics",
        title=(
            "List of `MedicinalProductPharmaceuticalCharacteristics` items "
            "(represented as `dict` in JSON)"
        ),
        description="Characteristics e.g. a products onset of action",
    )

    device: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="device",
        title=(
            "List of `Reference` items referencing `DeviceDefinition` (represented "
            "as `dict` in JSON)"
        ),
        description="Accompanying device",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="An identifier for the pharmaceutical medicinal product",
    )

    ingredient: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="ingredient",
        title=(
            "List of `Reference` items referencing `MedicinalProductIngredient` "
            "(represented as `dict` in JSON)"
        ),
        description="Ingredient",
    )

    routeOfAdministration: ListType[
        fhirtypes.MedicinalProductPharmaceuticalRouteOfAdministrationType
    ] = Field(
        ...,
        alias="routeOfAdministration",
        title=(
            "List of `MedicinalProductPharmaceuticalRouteOfAdministration` items "
            "(represented as `dict` in JSON)"
        ),
        description=(
            "The path by which the pharmaceutical product is taken into or makes "
            "contact with the body"
        ),
    )

    unitOfPresentation: fhirtypes.CodeableConceptType = Field(
        None,
        alias="unitOfPresentation",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Todo",
    )


class MedicinalProductPharmaceuticalCharacteristics(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Characteristics e.g. a products onset of action.
    """

    resource_type = Field("MedicinalProductPharmaceuticalCharacteristics", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="A coded characteristic",
    )

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The status of characteristic e.g. assigned or pending",
    )


class MedicinalProductPharmaceuticalRouteOfAdministration(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The path by which the pharmaceutical product is taken into or makes contact
    with the body.
    """

    resource_type = Field(
        "MedicinalProductPharmaceuticalRouteOfAdministration", const=True
    )

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Coded expression for the route",
    )

    firstDose: fhirtypes.QuantityType = Field(
        None,
        alias="firstDose",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description=(
            "The first dose (dose quantity) administered in humans can be "
            "specified, for a product under investigation, using a numerical value "
            "and its unit of measurement"
        ),
    )

    maxDosePerDay: fhirtypes.QuantityType = Field(
        None,
        alias="maxDosePerDay",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description=(
            "The maximum dose per day (maximum dose quantity to be administered in "
            "any one 24-h period) that can be administered as per the protocol "
            "referenced in the clinical trial authorisation"
        ),
    )

    maxDosePerTreatmentPeriod: fhirtypes.RatioType = Field(
        None,
        alias="maxDosePerTreatmentPeriod",
        title="Type `Ratio` (represented as `dict` in JSON)",
        description=(
            "The maximum dose per treatment period that can be administered as per "
            "the protocol referenced in the clinical trial authorisation"
        ),
    )

    maxSingleDose: fhirtypes.QuantityType = Field(
        None,
        alias="maxSingleDose",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description=(
            "The maximum single dose that can be administered as per the protocol "
            "of a clinical trial can be specified using a numerical value and its "
            "unit of measurement"
        ),
    )

    maxTreatmentPeriod: fhirtypes.DurationType = Field(
        None,
        alias="maxTreatmentPeriod",
        title="Type `Duration` (represented as `dict` in JSON)",
        description=(
            "The maximum treatment period during which an Investigational Medicinal"
            " Product can be administered as per the protocol referenced in the "
            "clinical trial authorisation"
        ),
    )

    targetSpecies: ListType[
        fhirtypes.MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesType
    ] = Field(
        None,
        alias="targetSpecies",
        title=(
            "List of "
            "`MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies` "
            "items (represented as `dict` in JSON)"
        ),
        description="A species for which this route applies",
    )


class MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A species for which this route applies.
    """

    resource_type = Field(
        "MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies", const=True
    )

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Coded expression for the species",
    )

    withdrawalPeriod: ListType[
        fhirtypes.MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriodType  # noqa: B950
    ] = Field(
        None,
        alias="withdrawalPeriod",
        title=(
            "List of `MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpec"
            "iesWithdrawalPeriod` items (represented as `dict` in JSON)"
        ),
        description=(
            "A species specific time during which consumption of animal product is "
            "not appropriate"
        ),
    )


class MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A species specific time during which consumption of animal product is not
    appropriate.
    """

    resource_type = Field(
        "MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod",
        const=True,
    )

    supportingInformation: fhirtypes.String = Field(
        None,
        alias="supportingInformation",
        title="Type `String`",
        description="Extra information about the withdrawal period",
    )
    supportingInformation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_supportingInformation",
        title="Extension field for ``supportingInformation``.",
    )

    tissue: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="tissue",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "Coded expression for the type of tissue for which the withdrawal "
            "period applues, e.g. meat, milk"
        ),
    )

    value: fhirtypes.QuantityType = Field(
        ...,
        alias="value",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="A value for the time",
    )
