#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ImmunizationEvaluation) on 2019-05-13.
#  2019, SMART Health IT.


from . import domainresource

class ImmunizationEvaluation(domainresource.DomainResource):
    """ Immunization evaluation information.

    Describes a comparison of an immunization event against published
    recommendations to determine if the administration is "valid" in relation
    to those  recommendations.
    """

    resource_type = "ImmunizationEvaluation"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.authority = None
        """ Who is responsible for publishing the recommendations.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.date = None
        """ Date evaluation was performed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.description = None
        """ Evaluation notes.
        Type `str`. """

        self.doseNumberPositiveInt = None
        """ Dose number within series.
        Type `int`. """

        self.doseNumberString = None
        """ Dose number within series.
        Type `str`. """

        self.doseStatus = None
        """ Status of the dose relative to published recommendations.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.doseStatusReason = None
        """ Reason for the dose status.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.immunizationEvent = None
        """ Immunization being evaluated.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.patient = None
        """ Who this evaluation is for.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.series = None
        """ Name of vaccine series.
        Type `str`. """

        self.seriesDosesPositiveInt = None
        """ Recommended number of doses for immunity.
        Type `int`. """

        self.seriesDosesString = None
        """ Recommended number of doses for immunity.
        Type `str`. """

        self.status = None
        """ completed | entered-in-error.
        Type `str`. """

        self.targetDisease = None
        """ Evaluation target disease.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(ImmunizationEvaluation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ImmunizationEvaluation, self).elementProperties()
        js.extend([
            ("authority", "authority", fhirreference.FHIRReference, "Reference", False, None, False),
            ("date", "date", fhirdate.FHIRDate, "dateTime", False, None, False),
            ("description", "description", str, "string", False, None, False),
            ("doseNumberPositiveInt", "doseNumberPositiveInt", int, "positiveInt", False, "doseNumber", False),
            ("doseNumberString", "doseNumberString", str, "string", False, "doseNumber", False),
            ("doseStatus", "doseStatus", codeableconcept.CodeableConcept, "CodeableConcept", False, None, True),
            ("doseStatusReason", "doseStatusReason", codeableconcept.CodeableConcept, "CodeableConcept", True, None, False),
            ("identifier", "identifier", identifier.Identifier, "Identifier", True, None, False),
            ("immunizationEvent", "immunizationEvent", fhirreference.FHIRReference, "Reference", False, None, True),
            ("patient", "patient", fhirreference.FHIRReference, "Reference", False, None, True),
            ("series", "series", str, "string", False, None, False),
            ("seriesDosesPositiveInt", "seriesDosesPositiveInt", int, "positiveInt", False, "seriesDoses", False),
            ("seriesDosesString", "seriesDosesString", str, "string", False, "seriesDoses", False),
            ("status", "status", str, "code", False, None, True),
            ("targetDisease", "targetDisease", codeableconcept.CodeableConcept, "CodeableConcept", False, None, True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
