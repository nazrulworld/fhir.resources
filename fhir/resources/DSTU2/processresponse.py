# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/DSTU2/processresponse.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic.v1 import Field

from . import domainresource, fhirtypes
from .backboneelement import BackboneElement


class ProcessResponse(domainresource.DomainResource):
    """ProcessResponse resource

    This resource provides processing status,
    errors and notes from the processing of a resource.
    """

    resource_type = Field("ProcessResponse", const=True)

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier",
        description="The Response business identifier.",
        element_property=True,
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title="Type 'Reference' referencing 'Any'  (represented as 'dict' in JSON).",
        description="Original request resource reference.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Any"],
        element_property=True,
    )

    outcome: fhirtypes.CodingType = Field(
        None,
        alias="outcome",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Transaction status: error, complete, held.",
        element_property=True,
    )

    disposition: fhirtypes.String = Field(
        None,
        alias="disposition",
        title="Type `String` (represented as `dict` in JSON)",
        description="Disposition Message",
        element_property=True,
    )

    ruleset: fhirtypes.CodingType = Field(
        None,
        alias="ruleset",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Resource version",
        element_property=True,
    )

    originalRuleset: fhirtypes.CodingType = Field(
        None,
        alias="originalRuleset",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Original version",
        element_property=True,
    )

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Creation date",
        description="The date when the enclosed suite of services were performed or completed.",
        element_property=True,
    )

    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title="Type 'Reference' referencing 'Organization'  (represented as 'dict' in JSON).",
        description="Authoring Organization",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
        element_property=True,
    )

    requestProvider: fhirtypes.ReferenceType = Field(
        None,
        alias="requestProvider",
        title="Type 'Reference' referencing 'Practitioner'  (represented as 'dict' in JSON).",
        description="Responsible Practitioner",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
        element_property=True,
    )

    requestOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="requestOrganization",
        title="Type 'Reference' referencing 'Organization'  (represented as 'dict' in JSON).",
        description="Responsible organization",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
        element_property=True,
    )

    form: fhirtypes.CodingType = Field(
        None,
        alias="form",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Printed Form Identifier",
        element_property=True,
    )

    notes: ListType[fhirtypes.ProcessResponseNotesType] = Field(
        None,
        alias="notes",
        title=(
            "Suite of processing note or additional requirements"
            " is the processing has been held."
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    error: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="error",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Error code",
        element_property=True,
    )


class ProcessResponseNotes(BackboneElement):
    """Notes


    Suite of processing note or additional requirements is the processing has been held.
    """

    resource_type = Field("ProcessResponseNotes", const=True)

    type: fhirtypes.CodingType = Field(
        None,
        alias="type",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="display | print | printoper",
        element_property=True,
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Type `String` (represented as `dict` in JSON)",
        description="Notes text",
        element_property=True,
    )
