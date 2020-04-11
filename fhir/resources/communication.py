# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Communication
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class Communication(domainresource.DomainResource):
    """ A record of information transmitted from a sender to a receiver.

    An occurrence of information being transmitted; e.g. an alert that was sent
    to a responsible provider, a public health agency that was notified about a
    reportable condition.
    """

    resource_type = "Communication"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.about = None
        """ Resources that pertain to this communication.
        List of `FHIRReference` items referencing `['Resource']` (represented as `dict` in JSON). """

        self.basedOn = None
        """ Request fulfilled by this communication.
        List of `FHIRReference` items referencing `['Resource']` (represented as `dict` in JSON). """

        self.category = None
        """ Message category.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.encounter = None
        """ Encounter created as part of.
        Type `FHIRReference` referencing `['Encounter']` (represented as `dict` in JSON). """

        self.identifier = None
        """ Unique identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.inResponseTo = None
        """ Reply to.
        List of `FHIRReference` items referencing `['Communication']` (represented as `dict` in JSON). """

        self.instantiatesCanonical = None
        """ Instantiates FHIR protocol or definition.
        List of `str` items referencing `['PlanDefinition', 'ActivityDefinition', 'Measure', 'OperationDefinition', 'Questionnaire']`. """

        self.instantiatesUri = None
        """ Instantiates external protocol or definition.
        List of `str` items. """

        self.medium = None
        """ A channel of communication.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.note = None
        """ Comments made about the communication.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.partOf = None
        """ Part of this action.
        List of `FHIRReference` items referencing `['Resource']` (represented as `dict` in JSON). """

        self.payload = None
        """ Message payload.
        List of `CommunicationPayload` items (represented as `dict` in JSON). """

        self.priority = None
        """ routine | urgent | asap | stat.
        Type `str`. """

        self.reasonCode = None
        """ Indication for message.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.reasonReference = None
        """ Why was communication done?.
        List of `FHIRReference` items referencing `['Condition', 'Observation', 'DiagnosticReport', 'DocumentReference']` (represented as `dict` in JSON). """

        self.received = None
        """ When received.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.recipient = None
        """ Message recipient.
        List of `FHIRReference` items referencing `['Device', 'Organization', 'Patient', 'Practitioner', 'PractitionerRole', 'RelatedPerson', 'Group', 'CareTeam', 'HealthcareService']` (represented as `dict` in JSON). """

        self.sender = None
        """ Message sender.
        Type `FHIRReference` referencing `['Device', 'Organization', 'Patient', 'Practitioner', 'PractitionerRole', 'RelatedPerson', 'HealthcareService']` (represented as `dict` in JSON). """

        self.sent = None
        """ When sent.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.status = None
        """ preparation | in-progress | not-done | on-hold | stopped |
        completed | entered-in-error | unknown.
        Type `str`. """

        self.statusReason = None
        """ Reason for current status.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.subject = None
        """ Focus of message.
        Type `FHIRReference` referencing `['Patient', 'Group']` (represented as `dict` in JSON). """

        self.topic = None
        """ Description of the purpose/content.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(Communication, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Communication, self).elementProperties()
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
                    "identifier",
                    "identifier",
                    identifier.Identifier,
                    "Identifier",
                    True,
                    None,
                    False,
                ),
                (
                    "inResponseTo",
                    "inResponseTo",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "instantiatesCanonical",
                    "instantiatesCanonical",
                    str,
                    "canonical",
                    True,
                    None,
                    False,
                ),
                ("instantiatesUri", "instantiatesUri", str, "uri", True, None, False),
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
                    "partOf",
                    "partOf",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "payload",
                    "payload",
                    CommunicationPayload,
                    "CommunicationPayload",
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
                    "received",
                    "received",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
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
                    "sender",
                    "sender",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("sent", "sent", fhirdate.FHIRDate, "dateTime", False, None, False),
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
                (
                    "topic",
                    "topic",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


class CommunicationPayload(backboneelement.BackboneElement):
    """ Message payload.

    Text, attachment(s), or resource(s) that was communicated to the recipient.
    """

    resource_type = "CommunicationPayload"

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

        super(CommunicationPayload, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CommunicationPayload, self).elementProperties()
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
