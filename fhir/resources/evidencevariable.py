# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EvidenceVariable
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
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

    approvalDate: fhirtypes.Date = Field(
        None,
        alias="approvalDate",
        title="When the resource was approved by publisher",
        description=(
            "The date on which the resource content was approved by the publisher. "
            "Approval happens once when the content is officially approved for "
            "usage.  See guidance around (not) making local changes to elements "
            "[here](canonicalresource.html#localization)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_approvalDate", title="Extension field for ``approvalDate``."
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
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    characteristic: typing.List[fhirtypes.EvidenceVariableCharacteristicType] = Field(
        None,
        alias="characteristic",
        title="A defining factor of the EvidenceVariable",
        description=(
            "A defining factor of the EvidenceVariable. Multiple characteristics "
            'are applied with "and" semantics.'
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
            "A copyright statement relating to the resource and/or its contents. "
            "Copyright statements are generally legal restrictions on the use and "
            "publishing of the resource."
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
            "The date  (and optionally time) when the evidence variable was last "
            "significantly changed. The date must change when the business version "
            "changes and it must change if the status code changes. In addition, it"
            " should change when the substantive content of the evidence variable "
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

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="When the resource is expected to be used",
        description=(
            "The period during which the resource content was or is planned to be "
            "in active use."
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
            "A Boolean value to indicate that this resource is authored for testing"
            " purposes (or education/evaluation/marketing) and is not intended to "
            "be used for genuine usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    handling: fhirtypes.Code = Field(
        None,
        alias="handling",
        title="continuous | dichotomous | ordinal | polychotomous",
        description="The method of handling in statistical analysis.",
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

    lastReviewDate: fhirtypes.Date = Field(
        None,
        alias="lastReviewDate",
        title="When the resource was last reviewed by the publisher",
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
        title="Name of the publisher/steward (organization or individual)",
        description=(
            "The name of the organization or individual responsible for the release"
            " and ongoing maintenance of the evidence variable."
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
        title="Why this EvidenceVariable is defined",
        description=(
            "Explanation of why this EvidenceVariable is needed and why it has been"
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
        title="Additional documentation, citations, etc",
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
            "and SHOULD be a literal address at which an authoritative instance of "
            "this evidence variable is (or will be) published. This URL can be the "
            "target of a canonical reference. It SHALL remain the same when the "
            "evidence variable is stored on different servers."
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
            "versionAlgorithmString",
            "versionAlgorithmCoding",
            "name",
            "title",
            "shortTitle",
            "status",
            "experimental",
            "date",
            "publisher",
            "contact",
            "description",
            "note",
            "useContext",
            "purpose",
            "copyright",
            "copyrightLabel",
            "approvalDate",
            "lastReviewDate",
            "effectivePeriod",
            "author",
            "editor",
            "reviewer",
            "endorser",
            "relatedArtifact",
            "actual",
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1779(
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
            "versionAlgorithm": ["versionAlgorithmCoding", "versionAlgorithmString"]
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


class EvidenceVariableCategory(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A grouping for ordinal or polychotomous variables.
    """

    resource_type = Field("EvidenceVariableCategory", const=True)

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Description of the grouping",
        description=None,
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
        description=None,
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
        description=None,
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
        description=None,
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

    A defining factor of the EvidenceVariable.
    A defining factor of the EvidenceVariable. Multiple characteristics are
    applied with "and" semantics.
    """

    resource_type = Field("EvidenceVariableCharacteristic", const=True)

    definitionByCombination: fhirtypes.EvidenceVariableCharacteristicDefinitionByCombinationType = Field(  # noqa: B950
        None,
        alias="definitionByCombination",
        title="Used to specify how two or more characteristics are combined",
        description=(
            "Defines the characteristic as a combination of two or more "
            "characteristics."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    definitionByTypeAndValue: fhirtypes.EvidenceVariableCharacteristicDefinitionByTypeAndValueType = Field(  # noqa: B950
        None,
        alias="definitionByTypeAndValue",
        title="Defines the characteristic using type and value",
        description="Defines the characteristic using both a type and value[x] elements.",
        # if property is element of this resource.
        element_property=True,
    )

    definitionCanonical: fhirtypes.Canonical = Field(
        None,
        alias="definitionCanonical",
        title=(
            "Defines the characteristic (without using type and value) by a "
            "Canonical"
        ),
        description="Defines the characteristic using Canonical.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["EvidenceVariable", "Evidence"],
    )
    definitionCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_definitionCanonical",
        title="Extension field for ``definitionCanonical``.",
    )

    definitionCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="definitionCodeableConcept",
        title=(
            "Defines the characteristic (without using type and value) by a "
            "CodeableConcept"
        ),
        description="Defines the characteristic using CodeableConcept.",
        # if property is element of this resource.
        element_property=True,
    )

    definitionExpression: fhirtypes.ExpressionType = Field(
        None,
        alias="definitionExpression",
        title=(
            "Defines the characteristic (without using type and value) by an "
            "expression"
        ),
        description="Defines the characteristic using Expression.",
        # if property is element of this resource.
        element_property=True,
    )

    definitionId: fhirtypes.Id = Field(
        None,
        alias="definitionId",
        title="Defines the characteristic (without using type and value) by an id",
        description="Defines the characteristic using id.",
        # if property is element of this resource.
        element_property=True,
    )
    definitionId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_definitionId", title="Extension field for ``definitionId``."
    )

    definitionReference: fhirtypes.ReferenceType = Field(
        None,
        alias="definitionReference",
        title=(
            "Defines the characteristic (without using type and value) by a "
            "Reference"
        ),
        description="Defines the characteristic using a Reference.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["EvidenceVariable", "Group", "Evidence"],
    )

    description: fhirtypes.Markdown = Field(
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

    durationQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="durationQuantity",
        title="Length of time in which the characteristic is met",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e duration[x]
        one_of_many="duration",
        one_of_many_required=False,
    )

    durationRange: fhirtypes.RangeType = Field(
        None,
        alias="durationRange",
        title="Length of time in which the characteristic is met",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e duration[x]
        one_of_many="duration",
        one_of_many_required=False,
    )

    exclude: bool = Field(
        None,
        alias="exclude",
        title=(
            "Whether the characteristic is an inclusion criterion or exclusion "
            "criterion"
        ),
        description=(
            "When true, this characteristic is an exclusion criterion. In other "
            "words, not matching this characteristic definition is equivalent to "
            "meeting this criterion."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    exclude__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_exclude", title="Extension field for ``exclude``."
    )

    instancesQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="instancesQuantity",
        title="Number of occurrences meeting the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e instances[x]
        one_of_many="instances",
        one_of_many_required=False,
    )

    instancesRange: fhirtypes.RangeType = Field(
        None,
        alias="instancesRange",
        title="Number of occurrences meeting the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e instances[x]
        one_of_many="instances",
        one_of_many_required=False,
    )

    linkId: fhirtypes.Id = Field(
        None,
        alias="linkId",
        title="Label for internal linking",
        description="Label used for when a characteristic refers to another characteristic.",
        # if property is element of this resource.
        element_property=True,
    )
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_linkId", title="Extension field for ``linkId``."
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Used for footnotes or explanatory notes",
        description=(
            "A human-readable string to clarify or explain concepts about the "
            "characteristic."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    timeFromEvent: typing.List[
        fhirtypes.EvidenceVariableCharacteristicTimeFromEventType
    ] = Field(
        None,
        alias="timeFromEvent",
        title="Timing in which the characteristic is determined",
        description=None,
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
            "linkId",
            "description",
            "note",
            "exclude",
            "definitionReference",
            "definitionCanonical",
            "definitionCodeableConcept",
            "definitionExpression",
            "definitionId",
            "definitionByTypeAndValue",
            "definitionByCombination",
            "instancesQuantity",
            "instancesRange",
            "durationQuantity",
            "durationRange",
            "timeFromEvent",
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
            "duration": ["durationQuantity", "durationRange"],
            "instances": ["instancesQuantity", "instancesRange"],
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


class EvidenceVariableCharacteristicDefinitionByCombination(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Used to specify how two or more characteristics are combined.
    Defines the characteristic as a combination of two or more characteristics.
    """

    resource_type = Field(
        "EvidenceVariableCharacteristicDefinitionByCombination", const=True
    )

    characteristic: typing.List[fhirtypes.EvidenceVariableCharacteristicType] = Field(
        ...,
        alias="characteristic",
        title="A defining factor of the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title=(
            "all-of | any-of | at-least | at-most | statistical | net-effect | "
            "dataset"
        ),
        description=(
            "Used to specify if two or more characteristics are combined with OR or"
            " AND."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "all-of",
            "any-of",
            "at-least",
            "at-most",
            "statistical",
            "net-effect",
            "dataset",
        ],
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    threshold: fhirtypes.PositiveInt = Field(
        None,
        alias="threshold",
        title='Provides the value of "n" when "at-least" or "at-most" codes are used',
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    threshold__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_threshold", title="Extension field for ``threshold``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EvidenceVariableCharacteristicDefinitionByCombination`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "threshold",
            "characteristic",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_5596(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("code", "code__ext")]
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


class EvidenceVariableCharacteristicDefinitionByTypeAndValue(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Defines the characteristic using type and value.
    Defines the characteristic using both a type and value[x] elements.
    """

    resource_type = Field(
        "EvidenceVariableCharacteristicDefinitionByTypeAndValue", const=True
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

    method: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="method",
        title="Method for how the characteristic value was determined",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    offset: fhirtypes.CodeableConceptType = Field(
        None,
        alias="offset",
        title="Reference point for valueQuantity or valueRange",
        description=(
            "Defines the reference point for comparison when valueQuantity or "
            "valueRange is not compared to zero."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Expresses the type of characteristic",
        description="Used to express the type of characteristic.",
        # if property is element of this resource.
        element_property=True,
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="Defines the characteristic when coupled with characteristic.type",
        description="Defines the characteristic when paired with characteristic.type.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="valueCodeableConcept",
        title="Defines the characteristic when coupled with characteristic.type",
        description="Defines the characteristic when paired with characteristic.type.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueId: fhirtypes.Id = Field(
        None,
        alias="valueId",
        title="Defines the characteristic when coupled with characteristic.type",
        description="Defines the characteristic when paired with characteristic.type.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueId", title="Extension field for ``valueId``."
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="Defines the characteristic when coupled with characteristic.type",
        description="Defines the characteristic when paired with characteristic.type.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueRange: fhirtypes.RangeType = Field(
        None,
        alias="valueRange",
        title="Defines the characteristic when coupled with characteristic.type",
        description="Defines the characteristic when paired with characteristic.type.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueReference",
        title="Defines the characteristic when coupled with characteristic.type",
        description="Defines the characteristic when paired with characteristic.type.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EvidenceVariableCharacteristicDefinitionByTypeAndValue`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "method",
            "device",
            "valueCodeableConcept",
            "valueBoolean",
            "valueQuantity",
            "valueRange",
            "valueReference",
            "valueId",
            "offset",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_5650(
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
            "value": [
                "valueBoolean",
                "valueCodeableConcept",
                "valueId",
                "valueQuantity",
                "valueRange",
                "valueReference",
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


class EvidenceVariableCharacteristicTimeFromEvent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Timing in which the characteristic is determined.
    """

    resource_type = Field("EvidenceVariableCharacteristicTimeFromEvent", const=True)

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Human readable description",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    eventCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="eventCodeableConcept",
        title="The event used as a base point (reference point) in time",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e event[x]
        one_of_many="event",
        one_of_many_required=False,
    )

    eventDateTime: fhirtypes.DateTime = Field(
        None,
        alias="eventDateTime",
        title="The event used as a base point (reference point) in time",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e event[x]
        one_of_many="event",
        one_of_many_required=False,
    )
    eventDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_eventDateTime", title="Extension field for ``eventDateTime``."
    )

    eventId: fhirtypes.Id = Field(
        None,
        alias="eventId",
        title="The event used as a base point (reference point) in time",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e event[x]
        one_of_many="event",
        one_of_many_required=False,
    )
    eventId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_eventId", title="Extension field for ``eventId``."
    )

    eventReference: fhirtypes.ReferenceType = Field(
        None,
        alias="eventReference",
        title="The event used as a base point (reference point) in time",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e event[x]
        one_of_many="event",
        one_of_many_required=False,
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Used for footnotes or explanatory notes",
        description=(
            "A human-readable string to clarify or explain concepts about the "
            "timeFromEvent."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title=(
            "Used to express the observation at a defined amount of time before or "
            "after the event"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    range: fhirtypes.RangeType = Field(
        None,
        alias="range",
        title=(
            "Used to express the observation within a period before and/or after "
            "the event"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EvidenceVariableCharacteristicTimeFromEvent`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "description",
            "note",
            "eventCodeableConcept",
            "eventReference",
            "eventDateTime",
            "eventId",
            "quantity",
            "range",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_4560(
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
            "event": [
                "eventCodeableConcept",
                "eventDateTime",
                "eventId",
                "eventReference",
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
