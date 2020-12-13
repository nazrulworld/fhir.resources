# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/DSTU2/parameters.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import domainresource, fhirtypes
from .backboneelement import BackboneElement


class Parameters(domainresource.DomainResource):
    """Operation Request or Response


    This special resource type is used to represent an operation request
    and response (operations.html). It has no other use, and there is no
    RESTful endpoint associated with it.
    """

    resource_type = Field("Parameters", const=True)

    parameter: ListType[fhirtypes.ParametersParameterType] = Field(
        None,
        alias="parameter",
        title="Operation Parameter",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

class ParametersParameter(BackboneElement):
    """Operation Parameter


    A parameter passed to or received from the operation.
    """

    resource_type = Field("ParametersParameter", const=True)

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name from the definition",
        element_property=True,
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="If parameter is a data type.",
        description="If the parameter is a data type.",
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="valueDecimal",
        title="If parameter is a data type.",
        description="If the parameter is a data type.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="valueDateTime",
        title="If parameter is a data type.",
        description="If the parameter is a data type.",
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueDate: fhirtypes.Date = Field(
        None,
        alias="valueDate",
        title="If parameter is a data type.",
        description="If the parameter is a data type.",
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueInstant: fhirtypes.Instant = Field(
        None,
        alias="valueInstant",
        title="If parameter is a data type.",
        description="If the parameter is a data type.",
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="If parameter is a data type.",
        description="If the parameter is a data type.",
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueUri: fhirtypes.Uri = Field(
        None,
        alias="valueUri",
        title="If parameter is a data type.",
        description="If the parameter is a data type.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="If parameter is a data type.",
        description="If the parameter is a data type.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueCode: fhirtypes.Code = Field(
        None,
        alias="valueCode",
        title="If parameter is a data type.",
        description="If the parameter is a data type.",
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueBase64Binary: fhirtypes.Base64Binary = Field(
        None,
        alias="valueBase64Binary",
        title="If parameter is a data type",
        description="If the parameter is a data type.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueCoding: fhirtypes.CodingType = Field(
        None,
        alias="valueCoding",
        title="If parameter is a data type",
        description="If the parameter is a data type",
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="valueCodeableConcept",
        title="If parameter is a data type",
        description="If the parameter is a data type.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="If parameter is a data type",
        description="If the parameter is a data type.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="valueIdentifier",
        title="If parameter is a data type",
        description="If the parameter is a data type.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="If parameter is a data type",
        description="If the parameter is a data type.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueRange: fhirtypes.RangeType = Field(
        None,
        alias="valueRange",
        title="If parameter is a data type",
        description="If the parameter is a data type.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valuePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="valuePeriod",
        title="If parameter is a data type",
        description="If the parameter is a data type.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueRatio: fhirtypes.RatioType = Field(
        None,
        alias="valueRatio",
        title="If parameter is a data type",
        description="If the parameter is a data type.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueHumanName: fhirtypes.HumanNameType = Field(
        None,
        alias="valueHumanName",
        title="If parameter is a data type",
        description="If the parameter is a data type.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueAddress: fhirtypes.AddressType = Field(
        None,
        alias="valueAddress",
        title="If parameter is a data type",
        description="If the parameter is a data type.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueContactPoint: fhirtypes.ContactPointType = Field(
        None,
        alias="valueContactPoint",
        title="If parameter is a data type",
        description="If the parameter is a data type.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueSchedule: fhirtypes.ScheduleType = Field(
        None,
        alias="valueSchedule",
        title="If parameter is a data type",
        description="If the parameter is a data type.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueReference",
        title="If parameter is a data type",
        description="If the parameter is a data type",
        # note: Listed Resource Type(s) should be allowed as Reference.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    resource: fhirtypes.ResourceType = Field(
        None,
        alias="resource",
        title="If parameter is a whole resource",
        description="If the parameter is a whole resource.",
        # if property is element of this resource.
        element_property=True,
    )

    part: typing.List[fhirtypes.ParametersParameterType] = Field(
        None,
        alias="part",
        title="Named part of a parameter (e.g. Tuple)",
        description="A named part of a parameter. In many implementation context, a set of named parts is known as a "Tuple".",
        # if property is element of this resource.
        element_property=True,
    )
