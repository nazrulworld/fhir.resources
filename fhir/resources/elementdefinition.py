# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ElementDefinition
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import backbonetype, element, fhirtypes


class ElementDefinition(backbonetype.BackboneType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Definition of an element in a resource or extension.
    Captures constraints on each element within the resource, profile, or
    extension.
    """

    resource_type = Field("ElementDefinition", const=True)

    alias: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="alias",
        title="Other names",
        description="Identifies additional names by which this element might also be known.",
        # if property is element of this resource.
        element_property=True,
    )
    alias__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_alias", title="Extension field for ``alias``.")

    base: fhirtypes.ElementDefinitionBaseType = Field(
        None,
        alias="base",
        title="Base definition information for tools",
        description=(
            "Information about the base definition of the element, provided to make"
            " it unnecessary for tools to trace the deviation of the element "
            "through the derived and related profiles. When the element definition "
            "is not the original definition of an element - e.g. either in a "
            "constraint on another type, or for elements from a super type in a "
            "snap shot - then the information in provided in the element definition"
            " may be different to the base definition. On the original definition "
            "of the element, it will be same."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    binding: fhirtypes.ElementDefinitionBindingType = Field(
        None,
        alias="binding",
        title="ValueSet details if this is coded",
        description=(
            "Binds to a value set if this element is coded (code, Coding, "
            "CodeableConcept, Quantity), or the data types (string, uri)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    code: typing.List[fhirtypes.CodingType] = Field(
        None,
        alias="code",
        title="Corresponding codes in terminologies",
        description=(
            "A code that has the same meaning as the element in a particular "
            "terminology."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    comment: fhirtypes.Markdown = Field(
        None,
        alias="comment",
        title="Comments about the use of this element",
        description=(
            "Explanatory notes and implementation guidance about the data element, "
            "including notes about how to use the data properly, exceptions to "
            "proper use, etc. (Note: The text you are reading is specified in "
            "ElementDefinition.comment)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    condition: typing.List[typing.Optional[fhirtypes.Id]] = Field(
        None,
        alias="condition",
        title="Reference to invariant about presence",
        description=(
            "A reference to an invariant that may make additional statements about "
            "the cardinality or value in the instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    condition__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_condition", title="Extension field for ``condition``.")

    constraint: typing.List[fhirtypes.ElementDefinitionConstraintType] = Field(
        None,
        alias="constraint",
        title="Condition that must evaluate to true",
        description=(
            "Formal constraints such as co-occurrence and other constraints that "
            "can be computationally evaluated within the context of the instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    contentReference: fhirtypes.Uri = Field(
        None,
        alias="contentReference",
        title="Reference to definition of content for the element",
        description=(
            "Identifies an element defined elsewhere in the definition whose "
            "content rules should be applied to the current element. "
            "ContentReferences bring across all the rules that are in the "
            "ElementDefinition for the element, including definitions, cardinality "
            "constraints, bindings, invariants etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    contentReference__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_contentReference",
        title="Extension field for ``contentReference``.",
    )

    defaultValueAddress: fhirtypes.AddressType = Field(
        None,
        alias="defaultValueAddress",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueAge: fhirtypes.AgeType = Field(
        None,
        alias="defaultValueAge",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueAvailability: fhirtypes.AvailabilityType = Field(
        None,
        alias="defaultValueAvailability",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
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
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )
    defaultValueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValueBoolean",
        title="Extension field for ``defaultValueBoolean``.",
    )

    defaultValueCanonical: fhirtypes.Canonical = Field(
        None,
        alias="defaultValueCanonical",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )
    defaultValueCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValueCanonical",
        title="Extension field for ``defaultValueCanonical``.",
    )

    defaultValueCode: fhirtypes.Code = Field(
        None,
        alias="defaultValueCode",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
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
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueCodeableReference: fhirtypes.CodeableReferenceType = Field(
        None,
        alias="defaultValueCodeableReference",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueContactDetail: fhirtypes.ContactDetailType = Field(
        None,
        alias="defaultValueContactDetail",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueCount: fhirtypes.CountType = Field(
        None,
        alias="defaultValueCount",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueDataRequirement: fhirtypes.DataRequirementType = Field(
        None,
        alias="defaultValueDataRequirement",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
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
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
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
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
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
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueDosage: fhirtypes.DosageType = Field(
        None,
        alias="defaultValueDosage",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueDuration: fhirtypes.DurationType = Field(
        None,
        alias="defaultValueDuration",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueExpression: fhirtypes.ExpressionType = Field(
        None,
        alias="defaultValueExpression",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueExtendedContactDetail: fhirtypes.ExtendedContactDetailType = Field(
        None,
        alias="defaultValueExtendedContactDetail",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )
    defaultValueId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_defaultValueId", title="Extension field for ``defaultValueId``."
    )

    defaultValueIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="defaultValueIdentifier",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
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
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )
    defaultValueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValueInteger",
        title="Extension field for ``defaultValueInteger``.",
    )

    defaultValueInteger64: fhirtypes.Integer64 = Field(
        None,
        alias="defaultValueInteger64",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )
    defaultValueInteger64__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValueInteger64",
        title="Extension field for ``defaultValueInteger64``.",
    )

    defaultValueMarkdown: fhirtypes.Markdown = Field(
        None,
        alias="defaultValueMarkdown",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
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
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueMoney: fhirtypes.MoneyType = Field(
        None,
        alias="defaultValueMoney",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )
    defaultValueOid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_defaultValueOid", title="Extension field for ``defaultValueOid``."
    )

    defaultValueParameterDefinition: fhirtypes.ParameterDefinitionType = Field(
        None,
        alias="defaultValueParameterDefinition",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
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
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueRatioRange: fhirtypes.RatioRangeType = Field(
        None,
        alias="defaultValueRatioRange",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueRelatedArtifact: fhirtypes.RelatedArtifactType = Field(
        None,
        alias="defaultValueRelatedArtifact",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueSampledData: fhirtypes.SampledDataType = Field(
        None,
        alias="defaultValueSampledData",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
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
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
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
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueTriggerDefinition: fhirtypes.TriggerDefinitionType = Field(
        None,
        alias="defaultValueTriggerDefinition",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
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
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )
    defaultValueUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_defaultValueUri", title="Extension field for ``defaultValueUri``."
    )

    defaultValueUrl: fhirtypes.Url = Field(
        None,
        alias="defaultValueUrl",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )
    defaultValueUrl__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_defaultValueUrl", title="Extension field for ``defaultValueUrl``."
    )

    defaultValueUsageContext: fhirtypes.UsageContextType = Field(
        None,
        alias="defaultValueUsageContext",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )

    defaultValueUuid: fhirtypes.Uuid = Field(
        None,
        alias="defaultValueUuid",
        title="Specified value if missing from instance",
        description=(
            "The value that should be used if there is no value stated in the "
            "instance (e.g. 'if not otherwise specified, the abstract is false')."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e defaultValue[x]
        one_of_many="defaultValue",
        one_of_many_required=False,
    )
    defaultValueUuid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_defaultValueUuid",
        title="Extension field for ``defaultValueUuid``.",
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
        # if property is element of this resource.
        element_property=True,
    )
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_definition", title="Extension field for ``definition``."
    )

    example: typing.List[fhirtypes.ElementDefinitionExampleType] = Field(
        None,
        alias="example",
        title="Example value (as defined for type)",
        description=(
            "A sample value for this element demonstrating the type of information "
            "that would typically be found in the element."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    fixedAddress: fhirtypes.AddressType = Field(
        None,
        alias="fixedAddress",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedAge: fhirtypes.AgeType = Field(
        None,
        alias="fixedAge",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
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
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
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
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedAvailability: fhirtypes.AvailabilityType = Field(
        None,
        alias="fixedAvailability",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
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
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
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
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )
    fixedBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fixedBoolean", title="Extension field for ``fixedBoolean``."
    )

    fixedCanonical: fhirtypes.Canonical = Field(
        None,
        alias="fixedCanonical",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )
    fixedCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fixedCanonical", title="Extension field for ``fixedCanonical``."
    )

    fixedCode: fhirtypes.Code = Field(
        None,
        alias="fixedCode",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )
    fixedCode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fixedCode", title="Extension field for ``fixedCode``."
    )

    fixedCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="fixedCodeableConcept",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedCodeableReference: fhirtypes.CodeableReferenceType = Field(
        None,
        alias="fixedCodeableReference",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
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
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedContactDetail: fhirtypes.ContactDetailType = Field(
        None,
        alias="fixedContactDetail",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
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
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedCount: fhirtypes.CountType = Field(
        None,
        alias="fixedCount",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedDataRequirement: fhirtypes.DataRequirementType = Field(
        None,
        alias="fixedDataRequirement",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
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
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )
    fixedDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fixedDate", title="Extension field for ``fixedDate``."
    )

    fixedDateTime: fhirtypes.DateTime = Field(
        None,
        alias="fixedDateTime",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )
    fixedDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fixedDateTime", title="Extension field for ``fixedDateTime``."
    )

    fixedDecimal: fhirtypes.Decimal = Field(
        None,
        alias="fixedDecimal",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )
    fixedDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fixedDecimal", title="Extension field for ``fixedDecimal``."
    )

    fixedDistance: fhirtypes.DistanceType = Field(
        None,
        alias="fixedDistance",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedDosage: fhirtypes.DosageType = Field(
        None,
        alias="fixedDosage",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedDuration: fhirtypes.DurationType = Field(
        None,
        alias="fixedDuration",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedExpression: fhirtypes.ExpressionType = Field(
        None,
        alias="fixedExpression",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedExtendedContactDetail: fhirtypes.ExtendedContactDetailType = Field(
        None,
        alias="fixedExtendedContactDetail",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
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
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
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
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )
    fixedId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fixedId", title="Extension field for ``fixedId``."
    )

    fixedIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="fixedIdentifier",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
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
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )
    fixedInstant__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fixedInstant", title="Extension field for ``fixedInstant``."
    )

    fixedInteger: fhirtypes.Integer = Field(
        None,
        alias="fixedInteger",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )
    fixedInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fixedInteger", title="Extension field for ``fixedInteger``."
    )

    fixedInteger64: fhirtypes.Integer64 = Field(
        None,
        alias="fixedInteger64",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )
    fixedInteger64__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fixedInteger64", title="Extension field for ``fixedInteger64``."
    )

    fixedMarkdown: fhirtypes.Markdown = Field(
        None,
        alias="fixedMarkdown",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )
    fixedMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fixedMarkdown", title="Extension field for ``fixedMarkdown``."
    )

    fixedMeta: fhirtypes.MetaType = Field(
        None,
        alias="fixedMeta",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedMoney: fhirtypes.MoneyType = Field(
        None,
        alias="fixedMoney",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
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
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )
    fixedOid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fixedOid", title="Extension field for ``fixedOid``."
    )

    fixedParameterDefinition: fhirtypes.ParameterDefinitionType = Field(
        None,
        alias="fixedParameterDefinition",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
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
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
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
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
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
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
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
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
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
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedRatioRange: fhirtypes.RatioRangeType = Field(
        None,
        alias="fixedRatioRange",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
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
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedRelatedArtifact: fhirtypes.RelatedArtifactType = Field(
        None,
        alias="fixedRelatedArtifact",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedSampledData: fhirtypes.SampledDataType = Field(
        None,
        alias="fixedSampledData",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
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
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
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
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )
    fixedString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fixedString", title="Extension field for ``fixedString``."
    )

    fixedTime: fhirtypes.Time = Field(
        None,
        alias="fixedTime",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )
    fixedTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fixedTime", title="Extension field for ``fixedTime``."
    )

    fixedTiming: fhirtypes.TimingType = Field(
        None,
        alias="fixedTiming",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedTriggerDefinition: fhirtypes.TriggerDefinitionType = Field(
        None,
        alias="fixedTriggerDefinition",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
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
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
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
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )
    fixedUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fixedUri", title="Extension field for ``fixedUri``."
    )

    fixedUrl: fhirtypes.Url = Field(
        None,
        alias="fixedUrl",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )
    fixedUrl__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fixedUrl", title="Extension field for ``fixedUrl``."
    )

    fixedUsageContext: fhirtypes.UsageContextType = Field(
        None,
        alias="fixedUsageContext",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )

    fixedUuid: fhirtypes.Uuid = Field(
        None,
        alias="fixedUuid",
        title="Value must be exactly this",
        description=(
            "Specifies a value that SHALL be exactly the value  for this element in"
            " the instance, if present. For purposes of comparison, non-significant"
            " whitespace is ignored, and all values must be an exact match (case "
            "and accent sensitive). Missing elements/attributes must also be "
            "missing."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fixed[x]
        one_of_many="fixed",
        one_of_many_required=False,
    )
    fixedUuid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fixedUuid", title="Extension field for ``fixedUuid``."
    )

    isModifier: bool = Field(
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
            "relevant to their particular system. When used on the root element in "
            "an extension definition, this indicates whether or not the extension "
            "is a modifier extension."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    isModifier__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_isModifier", title="Extension field for ``isModifier``."
    )

    isModifierReason: fhirtypes.String = Field(
        None,
        alias="isModifierReason",
        title="Reason that this element is marked as a modifier",
        description=(
            "Explains how that element affects the interpretation of the resource "
            "or element that contains it."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    isModifierReason__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_isModifierReason",
        title="Extension field for ``isModifierReason``.",
    )

    isSummary: bool = Field(
        None,
        alias="isSummary",
        title="Include when _summary = true?",
        description=(
            "Whether the element should be included if a client requests a search "
            "with the parameter _summary=true."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    isSummary__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_isSummary", title="Extension field for ``isSummary``."
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
        # if property is element of this resource.
        element_property=True,
    )
    label__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_label", title="Extension field for ``label``."
    )

    mapping: typing.List[fhirtypes.ElementDefinitionMappingType] = Field(
        None,
        alias="mapping",
        title="Map element to another set of definitions",
        description=(
            "Identifies a concept from an external specification that roughly "
            "corresponds to this element."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    max: fhirtypes.String = Field(
        None,
        alias="max",
        title="Maximum Cardinality (a number or *)",
        description=(
            "The maximum number of times this element is permitted to appear in the"
            " instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    max__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_max", title="Extension field for ``max``."
    )

    maxLength: fhirtypes.Integer = Field(
        None,
        alias="maxLength",
        title="Max length for string type data",
        description=(
            "Indicates the maximum length in characters that is permitted to be "
            "present in conformant instances and which is expected to be supported "
            "by conformant consumers that support the element. ```maxLength``` "
            "SHOULD only be used on primitive data types that have a string "
            "representation (see "
            "[http://hl7.org/fhir/StructureDefinition/structuredefinition-type-"
            "characteristics](http://hl7.org/fhir/extensions/StructureDefinition-"
            "structuredefinition-type-characteristics.html))."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    maxLength__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_maxLength", title="Extension field for ``maxLength``."
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e maxValue[x]
        one_of_many="maxValue",
        one_of_many_required=False,
    )
    maxValueDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_maxValueDate", title="Extension field for ``maxValueDate``."
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e maxValue[x]
        one_of_many="maxValue",
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
        title="Maximum Allowed Value (for some types)",
        description=(
            "The maximum allowed value for the element. The value is inclusive. "
            "This is allowed for the types date, dateTime, instant, time, decimal, "
            "integer, and Quantity."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e maxValue[x]
        one_of_many="maxValue",
        one_of_many_required=False,
    )
    maxValueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_maxValueDecimal", title="Extension field for ``maxValueDecimal``."
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e maxValue[x]
        one_of_many="maxValue",
        one_of_many_required=False,
    )
    maxValueInstant__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_maxValueInstant", title="Extension field for ``maxValueInstant``."
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e maxValue[x]
        one_of_many="maxValue",
        one_of_many_required=False,
    )
    maxValueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_maxValueInteger", title="Extension field for ``maxValueInteger``."
    )

    maxValueInteger64: fhirtypes.Integer64 = Field(
        None,
        alias="maxValueInteger64",
        title="Maximum Allowed Value (for some types)",
        description=(
            "The maximum allowed value for the element. The value is inclusive. "
            "This is allowed for the types date, dateTime, instant, time, decimal, "
            "integer, and Quantity."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e maxValue[x]
        one_of_many="maxValue",
        one_of_many_required=False,
    )
    maxValueInteger64__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_maxValueInteger64",
        title="Extension field for ``maxValueInteger64``.",
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e maxValue[x]
        one_of_many="maxValue",
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
        title="Maximum Allowed Value (for some types)",
        description=(
            "The maximum allowed value for the element. The value is inclusive. "
            "This is allowed for the types date, dateTime, instant, time, decimal, "
            "integer, and Quantity."
        ),
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e maxValue[x]
        one_of_many="maxValue",
        one_of_many_required=False,
    )
    maxValueTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_maxValueTime", title="Extension field for ``maxValueTime``."
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e maxValue[x]
        one_of_many="maxValue",
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
        title="Implicit meaning when this element is missing",
        description=(
            "The Implicit meaning that is to be understood when this element is "
            "missing (e.g. 'when this element is missing, the period is ongoing')."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    meaningWhenMissing__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_meaningWhenMissing",
        title="Extension field for ``meaningWhenMissing``.",
    )

    min: fhirtypes.UnsignedInt = Field(
        None,
        alias="min",
        title="Minimum Cardinality",
        description="The minimum number of times this element SHALL appear in the instance.",
        # if property is element of this resource.
        element_property=True,
    )
    min__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_min", title="Extension field for ``min``."
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e minValue[x]
        one_of_many="minValue",
        one_of_many_required=False,
    )
    minValueDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_minValueDate", title="Extension field for ``minValueDate``."
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e minValue[x]
        one_of_many="minValue",
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
        title="Minimum Allowed Value (for some types)",
        description=(
            "The minimum allowed value for the element. The value is inclusive. "
            "This is allowed for the types date, dateTime, instant, time, decimal, "
            "integer, and Quantity."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e minValue[x]
        one_of_many="minValue",
        one_of_many_required=False,
    )
    minValueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_minValueDecimal", title="Extension field for ``minValueDecimal``."
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e minValue[x]
        one_of_many="minValue",
        one_of_many_required=False,
    )
    minValueInstant__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_minValueInstant", title="Extension field for ``minValueInstant``."
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e minValue[x]
        one_of_many="minValue",
        one_of_many_required=False,
    )
    minValueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_minValueInteger", title="Extension field for ``minValueInteger``."
    )

    minValueInteger64: fhirtypes.Integer64 = Field(
        None,
        alias="minValueInteger64",
        title="Minimum Allowed Value (for some types)",
        description=(
            "The minimum allowed value for the element. The value is inclusive. "
            "This is allowed for the types date, dateTime, instant, time, decimal, "
            "integer, and Quantity."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e minValue[x]
        one_of_many="minValue",
        one_of_many_required=False,
    )
    minValueInteger64__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_minValueInteger64",
        title="Extension field for ``minValueInteger64``.",
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e minValue[x]
        one_of_many="minValue",
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
        title="Minimum Allowed Value (for some types)",
        description=(
            "The minimum allowed value for the element. The value is inclusive. "
            "This is allowed for the types date, dateTime, instant, time, decimal, "
            "integer, and Quantity."
        ),
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e minValue[x]
        one_of_many="minValue",
        one_of_many_required=False,
    )
    minValueTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_minValueTime", title="Extension field for ``minValueTime``."
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e minValue[x]
        one_of_many="minValue",
        one_of_many_required=False,
    )
    minValueUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_minValueUnsignedInt",
        title="Extension field for ``minValueUnsignedInt``.",
    )

    mustHaveValue: bool = Field(
        None,
        alias="mustHaveValue",
        title=(
            "For primitives, that a value must be present - not replaced by an "
            "extension"
        ),
        description=(
            "Specifies for a primitive data type that the value of the data type "
            "cannot be replaced by an extension."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    mustHaveValue__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_mustHaveValue", title="Extension field for ``mustHaveValue``."
    )

    mustSupport: bool = Field(
        None,
        alias="mustSupport",
        title="If the element must be supported (discouraged - see obligations)",
        description=(
            "If true, implementations that produce or consume resources SHALL "
            'provide "support" for the element in some meaningful way. Note that '
            "this is being phased out and replaced by obligations (see below).  If "
            "false, the element may be ignored and not supported. If false, whether"
            " to populate or use the data element in any way is at the discretion "
            "of the implementation."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    mustSupport__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_mustSupport", title="Extension field for ``mustSupport``."
    )

    orderMeaning: fhirtypes.String = Field(
        None,
        alias="orderMeaning",
        title="What the order of the elements means",
        description=(
            "If present, indicates that the order of the repeating element has "
            "meaning and describes what that meaning is.  If absent, it means that "
            "the order of the element has no meaning."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    orderMeaning__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_orderMeaning", title="Extension field for ``orderMeaning``."
    )

    path: fhirtypes.String = Field(
        None,
        alias="path",
        title="Path of the element in the hierarchy of elements",
        description=(
            'The path identifies the element and is expressed as a "."-separated '
            "list of ancestor elements, beginning with the name of the resource or "
            "extension."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_path", title="Extension field for ``path``."
    )

    patternAddress: fhirtypes.AddressType = Field(
        None,
        alias="patternAddress",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternAge: fhirtypes.AgeType = Field(
        None,
        alias="patternAge",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternAnnotation: fhirtypes.AnnotationType = Field(
        None,
        alias="patternAnnotation",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="patternAttachment",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternAvailability: fhirtypes.AvailabilityType = Field(
        None,
        alias="patternAvailability",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternBase64Binary: fhirtypes.Base64Binary = Field(
        None,
        alias="patternBase64Binary",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
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
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )
    patternBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_patternBoolean", title="Extension field for ``patternBoolean``."
    )

    patternCanonical: fhirtypes.Canonical = Field(
        None,
        alias="patternCanonical",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )
    patternCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_patternCanonical",
        title="Extension field for ``patternCanonical``.",
    )

    patternCode: fhirtypes.Code = Field(
        None,
        alias="patternCode",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )
    patternCode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_patternCode", title="Extension field for ``patternCode``."
    )

    patternCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="patternCodeableConcept",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternCodeableReference: fhirtypes.CodeableReferenceType = Field(
        None,
        alias="patternCodeableReference",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternCoding: fhirtypes.CodingType = Field(
        None,
        alias="patternCoding",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternContactDetail: fhirtypes.ContactDetailType = Field(
        None,
        alias="patternContactDetail",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternContactPoint: fhirtypes.ContactPointType = Field(
        None,
        alias="patternContactPoint",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternCount: fhirtypes.CountType = Field(
        None,
        alias="patternCount",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternDataRequirement: fhirtypes.DataRequirementType = Field(
        None,
        alias="patternDataRequirement",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternDate: fhirtypes.Date = Field(
        None,
        alias="patternDate",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )
    patternDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_patternDate", title="Extension field for ``patternDate``."
    )

    patternDateTime: fhirtypes.DateTime = Field(
        None,
        alias="patternDateTime",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )
    patternDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_patternDateTime", title="Extension field for ``patternDateTime``."
    )

    patternDecimal: fhirtypes.Decimal = Field(
        None,
        alias="patternDecimal",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )
    patternDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_patternDecimal", title="Extension field for ``patternDecimal``."
    )

    patternDistance: fhirtypes.DistanceType = Field(
        None,
        alias="patternDistance",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternDosage: fhirtypes.DosageType = Field(
        None,
        alias="patternDosage",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternDuration: fhirtypes.DurationType = Field(
        None,
        alias="patternDuration",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternExpression: fhirtypes.ExpressionType = Field(
        None,
        alias="patternExpression",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternExtendedContactDetail: fhirtypes.ExtendedContactDetailType = Field(
        None,
        alias="patternExtendedContactDetail",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternHumanName: fhirtypes.HumanNameType = Field(
        None,
        alias="patternHumanName",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternId: fhirtypes.Id = Field(
        None,
        alias="patternId",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )
    patternId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_patternId", title="Extension field for ``patternId``."
    )

    patternIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="patternIdentifier",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternInstant: fhirtypes.Instant = Field(
        None,
        alias="patternInstant",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )
    patternInstant__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_patternInstant", title="Extension field for ``patternInstant``."
    )

    patternInteger: fhirtypes.Integer = Field(
        None,
        alias="patternInteger",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )
    patternInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_patternInteger", title="Extension field for ``patternInteger``."
    )

    patternInteger64: fhirtypes.Integer64 = Field(
        None,
        alias="patternInteger64",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )
    patternInteger64__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_patternInteger64",
        title="Extension field for ``patternInteger64``.",
    )

    patternMarkdown: fhirtypes.Markdown = Field(
        None,
        alias="patternMarkdown",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )
    patternMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_patternMarkdown", title="Extension field for ``patternMarkdown``."
    )

    patternMeta: fhirtypes.MetaType = Field(
        None,
        alias="patternMeta",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternMoney: fhirtypes.MoneyType = Field(
        None,
        alias="patternMoney",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternOid: fhirtypes.Oid = Field(
        None,
        alias="patternOid",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )
    patternOid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_patternOid", title="Extension field for ``patternOid``."
    )

    patternParameterDefinition: fhirtypes.ParameterDefinitionType = Field(
        None,
        alias="patternParameterDefinition",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="patternPeriod",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternPositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="patternPositiveInt",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
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
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternRange: fhirtypes.RangeType = Field(
        None,
        alias="patternRange",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternRatio: fhirtypes.RatioType = Field(
        None,
        alias="patternRatio",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternRatioRange: fhirtypes.RatioRangeType = Field(
        None,
        alias="patternRatioRange",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternReference: fhirtypes.ReferenceType = Field(
        None,
        alias="patternReference",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternRelatedArtifact: fhirtypes.RelatedArtifactType = Field(
        None,
        alias="patternRelatedArtifact",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternSampledData: fhirtypes.SampledDataType = Field(
        None,
        alias="patternSampledData",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternSignature: fhirtypes.SignatureType = Field(
        None,
        alias="patternSignature",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternString: fhirtypes.String = Field(
        None,
        alias="patternString",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )
    patternString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_patternString", title="Extension field for ``patternString``."
    )

    patternTime: fhirtypes.Time = Field(
        None,
        alias="patternTime",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )
    patternTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_patternTime", title="Extension field for ``patternTime``."
    )

    patternTiming: fhirtypes.TimingType = Field(
        None,
        alias="patternTiming",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternTriggerDefinition: fhirtypes.TriggerDefinitionType = Field(
        None,
        alias="patternTriggerDefinition",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="patternUnsignedInt",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
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
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )
    patternUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_patternUri", title="Extension field for ``patternUri``."
    )

    patternUrl: fhirtypes.Url = Field(
        None,
        alias="patternUrl",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )
    patternUrl__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_patternUrl", title="Extension field for ``patternUrl``."
    )

    patternUsageContext: fhirtypes.UsageContextType = Field(
        None,
        alias="patternUsageContext",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )

    patternUuid: fhirtypes.Uuid = Field(
        None,
        alias="patternUuid",
        title="Value must have at least these property values",
        description=(
            "Specifies a value that each occurrence of the element in the instance "
            "SHALL follow - that is, any value in the pattern must be found in the "
            "instance, if the element has a value. Other additional values may be "
            "found too. This is effectively constraint by example.    When "
            "pattern[x] is used to constrain a primitive, it means that the value "
            "provided in the pattern[x] must match the instance value exactly.  "
            "When an element within a pattern[x] is used to constrain an array, it "
            "means that each element provided in the pattern[x] must (recursively) "
            "match at least one element from the instance array.  When pattern[x] "
            "is used to constrain a complex object, it means that each property in "
            "the pattern must be present in the complex object, and its value must "
            "recursively match -- i.e.,  1. If primitive: it must match exactly the"
            " pattern value 2. If a complex object: it must match (recursively) the"
            " pattern value 3. If an array: it must match (recursively) the pattern"
            " value  If a pattern[x] is declared on a repeating element, the "
            "pattern applies to all repetitions.  If the desire is for a pattern to"
            " apply to only one element or a subset of elements, slicing must be "
            "used. See [Examples of Patterns](elementdefinition-"
            "examples.html#pattern-examples) for examples of pattern usage and the "
            "effect it will have."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e pattern[x]
        one_of_many="pattern",
        one_of_many_required=False,
    )
    patternUuid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_patternUuid", title="Extension field for ``patternUuid``."
    )

    representation: typing.List[typing.Optional[fhirtypes.Code]] = Field(
        None,
        alias="representation",
        title="xmlAttr | xmlText | typeAttr | cdaText | xhtml",
        description=(
            "Codes that define how this element is represented in instances, when "
            "the deviation varies from the normal case. No extensions are allowed "
            "on elements with a representation of 'xmlAttr', no matter what FHIR "
            "serialization format is used."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["xmlAttr", "xmlText", "typeAttr", "cdaText", "xhtml"],
    )
    representation__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_representation", title="Extension field for ``representation``."
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
        # if property is element of this resource.
        element_property=True,
    )
    requirements__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_requirements", title="Extension field for ``requirements``."
    )

    short: fhirtypes.String = Field(
        None,
        alias="short",
        title="Concise definition for space-constrained presentation",
        description=(
            "A concise description of what this element means (e.g. for use in "
            "autogenerated summaries)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    short__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_short", title="Extension field for ``short``."
    )

    sliceIsConstraining: bool = Field(
        None,
        alias="sliceIsConstraining",
        title=(
            "If this slice definition constrains an inherited slice definition (or "
            "not)"
        ),
        description=(
            "If true, indicates that this slice definition is constraining a slice "
            "definition with the same name in an inherited profile. If false, the "
            "slice is not overriding any slice in an inherited profile. If missing,"
            " the slice might or might not be overriding a slice in an inherited "
            "profile, depending on the sliceName."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    sliceIsConstraining__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_sliceIsConstraining",
        title="Extension field for ``sliceIsConstraining``.",
    )

    sliceName: fhirtypes.String = Field(
        None,
        alias="sliceName",
        title="Name for this particular element (in a set of slices)",
        description=(
            "The name of this element definition slice, when slicing is working. "
            "The name must be a token with no dots or spaces. This is a unique name"
            " referring to a specific set of constraints applied to this element, "
            "used to provide a name to different slices of the same element."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    sliceName__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sliceName", title="Extension field for ``sliceName``."
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
        # if property is element of this resource.
        element_property=True,
    )

    type: typing.List[fhirtypes.ElementDefinitionTypeType] = Field(
        None,
        alias="type",
        title="Data type and Profile for this element",
        description=(
            "The data type or resource that the value of this element is permitted "
            "to be."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    valueAlternatives: typing.List[typing.Optional[fhirtypes.Canonical]] = Field(
        None,
        alias="valueAlternatives",
        title="Extensions that are allowed to replace a primitive value",
        description=(
            "Specifies a list of extensions that can appear in place of a primitive"
            " value."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureDefinition"],
    )
    valueAlternatives__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_valueAlternatives",
        title="Extension field for ``valueAlternatives``.",
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ElementDefinition`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "path",
            "representation",
            "sliceName",
            "sliceIsConstraining",
            "label",
            "code",
            "slicing",
            "short",
            "definition",
            "comment",
            "requirements",
            "alias",
            "min",
            "max",
            "base",
            "contentReference",
            "type",
            "defaultValueBase64Binary",
            "defaultValueBoolean",
            "defaultValueCanonical",
            "defaultValueCode",
            "defaultValueDate",
            "defaultValueDateTime",
            "defaultValueDecimal",
            "defaultValueId",
            "defaultValueInstant",
            "defaultValueInteger",
            "defaultValueInteger64",
            "defaultValueMarkdown",
            "defaultValueOid",
            "defaultValuePositiveInt",
            "defaultValueString",
            "defaultValueTime",
            "defaultValueUnsignedInt",
            "defaultValueUri",
            "defaultValueUrl",
            "defaultValueUuid",
            "defaultValueAddress",
            "defaultValueAge",
            "defaultValueAnnotation",
            "defaultValueAttachment",
            "defaultValueCodeableConcept",
            "defaultValueCodeableReference",
            "defaultValueCoding",
            "defaultValueContactPoint",
            "defaultValueCount",
            "defaultValueDistance",
            "defaultValueDuration",
            "defaultValueHumanName",
            "defaultValueIdentifier",
            "defaultValueMoney",
            "defaultValuePeriod",
            "defaultValueQuantity",
            "defaultValueRange",
            "defaultValueRatio",
            "defaultValueRatioRange",
            "defaultValueReference",
            "defaultValueSampledData",
            "defaultValueSignature",
            "defaultValueTiming",
            "defaultValueContactDetail",
            "defaultValueDataRequirement",
            "defaultValueExpression",
            "defaultValueParameterDefinition",
            "defaultValueRelatedArtifact",
            "defaultValueTriggerDefinition",
            "defaultValueUsageContext",
            "defaultValueAvailability",
            "defaultValueExtendedContactDetail",
            "defaultValueDosage",
            "defaultValueMeta",
            "meaningWhenMissing",
            "orderMeaning",
            "fixedBase64Binary",
            "fixedBoolean",
            "fixedCanonical",
            "fixedCode",
            "fixedDate",
            "fixedDateTime",
            "fixedDecimal",
            "fixedId",
            "fixedInstant",
            "fixedInteger",
            "fixedInteger64",
            "fixedMarkdown",
            "fixedOid",
            "fixedPositiveInt",
            "fixedString",
            "fixedTime",
            "fixedUnsignedInt",
            "fixedUri",
            "fixedUrl",
            "fixedUuid",
            "fixedAddress",
            "fixedAge",
            "fixedAnnotation",
            "fixedAttachment",
            "fixedCodeableConcept",
            "fixedCodeableReference",
            "fixedCoding",
            "fixedContactPoint",
            "fixedCount",
            "fixedDistance",
            "fixedDuration",
            "fixedHumanName",
            "fixedIdentifier",
            "fixedMoney",
            "fixedPeriod",
            "fixedQuantity",
            "fixedRange",
            "fixedRatio",
            "fixedRatioRange",
            "fixedReference",
            "fixedSampledData",
            "fixedSignature",
            "fixedTiming",
            "fixedContactDetail",
            "fixedDataRequirement",
            "fixedExpression",
            "fixedParameterDefinition",
            "fixedRelatedArtifact",
            "fixedTriggerDefinition",
            "fixedUsageContext",
            "fixedAvailability",
            "fixedExtendedContactDetail",
            "fixedDosage",
            "fixedMeta",
            "patternBase64Binary",
            "patternBoolean",
            "patternCanonical",
            "patternCode",
            "patternDate",
            "patternDateTime",
            "patternDecimal",
            "patternId",
            "patternInstant",
            "patternInteger",
            "patternInteger64",
            "patternMarkdown",
            "patternOid",
            "patternPositiveInt",
            "patternString",
            "patternTime",
            "patternUnsignedInt",
            "patternUri",
            "patternUrl",
            "patternUuid",
            "patternAddress",
            "patternAge",
            "patternAnnotation",
            "patternAttachment",
            "patternCodeableConcept",
            "patternCodeableReference",
            "patternCoding",
            "patternContactPoint",
            "patternCount",
            "patternDistance",
            "patternDuration",
            "patternHumanName",
            "patternIdentifier",
            "patternMoney",
            "patternPeriod",
            "patternQuantity",
            "patternRange",
            "patternRatio",
            "patternRatioRange",
            "patternReference",
            "patternSampledData",
            "patternSignature",
            "patternTiming",
            "patternContactDetail",
            "patternDataRequirement",
            "patternExpression",
            "patternParameterDefinition",
            "patternRelatedArtifact",
            "patternTriggerDefinition",
            "patternUsageContext",
            "patternAvailability",
            "patternExtendedContactDetail",
            "patternDosage",
            "patternMeta",
            "example",
            "minValueDate",
            "minValueDateTime",
            "minValueInstant",
            "minValueTime",
            "minValueDecimal",
            "minValueInteger",
            "minValueInteger64",
            "minValuePositiveInt",
            "minValueUnsignedInt",
            "minValueQuantity",
            "maxValueDate",
            "maxValueDateTime",
            "maxValueInstant",
            "maxValueTime",
            "maxValueDecimal",
            "maxValueInteger",
            "maxValueInteger64",
            "maxValuePositiveInt",
            "maxValueUnsignedInt",
            "maxValueQuantity",
            "maxLength",
            "condition",
            "constraint",
            "mustHaveValue",
            "valueAlternatives",
            "mustSupport",
            "isModifier",
            "isModifierReason",
            "isSummary",
            "binding",
            "mapping",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1926(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("path", "path__ext")]
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
    def validate_one_of_many_1926(
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
            "defaultValue": [
                "defaultValueAddress",
                "defaultValueAge",
                "defaultValueAnnotation",
                "defaultValueAttachment",
                "defaultValueAvailability",
                "defaultValueBase64Binary",
                "defaultValueBoolean",
                "defaultValueCanonical",
                "defaultValueCode",
                "defaultValueCodeableConcept",
                "defaultValueCodeableReference",
                "defaultValueCoding",
                "defaultValueContactDetail",
                "defaultValueContactPoint",
                "defaultValueCount",
                "defaultValueDataRequirement",
                "defaultValueDate",
                "defaultValueDateTime",
                "defaultValueDecimal",
                "defaultValueDistance",
                "defaultValueDosage",
                "defaultValueDuration",
                "defaultValueExpression",
                "defaultValueExtendedContactDetail",
                "defaultValueHumanName",
                "defaultValueId",
                "defaultValueIdentifier",
                "defaultValueInstant",
                "defaultValueInteger",
                "defaultValueInteger64",
                "defaultValueMarkdown",
                "defaultValueMeta",
                "defaultValueMoney",
                "defaultValueOid",
                "defaultValueParameterDefinition",
                "defaultValuePeriod",
                "defaultValuePositiveInt",
                "defaultValueQuantity",
                "defaultValueRange",
                "defaultValueRatio",
                "defaultValueRatioRange",
                "defaultValueReference",
                "defaultValueRelatedArtifact",
                "defaultValueSampledData",
                "defaultValueSignature",
                "defaultValueString",
                "defaultValueTime",
                "defaultValueTiming",
                "defaultValueTriggerDefinition",
                "defaultValueUnsignedInt",
                "defaultValueUri",
                "defaultValueUrl",
                "defaultValueUsageContext",
                "defaultValueUuid",
            ],
            "fixed": [
                "fixedAddress",
                "fixedAge",
                "fixedAnnotation",
                "fixedAttachment",
                "fixedAvailability",
                "fixedBase64Binary",
                "fixedBoolean",
                "fixedCanonical",
                "fixedCode",
                "fixedCodeableConcept",
                "fixedCodeableReference",
                "fixedCoding",
                "fixedContactDetail",
                "fixedContactPoint",
                "fixedCount",
                "fixedDataRequirement",
                "fixedDate",
                "fixedDateTime",
                "fixedDecimal",
                "fixedDistance",
                "fixedDosage",
                "fixedDuration",
                "fixedExpression",
                "fixedExtendedContactDetail",
                "fixedHumanName",
                "fixedId",
                "fixedIdentifier",
                "fixedInstant",
                "fixedInteger",
                "fixedInteger64",
                "fixedMarkdown",
                "fixedMeta",
                "fixedMoney",
                "fixedOid",
                "fixedParameterDefinition",
                "fixedPeriod",
                "fixedPositiveInt",
                "fixedQuantity",
                "fixedRange",
                "fixedRatio",
                "fixedRatioRange",
                "fixedReference",
                "fixedRelatedArtifact",
                "fixedSampledData",
                "fixedSignature",
                "fixedString",
                "fixedTime",
                "fixedTiming",
                "fixedTriggerDefinition",
                "fixedUnsignedInt",
                "fixedUri",
                "fixedUrl",
                "fixedUsageContext",
                "fixedUuid",
            ],
            "maxValue": [
                "maxValueDate",
                "maxValueDateTime",
                "maxValueDecimal",
                "maxValueInstant",
                "maxValueInteger",
                "maxValueInteger64",
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
                "minValueInteger64",
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
                "patternAvailability",
                "patternBase64Binary",
                "patternBoolean",
                "patternCanonical",
                "patternCode",
                "patternCodeableConcept",
                "patternCodeableReference",
                "patternCoding",
                "patternContactDetail",
                "patternContactPoint",
                "patternCount",
                "patternDataRequirement",
                "patternDate",
                "patternDateTime",
                "patternDecimal",
                "patternDistance",
                "patternDosage",
                "patternDuration",
                "patternExpression",
                "patternExtendedContactDetail",
                "patternHumanName",
                "patternId",
                "patternIdentifier",
                "patternInstant",
                "patternInteger",
                "patternInteger64",
                "patternMarkdown",
                "patternMeta",
                "patternMoney",
                "patternOid",
                "patternParameterDefinition",
                "patternPeriod",
                "patternPositiveInt",
                "patternQuantity",
                "patternRange",
                "patternRatio",
                "patternRatioRange",
                "patternReference",
                "patternRelatedArtifact",
                "patternSampledData",
                "patternSignature",
                "patternString",
                "patternTime",
                "patternTiming",
                "patternTriggerDefinition",
                "patternUnsignedInt",
                "patternUri",
                "patternUrl",
                "patternUsageContext",
                "patternUuid",
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
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Base definition information for tools.
    Information about the base definition of the element, provided to make it
    unnecessary for tools to trace the deviation of the element through the
    derived and related profiles. When the element definition is not the
    original definition of an element - e.g. either in a constraint on another
    type, or for elements from a super type in a snap shot - then the
    information in provided in the element definition may be different to the
    base definition. On the original definition of the element, it will be
    same.
    """

    resource_type = Field("ElementDefinitionBase", const=True)

    max: fhirtypes.String = Field(
        None,
        alias="max",
        title="Max cardinality of the base element",
        description="Maximum cardinality of the base element identified by the path.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    max__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_max", title="Extension field for ``max``."
    )

    min: fhirtypes.UnsignedInt = Field(
        None,
        alias="min",
        title="Min cardinality of the base element",
        description="Minimum cardinality of the base element identified by the path.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    min__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_min", title="Extension field for ``min``."
    )

    path: fhirtypes.String = Field(
        None,
        alias="path",
        title="Path that identifies the base element",
        description=(
            "The Path that identifies the base element - this matches the "
            "ElementDefinition.path for that element. Across FHIR, there is only "
            "one base definition of any element - that is, an element definition on"
            " a [StructureDefinition](structuredefinition.html#) without a "
            "StructureDefinition.base."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_path", title="Extension field for ``path``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ElementDefinitionBase`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "path", "min", "max"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2296(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("max", "max__ext"),
            ("min", "min__ext"),
            ("path", "path__ext"),
        ]
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


class ElementDefinitionBinding(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    ValueSet details if this is coded.
    Binds to a value set if this element is coded (code, Coding,
    CodeableConcept, Quantity), or the data types (string, uri).
    """

    resource_type = Field("ElementDefinitionBinding", const=True)

    additional: typing.List[fhirtypes.ElementDefinitionBindingAdditionalType] = Field(
        None,
        alias="additional",
        title="Additional Bindings - more rules about the binding",
        description=(
            "Additional bindings that help applications implementing this element. "
            "Additional bindings do not replace the main binding but provide more "
            "information and/or context."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Intended use of codes in the bound value set",
        description="Describes the intended use of this particular set of codes.",
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    strength: fhirtypes.Code = Field(
        None,
        alias="strength",
        title="required | extensible | preferred | example",
        description=(
            "Indicates the degree of conformance expectations associated with this "
            "binding - that is, the degree to which the provided value set must be "
            "adhered to in the instances."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["required", "extensible", "preferred", "example"],
    )
    strength__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_strength", title="Extension field for ``strength``."
    )

    valueSet: fhirtypes.Canonical = Field(
        None,
        alias="valueSet",
        title="Source of value set",
        description=(
            "Refers to the value set that identifies the set of codes the binding "
            "refers to."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ValueSet"],
    )
    valueSet__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueSet", title="Extension field for ``valueSet``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ElementDefinitionBinding`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "strength", "description", "valueSet", "additional"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2618(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("strength", "strength__ext")]
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


class ElementDefinitionBindingAdditional(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional Bindings - more rules about the binding.
    Additional bindings that help applications implementing this element.
    Additional bindings do not replace the main binding but provide more
    information and/or context.
    """

    resource_type = Field("ElementDefinitionBindingAdditional", const=True)

    any: bool = Field(
        None,
        alias="any",
        title="Whether binding can applies to all repeats, or just one",
        description=(
            "Whether the binding applies to all repeats, or just to any one of "
            "them. This is only relevant for elements that can repeat."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    any__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_any", title="Extension field for ``any``."
    )

    documentation: fhirtypes.Markdown = Field(
        None,
        alias="documentation",
        title="Documentation of the purpose of use of the binding",
        description=(
            "Documentation of the purpose of use of the bindingproviding additional"
            " information about how it is intended to be used."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    purpose: fhirtypes.Code = Field(
        None,
        alias="purpose",
        title=(
            "maximum | minimum | required | extensible | candidate | current | "
            "preferred | ui | starter | component"
        ),
        description="The use of this additional binding.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "maximum",
            "minimum",
            "required",
            "extensible",
            "candidate",
            "current",
            "preferred",
            "ui",
            "starter",
            "component",
        ],
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    shortDoco: fhirtypes.String = Field(
        None,
        alias="shortDoco",
        title="Concise documentation - for summary tables",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    shortDoco__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_shortDoco", title="Extension field for ``shortDoco``."
    )

    usage: typing.List[fhirtypes.UsageContextType] = Field(
        None,
        alias="usage",
        title="Qualifies the usage - jurisdiction, gender, workflow status etc.",
        description=(
            "Qualifies the usage of the binding. Typically bindings are qualified "
            "by jurisdiction, but they may also be qualified by gender, workflow "
            "status, clinical domain etc. The information to decide whether a usege"
            " context applies is usually outside the resource, determined by "
            "context, and this might present challenges for validation tooling."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    valueSet: fhirtypes.Canonical = Field(
        None,
        alias="valueSet",
        title="The value set for the additional binding",
        description="The valueSet that is being bound for the purpose.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ValueSet"],
    )
    valueSet__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueSet", title="Extension field for ``valueSet``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ElementDefinitionBindingAdditional`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "purpose",
            "valueSet",
            "documentation",
            "shortDoco",
            "usage",
            "any",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3640(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("purpose", "purpose__ext"), ("valueSet", "valueSet__ext")]
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


class ElementDefinitionConstraint(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Condition that must evaluate to true.
    Formal constraints such as co-occurrence and other constraints that can be
    computationally evaluated within the context of the instance.
    """

    resource_type = Field("ElementDefinitionConstraint", const=True)

    expression: fhirtypes.String = Field(
        None,
        alias="expression",
        title="FHIRPath expression of constraint",
        description=(
            "A [FHIRPath](fhirpath.html) expression of constraint that can be "
            "executed to see if this constraint is met."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_expression", title="Extension field for ``expression``."
    )

    human: fhirtypes.String = Field(
        None,
        alias="human",
        title="Human description of constraint",
        description=(
            "Text that can be used to describe the constraint in messages "
            "identifying that the constraint has been violated."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    human__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_human", title="Extension field for ``human``."
    )

    key: fhirtypes.Id = Field(
        None,
        alias="key",
        title="Target of 'condition' reference above",
        description=(
            "Allows identification of which elements have their cardinalities "
            "impacted by the constraint.  Will not be referenced for constraints "
            "that do not affect cardinality."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    key__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_key", title="Extension field for ``key``."
    )

    requirements: fhirtypes.Markdown = Field(
        None,
        alias="requirements",
        title="Why this constraint is necessary or appropriate",
        description="Description of why this constraint is necessary or appropriate.",
        # if property is element of this resource.
        element_property=True,
    )
    requirements__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_requirements", title="Extension field for ``requirements``."
    )

    severity: fhirtypes.Code = Field(
        None,
        alias="severity",
        title="error | warning",
        description=(
            "Identifies the impact constraint violation has on the conformance of "
            "the instance."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["error", "warning"],
    )
    severity__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_severity", title="Extension field for ``severity``."
    )

    source: fhirtypes.Canonical = Field(
        None,
        alias="source",
        title="Reference to original source of constraint",
        description=(
            "A reference to the original source of the constraint, for traceability"
            " purposes."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureDefinition"],
    )
    source__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_source", title="Extension field for ``source``."
    )

    suppress: bool = Field(
        None,
        alias="suppress",
        title="Suppress warning or hint in profile",
        description=(
            "If true, indicates that the warning or best practice guideline should "
            "be suppressed."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    suppress__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_suppress", title="Extension field for ``suppress``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ElementDefinitionConstraint`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "key",
            "requirements",
            "severity",
            "suppress",
            "human",
            "expression",
            "source",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2993(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("human", "human__ext"),
            ("key", "key__ext"),
            ("severity", "severity__ext"),
        ]
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


class ElementDefinitionExample(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Example value (as defined for type).
    A sample value for this element demonstrating the type of information that
    would typically be found in the element.
    """

    resource_type = Field("ElementDefinitionExample", const=True)

    label: fhirtypes.String = Field(
        None,
        alias="label",
        title="Describes the purpose of this example",
        description="Describes the purpose of this example among the set of examples.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    label__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_label", title="Extension field for ``label``."
    )

    valueAddress: fhirtypes.AddressType = Field(
        None,
        alias="valueAddress",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueAge: fhirtypes.AgeType = Field(
        None,
        alias="valueAge",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueAnnotation: fhirtypes.AnnotationType = Field(
        None,
        alias="valueAnnotation",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueAvailability: fhirtypes.AvailabilityType = Field(
        None,
        alias="valueAvailability",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueBase64Binary: fhirtypes.Base64Binary = Field(
        None,
        alias="valueBase64Binary",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
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
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCanonical: fhirtypes.Canonical = Field(
        None,
        alias="valueCanonical",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueCanonical", title="Extension field for ``valueCanonical``."
    )

    valueCode: fhirtypes.Code = Field(
        None,
        alias="valueCode",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueCode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueCode", title="Extension field for ``valueCode``."
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="valueCodeableConcept",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueCodeableReference: fhirtypes.CodeableReferenceType = Field(
        None,
        alias="valueCodeableReference",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueCoding: fhirtypes.CodingType = Field(
        None,
        alias="valueCoding",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueContactDetail: fhirtypes.ContactDetailType = Field(
        None,
        alias="valueContactDetail",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueContactPoint: fhirtypes.ContactPointType = Field(
        None,
        alias="valueContactPoint",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueCount: fhirtypes.CountType = Field(
        None,
        alias="valueCount",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueDataRequirement: fhirtypes.DataRequirementType = Field(
        None,
        alias="valueDataRequirement",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueDate: fhirtypes.Date = Field(
        None,
        alias="valueDate",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDate", title="Extension field for ``valueDate``."
    )

    valueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="valueDateTime",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDateTime", title="Extension field for ``valueDateTime``."
    )

    valueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="valueDecimal",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDecimal", title="Extension field for ``valueDecimal``."
    )

    valueDistance: fhirtypes.DistanceType = Field(
        None,
        alias="valueDistance",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueDosage: fhirtypes.DosageType = Field(
        None,
        alias="valueDosage",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueDuration: fhirtypes.DurationType = Field(
        None,
        alias="valueDuration",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueExpression: fhirtypes.ExpressionType = Field(
        None,
        alias="valueExpression",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueExtendedContactDetail: fhirtypes.ExtendedContactDetailType = Field(
        None,
        alias="valueExtendedContactDetail",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueHumanName: fhirtypes.HumanNameType = Field(
        None,
        alias="valueHumanName",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueId: fhirtypes.Id = Field(
        None,
        alias="valueId",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueId", title="Extension field for ``valueId``."
    )

    valueIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="valueIdentifier",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueInstant: fhirtypes.Instant = Field(
        None,
        alias="valueInstant",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueInstant__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueInstant", title="Extension field for ``valueInstant``."
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueInteger", title="Extension field for ``valueInteger``."
    )

    valueInteger64: fhirtypes.Integer64 = Field(
        None,
        alias="valueInteger64",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueInteger64__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueInteger64", title="Extension field for ``valueInteger64``."
    )

    valueMarkdown: fhirtypes.Markdown = Field(
        None,
        alias="valueMarkdown",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueMarkdown", title="Extension field for ``valueMarkdown``."
    )

    valueMeta: fhirtypes.MetaType = Field(
        None,
        alias="valueMeta",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueMoney: fhirtypes.MoneyType = Field(
        None,
        alias="valueMoney",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueOid: fhirtypes.Oid = Field(
        None,
        alias="valueOid",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueOid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueOid", title="Extension field for ``valueOid``."
    )

    valueParameterDefinition: fhirtypes.ParameterDefinitionType = Field(
        None,
        alias="valueParameterDefinition",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valuePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="valuePeriod",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valuePositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="valuePositiveInt",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
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
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueRange: fhirtypes.RangeType = Field(
        None,
        alias="valueRange",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueRatio: fhirtypes.RatioType = Field(
        None,
        alias="valueRatio",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueRatioRange: fhirtypes.RatioRangeType = Field(
        None,
        alias="valueRatioRange",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueReference",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueRelatedArtifact: fhirtypes.RelatedArtifactType = Field(
        None,
        alias="valueRelatedArtifact",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueSampledData: fhirtypes.SampledDataType = Field(
        None,
        alias="valueSampledData",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueSignature: fhirtypes.SignatureType = Field(
        None,
        alias="valueSignature",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    valueTime: fhirtypes.Time = Field(
        None,
        alias="valueTime",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueTime", title="Extension field for ``valueTime``."
    )

    valueTiming: fhirtypes.TimingType = Field(
        None,
        alias="valueTiming",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueTriggerDefinition: fhirtypes.TriggerDefinitionType = Field(
        None,
        alias="valueTriggerDefinition",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="valueUnsignedInt",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
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
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueUri", title="Extension field for ``valueUri``."
    )

    valueUrl: fhirtypes.Url = Field(
        None,
        alias="valueUrl",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueUrl__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueUrl", title="Extension field for ``valueUrl``."
    )

    valueUsageContext: fhirtypes.UsageContextType = Field(
        None,
        alias="valueUsageContext",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueUuid: fhirtypes.Uuid = Field(
        None,
        alias="valueUuid",
        title="Value of Example (one of allowed types)",
        description=(
            "The actual value for the element, which must be one of the types "
            "allowed for this element."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueUuid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueUuid", title="Extension field for ``valueUuid``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ElementDefinitionExample`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "label",
            "valueBase64Binary",
            "valueBoolean",
            "valueCanonical",
            "valueCode",
            "valueDate",
            "valueDateTime",
            "valueDecimal",
            "valueId",
            "valueInstant",
            "valueInteger",
            "valueInteger64",
            "valueMarkdown",
            "valueOid",
            "valuePositiveInt",
            "valueString",
            "valueTime",
            "valueUnsignedInt",
            "valueUri",
            "valueUrl",
            "valueUuid",
            "valueAddress",
            "valueAge",
            "valueAnnotation",
            "valueAttachment",
            "valueCodeableConcept",
            "valueCodeableReference",
            "valueCoding",
            "valueContactPoint",
            "valueCount",
            "valueDistance",
            "valueDuration",
            "valueHumanName",
            "valueIdentifier",
            "valueMoney",
            "valuePeriod",
            "valueQuantity",
            "valueRange",
            "valueRatio",
            "valueRatioRange",
            "valueReference",
            "valueSampledData",
            "valueSignature",
            "valueTiming",
            "valueContactDetail",
            "valueDataRequirement",
            "valueExpression",
            "valueParameterDefinition",
            "valueRelatedArtifact",
            "valueTriggerDefinition",
            "valueUsageContext",
            "valueAvailability",
            "valueExtendedContactDetail",
            "valueDosage",
            "valueMeta",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2633(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("label", "label__ext")]
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
    def validate_one_of_many_2633(
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
                "valueAddress",
                "valueAge",
                "valueAnnotation",
                "valueAttachment",
                "valueAvailability",
                "valueBase64Binary",
                "valueBoolean",
                "valueCanonical",
                "valueCode",
                "valueCodeableConcept",
                "valueCodeableReference",
                "valueCoding",
                "valueContactDetail",
                "valueContactPoint",
                "valueCount",
                "valueDataRequirement",
                "valueDate",
                "valueDateTime",
                "valueDecimal",
                "valueDistance",
                "valueDosage",
                "valueDuration",
                "valueExpression",
                "valueExtendedContactDetail",
                "valueHumanName",
                "valueId",
                "valueIdentifier",
                "valueInstant",
                "valueInteger",
                "valueInteger64",
                "valueMarkdown",
                "valueMeta",
                "valueMoney",
                "valueOid",
                "valueParameterDefinition",
                "valuePeriod",
                "valuePositiveInt",
                "valueQuantity",
                "valueRange",
                "valueRatio",
                "valueRatioRange",
                "valueReference",
                "valueRelatedArtifact",
                "valueSampledData",
                "valueSignature",
                "valueString",
                "valueTime",
                "valueTiming",
                "valueTriggerDefinition",
                "valueUnsignedInt",
                "valueUri",
                "valueUrl",
                "valueUsageContext",
                "valueUuid",
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
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Map element to another set of definitions.
    Identifies a concept from an external specification that roughly
    corresponds to this element.
    """

    resource_type = Field("ElementDefinitionMapping", const=True)

    comment: fhirtypes.Markdown = Field(
        None,
        alias="comment",
        title="Comments about the mapping or its use",
        description="Comments that provide information about the mapping or its use.",
        # if property is element of this resource.
        element_property=True,
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    identity: fhirtypes.Id = Field(
        None,
        alias="identity",
        title="Reference to mapping declaration",
        description="An internal reference to the definition of a mapping.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    identity__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_identity", title="Extension field for ``identity``."
    )

    language: fhirtypes.Code = Field(
        None,
        alias="language",
        title="Computable language of mapping",
        description="Identifies the computable language in which mapping.map is expressed.",
        # if property is element of this resource.
        element_property=True,
    )
    language__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_language", title="Extension field for ``language``."
    )

    map: fhirtypes.String = Field(
        None,
        alias="map",
        title="Details of the mapping",
        description=(
            "Expresses what part of the target specification corresponds to this "
            "element."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    map__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_map", title="Extension field for ``map``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ElementDefinitionMapping`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "identity", "language", "map", "comment"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2635(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("identity", "identity__ext"), ("map", "map__ext")]
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


class ElementDefinitionSlicing(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
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
        title="Text description of how slicing works (or not)",
        description=(
            "A human-readable text description of how the slicing works. If there "
            "is no discriminator, this is required to be present to provide "
            "whatever information is possible about how the slices can be "
            "differentiated."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    discriminator: typing.List[
        fhirtypes.ElementDefinitionSlicingDiscriminatorType
    ] = Field(
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
        # if property is element of this resource.
        element_property=True,
    )

    ordered: bool = Field(
        None,
        alias="ordered",
        title="If elements must be in same order as slices",
        description=(
            "If the matching elements have to occur in the same order as defined in"
            " the profile."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    ordered__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_ordered", title="Extension field for ``ordered``."
    )

    rules: fhirtypes.Code = Field(
        None,
        alias="rules",
        title="closed | open | openAtEnd",
        description=(
            "Whether additional slices are allowed or not. When the slices are "
            "ordered, profile authors can also say that additional slices are only "
            "allowed at the end."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["closed", "open", "openAtEnd"],
    )
    rules__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_rules", title="Extension field for ``rules``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ElementDefinitionSlicing`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "discriminator", "description", "ordered", "rules"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2632(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("rules", "rules__ext")]
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


class ElementDefinitionSlicingDiscriminator(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
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
        None,
        alias="path",
        title="Path to element value",
        description=(
            "A FHIRPath expression, using [the simple subset of "
            "FHIRPath](fhirpath.html#simple), that is used to identify the element "
            "on which discrimination is based."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_path", title="Extension field for ``path``."
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="value | exists | type | profile | position",
        description="How the element value is interpreted when discrimination is evaluated.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["value", "exists", "type", "profile", "position"],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ElementDefinitionSlicingDiscriminator`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "type", "path"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_4011(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("path", "path__ext"), ("type", "type__ext")]
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


class ElementDefinitionType(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Data type and Profile for this element.
    The data type or resource that the value of this element is permitted to
    be.
    """

    resource_type = Field("ElementDefinitionType", const=True)

    aggregation: typing.List[typing.Optional[fhirtypes.Code]] = Field(
        None,
        alias="aggregation",
        title="contained | referenced | bundled - how aggregated",
        description=(
            "If the type is a reference to another resource, how the resource is or"
            " can be aggregated - is it a contained resource, or a reference, and "
            "if the context is a bundle, is it included in the bundle."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["contained", "referenced", "bundled"],
    )
    aggregation__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_aggregation", title="Extension field for ``aggregation``.")

    code: fhirtypes.Uri = Field(
        None,
        alias="code",
        title="Data type or Resource (reference to definition)",
        description=(
            "URL of Data type or Resource that is a(or the) type used for this "
            "element. References are URLs that are relative to "
            'http://hl7.org/fhir/StructureDefinition e.g. "string" is a reference '
            "to http://hl7.org/fhir/StructureDefinition/string. Absolute URLs are "
            "only allowed in logical models."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    profile: typing.List[typing.Optional[fhirtypes.Canonical]] = Field(
        None,
        alias="profile",
        title="Profiles (StructureDefinition or IG) - one must apply",
        description=(
            "Identifies a profile structure or implementation Guide that applies to"
            " the datatype this element refers to. If any profiles are specified, "
            "then the content must conform to at least one of them. The URL can be "
            "a local reference - to a contained StructureDefinition, or a reference"
            " to another StructureDefinition or Implementation Guide by a canonical"
            " URL. When an implementation guide is specified, the type SHALL "
            "conform to at least one profile defined in the implementation guide."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureDefinition", "ImplementationGuide"],
    )
    profile__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_profile", title="Extension field for ``profile``.")

    targetProfile: typing.List[typing.Optional[fhirtypes.Canonical]] = Field(
        None,
        alias="targetProfile",
        title=(
            "Profile (StructureDefinition or IG) on the Reference/canonical target "
            "- one must apply"
        ),
        description=(
            'Used when the type is "Reference" or "canonical", and identifies a '
            "profile structure or implementation Guide that applies to the target "
            "of the reference this element refers to. If any profiles are "
            "specified, then the content must conform to at least one of them. The "
            "URL can be a local reference - to a contained StructureDefinition, or "
            "a reference to another StructureDefinition or Implementation Guide by "
            "a canonical URL. When an implementation guide is specified, the target"
            " resource SHALL conform to at least one profile defined in the "
            "implementation guide."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureDefinition", "ImplementationGuide"],
    )
    targetProfile__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_targetProfile", title="Extension field for ``targetProfile``."
    )

    versioning: fhirtypes.Code = Field(
        None,
        alias="versioning",
        title="either | independent | specific",
        description=(
            "Whether this reference needs to be version specific or version "
            "independent, or whether either can be used."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["either", "independent", "specific"],
    )
    versioning__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_versioning", title="Extension field for ``versioning``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ElementDefinitionType`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "code",
            "profile",
            "targetProfile",
            "aggregation",
            "versioning",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2335(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("code", "code__ext")]
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
