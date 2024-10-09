from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ActivityDefinition
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ActivityDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The definition of a specific activity to be taken, independent of any
    particular patient or context.
    This resource allows for the definition of some activity to be performed,
    independent of a particular patient, practitioner, or other performance
    context.
    """

    __resource_type__ = "ActivityDefinition"

    approvalDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="approvalDate",
        title="When the activity definition was approved by publisher",
        description=(
            "The date on which the resource content was approved by the publisher. "
            "Approval happens once when the content is officially approved for "
            "usage."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_approvalDate", title="Extension field for ``approvalDate``."
    )

    asNeededBoolean: bool | None = Field(  # type: ignore
        None,
        alias="asNeededBoolean",
        title="Preconditions for service",
        description=(
            "If a CodeableConcept is present, it indicates the pre-condition for "
            'performing the service.  For example "pain", "on flare-up", etc.'
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e asNeeded[x]
            "one_of_many": "asNeeded",
            "one_of_many_required": False,
        },
    )
    asNeededBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_asNeededBoolean", title="Extension field for ``asNeededBoolean``."
    )

    asNeededCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="asNeededCodeableConcept",
        title="Preconditions for service",
        description=(
            "If a CodeableConcept is present, it indicates the pre-condition for "
            'performing the service.  For example "pain", "on flare-up", etc.'
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e asNeeded[x]
            "one_of_many": "asNeeded",
            "one_of_many_required": False,
        },
    )

    author: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        None,
        alias="author",
        title="Who authored the content",
        description=(
            "An individiual or organization primarily involved in the creation and "
            "maintenance of the content."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    bodySite: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="bodySite",
        title="What part of body to perform on",
        description=(
            "Indicates the sites on the subject's body where the procedure should "
            "be performed (I.e. the target sites)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Detail type of activity",
        description=(
            "Detailed description of the type of activity; e.g. What lab test, what"
            " procedure, what kind of encounter."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    contact: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        None,
        alias="contact",
        title="Contact details for the publisher",
        description=(
            "Contact details to assist a user in finding and communicating with the"
            " publisher."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    copyright: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the activity definition and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the activity definition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    copyrightLabel: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="copyrightLabel",
        title="Copyright holder and year(s)",
        description=(
            "A short string (<50 characters), suitable for inclusion in a page "
            "footer that identifies the copyright holder, effective period, and "
            "optionally whether rights are resctricted. (e.g. 'All rights "
            "reserved', 'Some rights reserved')."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    copyrightLabel__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_copyrightLabel", title="Extension field for ``copyrightLabel``."
    )

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the activity definition was last "
            "significantly changed. The date must change when the business version "
            "changes and it must change if the status code changes. In addition, it"
            " should change when the substantive content of the activity definition"
            " changes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Natural language description of the activity definition",
        description=(
            "A free text natural language description of the activity definition "
            "from a consumer's perspective."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    doNotPerform: bool | None = Field(  # type: ignore
        None,
        alias="doNotPerform",
        title="True if the activity should not be performed",
        description=(
            "Set this to true if the definition is to indicate that a particular "
            "activity should NOT be performed. If true, this element should be "
            "interpreted to reinforce a negative coding. For example NPO as a code "
            "with a doNotPerform of true would still indicate to NOT perform the "
            "action."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    doNotPerform__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_doNotPerform", title="Extension field for ``doNotPerform``."
    )

    dosage: typing.List[fhirtypes.DosageType] | None = Field(  # type: ignore
        None,
        alias="dosage",
        title="Detailed dosage instructions",
        description=(
            "Provides detailed dosage instructions in the same way that they are "
            "described for MedicationRequest resources."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    dynamicValue: typing.List[fhirtypes.ActivityDefinitionDynamicValueType] | None = Field(  # type: ignore
        None,
        alias="dynamicValue",
        title="Dynamic aspects of the definition",
        description=(
            "Dynamic values that will be evaluated to produce values for elements "
            "of the resulting resource. For example, if the dosage of a medication "
            "must be computed based on the patient's weight, a dynamic value would "
            "be used to specify an expression that calculated the weight, and the "
            "path on the request resource that would contain the result."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    editor: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        None,
        alias="editor",
        title="Who edited the content",
        description=(
            "An individual or organization primarily responsible for internal "
            "coherence of the content."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    effectivePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="effectivePeriod",
        title="When the activity definition is expected to be used",
        description=(
            "The period during which the activity definition content was or is "
            "planned to be in active use."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    endorser: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        None,
        alias="endorser",
        title="Who endorsed the content",
        description=(
            "An individual or organization asserted by the publisher to be "
            "responsible for officially endorsing the content for use in some "
            "setting."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    experimental: bool | None = Field(  # type: ignore
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this activity definition is authored "
            "for testing purposes (or education/evaluation/marketing) and is not "
            "intended to be used for genuine usage."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Additional identifier for the activity definition",
        description=(
            "A formal identifier that is used to identify this activity definition "
            "when it is represented in other formats, or referenced in a "
            "specification, model, design or an instance."
        ),
        json_schema_extra={
            "element_property": True,
        },
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
            "activity and where the request should fit into the workflow chain."
        ),
        json_schema_extra={
            "element_property": True,
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

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for activity definition (if applicable)",
        description=(
            "A legal or geographic region in which the activity definition is "
            "intended to be used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    kind: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="kind",
        title="Kind of resource",
        description=(
            "A description of the kind of resource the activity definition is "
            "representing. For example, a MedicationRequest, a ServiceRequest, or a"
            " CommunicationRequest."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_kind", title="Extension field for ``kind``."
    )

    lastReviewDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="lastReviewDate",
        title="When the activity definition was last reviewed by the publisher",
        description=(
            "The date on which the resource content was last reviewed. Review "
            "happens periodically after approval but does not change the original "
            "approval date."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_lastReviewDate", title="Extension field for ``lastReviewDate``."
    )

    library: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="library",
        title="Logic used by the activity definition",
        description=(
            "A reference to a Library resource containing any formal logic used by "
            "the activity definition."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Library"],
        },
    )
    library__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_library", title="Extension field for ``library``."
    )

    location: fhirtypes.CodeableReferenceType | None = Field(  # type: ignore
        None,
        alias="location",
        title="Where it should happen",
        description=(
            "Identifies the facility where the activity will occur; e.g. home, "
            "hospital, specific clinic, etc."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name for this activity definition (computer friendly)",
        description=(
            "A natural language name identifying the activity definition. This name"
            " should be usable as an identifier for the module by machine "
            "processing applications such as code generation."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    observationRequirement: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="observationRequirement",
        title="What observations are required to perform this action",
        description=(
            "Defines observation requirements for the action to be performed, such "
            "as body weight or surface area."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ObservationDefinition"],
        },
    )
    observationRequirement__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_observationRequirement",
        title="Extension field for ``observationRequirement``.",
    )

    observationResultRequirement: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="observationResultRequirement",
        title="What observations must be produced by this action",
        description=(
            "Defines the observations that are expected to be produced by the "
            "action."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ObservationDefinition"],
        },
    )
    observationResultRequirement__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_observationResultRequirement",
        title="Extension field for ``observationResultRequirement``.",
    )

    participant: typing.List[fhirtypes.ActivityDefinitionParticipantType] | None = Field(  # type: ignore
        None,
        alias="participant",
        title="Who should participate in the action",
        description="Indicates who should participate in performing the action described.",
        json_schema_extra={
            "element_property": True,
        },
    )

    priority: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="priority",
        title="routine | urgent | asap | stat",
        description=(
            "Indicates how quickly the activity  should be addressed with respect "
            "to other requests."
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

    productCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="productCodeableConcept",
        title="What's administered/supplied",
        description=(
            "Identifies the food, drug or other product being consumed or supplied "
            "in the activity."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e product[x]
            "one_of_many": "product",
            "one_of_many_required": False,
        },
    )

    productReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="productReference",
        title="What's administered/supplied",
        description=(
            "Identifies the food, drug or other product being consumed or supplied "
            "in the activity."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e product[x]
            "one_of_many": "product",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Medication",
                "Ingredient",
                "Substance",
                "SubstanceDefinition",
            ],
        },
    )

    profile: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="profile",
        title="What profile the resource needs to conform to",
        description=(
            "A profile to which the target of the activity definition is expected "
            "to conform."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["StructureDefinition"],
        },
    )
    profile__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_profile", title="Extension field for ``profile``."
    )

    publisher: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="publisher",
        title="Name of the publisher/steward (organization or individual)",
        description=(
            "The name of the organization or individual responsible for the release"
            " and ongoing maintenance of the activity definition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="purpose",
        title="Why this activity definition is defined",
        description=(
            "Explanation of why this activity definition is needed and why it has "
            "been designed as it has."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="How much is administered/consumed/supplied",
        description=(
            "Identifies the quantity expected to be consumed at once (per dose, per"
            " meal, etc.)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    relatedArtifact: typing.List[fhirtypes.RelatedArtifactType] | None = Field(  # type: ignore
        None,
        alias="relatedArtifact",
        title="Additional documentation, citations, etc",
        description=(
            "Related artifacts such as additional documentation, justification, or "
            "bibliographic references."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reviewer: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        None,
        alias="reviewer",
        title="Who reviewed the content",
        description=(
            "An individual or organization asserted by the publisher to be "
            "primarily responsible for review of some aspect of the content."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    specimenRequirement: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="specimenRequirement",
        title="What specimens are required to perform this action",
        description=(
            "Defines specimen requirements for the action to be performed, such as "
            "required specimens for a lab test."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["SpecimenDefinition"],
        },
    )
    specimenRequirement__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_specimenRequirement",
        title="Extension field for ``specimenRequirement``.",
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this activity definition. Enables tracking the life-"
            "cycle of the content."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["draft", "active", "retired", "unknown"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    subjectCanonical: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="subjectCanonical",
        title="Type of individual the activity definition is intended for",
        description=(
            "A code, group definition, or canonical reference that describes  or "
            "identifies the intended subject of the activity being defined.  "
            "Canonical references are allowed to support the definition of "
            "protocols for drug and substance quality specifications, and is "
            "allowed to reference a MedicinalProductDefinition, "
            "SubstanceDefinition, AdministrableProductDefinition, "
            "ManufacturedItemDefinition, or PackagedProductDefinition resource."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e subject[x]
            "one_of_many": "subject",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["EvidenceVariable"],
        },
    )
    subjectCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_subjectCanonical",
        title="Extension field for ``subjectCanonical``.",
    )

    subjectCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="subjectCodeableConcept",
        title="Type of individual the activity definition is intended for",
        description=(
            "A code, group definition, or canonical reference that describes  or "
            "identifies the intended subject of the activity being defined.  "
            "Canonical references are allowed to support the definition of "
            "protocols for drug and substance quality specifications, and is "
            "allowed to reference a MedicinalProductDefinition, "
            "SubstanceDefinition, AdministrableProductDefinition, "
            "ManufacturedItemDefinition, or PackagedProductDefinition resource."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e subject[x]
            "one_of_many": "subject",
            "one_of_many_required": False,
        },
    )

    subjectReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="subjectReference",
        title="Type of individual the activity definition is intended for",
        description=(
            "A code, group definition, or canonical reference that describes  or "
            "identifies the intended subject of the activity being defined.  "
            "Canonical references are allowed to support the definition of "
            "protocols for drug and substance quality specifications, and is "
            "allowed to reference a MedicinalProductDefinition, "
            "SubstanceDefinition, AdministrableProductDefinition, "
            "ManufacturedItemDefinition, or PackagedProductDefinition resource."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e subject[x]
            "one_of_many": "subject",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Group",
                "MedicinalProductDefinition",
                "SubstanceDefinition",
                "AdministrableProductDefinition",
                "ManufacturedItemDefinition",
                "PackagedProductDefinition",
            ],
        },
    )

    subtitle: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="subtitle",
        title="Subordinate title of the activity definition",
        description=(
            "An explanatory or alternate title for the activity definition giving "
            "additional information about its content."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    subtitle__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_subtitle", title="Extension field for ``subtitle``."
    )

    timingAge: fhirtypes.AgeType | None = Field(  # type: ignore
        None,
        alias="timingAge",
        title="When activity is to occur",
        description="The timing or frequency upon which the described activity is to occur.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e timing[x]
            "one_of_many": "timing",
            "one_of_many_required": False,
        },
    )

    timingDuration: fhirtypes.DurationType | None = Field(  # type: ignore
        None,
        alias="timingDuration",
        title="When activity is to occur",
        description="The timing or frequency upon which the described activity is to occur.",
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
        title="When activity is to occur",
        description="The timing or frequency upon which the described activity is to occur.",
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
        title="When activity is to occur",
        description="The timing or frequency upon which the described activity is to occur.",
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
        title="Name for this activity definition (human friendly)",
        description="A short, descriptive, user-friendly title for the activity definition.",
        json_schema_extra={
            "element_property": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    topic: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="topic",
        title="E.g. Education, Treatment, Assessment, etc",
        description=(
            "Descriptive topics related to the content of the activity. Topics "
            "provide a high-level categorization of the activity that can be useful"
            " for filtering and searching."
        ),
        json_schema_extra={
            "element_property": True,
        },
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

    url: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="url",
        title=(
            "Canonical identifier for this activity definition, represented as a "
            "URI (globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this activity definition when"
            " it is referenced in a specification, model, design or an instance; "
            "also called its canonical identifier. This SHOULD be globally unique "
            "and SHOULD be a literal address at which an authoritative instance of "
            "this activity definition is (or will be) published. This URL can be "
            "the target of a canonical reference. It SHALL remain the same when the"
            " activity definition is stored on different servers."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_url", title="Extension field for ``url``."
    )

    usage: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="usage",
        title="Describes the clinical usage of the activity definition",
        description=(
            "A detailed description of how the activity definition is used from a "
            "clinical perspective."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    usage__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_usage", title="Extension field for ``usage``."
    )

    useContext: typing.List[fhirtypes.UsageContextType] | None = Field(  # type: ignore
        None,
        alias="useContext",
        title="The context that the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These contexts may be general categories "
            "(gender, age, ...) or may be references to specific programs "
            "(insurance plans, studies, ...) and may be used to assist with "
            "indexing and searching for appropriate activity definition instances."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="Business version of the activity definition",
        description=(
            "The identifier that is used to identify this version of the activity "
            "definition when it is referenced in a specification, model, design or "
            "instance. This is an arbitrary value managed by the activity "
            "definition author and is not expected to be globally unique. For "
            "example, it might be a timestamp (e.g. yyyymmdd) if a managed version "
            "is not available. There is also no expectation that versions can be "
            "placed in a lexicographical sequence. To provide a version consistent "
            "with the Decision Support Service specification, use the format "
            "Major.Minor.Revision (e.g. 1.0.0). For more information on versioning "
            "knowledge assets, refer to the Decision Support Service specification."
            " Note that a version is required for non-experimental active assets."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_version", title="Extension field for ``version``."
    )

    versionAlgorithmCoding: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="versionAlgorithmCoding",
        title="How to compare versions",
        description=(
            "Indicates the mechanism used to compare versions to determine which is"
            " more current."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e versionAlgorithm[x]
            "one_of_many": "versionAlgorithm",
            "one_of_many_required": False,
        },
    )

    versionAlgorithmString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="versionAlgorithmString",
        title="How to compare versions",
        description=(
            "Indicates the mechanism used to compare versions to determine which is"
            " more current."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e versionAlgorithm[x]
            "one_of_many": "versionAlgorithm",
            "one_of_many_required": False,
        },
    )
    versionAlgorithmString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_versionAlgorithmString",
        title="Extension field for ``versionAlgorithmString``.",
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ActivityDefinition`` according specification,
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
            "url",
            "identifier",
            "version",
            "versionAlgorithmString",
            "versionAlgorithmCoding",
            "name",
            "title",
            "subtitle",
            "status",
            "experimental",
            "subjectCodeableConcept",
            "subjectReference",
            "subjectCanonical",
            "date",
            "publisher",
            "contact",
            "description",
            "useContext",
            "jurisdiction",
            "purpose",
            "usage",
            "copyright",
            "copyrightLabel",
            "approvalDate",
            "lastReviewDate",
            "effectivePeriod",
            "topic",
            "author",
            "editor",
            "reviewer",
            "endorser",
            "relatedArtifact",
            "library",
            "kind",
            "profile",
            "code",
            "intent",
            "priority",
            "doNotPerform",
            "timingTiming",
            "timingAge",
            "timingRange",
            "timingDuration",
            "asNeededBoolean",
            "asNeededCodeableConcept",
            "location",
            "participant",
            "productReference",
            "productCodeableConcept",
            "quantity",
            "dosage",
            "bodySite",
            "specimenRequirement",
            "observationRequirement",
            "observationResultRequirement",
            "transform",
            "dynamicValue",
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
        one_of_many_fields = {
            "asNeeded": ["asNeededBoolean", "asNeededCodeableConcept"],
            "product": ["productCodeableConcept", "productReference"],
            "subject": [
                "subjectCanonical",
                "subjectCodeableConcept",
                "subjectReference",
            ],
            "timing": ["timingAge", "timingDuration", "timingRange", "timingTiming"],
            "versionAlgorithm": ["versionAlgorithmCoding", "versionAlgorithmString"],
        }
        return one_of_many_fields


class ActivityDefinitionDynamicValue(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Dynamic aspects of the definition.
    Dynamic values that will be evaluated to produce values for elements of the
    resulting resource. For example, if the dosage of a medication must be
    computed based on the patient's weight, a dynamic value would be used to
    specify an expression that calculated the weight, and the path on the
    request resource that would contain the result.
    """

    __resource_type__ = "ActivityDefinitionDynamicValue"

    expression: fhirtypes.ExpressionType = Field(  # type: ignore
        ...,
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
            "element_required": True,
        },
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_path", title="Extension field for ``path``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ActivityDefinitionDynamicValue`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "path", "expression"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("path", "path__ext")]
        return required_fields


class ActivityDefinitionParticipant(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who should participate in the action.
    Indicates who should participate in performing the action described.
    """

    __resource_type__ = "ActivityDefinitionParticipant"

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
        ``ActivityDefinitionParticipant`` according specification,
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
        ]
