#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.1.11917 (http://hl7.org/fhir/StructureDefinition/StructureMap) on 2019-05-13.
#  2019, SMART Health IT.


from . import domainresource

class StructureMap(domainresource.DomainResource):
    """ A Map of relationships between 2 structures that can be used to transform
    data.
    """

    resource_type = "StructureMap"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """

        self.date = None
        """ Date this was last changed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.description = None
        """ Natural language description of the structure map.
        Type `str`. """

        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """

        self.group = None
        """ Named sections for reader convenience.
        List of `StructureMapGroup` items (represented as `dict` in JSON). """

        self.identifier = None
        """ Additional identifier for the structure map.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.import_fhir = None
        """ Other maps used by this map (canonical URLs).
        List of `str` items. """

        self.jurisdiction = None
        """ Intended jurisdiction for structure map (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.name = None
        """ Name for this structure map (computer friendly).
        Type `str`. """

        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """

        self.purpose = None
        """ Why this structure map is defined.
        Type `str`. """

        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """

        self.structure = None
        """ Structure Definition used by this map.
        List of `StructureMapStructure` items (represented as `dict` in JSON). """

        self.title = None
        """ Name for this structure map (human friendly).
        Type `str`. """

        self.url = None
        """ Logical URI to reference this structure map (globally unique).
        Type `str`. """

        self.useContext = None
        """ Context the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """

        self.version = None
        """ Business version of the structure map.
        Type `str`. """

        super(StructureMap, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureMap, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, "ContactDetail", True, None, False),
            ("copyright", "copyright", str, "markdown", False, None, False),
            ("date", "date", fhirdate.FHIRDate, "dateTime", False, None, False),
            ("description", "description", str, "markdown", False, None, False),
            ("experimental", "experimental", bool, "boolean", False, None, False),
            ("group", "group", StructureMapGroup, "StructureMapGroup", True, None, True),
            ("identifier", "identifier", identifier.Identifier, "Identifier", True, None, False),
            ("import_fhir", "import", str, "uri", True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, "CodeableConcept", True, None, False),
            ("name", "name", str, "string", False, None, True),
            ("publisher", "publisher", str, "string", False, None, False),
            ("purpose", "purpose", str, "markdown", False, None, False),
            ("status", "status", str, "code", False, None, True),
            ("structure", "structure", StructureMapStructure, "StructureMapStructure", True, None, False),
            ("title", "title", str, "string", False, None, False),
            ("url", "url", str, "uri", False, None, True),
            ("useContext", "useContext", usagecontext.UsageContext, "UsageContext", True, None, False),
            ("version", "version", str, "string", False, None, False),
        ])
        return js


from . import backboneelement

class StructureMapGroup(backboneelement.BackboneElement):
    """ Named sections for reader convenience.

    Organizes the mapping into managable chunks for human review/ease of
    maintenance.
    """

    resource_type = "StructureMapGroup"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.documentation = None
        """ Additional description/explaination for group.
        Type `str`. """

        self.extends = None
        """ Another group that this group adds rules to.
        Type `str`. """

        self.input = None
        """ Named instance provided when invoking the map.
        List of `StructureMapGroupInput` items (represented as `dict` in JSON). """

        self.name = None
        """ Human-readable label.
        Type `str`. """

        self.rule = None
        """ Transform Rule from source to target.
        List of `StructureMapGroupRule` items (represented as `dict` in JSON). """

        self.typeMode = None
        """ none | types | type-and-types.
        Type `str`. """

        super(StructureMapGroup, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureMapGroup, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, "string", False, None, False),
            ("extends", "extends", str, "id", False, None, False),
            ("input", "input", StructureMapGroupInput, "StructureMapGroupInput", True, None, True),
            ("name", "name", str, "id", False, None, True),
            ("rule", "rule", StructureMapGroupRule, "StructureMapGroupRule", True, None, True),
            ("typeMode", "typeMode", str, "code", False, None, True),
        ])
        return js


class StructureMapGroupInput(backboneelement.BackboneElement):
    """ Named instance provided when invoking the map.

    A name assigned to an instance of data. The instance must be provided when
    the mapping is invoked.
    """

    resource_type = "StructureMapGroupInput"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.documentation = None
        """ Documentation for this instance of data.
        Type `str`. """

        self.mode = None
        """ source | target.
        Type `str`. """

        self.name = None
        """ Name for this instance of data.
        Type `str`. """

        self.type = None
        """ Type for this instance of data.
        Type `str`. """

        super(StructureMapGroupInput, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureMapGroupInput, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, "string", False, None, False),
            ("mode", "mode", str, "code", False, None, True),
            ("name", "name", str, "id", False, None, True),
            ("type", "type", str, "string", False, None, False),
        ])
        return js


class StructureMapGroupRule(backboneelement.BackboneElement):
    """ Transform Rule from source to target.
    """

    resource_type = "StructureMapGroupRule"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.dependent = None
        """ Which other rules to apply in the context of this rule.
        List of `StructureMapGroupRuleDependent` items (represented as `dict` in JSON). """

        self.documentation = None
        """ Documentation for this instance of data.
        Type `str`. """

        self.name = None
        """ Name of the rule for internal references.
        Type `str`. """

        self.rule = None
        """ Rules contained in this rule.
        List of `StructureMapGroupRule` items (represented as `dict` in JSON). """

        self.source = None
        """ Source inputs to the mapping.
        List of `StructureMapGroupRuleSource` items (represented as `dict` in JSON). """

        self.target = None
        """ Content to create because of this mapping rule.
        List of `StructureMapGroupRuleTarget` items (represented as `dict` in JSON). """

        super(StructureMapGroupRule, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureMapGroupRule, self).elementProperties()
        js.extend([
            ("dependent", "dependent", StructureMapGroupRuleDependent, "StructureMapGroupRuleDependent", True, None, False),
            ("documentation", "documentation", str, "string", False, None, False),
            ("name", "name", str, "id", False, None, True),
            ("rule", "rule", StructureMapGroupRule, "StructureMapGroupRule", True, None, False),
            ("source", "source", StructureMapGroupRuleSource, "StructureMapGroupRuleSource", True, None, True),
            ("target", "target", StructureMapGroupRuleTarget, "StructureMapGroupRuleTarget", True, None, False),
        ])
        return js


class StructureMapGroupRuleDependent(backboneelement.BackboneElement):
    """ Which other rules to apply in the context of this rule.
    """

    resource_type = "StructureMapGroupRuleDependent"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.name = None
        """ Name of a rule or group to apply.
        Type `str`. """

        self.variable = None
        """ Variable to pass to the rule or group.
        List of `str` items. """

        super(StructureMapGroupRuleDependent, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureMapGroupRuleDependent, self).elementProperties()
        js.extend([
            ("name", "name", str, "id", False, None, True),
            ("variable", "variable", str, "string", True, None, True),
        ])
        return js


class StructureMapGroupRuleSource(backboneelement.BackboneElement):
    """ Source inputs to the mapping.
    """

    resource_type = "StructureMapGroupRuleSource"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.check = None
        """ FHIRPath expression  - must be true or the mapping engine throws an
        error instead of completing.
        Type `str`. """

        self.condition = None
        """ FHIRPath expression  - must be true or the rule does not apply.
        Type `str`. """

        self.context = None
        """ Type or variable this rule applies to.
        Type `str`. """

        self.defaultValueAddress = None
        """ Default value if no value exists.
        Type `Address` (represented as `dict` in JSON). """

        self.defaultValueAge = None
        """ Default value if no value exists.
        Type `Age` (represented as `dict` in JSON). """

        self.defaultValueAnnotation = None
        """ Default value if no value exists.
        Type `Annotation` (represented as `dict` in JSON). """

        self.defaultValueAttachment = None
        """ Default value if no value exists.
        Type `Attachment` (represented as `dict` in JSON). """

        self.defaultValueBase64Binary = None
        """ Default value if no value exists.
        Type `str`. """

        self.defaultValueBoolean = None
        """ Default value if no value exists.
        Type `bool`. """

        self.defaultValueCode = None
        """ Default value if no value exists.
        Type `str`. """

        self.defaultValueCodeableConcept = None
        """ Default value if no value exists.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.defaultValueCoding = None
        """ Default value if no value exists.
        Type `Coding` (represented as `dict` in JSON). """

        self.defaultValueContactPoint = None
        """ Default value if no value exists.
        Type `ContactPoint` (represented as `dict` in JSON). """

        self.defaultValueCount = None
        """ Default value if no value exists.
        Type `Count` (represented as `dict` in JSON). """

        self.defaultValueDate = None
        """ Default value if no value exists.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.defaultValueDateTime = None
        """ Default value if no value exists.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.defaultValueDecimal = None
        """ Default value if no value exists.
        Type `float`. """

        self.defaultValueDistance = None
        """ Default value if no value exists.
        Type `Distance` (represented as `dict` in JSON). """

        self.defaultValueDuration = None
        """ Default value if no value exists.
        Type `Duration` (represented as `dict` in JSON). """

        self.defaultValueHumanName = None
        """ Default value if no value exists.
        Type `HumanName` (represented as `dict` in JSON). """

        self.defaultValueId = None
        """ Default value if no value exists.
        Type `str`. """

        self.defaultValueIdentifier = None
        """ Default value if no value exists.
        Type `Identifier` (represented as `dict` in JSON). """

        self.defaultValueInstant = None
        """ Default value if no value exists.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.defaultValueInteger = None
        """ Default value if no value exists.
        Type `int`. """

        self.defaultValueMarkdown = None
        """ Default value if no value exists.
        Type `str`. """

        self.defaultValueMeta = None
        """ Default value if no value exists.
        Type `Meta` (represented as `dict` in JSON). """

        self.defaultValueMoney = None
        """ Default value if no value exists.
        Type `Money` (represented as `dict` in JSON). """

        self.defaultValueOid = None
        """ Default value if no value exists.
        Type `str`. """

        self.defaultValuePeriod = None
        """ Default value if no value exists.
        Type `Period` (represented as `dict` in JSON). """

        self.defaultValuePositiveInt = None
        """ Default value if no value exists.
        Type `int`. """

        self.defaultValueQuantity = None
        """ Default value if no value exists.
        Type `Quantity` (represented as `dict` in JSON). """

        self.defaultValueRange = None
        """ Default value if no value exists.
        Type `Range` (represented as `dict` in JSON). """

        self.defaultValueRatio = None
        """ Default value if no value exists.
        Type `Ratio` (represented as `dict` in JSON). """

        self.defaultValueReference = None
        """ Default value if no value exists.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.defaultValueSampledData = None
        """ Default value if no value exists.
        Type `SampledData` (represented as `dict` in JSON). """

        self.defaultValueSignature = None
        """ Default value if no value exists.
        Type `Signature` (represented as `dict` in JSON). """

        self.defaultValueString = None
        """ Default value if no value exists.
        Type `str`. """

        self.defaultValueTime = None
        """ Default value if no value exists.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.defaultValueTiming = None
        """ Default value if no value exists.
        Type `Timing` (represented as `dict` in JSON). """

        self.defaultValueUnsignedInt = None
        """ Default value if no value exists.
        Type `int`. """

        self.defaultValueUri = None
        """ Default value if no value exists.
        Type `str`. """

        self.element = None
        """ Optional field for this source.
        Type `str`. """

        self.listMode = None
        """ first | not_first | last | not_last | only_one.
        Type `str`. """

        self.max = None
        """ Specified maximum cardinality (number or *).
        Type `str`. """

        self.min = None
        """ Specified minimum cardinality.
        Type `int`. """

        self.type = None
        """ Rule only applies if source has this type.
        Type `str`. """

        self.variable = None
        """ Named context for field, if a field is specified.
        Type `str`. """

        super(StructureMapGroupRuleSource, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureMapGroupRuleSource, self).elementProperties()
        js.extend([
            ("check", "check", str, "string", False, None, False),
            ("condition", "condition", str, "string", False, None, False),
            ("context", "context", str, "id", False, None, True),
            ("defaultValueAddress", "defaultValueAddress", address.Address, "Address", False, "defaultValue", False),
            ("defaultValueAge", "defaultValueAge", age.Age, "Age", False, "defaultValue", False),
            ("defaultValueAnnotation", "defaultValueAnnotation", annotation.Annotation, "Annotation", False, "defaultValue", False),
            ("defaultValueAttachment", "defaultValueAttachment", attachment.Attachment, "Attachment", False, "defaultValue", False),
            ("defaultValueBase64Binary", "defaultValueBase64Binary", str, "base64Binary", False, "defaultValue", False),
            ("defaultValueBoolean", "defaultValueBoolean", bool, "boolean", False, "defaultValue", False),
            ("defaultValueCode", "defaultValueCode", str, "code", False, "defaultValue", False),
            ("defaultValueCodeableConcept", "defaultValueCodeableConcept", codeableconcept.CodeableConcept, "CodeableConcept", False, "defaultValue", False),
            ("defaultValueCoding", "defaultValueCoding", coding.Coding, "Coding", False, "defaultValue", False),
            ("defaultValueContactPoint", "defaultValueContactPoint", contactpoint.ContactPoint, "ContactPoint", False, "defaultValue", False),
            ("defaultValueCount", "defaultValueCount", count.Count, "Count", False, "defaultValue", False),
            ("defaultValueDate", "defaultValueDate", fhirdate.FHIRDate, "date", False, "defaultValue", False),
            ("defaultValueDateTime", "defaultValueDateTime", fhirdate.FHIRDate, "dateTime", False, "defaultValue", False),
            ("defaultValueDecimal", "defaultValueDecimal", float, "decimal", False, "defaultValue", False),
            ("defaultValueDistance", "defaultValueDistance", distance.Distance, "Distance", False, "defaultValue", False),
            ("defaultValueDuration", "defaultValueDuration", duration.Duration, "Duration", False, "defaultValue", False),
            ("defaultValueHumanName", "defaultValueHumanName", humanname.HumanName, "HumanName", False, "defaultValue", False),
            ("defaultValueId", "defaultValueId", str, "id", False, "defaultValue", False),
            ("defaultValueIdentifier", "defaultValueIdentifier", identifier.Identifier, "Identifier", False, "defaultValue", False),
            ("defaultValueInstant", "defaultValueInstant", fhirdate.FHIRDate, "instant", False, "defaultValue", False),
            ("defaultValueInteger", "defaultValueInteger", int, "integer", False, "defaultValue", False),
            ("defaultValueMarkdown", "defaultValueMarkdown", str, "markdown", False, "defaultValue", False),
            ("defaultValueMeta", "defaultValueMeta", meta.Meta, "Meta", False, "defaultValue", False),
            ("defaultValueMoney", "defaultValueMoney", money.Money, "Money", False, "defaultValue", False),
            ("defaultValueOid", "defaultValueOid", str, "oid", False, "defaultValue", False),
            ("defaultValuePeriod", "defaultValuePeriod", period.Period, "Period", False, "defaultValue", False),
            ("defaultValuePositiveInt", "defaultValuePositiveInt", int, "positiveInt", False, "defaultValue", False),
            ("defaultValueQuantity", "defaultValueQuantity", quantity.Quantity, "Quantity", False, "defaultValue", False),
            ("defaultValueRange", "defaultValueRange", range.Range, "Range", False, "defaultValue", False),
            ("defaultValueRatio", "defaultValueRatio", ratio.Ratio, "Ratio", False, "defaultValue", False),
            ("defaultValueReference", "defaultValueReference", fhirreference.FHIRReference, "Reference", False, "defaultValue", False),
            ("defaultValueSampledData", "defaultValueSampledData", sampleddata.SampledData, "SampledData", False, "defaultValue", False),
            ("defaultValueSignature", "defaultValueSignature", signature.Signature, "Signature", False, "defaultValue", False),
            ("defaultValueString", "defaultValueString", str, "string", False, "defaultValue", False),
            ("defaultValueTime", "defaultValueTime", fhirdate.FHIRDate, "time", False, "defaultValue", False),
            ("defaultValueTiming", "defaultValueTiming", timing.Timing, "Timing", False, "defaultValue", False),
            ("defaultValueUnsignedInt", "defaultValueUnsignedInt", int, "unsignedInt", False, "defaultValue", False),
            ("defaultValueUri", "defaultValueUri", str, "uri", False, "defaultValue", False),
            ("element", "element", str, "string", False, None, False),
            ("listMode", "listMode", str, "code", False, None, False),
            ("max", "max", str, "string", False, None, False),
            ("min", "min", int, "integer", False, None, False),
            ("type", "type", str, "string", False, None, False),
            ("variable", "variable", str, "id", False, None, False),
        ])
        return js


class StructureMapGroupRuleTarget(backboneelement.BackboneElement):
    """ Content to create because of this mapping rule.
    """

    resource_type = "StructureMapGroupRuleTarget"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.context = None
        """ Type or variable this rule applies to.
        Type `str`. """

        self.contextType = None
        """ type | variable.
        Type `str`. """

        self.element = None
        """ Field to create in the context.
        Type `str`. """

        self.listMode = None
        """ first | share | last | collate.
        List of `str` items. """

        self.listRuleId = None
        """ Internal rule reference for shared list items.
        Type `str`. """

        self.parameter = None
        """ Parameters to the transform.
        List of `StructureMapGroupRuleTargetParameter` items (represented as `dict` in JSON). """

        self.transform = None
        """ create | copy +.
        Type `str`. """

        self.variable = None
        """ Named context for field, if desired, and a field is specified.
        Type `str`. """

        super(StructureMapGroupRuleTarget, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureMapGroupRuleTarget, self).elementProperties()
        js.extend([
            ("context", "context", str, "id", False, None, False),
            ("contextType", "contextType", str, "code", False, None, False),
            ("element", "element", str, "string", False, None, False),
            ("listMode", "listMode", str, "code", True, None, False),
            ("listRuleId", "listRuleId", str, "id", False, None, False),
            ("parameter", "parameter", StructureMapGroupRuleTargetParameter, "StructureMapGroupRuleTargetParameter", True, None, False),
            ("transform", "transform", str, "code", False, None, False),
            ("variable", "variable", str, "id", False, None, False),
        ])
        return js


class StructureMapGroupRuleTargetParameter(backboneelement.BackboneElement):
    """ Parameters to the transform.
    """

    resource_type = "StructureMapGroupRuleTargetParameter"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.valueBoolean = None
        """ Parameter value - variable or literal.
        Type `bool`. """

        self.valueDecimal = None
        """ Parameter value - variable or literal.
        Type `float`. """

        self.valueId = None
        """ Parameter value - variable or literal.
        Type `str`. """

        self.valueInteger = None
        """ Parameter value - variable or literal.
        Type `int`. """

        self.valueString = None
        """ Parameter value - variable or literal.
        Type `str`. """

        super(StructureMapGroupRuleTargetParameter, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureMapGroupRuleTargetParameter, self).elementProperties()
        js.extend([
            ("valueBoolean", "valueBoolean", bool, "boolean", False, "value", True),
            ("valueDecimal", "valueDecimal", float, "decimal", False, "value", True),
            ("valueId", "valueId", str, "id", False, "value", True),
            ("valueInteger", "valueInteger", int, "integer", False, "value", True),
            ("valueString", "valueString", str, "string", False, "value", True),
        ])
        return js


class StructureMapStructure(backboneelement.BackboneElement):
    """ Structure Definition used by this map.

    A structure definition used by this map. The structure definition may
    describe instances that are converted, or the instances that are produced.
    """

    resource_type = "StructureMapStructure"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.alias = None
        """ Name for type in this map.
        Type `str`. """

        self.documentation = None
        """ Documentation on use of structure.
        Type `str`. """

        self.mode = None
        """ source | queried | target | produced.
        Type `str`. """

        self.url = None
        """ Canonical URL for structure definition.
        Type `str`. """

        super(StructureMapStructure, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureMapStructure, self).elementProperties()
        js.extend([
            ("alias", "alias", str, "string", False, None, False),
            ("documentation", "documentation", str, "string", False, None, False),
            ("mode", "mode", str, "code", False, None, True),
            ("url", "url", str, "uri", False, None, True),
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
    from . import count
except ImportError:
    count = sys.modules[__package__ + '.count']
try:
    from . import distance
except ImportError:
    distance = sys.modules[__package__ + '.distance']
try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
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
    from . import meta
except ImportError:
    meta = sys.modules[__package__ + '.meta']
try:
    from . import money
except ImportError:
    money = sys.modules[__package__ + '.money']
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
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
