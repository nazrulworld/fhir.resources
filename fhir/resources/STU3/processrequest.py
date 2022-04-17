# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ProcessRequest
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


class ProcessRequest(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Request to perform some action on or in regards to an existing resource.
    This resource provides the target, request and response, and action details
    for an action to be performed by the target on or about existing resources.
    """

    resource_type = Field("ProcessRequest", const=True)

    action: fhirtypes.Code = Field(
        None,
        alias="action",
        title="cancel | poll | reprocess | status",
        description=(
            "The type of processing action being requested, for example Reversal, "
            "Readjudication, StatusRequest,PendedRequest."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["cancel", "poll", "reprocess", "status"],
    )
    action__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_action", title="Extension field for ``action``."
    )

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Creation date",
        description="The date when this resource was created.",
        # if property is element of this resource.
        element_property=True,
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
    )

    exclude: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="exclude",
        title="Resource type(s) to exclude",
        description="Names of resource types to exclude.",
        # if property is element of this resource.
        element_property=True,
    )
    exclude__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_exclude", title="Extension field for ``exclude``.")

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier",
        description="The ProcessRequest business identifier.",
        # if property is element of this resource.
        element_property=True,
    )

    include: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="include",
        title="Resource type(s) to include",
        description="Names of resource types to include.",
        # if property is element of this resource.
        element_property=True,
    )
    include__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_include", title="Extension field for ``include``.")

    item: typing.List[fhirtypes.ProcessRequestItemType] = Field(
        None,
        alias="item",
        title="Items to re-adjudicate",
        description=(
            "List of top level items to be re-adjudicated, if none specified then "
            "the entire submission is re-adjudicated."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    nullify: bool = Field(
        None,
        alias="nullify",
        title="Remove history",
        description="If true remove all history excluding audit.",
        # if property is element of this resource.
        element_property=True,
    )
    nullify__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_nullify", title="Extension field for ``nullify``."
    )

    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title="Responsible organization",
        description=(
            "The organization which is responsible for the action speccified in "
            "this request."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Selection period",
        description=(
            "A period of time during which the fulfilling resources would have been"
            " created."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    provider: fhirtypes.ReferenceType = Field(
        None,
        alias="provider",
        title="Responsible practitioner",
        description=(
            "The practitioner who is responsible for the action specified in this "
            "request."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    reference: fhirtypes.String = Field(
        None,
        alias="reference",
        title="Reference number/string",
        description="A reference to supply which authenticates the process.",
        # if property is element of this resource.
        element_property=True,
    )
    reference__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_reference", title="Extension field for ``reference``."
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title="Reference to the Request resource",
        description="Reference of resource which is the target or subject of this action.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    response: fhirtypes.ReferenceType = Field(
        None,
        alias="response",
        title="Reference to the Response resource",
        description=(
            "Reference of a prior response to resource which is the target or "
            "subject of this action."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="active | cancelled | draft | entered-in-error",
        description="The status of the resource instance.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "cancelled", "draft", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    target: fhirtypes.ReferenceType = Field(
        None,
        alias="target",
        title="Party which is the target of the request",
        description="The organization which is the target of the request.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
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

    resource_type = Field("ProcessRequestItem", const=True)

    sequenceLinkId: fhirtypes.Integer = Field(
        None,
        alias="sequenceLinkId",
        title="Service instance",
        description="A service line number.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    sequenceLinkId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequenceLinkId", title="Extension field for ``sequenceLinkId``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ProcessRequestItem`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "sequenceLinkId"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2068(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sequenceLinkId", "sequenceLinkId__ext")]
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
