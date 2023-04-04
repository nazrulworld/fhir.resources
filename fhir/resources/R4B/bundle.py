# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Bundle
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, fhirtypes, resource


class Bundle(resource.Resource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Contains a collection of resources.
    A container for a collection of resources.
    """

    resource_type = Field("Bundle", const=True)

    entry: typing.List[fhirtypes.BundleEntryType] = Field(
        None,
        alias="entry",
        title="Entry in the bundle - will have a resource or information",
        description=(
            "An entry in a bundle resource - will either contain a resource or "
            "information about a resource (transactions and history only)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Persistent identifier for the bundle",
        description=(
            "A persistent identifier for the bundle that won't change as a bundle "
            "is copied from server to server."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    link: typing.List[fhirtypes.BundleLinkType] = Field(
        None,
        alias="link",
        title="Links related to this Bundle",
        description="A series of links that provide context to this bundle.",
        # if property is element of this resource.
        element_property=True,
    )

    signature: fhirtypes.SignatureType = Field(
        None,
        alias="signature",
        title="Digital Signature",
        description="Digital Signature - base64 encoded. XML-DSig or a JWT.",
        # if property is element of this resource.
        element_property=True,
    )

    timestamp: fhirtypes.Instant = Field(
        None,
        alias="timestamp",
        title="When the bundle was assembled",
        description=(
            "The date/time that the bundle was assembled - i.e. when the resources "
            "were placed in the bundle."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    timestamp__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_timestamp", title="Extension field for ``timestamp``."
    )

    total: fhirtypes.UnsignedInt = Field(
        None,
        alias="total",
        title="If search, the total number of matches",
        description=(
            "If a set of search matches, this is the total number of entries of "
            "type 'match' across all pages in the search.  It does not include "
            "search.mode = 'include' or 'outcome' entries and it does not provide a"
            " count of the number of entries in the Bundle."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    total__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_total", title="Extension field for ``total``."
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title=(
            "document | message | transaction | transaction-response | batch | "
            "batch-response | history | searchset | collection"
        ),
        description="Indicates the purpose of this bundle - how it is intended to be used.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "document",
            "message",
            "transaction",
            "transaction-response",
            "batch",
            "batch-response",
            "history",
            "searchset",
            "collection",
        ],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Bundle`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "identifier",
            "type",
            "timestamp",
            "total",
            "link",
            "entry",
            "signature",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_769(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("type", "type__ext")]
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


class BundleEntry(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Entry in the bundle - will have a resource or information.
    An entry in a bundle resource - will either contain a resource or
    information about a resource (transactions and history only).
    """

    resource_type = Field("BundleEntry", const=True)

    fullUrl: fhirtypes.Uri = Field(
        None,
        alias="fullUrl",
        title="URI for resource (Absolute URL server address or URI for UUID/OID)",
        description=(
            "The Absolute URL for the resource.  The fullUrl SHALL NOT disagree "
            "with the id in the resource - i.e. if the fullUrl is not a urn:uuid, "
            "the URL shall be version-independent URL consistent with the "
            "Resource.id. The fullUrl is a version independent reference to the "
            "resource. The fullUrl element SHALL have a value except that:  * "
            "fullUrl can be empty on a POST (although it does not need to when "
            "specifying a temporary id for reference in the bundle) * Results from "
            "operations might involve resources that are not identified."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    fullUrl__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fullUrl", title="Extension field for ``fullUrl``."
    )

    link: typing.List[fhirtypes.BundleLinkType] = Field(
        None,
        alias="link",
        title="Links related to this entry",
        description="A series of links that provide context to this entry.",
        # if property is element of this resource.
        element_property=True,
    )

    request: fhirtypes.BundleEntryRequestType = Field(
        None,
        alias="request",
        title="Additional execution information (transaction/batch/history)",
        description=(
            "Additional information about how this entry should be processed as "
            "part of a transaction or batch.  For history, it shows how the entry "
            "was processed to create the version contained in the entry."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    resource: fhirtypes.ResourceType = Field(
        None,
        alias="resource",
        title="A resource in the bundle",
        description=(
            "The Resource for the entry. The purpose/meaning of the resource is "
            "determined by the Bundle.type."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    response: fhirtypes.BundleEntryResponseType = Field(
        None,
        alias="response",
        title="Results of execution (transaction/batch/history)",
        description=(
            "Indicates the results of processing the corresponding 'request' entry "
            "in the batch or transaction being responded to or what the results of "
            "an operation where when returning history."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    search: fhirtypes.BundleEntrySearchType = Field(
        None,
        alias="search",
        title="Search related information",
        description=(
            "Information about the search process that lead to the creation of this"
            " entry."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BundleEntry`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "link",
            "fullUrl",
            "resource",
            "search",
            "request",
            "response",
        ]


class BundleEntryRequest(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional execution information (transaction/batch/history).
    Additional information about how this entry should be processed as part of
    a transaction or batch.  For history, it shows how the entry was processed
    to create the version contained in the entry.
    """

    resource_type = Field("BundleEntryRequest", const=True)

    ifMatch: fhirtypes.String = Field(
        None,
        alias="ifMatch",
        title="For managing update contention",
        description=(
            "Only perform the operation if the Etag value matches. For more "
            'information, see the API section ["Managing Resource '
            'Contention"](http.html#concurrency).'
        ),
        # if property is element of this resource.
        element_property=True,
    )
    ifMatch__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_ifMatch", title="Extension field for ``ifMatch``."
    )

    ifModifiedSince: fhirtypes.Instant = Field(
        None,
        alias="ifModifiedSince",
        title="For managing cache currency",
        description=(
            "Only perform the operation if the last updated date matches. See the "
            'API documentation for ["Conditional Read"](http.html#cread).'
        ),
        # if property is element of this resource.
        element_property=True,
    )
    ifModifiedSince__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_ifModifiedSince", title="Extension field for ``ifModifiedSince``."
    )

    ifNoneExist: fhirtypes.String = Field(
        None,
        alias="ifNoneExist",
        title="For conditional creates",
        description=(
            "Instruct the server not to perform the create if a specified resource "
            "already exists. For further information, see the API documentation for"
            ' ["Conditional Create"](http.html#ccreate). This is just the query '
            'portion of the URL - what follows the "?" (not including the "?").'
        ),
        # if property is element of this resource.
        element_property=True,
    )
    ifNoneExist__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_ifNoneExist", title="Extension field for ``ifNoneExist``."
    )

    ifNoneMatch: fhirtypes.String = Field(
        None,
        alias="ifNoneMatch",
        title="For managing cache currency",
        description=(
            "If the ETag values match, return a 304 Not Modified status. See the "
            'API documentation for ["Conditional Read"](http.html#cread).'
        ),
        # if property is element of this resource.
        element_property=True,
    )
    ifNoneMatch__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_ifNoneMatch", title="Extension field for ``ifNoneMatch``."
    )

    method: fhirtypes.Code = Field(
        None,
        alias="method",
        title="GET | HEAD | POST | PUT | DELETE | PATCH",
        description=(
            "In a transaction or batch, this is the HTTP action to be executed for "
            "this entry. In a history bundle, this indicates the HTTP action that "
            "occurred."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["GET", "HEAD", "POST", "PUT", "DELETE", "PATCH"],
    )
    method__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_method", title="Extension field for ``method``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="URL for HTTP equivalent of this entry",
        description=(
            "The URL for this entry, relative to the root (the address to which the"
            " request is posted)."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BundleEntryRequest`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "method",
            "url",
            "ifNoneMatch",
            "ifModifiedSince",
            "ifMatch",
            "ifNoneExist",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2059(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("method", "method__ext"), ("url", "url__ext")]
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


class BundleEntryResponse(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Results of execution (transaction/batch/history).
    Indicates the results of processing the corresponding 'request' entry in
    the batch or transaction being responded to or what the results of an
    operation where when returning history.
    """

    resource_type = Field("BundleEntryResponse", const=True)

    etag: fhirtypes.String = Field(
        None,
        alias="etag",
        title="The Etag for the resource (if relevant)",
        description=(
            "The Etag for the resource, if the operation for the entry produced a "
            "versioned resource (see [Resource Metadata and "
            "Versioning](http.html#versioning) and [Managing Resource "
            "Contention](http.html#concurrency))."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    etag__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_etag", title="Extension field for ``etag``."
    )

    lastModified: fhirtypes.Instant = Field(
        None,
        alias="lastModified",
        title="Server's date time modified",
        description="The date/time that the resource was modified on the server.",
        # if property is element of this resource.
        element_property=True,
    )
    lastModified__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastModified", title="Extension field for ``lastModified``."
    )

    location: fhirtypes.Uri = Field(
        None,
        alias="location",
        title="The location (if the operation returns a location)",
        description=(
            "The location header created by processing this operation, populated if"
            " the operation returns a location."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    location__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_location", title="Extension field for ``location``."
    )

    outcome: fhirtypes.ResourceType = Field(
        None,
        alias="outcome",
        title="OperationOutcome with hints and warnings (for batch/transaction)",
        description=(
            "An OperationOutcome containing hints and warnings produced as part of "
            "processing this entry in a batch or transaction."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.String = Field(
        None,
        alias="status",
        title="Status response code (text optional)",
        description=(
            "The status code returned by processing this entry. The status SHALL "
            "start with a 3 digit HTTP code (e.g. 404) and may contain the standard"
            " HTTP description associated with the status code."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BundleEntryResponse`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "status",
            "location",
            "etag",
            "lastModified",
            "outcome",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2146(
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


class BundleEntrySearch(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Search related information.
    Information about the search process that lead to the creation of this
    entry.
    """

    resource_type = Field("BundleEntrySearch", const=True)

    mode: fhirtypes.Code = Field(
        None,
        alias="mode",
        title="match | include | outcome - why this is in the result set",
        description=(
            "Why this entry is in the result set - whether it's included as a match"
            " or because of an _include requirement, or to convey information or "
            "warning information about the search process."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["match", "include", "outcome"],
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_mode", title="Extension field for ``mode``."
    )

    score: fhirtypes.Decimal = Field(
        None,
        alias="score",
        title="Search ranking (between 0 and 1)",
        description="When searching, the server's search ranking score for the entry.",
        # if property is element of this resource.
        element_property=True,
    )
    score__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_score", title="Extension field for ``score``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BundleEntrySearch`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "mode", "score"]


class BundleLink(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Links related to this Bundle.
    A series of links that provide context to this bundle.
    """

    resource_type = Field("BundleLink", const=True)

    relation: fhirtypes.String = Field(
        None,
        alias="relation",
        title=(
            "See http://www.iana.org/assignments/link-relations/link-"
            "relations.xhtml#link-relations-1"
        ),
        description=(
            "A name which details the functional use for this link - see "
            "[http://www.iana.org/assignments/link-relations/link-"
            "relations.xhtml#link-"
            "relations-1](http://www.iana.org/assignments/link-relations/link-"
            "relations.xhtml#link-relations-1)."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    relation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_relation", title="Extension field for ``relation``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Reference details for the link",
        description="The reference details for the link.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BundleLink`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "relation", "url"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1173(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("relation", "relation__ext"), ("url", "url__ext")]
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
