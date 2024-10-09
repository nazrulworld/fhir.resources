from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationKnowledge
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class MedicationKnowledge(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Definition of Medication Knowledge.
    Information about a medication that is used to support knowledge.
    """

    __resource_type__ = "MedicationKnowledge"

    administrationGuidelines: typing.List[fhirtypes.MedicationKnowledgeAdministrationGuidelinesType] | None = Field(  # type: ignore
        None,
        alias="administrationGuidelines",
        title="Guidelines for administration of the medication",
        description="Guidelines for the administration of the medication.",
        json_schema_extra={
            "element_property": True,
        },
    )

    amount: fhirtypes.QuantityType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )

    associatedMedication: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="associatedMedication",
        title="A medication resource that is associated with this medication",
        description=(
            "Associated or related medications.  For example, if the medication is "
            "a branded product (e.g. Crestor), this is the Therapeutic Moeity (e.g."
            " Rosuvastatin) or if this is a generic medication (e.g. Rosuvastatin),"
            " this would link to a branded product (e.g. Crestor)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Medication"],
        },
    )

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )

    contraindication: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="contraindication",
        title="Potential clinical issue with or between medication(s)",
        description=(
            "Potential clinical issue with or between medication(s) (for example, "
            "drug-drug interaction, drug-disease contraindication, drug-allergy "
            "interaction, etc.)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DetectedIssue"],
        },
    )

    cost: typing.List[fhirtypes.MedicationKnowledgeCostType] | None = Field(  # type: ignore
        None,
        alias="cost",
        title="The pricing of the medication",
        description="The price of the medication.",
        json_schema_extra={
            "element_property": True,
        },
    )

    doseForm: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="doseForm",
        title="powder | tablets | capsule +",
        description="Describes the form of the item.  Powder; tablets; capsule.",
        json_schema_extra={
            "element_property": True,
        },
    )

    drugCharacteristic: typing.List[fhirtypes.MedicationKnowledgeDrugCharacteristicType] | None = Field(  # type: ignore
        None,
        alias="drugCharacteristic",
        title="Specifies descriptive properties of the medicine",
        description=(
            "Specifies descriptive properties of the medicine, such as color, "
            "shape, imprints, etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    ingredient: typing.List[fhirtypes.MedicationKnowledgeIngredientType] | None = Field(  # type: ignore
        None,
        alias="ingredient",
        title="Active or inactive ingredient",
        description="Identifies a particular constituent of interest in the product.",
        json_schema_extra={
            "element_property": True,
        },
    )

    intendedRoute: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="intendedRoute",
        title="The intended or approved route of administration",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    kinetics: typing.List[fhirtypes.MedicationKnowledgeKineticsType] | None = Field(  # type: ignore
        None,
        alias="kinetics",
        title=(
            "The time course of drug absorption, distribution, metabolism and "
            "excretion of a medication from the body"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    manufacturer: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="manufacturer",
        title="Manufacturer of the item",
        description=(
            "Describes the details of the manufacturer of the medication product.  "
            "This is not intended to represent the distributor of a medication "
            "product."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    medicineClassification: typing.List[fhirtypes.MedicationKnowledgeMedicineClassificationType] | None = Field(  # type: ignore
        None,
        alias="medicineClassification",
        title=(
            "Categorization of the medication within a formulary or classification "
            "system"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    monitoringProgram: typing.List[fhirtypes.MedicationKnowledgeMonitoringProgramType] | None = Field(  # type: ignore
        None,
        alias="monitoringProgram",
        title="Program under which a medication is reviewed",
        description="The program under which the medication is reviewed.",
        json_schema_extra={
            "element_property": True,
        },
    )

    monograph: typing.List[fhirtypes.MedicationKnowledgeMonographType] | None = Field(  # type: ignore
        None,
        alias="monograph",
        title="Associated documentation about the medication",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    packaging: fhirtypes.MedicationKnowledgePackagingType | None = Field(  # type: ignore
        None,
        alias="packaging",
        title="Details about packaged medications",
        description="Information that only applies to packages (not products).",
        json_schema_extra={
            "element_property": True,
        },
    )

    preparationInstruction: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="preparationInstruction",
        title="The instructions for preparing the medication",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    preparationInstruction__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_preparationInstruction",
        title="Extension field for ``preparationInstruction``.",
    )

    productType: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="productType",
        title="Category of the medication or product",
        description=(
            "Category of the medication or product (e.g. branded product, "
            "therapeutic moeity, generic product, innovator product, etc.)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    regulatory: typing.List[fhirtypes.MedicationKnowledgeRegulatoryType] | None = Field(  # type: ignore
        None,
        alias="regulatory",
        title="Regulatory information about a medication",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    relatedMedicationKnowledge: typing.List[fhirtypes.MedicationKnowledgeRelatedMedicationKnowledgeType] | None = Field(  # type: ignore
        None,
        alias="relatedMedicationKnowledge",
        title="Associated or related medication information",
        description="Associated or related knowledge about a medication.",
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="active | inactive | entered-in-error",
        description=(
            "A code to indicate if the medication is in active use.  The status "
            "refers to the validity about the information of the medication and not"
            " to its medicinal properties."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["active", "inactive", "entered-in-error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    synonym: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="synonym",
        title="Additional names for a medication",
        description=(
            "Additional names for a medication, for example, the name(s) given to a"
            " medication in different countries.  For example, acetaminophen and "
            "paracetamol or salbutamol and albuterol."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    synonym__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_synonym", title="Extension field for ``synonym``."
    )

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

    __resource_type__ = "MedicationKnowledgeAdministrationGuidelines"

    dosage: typing.List[fhirtypes.MedicationKnowledgeAdministrationGuidelinesDosageType] | None = Field(  # type: ignore
        None,
        alias="dosage",
        title="Dosage for the medication for the specific guidelines",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    indicationCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="indicationCodeableConcept",
        title=(
            "Indication for use that apply to the specific administration " "guidelines"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e indication[x]
            "one_of_many": "indication",
            "one_of_many_required": False,
        },
    )

    indicationReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="indicationReference",
        title=(
            "Indication for use that apply to the specific administration " "guidelines"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e indication[x]
            "one_of_many": "indication",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ObservationDefinition"],
        },
    )

    patientCharacteristics: typing.List[fhirtypes.MedicationKnowledgeAdministrationGuidelinesPatientCharacteristicsType] | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
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
            "indication": ["indicationCodeableConcept", "indicationReference"]
        }
        return one_of_many_fields


class MedicationKnowledgeAdministrationGuidelinesDosage(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Dosage for the medication for the specific guidelines.
    """

    __resource_type__ = "MedicationKnowledgeAdministrationGuidelinesDosage"

    dosage: typing.List[fhirtypes.DosageType] = Field(  # type: ignore
        ...,
        alias="dosage",
        title="Dosage for the medication for the specific guidelines",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Type of dosage",
        description=(
            "The type of dosage (for example, prophylaxis, maintenance, "
            "therapeutic, etc.)."
        ),
        json_schema_extra={
            "element_property": True,
        },
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

    __resource_type__ = (
        "MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics"
    )

    characteristicCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e characteristic[x]
            "one_of_many": "characteristic",
            "one_of_many_required": True,
        },
    )

    characteristicQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e characteristic[x]
            "one_of_many": "characteristic",
            "one_of_many_required": True,
        },
    )

    value: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="value",
        title="The specific characteristic",
        description="The specific characteristic (e.g. height, weight, gender, etc.).",
        json_schema_extra={
            "element_property": True,
        },
    )
    value__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "characteristicCodeableConcept",
            "characteristicQuantity",
            "value",
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
            "characteristic": [
                "characteristicCodeableConcept",
                "characteristicQuantity",
            ]
        }
        return one_of_many_fields


class MedicationKnowledgeCost(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The pricing of the medication.
    The price of the medication.
    """

    __resource_type__ = "MedicationKnowledgeCost"

    cost: fhirtypes.MoneyType = Field(  # type: ignore
        ...,
        alias="cost",
        title="The price of the medication",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    source: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="source",
        title="The source or owner for the price information",
        description="The source or owner that assigns the price to the medication.",
        json_schema_extra={
            "element_property": True,
        },
    )
    source__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_source", title="Extension field for ``source``."
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="The category of the cost information",
        description=(
            "The category of the cost information.  For example, manufacturers' "
            "cost, patient cost, claim reimbursement cost, actual acquisition cost."
        ),
        json_schema_extra={
            "element_property": True,
        },
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

    __resource_type__ = "MedicationKnowledgeDrugCharacteristic"

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Code specifying the type of characteristic of medication",
        description=(
            "A code specifying which characteristic of the medicine is being "
            "described (for example, colour, shape, imprint)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    valueBase64Binary: fhirtypes.Base64BinaryType | None = Field(  # type: ignore
        None,
        alias="valueBase64Binary",
        title="Description of the characteristic",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueBase64Binary__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_valueBase64Binary",
        title="Extension field for ``valueBase64Binary``.",
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="valueCodeableConcept",
        title="Description of the characteristic",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="valueQuantity",
        title="Description of the characteristic",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="valueString",
        title="Description of the characteristic",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
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
            "value": [
                "valueBase64Binary",
                "valueCodeableConcept",
                "valueQuantity",
                "valueString",
            ]
        }
        return one_of_many_fields


class MedicationKnowledgeIngredient(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Active or inactive ingredient.
    Identifies a particular constituent of interest in the product.
    """

    __resource_type__ = "MedicationKnowledgeIngredient"

    isActive: bool | None = Field(  # type: ignore
        None,
        alias="isActive",
        title="Active ingredient indicator",
        description=(
            "Indication of whether this ingredient affects the therapeutic action "
            "of the drug."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    isActive__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_isActive", title="Extension field for ``isActive``."
    )

    itemCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="itemCodeableConcept",
        title="Medication(s) or substance(s) contained in the medication",
        description=(
            "The actual ingredient - either a substance (simple ingredient) or "
            "another medication."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e item[x]
            "one_of_many": "item",
            "one_of_many_required": True,
        },
    )

    itemReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="itemReference",
        title="Medication(s) or substance(s) contained in the medication",
        description=(
            "The actual ingredient - either a substance (simple ingredient) or "
            "another medication."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e item[x]
            "one_of_many": "item",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Substance"],
        },
    )

    strength: fhirtypes.RatioType | None = Field(  # type: ignore
        None,
        alias="strength",
        title="Quantity of ingredient present",
        description=(
            "Specifies how many (or how much) of the items there are in this "
            "Medication.  For example, 250 mg per tablet.  This is expressed as a "
            "ratio where the numerator is 250mg and the denominator is 1 tablet."
        ),
        json_schema_extra={
            "element_property": True,
        },
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
        one_of_many_fields = {"item": ["itemCodeableConcept", "itemReference"]}
        return one_of_many_fields


class MedicationKnowledgeKinetics(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The time course of drug absorption, distribution, metabolism and excretion
    of a medication from the body.
    """

    __resource_type__ = "MedicationKnowledgeKinetics"

    areaUnderCurve: typing.List[fhirtypes.QuantityType] | None = Field(  # type: ignore
        None,
        alias="areaUnderCurve",
        title="The drug concentration measured at certain discrete points in time",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    halfLifePeriod: fhirtypes.DurationType | None = Field(  # type: ignore
        None,
        alias="halfLifePeriod",
        title="Time required for concentration in the body to decrease by half",
        description=(
            "The time required for any specified property (e.g., the concentration "
            "of a substance in the body) to decrease by half."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    lethalDose50: typing.List[fhirtypes.QuantityType] | None = Field(  # type: ignore
        None,
        alias="lethalDose50",
        title="The median lethal dose of a drug",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
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

    __resource_type__ = "MedicationKnowledgeMedicineClassification"

    classification: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="classification",
        title="Specific category assigned to the medication",
        description=(
            "Specific category assigned to the medication (e.g. anti-infective, "
            "anti-hypertensive, antibiotic, etc.)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title=(
            "The type of category for the medication (for example, therapeutic "
            "classification, therapeutic sub-classification)"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
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

    __resource_type__ = "MedicationKnowledgeMonitoringProgram"

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name of the reviewing program",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Type of program under which the medication is monitored",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
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

    __resource_type__ = "MedicationKnowledgeMonograph"

    source: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="source",
        title="Associated documentation about the medication",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DocumentReference", "Media"],
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="The category of medication document",
        description=(
            "The category of documentation about the medication. (e.g. professional"
            " monograph, patient education monograph)."
        ),
        json_schema_extra={
            "element_property": True,
        },
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

    __resource_type__ = "MedicationKnowledgePackaging"

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="The number of product units the package would contain if fully loaded",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
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

    __resource_type__ = "MedicationKnowledgeRegulatory"

    maxDispense: fhirtypes.MedicationKnowledgeRegulatoryMaxDispenseType | None = Field(  # type: ignore
        None,
        alias="maxDispense",
        title=(
            "The maximum number of units of the medication that can be dispensed in"
            " a period"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    regulatoryAuthority: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="regulatoryAuthority",
        title="Specifies the authority of the regulation",
        description="The authority that is specifying the regulations.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    schedule: typing.List[fhirtypes.MedicationKnowledgeRegulatoryScheduleType] | None = Field(  # type: ignore
        None,
        alias="schedule",
        title="Specifies the schedule of a medication in jurisdiction",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    substitution: typing.List[fhirtypes.MedicationKnowledgeRegulatorySubstitutionType] | None = Field(  # type: ignore
        None,
        alias="substitution",
        title=(
            "Specifies if changes are allowed when dispensing a medication from a "
            "regulatory perspective"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
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

    __resource_type__ = "MedicationKnowledgeRegulatoryMaxDispense"

    period: fhirtypes.DurationType | None = Field(  # type: ignore
        None,
        alias="period",
        title="The period that applies to the maximum number of units",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    quantity: fhirtypes.QuantityType = Field(  # type: ignore
        ...,
        alias="quantity",
        title="The maximum number of units of the medication that can be dispensed",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
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

    __resource_type__ = "MedicationKnowledgeRegulatorySchedule"

    schedule: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="schedule",
        title="Specifies the specific drug schedule",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
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

    __resource_type__ = "MedicationKnowledgeRegulatorySubstitution"

    allowed: bool | None = Field(  # type: ignore
        None,
        alias="allowed",
        title=(
            "Specifies if regulation allows for changes in the medication when "
            "dispensing"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    allowed__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_allowed", title="Extension field for ``allowed``."
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Specifies the type of substitution allowed",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationKnowledgeRegulatorySubstitution`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "allowed"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("allowed", "allowed__ext")]
        return required_fields


class MedicationKnowledgeRelatedMedicationKnowledge(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Associated or related medication information.
    Associated or related knowledge about a medication.
    """

    __resource_type__ = "MedicationKnowledgeRelatedMedicationKnowledge"

    reference: typing.List[fhirtypes.ReferenceType] = Field(  # type: ignore
        ...,
        alias="reference",
        title="Associated documentation about the associated medication knowledge",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["MedicationKnowledge"],
        },
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Category of medicationKnowledge",
        description="The category of the associated medication knowledge reference.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationKnowledgeRelatedMedicationKnowledge`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "reference"]
