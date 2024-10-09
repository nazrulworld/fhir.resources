from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/SubstanceSourceMaterial
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class SubstanceSourceMaterial(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Source material shall capture information on the taxonomic and anatomical
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

    __resource_type__ = "SubstanceSourceMaterial"

    countryOfOrigin: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="countryOfOrigin",
        title=(
            "The country where the plant material is harvested or the countries "
            "where the plasma is sourced from as laid down in accordance with the "
            "Plasma Master File. For \u201cPlasma-derived substances\u201d the attribute "
            "country of origin provides information about the countries used for "
            "the manufacturing of the Cryopoor plama or Crioprecipitate"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    developmentStage: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="developmentStage",
        title=(
            "Stage of life for animals, plants, insects and microorganisms. This "
            "information shall be provided only when the substance is significantly"
            " different in these stages (e.g. foetal bovine serum)"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    fractionDescription: typing.List[fhirtypes.SubstanceSourceMaterialFractionDescriptionType] | None = Field(  # type: ignore
        None,
        alias="fractionDescription",
        title=(
            "Many complex materials are fractions of parts of plants, animals, or "
            "minerals. Fraction elements are often necessary to define both "
            "Substances and Specified Group 1 Substances. For substances derived "
            "from Plants, fraction information will be captured at the Substance "
            "information level ( . Oils, Juices and Exudates). Additional "
            "information for Extracts, such as extraction solvent composition, will"
            " be captured at the Specified Substance Group 1 information level. For"
            " plasma-derived products fraction information will be captured at the "
            "Substance and the Specified Substance Group 1 levels"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    geographicalLocation: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="geographicalLocation",
        title=(
            "The place/region where the plant is harvested or the places/regions "
            "where the animal source material has its habitat"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    geographicalLocation__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_geographicalLocation",
        title="Extension field for ``geographicalLocation``.",
    )

    organism: fhirtypes.SubstanceSourceMaterialOrganismType | None = Field(  # type: ignore
        None,
        alias="organism",
        title=(
            "This subclause describes the organism which the substance is derived "
            "from. For vaccines, the parent organism shall be specified based on "
            "these subclause elements. As an example, full taxonomy will be "
            "described for the Substance Name: ., Leaf"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    organismId: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="organismId",
        title=(
            "The unique identifier associated with the source material parent "
            "organism shall be specified"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    organismName: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="organismName",
        title=(
            "The organism accepted Scientific name shall be provided based on the "
            "organism taxonomy"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    organismName__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_organismName", title="Extension field for ``organismName``."
    )

    parentSubstanceId: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="parentSubstanceId",
        title=(
            "The parent of the herbal drug Ginkgo biloba, Leaf is the substance ID "
            "of the substance (fresh) of Ginkgo biloba L. or Ginkgo biloba L. "
            "(Whole plant)"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    parentSubstanceName: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="parentSubstanceName",
        title="The parent substance of the Herbal Drug, or Herbal preparation",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    parentSubstanceName__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_parentSubstanceName",
        title="Extension field for ``parentSubstanceName``.",
    )

    partDescription: typing.List[fhirtypes.SubstanceSourceMaterialPartDescriptionType] | None = Field(  # type: ignore
        None,
        alias="partDescription",
        title="To do",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    sourceMaterialClass: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="sourceMaterialClass",
        title=(
            "General high level classification of the source material specific to "
            "the origin of the material"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    sourceMaterialState: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="sourceMaterialState",
        title="The state of the source material when extracted",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    sourceMaterialType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="sourceMaterialType",
        title=(
            "The type of the source material shall be specified based on a "
            "controlled vocabulary. For vaccines, this subclause refers to the "
            "class of infectious agent"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceSourceMaterial`` according specification,
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
            "sourceMaterialClass",
            "sourceMaterialType",
            "sourceMaterialState",
            "organismId",
            "organismName",
            "parentSubstanceId",
            "parentSubstanceName",
            "countryOfOrigin",
            "geographicalLocation",
            "developmentStage",
            "fractionDescription",
            "organism",
            "partDescription",
        ]


class SubstanceSourceMaterialFractionDescription(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Many complex materials are fractions of parts of plants, animals, or
    minerals. Fraction elements are often necessary to define both Substances
    and Specified Group 1 Substances. For substances derived from Plants,
    fraction information will be captured at the Substance information level (
    . Oils, Juices and Exudates). Additional information for Extracts, such as
    extraction solvent composition, will be captured at the Specified Substance
    Group 1 information level. For plasma-derived products fraction information
    will be captured at the Substance and the Specified Substance Group 1
    levels.
    """

    __resource_type__ = "SubstanceSourceMaterialFractionDescription"

    fraction: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="fraction",
        title=(
            "This element is capturing information about the fraction of a plant "
            "part, or human plasma for fractionation"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    fraction__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_fraction", title="Extension field for ``fraction``."
    )

    materialType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="materialType",
        title=(
            "The specific type of the material constituting the component. For "
            "Herbal preparations the particulars of the extracts (liquid/dry) is "
            "described in Specified Substance Group 1"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceSourceMaterialFractionDescription`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "fraction", "materialType"]


class SubstanceSourceMaterialOrganism(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    This subclause describes the organism which the substance is derived from.
    For vaccines, the parent organism shall be specified based on these
    subclause elements. As an example, full taxonomy will be described for the
    Substance Name: ., Leaf.
    """

    __resource_type__ = "SubstanceSourceMaterialOrganism"

    author: typing.List[fhirtypes.SubstanceSourceMaterialOrganismAuthorType] | None = Field(  # type: ignore
        None,
        alias="author",
        title="4.9.13.6.1 Author type (Conditional)",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    family: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="family",
        title="The family of an organism shall be specified",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    genus: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="genus",
        title=(
            "The genus of an organism shall be specified; refers to the Latin "
            "epithet of the genus element of the plant/animal scientific name; it "
            "is present in names for genera, species and infraspecies"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    hybrid: fhirtypes.SubstanceSourceMaterialOrganismHybridType | None = Field(  # type: ignore
        None,
        alias="hybrid",
        title="4.9.13.8.1 Hybrid species maternal organism ID (Optional)",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    intraspecificDescription: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="intraspecificDescription",
        title=(
            "The intraspecific description of an organism shall be specified based "
            "on a controlled vocabulary. For Influenza Vaccine, the intraspecific "
            "description shall contain the syntax of the antigen in line with the "
            "WHO convention"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    intraspecificDescription__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_intraspecificDescription",
        title="Extension field for ``intraspecificDescription``.",
    )

    intraspecificType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="intraspecificType",
        title="The Intraspecific type of an organism shall be specified",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    organismGeneral: fhirtypes.SubstanceSourceMaterialOrganismOrganismGeneralType | None = Field(  # type: ignore
        None,
        alias="organismGeneral",
        title="4.9.13.7.1 Kingdom (Conditional)",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    species: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="species",
        title=(
            "The species of an organism shall be specified; refers to the Latin "
            "epithet of the species of the plant/animal; it is present in names for"
            " species and infraspecies"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceSourceMaterialOrganism`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "family",
            "genus",
            "species",
            "intraspecificType",
            "intraspecificDescription",
            "author",
            "hybrid",
            "organismGeneral",
        ]


class SubstanceSourceMaterialOrganismAuthor(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    4.9.13.6.1 Author type (Conditional).
    """

    __resource_type__ = "SubstanceSourceMaterialOrganismAuthor"

    authorDescription: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="authorDescription",
        title=(
            "The author of an organism species shall be specified. The author year "
            "of an organism shall also be specified when applicable; refers to the "
            "year in which the first author(s) published the infraspecific "
            "plant/animal name (of any rank)"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    authorDescription__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_authorDescription",
        title="Extension field for ``authorDescription``.",
    )

    authorType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="authorType",
        title=(
            "The type of author of an organism species shall be specified. The "
            "parenthetical author of an organism species refers to the first author"
            " who published the plant/animal name (of any rank). The primary author"
            " of an organism species refers to the first author(s), who validly "
            "published the plant/animal name"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceSourceMaterialOrganismAuthor`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "authorType",
            "authorDescription",
        ]


class SubstanceSourceMaterialOrganismHybrid(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    4.9.13.8.1 Hybrid species maternal organism ID (Optional).
    """

    __resource_type__ = "SubstanceSourceMaterialOrganismHybrid"

    hybridType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="hybridType",
        title="The hybrid type of an organism shall be specified",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    maternalOrganismId: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="maternalOrganismId",
        title=(
            "The identifier of the maternal species constituting the hybrid "
            "organism shall be specified based on a controlled vocabulary. For "
            "plants, the parents aren\u2019t always known, and it is unlikely that it "
            "will be known which is maternal and which is paternal"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    maternalOrganismId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_maternalOrganismId",
        title="Extension field for ``maternalOrganismId``.",
    )

    maternalOrganismName: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="maternalOrganismName",
        title=(
            "The name of the maternal species constituting the hybrid organism "
            "shall be specified. For plants, the parents aren\u2019t always known, and "
            "it is unlikely that it will be known which is maternal and which is "
            "paternal"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    maternalOrganismName__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_maternalOrganismName",
        title="Extension field for ``maternalOrganismName``.",
    )

    paternalOrganismId: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="paternalOrganismId",
        title=(
            "The identifier of the paternal species constituting the hybrid "
            "organism shall be specified based on a controlled vocabulary"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    paternalOrganismId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_paternalOrganismId",
        title="Extension field for ``paternalOrganismId``.",
    )

    paternalOrganismName: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="paternalOrganismName",
        title=(
            "The name of the paternal species constituting the hybrid organism "
            "shall be specified"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    paternalOrganismName__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_paternalOrganismName",
        title="Extension field for ``paternalOrganismName``.",
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceSourceMaterialOrganismHybrid`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "maternalOrganismId",
            "maternalOrganismName",
            "paternalOrganismId",
            "paternalOrganismName",
            "hybridType",
        ]


class SubstanceSourceMaterialOrganismOrganismGeneral(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    4.9.13.7.1 Kingdom (Conditional).
    """

    __resource_type__ = "SubstanceSourceMaterialOrganismOrganismGeneral"

    class_fhir: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="class",
        title="The class of an organism shall be specified",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    kingdom: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="kingdom",
        title="The kingdom of an organism shall be specified",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    order: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="order",
        title="The order of an organism shall be specified,",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    phylum: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="phylum",
        title="The phylum of an organism shall be specified",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceSourceMaterialOrganismOrganismGeneral`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "kingdom",
            "phylum",
            "class",
            "order",
        ]


class SubstanceSourceMaterialPartDescription(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    To do.
    """

    __resource_type__ = "SubstanceSourceMaterialPartDescription"

    part: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="part",
        title="Entity of anatomical origin of source material within an organism",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    partLocation: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="partLocation",
        title=(
            "The detailed anatomic location when the part can be extracted from "
            "different anatomical locations of the organism. Multiple alternative "
            "locations may apply"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceSourceMaterialPartDescription`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "part", "partLocation"]
