# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Sequence
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Sequence(domainresource.DomainResource):
    """ Information about a biological sequence.
    Raw data describing a biological sequence.
    """

    resource_type = Field("Sequence", const=True)

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
        title="List of `Reference` items referencing `Sequence` (represented as `dict` in JSON)",
        description="Pointer to next atomic sequence",
    )

    quality: ListType[fhirtypes.SequenceQualityType] = Field(
        None,
        alias="quality",
        title="List of `SequenceQuality` items (represented as `dict` in JSON)",
        description="An set of value as quality of sequence",
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="The number of copies of the seqeunce of interest.  (RNASeq)",
    )

    readCoverage: fhirtypes.Integer = Field(
        None,
        alias="readCoverage",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Average number of reads representing a given nucleotide in the reconstructed sequence",
    )

    referenceSeq: fhirtypes.SequenceReferenceSeqType = Field(
        None,
        alias="referenceSeq",
        title="Type `SequenceReferenceSeq` (represented as `dict` in JSON)",
        description="A sequence used as reference",
    )

    repository: ListType[fhirtypes.SequenceRepositoryType] = Field(
        None,
        alias="repository",
        title="List of `SequenceRepository` items (represented as `dict` in JSON)",
        description="External repository which contains detailed report related with observedSeq in this resource",
    )

    specimen: fhirtypes.ReferenceType = Field(
        None,
        alias="specimen",
        title="Type `Reference` referencing `Specimen` (represented as `dict` in JSON)",
        description="Specimen used for sequencing",
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="aa | dna | rna",
    )

    variant: ListType[fhirtypes.SequenceVariantType] = Field(
        None,
        alias="variant",
        title="List of `SequenceVariant` items (represented as `dict` in JSON)",
        description="Variant in sequence",
    )


class SequenceQuality(backboneelement.BackboneElement):
    """ An set of value as quality of sequence.
    An experimental feature attribute that defines the quality of the feature
    in a quantitative way, such as a phred quality score ([SO:0001686](http://w
    ww.sequenceontology.org/browser/current_svn/term/SO:0001686)).
    """

    resource_type = Field("SequenceQuality", const=True)

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


class SequenceReferenceSeq(backboneelement.BackboneElement):
    """ A sequence used as reference.
    A sequence that is used as a reference to describe variants that are
    present in a sequence analyzed.
    """

    resource_type = Field("SequenceReferenceSeq", const=True)

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

    referenceSeqId: fhirtypes.CodeableConceptType = Field(
        None,
        alias="referenceSeqId",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Reference identifier",
    )

    referenceSeqPointer: fhirtypes.ReferenceType = Field(
        None,
        alias="referenceSeqPointer",
        title="Type `Reference` referencing `Sequence` (represented as `dict` in JSON)",
        description="A Pointer to another Sequence entity as reference sequence",
    )

    referenceSeqString: fhirtypes.String = Field(
        None,
        alias="referenceSeqString",
        title="Type `String` (represented as `dict` in JSON)",
        description="A string to represent reference sequence",
    )

    strand: fhirtypes.Integer = Field(
        None,
        alias="strand",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Directionality of DNA ( +1/-1)",
    )

    windowEnd: fhirtypes.Integer = Field(
        ...,
        alias="windowEnd",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="End position of the window on the reference sequence",
    )

    windowStart: fhirtypes.Integer = Field(
        ...,
        alias="windowStart",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Start position of the window on the  reference sequence",
    )


class SequenceRepository(backboneelement.BackboneElement):
    """ External repository which contains detailed report related with observedSeq
    in this resource.
    Configurations of the external repository. The repository shall store
    target's observedSeq or records related with target's observedSeq.
    """

    resource_type = Field("SequenceRepository", const=True)

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


class SequenceVariant(backboneelement.BackboneElement):
    """ Variant in sequence.
    The definition of variant here originates from Sequence ontology ([variant_
    of](http://www.sequenceontology.org/browser/current_svn/term/variant_of)).
    This element can represent amino acid or nucleic sequence change(including
    insertion,deletion,SNP,etc.)  It can represent some complex mutation or
    segment variation with the assist of CIGAR string.
    """

    resource_type = Field("SequenceVariant", const=True)

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
