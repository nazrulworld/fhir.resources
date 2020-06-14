# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationKnowledge
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class MedicationKnowledge(domainresource.DomainResource):
    """ Definition of Medication Knowledge.
    Information about a medication that is used to support knowledge.
    """

    resource_type = Field("MedicationKnowledge", const=True)

    administrationGuidelines: ListType[
        fhirtypes.MedicationKnowledgeAdministrationGuidelinesType
    ] = Field(
        None,
        alias="administrationGuidelines",
        title="List of `MedicationKnowledgeAdministrationGuidelines` items (represented as `dict` in JSON)",
        description="Guidelines for administration of the medication",
    )

    amount: fhirtypes.QuantityType = Field(
        None,
        alias="amount",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Amount of drug in package",
    )

    associatedMedication: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="associatedMedication",
        title="List of `Reference` items referencing `Medication` (represented as `dict` in JSON)",
        description="A medication resource that is associated with this medication",
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Code that identifies this medication",
    )

    contraindication: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="contraindication",
        title="List of `Reference` items referencing `DetectedIssue` (represented as `dict` in JSON)",
        description="Potential clinical issue with or between medication(s)",
    )

    cost: ListType[fhirtypes.MedicationKnowledgeCostType] = Field(
        None,
        alias="cost",
        title="List of `MedicationKnowledgeCost` items (represented as `dict` in JSON)",
        description="The pricing of the medication",
    )

    doseForm: fhirtypes.CodeableConceptType = Field(
        None,
        alias="doseForm",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="powder | tablets | capsule +",
    )

    drugCharacteristic: ListType[
        fhirtypes.MedicationKnowledgeDrugCharacteristicType
    ] = Field(
        None,
        alias="drugCharacteristic",
        title="List of `MedicationKnowledgeDrugCharacteristic` items (represented as `dict` in JSON)",
        description="Specifies descriptive properties of the medicine",
    )

    ingredient: ListType[fhirtypes.MedicationKnowledgeIngredientType] = Field(
        None,
        alias="ingredient",
        title="List of `MedicationKnowledgeIngredient` items (represented as `dict` in JSON)",
        description="Active or inactive ingredient",
    )

    intendedRoute: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="intendedRoute",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="The intended or approved route of administration",
    )

    kinetics: ListType[fhirtypes.MedicationKnowledgeKineticsType] = Field(
        None,
        alias="kinetics",
        title="List of `MedicationKnowledgeKinetics` items (represented as `dict` in JSON)",
        description="The time course of drug absorption, distribution, metabolism and excretion of a medication from the body",
    )

    manufacturer: fhirtypes.ReferenceType = Field(
        None,
        alias="manufacturer",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Manufacturer of the item",
    )

    medicineClassification: ListType[
        fhirtypes.MedicationKnowledgeMedicineClassificationType
    ] = Field(
        None,
        alias="medicineClassification",
        title="List of `MedicationKnowledgeMedicineClassification` items (represented as `dict` in JSON)",
        description="Categorization of the medication within a formulary or classification system",
    )

    monitoringProgram: ListType[
        fhirtypes.MedicationKnowledgeMonitoringProgramType
    ] = Field(
        None,
        alias="monitoringProgram",
        title="List of `MedicationKnowledgeMonitoringProgram` items (represented as `dict` in JSON)",
        description="Program under which a medication is reviewed",
    )

    monograph: ListType[fhirtypes.MedicationKnowledgeMonographType] = Field(
        None,
        alias="monograph",
        title="List of `MedicationKnowledgeMonograph` items (represented as `dict` in JSON)",
        description="Associated documentation about the medication",
    )

    packaging: fhirtypes.MedicationKnowledgePackagingType = Field(
        None,
        alias="packaging",
        title="Type `MedicationKnowledgePackaging` (represented as `dict` in JSON)",
        description="Details about packaged medications",
    )

    preparationInstruction: fhirtypes.Markdown = Field(
        None,
        alias="preparationInstruction",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="The instructions for preparing the medication",
    )

    productType: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="productType",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Category of the medication or product",
    )

    regulatory: ListType[fhirtypes.MedicationKnowledgeRegulatoryType] = Field(
        None,
        alias="regulatory",
        title="List of `MedicationKnowledgeRegulatory` items (represented as `dict` in JSON)",
        description="Regulatory information about a medication",
    )

    relatedMedicationKnowledge: ListType[
        fhirtypes.MedicationKnowledgeRelatedMedicationKnowledgeType
    ] = Field(
        None,
        alias="relatedMedicationKnowledge",
        title="List of `MedicationKnowledgeRelatedMedicationKnowledge` items (represented as `dict` in JSON)",
        description="Associated or related medication information",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="active | inactive | entered-in-error",
    )

    synonym: ListType[fhirtypes.String] = Field(
        None,
        alias="synonym",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Additional names for a medication",
    )


class MedicationKnowledgeAdministrationGuidelines(backboneelement.BackboneElement):
    """ Guidelines for administration of the medication.
    Guidelines for the administration of the medication.
    """

    resource_type = Field("MedicationKnowledgeAdministrationGuidelines", const=True)

    dosage: ListType[
        fhirtypes.MedicationKnowledgeAdministrationGuidelinesDosageType
    ] = Field(
        None,
        alias="dosage",
        title="List of `MedicationKnowledgeAdministrationGuidelinesDosage` items (represented as `dict` in JSON)",
        description="Dosage for the medication for the specific guidelines",
    )

    indicationCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="indicationCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Indication for use that apply to the specific administration guidelines",
        one_of_many="indication",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    indicationReference: fhirtypes.ReferenceType = Field(
        None,
        alias="indicationReference",
        title="Type `Reference` referencing `ObservationDefinition` (represented as `dict` in JSON)",
        description="Indication for use that apply to the specific administration guidelines",
        one_of_many="indication",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    patientCharacteristics: ListType[
        fhirtypes.MedicationKnowledgeAdministrationGuidelinesPatientCharacteristicsType
    ] = Field(
        None,
        alias="patientCharacteristics",
        title="List of `MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics` items (represented as `dict` in JSON)",
        description="Characteristics of the patient that are relevant to the administration guidelines",
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
            "indication": ["indicationCodeableConcept", "indicationReference",],
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


class MedicationKnowledgeAdministrationGuidelinesDosage(
    backboneelement.BackboneElement
):
    """ Dosage for the medication for the specific guidelines.
    """

    resource_type = Field(
        "MedicationKnowledgeAdministrationGuidelinesDosage", const=True
    )

    dosage: ListType[fhirtypes.DosageType] = Field(
        ...,
        alias="dosage",
        title="List of `Dosage` items (represented as `dict` in JSON)",
        description="Dosage for the medication for the specific guidelines",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of dosage",
    )


class MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics(
    backboneelement.BackboneElement
):
    """ Characteristics of the patient that are relevant to the administration
    guidelines.
    Characteristics of the patient that are relevant to the administration
    guidelines (for example, height, weight, gender, etc.).
    """

    resource_type = Field(
        "MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics", const=True
    )

    characteristicCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="characteristicCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Specific characteristic that is relevant to the administration guideline",
        one_of_many="characteristic",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    characteristicQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="characteristicQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Specific characteristic that is relevant to the administration guideline",
        one_of_many="characteristic",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    value: ListType[fhirtypes.String] = Field(
        None,
        alias="value",
        title="List of `String` items (represented as `dict` in JSON)",
        description="The specific characteristic",
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
            "characteristic": [
                "characteristicCodeableConcept",
                "characteristicQuantity",
            ],
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


class MedicationKnowledgeCost(backboneelement.BackboneElement):
    """ The pricing of the medication.
    The price of the medication.
    """

    resource_type = Field("MedicationKnowledgeCost", const=True)

    cost: fhirtypes.MoneyType = Field(
        ...,
        alias="cost",
        title="Type `Money` (represented as `dict` in JSON)",
        description="The price of the medication",
    )

    source: fhirtypes.String = Field(
        None,
        alias="source",
        title="Type `String` (represented as `dict` in JSON)",
        description="The source or owner for the price information",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The category of the cost information",
    )


class MedicationKnowledgeDrugCharacteristic(backboneelement.BackboneElement):
    """ Specifies descriptive properties of the medicine.
    Specifies descriptive properties of the medicine, such as color, shape,
    imprints, etc.
    """

    resource_type = Field("MedicationKnowledgeDrugCharacteristic", const=True)

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Code specifying the type of characteristic of medication",
    )

    valueBase64Binary: fhirtypes.Base64Binary = Field(
        None,
        alias="valueBase64Binary",
        title="Type `Base64Binary` (represented as `dict` in JSON)",
        description="Description of the characteristic",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="valueCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Description of the characteristic",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Description of the characteristic",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Type `String` (represented as `dict` in JSON)",
        description="Description of the characteristic",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
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
            "value": [
                "valueBase64Binary",
                "valueCodeableConcept",
                "valueQuantity",
                "valueString",
            ],
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


class MedicationKnowledgeIngredient(backboneelement.BackboneElement):
    """ Active or inactive ingredient.
    Identifies a particular constituent of interest in the product.
    """

    resource_type = Field("MedicationKnowledgeIngredient", const=True)

    isActive: bool = Field(
        None,
        alias="isActive",
        title="Type `bool`",
        description="Active ingredient indicator",
    )

    itemCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="itemCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Medication(s) or substance(s) contained in the medication",
        one_of_many="item",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    itemReference: fhirtypes.ReferenceType = Field(
        None,
        alias="itemReference",
        title="Type `Reference` referencing `Substance` (represented as `dict` in JSON)",
        description="Medication(s) or substance(s) contained in the medication",
        one_of_many="item",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    strength: fhirtypes.RatioType = Field(
        None,
        alias="strength",
        title="Type `Ratio` (represented as `dict` in JSON)",
        description="Quantity of ingredient present",
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
            "item": ["itemCodeableConcept", "itemReference",],
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


class MedicationKnowledgeKinetics(backboneelement.BackboneElement):
    """ The time course of drug absorption, distribution, metabolism and excretion
    of a medication from the body.
    """

    resource_type = Field("MedicationKnowledgeKinetics", const=True)

    areaUnderCurve: ListType[fhirtypes.QuantityType] = Field(
        None,
        alias="areaUnderCurve",
        title="List of `Quantity` items (represented as `dict` in JSON)",
        description="The drug concentration measured at certain discrete points in time",
    )

    halfLifePeriod: fhirtypes.DurationType = Field(
        None,
        alias="halfLifePeriod",
        title="Type `Duration` (represented as `dict` in JSON)",
        description="Time required for concentration in the body to decrease by half",
    )

    lethalDose50: ListType[fhirtypes.QuantityType] = Field(
        None,
        alias="lethalDose50",
        title="List of `Quantity` items (represented as `dict` in JSON)",
        description="The median lethal dose of a drug",
    )


class MedicationKnowledgeMedicineClassification(backboneelement.BackboneElement):
    """ Categorization of the medication within a formulary or classification
    system.
    """

    resource_type = Field("MedicationKnowledgeMedicineClassification", const=True)

    classification: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="classification",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Specific category assigned to the medication",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The type of category for the medication (for example, therapeutic classification, therapeutic sub-classification)",
    )


class MedicationKnowledgeMonitoringProgram(backboneelement.BackboneElement):
    """ Program under which a medication is reviewed.
    The program under which the medication is reviewed.
    """

    resource_type = Field("MedicationKnowledgeMonitoringProgram", const=True)

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of the reviewing program",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of program under which the medication is monitored",
    )


class MedicationKnowledgeMonograph(backboneelement.BackboneElement):
    """ Associated documentation about the medication.
    """

    resource_type = Field("MedicationKnowledgeMonograph", const=True)

    source: fhirtypes.ReferenceType = Field(
        None,
        alias="source",
        title="Type `Reference` referencing `DocumentReference, Media` (represented as `dict` in JSON)",
        description="Associated documentation about the medication",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The category of medication document",
    )


class MedicationKnowledgePackaging(backboneelement.BackboneElement):
    """ Details about packaged medications.
    Information that only applies to packages (not products).
    """

    resource_type = Field("MedicationKnowledgePackaging", const=True)

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="The number of product units the package would contain if fully loaded",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="A code that defines the specific type of packaging that the medication can be found in",
    )


class MedicationKnowledgeRegulatory(backboneelement.BackboneElement):
    """ Regulatory information about a medication.
    """

    resource_type = Field("MedicationKnowledgeRegulatory", const=True)

    maxDispense: fhirtypes.MedicationKnowledgeRegulatoryMaxDispenseType = Field(
        None,
        alias="maxDispense",
        title="Type `MedicationKnowledgeRegulatoryMaxDispense` (represented as `dict` in JSON)",
        description="The maximum number of units of the medication that can be dispensed in a period",
    )

    regulatoryAuthority: fhirtypes.ReferenceType = Field(
        ...,
        alias="regulatoryAuthority",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Specifies the authority of the regulation",
    )

    schedule: ListType[fhirtypes.MedicationKnowledgeRegulatoryScheduleType] = Field(
        None,
        alias="schedule",
        title="List of `MedicationKnowledgeRegulatorySchedule` items (represented as `dict` in JSON)",
        description="Specifies the schedule of a medication in jurisdiction",
    )

    substitution: ListType[
        fhirtypes.MedicationKnowledgeRegulatorySubstitutionType
    ] = Field(
        None,
        alias="substitution",
        title="List of `MedicationKnowledgeRegulatorySubstitution` items (represented as `dict` in JSON)",
        description="Specifies if changes are allowed when dispensing a medication from a regulatory perspective",
    )


class MedicationKnowledgeRegulatoryMaxDispense(backboneelement.BackboneElement):
    """ The maximum number of units of the medication that can be dispensed in a
    period.
    """

    resource_type = Field("MedicationKnowledgeRegulatoryMaxDispense", const=True)

    period: fhirtypes.DurationType = Field(
        None,
        alias="period",
        title="Type `Duration` (represented as `dict` in JSON)",
        description="The period that applies to the maximum number of units",
    )

    quantity: fhirtypes.QuantityType = Field(
        ...,
        alias="quantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="The maximum number of units of the medication that can be dispensed",
    )


class MedicationKnowledgeRegulatorySchedule(backboneelement.BackboneElement):
    """ Specifies the schedule of a medication in jurisdiction.
    """

    resource_type = Field("MedicationKnowledgeRegulatorySchedule", const=True)

    schedule: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="schedule",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Specifies the specific drug schedule",
    )


class MedicationKnowledgeRegulatorySubstitution(backboneelement.BackboneElement):
    """ Specifies if changes are allowed when dispensing a medication from a
    regulatory perspective.
    """

    resource_type = Field("MedicationKnowledgeRegulatorySubstitution", const=True)

    allowed: bool = Field(
        ...,
        alias="allowed",
        title="Type `bool`",
        description="Specifies if regulation allows for changes in the medication when dispensing",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Specifies the type of substitution allowed",
    )


class MedicationKnowledgeRelatedMedicationKnowledge(backboneelement.BackboneElement):
    """ Associated or related medication information.
    Associated or related knowledge about a medication.
    """

    resource_type = Field("MedicationKnowledgeRelatedMedicationKnowledge", const=True)

    reference: ListType[fhirtypes.ReferenceType] = Field(
        ...,
        alias="reference",
        title="List of `Reference` items referencing `MedicationKnowledge` (represented as `dict` in JSON)",
        description="Associated documentation about the associated medication knowledge",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Category of medicationKnowledge",
    )
