# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationAdministration
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import fhirtypes
from .backboneelement import BackboneElement
from .domainresource import DomainResource


class MedicationAdministration(DomainResource):
    """Administration of medication to a patient.

    Describes the event of a patient consuming or otherwise being administered
    a medication.  This may be as simple as swallowing a tablet or it may be a
    long running infusion.  Related resources tie this event to the authorizing
    prescription, and the specific encounter between patient and health care
    practitioner.
    """

    resource_type = Field("MedicationAdministration", const=True)

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code`.",
        description="in-progress | on-hold | completed | entered-in-error | stopped.",
    )
    wasNotGiven: fhirtypes.Boolean = Field(
        None,
        alias="wasNotGiven",
        title="Type `Boolean`.",
        description="True if medication not administered.",
    )

    note: fhirtypes.String = Field(
        None,
        alias="note",
        title="Type `String`.",
        description="Information about the administration.",
    )

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON).",
        description="Who received medication.",
    )
    practitioner: fhirtypes.ReferenceType = Field(
        None,
        alias="practitioner",
        title=(
            "Type `Reference` referencing `Practitioner, "
            "Patient, RelatedPerson` (represented as `dict` in JSON)."
        ),
        description="Who administered substance.",
    )

    prescription: fhirtypes.ReferenceType = Field(
        None,
        alias="prescription",
        title="Type `Reference` referencing `MedicationOrder` (represented as `dict` in JSON).",
        description="Order administration performed against.",
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Type `Reference` referencing `Encounter` (represented as `dict` in JSON).",
        description="Encounter administered as part of.",
    )

    dosage: fhirtypes.MedicationAdministrationDosageType = Field(
        None,
        alias="dosage",
        title="Type `MedicationAdministrationDosage` (represented as `dict` in JSON).",
        description="Details of how medication was taken.",
    )

    effectiveTimeDateTime: fhirtypes.DateTime = Field(
        None,
        alias="effectiveTimeDateTime",
        title="Type `DateTime`.",
        description="Start and end time of administration.",
        one_of_many="effective",  # Choice of Data Types. i.e reason[x]
        one_of_many_required=False,
    )
    effectiveTimePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectiveTimePeriod",
        title="Type `Period` (represented as `dict` in JSON).",
        description="Start and end time of administration.",
        one_of_many="effective",  # Choice of Data Types. i.e reason[x]
        one_of_many_required=False,
    )

    medicationReference: fhirtypes.ReferenceType = Field(
        None,
        alias="medicationReference",
        title="Type `Reference` referencing `Medication` (represented as `dict` in JSON).",
        description="What was administered.",
        one_of_many="medication",  # Choice of Data Types. i.e medication[x]
        one_of_many_required=False,
    )
    medicationCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="medicationCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="What was administered.",
        one_of_many="medication",  # Choice of Data Types. i.e medication[x]
        one_of_many_required=False,
    )

    device: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="device",
        title="List of `Reference` items referencing `Device` (represented as `dict` in JSON).",
        description="Device used to administer.",
    )
    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON).",
        description="External identifier.",
    )

    reasonGiven: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonGiven",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="Reason administration performed.",
    )

    reasonNotGiven: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonNotGiven",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="Reason administration not performed.",
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
            "effective": ["effectiveTimeDateTime", "effectiveTimePeriod"],
            "medication": ["medicationReference", "medicationCodeableConcept"],
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


class MedicationAdministrationDosage(BackboneElement):
    """Details of how medication was taken.

    Describes the medication dosage information details e.g. dose, rate, site,
    route, etc.
    """

    resource_type = Field("MedicationAdministrationDosage", const=True)

    method: fhirtypes.CodeableConceptType = Field(
        None,
        alias="method",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="How drug was administered.",
    )
    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Type `Quantity` (represented as `dict` in JSON).",
        description="Amount administered in one dose.",
    )

    rateRange: fhirtypes.RangeType = Field(
        None,
        alias="rateRange",
        title="Type `Range` (represented as `dict` in JSON).",
        description="Dose quantity per unit of time.",
        one_of_many="rate",  # Choice of Data Types. i.e reason[x]
        one_of_many_required=False,
    )

    rateRatio: fhirtypes.RatioType = Field(
        None,
        alias="rateRatio",
        title="Type `Ratio` (represented as `dict` in JSON).",
        description="Dose quantity per unit of time.",
        one_of_many="rate",  # Choice of Data Types. i.e reason[x]
        one_of_many_required=False,
    )

    route: fhirtypes.CodeableConceptType = Field(
        None,
        alias="route",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Path of substance into body.",
    )

    siteCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="siteCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Body site administered to.",
        one_of_many="site",  # Choice of Data Types. i.e reason[x]
        one_of_many_required=False,
    )

    siteReference: fhirtypes.ReferenceType = Field(
        None,
        alias="siteReference",
        title="Type `Reference` referencing `BodySite` (represented as `dict` in JSON).",
        description="Body site administered to.",
        one_of_many="site",  # Choice of Data Types. i.e site[x]
        one_of_many_required=False,
    )

    text: fhirtypes.String = Field(
        None, alias="text", title="Type `String`.", description="Dosage Instructions."
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
            "rate": ["rateRatio", "rateRange"],
            "site": ["siteCodeableConcept", "siteReference"],
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
