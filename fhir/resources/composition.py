# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Composition
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Composition(domainresource.DomainResource):
    """ A set of resources composed into a single coherent clinical statement with
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
        title="List of `Reference` items referencing `Practitioner, PractitionerRole, Device, Patient, RelatedPerson, Organization` (represented as `dict` in JSON)",
        description="Who and/or what authored the composition",
    )

    category: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
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
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
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
        title="Type `Reference` referencing `Encounter` (represented as `dict` in JSON)",
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
        description="Version-independent identifier for the Composition",
    )

    relatesTo: ListType[fhirtypes.CompositionRelatesToType] = Field(
        None,
        alias="relatesTo",
        title="List of `CompositionRelatesTo` items (represented as `dict` in JSON)",
        description="Relationships to other compositions/documents",
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
        None,
        alias="subject",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
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


class CompositionAttester(backboneelement.BackboneElement):
    """ Attests to accuracy of composition.
    A participant who has attested to the accuracy of the composition/document.
    """

    resource_type = Field("CompositionAttester", const=True)

    mode: fhirtypes.Code = Field(
        ...,
        alias="mode",
        title="Type `Code` (represented as `dict` in JSON)",
        description="personal | professional | legal | official",
    )

    party: fhirtypes.ReferenceType = Field(
        None,
        alias="party",
        title="Type `Reference` referencing `Patient, RelatedPerson, Practitioner, PractitionerRole, Organization` (represented as `dict` in JSON)",
        description="Who attested the composition",
    )

    time: fhirtypes.DateTime = Field(
        None,
        alias="time",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When the composition was attested",
    )


class CompositionEvent(backboneelement.BackboneElement):
    """ The clinical service(s) being documented.
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
        title="List of `Reference` items referencing `Resource` (represented as `dict` in JSON)",
        description="The event(s) being documented",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="The period covered by the documentation",
    )


class CompositionRelatesTo(backboneelement.BackboneElement):
    """ Relationships to other compositions/documents.
    Relationships that this composition has with other compositions or
    documents that already exist.
    """

    resource_type = Field("CompositionRelatesTo", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Type `Code` (represented as `dict` in JSON)",
        description="replaces | transforms | signs | appends",
    )

    targetIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="targetIdentifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Target of the relationship",
        one_of_many="target",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    targetReference: fhirtypes.ReferenceType = Field(
        None,
        alias="targetReference",
        title="Type `Reference` referencing `Composition` (represented as `dict` in JSON)",
        description="Target of the relationship",
        one_of_many="target",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
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
        one_of_many_fields = {
            "target": ["targetIdentifier", "targetReference",],
        }
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


class CompositionSection(backboneelement.BackboneElement):
    """ Composition is broken into sections.
    The root of the sections that make up the composition.
    """

    resource_type = Field("CompositionSection", const=True)

    author: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="author",
        title="List of `Reference` items referencing `Practitioner, PractitionerRole, Device, Patient, RelatedPerson, Organization` (represented as `dict` in JSON)",
        description="Who and/or what authored the section",
    )

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
        title="List of `Reference` items referencing `Resource` (represented as `dict` in JSON)",
        description="A reference to data that supports this section",
    )

    focus: fhirtypes.ReferenceType = Field(
        None,
        alias="focus",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="Who/what the section is about, when it is not about the subject of composition",
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
