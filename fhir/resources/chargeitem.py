# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ChargeItem
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class ChargeItem(domainresource.DomainResource):
    """ Item containing charge code(s) associated with the provision of healthcare
    provider products.
    The resource ChargeItem describes the provision of healthcare provider
    products for a certain patient, therefore referring not only to the
    product, but containing in addition details of the provision, like date,
    time, amounts and participating organizations and persons. Main Usage of
    the ChargeItem is to enable the billing process and internal cost
    allocation.
    """

    resource_type = Field("ChargeItem", const=True)

    account: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="account",
        title="List of `Reference` items referencing `Account` (represented as `dict` in JSON)",
        description="Account to place this charge",
    )

    bodysite: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="bodysite",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Anatomical location, if relevant",
    )

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="A code that identifies the charge, like a billing code",
    )

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title="Type `Reference` referencing `Encounter, EpisodeOfCare` (represented as `dict` in JSON)",
        description="Encounter / Episode associated with event",
    )

    costCenter: fhirtypes.ReferenceType = Field(
        None,
        alias="costCenter",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Organization that has ownership of the (potential, future) revenue",
    )

    definitionCanonical: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="definitionCanonical",
        title="List of `Canonical` items referencing `ChargeItemDefinition` (represented as `dict` in JSON)",
        description="Resource defining the code of this ChargeItem",
    )

    definitionUri: ListType[fhirtypes.Uri] = Field(
        None,
        alias="definitionUri",
        title="List of `Uri` items (represented as `dict` in JSON)",
        description="Defining information about the code of this charge item",
    )

    enteredDate: fhirtypes.DateTime = Field(
        None,
        alias="enteredDate",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date the charge item was entered",
    )

    enterer: fhirtypes.ReferenceType = Field(
        None,
        alias="enterer",
        title="Type `Reference` referencing `Practitioner, PractitionerRole, Organization, Patient, Device, RelatedPerson` (represented as `dict` in JSON)",
        description="Individual who was entering",
    )

    factorOverride: fhirtypes.Decimal = Field(
        None,
        alias="factorOverride",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Factor overriding the associated rules",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business Identifier for item",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Comments made about the ChargeItem",
    )

    occurrenceDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurrenceDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When the charged service was applied",
        one_of_many="occurrence",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    occurrencePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="occurrencePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When the charged service was applied",
        one_of_many="occurrence",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    occurrenceTiming: fhirtypes.TimingType = Field(
        None,
        alias="occurrenceTiming",
        title="Type `Timing` (represented as `dict` in JSON)",
        description="When the charged service was applied",
        one_of_many="occurrence",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    overrideReason: fhirtypes.String = Field(
        None,
        alias="overrideReason",
        title="Type `String` (represented as `dict` in JSON)",
        description="Reason for overriding the list price/factor",
    )

    partOf: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title="List of `Reference` items referencing `ChargeItem` (represented as `dict` in JSON)",
        description="Part of referenced ChargeItem",
    )

    performer: ListType[fhirtypes.ChargeItemPerformerType] = Field(
        None,
        alias="performer",
        title="List of `ChargeItemPerformer` items (represented as `dict` in JSON)",
        description="Who performed charged service",
    )

    performingOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="performingOrganization",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Organization providing the charged service",
    )

    priceOverride: fhirtypes.MoneyType = Field(
        None,
        alias="priceOverride",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Price overriding the associated rules",
    )

    productCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="productCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Product charged",
        one_of_many="product",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    productReference: fhirtypes.ReferenceType = Field(
        None,
        alias="productReference",
        title="Type `Reference` referencing `Device, Medication, Substance` (represented as `dict` in JSON)",
        description="Product charged",
        one_of_many="product",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Quantity of which the charge item has been serviced",
    )

    reason: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reason",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Why was the charged  service rendered?",
    )

    requestingOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="requestingOrganization",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Organization requesting the charged service",
    )

    service: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="service",
        title="List of `Reference` items referencing `DiagnosticReport, ImagingStudy, Immunization, MedicationAdministration, MedicationDispense, Observation, Procedure, SupplyDelivery` (represented as `dict` in JSON)",
        description="Which rendered service is being charged?",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="planned | billable | not-billable | aborted | billed | entered-in-error | unknown",
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Type `Reference` referencing `Patient, Group` (represented as `dict` in JSON)",
        description="Individual service was done for/to",
    )

    supportingInformation: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingInformation",
        title="List of `Reference` items referencing `Resource` (represented as `dict` in JSON)",
        description="Further information supporting this charge",
    )

    @root_validator(pre=True)
    def validate_one_of_many(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "occurrence": [
                "occurrenceDateTime",
                "occurrencePeriod",
                "occurrenceTiming",
            ],
            "product": ["productCodeableConcept", "productReference",],
        }
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values


class ChargeItemPerformer(backboneelement.BackboneElement):
    """ Who performed charged service.
    Indicates who or what performed or participated in the charged service.
    """

    resource_type = Field("ChargeItemPerformer", const=True)

    actor: fhirtypes.ReferenceType = Field(
        ...,
        alias="actor",
        title="Type `Reference` referencing `Practitioner, PractitionerRole, Organization, CareTeam, Patient, Device, RelatedPerson` (represented as `dict` in JSON)",
        description="Individual who was performing",
    )

    function: fhirtypes.CodeableConceptType = Field(
        None,
        alias="function",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="What type of performance was done",
    )
