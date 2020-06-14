# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubstanceSourceMaterial
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class SubstanceSourceMaterial(domainresource.DomainResource):
    """ Source material shall capture information on the taxonomic and anatomical
    origins as well as the fraction of a material that can result in or can be
    modified to form a substance. This set of data elements shall be used to
    define polymer substances isolated from biological matrices. Taxonomic and
    anatomical origins shall be described using a controlled vocabulary as
    required. This information is captured for naturally derived polymers ( .
    starch) and structurally diverse substances. For Organisms belonging to the
    Kingdom Plantae the Substance level defines the fresh material of a single
    species or infraspecies, the Herbal Drug and the Herbal preparation. For
    Herbal preparations, the fraction information will be captured at the
    Substance information level and additional information for herbal extracts
    will be captured at the Specified Substance Group 1 information level. See
    for further explanation the Substance Class: Structurally Diverse and the
    herbal annex.
    """

    resource_type = Field("SubstanceSourceMaterial", const=True)

    countryOfOrigin: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="countryOfOrigin",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="The country where the plant material is harvested or the countries where the plasma is sourced from as laid down in accordance with the Plasma Master File. For \u201cPlasma-derived substances\u201d the attribute country of origin provides information about the countries used for the manufacturing of the Cryopoor plama or Crioprecipitate",
    )

    developmentStage: fhirtypes.CodeableConceptType = Field(
        None,
        alias="developmentStage",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Stage of life for animals, plants, insects and microorganisms. This information shall be provided only when the substance is significantly different in these stages (e.g. foetal bovine serum)",
    )

    fractionDescription: ListType[
        fhirtypes.SubstanceSourceMaterialFractionDescriptionType
    ] = Field(
        None,
        alias="fractionDescription",
        title="List of `SubstanceSourceMaterialFractionDescription` items (represented as `dict` in JSON)",
        description="Many complex materials are fractions of parts of plants, animals, or minerals. Fraction elements are often necessary to define both Substances and Specified Group 1 Substances. For substances derived from Plants, fraction information will be captured at the Substance information level ( . Oils, Juices and Exudates). Additional information for Extracts, such as extraction solvent composition, will be captured at the Specified Substance Group 1 information level. For plasma-derived products fraction information will be captured at the Substance and the Specified Substance Group 1 levels",
    )

    geographicalLocation: ListType[fhirtypes.String] = Field(
        None,
        alias="geographicalLocation",
        title="List of `String` items (represented as `dict` in JSON)",
        description="The place/region where the plant is harvested or the places/regions where the animal source material has its habitat",
    )

    organism: fhirtypes.SubstanceSourceMaterialOrganismType = Field(
        None,
        alias="organism",
        title="Type `SubstanceSourceMaterialOrganism` (represented as `dict` in JSON)",
        description="This subclause describes the organism which the substance is derived from. For vaccines, the parent organism shall be specified based on these subclause elements. As an example, full taxonomy will be described for the Substance Name: ., Leaf",
    )

    organismId: fhirtypes.IdentifierType = Field(
        None,
        alias="organismId",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="The unique identifier associated with the source material parent organism shall be specified",
    )

    organismName: fhirtypes.String = Field(
        None,
        alias="organismName",
        title="Type `String` (represented as `dict` in JSON)",
        description="The organism accepted Scientific name shall be provided based on the organism taxonomy",
    )

    parentSubstanceId: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="parentSubstanceId",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="The parent of the herbal drug Ginkgo biloba, Leaf is the substance ID of the substance (fresh) of Ginkgo biloba L. or Ginkgo biloba L. (Whole plant)",
    )

    parentSubstanceName: ListType[fhirtypes.String] = Field(
        None,
        alias="parentSubstanceName",
        title="List of `String` items (represented as `dict` in JSON)",
        description="The parent substance of the Herbal Drug, or Herbal preparation",
    )

    partDescription: ListType[
        fhirtypes.SubstanceSourceMaterialPartDescriptionType
    ] = Field(
        None,
        alias="partDescription",
        title="List of `SubstanceSourceMaterialPartDescription` items (represented as `dict` in JSON)",
        description="To do",
    )

    sourceMaterialClass: fhirtypes.CodeableConceptType = Field(
        None,
        alias="sourceMaterialClass",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="General high level classification of the source material specific to the origin of the material",
    )

    sourceMaterialState: fhirtypes.CodeableConceptType = Field(
        None,
        alias="sourceMaterialState",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The state of the source material when extracted",
    )

    sourceMaterialType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="sourceMaterialType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The type of the source material shall be specified based on a controlled vocabulary. For vaccines, this subclause refers to the class of infectious agent",
    )


class SubstanceSourceMaterialFractionDescription(backboneelement.BackboneElement):
    """ Many complex materials are fractions of parts of plants, animals, or
    minerals. Fraction elements are often necessary to define both Substances
    and Specified Group 1 Substances. For substances derived from Plants,
    fraction information will be captured at the Substance information level (
    . Oils, Juices and Exudates). Additional information for Extracts, such as
    extraction solvent composition, will be captured at the Specified Substance
    Group 1 information level. For plasma-derived products fraction information
    will be captured at the Substance and the Specified Substance Group 1
    levels.
    """

    resource_type = Field("SubstanceSourceMaterialFractionDescription", const=True)

    fraction: fhirtypes.String = Field(
        None,
        alias="fraction",
        title="Type `String` (represented as `dict` in JSON)",
        description="This element is capturing information about the fraction of a plant part, or human plasma for fractionation",
    )

    materialType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="materialType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The specific type of the material constituting the component. For Herbal preparations the particulars of the extracts (liquid/dry) is described in Specified Substance Group 1",
    )


class SubstanceSourceMaterialOrganism(backboneelement.BackboneElement):
    """ This subclause describes the organism which the substance is derived from.
    For vaccines, the parent organism shall be specified based on these
    subclause elements. As an example, full taxonomy will be described for the
    Substance Name: ., Leaf.
    """

    resource_type = Field("SubstanceSourceMaterialOrganism", const=True)

    author: ListType[fhirtypes.SubstanceSourceMaterialOrganismAuthorType] = Field(
        None,
        alias="author",
        title="List of `SubstanceSourceMaterialOrganismAuthor` items (represented as `dict` in JSON)",
        description="4.9.13.6.1 Author type (Conditional)",
    )

    family: fhirtypes.CodeableConceptType = Field(
        None,
        alias="family",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The family of an organism shall be specified",
    )

    genus: fhirtypes.CodeableConceptType = Field(
        None,
        alias="genus",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The genus of an organism shall be specified; refers to the Latin epithet of the genus element of the plant/animal scientific name; it is present in names for genera, species and infraspecies",
    )

    hybrid: fhirtypes.SubstanceSourceMaterialOrganismHybridType = Field(
        None,
        alias="hybrid",
        title="Type `SubstanceSourceMaterialOrganismHybrid` (represented as `dict` in JSON)",
        description="4.9.13.8.1 Hybrid species maternal organism ID (Optional)",
    )

    intraspecificDescription: fhirtypes.String = Field(
        None,
        alias="intraspecificDescription",
        title="Type `String` (represented as `dict` in JSON)",
        description="The intraspecific description of an organism shall be specified based on a controlled vocabulary. For Influenza Vaccine, the intraspecific description shall contain the syntax of the antigen in line with the WHO convention",
    )

    intraspecificType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="intraspecificType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The Intraspecific type of an organism shall be specified",
    )

    organismGeneral: fhirtypes.SubstanceSourceMaterialOrganismOrganismGeneralType = Field(
        None,
        alias="organismGeneral",
        title="Type `SubstanceSourceMaterialOrganismOrganismGeneral` (represented as `dict` in JSON)",
        description="4.9.13.7.1 Kingdom (Conditional)",
    )

    species: fhirtypes.CodeableConceptType = Field(
        None,
        alias="species",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The species of an organism shall be specified; refers to the Latin epithet of the species of the plant/animal; it is present in names for species and infraspecies",
    )


class SubstanceSourceMaterialOrganismAuthor(backboneelement.BackboneElement):
    """ 4.9.13.6.1 Author type (Conditional).
    """

    resource_type = Field("SubstanceSourceMaterialOrganismAuthor", const=True)

    authorDescription: fhirtypes.String = Field(
        None,
        alias="authorDescription",
        title="Type `String` (represented as `dict` in JSON)",
        description="The author of an organism species shall be specified. The author year of an organism shall also be specified when applicable; refers to the year in which the first author(s) published the infraspecific plant/animal name (of any rank)",
    )

    authorType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="authorType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The type of author of an organism species shall be specified. The parenthetical author of an organism species refers to the first author who published the plant/animal name (of any rank). The primary author of an organism species refers to the first author(s), who validly published the plant/animal name",
    )


class SubstanceSourceMaterialOrganismHybrid(backboneelement.BackboneElement):
    """ 4.9.13.8.1 Hybrid species maternal organism ID (Optional).
    """

    resource_type = Field("SubstanceSourceMaterialOrganismHybrid", const=True)

    hybridType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="hybridType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The hybrid type of an organism shall be specified",
    )

    maternalOrganismId: fhirtypes.String = Field(
        None,
        alias="maternalOrganismId",
        title="Type `String` (represented as `dict` in JSON)",
        description="The identifier of the maternal species constituting the hybrid organism shall be specified based on a controlled vocabulary. For plants, the parents aren\u2019t always known, and it is unlikely that it will be known which is maternal and which is paternal",
    )

    maternalOrganismName: fhirtypes.String = Field(
        None,
        alias="maternalOrganismName",
        title="Type `String` (represented as `dict` in JSON)",
        description="The name of the maternal species constituting the hybrid organism shall be specified. For plants, the parents aren\u2019t always known, and it is unlikely that it will be known which is maternal and which is paternal",
    )

    paternalOrganismId: fhirtypes.String = Field(
        None,
        alias="paternalOrganismId",
        title="Type `String` (represented as `dict` in JSON)",
        description="The identifier of the paternal species constituting the hybrid organism shall be specified based on a controlled vocabulary",
    )

    paternalOrganismName: fhirtypes.String = Field(
        None,
        alias="paternalOrganismName",
        title="Type `String` (represented as `dict` in JSON)",
        description="The name of the paternal species constituting the hybrid organism shall be specified",
    )


class SubstanceSourceMaterialOrganismOrganismGeneral(backboneelement.BackboneElement):
    """ 4.9.13.7.1 Kingdom (Conditional).
    """

    resource_type = Field("SubstanceSourceMaterialOrganismOrganismGeneral", const=True)

    class_fhir: fhirtypes.CodeableConceptType = Field(
        None,
        alias="class",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The class of an organism shall be specified",
    )

    kingdom: fhirtypes.CodeableConceptType = Field(
        None,
        alias="kingdom",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The kingdom of an organism shall be specified",
    )

    order: fhirtypes.CodeableConceptType = Field(
        None,
        alias="order",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The order of an organism shall be specified,",
    )

    phylum: fhirtypes.CodeableConceptType = Field(
        None,
        alias="phylum",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The phylum of an organism shall be specified",
    )


class SubstanceSourceMaterialPartDescription(backboneelement.BackboneElement):
    """ To do.
    """

    resource_type = Field("SubstanceSourceMaterialPartDescription", const=True)

    part: fhirtypes.CodeableConceptType = Field(
        None,
        alias="part",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Entity of anatomical origin of source material within an organism",
    )

    partLocation: fhirtypes.CodeableConceptType = Field(
        None,
        alias="partLocation",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The detailed anatomic location when the part can be extracted from different anatomical locations of the organism. Multiple alternative locations may apply",
    )
