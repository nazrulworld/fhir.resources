# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Distance
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from pydantic import Field

from . import quantity


class Distance(quantity.Quantity):
    """ A length - a value with a unit that is a physical distance.
    """

    resource_type = Field("Distance", const=True)
