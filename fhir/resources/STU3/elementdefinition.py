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
from typing import Union

from pydantic import Field, root_validator

from . import element, fhirtypes


class ElementDefinition(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Definition of an element in a resource or extension.
    Captures constraints on each element within the resource, profile, or
    extension.
    """

    resource_type = Field("ElementDefinition", const=True)

    alias: ListType[fhirtypes.String] = Field(
        None, alias="alias", title="List of `String` items", description="Other names"
    )
    alias__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_alias", title="Extension field for ``alias``."
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
        title="Type `Markdown`",
        description="Comments about the use of this element",
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    condition: ListType[fhirtypes.Id] = Field(
        None,
        alias="condition",
        title="List of `Id` items",
        description="Reference to invariant about presence",
    )
    condition__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_condition", title="Extension field for ``condition``."
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
        title="Type `Uri`",
        description="Reference to definition of content for the element",
    )
    contentReference__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_contentReference",
        title="Extension field for ``contentReference``.",
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
        title="Type `Base64Binary`",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    defaultValueBase64Binary__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValueBase64Binary",
        title="Extension field for ``defaultValueBase64Binary``.",
    )

    defaultValueBoolean: bool = Field(
        None,
        alias="defaultValueBoolean",
        title="Type `bool`",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    defaultValueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValueBoolean",
        title="Extension field for ``defaultValueBoolean``.",
    )

    defaultValueCode: fhirtypes.Code = Field(
        None,
        alias="defaultValueCode",
        title="Type `Code`",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    defaultValueCode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValueCode",
        title="Extension field for ``defaultValueCode``.",
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
        title="Type `Date`",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    defaultValueDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValueDate",
        title="Extension field for ``defaultValueDate``.",
    )

    defaultValueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="defaultValueDateTime",
        title="Type `DateTime`",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    defaultValueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValueDateTime",
        title="Extension field for ``defaultValueDateTime``.",
    )

    defaultValueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="defaultValueDecimal",
        title="Type `Decimal`",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    defaultValueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValueDecimal",
        title="Extension field for ``defaultValueDecimal``.",
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
        title="Type `Id`",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    defaultValueId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_defaultValueId", title="Extension field for ``defaultValueId``."
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
        title="Type `Instant`",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    defaultValueInstant__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValueInstant",
        title="Extension field for ``defaultValueInstant``.",
    )

    defaultValueInteger: fhirtypes.Integer = Field(
        None,
        alias="defaultValueInteger",
        title="Type `Integer`",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    defaultValueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValueInteger",
        title="Extension field for ``defaultValueInteger``.",
    )

    defaultValueMarkdown: fhirtypes.Markdown = Field(
        None,
        alias="defaultValueMarkdown",
        title="Type `Markdown`",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    defaultValueMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValueMarkdown",
        title="Extension field for ``defaultValueMarkdown``.",
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
        title="Type `Oid`",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    defaultValueOid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_defaultValueOid", title="Extension field for ``defaultValueOid``."
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
        title="Type `PositiveInt`",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    defaultValuePositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValuePositiveInt",
        title="Extension field for ``defaultValuePositiveInt``.",
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
        title="Type `String`",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    defaultValueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValueString",
        title="Extension field for ``defaultValueString``.",
    )

    defaultValueTime: fhirtypes.Time = Field(
        None,
        alias="defaultValueTime",
        title="Type `Time`",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    defaultValueTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValueTime",
        title="Extension field for ``defaultValueTime``.",
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
        title="Type `UnsignedInt`",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    defaultValueUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValueUnsignedInt",
        title="Extension field for ``defaultValueUnsignedInt``.",
    )

    defaultValueUri: fhirtypes.Uri = Field(
        None,
        alias="defaultValueUri",
        title="Type `Uri`",
        description="Specified value if missing from instance",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    defaultValueUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_defaultValueUri", title="Extension field for ``defaultValueUri``."
    )

    definition: fhirtypes.Markdown = Field(
        None,
        alias="definition",
        title="Type `Markdown`",
        description="Full formal definition as narrative text",
    )
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_definition", title="Extension field for ``definition``."
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
        title="Type `Base64Binary`",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    fixedBase64Binary__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_fixedBase64Binary",
        title="Extension field for ``fixedBase64Binary``.",
    )

    fixedBoolean: bool = Field(
        None,
        alias="fixedBoolean",
        title="Type `bool`",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    fixedBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fixedBoolean", title="Extension field for ``fixedBoolean``."
    )

    fixedCode: fhirtypes.Code = Field(
        None,
        alias="fixedCode",
        title="Type `Code`",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    fixedCode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fixedCode", title="Extension field for ``fixedCode``."
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
        title="Type `Date`",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    fixedDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fixedDate", title="Extension field for ``fixedDate``."
    )

    fixedDateTime: fhirtypes.DateTime = Field(
        None,
        alias="fixedDateTime",
        title="Type `DateTime`",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    fixedDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fixedDateTime", title="Extension field for ``fixedDateTime``."
    )

    fixedDecimal: fhirtypes.Decimal = Field(
        None,
        alias="fixedDecimal",
        title="Type `Decimal`",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    fixedDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fixedDecimal", title="Extension field for ``fixedDecimal``."
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
        title="Type `Id`",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    fixedId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fixedId", title="Extension field for ``fixedId``."
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
        title="Type `Instant`",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    fixedInstant__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fixedInstant", title="Extension field for ``fixedInstant``."
    )

    fixedInteger: fhirtypes.Integer = Field(
        None,
        alias="fixedInteger",
        title="Type `Integer`",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    fixedInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fixedInteger", title="Extension field for ``fixedInteger``."
    )

    fixedMarkdown: fhirtypes.Markdown = Field(
        None,
        alias="fixedMarkdown",
        title="Type `Markdown`",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    fixedMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fixedMarkdown", title="Extension field for ``fixedMarkdown``."
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
        title="Type `Oid`",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    fixedOid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fixedOid", title="Extension field for ``fixedOid``."
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
        title="Type `PositiveInt`",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    fixedPositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_fixedPositiveInt",
        title="Extension field for ``fixedPositiveInt``.",
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
        title="Type `String`",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    fixedString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fixedString", title="Extension field for ``fixedString``."
    )

    fixedTime: fhirtypes.Time = Field(
        None,
        alias="fixedTime",
        title="Type `Time`",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    fixedTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fixedTime", title="Extension field for ``fixedTime``."
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
        title="Type `UnsignedInt`",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    fixedUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_fixedUnsignedInt",
        title="Extension field for ``fixedUnsignedInt``.",
    )

    fixedUri: fhirtypes.Uri = Field(
        None,
        alias="fixedUri",
        title="Type `Uri`",
        description="Value must be exactly this",
        one_of_many="fixed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    fixedUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fixedUri", title="Extension field for ``fixedUri``."
    )

    isModifier: bool = Field(
        None,
        alias="isModifier",
        title="Type `bool`",
        description="If this modifies the meaning of other elements",
    )
    isModifier__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_isModifier", title="Extension field for ``isModifier``."
    )

    isSummary: bool = Field(
        None,
        alias="isSummary",
        title="Type `bool`",
        description="Include when _summary = true?",
    )
    isSummary__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_isSummary", title="Extension field for ``isSummary``."
    )

    label: fhirtypes.String = Field(
        None,
        alias="label",
        title="Type `String`",
        description="Name for element to display with or prompt for element",
    )
    label__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_label", title="Extension field for ``label``."
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
        title="Type `String`",
        description="Maximum Cardinality (a number or *)",
    )
    max__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_max", title="Extension field for ``max``."
    )

    maxLength: fhirtypes.Integer = Field(
        None,
        alias="maxLength",
        title="Type `Integer`",
        description="Max length for strings",
    )
    maxLength__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_maxLength", title="Extension field for ``maxLength``."
    )

    maxValueDate: fhirtypes.Date = Field(
        None,
        alias="maxValueDate",
        title="Type `Date`",
        description="Maximum Allowed Value (for some types)",
        one_of_many="maxValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    maxValueDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_maxValueDate", title="Extension field for ``maxValueDate``."
    )

    maxValueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="maxValueDateTime",
        title="Type `DateTime`",
        description="Maximum Allowed Value (for some types)",
        one_of_many="maxValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    maxValueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_maxValueDateTime",
        title="Extension field for ``maxValueDateTime``.",
    )

    maxValueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="maxValueDecimal",
        title="Type `Decimal`",
        description="Maximum Allowed Value (for some types)",
        one_of_many="maxValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    maxValueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_maxValueDecimal", title="Extension field for ``maxValueDecimal``."
    )

    maxValueInstant: fhirtypes.Instant = Field(
        None,
        alias="maxValueInstant",
        title="Type `Instant`",
        description="Maximum Allowed Value (for some types)",
        one_of_many="maxValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    maxValueInstant__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_maxValueInstant", title="Extension field for ``maxValueInstant``."
    )

    maxValueInteger: fhirtypes.Integer = Field(
        None,
        alias="maxValueInteger",
        title="Type `Integer`",
        description="Maximum Allowed Value (for some types)",
        one_of_many="maxValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    maxValueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_maxValueInteger", title="Extension field for ``maxValueInteger``."
    )

    maxValuePositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="maxValuePositiveInt",
        title="Type `PositiveInt`",
        description="Maximum Allowed Value (for some types)",
        one_of_many="maxValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    maxValuePositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_maxValuePositiveInt",
        title="Extension field for ``maxValuePositiveInt``.",
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
        title="Type `Time`",
        description="Maximum Allowed Value (for some types)",
        one_of_many="maxValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    maxValueTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_maxValueTime", title="Extension field for ``maxValueTime``."
    )

    maxValueUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="maxValueUnsignedInt",
        title="Type `UnsignedInt`",
        description="Maximum Allowed Value (for some types)",
        one_of_many="maxValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    maxValueUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_maxValueUnsignedInt",
        title="Extension field for ``maxValueUnsignedInt``.",
    )

    meaningWhenMissing: fhirtypes.Markdown = Field(
        None,
        alias="meaningWhenMissing",
        title="Type `Markdown`",
        description="Implicit meaning when this element is missing",
    )
    meaningWhenMissing__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_meaningWhenMissing",
        title="Extension field for ``meaningWhenMissing``.",
    )

    min: fhirtypes.UnsignedInt = Field(
        None, alias="min", title="Type `UnsignedInt`", description="Minimum Cardinality"
    )
    min__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_min", title="Extension field for ``min``."
    )

    minValueDate: fhirtypes.Date = Field(
        None,
        alias="minValueDate",
        title="Type `Date`",
        description="Minimum Allowed Value (for some types)",
        one_of_many="minValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    minValueDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_minValueDate", title="Extension field for ``minValueDate``."
    )

    minValueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="minValueDateTime",
        title="Type `DateTime`",
        description="Minimum Allowed Value (for some types)",
        one_of_many="minValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    minValueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_minValueDateTime",
        title="Extension field for ``minValueDateTime``.",
    )

    minValueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="minValueDecimal",
        title="Type `Decimal`",
        description="Minimum Allowed Value (for some types)",
        one_of_many="minValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    minValueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_minValueDecimal", title="Extension field for ``minValueDecimal``."
    )

    minValueInstant: fhirtypes.Instant = Field(
        None,
        alias="minValueInstant",
        title="Type `Instant`",
        description="Minimum Allowed Value (for some types)",
        one_of_many="minValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    minValueInstant__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_minValueInstant", title="Extension field for ``minValueInstant``."
    )

    minValueInteger: fhirtypes.Integer = Field(
        None,
        alias="minValueInteger",
        title="Type `Integer`",
        description="Minimum Allowed Value (for some types)",
        one_of_many="minValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    minValueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_minValueInteger", title="Extension field for ``minValueInteger``."
    )

    minValuePositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="minValuePositiveInt",
        title="Type `PositiveInt`",
        description="Minimum Allowed Value (for some types)",
        one_of_many="minValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    minValuePositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_minValuePositiveInt",
        title="Extension field for ``minValuePositiveInt``.",
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
        title="Type `Time`",
        description="Minimum Allowed Value (for some types)",
        one_of_many="minValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    minValueTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_minValueTime", title="Extension field for ``minValueTime``."
    )

    minValueUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="minValueUnsignedInt",
        title="Type `UnsignedInt`",
        description="Minimum Allowed Value (for some types)",
        one_of_many="minValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    minValueUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_minValueUnsignedInt",
        title="Extension field for ``minValueUnsignedInt``.",
    )

    mustSupport: bool = Field(
        None,
        alias="mustSupport",
        title="Type `bool`",
        description="If the element must supported",
    )
    mustSupport__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_mustSupport", title="Extension field for ``mustSupport``."
    )

    orderMeaning: fhirtypes.String = Field(
        None,
        alias="orderMeaning",
        title="Type `String`",
        description="What the order of the elements means",
    )
    orderMeaning__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_orderMeaning", title="Extension field for ``orderMeaning``."
    )

    path: fhirtypes.String = Field(
        ...,
        alias="path",
        title="Type `String`",
        description="Path of the element in the hierarchy of elements",
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_path", title="Extension field for ``path``."
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
        title="Type `Base64Binary`",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    patternBase64Binary__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_patternBase64Binary",
        title="Extension field for ``patternBase64Binary``.",
    )

    patternBoolean: bool = Field(
        None,
        alias="patternBoolean",
        title="Type `bool`",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    patternBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_patternBoolean", title="Extension field for ``patternBoolean``."
    )

    patternCode: fhirtypes.Code = Field(
        None,
        alias="patternCode",
        title="Type `Code`",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    patternCode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_patternCode", title="Extension field for ``patternCode``."
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
        title="Type `Date`",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    patternDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_patternDate", title="Extension field for ``patternDate``."
    )

    patternDateTime: fhirtypes.DateTime = Field(
        None,
        alias="patternDateTime",
        title="Type `DateTime`",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    patternDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_patternDateTime", title="Extension field for ``patternDateTime``."
    )

    patternDecimal: fhirtypes.Decimal = Field(
        None,
        alias="patternDecimal",
        title="Type `Decimal`",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    patternDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_patternDecimal", title="Extension field for ``patternDecimal``."
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
        title="Type `Id`",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    patternId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_patternId", title="Extension field for ``patternId``."
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
        title="Type `Instant`",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    patternInstant__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_patternInstant", title="Extension field for ``patternInstant``."
    )

    patternInteger: fhirtypes.Integer = Field(
        None,
        alias="patternInteger",
        title="Type `Integer`",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    patternInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_patternInteger", title="Extension field for ``patternInteger``."
    )

    patternMarkdown: fhirtypes.Markdown = Field(
        None,
        alias="patternMarkdown",
        title="Type `Markdown`",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    patternMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_patternMarkdown", title="Extension field for ``patternMarkdown``."
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
        title="Type `Oid`",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    patternOid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_patternOid", title="Extension field for ``patternOid``."
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
        title="Type `PositiveInt`",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    patternPositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_patternPositiveInt",
        title="Extension field for ``patternPositiveInt``.",
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
        title="Type `String`",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    patternString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_patternString", title="Extension field for ``patternString``."
    )

    patternTime: fhirtypes.Time = Field(
        None,
        alias="patternTime",
        title="Type `Time`",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    patternTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_patternTime", title="Extension field for ``patternTime``."
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
        title="Type `UnsignedInt`",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    patternUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_patternUnsignedInt",
        title="Extension field for ``patternUnsignedInt``.",
    )

    patternUri: fhirtypes.Uri = Field(
        None,
        alias="patternUri",
        title="Type `Uri`",
        description="Value must have at least these property values",
        one_of_many="pattern",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    patternUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_patternUri", title="Extension field for ``patternUri``."
    )

    representation: ListType[fhirtypes.Code] = Field(
        None,
        alias="representation",
        title="List of `Code` items",
        description="xmlAttr | xmlText | typeAttr | cdaText | xhtml",
    )
    representation__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_representation", title="Extension field for ``representation``."
    )

    requirements: fhirtypes.Markdown = Field(
        None,
        alias="requirements",
        title="Type `Markdown`",
        description="Why this resource has been created",
    )
    requirements__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_requirements", title="Extension field for ``requirements``."
    )

    short: fhirtypes.String = Field(
        None,
        alias="short",
        title="Type `String`",
        description="Concise definition for space-constrained presentation",
    )
    short__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_short", title="Extension field for ``short``."
    )

    sliceName: fhirtypes.String = Field(
        None,
        alias="sliceName",
        title="Type `String`",
        description="Name for this particular element (in a set of slices)",
    )
    sliceName__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sliceName", title="Extension field for ``sliceName``."
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Base definition information for tools.
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
        title="Type `String`",
        description="Max cardinality of the base element",
    )
    max__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_max", title="Extension field for ``max``."
    )

    min: fhirtypes.UnsignedInt = Field(
        ...,
        alias="min",
        title="Type `UnsignedInt`",
        description="Min cardinality of the base element",
    )
    min__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_min", title="Extension field for ``min``."
    )

    path: fhirtypes.String = Field(
        ...,
        alias="path",
        title="Type `String`",
        description="Path that identifies the base element",
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_path", title="Extension field for ``path``."
    )


class ElementDefinitionBinding(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    ValueSet details if this is coded.
    Binds to a value set if this element is coded (code, Coding,
    CodeableConcept, Quantity), or the data types (string, uri).
    """

    resource_type = Field("ElementDefinitionBinding", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Human explanation of the value set",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    strength: fhirtypes.Code = Field(
        ...,
        alias="strength",
        title="Type `Code`",
        description="required | extensible | preferred | example",
    )
    strength__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_strength", title="Extension field for ``strength``."
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
        title="Type `Uri`",
        description="Source of value set",
        one_of_many="valueSet",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueSetUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueSetUri", title="Extension field for ``valueSetUri``."
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Condition that must evaluate to true.
    Formal constraints such as co-occurrence and other constraints that can be
    computationally evaluated within the context of the instance.
    """

    resource_type = Field("ElementDefinitionConstraint", const=True)

    expression: fhirtypes.String = Field(
        ...,
        alias="expression",
        title="Type `String`",
        description="FHIRPath expression of constraint",
    )
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_expression", title="Extension field for ``expression``."
    )

    human: fhirtypes.String = Field(
        ...,
        alias="human",
        title="Type `String`",
        description="Human description of constraint",
    )
    human__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_human", title="Extension field for ``human``."
    )

    key: fhirtypes.Id = Field(
        ...,
        alias="key",
        title="Type `Id`",
        description="Target of \u0027condition\u0027 reference above",
    )
    key__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_key", title="Extension field for ``key``."
    )

    requirements: fhirtypes.String = Field(
        None,
        alias="requirements",
        title="Type `String`",
        description="Why this constraint is necessary or appropriate",
    )
    requirements__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_requirements", title="Extension field for ``requirements``."
    )

    severity: fhirtypes.Code = Field(
        ..., alias="severity", title="Type `Code`", description="error | warning"
    )
    severity__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_severity", title="Extension field for ``severity``."
    )

    source: fhirtypes.Uri = Field(
        None,
        alias="source",
        title="Type `Uri`",
        description="Reference to original source of constraint",
    )
    source__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_source", title="Extension field for ``source``."
    )

    xpath: fhirtypes.String = Field(
        None,
        alias="xpath",
        title="Type `String`",
        description="XPath expression of constraint",
    )
    xpath__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_xpath", title="Extension field for ``xpath``."
    )


class ElementDefinitionExample(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Example value (as defined for type).
    A sample value for this element demonstrating the type of information that
    would typically be found in the element.
    """

    resource_type = Field("ElementDefinitionExample", const=True)

    label: fhirtypes.String = Field(
        ...,
        alias="label",
        title="Type `String`",
        description="Describes the purpose of this example",
    )
    label__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_label", title="Extension field for ``label``."
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
        title="Type `Base64Binary`",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueBase64Binary__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_valueBase64Binary",
        title="Extension field for ``valueBase64Binary``.",
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="Type `bool`",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCode: fhirtypes.Code = Field(
        None,
        alias="valueCode",
        title="Type `Code`",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueCode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueCode", title="Extension field for ``valueCode``."
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
        title="Type `Date`",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDate", title="Extension field for ``valueDate``."
    )

    valueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="valueDateTime",
        title="Type `DateTime`",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDateTime", title="Extension field for ``valueDateTime``."
    )

    valueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="valueDecimal",
        title="Type `Decimal`",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDecimal", title="Extension field for ``valueDecimal``."
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
        title="Type `Id`",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueId", title="Extension field for ``valueId``."
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
        title="Type `Instant`",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueInstant__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueInstant", title="Extension field for ``valueInstant``."
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="Type `Integer`",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueInteger", title="Extension field for ``valueInteger``."
    )

    valueMarkdown: fhirtypes.Markdown = Field(
        None,
        alias="valueMarkdown",
        title="Type `Markdown`",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueMarkdown", title="Extension field for ``valueMarkdown``."
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
        title="Type `Oid`",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueOid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueOid", title="Extension field for ``valueOid``."
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
        title="Type `PositiveInt`",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valuePositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_valuePositiveInt",
        title="Extension field for ``valuePositiveInt``.",
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
        title="Type `String`",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    valueTime: fhirtypes.Time = Field(
        None,
        alias="valueTime",
        title="Type `Time`",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueTime", title="Extension field for ``valueTime``."
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
        title="Type `UnsignedInt`",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_valueUnsignedInt",
        title="Extension field for ``valueUnsignedInt``.",
    )

    valueUri: fhirtypes.Uri = Field(
        None,
        alias="valueUri",
        title="Type `Uri`",
        description="Value of Example (one of allowed types)",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueUri", title="Extension field for ``valueUri``."
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Map element to another set of definitions.
    Identifies a concept from an external specification that roughly
    corresponds to this element.
    """

    resource_type = Field("ElementDefinitionMapping", const=True)

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Type `String`",
        description="Comments about the mapping or its use",
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    identity: fhirtypes.Id = Field(
        ...,
        alias="identity",
        title="Type `Id`",
        description="Reference to mapping declaration",
    )
    identity__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_identity", title="Extension field for ``identity``."
    )

    language: fhirtypes.Code = Field(
        None,
        alias="language",
        title="Type `Code`",
        description="Computable language of mapping",
    )
    language__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_language", title="Extension field for ``language``."
    )

    map: fhirtypes.String = Field(
        ..., alias="map", title="Type `String`", description="Details of the mapping"
    )
    map__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_map", title="Extension field for ``map``."
    )


class ElementDefinitionSlicing(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    This element is sliced - slices follow.
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
        title="Type `String`",
        description="Text description of how slicing works (or not)",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
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
    ordered__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_ordered", title="Extension field for ``ordered``."
    )

    rules: fhirtypes.Code = Field(
        ..., alias="rules", title="Type `Code`", description="closed | open | openAtEnd"
    )
    rules__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_rules", title="Extension field for ``rules``."
    )


class ElementDefinitionSlicingDiscriminator(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Element values that are used to distinguish the slices.
    Designates which child elements are used to discriminate between the slices
    when processing an instance. If one or more discriminators are provided,
    the value of the child elements in the instance data SHALL completely
    distinguish which slice the element in the resource matches based on the
    allowed values for those elements in each of the slices.
    """

    resource_type = Field("ElementDefinitionSlicingDiscriminator", const=True)

    path: fhirtypes.String = Field(
        ..., alias="path", title="Type `String`", description="Path to element value"
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_path", title="Extension field for ``path``."
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code`",
        description="value | exists | pattern | type | profile",
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )


class ElementDefinitionType(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Data type and Profile for this element.
    The data type or resource that the value of this element is permitted to
    be.
    """

    resource_type = Field("ElementDefinitionType", const=True)

    aggregation: ListType[fhirtypes.Code] = Field(
        None,
        alias="aggregation",
        title="List of `Code` items",
        description="contained | referenced | bundled - how aggregated",
    )
    aggregation__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_aggregation", title="Extension field for ``aggregation``.")

    code: fhirtypes.Uri = Field(
        ...,
        alias="code",
        title="Type `Uri`",
        description="Data type or Resource (reference to definition)",
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    profile: fhirtypes.Uri = Field(
        None,
        alias="profile",
        title="Type `Uri`",
        description="Profile (StructureDefinition) to apply (or IG)",
    )
    profile__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_profile", title="Extension field for ``profile``."
    )

    targetProfile: fhirtypes.Uri = Field(
        None,
        alias="targetProfile",
        title="Type `Uri`",
        description="Profile (StructureDefinition) to apply to reference target (or IG)",
    )
    targetProfile__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_targetProfile", title="Extension field for ``targetProfile``."
    )

    versioning: fhirtypes.Code = Field(
        None,
        alias="versioning",
        title="Type `Code`",
        description="either | independent | specific",
    )
    versioning__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_versioning", title="Extension field for ``versioning``."
    )
