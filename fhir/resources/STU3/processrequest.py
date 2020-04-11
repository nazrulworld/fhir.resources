# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ProcessRequest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import backboneelement, domainresource


class ProcessRequest(domainresource.DomainResource):
    """ Request to perform some action on or in regards to an existing resource.

    This resource provides the target, request and response, and action details
    for an action to be performed by the target on or about existing resources.
    """

    resource_type = "ProcessRequest"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.action = None
        """ cancel | poll | reprocess | status.
        Type `str`. """

        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.exclude = None
        """ Resource type(s) to exclude.
        List of `str` items. """

        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.include = None
        """ Resource type(s) to include.
        List of `str` items. """

        self.item = None
        """ Items to re-adjudicate.
        List of `ProcessRequestItem` items (represented as `dict` in JSON). """

        self.nullify = None
        """ Remove history.
        Type `bool`. """

        self.organization = None
        """ Responsible organization.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.period = None
        """ Selection period.
        Type `Period` (represented as `dict` in JSON). """

        self.provider = None
        """ Responsible practitioner.
        Type `FHIRReference` referencing `['Practitioner']` (represented as `dict` in JSON). """

        self.reference = None
        """ Reference number/string.
        Type `str`. """

        self.request = None
        """ Reference to the Request resource.
        Type `FHIRReference` referencing `['Resource']` (represented as `dict` in JSON). """

        self.response = None
        """ Reference to the Response resource.
        Type `FHIRReference` referencing `['Resource']` (represented as `dict` in JSON). """

        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """

        self.target = None
        """ Party which is the target of the request.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        super(ProcessRequest, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ProcessRequest, self).elementProperties()
        js.extend(
            [
                ("action", "action", str, "code", False, None, False),
                (
                    "created",
                    "created",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    None,
                    False,
                ),
                ("exclude", "exclude", str, "string", True, None, False),
                (
                    "identifier",
                    "identifier",
                    identifier.Identifier,
                    "Identifier",
                    True,
                    None,
                    False,
                ),
                ("include", "include", str, "string", True, None, False),
                (
                    "item",
                    "item",
                    ProcessRequestItem,
                    "ProcessRequestItem",
                    True,
                    None,
                    False,
                ),
                ("nullify", "nullify", bool, "boolean", False, None, False),
                (
                    "organization",
                    "organization",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("period", "period", period.Period, "Period", False, None, False),
                (
                    "provider",
                    "provider",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("reference", "reference", str, "string", False, None, False),
                (
                    "request",
                    "request",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "response",
                    "response",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("status", "status", str, "code", False, None, False),
                (
                    "target",
                    "target",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


class ProcessRequestItem(backboneelement.BackboneElement):
    """ Items to re-adjudicate.

    List of top level items to be re-adjudicated, if none specified then the
    entire submission is re-adjudicated.
    """

    resource_type = "ProcessRequestItem"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.sequenceLinkId = None
        """ Service instance.
        Type `int`. """

        super(ProcessRequestItem, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ProcessRequestItem, self).elementProperties()
        js.extend(
            [("sequenceLinkId", "sequenceLinkId", int, "integer", False, None, True),]
        )
        return js


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
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + ".period"]
