# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Observation
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class Observation(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Measurements and simple assertions.
    Measurements and simple assertions made about a patient, device or other
    subject.
    """

    resource_type = Field("Observation", const=True)

    basedOn: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="Fulfills plan, proposal or order",
        description=(
            "A plan, proposal or order that is fulfilled in whole or in part by "
            "this event."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "CarePlan",
            "DeviceRequest",
            "ImmunizationRecommendation",
            "MedicationRequest",
            "NutritionOrder",
            "ProcedureRequest",
            "ReferralRequest",
        ],
    )

    bodySite: fhirtypes.CodeableConceptType = Field(
        None,
        alias="bodySite",
        title="Observed body part",
        description=(
            "Indicates the site on the subject's body where the observation was "
            "made (i.e. the target site)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    category: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="Classification of  type of observation",
        description="A code that classifies the general type of observation being made.",
        # if property is element of this resource.
        element_property=True,
    )

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Type of observation (code / type)",
        description=(
            "Describes what was observed. Sometimes this is called the observation "
            '"name".'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Comments about result",
        description=(
            "May include statements about significant, unexpected or unreliable "
            "values, or information about the source of the value where this may be"
            " relevant to the interpretation of the result."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    component: typing.List[fhirtypes.ObservationComponentType] = Field(
        None,
        alias="component",
        title="Component results",
        description=(
            "Some observations have multiple component observations.  These "
            "component observations are expressed as separate code value pairs that"
            " share the same attributes.  Examples include systolic and diastolic "
            "component observations for blood pressure measurement and multiple "
            "component observations for genetics observations."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title="Healthcare event during which this observation is made",
        description=(
            "The healthcare event  (e.g. a patient and healthcare provider "
            "interaction) during which this observation is made."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter", "EpisodeOfCare"],
    )

    dataAbsentReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="dataAbsentReason",
        title="Why the result is missing",
        description=(
            "Provides a reason why the expected value in the element "
            "Observation.value[x] is missing."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    device: fhirtypes.ReferenceType = Field(
        None,
        alias="device",
        title="(Measurement) Device",
        description="The device used to generate the observation data.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device", "DeviceMetric"],
    )

    effectiveDateTime: fhirtypes.DateTime = Field(
        None,
        alias="effectiveDateTime",
        title="Clinically relevant time/time-period for observation",
        description=(
            "The time or time-period the observed value is asserted as being true. "
            "For biological subjects - e.g. human patients - this is usually called"
            ' the "physiologically relevant time". This is usually either the time '
            "of the procedure or of specimen collection, but very often the source "
            "of the date/time is not known, only the date/time itself."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e effective[x]
        one_of_many="effective",
        one_of_many_required=False,
    )
    effectiveDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_effectiveDateTime",
        title="Extension field for ``effectiveDateTime``.",
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="Clinically relevant time/time-period for observation",
        description=(
            "The time or time-period the observed value is asserted as being true. "
            "For biological subjects - e.g. human patients - this is usually called"
            ' the "physiologically relevant time". This is usually either the time '
            "of the procedure or of specimen collection, but very often the source "
            "of the date/time is not known, only the date/time itself."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e effective[x]
        one_of_many="effective",
        one_of_many_required=False,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier for observation",
        description="A unique identifier assigned to this observation.",
        # if property is element of this resource.
        element_property=True,
    )

    interpretation: fhirtypes.CodeableConceptType = Field(
        None,
        alias="interpretation",
        title="High, low, normal, etc.",
        description=(
            "The assessment made based on the result of the observation.  Intended "
            "as a simple compact code often placed adjacent to the result value in "
            "reports and flow sheets to signal the meaning/normalcy status of the "
            "result. Otherwise known as abnormal flag."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    issued: fhirtypes.Instant = Field(
        None,
        alias="issued",
        title="Date/Time this was made available",
        description=(
            "The date and time this observation was made available to providers, "
            "typically after the results have been reviewed and verified."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    issued__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_issued", title="Extension field for ``issued``."
    )

    method: fhirtypes.CodeableConceptType = Field(
        None,
        alias="method",
        title="How it was done",
        description="Indicates the mechanism used to perform the observation.",
        # if property is element of this resource.
        element_property=True,
    )

    performer: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="performer",
        title="Who is responsible for the observation",
        description='Who was responsible for asserting the observed value as "true".',
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "Organization",
            "Patient",
            "RelatedPerson",
        ],
    )

    referenceRange: typing.List[fhirtypes.ObservationReferenceRangeType] = Field(
        None,
        alias="referenceRange",
        title="Provides guide for interpretation",
        description=(
            "Guidance on how to interpret the value by comparison to a normal or "
            "recommended range."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    related: typing.List[fhirtypes.ObservationRelatedType] = Field(
        None,
        alias="related",
        title="Resource related to this observation",
        description=(
            "A  reference to another resource (usually another Observation) whose "
            "relationship is defined by the relationship type code."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    specimen: fhirtypes.ReferenceType = Field(
        None,
        alias="specimen",
        title="Specimen used for this observation",
        description="The specimen that was used when this observation was made.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Specimen"],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="registered | preliminary | final | amended +",
        description="The status of the result value.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["registered", "preliminary", "final", "amended", "+"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Who and/or what this is about",
        description=(
            "The patient, or group of patients, location, or device whose "
            "characteristics (direct or indirect) are described by the observation "
            "and into whose record the observation is placed.  Comments: Indirect "
            "characteristics may be those of a specimen, fetus, donor,  other "
            "observer (for example a relative or EMT), or any observation made "
            "about the subject."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group", "Device", "Location"],
    )

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="Actual result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="Actual result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="valueCodeableConcept",
        title="Actual result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="valueDateTime",
        title="Actual result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDateTime", title="Extension field for ``valueDateTime``."
    )

    valuePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="valuePeriod",
        title="Actual result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="Actual result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueRange: fhirtypes.RangeType = Field(
        None,
        alias="valueRange",
        title="Actual result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueRatio: fhirtypes.RatioType = Field(
        None,
        alias="valueRatio",
        title="Actual result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueSampledData: fhirtypes.SampledDataType = Field(
        None,
        alias="valueSampledData",
        title="Actual result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Actual result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    valueTime: fhirtypes.Time = Field(
        None,
        alias="valueTime",
        title="Actual result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueTime", title="Extension field for ``valueTime``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Observation`` according specification,
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
            "status",
            "category",
            "code",
            "subject",
            "context",
            "effectiveDateTime",
            "effectivePeriod",
            "issued",
            "performer",
            "valueQuantity",
            "valueCodeableConcept",
            "valueString",
            "valueBoolean",
            "valueRange",
            "valueRatio",
            "valueSampledData",
            "valueAttachment",
            "valueTime",
            "valueDateTime",
            "valuePeriod",
            "dataAbsentReason",
            "interpretation",
            "comment",
            "bodySite",
            "method",
            "specimen",
            "device",
            "referenceRange",
            "related",
            "component",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1353(
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
    def validate_one_of_many_1353(
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
            "effective": ["effectiveDateTime", "effectivePeriod"],
            "value": [
                "valueAttachment",
                "valueBoolean",
                "valueCodeableConcept",
                "valueDateTime",
                "valuePeriod",
                "valueQuantity",
                "valueRange",
                "valueRatio",
                "valueSampledData",
                "valueString",
                "valueTime",
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


class ObservationComponent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Component results.
    Some observations have multiple component observations.  These component
    observations are expressed as separate code value pairs that share the same
    attributes.  Examples include systolic and diastolic component observations
    for blood pressure measurement and multiple component observations for
    genetics observations.
    """

    resource_type = Field("ObservationComponent", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Type of component observation (code / type)",
        description=(
            "Describes what was observed. Sometimes this is called the observation "
            '"code".'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    dataAbsentReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="dataAbsentReason",
        title="Why the component result is missing",
        description=(
            "Provides a reason why the expected value in the element "
            "Observation.value[x] is missing."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    interpretation: fhirtypes.CodeableConceptType = Field(
        None,
        alias="interpretation",
        title="High, low, normal, etc.",
        description=(
            "The assessment made based on the result of the observation.  Intended "
            "as a simple compact code often placed adjacent to the result value in "
            "reports and flow sheets to signal the meaning/normalcy status of the "
            "result. Otherwise known as abnormal flag."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    referenceRange: typing.List[fhirtypes.ObservationReferenceRangeType] = Field(
        None,
        alias="referenceRange",
        title="Provides guide for interpretation of component result",
        description=(
            "Guidance on how to interpret the value by comparison to a normal or "
            "recommended range."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="Actual component result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="valueCodeableConcept",
        title="Actual component result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="valueDateTime",
        title="Actual component result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDateTime", title="Extension field for ``valueDateTime``."
    )

    valuePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="valuePeriod",
        title="Actual component result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="Actual component result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueRange: fhirtypes.RangeType = Field(
        None,
        alias="valueRange",
        title="Actual component result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueRatio: fhirtypes.RatioType = Field(
        None,
        alias="valueRatio",
        title="Actual component result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueSampledData: fhirtypes.SampledDataType = Field(
        None,
        alias="valueSampledData",
        title="Actual component result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Actual component result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    valueTime: fhirtypes.Time = Field(
        None,
        alias="valueTime",
        title="Actual component result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueTime", title="Extension field for ``valueTime``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ObservationComponent`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "valueQuantity",
            "valueCodeableConcept",
            "valueString",
            "valueRange",
            "valueRatio",
            "valueSampledData",
            "valueAttachment",
            "valueTime",
            "valueDateTime",
            "valuePeriod",
            "dataAbsentReason",
            "interpretation",
            "referenceRange",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2306(
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
            "value": [
                "valueAttachment",
                "valueCodeableConcept",
                "valueDateTime",
                "valuePeriod",
                "valueQuantity",
                "valueRange",
                "valueRatio",
                "valueSampledData",
                "valueString",
                "valueTime",
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


class ObservationReferenceRange(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Provides guide for interpretation.
    Guidance on how to interpret the value by comparison to a normal or
    recommended range.
    """

    resource_type = Field("ObservationReferenceRange", const=True)

    age: fhirtypes.RangeType = Field(
        None,
        alias="age",
        title="Applicable age range, if relevant",
        description=(
            "The age at which this reference range is applicable. This is a "
            "neonatal age (e.g. number of weeks at term) if the meaning says so."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    appliesTo: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="appliesTo",
        title="Reference range population",
        description=(
            "Codes to indicate the target population this reference range applies "
            "to.  For example, a reference range may be based on the normal "
            "population or a particular sex or race."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    high: fhirtypes.QuantityType = Field(
        None,
        alias="high",
        title="High Range, if relevant",
        description=(
            "The value of the high bound of the reference range.  The high bound of"
            " the reference range endpoint is inclusive of the value (e.g.  "
            "reference range is >=5 - <=9).   If the high bound is omitted,  it is "
            "assumed to be meaningless (e.g. reference range is >= 2.3)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    low: fhirtypes.QuantityType = Field(
        None,
        alias="low",
        title="Low Range, if relevant",
        description=(
            "The value of the low bound of the reference range.  The low bound of "
            "the reference range endpoint is inclusive of the value (e.g.  "
            "reference range is >=5 - <=9).   If the low bound is omitted,  it is "
            "assumed to be meaningless (e.g. reference range is <=2.3)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Text based reference range in an observation",
        description=(
            "Text based reference range in an observation which may be used when a "
            "quantitative range is not appropriate for an observation.  An example "
            'would be a reference value of "Negative" or a list or table of '
            "'normals'."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Reference range qualifier",
        description=(
            "Codes to indicate the what part of the targeted reference population "
            "it applies to. For example, the normal or therapeutic range."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ObservationReferenceRange`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "low",
            "high",
            "type",
            "appliesTo",
            "age",
            "text",
        ]


class ObservationRelated(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Resource related to this observation.
    A  reference to another resource (usually another Observation) whose
    relationship is defined by the relationship type code.
    """

    resource_type = Field("ObservationRelated", const=True)

    target: fhirtypes.ReferenceType = Field(
        ...,
        alias="target",
        title="Resource that is related to this one",
        description=(
            "A reference to the observation or "
            "[QuestionnaireResponse](questionnaireresponse.html#) resource that is "
            "related to this observation."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Observation", "QuestionnaireResponse", "Sequence"],
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title=(
            "has-member | derived-from | sequel-to | replaces | qualified-by | "
            "interfered-by"
        ),
        description=(
            "A code specifying the kind of relationship that exists with the target"
            " resource."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "has-member",
            "derived-from",
            "sequel-to",
            "replaces",
            "qualified-by",
            "interfered-by",
        ],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ObservationRelated`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "target"]
