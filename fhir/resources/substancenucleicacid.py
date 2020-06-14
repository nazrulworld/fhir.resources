# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubstanceNucleicAcid
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class SubstanceNucleicAcid(domainresource.DomainResource):
    """ Nucleic acids are defined by three distinct elements: the base, sugar and
    linkage. Individual substance/moiety IDs will be created for each of these
    elements. The nucleotide sequence will be always entered in the 5’-3’
    direction.
    """

    resource_type = Field("SubstanceNucleicAcid", const=True)

    areaOfHybridisation: fhirtypes.String = Field(
        None,
        alias="areaOfHybridisation",
        title="Type `String` (represented as `dict` in JSON)",
        description="The area of hybridisation shall be described if applicable for double stranded RNA or DNA. The number associated with the subunit followed by the number associated to the residue shall be specified in increasing order. The underscore \u201c\u201d shall be used as separator as follows: \u201cSubunitnumber Residue\u201d",
    )

    numberOfSubunits: fhirtypes.Integer = Field(
        None,
        alias="numberOfSubunits",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="The number of linear sequences of nucleotides linked through phosphodiester bonds shall be described. Subunits would be strands of nucleic acids that are tightly associated typically through Watson-Crick base pairing. NOTE: If not specified in the reference source, the assumption is that there is 1 subunit",
    )

    oligoNucleotideType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="oligoNucleotideType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="(TBC)",
    )

    sequenceType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="sequenceType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The type of the sequence shall be specified based on a controlled vocabulary",
    )

    subunit: ListType[fhirtypes.SubstanceNucleicAcidSubunitType] = Field(
        None,
        alias="subunit",
        title="List of `SubstanceNucleicAcidSubunit` items (represented as `dict` in JSON)",
        description="Subunits are listed in order of decreasing length; sequences of the same length will be ordered by molecular weight; subunits that have identical sequences will be repeated multiple times",
    )


class SubstanceNucleicAcidSubunit(backboneelement.BackboneElement):
    """ Subunits are listed in order of decreasing length; sequences of the same
    length will be ordered by molecular weight; subunits that have identical
    sequences will be repeated multiple times.
    """

    resource_type = Field("SubstanceNucleicAcidSubunit", const=True)

    fivePrime: fhirtypes.CodeableConceptType = Field(
        None,
        alias="fivePrime",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The nucleotide present at the 5\u2019 terminal shall be specified based on a controlled vocabulary. Since the sequence is represented from the 5\u0027 to the 3\u0027 end, the 5\u2019 prime nucleotide is the letter at the first position in the sequence. A separate representation would be redundant",
    )

    length: fhirtypes.Integer = Field(
        None,
        alias="length",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="The length of the sequence shall be captured",
    )

    linkage: ListType[fhirtypes.SubstanceNucleicAcidSubunitLinkageType] = Field(
        None,
        alias="linkage",
        title="List of `SubstanceNucleicAcidSubunitLinkage` items (represented as `dict` in JSON)",
        description="The linkages between sugar residues will also be captured",
    )

    sequence: fhirtypes.String = Field(
        None,
        alias="sequence",
        title="Type `String` (represented as `dict` in JSON)",
        description="Actual nucleotide sequence notation from 5\u0027 to 3\u0027 end using standard single letter codes. In addition to the base sequence, sugar and type of phosphate or non-phosphate linkage should also be captured",
    )

    sequenceAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="sequenceAttachment",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="(TBC)",
    )

    subunit: fhirtypes.Integer = Field(
        None,
        alias="subunit",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Index of linear sequences of nucleic acids in order of decreasing length. Sequences of the same length will be ordered by molecular weight. Subunits that have identical sequences will be repeated and have sequential subscripts",
    )

    sugar: ListType[fhirtypes.SubstanceNucleicAcidSubunitSugarType] = Field(
        None,
        alias="sugar",
        title="List of `SubstanceNucleicAcidSubunitSugar` items (represented as `dict` in JSON)",
        description="5.3.6.8.1 Sugar ID (Mandatory)",
    )

    threePrime: fhirtypes.CodeableConceptType = Field(
        None,
        alias="threePrime",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The nucleotide present at the 3\u2019 terminal shall be specified based on a controlled vocabulary. Since the sequence is represented from the 5\u0027 to the 3\u0027 end, the 5\u2019 prime nucleotide is the letter at the last position in the sequence. A separate representation would be redundant",
    )


class SubstanceNucleicAcidSubunitLinkage(backboneelement.BackboneElement):
    """ The linkages between sugar residues will also be captured.
    """

    resource_type = Field("SubstanceNucleicAcidSubunitLinkage", const=True)

    connectivity: fhirtypes.String = Field(
        None,
        alias="connectivity",
        title="Type `String` (represented as `dict` in JSON)",
        description="The entity that links the sugar residues together should also be captured for nearly all naturally occurring nucleic acid the linkage is a phosphate group. For many synthetic oligonucleotides phosphorothioate linkages are often seen. Linkage connectivity is assumed to be 3\u2019-5\u2019. If the linkage is either 3\u2019-3\u2019 or 5\u2019-5\u2019 this should be specified",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Each linkage will be registered as a fragment and have an ID",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Each linkage will be registered as a fragment and have at least one name. A single name shall be assigned to each linkage",
    )

    residueSite: fhirtypes.String = Field(
        None,
        alias="residueSite",
        title="Type `String` (represented as `dict` in JSON)",
        description="Residues shall be captured as described in 5.3.6.8.3",
    )


class SubstanceNucleicAcidSubunitSugar(backboneelement.BackboneElement):
    """ 5.3.6.8.1 Sugar ID (Mandatory).
    """

    resource_type = Field("SubstanceNucleicAcidSubunitSugar", const=True)

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="The Substance ID of the sugar or sugar-like component that make up the nucleotide",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="The name of the sugar or sugar-like component that make up the nucleotide",
    )

    residueSite: fhirtypes.String = Field(
        None,
        alias="residueSite",
        title="Type `String` (represented as `dict` in JSON)",
        description="The residues that contain a given sugar will be captured. The order of given residues will be captured in the 5\u2018-3\u2018direction consistent with the base sequences listed above",
    )
