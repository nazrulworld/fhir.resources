# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Task
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Task(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A task to be performed.
    """

    resource_type = Field("Task", const=True)

    authoredOn: fhirtypes.DateTime = Field(
        None,
        alias="authoredOn",
        title="Type `DateTime`",
        description="Task Creation Date",
    )
    authoredOn__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_authoredOn", title="Extension field for ``authoredOn``."
    )

    basedOn: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="Request fulfilled by this task",
    )

    businessStatus: fhirtypes.CodeableConceptType = Field(
        None,
        alias="businessStatus",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description='E.g. "Specimen collected", "IV prepped"',
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Task Type",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Human-readable explanation of task",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title=(
            "Type `Reference` referencing `Encounter` (represented as `dict` in "
            "JSON)"
        ),
        description="Healthcare event during which this task originated",
    )

    executionPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="executionPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Start and end time of execution",
    )

    focus: fhirtypes.ReferenceType = Field(
        None,
        alias="focus",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="What task is acting on",
    )

    for_fhir: fhirtypes.ReferenceType = Field(
        None,
        alias="for",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Beneficiary of the Task",
    )

    groupIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="groupIdentifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Requisition or grouper id",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Task Instance Identifier",
    )

    input: ListType[fhirtypes.TaskInputType] = Field(
        None,
        alias="input",
        title="List of `TaskInput` items (represented as `dict` in JSON)",
        description="Information used to perform task",
    )

    instantiatesCanonical: fhirtypes.Canonical = Field(
        None,
        alias="instantiatesCanonical",
        title="Type `Canonical` referencing `ActivityDefinition`",
        description="Formal definition of task",
    )
    instantiatesCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_instantiatesCanonical",
        title="Extension field for ``instantiatesCanonical``.",
    )

    instantiatesUri: fhirtypes.Uri = Field(
        None,
        alias="instantiatesUri",
        title="Type `Uri`",
        description="Formal definition of task",
    )
    instantiatesUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_instantiatesUri", title="Extension field for ``instantiatesUri``."
    )

    insurance: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="insurance",
        title=(
            "List of `Reference` items referencing `Coverage, ClaimResponse` "
            "(represented as `dict` in JSON)"
        ),
        description="Associated insurance coverage",
    )

    intent: fhirtypes.Code = Field(
        ...,
        alias="intent",
        title="Type `Code`",
        description=(
            "unknown | proposal | plan | order | original-order | reflex-order | "
            "filler-order | instance-order | option"
        ),
    )
    intent__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_intent", title="Extension field for ``intent``."
    )

    lastModified: fhirtypes.DateTime = Field(
        None,
        alias="lastModified",
        title="Type `DateTime`",
        description="Task Last Modified Date",
    )
    lastModified__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastModified", title="Extension field for ``lastModified``."
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title=(
            "Type `Reference` referencing `Location` (represented as `dict` in " "JSON)"
        ),
        description="Where task occurs",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Comments made about the task",
    )

    output: ListType[fhirtypes.TaskOutputType] = Field(
        None,
        alias="output",
        title="List of `TaskOutput` items (represented as `dict` in JSON)",
        description="Information produced as part of task",
    )

    owner: fhirtypes.ReferenceType = Field(
        None,
        alias="owner",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole, "
            "Organization, CareTeam, HealthcareService, Patient, Device, "
            "RelatedPerson` (represented as `dict` in JSON)"
        ),
        description="Responsible individual",
    )

    partOf: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title=(
            "List of `Reference` items referencing `Task` (represented as `dict` in"
            " JSON)"
        ),
        description="Composite task",
    )

    performerType: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="performerType",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Requested performer",
    )

    priority: fhirtypes.Code = Field(
        None,
        alias="priority",
        title="Type `Code`",
        description="routine | urgent | asap | stat",
    )
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_priority", title="Extension field for ``priority``."
    )

    reasonCode: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reasonCode",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Why task is needed",
    )

    reasonReference: fhirtypes.ReferenceType = Field(
        None,
        alias="reasonReference",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Why task is needed",
    )

    relevantHistory: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="relevantHistory",
        title=(
            "List of `Reference` items referencing `Provenance` (represented as "
            "`dict` in JSON)"
        ),
        description="Key events in history of the Task",
    )

    requester: fhirtypes.ReferenceType = Field(
        None,
        alias="requester",
        title=(
            "Type `Reference` referencing `Device, Organization, Patient, "
            "Practitioner, PractitionerRole, RelatedPerson` (represented as `dict` "
            "in JSON)"
        ),
        description="Who is asking for task to be done",
    )

    restriction: fhirtypes.TaskRestrictionType = Field(
        None,
        alias="restriction",
        title="Type `TaskRestriction` (represented as `dict` in JSON)",
        description="Constraints on fulfillment tasks",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`",
        description="draft | requested | received | accepted | +",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    statusReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="statusReason",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Reason for current status",
    )


class TaskInput(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information used to perform task.
    Additional information that may be needed in the execution of the task.
    """

    resource_type = Field("TaskInput", const=True)

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Label for the input",
    )

    valueAddress: fhirtypes.AddressType = Field(
        None,
        alias="valueAddress",
        title="Type `Address` (represented as `dict` in JSON)",
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueAge: fhirtypes.AgeType = Field(
        None,
        alias="valueAge",
        title="Type `Age` (represented as `dict` in JSON)",
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueAnnotation: fhirtypes.AnnotationType = Field(
        None,
        alias="valueAnnotation",
        title="Type `Annotation` (represented as `dict` in JSON)",
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueBase64Binary: fhirtypes.Base64Binary = Field(
        None,
        alias="valueBase64Binary",
        title="Type `Base64Binary`",
        description="Content to use in performing the task",
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
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCanonical: fhirtypes.Canonical = Field(
        None,
        alias="valueCanonical",
        title="Type `Canonical`",
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueCanonical", title="Extension field for ``valueCanonical``."
    )

    valueCode: fhirtypes.Code = Field(
        None,
        alias="valueCode",
        title="Type `Code`",
        description="Content to use in performing the task",
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
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueCoding: fhirtypes.CodingType = Field(
        None,
        alias="valueCoding",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueContactDetail: fhirtypes.ContactDetailType = Field(
        None,
        alias="valueContactDetail",
        title="Type `ContactDetail` (represented as `dict` in JSON)",
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueContactPoint: fhirtypes.ContactPointType = Field(
        None,
        alias="valueContactPoint",
        title="Type `ContactPoint` (represented as `dict` in JSON)",
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueContributor: fhirtypes.ContributorType = Field(
        None,
        alias="valueContributor",
        title="Type `Contributor` (represented as `dict` in JSON)",
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueCount: fhirtypes.CountType = Field(
        None,
        alias="valueCount",
        title="Type `Count` (represented as `dict` in JSON)",
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueDataRequirement: fhirtypes.DataRequirementType = Field(
        None,
        alias="valueDataRequirement",
        title="Type `DataRequirement` (represented as `dict` in JSON)",
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueDate: fhirtypes.Date = Field(
        None,
        alias="valueDate",
        title="Type `Date`",
        description="Content to use in performing the task",
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
        description="Content to use in performing the task",
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
        description="Content to use in performing the task",
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
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueDosage: fhirtypes.DosageType = Field(
        None,
        alias="valueDosage",
        title="Type `Dosage` (represented as `dict` in JSON)",
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueDuration: fhirtypes.DurationType = Field(
        None,
        alias="valueDuration",
        title="Type `Duration` (represented as `dict` in JSON)",
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueExpression: fhirtypes.ExpressionType = Field(
        None,
        alias="valueExpression",
        title="Type `Expression` (represented as `dict` in JSON)",
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueHumanName: fhirtypes.HumanNameType = Field(
        None,
        alias="valueHumanName",
        title="Type `HumanName` (represented as `dict` in JSON)",
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueId: fhirtypes.Id = Field(
        None,
        alias="valueId",
        title="Type `Id`",
        description="Content to use in performing the task",
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
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueInstant: fhirtypes.Instant = Field(
        None,
        alias="valueInstant",
        title="Type `Instant`",
        description="Content to use in performing the task",
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
        description="Content to use in performing the task",
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
        description="Content to use in performing the task",
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
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueMoney: fhirtypes.MoneyType = Field(
        None,
        alias="valueMoney",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueOid: fhirtypes.Oid = Field(
        None,
        alias="valueOid",
        title="Type `Oid`",
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueOid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueOid", title="Extension field for ``valueOid``."
    )

    valueParameterDefinition: fhirtypes.ParameterDefinitionType = Field(
        None,
        alias="valueParameterDefinition",
        title="Type `ParameterDefinition` (represented as `dict` in JSON)",
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valuePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="valuePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valuePositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="valuePositiveInt",
        title="Type `PositiveInt`",
        description="Content to use in performing the task",
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
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueRange: fhirtypes.RangeType = Field(
        None,
        alias="valueRange",
        title="Type `Range` (represented as `dict` in JSON)",
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueRatio: fhirtypes.RatioType = Field(
        None,
        alias="valueRatio",
        title="Type `Ratio` (represented as `dict` in JSON)",
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueReference",
        title="Type `Reference` (represented as `dict` in JSON)",
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueRelatedArtifact: fhirtypes.RelatedArtifactType = Field(
        None,
        alias="valueRelatedArtifact",
        title="Type `RelatedArtifact` (represented as `dict` in JSON)",
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueSampledData: fhirtypes.SampledDataType = Field(
        None,
        alias="valueSampledData",
        title="Type `SampledData` (represented as `dict` in JSON)",
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueSignature: fhirtypes.SignatureType = Field(
        None,
        alias="valueSignature",
        title="Type `Signature` (represented as `dict` in JSON)",
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Type `String`",
        description="Content to use in performing the task",
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
        description="Content to use in performing the task",
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
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueTriggerDefinition: fhirtypes.TriggerDefinitionType = Field(
        None,
        alias="valueTriggerDefinition",
        title="Type `TriggerDefinition` (represented as `dict` in JSON)",
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="valueUnsignedInt",
        title="Type `UnsignedInt`",
        description="Content to use in performing the task",
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
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueUri", title="Extension field for ``valueUri``."
    )

    valueUrl: fhirtypes.Url = Field(
        None,
        alias="valueUrl",
        title="Type `Url`",
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueUrl__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueUrl", title="Extension field for ``valueUrl``."
    )

    valueUsageContext: fhirtypes.UsageContextType = Field(
        None,
        alias="valueUsageContext",
        title="Type `UsageContext` (represented as `dict` in JSON)",
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueUuid: fhirtypes.Uuid = Field(
        None,
        alias="valueUuid",
        title="Type `Uuid`",
        description="Content to use in performing the task",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
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


class TaskOutput(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information produced as part of task.
    Outputs produced by the Task.
    """

    resource_type = Field("TaskOutput", const=True)

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Label for output",
    )

    valueAddress: fhirtypes.AddressType = Field(
        None,
        alias="valueAddress",
        title="Type `Address` (represented as `dict` in JSON)",
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueAge: fhirtypes.AgeType = Field(
        None,
        alias="valueAge",
        title="Type `Age` (represented as `dict` in JSON)",
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueAnnotation: fhirtypes.AnnotationType = Field(
        None,
        alias="valueAnnotation",
        title="Type `Annotation` (represented as `dict` in JSON)",
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueBase64Binary: fhirtypes.Base64Binary = Field(
        None,
        alias="valueBase64Binary",
        title="Type `Base64Binary`",
        description="Result of output",
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
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCanonical: fhirtypes.Canonical = Field(
        None,
        alias="valueCanonical",
        title="Type `Canonical`",
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueCanonical", title="Extension field for ``valueCanonical``."
    )

    valueCode: fhirtypes.Code = Field(
        None,
        alias="valueCode",
        title="Type `Code`",
        description="Result of output",
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
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueCoding: fhirtypes.CodingType = Field(
        None,
        alias="valueCoding",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueContactDetail: fhirtypes.ContactDetailType = Field(
        None,
        alias="valueContactDetail",
        title="Type `ContactDetail` (represented as `dict` in JSON)",
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueContactPoint: fhirtypes.ContactPointType = Field(
        None,
        alias="valueContactPoint",
        title="Type `ContactPoint` (represented as `dict` in JSON)",
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueContributor: fhirtypes.ContributorType = Field(
        None,
        alias="valueContributor",
        title="Type `Contributor` (represented as `dict` in JSON)",
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueCount: fhirtypes.CountType = Field(
        None,
        alias="valueCount",
        title="Type `Count` (represented as `dict` in JSON)",
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueDataRequirement: fhirtypes.DataRequirementType = Field(
        None,
        alias="valueDataRequirement",
        title="Type `DataRequirement` (represented as `dict` in JSON)",
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueDate: fhirtypes.Date = Field(
        None,
        alias="valueDate",
        title="Type `Date`",
        description="Result of output",
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
        description="Result of output",
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
        description="Result of output",
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
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueDosage: fhirtypes.DosageType = Field(
        None,
        alias="valueDosage",
        title="Type `Dosage` (represented as `dict` in JSON)",
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueDuration: fhirtypes.DurationType = Field(
        None,
        alias="valueDuration",
        title="Type `Duration` (represented as `dict` in JSON)",
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueExpression: fhirtypes.ExpressionType = Field(
        None,
        alias="valueExpression",
        title="Type `Expression` (represented as `dict` in JSON)",
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueHumanName: fhirtypes.HumanNameType = Field(
        None,
        alias="valueHumanName",
        title="Type `HumanName` (represented as `dict` in JSON)",
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueId: fhirtypes.Id = Field(
        None,
        alias="valueId",
        title="Type `Id`",
        description="Result of output",
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
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueInstant: fhirtypes.Instant = Field(
        None,
        alias="valueInstant",
        title="Type `Instant`",
        description="Result of output",
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
        description="Result of output",
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
        description="Result of output",
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
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueMoney: fhirtypes.MoneyType = Field(
        None,
        alias="valueMoney",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueOid: fhirtypes.Oid = Field(
        None,
        alias="valueOid",
        title="Type `Oid`",
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueOid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueOid", title="Extension field for ``valueOid``."
    )

    valueParameterDefinition: fhirtypes.ParameterDefinitionType = Field(
        None,
        alias="valueParameterDefinition",
        title="Type `ParameterDefinition` (represented as `dict` in JSON)",
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valuePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="valuePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valuePositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="valuePositiveInt",
        title="Type `PositiveInt`",
        description="Result of output",
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
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueRange: fhirtypes.RangeType = Field(
        None,
        alias="valueRange",
        title="Type `Range` (represented as `dict` in JSON)",
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueRatio: fhirtypes.RatioType = Field(
        None,
        alias="valueRatio",
        title="Type `Ratio` (represented as `dict` in JSON)",
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueReference",
        title="Type `Reference` (represented as `dict` in JSON)",
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueRelatedArtifact: fhirtypes.RelatedArtifactType = Field(
        None,
        alias="valueRelatedArtifact",
        title="Type `RelatedArtifact` (represented as `dict` in JSON)",
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueSampledData: fhirtypes.SampledDataType = Field(
        None,
        alias="valueSampledData",
        title="Type `SampledData` (represented as `dict` in JSON)",
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueSignature: fhirtypes.SignatureType = Field(
        None,
        alias="valueSignature",
        title="Type `Signature` (represented as `dict` in JSON)",
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Type `String`",
        description="Result of output",
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
        description="Result of output",
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
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueTriggerDefinition: fhirtypes.TriggerDefinitionType = Field(
        None,
        alias="valueTriggerDefinition",
        title="Type `TriggerDefinition` (represented as `dict` in JSON)",
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="valueUnsignedInt",
        title="Type `UnsignedInt`",
        description="Result of output",
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
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueUri", title="Extension field for ``valueUri``."
    )

    valueUrl: fhirtypes.Url = Field(
        None,
        alias="valueUrl",
        title="Type `Url`",
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueUrl__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueUrl", title="Extension field for ``valueUrl``."
    )

    valueUsageContext: fhirtypes.UsageContextType = Field(
        None,
        alias="valueUsageContext",
        title="Type `UsageContext` (represented as `dict` in JSON)",
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueUuid: fhirtypes.Uuid = Field(
        None,
        alias="valueUuid",
        title="Type `Uuid`",
        description="Result of output",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
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


class TaskRestriction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Constraints on fulfillment tasks.
    If the Task.focus is a request resource and the task is seeking fulfillment
    (i.e. is asking for the request to be actioned), this element identifies
    any limitations on what parts of the referenced request should be actioned.
    """

    resource_type = Field("TaskRestriction", const=True)

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When fulfillment sought",
    )

    recipient: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="recipient",
        title=(
            "List of `Reference` items referencing `Patient, Practitioner, "
            "PractitionerRole, RelatedPerson, Group, Organization` (represented as "
            "`dict` in JSON)"
        ),
        description="For whom is fulfillment sought?",
    )

    repetitions: fhirtypes.PositiveInt = Field(
        None,
        alias="repetitions",
        title="Type `PositiveInt`",
        description="How many times to repeat",
    )
    repetitions__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_repetitions", title="Extension field for ``repetitions``."
    )
