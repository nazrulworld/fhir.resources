# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EligibilityRequest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import domainresource, fhirtypes


class EligibilityRequest(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Determine insurance validity and scope of coverage.
    The EligibilityRequest provides patient and insurance coverage information
    to an insurer for them to respond, in the form of an EligibilityResponse,
    with information regarding whether the stated coverage is valid and in-
    force and optionally to provide the insurance details of the policy.
    """

    resource_type = Field("EligibilityRequest", const=True)

    benefitCategory: fhirtypes.CodeableConceptType = Field(
        None,
        alias="benefitCategory",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of services covered",
    )

    benefitSubCategory: fhirtypes.CodeableConceptType = Field(
        None,
        alias="benefitSubCategory",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Detailed services covered within the type",
    )

    businessArrangement: fhirtypes.String = Field(
        None,
        alias="businessArrangement",
        title="Type `String`",
        description="Business agreement",
    )
    businessArrangement__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_businessArrangement",
        title="Extension field for ``businessArrangement``.",
    )

    coverage: fhirtypes.ReferenceType = Field(
        None,
        alias="coverage",
        title=(
            "Type `Reference` referencing `Coverage` (represented as `dict` in " "JSON)"
        ),
        description="Insurance or medical plan",
    )

    created: fhirtypes.DateTime = Field(
        None, alias="created", title="Type `DateTime`", description="Creation date"
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
    )

    enterer: fhirtypes.ReferenceType = Field(
        None,
        alias="enterer",
        title=(
            "Type `Reference` referencing `Practitioner` (represented as `dict` in "
            "JSON)"
        ),
        description="Author",
    )

    facility: fhirtypes.ReferenceType = Field(
        None,
        alias="facility",
        title=(
            "Type `Reference` referencing `Location` (represented as `dict` in " "JSON)"
        ),
        description="Servicing Facility",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business Identifier",
    )

    insurer: fhirtypes.ReferenceType = Field(
        None,
        alias="insurer",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Target",
    )

    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Responsible organization",
    )

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="The subject of the Products and Services",
    )

    priority: fhirtypes.CodeableConceptType = Field(
        None,
        alias="priority",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Desired processing priority",
    )

    provider: fhirtypes.ReferenceType = Field(
        None,
        alias="provider",
        title=(
            "Type `Reference` referencing `Practitioner` (represented as `dict` in "
            "JSON)"
        ),
        description="Responsible practitioner",
    )

    servicedDate: fhirtypes.Date = Field(
        None,
        alias="servicedDate",
        title="Type `Date`",
        description="Estimated date or dates of Service",
        one_of_many="serviced",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    servicedDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_servicedDate", title="Extension field for ``servicedDate``."
    )

    servicedPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="servicedPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Estimated date or dates of Service",
        one_of_many="serviced",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code`",
        description="active | cancelled | draft | entered-in-error",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
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
        one_of_many_fields = {"serviced": ["servicedDate", "servicedPeriod"]}
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
