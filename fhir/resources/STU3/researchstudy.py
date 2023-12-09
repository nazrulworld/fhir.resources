# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ResearchStudy
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class ResearchStudy(domainresource.DomainResource):
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

    resource_type = Field("ResearchStudy", const=True)

    arm: typing.List[fhirtypes.ResearchStudyArmType] = Field(
        None,
        alias="arm",
        title="Defined path through the study for a subject",
        description=(
            "Describes an expected sequence of events for one of the participants "
            "of a study.  E.g. Exposure to drug A, wash-out, exposure to drug B, "
            "wash-out, follow-up."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    category: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="Classifications for the study",
        description=(
            "Codes categorizing the type of study such as investigational vs. "
            "observational, type of blinding, type of randomization, safety vs. "
            "efficacy, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    contact: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="Contact details for the study",
        description=(
            "Contact details to assist a user in learning more about or engaging "
            "with the study."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="What this is study doing",
        description="A full description of how the study is being conducted.",
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    enrollment: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="enrollment",
        title="Inclusion & exclusion criteria",
        description=(
            "Reference to a Group that defines the criteria for and quantity of "
            'subjects participating in the study.  E.g. " 200 female Europeans '
            'between the ages of 20 and 45 with early onset diabetes".'
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Group"],
    )

    focus: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="focus",
        title="Drugs, devices, conditions, etc. under study",
        description=(
            "The condition(s), medication(s), food(s), therapy(ies), device(s) or "
            "other concerns or interventions that the study is seeking to gain more"
            " information about."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier for study",
        description=(
            "Identifiers assigned to this research study by the sponsor or other "
            "systems."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Geographic region(s) for study",
        description=(
            "Indicates a country, state or other region where the study is taking "
            "place."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    keyword: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="keyword",
        title="Used to search for the study",
        description="Key terms to aid in searching for or filtering the study.",
        # if property is element of this resource.
        element_property=True,
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Comments made about the event",
        description=(
            "Comments made about the event by the performer, subject or other "
            "participants."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    partOf: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title="Part of larger study",
        description=(
            "A larger research study of which this particular study is a component "
            "or step."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ResearchStudy"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="When the study began and ended",
        description=(
            "Identifies the start date and the expected (or actual, depending on "
            "status) end date for the study."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    principalInvestigator: fhirtypes.ReferenceType = Field(
        None,
        alias="principalInvestigator",
        title="The individual responsible for the study",
        description=(
            "Indicates the individual who has primary oversite of the execution of "
            "the study."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    protocol: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="protocol",
        title="Steps followed in executing study",
        description=(
            "The set of steps expected to be performed as part of the execution of "
            "the study."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["PlanDefinition"],
    )

    reasonStopped: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reasonStopped",
        title="Reason for terminating study early",
        description=(
            "A description and/or code explaining the premature termination of the "
            "study."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    relatedArtifact: typing.List[fhirtypes.RelatedArtifactType] = Field(
        None,
        alias="relatedArtifact",
        title="References and dependencies",
        description="Citations, references and other related documents.",
        # if property is element of this resource.
        element_property=True,
    )

    site: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="site",
        title="Location involved in study execution",
        description=(
            "Clinic, hospital or other healthcare location that is participating in"
            " the study."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    sponsor: fhirtypes.ReferenceType = Field(
        None,
        alias="sponsor",
        title="Organization responsible for the study",
        description="The organization responsible for the execution of the study.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title=(
            "draft | in-progress | suspended | stopped | completed | entered-in-"
            "error"
        ),
        description="The current state of the study.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "draft",
            "in-progress",
            "suspended",
            "stopped",
            "completed",
            "entered-in-error",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Name for this study",
        description="A short, descriptive user-friendly label for the study.",
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ResearchStudy`` according specification,
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
            "title",
            "protocol",
            "partOf",
            "status",
            "category",
            "focus",
            "contact",
            "relatedArtifact",
            "keyword",
            "jurisdiction",
            "description",
            "enrollment",
            "period",
            "sponsor",
            "principalInvestigator",
            "site",
            "reasonStopped",
            "note",
            "arm",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1553(
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


class ResearchStudyArm(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Defined path through the study for a subject.
    Describes an expected sequence of events for one of the participants of a
    study.  E.g. Exposure to drug A, wash-out, exposure to drug B, wash-out,
    follow-up.
    """

    resource_type = Field("ResearchStudyArm", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Categorization of study arm",
        description=(
            "Categorization of study arm, e.g. experimental, active comparator, "
            "placebo comparater."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Short explanation of study path",
        description=(
            "A succinct description of the path through the study that would be "
            "followed by a subject adhering to this arm."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Label for study arm",
        description="Unique, human-readable label for this arm of the study.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ResearchStudyArm`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "name", "code", "description"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1829(
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
