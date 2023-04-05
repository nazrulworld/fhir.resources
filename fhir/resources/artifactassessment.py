# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ArtifactAssessment
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class ArtifactAssessment(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Adds metadata-supported comments, classifiers or ratings related to a
    Resource.
    This Resource provides one or more comments, classifiers or ratings about a
    Resource and supports attribution and rights management metadata for the
    added content.
    """

    resource_type = Field("ArtifactAssessment", const=True)

    approvalDate: fhirtypes.Date = Field(
        None,
        alias="approvalDate",
        title="When the artifact assessment was approved by publisher",
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

    artifactCanonical: fhirtypes.Canonical = Field(
        None,
        alias="artifactCanonical",
        title="The artifact assessed, commented upon or rated",
        description=(
            "A reference to a resource, canonical resource, or non-FHIR resource "
            "which the comment or assessment is about."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e artifact[x]
        one_of_many="artifact",
        one_of_many_required=True,
    )
    artifactCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_artifactCanonical",
        title="Extension field for ``artifactCanonical``.",
    )

    artifactReference: fhirtypes.ReferenceType = Field(
        None,
        alias="artifactReference",
        title="The artifact assessed, commented upon or rated",
        description=(
            "A reference to a resource, canonical resource, or non-FHIR resource "
            "which the comment or assessment is about."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e artifact[x]
        one_of_many="artifact",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    artifactUri: fhirtypes.Uri = Field(
        None,
        alias="artifactUri",
        title="The artifact assessed, commented upon or rated",
        description=(
            "A reference to a resource, canonical resource, or non-FHIR resource "
            "which the comment or assessment is about."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e artifact[x]
        one_of_many="artifact",
        one_of_many_required=True,
    )
    artifactUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_artifactUri", title="Extension field for ``artifactUri``."
    )

    citeAsMarkdown: fhirtypes.Markdown = Field(
        None,
        alias="citeAsMarkdown",
        title="How to cite the comment or rating",
        description=(
            "Display of or reference to the bibliographic citation of the comment, "
            "classifier, or rating."
        ),
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
        title="How to cite the comment or rating",
        description=(
            "Display of or reference to the bibliographic citation of the comment, "
            "classifier, or rating."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e citeAs[x]
        one_of_many="citeAs",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Citation"],
    )

    content: typing.List[fhirtypes.ArtifactAssessmentContentType] = Field(
        None,
        alias="content",
        title="Comment, classifier, or rating content",
        description="A component comment, classifier, or rating of the artifact.",
        # if property is element of this resource.
        element_property=True,
    )

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the artifact assessment and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the artifact assessment."
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
            "The date  (and optionally time) when the artifact assessment was "
            "published. The date must change when the disposition changes and it "
            "must change if the workflow status code changes. In addition, it "
            "should change when the substantive content of the artifact assessment "
            "changes."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    disposition: fhirtypes.Code = Field(
        None,
        alias="disposition",
        title=(
            "unresolved | not-persuasive | persuasive | persuasive-with-"
            "modification | not-persuasive-with-modification"
        ),
        description=(
            "Indicates the disposition of the responsible party to the comment or "
            "change request."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "unresolved",
            "not-persuasive",
            "persuasive",
            "persuasive-with-modification",
            "not-persuasive-with-modification",
        ],
    )
    disposition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_disposition", title="Extension field for ``disposition``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Additional identifier for the artifact assessment",
        description=(
            "A formal identifier that is used to identify this artifact assessment "
            "when it is represented in other formats, or referenced in a "
            "specification, model, design or an instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    lastReviewDate: fhirtypes.Date = Field(
        None,
        alias="lastReviewDate",
        title="When the artifact assessment was last reviewed by the publisher",
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

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="A short title for the assessment for use in displaying and selecting",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    workflowStatus: fhirtypes.Code = Field(
        None,
        alias="workflowStatus",
        title=(
            "submitted | triaged | waiting-for-input | resolved-no-change | "
            "resolved-change-required | deferred | duplicate | applied | published "
            "| entered-in-error"
        ),
        description="Indicates the workflow status of the comment or change request.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "submitted",
            "triaged",
            "waiting-for-input",
            "resolved-no-change",
            "resolved-change-required",
            "deferred",
            "duplicate",
            "applied",
            "published",
            "entered-in-error",
        ],
    )
    workflowStatus__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_workflowStatus", title="Extension field for ``workflowStatus``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ArtifactAssessment`` according specification,
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
            "title",
            "citeAsReference",
            "citeAsMarkdown",
            "date",
            "copyright",
            "approvalDate",
            "lastReviewDate",
            "artifactReference",
            "artifactCanonical",
            "artifactUri",
            "content",
            "workflowStatus",
            "disposition",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2057(
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
            "artifact": ["artifactCanonical", "artifactReference", "artifactUri"],
            "citeAs": ["citeAsMarkdown", "citeAsReference"],
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


class ArtifactAssessmentContent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Comment, classifier, or rating content.
    A component comment, classifier, or rating of the artifact.
    """

    resource_type = Field("ArtifactAssessmentContent", const=True)

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title="Who authored the content",
        description="Indicates who or what authored the content.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "Practitioner",
            "PractitionerRole",
            "Organization",
            "Device",
        ],
    )

    classifier: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="classifier",
        title="Rating, classifier, or assessment",
        description="Represents a rating, classifier, or assessment of the artifact.",
        # if property is element of this resource.
        element_property=True,
    )

    component: typing.List[fhirtypes.ArtifactAssessmentContentType] = Field(
        None,
        alias="component",
        title="Contained content",
        description="If the informationType is container, the components of the content.",
        # if property is element of this resource.
        element_property=True,
    )

    freeToShare: bool = Field(
        None,
        alias="freeToShare",
        title="Acceptable to publicly share the resource content",
        description="Acceptable to publicly share the comment, classifier or rating.",
        # if property is element of this resource.
        element_property=True,
    )
    freeToShare__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_freeToShare", title="Extension field for ``freeToShare``."
    )

    informationType: fhirtypes.Code = Field(
        None,
        alias="informationType",
        title="comment | classifier | rating | container | response | change-request",
        description="The type of information this component of the content represents.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "comment",
            "classifier",
            "rating",
            "container",
            "response",
            "change-request",
        ],
    )
    informationType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_informationType", title="Extension field for ``informationType``."
    )

    path: typing.List[typing.Optional[fhirtypes.Uri]] = Field(
        None,
        alias="path",
        title="What the comment is directed to",
        description=(
            "A URI that points to what the comment is about, such as a line of text"
            " in the CQL, or a specific element in a resource."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    path__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_path", title="Extension field for ``path``.")

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Quantitative rating",
        description="A quantitative rating of the artifact.",
        # if property is element of this resource.
        element_property=True,
    )

    relatedArtifact: typing.List[fhirtypes.RelatedArtifactType] = Field(
        None,
        alias="relatedArtifact",
        title="Additional information",
        description=(
            "Additional related artifacts that provide supporting documentation, "
            "additional evidence, or further information related to the content."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    summary: fhirtypes.Markdown = Field(
        None,
        alias="summary",
        title="Brief summary of the content",
        description="A brief summary of the content of this component.",
        # if property is element of this resource.
        element_property=True,
    )
    summary__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_summary", title="Extension field for ``summary``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="What type of content",
        description="Indicates what type of content this component represents.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ArtifactAssessmentContent`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "informationType",
            "summary",
            "type",
            "classifier",
            "quantity",
            "author",
            "path",
            "relatedArtifact",
            "freeToShare",
            "component",
        ]
