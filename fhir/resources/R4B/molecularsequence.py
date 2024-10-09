from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/MolecularSequence
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class MolecularSequence(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about a biological sequence.
    Raw data describing a biological sequence.
    """

    __resource_type__ = "MolecularSequence"

    coordinateSystem: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="coordinateSystem",
        title=(
            "Base number of coordinate system (0 for 0-based numbering or "
            "coordinates, inclusive start, exclusive end, 1 for 1-based numbering, "
            "inclusive start, inclusive end)"
        ),
        description=(
            "Whether the sequence is numbered starting at 0 (0-based numbering or "
            "coordinates, inclusive start, exclusive end) or starting at 1 (1-based"
            " numbering, inclusive start and inclusive end)."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    coordinateSystem__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_coordinateSystem",
        title="Extension field for ``coordinateSystem``.",
    )

    device: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="device",
        title="The method for sequencing",
        description="The method for sequencing, for example, chip information.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Device"],
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Unique ID for this particular sequence. This is a FHIR-defined id",
        description=(
            "A unique identifier for this particular sequence instance. This is a "
            "FHIR-defined id."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    observedSeq: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="observedSeq",
        title="Sequence that was observed",
        description=(
            "Sequence that was observed. It is the result marked by referenceSeq "
            "along with variant records on referenceSeq. This shall start from "
            "referenceSeq.windowStart and end by referenceSeq.windowEnd."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    observedSeq__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_observedSeq", title="Extension field for ``observedSeq``."
    )

    patient: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="patient",
        title="Who and/or what this is about",
        description="The patient whose sequencing results are described by this resource.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient"],
        },
    )

    performer: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="performer",
        title="Who should be responsible for test result",
        description="The organization or lab that should be responsible for this result.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    pointer: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="pointer",
        title="Pointer to next atomic sequence",
        description="Pointer to next atomic sequence which at most contains one variant.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["MolecularSequence"],
        },
    )

    quality: typing.List[fhirtypes.MolecularSequenceQualityType] | None = Field(  # type: ignore
        None,
        alias="quality",
        title="An set of value as quality of sequence",
        description=(
            "An experimental feature attribute that defines the quality of the "
            "feature in a quantitative way, such as a phred quality score ([SO:0001"
            "686](http://www.sequenceontology.org/browser/current_svn/term/SO:00016"
            "86))."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="The number of copies of the sequence of interest.  (RNASeq)",
        description="The number of copies of the sequence of interest. (RNASeq).",
        json_schema_extra={
            "element_property": True,
        },
    )

    readCoverage: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="readCoverage",
        title=(
            "Average number of reads representing a given nucleotide in the "
            "reconstructed sequence"
        ),
        description=(
            "Coverage (read depth or depth) is the average number of reads "
            "representing a given nucleotide in the reconstructed sequence."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    readCoverage__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_readCoverage", title="Extension field for ``readCoverage``."
    )

    referenceSeq: fhirtypes.MolecularSequenceReferenceSeqType | None = Field(  # type: ignore
        None,
        alias="referenceSeq",
        title="A sequence used as reference",
        description=(
            "A sequence that is used as a reference to describe variants that are "
            "present in a sequence analyzed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    repository: typing.List[fhirtypes.MolecularSequenceRepositoryType] | None = Field(  # type: ignore
        None,
        alias="repository",
        title=(
            "External repository which contains detailed report related with "
            "observedSeq in this resource"
        ),
        description=(
            "Configurations of the external repository. The repository shall store "
            "target's observedSeq or records related with target's observedSeq."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    specimen: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="specimen",
        title="Specimen used for sequencing",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Specimen"],
        },
    )

    structureVariant: typing.List[fhirtypes.MolecularSequenceStructureVariantType] | None = Field(  # type: ignore
        None,
        alias="structureVariant",
        title="Structural variant",
        description="Information about chromosome structure variation.",
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="aa | dna | rna",
        description="Amino Acid Sequence/ DNA Sequence / RNA Sequence.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["aa", "dna", "rna"],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    variant: typing.List[fhirtypes.MolecularSequenceVariantType] | None = Field(  # type: ignore
        None,
        alias="variant",
        title="Variant in sequence",
        description=(
            "The definition of variant here originates from Sequence ontology ([var"
            "iant_of](http://www.sequenceontology.org/browser/current_svn/term/vari"
            "ant_of)). This element can represent amino acid or nucleic sequence "
            "change(including insertion,deletion,SNP,etc.)  It can represent some "
            "complex mutation or segment variation with the assist of CIGAR string."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequence`` according specification,
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
            "type",
            "coordinateSystem",
            "patient",
            "specimen",
            "device",
            "performer",
            "quantity",
            "referenceSeq",
            "variant",
            "observedSeq",
            "quality",
            "readCoverage",
            "repository",
            "pointer",
            "structureVariant",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("coordinateSystem", "coordinateSystem__ext")]
        return required_fields


class MolecularSequenceQuality(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An set of value as quality of sequence.
    An experimental feature attribute that defines the quality of the feature
    in a quantitative way, such as a phred quality score ([SO:0001686](http://w
    ww.sequenceontology.org/browser/current_svn/term/SO:0001686)).
    """

    __resource_type__ = "MolecularSequenceQuality"

    end: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="end",
        title="End position of the sequence",
        description=(
            "End position of the sequence. If the coordinate system is 0-based then"
            " end is exclusive and does not include the last position. If the "
            "coordinate system is 1-base, then end is inclusive and includes the "
            "last position."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    end__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_end", title="Extension field for ``end``."
    )

    fScore: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="fScore",
        title="F-score",
        description=(
            "Harmonic mean of Recall and Precision, computed as: 2 * precision * "
            "recall / (precision + recall)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    fScore__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_fScore", title="Extension field for ``fScore``."
    )

    gtFP: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="gtFP",
        title=(
            "False positives where the non-REF alleles in the Truth and Query Call "
            "Sets match"
        ),
        description=(
            "The number of false positives where the non-REF alleles in the Truth "
            "and Query Call Sets match (i.e. cases where the truth is 1/1 and the "
            "query is 0/1 or similar)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    gtFP__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_gtFP", title="Extension field for ``gtFP``."
    )

    method: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="method",
        title="Method to get quality",
        description="Which method is used to get sequence quality.",
        json_schema_extra={
            "element_property": True,
        },
    )

    precision: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="precision",
        title="Precision of comparison",
        description="QUERY.TP / (QUERY.TP + QUERY.FP).",
        json_schema_extra={
            "element_property": True,
        },
    )
    precision__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_precision", title="Extension field for ``precision``."
    )

    queryFP: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="queryFP",
        title="False positives",
        description=(
            "False positives, i.e. the number of sites in the Query Call Set for "
            "which there is no path through the Truth Call Set that is consistent "
            "with this site. Sites with correct variant but incorrect genotype are "
            "counted here."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    queryFP__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_queryFP", title="Extension field for ``queryFP``."
    )

    queryTP: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="queryTP",
        title="True positives from the perspective of the query data",
        description=(
            "True positives, from the perspective of the query data, i.e. the "
            "number of sites in the Query Call Set for which there are paths "
            "through the Truth Call Set that are consistent with all of the alleles"
            " at this site, and for which there is an accurate genotype call for "
            "the event."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    queryTP__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_queryTP", title="Extension field for ``queryTP``."
    )

    recall: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="recall",
        title="Recall of comparison",
        description="TRUTH.TP / (TRUTH.TP + TRUTH.FN).",
        json_schema_extra={
            "element_property": True,
        },
    )
    recall__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_recall", title="Extension field for ``recall``."
    )

    roc: fhirtypes.MolecularSequenceQualityRocType | None = Field(  # type: ignore
        None,
        alias="roc",
        title="Receiver Operator Characteristic (ROC) Curve",
        description=(
            "Receiver Operator Characteristic (ROC) Curve  to give "
            "sensitivity/specificity tradeoff."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    score: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="score",
        title="Quality score for the comparison",
        description=(
            "The score of an experimentally derived feature such as a p-value ([SO:"
            "0001685](http://www.sequenceontology.org/browser/current_svn/term/SO:0"
            "001685))."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    standardSequence: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="standardSequence",
        title="Standard sequence for comparison",
        description="Gold standard sequence used for comparing against.",
        json_schema_extra={
            "element_property": True,
        },
    )

    start: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="start",
        title="Start position of the sequence",
        description=(
            "Start position of the sequence. If the coordinate system is either "
            "0-based or 1-based, then start position is inclusive."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    start__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_start", title="Extension field for ``start``."
    )

    truthFN: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="truthFN",
        title="False negatives",
        description=(
            "False negatives, i.e. the number of sites in the Truth Call Set for "
            "which there is no path through the Query Call Set that is consistent "
            "with all of the alleles at this site, or sites for which there is an "
            "inaccurate genotype call for the event. Sites with correct variant but"
            " incorrect genotype are counted here."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    truthFN__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_truthFN", title="Extension field for ``truthFN``."
    )

    truthTP: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="truthTP",
        title="True positives from the perspective of the truth data",
        description=(
            "True positives, from the perspective of the truth data, i.e. the "
            "number of sites in the Truth Call Set for which there are paths "
            "through the Query Call Set that are consistent with all of the alleles"
            " at this site, and for which there is an accurate genotype call for "
            "the event."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    truthTP__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_truthTP", title="Extension field for ``truthTP``."
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="indel | snp | unknown",
        description="INDEL / SNP / Undefined variant.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["indel", "snp", "unknown"],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceQuality`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "standardSequence",
            "start",
            "end",
            "score",
            "method",
            "truthTP",
            "queryTP",
            "truthFN",
            "queryFP",
            "gtFP",
            "precision",
            "recall",
            "fScore",
            "roc",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("type", "type__ext")]
        return required_fields


class MolecularSequenceQualityRoc(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Receiver Operator Characteristic (ROC) Curve.
    Receiver Operator Characteristic (ROC) Curve  to give
    sensitivity/specificity tradeoff.
    """

    __resource_type__ = "MolecularSequenceQualityRoc"

    fMeasure: typing.List[fhirtypes.DecimalType | None] | None = Field(  # type: ignore
        None,
        alias="fMeasure",
        title="FScore of the GQ score",
        description=(
            'Calculated fScore if the GQ score threshold was set to "score" field '
            "value."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    fMeasure__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_fMeasure", title="Extension field for ``fMeasure``."
    )

    numFN: typing.List[fhirtypes.IntegerType | None] | None = Field(  # type: ignore
        None,
        alias="numFN",
        title="Roc score false negative numbers",
        description=(
            "The number of false negatives if the GQ score threshold was set to "
            '"score" field value.'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    numFN__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_numFN", title="Extension field for ``numFN``."
    )

    numFP: typing.List[fhirtypes.IntegerType | None] | None = Field(  # type: ignore
        None,
        alias="numFP",
        title="Roc score false positive numbers",
        description=(
            "The number of false positives if the GQ score threshold was set to "
            '"score" field value.'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    numFP__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_numFP", title="Extension field for ``numFP``."
    )

    numTP: typing.List[fhirtypes.IntegerType | None] | None = Field(  # type: ignore
        None,
        alias="numTP",
        title="Roc score true positive numbers",
        description=(
            "The number of true positives if the GQ score threshold was set to "
            '"score" field value.'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    numTP__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_numTP", title="Extension field for ``numTP``."
    )

    precision: typing.List[fhirtypes.DecimalType | None] | None = Field(  # type: ignore
        None,
        alias="precision",
        title="Precision of the GQ score",
        description=(
            'Calculated precision if the GQ score threshold was set to "score" '
            "field value."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    precision__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_precision", title="Extension field for ``precision``."
    )

    score: typing.List[fhirtypes.IntegerType | None] | None = Field(  # type: ignore
        None,
        alias="score",
        title="Genotype quality score",
        description=(
            "Invidual data point representing the GQ (genotype quality) score "
            "threshold."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    score__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_score", title="Extension field for ``score``."
    )

    sensitivity: typing.List[fhirtypes.DecimalType | None] | None = Field(  # type: ignore
        None,
        alias="sensitivity",
        title="Sensitivity of the GQ score",
        description=(
            'Calculated sensitivity if the GQ score threshold was set to "score" '
            "field value."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    sensitivity__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_sensitivity", title="Extension field for ``sensitivity``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceQualityRoc`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "score",
            "numTP",
            "numFP",
            "numFN",
            "precision",
            "sensitivity",
            "fMeasure",
        ]


class MolecularSequenceReferenceSeq(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A sequence used as reference.
    A sequence that is used as a reference to describe variants that are
    present in a sequence analyzed.
    """

    __resource_type__ = "MolecularSequenceReferenceSeq"

    chromosome: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="chromosome",
        title="Chromosome containing genetic finding",
        description=(
            "Structural unit composed of a nucleic acid molecule which controls its"
            " own replication through the interaction of specific proteins at one "
            "or more origins of replication ([SO:0000340](http://www.sequenceontolo"
            "gy.org/browser/current_svn/term/SO:0000340))."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    genomeBuild: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="genomeBuild",
        title=(
            "The Genome Build used for reference, following GRCh build versions "
            "e.g. 'GRCh 37'"
        ),
        description=(
            "The Genome Build used for reference, following GRCh build versions "
            "e.g. 'GRCh 37'.  Version number must be included if a versioned "
            "release of a primary build was used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    genomeBuild__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_genomeBuild", title="Extension field for ``genomeBuild``."
    )

    orientation: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="orientation",
        title="sense | antisense",
        description=(
            "A relative reference to a DNA strand based on gene orientation. The "
            'strand that contains the open reading frame of the gene is the "sense"'
            ' strand, and the opposite complementary strand is the "antisense" '
            "strand."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["sense", "antisense"],
        },
    )
    orientation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_orientation", title="Extension field for ``orientation``."
    )

    referenceSeqId: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="referenceSeqId",
        title="Reference identifier",
        description=(
            "Reference identifier of reference sequence submitted to NCBI. It must "
            "match the type in the MolecularSequence.type field. For example, the "
            "prefix, \u201cNG_\u201d identifies reference sequence for genes, \u201cNM_\u201d for "
            "messenger RNA transcripts, and \u201cNP_\u201d for amino acid sequences."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    referenceSeqPointer: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="referenceSeqPointer",
        title="A pointer to another MolecularSequence entity as reference sequence",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["MolecularSequence"],
        },
    )

    referenceSeqString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="referenceSeqString",
        title="A string to represent reference sequence",
        description='A string like "ACGT".',
        json_schema_extra={
            "element_property": True,
        },
    )
    referenceSeqString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_referenceSeqString",
        title="Extension field for ``referenceSeqString``.",
    )

    strand: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="strand",
        title="watson | crick",
        description=(
            "An absolute reference to a strand. The Watson strand is the strand "
            "whose 5'-end is on the short arm of the chromosome, and the Crick "
            "strand as the one whose 5'-end is on the long arm."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["watson", "crick"],
        },
    )
    strand__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_strand", title="Extension field for ``strand``."
    )

    windowEnd: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="windowEnd",
        title="End position of the window on the reference sequence",
        description=(
            "End position of the window on the reference sequence. If the "
            "coordinate system is 0-based then end is exclusive and does not "
            "include the last position. If the coordinate system is 1-base, then "
            "end is inclusive and includes the last position."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    windowEnd__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_windowEnd", title="Extension field for ``windowEnd``."
    )

    windowStart: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="windowStart",
        title="Start position of the window on the  reference sequence",
        description=(
            "Start position of the window on the reference sequence. If the "
            "coordinate system is either 0-based or 1-based, then start position is"
            " inclusive."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    windowStart__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_windowStart", title="Extension field for ``windowStart``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceReferenceSeq`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "chromosome",
            "genomeBuild",
            "orientation",
            "referenceSeqId",
            "referenceSeqPointer",
            "referenceSeqString",
            "strand",
            "windowStart",
            "windowEnd",
        ]


class MolecularSequenceRepository(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    External repository which contains detailed report related with observedSeq
    in this resource.
    Configurations of the external repository. The repository shall store
    target's observedSeq or records related with target's observedSeq.
    """

    __resource_type__ = "MolecularSequenceRepository"

    datasetId: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="datasetId",
        title="Id of the dataset that used to call for dataset in repository",
        description=(
            "Id of the variant in this external repository. The server will "
            "understand how to use this id to call for more info about datasets in "
            "external repository."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    datasetId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_datasetId", title="Extension field for ``datasetId``."
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Repository's name",
        description=(
            "URI of an external repository which contains further details about the"
            " genetics data."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    readsetId: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="readsetId",
        title="Id of the read",
        description="Id of the read in this external repository.",
        json_schema_extra={
            "element_property": True,
        },
    )
    readsetId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_readsetId", title="Extension field for ``readsetId``."
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="directlink | openapi | login | oauth | other",
        description=(
            "Click and see / RESTful API / Need login to see / RESTful API with "
            "authentication / Other ways to see resource."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["directlink", "openapi", "login", "oauth", "other"],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    url: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="url",
        title="URI of the repository",
        description=(
            "URI of an external repository which contains further details about the"
            " genetics data."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_url", title="Extension field for ``url``."
    )

    variantsetId: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="variantsetId",
        title="Id of the variantset that used to call for variantset in repository",
        description=(
            "Id of the variantset in this external repository. The server will "
            "understand how to use this id to call for more info about variantsets "
            "in external repository."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    variantsetId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_variantsetId", title="Extension field for ``variantsetId``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceRepository`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "url",
            "name",
            "datasetId",
            "variantsetId",
            "readsetId",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("type", "type__ext")]
        return required_fields


class MolecularSequenceStructureVariant(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Structural variant.
    Information about chromosome structure variation.
    """

    __resource_type__ = "MolecularSequenceStructureVariant"

    exact: bool | None = Field(  # type: ignore
        None,
        alias="exact",
        title="Does the structural variant have base pair resolution breakpoints?",
        description=(
            "Used to indicate if the outer and inner start-end values have the same"
            " meaning."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    exact__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_exact", title="Extension field for ``exact``."
    )

    inner: fhirtypes.MolecularSequenceStructureVariantInnerType | None = Field(  # type: ignore
        None,
        alias="inner",
        title="Structural variant inner",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    length: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="length",
        title="Structural variant length",
        description="Length of the variant chromosome.",
        json_schema_extra={
            "element_property": True,
        },
    )
    length__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_length", title="Extension field for ``length``."
    )

    outer: fhirtypes.MolecularSequenceStructureVariantOuterType | None = Field(  # type: ignore
        None,
        alias="outer",
        title="Structural variant outer",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    variantType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="variantType",
        title="Structural variant change type",
        description="Information about chromosome structure variation DNA change type.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceStructureVariant`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "variantType",
            "exact",
            "length",
            "outer",
            "inner",
        ]


class MolecularSequenceStructureVariantInner(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Structural variant inner.
    """

    __resource_type__ = "MolecularSequenceStructureVariantInner"

    end: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="end",
        title="Structural variant inner end",
        description=(
            "Structural variant inner end. If the coordinate system is 0-based then"
            " end is exclusive and does not include the last position. If the "
            "coordinate system is 1-base, then end is inclusive and includes the "
            "last position."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    end__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_end", title="Extension field for ``end``."
    )

    start: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="start",
        title="Structural variant inner start",
        description=(
            "Structural variant inner start. If the coordinate system is either "
            "0-based or 1-based, then start position is inclusive."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    start__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_start", title="Extension field for ``start``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceStructureVariantInner`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "start", "end"]


class MolecularSequenceStructureVariantOuter(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Structural variant outer.
    """

    __resource_type__ = "MolecularSequenceStructureVariantOuter"

    end: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="end",
        title="Structural variant outer end",
        description=(
            "Structural variant outer end. If the coordinate system is 0-based then"
            " end is exclusive and does not include the last position. If the "
            "coordinate system is 1-base, then end is inclusive and includes the "
            "last position."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    end__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_end", title="Extension field for ``end``."
    )

    start: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="start",
        title="Structural variant outer start",
        description=(
            "Structural variant outer start. If the coordinate system is either "
            "0-based or 1-based, then start position is inclusive."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    start__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_start", title="Extension field for ``start``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceStructureVariantOuter`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "start", "end"]


class MolecularSequenceVariant(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Variant in sequence.
    The definition of variant here originates from Sequence ontology ([variant_
    of](http://www.sequenceontology.org/browser/current_svn/term/variant_of)).
    This element can represent amino acid or nucleic sequence change(including
    insertion,deletion,SNP,etc.)  It can represent some complex mutation or
    segment variation with the assist of CIGAR string.
    """

    __resource_type__ = "MolecularSequenceVariant"

    cigar: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="cigar",
        title="Extended CIGAR string for aligning the sequence with reference bases",
        description=(
            "Extended CIGAR string for aligning the sequence with reference bases. "
            "See detailed documentation [here](http://support.illumina.com/help/Seq"
            "uencingAnalysisWorkflow/Content/Vault/Informatics/Sequencing_Analysis/"
            "CASAVA/swSEQ_mCA_ExtendedCIGARFormat.htm)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    cigar__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_cigar", title="Extension field for ``cigar``."
    )

    end: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="end",
        title="End position of the variant on the reference sequence",
        description=(
            "End position of the variant on the reference sequence. If the "
            "coordinate system is 0-based then end is exclusive and does not "
            "include the last position. If the coordinate system is 1-base, then "
            "end is inclusive and includes the last position."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    end__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_end", title="Extension field for ``end``."
    )

    observedAllele: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="observedAllele",
        title="Allele that was observed",
        description=(
            "An allele is one of a set of coexisting sequence variants of a gene (["
            "SO:0001023](http://www.sequenceontology.org/browser/current_svn/term/S"
            "O:0001023)).  Nucleotide(s)/amino acids from start position of "
            "sequence to stop position of sequence on the positive (+) strand of "
            "the observed  sequence. When the sequence  type is DNA, it should be "
            "the sequence on the positive (+) strand. This will lay in the range "
            "between variant.start and variant.end."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    observedAllele__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_observedAllele", title="Extension field for ``observedAllele``."
    )

    referenceAllele: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="referenceAllele",
        title="Allele in the reference sequence",
        description=(
            "An allele is one of a set of coexisting sequence variants of a gene (["
            "SO:0001023](http://www.sequenceontology.org/browser/current_svn/term/S"
            "O:0001023)). Nucleotide(s)/amino acids from start position of sequence"
            " to stop position of sequence on the positive (+) strand of the "
            "reference sequence. When the sequence  type is DNA, it should be the "
            "sequence on the positive (+) strand. This will lay in the range "
            "between variant.start and variant.end."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    referenceAllele__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_referenceAllele", title="Extension field for ``referenceAllele``."
    )

    start: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="start",
        title="Start position of the variant on the  reference sequence",
        description=(
            "Start position of the variant on the  reference sequence. If the "
            "coordinate system is either 0-based or 1-based, then start position is"
            " inclusive."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    start__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_start", title="Extension field for ``start``."
    )

    variantPointer: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="variantPointer",
        title="Pointer to observed variant information",
        description="A pointer to an Observation containing variant information.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Observation"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceVariant`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "start",
            "end",
            "observedAllele",
            "referenceAllele",
            "cigar",
            "variantPointer",
        ]
