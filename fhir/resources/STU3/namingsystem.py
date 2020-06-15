# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/NamingSystem
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class NamingSystem(domainresource.DomainResource):
    """ System of unique identification.
    A curated namespace that issues unique symbols within that namespace for
    the identification of concepts, people, devices, etc.  Represents a
    "System" used within the Identifier and Coding data types.
    """

    resource_type = Field("NamingSystem", const=True)

    contact: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Contact details for the publisher",
    )

    date: fhirtypes.DateTime = Field(
        ...,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date this was last changed",
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Natural language description of the naming system",
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Intended jurisdiction for naming system (if applicable)",
    )

    kind: fhirtypes.Code = Field(
        ...,
        alias="kind",
        title="Type `Code` (represented as `dict` in JSON)",
        description="codesystem | identifier | root",
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this naming system (computer friendly)",
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of the publisher (organization or individual)",
    )

    replacedBy: fhirtypes.ReferenceType = Field(
        None,
        alias="replacedBy",
        title=(
            "Type `Reference` referencing `NamingSystem` (represented as `dict` in "
            "JSON)"
        ),
        description="Use this instead",
    )

    responsible: fhirtypes.String = Field(
        None,
        alias="responsible",
        title="Type `String` (represented as `dict` in JSON)",
        description="Who maintains system namespace?",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="draft | active | retired | unknown",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="e.g. driver,  provider,  patient, bank etc.",
    )

    uniqueId: ListType[fhirtypes.NamingSystemUniqueIdType] = Field(
        ...,
        alias="uniqueId",
        title="List of `NamingSystemUniqueId` items (represented as `dict` in JSON)",
        description="Unique identifiers used for system",
    )

    usage: fhirtypes.String = Field(
        None,
        alias="usage",
        title="Type `String` (represented as `dict` in JSON)",
        description="How/where is it used",
    )

    useContext: ListType[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="List of `UsageContext` items (represented as `dict` in JSON)",
        description="Context the content is intended to support",
    )


class NamingSystemUniqueId(backboneelement.BackboneElement):
    """ Unique identifiers used for system.
    Indicates how the system may be identified when referenced in electronic
    exchange.
    """

    resource_type = Field("NamingSystemUniqueId", const=True)

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Type `String` (represented as `dict` in JSON)",
        description="Notes about identifier usage",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When is identifier valid?",
    )

    preferred: bool = Field(
        None,
        alias="preferred",
        title="Type `bool`",
        description="Is this the id that should be used for this type",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="oid | uuid | uri | other",
    )

    value: fhirtypes.String = Field(
        ...,
        alias="value",
        title="Type `String` (represented as `dict` in JSON)",
        description="The unique identifier",
    )
