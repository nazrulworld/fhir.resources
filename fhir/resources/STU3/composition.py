# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Composition
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


class Composition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A set of resources composed into a single coherent clinical statement with
    clinical attestation.
    A set of healthcare-related information that is assembled together into a
    single logical document that provides a single coherent statement of
    meaning, establishes its own context and that has clinical attestation with
    regard to who is making the statement. While a Composition defines the
    structure, it does not actually contain the content: rather the full
    content of a document is contained in a Bundle, of which the Composition is
    the first resource contained.
    """

    resource_type = Field("Composition", const=True)

    attester: typing.List[fhirtypes.CompositionAttesterType] = Field(
        None,
        alias="attester",
        title="Attests to accuracy of composition",
        description=(
            "A participant who has attested to the accuracy of the "
            "composition/document."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    author: typing.List[fhirtypes.ReferenceType] = Field(
        ...,
        alias="author",
        title="Who and/or what authored the composition",
        description=(
            "Identifies who is responsible for the information in the composition, "
            "not necessarily who typed it in."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Device", "Patient", "RelatedPerson"],
    )

    class_fhir: fhirtypes.CodeableConceptType = Field(
        None,
        alias="class",
        title="Categorization of Composition",
        description=(
            "A categorization for the type of the composition - helps for indexing "
            "and searching. This may be implied by or derived from the code "
            "specified in the Composition Type."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    confidentiality: fhirtypes.Code = Field(
        None,
        alias="confidentiality",
        title="As defined by affinity domain",
        description="The code specifying the level of confidentiality of the Composition.",
        # if property is element of this resource.
        element_property=True,
    )
    confidentiality__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_confidentiality", title="Extension field for ``confidentiality``."
    )

    custodian: fhirtypes.ReferenceType = Field(
        None,
        alias="custodian",
        title="Organization which maintains the composition",
        description=(
            "Identifies the organization or group who is responsible for ongoing "
            "maintenance of and access to the composition/document information."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Composition editing time",
        description=(
            "The composition editing time, when the composition was last logically "
            "changed by the author."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Context of the Composition",
        description=(
            "Describes the clinical encounter or type of care this documentation is"
            " associated with."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    event: typing.List[fhirtypes.CompositionEventType] = Field(
        None,
        alias="event",
        title="The clinical service(s) being documented",
        description=(
            "The clinical service, such as a colonoscopy or an appendectomy, being "
            "documented."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Logical identifier of composition (version-independent)",
        description=(
            "Logical identifier for the composition, assigned when created. This "
            "identifier stays constant as the composition is changed over time."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    relatesTo: typing.List[fhirtypes.CompositionRelatesToType] = Field(
        None,
        alias="relatesTo",
        title="Relationships to other compositions/documents",
        description=(
            "Relationships that this composition has with other compositions or "
            "documents that already exist."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    section: typing.List[fhirtypes.CompositionSectionType] = Field(
        None,
        alias="section",
        title="Composition is broken into sections",
        description="The root of the sections that make up the composition.",
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="preliminary | final | amended | entered-in-error",
        description=(
            "The workflow/clinical status of this composition. The status is a "
            "marker for the clinical standing of the document."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["preliminary", "final", "amended", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Who and/or what the composition is about",
        description=(
            "Who or what the composition is about. The composition can be about a "
            "person, (patient or healthcare practitioner), a device (e.g. a "
            "machine) or even a group of subjects (such as a document about a herd "
            "of livestock, or a set of patients that share a common exposure)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Human Readable name/title",
        description="Official human-readable label for the composition.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Kind of composition (LOINC if possible)",
        description=(
            "Specifies the particular kind of composition (e.g. History and "
            "Physical, Discharge Summary, Progress Note). This usually equates to "
            "the purpose of making the composition."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Composition`` according specification,
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
            "identifier",
            "status",
            "type",
            "class",
            "subject",
            "encounter",
            "date",
            "author",
            "title",
            "confidentiality",
            "attester",
            "custodian",
            "relatesTo",
            "event",
            "section",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1349(
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
            ("date", "date__ext"),
            ("status", "status__ext"),
            ("title", "title__ext"),
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


class CompositionAttester(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Attests to accuracy of composition.
    A participant who has attested to the accuracy of the composition/document.
    """

    resource_type = Field("CompositionAttester", const=True)

    mode: typing.List[fhirtypes.Code] = Field(
        None,
        alias="mode",
        title="personal | professional | legal | official",
        description="The type of attestation the authenticator offers.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["personal", "professional", "legal", "official"],
    )
    mode__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_mode", title="Extension field for ``mode``.")

    party: fhirtypes.ReferenceType = Field(
        None,
        alias="party",
        title="Who attested the composition",
        description="Who attested the composition in the specified way.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Practitioner", "Organization"],
    )

    time: fhirtypes.DateTime = Field(
        None,
        alias="time",
        title="When the composition was attested",
        description="When the composition was attested by the party.",
        # if property is element of this resource.
        element_property=True,
    )
    time__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_time", title="Extension field for ``time``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CompositionAttester`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "mode", "time", "party"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2197(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("mode", "mode__ext")]
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


class CompositionEvent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The clinical service(s) being documented.
    The clinical service, such as a colonoscopy or an appendectomy, being
    documented.
    """

    resource_type = Field("CompositionEvent", const=True)

    code: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="code",
        title="Code(s) that apply to the event being documented",
        description=(
            "This list of codes represents the main clinical acts, such as a "
            "colonoscopy or an appendectomy, being documented. In some cases, the "
            'event is inherent in the typeCode, such as a "History and Physical '
            'Report" in which the procedure being documented is necessarily a '
            '"History and Physical" act.'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    detail: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="detail",
        title="The event(s) being documented",
        description=(
            "The description and/or reference of the event(s) being documented. For"
            " example, this could be used to document such a colonoscopy or an "
            "appendectomy."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="The period covered by the documentation",
        description=(
            "The period of time covered by the documentation. There is no assertion"
            " that the documentation is a complete representation for this period, "
            "only that it documents events during this time."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CompositionEvent`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "period", "detail"]


class CompositionRelatesTo(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Relationships to other compositions/documents.
    Relationships that this composition has with other compositions or
    documents that already exist.
    """

    resource_type = Field("CompositionRelatesTo", const=True)

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="replaces | transforms | signs | appends",
        description=(
            "The type of relationship that this composition has with anther "
            "composition or document."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["replaces", "transforms", "signs", "appends"],
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    targetIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="targetIdentifier",
        title="Target of the relationship",
        description="The target composition/document of this relationship.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e target[x]
        one_of_many="target",
        one_of_many_required=True,
    )

    targetReference: fhirtypes.ReferenceType = Field(
        None,
        alias="targetReference",
        title="Target of the relationship",
        description="The target composition/document of this relationship.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e target[x]
        one_of_many="target",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Composition"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CompositionRelatesTo`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "targetIdentifier",
            "targetReference",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2265(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2265(
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
        one_of_many_fields = {"target": ["targetIdentifier", "targetReference"]}
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


class CompositionSection(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Composition is broken into sections.
    The root of the sections that make up the composition.
    """

    resource_type = Field("CompositionSection", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Classification of section (recommended)",
        description=(
            "A code identifying the kind of content contained within the section. "
            "This must be consistent with the section title."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    emptyReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="emptyReason",
        title="Why the section is empty",
        description=(
            "If the section is empty, why the list is empty. An empty section "
            "typically has some text explaining the empty reason."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    entry: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="entry",
        title="A reference to data that supports this section",
        description=(
            "A reference to the actual resource from which the narrative in the "
            "section is derived."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    mode: fhirtypes.Code = Field(
        None,
        alias="mode",
        title="working | snapshot | changes",
        description=(
            "How the entry list was prepared - whether it is a working list that is"
            " suitable for being maintained on an ongoing basis, or if it "
            "represents a snapshot of a list of items from another source, or "
            "whether it is a prepared list where items may be marked as added, "
            "modified or deleted."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["working", "snapshot", "changes"],
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_mode", title="Extension field for ``mode``."
    )

    orderedBy: fhirtypes.CodeableConceptType = Field(
        None,
        alias="orderedBy",
        title="Order of section entries",
        description="Specifies the order applied to the items in the section entries.",
        # if property is element of this resource.
        element_property=True,
    )

    section: typing.List[fhirtypes.CompositionSectionType] = Field(
        None,
        alias="section",
        title="Nested Section",
        description="A nested sub-section within this section.",
        # if property is element of this resource.
        element_property=True,
    )

    text: fhirtypes.NarrativeType = Field(
        None,
        alias="text",
        title="Text summary of the section, for human interpretation",
        description=(
            "A human-readable narrative that contains the attested content of the "
            "section, used to represent the content of the resource to a human. The"
            " narrative need not encode all the structured data, but is required to"
            ' contain sufficient detail to make it "clinically safe" for a human to'
            " just read the narrative."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Label for section (e.g. for ToC)",
        description=(
            "The label for this particular section.  This will be part of the "
            "rendered content for the document, and is often used to build a table "
            "of contents."
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
        ``CompositionSection`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "title",
            "code",
            "text",
            "mode",
            "orderedBy",
            "entry",
            "emptyReason",
            "section",
        ]
