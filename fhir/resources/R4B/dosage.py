from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Dosage
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, element, fhirtypes


class Dosage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    How the medication is/was taken or should be taken.
    Indicates how the medication is/was taken or should be taken by the
    patient.
    """

    __resource_type__ = "Dosage"

    additionalInstruction: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )

    asNeededBoolean: bool | None = Field(  # type: ignore
        None,
        alias="asNeededBoolean",
        title='Take "as needed" (for x)',
        description=(
            "Indicates whether the Medication is only taken when needed within a "
            "specific dosing schedule (Boolean option), or it indicates the "
            "precondition for taking the Medication (CodeableConcept)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e asNeeded[x]
            "one_of_many": "asNeeded",
            "one_of_many_required": False,
        },
    )
    asNeededBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_asNeededBoolean", title="Extension field for ``asNeededBoolean``."
    )

    asNeededCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="asNeededCodeableConcept",
        title='Take "as needed" (for x)',
        description=(
            "Indicates whether the Medication is only taken when needed within a "
            "specific dosing schedule (Boolean option), or it indicates the "
            "precondition for taking the Medication (CodeableConcept)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e asNeeded[x]
            "one_of_many": "asNeeded",
            "one_of_many_required": False,
        },
    )

    doseAndRate: typing.List[fhirtypes.DosageDoseAndRateType] | None = Field(  # type: ignore
        None,
        alias="doseAndRate",
        title="Amount of medication administered",
        description="The amount of medication administered.",
        json_schema_extra={
            "element_property": True,
        },
    )

    maxDosePerAdministration: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="maxDosePerAdministration",
        title="Upper limit on medication per administration",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    maxDosePerLifetime: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="maxDosePerLifetime",
        title="Upper limit on medication per lifetime of the patient",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    maxDosePerPeriod: fhirtypes.RatioType | None = Field(  # type: ignore
        None,
        alias="maxDosePerPeriod",
        title="Upper limit on medication per unit of time",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    method: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="method",
        title="Technique for administering medication",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    patientInstruction: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="patientInstruction",
        title="Patient or consumer oriented instructions",
        description="Instructions in terms that are understood by the patient or consumer.",
        json_schema_extra={
            "element_property": True,
        },
    )
    patientInstruction__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_patientInstruction",
        title="Extension field for ``patientInstruction``.",
    )

    route: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="route",
        title="How drug should enter body",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    sequence: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="sequence",
        title="The order of the dosage instructions",
        description=(
            "Indicates the order in which the dosage instructions should be applied"
            " or interpreted."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    site: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="site",
        title="Body site to administer to",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    text: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="text",
        title="Free text dosage instructions e.g. SIG",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_text", title="Extension field for ``text``."
    )

    timing: fhirtypes.TimingType | None = Field(  # type: ignore
        None,
        alias="timing",
        title="When medication should be administered",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
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
            "asNeeded": ["asNeededBoolean", "asNeededCodeableConcept"]
        }
        return one_of_many_fields


class DosageDoseAndRate(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Amount of medication administered.
    The amount of medication administered.
    """

    __resource_type__ = "DosageDoseAndRate"

    doseQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="doseQuantity",
        title="Amount of medication per dose",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e dose[x]
            "one_of_many": "dose",
            "one_of_many_required": False,
        },
    )

    doseRange: fhirtypes.RangeType | None = Field(  # type: ignore
        None,
        alias="doseRange",
        title="Amount of medication per dose",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e dose[x]
            "one_of_many": "dose",
            "one_of_many_required": False,
        },
    )

    rateQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="rateQuantity",
        title="Amount of medication per unit of time",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e rate[x]
            "one_of_many": "rate",
            "one_of_many_required": False,
        },
    )

    rateRange: fhirtypes.RangeType | None = Field(  # type: ignore
        None,
        alias="rateRange",
        title="Amount of medication per unit of time",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e rate[x]
            "one_of_many": "rate",
            "one_of_many_required": False,
        },
    )

    rateRatio: fhirtypes.RatioType | None = Field(  # type: ignore
        None,
        alias="rateRatio",
        title="Amount of medication per unit of time",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e rate[x]
            "one_of_many": "rate",
            "one_of_many_required": False,
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="The kind of dose or rate specified",
        description=(
            "The kind of dose or rate specified, for example, ordered or " "calculated."
        ),
        json_schema_extra={
            "element_property": True,
        },
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
            "dose": ["doseQuantity", "doseRange"],
            "rate": ["rateQuantity", "rateRange", "rateRatio"],
        }
        return one_of_many_fields
