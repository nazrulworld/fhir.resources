# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationAdministration
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType
from typing import Union

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class MedicationAdministration(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Administration of medication to a patient.
    Describes the event of a patient consuming or otherwise being administered
    a medication.  This may be as simple as swallowing a tablet or it may be a
    long running infusion.  Related resources tie this event to the authorizing
    prescription, and the specific encounter between patient and health care
    practitioner.
    """

    resource_type = Field("MedicationAdministration", const=True)

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of medication usage",
    )

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title=(
            "Type `Reference` referencing `Encounter, EpisodeOfCare` (represented "
            "as `dict` in JSON)"
        ),
        description="Encounter or Episode of Care administered as part of",
    )

    device: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="device",
        title=(
            "List of `Reference` items referencing `Device` (represented as `dict` "
            "in JSON)"
        ),
        description="Device used to administer",
    )

    dosage: fhirtypes.MedicationAdministrationDosageType = Field(
        None,
        alias="dosage",
        title="Type `MedicationAdministrationDosage` (represented as `dict` in JSON)",
        description="Details of how medication was taken",
    )

    effectiveDateTime: fhirtypes.DateTime = Field(
        None,
        alias="effectiveDateTime",
        title="Type `DateTime`",
        description="Start and end time of administration",
        one_of_many="effective",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    effectiveDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_effectiveDateTime",
        title="Extension field for ``effectiveDateTime``.",
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Start and end time of administration",
        one_of_many="effective",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    eventHistory: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="eventHistory",
        title=(
            "List of `Reference` items referencing `Provenance` (represented as "
            "`dict` in JSON)"
        ),
        description="A list of events of interest in the lifecycle",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="External identifier",
    )

    instantiates: ListType[fhirtypes.Uri] = Field(
        None,
        alias="instantiates",
        title="List of `Uri` items",
        description="Instantiates protocol or definition",
    )
    instantiates__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_instantiates", title="Extension field for ``instantiates``."
    )

    medicationCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="medicationCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="What was administered",
        one_of_many="medication",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    medicationReference: fhirtypes.ReferenceType = Field(
        None,
        alias="medicationReference",
        title=(
            "Type `Reference` referencing `Medication` (represented as `dict` in "
            "JSON)"
        ),
        description="What was administered",
        one_of_many="medication",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Information about the administration",
    )

    partOf: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title=(
            "List of `Reference` items referencing `MedicationAdministration, "
            "Procedure` (represented as `dict` in JSON)"
        ),
        description="Part of referenced event",
    )

    performer: ListType[fhirtypes.MedicationAdministrationPerformerType] = Field(
        None,
        alias="performer",
        title=(
            "List of `MedicationAdministrationPerformer` items (represented as "
            "`dict` in JSON)"
        ),
        description="Who performed the medication administration and what they did",
    )

    reasonCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Reason administration performed",
    )

    reasonReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title=(
            "List of `Reference` items referencing `Condition, Observation, "
            "DiagnosticReport` (represented as `dict` in JSON)"
        ),
        description=(
            "Condition or observation that supports why the medication was "
            "administered"
        ),
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title=(
            "Type `Reference` referencing `MedicationRequest` (represented as "
            "`dict` in JSON)"
        ),
        description="Request administration performed against",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`",
        description=(
            "in-progress | not-done | on-hold | completed | entered-in-error | "
            "stopped | unknown"
        ),
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    statusReason: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="statusReason",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Reason administration not performed",
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title=(
            "Type `Reference` referencing `Patient, Group` (represented as `dict` "
            "in JSON)"
        ),
        description="Who received medication",
    )

    supportingInformation: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingInformation",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="Additional information to support administration",
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
            "effective": ["effectiveDateTime", "effectivePeriod"],
            "medication": ["medicationCodeableConcept", "medicationReference"],
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


class MedicationAdministrationDosage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details of how medication was taken.
    Describes the medication dosage information details e.g. dose, rate, site,
    route, etc.
    """

    resource_type = Field("MedicationAdministrationDosage", const=True)

    dose: fhirtypes.QuantityType = Field(
        None,
        alias="dose",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Amount of medication per dose",
    )

    method: fhirtypes.CodeableConceptType = Field(
        None,
        alias="method",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="How drug was administered",
    )

    rateQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="rateQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Dose quantity per unit of time",
        one_of_many="rate",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    rateRatio: fhirtypes.RatioType = Field(
        None,
        alias="rateRatio",
        title="Type `Ratio` (represented as `dict` in JSON)",
        description="Dose quantity per unit of time",
        one_of_many="rate",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    route: fhirtypes.CodeableConceptType = Field(
        None,
        alias="route",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Path of substance into body",
    )

    site: fhirtypes.CodeableConceptType = Field(
        None,
        alias="site",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Body site administered to",
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Type `String`",
        description="Free text dosage instructions e.g. SIG",
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
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
        one_of_many_fields = {"rate": ["rateQuantity", "rateRatio"]}
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


class MedicationAdministrationPerformer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who performed the medication administration and what they did.
    Indicates who or what performed the medication administration and how they
    were involved.
    """

    resource_type = Field("MedicationAdministrationPerformer", const=True)

    actor: fhirtypes.ReferenceType = Field(
        ...,
        alias="actor",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole, Patient,"
            " RelatedPerson, Device` (represented as `dict` in JSON)"
        ),
        description="Who performed the medication administration",
    )

    function: fhirtypes.CodeableConceptType = Field(
        None,
        alias="function",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of performance",
    )
