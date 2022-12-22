# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EvidenceVariable
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class EvidenceVariable(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A definition of an exposure, outcome, or other variable.
    The EvidenceVariable resource describes an element that knowledge
    (Evidence) is about.
    """

    resource_type = Field("EvidenceVariable", const=True)

    actual: bool = Field(
        None,
        alias="actual",
        title="Actual or conceptual",
        description=(
            "True if the actual variable measured, false if a conceptual "
            "representation of the intended variable."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    actual__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_actual", title="Extension field for ``actual``."
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

    category: typing.List[fhirtypes.EvidenceVariableCategoryType] = Field(
        None,
        alias="category",
        title="A grouping for ordinal or polychotomous variables",
        description=(
            "A grouping (or set of values) described along with other groupings to "
            "specify the set of groupings allowed for the variable."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    characteristic: typing.List[fhirtypes.EvidenceVariableCharacteristicType] = Field(
        None,
        alias="characteristic",
        title="What defines the members of the evidence element",
        description=(
            "A characteristic that defines the members of the evidence element. "
            'Multiple characteristics are applied with "and" semantics.'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    characteristicCombination: fhirtypes.Code = Field(
        None,
        alias="characteristicCombination",
        title="intersection | union",
        description=(
            "Used to specify if two or more characteristics are combined with OR or"
            " AND."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["intersection", "union"],
    )
    characteristicCombination__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_characteristicCombination",
        title="Extension field for ``characteristicCombination``.",
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

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the evidence variable was "
            "published. The date must change when the business version changes and "
            "it must change if the status code changes. In addition, it should "
            "change when the substantive content of the evidence variable changes."
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
        title="Natural language description of the evidence variable",
        description=(
            "A free text natural language description of the evidence variable from"
            " a consumer's perspective."
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

    endorser: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="endorser",
        title="Who endorsed the content",
        description=(
            "An individual or organization responsible for officially endorsing the"
            " content for use in some setting."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    handling: fhirtypes.Code = Field(
        None,
        alias="handling",
        title="continuous | dichotomous | ordinal | polychotomous",
        description="Used for an outcome to classify.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["continuous", "dichotomous", "ordinal", "polychotomous"],
    )
    handling__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_handling", title="Extension field for ``handling``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Additional identifier for the evidence variable",
        description=(
            "A formal identifier that is used to identify this evidence variable "
            "when it is represented in other formats, or referenced in a "
            "specification, model, design or an instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name for this evidence variable (computer friendly)",
        description=(
            "A natural language name identifying the evidence variable. This name "
            "should be usable as an identifier for the module by machine processing"
            " applications such as code generation."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Used for footnotes or explanatory notes",
        description=(
            "A human-readable string to clarify or explain concepts about the "
            "resource."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the organization or individual that published the evidence"
            " variable."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    relatedArtifact: typing.List[fhirtypes.RelatedArtifactType] = Field(
        None,
        alias="relatedArtifact",
        title="Additional documentation, citations, etc.",
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
            "An individual or organization primarily responsible for review of some"
            " aspect of the content."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    shortTitle: fhirtypes.String = Field(
        None,
        alias="shortTitle",
        title="Title for use in informal contexts",
        description=(
            "The short title provides an alternate title for use in informal "
            "descriptive contexts where the full, formal title is not necessary."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    shortTitle__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_shortTitle", title="Extension field for ``shortTitle``."
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this evidence variable. Enables tracking the life-cycle "
            "of the content."
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

    subtitle: fhirtypes.String = Field(
        None,
        alias="subtitle",
        title="Subordinate title of the EvidenceVariable",
        description=(
            "An explanatory or alternate title for the EvidenceVariable giving "
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
        title="Name for this evidence variable (human friendly)",
        description="A short, descriptive, user-friendly title for the evidence variable.",
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title=(
            "Canonical identifier for this evidence variable, represented as a URI "
            "(globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this evidence variable when "
            "it is referenced in a specification, model, design or an instance; "
            "also called its canonical identifier. This SHOULD be globally unique "
            "and SHOULD be a literal address at which at which an authoritative "
            "instance of this evidence variable is (or will be) published. This URL"
            " can be the target of a canonical reference. It SHALL remain the same "
            "when the evidence variable is stored on different servers."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
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
            "indexing and searching for appropriate evidence variable instances."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the evidence variable",
        description=(
            "The identifier that is used to identify this version of the evidence "
            "variable when it is referenced in a specification, model, design or "
            "instance. This is an arbitrary value managed by the evidence variable "
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
        ``EvidenceVariable`` according specification,
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
            "shortTitle",
            "subtitle",
            "status",
            "date",
            "description",
            "note",
            "useContext",
            "publisher",
            "contact",
            "author",
            "editor",
            "reviewer",
            "endorser",
            "relatedArtifact",
            "actual",
            "characteristicCombination",
            "characteristic",
            "handling",
            "category",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1779(
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


class EvidenceVariableCategory(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A grouping for ordinal or polychotomous variables.
    A grouping (or set of values) described along with other groupings to
    specify the set of groupings allowed for the variable.
    """

    resource_type = Field("EvidenceVariableCategory", const=True)

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Description of the grouping",
        description="A human-readable title or representation of the grouping.",
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="valueCodeableConcept",
        title="Definition of the grouping",
        description="Value or set of values that define the grouping.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="Definition of the grouping",
        description="Value or set of values that define the grouping.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueRange: fhirtypes.RangeType = Field(
        None,
        alias="valueRange",
        title="Definition of the grouping",
        description="Value or set of values that define the grouping.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EvidenceVariableCategory`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "name",
            "valueCodeableConcept",
            "valueQuantity",
            "valueRange",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2629(
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
            "value": ["valueCodeableConcept", "valueQuantity", "valueRange"]
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


class EvidenceVariableCharacteristic(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
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
        title="What code or expression defines members?",
        description=(
            "Define members of the evidence element using Codes (such as condition,"
            " medication, or observation), Expressions ( using an expression "
            "language such as FHIRPath or CQL) or DataRequirements (such as "
            "Diabetes diagnosis onset in the last year)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e definition[x]
        one_of_many="definition",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )
    definitionCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_definitionCanonical",
        title="Extension field for ``definitionCanonical``.",
    )

    definitionCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="definitionCodeableConcept",
        title="What code or expression defines members?",
        description=(
            "Define members of the evidence element using Codes (such as condition,"
            " medication, or observation), Expressions ( using an expression "
            "language such as FHIRPath or CQL) or DataRequirements (such as "
            "Diabetes diagnosis onset in the last year)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e definition[x]
        one_of_many="definition",
        one_of_many_required=True,
    )

    definitionExpression: fhirtypes.ExpressionType = Field(
        None,
        alias="definitionExpression",
        title="What code or expression defines members?",
        description=(
            "Define members of the evidence element using Codes (such as condition,"
            " medication, or observation), Expressions ( using an expression "
            "language such as FHIRPath or CQL) or DataRequirements (such as "
            "Diabetes diagnosis onset in the last year)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e definition[x]
        one_of_many="definition",
        one_of_many_required=True,
    )

    definitionReference: fhirtypes.ReferenceType = Field(
        None,
        alias="definitionReference",
        title="What code or expression defines members?",
        description=(
            "Define members of the evidence element using Codes (such as condition,"
            " medication, or observation), Expressions ( using an expression "
            "language such as FHIRPath or CQL) or DataRequirements (such as "
            "Diabetes diagnosis onset in the last year)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e definition[x]
        one_of_many="definition",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Group", "EvidenceVariable"],
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Natural language description of the characteristic",
        description=(
            "A short, natural language description of the characteristic that could"
            " be used to communicate the criteria to an end-user."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    device: fhirtypes.ReferenceType = Field(
        None,
        alias="device",
        title="Device used for determining characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device", "DeviceMetric"],
    )

    exclude: bool = Field(
        None,
        alias="exclude",
        title="Whether the characteristic includes or excludes members",
        description=(
            "When true, members with this characteristic are excluded from the "
            "element."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    exclude__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_exclude", title="Extension field for ``exclude``."
    )

    groupMeasure: fhirtypes.Code = Field(
        None,
        alias="groupMeasure",
        title=(
            "mean | median | mean-of-mean | mean-of-median | median-of-mean | "
            "median-of-median"
        ),
        description=(
            "Indicates how elements are aggregated within the study effective "
            "period."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "mean",
            "median",
            "mean-of-mean",
            "mean-of-median",
            "median-of-mean",
            "median-of-median",
        ],
    )
    groupMeasure__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_groupMeasure", title="Extension field for ``groupMeasure``."
    )

    method: fhirtypes.CodeableConceptType = Field(
        None,
        alias="method",
        title="Method used for describing characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    timeFromStart: fhirtypes.EvidenceVariableCharacteristicTimeFromStartType = Field(
        None,
        alias="timeFromStart",
        title="Observation time from study start",
        description=(
            "Indicates duration, period, or point of observation from the "
            "participant's study entry."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EvidenceVariableCharacteristic`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "description",
            "definitionReference",
            "definitionCanonical",
            "definitionCodeableConcept",
            "definitionExpression",
            "method",
            "device",
            "exclude",
            "timeFromStart",
            "groupMeasure",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3226(
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
            "definition": [
                "definitionCanonical",
                "definitionCodeableConcept",
                "definitionExpression",
                "definitionReference",
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


class EvidenceVariableCharacteristicTimeFromStart(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Observation time from study start.
    Indicates duration, period, or point of observation from the participant's
    study entry.
    """

    resource_type = Field("EvidenceVariableCharacteristicTimeFromStart", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Human readable description",
        description="A short, natural language description.",
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Used for footnotes or explanatory notes",
        description=(
            "A human-readable string to clarify or explain concepts about the "
            "resource."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title=(
            "Used to express the observation at a defined amount of time after the "
            "study start"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    range: fhirtypes.RangeType = Field(
        None,
        alias="range",
        title="Used to express the observation within a period after the study start",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EvidenceVariableCharacteristicTimeFromStart`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "description",
            "quantity",
            "range",
            "note",
        ]
