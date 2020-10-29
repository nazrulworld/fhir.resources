# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductPharmaceutical
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
import typing

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
        title="The administrable dose form, after necessary reconstitution",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    characteristics: typing.List[
        fhirtypes.MedicinalProductPharmaceuticalCharacteristicsType
    ] = Field(
        None,
        alias="characteristics",
        title="Characteristics e.g. a products onset of action",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    device: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="device",
        title="Accompanying device",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DeviceDefinition"],
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="An identifier for the pharmaceutical medicinal product",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    ingredient: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="ingredient",
        title="Ingredient",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicinalProductIngredient"],
    )

    routeOfAdministration: typing.List[
        fhirtypes.MedicinalProductPharmaceuticalRouteOfAdministrationType
    ] = Field(
        ...,
        alias="routeOfAdministration",
        title=(
            "The path by which the pharmaceutical product is taken into or makes "
            "contact with the body"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    unitOfPresentation: fhirtypes.CodeableConceptType = Field(
        None,
        alias="unitOfPresentation",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
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
        title="A coded characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title="The status of characteristic e.g. assigned or pending",
        description=None,
        # if property is element of this resource.
        element_property=True,
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
        title="Coded expression for the route",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    firstDose: fhirtypes.QuantityType = Field(
        None,
        alias="firstDose",
        title=(
            "The first dose (dose quantity) administered in humans can be "
            "specified, for a product under investigation, using a numerical value "
            "and its unit of measurement"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    maxDosePerDay: fhirtypes.QuantityType = Field(
        None,
        alias="maxDosePerDay",
        title=(
            "The maximum dose per day (maximum dose quantity to be administered in "
            "any one 24-h period) that can be administered as per the protocol "
            "referenced in the clinical trial authorisation"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    maxDosePerTreatmentPeriod: fhirtypes.RatioType = Field(
        None,
        alias="maxDosePerTreatmentPeriod",
        title=(
            "The maximum dose per treatment period that can be administered as per "
            "the protocol referenced in the clinical trial authorisation"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    maxSingleDose: fhirtypes.QuantityType = Field(
        None,
        alias="maxSingleDose",
        title=(
            "The maximum single dose that can be administered as per the protocol "
            "of a clinical trial can be specified using a numerical value and its "
            "unit of measurement"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    maxTreatmentPeriod: fhirtypes.DurationType = Field(
        None,
        alias="maxTreatmentPeriod",
        title=(
            "The maximum treatment period during which an Investigational Medicinal"
            " Product can be administered as per the protocol referenced in the "
            "clinical trial authorisation"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    targetSpecies: typing.List[
        fhirtypes.MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesType
    ] = Field(
        None,
        alias="targetSpecies",
        title="A species for which this route applies",
        description=None,
        # if property is element of this resource.
        element_property=True,
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
        title="Coded expression for the species",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    withdrawalPeriod: typing.List[
        fhirtypes.MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriodType  # noqa: B950
    ] = Field(
        None,
        alias="withdrawalPeriod",
        title=(
            "A species specific time during which consumption of animal product is "
            "not appropriate"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
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
        title="Extra information about the withdrawal period",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    supportingInformation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_supportingInformation",
        title="Extension field for ``supportingInformation``.",
    )

    tissue: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="tissue",
        title=(
            "Coded expression for the type of tissue for which the withdrawal "
            "period applues, e.g. meat, milk"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    value: fhirtypes.QuantityType = Field(
        ...,
        alias="value",
        title="A value for the time",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
