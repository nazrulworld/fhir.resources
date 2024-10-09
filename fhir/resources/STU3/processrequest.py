from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ProcessRequest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ProcessRequest(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Request to perform some action on or in regards to an existing resource.
    This resource provides the target, request and response, and action details
    for an action to be performed by the target on or about existing resources.
    """

    __resource_type__ = "ProcessRequest"

    action: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="action",
        title="cancel | poll | reprocess | status",
        description=(
            "The type of processing action being requested, for example Reversal, "
            "Readjudication, StatusRequest,PendedRequest."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["cancel", "poll", "reprocess", "status"],
        },
    )
    action__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_action", title="Extension field for ``action``."
    )

    created: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="created",
        title="Creation date",
        description="The date when this resource was created.",
        json_schema_extra={
            "element_property": True,
        },
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_created", title="Extension field for ``created``."
    )

    exclude: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="exclude",
        title="Resource type(s) to exclude",
        description="Names of resource types to exclude.",
        json_schema_extra={
            "element_property": True,
        },
    )
    exclude__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_exclude", title="Extension field for ``exclude``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business Identifier",
        description="The ProcessRequest business identifier.",
        json_schema_extra={
            "element_property": True,
        },
    )

    include: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="include",
        title="Resource type(s) to include",
        description="Names of resource types to include.",
        json_schema_extra={
            "element_property": True,
        },
    )
    include__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_include", title="Extension field for ``include``."
    )

    item: typing.List[fhirtypes.ProcessRequestItemType] | None = Field(  # type: ignore
        None,
        alias="item",
        title="Items to re-adjudicate",
        description=(
            "List of top level items to be re-adjudicated, if none specified then "
            "the entire submission is re-adjudicated."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    nullify: bool | None = Field(  # type: ignore
        None,
        alias="nullify",
        title="Remove history",
        description="If true remove all history excluding audit.",
        json_schema_extra={
            "element_property": True,
        },
    )
    nullify__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_nullify", title="Extension field for ``nullify``."
    )

    organization: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="organization",
        title="Responsible organization",
        description=(
            "The organization which is responsible for the action speccified in "
            "this request."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="period",
        title="Selection period",
        description=(
            "A period of time during which the fulfilling resources would have been"
            " created."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    provider: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="provider",
        title="Responsible practitioner",
        description=(
            "The practitioner who is responsible for the action specified in this "
            "request."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner"],
        },
    )

    reference: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="reference",
        title="Reference number/string",
        description="A reference to supply which authenticates the process.",
        json_schema_extra={
            "element_property": True,
        },
    )
    reference__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_reference", title="Extension field for ``reference``."
    )

    request: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="request",
        title="Reference to the Request resource",
        description="Reference of resource which is the target or subject of this action.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    response: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="response",
        title="Reference to the Response resource",
        description=(
            "Reference of a prior response to resource which is the target or "
            "subject of this action."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="active | cancelled | draft | entered-in-error",
        description="The status of the resource instance.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["active", "cancelled", "draft", "entered-in-error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    target: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="target",
        title="Party which is the target of the request",
        description="The organization which is the target of the request.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ProcessRequest`` according specification,
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
            "action",
            "target",
            "created",
            "provider",
            "organization",
            "request",
            "response",
            "nullify",
            "reference",
            "item",
            "include",
            "exclude",
            "period",
        ]


class ProcessRequestItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Items to re-adjudicate.
    List of top level items to be re-adjudicated, if none specified then the
    entire submission is re-adjudicated.
    """

    __resource_type__ = "ProcessRequestItem"

    sequenceLinkId: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="sequenceLinkId",
        title="Service instance",
        description="A service line number.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    sequenceLinkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sequenceLinkId", title="Extension field for ``sequenceLinkId``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ProcessRequestItem`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "sequenceLinkId"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sequenceLinkId", "sequenceLinkId__ext")]
        return required_fields
