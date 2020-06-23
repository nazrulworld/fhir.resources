# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DiagnosticReport
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class DiagnosticReport(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
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

    resource_type = Field("DiagnosticReport", const=True)

    basedOn: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title=(
            "List of `Reference` items referencing `CarePlan, "
            "ImmunizationRecommendation, MedicationRequest, NutritionOrder, "
            "ProcedureRequest, ReferralRequest` (represented as `dict` in JSON)"
        ),
        description="What was requested",
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Service category",
    )

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Name/Code for this diagnostic report",
    )

    codedDiagnosis: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="codedDiagnosis",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Codes for the conclusion",
    )

    conclusion: fhirtypes.String = Field(
        None,
        alias="conclusion",
        title="Type `String`",
        description="Clinical Interpretation of test results",
    )
    conclusion__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_conclusion", title="Extension field for ``conclusion``."
    )

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title=(
            "Type `Reference` referencing `Encounter, EpisodeOfCare` (represented "
            "as `dict` in JSON)"
        ),
        description="Health care event when test ordered",
    )

    effectiveDateTime: fhirtypes.DateTime = Field(
        None,
        alias="effectiveDateTime",
        title="Type `DateTime`",
        description="Clinically relevant time/time-period for report",
        one_of_many="effective",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    effectiveDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_effectiveDateTime",
        title="Extension field for ``effectiveDateTime``.",
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Clinically relevant time/time-period for report",
        one_of_many="effective",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business identifier for report",
    )

    image: ListType[fhirtypes.DiagnosticReportImageType] = Field(
        None,
        alias="image",
        title="List of `DiagnosticReportImage` items (represented as `dict` in JSON)",
        description="Key images associated with this report",
    )

    imagingStudy: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="imagingStudy",
        title=(
            "List of `Reference` items referencing `ImagingStudy, ImagingManifest` "
            "(represented as `dict` in JSON)"
        ),
        description=(
            "Reference to full details of imaging associated with the diagnostic "
            "report"
        ),
    )

    issued: fhirtypes.Instant = Field(
        None,
        alias="issued",
        title="Type `Instant`",
        description="DateTime this version was released",
    )
    issued__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_issued", title="Extension field for ``issued``."
    )

    performer: ListType[fhirtypes.DiagnosticReportPerformerType] = Field(
        None,
        alias="performer",
        title=(
            "List of `DiagnosticReportPerformer` items (represented as `dict` in "
            "JSON)"
        ),
        description="Participants in producing the report",
    )

    presentedForm: ListType[fhirtypes.AttachmentType] = Field(
        None,
        alias="presentedForm",
        title="List of `Attachment` items (represented as `dict` in JSON)",
        description="Entire report as issued",
    )

    result: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="result",
        title=(
            "List of `Reference` items referencing `Observation` (represented as "
            "`dict` in JSON)"
        ),
        description="Observations - simple, or complex nested groups",
    )

    specimen: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="specimen",
        title=(
            "List of `Reference` items referencing `Specimen` (represented as "
            "`dict` in JSON)"
        ),
        description="Specimens this report is based on",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`",
        description="registered | partial | preliminary | final +",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title=(
            "Type `Reference` referencing `Patient, Group, Device, Location` "
            "(represented as `dict` in JSON)"
        ),
        description="The subject of the report - usually, but not always, the patient",
    )

    @root_validator(pre=True)
    def validate_one_of_many(cls, values: Dict[str, Any]) -> Dict[str, Any]:
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


class DiagnosticReportImage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Key images associated with this report.
    A list of key images associated with this report. The images are generally
    created during the diagnostic process, and may be directly of the patient,
    or of treated specimens (i.e. slides of interest).
    """

    resource_type = Field("DiagnosticReportImage", const=True)

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Type `String`",
        description="Comment about the image (e.g. explanation)",
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    link: fhirtypes.ReferenceType = Field(
        ...,
        alias="link",
        title="Type `Reference` referencing `Media` (represented as `dict` in JSON)",
        description="Reference to the image source",
    )


class DiagnosticReportPerformer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Participants in producing the report.
    Indicates who or what participated in producing the report.
    """

    resource_type = Field("DiagnosticReportPerformer", const=True)

    actor: fhirtypes.ReferenceType = Field(
        ...,
        alias="actor",
        title=(
            "Type `Reference` referencing `Practitioner, Organization` (represented"
            " as `dict` in JSON)"
        ),
        description="Practitioner or Organization  participant",
    )

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of performer",
    )
