# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EncounterHistory
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


class EncounterHistory(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A record of significant events/milestones key data throughout the history
    of an Encounter.
    A record of significant events/milestones key data throughout the history
    of an Encounter, often tracked for specific purposes such as billing.
    """

    resource_type = Field("EncounterHistory", const=True)

    actualPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="actualPeriod",
        title=(
            "The actual start and end time associated with this set of values "
            "associated with the encounter"
        ),
        description=(
            "The start and end time associated with this set of values associated "
            "with the encounter, may be different to the planned times for various "
            "reasons."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    class_fhir: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="class",
        title="Classification of patient encounter",
        description=(
            "Concepts representing classification of patient encounter such as "
            "ambulatory (outpatient), inpatient, emergency, home health or others "
            "due to local variations."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="The Encounter associated with this set of historic values",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Identifier(s) by which this encounter is known",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    length: fhirtypes.DurationType = Field(
        None,
        alias="length",
        title="Actual quantity of time the encounter lasted (less time absent)",
        description=(
            "Actual quantity of time the encounter lasted. This excludes the time "
            "during leaves of absence.  When missing it is the time in between the "
            "start and end values."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    location: typing.List[fhirtypes.EncounterHistoryLocationType] = Field(
        None,
        alias="location",
        title="Location of the patient at this point in the encounter",
        description=(
            "The location of the patient at this point in the encounter, the "
            "multiple cardinality permits de-normalizing the levels of the location"
            " hierarchy, such as site/ward/room/bed."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    plannedEndDate: fhirtypes.DateTime = Field(
        None,
        alias="plannedEndDate",
        title="The planned end date/time (or discharge date) of the encounter",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    plannedEndDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_plannedEndDate", title="Extension field for ``plannedEndDate``."
    )

    plannedStartDate: fhirtypes.DateTime = Field(
        None,
        alias="plannedStartDate",
        title="The planned start date/time (or admission date) of the encounter",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    plannedStartDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_plannedStartDate",
        title="Extension field for ``plannedStartDate``.",
    )

    serviceType: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="serviceType",
        title="Specific type of service",
        description=(
            "Broad categorization of the service that is to be provided (e.g. "
            "cardiology)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["HealthcareService"],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title=(
            "planned | in-progress | on-hold | discharged | completed | cancelled |"
            " discontinued | entered-in-error | unknown"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "planned",
            "in-progress",
            "on-hold",
            "discharged",
            "completed",
            "cancelled",
            "discontinued",
            "entered-in-error",
            "unknown",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="The patient or group related to this encounter",
        description=(
            "The patient or group related to this encounter. In some use-cases the "
            "patient MAY not be present, such as a case meeting about a patient "
            "between several practitioners or a careteam."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group"],
    )

    subjectStatus: fhirtypes.CodeableConceptType = Field(
        None,
        alias="subjectStatus",
        title="The current status of the subject in relation to the Encounter",
        description=(
            "The subjectStatus value can be used to track the patient's status "
            "within the encounter. It details whether the patient has arrived or "
            "departed, has been triaged or is currently in a waiting status."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="Specific type of encounter",
        description=(
            "Specific type of encounter (e.g. e-mail consultation, surgical day-"
            "care, skilled nursing, rehabilitation)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EncounterHistory`` according specification,
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
            "encounter",
            "identifier",
            "status",
            "class",
            "type",
            "serviceType",
            "subject",
            "subjectStatus",
            "actualPeriod",
            "plannedStartDate",
            "plannedEndDate",
            "length",
            "location",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1891(
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


class EncounterHistoryLocation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Location of the patient at this point in the encounter.
    The location of the patient at this point in the encounter, the multiple
    cardinality permits de-normalizing the levels of the location hierarchy,
    such as site/ward/room/bed.
    """

    resource_type = Field("EncounterHistoryLocation", const=True)

    form: fhirtypes.CodeableConceptType = Field(
        None,
        alias="form",
        title=(
            "The physical type of the location (usually the level in the location "
            "hierarchy - bed, room, ward, virtual etc.)"
        ),
        description=(
            "This will be used to specify the required levels (bed/ward/room/etc.) "
            "desired to be recorded to simplify either messaging or query."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    location: fhirtypes.ReferenceType = Field(
        ...,
        alias="location",
        title="Location the encounter takes place",
        description="The location where the encounter takes place.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EncounterHistoryLocation`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "location", "form"]
