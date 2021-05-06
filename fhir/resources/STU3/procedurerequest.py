# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ProcedureRequest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class ProcedureRequest(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A request for a procedure or diagnostic to be performed.
    A record of a request for diagnostic investigations, treatments, or
    operations to be performed.
    """

    resource_type = Field("ProcedureRequest", const=True)

    asNeededBoolean: bool = Field(
        None,
        alias="asNeededBoolean",
        title="Preconditions for procedure or diagnostic",
        description=(
            "If a CodeableConcept is present, it indicates the pre-condition for "
            'performing the procedure.  For example "pain", "on flare-up", etc.'
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e asNeeded[x]
        one_of_many="asNeeded",
        one_of_many_required=False,
    )
    asNeededBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_asNeededBoolean", title="Extension field for ``asNeededBoolean``."
    )

    asNeededCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="asNeededCodeableConcept",
        title="Preconditions for procedure or diagnostic",
        description=(
            "If a CodeableConcept is present, it indicates the pre-condition for "
            'performing the procedure.  For example "pain", "on flare-up", etc.'
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e asNeeded[x]
        one_of_many="asNeeded",
        one_of_many_required=False,
    )

    authoredOn: fhirtypes.DateTime = Field(
        None,
        alias="authoredOn",
        title="Date request signed",
        description="When the request transitioned to being actionable.",
        # if property is element of this resource.
        element_property=True,
    )
    authoredOn__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_authoredOn", title="Extension field for ``authoredOn``."
    )

    basedOn: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="What request fulfills",
        description="Plan/proposal/order fulfilled by this request.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    bodySite: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="bodySite",
        title="Location on Body",
        description=(
            "Anatomic location where the procedure should be performed. This is the"
            " target site."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    category: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="Classification of procedure",
        description=(
            "A code that classifies the procedure for searching, sorting and "
            'display purposes (e.g. "Surgical Procedure").'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="What is being requested/ordered",
        description=(
            "A code that identifies a particular procedure, diagnostic "
            "investigation, or panel of investigations, that have been requested."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title="Encounter or Episode during which request was created",
        description=(
            "An encounter or episode of care that provides additional information "
            "about the healthcare context in which this request is made."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter", "EpisodeOfCare"],
    )

    definition: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="definition",
        title="Protocol or definition",
        description="Protocol or definition followed by this request.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ActivityDefinition", "PlanDefinition"],
    )

    doNotPerform: bool = Field(
        None,
        alias="doNotPerform",
        title="True if procedure should not be performed",
        description=(
            "Set this to true if the record is saying that the procedure should NOT"
            " be performed."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    doNotPerform__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_doNotPerform", title="Extension field for ``doNotPerform``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Identifiers assigned to this order",
        description=(
            "Identifiers assigned to this order instance by the orderer and/or the "
            "receiver and/or order fulfiller."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    intent: fhirtypes.Code = Field(
        None,
        alias="intent",
        title="proposal | plan | order +",
        description=(
            "Whether the request is a proposal, plan, an original order or a reflex"
            " order."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["proposal", "plan", "order", "+"],
    )
    intent__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_intent", title="Extension field for ``intent``."
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Comments",
        description=(
            "Any other notes and comments made about the service request. For "
            'example, letting provider know that "patient hates needles" or other '
            "provider instructions."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    occurrenceDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurrenceDateTime",
        title="When procedure should occur",
        description="The date/time at which the diagnostic testing should occur.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_occurrenceDateTime",
        title="Extension field for ``occurrenceDateTime``.",
    )

    occurrencePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="occurrencePeriod",
        title="When procedure should occur",
        description="The date/time at which the diagnostic testing should occur.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )

    occurrenceTiming: fhirtypes.TimingType = Field(
        None,
        alias="occurrenceTiming",
        title="When procedure should occur",
        description="The date/time at which the diagnostic testing should occur.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )

    performer: fhirtypes.ReferenceType = Field(
        None,
        alias="performer",
        title="Requested perfomer",
        description=(
            "The desired perfomer for doing the diagnostic testing.  For example, "
            "the surgeon, dermatopathologist, endoscopist, etc."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "Organization",
            "Patient",
            "Device",
            "RelatedPerson",
            "HealthcareService",
        ],
    )

    performerType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="performerType",
        title="Performer role",
        description="Desired type of performer for doing the diagnostic testing.",
        # if property is element of this resource.
        element_property=True,
    )

    priority: fhirtypes.Code = Field(
        None,
        alias="priority",
        title="routine | urgent | asap | stat",
        description=(
            "Indicates how quickly the ProcedureRequest should be addressed with "
            "respect to other requests."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["routine", "urgent", "asap", "stat"],
    )
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_priority", title="Extension field for ``priority``."
    )

    reasonCode: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="Explanation/Justification for test",
        description=(
            "An explanation or justification for why this diagnostic investigation "
            "is being requested in coded or textual form.   This is often for "
            "billing purposes.  May relate to the resources referred to in "
            "supportingInformation."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    reasonReference: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title="Explanation/Justification for test",
        description=(
            "Indicates another resource that provides a justification for why this "
            "diagnostic investigation is being requested.   May relate to the "
            "resources referred to in supportingInformation."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Condition", "Observation"],
    )

    relevantHistory: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="relevantHistory",
        title="Request provenance",
        description="Key events in the history of the request.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Provenance"],
    )

    replaces: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="replaces",
        title="What request replaces",
        description=(
            "The request takes the place of the referenced completed or terminated "
            "request(s)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    requester: fhirtypes.ProcedureRequestRequesterType = Field(
        None,
        alias="requester",
        title="Who/what is requesting procedure or diagnostic",
        description=(
            "The individual who initiated the request and has responsibility for "
            "its activation."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    requisition: fhirtypes.IdentifierType = Field(
        None,
        alias="requisition",
        title="Composite Request ID",
        description=(
            "A shared identifier common to all procedure or diagnostic requests "
            "that were authorized more or less simultaneously by a single author, "
            "representing the composite or group identifier."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    specimen: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="specimen",
        title="Procedure Samples",
        description="One or more specimens that the laboratory procedure will use.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Specimen"],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | suspended | completed | entered-in-error | cancelled",
        description="The status of the order.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "draft",
            "active",
            "suspended",
            "completed",
            "entered-in-error",
            "cancelled",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Individual the service is ordered for",
        description=(
            "On whom or what the procedure or diagnostic is to be performed. This "
            "is usually a human patient, but can also be requested on animals, "
            "groups of humans or animals, devices such as dialysis machines, or "
            "even locations (typically for environmental scans)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group", "Location", "Device"],
    )

    supportingInfo: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingInfo",
        title="Additional clinical information",
        description=(
            "Additional clinical information about the patient or specimen that may"
            " influence the procedure or diagnostics or their interpretations.     "
            "This information includes diagnosis, clinical findings and other "
            "observations.  In laboratory ordering these are typically referred to "
            'as "ask at order entry questions (AOEs)".  This includes observations '
            "explicitly requested by the producer (filler) to provide context or "
            "supporting information needed to complete the order. For example,  "
            "reporting the amount of inspired oxygen for blood gas measurements."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ProcedureRequest`` according specification,
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
            "definition",
            "basedOn",
            "replaces",
            "requisition",
            "status",
            "intent",
            "priority",
            "doNotPerform",
            "category",
            "code",
            "subject",
            "context",
            "occurrenceDateTime",
            "occurrencePeriod",
            "occurrenceTiming",
            "asNeededBoolean",
            "asNeededCodeableConcept",
            "authoredOn",
            "requester",
            "performerType",
            "performer",
            "reasonCode",
            "reasonReference",
            "supportingInfo",
            "specimen",
            "bodySite",
            "note",
            "relevantHistory",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1878(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("intent", "intent__ext"), ("status", "status__ext")]
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
    def validate_one_of_many_1878(
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
            "asNeeded": ["asNeededBoolean", "asNeededCodeableConcept"],
            "occurrence": [
                "occurrenceDateTime",
                "occurrencePeriod",
                "occurrenceTiming",
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


class ProcedureRequestRequester(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who/what is requesting procedure or diagnostic.
    The individual who initiated the request and has responsibility for its
    activation.
    """

    resource_type = Field("ProcedureRequestRequester", const=True)

    agent: fhirtypes.ReferenceType = Field(
        ...,
        alias="agent",
        title="Individual making the request",
        description="The device, practitioner or organization who initiated the request.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device", "Practitioner", "Organization"],
    )

    onBehalfOf: fhirtypes.ReferenceType = Field(
        None,
        alias="onBehalfOf",
        title="Organization agent is acting for",
        description="The organization the device or practitioner was acting on behalf of.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ProcedureRequestRequester`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "agent", "onBehalfOf"]
