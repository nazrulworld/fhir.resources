# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AppointmentResponse
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import domainresource


class AppointmentResponse(domainresource.DomainResource):
    """ A reply to an appointment request for a patient and/or practitioner(s),
    such as a confirmation or rejection.
    """

    resource_type = "AppointmentResponse"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.actor = None
        """ Person, Location, HealthcareService, or Device.
        Type `FHIRReference` referencing `['Patient', 'Practitioner', 'PractitionerRole', 'RelatedPerson', 'Device', 'HealthcareService', 'Location']` (represented as `dict` in JSON). """

        self.appointment = None
        """ Appointment this response relates to.
        Type `FHIRReference` referencing `['Appointment']` (represented as `dict` in JSON). """

        self.comment = None
        """ Additional comments.
        Type `str`. """

        self.end = None
        """ Time from appointment, or requested new end time.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.identifier = None
        """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.participantStatus = None
        """ accepted | declined | tentative | needs-action.
        Type `str`. """

        self.participantType = None
        """ Role of participant in the appointment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.start = None
        """ Time from appointment, or requested new start time.
        Type `FHIRDate` (represented as `str` in JSON). """

        super(AppointmentResponse, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(AppointmentResponse, self).elementProperties()
        js.extend(
            [
                (
                    "actor",
                    "actor",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "appointment",
                    "appointment",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                ("comment", "comment", str, "string", False, None, False),
                ("end", "end", fhirdate.FHIRDate, "instant", False, None, False),
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
                    "participantStatus",
                    "participantStatus",
                    str,
                    "code",
                    False,
                    None,
                    True,
                ),
                (
                    "participantType",
                    "participantType",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                ("start", "start", fhirdate.FHIRDate, "instant", False, None, False),
            ]
        )
        return js


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
