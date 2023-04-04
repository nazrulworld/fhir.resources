# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AdministrableProductDefinition
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

    resource_type = Field("AdministrableProductDefinition", const=True)

    administrableDoseForm: fhirtypes.CodeableConceptType = Field(
        None,
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
        # if property is element of this resource.
        element_property=True,
    )

    device: fhirtypes.ReferenceType = Field(
        None,
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
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DeviceDefinition"],
    )

    formOf: typing.List[fhirtypes.ReferenceType] = Field(
        None,
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
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicinalProductDefinition"],
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="An identifier for the administrable product",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    ingredient: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
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
        # if property is element of this resource.
        element_property=True,
    )

    producedFrom: typing.List[fhirtypes.ReferenceType] = Field(
        None,
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
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ManufacturedItemDefinition"],
    )

    property: typing.List[fhirtypes.AdministrableProductDefinitionPropertyType] = Field(
        None,
        alias="property",
        title="Characteristics e.g. a product's onset of action",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    routeOfAdministration: typing.List[
        fhirtypes.AdministrableProductDefinitionRouteOfAdministrationType
    ] = Field(
        ...,
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
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this administrable product. Enables tracking the life-"
            "cycle of the content."
        ),
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

    unitOfPresentation: fhirtypes.CodeableConceptType = Field(
        None,
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
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AdministrableProductDefinition`` according specification,
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
            "formOf",
            "administrableDoseForm",
            "unitOfPresentation",
            "producedFrom",
            "ingredient",
            "device",
            "property",
            "routeOfAdministration",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3288(
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


class AdministrableProductDefinitionProperty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Characteristics e.g. a product's onset of action.
    """

    resource_type = Field("AdministrableProductDefinitionProperty", const=True)

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title="The status of characteristic e.g. assigned or pending",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="A code expressing the type of characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="A value for the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="A value for the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="valueCodeableConcept",
        title="A value for the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueDate: fhirtypes.Date = Field(
        None,
        alias="valueDate",
        title="A value for the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDate", title="Extension field for ``valueDate``."
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="A value for the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AdministrableProductDefinitionProperty`` according specification,
        with preserving original sequence order.
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_4168(
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
            "value": [
                "valueAttachment",
                "valueBoolean",
                "valueCodeableConcept",
                "valueDate",
                "valueQuantity",
            ]
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

    resource_type = Field(
        "AdministrableProductDefinitionRouteOfAdministration", const=True
    )

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Coded expression for the route",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    firstDose: fhirtypes.QuantityType = Field(
        None,
        alias="firstDose",
        title=(
            "The first dose (dose quantity) administered can be specified for the "
            "product"
        ),
        description=(
            "The first dose (dose quantity) administered can be specified for the "
            "product, using a numerical value and its unit of measurement."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    maxDosePerDay: fhirtypes.QuantityType = Field(
        None,
        alias="maxDosePerDay",
        title="The maximum dose quantity to be administered in any one 24-h period",
        description=(
            "The maximum dose per day (maximum dose quantity to be administered in "
            "any one 24-h period) that can be administered."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    maxDosePerTreatmentPeriod: fhirtypes.RatioType = Field(
        None,
        alias="maxDosePerTreatmentPeriod",
        title="The maximum dose per treatment period that can be administered",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    maxSingleDose: fhirtypes.QuantityType = Field(
        None,
        alias="maxSingleDose",
        title="The maximum single dose that can be administered",
        description=(
            "The maximum single dose that can be administered, specified using a "
            "numerical value and its unit of measurement."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    maxTreatmentPeriod: fhirtypes.DurationType = Field(
        None,
        alias="maxTreatmentPeriod",
        title=(
            "The maximum treatment period during which the product can be "
            "administered"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    targetSpecies: typing.List[
        fhirtypes.AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesType
    ] = Field(
        None,
        alias="targetSpecies",
        title="A species for which this route applies",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AdministrableProductDefinitionRouteOfAdministration`` according specification,
        with preserving original sequence order.
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


class AdministrableProductDefinitionRouteOfAdministrationTargetSpecies(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A species for which this route applies.
    """

    resource_type = Field(
        "AdministrableProductDefinitionRouteOfAdministrationTargetSpecies", const=True
    )

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Coded expression for the species",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    withdrawalPeriod: typing.List[
        fhirtypes.AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriodType  # noqa: B950
    ] = Field(
        None,
        alias="withdrawalPeriod",
        title=(
            "A species specific time during which consumption of animal product is "
            "not appropriate"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AdministrableProductDefinitionRoute
        OfAdministrationTargetSpecies`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "withdrawalPeriod"]


class AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriod(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A species specific time during which consumption of animal product is not
    appropriate.
    """

    resource_type = Field(
        "AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriod",
        const=True,
    )

    supportingInformation: fhirtypes.String = Field(
        None,
        alias="supportingInformation",
        title="Extra information about the withdrawal period",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    supportingInformation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_supportingInformation",
        title="Extension field for ``supportingInformation``.",
    )

    tissue: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="tissue",
        title=(
            "The type of tissue for which the withdrawal period applies, e.g. meat,"
            " milk"
        ),
        description=(
            "Coded expression for the type of tissue for which the withdrawal "
            "period applies, e.g. meat, milk."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    value: fhirtypes.QuantityType = Field(
        ...,
        alias="value",
        title="A value for the time",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AdministrableProductDefinitionRoute
        OfAdministrationTargetSpeciesWithdrawalPeriod``
        according specification, with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "tissue",
            "value",
            "supportingInformation",
        ]
