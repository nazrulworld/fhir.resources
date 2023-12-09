# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationStatement
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


class MedicationStatement(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Record of medication being taken by a patient.
    A record of a medication that is being consumed by a patient.   A
    MedicationStatement may indicate that the patient may be taking the
    medication now or has taken the medication in the past or will be taking
    the medication in the future.  The source of this information can be the
    patient, significant other (such as a family member or spouse), or a
    clinician.  A common scenario where this information is captured is during
    the history taking process during a patient visit or stay.   The medication
    information may come from sources such as the patient's memory, from a
    prescription bottle,  or from a list of medications the patient, clinician
    or other party maintains.

    The primary difference between a medicationstatement and a
    medicationadministration is that the medication administration has complete
    administration information and is based on actual administration
    information from the person who administered the medication.  A
    medicationstatement is often, if not always, less specific.  There is no
    required date/time when the medication was administered, in fact we only
    know that a source has reported the patient is taking this medication,
    where details such as time, quantity, or rate or even medication product
    may be incomplete or missing or less precise.  As stated earlier, the
    Medication Statement information may come from the patient's memory, from a
    prescription bottle or from a list of medications the patient, clinician or
    other party maintains.  Medication administration is more formal and is not
    missing detailed information.

    The MedicationStatement resource was previously called MedicationStatement.
    """

    resource_type = Field("MedicationStatement", const=True)

    adherence: fhirtypes.MedicationStatementAdherenceType = Field(
        None,
        alias="adherence",
        title=(
            "Indicates whether the medication is or is not being consumed or "
            "administered"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    category: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="Type of medication statement",
        description=(
            "Type of medication statement (for example, drug classification like "
            "ATC, where meds would be administered, legal category of the "
            "medication.)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    dateAsserted: fhirtypes.DateTime = Field(
        None,
        alias="dateAsserted",
        title="When the usage was asserted?",
        description=(
            "The date when the Medication Statement was asserted by the information"
            " source."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    dateAsserted__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_dateAsserted", title="Extension field for ``dateAsserted``."
    )

    derivedFrom: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="derivedFrom",
        title="Link to information used to derive the MedicationStatement",
        description=(
            "Allows linking the MedicationStatement to the underlying "
            "MedicationRequest, or to other information that supports or is used to"
            " derive the MedicationStatement."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    dosage: typing.List[fhirtypes.DosageType] = Field(
        None,
        alias="dosage",
        title="Details of how medication is/was taken or should be taken",
        description="Indicates how the medication is/was or should be taken by the patient.",
        # if property is element of this resource.
        element_property=True,
    )

    effectiveDateTime: fhirtypes.DateTime = Field(
        None,
        alias="effectiveDateTime",
        title="The date/time or interval when the medication is/was/will be taken",
        description=(
            "The interval of time during which it is being asserted that the "
            "patient is/was/will be taking the medication (or was not taking, when "
            "the MedicationStatement.adherence element is Not Taking)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e effective[x]
        one_of_many="effective",
        one_of_many_required=False,
    )
    effectiveDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_effectiveDateTime",
        title="Extension field for ``effectiveDateTime``.",
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="The date/time or interval when the medication is/was/will be taken",
        description=(
            "The interval of time during which it is being asserted that the "
            "patient is/was/will be taking the medication (or was not taking, when "
            "the MedicationStatement.adherence element is Not Taking)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e effective[x]
        one_of_many="effective",
        one_of_many_required=False,
    )

    effectiveTiming: fhirtypes.TimingType = Field(
        None,
        alias="effectiveTiming",
        title="The date/time or interval when the medication is/was/will be taken",
        description=(
            "The interval of time during which it is being asserted that the "
            "patient is/was/will be taking the medication (or was not taking, when "
            "the MedicationStatement.adherence element is Not Taking)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e effective[x]
        one_of_many="effective",
        one_of_many_required=False,
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Encounter associated with MedicationStatement",
        description=(
            "The encounter that establishes the context for this "
            "MedicationStatement."
        ),
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
            "Identifiers associated with this Medication Statement that are defined"
            " by business processes and/or used to refer to it when a direct URL "
            "reference to the resource itself is not appropriate. They are business"
            " identifiers assigned to this resource by the performer or other "
            "systems and remain constant as the resource is updated and propagates "
            "from server to server."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    informationSource: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="informationSource",
        title=(
            "Person or organization that provided the information about the taking "
            "of this medication"
        ),
        description=(
            "The person or organization that provided the information about the "
            "taking of this medication. Note: Use derivedFrom when a "
            "MedicationStatement is derived from other resources, e.g. Claim or "
            "MedicationRequest."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "Practitioner",
            "PractitionerRole",
            "RelatedPerson",
            "Organization",
        ],
    )

    medication: fhirtypes.CodeableReferenceType = Field(
        ...,
        alias="medication",
        title="What medication was taken",
        description=(
            "Identifies the medication being administered. This is either a link to"
            " a resource representing the details of the medication or a simple "
            "attribute carrying a code that identifies the medication from a known "
            "list of medications."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Medication"],
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Further information about the usage",
        description=(
            "Provides extra information about the Medication Statement that is not "
            "conveyed by the other attributes."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    partOf: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title="Part of referenced event",
        description=(
            "A larger event of which this particular MedicationStatement is a "
            "component or step."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Procedure", "MedicationStatement"],
    )

    reason: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="reason",
        title="Reason for why the medication is being/was taken",
        description=(
            "A concept, Condition or observation that supports why the medication "
            "is being/was taken."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Condition", "Observation", "DiagnosticReport"],
    )

    relatedClinicalInformation: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="relatedClinicalInformation",
        title="Link to information relevant to the usage of a medication",
        description=(
            "Link to information that is relevant to a medication statement, for "
            "example, illicit drug use, gestational age, etc."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Observation", "Condition"],
    )

    renderedDosageInstruction: fhirtypes.Markdown = Field(
        None,
        alias="renderedDosageInstruction",
        title="Full representation of the dosage instructions",
        description=(
            "The full representation of the dose of the medication included in all "
            "dosage instructions.  To be used when multiple dosage instructions are"
            " included to represent complex dosing such as increasing or tapering "
            "doses."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    renderedDosageInstruction__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_renderedDosageInstruction",
        title="Extension field for ``renderedDosageInstruction``.",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="recorded | entered-in-error | draft",
        description="A code representing the status of recording the medication statement.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["recorded", "entered-in-error", "draft"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Who is/was taking  the medication",
        description="The person, animal or group who is/was taking the medication.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationStatement`` according specification,
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
            "partOf",
            "status",
            "category",
            "medication",
            "subject",
            "encounter",
            "effectiveDateTime",
            "effectivePeriod",
            "effectiveTiming",
            "dateAsserted",
            "informationSource",
            "derivedFrom",
            "reason",
            "note",
            "relatedClinicalInformation",
            "renderedDosageInstruction",
            "dosage",
            "adherence",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2163(
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
    def validate_one_of_many_2163(
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
            "effective": ["effectiveDateTime", "effectivePeriod", "effectiveTiming"]
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


class MedicationStatementAdherence(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Indicates whether the medication is or is not being consumed or
    administered.
    """

    resource_type = Field("MedicationStatementAdherence", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Type of adherence",
        description="Type of the adherence for the medication.",
        # if property is element of this resource.
        element_property=True,
    )

    reason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reason",
        title="Details of the reason for the current use of the medication",
        description="Captures the reason for the current use or adherence of a medication.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationStatementAdherence`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "reason"]
