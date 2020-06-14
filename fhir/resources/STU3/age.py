# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Age
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic import Field

from . import quantity


class Age(quantity.Quantity):
    """ A duration of time during which an organism (or a process) has existed.
    """

    resource_type = Field("Age", const=True)
