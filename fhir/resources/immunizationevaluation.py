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
        title="Who is responsible for publishing the recommendations",
        description="Indicates the authority who published the protocol (e.g. ACIP).",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date evaluation was performed",
        description=(
            "The date the evaluation of the vaccine administration event was "
            "performed."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Evaluation notes",
        description="Additional information about the evaluation.",
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    doseNumberPositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="doseNumberPositiveInt",
        title="Dose number within series",
        description="Nominal position in a series.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e doseNumber[x]
        one_of_many="doseNumber",
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
        title="Dose number within series",
        description="Nominal position in a series.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e doseNumber[x]
        one_of_many="doseNumber",
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
        title="Status of the dose relative to published recommendations",
        description=(
            "Indicates if the dose is valid or not valid with respect to the "
            "published recommendations."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    doseStatusReason: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="doseStatusReason",
        title="Reason for the dose status",
        description=(
            "Provides an explanation as to why the vaccine administration event is "
            "valid or not relative to the published recommendations."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier",
        description="A unique identifier assigned to this immunization evaluation record.",
        # if property is element of this resource.
        element_property=True,
    )

    immunizationEvent: fhirtypes.ReferenceType = Field(
        ...,
        alias="immunizationEvent",
        title="Immunization being evaluated",
        description="The vaccine administration event being evaluated.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Immunization"],
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Who this evaluation is for",
        description="The individual for whom the evaluation is being done.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    series: fhirtypes.String = Field(
        None,
        alias="series",
        title="Name of vaccine series",
        description=(
            "One possible path to achieve presumed immunity against a disease - "
            "within the context of an authority."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    series__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_series", title="Extension field for ``series``."
    )

    seriesDosesPositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="seriesDosesPositiveInt",
        title="Recommended number of doses for immunity",
        description="The recommended number of doses to achieve immunity.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e seriesDoses[x]
        one_of_many="seriesDoses",
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
        title="Recommended number of doses for immunity",
        description="The recommended number of doses to achieve immunity.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e seriesDoses[x]
        one_of_many="seriesDoses",
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
        title="completed | entered-in-error",
        description=(
            "Indicates the current status of the evaluation of the vaccination "
            "administration event."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["completed", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    targetDisease: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="targetDisease",
        title="Evaluation target disease",
        description="The vaccine preventable disease the dose is being evaluated against.",
        # if property is element of this resource.
        element_property=True,
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
