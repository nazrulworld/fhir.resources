from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ExampleScenario
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ExampleScenario(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Example of workflow instance.
    """

    __resource_type__ = "ExampleScenario"

    actor: typing.List[fhirtypes.ExampleScenarioActorType] | None = Field(  # type: ignore
        None,
        alias="actor",
        title="Individual involved in exchange",
        description=(
            "A system or person who shares or receives an instance within the "
            "scenario."
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
            "A copyright statement relating to the example scenario and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the example scenario."
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
            "The date  (and optionally time) when the example scenario was last "
            "significantly changed. The date must change when the business version "
            "changes and it must change if the status code changes. In addition, it"
            " should change when the substantive content of the example scenario "
            "changes. (e.g. the 'content logical definition')."
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
        title="Natural language description of the ExampleScenario",
        description=(
            "A free text natural language description of the ExampleScenario from a"
            " consumer's perspective."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    experimental: bool | None = Field(  # type: ignore
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this example scenario is authored for"
            " testing purposes (or education/evaluation/marketing) and is not "
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
        title="Additional identifier for the example scenario",
        description=(
            "A formal identifier that is used to identify this example scenario "
            "when it is represented in other formats, or referenced in a "
            "specification, model, design or an instance."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    instance: typing.List[fhirtypes.ExampleScenarioInstanceType] | None = Field(  # type: ignore
        None,
        alias="instance",
        title="Data used in the scenario",
        description="A single data collection that is shared as part of the scenario.",
        json_schema_extra={
            "element_property": True,
        },
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for example scenario (if applicable)",
        description=(
            "A legal or geographic region in which the example scenario is intended"
            " to be used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="To be removed?",
        description="Temporarily retained for tooling purposes.",
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    process: typing.List[fhirtypes.ExampleScenarioProcessType] | None = Field(  # type: ignore
        None,
        alias="process",
        title="Major process within scenario",
        description=(
            "A group of operations that represents a significant step within a "
            "scenario."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    publisher: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="publisher",
        title="Name of the publisher/steward (organization or individual)",
        description=(
            "The name of the organization or individual responsible for the release"
            " and ongoing maintenance of the example scenario."
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
        title="The purpose of the example, e.g. to illustrate a scenario",
        description=(
            "What the example scenario resource is created for. This should not be "
            "used to show the business purpose of the scenario itself, but the "
            "purpose of documenting a scenario."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this example scenario. Enables tracking the life-cycle "
            "of the content."
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

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Name for this example scenario (human friendly)",
        description="A short, descriptive, user-friendly title for the ExampleScenario.",
        json_schema_extra={
            "element_property": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="url",
        title=(
            "Canonical identifier for this example scenario, represented as a URI "
            "(globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this example scenario when it"
            " is referenced in a specification, model, design or an instance; also "
            "called its canonical identifier. This SHOULD be globally unique and "
            "SHOULD be a literal address at which an authoritative instance of this"
            " example scenario is (or will be) published. This URL can be the "
            "target of a canonical reference. It SHALL remain the same when the "
            "example scenario is stored on different servers."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_url", title="Extension field for ``url``."
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
            "indexing and searching for appropriate example scenario instances."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="Business version of the example scenario",
        description=(
            "The identifier that is used to identify this version of the example "
            "scenario when it is referenced in a specification, model, design or "
            "instance. This is an arbitrary value managed by the example scenario "
            "author and is not expected to be globally unique. For example, it "
            "might be a timestamp (e.g. yyyymmdd) if a managed version is not "
            "available. There is also no expectation that versions can be placed in"
            " a lexicographical sequence."
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
        ``ExampleScenario`` according specification,
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
            "status",
            "experimental",
            "date",
            "publisher",
            "contact",
            "description",
            "useContext",
            "jurisdiction",
            "purpose",
            "copyright",
            "copyrightLabel",
            "actor",
            "instance",
            "process",
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
            "versionAlgorithm": ["versionAlgorithmCoding", "versionAlgorithmString"]
        }
        return one_of_many_fields


class ExampleScenarioActor(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Individual involved in exchange.
    A system or person who shares or receives an instance within the scenario.
    """

    __resource_type__ = "ExampleScenarioActor"

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Details about actor",
        description="An explanation of who/what the actor is and its role in the scenario.",
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    key: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="key",
        title="ID or acronym of the actor",
        description=(
            "A unique string within the scenario that is used to reference the "
            "actor."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    key__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_key", title="Extension field for ``key``."
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Label for actor when rendering",
        description=(
            "The human-readable name for the actor used when rendering the " "scenario."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="person | system",
        description="The category of actor - person or system.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["person", "system"],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExampleScenarioActor`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "key",
            "type",
            "title",
            "description",
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
            ("key", "key__ext"),
            ("title", "title__ext"),
            ("type", "type__ext"),
        ]
        return required_fields


class ExampleScenarioInstance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Data used in the scenario.
    A single data collection that is shared as part of the scenario.
    """

    __resource_type__ = "ExampleScenarioInstance"

    containedInstance: typing.List[fhirtypes.ExampleScenarioInstanceContainedInstanceType] | None = Field(  # type: ignore
        None,
        alias="containedInstance",
        title="Resources contained in the instance",
        description=(
            "References to other instances that can be found within this instance "
            "(e.g. the observations contained in a bundle)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    content: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="content",
        title="Example instance data",
        description=(
            "Points to an instance (typically an example) that shows the data that "
            "would corespond to this instance."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Human-friendly description of the instance",
        description="An explanation of what the instance contains and what it's for.",
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    key: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="key",
        title="ID or acronym of the instance",
        description=(
            "A unique string within the scenario that is used to reference the "
            "instance."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    key__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_key", title="Extension field for ``key``."
    )

    structureProfileCanonical: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="structureProfileCanonical",
        title="Rules instance adheres to",
        description=(
            "Refers to a profile, template or other ruleset the instance adheres " "to."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e structureProfile[x]
            "one_of_many": "structureProfile",
            "one_of_many_required": False,
        },
    )
    structureProfileCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_structureProfileCanonical",
        title="Extension field for ``structureProfileCanonical``.",
    )

    structureProfileUri: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="structureProfileUri",
        title="Rules instance adheres to",
        description=(
            "Refers to a profile, template or other ruleset the instance adheres " "to."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e structureProfile[x]
            "one_of_many": "structureProfile",
            "one_of_many_required": False,
        },
    )
    structureProfileUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_structureProfileUri",
        title="Extension field for ``structureProfileUri``.",
    )

    structureType: fhirtypes.CodingType = Field(  # type: ignore
        ...,
        alias="structureType",
        title="Data structure for example",
        description=(
            "A code indicating the kind of data structure (FHIR resource or some "
            "other standard) this is an instance of."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    structureVersion: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="structureVersion",
        title="E.g. 4.0.1",
        description=(
            "Conveys the version of the data structure instantiated.  I.e. what "
            "release of FHIR, X12, OpenEHR, etc. is instance compliant with."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    structureVersion__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_structureVersion",
        title="Extension field for ``structureVersion``.",
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Label for instance",
        description=(
            "A short descriptive label the instance to be used in tables or "
            "diagrams."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    version: typing.List[fhirtypes.ExampleScenarioInstanceVersionType] | None = Field(  # type: ignore
        None,
        alias="version",
        title="Snapshot of instance that changes",
        description="Represents the instance as it was at a specific time-point.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExampleScenarioInstance`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "key",
            "structureType",
            "structureVersion",
            "structureProfileCanonical",
            "structureProfileUri",
            "title",
            "description",
            "content",
            "version",
            "containedInstance",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("key", "key__ext"), ("title", "title__ext")]
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
            "structureProfile": ["structureProfileCanonical", "structureProfileUri"]
        }
        return one_of_many_fields


class ExampleScenarioInstanceContainedInstance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Resources contained in the instance.
    References to other instances that can be found within this instance (e.g.
    the observations contained in a bundle).
    """

    __resource_type__ = "ExampleScenarioInstanceContainedInstance"

    instanceReference: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="instanceReference",
        title="Key of contained instance",
        description="A reference to the key of an instance found within this one.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    instanceReference__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_instanceReference",
        title="Extension field for ``instanceReference``.",
    )

    versionReference: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="versionReference",
        title="Key of contained instance version",
        description=(
            "A reference to the key of a specific version of an instance in this "
            "instance."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    versionReference__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_versionReference",
        title="Extension field for ``versionReference``.",
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExampleScenarioInstanceContainedInstance`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "instanceReference",
            "versionReference",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("instanceReference", "instanceReference__ext")]
        return required_fields


class ExampleScenarioInstanceVersion(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Snapshot of instance that changes.
    Represents the instance as it was at a specific time-point.
    """

    __resource_type__ = "ExampleScenarioInstanceVersion"

    content: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="content",
        title="Example instance version data",
        description=(
            "Points to an instance (typically an example) that shows the data that "
            "would flow at this point in the scenario."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Details about version",
        description=(
            "An explanation of what this specific version of the instance contains "
            "and represents."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    key: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="key",
        title="ID or acronym of the version",
        description=(
            "A unique string within the instance that is used to reference the "
            "version of the instance."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    key__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_key", title="Extension field for ``key``."
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Label for instance version",
        description=(
            "A short descriptive label the version to be used in tables or " "diagrams."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExampleScenarioInstanceVersion`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "key",
            "title",
            "description",
            "content",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("key", "key__ext"), ("title", "title__ext")]
        return required_fields


class ExampleScenarioProcess(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Major process within scenario.
    A group of operations that represents a significant step within a scenario.
    """

    __resource_type__ = "ExampleScenarioProcess"

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Human-friendly description of the process",
        description="An explanation of what the process represents and what it does.",
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    postConditions: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="postConditions",
        title="Status after successful completion",
        description=(
            "Description of the final state of the actors, environment and data "
            "after the process has been successfully completed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    postConditions__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_postConditions", title="Extension field for ``postConditions``."
    )

    preConditions: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="preConditions",
        title="Status before process starts",
        description=(
            "Description of the initial state of the actors, environment and data "
            "before the process starts."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    preConditions__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_preConditions", title="Extension field for ``preConditions``."
    )

    step: typing.List[fhirtypes.ExampleScenarioProcessStepType] | None = Field(  # type: ignore
        None,
        alias="step",
        title="Event within of the process",
        description="A significant action that occurs as part of the process.",
        json_schema_extra={
            "element_property": True,
        },
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Label for procss",
        description=(
            "A short descriptive label the process to be used in tables or " "diagrams."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExampleScenarioProcess`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "title",
            "description",
            "preConditions",
            "postConditions",
            "step",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("title", "title__ext")]
        return required_fields


class ExampleScenarioProcessStep(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Event within of the process.
    A significant action that occurs as part of the process.
    """

    __resource_type__ = "ExampleScenarioProcessStep"

    alternative: typing.List[fhirtypes.ExampleScenarioProcessStepAlternativeType] | None = Field(  # type: ignore
        None,
        alias="alternative",
        title="Alternate non-typical step action",
        description=(
            "Indicates an alternative step that can be taken instead of the sub-"
            "process, scenario or operation.  E.g. to represent non-happy-"
            "path/exceptional/atypical circumstances."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    number: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="number",
        title="Sequential number of the step",
        description="The sequential number of the step, e.g. 1.2.5.",
        json_schema_extra={
            "element_property": True,
        },
    )
    number__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_number", title="Extension field for ``number``."
    )

    operation: fhirtypes.ExampleScenarioProcessStepOperationType | None = Field(  # type: ignore
        None,
        alias="operation",
        title="Step is simple action",
        description="The step represents a single operation invoked on receiver by sender.",
        json_schema_extra={
            "element_property": True,
        },
    )

    pause: bool | None = Field(  # type: ignore
        None,
        alias="pause",
        title="Pause in the flow?",
        description=(
            "If true, indicates that, following this step, there is a pause in the "
            "flow and the subsequent step will occur at some later time (triggered "
            "by some event)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    pause__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_pause", title="Extension field for ``pause``."
    )

    process: fhirtypes.ExampleScenarioProcessType | None = Field(  # type: ignore
        None,
        alias="process",
        title="Step is nested process",
        description="Indicates that the step is a complex sub-process with its own steps.",
        json_schema_extra={
            "element_property": True,
        },
    )

    workflow: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="workflow",
        title="Step is nested workflow",
        description="Indicates that the step is defined by a seaparate scenario instance.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ExampleScenario"],
        },
    )
    workflow__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_workflow", title="Extension field for ``workflow``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExampleScenarioProcessStep`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "number",
            "process",
            "workflow",
            "operation",
            "alternative",
            "pause",
        ]


class ExampleScenarioProcessStepAlternative(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Alternate non-typical step action.
    Indicates an alternative step that can be taken instead of the sub-process,
    scenario or operation.  E.g. to represent non-happy-
    path/exceptional/atypical circumstances.
    """

    __resource_type__ = "ExampleScenarioProcessStepAlternative"

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Human-readable description of option",
        description=(
            "A human-readable description of the alternative explaining when the "
            "alternative should occur rather than the base step."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    step: typing.List[fhirtypes.ExampleScenarioProcessStepType] | None = Field(  # type: ignore
        None,
        alias="step",
        title="Alternative action(s)",
        description=(
            "Indicates the operation, sub-process or scenario that happens if the "
            "alternative option is selected."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Label for alternative",
        description=(
            "The label to display for the alternative that gives a sense of the "
            "circumstance in which the alternative should be invoked."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExampleScenarioProcessStepAlternative`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "title", "description", "step"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("title", "title__ext")]
        return required_fields


class ExampleScenarioProcessStepOperation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Step is simple action.
    The step represents a single operation invoked on receiver by sender.
    """

    __resource_type__ = "ExampleScenarioProcessStepOperation"

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Human-friendly description of the operation",
        description="An explanation of what the operation represents and what it does.",
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    initiator: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="initiator",
        title="Who starts the operation",
        description="The system that invokes the action/transmits the data.",
        json_schema_extra={
            "element_property": True,
        },
    )
    initiator__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_initiator", title="Extension field for ``initiator``."
    )

    initiatorActive: bool | None = Field(  # type: ignore
        None,
        alias="initiatorActive",
        title="Initiator stays active?",
        description="If false, the initiator is deactivated right after the operation.",
        json_schema_extra={
            "element_property": True,
        },
    )
    initiatorActive__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_initiatorActive", title="Extension field for ``initiatorActive``."
    )

    receiver: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="receiver",
        title="Who receives the operation",
        description="The system on which the action is invoked/receives the data.",
        json_schema_extra={
            "element_property": True,
        },
    )
    receiver__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_receiver", title="Extension field for ``receiver``."
    )

    receiverActive: bool | None = Field(  # type: ignore
        None,
        alias="receiverActive",
        title="Receiver stays active?",
        description="If false, the receiver is deactivated right after the operation.",
        json_schema_extra={
            "element_property": True,
        },
    )
    receiverActive__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_receiverActive", title="Extension field for ``receiverActive``."
    )

    request: fhirtypes.ExampleScenarioInstanceContainedInstanceType | None = Field(  # type: ignore
        None,
        alias="request",
        title="Instance transmitted on invocation",
        description=(
            "A reference to the instance that is transmitted from requester to "
            "receiver as part of the invocation of the operation."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    response: fhirtypes.ExampleScenarioInstanceContainedInstanceType | None = Field(  # type: ignore
        None,
        alias="response",
        title="Instance transmitted on invocation response",
        description=(
            "A reference to the instance that is transmitted from receiver to "
            "requester as part of the operation's synchronous response (if any)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Label for step",
        description="A short descriptive label the step to be used in tables or diagrams.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    type: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Kind of action",
        description="The standardized type of action (FHIR or otherwise).",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExampleScenarioProcessStepOperation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "title",
            "initiator",
            "receiver",
            "description",
            "initiatorActive",
            "receiverActive",
            "request",
            "response",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("title", "title__ext")]
        return required_fields
