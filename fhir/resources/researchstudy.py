# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ResearchStudy
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class ResearchStudy(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Investigation to increase healthcare-related patient-independent knowledge.
    A scientific study of nature that sometimes includes processes involved in
    health and disease. For example, clinical trials are research studies that
    involve people. These studies may be related to new ways to screen,
    prevent, diagnose, and treat disease. They may also study certain outcomes
    and certain groups of people by looking at data collected in the past or
    future.
    """

    resource_type = Field("ResearchStudy", const=True)

    associatedParty: typing.List[fhirtypes.ResearchStudyAssociatedPartyType] = Field(
        None,
        alias="associatedParty",
        title="Sponsors, collaborators, and other parties",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    classifier: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="classifier",
        title="Classification for the study",
        description=(
            "Additional grouping mechanism or categorization of a research study. "
            "Example: FDA regulated device, FDA regulated drug, MPG Paragraph 23b "
            "(a German legal requirement), IRB-exempt, etc. Implementation Note: do"
            " not use the classifier element to support existing semantics that are"
            " already supported thru explicit elements in the resource."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    comparisonGroup: typing.List[fhirtypes.ResearchStudyComparisonGroupType] = Field(
        None,
        alias="comparisonGroup",
        title="Defined path through the study for a subject",
        description=(
            "Describes an expected event or sequence of events for one of the "
            "subjects of a study. E.g. for a living subject: exposure to drug A, "
            "wash-out, exposure to drug B, wash-out, follow-up. E.g. for a "
            "stability study: {store sample from lot A at 25 degrees for 1 month}, "
            "{store sample from lot A at 40 degrees for 1 month}."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    condition: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="condition",
        title="Condition being studied",
        description=(
            "The condition that is the focus of the study.  For example, In a study"
            " to examine risk factors for Lupus, might have as an inclusion "
            'criterion "healthy volunteer", but the target condition code would be '
            "a Lupus SNOMED code."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date the resource last changed",
        description=(
            "The date (and optionally time) when the ResearchStudy Resource was "
            "last significantly changed. The date must change when the business "
            "version changes and it must change if the status code changes. In "
            "addition, it should change when the substantive content of the "
            "ResearchStudy Resource changes."
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
        title="Detailed narrative of the study",
        description=(
            "A detailed and human-readable narrative of the study. E.g., study "
            "abstract."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    descriptionSummary: fhirtypes.Markdown = Field(
        None,
        alias="descriptionSummary",
        title="Brief text explaining the study",
        description="A brief text for explaining the study.",
        # if property is element of this resource.
        element_property=True,
    )
    descriptionSummary__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_descriptionSummary",
        title="Extension field for ``descriptionSummary``.",
    )

    focus: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="focus",
        title="Drugs, devices, etc. under study",
        description=(
            "The medication(s), food(s), therapy(ies), device(s) or other concerns "
            "or interventions that the study is seeking to gain more information "
            "about."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Medication",
            "MedicinalProductDefinition",
            "SubstanceDefinition",
            "EvidenceVariable",
        ],
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier for study",
        description=(
            "Identifiers assigned to this research study by the sponsor or other "
            "systems."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    keyword: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="keyword",
        title="Used to search for the study",
        description="Key terms to aid in searching for or filtering the study.",
        # if property is element of this resource.
        element_property=True,
    )

    label: typing.List[fhirtypes.ResearchStudyLabelType] = Field(
        None,
        alias="label",
        title="Additional names for the study",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name for this study (computer friendly)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Comments made about the study",
        description=(
            "Comments made about the study by the performer, subject or other "
            "participants."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    objective: typing.List[fhirtypes.ResearchStudyObjectiveType] = Field(
        None,
        alias="objective",
        title="A goal for the study",
        description=(
            "A goal that the study is aiming to achieve in terms of a scientific "
            "question to be answered by the analysis of data collected during the "
            "study."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    outcomeMeasure: typing.List[fhirtypes.ResearchStudyOutcomeMeasureType] = Field(
        None,
        alias="outcomeMeasure",
        title="A variable measured during the study",
        description=(
            'An "outcome measure", "endpoint", "effect measure" or "measure of '
            'effect" is a specific measurement or observation used to quantify the '
            "effect of experimental variables on the participants in a study, or "
            "for observational studies, to describe patterns of diseases or traits "
            "or associations with exposures, risk factors or treatment."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    partOf: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title="Part of larger study",
        description=(
            "A larger research study of which this particular study is a component "
            "or step."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ResearchStudy"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="When the study began and ended",
        description=(
            "Identifies the start date and the expected (or actual, depending on "
            "status) end date for the study."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    phase: fhirtypes.CodeableConceptType = Field(
        None,
        alias="phase",
        title=(
            "n-a | early-phase-1 | phase-1 | phase-1-phase-2 | phase-2 | "
            "phase-2-phase-3 | phase-3 | phase-4"
        ),
        description=(
            "The stage in the progression of a therapy from initial experimental "
            "use in humans in clinical trials to post-market evaluation."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    primaryPurposeType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="primaryPurposeType",
        title=(
            "treatment | prevention | diagnostic | supportive-care | screening | "
            "health-services-research | basic-science | device-feasibility"
        ),
        description=(
            "The type of study based upon the intent of the study activities. A "
            "classification of the intent of the study."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    progressStatus: typing.List[fhirtypes.ResearchStudyProgressStatusType] = Field(
        None,
        alias="progressStatus",
        title="Status of study with time for that status",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    protocol: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="protocol",
        title="Steps followed in executing study",
        description=(
            "The set of steps expected to be performed as part of the execution of "
            "the study."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["PlanDefinition"],
    )

    recruitment: fhirtypes.ResearchStudyRecruitmentType = Field(
        None,
        alias="recruitment",
        title="Target or actual group of participants enrolled in study",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    region: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="region",
        title="Geographic area for the study",
        description=(
            "A country, state or other area where the study is taking place rather "
            "than its precise geographic location or address."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    relatedArtifact: typing.List[fhirtypes.RelatedArtifactType] = Field(
        None,
        alias="relatedArtifact",
        title="References, URLs, and attachments",
        description=(
            "Citations, references, URLs and other related documents.  When using "
            "relatedArtifact to share URLs, the relatedArtifact.type will often be "
            'set to one of "documentation" or "supported-with" and the URL value '
            "will often be in relatedArtifact.document.url but another possible "
            "location is relatedArtifact.resource when it is a canonical URL."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    result: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="result",
        title="Link to results generated during the study",
        description=(
            "Link to one or more sets of results generated by the study.  Could "
            "also link to a research registry holding the results such as "
            "ClinicalTrials.gov."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["EvidenceReport", "Citation", "DiagnosticReport"],
    )

    site: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="site",
        title="Facility where study activities are conducted",
        description="A facility in which study activities are conducted.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location", "ResearchStudy", "Organization"],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description="The publication state of the resource (not of the study).",
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
        title="Classifications of the study design characteristics",
        description=(
            "Codes categorizing the type of study such as investigational vs. "
            "observational, type of blinding, type of randomization, safety vs. "
            "efficacy, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Human readable name of the study",
        description="The human readable name of the research study.",
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Canonical identifier for this study resource",
        description=(
            "Canonical identifier for this study resource, represented as a "
            "globally unique URI."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="The business version for the study record",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    whyStopped: fhirtypes.CodeableConceptType = Field(
        None,
        alias="whyStopped",
        title=(
            "accrual-goal-met | closed-due-to-toxicity | closed-due-to-lack-of-"
            "study-progress | temporarily-closed-per-study-design"
        ),
        description=(
            "A description and/or code explaining the premature termination of the "
            "study."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ResearchStudy`` according specification,
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
            "label",
            "protocol",
            "partOf",
            "relatedArtifact",
            "date",
            "status",
            "primaryPurposeType",
            "phase",
            "studyDesign",
            "focus",
            "condition",
            "keyword",
            "region",
            "descriptionSummary",
            "description",
            "period",
            "site",
            "note",
            "classifier",
            "associatedParty",
            "progressStatus",
            "whyStopped",
            "recruitment",
            "comparisonGroup",
            "objective",
            "outcomeMeasure",
            "result",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1553(
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


class ResearchStudyAssociatedParty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Sponsors, collaborators, and other parties.
    """

    resource_type = Field("ResearchStudyAssociatedParty", const=True)

    classifier: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="classifier",
        title="nih | fda | government | nonprofit | academic | industry",
        description="A categorization other than role for the associated party.",
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name of associated party",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    party: fhirtypes.ReferenceType = Field(
        None,
        alias="party",
        title=(
            "Individual or organization associated with study (use practitionerRole"
            " to specify their organisation)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "PractitionerRole", "Organization"],
    )

    period: typing.List[fhirtypes.PeriodType] = Field(
        None,
        alias="period",
        title="When active in the role",
        description=(
            "Identifies the start date and the end date of the associated party in "
            "the role."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    role: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="role",
        title=(
            "sponsor | lead-sponsor | sponsor-investigator | primary-investigator |"
            " collaborator | funding-source | general-contact | recruitment-contact"
            " | sub-investigator | study-director | study-chair"
        ),
        description="Type of association.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ResearchStudyAssociatedParty`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "name",
            "role",
            "period",
            "classifier",
            "party",
        ]


class ResearchStudyComparisonGroup(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Defined path through the study for a subject.
    Describes an expected event or sequence of events for one of the subjects
    of a study. E.g. for a living subject: exposure to drug A, wash-out,
    exposure to drug B, wash-out, follow-up. E.g. for a stability study: {store
    sample from lot A at 25 degrees for 1 month}, {store sample from lot A at
    40 degrees for 1 month}.
    """

    resource_type = Field("ResearchStudyComparisonGroup", const=True)

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Short explanation of study path",
        description=(
            "A succinct description of the path through the study that would be "
            "followed by a subject adhering to this comparisonGroup."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    intendedExposure: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="intendedExposure",
        title="Interventions or exposures in this comparisonGroup or cohort",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["EvidenceVariable"],
    )

    linkId: fhirtypes.Id = Field(
        None,
        alias="linkId",
        title=(
            "Allows the comparisonGroup for the study and the comparisonGroup for "
            "the subject to be linked easily"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_linkId", title="Extension field for ``linkId``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Label for study comparisonGroup",
        description="Unique, human-readable label for this comparisonGroup of the study.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    observedGroup: fhirtypes.ReferenceType = Field(
        None,
        alias="observedGroup",
        title="Group of participants who were enrolled in study comparisonGroup",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Group"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Categorization of study comparisonGroup",
        description=(
            "Categorization of study comparisonGroup, e.g. experimental, active "
            "comparator, placebo comparater."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ResearchStudyComparisonGroup`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "linkId",
            "name",
            "type",
            "description",
            "intendedExposure",
            "observedGroup",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3120(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("name", "name__ext")]
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


class ResearchStudyLabel(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional names for the study.
    """

    resource_type = Field("ResearchStudyLabel", const=True)

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title=(
            "primary | official | scientific | plain-language | subtitle | short-"
            "title | acronym | earlier-title | language | auto-translated | human-"
            "use | machine-use | duplicate-uid"
        ),
        description="Kind of name.",
        # if property is element of this resource.
        element_property=True,
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="The name",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ResearchStudyLabel`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "value"]


class ResearchStudyObjective(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A goal for the study.
    A goal that the study is aiming to achieve in terms of a scientific
    question to be answered by the analysis of data collected during the study.
    """

    resource_type = Field("ResearchStudyObjective", const=True)

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Description of the objective",
        description=(
            "Free text description of the objective of the study.  This is what the"
            " study is trying to achieve rather than how it is going to achieve it "
            "(see ResearchStudy.description)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Label for the objective",
        description="Unique, human-readable label for this objective of the study.",
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="primary | secondary | exploratory",
        description="The kind of study objective.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ResearchStudyObjective`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "name", "type", "description"]


class ResearchStudyOutcomeMeasure(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A variable measured during the study.
    An "outcome measure", "endpoint", "effect measure" or "measure of effect"
    is a specific measurement or observation used to quantify the effect of
    experimental variables on the participants in a study, or for observational
    studies, to describe patterns of diseases or traits or associations with
    exposures, risk factors or treatment.
    """

    resource_type = Field("ResearchStudyOutcomeMeasure", const=True)

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Description of the outcome",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Label for the outcome",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    reference: fhirtypes.ReferenceType = Field(
        None,
        alias="reference",
        title="Structured outcome definition",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["EvidenceVariable"],
    )

    type: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="primary | secondary | exploratory",
        description=(
            "The parameter or characteristic being assessed as one of the values by"
            " which the study is assessed."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ResearchStudyOutcomeMeasure`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "name",
            "type",
            "description",
            "reference",
        ]


class ResearchStudyProgressStatus(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Status of study with time for that status.
    """

    resource_type = Field("ResearchStudyProgressStatus", const=True)

    actual: bool = Field(
        None,
        alias="actual",
        title="Actual if true else anticipated",
        description=(
            "An indication of whether or not the date is a known date when the "
            "state changed or will change. A value of true indicates a known date. "
            "A value of false indicates an estimated date."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    actual__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_actual", title="Extension field for ``actual``."
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Date range",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    state: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="state",
        title="Label for status or state (e.g. recruitment status)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ResearchStudyProgressStatus`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "state", "actual", "period"]


class ResearchStudyRecruitment(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Target or actual group of participants enrolled in study.
    """

    resource_type = Field("ResearchStudyRecruitment", const=True)

    actualGroup: fhirtypes.ReferenceType = Field(
        None,
        alias="actualGroup",
        title="Group of participants who were enrolled in study",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Group"],
    )

    actualNumber: fhirtypes.UnsignedInt = Field(
        None,
        alias="actualNumber",
        title="Actual total number of participants enrolled in study",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    actualNumber__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_actualNumber", title="Extension field for ``actualNumber``."
    )

    eligibility: fhirtypes.ReferenceType = Field(
        None,
        alias="eligibility",
        title="Inclusion and exclusion criteria",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Group", "EvidenceVariable"],
    )

    targetNumber: fhirtypes.UnsignedInt = Field(
        None,
        alias="targetNumber",
        title="Estimated total number of participants to be enrolled",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    targetNumber__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_targetNumber", title="Extension field for ``targetNumber``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ResearchStudyRecruitment`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "targetNumber",
            "actualNumber",
            "eligibility",
            "actualGroup",
        ]
