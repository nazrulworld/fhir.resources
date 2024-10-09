from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Immunization
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Immunization(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Immunization event information.
    Describes the event of a patient being administered a vaccine or a record
    of an immunization as reported by a patient, a clinician or another party.
    """

    __resource_type__ = "Immunization"

    doseQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="doseQuantity",
        title="Amount of vaccine administered",
        description="The quantity of vaccine product that was administered.",
        json_schema_extra={
            "element_property": True,
        },
    )

    education: typing.List[fhirtypes.ImmunizationEducationType] | None = Field(  # type: ignore
        None,
        alias="education",
        title="Educational material presented to patient",
        description=(
            "Educational material presented to the patient (or guardian) at the "
            "time of vaccine administration."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    encounter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="encounter",
        title="Encounter immunization was part of",
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

    fundingSource: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="fundingSource",
        title="Funding source for the vaccine",
        description=(
            "Indicates the source of the vaccine actually administered. This may be"
            " different than the patient eligibility (e.g. the patient may be "
            "eligible for a publically purchased vaccine but due to inventory "
            "issues, vaccine purchased with private funds was actually "
            "administered)."
        ),
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

    isSubpotent: bool | None = Field(  # type: ignore
        None,
        alias="isSubpotent",
        title="Dose potency",
        description=(
            "Indication if a dose is considered to be subpotent. By default, a dose"
            " should be considered to be potent."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    isSubpotent__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_isSubpotent", title="Extension field for ``isSubpotent``."
    )

    location: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="location",
        title="Where immunization occurred",
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

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="note",
        title="Additional immunization notes",
        description=(
            "Extra information about the immunization that is not conveyed by the "
            "other attributes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    occurrenceDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="occurrenceDateTime",
        title="Vaccine administration date",
        description="Date vaccine administered or was to be administered.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e occurrence[x]
            "one_of_many": "occurrence",
            "one_of_many_required": True,
        },
    )
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_occurrenceDateTime",
        title="Extension field for ``occurrenceDateTime``.",
    )

    occurrenceString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="occurrenceString",
        title="Vaccine administration date",
        description="Date vaccine administered or was to be administered.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e occurrence[x]
            "one_of_many": "occurrence",
            "one_of_many_required": True,
        },
    )
    occurrenceString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_occurrenceString",
        title="Extension field for ``occurrenceString``.",
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

    performer: typing.List[fhirtypes.ImmunizationPerformerType] | None = Field(  # type: ignore
        None,
        alias="performer",
        title="Who performed event",
        description="Indicates who performed the immunization event.",
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
        },
    )
    primarySource__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_primarySource", title="Extension field for ``primarySource``."
    )

    programEligibility: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="programEligibility",
        title="Patient eligibility for a vaccination program",
        description="Indicates a patient's eligibility for a funding program.",
        json_schema_extra={
            "element_property": True,
        },
    )

    protocolApplied: typing.List[fhirtypes.ImmunizationProtocolAppliedType] | None = Field(  # type: ignore
        None,
        alias="protocolApplied",
        title="Protocol followed by the provider",
        description=(
            "The protocol (set of recommendations) being followed by the provider "
            "who administered the dose."
        ),
        json_schema_extra={
            "element_property": True,
        },
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

    reasonCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="reasonCode",
        title="Why immunization occurred",
        description="Reasons why the vaccine was administered.",
        json_schema_extra={
            "element_property": True,
        },
    )

    reasonReference: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="reasonReference",
        title="Why immunization occurred",
        description=(
            "Condition, Observation or DiagnosticReport that supports why the "
            "immunization was administered."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Condition", "Observation", "DiagnosticReport"],
        },
    )

    recorded: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="recorded",
        title="When the immunization was first captured in the subject's record",
        description=(
            "The date the occurrence of the immunization was first captured in the "
            "record - potentially significantly after the occurrence of the event."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    recorded__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_recorded", title="Extension field for ``recorded``."
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
        title="completed | entered-in-error | not-done",
        description="Indicates the current status of the immunization event.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["completed", "entered-in-error", "not-done"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    statusReason: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="statusReason",
        title="Reason not done",
        description="Indicates the reason the immunization event was not performed.",
        json_schema_extra={
            "element_property": True,
        },
    )

    subpotentReason: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="subpotentReason",
        title="Reason for being subpotent",
        description="Reason why a dose is considered to be subpotent.",
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
            "statusReason",
            "vaccineCode",
            "patient",
            "encounter",
            "occurrenceDateTime",
            "occurrenceString",
            "recorded",
            "primarySource",
            "reportOrigin",
            "location",
            "manufacturer",
            "lotNumber",
            "expirationDate",
            "site",
            "route",
            "doseQuantity",
            "performer",
            "note",
            "reasonCode",
            "reasonReference",
            "isSubpotent",
            "subpotentReason",
            "education",
            "programEligibility",
            "fundingSource",
            "reaction",
            "protocolApplied",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        return required_fields

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
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
        one_of_many_fields = {"occurrence": ["occurrenceDateTime", "occurrenceString"]}
        return one_of_many_fields


class ImmunizationEducation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Educational material presented to patient.
    Educational material presented to the patient (or guardian) at the time of
    vaccine administration.
    """

    __resource_type__ = "ImmunizationEducation"

    documentType: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="documentType",
        title="Educational material document identifier",
        description="Identifier of the material presented to the patient.",
        json_schema_extra={
            "element_property": True,
        },
    )
    documentType__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_documentType", title="Extension field for ``documentType``."
    )

    presentationDate: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="presentationDate",
        title="Educational material presentation date",
        description="Date the educational material was given to the patient.",
        json_schema_extra={
            "element_property": True,
        },
    )
    presentationDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_presentationDate",
        title="Extension field for ``presentationDate``.",
    )

    publicationDate: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="publicationDate",
        title="Educational material publication date",
        description="Date the educational material was published.",
        json_schema_extra={
            "element_property": True,
        },
    )
    publicationDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_publicationDate", title="Extension field for ``publicationDate``."
    )

    reference: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="reference",
        title="Educational material reference pointer",
        description=(
            "Reference pointer to the educational material given to the patient if "
            "the information was on line."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    reference__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_reference", title="Extension field for ``reference``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImmunizationEducation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "documentType",
            "reference",
            "publicationDate",
            "presentationDate",
        ]


class ImmunizationPerformer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who performed event.
    Indicates who performed the immunization event.
    """

    __resource_type__ = "ImmunizationPerformer"

    actor: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="actor",
        title="Individual or organization who was performing",
        description="The practitioner or organization who performed the action.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
            ],
        },
    )

    function: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="function",
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
        ``ImmunizationPerformer`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "function", "actor"]


class ImmunizationProtocolApplied(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Protocol followed by the provider.
    The protocol (set of recommendations) being followed by the provider who
    administered the dose.
    """

    __resource_type__ = "ImmunizationProtocolApplied"

    authority: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="authority",
        title="Who is responsible for publishing the recommendations",
        description=(
            "Indicates the authority who published the protocol (e.g. ACIP) that is"
            " being followed."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    doseNumberPositiveInt: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="doseNumberPositiveInt",
        title="Dose number within series",
        description="Nominal position in a series.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e doseNumber[x]
            "one_of_many": "doseNumber",
            "one_of_many_required": True,
        },
    )
    doseNumberPositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_doseNumberPositiveInt",
        title="Extension field for ``doseNumberPositiveInt``.",
    )

    doseNumberString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="doseNumberString",
        title="Dose number within series",
        description="Nominal position in a series.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e doseNumber[x]
            "one_of_many": "doseNumber",
            "one_of_many_required": True,
        },
    )
    doseNumberString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_doseNumberString",
        title="Extension field for ``doseNumberString``.",
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

    seriesDosesPositiveInt: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="seriesDosesPositiveInt",
        title="Recommended number of doses for immunity",
        description="The recommended number of doses to achieve immunity.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e seriesDoses[x]
            "one_of_many": "seriesDoses",
            "one_of_many_required": False,
        },
    )
    seriesDosesPositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_seriesDosesPositiveInt",
        title="Extension field for ``seriesDosesPositiveInt``.",
    )

    seriesDosesString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="seriesDosesString",
        title="Recommended number of doses for immunity",
        description="The recommended number of doses to achieve immunity.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e seriesDoses[x]
            "one_of_many": "seriesDoses",
            "one_of_many_required": False,
        },
    )
    seriesDosesString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_seriesDosesString",
        title="Extension field for ``seriesDosesString``.",
    )

    targetDisease: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="targetDisease",
        title="Vaccine preventatable disease being targetted",
        description=(
            "The vaccine preventable disease the dose is being administered " "against."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImmunizationProtocolApplied`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "series",
            "authority",
            "targetDisease",
            "doseNumberPositiveInt",
            "doseNumberString",
            "seriesDosesPositiveInt",
            "seriesDosesString",
        ]

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
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
            "doseNumber": ["doseNumberPositiveInt", "doseNumberString"],
            "seriesDoses": ["seriesDosesPositiveInt", "seriesDosesString"],
        }
        return one_of_many_fields


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
