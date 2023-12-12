# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AuditEvent
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class AuditEvent(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Event record kept for security purposes.
    A record of an event made for purposes of maintaining a security log.
    Typical uses include detection of intrusion attempts and monitoring for
    inappropriate usage.
    """

    resource_type = Field("AuditEvent", const=True)

    action: fhirtypes.Code = Field(
        None,
        alias="action",
        title="Type of action performed during the event",
        description=(
            "Indicator for type of action performed during the event that generated"
            " the audit."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    action__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_action", title="Extension field for ``action``."
    )

    agent: typing.List[fhirtypes.AuditEventAgentType] = Field(
        ...,
        alias="agent",
        title="Actor involved in the event",
        description=(
            "An actor taking an active role in the event or activity that is " "logged."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    entity: typing.List[fhirtypes.AuditEventEntityType] = Field(
        None,
        alias="entity",
        title="Data or objects used",
        description="Specific instances of data or objects that have been accessed.",
        # if property is element of this resource.
        element_property=True,
    )

    outcome: fhirtypes.Code = Field(
        None,
        alias="outcome",
        title="Whether the event succeeded or failed",
        description="Indicates whether the event succeeded or failed.",
        # if property is element of this resource.
        element_property=True,
    )
    outcome__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_outcome", title="Extension field for ``outcome``."
    )

    outcomeDesc: fhirtypes.String = Field(
        None,
        alias="outcomeDesc",
        title="Description of the event outcome",
        description="A free text description of the outcome of the event.",
        # if property is element of this resource.
        element_property=True,
    )
    outcomeDesc__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_outcomeDesc", title="Extension field for ``outcomeDesc``."
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="When the activity occurred",
        description="The period during which the activity occurred.",
        # if property is element of this resource.
        element_property=True,
    )

    purposeOfEvent: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="purposeOfEvent",
        title="The purposeOfUse of the event",
        description=(
            "The purposeOfUse (reason) that was used during the event being "
            "recorded."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    recorded: fhirtypes.Instant = Field(
        None,
        alias="recorded",
        title="Time when the event was recorded",
        description="The time when the event was recorded.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    recorded__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_recorded", title="Extension field for ``recorded``."
    )

    source: fhirtypes.AuditEventSourceType = Field(
        ...,
        alias="source",
        title="Audit Event Reporter",
        description="The system that is reporting the event.",
        # if property is element of this resource.
        element_property=True,
    )

    subtype: typing.List[fhirtypes.CodingType] = Field(
        None,
        alias="subtype",
        title="More specific type/id for the event",
        description="Identifier for the category of event.",
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodingType = Field(
        ...,
        alias="type",
        title="Type/identifier of event",
        description=(
            "Identifier for a family of the event.  For example, a menu item, "
            "program, rule, policy, function code, application name or URL. It "
            "identifies the performed function."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AuditEvent`` according specification,
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
            "type",
            "subtype",
            "action",
            "period",
            "recorded",
            "outcome",
            "outcomeDesc",
            "purposeOfEvent",
            "agent",
            "source",
            "entity",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1198(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("recorded", "recorded__ext")]
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


class AuditEventAgent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Actor involved in the event.
    An actor taking an active role in the event or activity that is logged.
    """

    resource_type = Field("AuditEventAgent", const=True)

    altId: fhirtypes.String = Field(
        None,
        alias="altId",
        title="Alternative User identity",
        description=(
            "Alternative agent Identifier. For a human, this should be a user "
            "identifier text string from authentication system. This identifier "
            "would be one known to a common authentication system (e.g. single "
            "sign-on), if available."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    altId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_altId", title="Extension field for ``altId``."
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title="Where",
        description="Where the event occurred.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    media: fhirtypes.CodingType = Field(
        None,
        alias="media",
        title="Type of media",
        description=(
            "Type of media involved. Used when the event is about "
            "exporting/importing onto media."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Human friendly name for the agent",
        description="Human-meaningful name for the agent.",
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    network: fhirtypes.AuditEventAgentNetworkType = Field(
        None,
        alias="network",
        title="Logical network location for application activity",
        description=(
            "Logical network location for application activity, if the activity has"
            " a network location."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    policy: typing.List[typing.Optional[fhirtypes.Uri]] = Field(
        None,
        alias="policy",
        title="Policy that authorized event",
        description=(
            "The policy or plan that authorized the activity being recorded. "
            "Typically, a single activity may have multiple applicable policies, "
            "such as patient consent, guarantor funding, etc. The policy would also"
            " indicate the security token used."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    policy__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_policy", title="Extension field for ``policy``.")

    purposeOfUse: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="purposeOfUse",
        title="Reason given for this user",
        description=(
            "The reason (purpose of use), specific to this agent, that was used "
            "during the event being recorded."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    requestor: bool = Field(
        None,
        alias="requestor",
        title="Whether user is initiator",
        description=(
            "Indicator that the user is or is not the requestor, or initiator, for "
            "the event being audited."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    requestor__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_requestor", title="Extension field for ``requestor``."
    )

    role: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="role",
        title="Agent role in the event",
        description=(
            "The security role that the user was acting under, that come from local"
            " codes defined by the access control security system (e.g. RBAC, ABAC)"
            " used in the local context."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="How agent participated",
        description=(
            "Specification of the participation type the user plays when performing"
            " the event."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    who: fhirtypes.ReferenceType = Field(
        None,
        alias="who",
        title="Identifier of who",
        description="Reference to who this agent is that was involved in the event.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "PractitionerRole",
            "Practitioner",
            "Organization",
            "Device",
            "Patient",
            "RelatedPerson",
        ],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AuditEventAgent`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "role",
            "who",
            "altId",
            "name",
            "requestor",
            "location",
            "policy",
            "media",
            "network",
            "purposeOfUse",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1693(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("requestor", "requestor__ext")]
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


class AuditEventAgentNetwork(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Logical network location for application activity.
    Logical network location for application activity, if the activity has a
    network location.
    """

    resource_type = Field("AuditEventAgentNetwork", const=True)

    address: fhirtypes.String = Field(
        None,
        alias="address",
        title="Identifier for the network access point of the user device",
        description=(
            "An identifier for the network access point of the user device for the "
            "audit event."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    address__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_address", title="Extension field for ``address``."
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="The type of network access point",
        description=(
            "An identifier for the type of network access point that originated the"
            " audit event."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AuditEventAgentNetwork`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "address", "type"]


class AuditEventEntity(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Data or objects used.
    Specific instances of data or objects that have been accessed.
    """

    resource_type = Field("AuditEventEntity", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Descriptive text",
        description="Text that describes the entity in more detail.",
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    detail: typing.List[fhirtypes.AuditEventEntityDetailType] = Field(
        None,
        alias="detail",
        title="Additional Information about the entity",
        description=(
            "Tagged value pairs for conveying additional information about the "
            "entity."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    lifecycle: fhirtypes.CodingType = Field(
        None,
        alias="lifecycle",
        title="Life-cycle stage for the entity",
        description="Identifier for the data life-cycle stage for the entity.",
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Descriptor for entity",
        description="A name of the entity in the audit event.",
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    query: fhirtypes.Base64Binary = Field(
        None,
        alias="query",
        title="Query parameters",
        description="The query parameters for a query-type entities.",
        # if property is element of this resource.
        element_property=True,
    )
    query__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_query", title="Extension field for ``query``."
    )

    role: fhirtypes.CodingType = Field(
        None,
        alias="role",
        title="What role the entity played",
        description=(
            "Code representing the role the entity played in the event being "
            "audited."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    securityLabel: typing.List[fhirtypes.CodingType] = Field(
        None,
        alias="securityLabel",
        title="Security labels on the entity",
        description="Security labels for the identified entity.",
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodingType = Field(
        None,
        alias="type",
        title="Type of entity involved",
        description="The type of the object that was involved in this audit event.",
        # if property is element of this resource.
        element_property=True,
    )

    what: fhirtypes.ReferenceType = Field(
        None,
        alias="what",
        title="Specific instance of resource",
        description=(
            "Identifies a specific instance of the entity. The reference should be "
            "version specific."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AuditEventEntity`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "what",
            "type",
            "role",
            "lifecycle",
            "securityLabel",
            "name",
            "description",
            "query",
            "detail",
        ]


class AuditEventEntityDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional Information about the entity.
    Tagged value pairs for conveying additional information about the entity.
    """

    resource_type = Field("AuditEventEntityDetail", const=True)

    type: fhirtypes.String = Field(
        None,
        alias="type",
        title="Name of the property",
        description="The type of extra detail provided in the value.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    valueBase64Binary: fhirtypes.Base64Binary = Field(
        None,
        alias="valueBase64Binary",
        title="Property value",
        description="The  value of the extra detail.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueBase64Binary__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_valueBase64Binary",
        title="Extension field for ``valueBase64Binary``.",
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Property value",
        description="The  value of the extra detail.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AuditEventEntityDetail`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "valueString",
            "valueBase64Binary",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2422(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("type", "type__ext")]
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
    def validate_one_of_many_2422(
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
        one_of_many_fields = {"value": ["valueBase64Binary", "valueString"]}
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


class AuditEventSource(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Audit Event Reporter.
    The system that is reporting the event.
    """

    resource_type = Field("AuditEventSource", const=True)

    observer: fhirtypes.ReferenceType = Field(
        ...,
        alias="observer",
        title="The identity of source detecting the event",
        description="Identifier of the source where the event was detected.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "PractitionerRole",
            "Practitioner",
            "Organization",
            "Device",
            "Patient",
            "RelatedPerson",
        ],
    )

    site: fhirtypes.String = Field(
        None,
        alias="site",
        title="Logical source location within the enterprise",
        description=(
            "Logical source location within the healthcare enterprise network.  For"
            " example, a hospital or other provider location within a multi-entity "
            "provider group."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    site__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_site", title="Extension field for ``site``."
    )

    type: typing.List[fhirtypes.CodingType] = Field(
        None,
        alias="type",
        title="The type of source where event originated",
        description="Code specifying the type of source where event originated.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AuditEventSource`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "site", "observer", "type"]
