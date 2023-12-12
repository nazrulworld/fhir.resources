# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/NutritionIntake
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class NutritionIntake(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Record of food or fluid being taken by a patient.
    A record of food or fluid that is being consumed by a patient.   A
    NutritionIntake may indicate that the patient may be consuming the food or
    fluid now or has consumed the food or fluid in the past.  The source of
    this information can be the patient, significant other (such as a family
    member or spouse), or a clinician.  A common scenario where this
    information is captured is during the history taking process during a
    patient visit or stay or through an app that tracks food or fluids
    consumed.   The consumption information may come from sources such as the
    patient's memory, from a nutrition label,  or from a clinician documenting
    observed intake.
    """

    resource_type = Field("NutritionIntake", const=True)

    basedOn: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="Fulfils plan, proposal or order",
        description=(
            "A plan, proposal or order that is fulfilled in whole or in part by "
            "this event."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["NutritionOrder", "CarePlan", "ServiceRequest"],
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Code representing an overall type of nutrition intake",
        description="Overall type of nutrition intake.",
        # if property is element of this resource.
        element_property=True,
    )

    consumedItem: typing.List[fhirtypes.NutritionIntakeConsumedItemType] = Field(
        ...,
        alias="consumedItem",
        title="What food or fluid product or item was consumed",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    derivedFrom: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="derivedFrom",
        title="Additional supporting information",
        description=(
            "Allows linking the NutritionIntake to the underlying NutritionOrder, "
            "or to other information, such as AllergyIntolerance, that supports or "
            "is used to derive the NutritionIntake."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Encounter associated with NutritionIntake",
        description="The encounter that establishes the context for this NutritionIntake.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="External identifier",
        description=(
            "Identifiers associated with this Nutrition Intake that are defined by "
            "business processes and/or used to refer to it when a direct URL "
            "reference to the resource itself is not appropriate. They are business"
            " identifiers assigned to this resource by the performer or other "
            "systems and remain constant as the resource is updated and propagates "
            "from server to server."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    ingredientLabel: typing.List[fhirtypes.NutritionIntakeIngredientLabelType] = Field(
        None,
        alias="ingredientLabel",
        title="Total nutrient for the whole meal, product, serving",
        description="Total nutrient amounts for the whole meal, product, serving, etc.",
        # if property is element of this resource.
        element_property=True,
    )

    instantiatesCanonical: typing.List[typing.Optional[fhirtypes.Canonical]] = Field(
        None,
        alias="instantiatesCanonical",
        title="Instantiates FHIR protocol or definition",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "ActivityDefinition",
            "ChargeItemDefinition",
            "ClinicalUseDefinition",
            "EventDefinition",
            "Measure",
            "MessageDefinition",
            "ObservationDefinition",
            "OperationDefinition",
            "PlanDefinition",
            "Questionnaire",
            "Requirements",
            "SubscriptionTopic",
            "TestPlan",
            "TestScript",
        ],
    )
    instantiatesCanonical__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_instantiatesCanonical",
        title="Extension field for ``instantiatesCanonical``.",
    )

    instantiatesUri: typing.List[typing.Optional[fhirtypes.Uri]] = Field(
        None,
        alias="instantiatesUri",
        title="Instantiates external protocol or definition",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    instantiatesUri__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_instantiatesUri", title="Extension field for ``instantiatesUri``."
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title="Where the intake occurred",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Further information about the consumption",
        description=(
            "Provides extra information about the Nutrition Intake that is not "
            "conveyed by the other attributes."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    occurrenceDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurrenceDateTime",
        title="The date/time or interval when the food or fluid is/was consumed",
        description=(
            "The interval of time during which it is being asserted that the "
            "patient is/was consuming the food or fluid."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_occurrenceDateTime",
        title="Extension field for ``occurrenceDateTime``.",
    )

    occurrencePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="occurrencePeriod",
        title="The date/time or interval when the food or fluid is/was consumed",
        description=(
            "The interval of time during which it is being asserted that the "
            "patient is/was consuming the food or fluid."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )

    partOf: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title="Part of referenced event",
        description="A larger event of which this particular event is a component or step.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["NutritionIntake", "Procedure", "Observation"],
    )

    performer: typing.List[fhirtypes.NutritionIntakePerformerType] = Field(
        None,
        alias="performer",
        title="Who was performed in the intake",
        description="Who performed the intake and how they were involved.",
        # if property is element of this resource.
        element_property=True,
    )

    reason: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="reason",
        title="Reason for why the food or fluid is /was consumed",
        description=(
            "A reason, Condition or observation for why the food or fluid is /was "
            "consumed."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Condition",
            "Observation",
            "DiagnosticReport",
            "DocumentReference",
        ],
    )

    recorded: fhirtypes.DateTime = Field(
        None,
        alias="recorded",
        title="When the intake was recorded",
        description=(
            "The date when the Nutrition Intake was asserted by the information "
            "source."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    recorded__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_recorded", title="Extension field for ``recorded``."
    )

    reportedBoolean: bool = Field(
        None,
        alias="reportedBoolean",
        title=(
            "Person or organization that provided the information about the "
            "consumption of this food or fluid"
        ),
        description=(
            "The person or organization that provided the information about the "
            "consumption of this food or fluid. Note: Use derivedFrom when a "
            "NutritionIntake is derived from other resources."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e reported[x]
        one_of_many="reported",
        one_of_many_required=False,
    )
    reportedBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_reportedBoolean", title="Extension field for ``reportedBoolean``."
    )

    reportedReference: fhirtypes.ReferenceType = Field(
        None,
        alias="reportedReference",
        title=(
            "Person or organization that provided the information about the "
            "consumption of this food or fluid"
        ),
        description=(
            "The person or organization that provided the information about the "
            "consumption of this food or fluid. Note: Use derivedFrom when a "
            "NutritionIntake is derived from other resources."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e reported[x]
        one_of_many="reported",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "RelatedPerson",
            "Practitioner",
            "PractitionerRole",
            "Organization",
        ],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title=(
            "preparation | in-progress | not-done | on-hold | stopped | completed |"
            " entered-in-error | unknown"
        ),
        description=(
            "A code representing the patient or other source's judgment about the "
            "state of the intake that this assertion is about.  Generally, this "
            "will be active or completed."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "preparation",
            "in-progress",
            "not-done",
            "on-hold",
            "stopped",
            "completed",
            "entered-in-error",
            "unknown",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    statusReason: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="statusReason",
        title="Reason for current status",
        description="Captures the reason for the current state of the NutritionIntake.",
        # if property is element of this resource.
        element_property=True,
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Who is/was consuming the food or fluid",
        description="The person, animal or group who is/was consuming the food or fluid.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``NutritionIntake`` according specification,
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
            "instantiatesCanonical",
            "instantiatesUri",
            "basedOn",
            "partOf",
            "status",
            "statusReason",
            "code",
            "subject",
            "encounter",
            "occurrenceDateTime",
            "occurrencePeriod",
            "recorded",
            "reportedBoolean",
            "reportedReference",
            "consumedItem",
            "ingredientLabel",
            "performer",
            "location",
            "derivedFrom",
            "reason",
            "note",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1755(
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
    def validate_one_of_many_1755(
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
            "occurrence": ["occurrenceDateTime", "occurrencePeriod"],
            "reported": ["reportedBoolean", "reportedReference"],
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


class NutritionIntakeConsumedItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What food or fluid product or item was consumed.
    """

    resource_type = Field("NutritionIntakeConsumedItem", const=True)

    amount: fhirtypes.QuantityType = Field(
        None,
        alias="amount",
        title="Quantity of the specified food",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    notConsumed: bool = Field(
        None,
        alias="notConsumed",
        title=(
            "Flag to indicate if the food or fluid item was refused or otherwise "
            "not consumed"
        ),
        description=(
            "Indicator when a patient is in a setting where it is helpful to know "
            "if food was not consumed, such as it was refused, held (as in tube "
            "feedings), or otherwise not provided. If a consumption is being "
            "recorded from an app, such as MyFitnessPal, this indicator will likely"
            " not be used."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    notConsumed__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_notConsumed", title="Extension field for ``notConsumed``."
    )

    notConsumedReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="notConsumedReason",
        title="Reason food or fluid was not consumed",
        description=(
            "Document the reason the food or fluid was not consumed, such as "
            "refused, held, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    nutritionProduct: fhirtypes.CodeableReferenceType = Field(
        ...,
        alias="nutritionProduct",
        title="Code that identifies the food or fluid product that was consumed",
        description=(
            "Identifies the food or fluid product that was consumed. This is "
            "potentially a link to a resource representing the details of the food "
            "product (TBD) or a simple attribute carrying a code that identifies "
            "the food from a known list of foods."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["NutritionProduct"],
    )

    rate: fhirtypes.QuantityType = Field(
        None,
        alias="rate",
        title="Rate at which enteral feeding was administered",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    schedule: fhirtypes.TimingType = Field(
        None,
        alias="schedule",
        title="Scheduled frequency of consumption",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="The type of food or fluid product",
        description=(
            "Indicates what a category of item that was consumed: e.g., food, "
            "fluid, enteral, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``NutritionIntakeConsumedItem`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "nutritionProduct",
            "schedule",
            "amount",
            "rate",
            "notConsumed",
            "notConsumedReason",
        ]


class NutritionIntakeIngredientLabel(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Total nutrient for the whole meal, product, serving.
    Total nutrient amounts for the whole meal, product, serving, etc.
    """

    resource_type = Field("NutritionIntakeIngredientLabel", const=True)

    amount: fhirtypes.QuantityType = Field(
        ...,
        alias="amount",
        title="Total amount of nutrient consumed",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    nutrient: fhirtypes.CodeableReferenceType = Field(
        ...,
        alias="nutrient",
        title="Total nutrient consumed",
        description=(
            "Total nutrient consumed. This could be a macronutrient (protein, fat, "
            "carbohydrate), or a vitamin and mineral."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Substance"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``NutritionIntakeIngredientLabel`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "nutrient", "amount"]


class NutritionIntakePerformer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who was performed in the intake.
    Who performed the intake and how they were involved.
    """

    resource_type = Field("NutritionIntakePerformer", const=True)

    actor: fhirtypes.ReferenceType = Field(
        ...,
        alias="actor",
        title="Who performed the intake",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "Organization",
            "CareTeam",
            "Patient",
            "Device",
            "RelatedPerson",
        ],
    )

    function: fhirtypes.CodeableConceptType = Field(
        None,
        alias="function",
        title="Type of performer",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``NutritionIntakePerformer`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "function", "actor"]
