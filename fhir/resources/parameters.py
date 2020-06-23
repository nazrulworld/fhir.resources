# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Parameters
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, fhirtypes, resource


class Parameters(resource.Resource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Operation Request or Response.
    This resource is a non-persisted resource used to pass information into and
    back from an [operation](operations.html). It has no other use, and there
    is no RESTful endpoint associated with it.
    """

    resource_type = Field("Parameters", const=True)

    parameter: ListType[fhirtypes.ParametersParameterType] = Field(
        None,
        alias="parameter",
        title="List of `ParametersParameter` items (represented as `dict` in JSON)",
        description="Operation Parameter",
    )


class ParametersParameter(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Operation Parameter.
    A parameter passed to or received from the operation.
    """

    resource_type = Field("ParametersParameter", const=True)

    name: fhirtypes.String = Field(
        ..., alias="name", title="Type `String`", description="Name from the definition"
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    part: ListType[fhirtypes.ParametersParameterType] = Field(
        None,
        alias="part",
        title="List of `ParametersParameter` items (represented as `dict` in JSON)",
        description="Named part of a multi-part parameter",
    )

    resource: fhirtypes.ResourceType = Field(
        None,
        alias="resource",
        title="Type `Resource` (represented as `dict` in JSON)",
        description="If parameter is a whole resource",
    )

    valueAddress: fhirtypes.AddressType = Field(
        None,
        alias="valueAddress",
        title="Type `Address` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueAge: fhirtypes.AgeType = Field(
        None,
        alias="valueAge",
        title="Type `Age` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueAnnotation: fhirtypes.AnnotationType = Field(
        None,
        alias="valueAnnotation",
        title="Type `Annotation` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueBase64Binary: fhirtypes.Base64Binary = Field(
        None,
        alias="valueBase64Binary",
        title="Type `Base64Binary`",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
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
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCanonical: fhirtypes.Canonical = Field(
        None,
        alias="valueCanonical",
        title="Type `Canonical`",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueCanonical", title="Extension field for ``valueCanonical``."
    )

    valueCode: fhirtypes.Code = Field(
        None,
        alias="valueCode",
        title="Type `Code`",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueCode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueCode", title="Extension field for ``valueCode``."
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="valueCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueCoding: fhirtypes.CodingType = Field(
        None,
        alias="valueCoding",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueContactDetail: fhirtypes.ContactDetailType = Field(
        None,
        alias="valueContactDetail",
        title="Type `ContactDetail` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueContactPoint: fhirtypes.ContactPointType = Field(
        None,
        alias="valueContactPoint",
        title="Type `ContactPoint` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueContributor: fhirtypes.ContributorType = Field(
        None,
        alias="valueContributor",
        title="Type `Contributor` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueCount: fhirtypes.CountType = Field(
        None,
        alias="valueCount",
        title="Type `Count` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueDataRequirement: fhirtypes.DataRequirementType = Field(
        None,
        alias="valueDataRequirement",
        title="Type `DataRequirement` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueDate: fhirtypes.Date = Field(
        None,
        alias="valueDate",
        title="Type `Date`",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDate", title="Extension field for ``valueDate``."
    )

    valueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="valueDateTime",
        title="Type `DateTime`",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDateTime", title="Extension field for ``valueDateTime``."
    )

    valueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="valueDecimal",
        title="Type `Decimal`",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDecimal", title="Extension field for ``valueDecimal``."
    )

    valueDistance: fhirtypes.DistanceType = Field(
        None,
        alias="valueDistance",
        title="Type `Distance` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueDosage: fhirtypes.DosageType = Field(
        None,
        alias="valueDosage",
        title="Type `Dosage` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueDuration: fhirtypes.DurationType = Field(
        None,
        alias="valueDuration",
        title="Type `Duration` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueExpression: fhirtypes.ExpressionType = Field(
        None,
        alias="valueExpression",
        title="Type `Expression` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueHumanName: fhirtypes.HumanNameType = Field(
        None,
        alias="valueHumanName",
        title="Type `HumanName` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueId: fhirtypes.Id = Field(
        None,
        alias="valueId",
        title="Type `Id`",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueId", title="Extension field for ``valueId``."
    )

    valueIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="valueIdentifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueInstant: fhirtypes.Instant = Field(
        None,
        alias="valueInstant",
        title="Type `Instant`",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueInstant__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueInstant", title="Extension field for ``valueInstant``."
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="Type `Integer`",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueInteger", title="Extension field for ``valueInteger``."
    )

    valueMarkdown: fhirtypes.Markdown = Field(
        None,
        alias="valueMarkdown",
        title="Type `Markdown`",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueMarkdown", title="Extension field for ``valueMarkdown``."
    )

    valueMeta: fhirtypes.MetaType = Field(
        None,
        alias="valueMeta",
        title="Type `Meta` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueMoney: fhirtypes.MoneyType = Field(
        None,
        alias="valueMoney",
        title="Type `Money` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueOid: fhirtypes.Oid = Field(
        None,
        alias="valueOid",
        title="Type `Oid`",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueOid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueOid", title="Extension field for ``valueOid``."
    )

    valueParameterDefinition: fhirtypes.ParameterDefinitionType = Field(
        None,
        alias="valueParameterDefinition",
        title="Type `ParameterDefinition` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valuePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="valuePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valuePositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="valuePositiveInt",
        title="Type `PositiveInt`",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
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
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueRange: fhirtypes.RangeType = Field(
        None,
        alias="valueRange",
        title="Type `Range` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueRatio: fhirtypes.RatioType = Field(
        None,
        alias="valueRatio",
        title="Type `Ratio` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueReference",
        title="Type `Reference` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueRelatedArtifact: fhirtypes.RelatedArtifactType = Field(
        None,
        alias="valueRelatedArtifact",
        title="Type `RelatedArtifact` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueSampledData: fhirtypes.SampledDataType = Field(
        None,
        alias="valueSampledData",
        title="Type `SampledData` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueSignature: fhirtypes.SignatureType = Field(
        None,
        alias="valueSignature",
        title="Type `Signature` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Type `String`",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    valueTime: fhirtypes.Time = Field(
        None,
        alias="valueTime",
        title="Type `Time`",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueTime", title="Extension field for ``valueTime``."
    )

    valueTiming: fhirtypes.TimingType = Field(
        None,
        alias="valueTiming",
        title="Type `Timing` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueTriggerDefinition: fhirtypes.TriggerDefinitionType = Field(
        None,
        alias="valueTriggerDefinition",
        title="Type `TriggerDefinition` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="valueUnsignedInt",
        title="Type `UnsignedInt`",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
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
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueUri", title="Extension field for ``valueUri``."
    )

    valueUrl: fhirtypes.Url = Field(
        None,
        alias="valueUrl",
        title="Type `Url`",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueUrl__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueUrl", title="Extension field for ``valueUrl``."
    )

    valueUsageContext: fhirtypes.UsageContextType = Field(
        None,
        alias="valueUsageContext",
        title="Type `UsageContext` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueUuid: fhirtypes.Uuid = Field(
        None,
        alias="valueUuid",
        title="Type `Uuid`",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueUuid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueUuid", title="Extension field for ``valueUuid``."
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
                "valueCanonical",
                "valueCode",
                "valueCodeableConcept",
                "valueCoding",
                "valueContactDetail",
                "valueContactPoint",
                "valueContributor",
                "valueCount",
                "valueDataRequirement",
                "valueDate",
                "valueDateTime",
                "valueDecimal",
                "valueDistance",
                "valueDosage",
                "valueDuration",
                "valueExpression",
                "valueHumanName",
                "valueId",
                "valueIdentifier",
                "valueInstant",
                "valueInteger",
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
