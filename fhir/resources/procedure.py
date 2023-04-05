# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Procedure
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class Procedure(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An action that is being or was performed on an individual or entity.
    An action that is or was performed on or for a patient, practitioner,
    device, organization, or location. For example, this can be a physical
    intervention on a patient like an operation, or less invasive like long
    term services, counseling, or hypnotherapy.  This can be a quality or
    safety inspection for a location, organization, or device.  This can be an
    accreditation procedure on a practitioner for licensing.
    """

    resource_type = Field("Procedure", const=True)

    basedOn: typing.List[fhirtypes.ReferenceType] = Field(
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

    bodySite: typing.List[fhirtypes.CodeableConceptType] = Field(
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

    category: typing.List[fhirtypes.CodeableConceptType] = Field(
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

    complication: typing.List[fhirtypes.CodeableReferenceType] = Field(
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
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Condition"],
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="The Encounter during which this Procedure was created",
        description=(
            "The Encounter during which this Procedure was created or performed or "
            "to which the creation of this record is tightly associated."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    focalDevice: typing.List[fhirtypes.ProcedureFocalDeviceType] = Field(
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

    focus: fhirtypes.ReferenceType = Field(
        None,
        alias="focus",
        title=(
            "Who is the target of the procedure when it is not the subject of "
            "record only"
        ),
        description=(
            "Who is the target of the procedure when it is not the subject of "
            "record only.  If focus is not present, then subject is the focus.  If "
            "focus is present and the subject is one of the targets of the "
            "procedure, include subject as a focus as well. If focus is present and"
            " the subject is not included in focus, it implies that the procedure "
            "was only targeted on the focus. For example, when a caregiver is given"
            " education for a patient, the caregiver would be the focus and the "
            "procedure record is associated with the subject (e.g. patient).  For "
            "example, use focus when recording the target of the education, "
            "training, or counseling is the parent or relative of a patient."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "Group",
            "RelatedPerson",
            "Practitioner",
            "Organization",
            "CareTeam",
            "PractitionerRole",
            "Specimen",
        ],
    )

    followUp: typing.List[fhirtypes.CodeableConceptType] = Field(
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

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
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

    instantiatesCanonical: typing.List[typing.Optional[fhirtypes.Canonical]] = Field(
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
    instantiatesCanonical__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_instantiatesCanonical",
        title="Extension field for ``instantiatesCanonical``.",
    )

    instantiatesUri: typing.List[typing.Optional[fhirtypes.Uri]] = Field(
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
    instantiatesUri__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
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

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Additional information about the procedure",
        description="Any other notes and comments about the procedure.",
        # if property is element of this resource.
        element_property=True,
    )

    occurrenceAge: fhirtypes.AgeType = Field(
        None,
        alias="occurrenceAge",
        title="When the procedure occurred or is occurring",
        description=(
            "Estimated or actual date, date-time, period, or age when the procedure"
            " did occur or is occurring.  Allows a period to support complex "
            "procedures that span more than one date, and also allows for the "
            "length of the procedure to be captured."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )

    occurrenceDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurrenceDateTime",
        title="When the procedure occurred or is occurring",
        description=(
            "Estimated or actual date, date-time, period, or age when the procedure"
            " did occur or is occurring.  Allows a period to support complex "
            "procedures that span more than one date, and also allows for the "
            "length of the procedure to be captured."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_occurrenceDateTime",
        title="Extension field for ``occurrenceDateTime``.",
    )

    occurrencePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="occurrencePeriod",
        title="When the procedure occurred or is occurring",
        description=(
            "Estimated or actual date, date-time, period, or age when the procedure"
            " did occur or is occurring.  Allows a period to support complex "
            "procedures that span more than one date, and also allows for the "
            "length of the procedure to be captured."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )

    occurrenceRange: fhirtypes.RangeType = Field(
        None,
        alias="occurrenceRange",
        title="When the procedure occurred or is occurring",
        description=(
            "Estimated or actual date, date-time, period, or age when the procedure"
            " did occur or is occurring.  Allows a period to support complex "
            "procedures that span more than one date, and also allows for the "
            "length of the procedure to be captured."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )

    occurrenceString: fhirtypes.String = Field(
        None,
        alias="occurrenceString",
        title="When the procedure occurred or is occurring",
        description=(
            "Estimated or actual date, date-time, period, or age when the procedure"
            " did occur or is occurring.  Allows a period to support complex "
            "procedures that span more than one date, and also allows for the "
            "length of the procedure to be captured."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )
    occurrenceString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_occurrenceString",
        title="Extension field for ``occurrenceString``.",
    )

    occurrenceTiming: fhirtypes.TimingType = Field(
        None,
        alias="occurrenceTiming",
        title="When the procedure occurred or is occurring",
        description=(
            "Estimated or actual date, date-time, period, or age when the procedure"
            " did occur or is occurring.  Allows a period to support complex "
            "procedures that span more than one date, and also allows for the "
            "length of the procedure to be captured."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
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

    partOf: typing.List[fhirtypes.ReferenceType] = Field(
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

    performer: typing.List[fhirtypes.ProcedurePerformerType] = Field(
        None,
        alias="performer",
        title="Who performed the procedure and what they did",
        description=(
            "Indicates who or what performed the procedure and how they were "
            "involved."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    reason: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="reason",
        title="The justification that the procedure was performed",
        description=(
            "The coded reason or reference why the procedure was performed. This "
            "may be a coded entity of some type, be present as text, or be a "
            "reference to one of several resources that justify the procedure."
        ),
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

    recorded: fhirtypes.DateTime = Field(
        None,
        alias="recorded",
        title="When the procedure was first captured in the subject's record",
        description=(
            "The date the occurrence of the procedure was first captured in the "
            "record regardless of Procedure.status (potentially after the "
            "occurrence of the event)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    recorded__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_recorded", title="Extension field for ``recorded``."
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

    report: typing.List[fhirtypes.ReferenceType] = Field(
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

    reportedBoolean: bool = Field(
        None,
        alias="reportedBoolean",
        title="Reported rather than primary record",
        description=(
            "Indicates if this record was captured as a secondary 'reported' record"
            " rather than as an original primary source-of-truth record.  It may "
            "also indicate the source of the report."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e reported[x]
        one_of_many="reported",
        one_of_many_required=False,
    )
    reportedBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_reportedBoolean", title="Extension field for ``reportedBoolean``."
    )

    reportedReference: fhirtypes.ReferenceType = Field(
        None,
        alias="reportedReference",
        title="Reported rather than primary record",
        description=(
            "Indicates if this record was captured as a secondary 'reported' record"
            " rather than as an original primary source-of-truth record.  It may "
            "also indicate the source of the report."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e reported[x]
        one_of_many="reported",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "RelatedPerson",
            "Practitioner",
            "PractitionerRole",
            "Organization",
        ],
    )

    status: fhirtypes.Code = Field(
        None,
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
        element_required=True,
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
        title="Individual or entity the procedure was performed on",
        description=(
            "On whom or on what the procedure was performed. This is usually an "
            "individual human, but can also be performed on animals, groups of "
            "humans or animals, organizations or practitioners (for licensing), "
            "locations or devices (for safety inspections or regulatory "
            "authorizations).  If the actual focus of the procedure is different "
            "from the subject, the focus element specifies the actual focus of the "
            "procedure."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "Group",
            "Device",
            "Practitioner",
            "Organization",
            "Location",
        ],
    )

    supportingInfo: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingInfo",
        title="Extra information relevant to the procedure",
        description=(
            "Other resources from the patient record that may be relevant to the "
            "procedure.  The information from these resources was either used to "
            "create the instance or is provided to help with its interpretation. "
            "This extension should not be used if more specific inline elements or "
            "extensions are available."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    used: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="used",
        title="Items used during procedure",
        description=(
            "Identifies medications, devices and any other substance used as part "
            "of the procedure."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Device",
            "Medication",
            "Substance",
            "BiologicallyDerivedProduct",
        ],
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
            "instantiatesCanonical",
            "instantiatesUri",
            "basedOn",
            "partOf",
            "status",
            "statusReason",
            "category",
            "code",
            "subject",
            "focus",
            "encounter",
            "occurrenceDateTime",
            "occurrencePeriod",
            "occurrenceString",
            "occurrenceAge",
            "occurrenceRange",
            "occurrenceTiming",
            "recorded",
            "recorder",
            "reportedBoolean",
            "reportedReference",
            "performer",
            "location",
            "reason",
            "bodySite",
            "outcome",
            "report",
            "complication",
            "followUp",
            "note",
            "focalDevice",
            "used",
            "supportingInfo",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1118(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1118(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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
            "occurrence": [
                "occurrenceAge",
                "occurrenceDateTime",
                "occurrencePeriod",
                "occurrenceRange",
                "occurrenceString",
                "occurrenceTiming",
            ],
            "reported": ["reportedBoolean", "reportedReference"],
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
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
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

    Who performed the procedure and what they did.
    Indicates who or what performed the procedure and how they were involved.
    """

    resource_type = Field("ProcedurePerformer", const=True)

    actor: fhirtypes.ReferenceType = Field(
        ...,
        alias="actor",
        title="Who performed the procedure",
        description="Indicates who or what performed the procedure.",
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
            "CareTeam",
            "HealthcareService",
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
        description=(
            "The Organization the Patient, RelatedPerson, Device, CareTeam, and "
            "HealthcareService was acting on behalf of."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="When the performer performed the procedure",
        description="Time period during which the performer performed the procedure.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ProcedurePerformer`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "function",
            "actor",
            "onBehalfOf",
            "period",
        ]
