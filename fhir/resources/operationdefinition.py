#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/OperationDefinition) on 2019-05-13.
#  2019, SMART Health IT.


from . import domainresource

class OperationDefinition(domainresource.DomainResource):
    """ Definition of an operation or a named query.

    A formal computable definition of an operation (on the RESTful interface)
    or a named query (using the search interaction).
    """

    resource_type = "OperationDefinition"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.affectsState = None
        """ Whether content is changed by the operation.
        Type `bool`. """

        self.base = None
        """ Marks this as a profile of the base.
        Type `str`. """

        self.code = None
        """ Name used to invoke the operation.
        Type `str`. """

        self.comment = None
        """ Additional information about use.
        Type `str`. """

        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.date = None
        """ Date last changed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.description = None
        """ Natural language description of the operation definition.
        Type `str`. """

        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """

        self.inputProfile = None
        """ Validation information for in parameters.
        Type `str`. """

        self.instance = None
        """ Invoke on an instance?.
        Type `bool`. """

        self.jurisdiction = None
        """ Intended jurisdiction for operation definition (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.kind = None
        """ operation | query.
        Type `str`. """

        self.name = None
        """ Name for this operation definition (computer friendly).
        Type `str`. """

        self.outputProfile = None
        """ Validation information for out parameters.
        Type `str`. """

        self.overload = None
        """ Define overloaded variants for when  generating code.
        List of `OperationDefinitionOverload` items (represented as `dict` in JSON). """

        self.parameter = None
        """ Parameters for the operation/query.
        List of `OperationDefinitionParameter` items (represented as `dict` in JSON). """

        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """

        self.purpose = None
        """ Why this operation definition is defined.
        Type `str`. """

        self.resource = None
        """ Types this operation applies to.
        List of `str` items. """

        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """

        self.system = None
        """ Invoke at the system level?.
        Type `bool`. """

        self.title = None
        """ Name for this operation definition (human friendly).
        Type `str`. """

        self.type = None
        """ Invoke at the type level?.
        Type `bool`. """

        self.url = None
        """ Canonical identifier for this operation definition, represented as
        a URI (globally unique).
        Type `str`. """

        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """

        self.version = None
        """ Business version of the operation definition.
        Type `str`. """

        super(OperationDefinition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(OperationDefinition, self).elementProperties()
        js.extend([
            ("affectsState", "affectsState", bool, "boolean", False, None, False),
            ("base", "base", str, "canonical", False, None, False),
            ("code", "code", str, "code", False, None, True),
            ("comment", "comment", str, "markdown", False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, "ContactDetail", True, None, False),
            ("date", "date", fhirdate.FHIRDate, "dateTime", False, None, False),
            ("description", "description", str, "markdown", False, None, False),
            ("experimental", "experimental", bool, "boolean", False, None, False),
            ("inputProfile", "inputProfile", str, "canonical", False, None, False),
            ("instance", "instance", bool, "boolean", False, None, True),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, "CodeableConcept", True, None, False),
            ("kind", "kind", str, "code", False, None, True),
            ("name", "name", str, "string", False, None, True),
            ("outputProfile", "outputProfile", str, "canonical", False, None, False),
            ("overload", "overload", OperationDefinitionOverload, "OperationDefinitionOverload", True, None, False),
            ("parameter", "parameter", OperationDefinitionParameter, "OperationDefinitionParameter", True, None, False),
            ("publisher", "publisher", str, "string", False, None, False),
            ("purpose", "purpose", str, "markdown", False, None, False),
            ("resource", "resource", str, "code", True, None, False),
            ("status", "status", str, "code", False, None, True),
            ("system", "system", bool, "boolean", False, None, True),
            ("title", "title", str, "string", False, None, False),
            ("type", "type", bool, "boolean", False, None, True),
            ("url", "url", str, "uri", False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, "UsageContext", True, None, False),
            ("version", "version", str, "string", False, None, False),
        ])
        return js


from . import backboneelement

class OperationDefinitionOverload(backboneelement.BackboneElement):
    """ Define overloaded variants for when  generating code.

    Defines an appropriate combination of parameters to use when invoking this
    operation, to help code generators when generating overloaded parameter
    sets for this operation.
    """

    resource_type = "OperationDefinitionOverload"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.comment = None
        """ Comments to go on overload.
        Type `str`. """

        self.parameterName = None
        """ Name of parameter to include in overload.
        List of `str` items. """

        super(OperationDefinitionOverload, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(OperationDefinitionOverload, self).elementProperties()
        js.extend([
            ("comment", "comment", str, "string", False, None, False),
            ("parameterName", "parameterName", str, "string", True, None, False),
        ])
        return js


class OperationDefinitionParameter(backboneelement.BackboneElement):
    """ Parameters for the operation/query.

    The parameters for the operation/query.
    """

    resource_type = "OperationDefinitionParameter"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.binding = None
        """ ValueSet details if this is coded.
        Type `OperationDefinitionParameterBinding` (represented as `dict` in JSON). """

        self.documentation = None
        """ Description of meaning/use.
        Type `str`. """

        self.max = None
        """ Maximum Cardinality (a number or *).
        Type `str`. """

        self.min = None
        """ Minimum Cardinality.
        Type `int`. """

        self.name = None
        """ Name in Parameters.parameter.name or in URL.
        Type `str`. """

        self.part = None
        """ Parts of a nested Parameter.
        List of `OperationDefinitionParameter` items (represented as `dict` in JSON). """

        self.referencedFrom = None
        """ References to this parameter.
        List of `OperationDefinitionParameterReferencedFrom` items (represented as `dict` in JSON). """

        self.searchType = None
        """ number | date | string | token | reference | composite | quantity |
        uri | special.
        Type `str`. """

        self.targetProfile = None
        """ If type is Reference | canonical, allowed targets.
        List of `str` items. """

        self.type = None
        """ What type this parameter has.
        Type `str`. """

        self.use = None
        """ in | out.
        Type `str`. """

        super(OperationDefinitionParameter, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(OperationDefinitionParameter, self).elementProperties()
        js.extend([
            ("binding", "binding", OperationDefinitionParameterBinding, "OperationDefinitionParameterBinding", False, None, False),
            ("documentation", "documentation", str, "string", False, None, False),
            ("max", "max", str, "string", False, None, True),
            ("min", "min", int, "integer", False, None, True),
            ("name", "name", str, "code", False, None, True),
            ("part", "part", OperationDefinitionParameter, "OperationDefinitionParameter", True, None, False),
            ("referencedFrom", "referencedFrom", OperationDefinitionParameterReferencedFrom, "OperationDefinitionParameterReferencedFrom", True, None, False),
            ("searchType", "searchType", str, "code", False, None, False),
            ("targetProfile", "targetProfile", str, "canonical", True, None, False),
            ("type", "type", str, "code", False, None, False),
            ("use", "use", str, "code", False, None, True),
        ])
        return js


class OperationDefinitionParameterBinding(backboneelement.BackboneElement):
    """ ValueSet details if this is coded.

    Binds to a value set if this parameter is coded (code, Coding,
    CodeableConcept).
    """

    resource_type = "OperationDefinitionParameterBinding"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.strength = None
        """ required | extensible | preferred | example.
        Type `str`. """

        self.valueSet = None
        """ Source of value set.
        Type `str`. """

        super(OperationDefinitionParameterBinding, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(OperationDefinitionParameterBinding, self).elementProperties()
        js.extend([
            ("strength", "strength", str, "code", False, None, True),
            ("valueSet", "valueSet", str, "canonical", False, None, True),
        ])
        return js


class OperationDefinitionParameterReferencedFrom(backboneelement.BackboneElement):
    """ References to this parameter.

    Identifies other resource parameters within the operation invocation that
    are expected to resolve to this resource.
    """

    resource_type = "OperationDefinitionParameterReferencedFrom"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.source = None
        """ Referencing parameter.
        Type `str`. """

        self.sourceId = None
        """ Element id of reference.
        Type `str`. """

        super(OperationDefinitionParameterReferencedFrom, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(OperationDefinitionParameterReferencedFrom, self).elementProperties()
        js.extend([
            ("source", "source", str, "string", False, None, True),
            ("sourceId", "sourceId", str, "string", False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
