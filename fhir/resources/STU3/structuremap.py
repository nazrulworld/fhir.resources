# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/StructureMap
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType
from typing import Union

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class StructureMap(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A Map of relationships between 2 structures that can be used to transform
    data.
    """

    resource_type = Field("StructureMap", const=True)

    contact: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Contact details for the publisher",
    )

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Type `Markdown`",
        description="Use and/or publishing restrictions",
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime`",
        description="Date this was last changed",
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown`",
        description="Natural language description of the structure map",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="Type `bool`",
        description="For testing purposes, not real usage",
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    group: ListType[fhirtypes.StructureMapGroupType] = Field(
        ...,
        alias="group",
        title="List of `StructureMapGroup` items (represented as `dict` in JSON)",
        description="Named sections for reader convenience",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Additional identifier for the structure map",
    )

    import_fhir: ListType[fhirtypes.Uri] = Field(
        None,
        alias="import",
        title="List of `Uri` items",
        description="Other maps used by this map (canonical URLs)",
    )
    import__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_import", title="Extension field for ``import_fhir``."
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Intended jurisdiction for structure map (if applicable)",
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String`",
        description="Name for this structure map (computer friendly)",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Type `String`",
        description="Name of the publisher (organization or individual)",
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Type `Markdown`",
        description="Why this structure map is defined",
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`",
        description="draft | active | retired | unknown",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    structure: ListType[fhirtypes.StructureMapStructureType] = Field(
        None,
        alias="structure",
        title="List of `StructureMapStructure` items (represented as `dict` in JSON)",
        description="Structure Definition used by this map",
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String`",
        description="Name for this structure map (human friendly)",
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.Uri = Field(
        ...,
        alias="url",
        title="Type `Uri`",
        description="Logical URI to reference this structure map (globally unique)",
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    useContext: ListType[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="List of `UsageContext` items (represented as `dict` in JSON)",
        description="Context the content is intended to support",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String`",
        description="Business version of the structure map",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class StructureMapGroup(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Named sections for reader convenience.
    Organizes the mapping into managable chunks for human review/ease of
    maintenance.
    """

    resource_type = Field("StructureMapGroup", const=True)

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String`",
        description="Additional description/explaination for group",
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    extends: fhirtypes.Id = Field(
        None,
        alias="extends",
        title="Type `Id`",
        description="Another group that this group adds rules to",
    )
    extends__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_extends", title="Extension field for ``extends``."
    )

    input: ListType[fhirtypes.StructureMapGroupInputType] = Field(
        ...,
        alias="input",
        title="List of `StructureMapGroupInput` items (represented as `dict` in JSON)",
        description="Named instance provided when invoking the map",
    )

    name: fhirtypes.Id = Field(
        ..., alias="name", title="Type `Id`", description="Human-readable label"
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    rule: ListType[fhirtypes.StructureMapGroupRuleType] = Field(
        ...,
        alias="rule",
        title="List of `StructureMapGroupRule` items (represented as `dict` in JSON)",
        description="Transform Rule from source to target",
    )

    typeMode: fhirtypes.Code = Field(
        ...,
        alias="typeMode",
        title="Type `Code`",
        description="none | types | type-and-types",
    )
    typeMode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_typeMode", title="Extension field for ``typeMode``."
    )


class StructureMapGroupInput(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Named instance provided when invoking the map.
    A name assigned to an instance of data. The instance must be provided when
    the mapping is invoked.
    """

    resource_type = Field("StructureMapGroupInput", const=True)

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String`",
        description="Documentation for this instance of data",
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    mode: fhirtypes.Code = Field(
        ..., alias="mode", title="Type `Code`", description="source | target"
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_mode", title="Extension field for ``mode``."
    )

    name: fhirtypes.Id = Field(
        ...,
        alias="name",
        title="Type `Id`",
        description="Name for this instance of data",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    type: fhirtypes.String = Field(
        None,
        alias="type",
        title="Type `String`",
        description="Type for this instance of data",
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )


class StructureMapGroupRule(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Transform Rule from source to target.
    """

    resource_type = Field("StructureMapGroupRule", const=True)

    dependent: ListType[fhirtypes.StructureMapGroupRuleDependentType] = Field(
        None,
        alias="dependent",
        title=(
            "List of `StructureMapGroupRuleDependent` items (represented as `dict` "
            "in JSON)"
        ),
        description="Which other rules to apply in the context of this rule",
    )

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String`",
        description="Documentation for this instance of data",
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    name: fhirtypes.Id = Field(
        ...,
        alias="name",
        title="Type `Id`",
        description="Name of the rule for internal references",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    rule: ListType[fhirtypes.StructureMapGroupRuleType] = Field(
        None,
        alias="rule",
        title="List of `StructureMapGroupRule` items (represented as `dict` in JSON)",
        description="Rules contained in this rule",
    )

    source: ListType[fhirtypes.StructureMapGroupRuleSourceType] = Field(
        ...,
        alias="source",
        title=(
            "List of `StructureMapGroupRuleSource` items (represented as `dict` in "
            "JSON)"
        ),
        description="Source inputs to the mapping",
    )

    target: ListType[fhirtypes.StructureMapGroupRuleTargetType] = Field(
        None,
        alias="target",
        title=(
            "List of `StructureMapGroupRuleTarget` items (represented as `dict` in "
            "JSON)"
        ),
        description="Content to create because of this mapping rule",
    )


class StructureMapGroupRuleDependent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Which other rules to apply in the context of this rule.
    """

    resource_type = Field("StructureMapGroupRuleDependent", const=True)

    name: fhirtypes.Id = Field(
        ...,
        alias="name",
        title="Type `Id`",
        description="Name of a rule or group to apply",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    variable: ListType[fhirtypes.String] = Field(
        ...,
        alias="variable",
        title="List of `String` items",
        description="Variable to pass to the rule or group",
    )
    variable__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_variable", title="Extension field for ``variable``."
    )


class StructureMapGroupRuleSource(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Source inputs to the mapping.
    """

    resource_type = Field("StructureMapGroupRuleSource", const=True)

    check: fhirtypes.String = Field(
        None,
        alias="check",
        title="Type `String`",
        description=(
            "FHIRPath expression  - must be true or the mapping engine throws an "
            "error instead of completing"
        ),
    )
    check__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_check", title="Extension field for ``check``."
    )

    condition: fhirtypes.String = Field(
        None,
        alias="condition",
        title="Type `String`",
        description="FHIRPath expression  - must be true or the rule does not apply",
    )
    condition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_condition", title="Extension field for ``condition``."
    )

    context: fhirtypes.Id = Field(
        ...,
        alias="context",
        title="Type `Id`",
        description="Type or variable this rule applies to",
    )
    context__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_context", title="Extension field for ``context``."
    )

    defaultValueAddress: fhirtypes.AddressType = Field(
        None,
        alias="defaultValueAddress",
        title="Type `Address` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueAge: fhirtypes.AgeType = Field(
        None,
        alias="defaultValueAge",
        title="Type `Age` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueAnnotation: fhirtypes.AnnotationType = Field(
        None,
        alias="defaultValueAnnotation",
        title="Type `Annotation` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="defaultValueAttachment",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueBase64Binary: fhirtypes.Base64Binary = Field(
        None,
        alias="defaultValueBase64Binary",
        title="Type `Base64Binary`",
        description="Default value if no value exists",
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
        description="Default value if no value exists",
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
        description="Default value if no value exists",
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
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueCoding: fhirtypes.CodingType = Field(
        None,
        alias="defaultValueCoding",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueContactPoint: fhirtypes.ContactPointType = Field(
        None,
        alias="defaultValueContactPoint",
        title="Type `ContactPoint` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueCount: fhirtypes.CountType = Field(
        None,
        alias="defaultValueCount",
        title="Type `Count` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueDate: fhirtypes.Date = Field(
        None,
        alias="defaultValueDate",
        title="Type `Date`",
        description="Default value if no value exists",
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
        description="Default value if no value exists",
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
        description="Default value if no value exists",
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
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueDuration: fhirtypes.DurationType = Field(
        None,
        alias="defaultValueDuration",
        title="Type `Duration` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueHumanName: fhirtypes.HumanNameType = Field(
        None,
        alias="defaultValueHumanName",
        title="Type `HumanName` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueId: fhirtypes.Id = Field(
        None,
        alias="defaultValueId",
        title="Type `Id`",
        description="Default value if no value exists",
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
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueInstant: fhirtypes.Instant = Field(
        None,
        alias="defaultValueInstant",
        title="Type `Instant`",
        description="Default value if no value exists",
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
        description="Default value if no value exists",
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
        description="Default value if no value exists",
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
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueMoney: fhirtypes.MoneyType = Field(
        None,
        alias="defaultValueMoney",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueOid: fhirtypes.Oid = Field(
        None,
        alias="defaultValueOid",
        title="Type `Oid`",
        description="Default value if no value exists",
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
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValuePositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="defaultValuePositiveInt",
        title="Type `PositiveInt`",
        description="Default value if no value exists",
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
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueRange: fhirtypes.RangeType = Field(
        None,
        alias="defaultValueRange",
        title="Type `Range` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueRatio: fhirtypes.RatioType = Field(
        None,
        alias="defaultValueRatio",
        title="Type `Ratio` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueReference: fhirtypes.ReferenceType = Field(
        None,
        alias="defaultValueReference",
        title="Type `Reference` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueSampledData: fhirtypes.SampledDataType = Field(
        None,
        alias="defaultValueSampledData",
        title="Type `SampledData` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueSignature: fhirtypes.SignatureType = Field(
        None,
        alias="defaultValueSignature",
        title="Type `Signature` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueString: fhirtypes.String = Field(
        None,
        alias="defaultValueString",
        title="Type `String`",
        description="Default value if no value exists",
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
        description="Default value if no value exists",
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
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="defaultValueUnsignedInt",
        title="Type `UnsignedInt`",
        description="Default value if no value exists",
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
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    defaultValueUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_defaultValueUri", title="Extension field for ``defaultValueUri``."
    )

    element: fhirtypes.String = Field(
        None,
        alias="element",
        title="Type `String`",
        description="Optional field for this source",
    )
    element__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_element", title="Extension field for ``element``."
    )

    listMode: fhirtypes.Code = Field(
        None,
        alias="listMode",
        title="Type `Code`",
        description="first | not_first | last | not_last | only_one",
    )
    listMode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_listMode", title="Extension field for ``listMode``."
    )

    max: fhirtypes.String = Field(
        None,
        alias="max",
        title="Type `String`",
        description="Specified maximum cardinality (number or *)",
    )
    max__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_max", title="Extension field for ``max``."
    )

    min: fhirtypes.Integer = Field(
        None,
        alias="min",
        title="Type `Integer`",
        description="Specified minimum cardinality",
    )
    min__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_min", title="Extension field for ``min``."
    )

    type: fhirtypes.String = Field(
        None,
        alias="type",
        title="Type `String`",
        description="Rule only applies if source has this type",
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    variable: fhirtypes.Id = Field(
        None,
        alias="variable",
        title="Type `Id`",
        description="Named context for field, if a field is specified",
    )
    variable__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_variable", title="Extension field for ``variable``."
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


class StructureMapGroupRuleTarget(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Content to create because of this mapping rule.
    """

    resource_type = Field("StructureMapGroupRuleTarget", const=True)

    context: fhirtypes.Id = Field(
        None,
        alias="context",
        title="Type `Id`",
        description="Type or variable this rule applies to",
    )
    context__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_context", title="Extension field for ``context``."
    )

    contextType: fhirtypes.Code = Field(
        None, alias="contextType", title="Type `Code`", description="type | variable"
    )
    contextType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_contextType", title="Extension field for ``contextType``."
    )

    element: fhirtypes.String = Field(
        None,
        alias="element",
        title="Type `String`",
        description="Field to create in the context",
    )
    element__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_element", title="Extension field for ``element``."
    )

    listMode: ListType[fhirtypes.Code] = Field(
        None,
        alias="listMode",
        title="List of `Code` items",
        description="first | share | last | collate",
    )
    listMode__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_listMode", title="Extension field for ``listMode``."
    )

    listRuleId: fhirtypes.Id = Field(
        None,
        alias="listRuleId",
        title="Type `Id`",
        description="Internal rule reference for shared list items",
    )
    listRuleId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_listRuleId", title="Extension field for ``listRuleId``."
    )

    parameter: ListType[fhirtypes.StructureMapGroupRuleTargetParameterType] = Field(
        None,
        alias="parameter",
        title=(
            "List of `StructureMapGroupRuleTargetParameter` items (represented as "
            "`dict` in JSON)"
        ),
        description="Parameters to the transform",
    )

    transform: fhirtypes.Code = Field(
        None, alias="transform", title="Type `Code`", description="create | copy +"
    )
    transform__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_transform", title="Extension field for ``transform``."
    )

    variable: fhirtypes.Id = Field(
        None,
        alias="variable",
        title="Type `Id`",
        description="Named context for field, if desired, and a field is specified",
    )
    variable__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_variable", title="Extension field for ``variable``."
    )


class StructureMapGroupRuleTargetParameter(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Parameters to the transform.
    """

    resource_type = Field("StructureMapGroupRuleTargetParameter", const=True)

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="Type `bool`",
        description="Parameter value - variable or literal",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="valueDecimal",
        title="Type `Decimal`",
        description="Parameter value - variable or literal",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDecimal", title="Extension field for ``valueDecimal``."
    )

    valueId: fhirtypes.Id = Field(
        None,
        alias="valueId",
        title="Type `Id`",
        description="Parameter value - variable or literal",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueId", title="Extension field for ``valueId``."
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="Type `Integer`",
        description="Parameter value - variable or literal",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueInteger", title="Extension field for ``valueInteger``."
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Type `String`",
        description="Parameter value - variable or literal",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueString", title="Extension field for ``valueString``."
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
                "valueBoolean",
                "valueDecimal",
                "valueId",
                "valueInteger",
                "valueString",
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


class StructureMapStructure(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Structure Definition used by this map.
    A structure definition used by this map. The structure definition may
    describe instances that are converted, or the instances that are produced.
    """

    resource_type = Field("StructureMapStructure", const=True)

    alias: fhirtypes.String = Field(
        None,
        alias="alias",
        title="Type `String`",
        description="Name for type in this map",
    )
    alias__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_alias", title="Extension field for ``alias``."
    )

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String`",
        description="Documentation on use of structure",
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    mode: fhirtypes.Code = Field(
        ...,
        alias="mode",
        title="Type `Code`",
        description="source | queried | target | produced",
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_mode", title="Extension field for ``mode``."
    )

    url: fhirtypes.Uri = Field(
        ...,
        alias="url",
        title="Type `Uri`",
        description="Canonical URL for structure definition",
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )
