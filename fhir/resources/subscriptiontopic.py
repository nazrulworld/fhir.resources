# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubscriptionTopic
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


class SubscriptionTopic(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The definition of a specific topic for triggering events within the
    Subscriptions framework.
    Describes a stream of resource state changes or events and annotated with
    labels useful to filter projections from this topic.
    """

    resource_type = Field("SubscriptionTopic", const=True)

    approvalDate: fhirtypes.Date = Field(
        None,
        alias="approvalDate",
        title="When SubscriptionTopic is/was approved by publisher",
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

    canFilterBy: typing.List[fhirtypes.SubscriptionTopicCanFilterByType] = Field(
        None,
        alias="canFilterBy",
        title=(
            "Properties by which a Subscription can filter notifications from the "
            "SubscriptionTopic"
        ),
        description=(
            "List of properties by which Subscriptions on the SubscriptionTopic can"
            " be filtered. May be defined Search Parameters (e.g., "
            "Encounter.patient) or parameters defined within this SubscriptionTopic"
            " context (e.g., hub.event)."
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
            "A copyright statement relating to the SubscriptionTopic and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the SubscriptionTopic."
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
            "The date (and optionally time) when the subscription topic was last "
            "significantly changed. The date must change when the business version "
            "changes and it must change if the status code changes. In addition, it"
            " should change when the substantive content of the subscription topic "
            "changes."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    derivedFrom: typing.List[typing.Optional[fhirtypes.Canonical]] = Field(
        None,
        alias="derivedFrom",
        title="Based on FHIR protocol or definition",
        description=(
            "The canonical URL pointing to another FHIR-defined SubscriptionTopic "
            "that is adhered to in whole or in part by this SubscriptionTopic."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SubscriptionTopic"],
    )
    derivedFrom__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_derivedFrom", title="Extension field for ``derivedFrom``.")

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Natural language description of the SubscriptionTopic",
        description=(
            "A free text natural language description of the Topic from the "
            "consumer's perspective."
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
        title="The effective date range for the SubscriptionTopic",
        description=(
            "The period during which the SubscriptionTopic content was or is "
            "planned to be effective."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    eventTrigger: typing.List[fhirtypes.SubscriptionTopicEventTriggerType] = Field(
        None,
        alias="eventTrigger",
        title="Event definitions the SubscriptionTopic",
        description="Event definition which can be used to trigger the SubscriptionTopic.",
        # if property is element of this resource.
        element_property=True,
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="If for testing purposes, not real usage",
        description=(
            "A flag to indicate that this TopSubscriptionTopicic is authored for "
            "testing purposes (or education/evaluation/marketing), and is not "
            "intended to be used for genuine usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier for subscription topic",
        description=(
            "Business identifiers assigned to this subscription topic by the "
            "performer and/or other systems.  These identifiers remain constant as "
            "the resource is updated and propagates from server to server."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction of the SubscriptionTopic (if applicable)",
        description="A jurisdiction in which the Topic is intended to be used.",
        # if property is element of this resource.
        element_property=True,
    )

    lastReviewDate: fhirtypes.Date = Field(
        None,
        alias="lastReviewDate",
        title="Date the Subscription Topic was last reviewed by the publisher",
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
        title="Name for this subscription topic (computer friendly)",
        description=(
            "A natural language name identifying the subscription topic This name "
            "should be usable as an identifier for the module by machine processing"
            " applications such as code generation."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    notificationShape: typing.List[
        fhirtypes.SubscriptionTopicNotificationShapeType
    ] = Field(
        None,
        alias="notificationShape",
        title=(
            "Properties for describing the shape of notifications generated by this"
            " topic"
        ),
        description=(
            "List of properties to describe the shape (e.g., resources) included in"
            " notifications from this Subscription Topic."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title=(
            "The name of the individual or organization that published the "
            "SubscriptionTopic"
        ),
        description=(
            'Helps establish the "authority/credibility" of the SubscriptionTopic.'
            "  May also allow for contact."
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
        title="Why this SubscriptionTopic is defined",
        description=(
            "Explains why this Topic is needed and why it has been designed as it "
            "has."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    resourceTrigger: typing.List[
        fhirtypes.SubscriptionTopicResourceTriggerType
    ] = Field(
        None,
        alias="resourceTrigger",
        title="Definition of a resource-based trigger for the subscription topic",
        description=(
            "A definition of a resource-based event that triggers a notification "
            "based on the SubscriptionTopic. The criteria may be just a human "
            "readable description and/or a full FHIR search string or FHIRPath "
            "expression. Multiple triggers are considered OR joined (e.g., a "
            "resource update matching ANY of the definitions will trigger a "
            "notification)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description="The current state of the SubscriptionTopic.",
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
        title="Name for this subscription topic (human friendly)",
        description=(
            "A short, descriptive, user-friendly title for the subscription topic."
            '  For example, "admission".'
        ),
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
            "Canonical identifier for this subscription topic, represented as an "
            "absolute URI (globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this subscription topic when "
            "it is referenced in a specification, model, design or an instance; "
            "also called its canonical identifier. This SHOULD be globally unique "
            "and SHOULD be a literal address at which an authoritative instance of "
            "this subscription topic is (or will be) published. This URL can be the"
            " target of a canonical reference. It SHALL remain the same when the "
            "subscription topic is stored on different servers."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
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
            "indexing and searching of code system definitions."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the subscription topic",
        description=(
            "The identifier that is used to identify this version of the "
            "subscription topic when it is referenced in a specification, model, "
            "design or instance. This is an arbitrary value managed by the Topic "
            "author and is not expected to be globally unique. For example, it "
            "might be a timestamp (e.g. yyyymmdd) if a managed version is not "
            "available. There is also no expectation that versions are orderable."
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
        ``SubscriptionTopic`` according specification,
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
            "derivedFrom",
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
            "resourceTrigger",
            "eventTrigger",
            "canFilterBy",
            "notificationShape",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1978(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext"), ("url", "url__ext")]
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
    def validate_one_of_many_1978(
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


class SubscriptionTopicCanFilterBy(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Properties by which a Subscription can filter notifications from the
    SubscriptionTopic.
    List of properties by which Subscriptions on the SubscriptionTopic can be
    filtered. May be defined Search Parameters (e.g., Encounter.patient) or
    parameters defined within this SubscriptionTopic context (e.g., hub.event).
    """

    resource_type = Field("SubscriptionTopicCanFilterBy", const=True)

    comparator: typing.List[typing.Optional[fhirtypes.Code]] = Field(
        None,
        alias="comparator",
        title="eq | ne | gt | lt | ge | le | sa | eb | ap",
        description="Comparators allowed for the filter parameter.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["eq", "ne", "gt", "lt", "ge", "le", "sa", "eb", "ap"],
    )
    comparator__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_comparator", title="Extension field for ``comparator``.")

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Description of this filter parameter",
        description="Description of how this filtering parameter is intended to be used.",
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    filterDefinition: fhirtypes.Uri = Field(
        None,
        alias="filterDefinition",
        title="Canonical URL for a filterParameter definition",
        description=(
            "Either the canonical URL to a search parameter (like "
            '"http://hl7.org/fhir/SearchParameter/encounter-patient") or the '
            "officially-defined URI for a shared filter concept (like "
            '"http://example.org/concepts/shared-common-event").'
        ),
        # if property is element of this resource.
        element_property=True,
    )
    filterDefinition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_filterDefinition",
        title="Extension field for ``filterDefinition``.",
    )

    filterParameter: fhirtypes.String = Field(
        None,
        alias="filterParameter",
        title=(
            "Human-readable and computation-friendly name for a filter parameter "
            "usable by subscriptions on this topic, via "
            "Subscription.filterBy.filterParameter"
        ),
        description=(
            "Either the canonical URL to a search parameter (like "
            '"http://hl7.org/fhir/SearchParameter/encounter-patient") or topic-'
            'defined parameter (like "hub.event") which is a label for the filter.'
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    filterParameter__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_filterParameter", title="Extension field for ``filterParameter``."
    )

    modifier: typing.List[typing.Optional[fhirtypes.Code]] = Field(
        None,
        alias="modifier",
        title=(
            "missing | exact | contains | not | text | in | not-in | below | above "
            "| type | identifier | of-type | code-text | text-advanced | iterate"
        ),
        description="Modifiers allowed for the filter parameter.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "missing",
            "exact",
            "contains",
            "not",
            "text",
            "in",
            "not-in",
            "below",
            "above",
            "type",
            "identifier",
            "of-type",
            "code-text",
            "text-advanced",
            "iterate",
        ],
    )
    modifier__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_modifier", title="Extension field for ``modifier``.")

    resource: fhirtypes.Uri = Field(
        None,
        alias="resource",
        title="URL of the triggering Resource that this filter applies to",
        description=(
            "URL of the Resource that is the type used in this filter. This is the "
            '"focus" of the topic (or one of them if there are more than one). It '
            "will be the same, a generality, or a specificity of "
            "SubscriptionTopic.resourceTrigger.resource or "
            "SubscriptionTopic.eventTrigger.resource when they are present."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    resource__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_resource", title="Extension field for ``resource``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubscriptionTopicCanFilterBy`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "description",
            "resource",
            "filterParameter",
            "filterDefinition",
            "comparator",
            "modifier",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3075(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("filterParameter", "filterParameter__ext")]
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


class SubscriptionTopicEventTrigger(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Event definitions the SubscriptionTopic.
    Event definition which can be used to trigger the SubscriptionTopic.
    """

    resource_type = Field("SubscriptionTopicEventTrigger", const=True)

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Text representation of the event trigger",
        description=(
            "The human readable description of an event to trigger a notification "
            'for the SubscriptionTopic - for example, "Patient Admission, as '
            'defined in HL7v2 via message ADT^A01". Multiple values are considered '
            "OR joined (e.g., matching any single event listed)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    event: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="event",
        title="Event which can trigger a notification from the SubscriptionTopic",
        description=(
            "A well-defined event which can be used to trigger notifications from "
            "the SubscriptionTopic."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    resource: fhirtypes.Uri = Field(
        None,
        alias="resource",
        title=(
            "Data Type or Resource (reference to definition) for this trigger "
            "definition"
        ),
        description=(
            "URL of the Resource that is the focus type used in this event trigger."
            "  Relative URLs are relative to the StructureDefinition root of the "
            "implemented FHIR version (e.g., "
            'http://hl7.org/fhir/StructureDefinition). For example, "Patient" maps '
            "to http://hl7.org/fhir/StructureDefinition/Patient.  For more "
            'information, see <a href="elementdefinition-definitions.html#ElementDe'
            'finition.type.code">ElementDefinition.type.code</a>.'
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    resource__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_resource", title="Extension field for ``resource``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubscriptionTopicEventTrigger`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "description",
            "event",
            "resource",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3231(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("resource", "resource__ext")]
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


class SubscriptionTopicNotificationShape(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Properties for describing the shape of notifications generated by this
    topic.
    List of properties to describe the shape (e.g., resources) included in
    notifications from this Subscription Topic.
    """

    resource_type = Field("SubscriptionTopicNotificationShape", const=True)

    include: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="include",
        title="Include directives, rooted in the resource for this shape",
        description=(
            "Search-style _include directives, rooted in the resource for this "
            "shape. Servers SHOULD include resources listed here, if they exist and"
            " the user is authorized to receive them.  Clients SHOULD be prepared "
            "to receive these additional resources, but SHALL function properly "
            "without them."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    include__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_include", title="Extension field for ``include``.")

    resource: fhirtypes.Uri = Field(
        None,
        alias="resource",
        title=(
            "URL of the Resource that is the focus (main) resource in a "
            "notification shape"
        ),
        description=(
            "URL of the Resource that is the type used in this shape. This is the "
            "'focus' resource of the topic (or one of them if there are more than "
            "one) and the root resource for this shape definition. It will be the "
            "same, a generality, or a specificity of "
            "SubscriptionTopic.resourceTrigger.resource or "
            "SubscriptionTopic.eventTrigger.resource when they are present."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    resource__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_resource", title="Extension field for ``resource``."
    )

    revInclude: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="revInclude",
        title="Reverse include directives, rooted in the resource for this shape",
        description=(
            "Search-style _revinclude directives, rooted in the resource for this "
            "shape. Servers SHOULD include resources listed here, if they exist and"
            " the user is authorized to receive them.  Clients SHOULD be prepared "
            "to receive these additional resources, but SHALL function properly "
            "without them."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    revInclude__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_revInclude", title="Extension field for ``revInclude``.")

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubscriptionTopicNotificationShape`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "resource",
            "include",
            "revInclude",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3732(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("resource", "resource__ext")]
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


class SubscriptionTopicResourceTrigger(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Definition of a resource-based trigger for the subscription topic.
    A definition of a resource-based event that triggers a notification based
    on the SubscriptionTopic. The criteria may be just a human readable
    description and/or a full FHIR search string or FHIRPath expression.
    Multiple triggers are considered OR joined (e.g., a resource update
    matching ANY of the definitions will trigger a notification).
    """

    resource_type = Field("SubscriptionTopicResourceTrigger", const=True)

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Text representation of the resource trigger",
        description=(
            "The human readable description of this resource trigger for the "
            "SubscriptionTopic -  for example, \"An Encounter enters the 'in-"
            "progress' state\"."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    fhirPathCriteria: fhirtypes.String = Field(
        None,
        alias="fhirPathCriteria",
        title="FHIRPath based trigger rule",
        description=(
            "The FHIRPath based rules that the server should use to determine when "
            "to trigger a notification for this topic."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    fhirPathCriteria__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_fhirPathCriteria",
        title="Extension field for ``fhirPathCriteria``.",
    )

    queryCriteria: fhirtypes.SubscriptionTopicResourceTriggerQueryCriteriaType = Field(
        None,
        alias="queryCriteria",
        title="Query based trigger rule",
        description=(
            "The FHIR query based rules that the server should use to determine "
            "when to trigger a notification for this subscription topic."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    resource: fhirtypes.Uri = Field(
        None,
        alias="resource",
        title=(
            "Data Type or Resource (reference to definition) for this trigger "
            "definition"
        ),
        description=(
            "URL of the Resource that is the type used in this resource trigger.  "
            "Relative URLs are relative to the StructureDefinition root of the "
            "implemented FHIR version (e.g., "
            'http://hl7.org/fhir/StructureDefinition). For example, "Patient" maps '
            "to http://hl7.org/fhir/StructureDefinition/Patient.  For more "
            'information, see <a href="elementdefinition-definitions.html#ElementDe'
            'finition.type.code">ElementDefinition.type.code</a>.'
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    resource__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_resource", title="Extension field for ``resource``."
    )

    supportedInteraction: typing.List[typing.Optional[fhirtypes.Code]] = Field(
        None,
        alias="supportedInteraction",
        title="create | update | delete",
        description=(
            "The FHIR RESTful interaction which can be used to trigger a "
            "notification for the SubscriptionTopic. Multiple values are considered"
            " OR joined (e.g., CREATE or UPDATE). If not present, all supported "
            "interactions are assumed."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["create", "update", "delete"],
    )
    supportedInteraction__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_supportedInteraction",
        title="Extension field for ``supportedInteraction``.",
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubscriptionTopicResourceTrigger`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "description",
            "resource",
            "supportedInteraction",
            "queryCriteria",
            "fhirPathCriteria",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3557(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("resource", "resource__ext")]
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


class SubscriptionTopicResourceTriggerQueryCriteria(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Query based trigger rule.
    The FHIR query based rules that the server should use to determine when to
    trigger a notification for this subscription topic.
    """

    resource_type = Field("SubscriptionTopicResourceTriggerQueryCriteria", const=True)

    current: fhirtypes.String = Field(
        None,
        alias="current",
        title="Rule applied to current resource state",
        description=(
            "The FHIR query based rules are applied to the current resource state "
            "(e.g., state after an update)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    current__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_current", title="Extension field for ``current``."
    )

    previous: fhirtypes.String = Field(
        None,
        alias="previous",
        title="Rule applied to previous resource state",
        description=(
            "The FHIR query based rules are applied to the previous resource state "
            "(e.g., state before an update)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    previous__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_previous", title="Extension field for ``previous``."
    )

    requireBoth: bool = Field(
        None,
        alias="requireBoth",
        title="Both must be true flag",
        description=(
            "If set to `true`, both the `current` and `previous` query criteria "
            "must evaluate `true` to trigger a notification for this topic.  If set"
            " to `false` or not present, a notification for this topic will be "
            "triggered if either the `current` or `previous` tests evaluate to "
            "`true`."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    requireBoth__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_requireBoth", title="Extension field for ``requireBoth``."
    )

    resultForCreate: fhirtypes.Code = Field(
        None,
        alias="resultForCreate",
        title="test-passes | test-fails",
        description=(
            "For `create` interactions, should the `previous` criteria count as an "
            "automatic pass or an automatic fail. If not present, the testing "
            "behavior during `create` interactions is unspecified (server "
            "discretion)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["test-passes", "test-fails"],
    )
    resultForCreate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_resultForCreate", title="Extension field for ``resultForCreate``."
    )

    resultForDelete: fhirtypes.Code = Field(
        None,
        alias="resultForDelete",
        title="test-passes | test-fails",
        description=(
            "For 'delete' interactions, should the 'current' query criteria count "
            "as an automatic pass or an automatic fail. If not present, the testing"
            " behavior during `delete` interactions is unspecified (server "
            "discretion)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["test-passes", "test-fails"],
    )
    resultForDelete__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_resultForDelete", title="Extension field for ``resultForDelete``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubscriptionTopicResourceTriggerQueryCriteria`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "previous",
            "resultForCreate",
            "current",
            "resultForDelete",
            "requireBoth",
        ]
