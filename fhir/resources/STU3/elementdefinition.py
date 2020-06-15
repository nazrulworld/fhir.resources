# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ElementDefinition
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import element, fhirtypes


class ElementDefinition(element.Element):
    """ Definition of an element in a resource or extension.
    Captures constraints on each element within the resource, profile, or
    extension.
    """

    resource_type = Field("ElementDefinition", const=True)

    alias: ListType[fhirtypes.String] = Field(
        None,
        alias="alias",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Other names",
    )

    base: fhirtypes.ElementDefinitionBaseType = Field(
        None,
        alias="base",
        title="Type `ElementDefinitionBase` (represented as `dict` in JSON)",
        description="Base definition information for tools",
    )

    binding: fhirtypes.ElementDefinitionBindingType = Field(
        None,
        alias="binding",
        title="Type `ElementDefinitionBinding` (represented as `dict` in JSON)",
        description="ValueSet details if this is coded",
    )

    code: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="code",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="Corresponding codes in terminologies",
    )

    comment: fhirtypes.Markdown = Field(
        None,
        alias="comment",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Comments about the use of this element",
    )

    condition: ListType[fhirtypes.Id] = Field(
        None,
        alias="condition",
        title="List of `Id` items (represented as `dict` in JSON)",
        description="Reference to invariant about presence",
    )

    constraint: ListType[fhirtypes.ElementDefinitionConstraintType] = Field(
        None,
        alias="constraint",
        title=(
            "List of `ElementDefinitionConstraint` items (represented as `dict` in "
            "JSON)"
        ),
        description="Condition that must evaluate to true",
    )

    contentReference: fhirtypes.Uri = Field(
        None,
        alias="contentReference",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Reference to definition of content for the element",
    )

    defaultValueAddress: fhirtypes.AddressType = Field(
        None,
        alias="defaultValueAddress",
        title="Type `Address` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueAge: fhirtypes.AgeType = Field(
        None,
        alias="defaultValueAge",
        title="Type `Age` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueAnnotation: fhirtypes.AnnotationType = Field(
        None,
        alias="defaultValueAnnotation",
        title="Type `Annotation` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="defaultValueAttachment",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueBase64Binary: fhirtypes.Base64Binary = Field(
        None,
        alias="defaultValueBase64Binary",
        title="Type `Base64Binary` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueBoolean: bool = Field(
        None,
        alias="defaultValueBoolean",
        title="Type `bool`",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueCode: fhirtypes.Code = Field(
        None,
        alias="defaultValueCode",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="defaultValueCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueCoding: fhirtypes.CodingType = Field(
        None,
        alias="defaultValueCoding",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueContactPoint: fhirtypes.ContactPointType = Field(
        None,
        alias="defaultValueContactPoint",
        title="Type `ContactPoint` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueCount: fhirtypes.CountType = Field(
        None,
        alias="defaultValueCount",
        title="Type `Count` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueDate: fhirtypes.Date = Field(
        None,
        alias="defaultValueDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="defaultValueDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="defaultValueDecimal",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueDistance: fhirtypes.DistanceType = Field(
        None,
        alias="defaultValueDistance",
        title="Type `Distance` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueDuration: fhirtypes.DurationType = Field(
        None,
        alias="defaultValueDuration",
        title="Type `Duration` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueHumanName: fhirtypes.HumanNameType = Field(
        None,
        alias="defaultValueHumanName",
        title="Type `HumanName` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueId: fhirtypes.Id = Field(
        None,
        alias="defaultValueId",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="defaultValueIdentifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueInstant: fhirtypes.Instant = Field(
        None,
        alias="defaultValueInstant",
        title="Type `Instant` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueInteger: fhirtypes.Integer = Field(
        None,
        alias="defaultValueInteger",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueMarkdown: fhirtypes.Markdown = Field(
        None,
        alias="defaultValueMarkdown",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueMeta: fhirtypes.MetaType = Field(
        None,
        alias="defaultValueMeta",
        title="Type `Meta` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueMoney: fhirtypes.MoneyType = Field(
        None,
        alias="defaultValueMoney",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueOid: fhirtypes.Oid = Field(
        None,
        alias="defaultValueOid",
        title="Type `Oid` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValuePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="defaultValuePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValuePositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="defaultValuePositiveInt",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="defaultValueQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueRange: fhirtypes.RangeType = Field(
        None,
        alias="defaultValueRange",
        title="Type `Range` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueRatio: fhirtypes.RatioType = Field(
        None,
        alias="defaultValueRatio",
        title="Type `Ratio` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueReference: fhirtypes.ReferenceType = Field(
        None,
        alias="defaultValueReference",
        title="Type `Reference` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueSampledData: fhirtypes.SampledDataType = Field(
        None,
        alias="defaultValueSampledData",
        title="Type `SampledData` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueSignature: fhirtypes.SignatureType = Field(
        None,
        alias="defaultValueSignature",
        title="Type `Signature` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueString: fhirtypes.String = Field(
        None,
        alias="defaultValueString",
        title="Type `String` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueTime: fhirtypes.Time = Field(
        None,
        alias="defaultValueTime",
        title="Type `Time` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueTiming: fhirtypes.TimingType = Field(
        None,
        alias="defaultValueTiming",
        title="Type `Timing` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="defaultValueUnsignedInt",
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueUri: fhirtypes.Uri = Field(
        None,
        alias="defaultValueUri",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    definition: fhirtypes.Markdown = Field(
        None,
        alias="definition",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Full formal definition as narrative text",
    )

    example: ListType[fhirtypes.ElementDefinitionExampleType] = Field(
        None,
        alias="example",
        title=(
            "List of `ElementDefinitionExample` items (represented as `dict` in "
            "JSON)"
        ),
        description="Example value (as defined for type)",
    )

    fixedAddress: fhirtypes.AddressType = Field(
        None,
        alias="fixedAddress",
        title="Type `Address` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedAge: fhirtypes.AgeType = Field(
        None,
        alias="fixedAge",
        title="Type `Age` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedAnnotation: fhirtypes.AnnotationType = Field(
        None,
        alias="fixedAnnotation",
        title="Type `Annotation` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="fixedAttachment",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedBase64Binary: fhirtypes.Base64Binary = Field(
        None,
        alias="fixedBase64Binary",
        title="Type `Base64Binary` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedBoolean: bool = Field(
        None,
        alias="fixedBoolean",
        title="Type `bool`",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedCode: fhirtypes.Code = Field(
        None,
        alias="fixedCode",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="fixedCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedCoding: fhirtypes.CodingType = Field(
        None,
        alias="fixedCoding",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedContactPoint: fhirtypes.ContactPointType = Field(
        None,
        alias="fixedContactPoint",
        title="Type `ContactPoint` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedCount: fhirtypes.CountType = Field(
        None,
        alias="fixedCount",
        title="Type `Count` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedDate: fhirtypes.Date = Field(
        None,
        alias="fixedDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedDateTime: fhirtypes.DateTime = Field(
        None,
        alias="fixedDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedDecimal: fhirtypes.Decimal = Field(
        None,
        alias="fixedDecimal",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedDistance: fhirtypes.DistanceType = Field(
        None,
        alias="fixedDistance",
        title="Type `Distance` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedDuration: fhirtypes.DurationType = Field(
        None,
        alias="fixedDuration",
        title="Type `Duration` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedHumanName: fhirtypes.HumanNameType = Field(
        None,
        alias="fixedHumanName",
        title="Type `HumanName` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedId: fhirtypes.Id = Field(
        None,
        alias="fixedId",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="fixedIdentifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedInstant: fhirtypes.Instant = Field(
        None,
        alias="fixedInstant",
        title="Type `Instant` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedInteger: fhirtypes.Integer = Field(
        None,
        alias="fixedInteger",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedMarkdown: fhirtypes.Markdown = Field(
        None,
        alias="fixedMarkdown",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedMeta: fhirtypes.MetaType = Field(
        None,
        alias="fixedMeta",
        title="Type `Meta` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedMoney: fhirtypes.MoneyType = Field(
        None,
        alias="fixedMoney",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedOid: fhirtypes.Oid = Field(
        None,
        alias="fixedOid",
        title="Type `Oid` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="fixedPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedPositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="fixedPositiveInt",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="fixedQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedRange: fhirtypes.RangeType = Field(
        None,
        alias="fixedRange",
        title="Type `Range` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedRatio: fhirtypes.RatioType = Field(
        None,
        alias="fixedRatio",
        title="Type `Ratio` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedReference: fhirtypes.ReferenceType = Field(
        None,
        alias="fixedReference",
        title="Type `Reference` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedSampledData: fhirtypes.SampledDataType = Field(
        None,
        alias="fixedSampledData",
        title="Type `SampledData` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedSignature: fhirtypes.SignatureType = Field(
        None,
        alias="fixedSignature",
        title="Type `Signature` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedString: fhirtypes.String = Field(
        None,
        alias="fixedString",
        title="Type `String` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedTime: fhirtypes.Time = Field(
        None,
        alias="fixedTime",
        title="Type `Time` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedTiming: fhirtypes.TimingType = Field(
        None,
        alias="fixedTiming",
        title="Type `Timing` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="fixedUnsignedInt",
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    fixedUri: fhirtypes.Uri = Field(
        None,
        alias="fixedUri",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    isModifier: bool = Field(
        None,
        alias="isModifier",
        title="Type `bool`",
        description="If this modifies the meaning of other elements",
    )

    isSummary: bool = Field(
        None,
        alias="isSummary",
        title="Type `bool`",
        description="Include when _summary = true?",
    )

    label: fhirtypes.String = Field(
        None,
        alias="label",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for element to display with or prompt for element",
    )

    mapping: ListType[fhirtypes.ElementDefinitionMappingType] = Field(
        None,
        alias="mapping",
        title=(
            "List of `ElementDefinitionMapping` items (represented as `dict` in "
            "JSON)"
        ),
        description="Map element to another set of definitions",
    )

    max: fhirtypes.String = Field(
        None,
        alias="max",
        title="Type `String` (represented as `dict` in JSON)",
        description="Maximum Cardinality (a number or *)",
    )

    maxLength: fhirtypes.Integer = Field(
        None,
        alias="maxLength",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Max length for strings",
    )

    maxValueDate: fhirtypes.Date = Field(
        None,
        alias="maxValueDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="Maximum Allowed Value (for some types)",
        one_of_many="maxValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    maxValueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="maxValueDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Maximum Allowed Value (for some types)",
        one_of_many="maxValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    maxValueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="maxValueDecimal",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Maximum Allowed Value (for some types)",
        one_of_many="maxValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    maxValueInstant: fhirtypes.Instant = Field(
        None,
        alias="maxValueInstant",
        title="Type `Instant` (represented as `dict` in JSON)",
        description="Maximum Allowed Value (for some types)",
        one_of_many="maxValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    maxValueInteger: fhirtypes.Integer = Field(
        None,
        alias="maxValueInteger",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Maximum Allowed Value (for some types)",
        one_of_many="maxValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    maxValuePositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="maxValuePositiveInt",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Maximum Allowed Value (for some types)",
        one_of_many="maxValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    maxValueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="maxValueQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Maximum Allowed Value (for some types)",
        one_of_many="maxValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    maxValueTime: fhirtypes.Time = Field(
        None,
        alias="maxValueTime",
        title="Type `Time` (represented as `dict` in JSON)",
        description="Maximum Allowed Value (for some types)",
        one_of_many="maxValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    maxValueUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="maxValueUnsignedInt",
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="Maximum Allowed Value (for some types)",
        one_of_many="maxValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    meaningWhenMissing: fhirtypes.Markdown = Field(
        None,
        alias="meaningWhenMissing",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Implicit meaning when this element is missing",
    )

    min: fhirtypes.UnsignedInt = Field(
        None,
        alias="min",
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="Minimum Cardinality",
    )

    minValueDate: fhirtypes.Date = Field(
        None,
        alias="minValueDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="Minimum Allowed Value (for some types)",
        one_of_many="minValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    minValueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="minValueDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Minimum Allowed Value (for some types)",
        one_of_many="minValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    minValueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="minValueDecimal",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Minimum Allowed Value (for some types)",
        one_of_many="minValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    minValueInstant: fhirtypes.Instant = Field(
        None,
        alias="minValueInstant",
        title="Type `Instant` (represented as `dict` in JSON)",
        description="Minimum Allowed Value (for some types)",
        one_of_many="minValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    minValueInteger: fhirtypes.Integer = Field(
        None,
        alias="minValueInteger",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Minimum Allowed Value (for some types)",
        one_of_many="minValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    minValuePositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="minValuePositiveInt",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Minimum Allowed Value (for some types)",
        one_of_many="minValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    minValueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="minValueQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Minimum Allowed Value (for some types)",
        one_of_many="minValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    minValueTime: fhirtypes.Time = Field(
        None,
        alias="minValueTime",
        title="Type `Time` (represented as `dict` in JSON)",
        description="Minimum Allowed Value (for some types)",
        one_of_many="minValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    minValueUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="minValueUnsignedInt",
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="Minimum Allowed Value (for some types)",
        one_of_many="minValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    mustSupport: bool = Field(
        None,
        alias="mustSupport",
        title="Type `bool`",
        description="If the element must supported",
    )

    orderMeaning: fhirtypes.String = Field(
        None,
        alias="orderMeaning",
        title="Type `String` (represented as `dict` in JSON)",
        description="What the order of the elements means",
    )

    path: fhirtypes.String = Field(
        ...,
        alias="path",
        title="Type `String` (represented as `dict` in JSON)",
        description="Path of the element in the hierarchy of elements",
    )

    patternAddress: fhirtypes.AddressType = Field(
        None,
        alias="patternAddress",
        title="Type `Address` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternAge: fhirtypes.AgeType = Field(
        None,
        alias="patternAge",
        title="Type `Age` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternAnnotation: fhirtypes.AnnotationType = Field(
        None,
        alias="patternAnnotation",
        title="Type `Annotation` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="patternAttachment",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternBase64Binary: fhirtypes.Base64Binary = Field(
        None,
        alias="patternBase64Binary",
        title="Type `Base64Binary` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternBoolean: bool = Field(
        None,
        alias="patternBoolean",
        title="Type `bool`",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternCode: fhirtypes.Code = Field(
        None,
        alias="patternCode",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="patternCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternCoding: fhirtypes.CodingType = Field(
        None,
        alias="patternCoding",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternContactPoint: fhirtypes.ContactPointType = Field(
        None,
        alias="patternContactPoint",
        title="Type `ContactPoint` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternCount: fhirtypes.CountType = Field(
        None,
        alias="patternCount",
        title="Type `Count` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternDate: fhirtypes.Date = Field(
        None,
        alias="patternDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternDateTime: fhirtypes.DateTime = Field(
        None,
        alias="patternDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternDecimal: fhirtypes.Decimal = Field(
        None,
        alias="patternDecimal",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternDistance: fhirtypes.DistanceType = Field(
        None,
        alias="patternDistance",
        title="Type `Distance` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternDuration: fhirtypes.DurationType = Field(
        None,
        alias="patternDuration",
        title="Type `Duration` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternHumanName: fhirtypes.HumanNameType = Field(
        None,
        alias="patternHumanName",
        title="Type `HumanName` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternId: fhirtypes.Id = Field(
        None,
        alias="patternId",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="patternIdentifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternInstant: fhirtypes.Instant = Field(
        None,
        alias="patternInstant",
        title="Type `Instant` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternInteger: fhirtypes.Integer = Field(
        None,
        alias="patternInteger",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternMarkdown: fhirtypes.Markdown = Field(
        None,
        alias="patternMarkdown",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternMeta: fhirtypes.MetaType = Field(
        None,
        alias="patternMeta",
        title="Type `Meta` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternMoney: fhirtypes.MoneyType = Field(
        None,
        alias="patternMoney",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternOid: fhirtypes.Oid = Field(
        None,
        alias="patternOid",
        title="Type `Oid` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="patternPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternPositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="patternPositiveInt",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="patternQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternRange: fhirtypes.RangeType = Field(
        None,
        alias="patternRange",
        title="Type `Range` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternRatio: fhirtypes.RatioType = Field(
        None,
        alias="patternRatio",
        title="Type `Ratio` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternReference: fhirtypes.ReferenceType = Field(
        None,
        alias="patternReference",
        title="Type `Reference` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternSampledData: fhirtypes.SampledDataType = Field(
        None,
        alias="patternSampledData",
        title="Type `SampledData` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternSignature: fhirtypes.SignatureType = Field(
        None,
        alias="patternSignature",
        title="Type `Signature` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternString: fhirtypes.String = Field(
        None,
        alias="patternString",
        title="Type `String` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternTime: fhirtypes.Time = Field(
        None,
        alias="patternTime",
        title="Type `Time` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternTiming: fhirtypes.TimingType = Field(
        None,
        alias="patternTiming",
        title="Type `Timing` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="patternUnsignedInt",
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patternUri: fhirtypes.Uri = Field(
        None,
        alias="patternUri",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    representation: ListType[fhirtypes.Code] = Field(
        None,
        alias="representation",
        title="List of `Code` items (represented as `dict` in JSON)",
        description="xmlAttr | xmlText | typeAttr | cdaText | xhtml",
    )

    requirements: fhirtypes.Markdown = Field(
        None,
        alias="requirements",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Why this resource has been created",
    )

    short: fhirtypes.String = Field(
        None,
        alias="short",
        title="Type `String` (represented as `dict` in JSON)",
        description="Concise definition for space-constrained presentation",
    )

    sliceName: fhirtypes.String = Field(
        None,
        alias="sliceName",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this particular element (in a set of slices)",
    )

    slicing: fhirtypes.ElementDefinitionSlicingType = Field(
        None,
        alias="slicing",
        title="Type `ElementDefinitionSlicing` (represented as `dict` in JSON)",
        description="This element is sliced - slices follow",
    )

    type: ListType[fhirtypes.ElementDefinitionTypeType] = Field(
        None,
        alias="type",
        title="List of `ElementDefinitionType` items (represented as `dict` in JSON)",
        description="Data type and Profile for this element",
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
            "defaultValue": [
                "defaultValueAddress",
                "defaultValueAge",
                "defaultValueAnnotation",
                "defaultValueAttachment",
                "defaultValueBase64Binary",
                "defaultValueBoolean",
                "defaultValueCode",
                "defaultValueCodeableConcept",
                "defaultValueCoding",
                "defaultValueContactPoint",
                "defaultValueCount",
                "defaultValueDate",
                "defaultValueDateTime",
                "defaultValueDecimal",
                "defaultValueDistance",
                "defaultValueDuration",
                "defaultValueHumanName",
                "defaultValueId",
                "defaultValueIdentifier",
                "defaultValueInstant",
                "defaultValueInteger",
                "defaultValueMarkdown",
                "defaultValueMeta",
                "defaultValueMoney",
                "defaultValueOid",
                "defaultValuePeriod",
                "defaultValuePositiveInt",
                "defaultValueQuantity",
                "defaultValueRange",
                "defaultValueRatio",
                "defaultValueReference",
                "defaultValueSampledData",
                "defaultValueSignature",
                "defaultValueString",
                "defaultValueTime",
                "defaultValueTiming",
                "defaultValueUnsignedInt",
                "defaultValueUri",
            ],
            "fixed": [
                "fixedAddress",
                "fixedAge",
                "fixedAnnotation",
                "fixedAttachment",
                "fixedBase64Binary",
                "fixedBoolean",
                "fixedCode",
                "fixedCodeableConcept",
                "fixedCoding",
                "fixedContactPoint",
                "fixedCount",
                "fixedDate",
                "fixedDateTime",
                "fixedDecimal",
                "fixedDistance",
                "fixedDuration",
                "fixedHumanName",
                "fixedId",
                "fixedIdentifier",
                "fixedInstant",
                "fixedInteger",
                "fixedMarkdown",
                "fixedMeta",
                "fixedMoney",
                "fixedOid",
                "fixedPeriod",
                "fixedPositiveInt",
                "fixedQuantity",
                "fixedRange",
                "fixedRatio",
                "fixedReference",
                "fixedSampledData",
                "fixedSignature",
                "fixedString",
                "fixedTime",
                "fixedTiming",
                "fixedUnsignedInt",
                "fixedUri",
            ],
            "maxValue": [
                "maxValueDate",
                "maxValueDateTime",
                "maxValueDecimal",
                "maxValueInstant",
                "maxValueInteger",
                "maxValuePositiveInt",
                "maxValueQuantity",
                "maxValueTime",
                "maxValueUnsignedInt",
            ],
            "minValue": [
                "minValueDate",
                "minValueDateTime",
                "minValueDecimal",
                "minValueInstant",
                "minValueInteger",
                "minValuePositiveInt",
                "minValueQuantity",
                "minValueTime",
                "minValueUnsignedInt",
            ],
            "pattern": [
                "patternAddress",
                "patternAge",
                "patternAnnotation",
                "patternAttachment",
                "patternBase64Binary",
                "patternBoolean",
                "patternCode",
                "patternCodeableConcept",
                "patternCoding",
                "patternContactPoint",
                "patternCount",
                "patternDate",
                "patternDateTime",
                "patternDecimal",
                "patternDistance",
                "patternDuration",
                "patternHumanName",
                "patternId",
                "patternIdentifier",
                "patternInstant",
                "patternInteger",
                "patternMarkdown",
                "patternMeta",
                "patternMoney",
                "patternOid",
                "patternPeriod",
                "patternPositiveInt",
                "patternQuantity",
                "patternRange",
                "patternRatio",
                "patternReference",
                "patternSampledData",
                "patternSignature",
                "patternString",
                "patternTime",
                "patternTiming",
                "patternUnsignedInt",
                "patternUri",
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


class ElementDefinitionBase(element.Element):
    """ Base definition information for tools.
    Information about the base definition of the element, provided to make it
    unnecessary for tools to trace the deviation of the element through the
    derived and related profiles. This information is provided when the element
    definition is not the original definition of an element - i.g. either in a
    constraint on another type, or for elements from a super type in a snap
    shot.
    """

    resource_type = Field("ElementDefinitionBase", const=True)

    max: fhirtypes.String = Field(
        ...,
        alias="max",
        title="Type `String` (represented as `dict` in JSON)",
        description="Max cardinality of the base element",
    )

    min: fhirtypes.UnsignedInt = Field(
        ...,
        alias="min",
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="Min cardinality of the base element",
    )

    path: fhirtypes.String = Field(
        ...,
        alias="path",
        title="Type `String` (represented as `dict` in JSON)",
        description="Path that identifies the base element",
    )


class ElementDefinitionBinding(element.Element):
    """ ValueSet details if this is coded.
    Binds to a value set if this element is coded (code, Coding,
    CodeableConcept, Quantity), or the data types (string, uri).
    """

    resource_type = Field("ElementDefinitionBinding", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Human explanation of the value set",
    )

    strength: fhirtypes.Code = Field(
        ...,
        alias="strength",
        title="Type `Code` (represented as `dict` in JSON)",
        description="required | extensible | preferred | example",
    )

    valueSetReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueSetReference",
        title=(
            "Type `Reference` referencing `ValueSet` (represented as `dict` in " "JSON)"
        ),
        description="Source of value set",
        one_of_many="valueSet",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueSetUri: fhirtypes.Uri = Field(
        None,
        alias="valueSetUri",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Source of value set",
        one_of_many="valueSet",  # Choice of Data Types. i.e value[x]
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
        one_of_many_fields = {"valueSet": ["valueSetReference", "valueSetUri"]}
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


class ElementDefinitionConstraint(element.Element):
    """ Condition that must evaluate to true.
    Formal constraints such as co-occurrence and other constraints that can be
    computationally evaluated within the context of the instance.
    """

    resource_type = Field("ElementDefinitionConstraint", const=True)

    expression: fhirtypes.String = Field(
        ...,
        alias="expression",
        title="Type `String` (represented as `dict` in JSON)",
        description="FHIRPath expression of constraint",
    )

    human: fhirtypes.String = Field(
        ...,
        alias="human",
        title="Type `String` (represented as `dict` in JSON)",
        description="Human description of constraint",
    )

    key: fhirtypes.Id = Field(
        ...,
        alias="key",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Target of \u0027condition\u0027 reference above",
    )

    requirements: fhirtypes.String = Field(
        None,
        alias="requirements",
        title="Type `String` (represented as `dict` in JSON)",
        description="Why this constraint is necessary or appropriate",
    )

    severity: fhirtypes.Code = Field(
        ...,
        alias="severity",
        title="Type `Code` (represented as `dict` in JSON)",
        description="error | warning",
    )

    source: fhirtypes.Uri = Field(
        None,
        alias="source",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Reference to original source of constraint",
    )

    xpath: fhirtypes.String = Field(
        None,
        alias="xpath",
        title="Type `String` (represented as `dict` in JSON)",
        description="XPath expression of constraint",
    )


class ElementDefinitionExample(element.Element):
    """ Example value (as defined for type).
    A sample value for this element demonstrating the type of information that
    would typically be found in the element.
    """

    resource_type = Field("ElementDefinitionExample", const=True)

    label: fhirtypes.String = Field(
        ...,
        alias="label",
        title="Type `String` (represented as `dict` in JSON)",
        description="Describes the purpose of this example",
    )

    valueAddress: fhirtypes.AddressType = Field(
        None,
        alias="valueAddress",
        title="Type `Address` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueAge: fhirtypes.AgeType = Field(
        None,
        alias="valueAge",
        title="Type `Age` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueAnnotation: fhirtypes.AnnotationType = Field(
        None,
        alias="valueAnnotation",
        title="Type `Annotation` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueBase64Binary: fhirtypes.Base64Binary = Field(
        None,
        alias="valueBase64Binary",
        title="Type `Base64Binary` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="Type `bool`",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueCode: fhirtypes.Code = Field(
        None,
        alias="valueCode",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="valueCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueCoding: fhirtypes.CodingType = Field(
        None,
        alias="valueCoding",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueContactPoint: fhirtypes.ContactPointType = Field(
        None,
        alias="valueContactPoint",
        title="Type `ContactPoint` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueCount: fhirtypes.CountType = Field(
        None,
        alias="valueCount",
        title="Type `Count` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueDate: fhirtypes.Date = Field(
        None,
        alias="valueDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="valueDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="valueDecimal",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueDistance: fhirtypes.DistanceType = Field(
        None,
        alias="valueDistance",
        title="Type `Distance` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueDuration: fhirtypes.DurationType = Field(
        None,
        alias="valueDuration",
        title="Type `Duration` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueHumanName: fhirtypes.HumanNameType = Field(
        None,
        alias="valueHumanName",
        title="Type `HumanName` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueId: fhirtypes.Id = Field(
        None,
        alias="valueId",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="valueIdentifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueInstant: fhirtypes.Instant = Field(
        None,
        alias="valueInstant",
        title="Type `Instant` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueMarkdown: fhirtypes.Markdown = Field(
        None,
        alias="valueMarkdown",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueMeta: fhirtypes.MetaType = Field(
        None,
        alias="valueMeta",
        title="Type `Meta` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueMoney: fhirtypes.MoneyType = Field(
        None,
        alias="valueMoney",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueOid: fhirtypes.Oid = Field(
        None,
        alias="valueOid",
        title="Type `Oid` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valuePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="valuePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valuePositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="valuePositiveInt",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueRange: fhirtypes.RangeType = Field(
        None,
        alias="valueRange",
        title="Type `Range` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueRatio: fhirtypes.RatioType = Field(
        None,
        alias="valueRatio",
        title="Type `Ratio` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueReference",
        title="Type `Reference` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueSampledData: fhirtypes.SampledDataType = Field(
        None,
        alias="valueSampledData",
        title="Type `SampledData` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueSignature: fhirtypes.SignatureType = Field(
        None,
        alias="valueSignature",
        title="Type `Signature` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Type `String` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueTime: fhirtypes.Time = Field(
        None,
        alias="valueTime",
        title="Type `Time` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueTiming: fhirtypes.TimingType = Field(
        None,
        alias="valueTiming",
        title="Type `Timing` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="valueUnsignedInt",
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueUri: fhirtypes.Uri = Field(
        None,
        alias="valueUri",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
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
                "valueAddress",
                "valueAge",
                "valueAnnotation",
                "valueAttachment",
                "valueBase64Binary",
                "valueBoolean",
                "valueCode",
                "valueCodeableConcept",
                "valueCoding",
                "valueContactPoint",
                "valueCount",
                "valueDate",
                "valueDateTime",
                "valueDecimal",
                "valueDistance",
                "valueDuration",
                "valueHumanName",
                "valueId",
                "valueIdentifier",
                "valueInstant",
                "valueInteger",
                "valueMarkdown",
                "valueMeta",
                "valueMoney",
                "valueOid",
                "valuePeriod",
                "valuePositiveInt",
                "valueQuantity",
                "valueRange",
                "valueRatio",
                "valueReference",
                "valueSampledData",
                "valueSignature",
                "valueString",
                "valueTime",
                "valueTiming",
                "valueUnsignedInt",
                "valueUri",
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


class ElementDefinitionMapping(element.Element):
    """ Map element to another set of definitions.
    Identifies a concept from an external specification that roughly
    corresponds to this element.
    """

    resource_type = Field("ElementDefinitionMapping", const=True)

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Type `String` (represented as `dict` in JSON)",
        description="Comments about the mapping or its use",
    )

    identity: fhirtypes.Id = Field(
        ...,
        alias="identity",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Reference to mapping declaration",
    )

    language: fhirtypes.Code = Field(
        None,
        alias="language",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Computable language of mapping",
    )

    map: fhirtypes.String = Field(
        ...,
        alias="map",
        title="Type `String` (represented as `dict` in JSON)",
        description="Details of the mapping",
    )


class ElementDefinitionSlicing(element.Element):
    """ This element is sliced - slices follow.
    Indicates that the element is sliced into a set of alternative definitions
    (i.e. in a structure definition, there are multiple different constraints
    on a single element in the base resource). Slicing can be used in any
    resource that has cardinality ..* on the base resource, or any resource
    with a choice of types. The set of slices is any elements that come after
    this in the element sequence that have the same path, until a shorter path
    occurs (the shorter path terminates the set).
    """

    resource_type = Field("ElementDefinitionSlicing", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Text description of how slicing works (or not)",
    )

    discriminator: ListType[
        fhirtypes.ElementDefinitionSlicingDiscriminatorType
    ] = Field(
        None,
        alias="discriminator",
        title=(
            "List of `ElementDefinitionSlicingDiscriminator` items (represented as "
            "`dict` in JSON)"
        ),
        description="Element values that are used to distinguish the slices",
    )

    ordered: bool = Field(
        None,
        alias="ordered",
        title="Type `bool`",
        description="If elements must be in same order as slices",
    )

    rules: fhirtypes.Code = Field(
        ...,
        alias="rules",
        title="Type `Code` (represented as `dict` in JSON)",
        description="closed | open | openAtEnd",
    )


class ElementDefinitionSlicingDiscriminator(element.Element):
    """ Element values that are used to distinguish the slices.
    Designates which child elements are used to discriminate between the slices
    when processing an instance. If one or more discriminators are provided,
    the value of the child elements in the instance data SHALL completely
    distinguish which slice the element in the resource matches based on the
    allowed values for those elements in each of the slices.
    """

    resource_type = Field("ElementDefinitionSlicingDiscriminator", const=True)

    path: fhirtypes.String = Field(
        ...,
        alias="path",
        title="Type `String` (represented as `dict` in JSON)",
        description="Path to element value",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="value | exists | pattern | type | profile",
    )


class ElementDefinitionType(element.Element):
    """ Data type and Profile for this element.
    The data type or resource that the value of this element is permitted to
    be.
    """

    resource_type = Field("ElementDefinitionType", const=True)

    aggregation: ListType[fhirtypes.Code] = Field(
        None,
        alias="aggregation",
        title="List of `Code` items (represented as `dict` in JSON)",
        description="contained | referenced | bundled - how aggregated",
    )

    code: fhirtypes.Uri = Field(
        ...,
        alias="code",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Data type or Resource (reference to definition)",
    )

    profile: fhirtypes.Uri = Field(
        None,
        alias="profile",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Profile (StructureDefinition) to apply (or IG)",
    )

    targetProfile: fhirtypes.Uri = Field(
        None,
        alias="targetProfile",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Profile (StructureDefinition) to apply to reference target (or IG)",
    )

    versioning: fhirtypes.Code = Field(
        None,
        alias="versioning",
        title="Type `Code` (represented as `dict` in JSON)",
        description="either | independent | specific",
    )
