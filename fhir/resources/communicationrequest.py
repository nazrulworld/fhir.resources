# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CommunicationRequest
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class CommunicationRequest(domainresource.DomainResource):
    """ A request for information to be sent to a receiver.

    A request to convey information; e.g. the CDS system proposes that an alert
    be sent to a responsible provider, the CDS system proposes that the public
    health agency be notified about a reportable condition.
    """

    resource_type = "CommunicationRequest"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.about = None
        """ Resources that pertain to this communication request.
        List of `FHIRReference` items referencing `['Resource']` (represented as `dict` in JSON). """

        self.authoredOn = None
        """ When request transitioned to being actionable.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.basedOn = None
        """ Fulfills plan or proposal.
        List of `FHIRReference` items referencing `['Resource']` (represented as `dict` in JSON). """

        self.category = None
        """ Message category.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.doNotPerform = None
        """ True if request is prohibiting action.
        Type `bool`. """

        self.encounter = None
        """ Encounter created as part of.
        Type `FHIRReference` referencing `['Encounter']` (represented as `dict` in JSON). """

        self.groupIdentifier = None
        """ Composite request this is part of.
        Type `Identifier` (represented as `dict` in JSON). """

        self.identifier = None
        """ Unique identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.medium = None
        """ A channel of communication.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.note = None
        """ Comments made about communication request.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.occurrenceDateTime = None
        """ When scheduled.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.occurrencePeriod = None
        """ When scheduled.
        Type `Period` (represented as `dict` in JSON). """

        self.payload = None
        """ Message payload.
        List of `CommunicationRequestPayload` items (represented as `dict` in JSON). """

        self.priority = None
        """ routine | urgent | asap | stat.
        Type `str`. """

        self.reasonCode = None
        """ Why is communication needed?.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.reasonReference = None
        """ Why is communication needed?.
        List of `FHIRReference` items referencing `['Condition', 'Observation', 'DiagnosticReport', 'DocumentReference']` (represented as `dict` in JSON). """

        self.recipient = None
        """ Message recipient.
        List of `FHIRReference` items referencing `['Device', 'Organization', 'Patient', 'Practitioner', 'PractitionerRole', 'RelatedPerson', 'Group', 'CareTeam', 'HealthcareService']` (represented as `dict` in JSON). """

        self.replaces = None
        """ Request(s) replaced by this request.
        List of `FHIRReference` items referencing `['CommunicationRequest']` (represented as `dict` in JSON). """

        self.requester = None
        """ Who/what is requesting service.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole', 'Organization', 'Patient', 'RelatedPerson', 'Device']` (represented as `dict` in JSON). """

        self.sender = None
        """ Message sender.
        Type `FHIRReference` referencing `['Device', 'Organization', 'Patient', 'Practitioner', 'PractitionerRole', 'RelatedPerson', 'HealthcareService']` (represented as `dict` in JSON). """

        self.status = None
        """ draft | active | on-hold | revoked | completed | entered-in-error |
        unknown.
        Type `str`. """

        self.statusReason = None
        """ Reason for current status.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.subject = None
        """ Focus of message.
        Type `FHIRReference` referencing `['Patient', 'Group']` (represented as `dict` in JSON). """

        super(CommunicationRequest, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CommunicationRequest, self).elementProperties()
        js.extend(
            [
                (
                    "about",
                    "about",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "authoredOn",
                    "authoredOn",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    None,
                    False,
                ),
                (
                    "basedOn",
                    "basedOn",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "category",
                    "category",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                ("doNotPerform", "doNotPerform", bool, "boolean", False, None, False),
                (
                    "encounter",
                    "encounter",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "groupIdentifier",
                    "groupIdentifier",
                    identifier.Identifier,
                    "Identifier",
                    False,
                    None,
                    False,
                ),
                (
                    "identifier",
                    "identifier",
                    identifier.Identifier,
                    "Identifier",
                    True,
                    None,
                    False,
                ),
                (
                    "medium",
                    "medium",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "note",
                    "note",
                    annotation.Annotation,
                    "Annotation",
                    True,
                    None,
                    False,
                ),
                (
                    "occurrenceDateTime",
                    "occurrenceDateTime",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    "occurrence",
                    False,
                ),
                (
                    "occurrencePeriod",
                    "occurrencePeriod",
                    period.Period,
                    "Period",
                    False,
                    "occurrence",
                    False,
                ),
                (
                    "payload",
                    "payload",
                    CommunicationRequestPayload,
                    "CommunicationRequestPayload",
                    True,
                    None,
                    False,
                ),
                ("priority", "priority", str, "code", False, None, False),
                (
                    "reasonCode",
                    "reasonCode",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "reasonReference",
                    "reasonReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "recipient",
                    "recipient",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "replaces",
                    "replaces",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "requester",
                    "requester",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "sender",
                    "sender",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("status", "status", str, "code", False, None, True),
                (
                    "statusReason",
                    "statusReason",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "subject",
                    "subject",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


class CommunicationRequestPayload(backboneelement.BackboneElement):
    """ Message payload.

    Text, attachment(s), or resource(s) to be communicated to the recipient.
    """

    resource_type = "CommunicationRequestPayload"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.contentAttachment = None
        """ Message part content.
        Type `Attachment` (represented as `dict` in JSON). """

        self.contentReference = None
        """ Message part content.
        Type `FHIRReference` referencing `['Resource']` (represented as `dict` in JSON). """

        self.contentString = None
        """ Message part content.
        Type `str`. """

        super(CommunicationRequestPayload, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(CommunicationRequestPayload, self).elementProperties()
        js.extend(
            [
                (
                    "contentAttachment",
                    "contentAttachment",
                    attachment.Attachment,
                    "Attachment",
                    False,
                    "content",
                    True,
                ),
                (
                    "contentReference",
                    "contentReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "content",
                    True,
                ),
                (
                    "contentString",
                    "contentString",
                    str,
                    "string",
                    False,
                    "content",
                    True,
                ),
            ]
        )
        return js


try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + ".annotation"]
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + ".attachment"]
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + ".fhirdate"]
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + ".fhirreference"]
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + ".identifier"]
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + ".period"]
