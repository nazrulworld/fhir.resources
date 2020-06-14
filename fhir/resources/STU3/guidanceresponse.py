# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/GuidanceResponse
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import domainresource, fhirtypes


class GuidanceResponse(domainresource.DomainResource):
    """ The formal response to a guidance request.
    A guidance response is the formal response to a guidance request, including
    any output parameters returned by the evaluation, as well as the
    description of any proposed actions to be taken.
    """

    resource_type = Field("GuidanceResponse", const=True)

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title="Type `Reference` referencing `Encounter, EpisodeOfCare` (represented as `dict` in JSON)",
        description="Encounter or Episode during which the response was returned",
    )

    dataRequirement: ListType[fhirtypes.DataRequirementType] = Field(
        None,
        alias="dataRequirement",
        title="List of `DataRequirement` items (represented as `dict` in JSON)",
        description="Additional required data",
    )

    evaluationMessage: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="evaluationMessage",
        title="List of `Reference` items referencing `OperationOutcome` (represented as `dict` in JSON)",
        description="Messages resulting from the evaluation of the artifact or artifacts",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Business identifier",
    )

    module: fhirtypes.ReferenceType = Field(
        ...,
        alias="module",
        title="Type `Reference` referencing `ServiceDefinition` (represented as `dict` in JSON)",
        description="A reference to a knowledge module",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Additional notes about the response",
    )

    occurrenceDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurrenceDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When the guidance response was processed",
    )

    outputParameters: fhirtypes.ReferenceType = Field(
        None,
        alias="outputParameters",
        title="Type `Reference` referencing `Parameters` (represented as `dict` in JSON)",
        description="The output parameters of the evaluation, if any",
    )

    performer: fhirtypes.ReferenceType = Field(
        None,
        alias="performer",
        title="Type `Reference` referencing `Device` (represented as `dict` in JSON)",
        description="Device returning the guidance",
    )

    reasonCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reasonCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Reason for the response",
        one_of_many="reason",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    reasonReference: fhirtypes.ReferenceType = Field(
        None,
        alias="reasonReference",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="Reason for the response",
        one_of_many="reason",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    requestId: fhirtypes.Id = Field(
        None,
        alias="requestId",
        title="Type `Id` (represented as `dict` in JSON)",
        description="The id of the request associated with this response, if any",
    )

    result: fhirtypes.ReferenceType = Field(
        None,
        alias="result",
        title="Type `Reference` referencing `CarePlan, RequestGroup` (represented as `dict` in JSON)",
        description="Proposed actions, if any",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="success | data-requested | data-required | in-progress | failure | entered-in-error",
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Type `Reference` referencing `Patient, Group` (represented as `dict` in JSON)",
        description="Patient the request was performed for",
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
            "reason": ["reasonCodeableConcept", "reasonReference",],
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
