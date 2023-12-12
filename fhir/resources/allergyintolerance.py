# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AllergyIntolerance
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class AllergyIntolerance(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Allergy or Intolerance (generally: Risk of adverse reaction to a substance).
    Risk of harmful or undesirable physiological response which is specific to
    an individual and associated with exposure to a substance.
    """

    resource_type = Field("AllergyIntolerance", const=True)

    category: typing.List[typing.Optional[fhirtypes.Code]] = Field(
        None,
        alias="category",
        title="food | medication | environment | biologic",
        description="Category of the identified substance.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["food", "medication", "environment", "biologic"],
    )
    category__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_category", title="Extension field for ``category``.")

    clinicalStatus: fhirtypes.CodeableConceptType = Field(
        None,
        alias="clinicalStatus",
        title="active | inactive | resolved",
        description="The clinical status of the allergy or intolerance.",
        # if property is element of this resource.
        element_property=True,
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Code that identifies the allergy or intolerance",
        description=(
            "Code for an allergy or intolerance statement (either a positive or a "
            "negated/excluded statement).  This may be a code for a substance or "
            "pharmaceutical product that is considered to be responsible for the "
            'adverse reaction risk (e.g., "Latex"), an allergy or intolerance '
            'condition (e.g., "Latex allergy"), or a negated/excluded code for a '
            'specific substance or class (e.g., "No latex allergy") or a general or'
            ' categorical negated statement (e.g.,  "No known allergy", "No known '
            'drug allergies").  Note: the substance for a specific reaction may be '
            "different from the substance identified as the cause of the risk, but "
            "it must be consistent with it. For instance, it may be a more specific"
            " substance (e.g. a brand medication) or a composite product that "
            "includes the identified substance. It must be clinically safe to only "
            "process the 'code' and ignore the 'reaction.substance'.  If a "
            "receiving system is unable to confirm that "
            "AllergyIntolerance.reaction.substance falls within the semantic scope "
            "of AllergyIntolerance.code, then the receiving system should ignore "
            "AllergyIntolerance.reaction.substance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    criticality: fhirtypes.Code = Field(
        None,
        alias="criticality",
        title="low | high | unable-to-assess",
        description=(
            "Estimate of the potential clinical harm, or seriousness, of the "
            "reaction to the identified substance."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["low", "high", "unable-to-assess"],
    )
    criticality__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_criticality", title="Extension field for ``criticality``."
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Encounter when the allergy or intolerance was asserted",
        description="The encounter when the allergy or intolerance was asserted.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="External ids for this item",
        description=(
            "Business identifiers assigned to this AllergyIntolerance by the "
            "performer or other systems which remain constant as the resource is "
            "updated and propagates from server to server."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    lastOccurrence: fhirtypes.DateTime = Field(
        None,
        alias="lastOccurrence",
        title="Date(/time) of last known occurrence of a reaction",
        description=(
            "Represents the date and/or time of the last known occurrence of a "
            "reaction event."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    lastOccurrence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastOccurrence", title="Extension field for ``lastOccurrence``."
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Additional text not captured in other fields",
        description=(
            "Additional narrative about the propensity for the Adverse Reaction, "
            "not captured in other fields."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    onsetAge: fhirtypes.AgeType = Field(
        None,
        alias="onsetAge",
        title="When allergy or intolerance was identified",
        description=(
            "Estimated or actual date,  date-time, or age when allergy or "
            "intolerance was identified."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e onset[x]
        one_of_many="onset",
        one_of_many_required=False,
    )

    onsetDateTime: fhirtypes.DateTime = Field(
        None,
        alias="onsetDateTime",
        title="When allergy or intolerance was identified",
        description=(
            "Estimated or actual date,  date-time, or age when allergy or "
            "intolerance was identified."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e onset[x]
        one_of_many="onset",
        one_of_many_required=False,
    )
    onsetDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_onsetDateTime", title="Extension field for ``onsetDateTime``."
    )

    onsetPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="onsetPeriod",
        title="When allergy or intolerance was identified",
        description=(
            "Estimated or actual date,  date-time, or age when allergy or "
            "intolerance was identified."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e onset[x]
        one_of_many="onset",
        one_of_many_required=False,
    )

    onsetRange: fhirtypes.RangeType = Field(
        None,
        alias="onsetRange",
        title="When allergy or intolerance was identified",
        description=(
            "Estimated or actual date,  date-time, or age when allergy or "
            "intolerance was identified."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e onset[x]
        one_of_many="onset",
        one_of_many_required=False,
    )

    onsetString: fhirtypes.String = Field(
        None,
        alias="onsetString",
        title="When allergy or intolerance was identified",
        description=(
            "Estimated or actual date,  date-time, or age when allergy or "
            "intolerance was identified."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e onset[x]
        one_of_many="onset",
        one_of_many_required=False,
    )
    onsetString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_onsetString", title="Extension field for ``onsetString``."
    )

    participant: typing.List[fhirtypes.AllergyIntoleranceParticipantType] = Field(
        None,
        alias="participant",
        title=(
            "Who or what participated in the activities related to the allergy or "
            "intolerance and how they were involved"
        ),
        description=(
            "Indicates who or what participated in the activities related to the "
            "allergy or intolerance and how they were involved."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Who the allergy or intolerance is for",
        description="The patient who has the allergy or intolerance.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    reaction: typing.List[fhirtypes.AllergyIntoleranceReactionType] = Field(
        None,
        alias="reaction",
        title="Adverse Reaction Events linked to exposure to substance",
        description=(
            "Details about each adverse reaction event linked to exposure to the "
            "identified substance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    recordedDate: fhirtypes.DateTime = Field(
        None,
        alias="recordedDate",
        title="Date allergy or intolerance was first recorded",
        description=(
            "The recordedDate represents when this particular AllergyIntolerance "
            "record was created in the system, which is often a system-generated "
            "date."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    recordedDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_recordedDate", title="Extension field for ``recordedDate``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="allergy | intolerance - Underlying mechanism (if known)",
        description=(
            "Identification of the underlying physiological mechanism for the "
            "reaction risk."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    verificationStatus: fhirtypes.CodeableConceptType = Field(
        None,
        alias="verificationStatus",
        title="unconfirmed | presumed | confirmed | refuted | entered-in-error",
        description=(
            "Assertion about certainty associated with the propensity, or potential"
            " risk, of a reaction to the identified substance (including "
            "pharmaceutical product).  The verification status pertains to the "
            "allergy or intolerance, itself, not to any specific AllergyIntolerance"
            " attribute."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AllergyIntolerance`` according specification,
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
            "clinicalStatus",
            "verificationStatus",
            "type",
            "category",
            "criticality",
            "code",
            "patient",
            "encounter",
            "onsetDateTime",
            "onsetAge",
            "onsetPeriod",
            "onsetRange",
            "onsetString",
            "recordedDate",
            "participant",
            "lastOccurrence",
            "note",
            "reaction",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2026(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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


class AllergyIntoleranceParticipant(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who or what participated in the activities related to the allergy or
    intolerance and how they were involved.
    Indicates who or what participated in the activities related to the allergy
    or intolerance and how they were involved.
    """

    resource_type = Field("AllergyIntoleranceParticipant", const=True)

    actor: fhirtypes.ReferenceType = Field(
        ...,
        alias="actor",
        title=(
            "Who or what participated in the activities related to the allergy or "
            "intolerance"
        ),
        description=(
            "Indicates who or what participated in the activities related to the "
            "allergy or intolerance."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "Patient",
            "RelatedPerson",
            "Device",
            "Organization",
            "CareTeam",
        ],
    )

    function: fhirtypes.CodeableConceptType = Field(
        None,
        alias="function",
        title="Type of involvement",
        description=(
            "Distinguishes the type of involvement of the actor in the activities "
            "related to the allergy or intolerance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AllergyIntoleranceParticipant`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "function", "actor"]


class AllergyIntoleranceReaction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
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
        title="Description of the event as a whole",
        description=(
            "Text description about the reaction as a whole, including details of "
            "the manifestation if required."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    exposureRoute: fhirtypes.CodeableConceptType = Field(
        None,
        alias="exposureRoute",
        title="How the subject was exposed to the substance",
        description=(
            "Identification of the route by which the subject was exposed to the "
            "substance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    manifestation: typing.List[fhirtypes.CodeableReferenceType] = Field(
        ...,
        alias="manifestation",
        title="Clinical symptoms/signs associated with the Event",
        description=(
            "Clinical symptoms and/or signs that are observed or associated with "
            "the adverse reaction event."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Observation"],
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Text about event not captured in other fields",
        description=(
            "Additional text about the adverse reaction event not captured in other"
            " fields."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    onset: fhirtypes.DateTime = Field(
        None,
        alias="onset",
        title="Date(/time) when manifestations showed",
        description="Record of the date and/or time of the onset of the Reaction.",
        # if property is element of this resource.
        element_property=True,
    )
    onset__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_onset", title="Extension field for ``onset``."
    )

    severity: fhirtypes.Code = Field(
        None,
        alias="severity",
        title="mild | moderate | severe (of event as a whole)",
        description=(
            "Clinical assessment of the severity of the reaction event as a whole, "
            "potentially considering multiple different manifestations."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["mild", "moderate", "severe"],
    )
    severity__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_severity", title="Extension field for ``severity``."
    )

    substance: fhirtypes.CodeableConceptType = Field(
        None,
        alias="substance",
        title=(
            "Specific substance or pharmaceutical product considered to be "
            "responsible for event"
        ),
        description=(
            "Identification of the specific substance (or pharmaceutical product) "
            "considered to be responsible for the Adverse Reaction event. Note: the"
            " substance for a specific reaction may be different from the substance"
            " identified as the cause of the risk, but it must be consistent with "
            "it. For instance, it may be a more specific substance (e.g. a brand "
            "medication) or a composite product that includes the identified "
            "substance. It must be clinically safe to only process the 'code' and "
            "ignore the 'reaction.substance'.  If a receiving system is unable to "
            "confirm that AllergyIntolerance.reaction.substance falls within the "
            "semantic scope of AllergyIntolerance.code, then the receiving system "
            "should ignore AllergyIntolerance.reaction.substance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AllergyIntoleranceReaction`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "substance",
            "manifestation",
            "description",
            "onset",
            "severity",
            "exposureRoute",
            "note",
        ]
