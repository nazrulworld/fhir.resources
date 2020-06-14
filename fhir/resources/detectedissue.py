# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DetectedIssue
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class DetectedIssue(domainresource.DomainResource):
    """ Clinical issue with action.
    Indicates an actual or potential clinical issue with or between one or more
    active or proposed clinical actions for a patient; e.g. Drug-drug
    interaction, Ineffective treatment frequency, Procedure-condition conflict,
    etc.
    """

    resource_type = Field("DetectedIssue", const=True)

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title="Type `Reference` referencing `Practitioner, PractitionerRole, Device` (represented as `dict` in JSON)",
        description="The provider or device that identified the issue",
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Issue Category, e.g. drug-drug, duplicate therapy, etc.",
    )

    detail: fhirtypes.String = Field(
        None,
        alias="detail",
        title="Type `String` (represented as `dict` in JSON)",
        description="Description and context",
    )

    evidence: ListType[fhirtypes.DetectedIssueEvidenceType] = Field(
        None,
        alias="evidence",
        title="List of `DetectedIssueEvidence` items (represented as `dict` in JSON)",
        description="Supporting evidence",
    )

    identifiedDateTime: fhirtypes.DateTime = Field(
        None,
        alias="identifiedDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When identified",
        one_of_many="identified",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    identifiedPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="identifiedPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When identified",
        one_of_many="identified",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Unique id for the detected issue",
    )

    implicated: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="implicated",
        title="List of `Reference` items referencing `Resource` (represented as `dict` in JSON)",
        description="Problem resource",
    )

    mitigation: ListType[fhirtypes.DetectedIssueMitigationType] = Field(
        None,
        alias="mitigation",
        title="List of `DetectedIssueMitigation` items (represented as `dict` in JSON)",
        description="Step taken to address",
    )

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="Associated patient",
    )

    reference: fhirtypes.Uri = Field(
        None,
        alias="reference",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Authority for issue",
    )

    severity: fhirtypes.Code = Field(
        None,
        alias="severity",
        title="Type `Code` (represented as `dict` in JSON)",
        description="high | moderate | low",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="registered | preliminary | final | amended +",
    )

    @root_validator(pre=True)
    def validate_one_of_many(cls, values: Dict[str, Any]) -> Dict[str, Any]:
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
            "identified": ["identifiedDateTime", "identifiedPeriod",],
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


class DetectedIssueEvidence(backboneelement.BackboneElement):
    """ Supporting evidence.
    Supporting evidence or manifestations that provide the basis for
    identifying the detected issue such as a GuidanceResponse or MeasureReport.
    """

    resource_type = Field("DetectedIssueEvidence", const=True)

    code: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="code",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Manifestation",
    )

    detail: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="detail",
        title="List of `Reference` items referencing `Resource` (represented as `dict` in JSON)",
        description="Supporting information",
    )


class DetectedIssueMitigation(backboneelement.BackboneElement):
    """ Step taken to address.
    Indicates an action that has been taken or is committed to reduce or
    eliminate the likelihood of the risk identified by the detected issue from
    manifesting.  Can also reflect an observation of known mitigating factors
    that may reduce/eliminate the need for any action.
    """

    resource_type = Field("DetectedIssueMitigation", const=True)

    action: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="action",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="What mitigation?",
    )

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title="Type `Reference` referencing `Practitioner, PractitionerRole` (represented as `dict` in JSON)",
        description="Who is committing?",
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date committed",
    )
