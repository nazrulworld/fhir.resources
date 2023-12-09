# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DocumentReference
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


class DocumentReference(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A reference to a document.
    """

    resource_type = Field("DocumentReference", const=True)

    authenticator: fhirtypes.ReferenceType = Field(
        None,
        alias="authenticator",
        title="Who/what authenticated the document",
        description=(
            "Which person or organization authenticates that this document is " "valid."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Organization"],
    )

    author: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="author",
        title="Who and/or what authored the document",
        description=(
            "Identifies who is responsible for adding the information to the "
            "document."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "Organization",
            "Device",
            "Patient",
            "RelatedPerson",
        ],
    )

    class_fhir: fhirtypes.CodeableConceptType = Field(
        None,
        alias="class",
        title="Categorization of document",
        description=(
            "A categorization for the type of document referenced - helps for "
            "indexing and searching. This may be implied by or derived from the "
            "code specified in the DocumentReference.type."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    content: typing.List[fhirtypes.DocumentReferenceContentType] = Field(
        ...,
        alias="content",
        title="Document referenced",
        description=(
            "The document and format referenced. There may be multiple content "
            "element repetitions, each with a different format."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    context: fhirtypes.DocumentReferenceContextType = Field(
        None,
        alias="context",
        title="Clinical context of document",
        description="The clinical context in which the document was prepared.",
        # if property is element of this resource.
        element_property=True,
    )

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Document creation time",
        description="When the document was created.",
        # if property is element of this resource.
        element_property=True,
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
    )

    custodian: fhirtypes.ReferenceType = Field(
        None,
        alias="custodian",
        title="Organization which maintains the document",
        description=(
            "Identifies the organization or group who is responsible for ongoing "
            "maintenance of and access to the document."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Human-readable description (title)",
        description=(
            "Human-readable description of the source document. This is sometimes "
            'known as the "title".'
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    docStatus: fhirtypes.Code = Field(
        None,
        alias="docStatus",
        title="preliminary | final | appended | amended | entered-in-error",
        description="The status of the underlying document.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["preliminary", "final", "appended", "amended", "entered-in-error"],
    )
    docStatus__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_docStatus", title="Extension field for ``docStatus``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Other identifiers for the document",
        description=(
            "Other identifiers associated with the document, including version "
            "independent identifiers."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    indexed: fhirtypes.Instant = Field(
        None,
        alias="indexed",
        title="When this document reference was created",
        description="When the document reference was created.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    indexed__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_indexed", title="Extension field for ``indexed``."
    )

    masterIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="masterIdentifier",
        title="Master Version Specific Identifier",
        description=(
            "Document identifier as assigned by the source of the document. This "
            "identifier is specific to this version of the document. This unique "
            "identifier may be used elsewhere to identify this version of the "
            "document."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    relatesTo: typing.List[fhirtypes.DocumentReferenceRelatesToType] = Field(
        None,
        alias="relatesTo",
        title="Relationships to other documents",
        description=(
            "Relationships that this document has with other document references "
            "that already exist."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    securityLabel: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="securityLabel",
        title="Document security-tags",
        description=(
            "A set of Security-Tag codes specifying the level of privacy/security "
            "of the Document. Note that DocumentReference.meta.security contains "
            'the security labels of the "reference" to the document, while '
            "DocumentReference.securityLabel contains a snapshot of the security "
            "labels on the document the reference refers to."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="current | superseded | entered-in-error",
        description="The status of this document reference.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["current", "superseded", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Who/what is the subject of the document",
        description=(
            "Who or what the document is about. The document can be about a person,"
            " (patient or healthcare practitioner), a device (e.g. a machine) or "
            "even a group of subjects (such as a document about a herd of farm "
            "animals, or a set of patients that share a common exposure)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Practitioner", "Group", "Device"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Kind of document (LOINC if possible)",
        description=(
            "Specifies the particular kind of document referenced  (e.g. History "
            "and Physical, Discharge Summary, Progress Note). This usually equates "
            "to the purpose of making the document referenced."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DocumentReference`` according specification,
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
            "masterIdentifier",
            "identifier",
            "status",
            "docStatus",
            "type",
            "class",
            "subject",
            "created",
            "indexed",
            "author",
            "authenticator",
            "custodian",
            "relatesTo",
            "description",
            "securityLabel",
            "content",
            "context",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1911(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("indexed", "indexed__ext"), ("status", "status__ext")]
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


class DocumentReferenceContent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Document referenced.
    The document and format referenced. There may be multiple content element
    repetitions, each with a different format.
    """

    resource_type = Field("DocumentReferenceContent", const=True)

    attachment: fhirtypes.AttachmentType = Field(
        ...,
        alias="attachment",
        title="Where to access the document",
        description=(
            "The document or URL of the document along with critical metadata to "
            "prove content has integrity."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    format: fhirtypes.CodingType = Field(
        None,
        alias="format",
        title="Format/content rules for the document",
        description=(
            "An identifier of the document encoding, structure, and template that "
            "the document conforms to beyond the base format indicated in the "
            "mimeType."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DocumentReferenceContent`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "attachment", "format"]


class DocumentReferenceContext(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Clinical context of document.
    The clinical context in which the document was prepared.
    """

    resource_type = Field("DocumentReferenceContext", const=True)

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Context of the document  content",
        description=(
            "Describes the clinical encounter or type of care that the document "
            "content is associated with."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    event: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="event",
        title="Main clinical acts documented",
        description=(
            "This list of codes represents the main clinical acts, such as a "
            "colonoscopy or an appendectomy, being documented. In some cases, the "
            'event is inherent in the typeCode, such as a "History and Physical '
            'Report" in which the procedure being documented is necessarily a '
            '"History and Physical" act.'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    facilityType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="facilityType",
        title="Kind of facility where patient was seen",
        description="The kind of facility where the patient was seen.",
        # if property is element of this resource.
        element_property=True,
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Time of service that is being documented",
        description=(
            "The time period over which the service that is described by the "
            "document was provided."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    practiceSetting: fhirtypes.CodeableConceptType = Field(
        None,
        alias="practiceSetting",
        title=(
            "Additional details about where the content was created (e.g. clinical "
            "specialty)"
        ),
        description=(
            "This property may convey specifics about the practice setting where "
            "the content was created, often reflecting the clinical specialty."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    related: typing.List[fhirtypes.DocumentReferenceContextRelatedType] = Field(
        None,
        alias="related",
        title="Related identifiers or resources",
        description=(
            "Related identifiers or resources associated with the " "DocumentReference."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    sourcePatientInfo: fhirtypes.ReferenceType = Field(
        None,
        alias="sourcePatientInfo",
        title="Patient demographics from source",
        description=(
            "The Patient Information as known when the document was published. May "
            "be a reference to a version specific, or contained."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DocumentReferenceContext`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "encounter",
            "event",
            "period",
            "facilityType",
            "practiceSetting",
            "sourcePatientInfo",
            "related",
        ]


class DocumentReferenceContextRelated(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Related identifiers or resources.
    Related identifiers or resources associated with the DocumentReference.
    """

    resource_type = Field("DocumentReferenceContextRelated", const=True)

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Identifier of related objects or events",
        description=(
            "Related identifier to this DocumentReference. If both id and ref are "
            "present they shall refer to the same thing."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    ref: fhirtypes.ReferenceType = Field(
        None,
        alias="ref",
        title="Related Resource",
        description=(
            "Related Resource to this DocumentReference. If both id and ref are "
            "present they shall refer to the same thing."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DocumentReferenceContextRelated`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "identifier", "ref"]


class DocumentReferenceRelatesTo(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Relationships to other documents.
    Relationships that this document has with other document references that
    already exist.
    """

    resource_type = Field("DocumentReferenceRelatesTo", const=True)

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="replaces | transforms | signs | appends",
        description="The type of relationship that this document has with anther document.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["replaces", "transforms", "signs", "appends"],
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    target: fhirtypes.ReferenceType = Field(
        ...,
        alias="target",
        title="Target of the relationship",
        description="The target document of this relationship.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DocumentReferenceRelatesTo`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "target"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2836(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("code", "code__ext")]
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
