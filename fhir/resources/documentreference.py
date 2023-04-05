# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DocumentReference
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class DocumentReference(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A reference to a document.
    A reference to a document of any kind for any purpose. While the term
    “document” implies a more narrow focus, for this resource this "document"
    encompasses *any* serialized object with a mime-type, it includes formal
    patient-centric documents (CDA), clinical notes, scanned paper, non-patient
    specific documents like policy text, as well as a photo, video, or audio
    recording acquired or used in healthcare.  The DocumentReference resource
    provides metadata about the document so that the document can be discovered
    and managed.  The actual content may be inline base64 encoded data or
    provided by direct reference.
    """

    resource_type = Field("DocumentReference", const=True)

    attester: typing.List[fhirtypes.DocumentReferenceAttesterType] = Field(
        None,
        alias="attester",
        title="Attests to accuracy of the document",
        description="A participant who has authenticated the accuracy of the document.",
        # if property is element of this resource.
        element_property=True,
    )

    author: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="author",
        title="Who and/or what authored the document",
        description=(
            "Identifies who is responsible for adding the information to the "
            "document."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "Organization",
            "Device",
            "Patient",
            "RelatedPerson",
            "CareTeam",
        ],
    )

    basedOn: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="Procedure that caused this media to be created",
        description=(
            "A procedure that is fulfilled in whole or in part by the creation of "
            "this media."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Appointment",
            "AppointmentResponse",
            "CarePlan",
            "Claim",
            "CommunicationRequest",
            "Contract",
            "CoverageEligibilityRequest",
            "DeviceRequest",
            "EnrollmentRequest",
            "ImmunizationRecommendation",
            "MedicationRequest",
            "NutritionOrder",
            "RequestOrchestration",
            "ServiceRequest",
            "SupplyRequest",
            "VisionPrescription",
        ],
    )

    bodySite: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="bodySite",
        title="Body part included",
        description="The anatomic structures included in the document.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["BodyStructure"],
    )

    category: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="Categorization of document",
        description=(
            "A categorization for the type of document referenced - helps for "
            "indexing and searching. This may be implied by or derived from the "
            "code specified in the DocumentReference.type."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    content: typing.List[fhirtypes.DocumentReferenceContentType] = Field(
        ...,
        alias="content",
        title="Document referenced",
        description=(
            "The document and format referenced.  If there are multiple content "
            "element repetitions, these must all represent the same document in "
            "different format, or attachment metadata."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    context: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="context",
        title="Context of the document content",
        description=(
            "Describes the clinical encounter or type of care that the document "
            "content is associated with."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Appointment", "Encounter", "EpisodeOfCare"],
    )

    custodian: fhirtypes.ReferenceType = Field(
        None,
        alias="custodian",
        title="Organization which maintains the document",
        description=(
            "Identifies the organization or group who is responsible for ongoing "
            "maintenance of and access to the document."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    date: fhirtypes.Instant = Field(
        None,
        alias="date",
        title="When this document reference was created",
        description="When the document reference was created.",
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Human-readable description",
        description="Human-readable description of the source document.",
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    docStatus: fhirtypes.Code = Field(
        None,
        alias="docStatus",
        title=(
            "registered | partial | preliminary | final | amended | corrected | "
            "appended | cancelled | entered-in-error | deprecated | unknown"
        ),
        description="The status of the underlying document.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "registered",
            "partial",
            "preliminary",
            "final",
            "amended",
            "corrected",
            "appended",
            "cancelled",
            "entered-in-error",
            "deprecated",
            "unknown",
        ],
    )
    docStatus__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_docStatus", title="Extension field for ``docStatus``."
    )

    event: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="event",
        title="Main clinical acts documented",
        description=(
            "This list of codes represents the main clinical acts, such as a "
            "colonoscopy or an appendectomy, being documented. In some cases, the "
            'event is inherent in the type Code, such as a "History and Physical '
            'Report" in which the procedure being documented is necessarily a '
            '"History and Physical" act.'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    facilityType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="facilityType",
        title="Kind of facility where patient was seen",
        description="The kind of facility where the patient was seen.",
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifiers for the document",
        description=(
            "Other business identifiers associated with the document, including "
            "version independent identifiers."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    modality: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="modality",
        title="Imaging modality used",
        description=(
            "Imaging modality used. This may include both acquisition and non-"
            "acquisition modalities."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Time of service that is being documented",
        description=(
            "The time period over which the service that is described by the "
            "document was provided."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    practiceSetting: fhirtypes.CodeableConceptType = Field(
        None,
        alias="practiceSetting",
        title=(
            "Additional details about where the content was created (e.g. clinical "
            "specialty)"
        ),
        description=(
            "This property may convey specifics about the practice setting where "
            "the content was created, often reflecting the clinical specialty."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    relatesTo: typing.List[fhirtypes.DocumentReferenceRelatesToType] = Field(
        None,
        alias="relatesTo",
        title="Relationships to other documents",
        description=(
            "Relationships that this document has with other document references "
            "that already exist."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    securityLabel: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="securityLabel",
        title="Document security-tags",
        description=(
            "A set of Security-Tag codes specifying the level of privacy/security "
            "of the Document found at DocumentReference.content.attachment.url. "
            "Note that DocumentReference.meta.security contains the security labels"
            " of the data elements in DocumentReference, while "
            "DocumentReference.securityLabel contains the security labels for the "
            "document the reference refers to. The distinction recognizes that the "
            "document may contain sensitive information, while the "
            "DocumentReference is metadata about the document and thus might not be"
            " as sensitive as the document. For example: a psychotherapy episode "
            "may contain highly sensitive information, while the metadata may "
            "simply indicate that some episode happened."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="current | superseded | entered-in-error",
        description="The status of this document reference.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["current", "superseded", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Who/what is the subject of the document",
        description=(
            "Who or what the document is about. The document can be about a person,"
            " (patient or healthcare practitioner), a device (e.g. a machine) or "
            "even a group of subjects (such as a document about a herd of farm "
            "animals, or a set of patients that share a common exposure)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Kind of document (LOINC if possible)",
        description=(
            "Specifies the particular kind of document referenced  (e.g. History "
            "and Physical, Discharge Summary, Progress Note). This usually equates "
            "to the purpose of making the document referenced."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title=(
            "An explicitly assigned identifer of a variation of the content in the "
            "DocumentReference"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DocumentReference`` according specification,
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
            "version",
            "basedOn",
            "status",
            "docStatus",
            "modality",
            "type",
            "category",
            "subject",
            "context",
            "event",
            "bodySite",
            "facilityType",
            "practiceSetting",
            "period",
            "date",
            "author",
            "attester",
            "custodian",
            "relatesTo",
            "description",
            "securityLabel",
            "content",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1911(
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


class DocumentReferenceAttester(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Attests to accuracy of the document.
    A participant who has authenticated the accuracy of the document.
    """

    resource_type = Field("DocumentReferenceAttester", const=True)

    mode: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="mode",
        title="personal | professional | legal | official",
        description="The type of attestation the authenticator offers.",
        # if property is element of this resource.
        element_property=True,
    )

    party: fhirtypes.ReferenceType = Field(
        None,
        alias="party",
        title="Who attested the document",
        description="Who attested the document in the specified way.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "RelatedPerson",
            "Practitioner",
            "PractitionerRole",
            "Organization",
        ],
    )

    time: fhirtypes.DateTime = Field(
        None,
        alias="time",
        title="When the document was attested",
        description="When the document was attested by the party.",
        # if property is element of this resource.
        element_property=True,
    )
    time__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_time", title="Extension field for ``time``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DocumentReferenceAttester`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "mode", "time", "party"]


class DocumentReferenceContent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Document referenced.
    The document and format referenced.  If there are multiple content element
    repetitions, these must all represent the same document in different
    format, or attachment metadata.
    """

    resource_type = Field("DocumentReferenceContent", const=True)

    attachment: fhirtypes.AttachmentType = Field(
        ...,
        alias="attachment",
        title="Where to access the document",
        description=(
            "The document or URL of the document along with critical metadata to "
            "prove content has integrity."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    profile: typing.List[fhirtypes.DocumentReferenceContentProfileType] = Field(
        None,
        alias="profile",
        title="Content profile rules for the document",
        description=(
            "An identifier of the document constraints, encoding, structure, and "
            "template that the document conforms to beyond the base format "
            "indicated in the mimeType."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DocumentReferenceContent`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "attachment", "profile"]


class DocumentReferenceContentProfile(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Content profile rules for the document.
    An identifier of the document constraints, encoding, structure, and
    template that the document conforms to beyond the base format indicated in
    the mimeType.
    """

    resource_type = Field("DocumentReferenceContentProfile", const=True)

    valueCanonical: fhirtypes.Canonical = Field(
        None,
        alias="valueCanonical",
        title="Code|uri|canonical",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueCanonical", title="Extension field for ``valueCanonical``."
    )

    valueCoding: fhirtypes.CodingType = Field(
        None,
        alias="valueCoding",
        title="Code|uri|canonical",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueUri: fhirtypes.Uri = Field(
        None,
        alias="valueUri",
        title="Code|uri|canonical",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueUri", title="Extension field for ``valueUri``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DocumentReferenceContentProfile`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "valueCoding",
            "valueUri",
            "valueCanonical",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3363(
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
        one_of_many_fields = {"value": ["valueCanonical", "valueCoding", "valueUri"]}
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


class DocumentReferenceRelatesTo(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Relationships to other documents.
    Relationships that this document has with other document references that
    already exist.
    """

    resource_type = Field("DocumentReferenceRelatesTo", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="The relationship type with another document",
        description="The type of relationship that this document has with anther document.",
        # if property is element of this resource.
        element_property=True,
    )

    target: fhirtypes.ReferenceType = Field(
        ...,
        alias="target",
        title="Target of the relationship",
        description="The target document of this relationship.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DocumentReferenceRelatesTo`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "target"]
