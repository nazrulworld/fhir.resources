# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubstanceReferenceInformation
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class SubstanceReferenceInformation(domainresource.DomainResource):
    """ Todo.
    """

    resource_type = Field("SubstanceReferenceInformation", const=True)

    classification: ListType[
        fhirtypes.SubstanceReferenceInformationClassificationType
    ] = Field(
        None,
        alias="classification",
        title=(
            "List of `SubstanceReferenceInformationClassification` items "
            "(represented as `dict` in JSON)"
        ),
        description="Todo",
    )

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Type `String` (represented as `dict` in JSON)",
        description="Todo",
    )

    gene: ListType[fhirtypes.SubstanceReferenceInformationGeneType] = Field(
        None,
        alias="gene",
        title=(
            "List of `SubstanceReferenceInformationGene` items (represented as "
            "`dict` in JSON)"
        ),
        description="Todo",
    )

    geneElement: ListType[
        fhirtypes.SubstanceReferenceInformationGeneElementType
    ] = Field(
        None,
        alias="geneElement",
        title=(
            "List of `SubstanceReferenceInformationGeneElement` items (represented "
            "as `dict` in JSON)"
        ),
        description="Todo",
    )

    target: ListType[fhirtypes.SubstanceReferenceInformationTargetType] = Field(
        None,
        alias="target",
        title=(
            "List of `SubstanceReferenceInformationTarget` items (represented as "
            "`dict` in JSON)"
        ),
        description="Todo",
    )


class SubstanceReferenceInformationClassification(backboneelement.BackboneElement):
    """ Todo.
    """

    resource_type = Field("SubstanceReferenceInformationClassification", const=True)

    classification: fhirtypes.CodeableConceptType = Field(
        None,
        alias="classification",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Todo",
    )

    domain: fhirtypes.CodeableConceptType = Field(
        None,
        alias="domain",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Todo",
    )

    source: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="source",
        title=(
            "List of `Reference` items referencing `DocumentReference` (represented"
            " as `dict` in JSON)"
        ),
        description="Todo",
    )

    subtype: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="subtype",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Todo",
    )


class SubstanceReferenceInformationGene(backboneelement.BackboneElement):
    """ Todo.
    """

    resource_type = Field("SubstanceReferenceInformationGene", const=True)

    gene: fhirtypes.CodeableConceptType = Field(
        None,
        alias="gene",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Todo",
    )

    geneSequenceOrigin: fhirtypes.CodeableConceptType = Field(
        None,
        alias="geneSequenceOrigin",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Todo",
    )

    source: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="source",
        title=(
            "List of `Reference` items referencing `DocumentReference` (represented"
            " as `dict` in JSON)"
        ),
        description="Todo",
    )


class SubstanceReferenceInformationGeneElement(backboneelement.BackboneElement):
    """ Todo.
    """

    resource_type = Field("SubstanceReferenceInformationGeneElement", const=True)

    element: fhirtypes.IdentifierType = Field(
        None,
        alias="element",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Todo",
    )

    source: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="source",
        title=(
            "List of `Reference` items referencing `DocumentReference` (represented"
            " as `dict` in JSON)"
        ),
        description="Todo",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Todo",
    )


class SubstanceReferenceInformationTarget(backboneelement.BackboneElement):
    """ Todo.
    """

    resource_type = Field("SubstanceReferenceInformationTarget", const=True)

    amountQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="amountQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Todo",
        one_of_many="amount",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    amountRange: fhirtypes.RangeType = Field(
        None,
        alias="amountRange",
        title="Type `Range` (represented as `dict` in JSON)",
        description="Todo",
        one_of_many="amount",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    amountString: fhirtypes.String = Field(
        None,
        alias="amountString",
        title="Type `String` (represented as `dict` in JSON)",
        description="Todo",
        one_of_many="amount",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    amountType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="amountType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Todo",
    )

    interaction: fhirtypes.CodeableConceptType = Field(
        None,
        alias="interaction",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Todo",
    )

    organism: fhirtypes.CodeableConceptType = Field(
        None,
        alias="organism",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Todo",
    )

    organismType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="organismType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Todo",
    )

    source: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="source",
        title=(
            "List of `Reference` items referencing `DocumentReference` (represented"
            " as `dict` in JSON)"
        ),
        description="Todo",
    )

    target: fhirtypes.IdentifierType = Field(
        None,
        alias="target",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Todo",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Todo",
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
