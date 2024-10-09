from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/SubstanceReferenceInformation
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class SubstanceReferenceInformation(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Todo.
    """

    __resource_type__ = "SubstanceReferenceInformation"

    comment: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="comment",
        title="Todo",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_comment", title="Extension field for ``comment``."
    )

    gene: typing.List[fhirtypes.SubstanceReferenceInformationGeneType] | None = Field(  # type: ignore
        None,
        alias="gene",
        title="Todo",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    geneElement: typing.List[fhirtypes.SubstanceReferenceInformationGeneElementType] | None = Field(  # type: ignore
        None,
        alias="geneElement",
        title="Todo",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    target: typing.List[fhirtypes.SubstanceReferenceInformationTargetType] | None = Field(  # type: ignore
        None,
        alias="target",
        title="Todo",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceReferenceInformation`` according specification,
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
            "comment",
            "gene",
            "geneElement",
            "target",
        ]


class SubstanceReferenceInformationGene(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Todo.
    """

    __resource_type__ = "SubstanceReferenceInformationGene"

    gene: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="gene",
        title="Todo",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    geneSequenceOrigin: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="geneSequenceOrigin",
        title="Todo",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    source: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="source",
        title="Todo",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DocumentReference"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceReferenceInformationGene`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "geneSequenceOrigin",
            "gene",
            "source",
        ]


class SubstanceReferenceInformationGeneElement(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Todo.
    """

    __resource_type__ = "SubstanceReferenceInformationGeneElement"

    element: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="element",
        title="Todo",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    source: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="source",
        title="Todo",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DocumentReference"],
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Todo",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceReferenceInformationGeneElement`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "element", "source"]


class SubstanceReferenceInformationTarget(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Todo.
    """

    __resource_type__ = "SubstanceReferenceInformationTarget"

    amountQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="amountQuantity",
        title="Todo",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e amount[x]
            "one_of_many": "amount",
            "one_of_many_required": False,
        },
    )

    amountRange: fhirtypes.RangeType | None = Field(  # type: ignore
        None,
        alias="amountRange",
        title="Todo",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e amount[x]
            "one_of_many": "amount",
            "one_of_many_required": False,
        },
    )

    amountString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="amountString",
        title="Todo",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e amount[x]
            "one_of_many": "amount",
            "one_of_many_required": False,
        },
    )
    amountString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_amountString", title="Extension field for ``amountString``."
    )

    amountType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="amountType",
        title="Todo",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    interaction: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="interaction",
        title="Todo",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    organism: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="organism",
        title="Todo",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    organismType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="organismType",
        title="Todo",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    source: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="source",
        title="Todo",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DocumentReference"],
        },
    )

    target: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="target",
        title="Todo",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Todo",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceReferenceInformationTarget`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "target",
            "type",
            "interaction",
            "organism",
            "organismType",
            "amountQuantity",
            "amountRange",
            "amountString",
            "amountType",
            "source",
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
            "amount": ["amountQuantity", "amountRange", "amountString"]
        }
        return one_of_many_fields
