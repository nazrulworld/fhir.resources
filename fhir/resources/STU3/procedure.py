from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Procedure
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Procedure(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An action that is being or was performed on a patient.
    An action that is or was performed on a patient. This can be a physical
    intervention like an operation, or less invasive like counseling or
    hypnotherapy.
    """

    __resource_type__ = "Procedure"

    basedOn: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="basedOn",
        title="A request for this procedure",
        description=(
            "A reference to a resource that contains details of the request for "
            "this procedure."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["CarePlan", "ProcedureRequest", "ReferralRequest"],
        },
    )

    bodySite: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="bodySite",
        title="Target body sites",
        description=(
            "Detailed and structured anatomical location information. Multiple "
            "locations are allowed - e.g. multiple punch biopsies of a lesion."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    category: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="category",
        title="Classification of the procedure",
        description=(
            "A code that classifies the procedure for searching, sorting and "
            'display purposes (e.g. "Surgical Procedure").'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Identification of the procedure",
        description=(
            "The specific procedure that is performed. Use text if the exact nature"
            ' of the procedure cannot be coded (e.g. "Laparoscopic Appendectomy").'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    complication: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="complication",
        title="Complication following the procedure",
        description=(
            "Any complications that occurred during the procedure, or in the "
            "immediate post-performance period. These are generally tracked "
            "separately from the notes, which will typically describe the procedure"
            " itself rather than any 'post procedure' issues."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    complicationDetail: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="complicationDetail",
        title="A condition that\u00a0is a result of the procedure",
        description=(
            "Any complications that occurred during the procedure, or in the "
            "immediate post-performance period."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Condition"],
        },
    )

    context: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="context",
        title="Encounter or episode associated with the procedure",
        description="The encounter during which the procedure was performed.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter", "EpisodeOfCare"],
        },
    )

    definition: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="definition",
        title="Instantiates protocol or definition",
        description=(
            "A protocol, guideline, orderset or other definition that was adhered "
            "to in whole or in part by this procedure."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "PlanDefinition",
                "ActivityDefinition",
                "HealthcareService",
            ],
        },
    )

    focalDevice: typing.List[fhirtypes.ProcedureFocalDeviceType] | None = Field(  # type: ignore
        None,
        alias="focalDevice",
        title="Device changed in procedure",
        description=(
            "A device that is implanted, removed or otherwise manipulated "
            "(calibration, battery replacement, fitting a prosthesis, attaching a "
            "wound-vac, etc.) as a focal portion of the Procedure."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    followUp: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="followUp",
        title="Instructions for follow up",
        description=(
            "If the procedure required specific follow up - e.g. removal of "
            "sutures. The followup may be represented as a simple note, or could "
            "potentially be more complex in which case the CarePlan resource can be"
            " used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="External Identifiers for this procedure",
        description=(
            "This records identifiers associated with this procedure that are "
            "defined by business processes and/or used to refer to it when a direct"
            " URL reference to the resource itself is not appropriate (e.g. in CDA "
            "documents, or in written / printed documentation)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    location: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="location",
        title="Where the procedure happened",
        description=(
            "The location where the procedure actually happened.  E.g. a newborn at"
            " home, a tracheostomy at a restaurant."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    notDone: bool | None = Field(  # type: ignore
        None,
        alias="notDone",
        title="True if procedure was not performed as scheduled",
        description=(
            "Set this to true if the record is saying that the procedure was NOT "
            "performed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    notDone__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_notDone", title="Extension field for ``notDone``."
    )

    notDoneReason: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="notDoneReason",
        title="Reason procedure was not performed",
        description="A code indicating why the procedure was not performed.",
        json_schema_extra={
            "element_property": True,
        },
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="note",
        title="Additional information about the procedure",
        description="Any other notes about the procedure.  E.g. the operative notes.",
        json_schema_extra={
            "element_property": True,
        },
    )

    outcome: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="outcome",
        title="The result of procedure",
        description=(
            "The outcome of the procedure - did it resolve reasons for the "
            "procedure being performed?"
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    partOf: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="partOf",
        title="Part of referenced event",
        description=(
            "A larger event of which this particular procedure is a component or "
            "step."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Procedure",
                "Observation",
                "MedicationAdministration",
            ],
        },
    )

    performedDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="performedDateTime",
        title="Date/Period the procedure was performed",
        description=(
            "The date(time)/period over which the procedure was performed. Allows a"
            " period to support complex procedures that span more than one date, "
            "and also allows for the length of the procedure to be captured."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e performed[x]
            "one_of_many": "performed",
            "one_of_many_required": False,
        },
    )
    performedDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_performedDateTime",
        title="Extension field for ``performedDateTime``.",
    )

    performedPeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="performedPeriod",
        title="Date/Period the procedure was performed",
        description=(
            "The date(time)/period over which the procedure was performed. Allows a"
            " period to support complex procedures that span more than one date, "
            "and also allows for the length of the procedure to be captured."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e performed[x]
            "one_of_many": "performed",
            "one_of_many_required": False,
        },
    )

    performer: typing.List[fhirtypes.ProcedurePerformerType] | None = Field(  # type: ignore
        None,
        alias="performer",
        title="The people who performed the procedure",
        description="Limited to 'real' people rather than equipment.",
        json_schema_extra={
            "element_property": True,
        },
    )

    reasonCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="reasonCode",
        title="Coded reason procedure performed",
        description=(
            "The coded reason why the procedure was performed. This may be coded "
            "entity of some type, or may simply be present as text."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reasonReference: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="reasonReference",
        title="Condition that is the reason the procedure performed",
        description="The condition that is the reason why the procedure was performed.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Condition", "Observation"],
        },
    )

    report: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="report",
        title="Any report resulting from the procedure",
        description=(
            "This could be a histology result, pathology report, surgical report, "
            "etc.."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DiagnosticReport"],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title=(
            "preparation | in-progress | suspended | aborted | completed | entered-"
            "in-error | unknown"
        ),
        description=(
            "A code specifying the state of the procedure. Generally this will be "
            "in-progress or completed state."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "preparation",
                "in-progress",
                "suspended",
                "aborted",
                "completed",
                "entered-in-error",
                "unknown",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="subject",
        title="Who the procedure was performed on",
        description="The person, animal or group on which the procedure was performed.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "Group"],
        },
    )

    usedCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="usedCode",
        title="Coded items used during the procedure",
        description="Identifies coded items that were used as part of the procedure.",
        json_schema_extra={
            "element_property": True,
        },
    )

    usedReference: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="usedReference",
        title="Items used during procedure",
        description=(
            "Identifies medications, devices and any other substance used as part "
            "of the procedure."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Device", "Medication", "Substance"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Procedure`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "identifier",
            "definition",
            "basedOn",
            "partOf",
            "status",
            "notDone",
            "notDoneReason",
            "category",
            "code",
            "subject",
            "context",
            "performedDateTime",
            "performedPeriod",
            "performer",
            "location",
            "reasonCode",
            "reasonReference",
            "bodySite",
            "outcome",
            "report",
            "complication",
            "complicationDetail",
            "followUp",
            "note",
            "focalDevice",
            "usedReference",
            "usedCode",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        return required_fields

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
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
        return one_of_many_fields


class ProcedureFocalDevice(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Device changed in procedure.
    A device that is implanted, removed or otherwise manipulated (calibration,
    battery replacement, fitting a prosthesis, attaching a wound-vac, etc.) as
    a focal portion of the Procedure.
    """

    __resource_type__ = "ProcedureFocalDevice"

    action: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="action",
        title="Kind of change to device",
        description="The kind of change that happened to the device during the procedure.",
        json_schema_extra={
            "element_property": True,
        },
    )

    manipulated: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="manipulated",
        title="Device that was changed",
        description="The device that was manipulated (changed) during the procedure.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Device"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ProcedureFocalDevice`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "action", "manipulated"]


class ProcedurePerformer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The people who performed the procedure.
    Limited to 'real' people rather than equipment.
    """

    __resource_type__ = "ProcedurePerformer"

    actor: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="actor",
        title="The reference to the practitioner",
        description="The practitioner who was involved in the procedure.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "Organization",
                "Patient",
                "RelatedPerson",
                "Device",
            ],
        },
    )

    onBehalfOf: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="onBehalfOf",
        title="Organization the device or practitioner was acting for",
        description="The organization the device or practitioner was acting on behalf of.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    role: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="role",
        title="The role the actor was in",
        description="For example: surgeon, anaethetist, endoscopist.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ProcedurePerformer`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "role", "actor", "onBehalfOf"]
