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
from typing import Union

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Procedure(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An action that is being or was performed on a patient.
    An action that is or was performed on or for a patient. This can be a
    physical intervention like an operation, or less invasive like long term
    services, counseling, or hypnotherapy.
    """

    resource_type = Field("Procedure", const=True)

    asserter: fhirtypes.ReferenceType = Field(
        None,
        alias="asserter",
        title="Person who asserts this procedure",
        description="Individual who is making the procedure statement.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "RelatedPerson",
            "Practitioner",
            "PractitionerRole",
        ],
    )

    basedOn: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="A request for this procedure",
        description=(
            "A reference to a resource that contains details of the request for "
            "this procedure."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["CarePlan", "ServiceRequest"],
    )

    bodySite: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="bodySite",
        title="Target body sites",
        description=(
            "Detailed and structured anatomical location information. Multiple "
            "locations are allowed - e.g. multiple punch biopsies of a lesion."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Classification of the procedure",
        description=(
            "A code that classifies the procedure for searching, sorting and "
            'display purposes (e.g. "Surgical Procedure").'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Identification of the procedure",
        description=(
            "The specific procedure that is performed. Use text if the exact nature"
            ' of the procedure cannot be coded (e.g. "Laparoscopic Appendectomy").'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    complication: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="complication",
        title="Complication following the procedure",
        description=(
            "Any complications that occurred during the procedure, or in the "
            "immediate post-performance period. These are generally tracked "
            "separately from the notes, which will typically describe the procedure"
            " itself rather than any 'post procedure' issues."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    complicationDetail: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="complicationDetail",
        title="A condition that is a result of the procedure",
        description=(
            "Any complications that occurred during the procedure, or in the "
            "immediate post-performance period."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Condition"],
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Encounter created as part of",
        description=(
            "The Encounter during which this Procedure was created or performed or "
            "to which the creation of this record is tightly associated."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    focalDevice: ListType[fhirtypes.ProcedureFocalDeviceType] = Field(
        None,
        alias="focalDevice",
        title="Manipulated, implanted, or removed device",
        description=(
            "A device that is implanted, removed or otherwise manipulated "
            "(calibration, battery replacement, fitting a prosthesis, attaching a "
            "wound-vac, etc.) as a focal portion of the Procedure."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    followUp: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="followUp",
        title="Instructions for follow up",
        description=(
            "If the procedure required specific follow up - e.g. removal of "
            "sutures. The follow up may be represented as a simple note or could "
            "potentially be more complex, in which case the CarePlan resource can "
            "be used."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="External Identifiers for this procedure",
        description=(
            "Business identifiers assigned to this procedure by the performer or "
            "other systems which remain constant as the resource is updated and is "
            "propagated from server to server."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    instantiatesCanonical: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="instantiatesCanonical",
        title="Instantiates FHIR protocol or definition",
        description=(
            "The URL pointing to a FHIR-defined protocol, guideline, order set or "
            "other definition that is adhered to in whole or in part by this "
            "Procedure."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "PlanDefinition",
            "ActivityDefinition",
            "Measure",
            "OperationDefinition",
            "Questionnaire",
        ],
    )
    instantiatesCanonical__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_instantiatesCanonical",
        title="Extension field for ``instantiatesCanonical``.",
    )

    instantiatesUri: ListType[fhirtypes.Uri] = Field(
        None,
        alias="instantiatesUri",
        title="Instantiates external protocol or definition",
        description=(
            "The URL pointing to an externally maintained protocol, guideline, "
            "order set or other definition that is adhered to in whole or in part "
            "by this Procedure."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    instantiatesUri__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_instantiatesUri", title="Extension field for ``instantiatesUri``."
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title="Where the procedure happened",
        description=(
            "The location where the procedure actually happened.  E.g. a newborn at"
            " home, a tracheostomy at a restaurant."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Additional information about the procedure",
        description="Any other notes and comments about the procedure.",
        # if property is element of this resource.
        element_property=True,
    )

    outcome: fhirtypes.CodeableConceptType = Field(
        None,
        alias="outcome",
        title="The result of procedure",
        description=(
            "The outcome of the procedure - did it resolve the reasons for the "
            "procedure being performed?"
        ),
        # if property is element of this resource.
        element_property=True,
    )

    partOf: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title="Part of referenced event",
        description=(
            "A larger event of which this particular procedure is a component or "
            "step."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Procedure", "Observation", "MedicationAdministration"],
    )

    performedAge: fhirtypes.AgeType = Field(
        None,
        alias="performedAge",
        title="When the procedure was performed",
        description=(
            "Estimated or actual date, date-time, period, or age when the procedure"
            " was performed.  Allows a period to support complex procedures that "
            "span more than one date, and also allows for the length of the "
            "procedure to be captured."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e performed[x]
        one_of_many="performed",
        one_of_many_required=False,
    )

    performedDateTime: fhirtypes.DateTime = Field(
        None,
        alias="performedDateTime",
        title="When the procedure was performed",
        description=(
            "Estimated or actual date, date-time, period, or age when the procedure"
            " was performed.  Allows a period to support complex procedures that "
            "span more than one date, and also allows for the length of the "
            "procedure to be captured."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e performed[x]
        one_of_many="performed",
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
        title="When the procedure was performed",
        description=(
            "Estimated or actual date, date-time, period, or age when the procedure"
            " was performed.  Allows a period to support complex procedures that "
            "span more than one date, and also allows for the length of the "
            "procedure to be captured."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e performed[x]
        one_of_many="performed",
        one_of_many_required=False,
    )

    performedRange: fhirtypes.RangeType = Field(
        None,
        alias="performedRange",
        title="When the procedure was performed",
        description=(
            "Estimated or actual date, date-time, period, or age when the procedure"
            " was performed.  Allows a period to support complex procedures that "
            "span more than one date, and also allows for the length of the "
            "procedure to be captured."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e performed[x]
        one_of_many="performed",
        one_of_many_required=False,
    )

    performedString: fhirtypes.String = Field(
        None,
        alias="performedString",
        title="When the procedure was performed",
        description=(
            "Estimated or actual date, date-time, period, or age when the procedure"
            " was performed.  Allows a period to support complex procedures that "
            "span more than one date, and also allows for the length of the "
            "procedure to be captured."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e performed[x]
        one_of_many="performed",
        one_of_many_required=False,
    )
    performedString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_performedString", title="Extension field for ``performedString``."
    )

    performer: ListType[fhirtypes.ProcedurePerformerType] = Field(
        None,
        alias="performer",
        title="The people who performed the procedure",
        description='Limited to "real" people rather than equipment.',
        # if property is element of this resource.
        element_property=True,
    )

    reasonCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="Coded reason procedure performed",
        description=(
            "The coded reason why the procedure was performed. This may be a coded "
            "entity of some type, or may simply be present as text."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    reasonReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title="The justification that the procedure was performed",
        description="The justification of why the procedure was performed.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Condition",
            "Observation",
            "Procedure",
            "DiagnosticReport",
            "DocumentReference",
        ],
    )

    recorder: fhirtypes.ReferenceType = Field(
        None,
        alias="recorder",
        title="Who recorded the procedure",
        description=(
            "Individual who recorded the record and takes responsibility for its "
            "content."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "RelatedPerson",
            "Practitioner",
            "PractitionerRole",
        ],
    )

    report: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="report",
        title="Any report resulting from the procedure",
        description=(
            "This could be a histology result, pathology report, surgical report, "
            "etc."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DiagnosticReport", "DocumentReference", "Composition"],
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title=(
            "preparation | in-progress | not-done | on-hold | stopped | completed |"
            " entered-in-error | unknown"
        ),
        description=(
            "A code specifying the state of the procedure. Generally, this will be "
            "the in-progress or completed state."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "preparation",
            "in-progress",
            "not-done",
            "on-hold",
            "stopped",
            "completed",
            "entered-in-error",
            "unknown",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    statusReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="statusReason",
        title="Reason for current status",
        description="Captures the reason for the current state of the procedure.",
        # if property is element of this resource.
        element_property=True,
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Who the procedure was performed on",
        description="The person, animal or group on which the procedure was performed.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group"],
    )

    usedCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="usedCode",
        title="Coded items used during the procedure",
        description="Identifies coded items that were used as part of the procedure.",
        # if property is element of this resource.
        element_property=True,
    )

    usedReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="usedReference",
        title="Items used during procedure",
        description=(
            "Identifies medications, devices and any other substance used as part "
            "of the procedure."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device", "Medication", "Substance"],
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
            ]
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Manipulated, implanted, or removed device.
    A device that is implanted, removed or otherwise manipulated (calibration,
    battery replacement, fitting a prosthesis, attaching a wound-vac, etc.) as
    a focal portion of the Procedure.
    """

    resource_type = Field("ProcedureFocalDevice", const=True)

    action: fhirtypes.CodeableConceptType = Field(
        None,
        alias="action",
        title="Kind of change to device",
        description="The kind of change that happened to the device during the procedure.",
        # if property is element of this resource.
        element_property=True,
    )

    manipulated: fhirtypes.ReferenceType = Field(
        ...,
        alias="manipulated",
        title="Device that was changed",
        description="The device that was manipulated (changed) during the procedure.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device"],
    )


class ProcedurePerformer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The people who performed the procedure.
    Limited to "real" people rather than equipment.
    """

    resource_type = Field("ProcedurePerformer", const=True)

    actor: fhirtypes.ReferenceType = Field(
        ...,
        alias="actor",
        title="The reference to the practitioner",
        description="The practitioner who was involved in the procedure.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "Organization",
            "Patient",
            "RelatedPerson",
            "Device",
        ],
    )

    function: fhirtypes.CodeableConceptType = Field(
        None,
        alias="function",
        title="Type of performance",
        description=(
            "Distinguishes the type of involvement of the performer in the "
            "procedure. For example, surgeon, anaesthetist, endoscopist."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    onBehalfOf: fhirtypes.ReferenceType = Field(
        None,
        alias="onBehalfOf",
        title="Organization the device or practitioner was acting for",
        description="The organization the device or practitioner was acting on behalf of.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )
