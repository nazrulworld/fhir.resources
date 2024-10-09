from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/BiologicallyDerivedProductDispense
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class BiologicallyDerivedProductDispense(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A record of dispensation of a biologically derived product.
    This resource reflects an instance of a biologically derived product
    dispense. The supply or dispense of a biologically derived product from the
    supply organization or department (e.g. hospital transfusion laboratory) to
    the clinical team responsible for clinical application.
    """

    __resource_type__ = "BiologicallyDerivedProductDispense"

    basedOn: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="basedOn",
        title="The order or request that this dispense is fulfilling",
        description=(
            "The order or request that the dispense is fulfilling. This is a "
            "reference to a ServiceRequest resource."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ServiceRequest"],
        },
    )

    destination: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="destination",
        title="Where the product was dispatched to",
        description=(
            "Link to a resource identifying the physical location that the product "
            "was dispatched to."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business identifier for this dispense",
        description=(
            "Unique instance identifiers assigned to a biologically derived product"
            " dispense. Note: This is a business identifier, not a resource "
            "identifier."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    location: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="location",
        title="Where the dispense occurred",
        description="The physical location where the dispense was performed.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    matchStatus: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="matchStatus",
        title="Indicates the type of matching associated with the dispense",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="note",
        title="Additional notes",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    originRelationshipType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="originRelationshipType",
        title="Relationship between the donor and intended recipient",
        description=(
            "Indicates the relationship between the donor of the biologically "
            "derived product and the intended recipient."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    partOf: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="partOf",
        title="Short description",
        description="A larger event of which this particular event is a component.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["BiologicallyDerivedProductDispense"],
        },
    )

    patient: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="patient",
        title="The intended recipient of the dispensed product",
        description=(
            "A link to a resource representing the patient that the product is "
            "dispensed for."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient"],
        },
    )

    performer: typing.List[fhirtypes.BiologicallyDerivedProductDispensePerformerType] | None = Field(  # type: ignore
        None,
        alias="performer",
        title="Indicates who or what performed an action",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    preparedDate: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="preparedDate",
        title="When product was selected/matched",
        description="When the product was selected/ matched.",
        json_schema_extra={
            "element_property": True,
        },
    )
    preparedDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_preparedDate", title="Extension field for ``preparedDate``."
    )

    product: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="product",
        title="The BiologicallyDerivedProduct that is dispensed",
        description=(
            "A link to a resource identifying the biologically derived product that"
            " is being dispensed."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["BiologicallyDerivedProduct"],
        },
    )

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="Amount dispensed",
        description=(
            "The amount of product in the dispense. Quantity will depend on the "
            "product being dispensed. Examples are: volume; cell count; "
            "concentration."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title=(
            "preparation | in-progress | allocated | issued | unfulfilled | "
            "returned | entered-in-error | unknown"
        ),
        description="A code specifying the state of the dispense event.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "preparation",
                "in-progress",
                "allocated",
                "issued",
                "unfulfilled",
                "returned",
                "entered-in-error",
                "unknown",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    usageInstruction: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="usageInstruction",
        title="Specific instructions for use",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    usageInstruction__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_usageInstruction",
        title="Extension field for ``usageInstruction``.",
    )

    whenHandedOver: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="whenHandedOver",
        title="When the product was dispatched",
        description="When the product was dispatched for clinical use.",
        json_schema_extra={
            "element_property": True,
        },
    )
    whenHandedOver__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_whenHandedOver", title="Extension field for ``whenHandedOver``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BiologicallyDerivedProductDispense`` according specification,
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
            "basedOn",
            "partOf",
            "status",
            "originRelationshipType",
            "product",
            "patient",
            "matchStatus",
            "performer",
            "location",
            "quantity",
            "preparedDate",
            "whenHandedOver",
            "destination",
            "note",
            "usageInstruction",
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


class BiologicallyDerivedProductDispensePerformer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Indicates who or what performed an action.
    """

    __resource_type__ = "BiologicallyDerivedProductDispensePerformer"

    actor: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="actor",
        title="Who performed the action",
        description="Identifies the person responsible for the action.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner"],
        },
    )

    function: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="function",
        title="Identifies the function of the performer during the dispense",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BiologicallyDerivedProductDispensePerformer`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "function", "actor"]
