# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/RelatedArtifact
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import element


class RelatedArtifact(element.Element):
    """ Related artifacts for a knowledge resource.

    Related artifacts such as additional documentation, justification, or
    bibliographic references.
    """

    resource_type = "RelatedArtifact"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.citation = None
        """ Bibliographic citation for the artifact.
        Type `str`. """

        self.display = None
        """ Brief description of the related artifact.
        Type `str`. """

        self.document = None
        """ What document is being referenced.
        Type `Attachment` (represented as `dict` in JSON). """

        self.label = None
        """ Short label.
        Type `str`. """

        self.resource = None
        """ What resource is being referenced.
        Type `str` referencing `['Resource']`. """

        self.type = None
        """ documentation | justification | citation | predecessor | successor
        | derived-from | depends-on | composed-of.
        Type `str`. """

        self.url = None
        """ Where the artifact can be accessed.
        Type `str`. """

        super(RelatedArtifact, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(RelatedArtifact, self).elementProperties()
        js.extend(
            [
                ("citation", "citation", str, "markdown", False, None, False),
                ("display", "display", str, "string", False, None, False),
                (
                    "document",
                    "document",
                    attachment.Attachment,
                    "Attachment",
                    False,
                    None,
                    False,
                ),
                ("label", "label", str, "string", False, None, False),
                ("resource", "resource", str, "canonical", False, None, False),
                ("type", "type", str, "code", False, None, True),
                ("url", "url", str, "url", False, None, False),
            ]
        )
        return js


try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + ".attachment"]
