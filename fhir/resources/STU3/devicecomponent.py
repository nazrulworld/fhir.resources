# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceComponent
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import backboneelement, domainresource


class DeviceComponent(domainresource.DomainResource):
    """ An instance of a medical-related component of a medical device.

    The characteristics, operational status and capabilities of a medical-
    related component of a medical device.
    """

    resource_type = "DeviceComponent"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.identifier = None
        """ Instance id assigned by the software stack.
        Type `Identifier` (represented as `dict` in JSON). """

        self.languageCode = None
        """ Language code for the human-readable text strings produced by the
        device.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.lastSystemChange = None
        """ Recent system change timestamp.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.measurementPrinciple = None
        """ other | chemical | electrical | impedance | nuclear | optical |
        thermal | biological | mechanical | acoustical | manual+.
        Type `str`. """

        self.operationalStatus = None
        """ Current operational status of the component, for example On, Off or
        Standby.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.parameterGroup = None
        """ Current supported parameter group.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.parent = None
        """ Parent resource link.
        Type `FHIRReference` referencing `['DeviceComponent']` (represented as `dict` in JSON). """

        self.productionSpecification = None
        """ Specification details such as Component Revisions, or Serial
        Numbers.
        List of `DeviceComponentProductionSpecification` items (represented as `dict` in JSON). """

        self.source = None
        """ Top-level device resource link.
        Type `FHIRReference` referencing `['Device']` (represented as `dict` in JSON). """

        self.type = None
        """ What kind of component it is.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(DeviceComponent, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DeviceComponent, self).elementProperties()
        js.extend(
            [
                (
                    "identifier",
                    "identifier",
                    identifier.Identifier,
                    "Identifier",
                    False,
                    None,
                    True,
                ),
                (
                    "languageCode",
                    "languageCode",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "lastSystemChange",
                    "lastSystemChange",
                    fhirdate.FHIRDate,
                    "instant",
                    False,
                    None,
                    False,
                ),
                (
                    "measurementPrinciple",
                    "measurementPrinciple",
                    str,
                    "code",
                    False,
                    None,
                    False,
                ),
                (
                    "operationalStatus",
                    "operationalStatus",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "parameterGroup",
                    "parameterGroup",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "parent",
                    "parent",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "productionSpecification",
                    "productionSpecification",
                    DeviceComponentProductionSpecification,
                    "DeviceComponentProductionSpecification",
                    True,
                    None,
                    False,
                ),
                (
                    "source",
                    "source",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "type",
                    "type",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    True,
                ),
            ]
        )
        return js


class DeviceComponentProductionSpecification(backboneelement.BackboneElement):
    """ Specification details such as Component Revisions, or Serial Numbers.

    The production specification such as component revision, serial number,
    etc.
    """

    resource_type = "DeviceComponentProductionSpecification"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.componentId = None
        """ Internal component unique identification.
        Type `Identifier` (represented as `dict` in JSON). """

        self.productionSpec = None
        """ A printable string defining the component.
        Type `str`. """

        self.specType = None
        """ Type or kind of production specification, for example serial number
        or software revision.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(DeviceComponentProductionSpecification, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(DeviceComponentProductionSpecification, self).elementProperties()
        js.extend(
            [
                (
                    "componentId",
                    "componentId",
                    identifier.Identifier,
                    "Identifier",
                    False,
                    None,
                    False,
                ),
                ("productionSpec", "productionSpec", str, "string", False, None, False),
                (
                    "specType",
                    "specType",
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
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + ".fhirdate"]
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + ".fhirreference"]
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + ".identifier"]
