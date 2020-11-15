# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubstanceSpecification
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class SubstanceSpecification(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The detailed description of a substance, typically at a level beyond what
    is used for prescribing.
    """

    resource_type = Field("SubstanceSpecification", const=True)

    code: typing.List[fhirtypes.SubstanceSpecificationCodeType] = Field(
        None,
        alias="code",
        title="Codes associated with the substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Textual comment about this record of a substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Textual description of the substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    domain: fhirtypes.CodeableConceptType = Field(
        None,
        alias="domain",
        title="If the substance applies to only human or veterinary use",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Identifier by which this substance is known",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    moiety: typing.List[fhirtypes.SubstanceSpecificationMoietyType] = Field(
        None,
        alias="moiety",
        title="Moiety, for structural modifications",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    molecularWeight: typing.List[
        fhirtypes.SubstanceSpecificationStructureIsotopeMolecularWeightType
    ] = Field(
        None,
        alias="molecularWeight",
        title=(
            "The molecular weight or weight range (for proteins, polymers or "
            "nucleic acids)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    name: typing.List[fhirtypes.SubstanceSpecificationNameType] = Field(
        None,
        alias="name",
        title="Names applicable to this substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    nucleicAcid: fhirtypes.ReferenceType = Field(
        None,
        alias="nucleicAcid",
        title="Data items specific to nucleic acids",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SubstanceNucleicAcid"],
    )

    polymer: fhirtypes.ReferenceType = Field(
        None,
        alias="polymer",
        title="Data items specific to polymers",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SubstancePolymer"],
    )

    property: typing.List[fhirtypes.SubstanceSpecificationPropertyType] = Field(
        None,
        alias="property",
        title=(
            "General specifications for this substance, including how it is related"
            " to other substances"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    protein: fhirtypes.ReferenceType = Field(
        None,
        alias="protein",
        title="Data items specific to proteins",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SubstanceProtein"],
    )

    referenceInformation: fhirtypes.ReferenceType = Field(
        None,
        alias="referenceInformation",
        title="General information detailing this substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SubstanceReferenceInformation"],
    )

    relationship: typing.List[fhirtypes.SubstanceSpecificationRelationshipType] = Field(
        None,
        alias="relationship",
        title=(
            "A link between this substance and another, with details of the "
            "relationship"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    source: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="source",
        title="Supporting literature",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
    )

    sourceMaterial: fhirtypes.ReferenceType = Field(
        None,
        alias="sourceMaterial",
        title="Material or taxonomic/anatomical source for the substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SubstanceSourceMaterial"],
    )

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title="Status of substance within the catalogue e.g. approved",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    structure: fhirtypes.SubstanceSpecificationStructureType = Field(
        None,
        alias="structure",
        title="Structural information",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="High level categorization, e.g. polymer or nucleic acid",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class SubstanceSpecificationCode(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Codes associated with the substance.
    """

    resource_type = Field("SubstanceSpecificationCode", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="The specific code",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Any comment can be provided in this field, if necessary",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    source: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="source",
        title="Supporting literature",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
    )

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title="Status of the code assignment",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    statusDate: fhirtypes.DateTime = Field(
        None,
        alias="statusDate",
        title=(
            "The date at which the code status is changed as part of the "
            "terminology maintenance"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    statusDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_statusDate", title="Extension field for ``statusDate``."
    )


class SubstanceSpecificationMoiety(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Moiety, for structural modifications.
    """

    resource_type = Field("SubstanceSpecificationMoiety", const=True)

    amountQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="amountQuantity",
        title="Quantitative value for this moiety",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e amount[x]
        one_of_many="amount",
        one_of_many_required=False,
    )

    amountString: fhirtypes.String = Field(
        None,
        alias="amountString",
        title="Quantitative value for this moiety",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e amount[x]
        one_of_many="amount",
        one_of_many_required=False,
    )
    amountString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_amountString", title="Extension field for ``amountString``."
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Identifier by which this moiety substance is known",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    molecularFormula: fhirtypes.String = Field(
        None,
        alias="molecularFormula",
        title="Molecular formula",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    molecularFormula__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_molecularFormula",
        title="Extension field for ``molecularFormula``.",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Textual name for this moiety substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    opticalActivity: fhirtypes.CodeableConceptType = Field(
        None,
        alias="opticalActivity",
        title="Optical activity type",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="Role that the moiety is playing",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    stereochemistry: fhirtypes.CodeableConceptType = Field(
        None,
        alias="stereochemistry",
        title="Stereochemistry type",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3116(
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
        one_of_many_fields = {"amount": ["amountQuantity", "amountString"]}
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


class SubstanceSpecificationName(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Names applicable to this substance.
    """

    resource_type = Field("SubstanceSpecificationName", const=True)

    domain: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="domain",
        title=(
            "The use context of this name for example if there is a different name "
            "a drug active ingredient as opposed to a food colour additive"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="The jurisdiction where this name applies",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    language: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="language",
        title="Language of the name",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="The actual name",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    official: typing.List[fhirtypes.SubstanceSpecificationNameOfficialType] = Field(
        None,
        alias="official",
        title="Details of the official nature of this name",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    preferred: bool = Field(
        None,
        alias="preferred",
        title="If this is the preferred name for this substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    preferred__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_preferred", title="Extension field for ``preferred``."
    )

    source: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="source",
        title="Supporting literature",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
    )

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title="The status of the name",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    synonym: typing.List[fhirtypes.SubstanceSpecificationNameType] = Field(
        None,
        alias="synonym",
        title="A synonym of this name",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    translation: typing.List[fhirtypes.SubstanceSpecificationNameType] = Field(
        None,
        alias="translation",
        title="A translation for this name",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Name type",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2850(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("name", "name__ext")]
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


class SubstanceSpecificationNameOfficial(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details of the official nature of this name.
    """

    resource_type = Field("SubstanceSpecificationNameOfficial", const=True)

    authority: fhirtypes.CodeableConceptType = Field(
        None,
        alias="authority",
        title="Which authority uses this official name",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date of official name change",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title="The status of the official name",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class SubstanceSpecificationProperty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    General specifications for this substance, including how it is related to
    other substances.
    """

    resource_type = Field("SubstanceSpecificationProperty", const=True)

    amountQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="amountQuantity",
        title="Quantitative value for this property",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e amount[x]
        one_of_many="amount",
        one_of_many_required=False,
    )

    amountString: fhirtypes.String = Field(
        None,
        alias="amountString",
        title="Quantitative value for this property",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e amount[x]
        one_of_many="amount",
        one_of_many_required=False,
    )
    amountString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_amountString", title="Extension field for ``amountString``."
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="A category for this property, e.g. Physical, Chemical, Enzymatic",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Property type e.g. viscosity, pH, isoelectric point",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    definingSubstanceCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="definingSubstanceCodeableConcept",
        title=(
            "A substance upon which a defining property depends (e.g. for "
            "solubility: in water, in alcohol)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e definingSubstance[x]
        one_of_many="definingSubstance",
        one_of_many_required=False,
    )

    definingSubstanceReference: fhirtypes.ReferenceType = Field(
        None,
        alias="definingSubstanceReference",
        title=(
            "A substance upon which a defining property depends (e.g. for "
            "solubility: in water, in alcohol)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e definingSubstance[x]
        one_of_many="definingSubstance",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SubstanceSpecification", "Substance"],
    )

    parameters: fhirtypes.String = Field(
        None,
        alias="parameters",
        title=(
            "Parameters that were used in the measurement of a property (e.g. for "
            "viscosity: measured at 20C with a pH of 7.1)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    parameters__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_parameters", title="Extension field for ``parameters``."
    )

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3354(
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
            "amount": ["amountQuantity", "amountString"],
            "definingSubstance": [
                "definingSubstanceCodeableConcept",
                "definingSubstanceReference",
            ],
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


class SubstanceSpecificationRelationship(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A link between this substance and another, with details of the relationship.
    """

    resource_type = Field("SubstanceSpecificationRelationship", const=True)

    amountQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="amountQuantity",
        title=(
            "A numeric factor for the relationship, for instance to express that "
            "the salt of a substance has some percentage of the active substance in"
            " relation to some other"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e amount[x]
        one_of_many="amount",
        one_of_many_required=False,
    )

    amountRange: fhirtypes.RangeType = Field(
        None,
        alias="amountRange",
        title=(
            "A numeric factor for the relationship, for instance to express that "
            "the salt of a substance has some percentage of the active substance in"
            " relation to some other"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e amount[x]
        one_of_many="amount",
        one_of_many_required=False,
    )

    amountRatio: fhirtypes.RatioType = Field(
        None,
        alias="amountRatio",
        title=(
            "A numeric factor for the relationship, for instance to express that "
            "the salt of a substance has some percentage of the active substance in"
            " relation to some other"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e amount[x]
        one_of_many="amount",
        one_of_many_required=False,
    )

    amountRatioLowLimit: fhirtypes.RatioType = Field(
        None,
        alias="amountRatioLowLimit",
        title="For use when the numeric",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    amountString: fhirtypes.String = Field(
        None,
        alias="amountString",
        title=(
            "A numeric factor for the relationship, for instance to express that "
            "the salt of a substance has some percentage of the active substance in"
            " relation to some other"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e amount[x]
        one_of_many="amount",
        one_of_many_required=False,
    )
    amountString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_amountString", title="Extension field for ``amountString``."
    )

    amountType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="amountType",
        title=(
            'An operator for the amount, for example "average", "approximately", '
            '"less than"'
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    isDefining: bool = Field(
        None,
        alias="isDefining",
        title=(
            "For example where an enzyme strongly bonds with a particular "
            "substance, this is a defining relationship for that enzyme, out of "
            "several possible substance relationships"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    isDefining__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_isDefining", title="Extension field for ``isDefining``."
    )

    relationship: fhirtypes.CodeableConceptType = Field(
        None,
        alias="relationship",
        title='For example "salt to parent", "active moiety", "starting material"',
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    source: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="source",
        title="Supporting literature",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
    )

    substanceCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="substanceCodeableConcept",
        title=(
            "A pointer to another substance, as a resource or just a "
            "representational code"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e substance[x]
        one_of_many="substance",
        one_of_many_required=False,
    )

    substanceReference: fhirtypes.ReferenceType = Field(
        None,
        alias="substanceReference",
        title=(
            "A pointer to another substance, as a resource or just a "
            "representational code"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e substance[x]
        one_of_many="substance",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SubstanceSpecification"],
    )

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3742(
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
            "amount": ["amountQuantity", "amountRange", "amountRatio", "amountString"],
            "substance": ["substanceCodeableConcept", "substanceReference"],
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


class SubstanceSpecificationStructure(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Structural information.
    """

    resource_type = Field("SubstanceSpecificationStructure", const=True)

    isotope: typing.List[fhirtypes.SubstanceSpecificationStructureIsotopeType] = Field(
        None,
        alias="isotope",
        title=(
            "Applicable for single substances that contain a radionuclide or a non-"
            "natural isotopic ratio"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    molecularFormula: fhirtypes.String = Field(
        None,
        alias="molecularFormula",
        title="Molecular formula",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    molecularFormula__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_molecularFormula",
        title="Extension field for ``molecularFormula``.",
    )

    molecularFormulaByMoiety: fhirtypes.String = Field(
        None,
        alias="molecularFormulaByMoiety",
        title=(
            "Specified per moiety according to the Hill system, i.e. first C, then "
            "H, then alphabetical, each moiety separated by a dot"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    molecularFormulaByMoiety__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_molecularFormulaByMoiety",
        title="Extension field for ``molecularFormulaByMoiety``.",
    )

    molecularWeight: fhirtypes.SubstanceSpecificationStructureIsotopeMolecularWeightType = Field(  # noqa:B950
        None,
        alias="molecularWeight",
        title=(
            "The molecular weight or weight range (for proteins, polymers or "
            "nucleic acids)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    opticalActivity: fhirtypes.CodeableConceptType = Field(
        None,
        alias="opticalActivity",
        title="Optical activity type",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    representation: typing.List[
        fhirtypes.SubstanceSpecificationStructureRepresentationType
    ] = Field(
        None,
        alias="representation",
        title="Molecular structural representation",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    source: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="source",
        title="Supporting literature",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
    )

    stereochemistry: fhirtypes.CodeableConceptType = Field(
        None,
        alias="stereochemistry",
        title="Stereochemistry type",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class SubstanceSpecificationStructureIsotope(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Applicable for single substances that contain a radionuclide or a non-
    natural isotopic ratio.
    """

    resource_type = Field("SubstanceSpecificationStructureIsotope", const=True)

    halfLife: fhirtypes.QuantityType = Field(
        None,
        alias="halfLife",
        title="Half life - for a non-natural nuclide",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Substance identifier for each non-natural or radioisotope",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    molecularWeight: fhirtypes.SubstanceSpecificationStructureIsotopeMolecularWeightType = Field(  # noqa:B950
        None,
        alias="molecularWeight",
        title=(
            "The molecular weight or weight range (for proteins, polymers or "
            "nucleic acids)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.CodeableConceptType = Field(
        None,
        alias="name",
        title="Substance name for each non-natural or radioisotope",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    substitution: fhirtypes.CodeableConceptType = Field(
        None,
        alias="substitution",
        title="The type of isotopic substitution present in a single substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class SubstanceSpecificationStructureIsotopeMolecularWeight(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The molecular weight or weight range (for proteins, polymers or nucleic
    acids).
    """

    resource_type = Field(
        "SubstanceSpecificationStructureIsotopeMolecularWeight", const=True
    )

    amount: fhirtypes.QuantityType = Field(
        None,
        alias="amount",
        title=(
            "Used to capture quantitative values for a variety of elements. If only"
            " limits are given, the arithmetic mean would be the average. If only a"
            " single definite value for a given element is given, it would be "
            "captured in this field"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    method: fhirtypes.CodeableConceptType = Field(
        None,
        alias="method",
        title="The method by which the molecular weight was determined",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title=(
            "Type of molecular weight such as exact, average (also known as. number"
            " average), weight average"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class SubstanceSpecificationStructureRepresentation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Molecular structural representation.
    """

    resource_type = Field("SubstanceSpecificationStructureRepresentation", const=True)

    attachment: fhirtypes.AttachmentType = Field(
        None,
        alias="attachment",
        title="An attached file with the structural representation",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    representation: fhirtypes.String = Field(
        None,
        alias="representation",
        title=(
            "The structural representation as text string in a format e.g. InChI, "
            "SMILES, MOLFILE, CDX"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    representation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_representation", title="Extension field for ``representation``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="The type of structure (e.g. Full, Partial, Representative)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
