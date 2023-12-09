# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Immunization
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


class Immunization(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Immunization event information.
    Describes the event of a patient being administered a vaccination or a
    record of a vaccination as reported by a patient, a clinician or another
    party and may include vaccine reaction information and what vaccination
    protocol was followed.
    """

    resource_type = Field("Immunization", const=True)

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Vaccination administration date",
        description="Date vaccine administered or was to be administered.",
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    doseQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="doseQuantity",
        title="Amount of vaccine administered",
        description="The quantity of vaccine product that was administered.",
        # if property is element of this resource.
        element_property=True,
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Encounter administered as part of",
        description=(
            "The visit or admission or other contact between patient and health "
            "care provider the immunization was performed as part of."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    expirationDate: fhirtypes.Date = Field(
        None,
        alias="expirationDate",
        title="Vaccine expiration date",
        description="Date vaccine batch expires.",
        # if property is element of this resource.
        element_property=True,
    )
    expirationDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_expirationDate", title="Extension field for ``expirationDate``."
    )

    explanation: fhirtypes.ImmunizationExplanationType = Field(
        None,
        alias="explanation",
        title="Administration/non-administration reasons",
        description="Reasons why a vaccine was or was not administered.",
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier",
        description="A unique identifier assigned to this immunization record.",
        # if property is element of this resource.
        element_property=True,
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title="Where vaccination occurred",
        description=(
            "The service delivery location where the vaccine administration "
            "occurred."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    lotNumber: fhirtypes.String = Field(
        None,
        alias="lotNumber",
        title="Vaccine lot number",
        description="Lot number of the  vaccine product.",
        # if property is element of this resource.
        element_property=True,
    )
    lotNumber__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lotNumber", title="Extension field for ``lotNumber``."
    )

    manufacturer: fhirtypes.ReferenceType = Field(
        None,
        alias="manufacturer",
        title="Vaccine manufacturer",
        description="Name of vaccine manufacturer.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    notGiven: bool = Field(
        None,
        alias="notGiven",
        title="Flag for whether immunization was given",
        description="Indicates if the vaccination was or was not given.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    notGiven__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_notGiven", title="Extension field for ``notGiven``."
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Vaccination notes",
        description=(
            "Extra information about the immunization that is not conveyed by the "
            "other attributes."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Who was immunized",
        description="The patient who either received or did not receive the immunization.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    practitioner: typing.List[fhirtypes.ImmunizationPractitionerType] = Field(
        None,
        alias="practitioner",
        title="Who performed event",
        description="Indicates who or what performed the event.",
        # if property is element of this resource.
        element_property=True,
    )

    primarySource: bool = Field(
        None,
        alias="primarySource",
        title="Indicates context the data was recorded in",
        description=(
            "An indication that the content of the record is based on information "
            "from the person who administered the vaccine. This reflects the "
            "context under which the data was originally recorded."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    primarySource__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_primarySource", title="Extension field for ``primarySource``."
    )

    reaction: typing.List[fhirtypes.ImmunizationReactionType] = Field(
        None,
        alias="reaction",
        title="Details of a reaction that follows immunization",
        description=(
            "Categorical data indicating that an adverse event is associated in "
            "time to an immunization."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    reportOrigin: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reportOrigin",
        title="Indicates the source of a secondarily reported record",
        description=(
            "The source of the data when the report of the immunization event is "
            "not based on information from the person who administered the vaccine."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    route: fhirtypes.CodeableConceptType = Field(
        None,
        alias="route",
        title="How vaccine entered body",
        description="The path by which the vaccine product is taken into the body.",
        # if property is element of this resource.
        element_property=True,
    )

    site: fhirtypes.CodeableConceptType = Field(
        None,
        alias="site",
        title="Body site vaccine  was administered",
        description="Body site where vaccine was administered.",
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="completed | entered-in-error",
        description="Indicates the current status of the vaccination event.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["completed", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    vaccinationProtocol: typing.List[
        fhirtypes.ImmunizationVaccinationProtocolType
    ] = Field(
        None,
        alias="vaccinationProtocol",
        title="What protocol was followed",
        description=(
            "Contains information about the protocol(s) under which the vaccine was"
            " administered."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    vaccineCode: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="vaccineCode",
        title="Vaccine product administered",
        description="Vaccine that was administered or was to be administered.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Immunization`` according specification,
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
            "notGiven",
            "vaccineCode",
            "patient",
            "encounter",
            "date",
            "primarySource",
            "reportOrigin",
            "location",
            "manufacturer",
            "lotNumber",
            "expirationDate",
            "site",
            "route",
            "doseQuantity",
            "practitioner",
            "note",
            "explanation",
            "reaction",
            "vaccinationProtocol",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1467(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("notGiven", "notGiven__ext"),
            ("primarySource", "primarySource__ext"),
            ("status", "status__ext"),
        ]
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


class ImmunizationExplanation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Administration/non-administration reasons.
    Reasons why a vaccine was or was not administered.
    """

    resource_type = Field("ImmunizationExplanation", const=True)

    reason: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reason",
        title="Why immunization occurred",
        description="Reasons why a vaccine was administered.",
        # if property is element of this resource.
        element_property=True,
    )

    reasonNotGiven: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonNotGiven",
        title="Why immunization did not occur",
        description="Reason why a vaccine was not administered.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImmunizationExplanation`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "reason", "reasonNotGiven"]


class ImmunizationPractitioner(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who performed event.
    Indicates who or what performed the event.
    """

    resource_type = Field("ImmunizationPractitioner", const=True)

    actor: fhirtypes.ReferenceType = Field(
        ...,
        alias="actor",
        title="Individual who was performing",
        description="The device, practitioner, etc. who performed the action.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="What type of performance was done",
        description=(
            "Describes the type of performance (e.g. ordering provider, "
            "administering provider, etc.)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImmunizationPractitioner`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "role", "actor"]


class ImmunizationReaction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details of a reaction that follows immunization.
    Categorical data indicating that an adverse event is associated in time to
    an immunization.
    """

    resource_type = Field("ImmunizationReaction", const=True)

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="When reaction started",
        description="Date of reaction to the immunization.",
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    detail: fhirtypes.ReferenceType = Field(
        None,
        alias="detail",
        title="Additional information on reaction",
        description="Details of the reaction.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Observation"],
    )

    reported: bool = Field(
        None,
        alias="reported",
        title="Indicates self-reported reaction",
        description="Self-reported indicator.",
        # if property is element of this resource.
        element_property=True,
    )
    reported__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_reported", title="Extension field for ``reported``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImmunizationReaction`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "date", "detail", "reported"]


class ImmunizationVaccinationProtocol(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What protocol was followed.
    Contains information about the protocol(s) under which the vaccine was
    administered.
    """

    resource_type = Field("ImmunizationVaccinationProtocol", const=True)

    authority: fhirtypes.ReferenceType = Field(
        None,
        alias="authority",
        title="Who is responsible for protocol",
        description="Indicates the authority who published the protocol.  E.g. ACIP.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Details of vaccine protocol",
        description=(
            "Contains the description about the protocol under which the vaccine "
            "was administered."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    doseSequence: fhirtypes.PositiveInt = Field(
        None,
        alias="doseSequence",
        title="Dose number within series",
        description="Nominal position in a series.",
        # if property is element of this resource.
        element_property=True,
    )
    doseSequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_doseSequence", title="Extension field for ``doseSequence``."
    )

    doseStatus: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="doseStatus",
        title="Indicates if dose counts towards immunity",
        description=(
            'Indicates if the immunization event should "count" against  the '
            "protocol."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    doseStatusReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="doseStatusReason",
        title="Why dose does (not) count",
        description=(
            "Provides an explanation as to why an immunization event should or "
            "should not count against the protocol."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    series: fhirtypes.String = Field(
        None,
        alias="series",
        title="Name of vaccine series",
        description=(
            "One possible path to achieve presumed immunity against a disease - "
            "within the context of an authority."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    series__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_series", title="Extension field for ``series``."
    )

    seriesDoses: fhirtypes.PositiveInt = Field(
        None,
        alias="seriesDoses",
        title="Recommended number of doses for immunity",
        description="The recommended number of doses to achieve immunity.",
        # if property is element of this resource.
        element_property=True,
    )
    seriesDoses__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_seriesDoses", title="Extension field for ``seriesDoses``."
    )

    targetDisease: typing.List[fhirtypes.CodeableConceptType] = Field(
        ...,
        alias="targetDisease",
        title="Disease immunized against",
        description="The targeted disease.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImmunizationVaccinationProtocol`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "doseSequence",
            "description",
            "authority",
            "series",
            "seriesDoses",
            "targetDisease",
            "doseStatus",
            "doseStatusReason",
        ]
