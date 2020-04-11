# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductInteraction
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class MedicinalProductInteraction(domainresource.DomainResource):
    """ MedicinalProductInteraction.

    The interactions of the medicinal product with other medicinal products, or
    other forms of interactions.
    """

    resource_type = "MedicinalProductInteraction"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.description = None
        """ The interaction described.
        Type `str`. """

        self.effect = None
        """ The effect of the interaction, for example "reduced gastric
        absorption of primary medication".
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.incidence = None
        """ The incidence of the interaction, e.g. theoretical, observed.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.interactant = None
        """ The specific medication, food or laboratory test that interacts.
        List of `MedicinalProductInteractionInteractant` items (represented as `dict` in JSON). """

        self.management = None
        """ Actions for managing the interaction.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.subject = None
        """ The medication for which this is a described interaction.
        List of `FHIRReference` items referencing `['MedicinalProduct', 'Medication', 'Substance']` (represented as `dict` in JSON). """

        self.type = None
        """ The type of the interaction e.g. drug-drug interaction, drug-food
        interaction, drug-lab test interaction.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(MedicinalProductInteraction, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(MedicinalProductInteraction, self).elementProperties()
        js.extend(
            [
                ("description", "description", str, "string", False, None, False),
                (
                    "effect",
                    "effect",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "incidence",
                    "incidence",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "interactant",
                    "interactant",
                    MedicinalProductInteractionInteractant,
                    "MedicinalProductInteractionInteractant",
                    True,
                    None,
                    False,
                ),
                (
                    "management",
                    "management",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "subject",
                    "subject",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
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
                    False,
                ),
            ]
        )
        return js


class MedicinalProductInteractionInteractant(backboneelement.BackboneElement):
    """ The specific medication, food or laboratory test that interacts.
    """

    resource_type = "MedicinalProductInteractionInteractant"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.itemCodeableConcept = None
        """ The specific medication, food or laboratory test that interacts.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.itemReference = None
        """ The specific medication, food or laboratory test that interacts.
        Type `FHIRReference` referencing `['MedicinalProduct', 'Medication', 'Substance', 'ObservationDefinition']` (represented as `dict` in JSON). """

        super(MedicinalProductInteractionInteractant, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(MedicinalProductInteractionInteractant, self).elementProperties()
        js.extend(
            [
                (
                    "itemCodeableConcept",
                    "itemCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "item",
                    True,
                ),
                (
                    "itemReference",
                    "itemReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "item",
                    True,
                ),
            ]
        )
        return js


try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + ".fhirreference"]
