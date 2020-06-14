# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Immunization
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Immunization(domainresource.DomainResource):
    """ Immunization event information.
    Describes the event of a patient being administered a vaccine or a record
    of an immunization as reported by a patient, a clinician or another party.
    """

    resource_type = Field("Immunization", const=True)

    doseQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="doseQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Amount of vaccine administered",
    )

    education: ListType[fhirtypes.ImmunizationEducationType] = Field(
        None,
        alias="education",
        title="List of `ImmunizationEducation` items (represented as `dict` in JSON)",
        description="Educational material presented to patient",
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Type `Reference` referencing `Encounter` (represented as `dict` in JSON)",
        description="Encounter immunization was part of",
    )

    expirationDate: fhirtypes.Date = Field(
        None,
        alias="expirationDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="Vaccine expiration date",
    )

    fundingSource: fhirtypes.CodeableConceptType = Field(
        None,
        alias="fundingSource",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Funding source for the vaccine",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business identifier",
    )

    isSubpotent: bool = Field(
        None, alias="isSubpotent", title="Type `bool`", description="Dose potency",
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title="Type `Reference` referencing `Location` (represented as `dict` in JSON)",
        description="Where immunization occurred",
    )

    lotNumber: fhirtypes.String = Field(
        None,
        alias="lotNumber",
        title="Type `String` (represented as `dict` in JSON)",
        description="Vaccine lot number",
    )

    manufacturer: fhirtypes.ReferenceType = Field(
        None,
        alias="manufacturer",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Vaccine manufacturer",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Additional immunization notes",
    )

    occurrenceDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurrenceDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Vaccine administration date",
        one_of_many="occurrence",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    occurrenceString: fhirtypes.String = Field(
        None,
        alias="occurrenceString",
        title="Type `String` (represented as `dict` in JSON)",
        description="Vaccine administration date",
        one_of_many="occurrence",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="Who was immunized",
    )

    performer: ListType[fhirtypes.ImmunizationPerformerType] = Field(
        None,
        alias="performer",
        title="List of `ImmunizationPerformer` items (represented as `dict` in JSON)",
        description="Who performed event",
    )

    primarySource: bool = Field(
        None,
        alias="primarySource",
        title="Type `bool`",
        description="Indicates context the data was recorded in",
    )

    programEligibility: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="programEligibility",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Patient eligibility for a vaccination program",
    )

    protocolApplied: ListType[fhirtypes.ImmunizationProtocolAppliedType] = Field(
        None,
        alias="protocolApplied",
        title="List of `ImmunizationProtocolApplied` items (represented as `dict` in JSON)",
        description="Protocol followed by the provider",
    )

    reaction: ListType[fhirtypes.ImmunizationReactionType] = Field(
        None,
        alias="reaction",
        title="List of `ImmunizationReaction` items (represented as `dict` in JSON)",
        description="Details of a reaction that follows immunization",
    )

    reasonCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Why immunization occurred",
    )

    reasonReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title="List of `Reference` items referencing `Condition, Observation, DiagnosticReport` (represented as `dict` in JSON)",
        description="Why immunization occurred",
    )

    recorded: fhirtypes.DateTime = Field(
        None,
        alias="recorded",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When the immunization was first captured in the subject\u0027s record",
    )

    reportOrigin: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reportOrigin",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Indicates the source of a secondarily reported record",
    )

    route: fhirtypes.CodeableConceptType = Field(
        None,
        alias="route",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="How vaccine entered body",
    )

    site: fhirtypes.CodeableConceptType = Field(
        None,
        alias="site",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Body site vaccine  was administered",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="completed | entered-in-error | not-done",
    )

    statusReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="statusReason",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Reason not done",
    )

    subpotentReason: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="subpotentReason",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Reason for being subpotent",
    )

    vaccineCode: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="vaccineCode",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Vaccine product administered",
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
            "occurrence": ["occurrenceDateTime", "occurrenceString",],
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


class ImmunizationEducation(backboneelement.BackboneElement):
    """ Educational material presented to patient.
    Educational material presented to the patient (or guardian) at the time of
    vaccine administration.
    """

    resource_type = Field("ImmunizationEducation", const=True)

    documentType: fhirtypes.String = Field(
        None,
        alias="documentType",
        title="Type `String` (represented as `dict` in JSON)",
        description="Educational material document identifier",
    )

    presentationDate: fhirtypes.DateTime = Field(
        None,
        alias="presentationDate",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Educational material presentation date",
    )

    publicationDate: fhirtypes.DateTime = Field(
        None,
        alias="publicationDate",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Educational material publication date",
    )

    reference: fhirtypes.Uri = Field(
        None,
        alias="reference",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Educational material reference pointer",
    )


class ImmunizationPerformer(backboneelement.BackboneElement):
    """ Who performed event.
    Indicates who performed the immunization event.
    """

    resource_type = Field("ImmunizationPerformer", const=True)

    actor: fhirtypes.ReferenceType = Field(
        ...,
        alias="actor",
        title="Type `Reference` referencing `Practitioner, PractitionerRole, Organization` (represented as `dict` in JSON)",
        description="Individual or organization who was performing",
    )

    function: fhirtypes.CodeableConceptType = Field(
        None,
        alias="function",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="What type of performance was done",
    )


class ImmunizationProtocolApplied(backboneelement.BackboneElement):
    """ Protocol followed by the provider.
    The protocol (set of recommendations) being followed by the provider who
    administered the dose.
    """

    resource_type = Field("ImmunizationProtocolApplied", const=True)

    authority: fhirtypes.ReferenceType = Field(
        None,
        alias="authority",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Who is responsible for publishing the recommendations",
    )

    doseNumberPositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="doseNumberPositiveInt",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Dose number within series",
        one_of_many="doseNumber",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    doseNumberString: fhirtypes.String = Field(
        None,
        alias="doseNumberString",
        title="Type `String` (represented as `dict` in JSON)",
        description="Dose number within series",
        one_of_many="doseNumber",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    series: fhirtypes.String = Field(
        None,
        alias="series",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of vaccine series",
    )

    seriesDosesPositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="seriesDosesPositiveInt",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Recommended number of doses for immunity",
        one_of_many="seriesDoses",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    seriesDosesString: fhirtypes.String = Field(
        None,
        alias="seriesDosesString",
        title="Type `String` (represented as `dict` in JSON)",
        description="Recommended number of doses for immunity",
        one_of_many="seriesDoses",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    targetDisease: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="targetDisease",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Vaccine preventatable disease being targetted",
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
            "doseNumber": ["doseNumberPositiveInt", "doseNumberString",],
            "seriesDoses": ["seriesDosesPositiveInt", "seriesDosesString",],
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


class ImmunizationReaction(backboneelement.BackboneElement):
    """ Details of a reaction that follows immunization.
    Categorical data indicating that an adverse event is associated in time to
    an immunization.
    """

    resource_type = Field("ImmunizationReaction", const=True)

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When reaction started",
    )

    detail: fhirtypes.ReferenceType = Field(
        None,
        alias="detail",
        title="Type `Reference` referencing `Observation` (represented as `dict` in JSON)",
        description="Additional information on reaction",
    )

    reported: bool = Field(
        None,
        alias="reported",
        title="Type `bool`",
        description="Indicates self-reported reaction",
    )
