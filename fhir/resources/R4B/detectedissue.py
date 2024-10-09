from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/DetectedIssue
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class DetectedIssue(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Clinical issue with action.
    Indicates an actual or potential clinical issue with or between one or more
    active or proposed clinical actions for a patient; e.g. Drug-drug
    interaction, Ineffective treatment frequency, Procedure-condition conflict,
    etc.
    """

    __resource_type__ = "DetectedIssue"

    author: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="author",
        title="The provider or device that identified the issue",
        description=(
            "Individual or device responsible for the issue being raised.  For "
            "example, a decision support application or a pharmacist conducting a "
            "medication review."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner", "PractitionerRole", "Device"],
        },
    )

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Issue Category, e.g. drug-drug, duplicate therapy, etc.",
        description="Identifies the general type of issue identified.",
        json_schema_extra={
            "element_property": True,
        },
    )

    detail: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="detail",
        title="Description and context",
        description="A textual explanation of the detected issue.",
        json_schema_extra={
            "element_property": True,
        },
    )
    detail__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_detail", title="Extension field for ``detail``."
    )

    evidence: typing.List[fhirtypes.DetectedIssueEvidenceType] | None = Field(  # type: ignore
        None,
        alias="evidence",
        title="Supporting evidence",
        description=(
            "Supporting evidence or manifestations that provide the basis for "
            "identifying the detected issue such as a GuidanceResponse or "
            "MeasureReport."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    identifiedDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="identifiedDateTime",
        title="When identified",
        description="The date or period when the detected issue was initially identified.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e identified[x]
            "one_of_many": "identified",
            "one_of_many_required": False,
        },
    )
    identifiedDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_identifiedDateTime",
        title="Extension field for ``identifiedDateTime``.",
    )

    identifiedPeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="identifiedPeriod",
        title="When identified",
        description="The date or period when the detected issue was initially identified.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e identified[x]
            "one_of_many": "identified",
            "one_of_many_required": False,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Unique id for the detected issue",
        description="Business identifier associated with the detected issue record.",
        json_schema_extra={
            "element_property": True,
        },
    )

    implicated: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="implicated",
        title="Problem resource",
        description=(
            "Indicates the resource representing the current activity or proposed "
            "activity that is potentially problematic."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    mitigation: typing.List[fhirtypes.DetectedIssueMitigationType] | None = Field(  # type: ignore
        None,
        alias="mitigation",
        title="Step taken to address",
        description=(
            "Indicates an action that has been taken or is committed to reduce or "
            "eliminate the likelihood of the risk identified by the detected issue "
            "from manifesting.  Can also reflect an observation of known mitigating"
            " factors that may reduce/eliminate the need for any action."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    patient: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="patient",
        title="Associated patient",
        description=(
            "Indicates the patient whose record the detected issue is associated "
            "with."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient"],
        },
    )

    reference: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="reference",
        title="Authority for issue",
        description=(
            "The literature, knowledge-base or similar reference that describes the"
            " propensity for the detected issue identified."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    reference__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_reference", title="Extension field for ``reference``."
    )

    severity: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="severity",
        title="high | moderate | low",
        description=(
            "Indicates the degree of importance associated with the identified "
            "issue based on the potential impact on the patient."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["high", "moderate", "low"],
        },
    )
    severity__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_severity", title="Extension field for ``severity``."
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="registered | preliminary | final | amended +",
        description="Indicates the status of the detected issue.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["registered", "preliminary", "final", "amended", "+"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DetectedIssue`` according specification,
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
            "code",
            "severity",
            "patient",
            "identifiedDateTime",
            "identifiedPeriod",
            "author",
            "implicated",
            "evidence",
            "detail",
            "reference",
            "mitigation",
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
        one_of_many_fields = {"identified": ["identifiedDateTime", "identifiedPeriod"]}
        return one_of_many_fields


class DetectedIssueEvidence(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Supporting evidence.
    Supporting evidence or manifestations that provide the basis for
    identifying the detected issue such as a GuidanceResponse or MeasureReport.
    """

    __resource_type__ = "DetectedIssueEvidence"

    code: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="code",
        title="Manifestation",
        description="A manifestation that led to the recording of this detected issue.",
        json_schema_extra={
            "element_property": True,
        },
    )

    detail: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="detail",
        title="Supporting information",
        description=(
            "Links to resources that constitute evidence for the detected issue "
            "such as a GuidanceResponse or MeasureReport."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DetectedIssueEvidence`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "detail"]


class DetectedIssueMitigation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Step taken to address.
    Indicates an action that has been taken or is committed to reduce or
    eliminate the likelihood of the risk identified by the detected issue from
    manifesting.  Can also reflect an observation of known mitigating factors
    that may reduce/eliminate the need for any action.
    """

    __resource_type__ = "DetectedIssueMitigation"

    action: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="action",
        title="What mitigation?",
        description=(
            "Describes the action that was taken or the observation that was made "
            "that reduces/eliminates the risk associated with the identified issue."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    author: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="author",
        title="Who is committing?",
        description=(
            "Identifies the practitioner who determined the mitigation and takes "
            "responsibility for the mitigation step occurring."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner", "PractitionerRole"],
        },
    )

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="date",
        title="Date committed",
        description="Indicates when the mitigating action was documented.",
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DetectedIssueMitigation`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "action", "date", "author"]
