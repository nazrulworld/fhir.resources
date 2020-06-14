# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Procedure
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Procedure(domainresource.DomainResource):
    """ An action that is being or was performed on a patient.
    An action that is or was performed on or for a patient. This can be a
    physical intervention like an operation, or less invasive like long term
    services, counseling, or hypnotherapy.
    """

    resource_type = Field("Procedure", const=True)

    asserter: fhirtypes.ReferenceType = Field(
        None,
        alias="asserter",
        title="Type `Reference` referencing `Patient, RelatedPerson, Practitioner, PractitionerRole` (represented as `dict` in JSON)",
        description="Person who asserts this procedure",
    )

    basedOn: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="List of `Reference` items referencing `CarePlan, ServiceRequest` (represented as `dict` in JSON)",
        description="A request for this procedure",
    )

    bodySite: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="bodySite",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Target body sites",
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Classification of the procedure",
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Identification of the procedure",
    )

    complication: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="complication",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Complication following the procedure",
    )

    complicationDetail: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="complicationDetail",
        title="List of `Reference` items referencing `Condition` (represented as `dict` in JSON)",
        description="A condition that is a result of the procedure",
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Type `Reference` referencing `Encounter` (represented as `dict` in JSON)",
        description="Encounter created as part of",
    )

    focalDevice: ListType[fhirtypes.ProcedureFocalDeviceType] = Field(
        None,
        alias="focalDevice",
        title="List of `ProcedureFocalDevice` items (represented as `dict` in JSON)",
        description="Manipulated, implanted, or removed device",
    )

    followUp: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="followUp",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Instructions for follow up",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="External Identifiers for this procedure",
    )

    instantiatesCanonical: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="instantiatesCanonical",
        title="List of `Canonical` items referencing `PlanDefinition, ActivityDefinition, Measure, OperationDefinition, Questionnaire` (represented as `dict` in JSON)",
        description="Instantiates FHIR protocol or definition",
    )

    instantiatesUri: ListType[fhirtypes.Uri] = Field(
        None,
        alias="instantiatesUri",
        title="List of `Uri` items (represented as `dict` in JSON)",
        description="Instantiates external protocol or definition",
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title="Type `Reference` referencing `Location` (represented as `dict` in JSON)",
        description="Where the procedure happened",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Additional information about the procedure",
    )

    outcome: fhirtypes.CodeableConceptType = Field(
        None,
        alias="outcome",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The result of procedure",
    )

    partOf: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title="List of `Reference` items referencing `Procedure, Observation, MedicationAdministration` (represented as `dict` in JSON)",
        description="Part of referenced event",
    )

    performedAge: fhirtypes.AgeType = Field(
        None,
        alias="performedAge",
        title="Type `Age` (represented as `dict` in JSON)",
        description="When the procedure was performed",
        one_of_many="performed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    performedDateTime: fhirtypes.DateTime = Field(
        None,
        alias="performedDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When the procedure was performed",
        one_of_many="performed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    performedPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="performedPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When the procedure was performed",
        one_of_many="performed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    performedRange: fhirtypes.RangeType = Field(
        None,
        alias="performedRange",
        title="Type `Range` (represented as `dict` in JSON)",
        description="When the procedure was performed",
        one_of_many="performed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    performedString: fhirtypes.String = Field(
        None,
        alias="performedString",
        title="Type `String` (represented as `dict` in JSON)",
        description="When the procedure was performed",
        one_of_many="performed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    performer: ListType[fhirtypes.ProcedurePerformerType] = Field(
        None,
        alias="performer",
        title="List of `ProcedurePerformer` items (represented as `dict` in JSON)",
        description="The people who performed the procedure",
    )

    reasonCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Coded reason procedure performed",
    )

    reasonReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title="List of `Reference` items referencing `Condition, Observation, Procedure, DiagnosticReport, DocumentReference` (represented as `dict` in JSON)",
        description="The justification that the procedure was performed",
    )

    recorder: fhirtypes.ReferenceType = Field(
        None,
        alias="recorder",
        title="Type `Reference` referencing `Patient, RelatedPerson, Practitioner, PractitionerRole` (represented as `dict` in JSON)",
        description="Who recorded the procedure",
    )

    report: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="report",
        title="List of `Reference` items referencing `DiagnosticReport, DocumentReference, Composition` (represented as `dict` in JSON)",
        description="Any report resulting from the procedure",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown",
    )

    statusReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="statusReason",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Reason for current status",
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Type `Reference` referencing `Patient, Group` (represented as `dict` in JSON)",
        description="Who the procedure was performed on",
    )

    usedCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="usedCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Coded items used during the procedure",
    )

    usedReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="usedReference",
        title="List of `Reference` items referencing `Device, Medication, Substance` (represented as `dict` in JSON)",
        description="Items used during procedure",
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
            "performed": [
                "performedAge",
                "performedDateTime",
                "performedPeriod",
                "performedRange",
                "performedString",
            ],
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


class ProcedureFocalDevice(backboneelement.BackboneElement):
    """ Manipulated, implanted, or removed device.
    A device that is implanted, removed or otherwise manipulated (calibration,
    battery replacement, fitting a prosthesis, attaching a wound-vac, etc.) as
    a focal portion of the Procedure.
    """

    resource_type = Field("ProcedureFocalDevice", const=True)

    action: fhirtypes.CodeableConceptType = Field(
        None,
        alias="action",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Kind of change to device",
    )

    manipulated: fhirtypes.ReferenceType = Field(
        ...,
        alias="manipulated",
        title="Type `Reference` referencing `Device` (represented as `dict` in JSON)",
        description="Device that was changed",
    )


class ProcedurePerformer(backboneelement.BackboneElement):
    """ The people who performed the procedure.
    Limited to "real" people rather than equipment.
    """

    resource_type = Field("ProcedurePerformer", const=True)

    actor: fhirtypes.ReferenceType = Field(
        ...,
        alias="actor",
        title="Type `Reference` referencing `Practitioner, PractitionerRole, Organization, Patient, RelatedPerson, Device` (represented as `dict` in JSON)",
        description="The reference to the practitioner",
    )

    function: fhirtypes.CodeableConceptType = Field(
        None,
        alias="function",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of performance",
    )

    onBehalfOf: fhirtypes.ReferenceType = Field(
        None,
        alias="onBehalfOf",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Organization the device or practitioner was acting for",
    )
