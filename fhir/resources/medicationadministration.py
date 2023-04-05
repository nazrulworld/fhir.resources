# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationAdministration
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


class MedicationAdministration(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Administration of medication to a patient.
    Describes the event of a patient consuming or otherwise being administered
    a medication.  This may be as simple as swallowing a tablet or it may be a
    long running infusion.  Related resources tie this event to the authorizing
    prescription, and the specific encounter between patient and health care
    practitioner.
    """

    resource_type = Field("MedicationAdministration", const=True)

    basedOn: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="Plan this is fulfilled by this administration",
        description=(
            "A plan that is fulfilled in whole or in part by this "
            "MedicationAdministration."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["CarePlan"],
    )

    category: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="Type of medication administration",
        description=(
            "The type of medication administration (for example, drug "
            "classification like ATC, where meds would be administered, legal "
            "category of the medication)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    device: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="device",
        title="Device used to administer",
        description=(
            "The device that is to be used for the administration of the medication"
            " (for example, PCA Pump)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device"],
    )

    dosage: fhirtypes.MedicationAdministrationDosageType = Field(
        None,
        alias="dosage",
        title="Details of how medication was taken",
        description=(
            "Describes the medication dosage information details e.g. dose, rate, "
            "site, route, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Encounter administered as part of",
        description=(
            "The visit, admission, or other contact between patient and health care"
            " provider during which the medication administration was performed."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    eventHistory: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="eventHistory",
        title="A list of events of interest in the lifecycle",
        description=(
            "A summary of the events of interest that have occurred, such as when "
            "the administration was verified."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Provenance"],
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="External identifier",
        description=(
            "Identifiers associated with this Medication Administration that are "
            "defined by business processes and/or used to refer to it when a direct"
            " URL reference to the resource itself is not appropriate. They are "
            "business identifiers assigned to this resource by the performer or "
            "other systems and remain constant as the resource is updated and "
            "propagates from server to server."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    isSubPotent: bool = Field(
        None,
        alias="isSubPotent",
        title="Full dose was not administered",
        description="An indication that the full dose was not administered.",
        # if property is element of this resource.
        element_property=True,
    )
    isSubPotent__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_isSubPotent", title="Extension field for ``isSubPotent``."
    )

    medication: fhirtypes.CodeableReferenceType = Field(
        ...,
        alias="medication",
        title="What was administered",
        description=(
            "Identifies the medication that was administered. This is either a link"
            " to a resource representing the details of the medication or a simple "
            "attribute carrying a code that identifies the medication from a known "
            "list of medications."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Medication"],
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Information about the administration",
        description=(
            "Extra information about the medication administration that is not "
            "conveyed by the other attributes."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    occurenceDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurenceDateTime",
        title=(
            "Specific date/time or interval of time during which the administration"
            " took place (or did not take place)"
        ),
        description=(
            "A specific date/time or interval of time during which the "
            "administration took place (or did not take place). For many "
            "administrations, such as swallowing a tablet the use of dateTime is "
            "more appropriate."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurence[x]
        one_of_many="occurence",
        one_of_many_required=True,
    )
    occurenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_occurenceDateTime",
        title="Extension field for ``occurenceDateTime``.",
    )

    occurencePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="occurencePeriod",
        title=(
            "Specific date/time or interval of time during which the administration"
            " took place (or did not take place)"
        ),
        description=(
            "A specific date/time or interval of time during which the "
            "administration took place (or did not take place). For many "
            "administrations, such as swallowing a tablet the use of dateTime is "
            "more appropriate."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurence[x]
        one_of_many="occurence",
        one_of_many_required=True,
    )

    occurenceTiming: fhirtypes.TimingType = Field(
        None,
        alias="occurenceTiming",
        title=(
            "Specific date/time or interval of time during which the administration"
            " took place (or did not take place)"
        ),
        description=(
            "A specific date/time or interval of time during which the "
            "administration took place (or did not take place). For many "
            "administrations, such as swallowing a tablet the use of dateTime is "
            "more appropriate."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurence[x]
        one_of_many="occurence",
        one_of_many_required=True,
    )

    partOf: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title="Part of referenced event",
        description="A larger event of which this particular event is a component or step.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "MedicationAdministration",
            "Procedure",
            "MedicationDispense",
        ],
    )

    performer: typing.List[fhirtypes.MedicationAdministrationPerformerType] = Field(
        None,
        alias="performer",
        title=(
            "Who or what performed the medication administration and what type of "
            "performance they did"
        ),
        description=(
            "The performer of the medication treatment.  For devices this is the "
            "device that performed the administration of the medication.  An IV "
            "Pump would be an example of a device that is performing the "
            "administration. Both the IV Pump and the practitioner that set the "
            "rate or bolus on the pump can be listed as performers."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    reason: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="reason",
        title=(
            "Concept, condition or observation that supports why the medication was"
            " administered"
        ),
        description=(
            "A code, Condition or observation that supports why the medication was "
            "administered."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Condition", "Observation", "DiagnosticReport"],
    )

    recorded: fhirtypes.DateTime = Field(
        None,
        alias="recorded",
        title=(
            "When the MedicationAdministration was first captured in the subject's "
            "record"
        ),
        description=(
            "The date the occurrence of the  MedicationAdministration was first "
            "captured in the record - potentially significantly after the "
            "occurrence of the event."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    recorded__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_recorded", title="Extension field for ``recorded``."
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title="Request administration performed against",
        description=(
            "The original request, instruction or authority to perform the "
            "administration."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicationRequest"],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title=(
            "in-progress | not-done | on-hold | completed | entered-in-error | "
            "stopped | unknown"
        ),
        description=(
            "Will generally be set to show that the administration has been "
            "completed.  For some long running administrations such as infusions, "
            "it is possible for an administration to be started but not completed "
            "or it may be paused while some other process is under way."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "in-progress",
            "not-done",
            "on-hold",
            "completed",
            "entered-in-error",
            "stopped",
            "unknown",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    statusReason: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="statusReason",
        title="Reason administration not performed",
        description="A code indicating why the administration was not performed.",
        # if property is element of this resource.
        element_property=True,
    )

    subPotentReason: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="subPotentReason",
        title="Reason full dose was not administered",
        description="The reason or reasons why the full dose was not administered.",
        # if property is element of this resource.
        element_property=True,
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Who received medication",
        description="The person or animal or group receiving the medication.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group"],
    )

    supportingInformation: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingInformation",
        title="Additional information to support administration",
        description=(
            "Additional information (for example, patient height and weight) that "
            "supports the administration of the medication.  This attribute can be "
            "used to provide documentation of specific characteristics of the "
            "patient present at the time of administration.  For example, if the "
            'dose says "give "x" if the heartrate exceeds "y"", then the heart rate'
            " can be included using this attribute."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationAdministration`` according specification,
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
            "basedOn",
            "partOf",
            "status",
            "statusReason",
            "category",
            "medication",
            "subject",
            "encounter",
            "supportingInformation",
            "occurenceDateTime",
            "occurencePeriod",
            "occurenceTiming",
            "recorded",
            "isSubPotent",
            "subPotentReason",
            "performer",
            "reason",
            "request",
            "device",
            "note",
            "dosage",
            "eventHistory",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2686(
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
    def validate_one_of_many_2686(
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
            "occurence": ["occurenceDateTime", "occurencePeriod", "occurenceTiming"]
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


class MedicationAdministrationDosage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details of how medication was taken.
    Describes the medication dosage information details e.g. dose, rate, site,
    route, etc.
    """

    resource_type = Field("MedicationAdministrationDosage", const=True)

    dose: fhirtypes.QuantityType = Field(
        None,
        alias="dose",
        title="Amount of medication per dose",
        description=(
            "The amount of the medication given at one administration event.   Use "
            "this value when the administration is essentially an instantaneous "
            "event such as a swallowing a tablet or giving an injection."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    method: fhirtypes.CodeableConceptType = Field(
        None,
        alias="method",
        title="How drug was administered",
        description=(
            "A coded value indicating the method by which the medication is "
            "intended to be or was introduced into or on the body.  This attribute "
            "will most often NOT be populated.  It is most commonly used for "
            "injections.  For example, Slow Push, Deep IV."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    rateQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="rateQuantity",
        title="Dose quantity per unit of time",
        description=(
            "Identifies the speed with which the medication was or will be "
            "introduced into the patient.  Typically, the rate for an infusion e.g."
            " 100 ml per 1 hour or 100 ml/hr.  May also be expressed as a rate per "
            "unit of time, e.g. 500 ml per 2 hours.  Other examples:  200 mcg/min "
            "or 200 mcg/1 minute; 1 liter/8 hours."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e rate[x]
        one_of_many="rate",
        one_of_many_required=False,
    )

    rateRatio: fhirtypes.RatioType = Field(
        None,
        alias="rateRatio",
        title="Dose quantity per unit of time",
        description=(
            "Identifies the speed with which the medication was or will be "
            "introduced into the patient.  Typically, the rate for an infusion e.g."
            " 100 ml per 1 hour or 100 ml/hr.  May also be expressed as a rate per "
            "unit of time, e.g. 500 ml per 2 hours.  Other examples:  200 mcg/min "
            "or 200 mcg/1 minute; 1 liter/8 hours."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e rate[x]
        one_of_many="rate",
        one_of_many_required=False,
    )

    route: fhirtypes.CodeableConceptType = Field(
        None,
        alias="route",
        title="Path of substance into body",
        description=(
            "A code specifying the route or physiological path of administration of"
            " a therapeutic agent into or onto the patient.  For example, topical, "
            "intravenous, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    site: fhirtypes.CodeableConceptType = Field(
        None,
        alias="site",
        title="Body site administered to",
        description=(
            "A coded specification of the anatomic site where the medication first "
            'entered the body.  For example, "left arm".'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Free text dosage instructions e.g. SIG",
        description=(
            "Free text dosage can be used for cases where the dosage administered "
            "is too complex to code. When coded dosage is present, the free text "
            "dosage may still be present for display to humans.  The dosage "
            "instructions should reflect the dosage of the medication that was "
            "administered."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationAdministrationDosage`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "text",
            "site",
            "route",
            "method",
            "dose",
            "rateRatio",
            "rateQuantity",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3272(
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
        one_of_many_fields = {"rate": ["rateQuantity", "rateRatio"]}
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


class MedicationAdministrationPerformer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who or what performed the medication administration and what type of
    performance they did.
    The performer of the medication treatment.  For devices this is the device
    that performed the administration of the medication.  An IV Pump would be
    an example of a device that is performing the administration. Both the IV
    Pump and the practitioner that set the rate or bolus on the pump can be
    listed as performers.
    """

    resource_type = Field("MedicationAdministrationPerformer", const=True)

    actor: fhirtypes.CodeableReferenceType = Field(
        ...,
        alias="actor",
        title="Who or what performed the medication administration",
        description="Indicates who or what performed the medication administration.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
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
            "medication administration."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationAdministrationPerformer`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "function", "actor"]
