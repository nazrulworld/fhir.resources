#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.1.11917 (http://hl7.org/fhir/StructureDefinition/Extension) on 2019-05-13.
#  2019, SMART Health IT.


from . import element

class Extension(element.Element):
    """ Optional Extensions Element.

    Optional Extension Element - found in all resources.
    """

    resource_type = "Extension"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.url = None
        """ identifies the meaning of the extension.
        Type `str`. """

        self.valueAddress = None
        """ Value of extension.
        Type `Address` (represented as `dict` in JSON). """

        self.valueAge = None
        """ Value of extension.
        Type `Age` (represented as `dict` in JSON). """

        self.valueAnnotation = None
        """ Value of extension.
        Type `Annotation` (represented as `dict` in JSON). """

        self.valueAttachment = None
        """ Value of extension.
        Type `Attachment` (represented as `dict` in JSON). """

        self.valueBase64Binary = None
        """ Value of extension.
        Type `str`. """

        self.valueBoolean = None
        """ Value of extension.
        Type `bool`. """

        self.valueCode = None
        """ Value of extension.
        Type `str`. """

        self.valueCodeableConcept = None
        """ Value of extension.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.valueCoding = None
        """ Value of extension.
        Type `Coding` (represented as `dict` in JSON). """

        self.valueContactPoint = None
        """ Value of extension.
        Type `ContactPoint` (represented as `dict` in JSON). """

        self.valueCount = None
        """ Value of extension.
        Type `Count` (represented as `dict` in JSON). """

        self.valueDate = None
        """ Value of extension.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.valueDateTime = None
        """ Value of extension.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.valueDecimal = None
        """ Value of extension.
        Type `float`. """

        self.valueDistance = None
        """ Value of extension.
        Type `Distance` (represented as `dict` in JSON). """

        self.valueDuration = None
        """ Value of extension.
        Type `Duration` (represented as `dict` in JSON). """

        self.valueHumanName = None
        """ Value of extension.
        Type `HumanName` (represented as `dict` in JSON). """

        self.valueId = None
        """ Value of extension.
        Type `str`. """

        self.valueIdentifier = None
        """ Value of extension.
        Type `Identifier` (represented as `dict` in JSON). """

        self.valueInstant = None
        """ Value of extension.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.valueInteger = None
        """ Value of extension.
        Type `int`. """

        self.valueMarkdown = None
        """ Value of extension.
        Type `str`. """

        self.valueMeta = None
        """ Value of extension.
        Type `Meta` (represented as `dict` in JSON). """

        self.valueMoney = None
        """ Value of extension.
        Type `Money` (represented as `dict` in JSON). """

        self.valueOid = None
        """ Value of extension.
        Type `str`. """

        self.valuePeriod = None
        """ Value of extension.
        Type `Period` (represented as `dict` in JSON). """

        self.valuePositiveInt = None
        """ Value of extension.
        Type `int`. """

        self.valueQuantity = None
        """ Value of extension.
        Type `Quantity` (represented as `dict` in JSON). """

        self.valueRange = None
        """ Value of extension.
        Type `Range` (represented as `dict` in JSON). """

        self.valueRatio = None
        """ Value of extension.
        Type `Ratio` (represented as `dict` in JSON). """

        self.valueReference = None
        """ Value of extension.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.valueSampledData = None
        """ Value of extension.
        Type `SampledData` (represented as `dict` in JSON). """

        self.valueSignature = None
        """ Value of extension.
        Type `Signature` (represented as `dict` in JSON). """

        self.valueString = None
        """ Value of extension.
        Type `str`. """

        self.valueTime = None
        """ Value of extension.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.valueTiming = None
        """ Value of extension.
        Type `Timing` (represented as `dict` in JSON). """

        self.valueUnsignedInt = None
        """ Value of extension.
        Type `int`. """

        self.valueUri = None
        """ Value of extension.
        Type `str`. """

        super(Extension, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Extension, self).elementProperties()
        js.extend([
            ("url", "url", str, "uri", False, None, True),
            ("valueAddress", "valueAddress", address.Address, "Address", False, "value", False),
            ("valueAge", "valueAge", age.Age, "Age", False, "value", False),
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, "Annotation", False, "value", False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, "Attachment", False, "value", False),
            ("valueBase64Binary", "valueBase64Binary", str, "base64Binary", False, "value", False),
            ("valueBoolean", "valueBoolean", bool, "boolean", False, "value", False),
            ("valueCode", "valueCode", str, "code", False, "value", False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, "CodeableConcept", False, "value", False),
            ("valueCoding", "valueCoding", coding.Coding, "Coding", False, "value", False),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, "ContactPoint", False, "value", False),
            ("valueCount", "valueCount", count.Count, "Count", False, "value", False),
            ("valueDate", "valueDate", fhirdate.FHIRDate, "date", False, "value", False),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, "dateTime", False, "value", False),
            ("valueDecimal", "valueDecimal", float, "decimal", False, "value", False),
            ("valueDistance", "valueDistance", distance.Distance, "Distance", False, "value", False),
            ("valueDuration", "valueDuration", duration.Duration, "Duration", False, "value", False),
            ("valueHumanName", "valueHumanName", humanname.HumanName, "HumanName", False, "value", False),
            ("valueId", "valueId", str, "id", False, "value", False),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, "Identifier", False, "value", False),
            ("valueInstant", "valueInstant", fhirdate.FHIRDate, "instant", False, "value", False),
            ("valueInteger", "valueInteger", int, "integer", False, "value", False),
            ("valueMarkdown", "valueMarkdown", str, "markdown", False, "value", False),
            ("valueMeta", "valueMeta", meta.Meta, "Meta", False, "value", False),
            ("valueMoney", "valueMoney", money.Money, "Money", False, "value", False),
            ("valueOid", "valueOid", str, "oid", False, "value", False),
            ("valuePeriod", "valuePeriod", period.Period, "Period", False, "value", False),
            ("valuePositiveInt", "valuePositiveInt", int, "positiveInt", False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, "Quantity", False, "value", False),
            ("valueRange", "valueRange", range.Range, "Range", False, "value", False),
            ("valueRatio", "valueRatio", ratio.Ratio, "Ratio", False, "value", False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, "Reference", False, "value", False),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, "SampledData", False, "value", False),
            ("valueSignature", "valueSignature", signature.Signature, "Signature", False, "value", False),
            ("valueString", "valueString", str, "string", False, "value", False),
            ("valueTime", "valueTime", fhirdate.FHIRDate, "time", False, "value", False),
            ("valueTiming", "valueTiming", timing.Timing, "Timing", False, "value", False),
            ("valueUnsignedInt", "valueUnsignedInt", int, "unsignedInt", False, "value", False),
            ("valueUri", "valueUri", str, "uri", False, "value", False),
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
