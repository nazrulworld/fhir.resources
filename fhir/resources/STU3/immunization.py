from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Immunization
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

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

    __resource_type__ = "Immunization"

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="date",
        title="Vaccination administration date",
        description="Date vaccine administered or was to be administered.",
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    doseQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="doseQuantity",
        title="Amount of vaccine administered",
        description="The quantity of vaccine product that was administered.",
        json_schema_extra={
            "element_property": True,
        },
    )

    encounter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="encounter",
        title="Encounter administered as part of",
        description=(
            "The visit or admission or other contact between patient and health "
            "care provider the immunization was performed as part of."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter"],
        },
    )

    expirationDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="expirationDate",
        title="Vaccine expiration date",
        description="Date vaccine batch expires.",
        json_schema_extra={
            "element_property": True,
        },
    )
    expirationDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_expirationDate", title="Extension field for ``expirationDate``."
    )

    explanation: fhirtypes.ImmunizationExplanationType | None = Field(  # type: ignore
        None,
        alias="explanation",
        title="Administration/non-administration reasons",
        description="Reasons why a vaccine was or was not administered.",
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business identifier",
        description="A unique identifier assigned to this immunization record.",
        json_schema_extra={
            "element_property": True,
        },
    )

    location: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="location",
        title="Where vaccination occurred",
        description=(
            "The service delivery location where the vaccine administration "
            "occurred."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    lotNumber: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="lotNumber",
        title="Vaccine lot number",
        description="Lot number of the  vaccine product.",
        json_schema_extra={
            "element_property": True,
        },
    )
    lotNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_lotNumber", title="Extension field for ``lotNumber``."
    )

    manufacturer: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="manufacturer",
        title="Vaccine manufacturer",
        description="Name of vaccine manufacturer.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    notGiven: bool | None = Field(  # type: ignore
        None,
        alias="notGiven",
        title="Flag for whether immunization was given",
        description="Indicates if the vaccination was or was not given.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    notGiven__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_notGiven", title="Extension field for ``notGiven``."
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="note",
        title="Vaccination notes",
        description=(
            "Extra information about the immunization that is not conveyed by the "
            "other attributes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    patient: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="patient",
        title="Who was immunized",
        description="The patient who either received or did not receive the immunization.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient"],
        },
    )

    practitioner: typing.List[fhirtypes.ImmunizationPractitionerType] | None = Field(  # type: ignore
        None,
        alias="practitioner",
        title="Who performed event",
        description="Indicates who or what performed the event.",
        json_schema_extra={
            "element_property": True,
        },
    )

    primarySource: bool | None = Field(  # type: ignore
        None,
        alias="primarySource",
        title="Indicates context the data was recorded in",
        description=(
            "An indication that the content of the record is based on information "
            "from the person who administered the vaccine. This reflects the "
            "context under which the data was originally recorded."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    primarySource__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_primarySource", title="Extension field for ``primarySource``."
    )

    reaction: typing.List[fhirtypes.ImmunizationReactionType] | None = Field(  # type: ignore
        None,
        alias="reaction",
        title="Details of a reaction that follows immunization",
        description=(
            "Categorical data indicating that an adverse event is associated in "
            "time to an immunization."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reportOrigin: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="reportOrigin",
        title="Indicates the source of a secondarily reported record",
        description=(
            "The source of the data when the report of the immunization event is "
            "not based on information from the person who administered the vaccine."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    route: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="route",
        title="How vaccine entered body",
        description="The path by which the vaccine product is taken into the body.",
        json_schema_extra={
            "element_property": True,
        },
    )

    site: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="site",
        title="Body site vaccine  was administered",
        description="Body site where vaccine was administered.",
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="completed | entered-in-error",
        description="Indicates the current status of the vaccination event.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["completed", "entered-in-error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    vaccinationProtocol: typing.List[fhirtypes.ImmunizationVaccinationProtocolType] | None = Field(  # type: ignore
        None,
        alias="vaccinationProtocol",
        title="What protocol was followed",
        description=(
            "Contains information about the protocol(s) under which the vaccine was"
            " administered."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    vaccineCode: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="vaccineCode",
        title="Vaccine product administered",
        description="Vaccine that was administered or was to be administered.",
        json_schema_extra={
            "element_property": True,
        },
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

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
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
        return required_fields


class ImmunizationExplanation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Administration/non-administration reasons.
    Reasons why a vaccine was or was not administered.
    """

    __resource_type__ = "ImmunizationExplanation"

    reason: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="reason",
        title="Why immunization occurred",
        description="Reasons why a vaccine was administered.",
        json_schema_extra={
            "element_property": True,
        },
    )

    reasonNotGiven: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="reasonNotGiven",
        title="Why immunization did not occur",
        description="Reason why a vaccine was not administered.",
        json_schema_extra={
            "element_property": True,
        },
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

    __resource_type__ = "ImmunizationPractitioner"

    actor: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="actor",
        title="Individual who was performing",
        description="The device, practitioner, etc. who performed the action.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner"],
        },
    )

    role: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="role",
        title="What type of performance was done",
        description=(
            "Describes the type of performance (e.g. ordering provider, "
            "administering provider, etc.)."
        ),
        json_schema_extra={
            "element_property": True,
        },
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

    __resource_type__ = "ImmunizationReaction"

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="date",
        title="When reaction started",
        description="Date of reaction to the immunization.",
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    detail: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="detail",
        title="Additional information on reaction",
        description="Details of the reaction.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Observation"],
        },
    )

    reported: bool | None = Field(  # type: ignore
        None,
        alias="reported",
        title="Indicates self-reported reaction",
        description="Self-reported indicator.",
        json_schema_extra={
            "element_property": True,
        },
    )
    reported__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
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

    __resource_type__ = "ImmunizationVaccinationProtocol"

    authority: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="authority",
        title="Who is responsible for protocol",
        description="Indicates the authority who published the protocol.  E.g. ACIP.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    description: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Details of vaccine protocol",
        description=(
            "Contains the description about the protocol under which the vaccine "
            "was administered."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    doseSequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="doseSequence",
        title="Dose number within series",
        description="Nominal position in a series.",
        json_schema_extra={
            "element_property": True,
        },
    )
    doseSequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_doseSequence", title="Extension field for ``doseSequence``."
    )

    doseStatus: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="doseStatus",
        title="Indicates if dose counts towards immunity",
        description=(
            'Indicates if the immunization event should "count" against  the '
            "protocol."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    doseStatusReason: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="doseStatusReason",
        title="Why dose does (not) count",
        description=(
            "Provides an explanation as to why an immunization event should or "
            "should not count against the protocol."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    series: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="series",
        title="Name of vaccine series",
        description=(
            "One possible path to achieve presumed immunity against a disease - "
            "within the context of an authority."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    series__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_series", title="Extension field for ``series``."
    )

    seriesDoses: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="seriesDoses",
        title="Recommended number of doses for immunity",
        description="The recommended number of doses to achieve immunity.",
        json_schema_extra={
            "element_property": True,
        },
    )
    seriesDoses__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_seriesDoses", title="Extension field for ``seriesDoses``."
    )

    targetDisease: typing.List[fhirtypes.CodeableConceptType] = Field(  # type: ignore
        ...,
        alias="targetDisease",
        title="Disease immunized against",
        description="The targeted disease.",
        json_schema_extra={
            "element_property": True,
        },
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
