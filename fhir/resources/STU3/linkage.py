from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Linkage
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Linkage(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Links records for 'same' item.
    Identifies two or more records (resource instances) that are referring to
    the same real-world "occurrence".
    """

    __resource_type__ = "Linkage"

    active: bool | None = Field(  # type: ignore
        None,
        alias="active",
        title="Whether this linkage assertion is active or not",
        description=(
            "Indicates whether the asserted set of linkages are considered to be "
            '"in effect".'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_active", title="Extension field for ``active``."
    )

    author: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="author",
        title="Who is responsible for linkages",
        description=(
            "Identifies the user or organization responsible for asserting the "
            "linkages and who establishes the context for evaluating the nature of "
            "each linkage."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner", "Organization"],
        },
    )

    item: typing.List[fhirtypes.LinkageItemType] = Field(  # type: ignore
        ...,
        alias="item",
        title="Item to be linked",
        description=(
            "Identifies one of the records that is considered to refer to the same "
            "real-world occurrence as well as how the items hould be evaluated "
            "within the collection of linked items."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Linkage`` according specification,
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
            "active",
            "author",
            "item",
        ]


class LinkageItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Item to be linked.
    Identifies one of the records that is considered to refer to the same real-
    world occurrence as well as how the items hould be evaluated within the
    collection of linked items.
    """

    __resource_type__ = "LinkageItem"

    resource: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="resource",
        title="Resource being linked",
        description="The resource instance being linked as part of the group.",
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="source | alternate | historical",
        description=(
            'Distinguishes which item is "source of truth" (if any) and which items'
            " are no longer considered to be current representations."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["source", "alternate", "historical"],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``LinkageItem`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "resource"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("type", "type__ext")]
        return required_fields
