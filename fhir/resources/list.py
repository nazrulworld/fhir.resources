# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/List
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


class List(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A list is a curated collection of resources.
    """

    resource_type = Field("List", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="What the purpose of this list is",
        description="This code defines the purpose of the list - why it was created.",
        # if property is element of this resource.
        element_property=True,
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="When the list was prepared",
        description="The date that the list was prepared.",
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    emptyReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="emptyReason",
        title="Why list is empty",
        description="If the list is empty, why the list is empty.",
        # if property is element of this resource.
        element_property=True,
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Context in which list created",
        description="The encounter that is the context in which this list was created.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    entry: typing.List[fhirtypes.ListEntryType] = Field(
        None,
        alias="entry",
        title="Entries in the list",
        description="Entries in this list.",
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier",
        description=(
            "Identifier for the List assigned for business purposes outside the "
            "context of FHIR."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    mode: fhirtypes.Code = Field(
        None,
        alias="mode",
        title="working | snapshot | changes",
        description=(
            "How this list was prepared - whether it is a working list that is "
            "suitable for being maintained on an ongoing basis, or if it represents"
            " a snapshot of a list of items from another source, or whether it is a"
            " prepared list where items may be marked as added, modified or "
            "deleted."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["working", "snapshot", "changes"],
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_mode", title="Extension field for ``mode``."
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Comments about the list",
        description="Comments that apply to the overall list.",
        # if property is element of this resource.
        element_property=True,
    )

    orderedBy: fhirtypes.CodeableConceptType = Field(
        None,
        alias="orderedBy",
        title="What order the list has",
        description="What order applies to the items in the list.",
        # if property is element of this resource.
        element_property=True,
    )

    source: fhirtypes.ReferenceType = Field(
        None,
        alias="source",
        title="Who and/or what defined the list contents (aka Author)",
        description=(
            "The entity responsible for deciding what the contents of the list "
            "were. Where the list was created by a human, this is the same as the "
            "author of the list."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "PractitionerRole", "Patient", "Device"],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="current | retired | entered-in-error",
        description="Indicates the current state of this list.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["current", "retired", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="If all resources have the same subject",
        description=(
            "The common subject (or patient) of the resources that are in the list "
            "if there is one."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group", "Device", "Location"],
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Descriptive name for the list",
        description="A label for the list assigned by the author.",
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``List`` according specification,
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
            "mode",
            "title",
            "code",
            "subject",
            "encounter",
            "date",
            "source",
            "orderedBy",
            "note",
            "entry",
            "emptyReason",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_604(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("mode", "mode__ext"), ("status", "status__ext")]
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


class ListEntry(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Entries in the list.
    Entries in this list.
    """

    resource_type = Field("ListEntry", const=True)

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="When item added to list",
        description="When this item was added to the list.",
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    deleted: bool = Field(
        None,
        alias="deleted",
        title="If this item is actually marked as deleted",
        description="True if this item is marked as deleted in the list.",
        # if property is element of this resource.
        element_property=True,
    )
    deleted__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_deleted", title="Extension field for ``deleted``."
    )

    flag: fhirtypes.CodeableConceptType = Field(
        None,
        alias="flag",
        title="Status/Workflow information about this item",
        description=(
            "The flag allows the system constructing the list to indicate the role "
            "and significance of the item in the list."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    item: fhirtypes.ReferenceType = Field(
        ...,
        alias="item",
        title="Actual entry",
        description="A reference to the actual resource from which data was derived.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ListEntry`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "flag",
            "deleted",
            "date",
            "item",
        ]
