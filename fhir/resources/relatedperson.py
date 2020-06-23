# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/RelatedPerson
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class RelatedPerson(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A person that is related to a patient, but who is not a direct target of
    care.
    Information about a person that is involved in the care for a patient, but
    who is not the target of healthcare, nor has a formal responsibility in the
    care process.
    """

    resource_type = Field("RelatedPerson", const=True)

    active: bool = Field(
        None,
        alias="active",
        title="Type `bool`",
        description="Whether this related person\u0027s record is in active use",
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_active", title="Extension field for ``active``."
    )

    address: ListType[fhirtypes.AddressType] = Field(
        None,
        alias="address",
        title="List of `Address` items (represented as `dict` in JSON)",
        description="Address where the related person can be contacted or visited",
    )

    birthDate: fhirtypes.Date = Field(
        None,
        alias="birthDate",
        title="Type `Date`",
        description="The date on which the related person was born",
    )
    birthDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_birthDate", title="Extension field for ``birthDate``."
    )

    communication: ListType[fhirtypes.RelatedPersonCommunicationType] = Field(
        None,
        alias="communication",
        title=(
            "List of `RelatedPersonCommunication` items (represented as `dict` in "
            "JSON)"
        ),
        description=(
            "A language which may be used to communicate with about the patient\u0027s "
            "health"
        ),
    )

    gender: fhirtypes.Code = Field(
        None,
        alias="gender",
        title="Type `Code`",
        description="male | female | other | unknown",
    )
    gender__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_gender", title="Extension field for ``gender``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="A human identifier for this person",
    )

    name: ListType[fhirtypes.HumanNameType] = Field(
        None,
        alias="name",
        title="List of `HumanName` items (represented as `dict` in JSON)",
        description="A name associated with the person",
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="The patient this person is related to",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Period of time that this relationship is considered valid",
    )

    photo: ListType[fhirtypes.AttachmentType] = Field(
        None,
        alias="photo",
        title="List of `Attachment` items (represented as `dict` in JSON)",
        description="Image of the person",
    )

    relationship: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="relationship",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="The nature of the relationship",
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="List of `ContactPoint` items (represented as `dict` in JSON)",
        description="A contact detail for the person",
    )


class RelatedPersonCommunication(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A language which may be used to communicate with about the patient's health.
    """

    resource_type = Field("RelatedPersonCommunication", const=True)

    language: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="language",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "The language which can be used to communicate with the patient about "
            "his or her health"
        ),
    )

    preferred: bool = Field(
        None,
        alias="preferred",
        title="Type `bool`",
        description="Language preference indicator",
    )
    preferred__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_preferred", title="Extension field for ``preferred``."
    )
