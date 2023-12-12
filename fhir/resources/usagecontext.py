# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/UsageContext
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field, root_validator

from . import datatype, fhirtypes


class UsageContext(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Describes the context of use for a conformance or knowledge resource.
    Specifies clinical/business/etc. metadata that can be used to retrieve,
    index and/or categorize an artifact. This metadata can either be specific
    to the applicable population (e.g., age category, DRG) or the specific
    context of care (e.g., venue, care setting, provider of care).
    """

    resource_type = Field("UsageContext", const=True)

    code: fhirtypes.CodingType = Field(
        ...,
        alias="code",
        title="Type of context being specified",
        description=(
            "A code that identifies the type of context being specified by this "
            "usage context."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="valueCodeableConcept",
        title="Value that defines the context",
        description=(
            "A value that defines the context specified in this context of use. The"
            " interpretation of the value is defined by the code."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="Value that defines the context",
        description=(
            "A value that defines the context specified in this context of use. The"
            " interpretation of the value is defined by the code."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueRange: fhirtypes.RangeType = Field(
        None,
        alias="valueRange",
        title="Value that defines the context",
        description=(
            "A value that defines the context specified in this context of use. The"
            " interpretation of the value is defined by the code."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueReference",
        title="Value that defines the context",
        description=(
            "A value that defines the context specified in this context of use. The"
            " interpretation of the value is defined by the code."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "PlanDefinition",
            "ResearchStudy",
            "InsurancePlan",
            "HealthcareService",
            "Group",
            "Location",
            "Organization",
        ],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``UsageContext`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "code",
            "valueCodeableConcept",
            "valueQuantity",
            "valueRange",
            "valueReference",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1443(
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
            "value": [
                "valueCodeableConcept",
                "valueQuantity",
                "valueRange",
                "valueReference",
            ]
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
