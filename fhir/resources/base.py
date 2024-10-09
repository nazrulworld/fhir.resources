from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Base
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from fhir_core import fhirabstractmodel


class Base(fhirabstractmodel.FHIRAbstractModel):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Base for all types and resources.
    Base definition for all types defined in FHIR type system.
    """

    __resource_type__ = "Base"

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Base`` according specification,
        with preserving original sequence order.
        """
        return []
