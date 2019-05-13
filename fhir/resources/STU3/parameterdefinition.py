#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.1.11917 (http://hl7.org/fhir/StructureDefinition/ParameterDefinition) on 2019-05-13.
#  2019, SMART Health IT.


from . import element

class ParameterDefinition(element.Element):
    """ Definition of a parameter to a module.

    The parameters to the module. This collection specifies both the input and
    output parameters. Input parameters are provided by the caller as part of
    the $evaluate operation. Output parameters are included in the
    GuidanceResponse.
    """

    resource_type = "ParameterDefinition"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.documentation = None
        """ A brief description of the parameter.
        Type `str`. """

        self.max = None
        """ Maximum cardinality (a number of *).
        Type `str`. """

        self.min = None
        """ Minimum cardinality.
        Type `int`. """

        self.name = None
        """ Name used to access the parameter value.
        Type `str`. """

        self.profile = None
        """ What profile the value is expected to be.
        Type `FHIRReference` referencing `StructureDefinition` (represented as `dict` in JSON). """

        self.type = None
        """ What type of value.
        Type `str`. """

        self.use = None
        """ in | out.
        Type `str`. """

        super(ParameterDefinition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ParameterDefinition, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, "string", False, None, False),
            ("max", "max", str, "string", False, None, False),
            ("min", "min", int, "integer", False, None, False),
            ("name", "name", str, "code", False, None, False),
            ("profile", "profile", fhirreference.FHIRReference, "Reference", False, None, False),
            ("type", "type", str, "code", False, None, True),
            ("use", "use", str, "code", False, None, True),
        ])
        return js


import sys
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
