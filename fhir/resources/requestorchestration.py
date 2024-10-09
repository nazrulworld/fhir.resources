from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/RequestOrchestration
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class RequestOrchestration(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A set of related requests.
    A set of related requests that can be used to capture intended activities
    that have inter-dependencies such as "give this medication after that one".
    """

    __resource_type__ = "RequestOrchestration"

    action: typing.List[fhirtypes.RequestOrchestrationActionType] | None = Field(  # type: ignore
        None,
        alias="action",
        title="Proposed actions, if any",
        description="The actions, if any, produced by the evaluation of the artifact.",
        json_schema_extra={
            "element_property": True,
        },
    )

    author: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="author",
        title="Device or practitioner that authored the request orchestration",
        description="Provides a reference to the author of the request orchestration.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Device", "Practitioner", "PractitionerRole"],
        },
    )

    authoredOn: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="authoredOn",
        title="When the request orchestration was authored",
        description="Indicates when the request orchestration was created.",
        json_schema_extra={
            "element_property": True,
        },
    )
    authoredOn__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_authoredOn", title="Extension field for ``authoredOn``."
    )

    basedOn: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="basedOn",
        title="Fulfills plan, proposal, or order",
        description=(
            "A plan, proposal or order that is fulfilled in whole or in part by "
            "this request."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title="What's being requested/ordered",
        description="A code that identifies what the overall request orchestration is.",
        json_schema_extra={
            "element_property": True,
        },
    )

    encounter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="encounter",
        title="Created as part of",
        description="Describes the context of the request orchestration, if any.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter"],
        },
    )

    goal: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="goal",
        title="What goals",
        description=(
            "Goals that are intended to be achieved by following the requests in "
            "this RequestOrchestration."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Goal"],
        },
    )

    groupIdentifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="groupIdentifier",
        title="Composite request this is part of",
        description=(
            "A shared identifier common to multiple independent Request instances "
            "that were activated/authorized more or less simultaneously by a single"
            " author.  The presence of the same identifier on each request ties "
            "those requests together and may have business ramifications in terms "
            "of reporting of results, billing, etc.  E.g. a requisition number "
            "shared by a set of lab tests ordered together, or a prescription "
            "number shared by all meds ordered at one time."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business identifier",
        description=(
            "Allows a service to provide a unique, business identifier for the "
            "request."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    instantiatesCanonical: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="instantiatesCanonical",
        title="Instantiates FHIR protocol or definition",
        description=(
            "A canonical URL referencing a FHIR-defined protocol, guideline, "
            "orderset or other definition that is adhered to in whole or in part by"
            " this request."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    instantiatesCanonical__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_instantiatesCanonical",
        title="Extension field for ``instantiatesCanonical``.",
    )

    instantiatesUri: typing.List[fhirtypes.UriType | None] | None = Field(  # type: ignore
        None,
        alias="instantiatesUri",
        title="Instantiates external protocol or definition",
        description=(
            "A URL referencing an externally defined protocol, guideline, orderset "
            "or other definition that is adhered to in whole or in part by this "
            "request."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    instantiatesUri__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_instantiatesUri", title="Extension field for ``instantiatesUri``."
    )

    intent: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="intent",
        title=(
            "proposal | plan | directive | order | original-order | reflex-order | "
            "filler-order | instance-order | option"
        ),
        description=(
            "Indicates the level of authority/intentionality associated with the "
            "request and where the request fits into the workflow chain."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "proposal",
                "plan",
                "directive",
                "order",
                "original-order",
                "reflex-order",
                "filler-order",
                "instance-order",
                "option",
            ],
        },
    )
    intent__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_intent", title="Extension field for ``intent``."
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="note",
        title="Additional notes about the response",
        description=(
            "Provides a mechanism to communicate additional information about the "
            "response."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    priority: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="priority",
        title="routine | urgent | asap | stat",
        description=(
            "Indicates how quickly the request should be addressed with respect to "
            "other requests."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["routine", "urgent", "asap", "stat"],
        },
    )
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_priority", title="Extension field for ``priority``."
    )

    reason: typing.List[fhirtypes.CodeableReferenceType] | None = Field(  # type: ignore
        None,
        alias="reason",
        title="Why the request orchestration is needed",
        description=(
            "Describes the reason for the request orchestration in coded or textual"
            " form."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Condition",
                "Observation",
                "DiagnosticReport",
                "DocumentReference",
            ],
        },
    )

    replaces: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="replaces",
        title="Request(s) replaced by this request",
        description=(
            "Completed or terminated request(s) whose function is taken by this new"
            " request."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title=(
            "draft | active | on-hold | revoked | completed | entered-in-error | "
            "unknown"
        ),
        description=(
            "The current state of the request. For request orchestrations, the "
            "status reflects the status of all the requests in the orchestration."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "draft",
                "active",
                "on-hold",
                "revoked",
                "completed",
                "entered-in-error",
                "unknown",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="subject",
        title="Who the request orchestration is about",
        description="The subject for which the request orchestration was created.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "CareTeam",
                "Device",
                "Group",
                "HealthcareService",
                "Location",
                "Organization",
                "Patient",
                "Practitioner",
                "PractitionerRole",
                "RelatedPerson",
            ],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``RequestOrchestration`` according specification,
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
            "instantiatesCanonical",
            "instantiatesUri",
            "basedOn",
            "replaces",
            "groupIdentifier",
            "status",
            "intent",
            "priority",
            "code",
            "subject",
            "encounter",
            "authoredOn",
            "author",
            "reason",
            "goal",
            "note",
            "action",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("intent", "intent__ext"), ("status", "status__ext")]
        return required_fields


class RequestOrchestrationAction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Proposed actions, if any.
    The actions, if any, produced by the evaluation of the artifact.
    """

    __resource_type__ = "RequestOrchestrationAction"

    action: typing.List[fhirtypes.RequestOrchestrationActionType] | None = Field(  # type: ignore
        None,
        alias="action",
        title="Sub action",
        description="Sub actions.",
        json_schema_extra={
            "element_property": True,
        },
    )

    cardinalityBehavior: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="cardinalityBehavior",
        title="single | multiple",
        description="Defines whether the action can be selected multiple times.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["single", "multiple"],
        },
    )
    cardinalityBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_cardinalityBehavior",
        title="Extension field for ``cardinalityBehavior``.",
    )

    code: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="code",
        title="Code representing the meaning of the action or sub-actions",
        description=(
            "A code that provides meaning for the action or action group. For "
            "example, a section may have a LOINC code for a section of a "
            "documentation template."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    condition: typing.List[fhirtypes.RequestOrchestrationActionConditionType] | None = Field(  # type: ignore
        None,
        alias="condition",
        title="Whether or not the action is applicable",
        description=(
            "An expression that describes applicability criteria, or start/stop "
            "conditions for the action."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    definitionCanonical: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="definitionCanonical",
        title="Description of the activity to be performed",
        description=(
            "A reference to an ActivityDefinition that describes the action to be "
            "taken in detail, a PlanDefinition that describes a series of actions "
            "to be taken, a Questionnaire that should be filled out, a "
            "SpecimenDefinition describing a specimen to be collected, or an "
            "ObservationDefinition that specifies what observation should be "
            "captured."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e definition[x]
            "one_of_many": "definition",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "ActivityDefinition",
                "ObservationDefinition",
                "PlanDefinition",
                "Questionnaire",
                "SpecimenDefinition",
            ],
        },
    )
    definitionCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_definitionCanonical",
        title="Extension field for ``definitionCanonical``.",
    )

    definitionUri: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="definitionUri",
        title="Description of the activity to be performed",
        description=(
            "A reference to an ActivityDefinition that describes the action to be "
            "taken in detail, a PlanDefinition that describes a series of actions "
            "to be taken, a Questionnaire that should be filled out, a "
            "SpecimenDefinition describing a specimen to be collected, or an "
            "ObservationDefinition that specifies what observation should be "
            "captured."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e definition[x]
            "one_of_many": "definition",
            "one_of_many_required": False,
        },
    )
    definitionUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_definitionUri", title="Extension field for ``definitionUri``."
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Short description of the action",
        description=(
            "A short description of the action used to provide a summary to display"
            " to the user."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    documentation: typing.List[fhirtypes.RelatedArtifactType] | None = Field(  # type: ignore
        None,
        alias="documentation",
        title="Supporting documentation for the intended performer of the action",
        description=(
            "Didactic or other informational resources associated with the action "
            "that can be provided to the CDS recipient. Information resources can "
            "include inline text commentary and links to web resources."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    dynamicValue: typing.List[fhirtypes.RequestOrchestrationActionDynamicValueType] | None = Field(  # type: ignore
        None,
        alias="dynamicValue",
        title="Dynamic aspects of the definition",
        description=(
            "Customizations that should be applied to the statically defined "
            "resource. For example, if the dosage of a medication must be computed "
            "based on the patient's weight, a customization would be used to "
            "specify an expression that calculated the weight, and the path on the "
            "resource that would contain the result."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    goal: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="goal",
        title="What goals",
        description=(
            "Goals that are intended to be achieved by following the requests in "
            "this action."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Goal"],
        },
    )

    groupingBehavior: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="groupingBehavior",
        title="visual-group | logical-group | sentence-group",
        description="Defines the grouping behavior for the action and its children.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["visual-group", "logical-group", "sentence-group"],
        },
    )
    groupingBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_groupingBehavior",
        title="Extension field for ``groupingBehavior``.",
    )

    input: typing.List[fhirtypes.RequestOrchestrationActionInputType] | None = Field(  # type: ignore
        None,
        alias="input",
        title="Input data requirements",
        description="Defines input data requirements for the action.",
        json_schema_extra={
            "element_property": True,
        },
    )

    linkId: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="linkId",
        title="Pointer to specific item from the PlanDefinition",
        description=(
            "The linkId of the action from the PlanDefinition that corresponds to "
            "this action in the RequestOrchestration resource."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_linkId", title="Extension field for ``linkId``."
    )

    location: fhirtypes.CodeableReferenceType | None = Field(  # type: ignore
        None,
        alias="location",
        title="Where it should happen",
        description=(
            "Identifies the facility where the action will occur; e.g. home, "
            "hospital, specific clinic, etc."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    output: typing.List[fhirtypes.RequestOrchestrationActionOutputType] | None = Field(  # type: ignore
        None,
        alias="output",
        title="Output data definition",
        description="Defines the outputs of the action, if any.",
        json_schema_extra={
            "element_property": True,
        },
    )

    participant: typing.List[fhirtypes.RequestOrchestrationActionParticipantType] | None = Field(  # type: ignore
        None,
        alias="participant",
        title="Who should perform the action",
        description="The participant that should perform or be responsible for this action.",
        json_schema_extra={
            "element_property": True,
        },
    )

    precheckBehavior: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="precheckBehavior",
        title="yes | no",
        description="Defines whether the action should usually be preselected.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["yes", "no"],
        },
    )
    precheckBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_precheckBehavior",
        title="Extension field for ``precheckBehavior``.",
    )

    prefix: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="prefix",
        title="User-visible prefix for the action (e.g. 1. or A.)",
        description=(
            "A user-visible prefix for the action. For example a section or item "
            "numbering such as 1. or A."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    prefix__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_prefix", title="Extension field for ``prefix``."
    )

    priority: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="priority",
        title="routine | urgent | asap | stat",
        description=(
            "Indicates how quickly the action should be addressed with respect to "
            "other actions."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["routine", "urgent", "asap", "stat"],
        },
    )
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_priority", title="Extension field for ``priority``."
    )

    relatedAction: typing.List[fhirtypes.RequestOrchestrationActionRelatedActionType] | None = Field(  # type: ignore
        None,
        alias="relatedAction",
        title="Relationship to another action",
        description=(
            'A relationship to another action such as "before" or "30-60 minutes '
            'after start of".'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    requiredBehavior: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="requiredBehavior",
        title="must | could | must-unless-documented",
        description="Defines expectations around whether an action is required.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["must", "could", "must-unless-documented"],
        },
    )
    requiredBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_requiredBehavior",
        title="Extension field for ``requiredBehavior``.",
    )

    resource: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="resource",
        title="The target of the action",
        description=(
            "The resource that is the target of the action (e.g. "
            "CommunicationRequest)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    selectionBehavior: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="selectionBehavior",
        title="any | all | all-or-none | exactly-one | at-most-one | one-or-more",
        description="Defines the selection behavior for the action and its children.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "any",
                "all",
                "all-or-none",
                "exactly-one",
                "at-most-one",
                "one-or-more",
            ],
        },
    )
    selectionBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_selectionBehavior",
        title="Extension field for ``selectionBehavior``.",
    )

    textEquivalent: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="textEquivalent",
        title=(
            "Static text equivalent of the action, used if the dynamic aspects "
            "cannot be interpreted by the receiving system"
        ),
        description=(
            "A text equivalent of the action to be performed. This provides a "
            "human-interpretable description of the action when the definition is "
            "consumed by a system that might not be capable of interpreting it "
            "dynamically."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    textEquivalent__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_textEquivalent", title="Extension field for ``textEquivalent``."
    )

    timingAge: fhirtypes.AgeType | None = Field(  # type: ignore
        None,
        alias="timingAge",
        title="When the action should take place",
        description="An optional value describing when the action should be performed.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e timing[x]
            "one_of_many": "timing",
            "one_of_many_required": False,
        },
    )

    timingDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="timingDateTime",
        title="When the action should take place",
        description="An optional value describing when the action should be performed.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e timing[x]
            "one_of_many": "timing",
            "one_of_many_required": False,
        },
    )
    timingDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_timingDateTime", title="Extension field for ``timingDateTime``."
    )

    timingDuration: fhirtypes.DurationType | None = Field(  # type: ignore
        None,
        alias="timingDuration",
        title="When the action should take place",
        description="An optional value describing when the action should be performed.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e timing[x]
            "one_of_many": "timing",
            "one_of_many_required": False,
        },
    )

    timingPeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="timingPeriod",
        title="When the action should take place",
        description="An optional value describing when the action should be performed.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e timing[x]
            "one_of_many": "timing",
            "one_of_many_required": False,
        },
    )

    timingRange: fhirtypes.RangeType | None = Field(  # type: ignore
        None,
        alias="timingRange",
        title="When the action should take place",
        description="An optional value describing when the action should be performed.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e timing[x]
            "one_of_many": "timing",
            "one_of_many_required": False,
        },
    )

    timingTiming: fhirtypes.TimingType | None = Field(  # type: ignore
        None,
        alias="timingTiming",
        title="When the action should take place",
        description="An optional value describing when the action should be performed.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e timing[x]
            "one_of_many": "timing",
            "one_of_many_required": False,
        },
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="User-visible title",
        description="The title of the action displayed to a user.",
        json_schema_extra={
            "element_property": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    transform: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="transform",
        title="Transform to apply the template",
        description=(
            "A reference to a StructureMap resource that defines a transform that "
            "can be executed to produce the intent resource using the "
            "ActivityDefinition instance as the input."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["StructureMap"],
        },
    )
    transform__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_transform", title="Extension field for ``transform``."
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="create | update | remove | fire-event",
        description="The type of action to perform (create, update, remove).",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``RequestOrchestrationAction`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "linkId",
            "prefix",
            "title",
            "description",
            "textEquivalent",
            "priority",
            "code",
            "documentation",
            "goal",
            "condition",
            "input",
            "output",
            "relatedAction",
            "timingDateTime",
            "timingAge",
            "timingPeriod",
            "timingDuration",
            "timingRange",
            "timingTiming",
            "location",
            "participant",
            "type",
            "groupingBehavior",
            "selectionBehavior",
            "requiredBehavior",
            "precheckBehavior",
            "cardinalityBehavior",
            "resource",
            "definitionCanonical",
            "definitionUri",
            "transform",
            "dynamicValue",
            "action",
        ]

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
        one_of_many_fields = {
            "definition": ["definitionCanonical", "definitionUri"],
            "timing": [
                "timingAge",
                "timingDateTime",
                "timingDuration",
                "timingPeriod",
                "timingRange",
                "timingTiming",
            ],
        }
        return one_of_many_fields


class RequestOrchestrationActionCondition(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Whether or not the action is applicable.
    An expression that describes applicability criteria, or start/stop
    conditions for the action.
    """

    __resource_type__ = "RequestOrchestrationActionCondition"

    expression: fhirtypes.ExpressionType | None = Field(  # type: ignore
        None,
        alias="expression",
        title="Boolean-valued expression",
        description=(
            "An expression that returns true or false, indicating whether or not "
            "the condition is satisfied."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    kind: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="kind",
        title="applicability | start | stop",
        description="The kind of condition.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["applicability", "start", "stop"],
        },
    )
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_kind", title="Extension field for ``kind``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``RequestOrchestrationActionCondition`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "kind", "expression"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("kind", "kind__ext")]
        return required_fields


class RequestOrchestrationActionDynamicValue(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Dynamic aspects of the definition.
    Customizations that should be applied to the statically defined resource.
    For example, if the dosage of a medication must be computed based on the
    patient's weight, a customization would be used to specify an expression
    that calculated the weight, and the path on the resource that would contain
    the result.
    """

    __resource_type__ = "RequestOrchestrationActionDynamicValue"

    expression: fhirtypes.ExpressionType | None = Field(  # type: ignore
        None,
        alias="expression",
        title="An expression that provides the dynamic value for the customization",
        description="An expression specifying the value of the customized element.",
        json_schema_extra={
            "element_property": True,
        },
    )

    path: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="path",
        title="The path to the element to be set dynamically",
        description=(
            "The path to the element to be customized. This is the path on the "
            "resource that will hold the result of the calculation defined by the "
            "expression. The specified path SHALL be a FHIRPath resolvable on the "
            "specified target type of the ActivityDefinition, and SHALL consist "
            "only of identifiers, constant indexers, and a restricted subset of "
            "functions. The path is allowed to contain qualifiers (.) to traverse "
            "sub-elements, as well as indexers ([x]) to traverse multiple-"
            "cardinality sub-elements (see the [Simple FHIRPath "
            "Profile](fhirpath.html#simple) for full details)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_path", title="Extension field for ``path``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``RequestOrchestrationActionDynamicValue`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "path", "expression"]


class RequestOrchestrationActionInput(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Input data requirements.
    Defines input data requirements for the action.
    """

    __resource_type__ = "RequestOrchestrationActionInput"

    relatedData: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="relatedData",
        title="What data is provided",
        description=(
            "Points to an existing input or output element that provides data to "
            "this input."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    relatedData__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_relatedData", title="Extension field for ``relatedData``."
    )

    requirement: fhirtypes.DataRequirementType | None = Field(  # type: ignore
        None,
        alias="requirement",
        title="What data is provided",
        description="Defines the data that is to be provided as input to the action.",
        json_schema_extra={
            "element_property": True,
        },
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="User-visible title",
        description=(
            "A human-readable label for the data requirement used to label data "
            "flows in BPMN or similar diagrams. Also provides a human readable "
            "label when rendering the data requirement that conveys its purpose to "
            "human readers."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``RequestOrchestrationActionInput`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "title",
            "requirement",
            "relatedData",
        ]


class RequestOrchestrationActionOutput(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Output data definition.
    Defines the outputs of the action, if any.
    """

    __resource_type__ = "RequestOrchestrationActionOutput"

    relatedData: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="relatedData",
        title="What data is provided",
        description=(
            "Points to an existing input or output element that is results as "
            "output from the action."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    relatedData__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_relatedData", title="Extension field for ``relatedData``."
    )

    requirement: fhirtypes.DataRequirementType | None = Field(  # type: ignore
        None,
        alias="requirement",
        title="What data is provided",
        description="Defines the data that results as output from the action.",
        json_schema_extra={
            "element_property": True,
        },
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="User-visible title",
        description=(
            "A human-readable label for the data requirement used to label data "
            "flows in BPMN or similar diagrams. Also provides a human readable "
            "label when rendering the data requirement that conveys its purpose to "
            "human readers."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``RequestOrchestrationActionOutput`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "title",
            "requirement",
            "relatedData",
        ]


class RequestOrchestrationActionParticipant(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who should perform the action.
    The participant that should perform or be responsible for this action.
    """

    __resource_type__ = "RequestOrchestrationActionParticipant"

    actorCanonical: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="actorCanonical",
        title="Who/what is participating?",
        description="A reference to the actual participant.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e actor[x]
            "one_of_many": "actor",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["CapabilityStatement"],
        },
    )
    actorCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_actorCanonical", title="Extension field for ``actorCanonical``."
    )

    actorReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="actorReference",
        title="Who/what is participating?",
        description="A reference to the actual participant.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e actor[x]
            "one_of_many": "actor",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "CareTeam",
                "Device",
                "DeviceDefinition",
                "Endpoint",
                "Group",
                "HealthcareService",
                "Location",
                "Organization",
                "Patient",
                "Practitioner",
                "PractitionerRole",
                "RelatedPerson",
            ],
        },
    )

    function: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="function",
        title="E.g. Author, Reviewer, Witness, etc",
        description=(
            "Indicates how the actor will be involved in the action - author, "
            "reviewer, witness, etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    role: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="role",
        title="E.g. Nurse, Surgeon, Parent, etc",
        description=(
            "The role the participant should play in performing the described "
            "action."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title=(
            "careteam | device | group | healthcareservice | location | "
            "organization | patient | practitioner | practitionerrole | "
            "relatedperson"
        ),
        description="The type of participant in the action.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "careteam",
                "device",
                "group",
                "healthcareservice",
                "location",
                "organization",
                "patient",
                "practitioner",
                "practitionerrole",
                "relatedperson",
            ],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    typeCanonical: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="typeCanonical",
        title="Who or what can participate",
        description="The type of participant in the action.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["CapabilityStatement"],
        },
    )
    typeCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_typeCanonical", title="Extension field for ``typeCanonical``."
    )

    typeReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="typeReference",
        title="Who or what can participate",
        description="The type of participant in the action.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "CareTeam",
                "Device",
                "DeviceDefinition",
                "Endpoint",
                "Group",
                "HealthcareService",
                "Location",
                "Organization",
                "Patient",
                "Practitioner",
                "PractitionerRole",
                "RelatedPerson",
            ],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``RequestOrchestrationActionParticipant`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "typeCanonical",
            "typeReference",
            "role",
            "function",
            "actorCanonical",
            "actorReference",
        ]

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
        one_of_many_fields = {"actor": ["actorCanonical", "actorReference"]}
        return one_of_many_fields


class RequestOrchestrationActionRelatedAction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Relationship to another action.
    A relationship to another action such as "before" or "30-60 minutes after
    start of".
    """

    __resource_type__ = "RequestOrchestrationActionRelatedAction"

    endRelationship: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="endRelationship",
        title=(
            "before | before-start | before-end | concurrent | concurrent-with-"
            "start | concurrent-with-end | after | after-start | after-end"
        ),
        description="The relationship of the end of this action to the related action.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "before",
                "before-start",
                "before-end",
                "concurrent",
                "concurrent-with-start",
                "concurrent-with-end",
                "after",
                "after-start",
                "after-end",
            ],
        },
    )
    endRelationship__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_endRelationship", title="Extension field for ``endRelationship``."
    )

    offsetDuration: fhirtypes.DurationType | None = Field(  # type: ignore
        None,
        alias="offsetDuration",
        title="Time offset for the relationship",
        description=(
            "A duration or range of durations to apply to the relationship. For "
            "example, 30-60 minutes before."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e offset[x]
            "one_of_many": "offset",
            "one_of_many_required": False,
        },
    )

    offsetRange: fhirtypes.RangeType | None = Field(  # type: ignore
        None,
        alias="offsetRange",
        title="Time offset for the relationship",
        description=(
            "A duration or range of durations to apply to the relationship. For "
            "example, 30-60 minutes before."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e offset[x]
            "one_of_many": "offset",
            "one_of_many_required": False,
        },
    )

    relationship: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="relationship",
        title=(
            "before | before-start | before-end | concurrent | concurrent-with-"
            "start | concurrent-with-end | after | after-start | after-end"
        ),
        description="The relationship of this action to the related action.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "before",
                "before-start",
                "before-end",
                "concurrent",
                "concurrent-with-start",
                "concurrent-with-end",
                "after",
                "after-start",
                "after-end",
            ],
        },
    )
    relationship__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_relationship", title="Extension field for ``relationship``."
    )

    targetId: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="targetId",
        title="What action this is related to",
        description="The element id of the target related action.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    targetId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_targetId", title="Extension field for ``targetId``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``RequestOrchestrationActionRelatedAction`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "targetId",
            "relationship",
            "endRelationship",
            "offsetDuration",
            "offsetRange",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("relationship", "relationship__ext"),
            ("targetId", "targetId__ext"),
        ]
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
        one_of_many_fields = {"offset": ["offsetDuration", "offsetRange"]}
        return one_of_many_fields
