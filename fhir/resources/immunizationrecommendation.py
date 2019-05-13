#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ImmunizationRecommendation) on 2019-05-13.
#  2019, SMART Health IT.


from . import domainresource

class ImmunizationRecommendation(domainresource.DomainResource):
    """ Guidance or advice relating to an immunization.

    A patient's point-in-time set of recommendations (i.e. forecasting)
    according to a published schedule with optional supporting justification.
    """

    resource_type = "ImmunizationRecommendation"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.authority = None
        """ Who is responsible for protocol.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.date = None
        """ Date recommendation(s) created.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.patient = None
        """ Who this profile is for.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.recommendation = None
        """ Vaccine administration recommendations.
        List of `ImmunizationRecommendationRecommendation` items (represented as `dict` in JSON). """

        super(ImmunizationRecommendation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ImmunizationRecommendation, self).elementProperties()
        js.extend([
            ("authority", "authority", fhirreference.FHIRReference, "Reference", False, None, False),
            ("date", "date", fhirdate.FHIRDate, "dateTime", False, None, True),
            ("identifier", "identifier", identifier.Identifier, "Identifier", True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, "Reference", False, None, True),
            ("recommendation", "recommendation", ImmunizationRecommendationRecommendation, "ImmunizationRecommendationRecommendation", True, None, True),
        ])
        return js


from . import backboneelement

class ImmunizationRecommendationRecommendation(backboneelement.BackboneElement):
    """ Vaccine administration recommendations.
    """

    resource_type = "ImmunizationRecommendationRecommendation"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.contraindicatedVaccineCode = None
        """ Vaccine which is contraindicated to fulfill the recommendation.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.dateCriterion = None
        """ Dates governing proposed immunization.
        List of `ImmunizationRecommendationRecommendationDateCriterion` items (represented as `dict` in JSON). """

        self.description = None
        """ Protocol details.
        Type `str`. """

        self.doseNumberPositiveInt = None
        """ Recommended dose number within series.
        Type `int`. """

        self.doseNumberString = None
        """ Recommended dose number within series.
        Type `str`. """

        self.forecastReason = None
        """ Vaccine administration status reason.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.forecastStatus = None
        """ Vaccine recommendation status.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.series = None
        """ Name of vaccination series.
        Type `str`. """

        self.seriesDosesPositiveInt = None
        """ Recommended number of doses for immunity.
        Type `int`. """

        self.seriesDosesString = None
        """ Recommended number of doses for immunity.
        Type `str`. """

        self.supportingImmunization = None
        """ Past immunizations supporting recommendation.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.supportingPatientInformation = None
        """ Patient observations supporting recommendation.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.targetDisease = None
        """ Disease to be immunized against.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.vaccineCode = None
        """ Vaccine  or vaccine group recommendation applies to.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        super(ImmunizationRecommendationRecommendation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ImmunizationRecommendationRecommendation, self).elementProperties()
        js.extend([
            ("contraindicatedVaccineCode", "contraindicatedVaccineCode", codeableconcept.CodeableConcept, "CodeableConcept", True, None, False),
            ("dateCriterion", "dateCriterion", ImmunizationRecommendationRecommendationDateCriterion, "ImmunizationRecommendationRecommendationDateCriterion", True, None, False),
            ("description", "description", str, "string", False, None, False),
            ("doseNumberPositiveInt", "doseNumberPositiveInt", int, "positiveInt", False, "doseNumber", False),
            ("doseNumberString", "doseNumberString", str, "string", False, "doseNumber", False),
            ("forecastReason", "forecastReason", codeableconcept.CodeableConcept, "CodeableConcept", True, None, False),
            ("forecastStatus", "forecastStatus", codeableconcept.CodeableConcept, "CodeableConcept", False, None, True),
            ("series", "series", str, "string", False, None, False),
            ("seriesDosesPositiveInt", "seriesDosesPositiveInt", int, "positiveInt", False, "seriesDoses", False),
            ("seriesDosesString", "seriesDosesString", str, "string", False, "seriesDoses", False),
            ("supportingImmunization", "supportingImmunization", fhirreference.FHIRReference, "Reference", True, None, False),
            ("supportingPatientInformation", "supportingPatientInformation", fhirreference.FHIRReference, "Reference", True, None, False),
            ("targetDisease", "targetDisease", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
            ("vaccineCode", "vaccineCode", codeableconcept.CodeableConcept, "CodeableConcept", True, None, False),
        ])
        return js


class ImmunizationRecommendationRecommendationDateCriterion(backboneelement.BackboneElement):
    """ Dates governing proposed immunization.

    Vaccine date recommendations.  For example, earliest date to administer,
    latest date to administer, etc.
    """

    resource_type = "ImmunizationRecommendationRecommendationDateCriterion"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Type of date.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.value = None
        """ Recommended date.
        Type `FHIRDate` (represented as `str` in JSON). """

        super(ImmunizationRecommendationRecommendationDateCriterion, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ImmunizationRecommendationRecommendationDateCriterion, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, "CodeableConcept", False, None, True),
            ("value", "value", fhirdate.FHIRDate, "dateTime", False, None, True),
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
