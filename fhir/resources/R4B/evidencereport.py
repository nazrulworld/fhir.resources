# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EvidenceReport
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class EvidenceReport(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A EvidenceReport.
    The EvidenceReport Resource is a specialized container for a collection of
    resources and codable concepts, adapted to support compositions of
    Evidence, EvidenceVariable, and Citation resources and related concepts.
    """

    resource_type = Field("EvidenceReport", const=True)

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

    citeAsMarkdown: fhirtypes.Markdown = Field(
        None,
        alias="citeAsMarkdown",
        title="Citation for this report",
        description="Citation Resource or display of suggested citation for this report.",
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
        title="Citation for this report",
        description="Citation Resource or display of suggested citation for this report.",
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

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Unique identifier for the evidence report",
        description=(
            "A formal identifier that is used to identify this EvidenceReport when "
            "it is represented in other formats, or referenced in a specification, "
            "model, design or an instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Used for footnotes and annotations",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the organization or individual that published the evidence"
            " report."
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
        title="Link, description or reference to artifact associated with the report",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    relatedIdentifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="relatedIdentifier",
        title=(
            "Identifiers for articles that may relate to more than one evidence "
            "report"
        ),
        description=(
            "A formal identifier that is used to identify things closely related to"
            " this EvidenceReport."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    relatesTo: typing.List[fhirtypes.EvidenceReportRelatesToType] = Field(
        None,
        alias="relatesTo",
        title="Relationships to other compositions/documents",
        description=(
            "Relationships that this composition has with other compositions or "
            "documents that already exist."
        ),
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

    section: typing.List[fhirtypes.EvidenceReportSectionType] = Field(
        None,
        alias="section",
        title="Composition is broken into sections",
        description="The root of the sections that make up the composition.",
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

    subject: fhirtypes.EvidenceReportSubjectType = Field(
        ...,
        alias="subject",
        title="Focus of the report",
        description=(
            'Specifies the subject or focus of the report. Answers "What is this '
            'report about?".'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Kind of report",
        description=(
            "Specifies the kind of report, such as grouping of classifiers, search "
            "results, or human-compiled expression."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title=(
            "Canonical identifier for this EvidenceReport, represented as a "
            "globally unique URI"
        ),
        description=(
            "An absolute URI that is used to identify this EvidenceReport when it "
            "is referenced in a specification, model, design or an instance; also "
            "called its canonical identifier. This SHOULD be globally unique and "
            "SHOULD be a literal address at which at which an authoritative "
            "instance of this summary is (or will be) published. This URL can be "
            "the target of a canonical reference. It SHALL remain the same when the"
            " summary is stored on different servers."
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
            "indexing and searching for appropriate evidence report instances."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EvidenceReport`` according specification,
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
            "status",
            "useContext",
            "identifier",
            "relatedIdentifier",
            "citeAsReference",
            "citeAsMarkdown",
            "type",
            "note",
            "relatedArtifact",
            "subject",
            "publisher",
            "contact",
            "author",
            "editor",
            "reviewer",
            "endorser",
            "relatesTo",
            "section",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1624(
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
    def validate_one_of_many_1624(
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
        one_of_many_fields = {"citeAs": ["citeAsMarkdown", "citeAsReference"]}
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


class EvidenceReportRelatesTo(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Relationships to other compositions/documents.
    Relationships that this composition has with other compositions or
    documents that already exist.
    """

    resource_type = Field("EvidenceReportRelatesTo", const=True)

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title=(
            "replaces | amends | appends | transforms | replacedWith | amendedWith "
            "| appendedWith | transformedWith"
        ),
        description=(
            "The type of relationship that this composition has with anther "
            "composition or document."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "replaces",
            "amends",
            "appends",
            "transforms",
            "replacedWith",
            "amendedWith",
            "appendedWith",
            "transformedWith",
        ],
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    targetIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="targetIdentifier",
        title="Target of the relationship",
        description="The target composition/document of this relationship.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e target[x]
        one_of_many="target",
        one_of_many_required=True,
    )

    targetReference: fhirtypes.ReferenceType = Field(
        None,
        alias="targetReference",
        title="Target of the relationship",
        description="The target composition/document of this relationship.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e target[x]
        one_of_many="target",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["EvidenceReport"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EvidenceReportRelatesTo`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "targetIdentifier",
            "targetReference",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2534(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2534(
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
        one_of_many_fields = {"target": ["targetIdentifier", "targetReference"]}
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


class EvidenceReportSection(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Composition is broken into sections.
    The root of the sections that make up the composition.
    """

    resource_type = Field("EvidenceReportSection", const=True)

    author: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="author",
        title="Who and/or what authored the section",
        description=(
            "Identifies who is responsible for the information in this section, not"
            " necessarily who typed it in."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Person", "Device", "Group", "Organization"],
    )

    emptyReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="emptyReason",
        title="Why the section is empty",
        description=(
            "If the section is empty, why the list is empty. An empty section "
            "typically has some text explaining the empty reason."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    entryClassifier: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="entryClassifier",
        title="Extensible classifiers as content",
        description="Specifies any type of classification of the evidence report.",
        # if property is element of this resource.
        element_property=True,
    )

    entryQuantity: typing.List[fhirtypes.QuantityType] = Field(
        None,
        alias="entryQuantity",
        title="Quantity as content",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    entryReference: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="entryReference",
        title="Reference to resources as content",
        description=(
            "A reference to the actual resource from which the narrative in the "
            "section is derived."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    focus: fhirtypes.CodeableConceptType = Field(
        None,
        alias="focus",
        title="Classification of section (recommended)",
        description=(
            "A code identifying the kind of content contained within the section. "
            "This should be consistent with the section title."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    focusReference: fhirtypes.ReferenceType = Field(
        None,
        alias="focusReference",
        title="Classification of section by Resource",
        description=(
            "A definitional Resource identifying the kind of content contained "
            "within the section. This should be consistent with the section title."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    mode: fhirtypes.Code = Field(
        None,
        alias="mode",
        title="working | snapshot | changes",
        description=(
            "How the entry list was prepared - whether it is a working list that is"
            " suitable for being maintained on an ongoing basis, or if it "
            "represents a snapshot of a list of items from another source, or "
            "whether it is a prepared list where items may be marked as added, "
            "modified or deleted."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["working", "snapshot", "changes"],
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_mode", title="Extension field for ``mode``."
    )

    orderedBy: fhirtypes.CodeableConceptType = Field(
        None,
        alias="orderedBy",
        title="Order of section entries",
        description="Specifies the order applied to the items in the section entries.",
        # if property is element of this resource.
        element_property=True,
    )

    section: typing.List[fhirtypes.EvidenceReportSectionType] = Field(
        None,
        alias="section",
        title="Nested Section",
        description="A nested sub-section within this section.",
        # if property is element of this resource.
        element_property=True,
    )

    text: fhirtypes.NarrativeType = Field(
        None,
        alias="text",
        title="Text summary of the section, for human interpretation",
        description=(
            "A human-readable narrative that contains the attested content of the "
            "section, used to represent the content of the resource to a human. The"
            " narrative need not encode all the structured data, but is peferred to"
            " contain sufficient detail to make it acceptable for a human to just "
            "read the narrative."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Label for section (e.g. for ToC)",
        description=(
            "The label for this particular section.  This will be part of the "
            "rendered content for the document, and is often used to build a table "
            "of contents."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EvidenceReportSection`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "title",
            "focus",
            "focusReference",
            "author",
            "text",
            "mode",
            "orderedBy",
            "entryClassifier",
            "entryReference",
            "entryQuantity",
            "emptyReason",
            "section",
        ]


class EvidenceReportSubject(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Focus of the report.
    Specifies the subject or focus of the report. Answers "What is this report
    about?".
    """

    resource_type = Field("EvidenceReportSubject", const=True)

    characteristic: typing.List[
        fhirtypes.EvidenceReportSubjectCharacteristicType
    ] = Field(
        None,
        alias="characteristic",
        title="Characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Footnotes and/or explanatory notes",
        description="Used for general notes and annotations not coded elsewhere.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EvidenceReportSubject`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "characteristic", "note"]


class EvidenceReportSubjectCharacteristic(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Characteristic.
    """

    resource_type = Field("EvidenceReportSubjectCharacteristic", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Characteristic code",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    exclude: bool = Field(
        None,
        alias="exclude",
        title="Is used to express not the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    exclude__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_exclude", title="Extension field for ``exclude``."
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Timeframe for the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="Characteristic value",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="valueCodeableConcept",
        title="Characteristic value",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="Characteristic value",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueRange: fhirtypes.RangeType = Field(
        None,
        alias="valueRange",
        title="Characteristic value",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueReference",
        title="Characteristic value",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EvidenceReportSubjectCharacteristic`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "valueReference",
            "valueCodeableConcept",
            "valueBoolean",
            "valueQuantity",
            "valueRange",
            "exclude",
            "period",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3776(
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
            "value": [
                "valueBoolean",
                "valueCodeableConcept",
                "valueQuantity",
                "valueRange",
                "valueReference",
            ]
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
