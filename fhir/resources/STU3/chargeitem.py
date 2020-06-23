# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ChargeItem
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType
from typing import Union

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class ChargeItem(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Item containing charge code(s) associated with the provision of healthcare
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
        title=(
            "List of `Reference` items referencing `Account` (represented as `dict`"
            " in JSON)"
        ),
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
        title=(
            "Type `Reference` referencing `Encounter, EpisodeOfCare` (represented "
            "as `dict` in JSON)"
        ),
        description="Encounter / Episode associated with event",
    )

    definition: ListType[fhirtypes.Uri] = Field(
        None,
        alias="definition",
        title="List of `Uri` items",
        description="Defining information about the code of this charge item",
    )
    definition__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_definition", title="Extension field for ``definition``.")

    enteredDate: fhirtypes.DateTime = Field(
        None,
        alias="enteredDate",
        title="Type `DateTime`",
        description="Date the charge item was entered",
    )
    enteredDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_enteredDate", title="Extension field for ``enteredDate``."
    )

    enterer: fhirtypes.ReferenceType = Field(
        None,
        alias="enterer",
        title=(
            "Type `Reference` referencing `Practitioner, Organization, Patient, "
            "Device, RelatedPerson` (represented as `dict` in JSON)"
        ),
        description="Individual who was entering",
    )

    factorOverride: fhirtypes.Decimal = Field(
        None,
        alias="factorOverride",
        title="Type `Decimal`",
        description="Factor overriding the associated rules",
    )
    factorOverride__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_factorOverride", title="Extension field for ``factorOverride``."
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
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
        title="Type `DateTime`",
        description="When the charged service was applied",
        one_of_many="occurrence",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_occurrenceDateTime",
        title="Extension field for ``occurrenceDateTime``.",
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
        title="Type `String`",
        description="Reason for overriding the list price/factor",
    )
    overrideReason__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_overrideReason", title="Extension field for ``overrideReason``."
    )

    partOf: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title=(
            "List of `Reference` items referencing `ChargeItem` (represented as "
            "`dict` in JSON)"
        ),
        description="Part of referenced ChargeItem",
    )

    participant: ListType[fhirtypes.ChargeItemParticipantType] = Field(
        None,
        alias="participant",
        title="List of `ChargeItemParticipant` items (represented as `dict` in JSON)",
        description="Who performed charged service",
    )

    performingOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="performingOrganization",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Organization providing the charged sevice",
    )

    priceOverride: fhirtypes.MoneyType = Field(
        None,
        alias="priceOverride",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Price overriding the associated rules",
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
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Organization requesting the charged service",
    )

    service: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="service",
        title=(
            "List of `Reference` items referencing `DiagnosticReport, ImagingStudy,"
            " Immunization, MedicationAdministration, MedicationDispense, "
            "Observation, Procedure, SupplyDelivery` (represented as `dict` in "
            "JSON)"
        ),
        description="Which rendered service is being charged?",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`",
        description=(
            "planned | billable | not-billable | aborted | billed | entered-in-"
            "error | unknown"
        ),
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title=(
            "Type `Reference` referencing `Patient, Group` (represented as `dict` "
            "in JSON)"
        ),
        description="Individual service was done for/to",
    )

    supportingInformation: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingInformation",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="Further information supporting the this charge",
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
            "occurrence": ["occurrenceDateTime", "occurrencePeriod", "occurrenceTiming"]
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


class ChargeItemParticipant(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who performed charged service.
    Indicates who or what performed or participated in the charged service.
    """

    resource_type = Field("ChargeItemParticipant", const=True)

    actor: fhirtypes.ReferenceType = Field(
        ...,
        alias="actor",
        title=(
            "Type `Reference` referencing `Practitioner, Organization, Patient, "
            "Device, RelatedPerson` (represented as `dict` in JSON)"
        ),
        description="Individual who was performing",
    )

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="What type of performance was done",
    )
