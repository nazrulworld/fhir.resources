# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PlanDefinition
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class PlanDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The definition of a plan for a series of actions, independent of any
    specific patient or context.
    This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical artifacts
    such as clinical decision support rules, order sets and protocols.
    """

    resource_type = Field("PlanDefinition", const=True)

    action: typing.List[fhirtypes.PlanDefinitionActionType] = Field(
        None,
        alias="action",
        title="Action defined by the plan",
        description="An action to be taken as part of the plan.",
        # if property is element of this resource.
        element_property=True,
    )

    approvalDate: fhirtypes.Date = Field(
        None,
        alias="approvalDate",
        title="When the plan definition was approved by publisher",
        description=(
            "The date on which the resource content was approved by the publisher. "
            "Approval happens once when the content is officially approved for "
            "usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_approvalDate", title="Extension field for ``approvalDate``."
    )

    contact: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="Contact details for the publisher",
        description=(
            "Contact details to assist a user in finding and communicating with the"
            " publisher."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    contributor: typing.List[fhirtypes.ContributorType] = Field(
        None,
        alias="contributor",
        title="A content contributor",
        description=(
            "A contributor to the content of the asset, including authors, editors,"
            " reviewers, and endorsers."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the plan definition and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the plan definition."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date this was last changed",
        description=(
            "The date  (and optionally time) when the plan definition was "
            "published. The date must change if and when the business version "
            "changes and it must change if the status code changes. In addition, it"
            " should change when the substantive content of the plan definition "
            "changes."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Natural language description of the plan definition",
        description=(
            "A free text natural language description of the plan definition from a"
            " consumer's perspective."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="When the plan definition is expected to be used",
        description=(
            "The period during which the plan definition content was or is planned "
            "to be in active use."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A boolean value to indicate that this plan definition is authored for "
            "testing purposes (or education/evaluation/marketing), and is not "
            "intended to be used for genuine usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    goal: typing.List[fhirtypes.PlanDefinitionGoalType] = Field(
        None,
        alias="goal",
        title="What the plan is trying to accomplish",
        description=(
            "Goals that describe what the activities within the plan are intended "
            "to achieve. For example, weight loss, restoring an activity of daily "
            "living, obtaining herd immunity via immunization, meeting a process "
            "improvement objective, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Additional identifier for the plan definition",
        description=(
            "A formal identifier that is used to identify this plan definition when"
            " it is represented in other formats, or referenced in a specification,"
            " model, design or an instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for plan definition (if applicable)",
        description=(
            "A legal or geographic region in which the plan definition is intended "
            "to be used."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    lastReviewDate: fhirtypes.Date = Field(
        None,
        alias="lastReviewDate",
        title="When the plan definition was last reviewed",
        description=(
            "The date on which the resource content was last reviewed. Review "
            "happens periodically after approval, but doesn't change the original "
            "approval date."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastReviewDate", title="Extension field for ``lastReviewDate``."
    )

    library: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="library",
        title="Logic used by the plan definition",
        description=(
            "A reference to a Library resource containing any formal logic used by "
            "the plan definition."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Library"],
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name for this plan definition (computer friendly)",
        description=(
            "A natural language name identifying the plan definition. This name "
            "should be usable as an identifier for the module by machine processing"
            " applications such as code generation."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the individual or organization that published the plan "
            "definition."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Why this plan definition is defined",
        description=(
            "Explaination of why this plan definition is needed and why it has been"
            " designed as it has."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    relatedArtifact: typing.List[fhirtypes.RelatedArtifactType] = Field(
        None,
        alias="relatedArtifact",
        title="Related artifacts for the asset",
        description=(
            "Related artifacts such as additional documentation, justification, or "
            "bibliographic references."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this plan definition. Enables tracking the life-cycle of"
            " the content."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired", "unknown"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Name for this plan definition (human friendly)",
        description="A short, descriptive, user-friendly title for the plan definition.",
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    topic: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="topic",
        title="E.g. Education, Treatment, Assessment, etc",
        description=(
            "Descriptive topics related to the content of the plan definition. "
            "Topics provide a high-level categorization of the definition that can "
            "be useful for filtering and searching."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="order-set | protocol | eca-rule",
        description=(
            "The type of asset the plan definition represents, e.g. an order set, "
            "protocol, or event-condition-action rule."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Logical URI to reference this plan definition (globally unique)",
        description=(
            "An absolute URI that is used to identify this plan definition when it "
            "is referenced in a specification, model, design or an instance. This "
            "SHALL be a URL, SHOULD be globally unique, and SHOULD be an address at"
            " which this plan definition is (or will be) published. The URL SHOULD "
            "include the major version of the plan definition. For more information"
            " see [Technical and Business Versions](resource.html#versions)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    usage: fhirtypes.String = Field(
        None,
        alias="usage",
        title="Describes the clinical usage of the asset",
        description=(
            "A detailed description of how the asset is used from a clinical "
            "perspective."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    usage__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_usage", title="Extension field for ``usage``."
    )

    useContext: typing.List[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="Context the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These terms may be used to assist with "
            "indexing and searching for appropriate plan definition instances."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the plan definition",
        description=(
            "The identifier that is used to identify this version of the plan "
            "definition when it is referenced in a specification, model, design or "
            "instance. This is an arbitrary value managed by the plan definition "
            "author and is not expected to be globally unique. For example, it "
            "might be a timestamp (e.g. yyyymmdd) if a managed version is not "
            "available. There is also no expectation that versions can be placed in"
            " a lexicographical sequence. To provide a version consistent with the "
            "Decision Support Service specification, use the format "
            "Major.Minor.Revision (e.g. 1.0.0). For more information on versioning "
            "knowledge assets, refer to the Decision Support Service specification."
            " Note that a version is required for non-experimental active "
            "artifacts."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PlanDefinition`` according specification,
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
            "name",
            "title",
            "type",
            "status",
            "experimental",
            "date",
            "publisher",
            "description",
            "purpose",
            "usage",
            "approvalDate",
            "lastReviewDate",
            "effectivePeriod",
            "useContext",
            "jurisdiction",
            "topic",
            "contributor",
            "contact",
            "copyright",
            "relatedArtifact",
            "library",
            "goal",
            "action",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1618(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class PlanDefinitionAction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Action defined by the plan.
    An action to be taken as part of the plan.
    """

    resource_type = Field("PlanDefinitionAction", const=True)

    action: typing.List[fhirtypes.PlanDefinitionActionType] = Field(
        None,
        alias="action",
        title="A sub-action",
        description=(
            "Sub actions that are contained within the action. The behavior of this"
            " action determines the functionality of the sub-actions. For example, "
            "a selection behavior of at-most-one indicates that of the sub-actions,"
            " at most one may be chosen as part of realizing the action definition."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    cardinalityBehavior: fhirtypes.Code = Field(
        None,
        alias="cardinalityBehavior",
        title="single | multiple",
        description="Defines whether the action can be selected multiple times.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["single", "multiple"],
    )
    cardinalityBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_cardinalityBehavior",
        title="Extension field for ``cardinalityBehavior``.",
    )

    code: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="code",
        title="Code representing the meaning of the action or sub-actions",
        description=(
            "A code that provides meaning for the action or action group. For "
            "example, a section may have a LOINC code for a the section of a "
            "documentation template."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    condition: typing.List[fhirtypes.PlanDefinitionActionConditionType] = Field(
        None,
        alias="condition",
        title="Whether or not the action is applicable",
        description=(
            "An expression that describes applicability criteria, or start/stop "
            "conditions for the action."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    definition: fhirtypes.ReferenceType = Field(
        None,
        alias="definition",
        title="Description of the activity to be performed",
        description=(
            "A reference to an ActivityDefinition that describes the action to be "
            "taken in detail, or a PlanDefinition that describes a series of "
            "actions to be taken."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ActivityDefinition", "PlanDefinition"],
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Short description of the action",
        description=(
            "A short description of the action used to provide a summary to display"
            " to the user."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    documentation: typing.List[fhirtypes.RelatedArtifactType] = Field(
        None,
        alias="documentation",
        title="Supporting documentation for the intended performer of the action",
        description=(
            "Didactic or other informational resources associated with the action "
            "that can be provided to the CDS recipient. Information resources can "
            "include inline text commentary and links to web resources."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    dynamicValue: typing.List[fhirtypes.PlanDefinitionActionDynamicValueType] = Field(
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
        # if property is element of this resource.
        element_property=True,
    )

    goalId: typing.List[fhirtypes.Id] = Field(
        None,
        alias="goalId",
        title="What goals this action supports",
        description=(
            "Identifies goals that this action supports. The reference must be to a"
            " goal element defined within this plan definition."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    goalId__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_goalId", title="Extension field for ``goalId``.")

    groupingBehavior: fhirtypes.Code = Field(
        None,
        alias="groupingBehavior",
        title="visual-group | logical-group | sentence-group",
        description="Defines the grouping behavior for the action and its children.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["visual-group", "logical-group", "sentence-group"],
    )
    groupingBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_groupingBehavior",
        title="Extension field for ``groupingBehavior``.",
    )

    input: typing.List[fhirtypes.DataRequirementType] = Field(
        None,
        alias="input",
        title="Input data requirements",
        description="Defines input data requirements for the action.",
        # if property is element of this resource.
        element_property=True,
    )

    label: fhirtypes.String = Field(
        None,
        alias="label",
        title="User-visible label for the action (e.g. 1. or A.)",
        description="A user-visible label for the action.",
        # if property is element of this resource.
        element_property=True,
    )
    label__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_label", title="Extension field for ``label``."
    )

    output: typing.List[fhirtypes.DataRequirementType] = Field(
        None,
        alias="output",
        title="Output data definition",
        description="Defines the outputs of the action, if any.",
        # if property is element of this resource.
        element_property=True,
    )

    participant: typing.List[fhirtypes.PlanDefinitionActionParticipantType] = Field(
        None,
        alias="participant",
        title="Who should participate in the action",
        description="Indicates who should participate in performing the action described.",
        # if property is element of this resource.
        element_property=True,
    )

    precheckBehavior: fhirtypes.Code = Field(
        None,
        alias="precheckBehavior",
        title="yes | no",
        description="Defines whether the action should usually be preselected.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["yes", "no"],
    )
    precheckBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_precheckBehavior",
        title="Extension field for ``precheckBehavior``.",
    )

    reason: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reason",
        title="Why the action should be performed",
        description="A description of why this action is necessary or appropriate.",
        # if property is element of this resource.
        element_property=True,
    )

    relatedAction: typing.List[fhirtypes.PlanDefinitionActionRelatedActionType] = Field(
        None,
        alias="relatedAction",
        title="Relationship to another action",
        description=(
            'A relationship to another action such as "before" or "30-60 minutes '
            'after start of".'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    requiredBehavior: fhirtypes.Code = Field(
        None,
        alias="requiredBehavior",
        title="must | could | must-unless-documented",
        description="Defines the requiredness behavior for the action.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["must", "could", "must-unless-documented"],
    )
    requiredBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_requiredBehavior",
        title="Extension field for ``requiredBehavior``.",
    )

    selectionBehavior: fhirtypes.Code = Field(
        None,
        alias="selectionBehavior",
        title="any | all | all-or-none | exactly-one | at-most-one | one-or-more",
        description="Defines the selection behavior for the action and its children.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "any",
            "all",
            "all-or-none",
            "exactly-one",
            "at-most-one",
            "one-or-more",
        ],
    )
    selectionBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_selectionBehavior",
        title="Extension field for ``selectionBehavior``.",
    )

    textEquivalent: fhirtypes.String = Field(
        None,
        alias="textEquivalent",
        title=(
            "Static text equivalent of the action, used if the dynamic aspects "
            "cannot be interpreted by the receiving system"
        ),
        description=(
            "A text equivalent of the action to be performed. This provides a "
            "human-interpretable description of the action when the definition is "
            "consumed by a system that may not be capable of interpreting it "
            "dynamically."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    textEquivalent__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_textEquivalent", title="Extension field for ``textEquivalent``."
    )

    timingDateTime: fhirtypes.DateTime = Field(
        None,
        alias="timingDateTime",
        title="When the action should take place",
        description="An optional value describing when the action should be performed.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e timing[x]
        one_of_many="timing",
        one_of_many_required=False,
    )
    timingDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_timingDateTime", title="Extension field for ``timingDateTime``."
    )

    timingDuration: fhirtypes.DurationType = Field(
        None,
        alias="timingDuration",
        title="When the action should take place",
        description="An optional value describing when the action should be performed.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e timing[x]
        one_of_many="timing",
        one_of_many_required=False,
    )

    timingPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="timingPeriod",
        title="When the action should take place",
        description="An optional value describing when the action should be performed.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e timing[x]
        one_of_many="timing",
        one_of_many_required=False,
    )

    timingRange: fhirtypes.RangeType = Field(
        None,
        alias="timingRange",
        title="When the action should take place",
        description="An optional value describing when the action should be performed.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e timing[x]
        one_of_many="timing",
        one_of_many_required=False,
    )

    timingTiming: fhirtypes.TimingType = Field(
        None,
        alias="timingTiming",
        title="When the action should take place",
        description="An optional value describing when the action should be performed.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e timing[x]
        one_of_many="timing",
        one_of_many_required=False,
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="User-visible title",
        description="The title of the action displayed to a user.",
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    transform: fhirtypes.ReferenceType = Field(
        None,
        alias="transform",
        title="Transform to apply the template",
        description=(
            "A reference to a StructureMap resource that defines a transform that "
            "can be executed to produce the intent resource using the "
            "ActivityDefinition instance as the input."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureMap"],
    )

    triggerDefinition: typing.List[fhirtypes.TriggerDefinitionType] = Field(
        None,
        alias="triggerDefinition",
        title="When the action should be triggered",
        description="A description of when the action should be triggered.",
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodingType = Field(
        None,
        alias="type",
        title="create | update | remove | fire-event",
        description="The type of action to perform (create, update, remove).",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PlanDefinitionAction`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "label",
            "title",
            "description",
            "textEquivalent",
            "code",
            "reason",
            "documentation",
            "goalId",
            "triggerDefinition",
            "condition",
            "input",
            "output",
            "relatedAction",
            "timingDateTime",
            "timingPeriod",
            "timingDuration",
            "timingRange",
            "timingTiming",
            "participant",
            "type",
            "groupingBehavior",
            "selectionBehavior",
            "requiredBehavior",
            "precheckBehavior",
            "cardinalityBehavior",
            "definition",
            "transform",
            "dynamicValue",
            "action",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2224(
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
            "timing": [
                "timingDateTime",
                "timingDuration",
                "timingPeriod",
                "timingRange",
                "timingTiming",
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


class PlanDefinitionActionCondition(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Whether or not the action is applicable.
    An expression that describes applicability criteria, or start/stop
    conditions for the action.
    """

    resource_type = Field("PlanDefinitionActionCondition", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Natural language description of the condition",
        description=(
            "A brief, natural language description of the condition that "
            "effectively communicates the intended semantics."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    expression: fhirtypes.String = Field(
        None,
        alias="expression",
        title="Boolean-valued expression",
        description=(
            "An expression that returns true or false, indicating whether or not "
            "the condition is satisfied."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_expression", title="Extension field for ``expression``."
    )

    kind: fhirtypes.Code = Field(
        None,
        alias="kind",
        title="applicability | start | stop",
        description="The kind of condition.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["applicability", "start", "stop"],
    )
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_kind", title="Extension field for ``kind``."
    )

    language: fhirtypes.String = Field(
        None,
        alias="language",
        title="Language of the expression",
        description="The media type of the language for the expression.",
        # if property is element of this resource.
        element_property=True,
    )
    language__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_language", title="Extension field for ``language``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PlanDefinitionActionCondition`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "kind",
            "description",
            "language",
            "expression",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3159(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("kind", "kind__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class PlanDefinitionActionDynamicValue(backboneelement.BackboneElement):
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

    resource_type = Field("PlanDefinitionActionDynamicValue", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Natural language description of the dynamic value",
        description=(
            "A brief, natural language description of the intended semantics of the"
            " dynamic value."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    expression: fhirtypes.String = Field(
        None,
        alias="expression",
        title="An expression that provides the dynamic value for the customization",
        description="An expression specifying the value of the customized element.",
        # if property is element of this resource.
        element_property=True,
    )
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_expression", title="Extension field for ``expression``."
    )

    language: fhirtypes.String = Field(
        None,
        alias="language",
        title="Language of the expression",
        description="The media type of the language for the expression.",
        # if property is element of this resource.
        element_property=True,
    )
    language__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_language", title="Extension field for ``language``."
    )

    path: fhirtypes.String = Field(
        None,
        alias="path",
        title="The path to the element to be set dynamically",
        description=(
            "The path to the element to be customized. This is the path on the "
            "resource that will hold the result of the calculation defined by the "
            "expression."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_path", title="Extension field for ``path``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PlanDefinitionActionDynamicValue`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "description",
            "path",
            "language",
            "expression",
        ]


class PlanDefinitionActionParticipant(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who should participate in the action.
    Indicates who should participate in performing the action described.
    """

    resource_type = Field("PlanDefinitionActionParticipant", const=True)

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="E.g. Nurse, Surgeon, Parent, etc",
        description=(
            "The role the participant should play in performing the described "
            "action."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="patient | practitioner | related-person",
        description="The type of participant in the action.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["patient", "practitioner", "related-person"],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PlanDefinitionActionParticipant`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "role"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3381(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("type", "type__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class PlanDefinitionActionRelatedAction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Relationship to another action.
    A relationship to another action such as "before" or "30-60 minutes after
    start of".
    """

    resource_type = Field("PlanDefinitionActionRelatedAction", const=True)

    actionId: fhirtypes.Id = Field(
        None,
        alias="actionId",
        title="What action is this related to",
        description="The element id of the related action.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    actionId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_actionId", title="Extension field for ``actionId``."
    )

    offsetDuration: fhirtypes.DurationType = Field(
        None,
        alias="offsetDuration",
        title="Time offset for the relationship",
        description=(
            "A duration or range of durations to apply to the relationship. For "
            "example, 30-60 minutes before."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e offset[x]
        one_of_many="offset",
        one_of_many_required=False,
    )

    offsetRange: fhirtypes.RangeType = Field(
        None,
        alias="offsetRange",
        title="Time offset for the relationship",
        description=(
            "A duration or range of durations to apply to the relationship. For "
            "example, 30-60 minutes before."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e offset[x]
        one_of_many="offset",
        one_of_many_required=False,
    )

    relationship: fhirtypes.Code = Field(
        None,
        alias="relationship",
        title=(
            "before-start | before | before-end | concurrent-with-start | "
            "concurrent | concurrent-with-end | after-start | after | after-end"
        ),
        description="The relationship of this action to the related action.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "before-start",
            "before",
            "before-end",
            "concurrent-with-start",
            "concurrent",
            "concurrent-with-end",
            "after-start",
            "after",
            "after-end",
        ],
    )
    relationship__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_relationship", title="Extension field for ``relationship``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PlanDefinitionActionRelatedAction`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "actionId",
            "relationship",
            "offsetDuration",
            "offsetRange",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3535(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("actionId", "actionId__ext"),
            ("relationship", "relationship__ext"),
        ]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3535(
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
        one_of_many_fields = {"offset": ["offsetDuration", "offsetRange"]}
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


class PlanDefinitionGoal(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What the plan is trying to accomplish.
    Goals that describe what the activities within the plan are intended to
    achieve. For example, weight loss, restoring an activity of daily living,
    obtaining herd immunity via immunization, meeting a process improvement
    objective, etc.
    """

    resource_type = Field("PlanDefinitionGoal", const=True)

    addresses: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="addresses",
        title="What does the goal address",
        description=(
            "Identifies problems, conditions, issues, or concerns the goal is "
            "intended to address."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="E.g. Treatment, dietary, behavioral, etc",
        description="Indicates a category the goal falls within.",
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="description",
        title="Code or text describing the goal",
        description=(
            "Human-readable and/or coded description of a specific desired "
            'objective of care, such as "control blood pressure" or "negotiate an '
            'obstacle course" or "dance with child at wedding".'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    documentation: typing.List[fhirtypes.RelatedArtifactType] = Field(
        None,
        alias="documentation",
        title="Supporting documentation for the goal",
        description=(
            "Didactic or other informational resources associated with the goal "
            "that provide further supporting information about the goal. "
            "Information resources can include inline text commentary and links to "
            "web resources."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    priority: fhirtypes.CodeableConceptType = Field(
        None,
        alias="priority",
        title="high-priority | medium-priority | low-priority",
        description=(
            "Identifies the expected level of importance associated with "
            "reaching/sustaining the defined goal."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    start: fhirtypes.CodeableConceptType = Field(
        None,
        alias="start",
        title="When goal pursuit begins",
        description="The event after which the goal should begin being pursued.",
        # if property is element of this resource.
        element_property=True,
    )

    target: typing.List[fhirtypes.PlanDefinitionGoalTargetType] = Field(
        None,
        alias="target",
        title="Target outcome for the goal",
        description="Indicates what should be done and within what timeframe.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PlanDefinitionGoal`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "category",
            "description",
            "priority",
            "start",
            "addresses",
            "documentation",
            "target",
        ]


class PlanDefinitionGoalTarget(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Target outcome for the goal.
    Indicates what should be done and within what timeframe.
    """

    resource_type = Field("PlanDefinitionGoalTarget", const=True)

    detailCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="detailCodeableConcept",
        title="The target value to be achieved",
        description=(
            "The target value of the measure to be achieved to signify fulfillment "
            "of the goal, e.g. 150 pounds or 7.0%. Either the high or low or both "
            "values of the range can be specified. Whan a low value is missing, it "
            "indicates that the goal is achieved at any value at or below the high "
            "value. Similarly, if the high value is missing, it indicates that the "
            "goal is achieved at any value at or above the low value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e detail[x]
        one_of_many="detail",
        one_of_many_required=False,
    )

    detailQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="detailQuantity",
        title="The target value to be achieved",
        description=(
            "The target value of the measure to be achieved to signify fulfillment "
            "of the goal, e.g. 150 pounds or 7.0%. Either the high or low or both "
            "values of the range can be specified. Whan a low value is missing, it "
            "indicates that the goal is achieved at any value at or below the high "
            "value. Similarly, if the high value is missing, it indicates that the "
            "goal is achieved at any value at or above the low value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e detail[x]
        one_of_many="detail",
        one_of_many_required=False,
    )

    detailRange: fhirtypes.RangeType = Field(
        None,
        alias="detailRange",
        title="The target value to be achieved",
        description=(
            "The target value of the measure to be achieved to signify fulfillment "
            "of the goal, e.g. 150 pounds or 7.0%. Either the high or low or both "
            "values of the range can be specified. Whan a low value is missing, it "
            "indicates that the goal is achieved at any value at or below the high "
            "value. Similarly, if the high value is missing, it indicates that the "
            "goal is achieved at any value at or above the low value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e detail[x]
        one_of_many="detail",
        one_of_many_required=False,
    )

    due: fhirtypes.DurationType = Field(
        None,
        alias="due",
        title="Reach goal within",
        description=(
            "Indicates the timeframe after the start of the goal in which the goal "
            "should be met."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    measure: fhirtypes.CodeableConceptType = Field(
        None,
        alias="measure",
        title="The parameter whose value is to be tracked",
        description=(
            "The parameter whose value is to be tracked, e.g. body weigth, blood "
            "pressure, or hemoglobin A1c level."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PlanDefinitionGoalTarget`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "measure",
            "detailQuantity",
            "detailRange",
            "detailCodeableConcept",
            "due",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2626(
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
            "detail": ["detailCodeableConcept", "detailQuantity", "detailRange"]
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
