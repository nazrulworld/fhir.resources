# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Procedure
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Procedure(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An action that is being or was performed on a patient.
    An action that is or was performed on a patient. This can be a physical
    intervention like an operation, or less invasive like counseling or
    hypnotherapy.
    """

    resource_type = Field("Procedure", const=True)

    basedOn: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title=(
            "List of `Reference` items referencing `CarePlan, ProcedureRequest, "
            "ReferralRequest` (represented as `dict` in JSON)"
        ),
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
        title=(
            "List of `Reference` items referencing `Condition` (represented as "
            "`dict` in JSON)"
        ),
        description="A condition that\u00a0is a result of the procedure",
    )

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title=(
            "Type `Reference` referencing `Encounter, EpisodeOfCare` (represented "
            "as `dict` in JSON)"
        ),
        description="Encounter or episode associated with the procedure",
    )

    definition: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="definition",
        title=(
            "List of `Reference` items referencing `PlanDefinition, "
            "ActivityDefinition, HealthcareService` (represented as `dict` in JSON)"
        ),
        description="Instantiates protocol or definition",
    )

    focalDevice: ListType[fhirtypes.ProcedureFocalDeviceType] = Field(
        None,
        alias="focalDevice",
        title="List of `ProcedureFocalDevice` items (represented as `dict` in JSON)",
        description="Device changed in procedure",
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

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title=(
            "Type `Reference` referencing `Location` (represented as `dict` in " "JSON)"
        ),
        description="Where the procedure happened",
    )

    notDone: bool = Field(
        None,
        alias="notDone",
        title="Type `bool`",
        description="True if procedure was not performed as scheduled",
    )
    notDone__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_notDone", title="Extension field for ``notDone``."
    )

    notDoneReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="notDoneReason",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Reason procedure was not performed",
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
        title=(
            "List of `Reference` items referencing `Procedure, Observation, "
            "MedicationAdministration` (represented as `dict` in JSON)"
        ),
        description="Part of referenced event",
    )

    performedDateTime: fhirtypes.DateTime = Field(
        None,
        alias="performedDateTime",
        title="Type `DateTime`",
        description="Date/Period the procedure was performed",
        one_of_many="performed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    performedDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_performedDateTime",
        title="Extension field for ``performedDateTime``.",
    )

    performedPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="performedPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Date/Period the procedure was performed",
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
        title=(
            "List of `Reference` items referencing `Condition, Observation` "
            "(represented as `dict` in JSON)"
        ),
        description="Condition that is the reason the procedure performed",
    )

    report: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="report",
        title=(
            "List of `Reference` items referencing `DiagnosticReport` (represented "
            "as `dict` in JSON)"
        ),
        description="Any report resulting from the procedure",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`",
        description=(
            "preparation | in-progress | suspended | aborted | completed | entered-"
            "in-error | unknown"
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
        title=(
            "List of `Reference` items referencing `Device, Medication, Substance` "
            "(represented as `dict` in JSON)"
        ),
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
        one_of_many_fields = {"performed": ["performedDateTime", "performedPeriod"]}
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Device changed in procedure.
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The people who performed the procedure.
    Limited to 'real' people rather than equipment.
    """

    resource_type = Field("ProcedurePerformer", const=True)

    actor: fhirtypes.ReferenceType = Field(
        ...,
        alias="actor",
        title=(
            "Type `Reference` referencing `Practitioner, Organization, Patient, "
            "RelatedPerson, Device` (represented as `dict` in JSON)"
        ),
        description="The reference to the practitioner",
    )

    onBehalfOf: fhirtypes.ReferenceType = Field(
        None,
        alias="onBehalfOf",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Organization the device or practitioner was acting for",
    )

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The role the actor was in",
    )
