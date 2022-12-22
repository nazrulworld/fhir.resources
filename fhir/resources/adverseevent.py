# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AdverseEvent
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class AdverseEvent(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Medical care, research study or other healthcare event causing physical
    injury.
    Actual or  potential/avoided event causing unintended physical injury
    resulting from or contributed to by medical care, a research study or other
    healthcare setting factors that requires additional monitoring, treatment,
    or hospitalization, or that results in death.
    """

    resource_type = Field("AdverseEvent", const=True)

    actuality: fhirtypes.Code = Field(
        None,
        alias="actuality",
        title="actual | potential",
        description=(
            "Whether the event actually happened, or just had the potential to. "
            "Note that this is independent of whether anyone was affected or harmed"
            " or how severely."
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
            "product-problem | product-quality | product-use-error | wrong-dose | "
            "incorrect-prescribing-information | wrong-technique | wrong-route-of-"
            "administration | wrong-rate | wrong-duration | wrong-time | expired-"
            "drug | medical-device-use-error | problem-different-manufacturer | "
            "unsafe-physical-environment"
        ),
        description="The overall type of event, intended for search and filtering purposes.",
        # if property is element of this resource.
        element_property=True,
    )

    contributor: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="contributor",
        title="Who  was involved in the adverse event or the potential adverse event",
        description=(
            "Parties that may or should contribute or have contributed information "
            "to the adverse event, which can consist of one or more activities.  "
            "Such information includes information leading to the decision to "
            "perform the activity and how to perform the activity (e.g. "
            "consultant), information that the activity itself seeks to reveal "
            "(e.g. informant of clinical history), or information about what "
            "activity was performed (e.g. informant witness)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "PractitionerRole", "Device"],
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="When the event occurred",
        description="The date (and perhaps time) when the adverse event occurred.",
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
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
        title="Encounter created as part of",
        description=(
            "The Encounter during which AdverseEvent was created or to which the "
            "creation of this record is tightly associated."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    event: fhirtypes.CodeableConceptType = Field(
        None,
        alias="event",
        title="Type of the event itself in relation to the subject",
        description=(
            "This element defines the specific type of event that occurred or that "
            "was prevented from occurring."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identifier: fhirtypes.IdentifierType = Field(
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

    outcome: fhirtypes.CodeableConceptType = Field(
        None,
        alias="outcome",
        title=(
            "resolved | recovering | ongoing | resolvedWithSequelae | fatal | "
            "unknown"
        ),
        description="Describes the type of outcome from the adverse event.",
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
        ],
    )

    referenceDocument: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="referenceDocument",
        title="AdverseEvent.referenceDocument",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
    )

    resultingCondition: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="resultingCondition",
        title="Effect on the subject due to this event",
        description=(
            "Includes information about the reaction that occurred as a result of "
            "exposure to a substance (for example, a drug or a chemical)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Condition"],
    )

    seriousness: fhirtypes.CodeableConceptType = Field(
        None,
        alias="seriousness",
        title="Seriousness of the event",
        description="Assessment whether this event was of real importance.",
        # if property is element of this resource.
        element_property=True,
    )

    severity: fhirtypes.CodeableConceptType = Field(
        None,
        alias="severity",
        title="mild | moderate | severe",
        description=(
            "Describes the severity of the adverse event, in relation to the "
            "subject. Contrast to AdverseEvent.seriousness - a severe rash might "
            "not be serious, but a mild heart problem is."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    study: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="study",
        title="AdverseEvent.study",
        description=None,
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
        enum_reference_types=["Patient", "Group", "Practitioner", "RelatedPerson"],
    )

    subjectMedicalHistory: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="subjectMedicalHistory",
        title="AdverseEvent.subjectMedicalHistory",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Condition",
            "Observation",
            "AllergyIntolerance",
            "FamilyMemberHistory",
            "Immunization",
            "Procedure",
            "Media",
            "DocumentReference",
        ],
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
            "actuality",
            "category",
            "event",
            "subject",
            "encounter",
            "date",
            "detected",
            "recordedDate",
            "resultingCondition",
            "location",
            "seriousness",
            "severity",
            "outcome",
            "recorder",
            "contributor",
            "suspectEntity",
            "subjectMedicalHistory",
            "referenceDocument",
            "study",
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
        required_fields = [("actuality", "actuality__ext")]
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


class AdverseEventSuspectEntity(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The suspected agent causing the adverse event.
    Describes the entity that is suspected to have caused the adverse event.
    """

    resource_type = Field("AdverseEventSuspectEntity", const=True)

    causality: typing.List[fhirtypes.AdverseEventSuspectEntityCausalityType] = Field(
        None,
        alias="causality",
        title="Information on the possible cause of the event",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    instance: fhirtypes.ReferenceType = Field(
        ...,
        alias="instance",
        title="Refers to the specific entity that caused the adverse event",
        description=(
            "Identifies the actual instance of what caused the adverse event.  May "
            "be a substance, medication, medication administration, medication "
            "statement or a device."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Immunization",
            "Procedure",
            "Substance",
            "Medication",
            "MedicationAdministration",
            "MedicationStatement",
            "Device",
        ],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AdverseEventSuspectEntity`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "instance", "causality"]


class AdverseEventSuspectEntityCausality(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information on the possible cause of the event.
    """

    resource_type = Field("AdverseEventSuspectEntityCausality", const=True)

    assessment: fhirtypes.CodeableConceptType = Field(
        None,
        alias="assessment",
        title="Assessment of if the entity caused the event",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title="AdverseEvent.suspectEntity.causalityAuthor",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "PractitionerRole"],
    )

    method: fhirtypes.CodeableConceptType = Field(
        None,
        alias="method",
        title="ProbabilityScale | Bayesian | Checklist",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    productRelatedness: fhirtypes.String = Field(
        None,
        alias="productRelatedness",
        title="AdverseEvent.suspectEntity.causalityProductRelatedness",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    productRelatedness__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_productRelatedness",
        title="Extension field for ``productRelatedness``.",
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
            "assessment",
            "productRelatedness",
            "author",
            "method",
        ]
