# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MolecularSequence
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class MolecularSequence(domainresource.DomainResource):
    """ Information about a biological sequence.
    Raw data describing a biological sequence.
    """

    resource_type = Field("MolecularSequence", const=True)

    coordinateSystem: fhirtypes.Integer = Field(
        ...,
        alias="coordinateSystem",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Base number of coordinate system (0 for 0-based numbering or coordinates, inclusive start, exclusive end, 1 for 1-based numbering, inclusive start, inclusive end)",
    )

    device: fhirtypes.ReferenceType = Field(
        None,
        alias="device",
        title="Type `Reference` referencing `Device` (represented as `dict` in JSON)",
        description="The method for sequencing",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Unique ID for this particular sequence. This is a FHIR-defined id",
    )

    observedSeq: fhirtypes.String = Field(
        None,
        alias="observedSeq",
        title="Type `String` (represented as `dict` in JSON)",
        description="Sequence that was observed",
    )

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="Who and/or what this is about",
    )

    performer: fhirtypes.ReferenceType = Field(
        None,
        alias="performer",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Who should be responsible for test result",
    )

    pointer: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="pointer",
        title="List of `Reference` items referencing `MolecularSequence` (represented as `dict` in JSON)",
        description="Pointer to next atomic sequence",
    )

    quality: ListType[fhirtypes.MolecularSequenceQualityType] = Field(
        None,
        alias="quality",
        title="List of `MolecularSequenceQuality` items (represented as `dict` in JSON)",
        description="An set of value as quality of sequence",
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="The number of copies of the sequence of interest.  (RNASeq)",
    )

    readCoverage: fhirtypes.Integer = Field(
        None,
        alias="readCoverage",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Average number of reads representing a given nucleotide in the reconstructed sequence",
    )

    referenceSeq: fhirtypes.MolecularSequenceReferenceSeqType = Field(
        None,
        alias="referenceSeq",
        title="Type `MolecularSequenceReferenceSeq` (represented as `dict` in JSON)",
        description="A sequence used as reference",
    )

    repository: ListType[fhirtypes.MolecularSequenceRepositoryType] = Field(
        None,
        alias="repository",
        title="List of `MolecularSequenceRepository` items (represented as `dict` in JSON)",
        description="External repository which contains detailed report related with observedSeq in this resource",
    )

    specimen: fhirtypes.ReferenceType = Field(
        None,
        alias="specimen",
        title="Type `Reference` referencing `Specimen` (represented as `dict` in JSON)",
        description="Specimen used for sequencing",
    )

    structureVariant: ListType[fhirtypes.MolecularSequenceStructureVariantType] = Field(
        None,
        alias="structureVariant",
        title="List of `MolecularSequenceStructureVariant` items (represented as `dict` in JSON)",
        description="Structural variant",
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="aa | dna | rna",
    )

    variant: ListType[fhirtypes.MolecularSequenceVariantType] = Field(
        None,
        alias="variant",
        title="List of `MolecularSequenceVariant` items (represented as `dict` in JSON)",
        description="Variant in sequence",
    )


class MolecularSequenceQuality(backboneelement.BackboneElement):
    """ An set of value as quality of sequence.
    An experimental feature attribute that defines the quality of the feature
    in a quantitative way, such as a phred quality score ([SO:0001686](http://w
    ww.sequenceontology.org/browser/current_svn/term/SO:0001686)).
    """

    resource_type = Field("MolecularSequenceQuality", const=True)

    end: fhirtypes.Integer = Field(
        None,
        alias="end",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="End position of the sequence",
    )

    fScore: fhirtypes.Decimal = Field(
        None,
        alias="fScore",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="F-score",
    )

    gtFP: fhirtypes.Decimal = Field(
        None,
        alias="gtFP",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="False positives where the non-REF alleles in the Truth and Query Call Sets match",
    )

    method: fhirtypes.CodeableConceptType = Field(
        None,
        alias="method",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Method to get quality",
    )

    precision: fhirtypes.Decimal = Field(
        None,
        alias="precision",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Precision of comparison",
    )

    queryFP: fhirtypes.Decimal = Field(
        None,
        alias="queryFP",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="False positives",
    )

    queryTP: fhirtypes.Decimal = Field(
        None,
        alias="queryTP",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="True positives from the perspective of the query data",
    )

    recall: fhirtypes.Decimal = Field(
        None,
        alias="recall",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Recall of comparison",
    )

    roc: fhirtypes.MolecularSequenceQualityRocType = Field(
        None,
        alias="roc",
        title="Type `MolecularSequenceQualityRoc` (represented as `dict` in JSON)",
        description="Receiver Operator Characteristic (ROC) Curve",
    )

    score: fhirtypes.QuantityType = Field(
        None,
        alias="score",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Quality score for the comparison",
    )

    standardSequence: fhirtypes.CodeableConceptType = Field(
        None,
        alias="standardSequence",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Standard sequence for comparison",
    )

    start: fhirtypes.Integer = Field(
        None,
        alias="start",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Start position of the sequence",
    )

    truthFN: fhirtypes.Decimal = Field(
        None,
        alias="truthFN",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="False negatives",
    )

    truthTP: fhirtypes.Decimal = Field(
        None,
        alias="truthTP",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="True positives from the perspective of the truth data",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="indel | snp | unknown",
    )


class MolecularSequenceQualityRoc(backboneelement.BackboneElement):
    """ Receiver Operator Characteristic (ROC) Curve.
    Receiver Operator Characteristic (ROC) Curve  to give
    sensitivity/specificity tradeoff.
    """

    resource_type = Field("MolecularSequenceQualityRoc", const=True)

    fMeasure: ListType[fhirtypes.Decimal] = Field(
        None,
        alias="fMeasure",
        title="List of `Decimal` items (represented as `dict` in JSON)",
        description="FScore of the GQ score",
    )

    numFN: ListType[fhirtypes.Integer] = Field(
        None,
        alias="numFN",
        title="List of `Integer` items (represented as `dict` in JSON)",
        description="Roc score false negative numbers",
    )

    numFP: ListType[fhirtypes.Integer] = Field(
        None,
        alias="numFP",
        title="List of `Integer` items (represented as `dict` in JSON)",
        description="Roc score false positive numbers",
    )

    numTP: ListType[fhirtypes.Integer] = Field(
        None,
        alias="numTP",
        title="List of `Integer` items (represented as `dict` in JSON)",
        description="Roc score true positive numbers",
    )

    precision: ListType[fhirtypes.Decimal] = Field(
        None,
        alias="precision",
        title="List of `Decimal` items (represented as `dict` in JSON)",
        description="Precision of the GQ score",
    )

    score: ListType[fhirtypes.Integer] = Field(
        None,
        alias="score",
        title="List of `Integer` items (represented as `dict` in JSON)",
        description="Genotype quality score",
    )

    sensitivity: ListType[fhirtypes.Decimal] = Field(
        None,
        alias="sensitivity",
        title="List of `Decimal` items (represented as `dict` in JSON)",
        description="Sensitivity of the GQ score",
    )


class MolecularSequenceReferenceSeq(backboneelement.BackboneElement):
    """ A sequence used as reference.
    A sequence that is used as a reference to describe variants that are
    present in a sequence analyzed.
    """

    resource_type = Field("MolecularSequenceReferenceSeq", const=True)

    chromosome: fhirtypes.CodeableConceptType = Field(
        None,
        alias="chromosome",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Chromosome containing genetic finding",
    )

    genomeBuild: fhirtypes.String = Field(
        None,
        alias="genomeBuild",
        title="Type `String` (represented as `dict` in JSON)",
        description="The Genome Build used for reference, following GRCh build versions e.g. \u0027GRCh 37\u0027",
    )

    orientation: fhirtypes.Code = Field(
        None,
        alias="orientation",
        title="Type `Code` (represented as `dict` in JSON)",
        description="sense | antisense",
    )

    referenceSeqId: fhirtypes.CodeableConceptType = Field(
        None,
        alias="referenceSeqId",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Reference identifier",
    )

    referenceSeqPointer: fhirtypes.ReferenceType = Field(
        None,
        alias="referenceSeqPointer",
        title="Type `Reference` referencing `MolecularSequence` (represented as `dict` in JSON)",
        description="A pointer to another MolecularSequence entity as reference sequence",
    )

    referenceSeqString: fhirtypes.String = Field(
        None,
        alias="referenceSeqString",
        title="Type `String` (represented as `dict` in JSON)",
        description="A string to represent reference sequence",
    )

    strand: fhirtypes.Code = Field(
        None,
        alias="strand",
        title="Type `Code` (represented as `dict` in JSON)",
        description="watson | crick",
    )

    windowEnd: fhirtypes.Integer = Field(
        None,
        alias="windowEnd",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="End position of the window on the reference sequence",
    )

    windowStart: fhirtypes.Integer = Field(
        None,
        alias="windowStart",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Start position of the window on the  reference sequence",
    )


class MolecularSequenceRepository(backboneelement.BackboneElement):
    """ External repository which contains detailed report related with observedSeq
    in this resource.
    Configurations of the external repository. The repository shall store
    target's observedSeq or records related with target's observedSeq.
    """

    resource_type = Field("MolecularSequenceRepository", const=True)

    datasetId: fhirtypes.String = Field(
        None,
        alias="datasetId",
        title="Type `String` (represented as `dict` in JSON)",
        description="Id of the dataset that used to call for dataset in repository",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Repository\u0027s name",
    )

    readsetId: fhirtypes.String = Field(
        None,
        alias="readsetId",
        title="Type `String` (represented as `dict` in JSON)",
        description="Id of the read",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="directlink | openapi | login | oauth | other",
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="URI of the repository",
    )

    variantsetId: fhirtypes.String = Field(
        None,
        alias="variantsetId",
        title="Type `String` (represented as `dict` in JSON)",
        description="Id of the variantset that used to call for variantset in repository",
    )


class MolecularSequenceStructureVariant(backboneelement.BackboneElement):
    """ Structural variant.
    Information about chromosome structure variation.
    """

    resource_type = Field("MolecularSequenceStructureVariant", const=True)

    exact: bool = Field(
        None,
        alias="exact",
        title="Type `bool`",
        description="Does the structural variant have base pair resolution breakpoints?",
    )

    inner: fhirtypes.MolecularSequenceStructureVariantInnerType = Field(
        None,
        alias="inner",
        title="Type `MolecularSequenceStructureVariantInner` (represented as `dict` in JSON)",
        description="Structural variant inner",
    )

    length: fhirtypes.Integer = Field(
        None,
        alias="length",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Structural variant length",
    )

    outer: fhirtypes.MolecularSequenceStructureVariantOuterType = Field(
        None,
        alias="outer",
        title="Type `MolecularSequenceStructureVariantOuter` (represented as `dict` in JSON)",
        description="Structural variant outer",
    )

    variantType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="variantType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Structural variant change type",
    )


class MolecularSequenceStructureVariantInner(backboneelement.BackboneElement):
    """ Structural variant inner.
    """

    resource_type = Field("MolecularSequenceStructureVariantInner", const=True)

    end: fhirtypes.Integer = Field(
        None,
        alias="end",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Structural variant inner end",
    )

    start: fhirtypes.Integer = Field(
        None,
        alias="start",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Structural variant inner start",
    )


class MolecularSequenceStructureVariantOuter(backboneelement.BackboneElement):
    """ Structural variant outer.
    """

    resource_type = Field("MolecularSequenceStructureVariantOuter", const=True)

    end: fhirtypes.Integer = Field(
        None,
        alias="end",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Structural variant outer end",
    )

    start: fhirtypes.Integer = Field(
        None,
        alias="start",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Structural variant outer start",
    )


class MolecularSequenceVariant(backboneelement.BackboneElement):
    """ Variant in sequence.
    The definition of variant here originates from Sequence ontology ([variant_
    of](http://www.sequenceontology.org/browser/current_svn/term/variant_of)).
    This element can represent amino acid or nucleic sequence change(including
    insertion,deletion,SNP,etc.)  It can represent some complex mutation or
    segment variation with the assist of CIGAR string.
    """

    resource_type = Field("MolecularSequenceVariant", const=True)

    cigar: fhirtypes.String = Field(
        None,
        alias="cigar",
        title="Type `String` (represented as `dict` in JSON)",
        description="Extended CIGAR string for aligning the sequence with reference bases",
    )

    end: fhirtypes.Integer = Field(
        None,
        alias="end",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="End position of the variant on the reference sequence",
    )

    observedAllele: fhirtypes.String = Field(
        None,
        alias="observedAllele",
        title="Type `String` (represented as `dict` in JSON)",
        description="Allele that was observed",
    )

    referenceAllele: fhirtypes.String = Field(
        None,
        alias="referenceAllele",
        title="Type `String` (represented as `dict` in JSON)",
        description="Allele in the reference sequence",
    )

    start: fhirtypes.Integer = Field(
        None,
        alias="start",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Start position of the variant on the  reference sequence",
    )

    variantPointer: fhirtypes.ReferenceType = Field(
        None,
        alias="variantPointer",
        title="Type `Reference` referencing `Observation` (represented as `dict` in JSON)",
        description="Pointer to observed variant information",
    )
