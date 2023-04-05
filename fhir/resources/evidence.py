# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Evidence
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class Evidence(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Single evidence bit.
    The Evidence Resource provides a machine-interpretable expression of an
    evidence concept including the evidence variables (e.g., population,
    exposures/interventions, comparators, outcomes, measured variables,
    confounding variables), the statistics, and the certainty of this evidence.
    """

    resource_type = Field("Evidence", const=True)

    approvalDate: fhirtypes.Date = Field(
        None,
        alias="approvalDate",
        title="When the summary was approved by publisher",
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

    assertion: fhirtypes.Markdown = Field(
        None,
        alias="assertion",
        title="Declarative description of the Evidence",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    assertion__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_assertion", title="Extension field for ``assertion``."
    )

    author: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="author",
        title="Who authored the content",
        description=(
            "An individiual, organization, or device primarily involved in the "
            "creation and maintenance of the content."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    certainty: typing.List[fhirtypes.EvidenceCertaintyType] = Field(
        None,
        alias="certainty",
        title="Certainty or quality of the evidence",
        description=(
            "Assessment of certainty, confidence in the estimates, or quality of "
            "the evidence."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    citeAsMarkdown: fhirtypes.Markdown = Field(
        None,
        alias="citeAsMarkdown",
        title="Citation for this evidence",
        description="Citation Resource or display of suggested citation for this evidence.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e citeAs[x]
        one_of_many="citeAs",
        one_of_many_required=False,
    )
    citeAsMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_citeAsMarkdown", title="Extension field for ``citeAsMarkdown``."
    )

    citeAsReference: fhirtypes.ReferenceType = Field(
        None,
        alias="citeAsReference",
        title="Citation for this evidence",
        description="Citation Resource or display of suggested citation for this evidence.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e citeAs[x]
        one_of_many="citeAs",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Citation"],
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

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the Evidence and/or its contents. "
            "Copyright statements are generally legal restrictions on the use and "
            "publishing of the Evidence."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    copyrightLabel: fhirtypes.String = Field(
        None,
        alias="copyrightLabel",
        title="Copyright holder and year(s)",
        description=(
            "A short string (<50 characters), suitable for inclusion in a page "
            "footer that identifies the copyright holder, effective period, and "
            "optionally whether rights are resctricted. (e.g. 'All rights "
            "reserved', 'Some rights reserved')."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    copyrightLabel__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyrightLabel", title="Extension field for ``copyrightLabel``."
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the summary was last "
            "significantly changed. The date must change when the business version "
            "changes and it must change if the status code changes. In addition, it"
            " should change when the substantive content of the summary changes."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Description of the particular summary",
        description=(
            "A free text natural language description of the evidence from a "
            "consumer's perspective."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    editor: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="editor",
        title="Who edited the content",
        description=(
            "An individiual, organization, or device primarily responsible for "
            "internal coherence of the content."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    endorser: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="endorser",
        title="Who endorsed the content",
        description=(
            "An individiual, organization, or device responsible for officially "
            "endorsing the content for use in some setting."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this resource is authored for testing"
            " purposes (or education/evaluation/marketing) and is not intended to "
            "be used for genuine usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Additional identifier for the summary",
        description=(
            "A formal identifier that is used to identify this summary when it is "
            "represented in other formats, or referenced in a specification, model,"
            " design or an instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    lastReviewDate: fhirtypes.Date = Field(
        None,
        alias="lastReviewDate",
        title="When the summary was last reviewed by the publisher",
        description=(
            "The date on which the resource content was last reviewed. Review "
            "happens periodically after approval but does not change the original "
            "approval date."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastReviewDate", title="Extension field for ``lastReviewDate``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name for this summary (machine friendly)",
        description=(
            "A natural language name identifying the evidence. This name should be "
            "usable as an identifier for the module by machine processing "
            "applications such as code generation."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Footnotes and/or explanatory notes",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher/steward (organization or individual)",
        description=(
            "The name of the organization or individual responsible for the release"
            " and ongoing maintenance of the evidence."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Why this Evidence is defined",
        description=(
            "Explanation of why this Evidence is needed and why it has been "
            "designed as it has."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    relatedArtifact: typing.List[fhirtypes.RelatedArtifactType] = Field(
        None,
        alias="relatedArtifact",
        title="Link or citation to artifact associated with the summary",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    reviewer: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="reviewer",
        title="Who reviewed the content",
        description=(
            "An individiual, organization, or device primarily responsible for "
            "review of some aspect of the content."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    statistic: typing.List[fhirtypes.EvidenceStatisticType] = Field(
        None,
        alias="statistic",
        title="Values and parameters for a single statistic",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this summary. Enables tracking the life-cycle of the "
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

    studyDesign: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="studyDesign",
        title="The design of the study that produced this evidence",
        description=(
            "The design of the study that produced this evidence. The design is "
            "described with any number of study design characteristics."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    synthesisType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="synthesisType",
        title="The method to combine studies",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Name for this summary (human friendly)",
        description="A short, descriptive, user-friendly title for the summary.",
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title=(
            "Canonical identifier for this evidence, represented as a globally "
            "unique URI"
        ),
        description=(
            "An absolute URI that is used to identify this evidence when it is "
            "referenced in a specification, model, design or an instance; also "
            "called its canonical identifier. This SHOULD be globally unique and "
            "SHOULD be a literal address at which an authoritative instance of this"
            " summary is (or will be) published. This URL can be the target of a "
            "canonical reference. It SHALL remain the same when the summary is "
            "stored on different servers."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    useContext: typing.List[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="The context that the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These contexts may be general categories "
            "(gender, age, ...) or may be references to specific programs "
            "(insurance plans, studies, ...) and may be used to assist with "
            "indexing and searching for appropriate evidence instances."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    variableDefinition: typing.List[fhirtypes.EvidenceVariableDefinitionType] = Field(
        ...,
        alias="variableDefinition",
        title="Evidence variable such as population, exposure, or outcome",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of this summary",
        description=(
            "The identifier that is used to identify this version of the summary "
            "when it is referenced in a specification, model, design or instance. "
            "This is an arbitrary value managed by the summary author and is not "
            "expected to be globally unique. For example, it might be a timestamp "
            "(e.g. yyyymmdd) if a managed version is not available. There is also "
            "no expectation that versions can be placed in a lexicographical "
            "sequence."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    versionAlgorithmCoding: fhirtypes.CodingType = Field(
        None,
        alias="versionAlgorithmCoding",
        title="How to compare versions",
        description=(
            "Indicates the mechanism used to compare versions to determine which is"
            " more current."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e versionAlgorithm[x]
        one_of_many="versionAlgorithm",
        one_of_many_required=False,
    )

    versionAlgorithmString: fhirtypes.String = Field(
        None,
        alias="versionAlgorithmString",
        title="How to compare versions",
        description=(
            "Indicates the mechanism used to compare versions to determine which is"
            " more current."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e versionAlgorithm[x]
        one_of_many="versionAlgorithm",
        one_of_many_required=False,
    )
    versionAlgorithmString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_versionAlgorithmString",
        title="Extension field for ``versionAlgorithmString``.",
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Evidence`` according specification,
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
            "citeAsReference",
            "citeAsMarkdown",
            "status",
            "experimental",
            "date",
            "approvalDate",
            "lastReviewDate",
            "publisher",
            "contact",
            "author",
            "editor",
            "reviewer",
            "endorser",
            "useContext",
            "purpose",
            "copyright",
            "copyrightLabel",
            "relatedArtifact",
            "description",
            "assertion",
            "note",
            "variableDefinition",
            "synthesisType",
            "studyDesign",
            "statistic",
            "certainty",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_973(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_973(
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
            "citeAs": ["citeAsMarkdown", "citeAsReference"],
            "versionAlgorithm": ["versionAlgorithmCoding", "versionAlgorithmString"],
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


class EvidenceCertainty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Certainty or quality of the evidence.
    Assessment of certainty, confidence in the estimates, or quality of the
    evidence.
    """

    resource_type = Field("EvidenceCertainty", const=True)

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Textual description of certainty",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Footnotes and/or explanatory notes",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    rater: fhirtypes.String = Field(
        None,
        alias="rater",
        title="Individual or group who did the rating",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    rater__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_rater", title="Extension field for ``rater``."
    )

    rating: fhirtypes.CodeableConceptType = Field(
        None,
        alias="rating",
        title="Assessment or judgement of the aspect",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    subcomponent: typing.List[fhirtypes.EvidenceCertaintyType] = Field(
        None,
        alias="subcomponent",
        title="A domain or subdomain of certainty",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Aspect of certainty being rated",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EvidenceCertainty`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "description",
            "note",
            "type",
            "rating",
            "rater",
            "subcomponent",
        ]


class EvidenceStatistic(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Values and parameters for a single statistic.
    """

    resource_type = Field("EvidenceStatistic", const=True)

    attributeEstimate: typing.List[
        fhirtypes.EvidenceStatisticAttributeEstimateType
    ] = Field(
        None,
        alias="attributeEstimate",
        title="An attribute of the Statistic",
        description=(
            "A statistical attribute of the statistic such as a measure of "
            "heterogeneity."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Associated category for categorical variable",
        description=(
            "When the measured variable is handled categorically, the category "
            "element is used to define which category the statistic is reporting."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Description of content",
        description="A description of the content value of the statistic.",
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    modelCharacteristic: typing.List[
        fhirtypes.EvidenceStatisticModelCharacteristicType
    ] = Field(
        None,
        alias="modelCharacteristic",
        title="An aspect of the statistical model",
        description="A component of the method to generate the statistic.",
        # if property is element of this resource.
        element_property=True,
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Footnotes and/or explanatory notes",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    numberAffected: fhirtypes.UnsignedInt = Field(
        None,
        alias="numberAffected",
        title="The number of participants affected",
        description=(
            "The number of participants affected where the unit of analysis is the "
            "same as sampleSize.knownDataCount and sampleSize.numberOfParticipants."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    numberAffected__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_numberAffected", title="Extension field for ``numberAffected``."
    )

    numberOfEvents: fhirtypes.UnsignedInt = Field(
        None,
        alias="numberOfEvents",
        title="The number of events associated with the statistic",
        description=(
            "The number of events associated with the statistic, where the unit of "
            "analysis is different from numberAffected, sampleSize.knownDataCount "
            "and sampleSize.numberOfParticipants."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    numberOfEvents__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_numberOfEvents", title="Extension field for ``numberOfEvents``."
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Statistic value",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    sampleSize: fhirtypes.EvidenceStatisticSampleSizeType = Field(
        None,
        alias="sampleSize",
        title="Number of samples in the statistic",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    statisticType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="statisticType",
        title="Type of statistic, e.g., relative risk",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EvidenceStatistic`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "description",
            "note",
            "statisticType",
            "category",
            "quantity",
            "numberOfEvents",
            "numberAffected",
            "sampleSize",
            "attributeEstimate",
            "modelCharacteristic",
        ]


class EvidenceStatisticAttributeEstimate(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An attribute of the Statistic.
    A statistical attribute of the statistic such as a measure of
    heterogeneity.
    """

    resource_type = Field("EvidenceStatisticAttributeEstimate", const=True)

    attributeEstimate: typing.List[
        fhirtypes.EvidenceStatisticAttributeEstimateType
    ] = Field(
        None,
        alias="attributeEstimate",
        title=(
            "A nested attribute estimate; which is the attribute estimate of an "
            "attribute estimate"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Textual description of the attribute estimate",
        description="Human-readable summary of the estimate.",
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    level: fhirtypes.Decimal = Field(
        None,
        alias="level",
        title="Level of confidence interval, e.g., 0.95 for 95% confidence interval",
        description="Use 95 for a 95% confidence interval.",
        # if property is element of this resource.
        element_property=True,
    )
    level__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_level", title="Extension field for ``level``."
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Footnote or explanatory note about the estimate",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title=(
            "The singular quantity of the attribute estimate, for attribute "
            "estimates represented as single values; also used to report unit of "
            "measure"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    range: fhirtypes.RangeType = Field(
        None,
        alias="range",
        title="Lower and upper bound values of the attribute estimate",
        description="Lower bound of confidence interval.",
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="The type of attribute estimate, e.g., confidence interval or p value",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EvidenceStatisticAttributeEstimate`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "description",
            "note",
            "type",
            "quantity",
            "level",
            "range",
            "attributeEstimate",
        ]


class EvidenceStatisticModelCharacteristic(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An aspect of the statistical model.
    A component of the method to generate the statistic.
    """

    resource_type = Field("EvidenceStatisticModelCharacteristic", const=True)

    attributeEstimate: typing.List[
        fhirtypes.EvidenceStatisticAttributeEstimateType
    ] = Field(
        None,
        alias="attributeEstimate",
        title="An attribute of the statistic used as a model characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Model specification",
        description="Description of a component of the method to generate the statistic.",
        # if property is element of this resource.
        element_property=True,
    )

    value: fhirtypes.QuantityType = Field(
        None,
        alias="value",
        title="Numerical value to complete model specification",
        description=(
            "Further specification of the quantified value of the component of the "
            "method to generate the statistic."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    variable: typing.List[
        fhirtypes.EvidenceStatisticModelCharacteristicVariableType
    ] = Field(
        None,
        alias="variable",
        title="A variable adjusted for in the adjusted analysis",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EvidenceStatisticModelCharacteristic`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "value",
            "variable",
            "attributeEstimate",
        ]


class EvidenceStatisticModelCharacteristicVariable(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A variable adjusted for in the adjusted analysis.
    """

    resource_type = Field("EvidenceStatisticModelCharacteristicVariable", const=True)

    handling: fhirtypes.Code = Field(
        None,
        alias="handling",
        title="continuous | dichotomous | ordinal | polychotomous",
        description="How the variable is classified for use in adjusted analysis.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["continuous", "dichotomous", "ordinal", "polychotomous"],
    )
    handling__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_handling", title="Extension field for ``handling``."
    )

    valueCategory: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="valueCategory",
        title="Description for grouping of ordinal or polychotomous variables",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    valueQuantity: typing.List[fhirtypes.QuantityType] = Field(
        None,
        alias="valueQuantity",
        title="Discrete value for grouping of ordinal or polychotomous variables",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    valueRange: typing.List[fhirtypes.RangeType] = Field(
        None,
        alias="valueRange",
        title="Range of values for grouping of ordinal or polychotomous variables",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    variableDefinition: fhirtypes.ReferenceType = Field(
        ...,
        alias="variableDefinition",
        title="Description of the variable",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Group", "EvidenceVariable"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EvidenceStatisticModelCharacteristicVariable`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "variableDefinition",
            "handling",
            "valueCategory",
            "valueQuantity",
            "valueRange",
        ]


class EvidenceStatisticSampleSize(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Number of samples in the statistic.
    """

    resource_type = Field("EvidenceStatisticSampleSize", const=True)

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Textual description of sample size for statistic",
        description="Human-readable summary of population sample size.",
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    knownDataCount: fhirtypes.UnsignedInt = Field(
        None,
        alias="knownDataCount",
        title="Number of participants with known results for measured variables",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    knownDataCount__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_knownDataCount", title="Extension field for ``knownDataCount``."
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Footnote or explanatory note about the sample size",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    numberOfParticipants: fhirtypes.UnsignedInt = Field(
        None,
        alias="numberOfParticipants",
        title="Cumulative number of participants",
        description=(
            "A human-readable string to clarify or explain concepts about the "
            "sample size."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    numberOfParticipants__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_numberOfParticipants",
        title="Extension field for ``numberOfParticipants``.",
    )

    numberOfStudies: fhirtypes.UnsignedInt = Field(
        None,
        alias="numberOfStudies",
        title="Number of contributing studies",
        description="Number of participants in the population.",
        # if property is element of this resource.
        element_property=True,
    )
    numberOfStudies__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_numberOfStudies", title="Extension field for ``numberOfStudies``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EvidenceStatisticSampleSize`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "description",
            "note",
            "numberOfStudies",
            "numberOfParticipants",
            "knownDataCount",
        ]


class EvidenceVariableDefinition(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Evidence variable such as population, exposure, or outcome.
    """

    resource_type = Field("EvidenceVariableDefinition", const=True)

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="A text description or summary of the variable",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    directnessMatch: fhirtypes.CodeableConceptType = Field(
        None,
        alias="directnessMatch",
        title="low | moderate | high | exact",
        description=(
            "Indication of quality of match between intended variable to actual "
            "variable."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    intended: fhirtypes.ReferenceType = Field(
        None,
        alias="intended",
        title="Definition of the intended variable related to the Evidence",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Group", "EvidenceVariable"],
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Footnotes and/or explanatory notes",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    observed: fhirtypes.ReferenceType = Field(
        None,
        alias="observed",
        title="Definition of the actual variable related to the statistic(s)",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Group", "EvidenceVariable"],
    )

    variableRole: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="variableRole",
        title=(
            "population | subpopulation | exposure | referenceExposure | "
            "measuredVariable | confounder"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EvidenceVariableDefinition`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "description",
            "note",
            "variableRole",
            "observed",
            "intended",
            "directnessMatch",
        ]
