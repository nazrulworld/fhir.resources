#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/SubstanceReferenceInformation) on 2019-05-13.
#  2019, SMART Health IT.


from . import domainresource

class SubstanceReferenceInformation(domainresource.DomainResource):
    """ Todo.
    """

    resource_type = "SubstanceReferenceInformation"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.classification = None
        """ Todo.
        List of `SubstanceReferenceInformationClassification` items (represented as `dict` in JSON). """

        self.comment = None
        """ Todo.
        Type `str`. """

        self.gene = None
        """ Todo.
        List of `SubstanceReferenceInformationGene` items (represented as `dict` in JSON). """

        self.geneElement = None
        """ Todo.
        List of `SubstanceReferenceInformationGeneElement` items (represented as `dict` in JSON). """

        self.target = None
        """ Todo.
        List of `SubstanceReferenceInformationTarget` items (represented as `dict` in JSON). """

        super(SubstanceReferenceInformation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SubstanceReferenceInformation, self).elementProperties()
        js.extend([
            ("classification", "classification", SubstanceReferenceInformationClassification, "SubstanceReferenceInformationClassification", True, None, False),
            ("comment", "comment", str, "string", False, None, False),
            ("gene", "gene", SubstanceReferenceInformationGene, "SubstanceReferenceInformationGene", True, None, False),
            ("geneElement", "geneElement", SubstanceReferenceInformationGeneElement, "SubstanceReferenceInformationGeneElement", True, None, False),
            ("target", "target", SubstanceReferenceInformationTarget, "SubstanceReferenceInformationTarget", True, None, False),
        ])
        return js


from . import backboneelement

class SubstanceReferenceInformationClassification(backboneelement.BackboneElement):
    """ Todo.
    """

    resource_type = "SubstanceReferenceInformationClassification"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.classification = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.domain = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.source = None
        """ Todo.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.subtype = None
        """ Todo.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        super(SubstanceReferenceInformationClassification, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SubstanceReferenceInformationClassification, self).elementProperties()
        js.extend([
            ("classification", "classification", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
            ("domain", "domain", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
            ("source", "source", fhirreference.FHIRReference, "Reference", True, None, False),
            ("subtype", "subtype", codeableconcept.CodeableConcept, "CodeableConcept", True, None, False),
        ])
        return js


class SubstanceReferenceInformationGene(backboneelement.BackboneElement):
    """ Todo.
    """

    resource_type = "SubstanceReferenceInformationGene"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.gene = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.geneSequenceOrigin = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.source = None
        """ Todo.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        super(SubstanceReferenceInformationGene, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SubstanceReferenceInformationGene, self).elementProperties()
        js.extend([
            ("gene", "gene", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
            ("geneSequenceOrigin", "geneSequenceOrigin", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
            ("source", "source", fhirreference.FHIRReference, "Reference", True, None, False),
        ])
        return js


class SubstanceReferenceInformationGeneElement(backboneelement.BackboneElement):
    """ Todo.
    """

    resource_type = "SubstanceReferenceInformationGeneElement"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.element = None
        """ Todo.
        Type `Identifier` (represented as `dict` in JSON). """

        self.source = None
        """ Todo.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.type = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(SubstanceReferenceInformationGeneElement, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SubstanceReferenceInformationGeneElement, self).elementProperties()
        js.extend([
            ("element", "element", identifier.Identifier, "Identifier", False, None, False),
            ("source", "source", fhirreference.FHIRReference, "Reference", True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
        ])
        return js


class SubstanceReferenceInformationTarget(backboneelement.BackboneElement):
    """ Todo.
    """

    resource_type = "SubstanceReferenceInformationTarget"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.amountQuantity = None
        """ Todo.
        Type `Quantity` (represented as `dict` in JSON). """

        self.amountRange = None
        """ Todo.
        Type `Range` (represented as `dict` in JSON). """

        self.amountString = None
        """ Todo.
        Type `str`. """

        self.amountType = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.interaction = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.organism = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.organismType = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.source = None
        """ Todo.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.target = None
        """ Todo.
        Type `Identifier` (represented as `dict` in JSON). """

        self.type = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(SubstanceReferenceInformationTarget, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SubstanceReferenceInformationTarget, self).elementProperties()
        js.extend([
            ("amountQuantity", "amountQuantity", quantity.Quantity, "Quantity", False, "amount", False),
            ("amountRange", "amountRange", range.Range, "Range", False, "amount", False),
            ("amountString", "amountString", str, "string", False, "amount", False),
            ("amountType", "amountType", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
            ("interaction", "interaction", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
            ("organism", "organism", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
            ("organismType", "organismType", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
            ("source", "source", fhirreference.FHIRReference, "Reference", True, None, False),
            ("target", "target", identifier.Identifier, "Identifier", False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
