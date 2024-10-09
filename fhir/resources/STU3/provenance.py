from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Provenance
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Provenance(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who, What, When for a set of resources.
    Provenance of a resource is a record that describes entities and processes
    involved in producing and delivering or otherwise influencing that
    resource. Provenance provides a critical foundation for assessing
    authenticity, enabling trust, and allowing reproducibility. Provenance
    assertions are a form of contextual metadata and can themselves become
    important records with their own provenance. Provenance statement indicates
    clinical significance in terms of confidence in authenticity, reliability,
    and trustworthiness, integrity, and stage in lifecycle (e.g. Document
    Completion - has the artifact been legally authenticated), all of which may
    impact security, privacy, and trust policies.
    """

    __resource_type__ = "Provenance"

    activity: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="activity",
        title="Activity that occurred",
        description=(
            "An activity is something that occurs over a period of time and acts "
            "upon or with entities; it may include consuming, processing, "
            "transforming, modifying, relocating, using, or generating entities."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    agent: typing.List[fhirtypes.ProvenanceAgentType] = Field(  # type: ignore
        ...,
        alias="agent",
        title="Actor involved",
        description=(
            "An actor taking a role in an activity  for which it can be assigned "
            "some degree of responsibility for the activity taking place."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    entity: typing.List[fhirtypes.ProvenanceEntityType] | None = Field(  # type: ignore
        None,
        alias="entity",
        title="An entity used in this activity",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    location: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="location",
        title="Where the activity occurred, if relevant",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="period",
        title="When the activity occurred",
        description="The period during which the activity occurred.",
        json_schema_extra={
            "element_property": True,
        },
    )

    policy: typing.List[fhirtypes.UriType | None] | None = Field(  # type: ignore
        None,
        alias="policy",
        title="Policy or plan the activity was defined by",
        description=(
            "Policy or plan the activity was defined by. Typically, a single "
            "activity may have multiple applicable policy documents, such as "
            "patient consent, guarantor funding, etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    policy__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_policy", title="Extension field for ``policy``."
    )

    reason: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        None,
        alias="reason",
        title="Reason the activity is occurring",
        description="The reason that the activity was taking place.",
        json_schema_extra={
            "element_property": True,
        },
    )

    recorded: fhirtypes.InstantType | None = Field(  # type: ignore
        None,
        alias="recorded",
        title="When the activity was recorded / updated",
        description="The instant of time at which the activity was recorded.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    recorded__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_recorded", title="Extension field for ``recorded``."
    )

    signature: typing.List[fhirtypes.SignatureType] | None = Field(  # type: ignore
        None,
        alias="signature",
        title="Signature on target",
        description=(
            "A digital signature on the target Reference(s). The signer should "
            "match a Provenance.agent. The purpose of the signature is indicated."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    target: typing.List[fhirtypes.ReferenceType] = Field(  # type: ignore
        ...,
        alias="target",
        title="Target Reference(s) (usually version specific)",
        description=(
            "The Reference(s) that were generated or updated by  the activity "
            "described in this resource. A provenance can point to more than one "
            "target if multiple resources were created/updated by the same "
            "activity."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Provenance`` according specification,
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
            "target",
            "period",
            "recorded",
            "policy",
            "location",
            "reason",
            "activity",
            "agent",
            "entity",
            "signature",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("recorded", "recorded__ext")]
        return required_fields


class ProvenanceAgent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Actor involved.
    An actor taking a role in an activity  for which it can be assigned some
    degree of responsibility for the activity taking place.
    """

    __resource_type__ = "ProvenanceAgent"

    onBehalfOfReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="onBehalfOfReference",
        title="Who the agent is representing",
        description="The individual, device, or organization for whom the change was made.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e onBehalfOf[x]
            "one_of_many": "onBehalfOf",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "RelatedPerson",
                "Patient",
                "Device",
                "Organization",
            ],
        },
    )

    onBehalfOfUri: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="onBehalfOfUri",
        title="Who the agent is representing",
        description="The individual, device, or organization for whom the change was made.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e onBehalfOf[x]
            "one_of_many": "onBehalfOf",
            "one_of_many_required": False,
        },
    )
    onBehalfOfUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_onBehalfOfUri", title="Extension field for ``onBehalfOfUri``."
    )

    relatedAgentType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="relatedAgentType",
        title="Type of relationship between agents",
        description="The type of relationship between agents.",
        json_schema_extra={
            "element_property": True,
        },
    )

    role: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="role",
        title="What the agents role was",
        description=(
            "The function of the agent with respect to the activity. The security "
            "role enabling the agent with respect to the activity."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    whoReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="whoReference",
        title="Who participated",
        description="The individual, device or organization that participated in the event.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e who[x]
            "one_of_many": "who",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "RelatedPerson",
                "Patient",
                "Device",
                "Organization",
            ],
        },
    )

    whoUri: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="whoUri",
        title="Who participated",
        description="The individual, device or organization that participated in the event.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e who[x]
            "one_of_many": "who",
            "one_of_many_required": True,
        },
    )
    whoUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_whoUri", title="Extension field for ``whoUri``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ProvenanceAgent`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "role",
            "whoUri",
            "whoReference",
            "whoReference",
            "whoReference",
            "whoReference",
            "whoReference",
            "onBehalfOfUri",
            "onBehalfOfReference",
            "onBehalfOfReference",
            "onBehalfOfReference",
            "onBehalfOfReference",
            "onBehalfOfReference",
            "relatedAgentType",
        ]

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "onBehalfOf": ["onBehalfOfReference", "onBehalfOfUri"],
            "who": ["whoReference", "whoUri"],
        }
        return one_of_many_fields


class ProvenanceEntity(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An entity used in this activity.
    """

    __resource_type__ = "ProvenanceEntity"

    agent: typing.List[fhirtypes.ProvenanceAgentType] | None = Field(  # type: ignore
        None,
        alias="agent",
        title="Entity is attributed to this agent",
        description=(
            "The entity is attributed to an agent to express the agent's "
            "responsibility for that entity, possibly along with other agents. This"
            " description can be understood as shorthand for saying that the agent "
            "was responsible for the activity which generated the entity."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    role: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="role",
        title="derivation | revision | quotation | source | removal",
        description="How the entity was used during the activity.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["derivation", "revision", "quotation", "source", "removal"],
        },
    )
    role__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_role", title="Extension field for ``role``."
    )

    whatIdentifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="whatIdentifier",
        title="Identity of entity",
        description=(
            "Identity of the  Entity used. May be a logical or physical uri and "
            "maybe absolute or relative."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e what[x]
            "one_of_many": "what",
            "one_of_many_required": True,
        },
    )

    whatReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="whatReference",
        title="Identity of entity",
        description=(
            "Identity of the  Entity used. May be a logical or physical uri and "
            "maybe absolute or relative."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e what[x]
            "one_of_many": "what",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    whatUri: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="whatUri",
        title="Identity of entity",
        description=(
            "Identity of the  Entity used. May be a logical or physical uri and "
            "maybe absolute or relative."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e what[x]
            "one_of_many": "what",
            "one_of_many_required": True,
        },
    )
    whatUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_whatUri", title="Extension field for ``whatUri``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ProvenanceEntity`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "role",
            "whatUri",
            "whatReference",
            "whatIdentifier",
            "agent",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("role", "role__ext")]
        return required_fields

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {"what": ["whatIdentifier", "whatReference", "whatUri"]}
        return one_of_many_fields
