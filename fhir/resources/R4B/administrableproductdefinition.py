from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/AdministrableProductDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class AdministrableProductDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A medicinal product in the final form, suitable for administration - after
    any mixing of multiple components.
    A medicinal product in the final form which is suitable for administering
    to a patient (after any mixing of multiple components, dissolution etc. has
    been performed).
    """

    __resource_type__ = "AdministrableProductDefinition"

    administrableDoseForm: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="administrableDoseForm",
        title=(
            "The dose form of the final product after necessary reconstitution or "
            "processing"
        ),
        description=(
            "The dose form of the final product after necessary reconstitution or "
            "processing. Contrasts to the manufactured dose form (see "
            "ManufacturedItemDefinition). If the manufactured form was 'powder for "
            "solution for injection', the administrable dose form could be "
            "'solution for injection' (once mixed with another item having "
            "manufactured form 'solvent for solution for injection')."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    device: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="device",
        title=(
            "A device that is integral to the medicinal product, in effect being "
            'considered as an "ingredient" of the medicinal product'
        ),
        description=(
            "A device that is integral to the medicinal product, in effect being "
            'considered as an "ingredient" of the medicinal product. This is not '
            "intended for devices that are just co-packaged."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DeviceDefinition"],
        },
    )

    formOf: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="formOf",
        title=(
            "References a product from which one or more of the constituent parts "
            "of that product can be prepared and used as described by this "
            "administrable product"
        ),
        description=(
            "References a product from which one or more of the constituent parts "
            "of that product can be prepared and used as described by this "
            "administrable product.  If this administrable product describes the "
            "administration of a crushed tablet, the 'formOf' would be the product "
            "representing a distribution containing tablets and possibly also a "
            "cream.  This is distinct from the 'producedFrom' which refers to the "
            "specific components of the product that are used in this preparation, "
            "rather than the product as a whole."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["MedicinalProductDefinition"],
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        default=None,
        alias="identifier",
        title="An identifier for the administrable product",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    ingredient: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="ingredient",
        title=(
            "The ingredients of this administrable medicinal product. This is only "
            "needed if the ingredients are not specified either using "
            "ManufacturedItemDefiniton, or using by incoming references from the "
            "Ingredient resource"
        ),
        description=(
            "The ingredients of this administrable medicinal product. This is only "
            "needed if the ingredients are not specified either using "
            "ManufacturedItemDefiniton (via "
            "AdministrableProductDefinition.producedFrom) to state which component "
            "items are used to make this, or using by incoming references from the "
            "Ingredient resource, to state in detail which substances exist within "
            "this. This element allows a basic coded ingredient to be used."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    producedFrom: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="producedFrom",
        title=(
            "Indicates the specific manufactured items that are part of the "
            "'formOf' product that are used in the preparation of this specific "
            "administrable form"
        ),
        description=(
            "Indicates the specific manufactured items that are part of the "
            "'formOf' product that are used in the preparation of this specific "
            "administrable form.  In some cases, an administrable form might use "
            "all of the items from the overall product (or there might only be one "
            "item), while in other cases, an administrable form might use only a "
            "subset of the items available in the overall product.  For example, an"
            " administrable form might involve combining a liquid and a powder "
            "available as part of an overall product, but not involve applying the "
            "also supplied cream."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ManufacturedItemDefinition"],
        },
    )

    property: typing.List[fhirtypes.AdministrableProductDefinitionPropertyType] | None = Field(  # type: ignore
        default=None,
        alias="property",
        title="Characteristics e.g. a product's onset of action",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    routeOfAdministration: typing.List[fhirtypes.AdministrableProductDefinitionRouteOfAdministrationType] = Field(  # type: ignore
        default=...,
        alias="routeOfAdministration",
        title=(
            "The path by which the product is taken into or makes contact with the "
            "body"
        ),
        description=(
            "The path by which the product is taken into or makes contact with the "
            "body. In some regions this is referred to as the licenced or approved "
            "route. RouteOfAdministration cannot be used when the 'formOf' product "
            "already uses MedicinalProductDefinition.route (and vice versa)."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this administrable product. Enables tracking the life-"
            "cycle of the content."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["draft", "active", "retired", "unknown"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_status", title="Extension field for ``status``."
    )

    unitOfPresentation: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="unitOfPresentation",
        title=(
            "The presentation type in which this item is given to a patient. e.g. "
            "for a spray - 'puff'"
        ),
        description=(
            "The presentation type in which this item is given to a patient. e.g. "
            "for a spray - 'puff' (as in 'contains 100 mcg per puff'), or for a "
            "liquid - 'vial' (as in 'contains 5 ml per vial')."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``AdministrableProductDefinition`` according to specification,
        with preserving the original sequence order.
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
            "formOf",
            "administrableDoseForm",
            "unitOfPresentation",
            "producedFrom",
            "ingredient",
            "device",
            "property",
            "routeOfAdministration",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``AdministrableProductDefinition`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "identifier",
            "status",
            "formOf",
            "administrableDoseForm",
            "unitOfPresentation",
            "producedFrom",
            "ingredient",
            "device",
            "property",
            "routeOfAdministration",
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


class AdministrableProductDefinitionProperty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Characteristics e.g. a product's onset of action.
    """

    __resource_type__ = "AdministrableProductDefinitionProperty"

    status: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="status",
        title="The status of characteristic e.g. assigned or pending",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        default=...,
        alias="type",
        title="A code expressing the type of characteristic",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    valueAttachment: fhirtypes.AttachmentType | None = Field(  # type: ignore
        default=None,
        alias="valueAttachment",
        title="A value for the characteristic",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueBoolean: bool | None = Field(  # type: ignore
        default=None,
        alias="valueBoolean",
        title="A value for the characteristic",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_valueBoolean",
        title="Extension field for ``valueBoolean``.",
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="valueCodeableConcept",
        title="A value for the characteristic",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueDate: fhirtypes.DateType | None = Field(  # type: ignore
        default=None,
        alias="valueDate",
        title="A value for the characteristic",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_valueDate", title="Extension field for ``valueDate``."
    )

    valueQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        default=None,
        alias="valueQuantity",
        title="A value for the characteristic",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``AdministrableProductDefinitionProperty`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "valueCodeableConcept",
            "valueQuantity",
            "valueDate",
            "valueBoolean",
            "valueAttachment",
            "status",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``AdministrableProductDefinitionProperty`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "modifierExtension",
            "type",
            "valueCodeableConcept",
            "valueQuantity",
            "valueDate",
            "valueBoolean",
            "valueAttachment",
            "status",
        ]

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
            "value": [
                "valueAttachment",
                "valueBoolean",
                "valueCodeableConcept",
                "valueDate",
                "valueQuantity",
            ]
        }
        return one_of_many_fields


class AdministrableProductDefinitionRouteOfAdministration(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The path by which the product is taken into or makes contact with the body.
    The path by which the product is taken into or makes contact with the body.
    In some regions this is referred to as the licenced or approved route.
    RouteOfAdministration cannot be used when the 'formOf' product already uses
    MedicinalProductDefinition.route (and vice versa).
    """

    __resource_type__ = "AdministrableProductDefinitionRouteOfAdministration"

    code: fhirtypes.CodeableConceptType = Field(  # type: ignore
        default=...,
        alias="code",
        title="Coded expression for the route",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    firstDose: fhirtypes.QuantityType | None = Field(  # type: ignore
        default=None,
        alias="firstDose",
        title=(
            "The first dose (dose quantity) administered can be specified for the "
            "product"
        ),
        description=(
            "The first dose (dose quantity) administered can be specified for the "
            "product, using a numerical value and its unit of measurement."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    maxDosePerDay: fhirtypes.QuantityType | None = Field(  # type: ignore
        default=None,
        alias="maxDosePerDay",
        title="The maximum dose quantity to be administered in any one 24-h period",
        description=(
            "The maximum dose per day (maximum dose quantity to be administered in "
            "any one 24-h period) that can be administered."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    maxDosePerTreatmentPeriod: fhirtypes.RatioType | None = Field(  # type: ignore
        default=None,
        alias="maxDosePerTreatmentPeriod",
        title="The maximum dose per treatment period that can be administered",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    maxSingleDose: fhirtypes.QuantityType | None = Field(  # type: ignore
        default=None,
        alias="maxSingleDose",
        title="The maximum single dose that can be administered",
        description=(
            "The maximum single dose that can be administered, specified using a "
            "numerical value and its unit of measurement."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    maxTreatmentPeriod: fhirtypes.DurationType | None = Field(  # type: ignore
        default=None,
        alias="maxTreatmentPeriod",
        title=(
            "The maximum treatment period during which the product can be "
            "administered"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    targetSpecies: typing.List[fhirtypes.AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesType] | None = Field(  # type: ignore
        default=None,
        alias="targetSpecies",
        title="A species for which this route applies",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``AdministrableProductDefinitionRouteOfAdministration`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "firstDose",
            "maxSingleDose",
            "maxDosePerDay",
            "maxDosePerTreatmentPeriod",
            "maxTreatmentPeriod",
            "targetSpecies",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``AdministrableProductDefinitionRouteOfAdministration`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "modifierExtension",
            "code",
            "firstDose",
            "maxSingleDose",
            "maxDosePerDay",
            "maxDosePerTreatmentPeriod",
            "maxTreatmentPeriod",
            "targetSpecies",
        ]


class AdministrableProductDefinitionRouteOfAdministrationTargetSpecies(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A species for which this route applies.
    """

    __resource_type__ = (
        "AdministrableProductDefinitionRouteOfAdministrationTargetSpecies"
    )

    code: fhirtypes.CodeableConceptType = Field(  # type: ignore
        default=...,
        alias="code",
        title="Coded expression for the species",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    withdrawalPeriod: typing.List[fhirtypes.AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriodType] | None = Field(  # type: ignore
        default=None,
        alias="withdrawalPeriod",
        title=(
            "A species specific time during which consumption of animal product is "
            "not appropriate"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``AdministrableProductDefinitionRouteOfAdministrationTargetSpecies`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "withdrawalPeriod"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``AdministrableProductDefinitionRouteOfAdministrationTargetSpecies`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension", "code", "withdrawalPeriod"]


class AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriod(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A species specific time during which consumption of animal product is not
    appropriate.
    """

    __resource_type__ = "AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriod"

    supportingInformation: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="supportingInformation",
        title="Extra information about the withdrawal period",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    supportingInformation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_supportingInformation",
        title="Extension field for ``supportingInformation``.",
    )

    tissue: fhirtypes.CodeableConceptType = Field(  # type: ignore
        default=...,
        alias="tissue",
        title=(
            "The type of tissue for which the withdrawal period applies, e.g. meat,"
            " milk"
        ),
        description=(
            "Coded expression for the type of tissue for which the withdrawal "
            "period applies, e.g. meat, milk."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    value: fhirtypes.QuantityType = Field(  # type: ignore
        default=...,
        alias="value",
        title="A value for the time",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriod`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "tissue",
            "value",
            "supportingInformation",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriod`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension", "tissue", "value", "supportingInformation"]
