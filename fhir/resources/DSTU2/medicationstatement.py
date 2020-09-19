# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationStatement
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


class MedicationStatement(DomainResource):
    """Record of medication being taken by a patient.

        A record of a medication that is being consumed by a patient.   A
        MedicationStatement may indicate that the patient may be taking the
        medication now, or has taken the medication in the past or will be taking
        the medication in the future.  The source of this information can be the
        patient, significant other (such as a family member or spouse), or a
        clinician.  A common scenario where this information is captured is during
        the history taking process during a patient visit or stay.   The medication
        information may come from e.g. the patient's memory, from a prescription
        bottle,  or from a list of medications the patient, clinician or other
        party maintains

    The primary difference between a medication statement and
        a medication administration is that the medication administration has
        complete administration information and is based on actual administration
        information from the person who administered the medication.  A medication
        statement is often, if not always, less specific.  There is no required
        date/time when the medication was administered, in fact we only know that a
        source has reported the patient is taking this medication, where details
        such as time, quantity, or rate or even medication product may be
        incomplete or missing or less precise.  As stated earlier, the medication
        statement information may come from the patient's memory, from a
        prescription bottle or from a list of medications the patient, clinician or
        other party maintains.  Medication administration is more formal and is not
        missing detailed information.
    """

    resource_type = Field("MedicationStatement", const=True)

    wasNotTaken: fhirtypes.Boolean = Field(
        None,
        alias="wasNotTaken",
        title="Type `bool`.",
        description="True if medication is/was not being taken.",
    )
    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`.",
        description="active | completed | entered-in-error | intended.",
    )
    note: fhirtypes.Code = Field(
        None,
        alias="note",
        title="Type `String`.",
        description="Further information about the statement.",
    )

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON).",
        description="Who is/was taking  the medication.",
    )

    dateAsserted: fhirtypes.DateTime = Field(
        None,
        alias="dateAsserted",
        title="Type `DateTime`.",
        description="When the statement was asserted?.",
    )
    effectiveDateTime: fhirtypes.DateTime = Field(
        None,
        alias="effectiveDateTime",
        title="Type `DateTime`.",
        description="Over what period was medication consumed?.",
        one_of_many="effective",  # Choice of Data Types. i.e effective[x]
        one_of_many_required=False,
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="Type `Period` (represented as `dict` in JSON).",
        description="Over what period was medication consumed?.",
        one_of_many="effective",  # Choice of Data Types. i.e effective[x]
        one_of_many_required=False,
    )

    informationSource: fhirtypes.ReferenceType = Field(
        None,
        alias="informationSource",
        title=(
            "Type `Reference` referencing `Patient, Practitioner, "
            "RelatedPerson` (represented as `dict` in JSON)."
        ),
        description=None,
    )

    medicationReference: fhirtypes.ReferenceType = Field(
        None,
        alias="medicationReference",
        title="Type `Reference` referencing `Medication` (represented as `dict` in JSON).",
        description="What medication was taken.",
        one_of_many="medication",  # Choice of Data Types. i.e medication[x]
        one_of_many_required=False,
    )

    medicationCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="medicationCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="What medication was taken.",
        one_of_many="medication",  # Choice of Data Types. i.e medication[x]
        one_of_many_required=False,
    )

    reasonForUseCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reasonForUseCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description=None,
        one_of_many="reasonForUse",  # Choice of Data Types. i.e reasonForUse[x]
        one_of_many_required=False,
    )

    reasonForUseReference: fhirtypes.ReferenceType = Field(
        None,
        alias="reasonForUseReference",
        title="Type `Reference` referencing `Condition` (represented as `dict` in JSON).",
        description=None,
        one_of_many="reasonForUse",  # Choice of Data Types. i.e reasonForUse[x]
        one_of_many_required=False,
    )
    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON).",
        description="External identifier.",
    )

    dosage: ListType[fhirtypes.MedicationStatementDosageType] = Field(
        None,
        alias="dosage",
        title="List of `MedicationStatementDosage` items (represented as `dict` in JSON).",
        description="Details of how medication was taken.",
    )

    reasonNotTaken: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonNotTaken",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="True if asserting medication was not given.",
    )

    supportingInformation: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingInformation",
        title=(
            "List of `Reference` items referencing "
            "`Resource` (represented as `dict` in JSON)."
        ),
        description="Additional supporting information.",
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
            "reasonForUse": ["reasonForUseCodeableConcept", "reasonForUseReference"],
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


class MedicationStatementDosage(BackboneElement):
    """Details of how medication was taken.

    Indicates how the medication is/was used by the patient.
    """

    resource_type = Field("MedicationStatementDosage", const=True)

    asNeededBoolean: fhirtypes.Boolean = Field(
        None,
        alias="asNeededBoolean",
        title="Type `bool`.",
        description="Take 'as needed' (for x).",
        one_of_many="asNeeded",  # Choice of Data Types. i.e asNeeded[x]
        one_of_many_required=False,
    )
    asNeededCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="asNeededCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Take 'as needed' (for x).",
        one_of_many="asNeeded",  # Choice of Data Types. i.e asNeeded[x]
        one_of_many_required=False,
    )

    maxDosePerPeriod: fhirtypes.RatioType = Field(
        None,
        alias="maxDosePerPeriod",
        title="Type `Ratio` (represented as `dict` in JSON).",
        description="Maximum dose that was consumed per unit of time.",
    )

    method: fhirtypes.CodeableConceptType = Field(
        None,
        alias="method",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Technique used to administer medication.",
    )
    quantityQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantityQuantity",
        title="Type `quantityQuantity` (represented as `dict` in JSON).",
        description="Amount administered in one dose.",
        one_of_many="quantity",  # Choice of Data Types. i.e quantity[x]
        one_of_many_required=False,
    )

    quantityRange: fhirtypes.RangeType = Field(
        None,
        alias="quantityRange",
        title="Type `Range` (represented as `dict` in JSON).",
        description="Amount administered in one dose.",
        one_of_many="quantity",  # Choice of Data Types. i.e quantity[x]
        one_of_many_required=False,
    )

    rateRange: fhirtypes.RangeType = Field(
        None,
        alias="rateRange",
        title="Type `Range` (represented as `dict` in JSON).",
        description="Dose quantity per unit of time.",
        one_of_many="rate",  # Choice of Data Types. i.e rate[x]
        one_of_many_required=False,
    )

    rateRatio: fhirtypes.RatioType = Field(
        None,
        alias="rateRatio",
        title="Type `Ratio` (represented as `dict` in JSON).",
        description="Dose quantity per unit of time.",
        one_of_many="rate",  # Choice of Data Types. i.e rate[x]
        one_of_many_required=False,
    )

    route: fhirtypes.CodeableConceptType = Field(
        None,
        alias="route",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="How the medication entered the body.",
    )

    siteCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="siteCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Where (on body) medication is/was administered.",
        one_of_many="site",  # Choice of Data Types. i.e site[x]
        one_of_many_required=False,
    )

    siteReference: fhirtypes.ReferenceType = Field(
        None,
        alias="siteReference",
        title="Type `Reference` referencing `BodySite` (represented as `dict` in JSON).",
        description="Where (on body) medication is/was administered.",
        one_of_many="site",  # Choice of Data Types. i.e site[x]
        one_of_many_required=False,
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Type `String`",
        description="Reported dosage information.",
    )

    timing: fhirtypes.TimingType = Field(
        None,
        alias="timing",
        title="Type `Timing` (represented as `dict` in JSON).",
        description="When/how often was medication taken.",
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
            "asNeeded": ["asNeededBoolean", "asNeededCodeableConcept"],
            "site": ["siteCodeableConcept", "siteReference"],
            "quantity": ["quantityQuantity", "quantityRange"],
            "rate": ["rateRatio", "rateRange"],
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
