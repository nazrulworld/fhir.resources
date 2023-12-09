# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/FormularyItem
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field

from . import domainresource, fhirtypes


class FormularyItem(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Definition of a FormularyItem.
    This resource describes a product or service that is available through a
    program and includes the conditions and constraints of availability.  All
    of the information in this resource is specific to the inclusion of the
    item in the formulary and is not inherent to the item itself.
    """

    resource_type = Field("FormularyItem", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Codes that identify this formulary item",
        description=(
            "A code (or set of codes) that specify the product or service that is "
            "identified by this formulary item."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier for this formulary item",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="active | entered-in-error | inactive",
        description=(
            "The validity about the information of the formulary item and not of "
            "the underlying product or service itself."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "entered-in-error", "inactive"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``FormularyItem`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "identifier",
            "code",
            "status",
        ]
