#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Task) on 2019-05-13.
#  2019, SMART Health IT.


from . import domainresource

class Task(domainresource.DomainResource):
    """ A task to be performed.
    """

    resource_type = "Task"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.authoredOn = None
        """ Task Creation Date.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.basedOn = None
        """ Request fulfilled by this task.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.businessStatus = None
        """ E.g. "Specimen collected", "IV prepped".
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.code = None
        """ Task Type.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.description = None
        """ Human-readable explanation of task.
        Type `str`. """

        self.encounter = None
        """ Healthcare event during which this task originated.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.executionPeriod = None
        """ Start and end time of execution.
        Type `Period` (represented as `dict` in JSON). """

        self.focus = None
        """ What task is acting on.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.for_fhir = None
        """ Beneficiary of the Task.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.groupIdentifier = None
        """ Requisition or grouper id.
        Type `Identifier` (represented as `dict` in JSON). """

        self.identifier = None
        """ Task Instance Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.input = None
        """ Information used to perform task.
        List of `TaskInput` items (represented as `dict` in JSON). """

        self.instantiatesCanonical = None
        """ Formal definition of task.
        Type `str`. """

        self.instantiatesUri = None
        """ Formal definition of task.
        Type `str`. """

        self.insurance = None
        """ Associated insurance coverage.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.intent = None
        """ unknown | proposal | plan | order | original-order | reflex-order |
        filler-order | instance-order | option.
        Type `str`. """

        self.lastModified = None
        """ Task Last Modified Date.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.location = None
        """ Where task occurs.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.note = None
        """ Comments made about the task.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.output = None
        """ Information produced as part of task.
        List of `TaskOutput` items (represented as `dict` in JSON). """

        self.owner = None
        """ Responsible individual.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.partOf = None
        """ Composite task.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.performerType = None
        """ Requested performer.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.priority = None
        """ routine | urgent | asap | stat.
        Type `str`. """

        self.reasonCode = None
        """ Why task is needed.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.reasonReference = None
        """ Why task is needed.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.relevantHistory = None
        """ Key events in history of the Task.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.requester = None
        """ Who is asking for task to be done.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.restriction = None
        """ Constraints on fulfillment tasks.
        Type `TaskRestriction` (represented as `dict` in JSON). """

        self.status = None
        """ draft | requested | received | accepted | +.
        Type `str`. """

        self.statusReason = None
        """ Reason for current status.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(Task, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Task, self).elementProperties()
        js.extend([
            ("authoredOn", "authoredOn", fhirdate.FHIRDate, "dateTime", False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, "Reference", True, None, False),
            ("businessStatus", "businessStatus", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
            ("description", "description", str, "string", False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, "Reference", False, None, False),
            ("executionPeriod", "executionPeriod", period.Period, "Period", False, None, False),
            ("focus", "focus", fhirreference.FHIRReference, "Reference", False, None, False),
            ("for_fhir", "for", fhirreference.FHIRReference, "Reference", False, None, False),
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, "Identifier", False, None, False),
            ("identifier", "identifier", identifier.Identifier, "Identifier", True, None, False),
            ("input", "input", TaskInput, "TaskInput", True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, "canonical", False, None, False),
            ("instantiatesUri", "instantiatesUri", str, "uri", False, None, False),
            ("insurance", "insurance", fhirreference.FHIRReference, "Reference", True, None, False),
            ("intent", "intent", str, "code", False, None, True),
            ("lastModified", "lastModified", fhirdate.FHIRDate, "dateTime", False, None, False),
            ("location", "location", fhirreference.FHIRReference, "Reference", False, None, False),
            ("note", "note", annotation.Annotation, "Annotation", True, None, False),
            ("output", "output", TaskOutput, "TaskOutput", True, None, False),
            ("owner", "owner", fhirreference.FHIRReference, "Reference", False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, "Reference", True, None, False),
            ("performerType", "performerType", codeableconcept.CodeableConcept, "CodeableConcept", True, None, False),
            ("priority", "priority", str, "code", False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, "Reference", False, None, False),
            ("relevantHistory", "relevantHistory", fhirreference.FHIRReference, "Reference", True, None, False),
            ("requester", "requester", fhirreference.FHIRReference, "Reference", False, None, False),
            ("restriction", "restriction", TaskRestriction, "TaskRestriction", False, None, False),
            ("status", "status", str, "code", False, None, True),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
        ])
        return js


from . import backboneelement

class TaskInput(backboneelement.BackboneElement):
    """ Information used to perform task.

    Additional information that may be needed in the execution of the task.
    """

    resource_type = "TaskInput"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.type = None
        """ Label for the input.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.valueAddress = None
        """ Content to use in performing the task.
        Type `Address` (represented as `dict` in JSON). """

        self.valueAge = None
        """ Content to use in performing the task.
        Type `Age` (represented as `dict` in JSON). """

        self.valueAnnotation = None
        """ Content to use in performing the task.
        Type `Annotation` (represented as `dict` in JSON). """

        self.valueAttachment = None
        """ Content to use in performing the task.
        Type `Attachment` (represented as `dict` in JSON). """

        self.valueBase64Binary = None
        """ Content to use in performing the task.
        Type `str`. """

        self.valueBoolean = None
        """ Content to use in performing the task.
        Type `bool`. """

        self.valueCanonical = None
        """ Content to use in performing the task.
        Type `str`. """

        self.valueCode = None
        """ Content to use in performing the task.
        Type `str`. """

        self.valueCodeableConcept = None
        """ Content to use in performing the task.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.valueCoding = None
        """ Content to use in performing the task.
        Type `Coding` (represented as `dict` in JSON). """

        self.valueContactDetail = None
        """ Content to use in performing the task.
        Type `ContactDetail` (represented as `dict` in JSON). """

        self.valueContactPoint = None
        """ Content to use in performing the task.
        Type `ContactPoint` (represented as `dict` in JSON). """

        self.valueContributor = None
        """ Content to use in performing the task.
        Type `Contributor` (represented as `dict` in JSON). """

        self.valueCount = None
        """ Content to use in performing the task.
        Type `Count` (represented as `dict` in JSON). """

        self.valueDataRequirement = None
        """ Content to use in performing the task.
        Type `DataRequirement` (represented as `dict` in JSON). """

        self.valueDate = None
        """ Content to use in performing the task.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.valueDateTime = None
        """ Content to use in performing the task.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.valueDecimal = None
        """ Content to use in performing the task.
        Type `float`. """

        self.valueDistance = None
        """ Content to use in performing the task.
        Type `Distance` (represented as `dict` in JSON). """

        self.valueDosage = None
        """ Content to use in performing the task.
        Type `Dosage` (represented as `dict` in JSON). """

        self.valueDuration = None
        """ Content to use in performing the task.
        Type `Duration` (represented as `dict` in JSON). """

        self.valueExpression = None
        """ Content to use in performing the task.
        Type `Expression` (represented as `dict` in JSON). """

        self.valueHumanName = None
        """ Content to use in performing the task.
        Type `HumanName` (represented as `dict` in JSON). """

        self.valueId = None
        """ Content to use in performing the task.
        Type `str`. """

        self.valueIdentifier = None
        """ Content to use in performing the task.
        Type `Identifier` (represented as `dict` in JSON). """

        self.valueInstant = None
        """ Content to use in performing the task.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.valueInteger = None
        """ Content to use in performing the task.
        Type `int`. """

        self.valueMarkdown = None
        """ Content to use in performing the task.
        Type `str`. """

        self.valueMoney = None
        """ Content to use in performing the task.
        Type `Money` (represented as `dict` in JSON). """

        self.valueOid = None
        """ Content to use in performing the task.
        Type `str`. """

        self.valueParameterDefinition = None
        """ Content to use in performing the task.
        Type `ParameterDefinition` (represented as `dict` in JSON). """

        self.valuePeriod = None
        """ Content to use in performing the task.
        Type `Period` (represented as `dict` in JSON). """

        self.valuePositiveInt = None
        """ Content to use in performing the task.
        Type `int`. """

        self.valueQuantity = None
        """ Content to use in performing the task.
        Type `Quantity` (represented as `dict` in JSON). """

        self.valueRange = None
        """ Content to use in performing the task.
        Type `Range` (represented as `dict` in JSON). """

        self.valueRatio = None
        """ Content to use in performing the task.
        Type `Ratio` (represented as `dict` in JSON). """

        self.valueReference = None
        """ Content to use in performing the task.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.valueRelatedArtifact = None
        """ Content to use in performing the task.
        Type `RelatedArtifact` (represented as `dict` in JSON). """

        self.valueSampledData = None
        """ Content to use in performing the task.
        Type `SampledData` (represented as `dict` in JSON). """

        self.valueSignature = None
        """ Content to use in performing the task.
        Type `Signature` (represented as `dict` in JSON). """

        self.valueString = None
        """ Content to use in performing the task.
        Type `str`. """

        self.valueTime = None
        """ Content to use in performing the task.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.valueTiming = None
        """ Content to use in performing the task.
        Type `Timing` (represented as `dict` in JSON). """

        self.valueTriggerDefinition = None
        """ Content to use in performing the task.
        Type `TriggerDefinition` (represented as `dict` in JSON). """

        self.valueUnsignedInt = None
        """ Content to use in performing the task.
        Type `int`. """

        self.valueUri = None
        """ Content to use in performing the task.
        Type `str`. """

        self.valueUrl = None
        """ Content to use in performing the task.
        Type `str`. """

        self.valueUsageContext = None
        """ Content to use in performing the task.
        Type `UsageContext` (represented as `dict` in JSON). """

        self.valueUuid = None
        """ Content to use in performing the task.
        Type `str`. """

        super(TaskInput, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(TaskInput, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, "CodeableConcept", False, None, True),
            ("valueAddress", "valueAddress", address.Address, "Address", False, "value", True),
            ("valueAge", "valueAge", age.Age, "Age", False, "value", True),
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, "Annotation", False, "value", True),
            ("valueAttachment", "valueAttachment", attachment.Attachment, "Attachment", False, "value", True),
            ("valueBase64Binary", "valueBase64Binary", str, "base64Binary", False, "value", True),
            ("valueBoolean", "valueBoolean", bool, "boolean", False, "value", True),
            ("valueCanonical", "valueCanonical", str, "canonical", False, "value", True),
            ("valueCode", "valueCode", str, "code", False, "value", True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, "CodeableConcept", False, "value", True),
            ("valueCoding", "valueCoding", coding.Coding, "Coding", False, "value", True),
            ("valueContactDetail", "valueContactDetail", contactdetail.ContactDetail, "ContactDetail", False, "value", True),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, "ContactPoint", False, "value", True),
            ("valueContributor", "valueContributor", contributor.Contributor, "Contributor", False, "value", True),
            ("valueCount", "valueCount", count.Count, "Count", False, "value", True),
            ("valueDataRequirement", "valueDataRequirement", datarequirement.DataRequirement, "DataRequirement", False, "value", True),
            ("valueDate", "valueDate", fhirdate.FHIRDate, "date", False, "value", True),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, "dateTime", False, "value", True),
            ("valueDecimal", "valueDecimal", float, "decimal", False, "value", True),
            ("valueDistance", "valueDistance", distance.Distance, "Distance", False, "value", True),
            ("valueDosage", "valueDosage", dosage.Dosage, "Dosage", False, "value", True),
            ("valueDuration", "valueDuration", duration.Duration, "Duration", False, "value", True),
            ("valueExpression", "valueExpression", expression.Expression, "Expression", False, "value", True),
            ("valueHumanName", "valueHumanName", humanname.HumanName, "HumanName", False, "value", True),
            ("valueId", "valueId", str, "id", False, "value", True),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, "Identifier", False, "value", True),
            ("valueInstant", "valueInstant", fhirdate.FHIRDate, "instant", False, "value", True),
            ("valueInteger", "valueInteger", int, "integer", False, "value", True),
            ("valueMarkdown", "valueMarkdown", str, "markdown", False, "value", True),
            ("valueMoney", "valueMoney", money.Money, "Money", False, "value", True),
            ("valueOid", "valueOid", str, "oid", False, "value", True),
            ("valueParameterDefinition", "valueParameterDefinition", parameterdefinition.ParameterDefinition, "ParameterDefinition", False, "value", True),
            ("valuePeriod", "valuePeriod", period.Period, "Period", False, "value", True),
            ("valuePositiveInt", "valuePositiveInt", int, "positiveInt", False, "value", True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, "Quantity", False, "value", True),
            ("valueRange", "valueRange", range.Range, "Range", False, "value", True),
            ("valueRatio", "valueRatio", ratio.Ratio, "Ratio", False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, "Reference", False, "value", True),
            ("valueRelatedArtifact", "valueRelatedArtifact", relatedartifact.RelatedArtifact, "RelatedArtifact", False, "value", True),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, "SampledData", False, "value", True),
            ("valueSignature", "valueSignature", signature.Signature, "Signature", False, "value", True),
            ("valueString", "valueString", str, "string", False, "value", True),
            ("valueTime", "valueTime", fhirdate.FHIRDate, "time", False, "value", True),
            ("valueTiming", "valueTiming", timing.Timing, "Timing", False, "value", True),
            ("valueTriggerDefinition", "valueTriggerDefinition", triggerdefinition.TriggerDefinition, "TriggerDefinition", False, "value", True),
            ("valueUnsignedInt", "valueUnsignedInt", int, "unsignedInt", False, "value", True),
            ("valueUri", "valueUri", str, "uri", False, "value", True),
            ("valueUrl", "valueUrl", str, "url", False, "value", True),
            ("valueUsageContext", "valueUsageContext", usagecontext.UsageContext, "UsageContext", False, "value", True),
            ("valueUuid", "valueUuid", str, "uuid", False, "value", True),
        ])
        return js


class TaskOutput(backboneelement.BackboneElement):
    """ Information produced as part of task.

    Outputs produced by the Task.
    """

    resource_type = "TaskOutput"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.type = None
        """ Label for output.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.valueAddress = None
        """ Result of output.
        Type `Address` (represented as `dict` in JSON). """

        self.valueAge = None
        """ Result of output.
        Type `Age` (represented as `dict` in JSON). """

        self.valueAnnotation = None
        """ Result of output.
        Type `Annotation` (represented as `dict` in JSON). """

        self.valueAttachment = None
        """ Result of output.
        Type `Attachment` (represented as `dict` in JSON). """

        self.valueBase64Binary = None
        """ Result of output.
        Type `str`. """

        self.valueBoolean = None
        """ Result of output.
        Type `bool`. """

        self.valueCanonical = None
        """ Result of output.
        Type `str`. """

        self.valueCode = None
        """ Result of output.
        Type `str`. """

        self.valueCodeableConcept = None
        """ Result of output.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.valueCoding = None
        """ Result of output.
        Type `Coding` (represented as `dict` in JSON). """

        self.valueContactDetail = None
        """ Result of output.
        Type `ContactDetail` (represented as `dict` in JSON). """

        self.valueContactPoint = None
        """ Result of output.
        Type `ContactPoint` (represented as `dict` in JSON). """

        self.valueContributor = None
        """ Result of output.
        Type `Contributor` (represented as `dict` in JSON). """

        self.valueCount = None
        """ Result of output.
        Type `Count` (represented as `dict` in JSON). """

        self.valueDataRequirement = None
        """ Result of output.
        Type `DataRequirement` (represented as `dict` in JSON). """

        self.valueDate = None
        """ Result of output.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.valueDateTime = None
        """ Result of output.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.valueDecimal = None
        """ Result of output.
        Type `float`. """

        self.valueDistance = None
        """ Result of output.
        Type `Distance` (represented as `dict` in JSON). """

        self.valueDosage = None
        """ Result of output.
        Type `Dosage` (represented as `dict` in JSON). """

        self.valueDuration = None
        """ Result of output.
        Type `Duration` (represented as `dict` in JSON). """

        self.valueExpression = None
        """ Result of output.
        Type `Expression` (represented as `dict` in JSON). """

        self.valueHumanName = None
        """ Result of output.
        Type `HumanName` (represented as `dict` in JSON). """

        self.valueId = None
        """ Result of output.
        Type `str`. """

        self.valueIdentifier = None
        """ Result of output.
        Type `Identifier` (represented as `dict` in JSON). """

        self.valueInstant = None
        """ Result of output.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.valueInteger = None
        """ Result of output.
        Type `int`. """

        self.valueMarkdown = None
        """ Result of output.
        Type `str`. """

        self.valueMoney = None
        """ Result of output.
        Type `Money` (represented as `dict` in JSON). """

        self.valueOid = None
        """ Result of output.
        Type `str`. """

        self.valueParameterDefinition = None
        """ Result of output.
        Type `ParameterDefinition` (represented as `dict` in JSON). """

        self.valuePeriod = None
        """ Result of output.
        Type `Period` (represented as `dict` in JSON). """

        self.valuePositiveInt = None
        """ Result of output.
        Type `int`. """

        self.valueQuantity = None
        """ Result of output.
        Type `Quantity` (represented as `dict` in JSON). """

        self.valueRange = None
        """ Result of output.
        Type `Range` (represented as `dict` in JSON). """

        self.valueRatio = None
        """ Result of output.
        Type `Ratio` (represented as `dict` in JSON). """

        self.valueReference = None
        """ Result of output.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.valueRelatedArtifact = None
        """ Result of output.
        Type `RelatedArtifact` (represented as `dict` in JSON). """

        self.valueSampledData = None
        """ Result of output.
        Type `SampledData` (represented as `dict` in JSON). """

        self.valueSignature = None
        """ Result of output.
        Type `Signature` (represented as `dict` in JSON). """

        self.valueString = None
        """ Result of output.
        Type `str`. """

        self.valueTime = None
        """ Result of output.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.valueTiming = None
        """ Result of output.
        Type `Timing` (represented as `dict` in JSON). """

        self.valueTriggerDefinition = None
        """ Result of output.
        Type `TriggerDefinition` (represented as `dict` in JSON). """

        self.valueUnsignedInt = None
        """ Result of output.
        Type `int`. """

        self.valueUri = None
        """ Result of output.
        Type `str`. """

        self.valueUrl = None
        """ Result of output.
        Type `str`. """

        self.valueUsageContext = None
        """ Result of output.
        Type `UsageContext` (represented as `dict` in JSON). """

        self.valueUuid = None
        """ Result of output.
        Type `str`. """

        super(TaskOutput, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(TaskOutput, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, "CodeableConcept", False, None, True),
            ("valueAddress", "valueAddress", address.Address, "Address", False, "value", True),
            ("valueAge", "valueAge", age.Age, "Age", False, "value", True),
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, "Annotation", False, "value", True),
            ("valueAttachment", "valueAttachment", attachment.Attachment, "Attachment", False, "value", True),
            ("valueBase64Binary", "valueBase64Binary", str, "base64Binary", False, "value", True),
            ("valueBoolean", "valueBoolean", bool, "boolean", False, "value", True),
            ("valueCanonical", "valueCanonical", str, "canonical", False, "value", True),
            ("valueCode", "valueCode", str, "code", False, "value", True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, "CodeableConcept", False, "value", True),
            ("valueCoding", "valueCoding", coding.Coding, "Coding", False, "value", True),
            ("valueContactDetail", "valueContactDetail", contactdetail.ContactDetail, "ContactDetail", False, "value", True),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, "ContactPoint", False, "value", True),
            ("valueContributor", "valueContributor", contributor.Contributor, "Contributor", False, "value", True),
            ("valueCount", "valueCount", count.Count, "Count", False, "value", True),
            ("valueDataRequirement", "valueDataRequirement", datarequirement.DataRequirement, "DataRequirement", False, "value", True),
            ("valueDate", "valueDate", fhirdate.FHIRDate, "date", False, "value", True),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, "dateTime", False, "value", True),
            ("valueDecimal", "valueDecimal", float, "decimal", False, "value", True),
            ("valueDistance", "valueDistance", distance.Distance, "Distance", False, "value", True),
            ("valueDosage", "valueDosage", dosage.Dosage, "Dosage", False, "value", True),
            ("valueDuration", "valueDuration", duration.Duration, "Duration", False, "value", True),
            ("valueExpression", "valueExpression", expression.Expression, "Expression", False, "value", True),
            ("valueHumanName", "valueHumanName", humanname.HumanName, "HumanName", False, "value", True),
            ("valueId", "valueId", str, "id", False, "value", True),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, "Identifier", False, "value", True),
            ("valueInstant", "valueInstant", fhirdate.FHIRDate, "instant", False, "value", True),
            ("valueInteger", "valueInteger", int, "integer", False, "value", True),
            ("valueMarkdown", "valueMarkdown", str, "markdown", False, "value", True),
            ("valueMoney", "valueMoney", money.Money, "Money", False, "value", True),
            ("valueOid", "valueOid", str, "oid", False, "value", True),
            ("valueParameterDefinition", "valueParameterDefinition", parameterdefinition.ParameterDefinition, "ParameterDefinition", False, "value", True),
            ("valuePeriod", "valuePeriod", period.Period, "Period", False, "value", True),
            ("valuePositiveInt", "valuePositiveInt", int, "positiveInt", False, "value", True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, "Quantity", False, "value", True),
            ("valueRange", "valueRange", range.Range, "Range", False, "value", True),
            ("valueRatio", "valueRatio", ratio.Ratio, "Ratio", False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, "Reference", False, "value", True),
            ("valueRelatedArtifact", "valueRelatedArtifact", relatedartifact.RelatedArtifact, "RelatedArtifact", False, "value", True),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, "SampledData", False, "value", True),
            ("valueSignature", "valueSignature", signature.Signature, "Signature", False, "value", True),
            ("valueString", "valueString", str, "string", False, "value", True),
            ("valueTime", "valueTime", fhirdate.FHIRDate, "time", False, "value", True),
            ("valueTiming", "valueTiming", timing.Timing, "Timing", False, "value", True),
            ("valueTriggerDefinition", "valueTriggerDefinition", triggerdefinition.TriggerDefinition, "TriggerDefinition", False, "value", True),
            ("valueUnsignedInt", "valueUnsignedInt", int, "unsignedInt", False, "value", True),
            ("valueUri", "valueUri", str, "uri", False, "value", True),
            ("valueUrl", "valueUrl", str, "url", False, "value", True),
            ("valueUsageContext", "valueUsageContext", usagecontext.UsageContext, "UsageContext", False, "value", True),
            ("valueUuid", "valueUuid", str, "uuid", False, "value", True),
        ])
        return js


class TaskRestriction(backboneelement.BackboneElement):
    """ Constraints on fulfillment tasks.

    If the Task.focus is a request resource and the task is seeking fulfillment
    (i.e. is asking for the request to be actioned), this element identifies
    any limitations on what parts of the referenced request should be actioned.
    """

    resource_type = "TaskRestriction"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.period = None
        """ When fulfillment sought.
        Type `Period` (represented as `dict` in JSON). """

        self.recipient = None
        """ For whom is fulfillment sought?.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.repetitions = None
        """ How many times to repeat.
        Type `int`. """

        super(TaskRestriction, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(TaskRestriction, self).elementProperties()
        js.extend([
            ("period", "period", period.Period, "Period", False, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, "Reference", True, None, False),
            ("repetitions", "repetitions", int, "positiveInt", False, None, False),
        ])
        return js


import sys
try:
    from . import address
except ImportError:
    address = sys.modules[__package__ + '.address']
try:
    from . import age
except ImportError:
    age = sys.modules[__package__ + '.age']
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
try:
    from . import contributor
except ImportError:
    contributor = sys.modules[__package__ + '.contributor']
try:
    from . import count
except ImportError:
    count = sys.modules[__package__ + '.count']
try:
    from . import datarequirement
except ImportError:
    datarequirement = sys.modules[__package__ + '.datarequirement']
try:
    from . import distance
except ImportError:
    distance = sys.modules[__package__ + '.distance']
try:
    from . import dosage
except ImportError:
    dosage = sys.modules[__package__ + '.dosage']
try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
try:
    from . import expression
except ImportError:
    expression = sys.modules[__package__ + '.expression']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import humanname
except ImportError:
    humanname = sys.modules[__package__ + '.humanname']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import money
except ImportError:
    money = sys.modules[__package__ + '.money']
try:
    from . import parameterdefinition
except ImportError:
    parameterdefinition = sys.modules[__package__ + '.parameterdefinition']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']
try:
    from . import relatedartifact
except ImportError:
    relatedartifact = sys.modules[__package__ + '.relatedartifact']
try:
    from . import sampleddata
except ImportError:
    sampleddata = sys.modules[__package__ + '.sampleddata']
try:
    from . import signature
except ImportError:
    signature = sys.modules[__package__ + '.signature']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
try:
    from . import triggerdefinition
except ImportError:
    triggerdefinition = sys.modules[__package__ + '.triggerdefinition']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
