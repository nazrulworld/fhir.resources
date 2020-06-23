# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Dosage
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, element, fhirtypes


class Dosage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    How the medication is/was taken or should be taken.
    Indicates how the medication is/was taken or should be taken by the
    patient.
    """

    resource_type = Field("Dosage", const=True)

    additionalInstruction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="additionalInstruction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description=(
            'Supplemental instruction or warnings to the patient - e.g. "with '
            'meals", "may cause drowsiness"'
        ),
    )

    asNeededBoolean: bool = Field(
        None,
        alias="asNeededBoolean",
        title="Type `bool`",
        description='Take "as needed" (for x)',
        one_of_many="asNeeded",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    asNeededBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_asNeededBoolean", title="Extension field for ``asNeededBoolean``."
    )

    asNeededCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="asNeededCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description='Take "as needed" (for x)',
        one_of_many="asNeeded",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    doseAndRate: ListType[fhirtypes.DosageDoseAndRateType] = Field(
        None,
        alias="doseAndRate",
        title="List of `DosageDoseAndRate` items (represented as `dict` in JSON)",
        description="Amount of medication administered",
    )

    maxDosePerAdministration: fhirtypes.QuantityType = Field(
        None,
        alias="maxDosePerAdministration",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Upper limit on medication per administration",
    )

    maxDosePerLifetime: fhirtypes.QuantityType = Field(
        None,
        alias="maxDosePerLifetime",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Upper limit on medication per lifetime of the patient",
    )

    maxDosePerPeriod: fhirtypes.RatioType = Field(
        None,
        alias="maxDosePerPeriod",
        title="Type `Ratio` (represented as `dict` in JSON)",
        description="Upper limit on medication per unit of time",
    )

    method: fhirtypes.CodeableConceptType = Field(
        None,
        alias="method",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Technique for administering medication",
    )

    patientInstruction: fhirtypes.String = Field(
        None,
        alias="patientInstruction",
        title="Type `String`",
        description="Patient or consumer oriented instructions",
    )
    patientInstruction__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_patientInstruction",
        title="Extension field for ``patientInstruction``.",
    )

    route: fhirtypes.CodeableConceptType = Field(
        None,
        alias="route",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="How drug should enter body",
    )

    sequence: fhirtypes.Integer = Field(
        None,
        alias="sequence",
        title="Type `Integer`",
        description="The order of the dosage instructions",
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    site: fhirtypes.CodeableConceptType = Field(
        None,
        alias="site",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Body site to administer to",
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Type `String`",
        description="Free text dosage instructions e.g. SIG",
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )

    timing: fhirtypes.TimingType = Field(
        None,
        alias="timing",
        title="Type `Timing` (represented as `dict` in JSON)",
        description="When medication should be administered",
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
            "asNeeded": ["asNeededBoolean", "asNeededCodeableConcept"]
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


class DosageDoseAndRate(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Amount of medication administered.
    The amount of medication administered.
    """

    resource_type = Field("DosageDoseAndRate", const=True)

    doseQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="doseQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Amount of medication per dose",
        one_of_many="dose",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    doseRange: fhirtypes.RangeType = Field(
        None,
        alias="doseRange",
        title="Type `Range` (represented as `dict` in JSON)",
        description="Amount of medication per dose",
        one_of_many="dose",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    rateQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="rateQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Amount of medication per unit of time",
        one_of_many="rate",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    rateRange: fhirtypes.RangeType = Field(
        None,
        alias="rateRange",
        title="Type `Range` (represented as `dict` in JSON)",
        description="Amount of medication per unit of time",
        one_of_many="rate",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    rateRatio: fhirtypes.RatioType = Field(
        None,
        alias="rateRatio",
        title="Type `Ratio` (represented as `dict` in JSON)",
        description="Amount of medication per unit of time",
        one_of_many="rate",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The kind of dose or rate specified",
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
            "dose": ["doseQuantity", "doseRange"],
            "rate": ["rateQuantity", "rateRange", "rateRatio"],
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
