# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MolecularSequence
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class MolecularSequence(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Representation of a molecular sequence.
    """

    resource_type = Field("MolecularSequence", const=True)

    device: fhirtypes.ReferenceType = Field(
        None,
        alias="device",
        title="The method for sequencing",
        description="The method for sequencing, for example, chip information.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device"],
    )

    focus: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="focus",
        title=(
            "What the molecular sequence is about, when it is not about the subject"
            " of record"
        ),
        description=(
            "The actual focus of a molecular sequence when it is not the patient of"
            " record representing something or someone associated with the patient "
            "such as a spouse, parent, child, or sibling. For example, in trio "
            "testing, the subject would be the child (proband) and the focus would "
            "be the parent."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    formatted: typing.List[fhirtypes.AttachmentType] = Field(
        None,
        alias="formatted",
        title=(
            "Embedded file or a link (URL) which contains content to represent the "
            "sequence"
        ),
        description=(
            "Sequence that was observed as file content. Can be an actual file "
            "contents, or referenced by a URL to an external system."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Unique ID for this particular sequence",
        description="A unique identifier for this particular sequence instance.",
        # if property is element of this resource.
        element_property=True,
    )

    literal: fhirtypes.String = Field(
        None,
        alias="literal",
        title="Sequence that was observed",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    literal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_literal", title="Extension field for ``literal``."
    )

    performer: fhirtypes.ReferenceType = Field(
        None,
        alias="performer",
        title="Who should be responsible for test result",
        description="The organization or lab that should be responsible for this result.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    relative: typing.List[fhirtypes.MolecularSequenceRelativeType] = Field(
        None,
        alias="relative",
        title="A sequence defined relative to another sequence",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    specimen: fhirtypes.ReferenceType = Field(
        None,
        alias="specimen",
        title="Specimen used for sequencing",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Specimen"],
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Subject this sequence is associated too",
        description="Indicates the subject this sequence is associated too.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "Group",
            "Substance",
            "BiologicallyDerivedProduct",
            "NutritionProduct",
        ],
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="aa | dna | rna",
        description="Amino Acid Sequence/ DNA Sequence / RNA Sequence.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["aa", "dna", "rna"],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
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
            "subject",
            "focus",
            "specimen",
            "device",
            "performer",
            "literal",
            "formatted",
            "relative",
        ]


class MolecularSequenceRelative(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A sequence defined relative to another sequence.
    """

    resource_type = Field("MolecularSequenceRelative", const=True)

    coordinateSystem: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="coordinateSystem",
        title="Ways of identifying nucleotides or amino acids within a sequence",
        description=(
            "These are different ways of identifying nucleotides or amino acids "
            "within a sequence. Different databases and file types may use "
            "different systems. For detail definitions, see "
            "https://loinc.org/92822-6/ for more detail."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    edit: typing.List[fhirtypes.MolecularSequenceRelativeEditType] = Field(
        None,
        alias="edit",
        title="Changes in sequence from the starting sequence",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    ordinalPosition: fhirtypes.Integer = Field(
        None,
        alias="ordinalPosition",
        title=(
            "Indicates the order in which the sequence should be considered when "
            "putting multiple 'relative' elements together"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    ordinalPosition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_ordinalPosition", title="Extension field for ``ordinalPosition``."
    )

    sequenceRange: fhirtypes.RangeType = Field(
        None,
        alias="sequenceRange",
        title=(
            "Indicates the nucleotide range in the composed sequence when multiple "
            "'relative' elements are used together"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    startingSequence: fhirtypes.MolecularSequenceRelativeStartingSequenceType = Field(
        None,
        alias="startingSequence",
        title="A sequence used as starting sequence",
        description=(
            "A sequence that is used as a starting sequence to describe variants "
            "that are present in a sequence analyzed."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceRelative`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "coordinateSystem",
            "ordinalPosition",
            "sequenceRange",
            "startingSequence",
            "edit",
        ]


class MolecularSequenceRelativeEdit(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Changes in sequence from the starting sequence.
    """

    resource_type = Field("MolecularSequenceRelativeEdit", const=True)

    end: fhirtypes.Integer = Field(
        None,
        alias="end",
        title="End position of the edit on the starting sequence",
        description=(
            "End position of the edit on the starting sequence. If the coordinate "
            "system is 0-based then end is exclusive and does not include the last "
            "position. If the coordinate system is 1-base, then end is inclusive "
            "and includes the last position."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    end__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_end", title="Extension field for ``end``."
    )

    replacedSequence: fhirtypes.String = Field(
        None,
        alias="replacedSequence",
        title="Allele in the starting sequence",
        description=(
            "Allele in the starting sequence. Nucleotide(s)/amino acids from start "
            "position of sequence to stop position of sequence on the positive (+) "
            "strand of the starting sequence. When the sequence  type is DNA, it "
            "should be the sequence on the positive (+) strand. This will lay in "
            "the range between variant.start and variant.end."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    replacedSequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_replacedSequence",
        title="Extension field for ``replacedSequence``.",
    )

    replacementSequence: fhirtypes.String = Field(
        None,
        alias="replacementSequence",
        title="Allele that was observed",
        description=(
            "Allele that was observed. Nucleotide(s)/amino acids from start "
            "position of sequence to stop position of sequence on the positive (+) "
            "strand of the observed sequence. When the sequence type is DNA, it "
            "should be the sequence on the positive (+) strand. This will lay in "
            "the range between variant.start and variant.end."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    replacementSequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_replacementSequence",
        title="Extension field for ``replacementSequence``.",
    )

    start: fhirtypes.Integer = Field(
        None,
        alias="start",
        title="Start position of the edit on the starting sequence",
        description=(
            "Start position of the edit on the starting sequence. If the coordinate"
            " system is either 0-based or 1-based, then start position is "
            "inclusive."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    start__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_start", title="Extension field for ``start``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceRelativeEdit`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "start",
            "end",
            "replacementSequence",
            "replacedSequence",
        ]


class MolecularSequenceRelativeStartingSequence(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A sequence used as starting sequence.
    A sequence that is used as a starting sequence to describe variants that
    are present in a sequence analyzed.
    """

    resource_type = Field("MolecularSequenceRelativeStartingSequence", const=True)

    chromosome: fhirtypes.CodeableConceptType = Field(
        None,
        alias="chromosome",
        title="Chromosome Identifier",
        description=(
            "Structural unit composed of a nucleic acid molecule which controls its"
            " own replication through the interaction of specific proteins at one "
            "or more origins of replication ([SO:0000340](http://www.sequenceontolo"
            "gy.org/browser/current_svn/term/SO:0000340))."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    genomeAssembly: fhirtypes.CodeableConceptType = Field(
        None,
        alias="genomeAssembly",
        title="The genome assembly used for starting sequence, e.g. GRCh38",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    orientation: fhirtypes.Code = Field(
        None,
        alias="orientation",
        title="sense | antisense",
        description=(
            "A relative reference to a DNA strand based on gene orientation. The "
            'strand that contains the open reading frame of the gene is the "sense"'
            ' strand, and the opposite complementary strand is the "antisense" '
            "strand."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["sense", "antisense"],
    )
    orientation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_orientation", title="Extension field for ``orientation``."
    )

    sequenceCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="sequenceCodeableConcept",
        title="The reference sequence that represents the starting sequence",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e sequence[x]
        one_of_many="sequence",
        one_of_many_required=False,
    )

    sequenceReference: fhirtypes.ReferenceType = Field(
        None,
        alias="sequenceReference",
        title="The reference sequence that represents the starting sequence",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e sequence[x]
        one_of_many="sequence",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MolecularSequence"],
    )

    sequenceString: fhirtypes.String = Field(
        None,
        alias="sequenceString",
        title="The reference sequence that represents the starting sequence",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e sequence[x]
        one_of_many="sequence",
        one_of_many_required=False,
    )
    sequenceString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequenceString", title="Extension field for ``sequenceString``."
    )

    strand: fhirtypes.Code = Field(
        None,
        alias="strand",
        title="watson | crick",
        description=(
            "An absolute reference to a strand. The Watson strand is the strand "
            "whose 5'-end is on the short arm of the chromosome, and the Crick "
            "strand as the one whose 5'-end is on the long arm."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["watson", "crick"],
    )
    strand__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_strand", title="Extension field for ``strand``."
    )

    windowEnd: fhirtypes.Integer = Field(
        None,
        alias="windowEnd",
        title="End position of the window on the starting sequence",
        description=(
            "End position of the window on the starting sequence. This value should"
            " honor the rules of the  coordinateSystem."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    windowEnd__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_windowEnd", title="Extension field for ``windowEnd``."
    )

    windowStart: fhirtypes.Integer = Field(
        None,
        alias="windowStart",
        title="Start position of the window on the starting sequence",
        description=(
            "Start position of the window on the starting sequence. This value "
            "should honor the rules of the coordinateSystem."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    windowStart__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_windowStart", title="Extension field for ``windowStart``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceRelativeStartingSequence`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "genomeAssembly",
            "chromosome",
            "sequenceCodeableConcept",
            "sequenceString",
            "sequenceReference",
            "windowStart",
            "windowEnd",
            "orientation",
            "strand",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_4432(
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
            "sequence": [
                "sequenceCodeableConcept",
                "sequenceReference",
                "sequenceString",
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
