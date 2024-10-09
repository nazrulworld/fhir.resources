from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceAssociation
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class DeviceAssociation(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A record of association or dissociation of a device with a patient.
    """

    __resource_type__ = "DeviceAssociation"

    bodyStructure: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="bodyStructure",
        title="Current anatomical location of the device in/on subject",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["BodyStructure"],
        },
    )

    category: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="category",
        title="Describes the relationship between the device and subject",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    device: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="device",
        title="Reference to the devices associated with the patient or group",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Device"],
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Instance identifier",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    operation: typing.List[fhirtypes.DeviceAssociationOperationType] | None = Field(  # type: ignore
        None,
        alias="operation",
        title=(
            "The details about the device when it is in use to describe its "
            "operation"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="period",
        title="Begin and end dates and times for the device association",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="status",
        title="implanted | explanted | attached | entered-in-error | unknown",
        description="Indicates the state of the Device association.",
        json_schema_extra={
            "element_property": True,
        },
    )

    statusReason: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="statusReason",
        title="The reasons given for the current association status",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    subject: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="subject",
        title=(
            "The individual, group of individuals or device that the device is on "
            "or associated with"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Patient",
                "Group",
                "Practitioner",
                "RelatedPerson",
                "Device",
            ],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceAssociation`` according specification,
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
            "device",
            "category",
            "status",
            "statusReason",
            "subject",
            "bodyStructure",
            "period",
            "operation",
        ]


class DeviceAssociationOperation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The details about the device when it is in use to describe its operation.
    """

    __resource_type__ = "DeviceAssociationOperation"

    operator: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="operator",
        title="The individual performing the action enabled by the device",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "Practitioner", "RelatedPerson"],
        },
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="period",
        title="Begin and end dates and times for the device's operation",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="status",
        title="Device operational condition",
        description="Device operational condition corresponding to the association.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceAssociationOperation`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "status", "operator", "period"]
