from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Composition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

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

    __resource_type__ = "Composition"

    attester: typing.List[fhirtypes.CompositionAttesterType] | None = Field(  # type: ignore
        None,
        alias="attester",
        title="Attests to accuracy of composition",
        description=(
            "A participant who has attested to the accuracy of the "
            "composition/document."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    author: typing.List[fhirtypes.ReferenceType] = Field(  # type: ignore
        ...,
        alias="author",
        title="Who and/or what authored the composition",
        description=(
            "Identifies who is responsible for the information in the composition, "
            "not necessarily who typed it in."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Device",
                "Patient",
                "RelatedPerson",
                "Organization",
            ],
        },
    )

    category: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="category",
        title="Categorization of Composition",
        description=(
            "A categorization for the type of the composition - helps for indexing "
            "and searching. This may be implied by or derived from the code "
            "specified in the Composition Type."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    confidentiality: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="confidentiality",
        title="As defined by affinity domain",
        description="The code specifying the level of confidentiality of the Composition.",
        json_schema_extra={
            "element_property": True,
        },
    )
    confidentiality__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_confidentiality", title="Extension field for ``confidentiality``."
    )

    custodian: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="custodian",
        title="Organization which maintains the composition",
        description=(
            "Identifies the organization or group who is responsible for ongoing "
            "maintenance of and access to the composition/document information."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="date",
        title="Composition editing time",
        description=(
            "The composition editing time, when the composition was last logically "
            "changed by the author."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    encounter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="encounter",
        title="Context of the Composition",
        description=(
            "Describes the clinical encounter or type of care this documentation is"
            " associated with."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter"],
        },
    )

    event: typing.List[fhirtypes.CompositionEventType] | None = Field(  # type: ignore
        None,
        alias="event",
        title="The clinical service(s) being documented",
        description=(
            "The clinical service, such as a colonoscopy or an appendectomy, being "
            "documented."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Version-independent identifier for the Composition",
        description=(
            "A version-independent identifier for the Composition. This identifier "
            "stays constant as the composition is changed over time."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    relatesTo: typing.List[fhirtypes.CompositionRelatesToType] | None = Field(  # type: ignore
        None,
        alias="relatesTo",
        title="Relationships to other compositions/documents",
        description=(
            "Relationships that this composition has with other compositions or "
            "documents that already exist."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    section: typing.List[fhirtypes.CompositionSectionType] | None = Field(  # type: ignore
        None,
        alias="section",
        title="Composition is broken into sections",
        description="The root of the sections that make up the composition.",
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="preliminary | final | amended | entered-in-error",
        description=(
            "The workflow/clinical status of this composition. The status is a "
            "marker for the clinical standing of the document."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["preliminary", "final", "amended", "entered-in-error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="subject",
        title="Who and/or what the composition is about",
        description=(
            "Who or what the composition is about. The composition can be about a "
            "person, (patient or healthcare practitioner), a device (e.g. a "
            "machine) or even a group of subjects (such as a document about a herd "
            "of livestock, or a set of patients that share a common exposure)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Human Readable name/title",
        description="Official human-readable label for the composition.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Kind of composition (LOINC if possible)",
        description=(
            "Specifies the particular kind of composition (e.g. History and "
            "Physical, Discharge Summary, Progress Note). This usually equates to "
            "the purpose of making the composition."
        ),
        json_schema_extra={
            "element_property": True,
        },
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
            "identifier",
            "status",
            "type",
            "category",
            "subject",
            "encounter",
            "date",
            "author",
            "title",
            "confidentiality",
            "attester",
            "custodian",
            "relatesTo",
            "event",
            "section",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
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
        return required_fields


class CompositionAttester(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Attests to accuracy of composition.
    A participant who has attested to the accuracy of the composition/document.
    """

    __resource_type__ = "CompositionAttester"

    mode: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="mode",
        title="personal | professional | legal | official",
        description="The type of attestation the authenticator offers.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["personal", "professional", "legal", "official"],
        },
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_mode", title="Extension field for ``mode``."
    )

    party: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="party",
        title="Who attested the composition",
        description="Who attested the composition in the specified way.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Patient",
                "RelatedPerson",
                "Practitioner",
                "PractitionerRole",
                "Organization",
            ],
        },
    )

    time: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="time",
        title="When the composition was attested",
        description="When the composition was attested by the party.",
        json_schema_extra={
            "element_property": True,
        },
    )
    time__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_time", title="Extension field for ``time``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CompositionAttester`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "mode", "time", "party"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("mode", "mode__ext")]
        return required_fields


class CompositionEvent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The clinical service(s) being documented.
    The clinical service, such as a colonoscopy or an appendectomy, being
    documented.
    """

    __resource_type__ = "CompositionEvent"

    code: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="code",
        title="Code(s) that apply to the event being documented",
        description=(
            "This list of codes represents the main clinical acts, such as a "
            "colonoscopy or an appendectomy, being documented. In some cases, the "
            'event is inherent in the typeCode, such as a "History and Physical '
            'Report" in which the procedure being documented is necessarily a '
            '"History and Physical" act.'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    detail: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="detail",
        title="The event(s) being documented",
        description=(
            "The description and/or reference of the event(s) being documented. For"
            " example, this could be used to document such a colonoscopy or an "
            "appendectomy."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="period",
        title="The period covered by the documentation",
        description=(
            "The period of time covered by the documentation. There is no assertion"
            " that the documentation is a complete representation for this period, "
            "only that it documents events during this time."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CompositionEvent`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "period", "detail"]


class CompositionRelatesTo(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Relationships to other compositions/documents.
    Relationships that this composition has with other compositions or
    documents that already exist.
    """

    __resource_type__ = "CompositionRelatesTo"

    code: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="code",
        title="replaces | transforms | signs | appends",
        description=(
            "The type of relationship that this composition has with anther "
            "composition or document."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["replaces", "transforms", "signs", "appends"],
        },
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_code", title="Extension field for ``code``."
    )

    targetIdentifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="targetIdentifier",
        title="Target of the relationship",
        description="The target composition/document of this relationship.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e target[x]
            "one_of_many": "target",
            "one_of_many_required": True,
        },
    )

    targetReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="targetReference",
        title="Target of the relationship",
        description="The target composition/document of this relationship.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e target[x]
            "one_of_many": "target",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Composition"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CompositionRelatesTo`` according specification,
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

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("code", "code__ext")]
        return required_fields

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
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
        return one_of_many_fields


class CompositionSection(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Composition is broken into sections.
    The root of the sections that make up the composition.
    """

    __resource_type__ = "CompositionSection"

    author: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="author",
        title="Who and/or what authored the section",
        description=(
            "Identifies who is responsible for the information in this section, not"
            " necessarily who typed it in."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Device",
                "Patient",
                "RelatedPerson",
                "Organization",
            ],
        },
    )

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Classification of section (recommended)",
        description=(
            "A code identifying the kind of content contained within the section. "
            "This must be consistent with the section title."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    emptyReason: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="emptyReason",
        title="Why the section is empty",
        description=(
            "If the section is empty, why the list is empty. An empty section "
            "typically has some text explaining the empty reason."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    entry: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="entry",
        title="A reference to data that supports this section",
        description=(
            "A reference to the actual resource from which the narrative in the "
            "section is derived."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    focus: fhirtypes.ReferenceType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    mode: fhirtypes.CodeType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["working", "snapshot", "changes"],
        },
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_mode", title="Extension field for ``mode``."
    )

    orderedBy: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="orderedBy",
        title="Order of section entries",
        description="Specifies the order applied to the items in the section entries.",
        json_schema_extra={
            "element_property": True,
        },
    )

    section: typing.List[fhirtypes.CompositionSectionType] | None = Field(  # type: ignore
        None,
        alias="section",
        title="Nested Section",
        description="A nested sub-section within this section.",
        json_schema_extra={
            "element_property": True,
        },
    )

    text: fhirtypes.NarrativeType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Label for section (e.g. for ToC)",
        description=(
            "The label for this particular section.  This will be part of the "
            "rendered content for the document, and is often used to build a table "
            "of contents."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
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
            "mode",
            "orderedBy",
            "entry",
            "emptyReason",
            "section",
        ]
