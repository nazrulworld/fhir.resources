# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubstanceAmount
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
import typing

from pydantic import Field, root_validator

from . import backboneelement, element, fhirtypes


class SubstanceAmount(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Chemical substances are a single substance type whose primary defining
    element is the molecular structure. Chemical substances shall be defined on
    the basis of their complete covalent molecular structure; the presence of a
    salt (counter-ion) and/or solvates (water, alcohols) is also captured.
    Purity, grade, physical form or particle size are not taken into account in
    the definition of a chemical substance or in the assignment of a Substance
    ID.
    """

    resource_type = Field("SubstanceAmount", const=True)

    amountQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="amountQuantity",
        title=(
            "Used to capture quantitative values for a variety of elements. If only"
            " limits are given, the arithmetic mean would be the average. If only a"
            " single definite value for a given element is given, it would be "
            "captured in this field"
        ),
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
        title=(
            "Used to capture quantitative values for a variety of elements. If only"
            " limits are given, the arithmetic mean would be the average. If only a"
            " single definite value for a given element is given, it would be "
            "captured in this field"
        ),
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
        title=(
            "Used to capture quantitative values for a variety of elements. If only"
            " limits are given, the arithmetic mean would be the average. If only a"
            " single definite value for a given element is given, it would be "
            "captured in this field"
        ),
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

    amountText: fhirtypes.String = Field(
        None,
        alias="amountText",
        title="A textual comment on a numeric value",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    amountText__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_amountText", title="Extension field for ``amountText``."
    )

    amountType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="amountType",
        title=(
            "Most elements that require a quantitative value will also have a field"
            " called amount type. Amount type should always be specified because "
            "the actual value of the amount is often dependent on it. EXAMPLE: In "
            "capturing the actual relative amounts of substances or molecular "
            "fragments it is essential to indicate whether the amount refers to a "
            "mole ratio or weight ratio. For any given element an effort should be "
            "made to use same the amount type for all related definitional elements"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    referenceRange: fhirtypes.SubstanceAmountReferenceRangeType = Field(
        None,
        alias="referenceRange",
        title="Reference range of possible or expected values",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @root_validator(pre=True)
    def validate_one_of_many(
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


class SubstanceAmountReferenceRange(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Reference range of possible or expected values.
    """

    resource_type = Field("SubstanceAmountReferenceRange", const=True)

    highLimit: fhirtypes.QuantityType = Field(
        None,
        alias="highLimit",
        title="Upper limit possible or expected",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    lowLimit: fhirtypes.QuantityType = Field(
        None,
        alias="lowLimit",
        title="Lower limit possible or expected",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
