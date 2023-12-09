# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Claim
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


class Claim(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Claim, Pre-determination or Pre-authorization.
    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """

    resource_type = Field("Claim", const=True)

    accident: fhirtypes.ClaimAccidentType = Field(
        None,
        alias="accident",
        title="Details about an accident",
        description="An accident which resulted in the need for healthcare services.",
        # if property is element of this resource.
        element_property=True,
    )

    billablePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="billablePeriod",
        title="Period for charge submission",
        description="The billable period for which charges are being submitted.",
        # if property is element of this resource.
        element_property=True,
    )

    careTeam: typing.List[fhirtypes.ClaimCareTeamType] = Field(
        None,
        alias="careTeam",
        title="Members of the care team",
        description=(
            "The members of the team who provided the overall service as well as "
            "their role and whether responsible and qualifications."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Creation date",
        description=(
            "The date when the enclosed suite of services were performed or "
            "completed."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
    )

    diagnosis: typing.List[fhirtypes.ClaimDiagnosisType] = Field(
        None,
        alias="diagnosis",
        title="List of Diagnosis",
        description="List of patient diagnosis for which care is sought.",
        # if property is element of this resource.
        element_property=True,
    )

    employmentImpacted: fhirtypes.PeriodType = Field(
        None,
        alias="employmentImpacted",
        title="Period unable to work",
        description=(
            "The start and optional end dates of when the patient was precluded "
            "from working due to the treatable condition(s)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    enterer: fhirtypes.ReferenceType = Field(
        None,
        alias="enterer",
        title="Author",
        description=(
            "Person who created the invoice/claim/pre-determination or pre-"
            "authorization."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    facility: fhirtypes.ReferenceType = Field(
        None,
        alias="facility",
        title="Servicing Facility",
        description="Facility where the services were provided.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    fundsReserve: fhirtypes.CodeableConceptType = Field(
        None,
        alias="fundsReserve",
        title="Funds requested to be reserved",
        description=(
            "In the case of a Pre-Determination/Pre-Authorization the provider may "
            "request that funds in the amount of the expected Benefit be reserved "
            "('Patient' or 'Provider') to pay for the Benefits determined on the "
            "subsequent claim(s). 'None' explicitly indicates no funds reserving is"
            " requested."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    hospitalization: fhirtypes.PeriodType = Field(
        None,
        alias="hospitalization",
        title="Period in hospital",
        description=(
            "The start and optional end dates of when the patient was confined to a"
            " treatment center."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Claim number",
        description=(
            "The business identifier for the instance: claim number, pre-"
            "determination or pre-authorization number."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    information: typing.List[fhirtypes.ClaimInformationType] = Field(
        None,
        alias="information",
        title=(
            "Exceptions, special considerations, the condition, situation, prior or"
            " concurrent issues"
        ),
        description=(
            "Additional information codes regarding exceptions, special "
            "considerations, the condition, situation, prior or concurrent issues. "
            "Often there are mutiple jurisdiction specific valuesets which are "
            "required."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    insurance: typing.List[fhirtypes.ClaimInsuranceType] = Field(
        None,
        alias="insurance",
        title="Insurance or medical plan",
        description="Financial instrument by which payment information for health care.",
        # if property is element of this resource.
        element_property=True,
    )

    insurer: fhirtypes.ReferenceType = Field(
        None,
        alias="insurer",
        title="Target",
        description="The Insurer who is target of the request.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    item: typing.List[fhirtypes.ClaimItemType] = Field(
        None,
        alias="item",
        title="Goods and Services",
        description="First tier of goods and services.",
        # if property is element of this resource.
        element_property=True,
    )

    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title="Responsible organization",
        description=(
            "The organization which is responsible for the bill, claim pre-"
            "determination, pre-authorization."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    originalPrescription: fhirtypes.ReferenceType = Field(
        None,
        alias="originalPrescription",
        title="Original prescription if superceded by fulfiller",
        description=(
            "Original prescription which has been superceded by this prescription "
            "to support the dispensing of pharmacy services, medications or "
            "products. For example, a physician may prescribe a medication which "
            "the pharmacy determines is contraindicated, or for which the patient "
            "has an intolerance, and therefor issues a new precription for an "
            "alternate medication which has the same theraputic intent. The "
            "prescription from the pharmacy becomes the 'prescription' and that "
            "from the physician becomes the 'original prescription'."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicationRequest"],
    )

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="The subject of the Products and Services",
        description="Patient Resource.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    payee: fhirtypes.ClaimPayeeType = Field(
        None,
        alias="payee",
        title="Party to be paid any benefits payable",
        description="The party to be reimbursed for the services.",
        # if property is element of this resource.
        element_property=True,
    )

    prescription: fhirtypes.ReferenceType = Field(
        None,
        alias="prescription",
        title="Prescription authorizing services or products",
        description="Prescription to support the dispensing of Pharmacy or Vision products.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicationRequest", "VisionPrescription"],
    )

    priority: fhirtypes.CodeableConceptType = Field(
        None,
        alias="priority",
        title="Desired processing priority",
        description="Immediate (STAT), best effort (NORMAL), deferred (DEFER).",
        # if property is element of this resource.
        element_property=True,
    )

    procedure: typing.List[fhirtypes.ClaimProcedureType] = Field(
        None,
        alias="procedure",
        title="Procedures performed",
        description=(
            "Ordered list of patient procedures performed to support the "
            "adjudication."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    provider: fhirtypes.ReferenceType = Field(
        None,
        alias="provider",
        title="Responsible provider",
        description=(
            "The provider which is responsible for the bill, claim pre-"
            "determination, pre-authorization."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    referral: fhirtypes.ReferenceType = Field(
        None,
        alias="referral",
        title="Treatment Referral",
        description=(
            "The referral resource which lists the date, practitioner, reason and "
            "other supporting information."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ReferralRequest"],
    )

    related: typing.List[fhirtypes.ClaimRelatedType] = Field(
        None,
        alias="related",
        title="Related Claims which may be revelant to processing this claimn",
        description=(
            "Other claims which are related to this claim such as prior claim "
            "versions or for related services."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="active | cancelled | draft | entered-in-error",
        description="The status of the resource instance.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "cancelled", "draft", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subType: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="subType",
        title="Finer grained claim type information",
        description=(
            "A finer grained suite of claim subtype codes which may convey "
            "Inpatient vs Outpatient and/or a specialty service. In the US the "
            "BillType."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    total: fhirtypes.MoneyType = Field(
        None,
        alias="total",
        title="Total claim cost",
        description="The total value of the claim.",
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type or discipline",
        description=(
            "The category of claim, eg, oral, pharmacy, vision, insitutional, "
            "professional."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    use: fhirtypes.Code = Field(
        None,
        alias="use",
        title="complete | proposed | exploratory | other",
        description=(
            "Complete (Bill or Claim), Proposed (Pre-Authorization), Exploratory "
            "(Pre-determination)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["complete", "proposed", "exploratory", "other"],
    )
    use__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_use", title="Extension field for ``use``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Claim`` according specification,
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
            "type",
            "subType",
            "use",
            "patient",
            "billablePeriod",
            "created",
            "enterer",
            "insurer",
            "provider",
            "organization",
            "priority",
            "fundsReserve",
            "related",
            "prescription",
            "originalPrescription",
            "payee",
            "referral",
            "facility",
            "careTeam",
            "information",
            "diagnosis",
            "procedure",
            "insurance",
            "accident",
            "employmentImpacted",
            "hospitalization",
            "item",
            "total",
        ]


class ClaimAccident(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details about an accident.
    An accident which resulted in the need for healthcare services.
    """

    resource_type = Field("ClaimAccident", const=True)

    date: fhirtypes.Date = Field(
        None,
        alias="date",
        title="When the accident occurred see information codes see information codes",
        description="Date of an accident which these services are addressing.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    locationAddress: fhirtypes.AddressType = Field(
        None,
        alias="locationAddress",
        title="Accident Place",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e location[x]
        one_of_many="location",
        one_of_many_required=False,
    )

    locationReference: fhirtypes.ReferenceType = Field(
        None,
        alias="locationReference",
        title="Accident Place",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e location[x]
        one_of_many="location",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="The nature of the accident",
        description="Type of accident: work, auto, etc.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimAccident`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "date",
            "type",
            "locationAddress",
            "locationReference",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1464(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("date", "date__ext")]
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
    def validate_one_of_many_1464(
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
        one_of_many_fields = {"location": ["locationAddress", "locationReference"]}
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


class ClaimCareTeam(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Members of the care team.
    The members of the team who provided the overall service as well as their
    role and whether responsible and qualifications.
    """

    resource_type = Field("ClaimCareTeam", const=True)

    provider: fhirtypes.ReferenceType = Field(
        ...,
        alias="provider",
        title="Provider individual or organization",
        description="Member of the team who provided the overall service.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Organization"],
    )

    qualification: fhirtypes.CodeableConceptType = Field(
        None,
        alias="qualification",
        title="Type, classification or Specialization",
        description="The qualification which is applicable for this service.",
        # if property is element of this resource.
        element_property=True,
    )

    responsible: bool = Field(
        None,
        alias="responsible",
        title="Billing provider",
        description=(
            "The party who is billing and responsible for the claimed good or "
            "service rendered to the patient."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    responsible__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_responsible", title="Extension field for ``responsible``."
    )

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="Role on the team",
        description=(
            "The lead, assisting or supervising practitioner and their discipline "
            "if a multidisiplinary team."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    sequence: fhirtypes.PositiveInt = Field(
        None,
        alias="sequence",
        title="Number to covey order of careTeam",
        description="Sequence of the careTeam which serves to order and provide a link.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimCareTeam`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "provider",
            "responsible",
            "role",
            "qualification",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1432(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sequence", "sequence__ext")]
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


class ClaimDiagnosis(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    List of Diagnosis.
    List of patient diagnosis for which care is sought.
    """

    resource_type = Field("ClaimDiagnosis", const=True)

    diagnosisCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="diagnosisCodeableConcept",
        title="Patient's diagnosis",
        description="The diagnosis.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e diagnosis[x]
        one_of_many="diagnosis",
        one_of_many_required=True,
    )

    diagnosisReference: fhirtypes.ReferenceType = Field(
        None,
        alias="diagnosisReference",
        title="Patient's diagnosis",
        description="The diagnosis.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e diagnosis[x]
        one_of_many="diagnosis",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Condition"],
    )

    packageCode: fhirtypes.CodeableConceptType = Field(
        None,
        alias="packageCode",
        title="Package billing code",
        description=(
            "The package billing code, for example DRG, based on the assigned "
            "grouping code system."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    sequence: fhirtypes.PositiveInt = Field(
        None,
        alias="sequence",
        title="Number to covey order of diagnosis",
        description="Sequence of diagnosis which serves to provide a link.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    type: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="Timing or nature of the diagnosis",
        description=(
            "The type of the Diagnosis, for example: admitting, primary, secondary,"
            " discharge."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimDiagnosis`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "diagnosisCodeableConcept",
            "diagnosisReference",
            "type",
            "packageCode",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1597(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sequence", "sequence__ext")]
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
    def validate_one_of_many_1597(
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
            "diagnosis": ["diagnosisCodeableConcept", "diagnosisReference"]
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


class ClaimInformation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Exceptions, special considerations, the condition, situation, prior or
    concurrent issues.
    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues. Often there are
    mutiple jurisdiction specific valuesets which are required.
    """

    resource_type = Field("ClaimInformation", const=True)

    category: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="category",
        title="General class of information",
        description=(
            "The general class of the information supplied: information; exception;"
            " accident, employment; onset, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type of information",
        description=(
            "System and code pertaining to the specific information regarding "
            "special conditions relating to the setting, treatment or patient  for "
            "which care is sought which may influence the adjudication."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    reason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reason",
        title="Reason associated with the information",
        description=(
            "For example, provides the reason for: the additional stay, or missing "
            "tooth or any other situation where a reason code is required in "
            "addition to the content."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    sequence: fhirtypes.PositiveInt = Field(
        None,
        alias="sequence",
        title="Information instance identifier",
        description="Sequence of the information element which serves to provide a link.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    timingDate: fhirtypes.Date = Field(
        None,
        alias="timingDate",
        title="When it occurred",
        description="The date when or period to which this information refers.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e timing[x]
        one_of_many="timing",
        one_of_many_required=False,
    )
    timingDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_timingDate", title="Extension field for ``timingDate``."
    )

    timingPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="timingPeriod",
        title="When it occurred",
        description="The date when or period to which this information refers.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e timing[x]
        one_of_many="timing",
        one_of_many_required=False,
    )

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="Additional Data or supporting information",
        description=(
            "Additional data or information such as resources, documents, images "
            "etc. including references to the data or the actual inclusion of the "
            "data."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="Additional Data or supporting information",
        description=(
            "Additional data or information such as resources, documents, images "
            "etc. including references to the data or the actual inclusion of the "
            "data."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueReference",
        title="Additional Data or supporting information",
        description=(
            "Additional data or information such as resources, documents, images "
            "etc. including references to the data or the actual inclusion of the "
            "data."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Additional Data or supporting information",
        description=(
            "Additional data or information such as resources, documents, images "
            "etc. including references to the data or the actual inclusion of the "
            "data."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimInformation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "category",
            "code",
            "timingDate",
            "timingPeriod",
            "valueString",
            "valueQuantity",
            "valueAttachment",
            "valueReference",
            "reason",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1821(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sequence", "sequence__ext")]
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
    def validate_one_of_many_1821(
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
            "timing": ["timingDate", "timingPeriod"],
            "value": [
                "valueAttachment",
                "valueQuantity",
                "valueReference",
                "valueString",
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


class ClaimInsurance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Insurance or medical plan.
    Financial instrument by which payment information for health care.
    """

    resource_type = Field("ClaimInsurance", const=True)

    businessArrangement: fhirtypes.String = Field(
        None,
        alias="businessArrangement",
        title="Business agreement",
        description=(
            "The contract number of a business agreement which describes the terms "
            "and conditions."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    businessArrangement__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_businessArrangement",
        title="Extension field for ``businessArrangement``.",
    )

    claimResponse: fhirtypes.ReferenceType = Field(
        None,
        alias="claimResponse",
        title="Adjudication results",
        description="The Coverages adjudication details.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ClaimResponse"],
    )

    coverage: fhirtypes.ReferenceType = Field(
        ...,
        alias="coverage",
        title="Insurance information",
        description="Reference to the program or plan identification, underwriter or payor.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Coverage"],
    )

    focal: bool = Field(
        None,
        alias="focal",
        title="Is the focal Coverage",
        description=(
            "A flag to indicate that this Coverage is the focus for adjudication. "
            "The Coverage against which the claim is to be adjudicated."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    focal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_focal", title="Extension field for ``focal``."
    )

    preAuthRef: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="preAuthRef",
        title="Pre-Authorization/Determination Reference",
        description="A list of references from the Insurer to which these services pertain.",
        # if property is element of this resource.
        element_property=True,
    )
    preAuthRef__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_preAuthRef", title="Extension field for ``preAuthRef``.")

    sequence: fhirtypes.PositiveInt = Field(
        None,
        alias="sequence",
        title="Service instance identifier",
        description=(
            "Sequence of coverage which serves to provide a link and convey "
            "coordination of benefit order."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimInsurance`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "focal",
            "coverage",
            "businessArrangement",
            "preAuthRef",
            "claimResponse",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1590(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("focal", "focal__ext"), ("sequence", "sequence__ext")]
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


class ClaimItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Goods and Services.
    First tier of goods and services.
    """

    resource_type = Field("ClaimItem", const=True)

    bodySite: fhirtypes.CodeableConceptType = Field(
        None,
        alias="bodySite",
        title="Service Location",
        description="Physical service site on the patient (limb, tooth, etc).",
        # if property is element of this resource.
        element_property=True,
    )

    careTeamLinkId: typing.List[fhirtypes.PositiveInt] = Field(
        None,
        alias="careTeamLinkId",
        title="Applicable careTeam members",
        description="CareTeam applicable for this service or product line.",
        # if property is element of this resource.
        element_property=True,
    )
    careTeamLinkId__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_careTeamLinkId", title="Extension field for ``careTeamLinkId``."
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type of service or product",
        description=(
            "Health Care Service Type Codes  to identify the classification of "
            "service or benefits."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    detail: typing.List[fhirtypes.ClaimItemDetailType] = Field(
        None,
        alias="detail",
        title="Additional items",
        description="Second tier of goods and services.",
        # if property is element of this resource.
        element_property=True,
    )

    diagnosisLinkId: typing.List[fhirtypes.PositiveInt] = Field(
        None,
        alias="diagnosisLinkId",
        title="Applicable diagnoses",
        description="Diagnosis applicable for this service or product line.",
        # if property is element of this resource.
        element_property=True,
    )
    diagnosisLinkId__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_diagnosisLinkId", title="Extension field for ``diagnosisLinkId``."
    )

    encounter: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="encounter",
        title="Encounters related to this billed item",
        description=(
            "A billed item may include goods or services provided in multiple "
            "encounters."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    factor: fhirtypes.Decimal = Field(
        None,
        alias="factor",
        title="Price scaling factor",
        description=(
            "A real number that represents a multiplier used in determining the "
            "overall value of services delivered and/or goods received. The concept"
            " of a Factor allows for a discount or surcharge multiplier to be "
            "applied to a monetary amount."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_factor", title="Extension field for ``factor``."
    )

    informationLinkId: typing.List[fhirtypes.PositiveInt] = Field(
        None,
        alias="informationLinkId",
        title="Applicable exception and supporting information",
        description=(
            "Exceptions, special conditions and supporting information pplicable "
            "for this service or product line."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    informationLinkId__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_informationLinkId",
        title="Extension field for ``informationLinkId``.",
    )

    locationAddress: fhirtypes.AddressType = Field(
        None,
        alias="locationAddress",
        title="Place of service",
        description="Where the service was provided.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e location[x]
        one_of_many="location",
        one_of_many_required=False,
    )

    locationCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="locationCodeableConcept",
        title="Place of service",
        description="Where the service was provided.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e location[x]
        one_of_many="location",
        one_of_many_required=False,
    )

    locationReference: fhirtypes.ReferenceType = Field(
        None,
        alias="locationReference",
        title="Place of service",
        description="Where the service was provided.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e location[x]
        one_of_many="location",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    modifier: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="modifier",
        title="Service/Product billing modifiers",
        description=(
            "Item typification or modifiers codes, eg for Oral whether the "
            "treatment is cosmetic or associated with TMJ, or for medical whether "
            "the treatment was outside the clinic or out of office hours."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    net: fhirtypes.MoneyType = Field(
        None,
        alias="net",
        title="Total item cost",
        description=(
            "The quantity times the unit price for an addittional service or "
            "product or charge. For example, the formula: unit Quantity * unit "
            "Price (Cost per Point) * factor Number  * points = net Amount. "
            "Quantity, factor and points are assumed to be 1 if not supplied."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    procedureLinkId: typing.List[fhirtypes.PositiveInt] = Field(
        None,
        alias="procedureLinkId",
        title="Applicable procedures",
        description="Procedures applicable for this service or product line.",
        # if property is element of this resource.
        element_property=True,
    )
    procedureLinkId__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_procedureLinkId", title="Extension field for ``procedureLinkId``."
    )

    programCode: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="programCode",
        title="Program specific reason for item inclusion",
        description=(
            "For programs which require reason codes for the inclusion or covering "
            "of this billed item under the program or sub-program."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Count of Products or Services",
        description="The number of repetitions of a service or product.",
        # if property is element of this resource.
        element_property=True,
    )

    revenue: fhirtypes.CodeableConceptType = Field(
        None,
        alias="revenue",
        title="Revenue or cost center code",
        description=(
            "The type of reveneu or cost center providing the product and/or "
            "service."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    sequence: fhirtypes.PositiveInt = Field(
        None,
        alias="sequence",
        title="Service instance",
        description="A service line number.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    service: fhirtypes.CodeableConceptType = Field(
        None,
        alias="service",
        title="Billing Code",
        description=(
            "If this is an actual service or product line, ie. not a Group, then "
            "use code to indicate the Professional Service or Product supplied (eg."
            " CTP, HCPCS,USCLS,ICD10, NCPDP,DIN,RXNorm,ACHI,CCI). If a grouping "
            "item then use a group code to indicate the type of thing being grouped"
            " eg. 'glasses' or 'compound'."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    servicedDate: fhirtypes.Date = Field(
        None,
        alias="servicedDate",
        title="Date or dates of Service",
        description=(
            "The date or dates when the enclosed suite of services were performed "
            "or completed."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e serviced[x]
        one_of_many="serviced",
        one_of_many_required=False,
    )
    servicedDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_servicedDate", title="Extension field for ``servicedDate``."
    )

    servicedPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="servicedPeriod",
        title="Date or dates of Service",
        description=(
            "The date or dates when the enclosed suite of services were performed "
            "or completed."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e serviced[x]
        one_of_many="serviced",
        one_of_many_required=False,
    )

    subSite: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="subSite",
        title="Service Sub-location",
        description="A region or surface of the site, eg. limb region or tooth surface(s).",
        # if property is element of this resource.
        element_property=True,
    )

    udi: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="udi",
        title="Unique Device Identifier",
        description="List of Unique Device Identifiers associated with this line item.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device"],
    )

    unitPrice: fhirtypes.MoneyType = Field(
        None,
        alias="unitPrice",
        title="Fee, charge or cost per point",
        description=(
            "If the item is a node then this is the fee for the product or service,"
            " otherwise this is the total of the fees for the children of the "
            "group."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimItem`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "careTeamLinkId",
            "diagnosisLinkId",
            "procedureLinkId",
            "informationLinkId",
            "revenue",
            "category",
            "service",
            "modifier",
            "programCode",
            "servicedDate",
            "servicedPeriod",
            "locationCodeableConcept",
            "locationAddress",
            "locationReference",
            "quantity",
            "unitPrice",
            "factor",
            "net",
            "udi",
            "bodySite",
            "subSite",
            "encounter",
            "detail",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1061(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sequence", "sequence__ext")]
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
    def validate_one_of_many_1061(
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
            "location": [
                "locationAddress",
                "locationCodeableConcept",
                "locationReference",
            ],
            "serviced": ["servicedDate", "servicedPeriod"],
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


class ClaimItemDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional items.
    Second tier of goods and services.
    """

    resource_type = Field("ClaimItemDetail", const=True)

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type of service or product",
        description=(
            "Health Care Service Type Codes  to identify the classification of "
            "service or benefits."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    factor: fhirtypes.Decimal = Field(
        None,
        alias="factor",
        title="Price scaling factor",
        description=(
            "A real number that represents a multiplier used in determining the "
            "overall value of services delivered and/or goods received. The concept"
            " of a Factor allows for a discount or surcharge multiplier to be "
            "applied to a monetary amount."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_factor", title="Extension field for ``factor``."
    )

    modifier: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="modifier",
        title="Service/Product billing modifiers",
        description=(
            "Item typification or modifiers codes, eg for Oral whether the "
            "treatment is cosmetic or associated with TMJ, or for medical whether "
            "the treatment was outside the clinic or out of office hours."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    net: fhirtypes.MoneyType = Field(
        None,
        alias="net",
        title="Total additional item cost",
        description=(
            "The quantity times the unit price for an addittional service or "
            "product or charge. For example, the formula: unit Quantity * unit "
            "Price (Cost per Point) * factor Number  * points = net Amount. "
            "Quantity, factor and points are assumed to be 1 if not supplied."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    programCode: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="programCode",
        title="Program specific reason for item inclusion",
        description=(
            "For programs which require reson codes for the inclusion, covering, of"
            " this billed item under the program or sub-program."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Count of Products or Services",
        description="The number of repetitions of a service or product.",
        # if property is element of this resource.
        element_property=True,
    )

    revenue: fhirtypes.CodeableConceptType = Field(
        None,
        alias="revenue",
        title="Revenue or cost center code",
        description=(
            "The type of reveneu or cost center providing the product and/or "
            "service."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    sequence: fhirtypes.PositiveInt = Field(
        None,
        alias="sequence",
        title="Service instance",
        description="A service line number.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    service: fhirtypes.CodeableConceptType = Field(
        None,
        alias="service",
        title="Billing Code",
        description=(
            "If this is an actual service or product line, ie. not a Group, then "
            "use code to indicate the Professional Service or Product supplied (eg."
            " CTP, HCPCS,USCLS,ICD10, NCPDP,DIN,ACHI,CCI). If a grouping item then "
            "use a group code to indicate the type of thing being grouped eg. "
            "'glasses' or 'compound'."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    subDetail: typing.List[fhirtypes.ClaimItemDetailSubDetailType] = Field(
        None,
        alias="subDetail",
        title="Additional items",
        description="Third tier of goods and services.",
        # if property is element of this resource.
        element_property=True,
    )

    udi: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="udi",
        title="Unique Device Identifier",
        description="List of Unique Device Identifiers associated with this line item.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device"],
    )

    unitPrice: fhirtypes.MoneyType = Field(
        None,
        alias="unitPrice",
        title="Fee, charge or cost per point",
        description=(
            "If the item is a node then this is the fee for the product or service,"
            " otherwise this is the total of the fees for the children of the "
            "group."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimItemDetail`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "revenue",
            "category",
            "service",
            "modifier",
            "programCode",
            "quantity",
            "unitPrice",
            "factor",
            "net",
            "udi",
            "subDetail",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1655(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sequence", "sequence__ext")]
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


class ClaimItemDetailSubDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional items.
    Third tier of goods and services.
    """

    resource_type = Field("ClaimItemDetailSubDetail", const=True)

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type of service or product",
        description=(
            "Health Care Service Type Codes  to identify the classification of "
            "service or benefits."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    factor: fhirtypes.Decimal = Field(
        None,
        alias="factor",
        title="Price scaling factor",
        description=(
            "A real number that represents a multiplier used in determining the "
            "overall value of services delivered and/or goods received. The concept"
            " of a Factor allows for a discount or surcharge multiplier to be "
            "applied to a monetary amount."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_factor", title="Extension field for ``factor``."
    )

    modifier: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="modifier",
        title="Service/Product billing modifiers",
        description=(
            "Item typification or modifiers codes, eg for Oral whether the "
            "treatment is cosmetic or associated with TMJ, or for medical whether "
            "the treatment was outside the clinic or out of office hours."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    net: fhirtypes.MoneyType = Field(
        None,
        alias="net",
        title="Net additional item cost",
        description=(
            "The quantity times the unit price for an addittional service or "
            "product or charge. For example, the formula: unit Quantity * unit "
            "Price (Cost per Point) * factor Number  * points = net Amount. "
            "Quantity, factor and points are assumed to be 1 if not supplied."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    programCode: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="programCode",
        title="Program specific reason for item inclusion",
        description=(
            "For programs which require reson codes for the inclusion, covering, of"
            " this billed item under the program or sub-program."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Count of Products or Services",
        description="The number of repetitions of a service or product.",
        # if property is element of this resource.
        element_property=True,
    )

    revenue: fhirtypes.CodeableConceptType = Field(
        None,
        alias="revenue",
        title="Revenue or cost center code",
        description=(
            "The type of reveneu or cost center providing the product and/or "
            "service."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    sequence: fhirtypes.PositiveInt = Field(
        None,
        alias="sequence",
        title="Service instance",
        description="A service line number.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    service: fhirtypes.CodeableConceptType = Field(
        None,
        alias="service",
        title="Billing Code",
        description=(
            "A code to indicate the Professional Service or Product supplied (eg. "
            "CTP, HCPCS,USCLS,ICD10, NCPDP,DIN,ACHI,CCI)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    udi: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="udi",
        title="Unique Device Identifier",
        description="List of Unique Device Identifiers associated with this line item.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device"],
    )

    unitPrice: fhirtypes.MoneyType = Field(
        None,
        alias="unitPrice",
        title="Fee, charge or cost per point",
        description="The fee for an addittional service or product or charge.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimItemDetailSubDetail`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "revenue",
            "category",
            "service",
            "modifier",
            "programCode",
            "quantity",
            "unitPrice",
            "factor",
            "net",
            "udi",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2548(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sequence", "sequence__ext")]
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


class ClaimPayee(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Party to be paid any benefits payable.
    The party to be reimbursed for the services.
    """

    resource_type = Field("ClaimPayee", const=True)

    party: fhirtypes.ReferenceType = Field(
        None,
        alias="party",
        title="Party to receive the payable",
        description="Party to be reimbursed: Subscriber, provider, other.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "Organization",
            "Patient",
            "RelatedPerson",
        ],
    )

    resourceType: fhirtypes.CodingType = Field(
        None,
        alias="resourceType",
        title="organization | patient | practitioner | relatedperson",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type of party: Subscriber, Provider, other",
        description="Type of Party to be reimbursed: Subscriber, provider, other.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimPayee`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "resourceType", "party"]


class ClaimProcedure(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Procedures performed.
    Ordered list of patient procedures performed to support the adjudication.
    """

    resource_type = Field("ClaimProcedure", const=True)

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="When the procedure was performed",
        description="Date and optionally time the procedure was performed .",
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    procedureCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="procedureCodeableConcept",
        title="Patient's list of procedures performed",
        description="The procedure code.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e procedure[x]
        one_of_many="procedure",
        one_of_many_required=True,
    )

    procedureReference: fhirtypes.ReferenceType = Field(
        None,
        alias="procedureReference",
        title="Patient's list of procedures performed",
        description="The procedure code.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e procedure[x]
        one_of_many="procedure",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Procedure"],
    )

    sequence: fhirtypes.PositiveInt = Field(
        None,
        alias="sequence",
        title="Procedure sequence for reference",
        description="Sequence of procedures which serves to order and provide a link.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimProcedure`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "date",
            "procedureCodeableConcept",
            "procedureReference",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1591(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sequence", "sequence__ext")]
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
    def validate_one_of_many_1591(
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
            "procedure": ["procedureCodeableConcept", "procedureReference"]
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


class ClaimRelated(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Related Claims which may be revelant to processing this claimn.
    Other claims which are related to this claim such as prior claim versions
    or for related services.
    """

    resource_type = Field("ClaimRelated", const=True)

    claim: fhirtypes.ReferenceType = Field(
        None,
        alias="claim",
        title="Reference to the related claim",
        description=(
            "Other claims which are related to this claim such as prior claim "
            "versions or for related services."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Claim"],
    )

    reference: fhirtypes.IdentifierType = Field(
        None,
        alias="reference",
        title="Related file or case reference",
        description=(
            "An alternate organizational reference to the case or file to which "
            "this particular claim pertains - eg Property/Casualy insurer claim # "
            "or Workers Compensation case # ."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    relationship: fhirtypes.CodeableConceptType = Field(
        None,
        alias="relationship",
        title="How the reference claim is related",
        description="For example prior or umbrella.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimRelated`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "claim",
            "relationship",
            "reference",
        ]
