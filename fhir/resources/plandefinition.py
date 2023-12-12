# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PlanDefinition
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class PlanDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The definition of a plan for a series of actions, independent of any
    specific patient or context.
    This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical and non-
    clinical artifacts such as clinical decision support rules, order sets,
    protocols, and drug quality specifications.
    """

    resource_type = Field("PlanDefinition", const=True)

    action: typing.List[fhirtypes.PlanDefinitionActionType] = Field(
        None,
        alias="action",
        title="Action defined by the plan",
        description=(
            "An action or group of actions to be taken as part of the plan. For "
            "example, in clinical care, an action would be to prescribe a "
            "particular indicated medication, or perform a particular test as "
            "appropriate. In pharmaceutical quality, an action would be the test "
            "that needs to be performed on a drug product as defined in the quality"
            " specification."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    actor: typing.List[fhirtypes.PlanDefinitionActorType] = Field(
        None,
        alias="actor",
        title="Actors within the plan",
        description=(
            "Actors represent the individuals or groups involved in the execution "
            "of the defined set of activities."
        ),
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

    asNeededBoolean: bool = Field(
        None,
        alias="asNeededBoolean",
        title="Preconditions for service",
        description=(
            "If a CodeableConcept is present, it indicates the pre-condition for "
            'performing the service.  For example "pain", "on flare-up", etc.'
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e asNeeded[x]
        one_of_many="asNeeded",
        one_of_many_required=False,
    )
    asNeededBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_asNeededBoolean", title="Extension field for ``asNeededBoolean``."
    )

    asNeededCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="asNeededCodeableConcept",
        title="Preconditions for service",
        description=(
            "If a CodeableConcept is present, it indicates the pre-condition for "
            'performing the service.  For example "pain", "on flare-up", etc.'
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e asNeeded[x]
        one_of_many="asNeeded",
        one_of_many_required=False,
    )

    author: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="author",
        title="Who authored the content",
        description=(
            "An individiual or organization primarily involved in the creation and "
            "maintenance of the content."
        ),
        # if property is element of this resource.
        element_property=True,
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

    copyrightLabel: fhirtypes.String = Field(
        None,
        alias="copyrightLabel",
        title="Copyright holder and year(s)",
        description=(
            "A short string (<50 characters), suitable for inclusion in a page "
            "footer that identifies the copyright holder, effective period, and "
            "optionally whether rights are resctricted. (e.g. 'All rights "
            "reserved', 'Some rights reserved')."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    copyrightLabel__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyrightLabel", title="Extension field for ``copyrightLabel``."
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the plan definition was last "
            "significantly changed. The date must change when the business version "
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

    editor: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="editor",
        title="Who edited the content",
        description=(
            "An individual or organization primarily responsible for internal "
            "coherence of the content."
        ),
        # if property is element of this resource.
        element_property=True,
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

    endorser: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="endorser",
        title="Who endorsed the content",
        description=(
            "An individual or organization asserted by the publisher to be "
            "responsible for officially endorsing the content for use in some "
            "setting."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this plan definition is authored for "
            "testing purposes (or education/evaluation/marketing) and is not "
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
            "A goal describes an expected outcome that activities within the plan "
            "are intended to achieve. For example, weight loss, restoring an "
            "activity of daily living, obtaining herd immunity via immunization, "
            "meeting a process improvement objective, meeting the acceptance "
            "criteria for a test as specified by a quality specification, etc."
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
        title="When the plan definition was last reviewed by the publisher",
        description=(
            "The date on which the resource content was last reviewed. Review "
            "happens periodically after approval but does not change the original "
            "approval date."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastReviewDate", title="Extension field for ``lastReviewDate``."
    )

    library: typing.List[typing.Optional[fhirtypes.Canonical]] = Field(
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
    library__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_library", title="Extension field for ``library``.")

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
        title="Name of the publisher/steward (organization or individual)",
        description=(
            "The name of the organization or individual responsible for the release"
            " and ongoing maintenance of the plan definition."
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
            "Explanation of why this plan definition is needed and why it has been "
            "designed as it has."
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
        title="Additional documentation, citations",
        description=(
            "Related artifacts such as additional documentation, justification, or "
            "bibliographic references."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    reviewer: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="reviewer",
        title="Who reviewed the content",
        description=(
            "An individual or organization asserted by the publisher to be "
            "primarily responsible for review of some aspect of the content."
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

    subjectCanonical: fhirtypes.Canonical = Field(
        None,
        alias="subjectCanonical",
        title="Type of individual the plan definition is focused on",
        description=(
            "A code, group definition, or canonical reference that describes  or "
            "identifies the intended subject of the plan definition. Canonical "
            "references are allowed to support the definition of protocols for drug"
            " and substance quality specifications, and is allowed to reference a "
            "MedicinalProductDefinition, SubstanceDefinition, "
            "AdministrableProductDefinition, ManufacturedItemDefinition, or "
            "PackagedProductDefinition resource."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e subject[x]
        one_of_many="subject",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["EvidenceVariable"],
    )
    subjectCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_subjectCanonical",
        title="Extension field for ``subjectCanonical``.",
    )

    subjectCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="subjectCodeableConcept",
        title="Type of individual the plan definition is focused on",
        description=(
            "A code, group definition, or canonical reference that describes  or "
            "identifies the intended subject of the plan definition. Canonical "
            "references are allowed to support the definition of protocols for drug"
            " and substance quality specifications, and is allowed to reference a "
            "MedicinalProductDefinition, SubstanceDefinition, "
            "AdministrableProductDefinition, ManufacturedItemDefinition, or "
            "PackagedProductDefinition resource."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e subject[x]
        one_of_many="subject",
        one_of_many_required=False,
    )

    subjectReference: fhirtypes.ReferenceType = Field(
        None,
        alias="subjectReference",
        title="Type of individual the plan definition is focused on",
        description=(
            "A code, group definition, or canonical reference that describes  or "
            "identifies the intended subject of the plan definition. Canonical "
            "references are allowed to support the definition of protocols for drug"
            " and substance quality specifications, and is allowed to reference a "
            "MedicinalProductDefinition, SubstanceDefinition, "
            "AdministrableProductDefinition, ManufacturedItemDefinition, or "
            "PackagedProductDefinition resource."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e subject[x]
        one_of_many="subject",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Group",
            "MedicinalProductDefinition",
            "SubstanceDefinition",
            "AdministrableProductDefinition",
            "ManufacturedItemDefinition",
            "PackagedProductDefinition",
        ],
    )

    subtitle: fhirtypes.String = Field(
        None,
        alias="subtitle",
        title="Subordinate title of the plan definition",
        description=(
            "An explanatory or alternate title for the plan definition giving "
            "additional information about its content."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    subtitle__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_subtitle", title="Extension field for ``subtitle``."
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
        title="E.g. Education, Treatment, Assessment",
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
        title="order-set | clinical-protocol | eca-rule | workflow-definition",
        description=(
            "A high-level category for the plan definition that distinguishes the "
            "kinds of systems that would be interested in the plan definition."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title=(
            "Canonical identifier for this plan definition, represented as a URI "
            "(globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this plan definition when it "
            "is referenced in a specification, model, design or an instance; also "
            "called its canonical identifier. This SHOULD be globally unique and "
            "SHOULD be a literal address at which an authoritative instance of this"
            " plan definition is (or will be) published. This URL can be the target"
            " of a canonical reference. It SHALL remain the same when the plan "
            "definition is stored on different servers."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    usage: fhirtypes.Markdown = Field(
        None,
        alias="usage",
        title="Describes the clinical usage of the plan",
        description=(
            "A detailed description of how the plan definition is used from a "
            "clinical perspective."
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
        title="The context that the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These contexts may be general categories "
            "(gender, age, ...) or may be references to specific programs "
            "(insurance plans, studies, ...) and may be used to assist with "
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

    versionAlgorithmCoding: fhirtypes.CodingType = Field(
        None,
        alias="versionAlgorithmCoding",
        title="How to compare versions",
        description=(
            "Indicates the mechanism used to compare versions to determine which is"
            " more current."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e versionAlgorithm[x]
        one_of_many="versionAlgorithm",
        one_of_many_required=False,
    )

    versionAlgorithmString: fhirtypes.String = Field(
        None,
        alias="versionAlgorithmString",
        title="How to compare versions",
        description=(
            "Indicates the mechanism used to compare versions to determine which is"
            " more current."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e versionAlgorithm[x]
        one_of_many="versionAlgorithm",
        one_of_many_required=False,
    )
    versionAlgorithmString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_versionAlgorithmString",
        title="Extension field for ``versionAlgorithmString``.",
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
            "versionAlgorithmString",
            "versionAlgorithmCoding",
            "name",
            "title",
            "subtitle",
            "type",
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
            "goal",
            "actor",
            "action",
            "asNeededBoolean",
            "asNeededCodeableConcept",
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1618(
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
            "asNeeded": ["asNeededBoolean", "asNeededCodeableConcept"],
            "subject": [
                "subjectCanonical",
                "subjectCodeableConcept",
                "subjectReference",
            ],
            "versionAlgorithm": ["versionAlgorithmCoding", "versionAlgorithmString"],
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


class PlanDefinitionAction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Action defined by the plan.
    An action or group of actions to be taken as part of the plan. For example,
    in clinical care, an action would be to prescribe a particular indicated
    medication, or perform a particular test as appropriate. In pharmaceutical
    quality, an action would be the test that needs to be performed on a drug
    product as defined in the quality specification.
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

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Code representing the meaning of the action or sub-actions",
        description=(
            "A code that provides a meaning, grouping, or classification for the "
            "action or action group. For example, a section may have a LOINC code "
            "for the section of a documentation template. In pharmaceutical "
            "quality, an action (Test) such as pH could be classified as a physical"
            " property."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    condition: typing.List[fhirtypes.PlanDefinitionActionConditionType] = Field(
        None,
        alias="condition",
        title="Whether or not the action is applicable",
        description=(
            "An expression that describes applicability criteria or start/stop "
            "conditions for the action."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    definitionCanonical: fhirtypes.Canonical = Field(
        None,
        alias="definitionCanonical",
        title="Description of the activity to be performed",
        description=(
            "A reference to an ActivityDefinition that describes the action to be "
            "taken in detail, a MessageDefinition describing a message to be snet, "
            "a PlanDefinition that describes a series of actions to be taken, a "
            "Questionnaire that should be filled out, a SpecimenDefinition "
            "describing a specimen to be collected, or an ObservationDefinition "
            "that specifies what observation should be captured."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e definition[x]
        one_of_many="definition",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "ActivityDefinition",
            "MessageDefinition",
            "ObservationDefinition",
            "PlanDefinition",
            "Questionnaire",
            "SpecimenDefinition",
        ],
    )
    definitionCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_definitionCanonical",
        title="Extension field for ``definitionCanonical``.",
    )

    definitionUri: fhirtypes.Uri = Field(
        None,
        alias="definitionUri",
        title="Description of the activity to be performed",
        description=(
            "A reference to an ActivityDefinition that describes the action to be "
            "taken in detail, a MessageDefinition describing a message to be snet, "
            "a PlanDefinition that describes a series of actions to be taken, a "
            "Questionnaire that should be filled out, a SpecimenDefinition "
            "describing a specimen to be collected, or an ObservationDefinition "
            "that specifies what observation should be captured."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e definition[x]
        one_of_many="definition",
        one_of_many_required=False,
    )
    definitionUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_definitionUri", title="Extension field for ``definitionUri``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Brief description of the action",
        description=(
            "A brief description of the action used to provide a summary to display"
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

    goalId: typing.List[typing.Optional[fhirtypes.Id]] = Field(
        None,
        alias="goalId",
        title="What goals this action supports",
        description=(
            "Identifies goals that this action supports. The reference must be to a"
            " goal element defined within this plan definition. In pharmaceutical "
            "quality, a goal represents acceptance criteria (Goal) for a given "
            "action (Test), so the goalId would be the unique id of a defined goal "
            "element establishing the acceptance criteria for the action."
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

    input: typing.List[fhirtypes.PlanDefinitionActionInputType] = Field(
        None,
        alias="input",
        title="Input data requirements",
        description="Defines input data requirements for the action.",
        # if property is element of this resource.
        element_property=True,
    )

    linkId: fhirtypes.String = Field(
        None,
        alias="linkId",
        title="Unique id for the action in the PlanDefinition",
        description=(
            "An identifier that is unique within the PlanDefinition to allow "
            "linkage within the realized CarePlan and/or RequestOrchestration."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_linkId", title="Extension field for ``linkId``."
    )

    location: fhirtypes.CodeableReferenceType = Field(
        None,
        alias="location",
        title="Where it should happen",
        description=(
            "Identifies the facility where the action will occur; e.g. home, "
            "hospital, specific clinic, etc."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    output: typing.List[fhirtypes.PlanDefinitionActionOutputType] = Field(
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

    prefix: fhirtypes.String = Field(
        None,
        alias="prefix",
        title="User-visible prefix for the action (e.g. 1. or A.)",
        description=(
            "A user-visible prefix for the action. For example a section or item "
            "numbering such as 1. or A."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    prefix__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_prefix", title="Extension field for ``prefix``."
    )

    priority: fhirtypes.Code = Field(
        None,
        alias="priority",
        title="routine | urgent | asap | stat",
        description=(
            "Indicates how quickly the action should be addressed with respect to "
            "other actions."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["routine", "urgent", "asap", "stat"],
    )
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_priority", title="Extension field for ``priority``."
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
        description="Defines the required behavior for the action.",
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

    subjectCanonical: fhirtypes.Canonical = Field(
        None,
        alias="subjectCanonical",
        title="Type of individual the action is focused on",
        description=(
            "A code, group definition, or canonical reference that describes the "
            "intended subject of the action and its children, if any. Canonical "
            "references are allowed to support the definition of protocols for drug"
            " and substance quality specifications, and is allowed to reference a "
            "MedicinalProductDefinition, SubstanceDefinition, "
            "AdministrableProductDefinition, ManufacturedItemDefinition, or "
            "PackagedProductDefinition resource."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e subject[x]
        one_of_many="subject",
        one_of_many_required=False,
    )
    subjectCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_subjectCanonical",
        title="Extension field for ``subjectCanonical``.",
    )

    subjectCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="subjectCodeableConcept",
        title="Type of individual the action is focused on",
        description=(
            "A code, group definition, or canonical reference that describes the "
            "intended subject of the action and its children, if any. Canonical "
            "references are allowed to support the definition of protocols for drug"
            " and substance quality specifications, and is allowed to reference a "
            "MedicinalProductDefinition, SubstanceDefinition, "
            "AdministrableProductDefinition, ManufacturedItemDefinition, or "
            "PackagedProductDefinition resource."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e subject[x]
        one_of_many="subject",
        one_of_many_required=False,
    )

    subjectReference: fhirtypes.ReferenceType = Field(
        None,
        alias="subjectReference",
        title="Type of individual the action is focused on",
        description=(
            "A code, group definition, or canonical reference that describes the "
            "intended subject of the action and its children, if any. Canonical "
            "references are allowed to support the definition of protocols for drug"
            " and substance quality specifications, and is allowed to reference a "
            "MedicinalProductDefinition, SubstanceDefinition, "
            "AdministrableProductDefinition, ManufacturedItemDefinition, or "
            "PackagedProductDefinition resource."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e subject[x]
        one_of_many="subject",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Group"],
    )

    textEquivalent: fhirtypes.Markdown = Field(
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
        # if property is element of this resource.
        element_property=True,
    )
    textEquivalent__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_textEquivalent", title="Extension field for ``textEquivalent``."
    )

    timingAge: fhirtypes.AgeType = Field(
        None,
        alias="timingAge",
        title="When the action should take place",
        description="An optional value describing when the action should be performed.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e timing[x]
        one_of_many="timing",
        one_of_many_required=False,
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
        description=(
            "The textual description of the action displayed to a user. For "
            "example, when the action is a test to be performed, the title would be"
            " the title of the test such as Assay by HPLC."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    transform: fhirtypes.Canonical = Field(
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
    transform__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_transform", title="Extension field for ``transform``."
    )

    trigger: typing.List[fhirtypes.TriggerDefinitionType] = Field(
        None,
        alias="trigger",
        title="When the action should be triggered",
        description=(
            "A description of when the action should be triggered. When multiple "
            "triggers are specified on an action, any triggering event invokes the "
            "action."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
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
            "linkId",
            "prefix",
            "title",
            "description",
            "textEquivalent",
            "priority",
            "code",
            "reason",
            "documentation",
            "goalId",
            "subjectCodeableConcept",
            "subjectReference",
            "subjectCanonical",
            "trigger",
            "condition",
            "input",
            "output",
            "relatedAction",
            "timingAge",
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
            "definitionCanonical",
            "definitionUri",
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
            "definition": ["definitionCanonical", "definitionUri"],
            "subject": [
                "subjectCanonical",
                "subjectCodeableConcept",
                "subjectReference",
            ],
            "timing": ["timingAge", "timingDuration", "timingRange", "timingTiming"],
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
    An expression that describes applicability criteria or start/stop
    conditions for the action.
    """

    resource_type = Field("PlanDefinitionActionCondition", const=True)

    expression: fhirtypes.ExpressionType = Field(
        None,
        alias="expression",
        title="Boolean-valued expression",
        description=(
            "An expression that returns true or false, indicating whether the "
            "condition is satisfied."
        ),
        # if property is element of this resource.
        element_property=True,
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

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PlanDefinitionActionCondition`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "kind", "expression"]

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

    expression: fhirtypes.ExpressionType = Field(
        None,
        alias="expression",
        title="An expression that provides the dynamic value for the customization",
        description="An expression specifying the value of the customized element.",
        # if property is element of this resource.
        element_property=True,
    )

    path: fhirtypes.String = Field(
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
        return ["id", "extension", "modifierExtension", "path", "expression"]


class PlanDefinitionActionInput(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Input data requirements.
    Defines input data requirements for the action.
    """

    resource_type = Field("PlanDefinitionActionInput", const=True)

    relatedData: fhirtypes.Id = Field(
        None,
        alias="relatedData",
        title="What data is provided",
        description=(
            "Points to an existing input or output element that provides data to "
            "this input."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    relatedData__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_relatedData", title="Extension field for ``relatedData``."
    )

    requirement: fhirtypes.DataRequirementType = Field(
        None,
        alias="requirement",
        title="What data is provided",
        description="Defines the data that is to be provided as input to the action.",
        # if property is element of this resource.
        element_property=True,
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="User-visible title",
        description=(
            "A human-readable label for the data requirement used to label data "
            "flows in BPMN or similar diagrams. Also provides a human readable "
            "label when rendering the data requirement that conveys its purpose to "
            "human readers."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PlanDefinitionActionInput`` according specification,
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


class PlanDefinitionActionOutput(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Output data definition.
    Defines the outputs of the action, if any.
    """

    resource_type = Field("PlanDefinitionActionOutput", const=True)

    relatedData: fhirtypes.String = Field(
        None,
        alias="relatedData",
        title="What data is provided",
        description=(
            "Points to an existing input or output element that is results as "
            "output from the action."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    relatedData__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_relatedData", title="Extension field for ``relatedData``."
    )

    requirement: fhirtypes.DataRequirementType = Field(
        None,
        alias="requirement",
        title="What data is provided",
        description="Defines the data that results as output from the action.",
        # if property is element of this resource.
        element_property=True,
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="User-visible title",
        description=(
            "A human-readable label for the data requirement used to label data "
            "flows in BPMN or similar diagrams. Also provides a human readable "
            "label when rendering the data requirement that conveys its purpose to "
            "human readers."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PlanDefinitionActionOutput`` according specification,
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


class PlanDefinitionActionParticipant(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who should participate in the action.
    Indicates who should participate in performing the action described.
    """

    resource_type = Field("PlanDefinitionActionParticipant", const=True)

    actorId: fhirtypes.String = Field(
        None,
        alias="actorId",
        title="What actor",
        description=(
            "A reference to the id element of the actor who will participate in "
            "this action."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    actorId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_actorId", title="Extension field for ``actorId``."
    )

    function: fhirtypes.CodeableConceptType = Field(
        None,
        alias="function",
        title="E.g. Author, Reviewer, Witness, etc",
        description=(
            "Indicates how the actor will be involved in the action - author, "
            "reviewer, witness, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="E.g. Nurse, Surgeon, Parent",
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
        title=(
            "careteam | device | group | healthcareservice | location | "
            "organization | patient | practitioner | practitionerrole | "
            "relatedperson"
        ),
        description="The type of participant in the action.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
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
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    typeCanonical: fhirtypes.Canonical = Field(
        None,
        alias="typeCanonical",
        title="Who or what can participate",
        description="The type of participant in the action.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["CapabilityStatement"],
    )
    typeCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_typeCanonical", title="Extension field for ``typeCanonical``."
    )

    typeReference: fhirtypes.ReferenceType = Field(
        None,
        alias="typeReference",
        title="Who or what can participate",
        description="The type of participant in the action.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
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
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PlanDefinitionActionParticipant`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "actorId",
            "type",
            "typeCanonical",
            "typeReference",
            "role",
            "function",
        ]


class PlanDefinitionActionRelatedAction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Relationship to another action.
    A relationship to another action such as "before" or "30-60 minutes after
    start of".
    """

    resource_type = Field("PlanDefinitionActionRelatedAction", const=True)

    endRelationship: fhirtypes.Code = Field(
        None,
        alias="endRelationship",
        title=(
            "before | before-start | before-end | concurrent | concurrent-with-"
            "start | concurrent-with-end | after | after-start | after-end"
        ),
        description="The relationship of the end of this action to the related action.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
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
    )
    endRelationship__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_endRelationship", title="Extension field for ``endRelationship``."
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
            "before | before-start | before-end | concurrent | concurrent-with-"
            "start | concurrent-with-end | after | after-start | after-end"
        ),
        description="The relationship of the start of this action to the related action.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
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
    )
    relationship__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_relationship", title="Extension field for ``relationship``."
    )

    targetId: fhirtypes.Id = Field(
        None,
        alias="targetId",
        title="What action is this related to",
        description="The element id of the target related action.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    targetId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_targetId", title="Extension field for ``targetId``."
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
            "targetId",
            "relationship",
            "endRelationship",
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
            ("relationship", "relationship__ext"),
            ("targetId", "targetId__ext"),
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


class PlanDefinitionActor(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Actors within the plan.
    Actors represent the individuals or groups involved in the execution of the
    defined set of activities.
    """

    resource_type = Field("PlanDefinitionActor", const=True)

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Describes the actor",
        description=(
            "A description of how the actor fits into the overall actions of the "
            "plan definition."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    option: typing.List[fhirtypes.PlanDefinitionActorOptionType] = Field(
        ...,
        alias="option",
        title="Who or what can be this actor",
        description="The characteristics of the candidates that could serve as the actor.",
        # if property is element of this resource.
        element_property=True,
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="User-visible title",
        description="A descriptive label for the actor.",
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PlanDefinitionActor`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "title",
            "description",
            "option",
        ]


class PlanDefinitionActorOption(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who or what can be this actor.
    The characteristics of the candidates that could serve as the actor.
    """

    resource_type = Field("PlanDefinitionActorOption", const=True)

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="E.g. Nurse, Surgeon, Parent",
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
        title=(
            "careteam | device | group | healthcareservice | location | "
            "organization | patient | practitioner | practitionerrole | "
            "relatedperson"
        ),
        description="The type of participant in the action.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
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
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    typeCanonical: fhirtypes.Canonical = Field(
        None,
        alias="typeCanonical",
        title="Who or what can participate",
        description="The type of participant in the action.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["CapabilityStatement"],
    )
    typeCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_typeCanonical", title="Extension field for ``typeCanonical``."
    )

    typeReference: fhirtypes.ReferenceType = Field(
        None,
        alias="typeReference",
        title="Who or what can participate",
        description="The type of participant in the action.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
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
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PlanDefinitionActorOption`` according specification,
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
        ]


class PlanDefinitionGoal(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What the plan is trying to accomplish.
    A goal describes an expected outcome that activities within the plan are
    intended to achieve. For example, weight loss, restoring an activity of
    daily living, obtaining herd immunity via immunization, meeting a process
    improvement objective, meeting the acceptance criteria for a test as
    specified by a quality specification, etc.
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
        title="E.g. Treatment, dietary, behavioral",
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

    detailBoolean: bool = Field(
        None,
        alias="detailBoolean",
        title="The target value to be achieved",
        description=(
            "The target value of the measure to be achieved to signify fulfillment "
            "of the goal, e.g. 150 pounds or 7.0%, or in the case of pharmaceutical"
            " quality - NMT 0.6%, Clear solution, etc. Either the high or low or "
            "both values of the range can be specified. When a low value is "
            "missing, it indicates that the goal is achieved at any value at or "
            "below the high value. Similarly, if the high value is missing, it "
            "indicates that the goal is achieved at any value at or above the low "
            "value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e detail[x]
        one_of_many="detail",
        one_of_many_required=False,
    )
    detailBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_detailBoolean", title="Extension field for ``detailBoolean``."
    )

    detailCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="detailCodeableConcept",
        title="The target value to be achieved",
        description=(
            "The target value of the measure to be achieved to signify fulfillment "
            "of the goal, e.g. 150 pounds or 7.0%, or in the case of pharmaceutical"
            " quality - NMT 0.6%, Clear solution, etc. Either the high or low or "
            "both values of the range can be specified. When a low value is "
            "missing, it indicates that the goal is achieved at any value at or "
            "below the high value. Similarly, if the high value is missing, it "
            "indicates that the goal is achieved at any value at or above the low "
            "value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e detail[x]
        one_of_many="detail",
        one_of_many_required=False,
    )

    detailInteger: fhirtypes.Integer = Field(
        None,
        alias="detailInteger",
        title="The target value to be achieved",
        description=(
            "The target value of the measure to be achieved to signify fulfillment "
            "of the goal, e.g. 150 pounds or 7.0%, or in the case of pharmaceutical"
            " quality - NMT 0.6%, Clear solution, etc. Either the high or low or "
            "both values of the range can be specified. When a low value is "
            "missing, it indicates that the goal is achieved at any value at or "
            "below the high value. Similarly, if the high value is missing, it "
            "indicates that the goal is achieved at any value at or above the low "
            "value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e detail[x]
        one_of_many="detail",
        one_of_many_required=False,
    )
    detailInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_detailInteger", title="Extension field for ``detailInteger``."
    )

    detailQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="detailQuantity",
        title="The target value to be achieved",
        description=(
            "The target value of the measure to be achieved to signify fulfillment "
            "of the goal, e.g. 150 pounds or 7.0%, or in the case of pharmaceutical"
            " quality - NMT 0.6%, Clear solution, etc. Either the high or low or "
            "both values of the range can be specified. When a low value is "
            "missing, it indicates that the goal is achieved at any value at or "
            "below the high value. Similarly, if the high value is missing, it "
            "indicates that the goal is achieved at any value at or above the low "
            "value."
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
            "of the goal, e.g. 150 pounds or 7.0%, or in the case of pharmaceutical"
            " quality - NMT 0.6%, Clear solution, etc. Either the high or low or "
            "both values of the range can be specified. When a low value is "
            "missing, it indicates that the goal is achieved at any value at or "
            "below the high value. Similarly, if the high value is missing, it "
            "indicates that the goal is achieved at any value at or above the low "
            "value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e detail[x]
        one_of_many="detail",
        one_of_many_required=False,
    )

    detailRatio: fhirtypes.RatioType = Field(
        None,
        alias="detailRatio",
        title="The target value to be achieved",
        description=(
            "The target value of the measure to be achieved to signify fulfillment "
            "of the goal, e.g. 150 pounds or 7.0%, or in the case of pharmaceutical"
            " quality - NMT 0.6%, Clear solution, etc. Either the high or low or "
            "both values of the range can be specified. When a low value is "
            "missing, it indicates that the goal is achieved at any value at or "
            "below the high value. Similarly, if the high value is missing, it "
            "indicates that the goal is achieved at any value at or above the low "
            "value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e detail[x]
        one_of_many="detail",
        one_of_many_required=False,
    )

    detailString: fhirtypes.String = Field(
        None,
        alias="detailString",
        title="The target value to be achieved",
        description=(
            "The target value of the measure to be achieved to signify fulfillment "
            "of the goal, e.g. 150 pounds or 7.0%, or in the case of pharmaceutical"
            " quality - NMT 0.6%, Clear solution, etc. Either the high or low or "
            "both values of the range can be specified. When a low value is "
            "missing, it indicates that the goal is achieved at any value at or "
            "below the high value. Similarly, if the high value is missing, it "
            "indicates that the goal is achieved at any value at or above the low "
            "value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e detail[x]
        one_of_many="detail",
        one_of_many_required=False,
    )
    detailString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_detailString", title="Extension field for ``detailString``."
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
            "The parameter whose value is to be tracked, e.g. body weight, blood "
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
            "detailString",
            "detailBoolean",
            "detailInteger",
            "detailRatio",
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
            "detail": [
                "detailBoolean",
                "detailCodeableConcept",
                "detailInteger",
                "detailQuantity",
                "detailRange",
                "detailRatio",
                "detailString",
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
