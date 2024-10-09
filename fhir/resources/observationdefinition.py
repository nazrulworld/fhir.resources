from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ObservationDefinition
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ObservationDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Definition of an observation.
    Set of definitional characteristics for a kind of observation or
    measurement produced or consumed by an orderable health care service.
    """

    __resource_type__ = "ObservationDefinition"

    approvalDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="approvalDate",
        title="When ObservationDefinition was approved by publisher",
        description=(
            "The date on which the asset content was approved by the publisher. "
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

    bodySite: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="bodySite",
        title="Body part to be observed",
        description="The site on the subject's body where the  observation is to be made.",
        json_schema_extra={
            "element_property": True,
        },
    )

    category: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="category",
        title="General type of observation",
        description="A code that classifies the general type of observation.",
        json_schema_extra={
            "element_property": True,
        },
    )

    code: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="code",
        title="Type of observation",
        description=(
            "Describes what will be observed. Sometimes this is called the "
            'observation "name".'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    component: typing.List[fhirtypes.ObservationDefinitionComponentType] | None = Field(  # type: ignore
        None,
        alias="component",
        title="Component results",
        description=(
            "Some observations have multiple component observations, expressed as "
            "separate code value pairs."
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
            "Copyright statement relating to the ObservationDefinition and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the ObservationDefinition."
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
            "The date (and optionally time) when the ObservationDefinition was last"
            " significantly changed. The date must change when the business version"
            " changes and it must change if the status code changes. In addition, "
            "it should change when the substantive content of the "
            "ObservationDefinition changes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    derivedFromCanonical: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="derivedFromCanonical",
        title="Based on FHIR definition of another observation",
        description=(
            "The canonical URL pointing to another FHIR-defined "
            "ObservationDefinition that is adhered to in whole or in part by this "
            "definition."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ObservationDefinition"],
        },
    )
    derivedFromCanonical__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_derivedFromCanonical",
        title="Extension field for ``derivedFromCanonical``.",
    )

    derivedFromUri: typing.List[fhirtypes.UriType | None] | None = Field(  # type: ignore
        None,
        alias="derivedFromUri",
        title="Based on external definition",
        description=(
            "The URL pointing to an externally-defined observation definition, "
            "guideline or other definition that is adhered to in whole or in part "
            "by this definition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    derivedFromUri__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_derivedFromUri", title="Extension field for ``derivedFromUri``."
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Natural language description of the ObservationDefinition",
        description=(
            "A free text natural language description of the ObservationDefinition "
            "from the consumer's perspective."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    device: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="device",
        title="Measurement device or model of device",
        description=(
            "The measurement model of device or actual device used to produce "
            "observations of this type."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DeviceDefinition", "Device"],
        },
    )

    effectivePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="effectivePeriod",
        title="The effective date range for the ObservationDefinition",
        description=(
            "The period during which the ObservationDefinition content was or is "
            "planned to be effective."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    experimental: bool | None = Field(  # type: ignore
        None,
        alias="experimental",
        title="If for testing purposes, not real usage",
        description=(
            "A flag to indicate that this ObservationDefinition is authored for "
            "testing purposes (or education/evaluation/marketing), and is not "
            "intended to be used for genuine usage."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    hasMember: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="hasMember",
        title=(
            "Definitions of related resources belonging to this kind of observation"
            " group"
        ),
        description=(
            "This ObservationDefinition defines a group  observation (e.g. a "
            "battery, a panel of tests, a set of vital sign measurements) that "
            "includes the target as a member of the group."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ObservationDefinition", "Questionnaire"],
        },
    )

    identifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business identifier of the ObservationDefinition",
        description=(
            "Business identifiers assigned to this ObservationDefinition. by the "
            "performer and/or other systems. These identifiers remain constant as "
            "the resource is updated and propagates from server to server."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for this ObservationDefinition (if applicable)",
        description=(
            "A jurisdiction in which the ObservationDefinition is intended to be "
            "used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    lastReviewDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="lastReviewDate",
        title="Date on which the asset content was last reviewed by the publisher",
        description=(
            "The date on which the asset content was last reviewed. Review happens "
            "periodically after that, but doesn't change the original approval "
            "date."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_lastReviewDate", title="Extension field for ``lastReviewDate``."
    )

    method: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="method",
        title="Method used to produce the observation",
        description="The method or technique used to perform the observation.",
        json_schema_extra={
            "element_property": True,
        },
    )

    multipleResultsAllowed: bool | None = Field(  # type: ignore
        None,
        alias="multipleResultsAllowed",
        title="Multiple results allowed for conforming observations",
        description=(
            "Multiple results allowed for observations conforming to this "
            "ObservationDefinition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    multipleResultsAllowed__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_multipleResultsAllowed",
        title="Extension field for ``multipleResultsAllowed``.",
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name for this ObservationDefinition (computer friendly)",
        description=(
            "A natural language name identifying the ObservationDefinition. This "
            "name should be usable as an identifier for the module by machine "
            "processing applications such as code generation."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    performerType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="performerType",
        title="Desired kind of performer for such kind of observation",
        description=(
            "The type of individual/organization/device that is expected to act "
            "upon instances of this definition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    permittedDataType: typing.List[fhirtypes.CodeType | None] | None = Field(  # type: ignore
        None,
        alias="permittedDataType",
        title=(
            "Quantity | CodeableConcept | string | boolean | integer | Range | "
            "Ratio | SampledData | time | dateTime | Period"
        ),
        description=(
            "The data types allowed for the value element of the instance "
            "observations conforming to this ObservationDefinition."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "Quantity",
                "CodeableConcept",
                "string",
                "boolean",
                "integer",
                "Range",
                "Ratio",
                "SampledData",
                "time",
                "dateTime",
                "Period",
            ],
        },
    )
    permittedDataType__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_permittedDataType",
        title="Extension field for ``permittedDataType``.",
    )

    permittedUnit: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        None,
        alias="permittedUnit",
        title="Unit for quantitative results",
        description=(
            "Units allowed for the valueQuantity element in the instance "
            "observations conforming to this ObservationDefinition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    preferredReportName: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="preferredReportName",
        title="The preferred name to be used when reporting the observation results",
        description=(
            "The preferred name to be used when reporting the results of "
            "observations conforming to this ObservationDefinition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    preferredReportName__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_preferredReportName",
        title="Extension field for ``preferredReportName``.",
    )

    publisher: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="publisher",
        title=(
            "The name of the individual or organization that published the "
            "ObservationDefinition"
        ),
        description=(
            'Helps establish the "authority/credibility" of the '
            "ObservationDefinition. May also allow for contact."
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
        title="Why this ObservationDefinition is defined",
        description=(
            "Explains why this ObservationDefinition is needed and why it has been "
            "designed as it has."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    qualifiedValue: typing.List[fhirtypes.ObservationDefinitionQualifiedValueType] | None = Field(  # type: ignore
        None,
        alias="qualifiedValue",
        title="Set of qualified values for observation results",
        description=(
            "A set of qualified values associated with a context and a set of "
            "conditions -  provides a range for quantitative and ordinal "
            "observations and a collection of value sets for qualitative "
            "observations."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    specimen: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="specimen",
        title="Kind of specimen used by this type of observation",
        description="The kind of specimen that this type of observation is produced on.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["SpecimenDefinition"],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description="The current state of the ObservationDefinition.",
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

    subject: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="subject",
        title="Type of subject for the defined observation",
        description=(
            "A code that describes the intended kind of subject of Observation "
            "instances conforming to this ObservationDefinition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Name for this ObservationDefinition (human friendly)",
        description=(
            "A short, descriptive, user-friendly title for the "
            "ObservationDefinition."
        ),
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
            "Logical canonical URL to reference this ObservationDefinition "
            "(globally unique)"
        ),
        description=(
            "An absolute URL that is used to identify this ObservationDefinition "
            "when it is referenced in a specification, model, design or an "
            "instance. This SHALL be a URL, SHOULD be globally unique, and SHOULD "
            "be an address at which this ObservationDefinition is (or will be) "
            "published. The URL SHOULD include the major version of the "
            "ObservationDefinition. For more information see Technical and Business"
            " Versions."
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
        title="Content intends to support these contexts",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These contexts may be general categories "
            "(gender, age, ...) or may be references to specific programs "
            "(insurance plans, studies, ...) and may be used to assist with "
            "indexing and searching for appropriate ObservationDefinition "
            "instances."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="Business version of the ObservationDefinition",
        description=(
            "The identifier that is used to identify this version of the "
            "ObservationDefinition when it is referenced in a specification, model,"
            " design or instance. This is an arbitrary value managed by the "
            "ObservationDefinition author and is not expected to be globally "
            "unique. For example, it might be a timestamp (e.g. yyyymmdd) if a "
            "managed version is not available. There is also no expectation that "
            "versions are orderable."
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
        ``ObservationDefinition`` according specification,
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
            "approvalDate",
            "lastReviewDate",
            "effectivePeriod",
            "derivedFromCanonical",
            "derivedFromUri",
            "subject",
            "performerType",
            "category",
            "code",
            "permittedDataType",
            "multipleResultsAllowed",
            "bodySite",
            "method",
            "specimen",
            "device",
            "preferredReportName",
            "permittedUnit",
            "qualifiedValue",
            "hasMember",
            "component",
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


class ObservationDefinitionComponent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Component results.
    Some observations have multiple component observations, expressed as
    separate code value pairs.
    """

    __resource_type__ = "ObservationDefinitionComponent"

    code: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="code",
        title="Type of observation",
        description="Describes what will be observed.",
        json_schema_extra={
            "element_property": True,
        },
    )

    permittedDataType: typing.List[fhirtypes.CodeType | None] | None = Field(  # type: ignore
        None,
        alias="permittedDataType",
        title=(
            "Quantity | CodeableConcept | string | boolean | integer | Range | "
            "Ratio | SampledData | time | dateTime | Period"
        ),
        description=(
            "The data types allowed for the value element of the instance of this "
            "component observations."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "Quantity",
                "CodeableConcept",
                "string",
                "boolean",
                "integer",
                "Range",
                "Ratio",
                "SampledData",
                "time",
                "dateTime",
                "Period",
            ],
        },
    )
    permittedDataType__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_permittedDataType",
        title="Extension field for ``permittedDataType``.",
    )

    permittedUnit: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        None,
        alias="permittedUnit",
        title="Unit for quantitative results",
        description=(
            "Units allowed for the valueQuantity element in the instance "
            "observations conforming to this ObservationDefinition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    qualifiedValue: typing.List[fhirtypes.ObservationDefinitionQualifiedValueType] | None = Field(  # type: ignore
        None,
        alias="qualifiedValue",
        title="Set of qualified values for observation results",
        description=(
            "A set of qualified values associated with a context and a set of "
            "conditions -  provides a range for quantitative and ordinal "
            "observations and a collection of value sets for qualitative "
            "observations."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ObservationDefinitionComponent`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "permittedDataType",
            "permittedUnit",
            "qualifiedValue",
        ]


class ObservationDefinitionQualifiedValue(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Set of qualified values for observation results.
    A set of qualified values associated with a context and a set of conditions
    -  provides a range for quantitative and ordinal observations and a
    collection of value sets for qualitative observations.
    """

    __resource_type__ = "ObservationDefinitionQualifiedValue"

    abnormalCodedValueSet: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="abnormalCodedValueSet",
        title=(
            "Value set of abnormal coded values as part of this set of qualified "
            "values"
        ),
        description=(
            "The set of abnormal coded results for qualitative observations  that "
            "match the criteria of this set of qualified values."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ValueSet"],
        },
    )
    abnormalCodedValueSet__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_abnormalCodedValueSet",
        title="Extension field for ``abnormalCodedValueSet``.",
    )

    age: fhirtypes.RangeType | None = Field(  # type: ignore
        None,
        alias="age",
        title="Applicable age range for the set of qualified values",
        description="The age range this  set of qualified values applies to.",
        json_schema_extra={
            "element_property": True,
        },
    )

    appliesTo: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="appliesTo",
        title="Targetted population for the set of qualified values",
        description="The target population this  set of qualified values applies to.",
        json_schema_extra={
            "element_property": True,
        },
    )

    condition: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="condition",
        title="Condition associated with the set of qualified values",
        description=(
            "Text based condition for which the the set of qualified values is "
            "valid."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    condition__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_condition", title="Extension field for ``condition``."
    )

    context: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="context",
        title="Context qualifier for the set of qualified values",
        description="A concept defining the context for this set of qualified values.",
        json_schema_extra={
            "element_property": True,
        },
    )

    criticalCodedValueSet: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="criticalCodedValueSet",
        title=(
            "Value set of critical coded values as part of this set of qualified "
            "values"
        ),
        description=(
            "The set of critical coded results for qualitative observations  that "
            "match the criteria of this set of qualified values."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ValueSet"],
        },
    )
    criticalCodedValueSet__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_criticalCodedValueSet",
        title="Extension field for ``criticalCodedValueSet``.",
    )

    gender: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="gender",
        title="male | female | other | unknown",
        description="The gender this  set of qualified values applies to.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["male", "female", "other", "unknown"],
        },
    )
    gender__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_gender", title="Extension field for ``gender``."
    )

    gestationalAge: fhirtypes.RangeType | None = Field(  # type: ignore
        None,
        alias="gestationalAge",
        title="Applicable gestational age range for the set of qualified values",
        description="The gestational age this  set of qualified values applies to.",
        json_schema_extra={
            "element_property": True,
        },
    )

    normalCodedValueSet: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="normalCodedValueSet",
        title=(
            "Value set of normal coded values as part of this set of qualified "
            "values"
        ),
        description=(
            "The set of normal coded results for qualitative observations  that "
            "match the criteria of this set of qualified values."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ValueSet"],
        },
    )
    normalCodedValueSet__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_normalCodedValueSet",
        title="Extension field for ``normalCodedValueSet``.",
    )

    range: fhirtypes.RangeType | None = Field(  # type: ignore
        None,
        alias="range",
        title="The range for continuous or ordinal observations",
        description=(
            "The range of values defined for continuous or ordinal observations "
            "that match the criteria of this set of qualified values."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    rangeCategory: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="rangeCategory",
        title="reference | critical | absolute",
        description=(
            "The category of range of values for continuous or ordinal observations"
            " that match the criteria of this set of qualified values."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["reference", "critical", "absolute"],
        },
    )
    rangeCategory__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_rangeCategory", title="Extension field for ``rangeCategory``."
    )

    validCodedValueSet: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="validCodedValueSet",
        title=(
            "Value set of valid coded values as part of this set of qualified " "values"
        ),
        description=(
            "The set of valid coded results for qualitative observations  that "
            "match the criteria of this set of qualified values."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ValueSet"],
        },
    )
    validCodedValueSet__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_validCodedValueSet",
        title="Extension field for ``validCodedValueSet``.",
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ObservationDefinitionQualifiedValue`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "context",
            "appliesTo",
            "gender",
            "age",
            "gestationalAge",
            "condition",
            "rangeCategory",
            "range",
            "validCodedValueSet",
            "normalCodedValueSet",
            "abnormalCodedValueSet",
            "criticalCodedValueSet",
        ]
