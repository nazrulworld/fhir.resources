# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubstanceReferenceInformation
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
import typing

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class SubstanceReferenceInformation(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Todo.
    """

    resource_type = Field("SubstanceReferenceInformation", const=True)

    classification: typing.List[
        fhirtypes.SubstanceReferenceInformationClassificationType
    ] = Field(
        None,
        alias="classification",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    gene: typing.List[fhirtypes.SubstanceReferenceInformationGeneType] = Field(
        None,
        alias="gene",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    geneElement: typing.List[
        fhirtypes.SubstanceReferenceInformationGeneElementType
    ] = Field(
        None,
        alias="geneElement",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    target: typing.List[fhirtypes.SubstanceReferenceInformationTargetType] = Field(
        None,
        alias="target",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class SubstanceReferenceInformationClassification(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Todo.
    """

    resource_type = Field("SubstanceReferenceInformationClassification", const=True)

    classification: fhirtypes.CodeableConceptType = Field(
        None,
        alias="classification",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    domain: fhirtypes.CodeableConceptType = Field(
        None,
        alias="domain",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    source: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="source",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
    )

    subtype: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="subtype",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class SubstanceReferenceInformationGene(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Todo.
    """

    resource_type = Field("SubstanceReferenceInformationGene", const=True)

    gene: fhirtypes.CodeableConceptType = Field(
        None,
        alias="gene",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    geneSequenceOrigin: fhirtypes.CodeableConceptType = Field(
        None,
        alias="geneSequenceOrigin",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    source: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="source",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
    )


class SubstanceReferenceInformationGeneElement(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Todo.
    """

    resource_type = Field("SubstanceReferenceInformationGeneElement", const=True)

    element: fhirtypes.IdentifierType = Field(
        None,
        alias="element",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    source: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="source",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class SubstanceReferenceInformationTarget(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Todo.
    """

    resource_type = Field("SubstanceReferenceInformationTarget", const=True)

    amountQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="amountQuantity",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e amount[x]
        one_of_many="amount",
        one_of_many_required=False,
    )

    amountRange: fhirtypes.RangeType = Field(
        None,
        alias="amountRange",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e amount[x]
        one_of_many="amount",
        one_of_many_required=False,
    )

    amountString: fhirtypes.String = Field(
        None,
        alias="amountString",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e amount[x]
        one_of_many="amount",
        one_of_many_required=False,
    )
    amountString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_amountString", title="Extension field for ``amountString``."
    )

    amountType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="amountType",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    interaction: fhirtypes.CodeableConceptType = Field(
        None,
        alias="interaction",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    organism: fhirtypes.CodeableConceptType = Field(
        None,
        alias="organism",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    organismType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="organismType",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    source: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="source",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
    )

    target: fhirtypes.IdentifierType = Field(
        None,
        alias="target",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3819(
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
            "amount": ["amountQuantity", "amountRange", "amountString"]
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
