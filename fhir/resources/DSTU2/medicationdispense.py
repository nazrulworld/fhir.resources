# -*- coding: utf-8 -*-
"""
Profile: https://www.hl7.org/fhir/DSTU2/medicationdispense.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class MedicationDispense(domainresource.DomainResource):
    """Dispensing a medication to a named patient.

    Indicates that a medication product is to be or has been dispensed for a
    named person/patient.  This includes a description of the medication
    product (supply) provided and the instructions for administering the
    medication.  The medication dispense is the result of a pharmacy system
    responding to a medication order.
    """

    resource_type = Field("MedicationDispense", const=True)

    authorizingPrescription: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="authorizingPrescription",
        title="Medication order that authorizes the dispense",
        description="Indicates the medication order that is being dispensed against.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicationOrder"],
    )

    daysSupply: fhirtypes.QuantityType = Field(
        None,
        alias="daysSupply",
        title="Amount of medication expressed as a timing amount",
        description="The amount of medication expressed as a timing amount.",
    )

    destination: fhirtypes.ReferenceType = Field(
        None,
        alias="destination",
        title="Where the medication was sent",
        description=(
            "Identification of the facility/location where the medication was "
            "shipped to, as part of the dispense event."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    dispenser: fhirtypes.ReferenceType = Field(
        None,
        alias="dispenser",
        title=(
            "Type `Reference` referencing `Practitioner` (represented as `dict` in "
            "JSON)."
        ),
        description="Practitioner responsible for dispensing medication.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    dosageInstruction: ListType[
        fhirtypes.MedicationDispenseDosageInstructionType
    ] = Field(
        None,
        alias="dosageInstruction",
        title=(
            "How the medication is to be used by the patient or administered by the"
            " caregiver"
        ),
        description="Indicates how the medication is to be used by the patient.",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="External identifier",
        description=(
            "Identifiers associated with this Medication Dispense that are defined "
            "by business processes and/or used to refer to it when a direct URL "
            "reference to the resource itself is not appropriate. They are business"
            " identifiers assigned to this resource by the performer or other "
            "systems and remain constant as the resource is updated and propagates "
            "from server to server."
        ),
    )

    medicationCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="medicationCodeableConcept",
        title="What medication was supplied",
        description=(
            "Identifies the medication being administered. This is either a link to"
            " a resource representing the details of the medication or a simple "
            "attribute carrying a code that identifies the medication from a known "
            "list of medications."
        ),
        # Choice of Data Types. i.e medication[x]
        one_of_many="medication",
        one_of_many_required=True,
    )

    medicationReference: fhirtypes.ReferenceType = Field(
        None,
        alias="medicationReference",
        title="What medication was supplied",
        description=(
            "Identifies the medication being administered. This is either a link to"
            " a resource representing the details of the medication or a simple "
            "attribute carrying a code that identifies the medication from a known "
            "list of medications."
        ),
        # Choice of Data Types. i.e medication[x]
        one_of_many="medication",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Medication"],
    )

    note: fhirtypes.String = Field(
        None,
        alias="note",
        title="Information about the dispense",
        description=(
            "Extra information about the dispense that could not be conveyed in the"
            " other attributes."
        ),
    )

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="Who the dispense is for",
        description=(
            "A link to a resource representing the person or the group to whom the "
            "medication will be given."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Amount dispensed",
        description=(
            "The amount of medication that has been dispensed. Includes unit of "
            "measure."
        ),
    )

    receiver: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="receiver",
        title="Who collected the medication",
        description=(
            "Identifies the person who picked up the medication.  This will usually"
            " be a patient or their caregiver, but some cases exist where it can be"
            " a healthcare professional."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Practitioner"],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="in-progress | on-hold | completed | entered-in-error | stopped",
        description="A code specifying the state of the set of dispense events.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "in-progress",
            "on-hold",
            "completed",
            "entered-in-error",
            "stopped",
        ],
    )

    substitution: fhirtypes.MedicationDispenseSubstitutionType = Field(
        None,
        alias="substitution",
        title="Whether a substitution was performed on the dispense",
        description=(
            "Indicates whether or not substitution was made as part of the "
            "dispense.  In some cases, substitution will be expected but does not "
            "happen, in other cases substitution is not expected but does happen.  "
            "This block explains what substitution did or did not happen and why.  "
            "If nothing is specified, substitution was not done."
        ),
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Trial fill, partial fill, emergency fill, etc.",
        description=(
            "Indicates the type of dispensing event that is performed. For example,"
            " Trial Fill, Completion of Trial, Partial Fill, Emergency Fill, "
            "Samples, etc."
        ),
    )

    whenHandedOver: fhirtypes.DateTime = Field(
        None,
        alias="whenHandedOver",
        title="When product was given out",
        description=(
            "The time the dispensed product was provided to the patient or their "
            "representative."
        ),
    )

    whenPrepared: fhirtypes.DateTime = Field(
        None,
        alias="whenPrepared",
        title="When product was packaged and reviewed",
        description="The time when the dispensed product was packaged and reviewed.",
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


class MedicationDispenseDosageInstruction(backboneelement.BackboneElement):
    """Medicine administration instructions to the patient/caregiver.

    Indicates how the medication is to be used by the patient.
    """

    resource_type = Field("MedicationDispenseDosageInstruction", const=True)

    additionalInstructions: fhirtypes.CodeableConceptType = Field(
        None,
        alias="additionalInstructions",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description='E.g. "Take with food".',
    )

    asNeededBoolean: fhirtypes.Boolean = Field(
        None,
        alias="asNeededBoolean",
        title="Type `bool`.",
        description='Take "as needed" f(or x).',
        # Choice of Data Types. i.e asNeeded[x]
        one_of_many="asNeeded",
        one_of_many_required=False,
    )

    asNeededCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="asNeededCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description='Take "as needed" f(or x).',
        # Choice of Data Types. i.e asNeeded[x]
        one_of_many="asNeeded",
        one_of_many_required=False,
    )

    doseQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="doseQuantity",
        title=(
            "Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in "
            "JSON)."
        ),
        description="Amount of medication per dose.",
        # Choice of Data Types. i.e dose[x]
        one_of_many="dose",
        one_of_many_required=False,
    )

    doseRange: fhirtypes.RangeType = Field(
        None,
        alias="doseRange",
        title="Type `Range` (represented as `dict` in JSON).",
        description="Amount of medication per dose.",
        # Choice of Data Types. i.e dose[x]
        one_of_many="dose",
        one_of_many_required=False,
    )

    maxDosePerPeriod: fhirtypes.RatioType = Field(
        None,
        alias="maxDosePerPeriod",
        title="Type `Ratio` (represented as `dict` in JSON).",
        description="Upper limit on medication per unit of time.",
    )

    method: fhirtypes.CodeableConceptType = Field(
        None,
        alias="method",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Technique for administering medication.",
    )

    rateRange: fhirtypes.RatioType = Field(
        None,
        alias="rateRange",
        title="Type `Range` (represented as `dict` in JSON).",
        description="Amount of medication per unit of time.",
        # Choice of Data Types. i.e rate[x]
        one_of_many="rate",
        one_of_many_required=False,
    )

    rateRatio: fhirtypes.RangeType = Field(
        None,
        alias="rateRatio",
        title="Type `Ratio` (represented as `dict` in JSON).",
        description="Amount of medication per unit of time.",
        # Choice of Data Types. i.e rate[x]
        one_of_many="rate",
        one_of_many_required=False,
    )

    route: fhirtypes.CodeableConceptType = Field(
        None,
        alias="route",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="How drug should enter body.",
    )

    siteCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="siteCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Body site to administer to.",
        # Choice of Data Types. i.e site[x]
        one_of_many="site",
        one_of_many_required=False,
    )

    siteReference: fhirtypes.ReferenceType = Field(
        None,
        alias="siteReference",
        title=(
            "Type `Reference` referencing `BodySite` (represented as `dict` in JSON)."
        ),
        description="Body site to administer to.",
        # Choice of Data Types. i.e site[x]
        one_of_many="site",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["BodySite"],
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Type `str`.",
        description="Dosage Instructions.",
    )

    timing: fhirtypes.TimingType = Field(
        None,
        alias="timing",
        title="Type `Timing` (represented as `dict` in JSON).",
        description="When medication should be administered.",
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
            "dose": ["doseQuantity", "doseRange"],
            "rate": ["rateRange", "rateRatio"],
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


class MedicationDispenseSubstitution(backboneelement.BackboneElement):
    """Whether a substitution was performed on the dispense.

    Indicates whether or not substitution was made as part of the dispense.  In
    some cases, substitution will be expected but does not happen, in other
    cases substitution is not expected but does happen.  This block explains
    what substitution did or did not happen and why.  If nothing is specified,
    substitution was not done.
    """

    resource_type = Field("MedicationDispenseSubstitution", const=True)

    reason: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reason",
        title="Why was substitution made",
        description=(
            "Indicates the reason for the substitution (or lack of substitution) "
            "from what was prescribed."
        ),
    )

    responsibleParty: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="responsibleParty",
        title="Who is responsible for the substitution",
        description=(
            "The person or organization that has primary responsibility for the "
            "substitution."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title=(
            "Code signifying whether a different drug was dispensed from what was "
            "prescribed"
        ),
        description=(
            "A code signifying whether a different drug was dispensed from what was"
            " prescribed."
        ),
    )
