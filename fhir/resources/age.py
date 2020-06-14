# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Age
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from pydantic import Field

from . import quantity


class Age(quantity.Quantity):
    """ A duration of time during which an organism (or a process) has existed.
    """

    resource_type = Field("Age", const=True)
