from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ChargeItemDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
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
        title="Billing codes or product types this definition applies to",
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

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the charge item definition was "
            "published. The date must change when the business version changes and "
            "it must change if the status code changes. In addition, it should "
            "change when the substantive content of the charge item definition "
            "changes."
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
            "enum_reference_types": ["Medication", "Substance", "Device"],
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
        title="When the charge item definition was last reviewed",
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
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the organization or individual that published the charge "
            "item definition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_publisher", title="Extension field for ``publisher``."
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
            "globally unique and SHOULD be a literal address at which at which an "
            "authoritative instance of this charge item definition is (or will be) "
            "published. This URL can be the target of a canonical reference. It "
            "SHALL remain the same when the charge item definition is stored on "
            "different servers."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
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
            "copyright",
            "approvalDate",
            "lastReviewDate",
            "effectivePeriod",
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
        required_fields = [("status", "status__ext"), ("url", "url__ext")]
        return required_fields


class ChargeItemDefinitionApplicability(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Whether or not the billing code is applicable.
    Expressions that describe applicability criteria for the billing code.
    """

    __resource_type__ = "ChargeItemDefinitionApplicability"

    description: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Natural language description of the condition",
        description=(
            "A brief, natural language description of the condition that "
            "effectively communicates the intended semantics."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    expression: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="expression",
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
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_expression", title="Extension field for ``expression``."
    )

    language: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="language",
        title="Language of the expression",
        description=(
            'The media type of the language for the expression, e.g. "text/cql" for'
            ' Clinical Query Language expressions or "text/fhirpath" for FHIRPath '
            "expressions."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    language__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_language", title="Extension field for ``language``."
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
            "description",
            "language",
            "expression",
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

    priceComponent: typing.List[fhirtypes.ChargeItemDefinitionPropertyGroupPriceComponentType] | None = Field(  # type: ignore
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


class ChargeItemDefinitionPropertyGroupPriceComponent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Components of total line item price.
    The price for a ChargeItem may be calculated as a base price with
    surcharges/deductions that apply in certain conditions. A
    ChargeItemDefinition resource that defines the prices, factors and
    conditions that apply to a billing code is currently under development. The
    priceComponent element can be used to offer transparency to the recipient
    of the Invoice of how the prices have been calculated.
    """

    __resource_type__ = "ChargeItemDefinitionPropertyGroupPriceComponent"

    amount: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="amount",
        title="Monetary amount associated with this component",
        description="The amount calculated for this component.",
        json_schema_extra={
            "element_property": True,
        },
    )

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Code identifying the specific component",
        description=(
            "A code that identifies the component. Codes may be used to "
            "differentiate between kinds of taxes, surcharges, discounts etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    factor: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="factor",
        title="Factor used for calculating this component",
        description=(
            "The factor that has been applied on the base price for calculating "
            "this component."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_factor", title="Extension field for ``factor``."
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="base | surcharge | deduction | discount | tax | informational",
        description="This code identifies the type of the component.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "base",
                "surcharge",
                "deduction",
                "discount",
                "tax",
                "informational",
            ],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ChargeItemDefinitionPropertyGroupPriceComponent`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "code",
            "factor",
            "amount",
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
