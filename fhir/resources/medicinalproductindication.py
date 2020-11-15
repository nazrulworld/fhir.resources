# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductIndication
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
import typing

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class MedicinalProductIndication(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    MedicinalProductIndication.
    Indication for the Medicinal Product.
    """

    resource_type = Field("MedicinalProductIndication", const=True)

    comorbidity: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="comorbidity",
        title=(
            "Comorbidity (concurrent condition) or co-infection as part of the "
            "indication"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    diseaseStatus: fhirtypes.CodeableConceptType = Field(
        None,
        alias="diseaseStatus",
        title="The status of the disease or symptom for which the indication applies",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    diseaseSymptomProcedure: fhirtypes.CodeableConceptType = Field(
        None,
        alias="diseaseSymptomProcedure",
        title="The disease, symptom or procedure that is the indication for treatment",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    duration: fhirtypes.QuantityType = Field(
        None,
        alias="duration",
        title="Timing or duration information as part of the indication",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    intendedEffect: fhirtypes.CodeableConceptType = Field(
        None,
        alias="intendedEffect",
        title="The intended effect, aim or strategy to be achieved by the indication",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    otherTherapy: typing.List[
        fhirtypes.MedicinalProductIndicationOtherTherapyType
    ] = Field(
        None,
        alias="otherTherapy",
        title=(
            "Information about the use of the medicinal product in relation to "
            "other therapies described as part of the indication"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    population: typing.List[fhirtypes.PopulationType] = Field(
        None,
        alias="population",
        title="The population group to which this applies",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    subject: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="subject",
        title="The medication for which this is an indication",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicinalProduct", "Medication"],
    )

    undesirableEffect: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="undesirableEffect",
        title="Describe the undesirable effects of the medicinal product",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicinalProductUndesirableEffect"],
    )


class MedicinalProductIndicationOtherTherapy(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about the use of the medicinal product in relation to other
    therapies described as part of the indication.
    """

    resource_type = Field("MedicinalProductIndicationOtherTherapy", const=True)

    medicationCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="medicationCodeableConcept",
        title=(
            "Reference to a specific medication (active substance, medicinal "
            "product or class of products) as part of an indication or "
            "contraindication"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e medication[x]
        one_of_many="medication",
        one_of_many_required=True,
    )

    medicationReference: fhirtypes.ReferenceType = Field(
        None,
        alias="medicationReference",
        title=(
            "Reference to a specific medication (active substance, medicinal "
            "product or class of products) as part of an indication or "
            "contraindication"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e medication[x]
        one_of_many="medication",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "MedicinalProduct",
            "Medication",
            "Substance",
            "SubstanceSpecification",
        ],
    )

    therapyRelationshipType: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="therapyRelationshipType",
        title=(
            "The type of relationship between the medicinal product indication or "
            "contraindication and another therapy"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_4110(
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
            "medication": ["medicationCodeableConcept", "medicationReference"]
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
