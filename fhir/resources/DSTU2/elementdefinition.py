# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ElementDefinition
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic.v1 import Field, root_validator

from . import backboneelement, element, fhirtypes


class ElementDefinition(backboneelement.BackboneElement):
    """
    Definition of an element in a resource or extension.
    Captures constraints on each element within the resource, profile, or
    extension.
    """

    resource_type = Field("ElementDefinition", const=True)

    alias: ListType[fhirtypes.String] = Field(
        None,
        alias="alias",
        title="Other names",
        description="Identifies additional names by which this element might also be known.",
    )

    base: fhirtypes.ElementDefinitionBaseType = Field(
        None,
        alias="base",
        title="Base definition information for tools",
        description=(
            "Information about the base definition of the element, provided to make"
            " it unnecessary for tools to trace the deviation of the element "
            "through the derived and related profiles. When the element definition "
            "is not the original definition of an element - i.g. either in a "
            "constraint on another type, or for elements from a super type in a "
            "snap shot - then the information in provided in the element definition"
            " may be different to the base definition. On the original definition "
            "of the element, it will be same."
        ),
    )

    binding: fhirtypes.ElementDefinitionBindingType = Field(
        None,
        alias="binding",
        title="ValueSet details if this is coded",
        description=(
            "Binds to a value set if this element is coded (code, Coding, "
            "CodeableConcept, Quantity), or the data types (string, uri)."
        ),
    )

    code: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="code",
        title="Corresponding codes in terminologies",
        description=(
            "A code that has the same meaning as the element in a particular "
            "terminology."
        ),
    )

    comments: fhirtypes.Markdown = Field(
        None,
        alias="comments",
        title="Comments about the use of this element",
        description=(
            "Explanatory notes and implementation guidance about the data element, "
            "including notes about how to use the data properly, exceptions to "
            "proper use, etc. (Note: The text you are reading is specified in "
            "ElementDefinition.comment)."
        ),
    )

    condition: ListType[fhirtypes.Id] = Field(
        None,
        alias="condition",
        title="Reference to invariant about presence",
        description=(
            "A reference to an invariant that may make additional statements about "
            "the cardinality or value in the instance."
        ),
    )

    constraint: ListType[fhirtypes.ElementDefinitionConstraintType] = Field(
        None,
        alias="constraint",
        title="Condition that must evaluate to true",
        description=(
            "Formal constraints such as co-occurrence and other constraints that "
            "can be computationally evaluated within the context of the instance."
        ),
    )

    defaultValueAddress: fhirtypes.AddressType = Field(
        None,
        alias="defaultValueAddress",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueAnnotation: fhirtypes.AnnotationType = Field(
        None,
        alias="defaultValueAnnotation",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="defaultValueAttachment",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueBase64Binary: fhirtypes.Base64Binary = Field(
        None,
        alias="defaultValueBase64Binary",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )
    defaultValueBoolean: fhirtypes.Boolean = Field(
        None,
        alias="defaultValueBoolean",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueCode: fhirtypes.Code = Field(
        None,
        alias="defaultValueCode",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="defaultValueCodeableConcept",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueCoding: fhirtypes.CodingType = Field(
        None,
        alias="defaultValueCoding",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueContactPoint: fhirtypes.ContactPointType = Field(
        None,
        alias="defaultValueContactPoint",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueDate: fhirtypes.Date = Field(
        None,
        alias="defaultValueDate",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="defaultValueDateTime",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="defaultValueDecimal",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueHumanName: fhirtypes.HumanNameType = Field(
        None,
        alias="defaultValueHumanName",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueId: fhirtypes.Id = Field(
        None,
        alias="defaultValueId",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="defaultValueIdentifier",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueInstant: fhirtypes.Instant = Field(
        None,
        alias="defaultValueInstant",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueInteger: fhirtypes.Integer = Field(
        None,
        alias="defaultValueInteger",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueMarkdown: fhirtypes.Markdown = Field(
        None,
        alias="defaultValueMarkdown",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueMeta: fhirtypes.MetaType = Field(
        None,
        alias="defaultValueMeta",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueOid: fhirtypes.Oid = Field(
        None,
        alias="defaultValueOid",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValuePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="defaultValuePeriod",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValuePositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="defaultValuePositiveInt",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="defaultValueQuantity",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueRange: fhirtypes.RangeType = Field(
        None,
        alias="defaultValueRange",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueRatio: fhirtypes.RatioType = Field(
        None,
        alias="defaultValueRatio",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueReference: fhirtypes.ReferenceType = Field(
        None,
        alias="defaultValueReference",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    defaultValueSampledData: fhirtypes.SampledDataType = Field(
        None,
        alias="defaultValueSampledData",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueSignature: fhirtypes.SignatureType = Field(
        None,
        alias="defaultValueSignature",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueString: fhirtypes.String = Field(
        None,
        alias="defaultValueString",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueTime: fhirtypes.Time = Field(
        None,
        alias="defaultValueTime",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueTiming: fhirtypes.TimingType = Field(
        None,
        alias="defaultValueTiming",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="defaultValueUnsignedInt",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueUri: fhirtypes.Uri = Field(
        None,
        alias="defaultValueUri",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    definition: fhirtypes.Markdown = Field(
        None,
        alias="definition",
        title="Full formal definition as narrative text",
        description=(
            "Provides a complete explanation of the meaning of the data element for"
            " human readability.  For the case of elements derived from existing "
            "elements (e.g. constraints), the definition SHALL be consistent with "
            "the base definition, but convey the meaning of the element in the "
            "particular context of use of the resource. (Note: The text you are "
            "reading is specified in ElementDefinition.definition)."
        ),
    )

    exampleAddress: fhirtypes.AddressType = Field(
        None,
        alias="exampleAddress",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    exampleAnnotation: fhirtypes.AnnotationType = Field(
        None,
        alias="exampleAnnotation",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    exampleAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="exampleAttachment",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    exampleBase64Binary: fhirtypes.Base64Binary = Field(
        None,
        alias="exampleBase64Binary",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )
    exampleBoolean: fhirtypes.Boolean = Field(
        None,
        alias="exampleBoolean",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    exampleCode: fhirtypes.Code = Field(
        None,
        alias="exampleCode",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    exampleCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="exampleCodeableConcept",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    exampleCoding: fhirtypes.CodingType = Field(
        None,
        alias="exampleCoding",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    exampleContactPoint: fhirtypes.ContactPointType = Field(
        None,
        alias="exampleContactPoint",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    exampleDate: fhirtypes.Date = Field(
        None,
        alias="exampleDate",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    exampleDateTime: fhirtypes.DateTime = Field(
        None,
        alias="exampleDateTime",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    exampleDecimal: fhirtypes.Decimal = Field(
        None,
        alias="exampleDecimal",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    exampleHumanName: fhirtypes.HumanNameType = Field(
        None,
        alias="exampleHumanName",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    exampleId: fhirtypes.Id = Field(
        None,
        alias="exampleId",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    exampleIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="exampleIdentifier",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    exampleInstant: fhirtypes.Instant = Field(
        None,
        alias="exampleInstant",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    exampleInteger: fhirtypes.Integer = Field(
        None,
        alias="exampleInteger",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    exampleMarkdown: fhirtypes.Markdown = Field(
        None,
        alias="exampleMarkdown",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    exampleMeta: fhirtypes.MetaType = Field(
        None,
        alias="exampleMeta",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    exampleOid: fhirtypes.Oid = Field(
        None,
        alias="exampleOid",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    examplePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="examplePeriod",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    examplePositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="examplePositiveInt",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    exampleQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="exampleQuantity",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    exampleRange: fhirtypes.RangeType = Field(
        None,
        alias="exampleRange",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    exampleRatio: fhirtypes.RatioType = Field(
        None,
        alias="exampleRatio",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    exampleReference: fhirtypes.ReferenceType = Field(
        None,
        alias="exampleReference",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    exampleSampledData: fhirtypes.SampledDataType = Field(
        None,
        alias="exampleSampledData",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    exampleSignature: fhirtypes.SignatureType = Field(
        None,
        alias="exampleSignature",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    exampleString: fhirtypes.String = Field(
        None,
        alias="exampleString",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    exampleTime: fhirtypes.Time = Field(
        None,
        alias="exampleTime",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    exampleTiming: fhirtypes.TimingType = Field(
        None,
        alias="exampleTiming",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    exampleUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="exampleUnsignedInt",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    exampleUri: fhirtypes.Uri = Field(
        None,
        alias="exampleUri",
        title="Specified value if missing from instance",
        description=(
            "A sample value for this element demonstrating the type of"
            "information that would typically be captured."
        ),
        # Choice of Data Types. i.e example[x]
        one_of_many="example",
        one_of_many_required=False,
    )

    fixedAddress: fhirtypes.AddressType = Field(
        None,
        alias="fixedAddress",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedAnnotation: fhirtypes.AnnotationType = Field(
        None,
        alias="fixedAnnotation",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="fixedAttachment",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedBase64Binary: fhirtypes.Base64Binary = Field(
        None,
        alias="fixedBase64Binary",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedBoolean: fhirtypes.Boolean = Field(
        None,
        alias="fixedBoolean",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedCode: fhirtypes.Code = Field(
        None,
        alias="fixedCode",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="fixedCodeableConcept",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedCoding: fhirtypes.CodingType = Field(
        None,
        alias="fixedCoding",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedContactPoint: fhirtypes.ContactPointType = Field(
        None,
        alias="fixedContactPoint",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedDate: fhirtypes.Date = Field(
        None,
        alias="fixedDate",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedDateTime: fhirtypes.DateTime = Field(
        None,
        alias="fixedDateTime",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedDecimal: fhirtypes.Decimal = Field(
        None,
        alias="fixedDecimal",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedHumanName: fhirtypes.HumanNameType = Field(
        None,
        alias="fixedHumanName",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedId: fhirtypes.Id = Field(
        None,
        alias="fixedId",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="fixedIdentifier",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedInstant: fhirtypes.Instant = Field(
        None,
        alias="fixedInstant",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedInteger: fhirtypes.Integer = Field(
        None,
        alias="fixedInteger",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedMarkdown: fhirtypes.Markdown = Field(
        None,
        alias="fixedMarkdown",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedMeta: fhirtypes.MetaType = Field(
        None,
        alias="fixedMeta",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedOid: fhirtypes.Oid = Field(
        None,
        alias="fixedOid",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="fixedPeriod",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedPositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="fixedPositiveInt",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="fixedQuantity",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedRange: fhirtypes.RangeType = Field(
        None,
        alias="fixedRange",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedRatio: fhirtypes.RatioType = Field(
        None,
        alias="fixedRatio",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedReference: fhirtypes.ReferenceType = Field(
        None,
        alias="fixedReference",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    fixedSampledData: fhirtypes.SampledDataType = Field(
        None,
        alias="fixedSampledData",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedSignature: fhirtypes.SignatureType = Field(
        None,
        alias="fixedSignature",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedString: fhirtypes.String = Field(
        None,
        alias="fixedString",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedTime: fhirtypes.Time = Field(
        None,
        alias="fixedTime",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedTiming: fhirtypes.TimingType = Field(
        None,
        alias="fixedTiming",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="fixedUnsignedInt",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedUri: fhirtypes.Uri = Field(
        None,
        alias="fixedUri",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance. For purposes of comparison, non-significant whitespace "
            "is ignored, and all values must be an exact match (case and accent "
            "sensitive). Missing elements/attributes must also be missing."
        ),
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    isModifier: fhirtypes.Boolean = Field(
        None,
        alias="isModifier",
        title="If this modifies the meaning of other elements",
        description=(
            "If true, the value of this element affects the interpretation of the "
            "element or resource that contains it, and the value of the element "
            "cannot be ignored. Typically, this is used for status, negation and "
            "qualification codes. The effect of this is that the element cannot be "
            "ignored by systems: they SHALL either recognize the element and "
            "process it, and/or a pre-determination has been made that it is not "
            "relevant to their particular system."
        ),
    )

    isSummary: fhirtypes.Boolean = Field(
        None,
        alias="isSummary",
        title="Include when _summary = true?",
        description=(
            "Whether the element should be included if a client requests a search "
            "with the parameter _summary=true."
        ),
    )

    label: fhirtypes.String = Field(
        None,
        alias="label",
        title="Name for element to display with or prompt for element",
        description=(
            "A single preferred label which is the text to display beside the "
            "element indicating its meaning or to use to prompt for the element in "
            "a user display or form."
        ),
    )

    mapping: ListType[fhirtypes.ElementDefinitionMappingType] = Field(
        None,
        alias="mapping",
        title="Map element to another set of definitions",
        description=(
            "Identifies a concept from an external specification that roughly "
            "corresponds to this element."
        ),
    )

    max: fhirtypes.String = Field(
        None,
        alias="max",
        title="Maximum Cardinality (a number or *)",
        description=(
            "The maximum number of times this element is permitted to appear in the"
            " instance."
        ),
    )

    maxLength: fhirtypes.Integer = Field(
        None,
        alias="maxLength",
        title="Max length for strings",
        description=(
            "Indicates the maximum length in characters that is permitted to be "
            "present in conformant instances and which is expected to be supported "
            "by conformant consumers that support the element."
        ),
    )

    maxValueDate: fhirtypes.Date = Field(
        None,
        alias="maxValueDate",
        title="Maximum Allowed Value (for some types)",
        description=(
            "The maximum allowed value for the element. The value is inclusive. "
            "This is allowed for the types date, dateTime, instant, time, decimal, "
            "integer, and Quantity."
        ),
        # Choice of Data Types. i.e maxValue[x]
        one_of_many="maxValue",
        one_of_many_required=False,
    )

    maxValueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="maxValueDateTime",
        title="Maximum Allowed Value (for some types)",
        description=(
            "The maximum allowed value for the element. The value is inclusive. "
            "This is allowed for the types date, dateTime, instant, time, decimal, "
            "integer, and Quantity."
        ),
        # Choice of Data Types. i.e maxValue[x]
        one_of_many="maxValue",
        one_of_many_required=False,
    )

    maxValueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="maxValueDecimal",
        title="Maximum Allowed Value (for some types)",
        description=(
            "The maximum allowed value for the element. The value is inclusive. "
            "This is allowed for the types date, dateTime, instant, time, decimal, "
            "integer, and Quantity."
        ),
        # Choice of Data Types. i.e maxValue[x]
        one_of_many="maxValue",
        one_of_many_required=False,
    )

    maxValueInstant: fhirtypes.Instant = Field(
        None,
        alias="maxValueInstant",
        title="Maximum Allowed Value (for some types)",
        description=(
            "The maximum allowed value for the element. The value is inclusive. "
            "This is allowed for the types date, dateTime, instant, time, decimal, "
            "integer, and Quantity."
        ),
        # Choice of Data Types. i.e maxValue[x]
        one_of_many="maxValue",
        one_of_many_required=False,
    )

    maxValueInteger: fhirtypes.Integer = Field(
        None,
        alias="maxValueInteger",
        title="Maximum Allowed Value (for some types)",
        description=(
            "The maximum allowed value for the element. The value is inclusive. "
            "This is allowed for the types date, dateTime, instant, time, decimal, "
            "integer, and Quantity."
        ),
        # Choice of Data Types. i.e maxValue[x]
        one_of_many="maxValue",
        one_of_many_required=False,
    )

    maxValuePositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="maxValuePositiveInt",
        title="Maximum Allowed Value (for some types)",
        description=(
            "The maximum allowed value for the element. The value is inclusive. "
            "This is allowed for the types date, dateTime, instant, time, decimal, "
            "integer, and Quantity."
        ),
        # Choice of Data Types. i.e maxValue[x]
        one_of_many="maxValue",
        one_of_many_required=False,
    )

    maxValueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="maxValueQuantity",
        title="Maximum Allowed Value (for some types)",
        description=(
            "The maximum allowed value for the element. The value is inclusive. "
            "This is allowed for the types date, dateTime, instant, time, decimal, "
            "integer, and Quantity."
        ),
        # Choice of Data Types. i.e maxValue[x]
        one_of_many="maxValue",
        one_of_many_required=False,
    )

    maxValueTime: fhirtypes.Time = Field(
        None,
        alias="maxValueTime",
        title="Maximum Allowed Value (for some types)",
        description=(
            "The maximum allowed value for the element. The value is inclusive. "
            "This is allowed for the types date, dateTime, instant, time, decimal, "
            "integer, and Quantity."
        ),
        # Choice of Data Types. i.e maxValue[x]
        one_of_many="maxValue",
        one_of_many_required=False,
    )

    maxValueUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="maxValueUnsignedInt",
        title="Maximum Allowed Value (for some types)",
        description=(
            "The maximum allowed value for the element. The value is inclusive. "
            "This is allowed for the types date, dateTime, instant, time, decimal, "
            "integer, and Quantity."
        ),
        # Choice of Data Types. i.e maxValue[x]
        one_of_many="maxValue",
        one_of_many_required=False,
    )

    meaningWhenMissing: fhirtypes.Markdown = Field(
        None,
        alias="meaningWhenMissing",
        title="Implicit meaning when this element is missing",
        description=(
            "The Implicit meaning that is to be understood when this element is "
            "missing (e.g. 'when this element is missing, the period is ongoing')."
        ),
    )

    min: fhirtypes.Integer = Field(
        None,
        alias="min",
        title="Minimum Cardinality",
        description="The minimum number of times this element SHALL appear in the instance.",
    )

    minValueDate: fhirtypes.Date = Field(
        None,
        alias="minValueDate",
        title="Minimum Allowed Value (for some types)",
        description=(
            "The minimum allowed value for the element. The value is inclusive. "
            "This is allowed for the types date, dateTime, instant, time, decimal, "
            "integer, and Quantity."
        ),
        # Choice of Data Types. i.e minValue[x]
        one_of_many="minValue",
        one_of_many_required=False,
    )

    minValueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="minValueDateTime",
        title="Minimum Allowed Value (for some types)",
        description=(
            "The minimum allowed value for the element. The value is inclusive. "
            "This is allowed for the types date, dateTime, instant, time, decimal, "
            "integer, and Quantity."
        ),
        # Choice of Data Types. i.e minValue[x]
        one_of_many="minValue",
        one_of_many_required=False,
    )

    minValueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="minValueDecimal",
        title="Minimum Allowed Value (for some types)",
        description=(
            "The minimum allowed value for the element. The value is inclusive. "
            "This is allowed for the types date, dateTime, instant, time, decimal, "
            "integer, and Quantity."
        ),
        # Choice of Data Types. i.e minValue[x]
        one_of_many="minValue",
        one_of_many_required=False,
    )

    minValueInstant: fhirtypes.Instant = Field(
        None,
        alias="minValueInstant",
        title="Minimum Allowed Value (for some types)",
        description=(
            "The minimum allowed value for the element. The value is inclusive. "
            "This is allowed for the types date, dateTime, instant, time, decimal, "
            "integer, and Quantity."
        ),
        # Choice of Data Types. i.e minValue[x]
        one_of_many="minValue",
        one_of_many_required=False,
    )

    minValueInteger: fhirtypes.Integer = Field(
        None,
        alias="minValueInteger",
        title="Minimum Allowed Value (for some types)",
        description=(
            "The minimum allowed value for the element. The value is inclusive. "
            "This is allowed for the types date, dateTime, instant, time, decimal, "
            "integer, and Quantity."
        ),
        # Choice of Data Types. i.e minValue[x]
        one_of_many="minValue",
        one_of_many_required=False,
    )

    minValuePositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="minValuePositiveInt",
        title="Minimum Allowed Value (for some types)",
        description=(
            "The minimum allowed value for the element. The value is inclusive. "
            "This is allowed for the types date, dateTime, instant, time, decimal, "
            "integer, and Quantity."
        ),
        # Choice of Data Types. i.e minValue[x]
        one_of_many="minValue",
        one_of_many_required=False,
    )

    minValueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="minValueQuantity",
        title="Minimum Allowed Value (for some types)",
        description=(
            "The minimum allowed value for the element. The value is inclusive. "
            "This is allowed for the types date, dateTime, instant, time, decimal, "
            "integer, and Quantity."
        ),
        # Choice of Data Types. i.e minValue[x]
        one_of_many="minValue",
        one_of_many_required=False,
    )

    minValueTime: fhirtypes.Time = Field(
        None,
        alias="minValueTime",
        title="Minimum Allowed Value (for some types)",
        description=(
            "The minimum allowed value for the element. The value is inclusive. "
            "This is allowed for the types date, dateTime, instant, time, decimal, "
            "integer, and Quantity."
        ),
        # Choice of Data Types. i.e minValue[x]
        one_of_many="minValue",
        one_of_many_required=False,
    )

    minValueUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="minValueUnsignedInt",
        title="Minimum Allowed Value (for some types)",
        description=(
            "The minimum allowed value for the element. The value is inclusive. "
            "This is allowed for the types date, dateTime, instant, time, decimal, "
            "integer, and Quantity."
        ),
        # Choice of Data Types. i.e minValue[x]
        one_of_many="minValue",
        one_of_many_required=False,
    )

    mustSupport: fhirtypes.Boolean = Field(
        None,
        alias="mustSupport",
        title="If the element must be supported",
        description=(
            "If true, implementations that produce or consume resources SHALL "
            'provide "support" for the element in some meaningful way.  If false, '
            "the element may be ignored and not supported. If false, whether to "
            "populate or use the data element in any way is at the discretion of "
            "the implementation."
        ),
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name for this particular element definition (reference target)",
        description=(
            "The name of this element definition (to refer to it from other element "
            "definitions using ElementDefinition.nameReference). This is a unique name "
            "referring to a specific set of constraints applied to this element. One "
            "use of this is to provide a name to different slices of the same element."
        ),
    )

    nameReference: fhirtypes.String = Field(
        None,
        alias="nameReference",
        title="To another element constraint (by element.name)",
        description=(
            "Identifies the name of a slice defined elsewhere in the profile"
            "whose constraints should be applied to the current element."
        ),
    )

    path: fhirtypes.String = Field(
        ...,
        alias="path",
        title="Path of the element in the hierarchy of elements",
        description=(
            'The path identifies the element and is expressed as a "."-separated '
            "list of ancestor elements, beginning with the name of the resource or "
            "extension."
        ),
    )

    patternAddress: fhirtypes.AddressType = Field(
        None,
        alias="patternAddress",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternAnnotation: fhirtypes.AnnotationType = Field(
        None,
        alias="patternAnnotation",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="patternAttachment",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternBase64Binary: fhirtypes.Base64Binary = Field(
        None,
        alias="patternBase64Binary",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternBoolean: fhirtypes.Boolean = Field(
        None,
        alias="patternBoolean",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternCode: fhirtypes.Code = Field(
        None,
        alias="patternCode",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="patternCodeableConcept",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternCoding: fhirtypes.CodingType = Field(
        None,
        alias="patternCoding",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternContactPoint: fhirtypes.ContactPointType = Field(
        None,
        alias="patternContactPoint",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternDate: fhirtypes.Date = Field(
        None,
        alias="patternDate",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternDateTime: fhirtypes.DateTime = Field(
        None,
        alias="patternDateTime",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternDecimal: fhirtypes.Decimal = Field(
        None,
        alias="patternDecimal",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternHumanName: fhirtypes.HumanNameType = Field(
        None,
        alias="patternHumanName",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternId: fhirtypes.Id = Field(
        None,
        alias="patternId",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="patternIdentifier",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternInstant: fhirtypes.Instant = Field(
        None,
        alias="patternInstant",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternInteger: fhirtypes.Integer = Field(
        None,
        alias="patternInteger",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternMarkdown: fhirtypes.Markdown = Field(
        None,
        alias="patternMarkdown",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternMeta: fhirtypes.MetaType = Field(
        None,
        alias="patternMeta",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternOid: fhirtypes.Oid = Field(
        None,
        alias="patternOid",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="patternPeriod",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternPositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="patternPositiveInt",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="patternQuantity",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternRange: fhirtypes.RangeType = Field(
        None,
        alias="patternRange",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternRatio: fhirtypes.RatioType = Field(
        None,
        alias="patternRatio",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternReference: fhirtypes.ReferenceType = Field(
        None,
        alias="patternReference",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    patternSampledData: fhirtypes.SampledDataType = Field(
        None,
        alias="patternSampledData",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternSignature: fhirtypes.SignatureType = Field(
        None,
        alias="patternSignature",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternString: fhirtypes.String = Field(
        None,
        alias="patternString",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternTime: fhirtypes.Time = Field(
        None,
        alias="patternTime",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternTiming: fhirtypes.TimingType = Field(
        None,
        alias="patternTiming",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="patternUnsignedInt",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternUri: fhirtypes.Uri = Field(
        None,
        alias="patternUri",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that the value in the instance SHALL follow - that "
            "is, any value in the pattern must be found in the instance. Other "
            "additional values may be found too. This is effectively constraint by "
            "example.    When pattern[x] is used to constrain a primitive, it means"
            " that the value provided in the pattern[x] must match the instance "
            "value exactly.  When pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] array must "
            "(recursively) match at least one element from the instance array.  "
            "When pattern[x] is used to constrain a complex object, it means that "
            "each property in the pattern must be present in the complex object, "
            "and its value must recursively match -- i.e.,  1. If primitive: it "
            "must match exactly the pattern value 2. If a complex object: it must "
            "match (recursively) the pattern value 3. If an array: it must match "
            "(recursively) the pattern value."
        ),
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    representation: ListType[fhirtypes.Code] = Field(
        None,
        alias="representation",
        title="How this element is represented in instances",
        description=(
            "Codes that define how this element is represented in instances, when "
            "the deviation varies from the normal case."
        ),
    )

    requirements: fhirtypes.Markdown = Field(
        None,
        alias="requirements",
        title="Why this resource has been created",
        description=(
            "This element is for traceability of why the element was created and "
            "why the constraints exist as they do. This may be used to point to "
            "source materials or specifications that drove the structure of this "
            "element."
        ),
    )

    short: fhirtypes.String = Field(
        None,
        alias="short",
        title="Concise definition for space-constrained presentation",
        description=(
            "A concise description of what this element means (e.g. for use in "
            "autogenerated summaries)."
        ),
    )

    slicing: fhirtypes.ElementDefinitionSlicingType = Field(
        None,
        alias="slicing",
        title="This element is sliced - slices follow",
        description=(
            "Indicates that the element is sliced into a set of alternative "
            "definitions (i.e. in a structure definition, there are multiple "
            "different constraints on a single element in the base resource). "
            "Slicing can be used in any resource that has cardinality ..* on the "
            "base resource, or any resource with a choice of types. The set of "
            "slices is any elements that come after this in the element sequence "
            "that have the same path, until a shorter path occurs (the shorter path"
            " terminates the set)."
        ),
    )

    type: ListType[fhirtypes.ElementDefinitionTypeType] = Field(
        None,
        alias="type",
        title="Data type and Profile for this element",
        description=(
            "The data type or resource that the value of this element is permitted "
            "to be."
        ),
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
                "defaultValueAnnotation",
                "defaultValueAttachment",
                "defaultValueBase64Binary",
                "defaultValueBoolean",
                "defaultValueCode",
                "defaultValueCodeableConcept",
                "defaultValueCoding",
                "defaultValueContactPoint",
                "defaultValueDate",
                "defaultValueDateTime",
                "defaultValueDecimal",
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
            "example": [
                "exampleAddress",
                "exampleAnnotation",
                "exampleAttachment",
                "exampleBase64Binary",
                "exampleBoolean",
                "exampleCode",
                "exampleCodeableConcept",
                "exampleCoding",
                "exampleContactPoint",
                "exampleDate",
                "exampleDateTime",
                "exampleDecimal",
                "exampleHumanName",
                "exampleId",
                "exampleIdentifier",
                "exampleInstant",
                "exampleInteger",
                "exampleMarkdown",
                "exampleMeta",
                "exampleMoney",
                "exampleOid",
                "examplePeriod",
                "examplePositiveInt",
                "exampleQuantity",
                "exampleRange",
                "exampleRatio",
                "exampleReference",
                "exampleSampledData",
                "exampleSignature",
                "exampleString",
                "exampleTime",
                "exampleTiming",
                "exampleUnsignedInt",
                "exampleUri",
            ],
            "fixed": [
                "fixedAddress",
                "fixedAnnotation",
                "fixedAttachment",
                "fixedBase64Binary",
                "fixedBoolean",
                "fixedCode",
                "fixedCodeableConcept",
                "fixedCoding",
                "fixedContactPoint",
                "fixedDate",
                "fixedDateTime",
                "fixedDecimal",
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
                "patternAnnotation",
                "patternAttachment",
                "patternBase64Binary",
                "patternBoolean",
                "patternCode",
                "patternCodeableConcept",
                "patternCoding",
                "patternContactPoint",
                "patternDate",
                "patternDateTime",
                "patternDecimal",
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
    """
    Base definition information for tools.
    Information about the base definition of the element, provided to make it
    unnecessary for tools to trace the deviation of the element through the
    derived and related profiles. When the element definition is not the
    original definition of an element - i.g. either in a constraint on another
    type, or for elements from a super type in a snap shot - then the
    information in provided in the element definition may be different to the
    base definition. On the original definition of the element, it will be
    same.
    """

    resource_type = Field("ElementDefinitionBase", const=True)

    max: fhirtypes.String = Field(
        ...,
        alias="max",
        title="Max cardinality of the base element",
        description="Maximum cardinality of the base element identified by the path.",
    )

    min: fhirtypes.Integer = Field(
        ...,
        alias="min",
        title="Min cardinality of the base element",
        description="Minimum cardinality of the base element identified by the path.",
    )

    path: fhirtypes.String = Field(
        ...,
        alias="path",
        title="Path that identifies the base element",
        description=(
            "The Path that identifies the base element - this matches the "
            "ElementDefinition.path for that element. Across FHIR, there is only "
            "one base definition of any element - that is, an element definition on"
            " a [StructureDefinition](structuredefinition.html#) without a "
            "StructureDefinition.base."
        ),
    )


class ElementDefinitionBinding(element.Element):
    """
    ValueSet details if this is coded.
    Binds to a value set if this element is coded (code, Coding,
    CodeableConcept, Quantity), or the data types (string, uri).
    """

    resource_type = Field("ElementDefinitionBinding", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Human explanation of the value set",
        description="Describes the intended use of this particular set of codes.",
    )

    strength: fhirtypes.Code = Field(
        ...,
        alias="strength",
        title="required | extensible | preferred | example",
        description=(
            "Indicates the degree of conformance expectations associated with this "
            "binding - that is, the degree to which the provided value set must be "
            "adhered to in the instances."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["required", "extensible", "preferred", "example"],
    )

    valueSetUri: fhirtypes.Uri = Field(
        None,
        alias="valueSetUri",
        title="Value Set URI",
        description=(
            "Points to the value set or external definition "
            "(e.g. implicit value set) that identifies the set of codes to be used."
        ),
        one_of_many="valueSet",
        one_of_many_required=True,
    )

    valueSetReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueSetReference",
        title="ValueSet reference",
        description="A reference to an associated resource of the value set",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ValueSet"],
        # Choice of Data Types. i.e valueSet[x]
        one_of_many="valueSet",
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
        one_of_many_fields = {"valueSet": ["valueSetUri", "valueSetReference"]}

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
    """
    Condition that must evaluate to true.
    Formal constraints such as co-occurrence and other constraints that can be
    computationally evaluated within the context of the instance.
    """

    resource_type = Field("ElementDefinitionConstraint", const=True)

    human: fhirtypes.String = Field(
        ...,
        alias="human",
        title="Human description of constraint",
        description=(
            "Text that can be used to describe the constraint in messages "
            "identifying that the constraint has been violated."
        ),
    )

    key: fhirtypes.Id = Field(
        ...,
        alias="key",
        title="Target of 'condition' reference above",
        description=(
            "Allows identification of which elements have their cardinalities "
            "impacted by the constraint.  Will not be referenced for constraints "
            "that do not affect cardinality."
        ),
    )

    requirements: fhirtypes.String = Field(
        None,
        alias="requirements",
        title="Why this constraint is necessary or appropriate",
        description="Description of why this constraint is necessary or appropriate.",
    )

    severity: fhirtypes.Code = Field(
        ...,
        alias="severity",
        title="error | warning",
        description=(
            "Identifies the impact constraint violation has on the conformance of "
            "the instance."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["error", "warning"],
    )

    xpath: fhirtypes.String = Field(
        ...,
        alias="xpath",
        title="XPath expression of constraint",
        description=(
            "An XPath expression of constraint that can be executed to see if this "
            "constraint is met."
        ),
    )


class ElementDefinitionMapping(element.Element):
    """
    Map element to another set of definitions.
    Identifies a concept from an external specification that roughly
    corresponds to this element.
    """

    resource_type = Field("ElementDefinitionMapping", const=True)

    identity: fhirtypes.Id = Field(
        ...,
        alias="identity",
        title="Reference to mapping declaration",
        description="An internal reference to the definition of a mapping.",
    )

    language: fhirtypes.Code = Field(
        None,
        alias="language",
        title="Computable language of mapping",
        description="Identifies the computable language in which mapping.map is expressed.",
    )

    map: fhirtypes.String = Field(
        ...,
        alias="map",
        title="Details of the mapping",
        description=(
            "Expresses what part of the target specification corresponds to this "
            "element."
        ),
    )


class ElementDefinitionSlicing(element.Element):
    """
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
        title="Text description of how slicing works (or not)",
        description=(
            "A human-readable text description of how the slicing works. If there "
            "is no discriminator, this is required to be present to provide "
            "whatever information is possible about how the slices can be "
            "differentiated."
        ),
    )

    discriminator: ListType[fhirtypes.String] = Field(
        None,
        alias="discriminator",
        title="Element values that are used to distinguish the slices",
        description=(
            "Designates which child elements are used to discriminate between the "
            "slices when processing an instance. If one or more discriminators are "
            "provided, the value of the child elements in the instance data SHALL "
            "completely distinguish which slice the element in the resource matches"
            " based on the allowed values for those elements in each of the slices."
        ),
    )

    ordered: fhirtypes.Boolean = Field(
        None,
        alias="ordered",
        title="If elements must be in same order as slices",
        description=(
            "If the matching elements have to occur in the same order as defined in"
            " the profile."
        ),
    )

    rules: fhirtypes.Code = Field(
        ...,
        alias="rules",
        title="closed | open | openAtEnd",
        description=(
            "Whether additional slices are allowed or not. When the slices are "
            "ordered, profile authors can also say that additional slices are only "
            "allowed at the end."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["closed", "open", "openAtEnd"],
    )


class ElementDefinitionType(element.Element):
    """
    Data type and Profile for this element.
    The data type or resource that the value of this element is permitted to
    be.
    """

    resource_type = Field("ElementDefinitionType", const=True)

    aggregation: ListType[fhirtypes.Code] = Field(
        None,
        alias="aggregation",
        title="contained | referenced | bundled - how aggregated",
        description=(
            "If the type is a reference to another resource, how the resource is or"
            " can be aggregated - is it a contained resource, or a reference, and "
            "if the context is a bundle, is it included in the bundle."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["contained", "referenced", "bundled"],
    )

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Data type or Resource (reference to definition)",
        description=(
            "If the element is a reference to another resource, "
            'this element contains "Reference", and the profile element '
            "refers to the profile of the allowed target of the resource, "
            "which may be a reference to the general definition of a resource "
            "(e.g. http://hl7.org/fhir/StructureDefinition/Patient). There would "
            "be one pair of type/code for each allowed target resource type."
        ),
    )

    profile: ListType[fhirtypes.Uri] = Field(
        None,
        alias="profile",
        title="Profiles (StructureDefinition or IG) - one must apply",
        description=(
            "Identifies a profile structure or implementation Guide that "
            "SHALL hold for resources or datatypes referenced as the type "
            "of this element. Can be a local reference - to another structure"
            "in this profile, or a reference to a structure in another profile. "
            "When more than one profile is specified, the content must conform to "
            "all of them. When an implementation guide is specified, the resource "
            "SHALL conform to at least one profile defined in the implementation "
            "guide."
        ),
    )
