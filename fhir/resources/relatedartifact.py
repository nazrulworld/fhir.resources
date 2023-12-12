# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/RelatedArtifact
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import datatype, fhirtypes


class RelatedArtifact(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Related artifacts for a knowledge resource.
    Related artifacts such as additional documentation, justification, or
    bibliographic references.
    """

    resource_type = Field("RelatedArtifact", const=True)

    citation: fhirtypes.Markdown = Field(
        None,
        alias="citation",
        title="Bibliographic citation for the artifact",
        description=(
            "A bibliographic citation for the related artifact. This text SHOULD be"
            " formatted according to an accepted citation format."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    citation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_citation", title="Extension field for ``citation``."
    )

    classifier: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="classifier",
        title="Additional classifiers",
        description="Provides additional classifiers of the related artifact.",
        # if property is element of this resource.
        element_property=True,
    )

    display: fhirtypes.String = Field(
        None,
        alias="display",
        title="Brief description of the related artifact",
        description=(
            "A brief description of the document or knowledge resource being "
            "referenced, suitable for display to a consumer."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_display", title="Extension field for ``display``."
    )

    document: fhirtypes.AttachmentType = Field(
        None,
        alias="document",
        title="What document is being referenced",
        description=(
            "The document being referenced, represented as an attachment. This is "
            "exclusive with the resource element."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    label: fhirtypes.String = Field(
        None,
        alias="label",
        title="Short label",
        description=(
            "A short label that can be used to reference the citation from "
            "elsewhere in the containing artifact, such as a footnote index."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    label__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_label", title="Extension field for ``label``."
    )

    publicationDate: fhirtypes.Date = Field(
        None,
        alias="publicationDate",
        title="Date of publication of the artifact being referred to",
        description="The date of publication of the artifact being referred to.",
        # if property is element of this resource.
        element_property=True,
    )
    publicationDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publicationDate", title="Extension field for ``publicationDate``."
    )

    publicationStatus: fhirtypes.Code = Field(
        None,
        alias="publicationStatus",
        title="draft | active | retired | unknown",
        description="The publication status of the artifact being referred to.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired", "unknown"],
    )
    publicationStatus__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_publicationStatus",
        title="Extension field for ``publicationStatus``.",
    )

    resource: fhirtypes.Canonical = Field(
        None,
        alias="resource",
        title="What artifact is being referenced",
        description=(
            "The related artifact, such as a library, value set, profile, or other "
            "knowledge resource."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )
    resource__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_resource", title="Extension field for ``resource``."
    )

    resourceReference: fhirtypes.ReferenceType = Field(
        None,
        alias="resourceReference",
        title="What artifact, if not a conformance resource",
        description=(
            "The related artifact, if the artifact is not a canonical resource, or "
            "a resource reference to a canonical resource."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title=(
            "documentation | justification | citation | predecessor | successor | "
            "derived-from | depends-on | composed-of | part-of | amends | amended-"
            "with | appends | appended-with | cites | cited-by | comments-on | "
            "comment-in | contains | contained-in | corrects | correction-in | "
            "replaces | replaced-with | retracts | retracted-by | signs | similar-"
            "to | supports | supported-with | transforms | transformed-into | "
            "transformed-with | documents | specification-of | created-with | cite-"
            "as"
        ),
        description="The type of relationship to the related artifact.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "documentation",
            "justification",
            "citation",
            "predecessor",
            "successor",
            "derived-from",
            "depends-on",
            "composed-of",
            "part-of",
            "amends",
            "amended-with",
            "appends",
            "appended-with",
            "cites",
            "cited-by",
            "comments-on",
            "comment-in",
            "contains",
            "contained-in",
            "corrects",
            "correction-in",
            "replaces",
            "replaced-with",
            "retracts",
            "retracted-by",
            "signs",
            "similar-to",
            "supports",
            "supported-with",
            "transforms",
            "transformed-into",
            "transformed-with",
            "documents",
            "specification-of",
            "created-with",
            "cite-as",
        ],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``RelatedArtifact`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "type",
            "classifier",
            "label",
            "display",
            "citation",
            "document",
            "resource",
            "resourceReference",
            "publicationStatus",
            "publicationDate",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1717(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("type", "type__ext")]
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
