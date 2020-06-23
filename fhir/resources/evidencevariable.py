# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EvidenceVariable
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class EvidenceVariable(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A population, intervention, or exposure definition.
    The EvidenceVariable resource describes a "PICO" element that knowledge
    (evidence, assertion, recommendation) is about.
    """

    resource_type = Field("EvidenceVariable", const=True)

    approvalDate: fhirtypes.Date = Field(
        None,
        alias="approvalDate",
        title="Type `Date`",
        description="When the evidence variable was approved by publisher",
    )
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_approvalDate", title="Extension field for ``approvalDate``."
    )

    author: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="author",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Who authored the content",
    )

    characteristic: ListType[fhirtypes.EvidenceVariableCharacteristicType] = Field(
        ...,
        alias="characteristic",
        title=(
            "List of `EvidenceVariableCharacteristic` items (represented as `dict` "
            "in JSON)"
        ),
        description="What defines the members of the evidence element",
    )

    contact: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Contact details for the publisher",
    )

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Type `Markdown`",
        description="Use and/or publishing restrictions",
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    date: fhirtypes.DateTime = Field(
        None, alias="date", title="Type `DateTime`", description="Date last changed"
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown`",
        description="Natural language description of the evidence variable",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    editor: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="editor",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Who edited the content",
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When the evidence variable is expected to be used",
    )

    endorser: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="endorser",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Who endorsed the content",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Additional identifier for the evidence variable",
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Intended jurisdiction for evidence variable (if applicable)",
    )

    lastReviewDate: fhirtypes.Date = Field(
        None,
        alias="lastReviewDate",
        title="Type `Date`",
        description="When the evidence variable was last reviewed",
    )
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastReviewDate", title="Extension field for ``lastReviewDate``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`",
        description="Name for this evidence variable (computer friendly)",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Used for footnotes or explanatory notes",
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Type `String`",
        description="Name of the publisher (organization or individual)",
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    relatedArtifact: ListType[fhirtypes.RelatedArtifactType] = Field(
        None,
        alias="relatedArtifact",
        title="List of `RelatedArtifact` items (represented as `dict` in JSON)",
        description="Additional documentation, citations, etc.",
    )

    reviewer: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="reviewer",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Who reviewed the content",
    )

    shortTitle: fhirtypes.String = Field(
        None,
        alias="shortTitle",
        title="Type `String`",
        description="Title for use in informal contexts",
    )
    shortTitle__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_shortTitle", title="Extension field for ``shortTitle``."
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`",
        description="draft | active | retired | unknown",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subtitle: fhirtypes.String = Field(
        None,
        alias="subtitle",
        title="Type `String`",
        description="Subordinate title of the EvidenceVariable",
    )
    subtitle__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_subtitle", title="Extension field for ``subtitle``."
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String`",
        description="Name for this evidence variable (human friendly)",
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    topic: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="topic",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description=(
            "The category of the EvidenceVariable, such as Education, Treatment, "
            "Assessment, etc."
        ),
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="Type `Code`",
        description="dichotomous | continuous | descriptive",
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri`",
        description=(
            "Canonical identifier for this evidence variable, represented as a URI "
            "(globally unique)"
        ),
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    useContext: ListType[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="List of `UsageContext` items (represented as `dict` in JSON)",
        description="The context that the content is intended to support",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String`",
        description="Business version of the evidence variable",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class EvidenceVariableCharacteristic(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What defines the members of the evidence element.
    A characteristic that defines the members of the evidence element. Multiple
    characteristics are applied with "and" semantics.
    """

    resource_type = Field("EvidenceVariableCharacteristic", const=True)

    definitionCanonical: fhirtypes.Canonical = Field(
        None,
        alias="definitionCanonical",
        title="Type `Canonical` referencing `ActivityDefinition`",
        description="What code or expression defines members?",
        one_of_many="definition",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    definitionCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_definitionCanonical",
        title="Extension field for ``definitionCanonical``.",
    )

    definitionCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="definitionCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="What code or expression defines members?",
        one_of_many="definition",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    definitionDataRequirement: fhirtypes.DataRequirementType = Field(
        None,
        alias="definitionDataRequirement",
        title="Type `DataRequirement` (represented as `dict` in JSON)",
        description="What code or expression defines members?",
        one_of_many="definition",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    definitionExpression: fhirtypes.ExpressionType = Field(
        None,
        alias="definitionExpression",
        title="Type `Expression` (represented as `dict` in JSON)",
        description="What code or expression defines members?",
        one_of_many="definition",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    definitionReference: fhirtypes.ReferenceType = Field(
        None,
        alias="definitionReference",
        title="Type `Reference` referencing `Group` (represented as `dict` in JSON)",
        description="What code or expression defines members?",
        one_of_many="definition",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    definitionTriggerDefinition: fhirtypes.TriggerDefinitionType = Field(
        None,
        alias="definitionTriggerDefinition",
        title="Type `TriggerDefinition` (represented as `dict` in JSON)",
        description="What code or expression defines members?",
        one_of_many="definition",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Natural language description of the characteristic",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    exclude: bool = Field(
        None,
        alias="exclude",
        title="Type `bool`",
        description="Whether the characteristic includes or excludes members",
    )
    exclude__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_exclude", title="Extension field for ``exclude``."
    )

    groupMeasure: fhirtypes.Code = Field(
        None,
        alias="groupMeasure",
        title="Type `Code`",
        description=(
            "mean | median | mean-of-mean | mean-of-median | median-of-mean | "
            "median-of-median"
        ),
    )
    groupMeasure__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_groupMeasure", title="Extension field for ``groupMeasure``."
    )

    participantEffectiveDateTime: fhirtypes.DateTime = Field(
        None,
        alias="participantEffectiveDateTime",
        title="Type `DateTime`",
        description="What time period do participants cover",
        one_of_many="participantEffective",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    participantEffectiveDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_participantEffectiveDateTime",
        title="Extension field for ``participantEffectiveDateTime``.",
    )

    participantEffectiveDuration: fhirtypes.DurationType = Field(
        None,
        alias="participantEffectiveDuration",
        title="Type `Duration` (represented as `dict` in JSON)",
        description="What time period do participants cover",
        one_of_many="participantEffective",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    participantEffectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="participantEffectivePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="What time period do participants cover",
        one_of_many="participantEffective",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    participantEffectiveTiming: fhirtypes.TimingType = Field(
        None,
        alias="participantEffectiveTiming",
        title="Type `Timing` (represented as `dict` in JSON)",
        description="What time period do participants cover",
        one_of_many="participantEffective",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    timeFromStart: fhirtypes.DurationType = Field(
        None,
        alias="timeFromStart",
        title="Type `Duration` (represented as `dict` in JSON)",
        description="Observation time from study start",
    )

    usageContext: ListType[fhirtypes.UsageContextType] = Field(
        None,
        alias="usageContext",
        title="List of `UsageContext` items (represented as `dict` in JSON)",
        description="What code/value pairs define members?",
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
            "definition": [
                "definitionCanonical",
                "definitionCodeableConcept",
                "definitionDataRequirement",
                "definitionExpression",
                "definitionReference",
                "definitionTriggerDefinition",
            ],
            "participantEffective": [
                "participantEffectiveDateTime",
                "participantEffectiveDuration",
                "participantEffectivePeriod",
                "participantEffectiveTiming",
            ],
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
