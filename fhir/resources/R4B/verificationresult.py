from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/VerificationResult
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class VerificationResult(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Describes validation requirements, source(s), status and dates for one or
    more elements.
    """

    __resource_type__ = "VerificationResult"

    attestation: fhirtypes.VerificationResultAttestationType | None = Field(  # type: ignore
        None,
        alias="attestation",
        title="Information about the entity attesting to information",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    failureAction: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="failureAction",
        title="fatal | warn | rec-only | none",
        description="The result if validation fails (fatal; warning; record only; none).",
        json_schema_extra={
            "element_property": True,
        },
    )

    frequency: fhirtypes.TimingType | None = Field(  # type: ignore
        None,
        alias="frequency",
        title="Frequency of revalidation",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    lastPerformed: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="lastPerformed",
        title=(
            "The date/time validation was last completed (including failed "
            "validations)"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    lastPerformed__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_lastPerformed", title="Extension field for ``lastPerformed``."
    )

    need: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="need",
        title="none | initial | periodic",
        description=(
            "The frequency with which the target must be validated (none; initial; "
            "periodic)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    nextScheduled: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="nextScheduled",
        title="The date when target is next validated, if appropriate",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    nextScheduled__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_nextScheduled", title="Extension field for ``nextScheduled``."
    )

    primarySource: typing.List[fhirtypes.VerificationResultPrimarySourceType] | None = Field(  # type: ignore
        None,
        alias="primarySource",
        title="Information about the primary source(s) involved in validation",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title=(
            "attested | validated | in-process | req-revalid | val-fail | reval-" "fail"
        ),
        description=(
            "The validation status of the target (attested; validated; in process; "
            "requires revalidation; validation failed; revalidation failed)."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "attested",
                "validated",
                "in-process",
                "req-revalid",
                "val-fail",
                "reval-fail",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    statusDate: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="statusDate",
        title="When the validation status was updated",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    statusDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_statusDate", title="Extension field for ``statusDate``."
    )

    target: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="target",
        title="A resource that was validated",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    targetLocation: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="targetLocation",
        title="The fhirpath location(s) within the resource that was validated",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    targetLocation__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_targetLocation", title="Extension field for ``targetLocation``."
    )

    validationProcess: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="validationProcess",
        title=(
            "The primary process by which the target is validated (edit check; "
            "value set; primary source; multiple sources; standalone; in context)"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    validationType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="validationType",
        title="nothing | primary | multiple",
        description=(
            "What the target is validated against (nothing; primary source; "
            "multiple sources)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    validator: typing.List[fhirtypes.VerificationResultValidatorType] | None = Field(  # type: ignore
        None,
        alias="validator",
        title="Information about the entity validating information",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``VerificationResult`` according specification,
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
            "target",
            "targetLocation",
            "need",
            "status",
            "statusDate",
            "validationType",
            "validationProcess",
            "frequency",
            "lastPerformed",
            "nextScheduled",
            "failureAction",
            "primarySource",
            "attestation",
            "validator",
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


class VerificationResultAttestation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about the entity attesting to information.
    """

    __resource_type__ = "VerificationResultAttestation"

    communicationMethod: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="communicationMethod",
        title="The method by which attested information was submitted/retrieved",
        description=(
            "The method by which attested information was submitted/retrieved "
            "(manual; API; Push)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    date: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="date",
        title="The date the information was attested to",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    onBehalfOf: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="onBehalfOf",
        title=(
            "When the who is asserting on behalf of another (organization or "
            "individual)"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Organization",
                "Practitioner",
                "PractitionerRole",
            ],
        },
    )

    proxyIdentityCertificate: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="proxyIdentityCertificate",
        title=(
            "A digital identity certificate associated with the proxy entity "
            "submitting attested information on behalf of the attestation source"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    proxyIdentityCertificate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_proxyIdentityCertificate",
        title="Extension field for ``proxyIdentityCertificate``.",
    )

    proxySignature: fhirtypes.SignatureType | None = Field(  # type: ignore
        None,
        alias="proxySignature",
        title="Proxy signature",
        description=(
            "Signed assertion by the proxy entity indicating that they have the "
            "right to submit attested information on behalf of the attestation "
            "source."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    sourceIdentityCertificate: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="sourceIdentityCertificate",
        title="A digital identity certificate associated with the attestation source",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    sourceIdentityCertificate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_sourceIdentityCertificate",
        title="Extension field for ``sourceIdentityCertificate``.",
    )

    sourceSignature: fhirtypes.SignatureType | None = Field(  # type: ignore
        None,
        alias="sourceSignature",
        title="Attester signature",
        description=(
            "Signed assertion by the attestation source that they have attested to "
            "the information."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    who: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="who",
        title="The individual or organization attesting to information",
        description=None,
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

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``VerificationResultAttestation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "who",
            "onBehalfOf",
            "communicationMethod",
            "date",
            "sourceIdentityCertificate",
            "proxyIdentityCertificate",
            "proxySignature",
            "sourceSignature",
        ]


class VerificationResultPrimarySource(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about the primary source(s) involved in validation.
    """

    __resource_type__ = "VerificationResultPrimarySource"

    canPushUpdates: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="canPushUpdates",
        title="yes | no | undetermined",
        description=(
            "Ability of the primary source to push updates/alerts (yes; no; "
            "undetermined)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    communicationMethod: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="communicationMethod",
        title="Method for exchanging information with the primary source",
        description="Method for communicating with the primary source (manual; API; Push).",
        json_schema_extra={
            "element_property": True,
        },
    )

    pushTypeAvailable: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="pushTypeAvailable",
        title="specific | any | source",
        description=(
            "Type of alerts/updates the primary source can send (specific requested"
            " changes; any changes; as defined by source)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    type: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="type",
        title=(
            "Type of primary source (License Board; Primary Education; Continuing "
            "Education; Postal Service; Relationship owner; Registration Authority;"
            " legal source; issuing source; authoritative source)"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    validationDate: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="validationDate",
        title="When the target was validated against the primary source",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    validationDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_validationDate", title="Extension field for ``validationDate``."
    )

    validationStatus: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="validationStatus",
        title="successful | failed | unknown",
        description=(
            "Status of the validation of the target against the primary source "
            "(successful; failed; unknown)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    who: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="who",
        title="Reference to the primary source",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Organization",
                "Practitioner",
                "PractitionerRole",
            ],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``VerificationResultPrimarySource`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "who",
            "type",
            "communicationMethod",
            "validationStatus",
            "validationDate",
            "canPushUpdates",
            "pushTypeAvailable",
        ]


class VerificationResultValidator(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about the entity validating information.
    """

    __resource_type__ = "VerificationResultValidator"

    attestationSignature: fhirtypes.SignatureType | None = Field(  # type: ignore
        None,
        alias="attestationSignature",
        title="Validator signature",
        description=(
            "Signed assertion by the validator that they have validated the "
            "information."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    identityCertificate: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="identityCertificate",
        title="A digital identity certificate associated with the validator",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    identityCertificate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_identityCertificate",
        title="Extension field for ``identityCertificate``.",
    )

    organization: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="organization",
        title="Reference to the organization validating information",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``VerificationResultValidator`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "organization",
            "identityCertificate",
            "attestationSignature",
        ]
