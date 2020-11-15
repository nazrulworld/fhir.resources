# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Evidence
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import domainresource, fhirtypes


class Evidence(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A research context or question.
    The Evidence resource describes the conditional state (population and any
    exposures being compared within the population) and outcome (if specified)
    that the knowledge (evidence, assertion, recommendation) is about.
    """

    resource_type = Field("Evidence", const=True)

    approvalDate: fhirtypes.Date = Field(
        None,
        alias="approvalDate",
        title="When the evidence was approved by publisher",
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

    author: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="author",
        title="Who authored the content",
        description=(
            "An individiual or organization primarily involved in the creation and "
            "maintenance of the content."
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

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the evidence and/or its contents. "
            "Copyright statements are generally legal restrictions on the use and "
            "publishing of the evidence."
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
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the evidence was published. The "
            "date must change when the business version changes and it must change "
            "if the status code changes. In addition, it should change when the "
            "substantive content of the evidence changes."
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
        title="Natural language description of the evidence",
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
            "An individual or organization primarily responsible for internal "
            "coherence of the content."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="When the evidence is expected to be used",
        description=(
            "The period during which the evidence content was or is planned to be "
            "in active use."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    endorser: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="endorser",
        title="Who endorsed the content",
        description=(
            "An individual or organization responsible for officially endorsing the"
            " content for use in some setting."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    exposureBackground: fhirtypes.ReferenceType = Field(
        ...,
        alias="exposureBackground",
        title="What population?",
        description=(
            "A reference to a EvidenceVariable resource that defines the population"
            " for the research."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["EvidenceVariable"],
    )

    exposureVariant: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="exposureVariant",
        title="What exposure?",
        description=(
            "A reference to a EvidenceVariable resource that defines the exposure "
            "for the research."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["EvidenceVariable"],
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Additional identifier for the evidence",
        description=(
            "A formal identifier that is used to identify this evidence when it is "
            "represented in other formats, or referenced in a specification, model,"
            " design or an instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for evidence (if applicable)",
        description=(
            "A legal or geographic region in which the evidence is intended to be "
            "used."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    lastReviewDate: fhirtypes.Date = Field(
        None,
        alias="lastReviewDate",
        title="When the evidence was last reviewed",
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
        title="Name for this evidence (computer friendly)",
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
        title="Used for footnotes or explanatory notes",
        description=(
            "A human-readable string to clarify or explain concepts about the "
            "resource."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    outcome: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="outcome",
        title="What outcome?",
        description=(
            "A reference to a EvidenceVariable resomece that defines the outcome "
            "for the research."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["EvidenceVariable"],
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the organization or individual that published the " "evidence."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    relatedArtifact: typing.List[fhirtypes.RelatedArtifactType] = Field(
        None,
        alias="relatedArtifact",
        title="Additional documentation, citations, etc.",
        description=(
            "Related artifacts such as additional documentation, justification, or "
            "bibliographic references."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    reviewer: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="reviewer",
        title="Who reviewed the content",
        description=(
            "An individual or organization primarily responsible for review of some"
            " aspect of the content."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    shortTitle: fhirtypes.String = Field(
        None,
        alias="shortTitle",
        title="Title for use in informal contexts",
        description=(
            "The short title provides an alternate title for use in informal "
            "descriptive contexts where the full, formal title is not necessary."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    shortTitle__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_shortTitle", title="Extension field for ``shortTitle``."
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this evidence. Enables tracking the life-cycle of the "
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

    subtitle: fhirtypes.String = Field(
        None,
        alias="subtitle",
        title="Subordinate title of the Evidence",
        description=(
            "An explanatory or alternate title for the Evidence giving additional "
            "information about its content."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    subtitle__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_subtitle", title="Extension field for ``subtitle``."
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Name for this evidence (human friendly)",
        description="A short, descriptive, user-friendly title for the evidence.",
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    topic: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="topic",
        title=(
            "The category of the Evidence, such as Education, Treatment, "
            "Assessment, etc."
        ),
        description=(
            "Descriptive topics related to the content of the Evidence. Topics "
            "provide a high-level categorization grouping types of Evidences that "
            "can be useful for filtering and searching."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title=(
            "Canonical identifier for this evidence, represented as a URI (globally"
            " unique)"
        ),
        description=(
            "An absolute URI that is used to identify this evidence when it is "
            "referenced in a specification, model, design or an instance; also "
            "called its canonical identifier. This SHOULD be globally unique and "
            "SHOULD be a literal address at which at which an authoritative "
            "instance of this evidence is (or will be) published. This URL can be "
            "the target of a canonical reference. It SHALL remain the same when the"
            " evidence is stored on different servers."
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

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the evidence",
        description=(
            "The identifier that is used to identify this version of the evidence "
            "when it is referenced in a specification, model, design or instance. "
            "This is an arbitrary value managed by the evidence author and is not "
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
