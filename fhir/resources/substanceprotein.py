# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubstanceProtein
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field

from . import backboneelement, domainresource, fhirtypes


class SubstanceProtein(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
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

    disulfideLinkage: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="disulfideLinkage",
        title=(
            "The disulphide bond between two cysteine residues either on the same "
            "subunit or on two different subunits shall be described. The position "
            "of the disulfide bonds in the SubstanceProtein shall be listed in "
            "increasing order of subunit number and position within subunit "
            "followed by the abbreviation of the amino acids involved. The "
            "disulfide linkage positions shall actually contain the amino acid "
            "Cysteine at the respective positions"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    disulfideLinkage__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_disulfideLinkage",
        title="Extension field for ``disulfideLinkage``.",
    )

    numberOfSubunits: fhirtypes.Integer = Field(
        None,
        alias="numberOfSubunits",
        title=(
            "Number of linear sequences of amino acids linked through peptide "
            "bonds. The number of subunits constituting the SubstanceProtein shall "
            "be described. It is possible that the number of subunits can be "
            "variable"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    numberOfSubunits__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_numberOfSubunits",
        title="Extension field for ``numberOfSubunits``.",
    )

    sequenceType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="sequenceType",
        title=(
            "The SubstanceProtein descriptive elements will only be used when a "
            "complete or partial amino acid sequence is available or derivable from"
            " a nucleic acid sequence"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    subunit: typing.List[fhirtypes.SubstanceProteinSubunitType] = Field(
        None,
        alias="subunit",
        title=(
            "This subclause refers to the description of each subunit constituting "
            "the SubstanceProtein. A subunit is a linear sequence of amino acids "
            "linked through peptide bonds. The Subunit information shall be "
            "provided when the finished SubstanceProtein is a complex of multiple "
            "sequences; subunits are not used to delineate domains within a single "
            "sequence. Subunits are listed in order of decreasing length; sequences"
            " of the same length will be ordered by decreasing molecular weight; "
            "subunits that have identical sequences will be repeated multiple times"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceProtein`` according specification,
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
            "sequenceType",
            "numberOfSubunits",
            "disulfideLinkage",
            "subunit",
        ]


class SubstanceProteinSubunit(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
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
        title="The modification at the C-terminal shall be specified",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    cTerminalModification__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_cTerminalModification",
        title="Extension field for ``cTerminalModification``.",
    )

    cTerminalModificationId: fhirtypes.IdentifierType = Field(
        None,
        alias="cTerminalModificationId",
        title=(
            "Unique identifier for molecular fragment modification based on the ISO"
            " 11238 Substance ID"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    length: fhirtypes.Integer = Field(
        None,
        alias="length",
        title="Length of linear sequences of amino acids contained in the subunit",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    length__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_length", title="Extension field for ``length``."
    )

    nTerminalModification: fhirtypes.String = Field(
        None,
        alias="nTerminalModification",
        title=(
            "The name of the fragment modified at the N-terminal of the "
            "SubstanceProtein shall be specified"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    nTerminalModification__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_nTerminalModification",
        title="Extension field for ``nTerminalModification``.",
    )

    nTerminalModificationId: fhirtypes.IdentifierType = Field(
        None,
        alias="nTerminalModificationId",
        title=(
            "Unique identifier for molecular fragment modification based on the ISO"
            " 11238 Substance ID"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    sequence: fhirtypes.String = Field(
        None,
        alias="sequence",
        title=(
            "The sequence information shall be provided enumerating the amino acids"
            " from N- to C-terminal end using standard single-letter amino acid "
            "codes. Uppercase shall be used for L-amino acids and lowercase for "
            "D-amino acids. Transcribed SubstanceProteins will always be described "
            "using the translated sequence; for synthetic peptide containing amino "
            "acids that are not represented with a single letter code an X should "
            "be used within the sequence. The modified amino acids will be "
            "distinguished by their position in the sequence"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    sequenceAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="sequenceAttachment",
        title=(
            "The sequence information shall be provided enumerating the amino acids"
            " from N- to C-terminal end using standard single-letter amino acid "
            "codes. Uppercase shall be used for L-amino acids and lowercase for "
            "D-amino acids. Transcribed SubstanceProteins will always be described "
            "using the translated sequence; for synthetic peptide containing amino "
            "acids that are not represented with a single letter code an X should "
            "be used within the sequence. The modified amino acids will be "
            "distinguished by their position in the sequence"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    subunit: fhirtypes.Integer = Field(
        None,
        alias="subunit",
        title=(
            "Index of primary sequences of amino acids linked through peptide bonds"
            " in order of decreasing length. Sequences of the same length will be "
            "ordered by molecular weight. Subunits that have identical sequences "
            "will be repeated and have sequential subscripts"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    subunit__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_subunit", title="Extension field for ``subunit``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceProteinSubunit`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "subunit",
            "sequence",
            "length",
            "sequenceAttachment",
            "nTerminalModificationId",
            "nTerminalModification",
            "cTerminalModificationId",
            "cTerminalModification",
        ]
