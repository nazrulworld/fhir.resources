# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Composition
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic import Field

from . import fhirtypes
from .backboneelement import BackboneElement
from .domainresource import DomainResource


class Composition(DomainResource):
    """A set of resources composed into a single coherent clinical statement with
    clinical attestation.

    A set of healthcare-related information that is assembled together into a
    single logical document that provides a single coherent statement of
    meaning, establishes its own context and that has clinical attestation with
    regard to who is making the statement. While a Composition defines the
    structure, it does not actually contain the content: rather the full
    content of a document is contained in a Bundle, of which the Composition is
    the first resource contained.
    """

    resource_type = Field("Composition", const=True)

    attester: ListType[fhirtypes.CompositionAttesterType] = Field(
        None,
        alias="attester",
        title="List of `CompositionAttester` items (represented as `dict` in JSON)",
        description="Attests to accuracy of composition",
    )

    author: ListType[fhirtypes.ReferenceType] = Field(
        ...,
        alias="author",
        title=(
            "List of `Reference` items referencing `Practitioner, Device, Patient, "
            "RelatedPerson` (represented as `dict` in JSON)"
        ),
        description="Who and/or what authored the composition",
    )

    class_fhir: fhirtypes.CodeableConceptType = Field(
        None,
        alias="class",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Categorization of Composition",
    )

    confidentiality: fhirtypes.Code = Field(
        None,
        alias="confidentiality",
        title="Type `Code` (represented as `dict` in JSON)",
        description="As defined by affinity domain",
    )

    custodian: fhirtypes.ReferenceType = Field(
        None,
        alias="custodian",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Organization which maintains the composition",
    )

    date: fhirtypes.DateTime = Field(
        ...,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Composition editing time",
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title=(
            "Type `Reference` referencing `Encounter` (represented as `dict` in "
            "JSON)"
        ),
        description="Context of the Composition",
    )

    event: ListType[fhirtypes.CompositionEventType] = Field(
        None,
        alias="event",
        title="List of `CompositionEvent` items (represented as `dict` in JSON)",
        description="The clinical service(s) being documented",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Logical identifier of composition (version-independent)",
    )

    section: ListType[fhirtypes.CompositionSectionType] = Field(
        None,
        alias="section",
        title="List of `CompositionSection` items (represented as `dict` in JSON)",
        description="Composition is broken into sections",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="preliminary | final | amended | entered-in-error",
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Who and/or what the composition is about",
    )

    title: fhirtypes.String = Field(
        ...,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="Human Readable name/title",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Kind of composition (LOINC if possible)",
    )


class CompositionAttester(BackboneElement):
    """Attests to accuracy of composition.

    A participant who has attested to the accuracy of the composition/document.
    """

    resource_type = Field("CompositionAttester", const=True)

    mode: ListType[fhirtypes.Code] = Field(
        ...,
        alias="mode",
        title="List of `Code` items (represented as `dict` in JSON)",
        description="personal | professional | legal | official",
    )

    party: fhirtypes.ReferenceType = Field(
        None,
        alias="party",
        title=(
            "Type `Reference` referencing `Patient, Practitioner, Organization` "
            "(represented as `dict` in JSON)"
        ),
        description="Who attested the composition",
    )

    time: fhirtypes.DateTime = Field(
        None,
        alias="time",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When the composition was attested",
    )


class CompositionEvent(BackboneElement):
    """The clinical service(s) being documented.

    The clinical service, such as a colonoscopy or an appendectomy, being
    documented.
    """

    resource_type = Field("CompositionEvent", const=True)

    code: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="code",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Code(s) that apply to the event being documented",
    )

    detail: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="detail",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="The event(s) being documented",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="The period covered by the documentation",
    )


class CompositionSection(BackboneElement):
    """Composition is broken into sections.

    The root of the sections that make up the composition.
    """

    resource_type = Field("CompositionSection", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Classification of section (recommended)",
    )

    emptyReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="emptyReason",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Why the section is empty",
    )

    entry: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="entry",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="A reference to data that supports this section",
    )

    mode: fhirtypes.Code = Field(
        None,
        alias="mode",
        title="Type `Code` (represented as `dict` in JSON)",
        description="working | snapshot | changes",
    )

    orderedBy: fhirtypes.CodeableConceptType = Field(
        None,
        alias="orderedBy",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Order of section entries",
    )

    section: ListType[fhirtypes.CompositionSectionType] = Field(
        None,
        alias="section",
        title="List of `CompositionSection` items (represented as `dict` in JSON)",
        description="Nested Section",
    )

    text: fhirtypes.NarrativeType = Field(
        None,
        alias="text",
        title="Type `Narrative` (represented as `dict` in JSON)",
        description="Text summary of the section, for human interpretation",
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="Label for section (e.g. for ToC)",
    )
