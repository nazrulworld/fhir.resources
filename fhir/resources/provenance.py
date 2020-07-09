# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Provenance
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType
from typing import Union

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Provenance(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
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

    resource_type = Field("Provenance", const=True)

    activity: fhirtypes.CodeableConceptType = Field(
        None,
        alias="activity",
        title="Activity that occurred",
        description=(
            "An activity is something that occurs over a period of time and acts "
            "upon or with entities; it may include consuming, processing, "
            "transforming, modifying, relocating, using, or generating entities."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    agent: ListType[fhirtypes.ProvenanceAgentType] = Field(
        ...,
        alias="agent",
        title="Actor involved",
        description=(
            "An actor taking a role in an activity  for which it can be assigned "
            "some degree of responsibility for the activity taking place."
        ),
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

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title="Where the activity occurred, if relevant",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    occurredDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurredDateTime",
        title="When the activity occurred",
        description="The period during which the activity occurred.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurred[x]
        one_of_many="occurred",
        one_of_many_required=False,
    )
    occurredDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_occurredDateTime",
        title="Extension field for ``occurredDateTime``.",
    )

    occurredPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="occurredPeriod",
        title="When the activity occurred",
        description="The period during which the activity occurred.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurred[x]
        one_of_many="occurred",
        one_of_many_required=False,
    )

    policy: ListType[fhirtypes.Uri] = Field(
        None,
        alias="policy",
        title="Policy or plan the activity was defined by",
        description=(
            "Policy or plan the activity was defined by. Typically, a single "
            "activity may have multiple applicable policy documents, such as "
            "patient consent, guarantor funding, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    policy__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_policy", title="Extension field for ``policy``."
    )

    reason: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reason",
        title="Reason the activity is occurring",
        description="The reason that the activity was taking place.",
        # if property is element of this resource.
        element_property=True,
    )

    recorded: fhirtypes.Instant = Field(
        ...,
        alias="recorded",
        title="When the activity was recorded / updated",
        description="The instant of time at which the activity was recorded.",
        # if property is element of this resource.
        element_property=True,
    )
    recorded__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_recorded", title="Extension field for ``recorded``."
    )

    signature: ListType[fhirtypes.SignatureType] = Field(
        None,
        alias="signature",
        title="Signature on target",
        description=(
            "A digital signature on the target Reference(s). The signer should "
            "match a Provenance.agent. The purpose of the signature is indicated."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    target: ListType[fhirtypes.ReferenceType] = Field(
        ...,
        alias="target",
        title="Target Reference(s) (usually version specific)",
        description=(
            "The Reference(s) that were generated or updated by  the activity "
            "described in this resource. A provenance can point to more than one "
            "target if multiple resources were created/updated by the same "
            "activity."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    @root_validator(pre=True)
    def validate_one_of_many(cls, values: Dict[str, Any]) -> Dict[str, Any]:
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
        one_of_many_fields = {"occurred": ["occurredDateTime", "occurredPeriod"]}
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values


class ProvenanceAgent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Actor involved.
    An actor taking a role in an activity  for which it can be assigned some
    degree of responsibility for the activity taking place.
    """

    resource_type = Field("ProvenanceAgent", const=True)

    onBehalfOf: fhirtypes.ReferenceType = Field(
        None,
        alias="onBehalfOf",
        title="Who the agent is representing",
        description="The individual, device, or organization for whom the change was made.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "RelatedPerson",
            "Patient",
            "Device",
            "Organization",
        ],
    )

    role: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="role",
        title="What the agents role was",
        description=(
            "The function of the agent with respect to the activity. The security "
            "role enabling the agent with respect to the activity."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="How the agent participated",
        description="The participation the agent had with respect to the activity.",
        # if property is element of this resource.
        element_property=True,
    )

    who: fhirtypes.ReferenceType = Field(
        ...,
        alias="who",
        title="Who participated",
        description="The individual, device or organization that participated in the event.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "RelatedPerson",
            "Patient",
            "Device",
            "Organization",
        ],
    )


class ProvenanceEntity(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An entity used in this activity.
    """

    resource_type = Field("ProvenanceEntity", const=True)

    agent: ListType[fhirtypes.ProvenanceAgentType] = Field(
        None,
        alias="agent",
        title="Entity is attributed to this agent",
        description=(
            "The entity is attributed to an agent to express the agent's "
            "responsibility for that entity, possibly along with other agents. This"
            " description can be understood as shorthand for saying that the agent "
            "was responsible for the activity which generated the entity."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    role: fhirtypes.Code = Field(
        ...,
        alias="role",
        title="derivation | revision | quotation | source | removal",
        description="How the entity was used during the activity.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["derivation", "revision", "quotation", "source", "removal"],
    )
    role__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_role", title="Extension field for ``role``."
    )

    what: fhirtypes.ReferenceType = Field(
        ...,
        alias="what",
        title="Identity of entity",
        description=(
            "Identity of the  Entity used. May be a logical or physical uri and "
            "maybe absolute or relative."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )
