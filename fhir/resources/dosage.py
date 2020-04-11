# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Dosage
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
import sys
if sys.version.startswith("2"):
    # Disclaimer: Dosage is originally baseDefinition
    # from http://hl7.org/fhir/StructureDefinition/BackboneElement
    # But there is circular dependency problem in python2!
    # extension.Extension is used in BackboneElement.modifierExtension as value type.
    # and also dosage.Dosage is used as Extension.valueDosage value type.
    # As a result we are using ``BackboneElement`` as base class of Dosage,
    # faced import error (because od circular dependency).
    from .element import Element as BaseDosage
else:
    from .backboneelement import BackboneElement as BaseDosage
from . import element


class Dosage(BaseDosage):
    """ How the medication is/was taken or should be taken.

    Indicates how the medication is/was taken or should be taken by the
    patient.
    """

    resource_type = "Dosage"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.additionalInstruction = None
        """ Supplemental instruction or warnings to the patient - e.g. "with
        meals", "may cause drowsiness".
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.asNeededBoolean = None
        """ Take "as needed" (for x).
        Type `bool`. """

        self.asNeededCodeableConcept = None
        """ Take "as needed" (for x).
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.doseAndRate = None
        """ Amount of medication administered.
        List of `DosageDoseAndRate` items (represented as `dict` in JSON). """

        self.maxDosePerAdministration = None
        """ Upper limit on medication per administration.
        Type `Quantity` (represented as `dict` in JSON). """

        self.maxDosePerLifetime = None
        """ Upper limit on medication per lifetime of the patient.
        Type `Quantity` (represented as `dict` in JSON). """

        self.maxDosePerPeriod = None
        """ Upper limit on medication per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """

        self.method = None
        """ Technique for administering medication.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.patientInstruction = None
        """ Patient or consumer oriented instructions.
        Type `str`. """

        self.route = None
        """ How drug should enter body.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.sequence = None
        """ The order of the dosage instructions.
        Type `int`. """

        self.site = None
        """ Body site to administer to.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.text = None
        """ Free text dosage instructions e.g. SIG.
        Type `str`. """

        self.timing = None
        """ When medication should be administered.
        Type `Timing` (represented as `dict` in JSON). """

        super(Dosage, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Dosage, self).elementProperties()
        js.extend(
            [
                (
                    "additionalInstruction",
                    "additionalInstruction",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "asNeededBoolean",
                    "asNeededBoolean",
                    bool,
                    "boolean",
                    False,
                    "asNeeded",
                    False,
                ),
                (
                    "asNeededCodeableConcept",
                    "asNeededCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "asNeeded",
                    False,
                ),
                (
                    "doseAndRate",
                    "doseAndRate",
                    DosageDoseAndRate,
                    "DosageDoseAndRate",
                    True,
                    None,
                    False,
                ),
                (
                    "maxDosePerAdministration",
                    "maxDosePerAdministration",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    None,
                    False,
                ),
                (
                    "maxDosePerLifetime",
                    "maxDosePerLifetime",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    None,
                    False,
                ),
                (
                    "maxDosePerPeriod",
                    "maxDosePerPeriod",
                    ratio.Ratio,
                    "Ratio",
                    False,
                    None,
                    False,
                ),
                (
                    "method",
                    "method",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "patientInstruction",
                    "patientInstruction",
                    str,
                    "string",
                    False,
                    None,
                    False,
                ),
                (
                    "route",
                    "route",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("sequence", "sequence", int, "integer", False, None, False),
                (
                    "site",
                    "site",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("text", "text", str, "string", False, None, False),
                ("timing", "timing", timing.Timing, "Timing", False, None, False),
            ]
        )
        return js


class DosageDoseAndRate(element.Element):
    """ Amount of medication administered.

    The amount of medication administered.
    """

    resource_type = "DosageDoseAndRate"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.doseQuantity = None
        """ Amount of medication per dose.
        Type `Quantity` (represented as `dict` in JSON). """

        self.doseRange = None
        """ Amount of medication per dose.
        Type `Range` (represented as `dict` in JSON). """

        self.rateQuantity = None
        """ Amount of medication per unit of time.
        Type `Quantity` (represented as `dict` in JSON). """

        self.rateRange = None
        """ Amount of medication per unit of time.
        Type `Range` (represented as `dict` in JSON). """

        self.rateRatio = None
        """ Amount of medication per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """

        self.type = None
        """ The kind of dose or rate specified.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(DosageDoseAndRate, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DosageDoseAndRate, self).elementProperties()
        js.extend(
            [
                (
                    "doseQuantity",
                    "doseQuantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    "dose",
                    False,
                ),
                ("doseRange", "doseRange", range.Range, "Range", False, "dose", False),
                (
                    "rateQuantity",
                    "rateQuantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    "rate",
                    False,
                ),
                ("rateRange", "rateRange", range.Range, "Range", False, "rate", False),
                ("rateRatio", "rateRatio", ratio.Ratio, "Ratio", False, "rate", False),
                (
                    "type",
                    "type",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + ".quantity"]
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + ".range"]
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + ".ratio"]
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + ".timing"]
