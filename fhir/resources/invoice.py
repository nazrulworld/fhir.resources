# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Invoice
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


class Invoice(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Invoice containing ChargeItems from an Account.
    Invoice containing collected ChargeItems from an Account with calculated
    individual and total price for Billing purpose.
    """

    resource_type = Field("Invoice", const=True)

    account: fhirtypes.ReferenceType = Field(
        None,
        alias="account",
        title="Account that is being balanced",
        description="Account which is supposed to be balanced with this Invoice.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Account"],
    )

    cancelledReason: fhirtypes.String = Field(
        None,
        alias="cancelledReason",
        title="Reason for cancellation of this Invoice",
        description=(
            "In case of Invoice cancellation a reason must be given (entered in "
            "error, superseded by corrected invoice etc.)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    cancelledReason__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_cancelledReason", title="Extension field for ``cancelledReason``."
    )

    creation: fhirtypes.DateTime = Field(
        None,
        alias="creation",
        title="When posted",
        description="Date/time(s) of when this Invoice was posted.",
        # if property is element of this resource.
        element_property=True,
    )
    creation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_creation", title="Extension field for ``creation``."
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="DEPRICATED",
        description="Depricared by the element below.",
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier for item",
        description=(
            "Identifier of this Invoice, often used for reference in correspondence"
            " about this invoice or for tracking of payments."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    issuer: fhirtypes.ReferenceType = Field(
        None,
        alias="issuer",
        title="Issuing Organization of Invoice",
        description="The organizationissuing the Invoice.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    lineItem: typing.List[fhirtypes.InvoiceLineItemType] = Field(
        None,
        alias="lineItem",
        title="Line items of this Invoice",
        description=(
            "Each line item represents one charge for goods and services rendered. "
            "Details such.ofType(date), code and amount are found in the referenced"
            " ChargeItem resource."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Comments made about the invoice",
        description=(
            "Comments made about the invoice by the issuer, subject, or other "
            "participants."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    participant: typing.List[fhirtypes.InvoiceParticipantType] = Field(
        None,
        alias="participant",
        title="Participant in creation of this Invoice",
        description=(
            "Indicates who or what performed or participated in the charged " "service."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    paymentTerms: fhirtypes.Markdown = Field(
        None,
        alias="paymentTerms",
        title="Payment details",
        description=(
            "Payment details such as banking details, period of payment, "
            "deductibles, methods of payment."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    paymentTerms__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_paymentTerms", title="Extension field for ``paymentTerms``."
    )

    periodDate: fhirtypes.Date = Field(
        None,
        alias="periodDate",
        title="Billing date or period",
        description="Date/time(s) range of services included in this invoice.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e period[x]
        one_of_many="period",
        one_of_many_required=False,
    )
    periodDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_periodDate", title="Extension field for ``periodDate``."
    )

    periodPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="periodPeriod",
        title="Billing date or period",
        description="Date/time(s) range of services included in this invoice.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e period[x]
        one_of_many="period",
        one_of_many_required=False,
    )

    recipient: fhirtypes.ReferenceType = Field(
        None,
        alias="recipient",
        title="Recipient of this invoice",
        description=(
            "The individual or Organization responsible for balancing of this "
            "invoice."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization", "Patient", "RelatedPerson"],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | issued | balanced | cancelled | entered-in-error",
        description="The current state of the Invoice.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "issued", "balanced", "cancelled", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Recipient(s) of goods and services",
        description=(
            "The individual or set of individuals receiving the goods and services "
            "billed in this invoice."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group"],
    )

    totalGross: fhirtypes.MoneyType = Field(
        None,
        alias="totalGross",
        title="Gross total of this Invoice",
        description="Invoice total, tax included.",
        # if property is element of this resource.
        element_property=True,
    )

    totalNet: fhirtypes.MoneyType = Field(
        None,
        alias="totalNet",
        title="Net total of this Invoice",
        description="Invoice total , taxes excluded.",
        # if property is element of this resource.
        element_property=True,
    )

    totalPriceComponent: typing.List[fhirtypes.MonetaryComponentType] = Field(
        None,
        alias="totalPriceComponent",
        title="Components of Invoice total",
        description=(
            "The total amount for the Invoice may be calculated as the sum of the "
            "line items with surcharges/deductions that apply in certain "
            "conditions.  The priceComponent element can be used to offer "
            "transparency to the recipient of the Invoice of how the total price "
            "was calculated."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type of Invoice",
        description=(
            "Type of Invoice depending on domain, realm an usage (e.g. "
            "internal/external, dental, preliminary)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Invoice`` according specification,
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
            "cancelledReason",
            "type",
            "subject",
            "recipient",
            "date",
            "creation",
            "periodDate",
            "periodPeriod",
            "participant",
            "issuer",
            "account",
            "lineItem",
            "totalPriceComponent",
            "totalNet",
            "totalGross",
            "paymentTerms",
            "note",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_891(
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
    def validate_one_of_many_891(
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
        one_of_many_fields = {"period": ["periodDate", "periodPeriod"]}
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


class InvoiceLineItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Line items of this Invoice.
    Each line item represents one charge for goods and services rendered.
    Details such.ofType(date), code and amount are found in the referenced
    ChargeItem resource.
    """

    resource_type = Field("InvoiceLineItem", const=True)

    chargeItemCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="chargeItemCodeableConcept",
        title=(
            "Reference to ChargeItem containing details of this line item or an "
            "inline billing code"
        ),
        description=(
            "The ChargeItem contains information such as the billing code, date, "
            "amount etc. If no further details are required for the lineItem, "
            "inline billing codes can be added using the CodeableConcept data type "
            "instead of the Reference."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e chargeItem[x]
        one_of_many="chargeItem",
        one_of_many_required=True,
    )

    chargeItemReference: fhirtypes.ReferenceType = Field(
        None,
        alias="chargeItemReference",
        title=(
            "Reference to ChargeItem containing details of this line item or an "
            "inline billing code"
        ),
        description=(
            "The ChargeItem contains information such as the billing code, date, "
            "amount etc. If no further details are required for the lineItem, "
            "inline billing codes can be added using the CodeableConcept data type "
            "instead of the Reference."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e chargeItem[x]
        one_of_many="chargeItem",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ChargeItem"],
    )

    priceComponent: typing.List[fhirtypes.MonetaryComponentType] = Field(
        None,
        alias="priceComponent",
        title="Components of total line item price",
        description=(
            "The price for a ChargeItem may be calculated as a base price with "
            "surcharges/deductions that apply in certain conditions. A "
            "ChargeItemDefinition resource that defines the prices, factors and "
            "conditions that apply to a billing code is currently under "
            "development. The priceComponent element can be used to offer "
            "transparency to the recipient of the Invoice as to how the prices have"
            " been calculated."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    sequence: fhirtypes.PositiveInt = Field(
        None,
        alias="sequence",
        title="Sequence number of line item",
        description="Sequence in which the items appear on the invoice.",
        # if property is element of this resource.
        element_property=True,
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    servicedDate: fhirtypes.Date = Field(
        None,
        alias="servicedDate",
        title="Service data or period",
        description="Date/time(s) range when this service was delivered or completed.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e serviced[x]
        one_of_many="serviced",
        one_of_many_required=False,
    )
    servicedDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_servicedDate", title="Extension field for ``servicedDate``."
    )

    servicedPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="servicedPeriod",
        title="Service data or period",
        description="Date/time(s) range when this service was delivered or completed.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e serviced[x]
        one_of_many="serviced",
        one_of_many_required=False,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``InvoiceLineItem`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "servicedDate",
            "servicedPeriod",
            "chargeItemReference",
            "chargeItemCodeableConcept",
            "priceComponent",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1690(
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
            "chargeItem": ["chargeItemCodeableConcept", "chargeItemReference"],
            "serviced": ["servicedDate", "servicedPeriod"],
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


class InvoiceParticipant(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Participant in creation of this Invoice.
    Indicates who or what performed or participated in the charged service.
    """

    resource_type = Field("InvoiceParticipant", const=True)

    actor: fhirtypes.ReferenceType = Field(
        ...,
        alias="actor",
        title="Individual who was involved",
        description=(
            "The device, practitioner, etc. who performed or participated in the "
            "service."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "Organization",
            "Patient",
            "PractitionerRole",
            "Device",
            "RelatedPerson",
        ],
    )

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="Type of involvement in creation of this Invoice",
        description=(
            "Describes the type of involvement (e.g. transcriptionist, creator "
            "etc.). If the invoice has been created automatically, the Participant "
            "may be a billing engine or another kind of device."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``InvoiceParticipant`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "role", "actor"]
