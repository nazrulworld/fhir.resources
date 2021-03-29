# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AllergyIntolerance
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class AllergyIntolerance(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Allergy or Intolerance (generally: Risk of adverse reaction to a substance).
    Risk of harmful or undesirable, physiological response which is unique to
    an individual and associated with exposure to a substance.
    """

    resource_type = Field("AllergyIntolerance", const=True)

    assertedDate: fhirtypes.DateTime = Field(
        None,
        alias="assertedDate",
        title="Date record was believed accurate",
        description=(
            "The date on which the existance of the AllergyIntolerance was first "
            "asserted or acknowledged."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    assertedDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_assertedDate", title="Extension field for ``assertedDate``."
    )

    asserter: fhirtypes.ReferenceType = Field(
        None,
        alias="asserter",
        title="Source of the information about the allergy",
        description="The source of the information about the allergy that is recorded.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "RelatedPerson", "Practitioner"],
    )

    category: typing.List[fhirtypes.Code] = Field(
        None,
        alias="category",
        title="food | medication | environment | biologic",
        description="Category of the identified substance.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["food", "medication", "environment", "biologic"],
    )
    category__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_category", title="Extension field for ``category``.")

    clinicalStatus: fhirtypes.Code = Field(
        None,
        alias="clinicalStatus",
        title="active | inactive | resolved",
        description="The clinical status of the allergy or intolerance.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "inactive", "resolved"],
    )
    clinicalStatus__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_clinicalStatus", title="Extension field for ``clinicalStatus``."
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Code that identifies the allergy or intolerance",
        description=(
            "Code for an allergy or intolerance statement (either a positive or a "
            "negated/excluded statement).  This may be a code for a substance or "
            "pharmaceutical product that is considered to be responsible for the "
            'adverse reaction risk (e.g., "Latex"), an allergy or intolerance '
            'condition (e.g., "Latex allergy"), or a negated/excluded code for a '
            'specific substance or class (e.g., "No latex allergy") or a general or'
            ' categorical negated statement (e.g.,  "No known allergy", "No known '
            'drug allergies").'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    criticality: fhirtypes.Code = Field(
        None,
        alias="criticality",
        title="low | high | unable-to-assess",
        description=(
            "Estimate of the potential clinical harm, or seriousness, of the "
            "reaction to the identified substance."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["low", "high", "unable-to-assess"],
    )
    criticality__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_criticality", title="Extension field for ``criticality``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="External ids for this item",
        description=(
            "This records identifiers associated with this allergy/intolerance "
            "concern that are defined by business processes and/or used to refer to"
            " it when a direct URL reference to the resource itself is not "
            "appropriate (e.g. in CDA documents, or in written / printed "
            "documentation)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    lastOccurrence: fhirtypes.DateTime = Field(
        None,
        alias="lastOccurrence",
        title="Date(/time) of last known occurrence of a reaction",
        description=(
            "Represents the date and/or time of the last known occurrence of a "
            "reaction event."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    lastOccurrence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastOccurrence", title="Extension field for ``lastOccurrence``."
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Additional text not captured in other fields",
        description=(
            "Additional narrative about the propensity for the Adverse Reaction, "
            "not captured in other fields."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    onsetAge: fhirtypes.AgeType = Field(
        None,
        alias="onsetAge",
        title="When allergy or intolerance was identified",
        description=(
            "Estimated or actual date,  date-time, or age when allergy or "
            "intolerance was identified."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e onset[x]
        one_of_many="onset",
        one_of_many_required=False,
    )

    onsetDateTime: fhirtypes.DateTime = Field(
        None,
        alias="onsetDateTime",
        title="When allergy or intolerance was identified",
        description=(
            "Estimated or actual date,  date-time, or age when allergy or "
            "intolerance was identified."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e onset[x]
        one_of_many="onset",
        one_of_many_required=False,
    )
    onsetDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_onsetDateTime", title="Extension field for ``onsetDateTime``."
    )

    onsetPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="onsetPeriod",
        title="When allergy or intolerance was identified",
        description=(
            "Estimated or actual date,  date-time, or age when allergy or "
            "intolerance was identified."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e onset[x]
        one_of_many="onset",
        one_of_many_required=False,
    )

    onsetRange: fhirtypes.RangeType = Field(
        None,
        alias="onsetRange",
        title="When allergy or intolerance was identified",
        description=(
            "Estimated or actual date,  date-time, or age when allergy or "
            "intolerance was identified."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e onset[x]
        one_of_many="onset",
        one_of_many_required=False,
    )

    onsetString: fhirtypes.String = Field(
        None,
        alias="onsetString",
        title="When allergy or intolerance was identified",
        description=(
            "Estimated or actual date,  date-time, or age when allergy or "
            "intolerance was identified."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e onset[x]
        one_of_many="onset",
        one_of_many_required=False,
    )
    onsetString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_onsetString", title="Extension field for ``onsetString``."
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Who the sensitivity is for",
        description="The patient who has the allergy or intolerance.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    reaction: typing.List[fhirtypes.AllergyIntoleranceReactionType] = Field(
        None,
        alias="reaction",
        title="Adverse Reaction Events linked to exposure to substance",
        description=(
            "Details about each adverse reaction event linked to exposure to the "
            "identified substance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    recorder: fhirtypes.ReferenceType = Field(
        None,
        alias="recorder",
        title="Who recorded the sensitivity",
        description=(
            "Individual who recorded the record and takes responsibility for its "
            "content."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Patient"],
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="allergy | intolerance - Underlying mechanism (if known)",
        description=(
            "Identification of the underlying physiological mechanism for the "
            "reaction risk."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["allergy", "intolerance"],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    verificationStatus: fhirtypes.Code = Field(
        None,
        alias="verificationStatus",
        title="unconfirmed | confirmed | refuted | entered-in-error",
        description=(
            "Assertion about certainty associated with the propensity, or potential"
            " risk, of a reaction to the identified substance (including "
            "pharmaceutical product)."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["unconfirmed", "confirmed", "refuted", "entered-in-error"],
    )
    verificationStatus__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_verificationStatus",
        title="Extension field for ``verificationStatus``.",
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AllergyIntolerance`` according specification,
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
            "clinicalStatus",
            "verificationStatus",
            "type",
            "category",
            "criticality",
            "code",
            "patient",
            "onsetDateTime",
            "onsetAge",
            "onsetPeriod",
            "onsetRange",
            "onsetString",
            "assertedDate",
            "recorder",
            "asserter",
            "lastOccurrence",
            "note",
            "reaction",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2026(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("verificationStatus", "verificationStatus__ext")]
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
    def validate_one_of_many_2026(
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
            "onset": [
                "onsetAge",
                "onsetDateTime",
                "onsetPeriod",
                "onsetRange",
                "onsetString",
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


class AllergyIntoleranceReaction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Adverse Reaction Events linked to exposure to substance.
    Details about each adverse reaction event linked to exposure to the
    identified substance.
    """

    resource_type = Field("AllergyIntoleranceReaction", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Description of the event as a whole",
        description=(
            "Text description about the reaction as a whole, including details of "
            "the manifestation if required."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    exposureRoute: fhirtypes.CodeableConceptType = Field(
        None,
        alias="exposureRoute",
        title="How the subject was exposed to the substance",
        description=(
            "Identification of the route by which the subject was exposed to the "
            "substance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    manifestation: typing.List[fhirtypes.CodeableConceptType] = Field(
        ...,
        alias="manifestation",
        title="Clinical symptoms/signs associated with the Event",
        description=(
            "Clinical symptoms and/or signs that are observed or associated with "
            "the adverse reaction event."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Text about event not captured in other fields",
        description=(
            "Additional text about the adverse reaction event not captured in other"
            " fields."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    onset: fhirtypes.DateTime = Field(
        None,
        alias="onset",
        title="Date(/time) when manifestations showed",
        description="Record of the date and/or time of the onset of the Reaction.",
        # if property is element of this resource.
        element_property=True,
    )
    onset__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_onset", title="Extension field for ``onset``."
    )

    severity: fhirtypes.Code = Field(
        None,
        alias="severity",
        title="mild | moderate | severe (of event as a whole)",
        description=(
            "Clinical assessment of the severity of the reaction event as a whole, "
            "potentially considering multiple different manifestations."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["mild", "moderate", "severe"],
    )
    severity__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_severity", title="Extension field for ``severity``."
    )

    substance: fhirtypes.CodeableConceptType = Field(
        None,
        alias="substance",
        title=(
            "Specific substance or pharmaceutical product considered to be "
            "responsible for event"
        ),
        description=(
            "Identification of the specific substance (or pharmaceutical product) "
            "considered to be responsible for the Adverse Reaction event. Note: the"
            " substance for a specific reaction may be different from the substance"
            " identified as the cause of the risk, but it must be consistent with "
            "it. For instance, it may be a more specific substance (e.g. a brand "
            "medication) or a composite product that includes the identified "
            "substance. It must be clinically safe to only process the 'code' and "
            "ignore the 'reaction.substance'."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AllergyIntoleranceReaction`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "substance",
            "manifestation",
            "description",
            "onset",
            "severity",
            "exposureRoute",
            "note",
        ]
