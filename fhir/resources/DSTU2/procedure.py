# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Element
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic.v1 import Field, root_validator

from . import fhirtypes
from .backboneelement import BackboneElement
from .domainresource import DomainResource


class Procedure(DomainResource):
    """An action that is being or was performed on a patient.

    An action that is or was performed on a patient. This can be a physical
    intervention like an operation, or less invasive like counseling or
    hypnotherapy.
    """

    resource_type = Field("Procedure", const=True)

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`",
        description="in-progress | aborted | completed | entered-in-error.",
    )
    notPerformed: fhirtypes.Boolean = Field(
        None,
        alias="notPerformed",
        title="Type `Boolean`",
        description="True if procedure was not performed as scheduled.",
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title=(
            "Type `Reference` referencing `CarePlan, DiagnosticOrder, ProcedureRequest,"
            "ReferralRequest` (represented as `dict` in JSON)."
        ),
        description="A request for this procedure.",
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title=(
            "Type `Reference` referencing `Patient, Group` "
            "(represented as `dict` in JSON)."
        ),
        description="Who the procedure was performed on",
    )
    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title="Type `Reference` referencing `Location` (represented as `dict` in JSON).",
        description="Where the procedure happened.",
    )

    outcome: fhirtypes.CodeableConceptType = Field(
        None,
        alias="outcome",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="The result of procedure.",
    )

    performedDateTime: fhirtypes.DateTime = Field(
        None,
        alias="performedDateTime",
        title="Type `DateTime` .",
        description="Date/Period the procedure was performed.",
        one_of_many="performed",  # Choice of Data Types. i.e performed[x]
        one_of_many_required=False,
    )

    performedPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="performedPeriod",
        title="Type `Period` (represented as `dict` in JSON).",
        description="Date/Period the procedure was performed.",
        one_of_many="performed",  # Choice of Data Types. i.e performed[x]
        one_of_many_required=False,
    )

    bodySite: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="bodySite",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="Target body sites.",
    )

    category: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Classification of the procedure.",
    )

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="Identification of the procedure.",
    )

    complication: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="complication",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="Complication following the procedure.",
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title="Type `Reference` referencing `Encounter` (represented as `dict` in JSON).",
        description="The encounter associated with the procedure.",
    )

    focalDevice: ListType[fhirtypes.ProcedureFocalDeviceType] = Field(
        None,
        alias="focalDevice",
        title="List of `ProcedureFocalDevice` items (represented as `dict` in JSON).",
        description="Device changed in procedure.",
    )

    followUp: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="followUp",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="Instructions for follow up.",
    )
    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON).",
        description="External Identifiers for this procedure.",
    )

    notes: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="notes",
        title="List of `Annotation` items (represented as `dict` in JSON).",
        description="Additional information about the procedure.",
    )

    performer: ListType[fhirtypes.ProcedurePerformerType] = Field(
        None,
        alias="performer",
        title="List of `ProcedurePerformer` items (represented as `dict` in JSON).",
        description="The people who performed the procedure.",
    )

    reasonNotPerformed: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonNotPerformed",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="Reason procedure was not performed.",
    )

    reasonCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reasonCodeableConcept",
        title="Type `CodeableConcept`  (represented as `dict` in JSON).",
        description="Reason procedure performed.",
        one_of_many="reason",  # Choice of Data Types. i.e reason[x]
        one_of_many_required=False,
    )
    reasonReference: fhirtypes.ReferenceType = Field(
        None,
        alias="reasonReference",
        title="Type `Reference` referencing `Condition` (represented as `dict` in JSON).",
        description="Reason procedure performed.",
        one_of_many="reason",  # Choice of Data Types. i.e reason[x]
        one_of_many_required=False,
    )

    report: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="report",
        title=(
            "List of `RReference` items referencing `DiagnosticReport`"
            " (represented as `dict` in JSON)."
        ),
        description="Any report resulting from the procedure.",
    )
    used: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="used",
        title=(
            "List of `Reference` items referencing `Device, Medication,"
            " Substance` (represented as `dict` in JSON)."
        ),
        description="Items used during procedure.",
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
            "performed": ["performedDateTime", "performedPeriod"],
            "reason": ["reasonCodeableConcept", "reasonReference"],
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


class ProcedureFocalDevice(BackboneElement):
    """Device changed in procedure.

    A device that is implanted, removed or otherwise manipulated (calibration,
    battery replacement, fitting a prosthesis, attaching a wound-vac, etc.) as
    a focal portion of the Procedure.
    """

    resource_type = Field("ProcedureFocalDevice", const=True)

    action: fhirtypes.CodeableConceptType = Field(
        None,
        alias="action",
        title="Type `CodeableConcept`  (represented as `dict` in JSON).",
        description="Kind of change to device.",
    )
    manipulated: fhirtypes.ReferenceType = Field(
        ...,
        alias="manipulated",
        title="Type `Reference` referencing `Device` (represented as `dict` in JSON).",
        description="Device that was changed.",
    )


class ProcedurePerformer(BackboneElement):
    """The people who performed the procedure.

    Limited to 'real' people rather than equipment.
    """

    resource_type = Field("ProcedurePerformer", const=True)

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="Type `CodeableConcept`  (represented as `dict` in JSON).",
        description="The role the actor was in.",
    )
    actor: fhirtypes.ReferenceType = Field(
        None,
        alias="actor",
        title=(
            "Type `Reference` referencing `Practitioner, Organization, "
            "Patient, RelatedPerson` (represented as `dict` in JSON)."
        ),
        description="The reference to the practitioner.",
    )
