from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Group
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Group(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Group of multiple entities.
    Represents a defined collection of entities that may be discussed or acted
    upon collectively but which are not expected to act collectively and are
    not formally or legally recognized; i.e. a collection of entities that
    isn't an Organization.
    """

    __resource_type__ = "Group"

    active: bool | None = Field(  # type: ignore
        None,
        alias="active",
        title="Whether this group's record is in active use",
        description=(
            "Indicates whether the record for the group is available for use or is "
            "merely being retained for historical purposes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_active", title="Extension field for ``active``."
    )

    actual: bool | None = Field(  # type: ignore
        None,
        alias="actual",
        title="Descriptive or actual",
        description=(
            "If true, indicates that the resource refers to a specific group of "
            "real individuals.  If false, the group defines a set of intended "
            "individuals."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    actual__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_actual", title="Extension field for ``actual``."
    )

    characteristic: typing.List[fhirtypes.GroupCharacteristicType] | None = Field(  # type: ignore
        None,
        alias="characteristic",
        title="Trait of group members",
        description="Identifies the traits shared by members of the group.",
        json_schema_extra={
            "element_property": True,
        },
    )

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Kind of Group members",
        description=(
            'Provides a specific type of resource the group includes; e.g. "cow", '
            '"syringe", etc.'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Unique id",
        description="A unique business identifier for this group.",
        json_schema_extra={
            "element_property": True,
        },
    )

    member: typing.List[fhirtypes.GroupMemberType] | None = Field(  # type: ignore
        None,
        alias="member",
        title="Who or what is in group",
        description="Identifies the resource instances that are members of the group.",
        json_schema_extra={
            "element_property": True,
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Label for Group",
        description=(
            "A label assigned to the group for human identification and "
            "communication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    quantity: fhirtypes.UnsignedIntType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="Number of members",
        description=(
            "A count of the number of resource instances that are part of the " "group."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    quantity__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_quantity", title="Extension field for ``quantity``."
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="person | animal | practitioner | device | medication | substance",
        description=(
            "Identifies the broad classification of the kind of resources the group"
            " includes."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "person",
                "animal",
                "practitioner",
                "device",
                "medication",
                "substance",
            ],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Group`` according specification,
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
            "active",
            "type",
            "actual",
            "code",
            "name",
            "quantity",
            "characteristic",
            "member",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("actual", "actual__ext"), ("type", "type__ext")]
        return required_fields


class GroupCharacteristic(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Trait of group members.
    Identifies the traits shared by members of the group.
    """

    __resource_type__ = "GroupCharacteristic"

    code: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="code",
        title="Kind of characteristic",
        description="A code that identifies the kind of trait being asserted.",
        json_schema_extra={
            "element_property": True,
        },
    )

    exclude: bool | None = Field(  # type: ignore
        None,
        alias="exclude",
        title="Group includes or excludes",
        description=(
            "If true, indicates the characteristic is one that is NOT held by "
            "members of the group."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    exclude__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_exclude", title="Extension field for ``exclude``."
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="period",
        title="Period over which characteristic is tested",
        description=(
            "The period over which the characteristic is tested; e.g. the patient "
            "had an operation during the month of June."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    valueBoolean: bool | None = Field(  # type: ignore
        None,
        alias="valueBoolean",
        title="Value held by characteristic",
        description=(
            "The value of the trait that holds (or does not hold - see 'exclude') "
            "for members of the group."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="valueCodeableConcept",
        title="Value held by characteristic",
        description=(
            "The value of the trait that holds (or does not hold - see 'exclude') "
            "for members of the group."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="valueQuantity",
        title="Value held by characteristic",
        description=(
            "The value of the trait that holds (or does not hold - see 'exclude') "
            "for members of the group."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueRange: fhirtypes.RangeType | None = Field(  # type: ignore
        None,
        alias="valueRange",
        title="Value held by characteristic",
        description=(
            "The value of the trait that holds (or does not hold - see 'exclude') "
            "for members of the group."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``GroupCharacteristic`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "valueCodeableConcept",
            "valueBoolean",
            "valueQuantity",
            "valueRange",
            "exclude",
            "period",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("exclude", "exclude__ext")]
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
        one_of_many_fields = {
            "value": [
                "valueBoolean",
                "valueCodeableConcept",
                "valueQuantity",
                "valueRange",
            ]
        }
        return one_of_many_fields


class GroupMember(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who or what is in group.
    Identifies the resource instances that are members of the group.
    """

    __resource_type__ = "GroupMember"

    entity: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="entity",
        title="Reference to the group member",
        description=(
            "A reference to the entity that is a member of the group. Must be "
            "consistent with Group.type."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Patient",
                "Practitioner",
                "Device",
                "Medication",
                "Substance",
            ],
        },
    )

    inactive: bool | None = Field(  # type: ignore
        None,
        alias="inactive",
        title="If member is no longer in group",
        description=(
            "A flag to indicate that the member is no longer in the group, but "
            "previously may have been a member."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    inactive__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_inactive", title="Extension field for ``inactive``."
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="period",
        title="Period member belonged to the group",
        description="The period that the member was in the group, if known.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``GroupMember`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "entity", "period", "inactive"]
