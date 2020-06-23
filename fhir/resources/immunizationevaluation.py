# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ImmunizationEvaluation
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import domainresource, fhirtypes


class ImmunizationEvaluation(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Immunization evaluation information.
    Describes a comparison of an immunization event against published
    recommendations to determine if the administration is "valid" in relation
    to those  recommendations.
    """

    resource_type = Field("ImmunizationEvaluation", const=True)

    authority: fhirtypes.ReferenceType = Field(
        None,
        alias="authority",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Who is responsible for publishing the recommendations",
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime`",
        description="Date evaluation was performed",
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.String = Field(
        None, alias="description", title="Type `String`", description="Evaluation notes"
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    doseNumberPositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="doseNumberPositiveInt",
        title="Type `PositiveInt`",
        description="Dose number within series",
        one_of_many="doseNumber",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    doseNumberPositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_doseNumberPositiveInt",
        title="Extension field for ``doseNumberPositiveInt``.",
    )

    doseNumberString: fhirtypes.String = Field(
        None,
        alias="doseNumberString",
        title="Type `String`",
        description="Dose number within series",
        one_of_many="doseNumber",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    doseNumberString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_doseNumberString",
        title="Extension field for ``doseNumberString``.",
    )

    doseStatus: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="doseStatus",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Status of the dose relative to published recommendations",
    )

    doseStatusReason: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="doseStatusReason",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Reason for the dose status",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business identifier",
    )

    immunizationEvent: fhirtypes.ReferenceType = Field(
        ...,
        alias="immunizationEvent",
        title=(
            "Type `Reference` referencing `Immunization` (represented as `dict` in "
            "JSON)"
        ),
        description="Immunization being evaluated",
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="Who this evaluation is for",
    )

    series: fhirtypes.String = Field(
        None,
        alias="series",
        title="Type `String`",
        description="Name of vaccine series",
    )
    series__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_series", title="Extension field for ``series``."
    )

    seriesDosesPositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="seriesDosesPositiveInt",
        title="Type `PositiveInt`",
        description="Recommended number of doses for immunity",
        one_of_many="seriesDoses",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    seriesDosesPositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_seriesDosesPositiveInt",
        title="Extension field for ``seriesDosesPositiveInt``.",
    )

    seriesDosesString: fhirtypes.String = Field(
        None,
        alias="seriesDosesString",
        title="Type `String`",
        description="Recommended number of doses for immunity",
        one_of_many="seriesDoses",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    seriesDosesString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_seriesDosesString",
        title="Extension field for ``seriesDosesString``.",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`",
        description="completed | entered-in-error",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    targetDisease: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="targetDisease",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Evaluation target disease",
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
            "doseNumber": ["doseNumberPositiveInt", "doseNumberString"],
            "seriesDoses": ["seriesDosesPositiveInt", "seriesDosesString"],
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
