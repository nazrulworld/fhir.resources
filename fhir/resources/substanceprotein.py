# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubstanceProtein
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType
from typing import Union

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class SubstanceProtein(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A SubstanceProtein is defined as a single unit of a linear amino acid
    sequence, or a combination of subunits that are either covalently linked or
    have a defined invariant stoichiometric relationship. This includes all
    synthetic, recombinant and purified SubstanceProteins of defined sequence,
    whether the use is therapeutic or prophylactic. This set of elements will
    be used to describe albumins, coagulation factors, cytokines, growth
    factors, peptide/SubstanceProtein hormones, enzymes, toxins, toxoids,
    recombinant vaccines, and immunomodulators.
    """

    resource_type = Field("SubstanceProtein", const=True)

    disulfideLinkage: ListType[fhirtypes.String] = Field(
        None,
        alias="disulfideLinkage",
        title="List of `String` items",
        description=(
            "The disulphide bond between two cysteine residues either on the same "
            "subunit or on two different subunits shall be described. The position "
            "of the disulfide bonds in the SubstanceProtein shall be listed in "
            "increasing order of subunit number and position within subunit "
            "followed by the abbreviation of the amino acids involved. The "
            "disulfide linkage positions shall actually contain the amino acid "
            "Cysteine at the respective positions"
        ),
    )
    disulfideLinkage__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_disulfideLinkage",
        title="Extension field for ``disulfideLinkage``.",
    )

    numberOfSubunits: fhirtypes.Integer = Field(
        None,
        alias="numberOfSubunits",
        title="Type `Integer`",
        description=(
            "Number of linear sequences of amino acids linked through peptide "
            "bonds. The number of subunits constituting the SubstanceProtein shall "
            "be described. It is possible that the number of subunits can be "
            "variable"
        ),
    )
    numberOfSubunits__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_numberOfSubunits",
        title="Extension field for ``numberOfSubunits``.",
    )

    sequenceType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="sequenceType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "The SubstanceProtein descriptive elements will only be used when a "
            "complete or partial amino acid sequence is available or derivable from"
            " a nucleic acid sequence"
        ),
    )

    subunit: ListType[fhirtypes.SubstanceProteinSubunitType] = Field(
        None,
        alias="subunit",
        title=(
            "List of `SubstanceProteinSubunit` items (represented as `dict` in " "JSON)"
        ),
        description=(
            "This subclause refers to the description of each subunit constituting "
            "the SubstanceProtein. A subunit is a linear sequence of amino acids "
            "linked through peptide bonds. The Subunit information shall be "
            "provided when the finished SubstanceProtein is a complex of multiple "
            "sequences; subunits are not used to delineate domains within a single "
            "sequence. Subunits are listed in order of decreasing length; sequences"
            " of the same length will be ordered by decreasing molecular weight; "
            "subunits that have identical sequences will be repeated multiple times"
        ),
    )


class SubstanceProteinSubunit(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    This subclause refers to the description of each subunit constituting the
    SubstanceProtein. A subunit is a linear sequence of amino acids linked
    through peptide bonds. The Subunit information shall be provided when the
    finished SubstanceProtein is a complex of multiple sequences; subunits are
    not used to delineate domains within a single sequence. Subunits are listed
    in order of decreasing length; sequences of the same length will be ordered
    by decreasing molecular weight; subunits that have identical sequences will
    be repeated multiple times.
    """

    resource_type = Field("SubstanceProteinSubunit", const=True)

    cTerminalModification: fhirtypes.String = Field(
        None,
        alias="cTerminalModification",
        title="Type `String`",
        description="The modification at the C-terminal shall be specified",
    )
    cTerminalModification__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_cTerminalModification",
        title="Extension field for ``cTerminalModification``.",
    )

    cTerminalModificationId: fhirtypes.IdentifierType = Field(
        None,
        alias="cTerminalModificationId",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description=(
            "Unique identifier for molecular fragment modification based on the ISO"
            " 11238 Substance ID"
        ),
    )

    length: fhirtypes.Integer = Field(
        None,
        alias="length",
        title="Type `Integer`",
        description="Length of linear sequences of amino acids contained in the subunit",
    )
    length__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_length", title="Extension field for ``length``."
    )

    nTerminalModification: fhirtypes.String = Field(
        None,
        alias="nTerminalModification",
        title="Type `String`",
        description=(
            "The name of the fragment modified at the N-terminal of the "
            "SubstanceProtein shall be specified"
        ),
    )
    nTerminalModification__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_nTerminalModification",
        title="Extension field for ``nTerminalModification``.",
    )

    nTerminalModificationId: fhirtypes.IdentifierType = Field(
        None,
        alias="nTerminalModificationId",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description=(
            "Unique identifier for molecular fragment modification based on the ISO"
            " 11238 Substance ID"
        ),
    )

    sequence: fhirtypes.String = Field(
        None,
        alias="sequence",
        title="Type `String`",
        description=(
            "The sequence information shall be provided enumerating the amino acids"
            " from N- to C-terminal end using standard single-letter amino acid "
            "codes. Uppercase shall be used for L-amino acids and lowercase for "
            "D-amino acids. Transcribed SubstanceProteins will always be described "
            "using the translated sequence; for synthetic peptide containing amino "
            "acids that are not represented with a single letter code an X should "
            "be used within the sequence. The modified amino acids will be "
            "distinguished by their position in the sequence"
        ),
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    sequenceAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="sequenceAttachment",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description=(
            "The sequence information shall be provided enumerating the amino acids"
            " from N- to C-terminal end using standard single-letter amino acid "
            "codes. Uppercase shall be used for L-amino acids and lowercase for "
            "D-amino acids. Transcribed SubstanceProteins will always be described "
            "using the translated sequence; for synthetic peptide containing amino "
            "acids that are not represented with a single letter code an X should "
            "be used within the sequence. The modified amino acids will be "
            "distinguished by their position in the sequence"
        ),
    )

    subunit: fhirtypes.Integer = Field(
        None,
        alias="subunit",
        title="Type `Integer`",
        description=(
            "Index of primary sequences of amino acids linked through peptide bonds"
            " in order of decreasing length. Sequences of the same length will be "
            "ordered by molecular weight. Subunits that have identical sequences "
            "will be repeated and have sequential subscripts"
        ),
    )
    subunit__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_subunit", title="Extension field for ``subunit``."
    )
