# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationKnowledge
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class MedicationKnowledge(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Definition of Medication Knowledge.
    Information about a medication that is used to support knowledge.
    """

    resource_type = Field("MedicationKnowledge", const=True)

    administrationGuidelines: typing.List[
        fhirtypes.MedicationKnowledgeAdministrationGuidelinesType
    ] = Field(
        None,
        alias="administrationGuidelines",
        title="Guidelines for administration of the medication",
        description="Guidelines for the administration of the medication.",
        # if property is element of this resource.
        element_property=True,
    )

    amount: fhirtypes.QuantityType = Field(
        None,
        alias="amount",
        title="Amount of drug in package",
        description=(
            "Specific amount of the drug in the packaged product.  For example, "
            "when specifying a product that has the same strength (For example, "
            "Insulin glargine 100 unit per mL solution for injection), this "
            "attribute provides additional clarification of the package amount (For"
            " example, 3 mL, 10mL, etc.)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    associatedMedication: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="associatedMedication",
        title="A medication resource that is associated with this medication",
        description=(
            "Associated or related medications.  For example, if the medication is "
            "a branded product (e.g. Crestor), this is the Therapeutic Moeity (e.g."
            " Rosuvastatin) or if this is a generic medication (e.g. Rosuvastatin),"
            " this would link to a branded product (e.g. Crestor)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Medication"],
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Code that identifies this medication",
        description=(
            "A code that specifies this medication, or a textual description if no "
            "code is available. Usage note: This could be a standard medication "
            "code such as a code from RxNorm, SNOMED CT, IDMP etc. It could also be"
            " a national or local formulary code, optionally with translations to "
            "other code systems."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    contraindication: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="contraindication",
        title="Potential clinical issue with or between medication(s)",
        description=(
            "Potential clinical issue with or between medication(s) (for example, "
            "drug-drug interaction, drug-disease contraindication, drug-allergy "
            "interaction, etc.)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DetectedIssue"],
    )

    cost: typing.List[fhirtypes.MedicationKnowledgeCostType] = Field(
        None,
        alias="cost",
        title="The pricing of the medication",
        description="The price of the medication.",
        # if property is element of this resource.
        element_property=True,
    )

    doseForm: fhirtypes.CodeableConceptType = Field(
        None,
        alias="doseForm",
        title="powder | tablets | capsule +",
        description="Describes the form of the item.  Powder; tablets; capsule.",
        # if property is element of this resource.
        element_property=True,
    )

    drugCharacteristic: typing.List[
        fhirtypes.MedicationKnowledgeDrugCharacteristicType
    ] = Field(
        None,
        alias="drugCharacteristic",
        title="Specifies descriptive properties of the medicine",
        description=(
            "Specifies descriptive properties of the medicine, such as color, "
            "shape, imprints, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    ingredient: typing.List[fhirtypes.MedicationKnowledgeIngredientType] = Field(
        None,
        alias="ingredient",
        title="Active or inactive ingredient",
        description="Identifies a particular constituent of interest in the product.",
        # if property is element of this resource.
        element_property=True,
    )

    intendedRoute: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="intendedRoute",
        title="The intended or approved route of administration",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    kinetics: typing.List[fhirtypes.MedicationKnowledgeKineticsType] = Field(
        None,
        alias="kinetics",
        title=(
            "The time course of drug absorption, distribution, metabolism and "
            "excretion of a medication from the body"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    manufacturer: fhirtypes.ReferenceType = Field(
        None,
        alias="manufacturer",
        title="Manufacturer of the item",
        description=(
            "Describes the details of the manufacturer of the medication product.  "
            "This is not intended to represent the distributor of a medication "
            "product."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    medicineClassification: typing.List[
        fhirtypes.MedicationKnowledgeMedicineClassificationType
    ] = Field(
        None,
        alias="medicineClassification",
        title=(
            "Categorization of the medication within a formulary or classification "
            "system"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    monitoringProgram: typing.List[
        fhirtypes.MedicationKnowledgeMonitoringProgramType
    ] = Field(
        None,
        alias="monitoringProgram",
        title="Program under which a medication is reviewed",
        description="The program under which the medication is reviewed.",
        # if property is element of this resource.
        element_property=True,
    )

    monograph: typing.List[fhirtypes.MedicationKnowledgeMonographType] = Field(
        None,
        alias="monograph",
        title="Associated documentation about the medication",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    packaging: fhirtypes.MedicationKnowledgePackagingType = Field(
        None,
        alias="packaging",
        title="Details about packaged medications",
        description="Information that only applies to packages (not products).",
        # if property is element of this resource.
        element_property=True,
    )

    preparationInstruction: fhirtypes.Markdown = Field(
        None,
        alias="preparationInstruction",
        title="The instructions for preparing the medication",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    preparationInstruction__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_preparationInstruction",
        title="Extension field for ``preparationInstruction``.",
    )

    productType: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="productType",
        title="Category of the medication or product",
        description=(
            "Category of the medication or product (e.g. branded product, "
            "therapeutic moeity, generic product, innovator product, etc.)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    regulatory: typing.List[fhirtypes.MedicationKnowledgeRegulatoryType] = Field(
        None,
        alias="regulatory",
        title="Regulatory information about a medication",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    relatedMedicationKnowledge: typing.List[
        fhirtypes.MedicationKnowledgeRelatedMedicationKnowledgeType
    ] = Field(
        None,
        alias="relatedMedicationKnowledge",
        title="Associated or related medication information",
        description="Associated or related knowledge about a medication.",
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="active | inactive | entered-in-error",
        description=(
            "A code to indicate if the medication is in active use.  The status "
            "refers to the validity about the information of the medication and not"
            " to its medicinal properties."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "inactive", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    synonym: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="synonym",
        title="Additional names for a medication",
        description=(
            "Additional names for a medication, for example, the name(s) given to a"
            " medication in different countries.  For example, acetaminophen and "
            "paracetamol or salbutamol and albuterol."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    synonym__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_synonym", title="Extension field for ``synonym``.")

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationKnowledge`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "code",
            "status",
            "manufacturer",
            "doseForm",
            "amount",
            "synonym",
            "relatedMedicationKnowledge",
            "associatedMedication",
            "productType",
            "monograph",
            "ingredient",
            "preparationInstruction",
            "intendedRoute",
            "cost",
            "monitoringProgram",
            "administrationGuidelines",
            "medicineClassification",
            "packaging",
            "drugCharacteristic",
            "contraindication",
            "regulatory",
            "kinetics",
        ]


class MedicationKnowledgeAdministrationGuidelines(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Guidelines for administration of the medication.
    Guidelines for the administration of the medication.
    """

    resource_type = Field("MedicationKnowledgeAdministrationGuidelines", const=True)

    dosage: typing.List[
        fhirtypes.MedicationKnowledgeAdministrationGuidelinesDosageType
    ] = Field(
        None,
        alias="dosage",
        title="Dosage for the medication for the specific guidelines",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    indicationCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="indicationCodeableConcept",
        title=(
            "Indication for use that apply to the specific administration " "guidelines"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e indication[x]
        one_of_many="indication",
        one_of_many_required=False,
    )

    indicationReference: fhirtypes.ReferenceType = Field(
        None,
        alias="indicationReference",
        title=(
            "Indication for use that apply to the specific administration " "guidelines"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e indication[x]
        one_of_many="indication",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ObservationDefinition"],
    )

    patientCharacteristics: typing.List[
        fhirtypes.MedicationKnowledgeAdministrationGuidelinesPatientCharacteristicsType
    ] = Field(
        None,
        alias="patientCharacteristics",
        title=(
            "Characteristics of the patient that are relevant to the administration"
            " guidelines"
        ),
        description=(
            "Characteristics of the patient that are relevant to the administration"
            " guidelines (for example, height, weight, gender, etc.)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationKnowledgeAdministrationGuidelines`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "dosage",
            "indicationCodeableConcept",
            "indicationReference",
            "patientCharacteristics",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_4652(
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
            "indication": ["indicationCodeableConcept", "indicationReference"]
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
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Dosage for the medication for the specific guidelines.
    """

    resource_type = Field(
        "MedicationKnowledgeAdministrationGuidelinesDosage", const=True
    )

    dosage: typing.List[fhirtypes.DosageType] = Field(
        ...,
        alias="dosage",
        title="Dosage for the medication for the specific guidelines",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type of dosage",
        description=(
            "The type of dosage (for example, prophylaxis, maintenance, "
            "therapeutic, etc.)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationKnowledgeAdministrationGuidelinesDosage`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "dosage"]


class MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Characteristics of the patient that are relevant to the administration
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
        title=(
            "Specific characteristic that is relevant to the administration "
            "guideline"
        ),
        description=(
            "Specific characteristic that is relevant to the administration "
            "guideline (e.g. height, weight, gender)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e characteristic[x]
        one_of_many="characteristic",
        one_of_many_required=True,
    )

    characteristicQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="characteristicQuantity",
        title=(
            "Specific characteristic that is relevant to the administration "
            "guideline"
        ),
        description=(
            "Specific characteristic that is relevant to the administration "
            "guideline (e.g. height, weight, gender)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e characteristic[x]
        one_of_many="characteristic",
        one_of_many_required=True,
    )

    value: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="value",
        title="The specific characteristic",
        description="The specific characteristic (e.g. height, weight, gender, etc.).",
        # if property is element of this resource.
        element_property=True,
    )
    value__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_value", title="Extension field for ``value``.")

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics``
        according specification, with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "characteristicCodeableConcept",
            "characteristicQuantity",
            "value",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_6941(
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
            "characteristic": [
                "characteristicCodeableConcept",
                "characteristicQuantity",
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


class MedicationKnowledgeCost(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The pricing of the medication.
    The price of the medication.
    """

    resource_type = Field("MedicationKnowledgeCost", const=True)

    cost: fhirtypes.MoneyType = Field(
        ...,
        alias="cost",
        title="The price of the medication",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    source: fhirtypes.String = Field(
        None,
        alias="source",
        title="The source or owner for the price information",
        description="The source or owner that assigns the price to the medication.",
        # if property is element of this resource.
        element_property=True,
    )
    source__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_source", title="Extension field for ``source``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="The category of the cost information",
        description=(
            "The category of the cost information.  For example, manufacturers' "
            "cost, patient cost, claim reimbursement cost, actual acquisition cost."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationKnowledgeCost`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "source", "cost"]


class MedicationKnowledgeDrugCharacteristic(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Specifies descriptive properties of the medicine.
    Specifies descriptive properties of the medicine, such as color, shape,
    imprints, etc.
    """

    resource_type = Field("MedicationKnowledgeDrugCharacteristic", const=True)

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Code specifying the type of characteristic of medication",
        description=(
            "A code specifying which characteristic of the medicine is being "
            "described (for example, colour, shape, imprint)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    valueBase64Binary: fhirtypes.Base64Binary = Field(
        None,
        alias="valueBase64Binary",
        title="Description of the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueBase64Binary__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_valueBase64Binary",
        title="Extension field for ``valueBase64Binary``.",
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="valueCodeableConcept",
        title="Description of the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="Description of the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Description of the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationKnowledgeDrugCharacteristic`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "valueCodeableConcept",
            "valueString",
            "valueQuantity",
            "valueBase64Binary",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3976(
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
                "valueBase64Binary",
                "valueCodeableConcept",
                "valueQuantity",
                "valueString",
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


class MedicationKnowledgeIngredient(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Active or inactive ingredient.
    Identifies a particular constituent of interest in the product.
    """

    resource_type = Field("MedicationKnowledgeIngredient", const=True)

    isActive: bool = Field(
        None,
        alias="isActive",
        title="Active ingredient indicator",
        description=(
            "Indication of whether this ingredient affects the therapeutic action "
            "of the drug."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    isActive__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_isActive", title="Extension field for ``isActive``."
    )

    itemCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="itemCodeableConcept",
        title="Medication(s) or substance(s) contained in the medication",
        description=(
            "The actual ingredient - either a substance (simple ingredient) or "
            "another medication."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e item[x]
        one_of_many="item",
        one_of_many_required=True,
    )

    itemReference: fhirtypes.ReferenceType = Field(
        None,
        alias="itemReference",
        title="Medication(s) or substance(s) contained in the medication",
        description=(
            "The actual ingredient - either a substance (simple ingredient) or "
            "another medication."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e item[x]
        one_of_many="item",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Substance"],
    )

    strength: fhirtypes.RatioType = Field(
        None,
        alias="strength",
        title="Quantity of ingredient present",
        description=(
            "Specifies how many (or how much) of the items there are in this "
            "Medication.  For example, 250 mg per tablet.  This is expressed as a "
            "ratio where the numerator is 250mg and the denominator is 1 tablet."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationKnowledgeIngredient`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "itemCodeableConcept",
            "itemReference",
            "isActive",
            "strength",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3175(
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
        one_of_many_fields = {"item": ["itemCodeableConcept", "itemReference"]}
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
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The time course of drug absorption, distribution, metabolism and excretion
    of a medication from the body.
    """

    resource_type = Field("MedicationKnowledgeKinetics", const=True)

    areaUnderCurve: typing.List[fhirtypes.QuantityType] = Field(
        None,
        alias="areaUnderCurve",
        title="The drug concentration measured at certain discrete points in time",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    halfLifePeriod: fhirtypes.DurationType = Field(
        None,
        alias="halfLifePeriod",
        title="Time required for concentration in the body to decrease by half",
        description=(
            "The time required for any specified property (e.g., the concentration "
            "of a substance in the body) to decrease by half."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    lethalDose50: typing.List[fhirtypes.QuantityType] = Field(
        None,
        alias="lethalDose50",
        title="The median lethal dose of a drug",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationKnowledgeKinetics`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "areaUnderCurve",
            "lethalDose50",
            "halfLifePeriod",
        ]


class MedicationKnowledgeMedicineClassification(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Categorization of the medication within a formulary or classification
    system.
    """

    resource_type = Field("MedicationKnowledgeMedicineClassification", const=True)

    classification: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="classification",
        title="Specific category assigned to the medication",
        description=(
            "Specific category assigned to the medication (e.g. anti-infective, "
            "anti-hypertensive, antibiotic, etc.)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title=(
            "The type of category for the medication (for example, therapeutic "
            "classification, therapeutic sub-classification)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationKnowledgeMedicineClassification`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "classification"]


class MedicationKnowledgeMonitoringProgram(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Program under which a medication is reviewed.
    The program under which the medication is reviewed.
    """

    resource_type = Field("MedicationKnowledgeMonitoringProgram", const=True)

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name of the reviewing program",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type of program under which the medication is monitored",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationKnowledgeMonitoringProgram`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "name"]


class MedicationKnowledgeMonograph(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Associated documentation about the medication.
    """

    resource_type = Field("MedicationKnowledgeMonograph", const=True)

    source: fhirtypes.ReferenceType = Field(
        None,
        alias="source",
        title="Associated documentation about the medication",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference", "Media"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="The category of medication document",
        description=(
            "The category of documentation about the medication. (e.g. professional"
            " monograph, patient education monograph)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationKnowledgeMonograph`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "source"]


class MedicationKnowledgePackaging(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details about packaged medications.
    Information that only applies to packages (not products).
    """

    resource_type = Field("MedicationKnowledgePackaging", const=True)

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="The number of product units the package would contain if fully loaded",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title=(
            "A code that defines the specific type of packaging that the medication"
            " can be found in"
        ),
        description=(
            "A code that defines the specific type of packaging that the medication"
            " can be found in (e.g. blister sleeve, tube, bottle)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationKnowledgePackaging`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "quantity"]


class MedicationKnowledgeRegulatory(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Regulatory information about a medication.
    """

    resource_type = Field("MedicationKnowledgeRegulatory", const=True)

    maxDispense: fhirtypes.MedicationKnowledgeRegulatoryMaxDispenseType = Field(
        None,
        alias="maxDispense",
        title=(
            "The maximum number of units of the medication that can be dispensed in"
            " a period"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    regulatoryAuthority: fhirtypes.ReferenceType = Field(
        ...,
        alias="regulatoryAuthority",
        title="Specifies the authority of the regulation",
        description="The authority that is specifying the regulations.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    schedule: typing.List[fhirtypes.MedicationKnowledgeRegulatoryScheduleType] = Field(
        None,
        alias="schedule",
        title="Specifies the schedule of a medication in jurisdiction",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    substitution: typing.List[
        fhirtypes.MedicationKnowledgeRegulatorySubstitutionType
    ] = Field(
        None,
        alias="substitution",
        title=(
            "Specifies if changes are allowed when dispensing a medication from a "
            "regulatory perspective"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationKnowledgeRegulatory`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "regulatoryAuthority",
            "substitution",
            "schedule",
            "maxDispense",
        ]


class MedicationKnowledgeRegulatoryMaxDispense(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The maximum number of units of the medication that can be dispensed in a
    period.
    """

    resource_type = Field("MedicationKnowledgeRegulatoryMaxDispense", const=True)

    period: fhirtypes.DurationType = Field(
        None,
        alias="period",
        title="The period that applies to the maximum number of units",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    quantity: fhirtypes.QuantityType = Field(
        ...,
        alias="quantity",
        title="The maximum number of units of the medication that can be dispensed",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationKnowledgeRegulatoryMaxDispense`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "quantity", "period"]


class MedicationKnowledgeRegulatorySchedule(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Specifies the schedule of a medication in jurisdiction.
    """

    resource_type = Field("MedicationKnowledgeRegulatorySchedule", const=True)

    schedule: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="schedule",
        title="Specifies the specific drug schedule",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationKnowledgeRegulatorySchedule`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "schedule"]


class MedicationKnowledgeRegulatorySubstitution(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Specifies if changes are allowed when dispensing a medication from a
    regulatory perspective.
    """

    resource_type = Field("MedicationKnowledgeRegulatorySubstitution", const=True)

    allowed: bool = Field(
        None,
        alias="allowed",
        title=(
            "Specifies if regulation allows for changes in the medication when "
            "dispensing"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    allowed__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_allowed", title="Extension field for ``allowed``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Specifies the type of substitution allowed",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationKnowledgeRegulatorySubstitution`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "allowed"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_4515(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("allowed", "allowed__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class MedicationKnowledgeRelatedMedicationKnowledge(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Associated or related medication information.
    Associated or related knowledge about a medication.
    """

    resource_type = Field("MedicationKnowledgeRelatedMedicationKnowledge", const=True)

    reference: typing.List[fhirtypes.ReferenceType] = Field(
        ...,
        alias="reference",
        title="Associated documentation about the associated medication knowledge",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicationKnowledge"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Category of medicationKnowledge",
        description="The category of the associated medication knowledge reference.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationKnowledgeRelatedMedicationKnowledge`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "reference"]
