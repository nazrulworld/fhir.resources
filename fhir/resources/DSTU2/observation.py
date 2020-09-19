# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Observation
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import fhirtypes
from .backboneelement import BackboneElement
from .domainresource import DomainResource


class Observation(DomainResource):
    """Measurements and simple assertions.

    Measurements and simple assertions made about a patient, device or other
    subject.
    """

    resource_type = Field("Observation", const=True)

    comments: fhirtypes.String = Field(
        None,
        alias="comments",
        title="Type `str`.",
        description="Comments about result.",
    )
    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code`.",
        description="registered | preliminary | final | amended +.",
    )

    bodySite: fhirtypes.CodeableConceptType = Field(
        None,
        alias="bodySite",
        title="Type `CodeableConcept`.",
        description="Observed body part.",
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Classification of  type of observation.",
    )
    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Type of observation (code / type).",
    )

    component: ListType[fhirtypes.ObservationComponentType] = Field(
        None,
        alias="component",
        title="List of `ObservationComponent` items (represented as `dict` in JSON).",
        description="Component results.",
    )

    dataAbsentReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="dataAbsentReason",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Why the result is missing.",
    )
    device: fhirtypes.ReferenceType = Field(
        None,
        alias="device",
        title=(
            "Type `Reference` referencing `Device, DeviceMetric`"
            " (represented as `dict` in JSON)."
        ),
        description="(Measurement) Device.",
    )

    effectiveDateTime: fhirtypes.DateTime = Field(
        None,
        alias="effectiveDateTime",
        title="Type `DateTime` .",
        description="Clinically relevant time/time-period for observation.",
        one_of_many="effective",  # Choice of Data Types. i.e effective[x]
        one_of_many_required=False,
    )
    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="Type `Period` (represented as `dict` in JSON).",
        description="Clinically relevant time/time-period for observation.",
        one_of_many="effective",  # Choice of Data Types. i.e effective[x]
        one_of_many_required=False,
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Type `Reference` referencing `Encounter` (represented as `dict` in JSON).",
        description="Healthcare event during which this observation is made.",
    )

    interpretation: fhirtypes.CodeableConceptType = Field(
        None,
        alias="interpretation",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="High, low, normal, etc.",
    )

    issued: fhirtypes.Instant = Field(
        None,
        alias="issued",
        title="Type `Instant`.",
        description="Date/Time this was made available.",
    )

    method: fhirtypes.CodeableConceptType = Field(
        None,
        alias="method",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="How it was done.",
    )

    performer: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="performer",
        title=(
            "List of `Reference` items referencing `Practitioner, "
            "Organization, Patient, RelatedPerson` (represented as `dict` in JSON)."
        ),
        description="Who is responsible for the observation.",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON).",
        description="Unique Id for this particular observation.",
    )

    referenceRange: ListType[fhirtypes.ObservationReferenceRangeType] = Field(
        None,
        alias="referenceRange",
        title="List of `ObservationReferenceRange` items (represented as `dict` in JSON).",
        description="Provides guide for interpretation.",
    )

    related: ListType[fhirtypes.ObservationRelatedType] = Field(
        None,
        alias="related",
        title="List of `ObservationRelated` items (represented as `dict` in JSON).",
        description="Resource related to this observation.",
    )
    specimen: fhirtypes.ReferenceType = Field(
        None,
        alias="specimen",
        title="Type `Reference` referencing `Specimen` (represented as `dict` in JSON).",
        description="Specimen used for this observation.",
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title=(
            "Type `Reference` referencing `Patient, Group, Device, "
            "Location` (represented as `dict` in JSON)."
        ),
        description="Who and/or what this is about.",
    )

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="Type `Attachment` (represented as `dict` in JSON).",
        description="Actual result.",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="valueCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Actual result.",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="valueDateTime",
        title="Type `DateTime`.",
        description="Actual result.",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valuePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="valuePeriod",
        title="Type `Period` (represented as `dict` in JSON).",
        description="Actual result.",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="Type `Quantity` (represented as `dict` in JSON).",
        description="Actual result.",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueRange: fhirtypes.RangeType = Field(
        None,
        alias="valueRange",
        title="Type `Range` (represented as `dict` in JSON).",
        description="Actual result.",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueRatio: fhirtypes.RatioType = Field(
        None,
        alias="valueRatio",
        title="Type `Ratio` (represented as `dict` in JSON).",
        description="Actual result.",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueSampledData: fhirtypes.SampledDataType = Field(
        None,
        alias="valueSampledData",
        title="Type `SampledData` (represented as `dict` in JSON).",
        description="Actual result.",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Type `String`.",
        description="Actual result.",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueTime: fhirtypes.Time = Field(
        None,
        alias="valueTime",
        title="Type `Time`.",
        description="Actual result.",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
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
            "effective": ["effectiveDateTime", "effectivePeriod"],
            "value": [
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


class ObservationComponent(BackboneElement):
    """Component results.

    Some observations have multiple component observations.  These component
    observations are expressed as separate code value pairs that share the same
    attributes.  Examples include systolic and diastolic component observations
    for blood pressure measurement and multiple component observations for
    genetics observations.
    """

    resource_type = Field("ObservationComponent", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Type of component observation (code / type).",
    )

    dataAbsentReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="dataAbsentReason",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Why the component result is missing.",
    )

    referenceRange: ListType[fhirtypes.ObservationReferenceRangeType] = Field(
        None,
        alias="referenceRange",
        title="List of `ObservationReferenceRange` items (represented as `dict` in JSON).",
        description="Provides guide for interpretation of component result.",
    )

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="Type `Attachment` (represented as `dict` in JSON).",
        description="Actual component result.",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="valueCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Actual component result.",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="valueDateTime",
        title="Type `DateTime`.",
        description="Actual component result.",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valuePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="valuePeriod",
        title="Type `Period` (represented as `dict` in JSON).",
        description="Actual component result.",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="Type `Quantity` (represented as `dict` in JSON).",
        description="Actual component result.",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueRange: fhirtypes.RangeType = Field(
        None,
        alias="valueRange",
        title="Type `Range` (represented as `dict` in JSON).",
        description="Actual component result.",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueRatio: fhirtypes.RatioType = Field(
        None,
        alias="valueRatio",
        title="Type `Ratio` (represented as `dict` in JSON).",
        description="Actual component result.",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueSampledData: fhirtypes.SampledDataType = Field(
        None,
        alias="valueSampledData",
        title="Type `SampledData` (represented as `dict` in JSON).",
        description="Actual component result.",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Type `String`.",
        description="Actual component result.",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueTime: fhirtypes.Time = Field(
        None,
        alias="valueTime",
        title="Type `Time`.",
        description="Actual component result.",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
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
            "value": [
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


class ObservationReferenceRange(BackboneElement):
    """Provides guide for interpretation.

    Guidance on how to interpret the value by comparison to a normal or
    recommended range.
    """

    resource_type = Field("ObservationReferenceRange", const=True)

    age: fhirtypes.RangeType = Field(
        None,
        alias="age",
        title="Type `Range` (represented as `dict` in JSON).",
        description="Applicable age range, if relevant.",
    )
    high: fhirtypes.QuantityType = Field(
        None,
        alias="high",
        title="Type `Quantity` (represented as `dict` in JSON).",
        description="High Range, if relevant.",
    )

    low: fhirtypes.QuantityType = Field(
        None,
        alias="low",
        title="Type `Quantity` (represented as `dict` in JSON).",
        description="Low Range, if relevant.",
    )

    meaning: fhirtypes.CodeableConceptType = Field(
        None,
        alias="meaning",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Indicates the meaning/use of this range of this range.",
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Type `str`.",
        description="Text based reference range in an observation.",
    )


class ObservationRelated(BackboneElement):
    """Resource related to this observation.

    A  reference to another resource (usually another Observation but could
    also be a QuestionnaireAnswer) whose relationship is defined by the
    relationship type code.
    """

    resource_type = Field("ObservationRelated", const=True)

    target: fhirtypes.ReferenceType = Field(
        None,
        alias="target",
        title=(
            "Type `Reference` referencing `Observation, "
            "QuestionnaireResponse` (represented as `dict` in JSON)."
        ),
        description="Resource that is related to this one.",
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="Type `Code`.",
        description=(
            "has-member | derived-from | sequel-to | "
            "replaces | qualified-by | interfered-by."
        ),
    )
