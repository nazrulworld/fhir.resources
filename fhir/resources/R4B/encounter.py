# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Encounter
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class Encounter(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An interaction during which services are provided to the patient.
    An interaction between a patient and healthcare provider(s) for the purpose
    of providing healthcare service(s) or assessing the health status of a
    patient.
    """

    resource_type = Field("Encounter", const=True)

    account: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="account",
        title="The set of accounts that may be used for billing for this Encounter",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Account"],
    )

    appointment: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="appointment",
        title="The appointment that scheduled this encounter",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Appointment"],
    )

    basedOn: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="The ServiceRequest that initiated this encounter",
        description=(
            "The request this encounter satisfies (e.g. incoming referral or "
            "procedure request)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ServiceRequest"],
    )

    classHistory: typing.List[fhirtypes.EncounterClassHistoryType] = Field(
        None,
        alias="classHistory",
        title="List of past encounter classes",
        description=(
            "The class history permits the tracking of the encounters transitions "
            "without needing to go  through the resource history.  This would be "
            "used for a case where an admission starts of as an emergency "
            "encounter, then transitions into an inpatient scenario. Doing this and"
            " not restarting a new encounter ensures that any lab/diagnostic "
            "results can more easily follow the patient and not require re-"
            "processing and not get lost or cancelled during a kind of discharge "
            "from emergency to inpatient."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    class_fhir: fhirtypes.CodingType = Field(
        ...,
        alias="class",
        title="Classification of patient encounter",
        description=(
            "Concepts representing classification of patient encounter such as "
            "ambulatory (outpatient), inpatient, emergency, home health or others "
            "due to local variations."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    diagnosis: typing.List[fhirtypes.EncounterDiagnosisType] = Field(
        None,
        alias="diagnosis",
        title="The list of diagnosis relevant to this encounter",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    episodeOfCare: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="episodeOfCare",
        title="Episode(s) of care that this encounter should be recorded against",
        description=(
            "Where a specific encounter should be classified as a part of a "
            "specific episode(s) of care this field should be used. This "
            "association can facilitate grouping of related encounters together for"
            " a specific purpose, such as government reporting, issue tracking, "
            "association via a common problem.  The association is recorded on the "
            "encounter as these are typically created after the episode of care and"
            " grouped on entry rather than editing the episode of care to append "
            "another encounter to it (the episode of care could span years)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["EpisodeOfCare"],
    )

    hospitalization: fhirtypes.EncounterHospitalizationType = Field(
        None,
        alias="hospitalization",
        title="Details about the admission to a healthcare service",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Identifier(s) by which this encounter is known",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    length: fhirtypes.DurationType = Field(
        None,
        alias="length",
        title="Quantity of time the encounter lasted (less time absent)",
        description=(
            "Quantity of time the encounter lasted. This excludes the time during "
            "leaves of absence."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    location: typing.List[fhirtypes.EncounterLocationType] = Field(
        None,
        alias="location",
        title="List of locations where the patient has been",
        description="List of locations where  the patient has been during this encounter.",
        # if property is element of this resource.
        element_property=True,
    )

    partOf: fhirtypes.ReferenceType = Field(
        None,
        alias="partOf",
        title="Another Encounter this encounter is part of",
        description=(
            "Another Encounter of which this encounter is a part of "
            "(administratively or in time)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    participant: typing.List[fhirtypes.EncounterParticipantType] = Field(
        None,
        alias="participant",
        title="List of participants involved in the encounter",
        description="The list of people responsible for providing the service.",
        # if property is element of this resource.
        element_property=True,
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="The start and end time of the encounter",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    priority: fhirtypes.CodeableConceptType = Field(
        None,
        alias="priority",
        title="Indicates the urgency of the encounter",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    reasonCode: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="Coded reason the encounter takes place",
        description=(
            "Reason the encounter takes place, expressed as a code. For admissions,"
            " this can be used for a coded admission diagnosis."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    reasonReference: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title="Reason the encounter takes place (reference)",
        description=(
            "Reason the encounter takes place, expressed as a code. For admissions,"
            " this can be used for a coded admission diagnosis."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Condition",
            "Procedure",
            "Observation",
            "ImmunizationRecommendation",
        ],
    )

    serviceProvider: fhirtypes.ReferenceType = Field(
        None,
        alias="serviceProvider",
        title="The organization (facility) responsible for this encounter",
        description=(
            "The organization that is primarily responsible for this Encounter's "
            "services. This MAY be the same as the organization on the Patient "
            "record, however it could be different, such as if the actor performing"
            " the services was from an external organization (which may be billed "
            "seperately) for an external consultation.  Refer to the example bundle"
            " showing an abbreviated set of Encounters for a colonoscopy."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    serviceType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="serviceType",
        title="Specific type of service",
        description=(
            "Broad categorization of the service that is to be provided (e.g. "
            "cardiology)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title=(
            "planned | arrived | triaged | in-progress | onleave | finished | "
            "cancelled +"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "planned",
            "arrived",
            "triaged",
            "in-progress",
            "onleave",
            "finished",
            "cancelled",
            "+",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    statusHistory: typing.List[fhirtypes.EncounterStatusHistoryType] = Field(
        None,
        alias="statusHistory",
        title="List of past encounter statuses",
        description=(
            "The status history permits the encounter resource to contain the "
            "status history without needing to read through the historical versions"
            " of the resource, or even have the server store them."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="The patient or group present at the encounter",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group"],
    )

    type: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="Specific type of encounter",
        description=(
            "Specific type of encounter (e.g. e-mail consultation, surgical day-"
            "care, skilled nursing, rehabilitation)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Encounter`` according specification,
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
            "status",
            "statusHistory",
            "class",
            "classHistory",
            "type",
            "serviceType",
            "priority",
            "subject",
            "episodeOfCare",
            "basedOn",
            "participant",
            "appointment",
            "period",
            "length",
            "reasonCode",
            "reasonReference",
            "diagnosis",
            "account",
            "hospitalization",
            "location",
            "serviceProvider",
            "partOf",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1130(
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


class EncounterClassHistory(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    List of past encounter classes.
    The class history permits the tracking of the encounters transitions
    without needing to go  through the resource history.  This would be used
    for a case where an admission starts of as an emergency encounter, then
    transitions into an inpatient scenario. Doing this and not restarting a new
    encounter ensures that any lab/diagnostic results can more easily follow
    the patient and not require re-processing and not get lost or cancelled
    during a kind of discharge from emergency to inpatient.
    """

    resource_type = Field("EncounterClassHistory", const=True)

    class_fhir: fhirtypes.CodingType = Field(
        ...,
        alias="class",
        title="inpatient | outpatient | ambulatory | emergency +",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    period: fhirtypes.PeriodType = Field(
        ...,
        alias="period",
        title="The time that the episode was in the specified class",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EncounterClassHistory`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "class", "period"]


class EncounterDiagnosis(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The list of diagnosis relevant to this encounter.
    """

    resource_type = Field("EncounterDiagnosis", const=True)

    condition: fhirtypes.ReferenceType = Field(
        ...,
        alias="condition",
        title="The diagnosis or procedure relevant to the encounter",
        description=(
            "Reason the encounter takes place, as specified using information from "
            "another resource. For admissions, this is the admission diagnosis. The"
            " indication will typically be a Condition (with other resources "
            "referenced in the evidence.detail), or a Procedure."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Condition", "Procedure"],
    )

    rank: fhirtypes.PositiveInt = Field(
        None,
        alias="rank",
        title="Ranking of the diagnosis (for each role type)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    rank__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_rank", title="Extension field for ``rank``."
    )

    use: fhirtypes.CodeableConceptType = Field(
        None,
        alias="use",
        title=(
            "Role that this diagnosis has within the encounter (e.g. admission, "
            "billing, discharge \u2026)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EncounterDiagnosis`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "condition", "use", "rank"]


class EncounterHospitalization(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details about the admission to a healthcare service.
    """

    resource_type = Field("EncounterHospitalization", const=True)

    admitSource: fhirtypes.CodeableConceptType = Field(
        None,
        alias="admitSource",
        title="From where patient was admitted (physician referral, transfer)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    destination: fhirtypes.ReferenceType = Field(
        None,
        alias="destination",
        title="Location/organization to which the patient is discharged",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location", "Organization"],
    )

    dietPreference: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="dietPreference",
        title="Diet preferences reported by the patient",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    dischargeDisposition: fhirtypes.CodeableConceptType = Field(
        None,
        alias="dischargeDisposition",
        title="Category or kind of location after discharge",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    origin: fhirtypes.ReferenceType = Field(
        None,
        alias="origin",
        title="The location/organization from which the patient came before admission",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location", "Organization"],
    )

    preAdmissionIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="preAdmissionIdentifier",
        title="Pre-admission identifier",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    reAdmission: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reAdmission",
        title=(
            "The type of hospital re-admission that has occurred (if any). If the "
            "value is absent, then this is not identified as a readmission"
        ),
        description="Whether this hospitalization is a readmission and why if known.",
        # if property is element of this resource.
        element_property=True,
    )

    specialArrangement: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="specialArrangement",
        title="Wheelchair, translator, stretcher, etc.",
        description=(
            "Any special requests that have been made for this hospitalization "
            "encounter, such as the provision of specific equipment or other "
            "things."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    specialCourtesy: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="specialCourtesy",
        title="Special courtesies (VIP, board member)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EncounterHospitalization`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "preAdmissionIdentifier",
            "origin",
            "admitSource",
            "reAdmission",
            "dietPreference",
            "specialCourtesy",
            "specialArrangement",
            "destination",
            "dischargeDisposition",
        ]


class EncounterLocation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    List of locations where the patient has been.
    List of locations where  the patient has been during this encounter.
    """

    resource_type = Field("EncounterLocation", const=True)

    location: fhirtypes.ReferenceType = Field(
        ...,
        alias="location",
        title="Location the encounter takes place",
        description="The location where the encounter takes place.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Time period during which the patient was present at the location",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    physicalType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="physicalType",
        title=(
            "The physical type of the location (usually the level in the location "
            "hierachy - bed room ward etc.)"
        ),
        description=(
            "This will be used to specify the required levels (bed/ward/room/etc.) "
            "desired to be recorded to simplify either messaging or query."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="planned | active | reserved | completed",
        description=(
            "The status of the participants' presence at the specified location "
            "during the period specified. If the participant is no longer at the "
            "location, then the period will have an end date/time."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["planned", "active", "reserved", "completed"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EncounterLocation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "location",
            "status",
            "physicalType",
            "period",
        ]


class EncounterParticipant(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    List of participants involved in the encounter.
    The list of people responsible for providing the service.
    """

    resource_type = Field("EncounterParticipant", const=True)

    individual: fhirtypes.ReferenceType = Field(
        None,
        alias="individual",
        title="Persons involved in the encounter other than the patient",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "PractitionerRole", "RelatedPerson"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Period of time during the encounter that the participant participated",
        description=(
            "The period of time that the specified participant participated in the "
            "encounter. These can overlap or be sub-sets of the overall encounter's"
            " period."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="Role of participant in encounter",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EncounterParticipant`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "period", "individual"]


class EncounterStatusHistory(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    List of past encounter statuses.
    The status history permits the encounter resource to contain the status
    history without needing to read through the historical versions of the
    resource, or even have the server store them.
    """

    resource_type = Field("EncounterStatusHistory", const=True)

    period: fhirtypes.PeriodType = Field(
        ...,
        alias="period",
        title="The time that the episode was in the specified status",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title=(
            "planned | arrived | triaged | in-progress | onleave | finished | "
            "cancelled +"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "planned",
            "arrived",
            "triaged",
            "in-progress",
            "onleave",
            "finished",
            "cancelled",
            "+",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EncounterStatusHistory`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "status", "period"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2535(
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
