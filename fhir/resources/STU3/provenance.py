# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Provenance
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

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

    resource_type = Field("Provenance", const=True)

    activity: fhirtypes.CodingType = Field(
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

    agent: typing.List[fhirtypes.ProvenanceAgentType] = Field(
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

    entity: typing.List[fhirtypes.ProvenanceEntityType] = Field(
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

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="When the activity occurred",
        description="The period during which the activity occurred.",
        # if property is element of this resource.
        element_property=True,
    )

    policy: typing.List[fhirtypes.Uri] = Field(
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
    policy__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_policy", title="Extension field for ``policy``.")

    reason: typing.List[fhirtypes.CodingType] = Field(
        None,
        alias="reason",
        title="Reason the activity is occurring",
        description="The reason that the activity was taking place.",
        # if property is element of this resource.
        element_property=True,
    )

    recorded: fhirtypes.Instant = Field(
        None,
        alias="recorded",
        title="When the activity was recorded / updated",
        description="The instant of time at which the activity was recorded.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    recorded__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_recorded", title="Extension field for ``recorded``."
    )

    signature: typing.List[fhirtypes.SignatureType] = Field(
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

    target: typing.List[fhirtypes.ReferenceType] = Field(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1222(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("recorded", "recorded__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class ProvenanceAgent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
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
        title="Who the agent is representing",
        description="The individual, device, or organization for whom the change was made.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e onBehalfOf[x]
        one_of_many="onBehalfOf",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "RelatedPerson",
            "Patient",
            "Device",
            "Organization",
        ],
    )

    onBehalfOfUri: fhirtypes.Uri = Field(
        None,
        alias="onBehalfOfUri",
        title="Who the agent is representing",
        description="The individual, device, or organization for whom the change was made.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e onBehalfOf[x]
        one_of_many="onBehalfOf",
        one_of_many_required=False,
    )
    onBehalfOfUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_onBehalfOfUri", title="Extension field for ``onBehalfOfUri``."
    )

    relatedAgentType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="relatedAgentType",
        title="Type of relationship between agents",
        description="The type of relationship between agents.",
        # if property is element of this resource.
        element_property=True,
    )

    role: typing.List[fhirtypes.CodeableConceptType] = Field(
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

    whoReference: fhirtypes.ReferenceType = Field(
        None,
        alias="whoReference",
        title="Who participated",
        description="The individual, device or organization that participated in the event.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e who[x]
        one_of_many="who",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "RelatedPerson",
            "Patient",
            "Device",
            "Organization",
        ],
    )

    whoUri: fhirtypes.Uri = Field(
        None,
        alias="whoUri",
        title="Who participated",
        description="The individual, device or organization that participated in the event.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e who[x]
        one_of_many="who",
        one_of_many_required=True,
    )
    whoUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1732(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An entity used in this activity.
    """

    resource_type = Field("ProvenanceEntity", const=True)

    agent: typing.List[fhirtypes.ProvenanceAgentType] = Field(
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
        None,
        alias="role",
        title="derivation | revision | quotation | source | removal",
        description="How the entity was used during the activity.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["derivation", "revision", "quotation", "source", "removal"],
    )
    role__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_role", title="Extension field for ``role``."
    )

    whatIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="whatIdentifier",
        title="Identity of entity",
        description=(
            "Identity of the  Entity used. May be a logical or physical uri and "
            "maybe absolute or relative."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e what[x]
        one_of_many="what",
        one_of_many_required=True,
    )

    whatReference: fhirtypes.ReferenceType = Field(
        None,
        alias="whatReference",
        title="Identity of entity",
        description=(
            "Identity of the  Entity used. May be a logical or physical uri and "
            "maybe absolute or relative."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e what[x]
        one_of_many="what",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    whatUri: fhirtypes.Uri = Field(
        None,
        alias="whatUri",
        title="Identity of entity",
        description=(
            "Identity of the  Entity used. May be a logical or physical uri and "
            "maybe absolute or relative."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e what[x]
        one_of_many="what",
        one_of_many_required=True,
    )
    whatUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1879(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("role", "role__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1879(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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
