# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ClaimResponse
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class ClaimResponse(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Remittance resource.
    This resource provides the adjudication details from the processing of a
    Claim resource.
    """

    resource_type = Field("ClaimResponse", const=True)

    addItem: typing.List[fhirtypes.ClaimResponseAddItemType] = Field(
        None,
        alias="addItem",
        title="Insurer added line items",
        description="The first tier service adjudications for payor added services.",
        # if property is element of this resource.
        element_property=True,
    )

    communicationRequest: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="communicationRequest",
        title="Request for additional information",
        description=(
            "Request for additional supporting or authorizing information, such as:"
            " documents, images or resources."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["CommunicationRequest"],
    )

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Creation date",
        description=(
            "The date when the enclosed suite of services were performed or "
            "completed."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
    )

    disposition: fhirtypes.String = Field(
        None,
        alias="disposition",
        title="Disposition Message",
        description="A description of the status of the adjudication.",
        # if property is element of this resource.
        element_property=True,
    )
    disposition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_disposition", title="Extension field for ``disposition``."
    )

    error: typing.List[fhirtypes.ClaimResponseErrorType] = Field(
        None,
        alias="error",
        title="Processing errors",
        description="Mutually exclusive with Services Provided (Item).",
        # if property is element of this resource.
        element_property=True,
    )

    form: fhirtypes.CodeableConceptType = Field(
        None,
        alias="form",
        title="Printed Form Identifier",
        description="The form to be used for printing the content.",
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Response  number",
        description="The Response business identifier.",
        # if property is element of this resource.
        element_property=True,
    )

    insurance: typing.List[fhirtypes.ClaimResponseInsuranceType] = Field(
        None,
        alias="insurance",
        title="Insurance or medical plan",
        description="Financial instrument by which payment information for health care.",
        # if property is element of this resource.
        element_property=True,
    )

    insurer: fhirtypes.ReferenceType = Field(
        None,
        alias="insurer",
        title="Insurance issuing organization",
        description="The Insurer who produced this adjudicated response.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    item: typing.List[fhirtypes.ClaimResponseItemType] = Field(
        None,
        alias="item",
        title="Line items",
        description="The first tier service adjudications for submitted services.",
        # if property is element of this resource.
        element_property=True,
    )

    outcome: fhirtypes.CodeableConceptType = Field(
        None,
        alias="outcome",
        title="complete | error | partial",
        description="Processing outcome errror, partial or complete processing.",
        # if property is element of this resource.
        element_property=True,
    )

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="The subject of the Products and Services",
        description="Patient Resource.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    payeeType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="payeeType",
        title="Party to be paid any benefits payable",
        description="Party to be reimbursed: Subscriber, provider, other.",
        # if property is element of this resource.
        element_property=True,
    )

    payment: fhirtypes.ClaimResponsePaymentType = Field(
        None,
        alias="payment",
        title="Payment details, if paid",
        description="Payment details for the claim if the claim has been paid.",
        # if property is element of this resource.
        element_property=True,
    )

    processNote: typing.List[fhirtypes.ClaimResponseProcessNoteType] = Field(
        None,
        alias="processNote",
        title="Processing notes",
        description="Note text.",
        # if property is element of this resource.
        element_property=True,
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title="Id of resource triggering adjudication",
        description="Original request resource referrence.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Claim"],
    )

    requestOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="requestOrganization",
        title="Responsible organization",
        description=(
            "The organization which is responsible for the services rendered to the"
            " patient."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    requestProvider: fhirtypes.ReferenceType = Field(
        None,
        alias="requestProvider",
        title="Responsible practitioner",
        description=(
            "The practitioner who is responsible for the services rendered to the "
            "patient."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    reserved: fhirtypes.CodingType = Field(
        None,
        alias="reserved",
        title="Funds reserved status",
        description="Status of funds reservation (For provider, for Patient, None).",
        # if property is element of this resource.
        element_property=True,
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

    totalBenefit: fhirtypes.MoneyType = Field(
        None,
        alias="totalBenefit",
        title="Total benefit payable for the Claim",
        description=(
            "Total amount of benefit payable (Equal to sum of the Benefit amounts "
            "from all detail lines and additions less the Unallocated Deductible)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    totalCost: fhirtypes.MoneyType = Field(
        None,
        alias="totalCost",
        title="Total Cost of service from the Claim",
        description="The total cost of the services reported.",
        # if property is element of this resource.
        element_property=True,
    )

    unallocDeductable: fhirtypes.MoneyType = Field(
        None,
        alias="unallocDeductable",
        title="Unallocated deductible",
        description=(
            "The amount of deductible applied which was not allocated to any "
            "particular service line."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponse`` according specification,
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
            "patient",
            "created",
            "insurer",
            "requestProvider",
            "requestOrganization",
            "request",
            "outcome",
            "disposition",
            "payeeType",
            "item",
            "addItem",
            "error",
            "totalCost",
            "unallocDeductable",
            "totalBenefit",
            "payment",
            "reserved",
            "form",
            "processNote",
            "communicationRequest",
            "insurance",
        ]


class ClaimResponseAddItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Insurer added line items.
    The first tier service adjudications for payor added services.
    """

    resource_type = Field("ClaimResponseAddItem", const=True)

    adjudication: typing.List[fhirtypes.ClaimResponseItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title="Added items adjudication",
        description="The adjudications results.",
        # if property is element of this resource.
        element_property=True,
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type of service or product",
        description=(
            "Health Care Service Type Codes  to identify the classification of "
            "service or benefits."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    detail: typing.List[fhirtypes.ClaimResponseAddItemDetailType] = Field(
        None,
        alias="detail",
        title="Added items details",
        description="The second tier service adjudications for payor added services.",
        # if property is element of this resource.
        element_property=True,
    )

    fee: fhirtypes.MoneyType = Field(
        None,
        alias="fee",
        title="Professional fee or Product charge",
        description="The fee charged for the professional service or product..",
        # if property is element of this resource.
        element_property=True,
    )

    modifier: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="modifier",
        title="Service/Product billing modifiers",
        description=(
            "Item typification or modifiers codes, eg for Oral whether the "
            "treatment is cosmetic or associated with TMJ, or for medical whether "
            "the treatment was outside the clinic or out of office hours."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    noteNumber: typing.List[fhirtypes.PositiveInt] = Field(
        None,
        alias="noteNumber",
        title="List of note numbers which apply",
        description="A list of note references to the notes provided below.",
        # if property is element of this resource.
        element_property=True,
    )
    noteNumber__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_noteNumber", title="Extension field for ``noteNumber``.")

    revenue: fhirtypes.CodeableConceptType = Field(
        None,
        alias="revenue",
        title="Revenue or cost center code",
        description=(
            "The type of reveneu or cost center providing the product and/or "
            "service."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    sequenceLinkId: typing.List[fhirtypes.PositiveInt] = Field(
        None,
        alias="sequenceLinkId",
        title="Service instances",
        description=(
            "List of input service items which this service line is intended to "
            "replace."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    sequenceLinkId__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_sequenceLinkId", title="Extension field for ``sequenceLinkId``."
    )

    service: fhirtypes.CodeableConceptType = Field(
        None,
        alias="service",
        title="Group, Service or Product",
        description="A code to indicate the Professional Service or Product supplied.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseAddItem`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequenceLinkId",
            "revenue",
            "category",
            "service",
            "modifier",
            "fee",
            "noteNumber",
            "adjudication",
            "detail",
        ]


class ClaimResponseAddItemDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Added items details.
    The second tier service adjudications for payor added services.
    """

    resource_type = Field("ClaimResponseAddItemDetail", const=True)

    adjudication: typing.List[fhirtypes.ClaimResponseItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title="Added items detail adjudication",
        description="The adjudications results.",
        # if property is element of this resource.
        element_property=True,
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type of service or product",
        description=(
            "Health Care Service Type Codes  to identify the classification of "
            "service or benefits."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    fee: fhirtypes.MoneyType = Field(
        None,
        alias="fee",
        title="Professional fee or Product charge",
        description="The fee charged for the professional service or product..",
        # if property is element of this resource.
        element_property=True,
    )

    modifier: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="modifier",
        title="Service/Product billing modifiers",
        description=(
            "Item typification or modifiers codes, eg for Oral whether the "
            "treatment is cosmetic or associated with TMJ, or for medical whether "
            "the treatment was outside the clinic or out of office hours."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    noteNumber: typing.List[fhirtypes.PositiveInt] = Field(
        None,
        alias="noteNumber",
        title="List of note numbers which apply",
        description="A list of note references to the notes provided below.",
        # if property is element of this resource.
        element_property=True,
    )
    noteNumber__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_noteNumber", title="Extension field for ``noteNumber``.")

    revenue: fhirtypes.CodeableConceptType = Field(
        None,
        alias="revenue",
        title="Revenue or cost center code",
        description=(
            "The type of reveneu or cost center providing the product and/or "
            "service."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    service: fhirtypes.CodeableConceptType = Field(
        None,
        alias="service",
        title="Service or Product",
        description="A code to indicate the Professional Service or Product supplied.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseAddItemDetail`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "revenue",
            "category",
            "service",
            "modifier",
            "fee",
            "noteNumber",
            "adjudication",
        ]


class ClaimResponseError(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Processing errors.
    Mutually exclusive with Services Provided (Item).
    """

    resource_type = Field("ClaimResponseError", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Error code detailing processing issues",
        description=(
            "An error code,from a specified code system, which details why the "
            "claim could not be adjudicated."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    detailSequenceLinkId: fhirtypes.PositiveInt = Field(
        None,
        alias="detailSequenceLinkId",
        title="Detail sequence number",
        description=(
            "The sequence number of the addition within the line item submitted "
            "which contains the error. This value is omitted when the error is not "
            "related to an Addition."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    detailSequenceLinkId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_detailSequenceLinkId",
        title="Extension field for ``detailSequenceLinkId``.",
    )

    sequenceLinkId: fhirtypes.PositiveInt = Field(
        None,
        alias="sequenceLinkId",
        title="Item sequence number",
        description=(
            "The sequence number of the line item submitted which contains the "
            "error. This value is omitted when the error is elsewhere."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    sequenceLinkId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequenceLinkId", title="Extension field for ``sequenceLinkId``."
    )

    subdetailSequenceLinkId: fhirtypes.PositiveInt = Field(
        None,
        alias="subdetailSequenceLinkId",
        title="Subdetail sequence number",
        description=(
            "The sequence number of the addition within the line item submitted "
            "which contains the error. This value is omitted when the error is not "
            "related to an Addition."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    subdetailSequenceLinkId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_subdetailSequenceLinkId",
        title="Extension field for ``subdetailSequenceLinkId``.",
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseError`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequenceLinkId",
            "detailSequenceLinkId",
            "subdetailSequenceLinkId",
            "code",
        ]


class ClaimResponseInsurance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Insurance or medical plan.
    Financial instrument by which payment information for health care.
    """

    resource_type = Field("ClaimResponseInsurance", const=True)

    businessArrangement: fhirtypes.String = Field(
        None,
        alias="businessArrangement",
        title="Business agreement",
        description=(
            "The contract number of a business agreement which describes the terms "
            "and conditions."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    businessArrangement__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_businessArrangement",
        title="Extension field for ``businessArrangement``.",
    )

    claimResponse: fhirtypes.ReferenceType = Field(
        None,
        alias="claimResponse",
        title="Adjudication results",
        description="The Coverages adjudication details.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ClaimResponse"],
    )

    coverage: fhirtypes.ReferenceType = Field(
        ...,
        alias="coverage",
        title="Insurance information",
        description="Reference to the program or plan identification, underwriter or payor.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Coverage"],
    )

    focal: bool = Field(
        None,
        alias="focal",
        title="Is the focal Coverage",
        description=(
            "The instance number of the Coverage which is the focus for "
            "adjudication. The Coverage against which the claim is to be "
            "adjudicated."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    focal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_focal", title="Extension field for ``focal``."
    )

    preAuthRef: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="preAuthRef",
        title="Pre-Authorization/Determination Reference",
        description="A list of references from the Insurer to which these services pertain.",
        # if property is element of this resource.
        element_property=True,
    )
    preAuthRef__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_preAuthRef", title="Extension field for ``preAuthRef``.")

    sequence: fhirtypes.PositiveInt = Field(
        None,
        alias="sequence",
        title="Service instance identifier",
        description="A service line item.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseInsurance`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "focal",
            "coverage",
            "businessArrangement",
            "preAuthRef",
            "claimResponse",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2437(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("focal", "focal__ext"), ("sequence", "sequence__ext")]
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


class ClaimResponseItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Line items.
    The first tier service adjudications for submitted services.
    """

    resource_type = Field("ClaimResponseItem", const=True)

    adjudication: typing.List[fhirtypes.ClaimResponseItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title="Adjudication details",
        description="The adjudication results.",
        # if property is element of this resource.
        element_property=True,
    )

    detail: typing.List[fhirtypes.ClaimResponseItemDetailType] = Field(
        None,
        alias="detail",
        title="Detail line items",
        description="The second tier service adjudications for submitted services.",
        # if property is element of this resource.
        element_property=True,
    )

    noteNumber: typing.List[fhirtypes.PositiveInt] = Field(
        None,
        alias="noteNumber",
        title="List of note numbers which apply",
        description="A list of note references to the notes provided below.",
        # if property is element of this resource.
        element_property=True,
    )
    noteNumber__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_noteNumber", title="Extension field for ``noteNumber``.")

    sequenceLinkId: fhirtypes.PositiveInt = Field(
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
        ``ClaimResponseItem`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequenceLinkId",
            "noteNumber",
            "adjudication",
            "detail",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1908(
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


class ClaimResponseItemAdjudication(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Adjudication details.
    The adjudication results.
    """

    resource_type = Field("ClaimResponseItemAdjudication", const=True)

    amount: fhirtypes.MoneyType = Field(
        None,
        alias="amount",
        title="Monetary amount",
        description="Monetary amount associated with the code.",
        # if property is element of this resource.
        element_property=True,
    )

    category: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="category",
        title="Adjudication category such as co-pay, eligible, benefit, etc.",
        description="Code indicating: Co-Pay, deductible, eligible, benefit, tax, etc.",
        # if property is element of this resource.
        element_property=True,
    )

    reason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reason",
        title="Explanation of Adjudication outcome",
        description="Adjudication reason such as limit reached.",
        # if property is element of this resource.
        element_property=True,
    )

    value: fhirtypes.Decimal = Field(
        None,
        alias="value",
        title="Non-monetary value",
        description=(
            "A non-monetary value for example a percentage. Mutually exclusive to "
            "the amount element above."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseItemAdjudication`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "category",
            "reason",
            "amount",
            "value",
        ]


class ClaimResponseItemDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Detail line items.
    The second tier service adjudications for submitted services.
    """

    resource_type = Field("ClaimResponseItemDetail", const=True)

    adjudication: typing.List[fhirtypes.ClaimResponseItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title="Detail level adjudication details",
        description="The adjudications results.",
        # if property is element of this resource.
        element_property=True,
    )

    noteNumber: typing.List[fhirtypes.PositiveInt] = Field(
        None,
        alias="noteNumber",
        title="List of note numbers which apply",
        description="A list of note references to the notes provided below.",
        # if property is element of this resource.
        element_property=True,
    )
    noteNumber__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_noteNumber", title="Extension field for ``noteNumber``.")

    sequenceLinkId: fhirtypes.PositiveInt = Field(
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

    subDetail: typing.List[fhirtypes.ClaimResponseItemDetailSubDetailType] = Field(
        None,
        alias="subDetail",
        title="Subdetail line items",
        description="The third tier service adjudications for submitted services.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseItemDetail`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequenceLinkId",
            "noteNumber",
            "adjudication",
            "subDetail",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2502(
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


class ClaimResponseItemDetailSubDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Subdetail line items.
    The third tier service adjudications for submitted services.
    """

    resource_type = Field("ClaimResponseItemDetailSubDetail", const=True)

    adjudication: typing.List[fhirtypes.ClaimResponseItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title="Subdetail level adjudication details",
        description="The adjudications results.",
        # if property is element of this resource.
        element_property=True,
    )

    noteNumber: typing.List[fhirtypes.PositiveInt] = Field(
        None,
        alias="noteNumber",
        title="List of note numbers which apply",
        description="A list of note references to the notes provided below.",
        # if property is element of this resource.
        element_property=True,
    )
    noteNumber__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_noteNumber", title="Extension field for ``noteNumber``.")

    sequenceLinkId: fhirtypes.PositiveInt = Field(
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
        ``ClaimResponseItemDetailSubDetail`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequenceLinkId",
            "noteNumber",
            "adjudication",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3395(
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


class ClaimResponsePayment(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Payment details, if paid.
    Payment details for the claim if the claim has been paid.
    """

    resource_type = Field("ClaimResponsePayment", const=True)

    adjustment: fhirtypes.MoneyType = Field(
        None,
        alias="adjustment",
        title="Payment adjustment for non-Claim issues",
        description=(
            "Adjustment to the payment of this transaction which is not related to "
            "adjudication of this transaction."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    adjustmentReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="adjustmentReason",
        title="Explanation for the non-claim adjustment",
        description="Reason for the payment adjustment.",
        # if property is element of this resource.
        element_property=True,
    )

    amount: fhirtypes.MoneyType = Field(
        None,
        alias="amount",
        title="Payable amount after adjustment",
        description="Payable less any payment adjustment.",
        # if property is element of this resource.
        element_property=True,
    )

    date: fhirtypes.Date = Field(
        None,
        alias="date",
        title="Expected data of Payment",
        description="Estimated payment data.",
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Identifier of the payment instrument",
        description="Payment identifier.",
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Partial or Complete",
        description="Whether this represents partial or complete payment of the claim.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponsePayment`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "adjustment",
            "adjustmentReason",
            "date",
            "amount",
            "identifier",
        ]


class ClaimResponseProcessNote(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Processing notes.
    Note text.
    """

    resource_type = Field("ClaimResponseProcessNote", const=True)

    language: fhirtypes.CodeableConceptType = Field(
        None,
        alias="language",
        title="Language if different from the resource",
        description=(
            "The ISO-639-1 alpha 2 code in lower case for the language, optionally "
            "followed by a hyphen and the ISO-3166-1 alpha 2 code for the region in"
            ' upper case; e.g. "en" for English, or "en-US" for American English '
            'versus "en-EN" for England English.'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    number: fhirtypes.PositiveInt = Field(
        None,
        alias="number",
        title="Sequence Number for this note",
        description=(
            "An integer associated with each note which may be referred to from "
            "each service line item."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    number__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_number", title="Extension field for ``number``."
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Note explanatory text",
        description="The note text.",
        # if property is element of this resource.
        element_property=True,
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="display | print | printoper",
        description="The note purpose: Print/Display.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseProcessNote`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "number",
            "type",
            "text",
            "language",
        ]
