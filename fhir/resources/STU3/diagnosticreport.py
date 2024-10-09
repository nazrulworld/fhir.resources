from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/DiagnosticReport
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class DiagnosticReport(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A Diagnostic report - a combination of request information, atomic results,
    images, interpretation, as well as formatted reports.
    The findings and interpretation of diagnostic  tests performed on patients,
    groups of patients, devices, and locations, and/or specimens derived from
    these. The report includes clinical context such as requesting and provider
    information, and some mix of atomic results, images, textual and coded
    interpretations, and formatted representation of diagnostic reports.
    """

    __resource_type__ = "DiagnosticReport"

    basedOn: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="basedOn",
        title="What was requested",
        description="Details concerning a test or procedure requested.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "CarePlan",
                "ImmunizationRecommendation",
                "MedicationRequest",
                "NutritionOrder",
                "ProcedureRequest",
                "ReferralRequest",
            ],
        },
    )

    category: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="category",
        title="Service category",
        description=(
            "A code that classifies the clinical discipline, department or "
            "diagnostic service that created the report (e.g. cardiology, "
            "biochemistry, hematology, MRI). This is used for searching, sorting "
            "and display purposes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    code: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="code",
        title="Name/Code for this diagnostic report",
        description="A code or name that describes this diagnostic report.",
        json_schema_extra={
            "element_property": True,
        },
    )

    codedDiagnosis: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="codedDiagnosis",
        title="Codes for the conclusion",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    conclusion: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="conclusion",
        title="Clinical Interpretation of test results",
        description=(
            "Concise and clinically contextualized impression / summary of the "
            "diagnostic report."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    conclusion__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_conclusion", title="Extension field for ``conclusion``."
    )

    context: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="context",
        title="Health care event when test ordered",
        description=(
            "The healthcare event  (e.g. a patient and healthcare provider "
            "interaction) which this DiagnosticReport per is about."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter", "EpisodeOfCare"],
        },
    )

    effectiveDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="effectiveDateTime",
        title="Clinically relevant time/time-period for report",
        description=(
            "The time or time-period the observed values are related to. When the "
            "subject of the report is a patient, this is usually either the time of"
            " the procedure or of specimen collection(s), but very often the source"
            " of the date/time is not known, only the date/time itself."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e effective[x]
            "one_of_many": "effective",
            "one_of_many_required": False,
        },
    )
    effectiveDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_effectiveDateTime",
        title="Extension field for ``effectiveDateTime``.",
    )

    effectivePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="effectivePeriod",
        title="Clinically relevant time/time-period for report",
        description=(
            "The time or time-period the observed values are related to. When the "
            "subject of the report is a patient, this is usually either the time of"
            " the procedure or of specimen collection(s), but very often the source"
            " of the date/time is not known, only the date/time itself."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e effective[x]
            "one_of_many": "effective",
            "one_of_many_required": False,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business identifier for report",
        description="Identifiers assigned to this report by the performer or other systems.",
        json_schema_extra={
            "element_property": True,
        },
    )

    image: typing.List[fhirtypes.DiagnosticReportImageType] | None = Field(  # type: ignore
        None,
        alias="image",
        title="Key images associated with this report",
        description=(
            "A list of key images associated with this report. The images are "
            "generally created during the diagnostic process, and may be directly "
            "of the patient, or of treated specimens (i.e. slides of interest)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    imagingStudy: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="imagingStudy",
        title=(
            "Reference to full details of imaging associated with the diagnostic "
            "report"
        ),
        description=(
            "One or more links to full details of any imaging performed during the "
            "diagnostic investigation. Typically, this is imaging performed by "
            "DICOM enabled modalities, but this is not required. A fully enabled "
            "PACS viewer can use this information to provide views of the source "
            "images."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ImagingStudy", "ImagingManifest"],
        },
    )

    issued: fhirtypes.InstantType | None = Field(  # type: ignore
        None,
        alias="issued",
        title="DateTime this version was released",
        description=(
            "The date and time that this version of the report was released from "
            "the source diagnostic service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    issued__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_issued", title="Extension field for ``issued``."
    )

    performer: typing.List[fhirtypes.DiagnosticReportPerformerType] | None = Field(  # type: ignore
        None,
        alias="performer",
        title="Participants in producing the report",
        description="Indicates who or what participated in producing the report.",
        json_schema_extra={
            "element_property": True,
        },
    )

    presentedForm: typing.List[fhirtypes.AttachmentType] | None = Field(  # type: ignore
        None,
        alias="presentedForm",
        title="Entire report as issued",
        description=(
            "Rich text representation of the entire result as issued by the "
            "diagnostic service. Multiple formats are allowed but they SHALL be "
            "semantically equivalent."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    result: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="result",
        title="Observations - simple, or complex nested groups",
        description=(
            "Observations that are part of this diagnostic report. Observations can"
            ' be simple name/value pairs (e.g. "atomic" results), or they can be '
            "grouping observations that include references to other members of the "
            'group (e.g. "panels").'
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Observation"],
        },
    )

    specimen: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="specimen",
        title="Specimens this report is based on",
        description="Details about the specimens on which this diagnostic report is based.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Specimen"],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="registered | partial | preliminary | final +",
        description="The status of the diagnostic report as a whole.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["registered", "partial", "preliminary", "final", "+"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="subject",
        title="The subject of the report - usually, but not always, the patient",
        description=(
            "The subject of the report. Usually, but not always, this is a patient."
            " However diagnostic services also perform analyses on specimens "
            "collected from a variety of other sources."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "Group", "Device", "Location"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DiagnosticReport`` according specification,
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
            "basedOn",
            "status",
            "category",
            "code",
            "subject",
            "context",
            "effectiveDateTime",
            "effectivePeriod",
            "issued",
            "performer",
            "specimen",
            "result",
            "imagingStudy",
            "image",
            "conclusion",
            "codedDiagnosis",
            "presentedForm",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
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
        one_of_many_fields = {"effective": ["effectiveDateTime", "effectivePeriod"]}
        return one_of_many_fields


class DiagnosticReportImage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Key images associated with this report.
    A list of key images associated with this report. The images are generally
    created during the diagnostic process, and may be directly of the patient,
    or of treated specimens (i.e. slides of interest).
    """

    __resource_type__ = "DiagnosticReportImage"

    comment: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="comment",
        title="Comment about the image (e.g. explanation)",
        description=(
            "A comment about the image. Typically, this is used to provide an "
            "explanation for why the image is included, or to draw the viewer's "
            "attention to important features."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_comment", title="Extension field for ``comment``."
    )

    link: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="link",
        title="Reference to the image source",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Media"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DiagnosticReportImage`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "comment", "link"]


class DiagnosticReportPerformer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Participants in producing the report.
    Indicates who or what participated in producing the report.
    """

    __resource_type__ = "DiagnosticReportPerformer"

    actor: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="actor",
        title="Practitioner or Organization  participant",
        description=(
            "The reference to the  practitioner or organization involved in "
            "producing the report. For example, the diagnostic service that is "
            "responsible for issuing the report."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner", "Organization"],
        },
    )

    role: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="role",
        title="Type of performer",
        description=(
            "Describes the type of participation (e.g.  a responsible party, "
            "author, or verifier)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DiagnosticReportPerformer`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "role", "actor"]
