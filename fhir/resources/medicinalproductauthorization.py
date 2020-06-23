# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductAuthorization
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class MedicinalProductAuthorization(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The regulatory authorization of a medicinal product.
    """

    resource_type = Field("MedicinalProductAuthorization", const=True)

    country: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="country",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="The country in which the marketing authorization has been granted",
    )

    dataExclusivityPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="dataExclusivityPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description=(
            "A period of time after authorization before generic product "
            "applicatiosn can be submitted"
        ),
    )

    dateOfFirstAuthorization: fhirtypes.DateTime = Field(
        None,
        alias="dateOfFirstAuthorization",
        title="Type `DateTime`",
        description=(
            "The date when the first authorization was granted by a Medicines "
            "Regulatory Agency"
        ),
    )
    dateOfFirstAuthorization__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_dateOfFirstAuthorization",
        title="Extension field for ``dateOfFirstAuthorization``.",
    )

    holder: fhirtypes.ReferenceType = Field(
        None,
        alias="holder",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Marketing Authorization Holder",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description=(
            "Business identifier for the marketing authorization, as assigned by a "
            "regulator"
        ),
    )

    internationalBirthDate: fhirtypes.DateTime = Field(
        None,
        alias="internationalBirthDate",
        title="Type `DateTime`",
        description=(
            "Date of first marketing authorization for a company\u0027s new medicinal "
            "product in any country in the World"
        ),
    )
    internationalBirthDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_internationalBirthDate",
        title="Extension field for ``internationalBirthDate``.",
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Jurisdiction within a country",
    )

    jurisdictionalAuthorization: ListType[
        fhirtypes.MedicinalProductAuthorizationJurisdictionalAuthorizationType
    ] = Field(
        None,
        alias="jurisdictionalAuthorization",
        title=(
            "List of `MedicinalProductAuthorizationJurisdictionalAuthorization` "
            "items (represented as `dict` in JSON)"
        ),
        description="Authorization in areas within a country",
    )

    legalBasis: fhirtypes.CodeableConceptType = Field(
        None,
        alias="legalBasis",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The legal framework against which this authorization is granted",
    )

    procedure: fhirtypes.MedicinalProductAuthorizationProcedureType = Field(
        None,
        alias="procedure",
        title=(
            "Type `MedicinalProductAuthorizationProcedure` (represented as `dict` "
            "in JSON)"
        ),
        description=(
            "The regulatory procedure for granting or amending a marketing "
            "authorization"
        ),
    )

    regulator: fhirtypes.ReferenceType = Field(
        None,
        alias="regulator",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Medicines Regulatory Agency",
    )

    restoreDate: fhirtypes.DateTime = Field(
        None,
        alias="restoreDate",
        title="Type `DateTime`",
        description=(
            "The date when a suspended the marketing or the marketing authorization"
            " of the product is anticipated to be restored"
        ),
    )
    restoreDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_restoreDate", title="Extension field for ``restoreDate``."
    )

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The status of the marketing authorization",
    )

    statusDate: fhirtypes.DateTime = Field(
        None,
        alias="statusDate",
        title="Type `DateTime`",
        description="The date at which the given status has become applicable",
    )
    statusDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_statusDate", title="Extension field for ``statusDate``."
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title=(
            "Type `Reference` referencing `MedicinalProduct, "
            "MedicinalProductPackaged` (represented as `dict` in JSON)"
        ),
        description="The medicinal product that is being authorized",
    )

    validityPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="validityPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description=(
            "The beginning of the time period in which the marketing authorization "
            "is in the specific status shall be specified A complete date "
            "consisting of day, month and year shall be specified using the ISO "
            "8601 date format"
        ),
    )


class MedicinalProductAuthorizationJurisdictionalAuthorization(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Authorization in areas within a country.
    """

    resource_type = Field(
        "MedicinalProductAuthorizationJurisdictionalAuthorization", const=True
    )

    country: fhirtypes.CodeableConceptType = Field(
        None,
        alias="country",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Country of authorization",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="The assigned number for the marketing authorization",
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Jurisdiction within a country",
    )

    legalStatusOfSupply: fhirtypes.CodeableConceptType = Field(
        None,
        alias="legalStatusOfSupply",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The legal status of supply in a jurisdiction or region",
    )

    validityPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="validityPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="The start and expected end date of the authorization",
    )


class MedicinalProductAuthorizationProcedure(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The regulatory procedure for granting or amending a marketing authorization.
    """

    resource_type = Field("MedicinalProductAuthorizationProcedure", const=True)

    application: ListType[fhirtypes.MedicinalProductAuthorizationProcedureType] = Field(
        None,
        alias="application",
        title=(
            "List of `MedicinalProductAuthorizationProcedure` items (represented as"
            " `dict` in JSON)"
        ),
        description="Applcations submitted to obtain a marketing authorization",
    )

    dateDateTime: fhirtypes.DateTime = Field(
        None,
        alias="dateDateTime",
        title="Type `DateTime`",
        description="Date of procedure",
        one_of_many="date",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    dateDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_dateDateTime", title="Extension field for ``dateDateTime``."
    )

    datePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="datePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Date of procedure",
        one_of_many="date",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Identifier for this procedure",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of procedure",
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
        one_of_many_fields = {"date": ["dateDateTime", "datePeriod"]}
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
