# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/DSTU2/provenance.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic.v1 import Field

from . import domainresource, fhirtypes
from .backboneelement import BackboneElement


class Provenance(domainresource.DomainResource):
    """Who, What, When for a set of resources


    Provenance of a resource is a record that describes entities and processes
    involved in producing and delivering or otherwise influencing that resource.
     Provenance provides a critical foundation for assessing authenticity,
     enabling trust, and allowing reproducibility. Provenance assertions are a
     form of contextual metadata and can themselves become important records
     with their own provenance. Provenance statement indicates clinical
     significance in terms of confidence in authenticity, reliability, and
     trustworthiness, integrity, and stage in lifecycle (e.g. Document
     Completion - has the artifact been legally authenticated), all of which
     may impact security, privacy, and trust policies.
    """

    resource_type = Field("Provenance", const=True)

    target: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="target",
        title="Type 'Reference' referencing 'Any'  (represented as 'dict' in JSON).",
        description="Target Reference(s) (usually version specific)",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Any"],
        element_property=True,
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="When the activity occurred",
        description="The period during which the activity occurred.",
        # if property is element of this resource.
        element_property=True,
    )

    recorded: fhirtypes.Instant = Field(
        ...,
        alias="recorded",
        title="Type `Instant` (represented as `dict` in JSON)",
        description="When the activity was recorded / updated",
        element_property=True,
    )

    reason: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reason",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Reason the activity is occurring",
        element_property=True,
    )

    activity: fhirtypes.CodeableConceptType = Field(
        None,
        alias="activity",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Activity that occurred",
        element_property=True,
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title="Type 'Reference' referencing 'Location'  (represented as 'dict' in JSON).",
        description="Where the activity occurred, if relevant",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
        element_property=True,
    )

    policy: ListType[fhirtypes.Uri] = Field(
        None,
        alias="policy",
        title="Policy or plan the activity was defined by",
        description=(
            "Policy or plan the activity was defined by. Typically, "
            "a single activity may have multiple applicable policy documents, "
            "such as patient consent, guarantor funding, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    agent: ListType[fhirtypes.ProvenanceAgentType] = Field(
        None,
        alias="agent",
        title="Agents involved in creating resource",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    entity: ListType[fhirtypes.ProvenanceEntityType] = Field(
        None,
        alias="entity",
        title="An entity used in this activity",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    signature: ListType[fhirtypes.SignatureType] = Field(
        None,
        alias="signature",
        title="List of Type `Signature` (represented as `dict` in JSON)",
        description="Value of extension",
        element_property=True,
    )


class ProvenanceAgent(BackboneElement):
    """Agents involved in creating resource


    An agent takes a role in an activity such that the agent can be assigned
    some degree of responsibility for the activity taking place. An agent can
    be a person, an organization, software, or other entities that may be
    ascribed responsibility.
    """

    resource_type = Field("ProvenanceAgent", const=True)

    role: fhirtypes.CodingType = Field(
        None,
        alias="role",
        title="What the agents involvement was",
        description="The function of the agent with respect to the activity.",
        # if property is element of this resource.
        element_property=True,
    )

    actor: fhirtypes.ReferenceType = Field(
        None,
        alias="actor",
        title=(
            "Type 'Reference' referencing 'Practitioner', 'RelatedPerson',"
            " 'Patient', 'Device', 'Organization'  "
            "(represented as 'dict' in JSON)."
        ),
        description="Individual, device or organization playing role",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "RelatedPerson",
            "Patient",
            "Device",
            "Organization",
        ],
        element_property=True,
    )

    userId: fhirtypes.IdentifierType = Field(
        None,
        alias="userId",
        title="Authorization-system identifier for the agent",
        description="The identity of the agent as known by the authorization system.",
        element_property=True,
    )

    relatedAgent: ListType[fhirtypes.ProvenanceAgentRelatedAgentType] = Field(
        None,
        alias="relatedAgent",
        title="Track delegation between agents",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class ProvenanceAgentRelatedAgent(BackboneElement):
    """Track delegation between agents


    A relationship between two the agents referenced in this resource.
    This is defined to allow for explicit description of the delegation
    between agents. For example, this human author used this device, or
    one person acted on another's behest.
    """

    resource_type = Field("ProvenanceAgentRelatedAgent", const=True)

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Type of relationship between agents",
        element_property=True,
    )

    target: fhirtypes.Uri = Field(
        None,
        alias="target",
        title="Reference to other agent in this resource by identifier",
        description=(
            "An internal reference to another agent listed in "
            "this provenance by its identifier."
        ),
        # if property is element of this resource.
        element_property=True,
    )


class ProvenanceEntity(BackboneElement):
    """An entity used in this activity


    An entity used in this activity.
    """

    resource_type = Field("ProvenanceEntity", const=True)

    role: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON).",
        description="derivation | revision | quotation | source",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["derivation", "revision", "quotation", "source"],
        element_property=True,
    )

    type: fhirtypes.CodingType = Field(
        None,
        alias="type",
        title="The type of resource in this entity",
        description=(
            "The type of the entity. If the entity is a resource, "
            "then this is a resource type."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    reference: fhirtypes.Uri = Field(
        None,
        alias="reference",
        title="Identity of entity",
        description=(
            "Identity of the Entity used. May be a logical or physical "
            "uri and maybe absolute or relative."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    display: fhirtypes.String = Field(
        None,
        alias="display",
        title="Human description of entity",
        description="Human-readable description of the entity.",
        element_property=True,
    )

    agent: fhirtypes.ProvenanceAgentType = Field(
        None,
        alias="agent",
        title="Entity is attributed to this agent",
        description=(
            "The entity is attributed to an agent to express the agent's"
            " responsibility for that entity, possibly along with other agents."
            " This description can be understood as shorthand for saying that the"
            " agent was responsible for the activity which generated the entity"
        ),
        # if property is element of this resource.
        element_property=True,
    )
