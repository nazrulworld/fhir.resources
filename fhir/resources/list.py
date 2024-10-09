from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/List
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class List(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A list is a curated collection of resources.
    A List is a curated collection of resources, for things such as problem
    lists, allergy lists, facility list, organization list, etc.
    """

    __resource_type__ = "List"

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title="What the purpose of this list is",
        description="This code defines the purpose of the list - why it was created.",
        json_schema_extra={
            "element_property": True,
        },
    )

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="date",
        title="When the list was prepared",
        description="Date list was last reviewed/revised and determined to be 'current'.",
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    emptyReason: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="emptyReason",
        title="Why list is empty",
        description="If the list is empty, why the list is empty.",
        json_schema_extra={
            "element_property": True,
        },
    )

    encounter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="encounter",
        title="Context in which list created",
        description="The encounter that is the context in which this list was created.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter"],
        },
    )

    entry: typing.List[fhirtypes.ListEntryType] | None = Field(  # type: ignore
        None,
        alias="entry",
        title="Entries in the list",
        description="Entries in this list.",
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business identifier",
        description=(
            "Identifier for the List assigned for business purposes outside the "
            "context of FHIR."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    mode: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="mode",
        title="working | snapshot | changes",
        description=(
            "How this list was prepared - whether it is a working list that is "
            "suitable for being maintained on an ongoing basis, or if it represents"
            " a snapshot of a list of items from another source, or whether it is a"
            " prepared list where items may be marked as added, modified or "
            "deleted."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["working", "snapshot", "changes"],
        },
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_mode", title="Extension field for ``mode``."
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="note",
        title="Comments about the list",
        description="Comments that apply to the overall list.",
        json_schema_extra={
            "element_property": True,
        },
    )

    orderedBy: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="orderedBy",
        title="What order the list has",
        description="What order applies to the items in the list.",
        json_schema_extra={
            "element_property": True,
        },
    )

    source: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="source",
        title="Who and/or what defined the list contents (aka Author)",
        description=(
            "The entity responsible for deciding what the contents of the list "
            "were. Where the list was created by a human, this is the same as the "
            "author of the list."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Patient",
                "Device",
                "Organization",
                "RelatedPerson",
                "CareTeam",
            ],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="current | retired | entered-in-error",
        description="Indicates the current state of this list.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["current", "retired", "entered-in-error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="subject",
        title="If all resources have the same subject(s)",
        description=(
            "The common subject(s) (or patient(s)) of the resources that are in the"
            " list if there is one (or a set of subjects)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Descriptive name for the list",
        description="A label for the list assigned by the author.",
        json_schema_extra={
            "element_property": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``List`` according specification,
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
            "status",
            "mode",
            "title",
            "code",
            "subject",
            "encounter",
            "date",
            "source",
            "orderedBy",
            "note",
            "entry",
            "emptyReason",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("mode", "mode__ext"), ("status", "status__ext")]
        return required_fields


class ListEntry(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Entries in the list.
    Entries in this list.
    """

    __resource_type__ = "ListEntry"

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="date",
        title="When item added to list",
        description="When this item was added to the list.",
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    deleted: bool | None = Field(  # type: ignore
        None,
        alias="deleted",
        title="If this item is actually marked as deleted",
        description="True if this item is marked as deleted in the list.",
        json_schema_extra={
            "element_property": True,
        },
    )
    deleted__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_deleted", title="Extension field for ``deleted``."
    )

    flag: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="flag",
        title="Status/Workflow information about this item",
        description=(
            "The flag allows the system constructing the list to indicate the role "
            "and significance of the item in the list."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    item: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="item",
        title="Actual entry",
        description="A reference to the actual resource from which data was derived.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ListEntry`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "flag",
            "deleted",
            "date",
            "item",
        ]
