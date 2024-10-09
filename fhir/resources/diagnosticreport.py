from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/DiagnosticReport
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
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
    The findings and interpretation of diagnostic tests performed on patients,
    groups of patients, products, substances, devices, and locations, and/or
    specimens derived from these. The report includes clinical context such as
    requesting provider information, and some mix of atomic results, images,
    textual and coded interpretations, and formatted representation of
    diagnostic reports. The report also includes non-clinical context such as
    batch analysis and stability reporting of products and substances.
    """

    __resource_type__ = "DiagnosticReport"

    basedOn: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="basedOn",
        title="What was requested",
        description="Details concerning a service requested.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "CarePlan",
                "ImmunizationRecommendation",
                "MedicationRequest",
                "NutritionOrder",
                "ServiceRequest",
            ],
        },
    )

    category: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
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

    composition: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="composition",
        title="Reference to a Composition resource for the DiagnosticReport structure",
        description=(
            "Reference to a Composition resource instance that provides structure "
            "for organizing the contents of the DiagnosticReport."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Composition"],
        },
    )

    conclusion: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="conclusion",
        title="Clinical conclusion (interpretation) of test results",
        description=(
            "Concise and clinically contextualized summary conclusion "
            "(interpretation/impression) of the diagnostic report."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    conclusion__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_conclusion", title="Extension field for ``conclusion``."
    )

    conclusionCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="conclusionCode",
        title="Codes for the clinical conclusion of test results",
        description=(
            "One or more codes that represent the summary conclusion "
            "(interpretation/impression) of the diagnostic report."
        ),
        json_schema_extra={
            "element_property": True,
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

    encounter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="encounter",
        title="Health care event when test ordered",
        description=(
            "The healthcare event  (e.g. a patient and healthcare provider "
            "interaction) which this DiagnosticReport is about."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter"],
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

    issued: fhirtypes.InstantType | None = Field(  # type: ignore
        None,
        alias="issued",
        title="DateTime this version was made",
        description=(
            "The date and time that this version of the report was made available "
            "to providers, typically after the report was reviewed and verified."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    issued__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_issued", title="Extension field for ``issued``."
    )

    media: typing.List[fhirtypes.DiagnosticReportMediaType] | None = Field(  # type: ignore
        None,
        alias="media",
        title="Key images or data associated with this report",
        description=(
            "A list of key images or data associated with this report. The images "
            "or data are generally created during the diagnostic process, and may "
            "be directly of the patient, or of treated specimens (i.e. slides of "
            "interest)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="note",
        title="Comments about the diagnostic report",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    performer: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="performer",
        title="Responsible Diagnostic Service",
        description="The diagnostic service that is responsible for issuing the report.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
                "CareTeam",
            ],
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
        title="Observations",
        description=(
            "[Observations](observation.html)  that are part of this diagnostic "
            "report."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Observation"],
        },
    )

    resultsInterpreter: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="resultsInterpreter",
        title="Primary result interpreter",
        description=(
            "The practitioner or organization that is responsible for the report's "
            "conclusions and interpretations."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
                "CareTeam",
            ],
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
        title=(
            "registered | partial | preliminary | modified | final | amended | "
            "corrected | appended | cancelled | entered-in-error | unknown"
        ),
        description="The status of the diagnostic report.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "registered",
                "partial",
                "preliminary",
                "modified",
                "final",
                "amended",
                "corrected",
                "appended",
                "cancelled",
                "entered-in-error",
                "unknown",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    study: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="study",
        title=(
            "Reference to full details of an analysis associated with the "
            "diagnostic report"
        ),
        description=(
            "One or more links to full details of any study performed during the "
            "diagnostic investigation. An ImagingStudy might comprise a set of "
            "radiologic images obtained via a procedure that are analyzed as a "
            "group. Typically, this is imaging performed by DICOM enabled "
            "modalities, but this is not required. A fully enabled PACS viewer can "
            "use this information to provide views of the source images. A "
            "GenomicStudy might comprise one or more analyses, each serving a "
            "specific purpose. These analyses may vary in method (e.g., "
            "karyotyping, CNV, or SNV detection), performer, software, devices "
            "used, or regions targeted."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["GenomicStudy", "ImagingStudy"],
        },
    )

    subject: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="subject",
        title="The subject of the report - usually, but not always, the patient",
        description=(
            "The subject of the report. Usually, but not always, this is a patient."
            " However, diagnostic services also perform analyses on specimens "
            "collected from a variety of other sources."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Patient",
                "Group",
                "Device",
                "Location",
                "Organization",
                "Practitioner",
                "Medication",
                "Substance",
                "BiologicallyDerivedProduct",
            ],
        },
    )

    supportingInfo: typing.List[fhirtypes.DiagnosticReportSupportingInfoType] | None = Field(  # type: ignore
        None,
        alias="supportingInfo",
        title="Additional information supporting the diagnostic report",
        description=(
            "This backbone element contains supporting information that was used in"
            " the creation of the report not included in the results already "
            "included in the report."
        ),
        json_schema_extra={
            "element_property": True,
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
            "encounter",
            "effectiveDateTime",
            "effectivePeriod",
            "issued",
            "performer",
            "resultsInterpreter",
            "specimen",
            "result",
            "note",
            "study",
            "supportingInfo",
            "media",
            "composition",
            "conclusion",
            "conclusionCode",
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


class DiagnosticReportMedia(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Key images or data associated with this report.
    A list of key images or data associated with this report. The images or
    data are generally created during the diagnostic process, and may be
    directly of the patient, or of treated specimens (i.e. slides of interest).
    """

    __resource_type__ = "DiagnosticReportMedia"

    comment: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="comment",
        title="Comment about the image or data (e.g. explanation)",
        description=(
            "A comment about the image or data. Typically, this is used to provide "
            "an explanation for why the image or data is included, or to draw the "
            "viewer's attention to important features."
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
        title="Reference to the image or data source",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DocumentReference"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DiagnosticReportMedia`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "comment", "link"]


class DiagnosticReportSupportingInfo(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional information supporting the diagnostic report.
    This backbone element contains supporting information that was used in the
    creation of the report not included in the results already included in the
    report.
    """

    __resource_type__ = "DiagnosticReportSupportingInfo"

    reference: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="reference",
        title="Supporting information reference",
        description="The reference for the supporting information in the diagnostic report.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Procedure",
                "Observation",
                "DiagnosticReport",
                "Citation",
            ],
        },
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Supporting information role code",
        description=(
            "The code value for the role of the supporting information in the "
            "diagnostic report."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DiagnosticReportSupportingInfo`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "reference"]
