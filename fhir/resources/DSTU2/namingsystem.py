# -*- coding: utf-8 -*-
"""
Profile: https://www.hl7.org/fhir/DSTU2/namingsystem.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class NamingSystem(domainresource.DomainResource):
    """System of unique identification.

    A curated namespace that issues unique symbols within that namespace for
    the identification of concepts, people, devices, etc.  Represents a
    "System" used within the Identifier and Coding data types.
    """

    resource_type = Field("NamingSystem", const=True)

    contact: ListType[fhirtypes.NamingSystemContactType] = Field(
        None,
        alias="contact",
        title="Contact details for the publisher",
        description=(
            "Contact details to assist a user in finding and communicating with the"
            " publisher."
        ),
    )

    date: fhirtypes.DateTime = Field(
        ...,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the naming system was published. "
            "The date must change when the business version changes and it must "
            "change if the status code changes. In addition, it should change when "
            "the substantive content of the naming system changes."
        ),
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Natural language description of the naming system",
        description=(
            "A free text natural language description of the naming system from a "
            "consumer's perspective. Details about what the namespace identifies "
            "including scope, granularity, version labeling, etc."
        ),
    )

    kind: fhirtypes.Code = Field(
        ...,
        alias="kind",
        title="codesystem | identifier | root",
        description=(
            "Indicates the purpose for the naming system - what kinds of things "
            "does it make unique?"
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["codesystem", "identifier", "root"],
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Name for this naming system (computer friendly)",
        description=(
            "A natural language name identifying the naming system. This name "
            "should be usable as an identifier for the module by machine processing"
            " applications such as code generation."
        ),
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the organization or individual that published the naming "
            "system."
        ),
    )

    replacedBy: fhirtypes.ReferenceType = Field(
        None,
        alias="replacedBy",
        title=(
            "Type `Reference` referencing `NamingSystem` (represented as `dict` in "
            "JSON)."
        ),
        description="Use this instead.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["NamingSystem"],
    )

    responsible: fhirtypes.String = Field(
        None,
        alias="responsible",
        title="Who maintains system namespace?",
        description=(
            "The name of the organization that is responsible for issuing "
            "identifiers or codes for this namespace and ensuring their non-"
            "collision."
        ),
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="draft | active | retired",
        description=(
            "The status of this naming system. Enables tracking the life-cycle of "
            "the content."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="e.g. driver,  provider,  patient, bank etc.",
        description=(
            "Categorizes a naming system for easier search by grouping related "
            "naming systems."
        ),
    )

    uniqueId: ListType[fhirtypes.NamingSystemUniqueIdType] = Field(
        ...,
        alias="uniqueId",
        title="Unique identifiers used for system",
        description=(
            "Indicates how the system may be identified when referenced in "
            "electronic exchange."
        ),
    )

    usage: fhirtypes.String = Field(
        None,
        alias="usage",
        title="How/where is it used",
        description=(
            "Provides guidance on the use of the namespace, including the handling "
            "of formatting characters, use of upper vs. lower case, etc."
        ),
    )

    useContext: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="useContext",
        title="The context that the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These contexts may be general categories "
            "(gender, age, ...) or may be references to specific programs "
            "(insurance plans, studies, ...) and may be used to assist with "
            "indexing and searching for appropriate naming system instances."
        ),
    )


class NamingSystemContact(backboneelement.BackboneElement):
    """Contact details of the publisher.

    Contacts to assist a user in finding and communicating with the publisher.
    """

    resource_type = Field("NamingSystemContact", const=True)

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `str`.",
        description="Name of a individual to contact.",
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="List of `ContactPoint` items (represented as `dict` in JSON).",
        description="Contact details for individual or publisher.",
    )


class NamingSystemUniqueId(backboneelement.BackboneElement):
    """Unique identifiers used for system.

    Indicates how the system may be identified when referenced in electronic
    exchange.
    """

    resource_type = Field("NamingSystemUniqueId", const=True)

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="When is identifier valid?",
        description=(
            "Identifies the period of time over which this identifier is considered"
            " appropriate to refer to the naming system.  Outside of this window, "
            "the identifier might be non-deterministic."
        ),
    )

    preferred: fhirtypes.Boolean = Field(
        None,
        alias="preferred",
        title="Is this the id that should be used for this type",
        description=(
            'Indicates whether this identifier is the "preferred" identifier of '
            "this type."
        ),
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="oid | uuid | uri | other",
        description=(
            "Identifies the unique identifier scheme used for this particular "
            "identifier."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["oid", "uuid", "uri", "other"],
    )

    value: fhirtypes.String = Field(
        ...,
        alias="value",
        title="The unique identifier",
        description=(
            "The string that should be sent over the wire to identify the code "
            "system or identifier system."
        ),
    )
