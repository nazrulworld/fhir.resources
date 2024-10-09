from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ResearchSubject
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import domainresource, fhirtypes


class ResearchSubject(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Investigation to increase healthcare-related patient-independent knowledge.
    A process where a researcher or organization plans and then executes a
    series of steps intended to increase the field of healthcare-related
    knowledge.  This includes studies of safety, efficacy, comparative
    effectiveness and other information about medications, devices, therapies
    and other interventional and investigative techniques.  A ResearchStudy
    involves the gathering of information about human or animal subjects.
    """

    __resource_type__ = "ResearchSubject"

    actualArm: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="actualArm",
        title="What path was followed",
        description=(
            "The name of the arm in the study the subject actually followed as part"
            " of this study."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    actualArm__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_actualArm", title="Extension field for ``actualArm``."
    )

    assignedArm: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="assignedArm",
        title="What path should be followed",
        description=(
            "The name of the arm in the study the subject is expected to follow as "
            "part of this study."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    assignedArm__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_assignedArm", title="Extension field for ``assignedArm``."
    )

    consent: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="consent",
        title="Agreement to participate in study",
        description=(
            "A record of the patient's informed agreement to participate in the "
            "study."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Consent"],
        },
    )

    identifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business Identifier for research subject",
        description=(
            "Identifiers assigned to this research study by the sponsor or other "
            "systems."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    individual: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="individual",
        title="Who is part of study",
        description="The record of the person or animal who is involved in the study.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient"],
        },
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="period",
        title="Start and end of participation",
        description=(
            "The dates the subject began and ended their participation in the " "study."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="candidate | enrolled | active | suspended | withdrawn | completed",
        description="The current state of the subject.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "candidate",
                "enrolled",
                "active",
                "suspended",
                "withdrawn",
                "completed",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    study: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="study",
        title="Study subject is part of",
        description="Reference to the study the subject is participating in.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ResearchStudy"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ResearchSubject`` according specification,
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
            "period",
            "study",
            "individual",
            "assignedArm",
            "actualArm",
            "consent",
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
