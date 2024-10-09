from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Observation
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Observation(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Measurements and simple assertions.
    Measurements and simple assertions made about a patient, device or other
    subject.
    """

    __resource_type__ = "Observation"

    basedOn: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="basedOn",
        title="Fulfills plan, proposal or order",
        description=(
            "A plan, proposal or order that is fulfilled in whole or in part by "
            "this event."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "CarePlan",
                "DeviceRequest",
                "ImmunizationRecommendation",
                "MedicationRequest",
                "NutritionOrder",
                "ProcedureRequest",
                "ReferralRequest",
            ],
        },
    )

    bodySite: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="bodySite",
        title="Observed body part",
        description=(
            "Indicates the site on the subject's body where the observation was "
            "made (i.e. the target site)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    category: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="category",
        title="Classification of  type of observation",
        description="A code that classifies the general type of observation being made.",
        json_schema_extra={
            "element_property": True,
        },
    )

    code: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="code",
        title="Type of observation (code / type)",
        description=(
            "Describes what was observed. Sometimes this is called the observation "
            '"name".'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    comment: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="comment",
        title="Comments about result",
        description=(
            "May include statements about significant, unexpected or unreliable "
            "values, or information about the source of the value where this may be"
            " relevant to the interpretation of the result."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_comment", title="Extension field for ``comment``."
    )

    component: typing.List[fhirtypes.ObservationComponentType] | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )

    context: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="context",
        title="Healthcare event during which this observation is made",
        description=(
            "The healthcare event  (e.g. a patient and healthcare provider "
            "interaction) during which this observation is made."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter", "EpisodeOfCare"],
        },
    )

    dataAbsentReason: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="dataAbsentReason",
        title="Why the result is missing",
        description=(
            "Provides a reason why the expected value in the element "
            "Observation.value[x] is missing."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    device: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="device",
        title="(Measurement) Device",
        description="The device used to generate the observation data.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Device", "DeviceMetric"],
        },
    )

    effectiveDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e effective[x]
            "one_of_many": "effective",
            "one_of_many_required": False,
        },
    )
    effectiveDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_effectiveDateTime",
        title="Extension field for ``effectiveDateTime``.",
    )

    effectivePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e effective[x]
            "one_of_many": "effective",
            "one_of_many_required": False,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business Identifier for observation",
        description="A unique identifier assigned to this observation.",
        json_schema_extra={
            "element_property": True,
        },
    )

    interpretation: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="interpretation",
        title="High, low, normal, etc.",
        description=(
            "The assessment made based on the result of the observation.  Intended "
            "as a simple compact code often placed adjacent to the result value in "
            "reports and flow sheets to signal the meaning/normalcy status of the "
            "result. Otherwise known as abnormal flag."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    issued: fhirtypes.InstantType | None = Field(  # type: ignore
        None,
        alias="issued",
        title="Date/Time this was made available",
        description=(
            "The date and time this observation was made available to providers, "
            "typically after the results have been reviewed and verified."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    issued__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_issued", title="Extension field for ``issued``."
    )

    method: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="method",
        title="How it was done",
        description="Indicates the mechanism used to perform the observation.",
        json_schema_extra={
            "element_property": True,
        },
    )

    performer: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="performer",
        title="Who is responsible for the observation",
        description='Who was responsible for asserting the observed value as "true".',
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "Organization",
                "Patient",
                "RelatedPerson",
            ],
        },
    )

    referenceRange: typing.List[fhirtypes.ObservationReferenceRangeType] | None = Field(  # type: ignore
        None,
        alias="referenceRange",
        title="Provides guide for interpretation",
        description=(
            "Guidance on how to interpret the value by comparison to a normal or "
            "recommended range."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    related: typing.List[fhirtypes.ObservationRelatedType] | None = Field(  # type: ignore
        None,
        alias="related",
        title="Resource related to this observation",
        description=(
            "A  reference to another resource (usually another Observation) whose "
            "relationship is defined by the relationship type code."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    specimen: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="specimen",
        title="Specimen used for this observation",
        description="The specimen that was used when this observation was made.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Specimen"],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="registered | preliminary | final | amended +",
        description="The status of the result value.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["registered", "preliminary", "final", "amended", "+"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "Group", "Device", "Location"],
        },
    )

    valueAttachment: fhirtypes.AttachmentType | None = Field(  # type: ignore
        None,
        alias="valueAttachment",
        title="Actual result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueBoolean: bool | None = Field(  # type: ignore
        None,
        alias="valueBoolean",
        title="Actual result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="valueCodeableConcept",
        title="Actual result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="valueDateTime",
        title="Actual result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueDateTime", title="Extension field for ``valueDateTime``."
    )

    valuePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="valuePeriod",
        title="Actual result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="valueQuantity",
        title="Actual result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueRange: fhirtypes.RangeType | None = Field(  # type: ignore
        None,
        alias="valueRange",
        title="Actual result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueRatio: fhirtypes.RatioType | None = Field(  # type: ignore
        None,
        alias="valueRatio",
        title="Actual result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueSampledData: fhirtypes.SampledDataType | None = Field(  # type: ignore
        None,
        alias="valueSampledData",
        title="Actual result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="valueString",
        title="Actual result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    valueTime: fhirtypes.TimeType | None = Field(  # type: ignore
        None,
        alias="valueTime",
        title="Actual result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
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
        return one_of_many_fields


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

    __resource_type__ = "ObservationComponent"

    code: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="code",
        title="Type of component observation (code / type)",
        description=(
            "Describes what was observed. Sometimes this is called the observation "
            '"code".'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    dataAbsentReason: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="dataAbsentReason",
        title="Why the component result is missing",
        description=(
            "Provides a reason why the expected value in the element "
            "Observation.value[x] is missing."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    interpretation: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="interpretation",
        title="High, low, normal, etc.",
        description=(
            "The assessment made based on the result of the observation.  Intended "
            "as a simple compact code often placed adjacent to the result value in "
            "reports and flow sheets to signal the meaning/normalcy status of the "
            "result. Otherwise known as abnormal flag."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    referenceRange: typing.List[fhirtypes.ObservationReferenceRangeType] | None = Field(  # type: ignore
        None,
        alias="referenceRange",
        title="Provides guide for interpretation of component result",
        description=(
            "Guidance on how to interpret the value by comparison to a normal or "
            "recommended range."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    valueAttachment: fhirtypes.AttachmentType | None = Field(  # type: ignore
        None,
        alias="valueAttachment",
        title="Actual component result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="valueCodeableConcept",
        title="Actual component result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="valueDateTime",
        title="Actual component result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueDateTime", title="Extension field for ``valueDateTime``."
    )

    valuePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="valuePeriod",
        title="Actual component result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="valueQuantity",
        title="Actual component result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueRange: fhirtypes.RangeType | None = Field(  # type: ignore
        None,
        alias="valueRange",
        title="Actual component result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueRatio: fhirtypes.RatioType | None = Field(  # type: ignore
        None,
        alias="valueRatio",
        title="Actual component result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueSampledData: fhirtypes.SampledDataType | None = Field(  # type: ignore
        None,
        alias="valueSampledData",
        title="Actual component result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="valueString",
        title="Actual component result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    valueTime: fhirtypes.TimeType | None = Field(  # type: ignore
        None,
        alias="valueTime",
        title="Actual component result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
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
        return one_of_many_fields


class ObservationReferenceRange(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Provides guide for interpretation.
    Guidance on how to interpret the value by comparison to a normal or
    recommended range.
    """

    __resource_type__ = "ObservationReferenceRange"

    age: fhirtypes.RangeType | None = Field(  # type: ignore
        None,
        alias="age",
        title="Applicable age range, if relevant",
        description=(
            "The age at which this reference range is applicable. This is a "
            "neonatal age (e.g. number of weeks at term) if the meaning says so."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    appliesTo: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="appliesTo",
        title="Reference range population",
        description=(
            "Codes to indicate the target population this reference range applies "
            "to.  For example, a reference range may be based on the normal "
            "population or a particular sex or race."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    high: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="high",
        title="High Range, if relevant",
        description=(
            "The value of the high bound of the reference range.  The high bound of"
            " the reference range endpoint is inclusive of the value (e.g.  "
            "reference range is >=5 - <=9).   If the high bound is omitted,  it is "
            "assumed to be meaningless (e.g. reference range is >= 2.3)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    low: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="low",
        title="Low Range, if relevant",
        description=(
            "The value of the low bound of the reference range.  The low bound of "
            "the reference range endpoint is inclusive of the value (e.g.  "
            "reference range is >=5 - <=9).   If the low bound is omitted,  it is "
            "assumed to be meaningless (e.g. reference range is <=2.3)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    text: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="text",
        title="Text based reference range in an observation",
        description=(
            "Text based reference range in an observation which may be used when a "
            "quantitative range is not appropriate for an observation.  An example "
            'would be a reference value of "Negative" or a list or table of '
            "'normals'."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_text", title="Extension field for ``text``."
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Reference range qualifier",
        description=(
            "Codes to indicate the what part of the targeted reference population "
            "it applies to. For example, the normal or therapeutic range."
        ),
        json_schema_extra={
            "element_property": True,
        },
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

    __resource_type__ = "ObservationRelated"

    target: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="target",
        title="Resource that is related to this one",
        description=(
            "A reference to the observation or "
            "[QuestionnaireResponse](questionnaireresponse.html#) resource that is "
            "related to this observation."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Observation",
                "QuestionnaireResponse",
                "Sequence",
            ],
        },
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "has-member",
                "derived-from",
                "sequel-to",
                "replaces",
                "qualified-by",
                "interfered-by",
            ],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ObservationRelated`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "target"]
