# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Provenance
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
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

    activity: fhirtypes.CodingType = Field(
        None,
        alias="activity",
        title="Type `Coding` (represented as `dict` in JSON)",
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

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When the activity occurred",
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

    reason: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="reason",
        title="List of `Coding` items (represented as `dict` in JSON)",
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


class ProvenanceAgent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Actor involved.
    An actor taking a role in an activity  for which it can be assigned some
    degree of responsibility for the activity taking place.
    """

    resource_type = Field("ProvenanceAgent", const=True)

    onBehalfOfReference: fhirtypes.ReferenceType = Field(
        None,
        alias="onBehalfOfReference",
        title=(
            "Type `Reference` referencing `Practitioner, RelatedPerson, Patient, "
            "Device, Organization` (represented as `dict` in JSON)"
        ),
        description="Who the agent is representing",
        one_of_many="onBehalfOf",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    onBehalfOfUri: fhirtypes.Uri = Field(
        None,
        alias="onBehalfOfUri",
        title="Type `Uri`",
        description="Who the agent is representing",
        one_of_many="onBehalfOf",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    onBehalfOfUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_onBehalfOfUri", title="Extension field for ``onBehalfOfUri``."
    )

    relatedAgentType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="relatedAgentType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of relationship between agents",
    )

    role: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="role",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="What the agents role was",
    )

    whoReference: fhirtypes.ReferenceType = Field(
        None,
        alias="whoReference",
        title=(
            "Type `Reference` referencing `Practitioner, RelatedPerson, Patient, "
            "Device, Organization` (represented as `dict` in JSON)"
        ),
        description="Who participated",
        one_of_many="who",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    whoUri: fhirtypes.Uri = Field(
        None,
        alias="whoUri",
        title="Type `Uri`",
        description="Who participated",
        one_of_many="who",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    whoUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_whoUri", title="Extension field for ``whoUri``."
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
        one_of_many_fields = {
            "onBehalfOf": ["onBehalfOfReference", "onBehalfOfUri"],
            "who": ["whoReference", "whoUri"],
        }
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

    whatIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="whatIdentifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Identity of entity",
        one_of_many="what",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    whatReference: fhirtypes.ReferenceType = Field(
        None,
        alias="whatReference",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Identity of entity",
        one_of_many="what",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    whatUri: fhirtypes.Uri = Field(
        None,
        alias="whatUri",
        title="Type `Uri`",
        description="Identity of entity",
        one_of_many="what",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    whatUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_whatUri", title="Extension field for ``whatUri``."
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
        one_of_many_fields = {"what": ["whatIdentifier", "whatReference", "whatUri"]}
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
