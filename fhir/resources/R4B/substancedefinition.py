# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubstanceDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class SubstanceDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The detailed description of a substance, typically at a level beyond what
    is used for prescribing.
    """

    resource_type = Field("SubstanceDefinition", const=True)

    classification: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="classification",
        title=(
            "A categorization, high level e.g. polymer or nucleic acid, or food, "
            "chemical, biological, or lower e.g. polymer linear or branch chain, or"
            " type of impurity"
        ),
        description=(
            "A high level categorization, e.g. polymer or nucleic acid, or food, "
            "chemical, biological, or a lower level such as the general types of "
            "polymer (linear or branch chain) or type of impurity (process related "
            "or contaminant)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    code: typing.List[fhirtypes.SubstanceDefinitionCodeType] = Field(
        None,
        alias="code",
        title="Codes associated with the substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.Markdown = Field(
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
        title="If the substance applies to human or veterinary use",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    grade: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="grade",
        title=(
            "The quality standard, established benchmark, to which substance "
            "complies (e.g. USP/NF, BP)"
        ),
        description=(
            "The quality standard, established benchmark, to which substance "
            "complies (e.g. USP/NF, Ph. Eur, JP, BP, Company Standard)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Identifier by which this substance is known",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    informationSource: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="informationSource",
        title="Supporting literature",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Citation"],
    )

    manufacturer: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="manufacturer",
        title="The entity that creates, makes, produces or fabricates the substance",
        description=(
            "The entity that creates, makes, produces or fabricates the substance. "
            "This is a set of potential manufacturers but is not necessarily "
            "comprehensive."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    moiety: typing.List[fhirtypes.SubstanceDefinitionMoietyType] = Field(
        None,
        alias="moiety",
        title="Moiety, for structural modifications",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    molecularWeight: typing.List[
        fhirtypes.SubstanceDefinitionMolecularWeightType
    ] = Field(
        None,
        alias="molecularWeight",
        title="The molecular weight or weight range",
        description=(
            "The molecular weight or weight range (for proteins, polymers or "
            "nucleic acids)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    name: typing.List[fhirtypes.SubstanceDefinitionNameType] = Field(
        None,
        alias="name",
        title="Names applicable to this substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Textual comment about the substance's catalogue or registry record",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    property: typing.List[fhirtypes.SubstanceDefinitionPropertyType] = Field(
        None,
        alias="property",
        title="General specifications for this substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    relationship: typing.List[fhirtypes.SubstanceDefinitionRelationshipType] = Field(
        None,
        alias="relationship",
        title="A link between this substance and another",
        description=(
            "A link between this substance and another, with details of the "
            "relationship."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    sourceMaterial: fhirtypes.SubstanceDefinitionSourceMaterialType = Field(
        None,
        alias="sourceMaterial",
        title="Material or taxonomic/anatomical source",
        description="Material or taxonomic/anatomical source for the substance.",
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title="Status of substance within the catalogue e.g. active, retired",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    structure: fhirtypes.SubstanceDefinitionStructureType = Field(
        None,
        alias="structure",
        title="Structural information",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    supplier: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="supplier",
        title=(
            "An entity that is the source for the substance. It may be different "
            "from the manufacturer"
        ),
        description=(
            "An entity that is the source for the substance. It may be different "
            "from the manufacturer. Supplier is synonymous to a distributor."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="A business level version identifier of the substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceDefinition`` according specification,
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
            "version",
            "status",
            "classification",
            "domain",
            "grade",
            "description",
            "informationSource",
            "note",
            "manufacturer",
            "supplier",
            "moiety",
            "property",
            "molecularWeight",
            "structure",
            "code",
            "name",
            "relationship",
            "sourceMaterial",
        ]


class SubstanceDefinitionCode(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Codes associated with the substance.
    """

    resource_type = Field("SubstanceDefinitionCode", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="The specific code",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Any comment can be provided in this field",
        description="Any comment can be provided in this field, if necessary.",
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

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title="Status of the code assignment, for example 'provisional', 'approved'",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    statusDate: fhirtypes.DateTime = Field(
        None,
        alias="statusDate",
        title="The date at which the code status was changed",
        description=(
            "The date at which the code status was changed as part of the "
            "terminology maintenance."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    statusDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_statusDate", title="Extension field for ``statusDate``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceDefinitionCode`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "status",
            "statusDate",
            "note",
            "source",
        ]


class SubstanceDefinitionMoiety(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Moiety, for structural modifications.
    """

    resource_type = Field("SubstanceDefinitionMoiety", const=True)

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

    measurementType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="measurementType",
        title="The measurement type of the quantitative value",
        description=(
            "The measurement type of the quantitative value. In capturing the "
            "actual relative amounts of substances or molecular fragments it may be"
            " necessary to indicate whether the amount refers to, for example, a "
            "mole ratio or weight ratio."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    molecularFormula: fhirtypes.String = Field(
        None,
        alias="molecularFormula",
        title="Molecular formula for this moiety (e.g. with the Hill system)",
        description=(
            "Molecular formula for this moiety of this substance, typically using "
            "the Hill system."
        ),
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

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceDefinitionMoiety`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "role",
            "identifier",
            "name",
            "stereochemistry",
            "opticalActivity",
            "molecularFormula",
            "amountQuantity",
            "amountString",
            "measurementType",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2804(
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


class SubstanceDefinitionMolecularWeight(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The molecular weight or weight range.
    The molecular weight or weight range (for proteins, polymers or nucleic
    acids).
    """

    resource_type = Field("SubstanceDefinitionMolecularWeight", const=True)

    amount: fhirtypes.QuantityType = Field(
        ...,
        alias="amount",
        title="Used to capture quantitative values for a variety of elements",
        description=(
            "Used to capture quantitative values for a variety of elements. If only"
            " limits are given, the arithmetic mean would be the average. If only a"
            " single definite value for a given element is given, it would be "
            "captured in this field."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    method: fhirtypes.CodeableConceptType = Field(
        None,
        alias="method",
        title="The method by which the weight was determined",
        description="The method by which the molecular weight was determined.",
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type of molecular weight e.g. exact, average, weight average",
        description=(
            "Type of molecular weight such as exact, average (also known as. number"
            " average), weight average."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceDefinitionMolecularWeight`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "method", "type", "amount"]


class SubstanceDefinitionName(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Names applicable to this substance.
    """

    resource_type = Field("SubstanceDefinitionName", const=True)

    domain: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="domain",
        title=(
            "The use context of this name e.g. as an active ingredient or as a food"
            " colour additive"
        ),
        description=(
            "The use context of this name for example if there is a different name "
            "a drug active ingredient as opposed to a food colour additive."
        ),
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
        title="Human language that the name is written in",
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

    official: typing.List[fhirtypes.SubstanceDefinitionNameOfficialType] = Field(
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
        title="The status of the name e.g. 'current', 'proposed'",
        description="The status of the name, for example 'current', 'proposed'.",
        # if property is element of this resource.
        element_property=True,
    )

    synonym: typing.List[fhirtypes.SubstanceDefinitionNameType] = Field(
        None,
        alias="synonym",
        title=(
            "A synonym of this particular name, by which the substance is also " "known"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    translation: typing.List[fhirtypes.SubstanceDefinitionNameType] = Field(
        None,
        alias="translation",
        title="A translation for this name into another human language",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Name type e.g. 'systematic',  'scientific, 'brand'",
        description="Name type, for example 'systematic',  'scientific, 'brand'.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceDefinitionName`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "name",
            "type",
            "status",
            "preferred",
            "language",
            "domain",
            "jurisdiction",
            "synonym",
            "translation",
            "official",
            "source",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2538(
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


class SubstanceDefinitionNameOfficial(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details of the official nature of this name.
    """

    resource_type = Field("SubstanceDefinitionNameOfficial", const=True)

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
        description="Date of the official name change.",
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title="The status of the official name, for example 'draft', 'active'",
        description=(
            "The status of the official name, for example 'draft', 'active', "
            "'retired'."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceDefinitionNameOfficial`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "authority", "status", "date"]


class SubstanceDefinitionProperty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    General specifications for this substance.
    """

    resource_type = Field("SubstanceDefinitionProperty", const=True)

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="A code expressing the type of property",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="A value for the property",
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
        title="A value for the property",
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
        title="A value for the property",
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
        title="A value for the property",
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
        title="A value for the property",
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
        ``SubstanceDefinitionProperty`` according specification,
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
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3042(
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


class SubstanceDefinitionRelationship(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A link between this substance and another.
    A link between this substance and another, with details of the
    relationship.
    """

    resource_type = Field("SubstanceDefinitionRelationship", const=True)

    amountQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="amountQuantity",
        title=(
            "A numeric factor for the relationship, e.g. that a substance salt has "
            "some percentage of active substance in relation to some other"
        ),
        description=(
            "A numeric factor for the relationship, for instance to express that "
            "the salt of a substance has some percentage of the active substance in"
            " relation to some other."
        ),
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
            "A numeric factor for the relationship, e.g. that a substance salt has "
            "some percentage of active substance in relation to some other"
        ),
        description=(
            "A numeric factor for the relationship, for instance to express that "
            "the salt of a substance has some percentage of the active substance in"
            " relation to some other."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e amount[x]
        one_of_many="amount",
        one_of_many_required=False,
    )

    amountString: fhirtypes.String = Field(
        None,
        alias="amountString",
        title=(
            "A numeric factor for the relationship, e.g. that a substance salt has "
            "some percentage of active substance in relation to some other"
        ),
        description=(
            "A numeric factor for the relationship, for instance to express that "
            "the salt of a substance has some percentage of the active substance in"
            " relation to some other."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e amount[x]
        one_of_many="amount",
        one_of_many_required=False,
    )
    amountString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_amountString", title="Extension field for ``amountString``."
    )

    comparator: fhirtypes.CodeableConceptType = Field(
        None,
        alias="comparator",
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
            "several possible relationships"
        ),
        description=(
            "For example where an enzyme strongly bonds with a particular "
            "substance, this is a defining relationship for that enzyme, out of "
            "several possible substance relationships."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    isDefining__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_isDefining", title="Extension field for ``isDefining``."
    )

    ratioHighLimitAmount: fhirtypes.RatioType = Field(
        None,
        alias="ratioHighLimitAmount",
        title="For use when the numeric has an uncertain range",
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

    substanceDefinitionCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="substanceDefinitionCodeableConcept",
        title=(
            "A pointer to another substance, as a resource or a representational "
            "code"
        ),
        description=(
            "A pointer to another substance, as a resource or just a "
            "representational code."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e substanceDefinition[x]
        one_of_many="substanceDefinition",
        one_of_many_required=False,
    )

    substanceDefinitionReference: fhirtypes.ReferenceType = Field(
        None,
        alias="substanceDefinitionReference",
        title=(
            "A pointer to another substance, as a resource or a representational "
            "code"
        ),
        description=(
            "A pointer to another substance, as a resource or just a "
            "representational code."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e substanceDefinition[x]
        one_of_many="substanceDefinition",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SubstanceDefinition"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title='For example "salt to parent", "active moiety"',
        description=(
            'For example "salt to parent", "active moiety", "starting material", '
            '"polymorph", "impurity of".'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceDefinitionRelationship`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "substanceDefinitionReference",
            "substanceDefinitionCodeableConcept",
            "type",
            "isDefining",
            "amountQuantity",
            "amountRatio",
            "amountString",
            "ratioHighLimitAmount",
            "comparator",
            "source",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3430(
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
            "amount": ["amountQuantity", "amountRatio", "amountString"],
            "substanceDefinition": [
                "substanceDefinitionCodeableConcept",
                "substanceDefinitionReference",
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


class SubstanceDefinitionSourceMaterial(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Material or taxonomic/anatomical source.
    Material or taxonomic/anatomical source for the substance.
    """

    resource_type = Field("SubstanceDefinitionSourceMaterial", const=True)

    countryOfOrigin: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="countryOfOrigin",
        title="The country or countries where the material is harvested",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    genus: fhirtypes.CodeableConceptType = Field(
        None,
        alias="genus",
        title=(
            "The genus of an organism e.g. the Latin epithet of the plant/animal "
            "scientific name"
        ),
        description=(
            "The genus of an organism, typically referring to the Latin epithet of "
            "the genus element of the plant/animal scientific name."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    part: fhirtypes.CodeableConceptType = Field(
        None,
        alias="part",
        title="An anatomical origin of the source material within an organism",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    species: fhirtypes.CodeableConceptType = Field(
        None,
        alias="species",
        title=(
            "The species of an organism e.g. the Latin epithet of the species of "
            "the plant/animal"
        ),
        description=(
            "The species of an organism, typically referring to the Latin epithet "
            "of the species of the plant/animal."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title=(
            "Classification of the origin of the raw material. e.g. cat hair is an "
            "Animal source type"
        ),
        description=(
            "A classification that provides the origin of the raw material. "
            "Example: cat hair would be an Animal source type."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceDefinitionSourceMaterial`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "genus",
            "species",
            "part",
            "countryOfOrigin",
        ]


class SubstanceDefinitionStructure(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Structural information.
    """

    resource_type = Field("SubstanceDefinitionStructure", const=True)

    molecularFormula: fhirtypes.String = Field(
        None,
        alias="molecularFormula",
        title="Molecular formula (e.g. using the Hill system)",
        description="Molecular formula of this substance, typically using the Hill system.",
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
        title="Specified per moiety according to the Hill system",
        description=(
            "Specified per moiety according to the Hill system, i.e. first C, then "
            "H, then alphabetical, each moiety separated by a dot."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    molecularFormulaByMoiety__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_molecularFormulaByMoiety",
        title="Extension field for ``molecularFormulaByMoiety``.",
    )

    molecularWeight: fhirtypes.SubstanceDefinitionMolecularWeightType = Field(
        None,
        alias="molecularWeight",
        title="The molecular weight or weight range",
        description=(
            "The molecular weight or weight range (for proteins, polymers or "
            "nucleic acids)."
        ),
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
        fhirtypes.SubstanceDefinitionStructureRepresentationType
    ] = Field(
        None,
        alias="representation",
        title="A depiction of the structure or characterization of the substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    sourceDocument: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="sourceDocument",
        title="Source of information for the structure",
        description="The source of information about the structure.",
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

    technique: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="technique",
        title="The method used to find the structure e.g. X-ray, NMR",
        description=(
            "The method used to elucidate the structure or characterization of the "
            "drug substance. Examples: X-ray, HPLC, NMR, Peptide mapping, Ligand "
            "binding assay."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceDefinitionStructure`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "stereochemistry",
            "opticalActivity",
            "molecularFormula",
            "molecularFormulaByMoiety",
            "molecularWeight",
            "technique",
            "sourceDocument",
            "representation",
        ]


class SubstanceDefinitionStructureRepresentation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A depiction of the structure or characterization of the substance.
    """

    resource_type = Field("SubstanceDefinitionStructureRepresentation", const=True)

    document: fhirtypes.ReferenceType = Field(
        None,
        alias="document",
        title=(
            "An attachment with the structural representation e.g. a structure "
            "graphic or AnIML file"
        ),
        description=(
            "An attached file with the structural representation or "
            "characterization e.g. a molecular structure graphic of the substance, "
            "a JCAMP or AnIML file."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
    )

    format: fhirtypes.CodeableConceptType = Field(
        None,
        alias="format",
        title=(
            "The format of the representation e.g. InChI, SMILES, MOLFILE (note: "
            "not the physical file format)"
        ),
        description=(
            "The format of the representation e.g. InChI, SMILES, MOLFILE, CDX, "
            "SDF, PDB, mmCIF. The logical content type rather than the physical "
            "file format of a document."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    representation: fhirtypes.String = Field(
        None,
        alias="representation",
        title=(
            "The structural representation or characterization as a text string in "
            "a standard format"
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
        title="The kind of structural representation (e.g. full, partial)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceDefinitionStructureRepresentation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "representation",
            "format",
            "document",
        ]
