# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Distance
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic import Field

from . import quantity


class Distance(quantity.Quantity):
    """ A length - a value with a unit that is a physical distance.
    """

    resource_type = Field("Distance", const=True)
