# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AllergyIntolerance
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType
from typing import Union

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class AllergyIntolerance(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Allergy or Intolerance (generally: Risk of adverse reaction to a substance).
    Risk of harmful or undesirable, physiological response which is unique to
    an individual and associated with exposure to a substance.
    """

    resource_type = Field("AllergyIntolerance", const=True)

    assertedDate: fhirtypes.DateTime = Field(
        None,
        alias="assertedDate",
        title="Type `DateTime`",
        description="Date record was believed accurate",
    )
    assertedDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_assertedDate", title="Extension field for ``assertedDate``."
    )

    asserter: fhirtypes.ReferenceType = Field(
        None,
        alias="asserter",
        title=(
            "Type `Reference` referencing `Patient, RelatedPerson, Practitioner` "
            "(represented as `dict` in JSON)"
        ),
        description="Source of the information about the allergy",
    )

    category: ListType[fhirtypes.Code] = Field(
        None,
        alias="category",
        title="List of `Code` items",
        description="food | medication | environment | biologic",
    )
    category__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_category", title="Extension field for ``category``."
    )

    clinicalStatus: fhirtypes.Code = Field(
        None,
        alias="clinicalStatus",
        title="Type `Code`",
        description="active | inactive | resolved",
    )
    clinicalStatus__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_clinicalStatus", title="Extension field for ``clinicalStatus``."
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Code that identifies the allergy or intolerance",
    )

    criticality: fhirtypes.Code = Field(
        None,
        alias="criticality",
        title="Type `Code`",
        description="low | high | unable-to-assess",
    )
    criticality__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_criticality", title="Extension field for ``criticality``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="External ids for this item",
    )

    lastOccurrence: fhirtypes.DateTime = Field(
        None,
        alias="lastOccurrence",
        title="Type `DateTime`",
        description="Date(/time) of last known occurrence of a reaction",
    )
    lastOccurrence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastOccurrence", title="Extension field for ``lastOccurrence``."
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Additional text not captured in other fields",
    )

    onsetAge: fhirtypes.AgeType = Field(
        None,
        alias="onsetAge",
        title="Type `Age` (represented as `dict` in JSON)",
        description="When allergy or intolerance was identified",
        one_of_many="onset",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    onsetDateTime: fhirtypes.DateTime = Field(
        None,
        alias="onsetDateTime",
        title="Type `DateTime`",
        description="When allergy or intolerance was identified",
        one_of_many="onset",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    onsetDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_onsetDateTime", title="Extension field for ``onsetDateTime``."
    )

    onsetPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="onsetPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When allergy or intolerance was identified",
        one_of_many="onset",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    onsetRange: fhirtypes.RangeType = Field(
        None,
        alias="onsetRange",
        title="Type `Range` (represented as `dict` in JSON)",
        description="When allergy or intolerance was identified",
        one_of_many="onset",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    onsetString: fhirtypes.String = Field(
        None,
        alias="onsetString",
        title="Type `String`",
        description="When allergy or intolerance was identified",
        one_of_many="onset",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    onsetString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_onsetString", title="Extension field for ``onsetString``."
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="Who the sensitivity is for",
    )

    reaction: ListType[fhirtypes.AllergyIntoleranceReactionType] = Field(
        None,
        alias="reaction",
        title=(
            "List of `AllergyIntoleranceReaction` items (represented as `dict` in "
            "JSON)"
        ),
        description="Adverse Reaction Events linked to exposure to substance",
    )

    recorder: fhirtypes.ReferenceType = Field(
        None,
        alias="recorder",
        title=(
            "Type `Reference` referencing `Practitioner, Patient` (represented as "
            "`dict` in JSON)"
        ),
        description="Who recorded the sensitivity",
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="Type `Code`",
        description="allergy | intolerance - Underlying mechanism (if known)",
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    verificationStatus: fhirtypes.Code = Field(
        ...,
        alias="verificationStatus",
        title="Type `Code`",
        description="unconfirmed | confirmed | refuted | entered-in-error",
    )
    verificationStatus__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_verificationStatus",
        title="Extension field for ``verificationStatus``.",
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
            "onset": [
                "onsetAge",
                "onsetDateTime",
                "onsetPeriod",
                "onsetRange",
                "onsetString",
            ]
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


class AllergyIntoleranceReaction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Adverse Reaction Events linked to exposure to substance.
    Details about each adverse reaction event linked to exposure to the
    identified substance.
    """

    resource_type = Field("AllergyIntoleranceReaction", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Description of the event as a whole",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    exposureRoute: fhirtypes.CodeableConceptType = Field(
        None,
        alias="exposureRoute",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="How the subject was exposed to the substance",
    )

    manifestation: ListType[fhirtypes.CodeableConceptType] = Field(
        ...,
        alias="manifestation",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Clinical symptoms/signs associated with the Event",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Text about event not captured in other fields",
    )

    onset: fhirtypes.DateTime = Field(
        None,
        alias="onset",
        title="Type `DateTime`",
        description="Date(/time) when manifestations showed",
    )
    onset__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_onset", title="Extension field for ``onset``."
    )

    severity: fhirtypes.Code = Field(
        None,
        alias="severity",
        title="Type `Code`",
        description="mild | moderate | severe (of event as a whole)",
    )
    severity__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_severity", title="Extension field for ``severity``."
    )

    substance: fhirtypes.CodeableConceptType = Field(
        None,
        alias="substance",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "Specific substance or pharmaceutical product considered to be "
            "responsible for event"
        ),
    )
