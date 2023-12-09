# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Measure
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class Measure(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A quality measure definition.
    The Measure resource provides the definition of a quality measure.
    """

    resource_type = Field("Measure", const=True)

    approvalDate: fhirtypes.Date = Field(
        None,
        alias="approvalDate",
        title="When the measure was approved by publisher",
        description=(
            "The date on which the resource content was approved by the publisher. "
            "Approval happens once when the content is officially approved for "
            "usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_approvalDate", title="Extension field for ``approvalDate``."
    )

    clinicalRecommendationStatement: fhirtypes.Markdown = Field(
        None,
        alias="clinicalRecommendationStatement",
        title="Summary of clinical guidelines",
        description=(
            "Provides a summary of relevant clinical guidelines or other clinical "
            "recommendations supporting the measure."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    clinicalRecommendationStatement__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_clinicalRecommendationStatement",
        title="Extension field for ``clinicalRecommendationStatement``.",
    )

    compositeScoring: fhirtypes.CodeableConceptType = Field(
        None,
        alias="compositeScoring",
        title="opportunity | all-or-nothing | linear | weighted",
        description=(
            "If this is a composite measure, the scoring method used to combine the"
            " component measures to determine the composite score."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    contact: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="Contact details for the publisher",
        description=(
            "Contact details to assist a user in finding and communicating with the"
            " publisher."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    contributor: typing.List[fhirtypes.ContributorType] = Field(
        None,
        alias="contributor",
        title="A content contributor",
        description=(
            "A contributor to the content of the measure, including authors, "
            "editors, reviewers, and endorsers."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the measure and/or its contents. "
            "Copyright statements are generally legal restrictions on the use and "
            "publishing of the measure."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date this was last changed",
        description=(
            "The date  (and optionally time) when the measure was published. The "
            "date must change if and when the business version changes and it must "
            "change if the status code changes. In addition, it should change when "
            "the substantive content of the measure changes."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    definition: typing.List[fhirtypes.Markdown] = Field(
        None,
        alias="definition",
        title="Defined terms used in the measure documentation",
        description="Provides a description of an individual term used within the measure.",
        # if property is element of this resource.
        element_property=True,
    )
    definition__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_definition", title="Extension field for ``definition``.")

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Natural language description of the measure",
        description=(
            "A free text natural language description of the measure from a "
            "consumer's perspective."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    disclaimer: fhirtypes.Markdown = Field(
        None,
        alias="disclaimer",
        title="Disclaimer for use of the measure or its referenced content",
        description=(
            "Notices and disclaimers regarding the use of the measure, or related "
            "to intellectual property (such as code systems) referenced by the "
            "measure."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    disclaimer__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_disclaimer", title="Extension field for ``disclaimer``."
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="When the measure is expected to be used",
        description=(
            "The period during which the measure content was or is planned to be in"
            " active use."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A boolean value to indicate that this measure is authored for testing "
            "purposes (or education/evaluation/marketing), and is not intended to "
            "be used for genuine usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    group: typing.List[fhirtypes.MeasureGroupType] = Field(
        None,
        alias="group",
        title="Population criteria group",
        description="A group of population criteria for the measure.",
        # if property is element of this resource.
        element_property=True,
    )

    guidance: fhirtypes.Markdown = Field(
        None,
        alias="guidance",
        title="Additional guidance for implementers",
        description=(
            "Additional guidance for the measure including how it can be used in a "
            "clinical context, and the intent of the measure."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    guidance__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_guidance", title="Extension field for ``guidance``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Additional identifier for the measure",
        description=(
            "A formal identifier that is used to identify this measure when it is "
            "represented in other formats, or referenced in a specification, model,"
            " design or an instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    improvementNotation: fhirtypes.String = Field(
        None,
        alias="improvementNotation",
        title=(
            "Improvement notation for the measure, e.g. higher score indicates "
            "better quality"
        ),
        description=(
            "Information on whether an increase or decrease in score is the "
            "preferred result (e.g., a higher score indicates better quality OR a "
            "lower score indicates better quality OR quality is whthin a range)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    improvementNotation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_improvementNotation",
        title="Extension field for ``improvementNotation``.",
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for measure (if applicable)",
        description=(
            "A legal or geographic region in which the measure is intended to be "
            "used."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    lastReviewDate: fhirtypes.Date = Field(
        None,
        alias="lastReviewDate",
        title="When the measure was last reviewed",
        description=(
            "The date on which the resource content was last reviewed. Review "
            "happens periodically after approval, but doesn't change the original "
            "approval date."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastReviewDate", title="Extension field for ``lastReviewDate``."
    )

    library: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="library",
        title="Logic used by the measure",
        description=(
            "A reference to a Library resource containing the formal logic used by "
            "the measure."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Library"],
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name for this measure (computer friendly)",
        description=(
            "A natural language name identifying the measure. This name should be "
            "usable as an identifier for the module by machine processing "
            "applications such as code generation."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description="The name of the individual or organization that published the measure.",
        # if property is element of this resource.
        element_property=True,
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Why this measure is defined",
        description=(
            "Explaination of why this measure is needed and why it has been "
            "designed as it has."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    rateAggregation: fhirtypes.String = Field(
        None,
        alias="rateAggregation",
        title="How is rate aggregation performed for this measure",
        description=(
            "Describes how to combine the information calculated, based on logic in"
            " each of several populations, into one summarized result."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    rateAggregation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_rateAggregation", title="Extension field for ``rateAggregation``."
    )

    rationale: fhirtypes.Markdown = Field(
        None,
        alias="rationale",
        title="Why does this measure exist",
        description=(
            "Provides a succint statement of the need for the measure. Usually "
            "includes statements pertaining to importance criterion: impact, gap in"
            " care, and evidence."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    rationale__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_rationale", title="Extension field for ``rationale``."
    )

    relatedArtifact: typing.List[fhirtypes.RelatedArtifactType] = Field(
        None,
        alias="relatedArtifact",
        title="Additional documentation, citations, etc",
        description=(
            "Related artifacts such as additional documentation, justification, or "
            "bibliographic references."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    riskAdjustment: fhirtypes.String = Field(
        None,
        alias="riskAdjustment",
        title="How is risk adjustment applied for this measure",
        description=(
            "A description of the risk adjustment factors that may impact the "
            "resulting score for the measure and how they may be accounted for when"
            " computing and reporting measure results."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    riskAdjustment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_riskAdjustment", title="Extension field for ``riskAdjustment``."
    )

    scoring: fhirtypes.CodeableConceptType = Field(
        None,
        alias="scoring",
        title="proportion | ratio | continuous-variable | cohort",
        description=(
            "Indicates how the calculation is performed for the measure, including "
            "proportion, ratio, continuous variable, and cohort. The value set is "
            "extensible, allowing additional measure scoring types to be "
            "represented."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    set: fhirtypes.String = Field(
        None,
        alias="set",
        title="The measure set, e.g. Preventive Care and Screening",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    set__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_set", title="Extension field for ``set``."
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this measure. Enables tracking the life-cycle of the "
            "content."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired", "unknown"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    supplementalData: typing.List[fhirtypes.MeasureSupplementalDataType] = Field(
        None,
        alias="supplementalData",
        title="What other data should be reported with the measure",
        description=(
            "The supplemental data criteria for the measure report, specified as "
            "either the name of a valid CQL expression within a referenced library,"
            " or a valid FHIR Resource Path."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Name for this measure (human friendly)",
        description="A short, descriptive, user-friendly title for the measure.",
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    topic: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="topic",
        title="E.g. Education, Treatment, Assessment, etc",
        description=(
            "Descriptive topics related to the content of the measure. Topics "
            "provide a high-level categorization of the type of the measure that "
            "can be useful for filtering and searching."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="process | outcome | structure | patient-reported-outcome | composite",
        description=(
            "Indicates whether the measure is used to examine a process, an outcome"
            " over time, a patient-reported outcome, or a structure measure such as"
            " utilization."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Logical URI to reference this measure (globally unique)",
        description=(
            "An absolute URI that is used to identify this measure when it is "
            "referenced in a specification, model, design or an instance. This "
            "SHALL be a URL, SHOULD be globally unique, and SHOULD be an address at"
            " which this measure is (or will be) published. The URL SHOULD include "
            "the major version of the measure. For more information see [Technical "
            "and Business Versions](resource.html#versions)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    usage: fhirtypes.String = Field(
        None,
        alias="usage",
        title="Describes the clinical usage of the measure",
        description=(
            "A detailed description of how the measure is used from a clinical "
            "perspective."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    usage__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_usage", title="Extension field for ``usage``."
    )

    useContext: typing.List[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="Context the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These terms may be used to assist with "
            "indexing and searching for appropriate measure instances."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the measure",
        description=(
            "The identifier that is used to identify this version of the measure "
            "when it is referenced in a specification, model, design or instance. "
            "This is an arbitrary value managed by the measure author and is not "
            "expected to be globally unique. For example, it might be a timestamp "
            "(e.g. yyyymmdd) if a managed version is not available. There is also "
            "no expectation that versions can be placed in a lexicographical "
            "sequence. To provide a version consistent with the Decision Support "
            "Service specification, use the format Major.Minor.Revision (e.g. "
            "1.0.0). For more information on versioning knowledge assets, refer to "
            "the Decision Support Service specification. Note that a version is "
            "required for non-experimental active artifacts."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Measure`` according specification,
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
            "name",
            "title",
            "status",
            "experimental",
            "date",
            "publisher",
            "description",
            "purpose",
            "usage",
            "approvalDate",
            "lastReviewDate",
            "effectivePeriod",
            "useContext",
            "jurisdiction",
            "topic",
            "contributor",
            "contact",
            "copyright",
            "relatedArtifact",
            "library",
            "disclaimer",
            "scoring",
            "compositeScoring",
            "type",
            "riskAdjustment",
            "rateAggregation",
            "rationale",
            "clinicalRecommendationStatement",
            "improvementNotation",
            "definition",
            "guidance",
            "set",
            "group",
            "supplementalData",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_900(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class MeasureGroup(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Population criteria group.
    A group of population criteria for the measure.
    """

    resource_type = Field("MeasureGroup", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Summary description",
        description="The human readable description of this population group.",
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    identifier: fhirtypes.IdentifierType = Field(
        ...,
        alias="identifier",
        title="Unique identifier",
        description=(
            "A unique identifier for the group. This identifier will used to report"
            " data for the group in the measure report."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Short name",
        description="Optional name or short description of this group.",
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    population: typing.List[fhirtypes.MeasureGroupPopulationType] = Field(
        None,
        alias="population",
        title="Population criteria",
        description="A population criteria for the measure.",
        # if property is element of this resource.
        element_property=True,
    )

    stratifier: typing.List[fhirtypes.MeasureGroupStratifierType] = Field(
        None,
        alias="stratifier",
        title="Stratifier criteria for the measure",
        description=(
            "The stratifier criteria for the measure report, specified as either "
            "the name of a valid CQL expression defined within a referenced "
            "library, or a valid FHIR Resource Path."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MeasureGroup`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "identifier",
            "name",
            "description",
            "population",
            "stratifier",
        ]


class MeasureGroupPopulation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Population criteria.
    A population criteria for the measure.
    """

    resource_type = Field("MeasureGroupPopulation", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title=(
            "initial-population | numerator | numerator-exclusion | denominator | "
            "denominator-exclusion | denominator-exception | measure-population | "
            "measure-population-exclusion | measure-observation"
        ),
        description="The type of population criteria.",
        # if property is element of this resource.
        element_property=True,
    )

    criteria: fhirtypes.String = Field(
        None,
        alias="criteria",
        title=(
            "The name of a valid referenced CQL expression (may be namespaced) that"
            " defines this population criteria"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    criteria__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_criteria", title="Extension field for ``criteria``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="The human readable description of this population criteria",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Unique identifier",
        description=(
            "A unique identifier for the population criteria. This identifier is "
            "used to report data against this criteria within the measure report."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Short name",
        description="Optional name or short description of this population.",
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MeasureGroupPopulation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "identifier",
            "code",
            "name",
            "description",
            "criteria",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2501(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("criteria", "criteria__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class MeasureGroupStratifier(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Stratifier criteria for the measure.
    The stratifier criteria for the measure report, specified as either the
    name of a valid CQL expression defined within a referenced library, or a
    valid FHIR Resource Path.
    """

    resource_type = Field("MeasureGroupStratifier", const=True)

    criteria: fhirtypes.String = Field(
        None,
        alias="criteria",
        title="How the measure should be stratified",
        description=(
            "The criteria for the stratifier. This must be the name of an "
            "expression defined within a referenced library."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    criteria__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_criteria", title="Extension field for ``criteria``."
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title=(
            "The identifier for the stratifier used to coordinate the reported data"
            " back to this stratifier"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    path: fhirtypes.String = Field(
        None,
        alias="path",
        title="Path to the stratifier",
        description=(
            "The path to an element that defines the stratifier, specified as a "
            "valid FHIR resource path."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_path", title="Extension field for ``path``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MeasureGroupStratifier`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "identifier",
            "criteria",
            "path",
        ]


class MeasureSupplementalData(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What other data should be reported with the measure.
    The supplemental data criteria for the measure report, specified as either
    the name of a valid CQL expression within a referenced library, or a valid
    FHIR Resource Path.
    """

    resource_type = Field("MeasureSupplementalData", const=True)

    criteria: fhirtypes.String = Field(
        None,
        alias="criteria",
        title="Expression describing additional data to be reported",
        description=(
            "The criteria for the supplemental data. This must be the name of a "
            "valid expression defined within a referenced library, and defines the "
            "data to be returned for this element."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    criteria__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_criteria", title="Extension field for ``criteria``."
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Identifier, unique within the measure",
        description="An identifier for the supplemental data.",
        # if property is element of this resource.
        element_property=True,
    )

    path: fhirtypes.String = Field(
        None,
        alias="path",
        title="Path to the supplemental data element",
        description=(
            "The supplemental data to be supplied as part of the measure response, "
            "specified as a valid FHIR Resource Path."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_path", title="Extension field for ``path``."
    )

    usage: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="usage",
        title="supplemental-data | risk-adjustment-factor",
        description=(
            "An indicator of the intended usage for the supplemental data element. "
            "Supplemental data indicates the data is additional information "
            "requested to augment the measure information. Risk adjustment factor "
            "indicates the data is additional information used to calculate risk "
            "adjustment factors when applying a risk model to the measure "
            "calculation."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MeasureSupplementalData`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "identifier",
            "usage",
            "criteria",
            "path",
        ]
