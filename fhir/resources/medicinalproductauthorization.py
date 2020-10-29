# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductAuthorization
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
import typing

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class MedicinalProductAuthorization(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The regulatory authorization of a medicinal product.
    """

    resource_type = Field("MedicinalProductAuthorization", const=True)

    country: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="country",
        title="The country in which the marketing authorization has been granted",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    dataExclusivityPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="dataExclusivityPeriod",
        title=(
            "A period of time after authorization before generic product "
            "applicatiosn can be submitted"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    dateOfFirstAuthorization: fhirtypes.DateTime = Field(
        None,
        alias="dateOfFirstAuthorization",
        title=(
            "The date when the first authorization was granted by a Medicines "
            "Regulatory Agency"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    dateOfFirstAuthorization__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_dateOfFirstAuthorization",
        title="Extension field for ``dateOfFirstAuthorization``.",
    )

    holder: fhirtypes.ReferenceType = Field(
        None,
        alias="holder",
        title="Marketing Authorization Holder",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title=(
            "Business identifier for the marketing authorization, as assigned by a "
            "regulator"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    internationalBirthDate: fhirtypes.DateTime = Field(
        None,
        alias="internationalBirthDate",
        title=(
            "Date of first marketing authorization for a company's new medicinal "
            "product in any country in the World"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    internationalBirthDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_internationalBirthDate",
        title="Extension field for ``internationalBirthDate``.",
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Jurisdiction within a country",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    jurisdictionalAuthorization: typing.List[
        fhirtypes.MedicinalProductAuthorizationJurisdictionalAuthorizationType
    ] = Field(
        None,
        alias="jurisdictionalAuthorization",
        title="Authorization in areas within a country",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    legalBasis: fhirtypes.CodeableConceptType = Field(
        None,
        alias="legalBasis",
        title="The legal framework against which this authorization is granted",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    procedure: fhirtypes.MedicinalProductAuthorizationProcedureType = Field(
        None,
        alias="procedure",
        title=(
            "The regulatory procedure for granting or amending a marketing "
            "authorization"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    regulator: fhirtypes.ReferenceType = Field(
        None,
        alias="regulator",
        title="Medicines Regulatory Agency",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    restoreDate: fhirtypes.DateTime = Field(
        None,
        alias="restoreDate",
        title=(
            "The date when a suspended the marketing or the marketing authorization"
            " of the product is anticipated to be restored"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    restoreDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_restoreDate", title="Extension field for ``restoreDate``."
    )

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title="The status of the marketing authorization",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    statusDate: fhirtypes.DateTime = Field(
        None,
        alias="statusDate",
        title="The date at which the given status has become applicable",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    statusDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_statusDate", title="Extension field for ``statusDate``."
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="The medicinal product that is being authorized",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicinalProduct", "MedicinalProductPackaged"],
    )

    validityPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="validityPeriod",
        title=(
            "The beginning of the time period in which the marketing authorization "
            "is in the specific status shall be specified A complete date "
            "consisting of day, month and year shall be specified using the ISO "
            "8601 date format"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
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
        title="Country of authorization",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="The assigned number for the marketing authorization",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Jurisdiction within a country",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    legalStatusOfSupply: fhirtypes.CodeableConceptType = Field(
        None,
        alias="legalStatusOfSupply",
        title="The legal status of supply in a jurisdiction or region",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    validityPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="validityPeriod",
        title="The start and expected end date of the authorization",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class MedicinalProductAuthorizationProcedure(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The regulatory procedure for granting or amending a marketing authorization.
    """

    resource_type = Field("MedicinalProductAuthorizationProcedure", const=True)

    application: typing.List[
        fhirtypes.MedicinalProductAuthorizationProcedureType
    ] = Field(
        None,
        alias="application",
        title="Applcations submitted to obtain a marketing authorization",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    dateDateTime: fhirtypes.DateTime = Field(
        None,
        alias="dateDateTime",
        title="Date of procedure",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e date[x]
        one_of_many="date",
        one_of_many_required=False,
    )
    dateDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_dateDateTime", title="Extension field for ``dateDateTime``."
    )

    datePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="datePeriod",
        title="Date of procedure",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e date[x]
        one_of_many="date",
        one_of_many_required=False,
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Identifier for this procedure",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type of procedure",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @root_validator(pre=True)
    def validate_one_of_many(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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
