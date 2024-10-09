from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ChargeItemDefinition
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ChargeItemDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Definition of properties and rules about how the price and the
    applicability of a ChargeItem can be determined.
    The ChargeItemDefinition resource provides the properties that apply to the
    (billing) codes necessary to calculate costs and prices. The properties may
    differ largely depending on type and realm, therefore this resource gives
    only a rough structure and requires profiling for each type of billing code
    system.
    """

    __resource_type__ = "ChargeItemDefinition"

    applicability: typing.List[fhirtypes.ChargeItemDefinitionApplicabilityType] | None = Field(  # type: ignore
        None,
        alias="applicability",
        title="Whether or not the billing code is applicable",
        description="Expressions that describe applicability criteria for the billing code.",
        json_schema_extra={
            "element_property": True,
        },
    )

    approvalDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="approvalDate",
        title="When the charge item definition was approved by publisher",
        description=(
            "The date on which the resource content was approved by the publisher. "
            "Approval happens once when the content is officially approved for "
            "usage."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_approvalDate", title="Extension field for ``approvalDate``."
    )

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Billing code or product type this definition applies to",
        description=(
            "The defined billing details in this resource pertain to the given "
            "billing code."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    contact: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        None,
        alias="contact",
        title="Contact details for the publisher",
        description=(
            "Contact details to assist a user in finding and communicating with the"
            " publisher."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    copyright: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the charge item definition and/or "
            "its contents. Copyright statements are generally legal restrictions on"
            " the use and publishing of the charge item definition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    copyrightLabel: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="copyrightLabel",
        title="Copyright holder and year(s)",
        description=(
            "A short string (<50 characters), suitable for inclusion in a page "
            "footer that identifies the copyright holder, effective period, and "
            "optionally whether rights are resctricted. (e.g. 'All rights "
            "reserved', 'Some rights reserved')."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    copyrightLabel__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_copyrightLabel", title="Extension field for ``copyrightLabel``."
    )

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the charge item definition was "
            "last significantly changed. The date must change when the business "
            "version changes and it must change if the status code changes. In "
            "addition, it should change when the substantive content of the charge "
            "item definition changes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    derivedFromUri: typing.List[fhirtypes.UriType | None] | None = Field(  # type: ignore
        None,
        alias="derivedFromUri",
        title="Underlying externally-defined charge item definition",
        description=(
            "The URL pointing to an externally-defined charge item definition that "
            "is adhered to in whole or in part by this definition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    derivedFromUri__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_derivedFromUri", title="Extension field for ``derivedFromUri``."
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Natural language description of the charge item definition",
        description=(
            "A free text natural language description of the charge item definition"
            " from a consumer's perspective."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    experimental: bool | None = Field(  # type: ignore
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this charge item definition is "
            "authored for testing purposes (or education/evaluation/marketing) and "
            "is not intended to be used for genuine usage."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Additional identifier for the charge item definition",
        description=(
            "A formal identifier that is used to identify this charge item "
            "definition when it is represented in other formats, or referenced in a"
            " specification, model, design or an instance."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    instance: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="instance",
        title="Instances this definition applies to",
        description=(
            "The defined billing details in this resource pertain to the given "
            "product instance(s)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Medication",
                "Substance",
                "Device",
                "DeviceDefinition",
                "ActivityDefinition",
                "PlanDefinition",
                "HealthcareService",
            ],
        },
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for charge item definition (if applicable)",
        description=(
            "A legal or geographic region in which the charge item definition is "
            "intended to be used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    lastReviewDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="lastReviewDate",
        title="When the charge item definition was last reviewed by the publisher",
        description=(
            "The date on which the resource content was last reviewed. Review "
            "happens periodically after approval but does not change the original "
            "approval date."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_lastReviewDate", title="Extension field for ``lastReviewDate``."
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name for this charge item definition (computer friendly)",
        description=(
            "A natural language name identifying the ChargeItemDefinition. This "
            "name should be usable as an identifier for the module by machine "
            "processing applications such as code generation."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    partOf: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="partOf",
        title=(
            "A larger definition of which this particular definition is a component"
            " or step"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ChargeItemDefinition"],
        },
    )
    partOf__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_partOf", title="Extension field for ``partOf``."
    )

    propertyGroup: typing.List[fhirtypes.ChargeItemDefinitionPropertyGroupType] | None = Field(  # type: ignore
        None,
        alias="propertyGroup",
        title="Group of properties which are applicable under the same conditions",
        description=(
            "Group of properties which are applicable under the same conditions. If"
            " no applicability rules are established for the group, then all "
            "properties always apply."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    publisher: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="publisher",
        title="Name of the publisher/steward (organization or individual)",
        description=(
            "The name of the organization or individual responsible for the release"
            " and ongoing maintenance of the charge item definition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="purpose",
        title="Why this charge item definition is defined",
        description=(
            "Explanation of why this charge item definition is needed and why it "
            "has been designed as it has."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    replaces: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="replaces",
        title=(
            "Completed or terminated request(s) whose function is taken by this new"
            " request"
        ),
        description=(
            "As new versions of a protocol or guideline are defined, allows "
            "identification of what versions are replaced by a new instance."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ChargeItemDefinition"],
        },
    )
    replaces__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_replaces", title="Extension field for ``replaces``."
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description="The current state of the ChargeItemDefinition.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["draft", "active", "retired", "unknown"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Name for this charge item definition (human friendly)",
        description=(
            "A short, descriptive, user-friendly title for the charge item "
            "definition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="url",
        title=(
            "Canonical identifier for this charge item definition, represented as a"
            " URI (globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this charge item definition "
            "when it is referenced in a specification, model, design or an "
            "instance; also called its canonical identifier. This SHOULD be "
            "globally unique and SHOULD be a literal address at which an "
            "authoritative instance of this charge item definition is (or will be) "
            "published. This URL can be the target of a canonical reference. It "
            "SHALL remain the same when the charge item definition is stored on "
            "different servers."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_url", title="Extension field for ``url``."
    )

    useContext: typing.List[fhirtypes.UsageContextType] | None = Field(  # type: ignore
        None,
        alias="useContext",
        title="The context that the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These contexts may be general categories "
            "(gender, age, ...) or may be references to specific programs "
            "(insurance plans, studies, ...) and may be used to assist with "
            "indexing and searching for appropriate charge item definition "
            "instances."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="Business version of the charge item definition",
        description=(
            "The identifier that is used to identify this version of the charge "
            "item definition when it is referenced in a specification, model, "
            "design or instance. This is an arbitrary value managed by the charge "
            "item definition author and is not expected to be globally unique. For "
            "example, it might be a timestamp (e.g. yyyymmdd) if a managed version "
            "is not available. There is also no expectation that versions can be "
            "placed in a lexicographical sequence. To provide a version consistent "
            "with the Decision Support Service specification, use the format "
            "Major.Minor.Revision (e.g. 1.0.0). For more information on versioning "
            "knowledge assets, refer to the Decision Support Service specification."
            " Note that a version is required for non-experimental active assets."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_version", title="Extension field for ``version``."
    )

    versionAlgorithmCoding: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="versionAlgorithmCoding",
        title="How to compare versions",
        description=(
            "Indicates the mechanism used to compare versions to determine which is"
            " more current."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e versionAlgorithm[x]
            "one_of_many": "versionAlgorithm",
            "one_of_many_required": False,
        },
    )

    versionAlgorithmString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="versionAlgorithmString",
        title="How to compare versions",
        description=(
            "Indicates the mechanism used to compare versions to determine which is"
            " more current."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e versionAlgorithm[x]
            "one_of_many": "versionAlgorithm",
            "one_of_many_required": False,
        },
    )
    versionAlgorithmString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_versionAlgorithmString",
        title="Extension field for ``versionAlgorithmString``.",
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ChargeItemDefinition`` according specification,
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
            "url",
            "identifier",
            "version",
            "versionAlgorithmString",
            "versionAlgorithmCoding",
            "name",
            "title",
            "derivedFromUri",
            "partOf",
            "replaces",
            "status",
            "experimental",
            "date",
            "publisher",
            "contact",
            "description",
            "useContext",
            "jurisdiction",
            "purpose",
            "copyright",
            "copyrightLabel",
            "approvalDate",
            "lastReviewDate",
            "code",
            "instance",
            "applicability",
            "propertyGroup",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        return required_fields

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
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
            "versionAlgorithm": ["versionAlgorithmCoding", "versionAlgorithmString"]
        }
        return one_of_many_fields


class ChargeItemDefinitionApplicability(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Whether or not the billing code is applicable.
    Expressions that describe applicability criteria for the billing code.
    """

    __resource_type__ = "ChargeItemDefinitionApplicability"

    condition: fhirtypes.ExpressionType | None = Field(  # type: ignore
        None,
        alias="condition",
        title="Boolean-valued expression",
        description=(
            "An expression that returns true or false, indicating whether the "
            "condition is satisfied. When using FHIRPath expressions, the %context "
            "environment variable must be replaced at runtime with the ChargeItem "
            "resource to which this definition is applied."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    effectivePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="effectivePeriod",
        title="When the charge item definition is expected to be used",
        description=(
            "The period during which the charge item definition content was or is "
            "planned to be in active use."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    relatedArtifact: fhirtypes.RelatedArtifactType | None = Field(  # type: ignore
        None,
        alias="relatedArtifact",
        title=(
            "Reference to / quotation of the external source of the group of "
            "properties"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ChargeItemDefinitionApplicability`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "condition",
            "effectivePeriod",
            "relatedArtifact",
        ]


class ChargeItemDefinitionPropertyGroup(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Group of properties which are applicable under the same conditions.
    Group of properties which are applicable under the same conditions. If no
    applicability rules are established for the group, then all properties
    always apply.
    """

    __resource_type__ = "ChargeItemDefinitionPropertyGroup"

    applicability: typing.List[fhirtypes.ChargeItemDefinitionApplicabilityType] | None = Field(  # type: ignore
        None,
        alias="applicability",
        title="Conditions under which the priceComponent is applicable",
        description=(
            "Expressions that describe applicability criteria for the "
            "priceComponent."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    priceComponent: typing.List[fhirtypes.MonetaryComponentType] | None = Field(  # type: ignore
        None,
        alias="priceComponent",
        title="Components of total line item price",
        description=(
            "The price for a ChargeItem may be calculated as a base price with "
            "surcharges/deductions that apply in certain conditions. A "
            "ChargeItemDefinition resource that defines the prices, factors and "
            "conditions that apply to a billing code is currently under "
            "development. The priceComponent element can be used to offer "
            "transparency to the recipient of the Invoice of how the prices have "
            "been calculated."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ChargeItemDefinitionPropertyGroup`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "applicability",
            "priceComponent",
        ]
