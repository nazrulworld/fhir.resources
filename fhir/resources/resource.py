# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Resource
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import fhirabstractresource


class Resource(fhirabstractresource.FHIRAbstractResource):
    """ Base Resource.

    This is the base resource type for everything.
    """

    resource_type = "Resource"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.id = None
        """ Logical id of this artifact.
        Type `str`. """

        self.implicitRules = None
        """ A set of rules under which this content was created.
        Type `str`. """

        self.language = None
        """ Language of the resource content.
        Type `str`. """

        self.meta = None
        """ Metadata about the resource.
        Type `Meta` (represented as `dict` in JSON). """

        super(Resource, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Resource, self).elementProperties()
        js.extend(
            [
                ("id", "id", str, "string", False, None, False),
                ("implicitRules", "implicitRules", str, "uri", False, None, False),
                ("language", "language", str, "code", False, None, False),
                ("meta", "meta", meta.Meta, "Meta", False, None, False),
            ]
        )
        return js


try:
    from . import meta
except ImportError:
    meta = sys.modules[__package__ + ".meta"]
