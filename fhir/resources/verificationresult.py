# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/VerificationResult
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType
from typing import Union

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class VerificationResult(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Describes validation requirements, source(s), status and dates for one or
    more elements.
    """

    resource_type = Field("VerificationResult", const=True)

    attestation: fhirtypes.VerificationResultAttestationType = Field(
        None,
        alias="attestation",
        title="Type `VerificationResultAttestation` (represented as `dict` in JSON)",
        description="Information about the entity attesting to information",
    )

    failureAction: fhirtypes.CodeableConceptType = Field(
        None,
        alias="failureAction",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="fatal | warn | rec-only | none",
    )

    frequency: fhirtypes.TimingType = Field(
        None,
        alias="frequency",
        title="Type `Timing` (represented as `dict` in JSON)",
        description="Frequency of revalidation",
    )

    lastPerformed: fhirtypes.DateTime = Field(
        None,
        alias="lastPerformed",
        title="Type `DateTime`",
        description=(
            "The date/time validation was last completed (including failed "
            "validations)"
        ),
    )
    lastPerformed__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastPerformed", title="Extension field for ``lastPerformed``."
    )

    need: fhirtypes.CodeableConceptType = Field(
        None,
        alias="need",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="none | initial | periodic",
    )

    nextScheduled: fhirtypes.Date = Field(
        None,
        alias="nextScheduled",
        title="Type `Date`",
        description="The date when target is next validated, if appropriate",
    )
    nextScheduled__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_nextScheduled", title="Extension field for ``nextScheduled``."
    )

    primarySource: ListType[fhirtypes.VerificationResultPrimarySourceType] = Field(
        None,
        alias="primarySource",
        title=(
            "List of `VerificationResultPrimarySource` items (represented as `dict`"
            " in JSON)"
        ),
        description="Information about the primary source(s) involved in validation",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`",
        description=(
            "attested | validated | in-process | req-revalid | val-fail | reval-" "fail"
        ),
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    statusDate: fhirtypes.DateTime = Field(
        None,
        alias="statusDate",
        title="Type `DateTime`",
        description="When the validation status was updated",
    )
    statusDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_statusDate", title="Extension field for ``statusDate``."
    )

    target: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="target",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="A resource that was validated",
    )

    targetLocation: ListType[fhirtypes.String] = Field(
        None,
        alias="targetLocation",
        title="List of `String` items",
        description="The fhirpath location(s) within the resource that was validated",
    )
    targetLocation__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_targetLocation", title="Extension field for ``targetLocation``."
    )

    validationProcess: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="validationProcess",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description=(
            "The primary process by which the target is validated (edit check; "
            "value set; primary source; multiple sources; standalone; in context)"
        ),
    )

    validationType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="validationType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="nothing | primary | multiple",
    )

    validator: ListType[fhirtypes.VerificationResultValidatorType] = Field(
        None,
        alias="validator",
        title=(
            "List of `VerificationResultValidator` items (represented as `dict` in "
            "JSON)"
        ),
        description="Information about the entity validating information",
    )


class VerificationResultAttestation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about the entity attesting to information.
    """

    resource_type = Field("VerificationResultAttestation", const=True)

    communicationMethod: fhirtypes.CodeableConceptType = Field(
        None,
        alias="communicationMethod",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The method by which attested information was submitted/retrieved",
    )

    date: fhirtypes.Date = Field(
        None,
        alias="date",
        title="Type `Date`",
        description="The date the information was attested to",
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    onBehalfOf: fhirtypes.ReferenceType = Field(
        None,
        alias="onBehalfOf",
        title=(
            "Type `Reference` referencing `Organization, Practitioner, "
            "PractitionerRole` (represented as `dict` in JSON)"
        ),
        description=(
            "When the who is asserting on behalf of another (organization or "
            "individual)"
        ),
    )

    proxyIdentityCertificate: fhirtypes.String = Field(
        None,
        alias="proxyIdentityCertificate",
        title="Type `String`",
        description=(
            "A digital identity certificate associated with the proxy entity "
            "submitting attested information on behalf of the attestation source"
        ),
    )
    proxyIdentityCertificate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_proxyIdentityCertificate",
        title="Extension field for ``proxyIdentityCertificate``.",
    )

    proxySignature: fhirtypes.SignatureType = Field(
        None,
        alias="proxySignature",
        title="Type `Signature` (represented as `dict` in JSON)",
        description="Proxy signature",
    )

    sourceIdentityCertificate: fhirtypes.String = Field(
        None,
        alias="sourceIdentityCertificate",
        title="Type `String`",
        description="A digital identity certificate associated with the attestation source",
    )
    sourceIdentityCertificate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_sourceIdentityCertificate",
        title="Extension field for ``sourceIdentityCertificate``.",
    )

    sourceSignature: fhirtypes.SignatureType = Field(
        None,
        alias="sourceSignature",
        title="Type `Signature` (represented as `dict` in JSON)",
        description="Attester signature",
    )

    who: fhirtypes.ReferenceType = Field(
        None,
        alias="who",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole, "
            "Organization` (represented as `dict` in JSON)"
        ),
        description="The individual or organization attesting to information",
    )


class VerificationResultPrimarySource(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about the primary source(s) involved in validation.
    """

    resource_type = Field("VerificationResultPrimarySource", const=True)

    canPushUpdates: fhirtypes.CodeableConceptType = Field(
        None,
        alias="canPushUpdates",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="yes | no | undetermined",
    )

    communicationMethod: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="communicationMethod",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Method for exchanging information with the primary source",
    )

    pushTypeAvailable: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="pushTypeAvailable",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="specific | any | source",
    )

    type: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description=(
            "Type of primary source (License Board; Primary Education; Continuing "
            "Education; Postal Service; Relationship owner; Registration Authority;"
            " legal source; issuing source; authoritative source)"
        ),
    )

    validationDate: fhirtypes.DateTime = Field(
        None,
        alias="validationDate",
        title="Type `DateTime`",
        description="When the target was validated against the primary source",
    )
    validationDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_validationDate", title="Extension field for ``validationDate``."
    )

    validationStatus: fhirtypes.CodeableConceptType = Field(
        None,
        alias="validationStatus",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="successful | failed | unknown",
    )

    who: fhirtypes.ReferenceType = Field(
        None,
        alias="who",
        title=(
            "Type `Reference` referencing `Organization, Practitioner, "
            "PractitionerRole` (represented as `dict` in JSON)"
        ),
        description="Reference to the primary source",
    )


class VerificationResultValidator(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about the entity validating information.
    """

    resource_type = Field("VerificationResultValidator", const=True)

    attestationSignature: fhirtypes.SignatureType = Field(
        None,
        alias="attestationSignature",
        title="Type `Signature` (represented as `dict` in JSON)",
        description="Validator signature",
    )

    identityCertificate: fhirtypes.String = Field(
        None,
        alias="identityCertificate",
        title="Type `String`",
        description="A digital identity certificate associated with the validator",
    )
    identityCertificate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_identityCertificate",
        title="Extension field for ``identityCertificate``.",
    )

    organization: fhirtypes.ReferenceType = Field(
        ...,
        alias="organization",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Reference to the organization validating information",
    )
