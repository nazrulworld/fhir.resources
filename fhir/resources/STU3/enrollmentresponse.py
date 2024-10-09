from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/EnrollmentResponse
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import domainresource, fhirtypes


class EnrollmentResponse(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    EnrollmentResponse resource.
    This resource provides enrollment and plan details from the processing of
    an Enrollment resource.
    """

    __resource_type__ = "EnrollmentResponse"

    created: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="created",
        title="Creation date",
        description=(
            "The date when the enclosed suite of services were performed or "
            "completed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_created", title="Extension field for ``created``."
    )

    disposition: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="disposition",
        title="Disposition Message",
        description="A description of the status of the adjudication.",
        json_schema_extra={
            "element_property": True,
        },
    )
    disposition__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_disposition", title="Extension field for ``disposition``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business Identifier",
        description="The Response business identifier.",
        json_schema_extra={
            "element_property": True,
        },
    )

    organization: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="organization",
        title="Insurer",
        description="The Insurer who produced this adjudicated response.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    outcome: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="outcome",
        title="complete | error | partial",
        description="Processing status: error, complete.",
        json_schema_extra={
            "element_property": True,
        },
    )

    request: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="request",
        title="Claim reference",
        description="Original request resource reference.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["EnrollmentRequest"],
        },
    )

    requestOrganization: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="requestOrganization",
        title="Responsible organization",
        description=(
            "The organization which is responsible for the services rendered to the"
            " patient."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    requestProvider: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="requestProvider",
        title="Responsible practitioner",
        description=(
            "The practitioner who is responsible for the services rendered to the "
            "patient."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner"],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="active | cancelled | draft | entered-in-error",
        description="The status of the resource instance.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["active", "cancelled", "draft", "entered-in-error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EnrollmentResponse`` according specification,
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
            "request",
            "outcome",
            "disposition",
            "created",
            "organization",
            "requestProvider",
            "requestOrganization",
        ]
