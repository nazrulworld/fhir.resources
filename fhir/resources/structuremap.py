# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/StructureMap
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class StructureMap(domainresource.DomainResource):
    """ A Map of relationships between 2 structures that can be used to transform
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
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Use and/or publishing restrictions",
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date last changed",
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Natural language description of the structure map",
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="Type `bool`",
        description="For testing purposes, not real usage",
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

    import_fhir: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="import",
        title=(
            "List of `Canonical` items referencing `StructureMap` (represented as "
            "`dict` in JSON)"
        ),
        description="Other maps used by this map (canonical URLs)",
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
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this structure map (computer friendly)",
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of the publisher (organization or individual)",
    )

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Why this structure map is defined",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="draft | active | retired | unknown",
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
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this structure map (human friendly)",
    )

    url: fhirtypes.Uri = Field(
        ...,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description=(
            "Canonical identifier for this structure map, represented as a URI "
            "(globally unique)"
        ),
    )

    useContext: ListType[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="List of `UsageContext` items (represented as `dict` in JSON)",
        description="The context that the content is intended to support",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String` (represented as `dict` in JSON)",
        description="Business version of the structure map",
    )


class StructureMapGroup(backboneelement.BackboneElement):
    """ Named sections for reader convenience.
    Organizes the mapping into manageable chunks for human review/ease of
    maintenance.
    """

    resource_type = Field("StructureMapGroup", const=True)

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String` (represented as `dict` in JSON)",
        description="Additional description/explanation for group",
    )

    extends: fhirtypes.Id = Field(
        None,
        alias="extends",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Another group that this group adds rules to",
    )

    input: ListType[fhirtypes.StructureMapGroupInputType] = Field(
        ...,
        alias="input",
        title="List of `StructureMapGroupInput` items (represented as `dict` in JSON)",
        description="Named instance provided when invoking the map",
    )

    name: fhirtypes.Id = Field(
        ...,
        alias="name",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Human-readable label",
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
        title="Type `Code` (represented as `dict` in JSON)",
        description="none | types | type-and-types",
    )


class StructureMapGroupInput(backboneelement.BackboneElement):
    """ Named instance provided when invoking the map.
    A name assigned to an instance of data. The instance must be provided when
    the mapping is invoked.
    """

    resource_type = Field("StructureMapGroupInput", const=True)

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String` (represented as `dict` in JSON)",
        description="Documentation for this instance of data",
    )

    mode: fhirtypes.Code = Field(
        ...,
        alias="mode",
        title="Type `Code` (represented as `dict` in JSON)",
        description="source | target",
    )

    name: fhirtypes.Id = Field(
        ...,
        alias="name",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Name for this instance of data",
    )

    type: fhirtypes.String = Field(
        None,
        alias="type",
        title="Type `String` (represented as `dict` in JSON)",
        description="Type for this instance of data",
    )


class StructureMapGroupRule(backboneelement.BackboneElement):
    """ Transform Rule from source to target.
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
        title="Type `String` (represented as `dict` in JSON)",
        description="Documentation for this instance of data",
    )

    name: fhirtypes.Id = Field(
        ...,
        alias="name",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Name of the rule for internal references",
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
    """ Which other rules to apply in the context of this rule.
    """

    resource_type = Field("StructureMapGroupRuleDependent", const=True)

    name: fhirtypes.Id = Field(
        ...,
        alias="name",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Name of a rule or group to apply",
    )

    variable: ListType[fhirtypes.String] = Field(
        ...,
        alias="variable",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Variable to pass to the rule or group",
    )


class StructureMapGroupRuleSource(backboneelement.BackboneElement):
    """ Source inputs to the mapping.
    """

    resource_type = Field("StructureMapGroupRuleSource", const=True)

    check: fhirtypes.String = Field(
        None,
        alias="check",
        title="Type `String` (represented as `dict` in JSON)",
        description=(
            "FHIRPath expression  - must be true or the mapping engine throws an "
            "error instead of completing"
        ),
    )

    condition: fhirtypes.String = Field(
        None,
        alias="condition",
        title="Type `String` (represented as `dict` in JSON)",
        description="FHIRPath expression  - must be true or the rule does not apply",
    )

    context: fhirtypes.Id = Field(
        ...,
        alias="context",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Type or variable this rule applies to",
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
        title="Type `Base64Binary` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueBoolean: bool = Field(
        None,
        alias="defaultValueBoolean",
        title="Type `bool`",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueCanonical: fhirtypes.Canonical = Field(
        None,
        alias="defaultValueCanonical",
        title="Type `Canonical` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueCode: fhirtypes.Code = Field(
        None,
        alias="defaultValueCode",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
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

    defaultValueContactDetail: fhirtypes.ContactDetailType = Field(
        None,
        alias="defaultValueContactDetail",
        title="Type `ContactDetail` (represented as `dict` in JSON)",
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

    defaultValueContributor: fhirtypes.ContributorType = Field(
        None,
        alias="defaultValueContributor",
        title="Type `Contributor` (represented as `dict` in JSON)",
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

    defaultValueDataRequirement: fhirtypes.DataRequirementType = Field(
        None,
        alias="defaultValueDataRequirement",
        title="Type `DataRequirement` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueDate: fhirtypes.Date = Field(
        None,
        alias="defaultValueDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="defaultValueDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="defaultValueDecimal",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueDistance: fhirtypes.DistanceType = Field(
        None,
        alias="defaultValueDistance",
        title="Type `Distance` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueDosage: fhirtypes.DosageType = Field(
        None,
        alias="defaultValueDosage",
        title="Type `Dosage` (represented as `dict` in JSON)",
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

    defaultValueExpression: fhirtypes.ExpressionType = Field(
        None,
        alias="defaultValueExpression",
        title="Type `Expression` (represented as `dict` in JSON)",
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
        title="Type `Id` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
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
        title="Type `Instant` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueInteger: fhirtypes.Integer = Field(
        None,
        alias="defaultValueInteger",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueMarkdown: fhirtypes.Markdown = Field(
        None,
        alias="defaultValueMarkdown",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
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
        title="Type `Oid` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueParameterDefinition: fhirtypes.ParameterDefinitionType = Field(
        None,
        alias="defaultValueParameterDefinition",
        title="Type `ParameterDefinition` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
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
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
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

    defaultValueRelatedArtifact: fhirtypes.RelatedArtifactType = Field(
        None,
        alias="defaultValueRelatedArtifact",
        title="Type `RelatedArtifact` (represented as `dict` in JSON)",
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
        title="Type `String` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueTime: fhirtypes.Time = Field(
        None,
        alias="defaultValueTime",
        title="Type `Time` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueTiming: fhirtypes.TimingType = Field(
        None,
        alias="defaultValueTiming",
        title="Type `Timing` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueTriggerDefinition: fhirtypes.TriggerDefinitionType = Field(
        None,
        alias="defaultValueTriggerDefinition",
        title="Type `TriggerDefinition` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="defaultValueUnsignedInt",
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueUri: fhirtypes.Uri = Field(
        None,
        alias="defaultValueUri",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueUrl: fhirtypes.Url = Field(
        None,
        alias="defaultValueUrl",
        title="Type `Url` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueUsageContext: fhirtypes.UsageContextType = Field(
        None,
        alias="defaultValueUsageContext",
        title="Type `UsageContext` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    defaultValueUuid: fhirtypes.Uuid = Field(
        None,
        alias="defaultValueUuid",
        title="Type `Uuid` (represented as `dict` in JSON)",
        description="Default value if no value exists",
        one_of_many="defaultValue",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    element: fhirtypes.String = Field(
        None,
        alias="element",
        title="Type `String` (represented as `dict` in JSON)",
        description="Optional field for this source",
    )

    listMode: fhirtypes.Code = Field(
        None,
        alias="listMode",
        title="Type `Code` (represented as `dict` in JSON)",
        description="first | not_first | last | not_last | only_one",
    )

    logMessage: fhirtypes.String = Field(
        None,
        alias="logMessage",
        title="Type `String` (represented as `dict` in JSON)",
        description="Message to put in log if source exists (FHIRPath)",
    )

    max: fhirtypes.String = Field(
        None,
        alias="max",
        title="Type `String` (represented as `dict` in JSON)",
        description="Specified maximum cardinality (number or *)",
    )

    min: fhirtypes.Integer = Field(
        None,
        alias="min",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Specified minimum cardinality",
    )

    type: fhirtypes.String = Field(
        None,
        alias="type",
        title="Type `String` (represented as `dict` in JSON)",
        description="Rule only applies if source has this type",
    )

    variable: fhirtypes.Id = Field(
        None,
        alias="variable",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Named context for field, if a field is specified",
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
                "defaultValueCanonical",
                "defaultValueCode",
                "defaultValueCodeableConcept",
                "defaultValueCoding",
                "defaultValueContactDetail",
                "defaultValueContactPoint",
                "defaultValueContributor",
                "defaultValueCount",
                "defaultValueDataRequirement",
                "defaultValueDate",
                "defaultValueDateTime",
                "defaultValueDecimal",
                "defaultValueDistance",
                "defaultValueDosage",
                "defaultValueDuration",
                "defaultValueExpression",
                "defaultValueHumanName",
                "defaultValueId",
                "defaultValueIdentifier",
                "defaultValueInstant",
                "defaultValueInteger",
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
    """ Content to create because of this mapping rule.
    """

    resource_type = Field("StructureMapGroupRuleTarget", const=True)

    context: fhirtypes.Id = Field(
        None,
        alias="context",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Type or variable this rule applies to",
    )

    contextType: fhirtypes.Code = Field(
        None,
        alias="contextType",
        title="Type `Code` (represented as `dict` in JSON)",
        description="type | variable",
    )

    element: fhirtypes.String = Field(
        None,
        alias="element",
        title="Type `String` (represented as `dict` in JSON)",
        description="Field to create in the context",
    )

    listMode: ListType[fhirtypes.Code] = Field(
        None,
        alias="listMode",
        title="List of `Code` items (represented as `dict` in JSON)",
        description="first | share | last | collate",
    )

    listRuleId: fhirtypes.Id = Field(
        None,
        alias="listRuleId",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Internal rule reference for shared list items",
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
        None,
        alias="transform",
        title="Type `Code` (represented as `dict` in JSON)",
        description="create | copy +",
    )

    variable: fhirtypes.Id = Field(
        None,
        alias="variable",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Named context for field, if desired, and a field is specified",
    )


class StructureMapGroupRuleTargetParameter(backboneelement.BackboneElement):
    """ Parameters to the transform.
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

    valueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="valueDecimal",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Parameter value - variable or literal",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueId: fhirtypes.Id = Field(
        None,
        alias="valueId",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Parameter value - variable or literal",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Parameter value - variable or literal",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Type `String` (represented as `dict` in JSON)",
        description="Parameter value - variable or literal",
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
    """ Structure Definition used by this map.
    A structure definition used by this map. The structure definition may
    describe instances that are converted, or the instances that are produced.
    """

    resource_type = Field("StructureMapStructure", const=True)

    alias: fhirtypes.String = Field(
        None,
        alias="alias",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for type in this map",
    )

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String` (represented as `dict` in JSON)",
        description="Documentation on use of structure",
    )

    mode: fhirtypes.Code = Field(
        ...,
        alias="mode",
        title="Type `Code` (represented as `dict` in JSON)",
        description="source | queried | target | produced",
    )

    url: fhirtypes.Canonical = Field(
        ...,
        alias="url",
        title=(
            "Type `Canonical` referencing `StructureDefinition` (represented as "
            "`dict` in JSON)"
        ),
        description="Canonical reference to structure definition",
    )
