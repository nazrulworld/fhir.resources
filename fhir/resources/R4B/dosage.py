# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Dosage
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic.v1 import Field, root_validator

from . import backboneelement, element, fhirtypes


class Dosage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    How the medication is/was taken or should be taken.
    Indicates how the medication is/was taken or should be taken by the
    patient.
    """

    resource_type = Field("Dosage", const=True)

    additionalInstruction: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="additionalInstruction",
        title=(
            'Supplemental instruction or warnings to the patient - e.g. "with '
            'meals", "may cause drowsiness"'
        ),
        description=(
            "Supplemental instructions to the patient on how to take the medication"
            '  (e.g. "with meals" or"take half to one hour before food") or '
            'warnings for the patient about the medication (e.g. "may cause '
            'drowsiness" or "avoid exposure of skin to direct sunlight or '
            'sunlamps").'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    asNeededBoolean: bool = Field(
        None,
        alias="asNeededBoolean",
        title='Take "as needed" (for x)',
        description=(
            "Indicates whether the Medication is only taken when needed within a "
            "specific dosing schedule (Boolean option), or it indicates the "
            "precondition for taking the Medication (CodeableConcept)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e asNeeded[x]
        one_of_many="asNeeded",
        one_of_many_required=False,
    )
    asNeededBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_asNeededBoolean", title="Extension field for ``asNeededBoolean``."
    )

    asNeededCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="asNeededCodeableConcept",
        title='Take "as needed" (for x)',
        description=(
            "Indicates whether the Medication is only taken when needed within a "
            "specific dosing schedule (Boolean option), or it indicates the "
            "precondition for taking the Medication (CodeableConcept)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e asNeeded[x]
        one_of_many="asNeeded",
        one_of_many_required=False,
    )

    doseAndRate: typing.List[fhirtypes.DosageDoseAndRateType] = Field(
        None,
        alias="doseAndRate",
        title="Amount of medication administered",
        description="The amount of medication administered.",
        # if property is element of this resource.
        element_property=True,
    )

    maxDosePerAdministration: fhirtypes.QuantityType = Field(
        None,
        alias="maxDosePerAdministration",
        title="Upper limit on medication per administration",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    maxDosePerLifetime: fhirtypes.QuantityType = Field(
        None,
        alias="maxDosePerLifetime",
        title="Upper limit on medication per lifetime of the patient",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    maxDosePerPeriod: fhirtypes.RatioType = Field(
        None,
        alias="maxDosePerPeriod",
        title="Upper limit on medication per unit of time",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    method: fhirtypes.CodeableConceptType = Field(
        None,
        alias="method",
        title="Technique for administering medication",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    patientInstruction: fhirtypes.String = Field(
        None,
        alias="patientInstruction",
        title="Patient or consumer oriented instructions",
        description="Instructions in terms that are understood by the patient or consumer.",
        # if property is element of this resource.
        element_property=True,
    )
    patientInstruction__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_patientInstruction",
        title="Extension field for ``patientInstruction``.",
    )

    route: fhirtypes.CodeableConceptType = Field(
        None,
        alias="route",
        title="How drug should enter body",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    sequence: fhirtypes.Integer = Field(
        None,
        alias="sequence",
        title="The order of the dosage instructions",
        description=(
            "Indicates the order in which the dosage instructions should be applied"
            " or interpreted."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    site: fhirtypes.CodeableConceptType = Field(
        None,
        alias="site",
        title="Body site to administer to",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Free text dosage instructions e.g. SIG",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )

    timing: fhirtypes.TimingType = Field(
        None,
        alias="timing",
        title="When medication should be administered",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Dosage`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "text",
            "additionalInstruction",
            "patientInstruction",
            "timing",
            "asNeededBoolean",
            "asNeededCodeableConcept",
            "site",
            "route",
            "method",
            "doseAndRate",
            "maxDosePerPeriod",
            "maxDosePerAdministration",
            "maxDosePerLifetime",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_764(
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
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Amount of medication administered.
    The amount of medication administered.
    """

    resource_type = Field("DosageDoseAndRate", const=True)

    doseQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="doseQuantity",
        title="Amount of medication per dose",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e dose[x]
        one_of_many="dose",
        one_of_many_required=False,
    )

    doseRange: fhirtypes.RangeType = Field(
        None,
        alias="doseRange",
        title="Amount of medication per dose",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e dose[x]
        one_of_many="dose",
        one_of_many_required=False,
    )

    rateQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="rateQuantity",
        title="Amount of medication per unit of time",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e rate[x]
        one_of_many="rate",
        one_of_many_required=False,
    )

    rateRange: fhirtypes.RangeType = Field(
        None,
        alias="rateRange",
        title="Amount of medication per unit of time",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e rate[x]
        one_of_many="rate",
        one_of_many_required=False,
    )

    rateRatio: fhirtypes.RatioType = Field(
        None,
        alias="rateRatio",
        title="Amount of medication per unit of time",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e rate[x]
        one_of_many="rate",
        one_of_many_required=False,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="The kind of dose or rate specified",
        description=(
            "The kind of dose or rate specified, for example, ordered or " "calculated."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DosageDoseAndRate`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "type",
            "doseRange",
            "doseQuantity",
            "rateRatio",
            "rateRange",
            "rateQuantity",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1830(
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
