# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ClinicalUseDefinition
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


class ClinicalUseDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A single issue - either an indication, contraindication, interaction or an
    undesirable effect for a medicinal product, medication, device or procedure.
    """

    resource_type = Field("ClinicalUseDefinition", const=True)

    category: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title=(
            "A categorisation of the issue, primarily for dividing warnings into "
            'subject heading areas such as "Pregnancy", "Overdose"'
        ),
        description=(
            "A categorisation of the issue, primarily for dividing warnings into "
            'subject heading areas such as "Pregnancy and Lactation", "Overdose", '
            '"Effects on Ability to Drive and Use Machines".'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    contraindication: fhirtypes.ClinicalUseDefinitionContraindicationType = Field(
        None,
        alias="contraindication",
        title="Specifics for when this is a contraindication",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier for this issue",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    indication: fhirtypes.ClinicalUseDefinitionIndicationType = Field(
        None,
        alias="indication",
        title="Specifics for when this is an indication",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    interaction: fhirtypes.ClinicalUseDefinitionInteractionType = Field(
        None,
        alias="interaction",
        title="Specifics for when this is an interaction",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    library: typing.List[typing.Optional[fhirtypes.Canonical]] = Field(
        None,
        alias="library",
        title="Logic used by the clinical use definition",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Library"],
    )
    library__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_library", title="Extension field for ``library``.")

    population: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="population",
        title="The population group to which this applies",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Group"],
    )

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title="Whether this is a current issue or one that has been retired etc",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    subject: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="subject",
        title=(
            "The medication, product, substance, device, procedure etc. for which "
            "this is an indication"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "MedicinalProductDefinition",
            "Medication",
            "ActivityDefinition",
            "PlanDefinition",
            "Device",
            "DeviceDefinition",
            "Substance",
            "NutritionProduct",
            "BiologicallyDerivedProduct",
        ],
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title=(
            "indication | contraindication | interaction | undesirable-effect | "
            "warning"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "indication",
            "contraindication",
            "interaction",
            "undesirable-effect",
            "warning",
        ],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    undesirableEffect: fhirtypes.ClinicalUseDefinitionUndesirableEffectType = Field(
        None,
        alias="undesirableEffect",
        title="A possible negative outcome from the use of this treatment",
        description=(
            "Describe the possible undesirable effects (negative outcomes) from the"
            " use of the medicinal product as treatment."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    warning: fhirtypes.ClinicalUseDefinitionWarningType = Field(
        None,
        alias="warning",
        title=(
            "Critical environmental, health or physical risks or hazards. For "
            "example 'Do not operate heavy machinery', 'May cause drowsiness'"
        ),
        description=(
            "A critical piece of information about environmental, health or "
            "physical risks or hazards that serve as caution to the user. For "
            "example 'Do not operate heavy machinery', 'May cause drowsiness', or "
            "'Get medical advice/attention if you feel unwell'."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClinicalUseDefinition`` according specification,
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
            "type",
            "category",
            "subject",
            "status",
            "contraindication",
            "indication",
            "interaction",
            "population",
            "library",
            "undesirableEffect",
            "warning",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2310(
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


class ClinicalUseDefinitionContraindication(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Specifics for when this is a contraindication.
    """

    resource_type = Field("ClinicalUseDefinitionContraindication", const=True)

    applicability: fhirtypes.ExpressionType = Field(
        None,
        alias="applicability",
        title=(
            "An expression that returns true or false, indicating whether the "
            "indication is applicable or not, after having applied its other "
            "elements"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    comorbidity: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="comorbidity",
        title="A comorbidity (concurrent condition) or coinfection",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ObservationDefinition"],
    )

    diseaseStatus: fhirtypes.CodeableReferenceType = Field(
        None,
        alias="diseaseStatus",
        title="The status of the disease or symptom for the contraindication",
        description=(
            "The status of the disease or symptom for the contraindication, for "
            'example "chronic" or "metastatic".'
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ObservationDefinition"],
    )

    diseaseSymptomProcedure: fhirtypes.CodeableReferenceType = Field(
        None,
        alias="diseaseSymptomProcedure",
        title=(
            "The situation that is being documented as contraindicating against "
            "this item"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ObservationDefinition"],
    )

    indication: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="indication",
        title="The indication which this is a contraidication for",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ClinicalUseDefinition"],
    )

    otherTherapy: typing.List[
        fhirtypes.ClinicalUseDefinitionContraindicationOtherTherapyType
    ] = Field(
        None,
        alias="otherTherapy",
        title=(
            "Information about use of the product in relation to other therapies "
            "described as part of the contraindication"
        ),
        description=(
            "Information about the use of the medicinal product in relation to "
            "other therapies described as part of the contraindication."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClinicalUseDefinitionContraindication`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "diseaseSymptomProcedure",
            "diseaseStatus",
            "comorbidity",
            "indication",
            "applicability",
            "otherTherapy",
        ]


class ClinicalUseDefinitionContraindicationOtherTherapy(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about use of the product in relation to other therapies
    described as part of the contraindication.
    Information about the use of the medicinal product in relation to other
    therapies described as part of the contraindication.
    """

    resource_type = Field(
        "ClinicalUseDefinitionContraindicationOtherTherapy", const=True
    )

    relationshipType: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="relationshipType",
        title=(
            "The type of relationship between the product "
            "indication/contraindication and another therapy"
        ),
        description=(
            "The type of relationship between the medicinal product indication or "
            "contraindication and another therapy."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    treatment: fhirtypes.CodeableReferenceType = Field(
        ...,
        alias="treatment",
        title=(
            "Reference to a specific medication, substance etc. as part of an "
            "indication or contraindication"
        ),
        description=(
            "Reference to a specific medication (active substance, medicinal "
            "product or class of products, biological, food etc.) as part of an "
            "indication or contraindication."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "MedicinalProductDefinition",
            "Medication",
            "Substance",
            "SubstanceDefinition",
            "NutritionProduct",
            "BiologicallyDerivedProduct",
            "ActivityDefinition",
        ],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClinicalUseDefinitionContraindicationOtherTherapy`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "relationshipType", "treatment"]


class ClinicalUseDefinitionIndication(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Specifics for when this is an indication.
    """

    resource_type = Field("ClinicalUseDefinitionIndication", const=True)

    applicability: fhirtypes.ExpressionType = Field(
        None,
        alias="applicability",
        title=(
            "An expression that returns true or false, indicating whether the "
            "indication is applicable or not, after having applied its other "
            "elements"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    comorbidity: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="comorbidity",
        title="A comorbidity or coinfection as part of the indication",
        description=(
            "A comorbidity (concurrent condition) or coinfection as part of the "
            "indication."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ObservationDefinition"],
    )

    diseaseStatus: fhirtypes.CodeableReferenceType = Field(
        None,
        alias="diseaseStatus",
        title="The status of the disease or symptom for the indication",
        description=(
            "The status of the disease or symptom for the indication, for example "
            '"chronic" or "metastatic".'
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ObservationDefinition"],
    )

    diseaseSymptomProcedure: fhirtypes.CodeableReferenceType = Field(
        None,
        alias="diseaseSymptomProcedure",
        title="The situation that is being documented as an indicaton for this item",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ObservationDefinition"],
    )

    durationRange: fhirtypes.RangeType = Field(
        None,
        alias="durationRange",
        title="Timing or duration information",
        description=(
            "Timing or duration information, that may be associated with use with "
            "the indicated condition e.g. Adult patients suffering from myocardial "
            "infarction (from a few days until less than 35 days), ischaemic stroke"
            " (from 7 days until less than 6 months)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e duration[x]
        one_of_many="duration",
        one_of_many_required=False,
    )

    durationString: fhirtypes.String = Field(
        None,
        alias="durationString",
        title="Timing or duration information",
        description=(
            "Timing or duration information, that may be associated with use with "
            "the indicated condition e.g. Adult patients suffering from myocardial "
            "infarction (from a few days until less than 35 days), ischaemic stroke"
            " (from 7 days until less than 6 months)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e duration[x]
        one_of_many="duration",
        one_of_many_required=False,
    )
    durationString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_durationString", title="Extension field for ``durationString``."
    )

    intendedEffect: fhirtypes.CodeableReferenceType = Field(
        None,
        alias="intendedEffect",
        title="The intended effect, aim or strategy to be achieved",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ObservationDefinition"],
    )

    otherTherapy: typing.List[
        fhirtypes.ClinicalUseDefinitionContraindicationOtherTherapyType
    ] = Field(
        None,
        alias="otherTherapy",
        title=(
            "The use of the medicinal product in relation to other therapies "
            "described as part of the indication"
        ),
        description=(
            "Information about the use of the medicinal product in relation to "
            "other therapies described as part of the indication."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    undesirableEffect: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="undesirableEffect",
        title=(
            "An unwanted side effect or negative outcome of the subject of this "
            "resource when being used for this indication"
        ),
        description=(
            "An unwanted side effect or negative outcome that may happen if you use"
            " the drug (or other subject of this resource) for this indication."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ClinicalUseDefinition"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClinicalUseDefinitionIndication`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "diseaseSymptomProcedure",
            "diseaseStatus",
            "comorbidity",
            "intendedEffect",
            "durationRange",
            "durationString",
            "undesirableEffect",
            "applicability",
            "otherTherapy",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3336(
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
        one_of_many_fields = {"duration": ["durationRange", "durationString"]}
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


class ClinicalUseDefinitionInteraction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Specifics for when this is an interaction.
    """

    resource_type = Field("ClinicalUseDefinitionInteraction", const=True)

    effect: fhirtypes.CodeableReferenceType = Field(
        None,
        alias="effect",
        title=(
            'The effect of the interaction, for example "reduced gastric absorption'
            ' of primary medication"'
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ObservationDefinition"],
    )

    incidence: fhirtypes.CodeableConceptType = Field(
        None,
        alias="incidence",
        title="The incidence of the interaction, e.g. theoretical, observed",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    interactant: typing.List[
        fhirtypes.ClinicalUseDefinitionInteractionInteractantType
    ] = Field(
        None,
        alias="interactant",
        title=(
            "The specific medication, product, food etc. or laboratory test that "
            "interacts"
        ),
        description=(
            "The specific medication, product, food, substance etc. or laboratory "
            "test that interacts."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    management: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="management",
        title="Actions for managing the interaction",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title=(
            "The type of the interaction e.g. drug-drug interaction, drug-lab test "
            "interaction"
        ),
        description=(
            "The type of the interaction e.g. drug-drug interaction, drug-food "
            "interaction, drug-lab test interaction."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClinicalUseDefinitionInteraction`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "interactant",
            "type",
            "effect",
            "incidence",
            "management",
        ]


class ClinicalUseDefinitionInteractionInteractant(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The specific medication, product, food etc. or laboratory test that
    interacts.
    The specific medication, product, food, substance etc. or laboratory test
    that interacts.
    """

    resource_type = Field("ClinicalUseDefinitionInteractionInteractant", const=True)

    itemCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="itemCodeableConcept",
        title=(
            "The specific medication, product, food etc. or laboratory test that "
            "interacts"
        ),
        description=(
            "The specific medication, product, food, substance etc. or laboratory "
            "test that interacts."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e item[x]
        one_of_many="item",
        one_of_many_required=True,
    )

    itemReference: fhirtypes.ReferenceType = Field(
        None,
        alias="itemReference",
        title=(
            "The specific medication, product, food etc. or laboratory test that "
            "interacts"
        ),
        description=(
            "The specific medication, product, food, substance etc. or laboratory "
            "test that interacts."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e item[x]
        one_of_many="item",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "MedicinalProductDefinition",
            "Medication",
            "Substance",
            "NutritionProduct",
            "BiologicallyDerivedProduct",
            "ObservationDefinition",
        ],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClinicalUseDefinitionInteractionInteractant`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "itemReference",
            "itemCodeableConcept",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_4617(
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
        one_of_many_fields = {"item": ["itemCodeableConcept", "itemReference"]}
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


class ClinicalUseDefinitionUndesirableEffect(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A possible negative outcome from the use of this treatment.
    Describe the possible undesirable effects (negative outcomes) from the use
    of the medicinal product as treatment.
    """

    resource_type = Field("ClinicalUseDefinitionUndesirableEffect", const=True)

    classification: fhirtypes.CodeableConceptType = Field(
        None,
        alias="classification",
        title="High level classification of the effect",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    frequencyOfOccurrence: fhirtypes.CodeableConceptType = Field(
        None,
        alias="frequencyOfOccurrence",
        title="How often the effect is seen",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    symptomConditionEffect: fhirtypes.CodeableReferenceType = Field(
        None,
        alias="symptomConditionEffect",
        title="The situation in which the undesirable effect may manifest",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ObservationDefinition"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClinicalUseDefinitionUndesirableEffect`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "symptomConditionEffect",
            "classification",
            "frequencyOfOccurrence",
        ]


class ClinicalUseDefinitionWarning(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Critical environmental, health or physical risks or hazards. For example
    'Do not operate heavy machinery', 'May cause drowsiness'.
    A critical piece of information about environmental, health or physical
    risks or hazards that serve as caution to the user. For example 'Do not
    operate heavy machinery', 'May cause drowsiness', or 'Get medical
    advice/attention if you feel unwell'.
    """

    resource_type = Field("ClinicalUseDefinitionWarning", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="A coded or unformatted textual definition of this warning",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="A textual definition of this warning, with formatting",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClinicalUseDefinitionWarning`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "description", "code"]
