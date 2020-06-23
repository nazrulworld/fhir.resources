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
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Activity that occurred",
    )

    agent: ListType[fhirtypes.ProvenanceAgentType] = Field(
        ...,
        alias="agent",
        title="List of `ProvenanceAgent` items (represented as `dict` in JSON)",
        description="Actor involved",
    )

    entity: ListType[fhirtypes.ProvenanceEntityType] = Field(
        None,
        alias="entity",
        title="List of `ProvenanceEntity` items (represented as `dict` in JSON)",
        description="An entity used in this activity",
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title=(
            "Type `Reference` referencing `Location` (represented as `dict` in " "JSON)"
        ),
        description="Where the activity occurred, if relevant",
    )

    occurredDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurredDateTime",
        title="Type `DateTime`",
        description="When the activity occurred",
        one_of_many="occurred",  # Choice of Data Types. i.e value[x]
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
        title="Type `Period` (represented as `dict` in JSON)",
        description="When the activity occurred",
        one_of_many="occurred",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    policy: ListType[fhirtypes.Uri] = Field(
        None,
        alias="policy",
        title="List of `Uri` items",
        description="Policy or plan the activity was defined by",
    )
    policy__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_policy", title="Extension field for ``policy``."
    )

    reason: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reason",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Reason the activity is occurring",
    )

    recorded: fhirtypes.Instant = Field(
        ...,
        alias="recorded",
        title="Type `Instant`",
        description="When the activity was recorded / updated",
    )
    recorded__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_recorded", title="Extension field for ``recorded``."
    )

    signature: ListType[fhirtypes.SignatureType] = Field(
        None,
        alias="signature",
        title="List of `Signature` items (represented as `dict` in JSON)",
        description="Signature on target",
    )

    target: ListType[fhirtypes.ReferenceType] = Field(
        ...,
        alias="target",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="Target Reference(s) (usually version specific)",
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
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole, "
            "RelatedPerson, Patient, Device, Organization` (represented as `dict` "
            "in JSON)"
        ),
        description="Who the agent is representing",
    )

    role: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="role",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="What the agents role was",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="How the agent participated",
    )

    who: fhirtypes.ReferenceType = Field(
        ...,
        alias="who",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole, "
            "RelatedPerson, Patient, Device, Organization` (represented as `dict` "
            "in JSON)"
        ),
        description="Who participated",
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
        title="List of `ProvenanceAgent` items (represented as `dict` in JSON)",
        description="Entity is attributed to this agent",
    )

    role: fhirtypes.Code = Field(
        ...,
        alias="role",
        title="Type `Code`",
        description="derivation | revision | quotation | source | removal",
    )
    role__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_role", title="Extension field for ``role``."
    )

    what: fhirtypes.ReferenceType = Field(
        ...,
        alias="what",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Identity of entity",
    )
