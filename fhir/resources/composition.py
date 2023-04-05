# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Composition
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


class Composition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A set of resources composed into a single coherent clinical statement with
    clinical attestation.
    A set of healthcare-related information that is assembled together into a
    single logical package that provides a single coherent statement of
    meaning, establishes its own context and that has clinical attestation with
    regard to who is making the statement. A Composition defines the structure
    and narrative content necessary for a document. However, a Composition
    alone does not constitute a document. Rather, the Composition must be the
    first entry in a Bundle where Bundle.type=document, and any other resources
    referenced from Composition must be included as subsequent entries in the
    Bundle (for example Patient, Practitioner, Encounter, etc.).
    """

    resource_type = Field("Composition", const=True)

    attester: typing.List[fhirtypes.CompositionAttesterType] = Field(
        None,
        alias="attester",
        title="Attests to accuracy of composition",
        description=(
            "A participant who has attested to the accuracy of the "
            "composition/document."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    author: typing.List[fhirtypes.ReferenceType] = Field(
        ...,
        alias="author",
        title="Who and/or what authored the composition",
        description=(
            "Identifies who is responsible for the information in the composition, "
            "not necessarily who typed it in."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "Device",
            "Patient",
            "RelatedPerson",
            "Organization",
        ],
    )

    category: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="Categorization of Composition",
        description=(
            "A categorization for the type of the composition - helps for indexing "
            "and searching. This may be implied by or derived from the code "
            "specified in the Composition Type."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    custodian: fhirtypes.ReferenceType = Field(
        None,
        alias="custodian",
        title="Organization which maintains the composition",
        description=(
            "Identifies the organization or group who is responsible for ongoing "
            "maintenance of and access to the composition/document information."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Composition editing time",
        description=(
            "The composition editing time, when the composition was last logically "
            "changed by the author."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Context of the Composition",
        description=(
            "Describes the clinical encounter or type of care this documentation is"
            " associated with."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    event: typing.List[fhirtypes.CompositionEventType] = Field(
        None,
        alias="event",
        title="The clinical service(s) being documented",
        description=(
            "The clinical service, such as a colonoscopy or an appendectomy, being "
            "documented."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Version-independent identifier for the Composition",
        description=(
            "A version-independent identifier for the Composition. This identifier "
            "stays constant as the composition is changed over time."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name for this Composition (computer friendly)",
        description=(
            "A natural language name identifying the {{title}}. This name should be"
            " usable as an identifier for the module by machine processing "
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
        title="For any additional notes",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    relatesTo: typing.List[fhirtypes.RelatedArtifactType] = Field(
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

    section: typing.List[fhirtypes.CompositionSectionType] = Field(
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
        title=(
            "registered | partial | preliminary | final | amended | corrected | "
            "appended | cancelled | entered-in-error | deprecated | unknown"
        ),
        description=(
            "The workflow/clinical status of this composition. The status is a "
            "marker for the clinical standing of the document."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "registered",
            "partial",
            "preliminary",
            "final",
            "amended",
            "corrected",
            "appended",
            "cancelled",
            "entered-in-error",
            "deprecated",
            "unknown",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="subject",
        title="Who and/or what the composition is about",
        description=(
            "Who or what the composition is about. The composition can be about a "
            "person, (patient or healthcare practitioner), a device (e.g. a "
            "machine) or even a group of subjects (such as a document about a herd "
            "of livestock, or a set of patients that share a common exposure)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Human Readable name/title",
        description="Official human-readable label for the composition.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Kind of composition (LOINC if possible)",
        description=(
            "Specifies the particular kind of composition (e.g. History and "
            "Physical, Discharge Summary, Progress Note). This usually equates to "
            "the purpose of making the composition."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title=(
            "Canonical identifier for this Composition, represented as a URI "
            "(globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this Composition when it is "
            "referenced in a specification, model, design or an instance; also "
            "called its canonical identifier. This SHOULD be globally unique and "
            "SHOULD be a literal address at which an authoritative instance of this"
            " Composition is (or will be) published. This URL can be the target of "
            "a canonical reference. It SHALL remain the same when the Composition "
            "is stored on different servers."
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
            "indexing and searching for appropriate Composition instances."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title=(
            "An explicitly assigned identifer of a variation of the content in the "
            "Composition"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Composition`` according specification,
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
            "status",
            "type",
            "category",
            "subject",
            "encounter",
            "date",
            "useContext",
            "author",
            "name",
            "title",
            "note",
            "attester",
            "custodian",
            "relatesTo",
            "event",
            "section",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1349(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("date", "date__ext"),
            ("status", "status__ext"),
            ("title", "title__ext"),
        ]
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


class CompositionAttester(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Attests to accuracy of composition.
    A participant who has attested to the accuracy of the composition/document.
    """

    resource_type = Field("CompositionAttester", const=True)

    mode: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="mode",
        title="personal | professional | legal | official",
        description="The type of attestation the authenticator offers.",
        # if property is element of this resource.
        element_property=True,
    )

    party: fhirtypes.ReferenceType = Field(
        None,
        alias="party",
        title="Who attested the composition",
        description="Who attested the composition in the specified way.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "RelatedPerson",
            "Practitioner",
            "PractitionerRole",
            "Organization",
        ],
    )

    time: fhirtypes.DateTime = Field(
        None,
        alias="time",
        title="When the composition was attested",
        description="When the composition was attested by the party.",
        # if property is element of this resource.
        element_property=True,
    )
    time__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_time", title="Extension field for ``time``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CompositionAttester`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "mode", "time", "party"]


class CompositionEvent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The clinical service(s) being documented.
    The clinical service, such as a colonoscopy or an appendectomy, being
    documented.
    """

    resource_type = Field("CompositionEvent", const=True)

    detail: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="detail",
        title="The event(s) being documented, as code(s), reference(s), or both",
        description=(
            "Represents the main clinical acts, such as a colonoscopy or an "
            "appendectomy, being documented. In some cases, the event is inherent "
            'in the typeCode, such as a "History and Physical Report" in which case'
            ' the procedure being documented is necessarily a "History and '
            'Physical" act. The events may be included as a code or as a reference '
            "to an other resource."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="The period covered by the documentation",
        description=(
            "The period of time covered by the documentation. There is no assertion"
            " that the documentation is a complete representation for this period, "
            "only that it documents events during this time."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CompositionEvent`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "period", "detail"]


class CompositionSection(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Composition is broken into sections.
    The root of the sections that make up the composition.
    """

    resource_type = Field("CompositionSection", const=True)

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
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "Device",
            "Patient",
            "RelatedPerson",
            "Organization",
        ],
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Classification of section (recommended)",
        description=(
            "A code identifying the kind of content contained within the section. "
            "This must be consistent with the section title."
        ),
        # if property is element of this resource.
        element_property=True,
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

    entry: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="entry",
        title="A reference to data that supports this section",
        description=(
            "A reference to the actual resource from which the narrative in the "
            "section is derived."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    focus: fhirtypes.ReferenceType = Field(
        None,
        alias="focus",
        title=(
            "Who/what the section is about, when it is not about the subject of "
            "composition"
        ),
        description=(
            "The actual focus of the section when it is not the subject of the "
            "composition, but instead represents something or someone associated "
            "with the subject such as (for a patient subject) a spouse, parent, "
            "fetus, or donor. If not focus is specified, the focus is assumed to be"
            " focus of the parent section, or, for a section in the Composition "
            "itself, the subject of the composition. Sections with a focus SHALL "
            "only include resources where the logical subject (patient, subject, "
            "focus, etc.) matches the section focus, or the resources have no "
            "logical subject (few resources)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    orderedBy: fhirtypes.CodeableConceptType = Field(
        None,
        alias="orderedBy",
        title="Order of section entries",
        description="Specifies the order applied to the items in the section entries.",
        # if property is element of this resource.
        element_property=True,
    )

    section: typing.List[fhirtypes.CompositionSectionType] = Field(
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
            " narrative need not encode all the structured data, but is required to"
            ' contain sufficient detail to make it "clinically safe" for a human to'
            " just read the narrative."
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
        ``CompositionSection`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "title",
            "code",
            "author",
            "focus",
            "text",
            "orderedBy",
            "entry",
            "emptyReason",
            "section",
        ]
