# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AdverseEvent
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class AdverseEvent(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An event that may be related to unintended effects on a patient or research
    participant.
    An event (i.e. any change to current patient status) that may be related to
    unintended effects on a patient or research participant. The unintended
    effects may require additional monitoring, treatment, hospitalization, or
    may result in death. The AdverseEvent resource also extends to potential or
    avoided events that could have had such effects. There are two major
    domains where the AdverseEvent resource is expected to be used. One is in
    clinical care reported adverse events and the other is in reporting adverse
    events in clinical  research trial management. Adverse events can be
    reported by healthcare providers, patients, caregivers or by medical
    products manufacturers. Given the differences between these two concepts,
    we recommend consulting the domain specific implementation guides when
    implementing the AdverseEvent Resource. The implementation guides include
    specific extensions, value sets and constraints.
    """

    resource_type = Field("AdverseEvent", const=True)

    actuality: fhirtypes.Code = Field(
        None,
        alias="actuality",
        title="actual | potential",
        description=(
            "Whether the event actually happened or was a near miss. Note that this"
            " is independent of whether anyone was affected or harmed or how "
            "severely."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["actual", "potential"],
    )
    actuality__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_actuality", title="Extension field for ``actuality``."
    )

    category: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title=(
            "wrong-patient | procedure-mishap | medication-mishap | device | "
            "unsafe-physical-environment | hospital-aquired-infection | wrong-body-"
            "site"
        ),
        description="The overall type of event, intended for search and filtering purposes.",
        # if property is element of this resource.
        element_property=True,
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Event or incident that occurred or was averted",
        description=(
            "Specific event that occurred or that was averted, such as patient "
            "fall, wrong organ removed, or wrong blood transfused."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    contributingFactor: typing.List[
        fhirtypes.AdverseEventContributingFactorType
    ] = Field(
        None,
        alias="contributingFactor",
        title=(
            "Contributing factors suspected to have increased the probability or "
            "severity of the adverse event"
        ),
        description=(
            "The contributing factors suspected to have increased the probability "
            "or severity of the adverse event."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    detected: fhirtypes.DateTime = Field(
        None,
        alias="detected",
        title="When the event was detected",
        description=(
            "Estimated or actual date the AdverseEvent began, in the opinion of the"
            " reporter."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    detected__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_detected", title="Extension field for ``detected``."
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="The Encounter associated with the start of the AdverseEvent",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    expectedInResearchStudy: bool = Field(
        None,
        alias="expectedInResearchStudy",
        title="Considered likely or probable or anticipated in the research study",
        description=(
            "Considered likely or probable or anticipated in the research study.  "
            "Whether the reported event matches any of the outcomes for the patient"
            " that are considered by the study as known or likely."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    expectedInResearchStudy__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_expectedInResearchStudy",
        title="Extension field for ``expectedInResearchStudy``.",
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier for the event",
        description=(
            "Business identifiers assigned to this adverse event by the performer "
            "or other systems which remain constant as the resource is updated and "
            "propagates from server to server."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title="Location where adverse event occurred",
        description="The information about where the adverse event occurred.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    mitigatingAction: typing.List[fhirtypes.AdverseEventMitigatingActionType] = Field(
        None,
        alias="mitigatingAction",
        title=(
            "Ameliorating actions taken after the adverse event occured in order to"
            " reduce the extent of harm"
        ),
        description=(
            "The ameliorating action taken after the adverse event occured in order"
            " to reduce the extent of harm."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Comment on adverse event",
        description=(
            "Comments made about the adverse event by the performer, subject or "
            "other participants."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    occurrenceDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurrenceDateTime",
        title="When the event occurred",
        description="The date (and perhaps time) when the adverse event occurred.",
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
        title="When the event occurred",
        description="The date (and perhaps time) when the adverse event occurred.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )

    occurrenceTiming: fhirtypes.TimingType = Field(
        None,
        alias="occurrenceTiming",
        title="When the event occurred",
        description="The date (and perhaps time) when the adverse event occurred.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )

    outcome: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="outcome",
        title="Type of outcome from the adverse event",
        description=(
            "Describes the type of outcome from the adverse event, such as "
            "resolved, recovering, ongoing, resolved-with-sequelae, or fatal."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    participant: typing.List[fhirtypes.AdverseEventParticipantType] = Field(
        None,
        alias="participant",
        title=(
            "Who was involved in the adverse event or the potential adverse event "
            "and what they did"
        ),
        description=(
            "Indicates who or what participated in the adverse event and how they "
            "were involved."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    preventiveAction: typing.List[fhirtypes.AdverseEventPreventiveActionType] = Field(
        None,
        alias="preventiveAction",
        title="Preventive actions that contributed to avoiding the adverse event",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    recordedDate: fhirtypes.DateTime = Field(
        None,
        alias="recordedDate",
        title="When the event was recorded",
        description=(
            "The date on which the existence of the AdverseEvent was first " "recorded."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    recordedDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_recordedDate", title="Extension field for ``recordedDate``."
    )

    recorder: fhirtypes.ReferenceType = Field(
        None,
        alias="recorder",
        title="Who recorded the adverse event",
        description=(
            "Information on who recorded the adverse event.  May be the patient or "
            "a practitioner."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "Practitioner",
            "PractitionerRole",
            "RelatedPerson",
            "ResearchSubject",
        ],
    )

    resultingEffect: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="resultingEffect",
        title="Effect on the subject due to this event",
        description=(
            "Information about the condition that occurred as a result of the "
            "adverse event, such as hives due to the exposure to a substance (for "
            "example, a drug or a chemical) or a broken leg as a result of the "
            "fall."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Condition", "Observation"],
    )

    seriousness: fhirtypes.CodeableConceptType = Field(
        None,
        alias="seriousness",
        title="Seriousness or gravity of the event",
        description=(
            "Assessment whether this event, or averted event, was of clinical "
            "importance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="in-progress | completed | entered-in-error | unknown",
        description="The current state of the adverse event or potential adverse event.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["in-progress", "completed", "entered-in-error", "unknown"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    study: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="study",
        title="Research study that the subject is enrolled in",
        description="The research study that the subject is enrolled in.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ResearchStudy"],
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Subject impacted by event",
        description="This subject or group impacted by the event.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "Group",
            "Practitioner",
            "RelatedPerson",
            "ResearchSubject",
        ],
    )

    supportingInfo: typing.List[fhirtypes.AdverseEventSupportingInfoType] = Field(
        None,
        alias="supportingInfo",
        title="Supporting information relevant to the event",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    suspectEntity: typing.List[fhirtypes.AdverseEventSuspectEntityType] = Field(
        None,
        alias="suspectEntity",
        title="The suspected agent causing the adverse event",
        description=(
            "Describes the entity that is suspected to have caused the adverse "
            "event."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AdverseEvent`` according specification,
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
            "actuality",
            "category",
            "code",
            "subject",
            "encounter",
            "occurrenceDateTime",
            "occurrencePeriod",
            "occurrenceTiming",
            "detected",
            "recordedDate",
            "resultingEffect",
            "location",
            "seriousness",
            "outcome",
            "recorder",
            "participant",
            "study",
            "expectedInResearchStudy",
            "suspectEntity",
            "contributingFactor",
            "preventiveAction",
            "mitigatingAction",
            "supportingInfo",
            "note",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1409(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("actuality", "actuality__ext"), ("status", "status__ext")]
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
    def validate_one_of_many_1409(
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
            "occurrence": ["occurrenceDateTime", "occurrencePeriod", "occurrenceTiming"]
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


class AdverseEventContributingFactor(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Contributing factors suspected to have increased the probability or
    severity of the adverse event.
    The contributing factors suspected to have increased the probability or
    severity of the adverse event.
    """

    resource_type = Field("AdverseEventContributingFactor", const=True)

    itemCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="itemCodeableConcept",
        title=(
            "Item suspected to have increased the probability or severity of the "
            "adverse event"
        ),
        description=(
            "The item that is suspected to have increased the probability or "
            "severity of the adverse event."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e item[x]
        one_of_many="item",
        one_of_many_required=True,
    )

    itemReference: fhirtypes.ReferenceType = Field(
        None,
        alias="itemReference",
        title=(
            "Item suspected to have increased the probability or severity of the "
            "adverse event"
        ),
        description=(
            "The item that is suspected to have increased the probability or "
            "severity of the adverse event."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e item[x]
        one_of_many="item",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Condition",
            "Observation",
            "AllergyIntolerance",
            "FamilyMemberHistory",
            "Immunization",
            "Procedure",
            "Device",
            "DeviceUsage",
            "DocumentReference",
            "MedicationAdministration",
            "MedicationStatement",
        ],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AdverseEventContributingFactor`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "itemReference",
            "itemCodeableConcept",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3286(
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
        one_of_many_fields = {"item": ["itemCodeableConcept", "itemReference"]}
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


class AdverseEventMitigatingAction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Ameliorating actions taken after the adverse event occured in order to
    reduce the extent of harm.
    The ameliorating action taken after the adverse event occured in order to
    reduce the extent of harm.
    """

    resource_type = Field("AdverseEventMitigatingAction", const=True)

    itemCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="itemCodeableConcept",
        title=(
            "Ameliorating action taken after the adverse event occured in order to "
            "reduce the extent of harm"
        ),
        description=(
            "The ameliorating action taken after the adverse event occured in order"
            " to reduce the extent of harm."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e item[x]
        one_of_many="item",
        one_of_many_required=True,
    )

    itemReference: fhirtypes.ReferenceType = Field(
        None,
        alias="itemReference",
        title=(
            "Ameliorating action taken after the adverse event occured in order to "
            "reduce the extent of harm"
        ),
        description=(
            "The ameliorating action taken after the adverse event occured in order"
            " to reduce the extent of harm."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e item[x]
        one_of_many="item",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Procedure",
            "DocumentReference",
            "MedicationAdministration",
            "MedicationRequest",
        ],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AdverseEventMitigatingAction`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "itemReference",
            "itemCodeableConcept",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3046(
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
        one_of_many_fields = {"item": ["itemCodeableConcept", "itemReference"]}
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


class AdverseEventParticipant(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who was involved in the adverse event or the potential adverse event and
    what they did.
    Indicates who or what participated in the adverse event and how they were
    involved.
    """

    resource_type = Field("AdverseEventParticipant", const=True)

    actor: fhirtypes.ReferenceType = Field(
        ...,
        alias="actor",
        title="Who was involved in the adverse event or the potential adverse event",
        description="Indicates who or what participated in the event.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "Organization",
            "CareTeam",
            "Patient",
            "Device",
            "RelatedPerson",
            "ResearchSubject",
        ],
    )

    function: fhirtypes.CodeableConceptType = Field(
        None,
        alias="function",
        title="Type of involvement",
        description=(
            "Distinguishes the type of involvement of the actor in the adverse "
            "event, such as contributor or informant."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AdverseEventParticipant`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "function", "actor"]


class AdverseEventPreventiveAction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Preventive actions that contributed to avoiding the adverse event.
    """

    resource_type = Field("AdverseEventPreventiveAction", const=True)

    itemCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="itemCodeableConcept",
        title="Action that contributed to avoiding the adverse event",
        description="The action that contributed to avoiding the adverse event.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e item[x]
        one_of_many="item",
        one_of_many_required=True,
    )

    itemReference: fhirtypes.ReferenceType = Field(
        None,
        alias="itemReference",
        title="Action that contributed to avoiding the adverse event",
        description="The action that contributed to avoiding the adverse event.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e item[x]
        one_of_many="item",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Immunization",
            "Procedure",
            "DocumentReference",
            "MedicationAdministration",
            "MedicationRequest",
        ],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AdverseEventPreventiveAction`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "itemReference",
            "itemCodeableConcept",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3073(
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
        one_of_many_fields = {"item": ["itemCodeableConcept", "itemReference"]}
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


class AdverseEventSupportingInfo(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Supporting information relevant to the event.
    """

    resource_type = Field("AdverseEventSupportingInfo", const=True)

    itemCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="itemCodeableConcept",
        title="Subject medical history or document relevant to this adverse event",
        description=(
            "Relevant past history for the subject. In a clinical care context, an "
            "example being a patient had an adverse event following a pencillin "
            "administration and the patient had a previously documented penicillin "
            "allergy. In a clinical trials context, an example is a bunion or rash "
            "that was present prior to the study. Additionally, the supporting item"
            " can be a document that is relevant to this instance of the adverse "
            "event that is not part of the subject's medical history. For example, "
            "a clinical note, staff list, or material safety data sheet (MSDS).  "
            "Supporting information is not a contributing factor, preventive "
            "action, or mitigating action."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e item[x]
        one_of_many="item",
        one_of_many_required=True,
    )

    itemReference: fhirtypes.ReferenceType = Field(
        None,
        alias="itemReference",
        title="Subject medical history or document relevant to this adverse event",
        description=(
            "Relevant past history for the subject. In a clinical care context, an "
            "example being a patient had an adverse event following a pencillin "
            "administration and the patient had a previously documented penicillin "
            "allergy. In a clinical trials context, an example is a bunion or rash "
            "that was present prior to the study. Additionally, the supporting item"
            " can be a document that is relevant to this instance of the adverse "
            "event that is not part of the subject's medical history. For example, "
            "a clinical note, staff list, or material safety data sheet (MSDS).  "
            "Supporting information is not a contributing factor, preventive "
            "action, or mitigating action."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e item[x]
        one_of_many="item",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Condition",
            "Observation",
            "AllergyIntolerance",
            "FamilyMemberHistory",
            "Immunization",
            "Procedure",
            "DocumentReference",
            "MedicationAdministration",
            "MedicationStatement",
            "QuestionnaireResponse",
        ],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AdverseEventSupportingInfo`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "itemReference",
            "itemCodeableConcept",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2883(
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
        one_of_many_fields = {"item": ["itemCodeableConcept", "itemReference"]}
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


class AdverseEventSuspectEntity(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The suspected agent causing the adverse event.
    Describes the entity that is suspected to have caused the adverse event.
    """

    resource_type = Field("AdverseEventSuspectEntity", const=True)

    causality: fhirtypes.AdverseEventSuspectEntityCausalityType = Field(
        None,
        alias="causality",
        title="Information on the possible cause of the event",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    instanceCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="instanceCodeableConcept",
        title="Refers to the specific entity that caused the adverse event",
        description=(
            "Identifies the actual instance of what caused the adverse event.  May "
            "be a substance, medication, medication administration, medication "
            "statement or a device."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e instance[x]
        one_of_many="instance",
        one_of_many_required=True,
    )

    instanceReference: fhirtypes.ReferenceType = Field(
        None,
        alias="instanceReference",
        title="Refers to the specific entity that caused the adverse event",
        description=(
            "Identifies the actual instance of what caused the adverse event.  May "
            "be a substance, medication, medication administration, medication "
            "statement or a device."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e instance[x]
        one_of_many="instance",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Immunization",
            "Procedure",
            "Substance",
            "Medication",
            "MedicationAdministration",
            "MedicationStatement",
            "Device",
            "BiologicallyDerivedProduct",
            "ResearchStudy",
        ],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AdverseEventSuspectEntity`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "instanceCodeableConcept",
            "instanceReference",
            "causality",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2794(
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
            "instance": ["instanceCodeableConcept", "instanceReference"]
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


class AdverseEventSuspectEntityCausality(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information on the possible cause of the event.
    """

    resource_type = Field("AdverseEventSuspectEntityCausality", const=True)

    assessmentMethod: fhirtypes.CodeableConceptType = Field(
        None,
        alias="assessmentMethod",
        title=(
            "Method of evaluating the relatedness of the suspected entity to the "
            "event"
        ),
        description=(
            "The method of evaluating the relatedness of the suspected entity to "
            "the event."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title="Author of the information on the possible cause of the event",
        description="The author of the information on the possible cause of the event.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "Patient",
            "RelatedPerson",
            "ResearchSubject",
        ],
    )

    entityRelatedness: fhirtypes.CodeableConceptType = Field(
        None,
        alias="entityRelatedness",
        title=(
            "Result of the assessment regarding the relatedness of the suspected "
            "entity to the event"
        ),
        description=(
            "The result of the assessment regarding the relatedness of the "
            "suspected entity to the event."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AdverseEventSuspectEntityCausality`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "assessmentMethod",
            "entityRelatedness",
            "author",
        ]
