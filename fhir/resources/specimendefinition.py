# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SpecimenDefinition
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


class SpecimenDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Kind of specimen.
    A kind of specimen with associated set of requirements.
    """

    resource_type = Field("SpecimenDefinition", const=True)

    approvalDate: fhirtypes.Date = Field(
        None,
        alias="approvalDate",
        title="When SpecimenDefinition was approved by publisher",
        description=(
            "The date on which the asset content was approved by the publisher. "
            "Approval happens once when the content is officially approved for "
            "usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_approvalDate", title="Extension field for ``approvalDate``."
    )

    collection: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="collection",
        title="Specimen collection procedure",
        description="The action to be performed for collecting the specimen.",
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
            "Copyright statement relating to the SpecimenDefinition and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the SpecimenDefinition."
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
        title="Date status first applied",
        description=(
            "For draft definitions, indicates the date of initial creation. For "
            "active definitions, represents the date of activation. For withdrawn "
            "definitions, indicates the date of withdrawal."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    derivedFromCanonical: typing.List[typing.Optional[fhirtypes.Canonical]] = Field(
        None,
        alias="derivedFromCanonical",
        title="Based on FHIR definition of another SpecimenDefinition",
        description=(
            "The canonical URL pointing to another FHIR-defined SpecimenDefinition "
            "that is adhered to in whole or in part by this definition."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SpecimenDefinition"],
    )
    derivedFromCanonical__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_derivedFromCanonical",
        title="Extension field for ``derivedFromCanonical``.",
    )

    derivedFromUri: typing.List[typing.Optional[fhirtypes.Uri]] = Field(
        None,
        alias="derivedFromUri",
        title="Based on external definition",
        description=(
            "The URL pointing to an externally-defined type of specimen, guideline "
            "or other definition that is adhered to in whole or in part by this "
            "definition."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    derivedFromUri__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_derivedFromUri", title="Extension field for ``derivedFromUri``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Natural language description of the SpecimenDefinition",
        description=(
            "A free text natural language description of the SpecimenDefinition "
            "from the consumer's perspective."
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
        title="The effective date range for the SpecimenDefinition",
        description=(
            "The period during which the SpecimenDefinition content was or is "
            "planned to be effective."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="If this SpecimenDefinition is not for real usage",
        description=(
            "A flag to indicate that this SpecimenDefinition is not authored for  "
            "genuine usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Business identifier",
        description="A business identifier assigned to this SpecimenDefinition.",
        # if property is element of this resource.
        element_property=True,
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for this SpecimenDefinition (if applicable)",
        description="A jurisdiction in which the SpecimenDefinition is intended to be used.",
        # if property is element of this resource.
        element_property=True,
    )

    lastReviewDate: fhirtypes.Date = Field(
        None,
        alias="lastReviewDate",
        title="The date on which the asset content was last reviewed by the publisher",
        description=(
            "The date on which the asset content was last reviewed. Review happens "
            "periodically after that, but doesn't change the original approval "
            "date."
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
        title="Name for this {{title}} (computer friendly)",
        description=(
            "A natural language name identifying the {{title}}. This name should be"
            " usable as an identifier for the module by machine processing "
            "applications such as code generation."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    patientPreparation: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="patientPreparation",
        title="Patient preparation for collection",
        description="Preparation of the patient for specimen collection.",
        # if property is element of this resource.
        element_property=True,
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title=(
            "The name of the individual or organization that published the "
            "SpecimenDefinition"
        ),
        description=(
            'Helps establish the "authority/credibility" of the SpecimenDefinition.'
            " May also allow for contact."
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
        title="Why this SpecimenDefinition is defined",
        description=(
            "Explains why this SpecimeDefinition is needed and why it has been "
            "designed as it has."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description="The current state of theSpecimenDefinition.",
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

    subjectCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="subjectCodeableConcept",
        title="Type of subject for specimen collection",
        description=(
            "A code or group definition that describes the intended subject  from "
            "which this kind of specimen is to be collected."
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
        title="Type of subject for specimen collection",
        description=(
            "A code or group definition that describes the intended subject  from "
            "which this kind of specimen is to be collected."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e subject[x]
        one_of_many="subject",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Group"],
    )

    timeAspect: fhirtypes.String = Field(
        None,
        alias="timeAspect",
        title="Time aspect for collection",
        description="Time aspect of specimen collection (duration or offset).",
        # if property is element of this resource.
        element_property=True,
    )
    timeAspect__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_timeAspect", title="Extension field for ``timeAspect``."
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Name for this SpecimenDefinition (Human friendly)",
        description="A short, descriptive, user-friendly title for the SpecimenDefinition.",
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    typeCollected: fhirtypes.CodeableConceptType = Field(
        None,
        alias="typeCollected",
        title="Kind of material to collect",
        description="The kind of material to be collected.",
        # if property is element of this resource.
        element_property=True,
    )

    typeTested: typing.List[fhirtypes.SpecimenDefinitionTypeTestedType] = Field(
        None,
        alias="typeTested",
        title="Specimen in container intended for testing by lab",
        description=(
            "Specimen conditioned in a container as expected by the testing "
            "laboratory."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title=(
            "Logical canonical URL to reference this SpecimenDefinition (globally "
            "unique)"
        ),
        description=(
            "An absolute URL that is used to identify this SpecimenDefinition when "
            "it is referenced in a specification, model, design or an instance. "
            "This SHALL be a URL, SHOULD be globally unique, and SHOULD be an "
            "address at which this SpecimenDefinition is (or will be) published. "
            "The URL SHOULD include the major version of the SpecimenDefinition. "
            "For more information see Technical and Business Versions."
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
        title="Content intends to support these contexts",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These terms may be used to assist with "
            "indexing and searching of specimen definitions."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the SpecimenDefinition",
        description=(
            "The identifier that is used to identify this version of the "
            "SpecimenDefinition when it is referenced in a specification, model, "
            "design or instance. This is an arbitrary value managed by the "
            "SpecimenDefinition author and is not expected to be globally unique."
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
        ``SpecimenDefinition`` according specification,
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
            "derivedFromCanonical",
            "derivedFromUri",
            "status",
            "experimental",
            "subjectCodeableConcept",
            "subjectReference",
            "date",
            "publisher",
            "contact",
            "description",
            "useContext",
            "jurisdiction",
            "purpose",
            "copyright",
            "copyrightLabel",
            "approvalDate",
            "lastReviewDate",
            "effectivePeriod",
            "typeCollected",
            "patientPreparation",
            "timeAspect",
            "collection",
            "typeTested",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2046(
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
    def validate_one_of_many_2046(
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
            "subject": ["subjectCodeableConcept", "subjectReference"],
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


class SpecimenDefinitionTypeTested(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Specimen in container intended for testing by lab.
    Specimen conditioned in a container as expected by the testing laboratory.
    """

    resource_type = Field("SpecimenDefinitionTypeTested", const=True)

    container: fhirtypes.SpecimenDefinitionTypeTestedContainerType = Field(
        None,
        alias="container",
        title="The specimen's container",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    handling: typing.List[fhirtypes.SpecimenDefinitionTypeTestedHandlingType] = Field(
        None,
        alias="handling",
        title="Specimen handling before testing",
        description=(
            "Set of instructions for preservation/transport of the specimen at a "
            "defined temperature interval, prior the testing process."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    isDerived: bool = Field(
        None,
        alias="isDerived",
        title="Primary or secondary specimen",
        description="Primary of secondary specimen.",
        # if property is element of this resource.
        element_property=True,
    )
    isDerived__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_isDerived", title="Extension field for ``isDerived``."
    )

    preference: fhirtypes.Code = Field(
        None,
        alias="preference",
        title="preferred | alternate",
        description="The preference for this type of conditioned specimen.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["preferred", "alternate"],
    )
    preference__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_preference", title="Extension field for ``preference``."
    )

    rejectionCriterion: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="rejectionCriterion",
        title="Criterion specified for specimen rejection",
        description=(
            "Criterion for rejection of the specimen in its container by the "
            "laboratory."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    requirement: fhirtypes.Markdown = Field(
        None,
        alias="requirement",
        title="Requirements for specimen delivery and special handling",
        description=(
            "Requirements for delivery and special handling of this kind of "
            "conditioned specimen."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    requirement__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_requirement", title="Extension field for ``requirement``."
    )

    retentionTime: fhirtypes.DurationType = Field(
        None,
        alias="retentionTime",
        title="The usual time for retaining this kind of specimen",
        description=(
            "The usual time that a specimen of this kind is retained after the "
            "ordered tests are completed, for the purpose of additional testing."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    singleUse: bool = Field(
        None,
        alias="singleUse",
        title="Specimen for single use only",
        description='Specimen can be used by only one test or panel if the value is "true".',
        # if property is element of this resource.
        element_property=True,
    )
    singleUse__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_singleUse", title="Extension field for ``singleUse``."
    )

    testingDestination: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="testingDestination",
        title="Where the specimen will be tested",
        description=(
            "Where the specimen will be tested: e.g., lab, sector, device or any "
            "combination of these."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type of intended specimen",
        description="The kind of specimen conditioned for testing expected by lab.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SpecimenDefinitionTypeTested`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "isDerived",
            "type",
            "preference",
            "container",
            "requirement",
            "retentionTime",
            "singleUse",
            "rejectionCriterion",
            "handling",
            "testingDestination",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3071(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("preference", "preference__ext")]
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


class SpecimenDefinitionTypeTestedContainer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The specimen's container.
    """

    resource_type = Field("SpecimenDefinitionTypeTestedContainer", const=True)

    additive: typing.List[
        fhirtypes.SpecimenDefinitionTypeTestedContainerAdditiveType
    ] = Field(
        None,
        alias="additive",
        title="Additive associated with container",
        description=(
            "Substance introduced in the kind of container to preserve, maintain or"
            " enhance the specimen. Examples: Formalin, Citrate, EDTA."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    cap: fhirtypes.CodeableConceptType = Field(
        None,
        alias="cap",
        title="Color of container cap",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    capacity: fhirtypes.QuantityType = Field(
        None,
        alias="capacity",
        title="The capacity of this kind of container",
        description="The capacity (volume or other measure) of this kind of container.",
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="The description of the kind of container",
        description="The textual description of the kind of container.",
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    material: fhirtypes.CodeableConceptType = Field(
        None,
        alias="material",
        title="The material type used for the container",
        description="The type of material of the container.",
        # if property is element of this resource.
        element_property=True,
    )

    minimumVolumeQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="minimumVolumeQuantity",
        title="Minimum volume",
        description="The minimum volume to be conditioned in the container.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e minimumVolume[x]
        one_of_many="minimumVolume",
        one_of_many_required=False,
    )

    minimumVolumeString: fhirtypes.String = Field(
        None,
        alias="minimumVolumeString",
        title="Minimum volume",
        description="The minimum volume to be conditioned in the container.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e minimumVolume[x]
        one_of_many="minimumVolume",
        one_of_many_required=False,
    )
    minimumVolumeString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_minimumVolumeString",
        title="Extension field for ``minimumVolumeString``.",
    )

    preparation: fhirtypes.Markdown = Field(
        None,
        alias="preparation",
        title="Special processing applied to the container for this specimen type",
        description=(
            "Special processing that should be applied to the container for this "
            "kind of specimen."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    preparation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_preparation", title="Extension field for ``preparation``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Kind of container associated with the kind of specimen",
        description="The type of container used to contain this kind of specimen.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SpecimenDefinitionTypeTestedContainer`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "material",
            "type",
            "cap",
            "description",
            "capacity",
            "minimumVolumeQuantity",
            "minimumVolumeString",
            "additive",
            "preparation",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_4016(
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
            "minimumVolume": ["minimumVolumeQuantity", "minimumVolumeString"]
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


class SpecimenDefinitionTypeTestedContainerAdditive(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additive associated with container.
    Substance introduced in the kind of container to preserve, maintain or
    enhance the specimen. Examples: Formalin, Citrate, EDTA.
    """

    resource_type = Field("SpecimenDefinitionTypeTestedContainerAdditive", const=True)

    additiveCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="additiveCodeableConcept",
        title="Additive associated with container",
        description=(
            "Substance introduced in the kind of container to preserve, maintain or"
            " enhance the specimen. Examples: Formalin, Citrate, EDTA."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e additive[x]
        one_of_many="additive",
        one_of_many_required=True,
    )

    additiveReference: fhirtypes.ReferenceType = Field(
        None,
        alias="additiveReference",
        title="Additive associated with container",
        description=(
            "Substance introduced in the kind of container to preserve, maintain or"
            " enhance the specimen. Examples: Formalin, Citrate, EDTA."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e additive[x]
        one_of_many="additive",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SubstanceDefinition"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SpecimenDefinitionTypeTestedContainerAdditive`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "additiveCodeableConcept",
            "additiveReference",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_4813(
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
            "additive": ["additiveCodeableConcept", "additiveReference"]
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


class SpecimenDefinitionTypeTestedHandling(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Specimen handling before testing.
    Set of instructions for preservation/transport of the specimen at a defined
    temperature interval, prior the testing process.
    """

    resource_type = Field("SpecimenDefinitionTypeTestedHandling", const=True)

    instruction: fhirtypes.Markdown = Field(
        None,
        alias="instruction",
        title="Preservation instruction",
        description=(
            "Additional textual instructions for the preservation or transport of "
            "the specimen. For instance, 'Protect from light exposure'."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    instruction__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_instruction", title="Extension field for ``instruction``."
    )

    maxDuration: fhirtypes.DurationType = Field(
        None,
        alias="maxDuration",
        title="Maximum preservation time",
        description=(
            "The maximum time interval of preservation of the specimen with these "
            "conditions."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    temperatureQualifier: fhirtypes.CodeableConceptType = Field(
        None,
        alias="temperatureQualifier",
        title="Qualifies the interval of temperature",
        description=(
            "It qualifies the interval of temperature, which characterizes an "
            "occurrence of handling. Conditions that are not related to temperature"
            " may be handled in the instruction element."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    temperatureRange: fhirtypes.RangeType = Field(
        None,
        alias="temperatureRange",
        title="Temperature range for these handling instructions",
        description="The temperature interval for this set of handling instructions.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SpecimenDefinitionTypeTestedHandling`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "temperatureQualifier",
            "temperatureRange",
            "maxDuration",
            "instruction",
        ]
