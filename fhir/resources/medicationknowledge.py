# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationKnowledge
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class MedicationKnowledge(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Definition of Medication Knowledge.
    Information about a medication that is used to support knowledge.
    """

    resource_type = Field("MedicationKnowledge", const=True)

    associatedMedication: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="associatedMedication",
        title=(
            "The set of medication resources that are associated with this "
            "medication"
        ),
        description=(
            "Links to associated medications that could be prescribed, dispensed or"
            " administered."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Medication"],
    )

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title="Creator or owner of the knowledge or information about the medication",
        description=(
            "The creator or owner of the knowledge or information about the "
            "medication."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    clinicalUseIssue: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="clinicalUseIssue",
        title="Potential clinical issue with or between medication(s)",
        description=(
            "Potential clinical issue with or between medication(s) (for example, "
            "drug-drug interaction, drug-disease contraindication, drug-allergy "
            "interaction, etc.)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ClinicalUseDefinition"],
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

    cost: typing.List[fhirtypes.MedicationKnowledgeCostType] = Field(
        None,
        alias="cost",
        title="The pricing of the medication",
        description="The price of the medication.",
        # if property is element of this resource.
        element_property=True,
    )

    definitional: fhirtypes.MedicationKnowledgeDefinitionalType = Field(
        None,
        alias="definitional",
        title="Minimal definition information about the medication",
        description=(
            "Along with the link to a Medicinal Product Definition resource, this "
            "information provides common definitional elements that are needed to "
            "understand the specific medication that is being described."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier for this medication",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    indicationGuideline: typing.List[
        fhirtypes.MedicationKnowledgeIndicationGuidelineType
    ] = Field(
        None,
        alias="indicationGuideline",
        title=(
            "Guidelines or protocols for administration of the medication for an "
            "indication"
        ),
        description=(
            "Guidelines or protocols that are applicable for the administration of "
            "the medication based on indication."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    intendedJurisdiction: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="intendedJurisdiction",
        title=(
            "Codes that identify the different jurisdictions for which the "
            "information of this resource was created"
        ),
        description=(
            "Lists the jurisdictions that this medication knowledge was written " "for."
        ),
        # if property is element of this resource.
        element_property=True,
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

    name: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="name",
        title="A name associated with the medication being described",
        description=(
            "All of the names for a medication, for example, the name(s) given to a"
            " medication in different countries.  For example, acetaminophen and "
            "paracetamol or salbutamol and albuterol."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_name", title="Extension field for ``name``.")

    packaging: typing.List[fhirtypes.MedicationKnowledgePackagingType] = Field(
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
        description=(
            "Associated or related medications. For example, if the medication is a"
            " branded product (e.g. Crestor), this is the Therapeutic Moeity (e.g. "
            "Rosuvastatin) or if this is a generic medication (e.g. Rosuvastatin), "
            "this would link to a branded product (e.g. Crestor."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="active | entered-in-error | inactive",
        description=(
            "A code to indicate if the medication referred to by this "
            "MedicationKnowledge is in active use within the drug database or "
            "inventory system. The status refers to the validity about the "
            "information of the medication and not to its medicinal properties."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "entered-in-error", "inactive"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    storageGuideline: typing.List[
        fhirtypes.MedicationKnowledgeStorageGuidelineType
    ] = Field(
        None,
        alias="storageGuideline",
        title="How the medication should be stored",
        description=(
            "Information on how the medication should be stored, for example, "
            "refrigeration temperatures and length of stability at a given "
            "temperature."
        ),
        # if property is element of this resource.
        element_property=True,
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
            "identifier",
            "code",
            "status",
            "author",
            "intendedJurisdiction",
            "name",
            "relatedMedicationKnowledge",
            "associatedMedication",
            "productType",
            "monograph",
            "preparationInstruction",
            "cost",
            "monitoringProgram",
            "indicationGuideline",
            "medicineClassification",
            "packaging",
            "clinicalUseIssue",
            "storageGuideline",
            "regulatory",
            "definitional",
        ]


class MedicationKnowledgeCost(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The pricing of the medication.
    The price of the medication.
    """

    resource_type = Field("MedicationKnowledgeCost", const=True)

    costCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="costCodeableConcept",
        title="The price or category of the cost of the medication",
        description=(
            "The price or representation of the cost (for example, Band A, Band B "
            "or $, $$) of the medication."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e cost[x]
        one_of_many="cost",
        one_of_many_required=True,
    )

    costMoney: fhirtypes.MoneyType = Field(
        None,
        alias="costMoney",
        title="The price or category of the cost of the medication",
        description=(
            "The price or representation of the cost (for example, Band A, Band B "
            "or $, $$) of the medication."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e cost[x]
        one_of_many="cost",
        one_of_many_required=True,
    )

    effectiveDate: typing.List[fhirtypes.PeriodType] = Field(
        None,
        alias="effectiveDate",
        title="The date range for which the cost is effective",
        description=(
            "The date range for which the cost information of the medication is "
            "effective."
        ),
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
        return [
            "id",
            "extension",
            "modifierExtension",
            "effectiveDate",
            "type",
            "source",
            "costMoney",
            "costCodeableConcept",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2551(
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
        one_of_many_fields = {"cost": ["costCodeableConcept", "costMoney"]}
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


class MedicationKnowledgeDefinitional(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Minimal definition information about the medication.
    Along with the link to a Medicinal Product Definition resource, this
    information provides common definitional elements that are needed to
    understand the specific medication that is being described.
    """

    resource_type = Field("MedicationKnowledgeDefinitional", const=True)

    definition: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="definition",
        title=(
            "Definitional resources that provide more information about this "
            "medication"
        ),
        description="Associated definitions for this medication.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicinalProductDefinition"],
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
        fhirtypes.MedicationKnowledgeDefinitionalDrugCharacteristicType
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

    ingredient: typing.List[
        fhirtypes.MedicationKnowledgeDefinitionalIngredientType
    ] = Field(
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

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationKnowledgeDefinitional`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "definition",
            "doseForm",
            "intendedRoute",
            "ingredient",
            "drugCharacteristic",
        ]


class MedicationKnowledgeDefinitionalDrugCharacteristic(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Specifies descriptive properties of the medicine.
    Specifies descriptive properties of the medicine, such as color, shape,
    imprints, etc.
    """

    resource_type = Field(
        "MedicationKnowledgeDefinitionalDrugCharacteristic", const=True
    )

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

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="Description of the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
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
        ``MedicationKnowledgeDefinitionalDrugCharacteristic`` according specification,
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
            "valueAttachment",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_5214(
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
                "valueAttachment",
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


class MedicationKnowledgeDefinitionalIngredient(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Active or inactive ingredient.
    Identifies a particular constituent of interest in the product.
    """

    resource_type = Field("MedicationKnowledgeDefinitionalIngredient", const=True)

    item: fhirtypes.CodeableReferenceType = Field(
        ...,
        alias="item",
        title="Substances contained in the medication",
        description=(
            "A reference to the resource that provides information about the "
            "ingredient."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Substance"],
    )

    strengthCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="strengthCodeableConcept",
        title="Quantity of ingredient present",
        description=(
            "Specifies how many (or how much) of the items there are in this "
            "Medication.  For example, 250 mg per tablet.  This is expressed as a "
            "ratio where the numerator is 250mg and the denominator is 1 tablet but"
            " can also be expressed a quantity when the denominator is assumed to "
            "be 1 tablet."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e strength[x]
        one_of_many="strength",
        one_of_many_required=False,
    )

    strengthQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="strengthQuantity",
        title="Quantity of ingredient present",
        description=(
            "Specifies how many (or how much) of the items there are in this "
            "Medication.  For example, 250 mg per tablet.  This is expressed as a "
            "ratio where the numerator is 250mg and the denominator is 1 tablet but"
            " can also be expressed a quantity when the denominator is assumed to "
            "be 1 tablet."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e strength[x]
        one_of_many="strength",
        one_of_many_required=False,
    )

    strengthRatio: fhirtypes.RatioType = Field(
        None,
        alias="strengthRatio",
        title="Quantity of ingredient present",
        description=(
            "Specifies how many (or how much) of the items there are in this "
            "Medication.  For example, 250 mg per tablet.  This is expressed as a "
            "ratio where the numerator is 250mg and the denominator is 1 tablet but"
            " can also be expressed a quantity when the denominator is assumed to "
            "be 1 tablet."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e strength[x]
        one_of_many="strength",
        one_of_many_required=False,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="A code that defines the type of ingredient, active, base, etc",
        description=(
            "Indication of whether this ingredient affects the therapeutic action "
            "of the drug."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationKnowledgeDefinitionalIngredient`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "item",
            "type",
            "strengthRatio",
            "strengthCodeableConcept",
            "strengthQuantity",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_4413(
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
            "strength": ["strengthCodeableConcept", "strengthQuantity", "strengthRatio"]
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


class MedicationKnowledgeIndicationGuideline(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Guidelines or protocols for administration of the medication for an
    indication.
    Guidelines or protocols that are applicable for the administration of the
    medication based on indication.
    """

    resource_type = Field("MedicationKnowledgeIndicationGuideline", const=True)

    dosingGuideline: typing.List[
        fhirtypes.MedicationKnowledgeIndicationGuidelineDosingGuidelineType
    ] = Field(
        None,
        alias="dosingGuideline",
        title="Guidelines for dosage of the medication",
        description="The guidelines for the dosage of the medication for the indication.",
        # if property is element of this resource.
        element_property=True,
    )

    indication: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="indication",
        title=(
            "Indication for use that applies to the specific administration "
            "guideline"
        ),
        description=(
            "Indication or reason for use of the medication that applies to the "
            "specific administration guideline."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ClinicalUseDefinition"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationKnowledgeIndicationGuideline`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "indication", "dosingGuideline"]


class MedicationKnowledgeIndicationGuidelineDosingGuideline(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Guidelines for dosage of the medication.
    The guidelines for the dosage of the medication for the indication.
    """

    resource_type = Field(
        "MedicationKnowledgeIndicationGuidelineDosingGuideline", const=True
    )

    administrationTreatment: fhirtypes.CodeableConceptType = Field(
        None,
        alias="administrationTreatment",
        title="Type of treatment the guideline applies to",
        description=(
            "The type of the treatment that the guideline applies to, for example, "
            "long term therapy, first line treatment, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    dosage: typing.List[
        fhirtypes.MedicationKnowledgeIndicationGuidelineDosingGuidelineDosageType
    ] = Field(
        None,
        alias="dosage",
        title="Dosage for the medication for the specific guidelines",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    patientCharacteristic: typing.List[
        fhirtypes.MedicationKnowledgeIndicationGuidelineDosingGuidelinePatientCharacteristicType
    ] = Field(
        None,
        alias="patientCharacteristic",
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

    treatmentIntent: fhirtypes.CodeableConceptType = Field(
        None,
        alias="treatmentIntent",
        title="Intention of the treatment",
        description=(
            "The overall intention of the treatment, for example, prophylactic, "
            "supporative, curative, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationKnowledgeIndicationGuidelineDosingGuideline`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "treatmentIntent",
            "dosage",
            "administrationTreatment",
            "patientCharacteristic",
        ]


class MedicationKnowledgeIndicationGuidelineDosingGuidelineDosage(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Dosage for the medication for the specific guidelines.
    """

    resource_type = Field(
        "MedicationKnowledgeIndicationGuidelineDosingGuidelineDosage", const=True
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
        title="Category of dosage for a medication",
        description=(
            "The type or category of dosage for a given medication (for example, "
            "prophylaxis, maintenance, therapeutic, etc.)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationKnowledgeIndicationGuidelineDosingGuidelineDosage`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "dosage"]


class MedicationKnowledgeIndicationGuidelineDosingGuidelinePatientCharacteristic(
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
        "MedicationKnowledgeIndicationGuidelineDosingGuidelinePatientCharacteristic",
        const=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title=(
            "Categorization of specific characteristic that is relevant to the "
            "administration guideline"
        ),
        description=(
            "The categorization of the specific characteristic that is relevant to "
            "the administration guideline (e.g. height, weight, gender)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="valueCodeableConcept",
        title="The specific characteristic",
        description="The specific characteristic (e.g. height, weight, gender, etc.).",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="The specific characteristic",
        description="The specific characteristic (e.g. height, weight, gender, etc.).",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueRange: fhirtypes.RangeType = Field(
        None,
        alias="valueRange",
        title="The specific characteristic",
        description="The specific characteristic (e.g. height, weight, gender, etc.).",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationKnowledgeIndicationGuidelineDosingGuidelinePatientCharacteristic``
        according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "valueCodeableConcept",
            "valueQuantity",
            "valueRange",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_7773(
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
            "value": ["valueCodeableConcept", "valueQuantity", "valueRange"]
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

    sourceString: fhirtypes.String = Field(
        None,
        alias="sourceString",
        title="The source of the classification",
        description=(
            "Either a textual source of the classification or a reference to an "
            "online source."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e source[x]
        one_of_many="source",
        one_of_many_required=False,
    )
    sourceString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sourceString", title="Extension field for ``sourceString``."
    )

    sourceUri: fhirtypes.Uri = Field(
        None,
        alias="sourceUri",
        title="The source of the classification",
        description=(
            "Either a textual source of the classification or a reference to an "
            "online source."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e source[x]
        one_of_many="source",
        one_of_many_required=False,
    )
    sourceUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sourceUri", title="Extension field for ``sourceUri``."
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
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "sourceString",
            "sourceUri",
            "classification",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_4386(
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
        one_of_many_fields = {"source": ["sourceString", "sourceUri"]}
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
        enum_reference_types=["DocumentReference"],
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

    cost: typing.List[fhirtypes.MedicationKnowledgeCostType] = Field(
        None,
        alias="cost",
        title="Cost of the packaged medication",
        description="The cost of the packaged medication.",
        # if property is element of this resource.
        element_property=True,
    )

    packagedProduct: fhirtypes.ReferenceType = Field(
        None,
        alias="packagedProduct",
        title="The packaged medication that is being priced",
        description=(
            "A reference to a PackagedProductDefinition that provides the details "
            "of the product that is in the packaging and is being priced."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["PackagedProductDefinition"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationKnowledgePackaging`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "cost", "packagedProduct"]


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

    schedule: typing.List[fhirtypes.CodeableConceptType] = Field(
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
    Associated or related medications. For example, if the medication is a
    branded product (e.g. Crestor), this is the Therapeutic Moeity (e.g.
    Rosuvastatin) or if this is a generic medication (e.g. Rosuvastatin), this
    would link to a branded product (e.g. Crestor.
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


class MedicationKnowledgeStorageGuideline(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    How the medication should be stored.
    Information on how the medication should be stored, for example,
    refrigeration temperatures and length of stability at a given temperature.
    """

    resource_type = Field("MedicationKnowledgeStorageGuideline", const=True)

    environmentalSetting: typing.List[
        fhirtypes.MedicationKnowledgeStorageGuidelineEnvironmentalSettingType
    ] = Field(
        None,
        alias="environmentalSetting",
        title="Setting or value of environment for adequate storage",
        description=(
            "Describes a setting/value on the environment for the adequate storage "
            "of the medication and other substances.  Environment settings may "
            "involve temperature, humidity, or exposure to light."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Additional storage notes",
        description="Additional notes about the storage.",
        # if property is element of this resource.
        element_property=True,
    )

    reference: fhirtypes.Uri = Field(
        None,
        alias="reference",
        title="Reference to additional information",
        description="Reference to additional information about the storage guidelines.",
        # if property is element of this resource.
        element_property=True,
    )
    reference__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_reference", title="Extension field for ``reference``."
    )

    stabilityDuration: fhirtypes.DurationType = Field(
        None,
        alias="stabilityDuration",
        title="Duration remains stable",
        description=(
            "Duration that the medication remains stable if the "
            "environmentalSetting is respected."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationKnowledgeStorageGuideline`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "reference",
            "note",
            "stabilityDuration",
            "environmentalSetting",
        ]


class MedicationKnowledgeStorageGuidelineEnvironmentalSetting(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Setting or value of environment for adequate storage.
    Describes a setting/value on the environment for the adequate storage of
    the medication and other substances.  Environment settings may involve
    temperature, humidity, or exposure to light.
    """

    resource_type = Field(
        "MedicationKnowledgeStorageGuidelineEnvironmentalSetting", const=True
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Categorization of the setting",
        description=(
            "Identifies the category or type of setting (e.g., type of location, "
            "temperature, humidity)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="valueCodeableConcept",
        title="Value of the setting",
        description=(
            "Value associated to the setting. E.g., "
            "40\u00b0 \u2013 50\u00b0F for temperature."
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
        title="Value of the setting",
        description=(
            "Value associated to the setting. "
            "E.g., 40\u00b0 \u2013 50\u00b0F for temperature."
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
        title="Value of the setting",
        description=(
            "Value associated to the setting. "
            "E.g., 40\u00b0 \u2013 50\u00b0F for temperature."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationKnowledgeStorageGuidelineEnvironmentalSetting`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "valueQuantity",
            "valueRange",
            "valueCodeableConcept",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_5884(
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
            "value": ["valueCodeableConcept", "valueQuantity", "valueRange"]
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
