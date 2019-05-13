#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Library) on 2019-05-13.
#  2019, SMART Health IT.


from . import domainresource

class Library(domainresource.DomainResource):
    """ Represents a library of quality improvement components.

    The Library resource is a general-purpose container for knowledge asset
    definitions. It can be used to describe and expose existing knowledge
    assets such as logic libraries and information model descriptions, as well
    as to describe a collection of knowledge assets.
    """

    resource_type = "Library"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.approvalDate = None
        """ When the library was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.author = None
        """ Who authored the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.content = None
        """ Contents of the library, either embedded or referenced.
        List of `Attachment` items (represented as `dict` in JSON). """

        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """

        self.dataRequirement = None
        """ What data is referenced by this library.
        List of `DataRequirement` items (represented as `dict` in JSON). """

        self.date = None
        """ Date last changed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.description = None
        """ Natural language description of the library.
        Type `str`. """

        self.editor = None
        """ Who edited the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.effectivePeriod = None
        """ When the library is expected to be used.
        Type `Period` (represented as `dict` in JSON). """

        self.endorser = None
        """ Who endorsed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """

        self.identifier = None
        """ Additional identifier for the library.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.jurisdiction = None
        """ Intended jurisdiction for library (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.lastReviewDate = None
        """ When the library was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.name = None
        """ Name for this library (computer friendly).
        Type `str`. """

        self.parameter = None
        """ Parameters defined by the library.
        List of `ParameterDefinition` items (represented as `dict` in JSON). """

        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """

        self.purpose = None
        """ Why this library is defined.
        Type `str`. """

        self.relatedArtifact = None
        """ Additional documentation, citations, etc..
        List of `RelatedArtifact` items (represented as `dict` in JSON). """

        self.reviewer = None
        """ Who reviewed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """

        self.subjectCodeableConcept = None
        """ Type of individual the library content is focused on.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.subjectReference = None
        """ Type of individual the library content is focused on.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.subtitle = None
        """ Subordinate title of the library.
        Type `str`. """

        self.title = None
        """ Name for this library (human friendly).
        Type `str`. """

        self.topic = None
        """ E.g. Education, Treatment, Assessment, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.type = None
        """ logic-library | model-definition | asset-collection | module-
        definition.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.url = None
        """ Canonical identifier for this library, represented as a URI
        (globally unique).
        Type `str`. """

        self.usage = None
        """ Describes the clinical usage of the library.
        Type `str`. """

        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """

        self.version = None
        """ Business version of the library.
        Type `str`. """

        super(Library, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Library, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, "date", False, None, False),
            ("author", "author", contactdetail.ContactDetail, "ContactDetail", True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, "ContactDetail", True, None, False),
            ("content", "content", attachment.Attachment, "Attachment", True, None, False),
            ("copyright", "copyright", str, "markdown", False, None, False),
            ("dataRequirement", "dataRequirement", datarequirement.DataRequirement, "DataRequirement", True, None, False),
            ("date", "date", fhirdate.FHIRDate, "dateTime", False, None, False),
            ("description", "description", str, "markdown", False, None, False),
            ("editor", "editor", contactdetail.ContactDetail, "ContactDetail", True, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, "Period", False, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, "ContactDetail", True, None, False),
            ("experimental", "experimental", bool, "boolean", False, None, False),
            ("identifier", "identifier", identifier.Identifier, "Identifier", True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, "CodeableConcept", True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, "date", False, None, False),
            ("name", "name", str, "string", False, None, False),
            ("parameter", "parameter", parameterdefinition.ParameterDefinition, "ParameterDefinition", True, None, False),
            ("publisher", "publisher", str, "string", False, None, False),
            ("purpose", "purpose", str, "markdown", False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, "RelatedArtifact", True, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, "ContactDetail", True, None, False),
            ("status", "status", str, "code", False, None, True),
            ("subjectCodeableConcept", "subjectCodeableConcept", codeableconcept.CodeableConcept, "CodeableConcept", False, "subject", False),
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, "Reference", False, "subject", False),
            ("subtitle", "subtitle", str, "string", False, None, False),
            ("title", "title", str, "string", False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, "CodeableConcept", True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, "CodeableConcept", False, None, True),
            ("url", "url", str, "uri", False, None, False),
            ("usage", "usage", str, "string", False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, "UsageContext", True, None, False),
            ("version", "version", str, "string", False, None, False),
        ])
        return js


import sys
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import datarequirement
except ImportError:
    datarequirement = sys.modules[__package__ + '.datarequirement']
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
try:
    from . import parameterdefinition
except ImportError:
    parameterdefinition = sys.modules[__package__ + '.parameterdefinition']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import relatedartifact
except ImportError:
    relatedartifact = sys.modules[__package__ + '.relatedartifact']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
