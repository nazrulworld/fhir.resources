# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubstanceSpecification
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class SubstanceSpecification(domainresource.DomainResource):
    """ The detailed description of a substance, typically at a level beyond what
    is used for prescribing.
    """

    resource_type = Field("SubstanceSpecification", const=True)

    code: ListType[fhirtypes.SubstanceSpecificationCodeType] = Field(
        None,
        alias="code",
        title="List of `SubstanceSpecificationCode` items (represented as `dict` in JSON)",
        description="Codes associated with the substance",
    )

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Type `String` (represented as `dict` in JSON)",
        description="Textual comment about this record of a substance",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Textual description of the substance",
    )

    domain: fhirtypes.CodeableConceptType = Field(
        None,
        alias="domain",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="If the substance applies to only human or veterinary use",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Identifier by which this substance is known",
    )

    moiety: ListType[fhirtypes.SubstanceSpecificationMoietyType] = Field(
        None,
        alias="moiety",
        title="List of `SubstanceSpecificationMoiety` items (represented as `dict` in JSON)",
        description="Moiety, for structural modifications",
    )

    molecularWeight: ListType[
        fhirtypes.SubstanceSpecificationStructureIsotopeMolecularWeightType
    ] = Field(
        None,
        alias="molecularWeight",
        title="List of `SubstanceSpecificationStructureIsotopeMolecularWeight` items (represented as `dict` in JSON)",
        description="The molecular weight or weight range (for proteins, polymers or nucleic acids)",
    )

    name: ListType[fhirtypes.SubstanceSpecificationNameType] = Field(
        None,
        alias="name",
        title="List of `SubstanceSpecificationName` items (represented as `dict` in JSON)",
        description="Names applicable to this substance",
    )

    nucleicAcid: fhirtypes.ReferenceType = Field(
        None,
        alias="nucleicAcid",
        title="Type `Reference` referencing `SubstanceNucleicAcid` (represented as `dict` in JSON)",
        description="Data items specific to nucleic acids",
    )

    polymer: fhirtypes.ReferenceType = Field(
        None,
        alias="polymer",
        title="Type `Reference` referencing `SubstancePolymer` (represented as `dict` in JSON)",
        description="Data items specific to polymers",
    )

    property: ListType[fhirtypes.SubstanceSpecificationPropertyType] = Field(
        None,
        alias="property",
        title="List of `SubstanceSpecificationProperty` items (represented as `dict` in JSON)",
        description="General specifications for this substance, including how it is related to other substances",
    )

    protein: fhirtypes.ReferenceType = Field(
        None,
        alias="protein",
        title="Type `Reference` referencing `SubstanceProtein` (represented as `dict` in JSON)",
        description="Data items specific to proteins",
    )

    referenceInformation: fhirtypes.ReferenceType = Field(
        None,
        alias="referenceInformation",
        title="Type `Reference` referencing `SubstanceReferenceInformation` (represented as `dict` in JSON)",
        description="General information detailing this substance",
    )

    relationship: ListType[fhirtypes.SubstanceSpecificationRelationshipType] = Field(
        None,
        alias="relationship",
        title="List of `SubstanceSpecificationRelationship` items (represented as `dict` in JSON)",
        description="A link between this substance and another, with details of the relationship",
    )

    source: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="source",
        title="List of `Reference` items referencing `DocumentReference` (represented as `dict` in JSON)",
        description="Supporting literature",
    )

    sourceMaterial: fhirtypes.ReferenceType = Field(
        None,
        alias="sourceMaterial",
        title="Type `Reference` referencing `SubstanceSourceMaterial` (represented as `dict` in JSON)",
        description="Material or taxonomic/anatomical source for the substance",
    )

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Status of substance within the catalogue e.g. approved",
    )

    structure: fhirtypes.SubstanceSpecificationStructureType = Field(
        None,
        alias="structure",
        title="Type `SubstanceSpecificationStructure` (represented as `dict` in JSON)",
        description="Structural information",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="High level categorization, e.g. polymer or nucleic acid",
    )


class SubstanceSpecificationCode(backboneelement.BackboneElement):
    """ Codes associated with the substance.
    """

    resource_type = Field("SubstanceSpecificationCode", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The specific code",
    )

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Type `String` (represented as `dict` in JSON)",
        description="Any comment can be provided in this field, if necessary",
    )

    source: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="source",
        title="List of `Reference` items referencing `DocumentReference` (represented as `dict` in JSON)",
        description="Supporting literature",
    )

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Status of the code assignment",
    )

    statusDate: fhirtypes.DateTime = Field(
        None,
        alias="statusDate",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="The date at which the code status is changed as part of the terminology maintenance",
    )


class SubstanceSpecificationMoiety(backboneelement.BackboneElement):
    """ Moiety, for structural modifications.
    """

    resource_type = Field("SubstanceSpecificationMoiety", const=True)

    amountQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="amountQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Quantitative value for this moiety",
        one_of_many="amount",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    amountString: fhirtypes.String = Field(
        None,
        alias="amountString",
        title="Type `String` (represented as `dict` in JSON)",
        description="Quantitative value for this moiety",
        one_of_many="amount",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Identifier by which this moiety substance is known",
    )

    molecularFormula: fhirtypes.String = Field(
        None,
        alias="molecularFormula",
        title="Type `String` (represented as `dict` in JSON)",
        description="Molecular formula",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Textual name for this moiety substance",
    )

    opticalActivity: fhirtypes.CodeableConceptType = Field(
        None,
        alias="opticalActivity",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Optical activity type",
    )

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Role that the moiety is playing",
    )

    stereochemistry: fhirtypes.CodeableConceptType = Field(
        None,
        alias="stereochemistry",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Stereochemistry type",
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
            "amount": ["amountQuantity", "amountString",],
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


class SubstanceSpecificationName(backboneelement.BackboneElement):
    """ Names applicable to this substance.
    """

    resource_type = Field("SubstanceSpecificationName", const=True)

    domain: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="domain",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="The use context of this name for example if there is a different name a drug active ingredient as opposed to a food colour additive",
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="The jurisdiction where this name applies",
    )

    language: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="language",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Language of the name",
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="The actual name",
    )

    official: ListType[fhirtypes.SubstanceSpecificationNameOfficialType] = Field(
        None,
        alias="official",
        title="List of `SubstanceSpecificationNameOfficial` items (represented as `dict` in JSON)",
        description="Details of the official nature of this name",
    )

    preferred: bool = Field(
        None,
        alias="preferred",
        title="Type `bool`",
        description="If this is the preferred name for this substance",
    )

    source: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="source",
        title="List of `Reference` items referencing `DocumentReference` (represented as `dict` in JSON)",
        description="Supporting literature",
    )

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The status of the name",
    )

    synonym: ListType[fhirtypes.SubstanceSpecificationNameType] = Field(
        None,
        alias="synonym",
        title="List of `SubstanceSpecificationName` items (represented as `dict` in JSON)",
        description="A synonym of this name",
    )

    translation: ListType[fhirtypes.SubstanceSpecificationNameType] = Field(
        None,
        alias="translation",
        title="List of `SubstanceSpecificationName` items (represented as `dict` in JSON)",
        description="A translation for this name",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Name type",
    )


class SubstanceSpecificationNameOfficial(backboneelement.BackboneElement):
    """ Details of the official nature of this name.
    """

    resource_type = Field("SubstanceSpecificationNameOfficial", const=True)

    authority: fhirtypes.CodeableConceptType = Field(
        None,
        alias="authority",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Which authority uses this official name",
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date of official name change",
    )

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The status of the official name",
    )


class SubstanceSpecificationProperty(backboneelement.BackboneElement):
    """ General specifications for this substance, including how it is related to
    other substances.
    """

    resource_type = Field("SubstanceSpecificationProperty", const=True)

    amountQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="amountQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Quantitative value for this property",
        one_of_many="amount",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    amountString: fhirtypes.String = Field(
        None,
        alias="amountString",
        title="Type `String` (represented as `dict` in JSON)",
        description="Quantitative value for this property",
        one_of_many="amount",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="A category for this property, e.g. Physical, Chemical, Enzymatic",
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Property type e.g. viscosity, pH, isoelectric point",
    )

    definingSubstanceCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="definingSubstanceCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="A substance upon which a defining property depends (e.g. for solubility: in water, in alcohol)",
        one_of_many="definingSubstance",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    definingSubstanceReference: fhirtypes.ReferenceType = Field(
        None,
        alias="definingSubstanceReference",
        title="Type `Reference` referencing `SubstanceSpecification, Substance` (represented as `dict` in JSON)",
        description="A substance upon which a defining property depends (e.g. for solubility: in water, in alcohol)",
        one_of_many="definingSubstance",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    parameters: fhirtypes.String = Field(
        None,
        alias="parameters",
        title="Type `String` (represented as `dict` in JSON)",
        description="Parameters that were used in the measurement of a property (e.g. for viscosity: measured at 20C with a pH of 7.1)",
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
            "amount": ["amountQuantity", "amountString",],
            "definingSubstance": [
                "definingSubstanceCodeableConcept",
                "definingSubstanceReference",
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


class SubstanceSpecificationRelationship(backboneelement.BackboneElement):
    """ A link between this substance and another, with details of the relationship.
    """

    resource_type = Field("SubstanceSpecificationRelationship", const=True)

    amountQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="amountQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="A numeric factor for the relationship, for instance to express that the salt of a substance has some percentage of the active substance in relation to some other",
        one_of_many="amount",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    amountRange: fhirtypes.RangeType = Field(
        None,
        alias="amountRange",
        title="Type `Range` (represented as `dict` in JSON)",
        description="A numeric factor for the relationship, for instance to express that the salt of a substance has some percentage of the active substance in relation to some other",
        one_of_many="amount",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    amountRatio: fhirtypes.RatioType = Field(
        None,
        alias="amountRatio",
        title="Type `Ratio` (represented as `dict` in JSON)",
        description="A numeric factor for the relationship, for instance to express that the salt of a substance has some percentage of the active substance in relation to some other",
        one_of_many="amount",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    amountRatioLowLimit: fhirtypes.RatioType = Field(
        None,
        alias="amountRatioLowLimit",
        title="Type `Ratio` (represented as `dict` in JSON)",
        description="For use when the numeric",
    )

    amountString: fhirtypes.String = Field(
        None,
        alias="amountString",
        title="Type `String` (represented as `dict` in JSON)",
        description="A numeric factor for the relationship, for instance to express that the salt of a substance has some percentage of the active substance in relation to some other",
        one_of_many="amount",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    amountType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="amountType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description='An operator for the amount, for example "average", "approximately", "less than"',
    )

    isDefining: bool = Field(
        None,
        alias="isDefining",
        title="Type `bool`",
        description="For example where an enzyme strongly bonds with a particular substance, this is a defining relationship for that enzyme, out of several possible substance relationships",
    )

    relationship: fhirtypes.CodeableConceptType = Field(
        None,
        alias="relationship",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description='For example "salt to parent", "active moiety", "starting material"',
    )

    source: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="source",
        title="List of `Reference` items referencing `DocumentReference` (represented as `dict` in JSON)",
        description="Supporting literature",
    )

    substanceCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="substanceCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="A pointer to another substance, as a resource or just a representational code",
        one_of_many="substance",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    substanceReference: fhirtypes.ReferenceType = Field(
        None,
        alias="substanceReference",
        title="Type `Reference` referencing `SubstanceSpecification` (represented as `dict` in JSON)",
        description="A pointer to another substance, as a resource or just a representational code",
        one_of_many="substance",  # Choice of Data Types. i.e value[x]
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
            "amount": ["amountQuantity", "amountRange", "amountRatio", "amountString",],
            "substance": ["substanceCodeableConcept", "substanceReference",],
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


class SubstanceSpecificationStructure(backboneelement.BackboneElement):
    """ Structural information.
    """

    resource_type = Field("SubstanceSpecificationStructure", const=True)

    isotope: ListType[fhirtypes.SubstanceSpecificationStructureIsotopeType] = Field(
        None,
        alias="isotope",
        title="List of `SubstanceSpecificationStructureIsotope` items (represented as `dict` in JSON)",
        description="Applicable for single substances that contain a radionuclide or a non-natural isotopic ratio",
    )

    molecularFormula: fhirtypes.String = Field(
        None,
        alias="molecularFormula",
        title="Type `String` (represented as `dict` in JSON)",
        description="Molecular formula",
    )

    molecularFormulaByMoiety: fhirtypes.String = Field(
        None,
        alias="molecularFormulaByMoiety",
        title="Type `String` (represented as `dict` in JSON)",
        description="Specified per moiety according to the Hill system, i.e. first C, then H, then alphabetical, each moiety separated by a dot",
    )

    molecularWeight: fhirtypes.SubstanceSpecificationStructureIsotopeMolecularWeightType = Field(
        None,
        alias="molecularWeight",
        title="Type `SubstanceSpecificationStructureIsotopeMolecularWeight` (represented as `dict` in JSON)",
        description="The molecular weight or weight range (for proteins, polymers or nucleic acids)",
    )

    opticalActivity: fhirtypes.CodeableConceptType = Field(
        None,
        alias="opticalActivity",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Optical activity type",
    )

    representation: ListType[
        fhirtypes.SubstanceSpecificationStructureRepresentationType
    ] = Field(
        None,
        alias="representation",
        title="List of `SubstanceSpecificationStructureRepresentation` items (represented as `dict` in JSON)",
        description="Molecular structural representation",
    )

    source: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="source",
        title="List of `Reference` items referencing `DocumentReference` (represented as `dict` in JSON)",
        description="Supporting literature",
    )

    stereochemistry: fhirtypes.CodeableConceptType = Field(
        None,
        alias="stereochemistry",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Stereochemistry type",
    )


class SubstanceSpecificationStructureIsotope(backboneelement.BackboneElement):
    """ Applicable for single substances that contain a radionuclide or a non-
    natural isotopic ratio.
    """

    resource_type = Field("SubstanceSpecificationStructureIsotope", const=True)

    halfLife: fhirtypes.QuantityType = Field(
        None,
        alias="halfLife",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Half life - for a non-natural nuclide",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Substance identifier for each non-natural or radioisotope",
    )

    molecularWeight: fhirtypes.SubstanceSpecificationStructureIsotopeMolecularWeightType = Field(
        None,
        alias="molecularWeight",
        title="Type `SubstanceSpecificationStructureIsotopeMolecularWeight` (represented as `dict` in JSON)",
        description="The molecular weight or weight range (for proteins, polymers or nucleic acids)",
    )

    name: fhirtypes.CodeableConceptType = Field(
        None,
        alias="name",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Substance name for each non-natural or radioisotope",
    )

    substitution: fhirtypes.CodeableConceptType = Field(
        None,
        alias="substitution",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The type of isotopic substitution present in a single substance",
    )


class SubstanceSpecificationStructureIsotopeMolecularWeight(
    backboneelement.BackboneElement
):
    """ The molecular weight or weight range (for proteins, polymers or nucleic
    acids).
    """

    resource_type = Field(
        "SubstanceSpecificationStructureIsotopeMolecularWeight", const=True
    )

    amount: fhirtypes.QuantityType = Field(
        None,
        alias="amount",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Used to capture quantitative values for a variety of elements. If only limits are given, the arithmetic mean would be the average. If only a single definite value for a given element is given, it would be captured in this field",
    )

    method: fhirtypes.CodeableConceptType = Field(
        None,
        alias="method",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The method by which the molecular weight was determined",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of molecular weight such as exact, average (also known as. number average), weight average",
    )


class SubstanceSpecificationStructureRepresentation(backboneelement.BackboneElement):
    """ Molecular structural representation.
    """

    resource_type = Field("SubstanceSpecificationStructureRepresentation", const=True)

    attachment: fhirtypes.AttachmentType = Field(
        None,
        alias="attachment",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="An attached file with the structural representation",
    )

    representation: fhirtypes.String = Field(
        None,
        alias="representation",
        title="Type `String` (represented as `dict` in JSON)",
        description="The structural representation as text string in a format e.g. InChI, SMILES, MOLFILE, CDX",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The type of structure (e.g. Full, Partial, Representative)",
    )
