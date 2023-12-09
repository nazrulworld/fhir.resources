# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ResearchSubject
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import domainresource, fhirtypes


class ResearchSubject(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Investigation to increase healthcare-related patient-independent knowledge.
    A process where a researcher or organization plans and then executes a
    series of steps intended to increase the field of healthcare-related
    knowledge.  This includes studies of safety, efficacy, comparative
    effectiveness and other information about medications, devices, therapies
    and other interventional and investigative techniques.  A ResearchStudy
    involves the gathering of information about human or animal subjects.
    """

    resource_type = Field("ResearchSubject", const=True)

    actualArm: fhirtypes.String = Field(
        None,
        alias="actualArm",
        title="What path was followed",
        description=(
            "The name of the arm in the study the subject actually followed as part"
            " of this study."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    actualArm__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_actualArm", title="Extension field for ``actualArm``."
    )

    assignedArm: fhirtypes.String = Field(
        None,
        alias="assignedArm",
        title="What path should be followed",
        description=(
            "The name of the arm in the study the subject is expected to follow as "
            "part of this study."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    assignedArm__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_assignedArm", title="Extension field for ``assignedArm``."
    )

    consent: fhirtypes.ReferenceType = Field(
        None,
        alias="consent",
        title="Agreement to participate in study",
        description=(
            "A record of the patient's informed agreement to participate in the "
            "study."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Consent"],
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Business Identifier for research subject",
        description=(
            "Identifiers assigned to this research study by the sponsor or other "
            "systems."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    individual: fhirtypes.ReferenceType = Field(
        ...,
        alias="individual",
        title="Who is part of study",
        description="The record of the person or animal who is involved in the study.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Start and end of participation",
        description=(
            "The dates the subject began and ended their participation in the " "study."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="candidate | enrolled | active | suspended | withdrawn | completed",
        description="The current state of the subject.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "candidate",
            "enrolled",
            "active",
            "suspended",
            "withdrawn",
            "completed",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    study: fhirtypes.ReferenceType = Field(
        ...,
        alias="study",
        title="Study subject is part of",
        description="Reference to the study the subject is participating in.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ResearchStudy"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ResearchSubject`` according specification,
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
            "period",
            "study",
            "individual",
            "assignedArm",
            "actualArm",
            "consent",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1731(
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
