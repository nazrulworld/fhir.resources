# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/RegulatedAuthorization
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class RegulatedAuthorization(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Regulatory approval, clearance or licencing related to a regulated product,
    treatment, facility or activity e.g. Market Authorization for a Medicinal
    Product.
    Regulatory approval, clearance or licencing related to a regulated product,
    treatment, facility or activity that is cited in a guidance, regulation,
    rule or legislative act. An example is Market Authorization relating to a
    Medicinal Product.
    """

    resource_type = Field("RegulatedAuthorization", const=True)

    basis: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="basis",
        title=(
            "The legal/regulatory framework or reasons under which this "
            "authorization is granted"
        ),
        description=(
            "The legal or regulatory framework against which this authorization is "
            "granted, or other reasons for it."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    case: fhirtypes.RegulatedAuthorizationCaseType = Field(
        None,
        alias="case",
        title=(
            "The case or regulatory procedure for granting or amending a regulated "
            "authorization. Note: This area is subject to ongoing review and the "
            "workgroup is seeking implementer feedback on its use (see link at "
            "bottom of page)"
        ),
        description=(
            "The case or regulatory procedure for granting or amending a regulated "
            "authorization. An authorization is granted in response to "
            "submissions/applications by those seeking authorization. A case is the"
            " administrative process that deals with the application(s) that relate"
            " to this and assesses them. Note: This area is subject to ongoing "
            "review and the workgroup is seeking implementer feedback on its use "
            "(see link at bottom of page)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="General textual supporting information",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    holder: fhirtypes.ReferenceType = Field(
        None,
        alias="holder",
        title=(
            "The organization that has been granted this authorization, by the "
            "regulator"
        ),
        description=(
            "The organization that has been granted this authorization, by some "
            "authoritative body (the 'regulator')."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title=(
            "Business identifier for the authorization, typically assigned by the "
            "authorizing body"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    indication: fhirtypes.CodeableReferenceType = Field(
        None,
        alias="indication",
        title="Condition for which the use of the regulated product applies",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ClinicalUseDefinition"],
    )

    intendedUse: fhirtypes.CodeableConceptType = Field(
        None,
        alias="intendedUse",
        title="The intended use of the product, e.g. prevention, treatment",
        description=(
            "The intended use of the product, e.g. prevention, treatment, " "diagnosis."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    region: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="region",
        title="The territory in which the authorization has been granted",
        description=(
            "The territory (e.g., country, jurisdiction etc.) in which the "
            "authorization has been granted."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    regulator: fhirtypes.ReferenceType = Field(
        None,
        alias="regulator",
        title=(
            "The regulatory authority or authorizing body granting the " "authorization"
        ),
        description=(
            "The regulatory authority or authorizing body granting the "
            "authorization. For example, European Medicines Agency (EMA), Food and "
            "Drug Administration (FDA), Health Canada (HC), etc."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title=(
            "The status that is authorised e.g. approved. Intermediate states can "
            "be tracked with cases and applications"
        ),
        description=(
            "The status that is authorised e.g. approved. Intermediate states and "
            "actions can be tracked with cases and applications."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    statusDate: fhirtypes.DateTime = Field(
        None,
        alias="statusDate",
        title="The date at which the current status was assigned",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    statusDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_statusDate", title="Extension field for ``statusDate``."
    )

    subject: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="subject",
        title=(
            "The product type, treatment, facility or activity that is being "
            "authorized"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "MedicinalProductDefinition",
            "BiologicallyDerivedProduct",
            "NutritionProduct",
            "PackagedProductDefinition",
            "SubstanceDefinition",
            "DeviceDefinition",
            "ResearchStudy",
            "ActivityDefinition",
            "PlanDefinition",
            "ObservationDefinition",
            "Practitioner",
            "Organization",
            "Location",
        ],
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title=(
            "Overall type of this authorization, for example drug marketing "
            "approval, orphan drug designation"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    validityPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="validityPeriod",
        title=(
            "The time period in which the regulatory approval etc. is in effect, "
            "e.g. a Marketing Authorization includes the date of authorization "
            "and/or expiration date"
        ),
        description=(
            "The time period in which the regulatory approval, clearance or "
            "licencing is in effect. As an example, a Marketing Authorization "
            "includes the date of authorization and/or an expiration date."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``RegulatedAuthorization`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "identifier",
            "subject",
            "type",
            "description",
            "region",
            "status",
            "statusDate",
            "validityPeriod",
            "indication",
            "intendedUse",
            "basis",
            "holder",
            "regulator",
            "case",
        ]


class RegulatedAuthorizationCase(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The case or regulatory procedure for granting or amending a regulated
    authorization. Note: This area is subject to ongoing review and the
    workgroup is seeking implementer feedback on its use (see link at bottom of
    page).
    The case or regulatory procedure for granting or amending a regulated
    authorization. An authorization is granted in response to
    submissions/applications by those seeking authorization. A case is the
    administrative process that deals with the application(s) that relate to
    this and assesses them. Note: This area is subject to ongoing review and
    the workgroup is seeking implementer feedback on its use (see link at
    bottom of page).
    """

    resource_type = Field("RegulatedAuthorizationCase", const=True)

    application: typing.List[fhirtypes.RegulatedAuthorizationCaseType] = Field(
        None,
        alias="application",
        title=(
            "Applications submitted to obtain a regulated authorization. Steps "
            "within the longer running case or procedure"
        ),
        description=(
            "A regulatory submission from an organization to a regulator, as part "
            "of an assessing case. Multiple applications may occur over time, with "
            "more or different information to support or modify the submission or "
            "the authorization. The applications can be considered as steps within "
            "the longer running case or procedure for this authorization process."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    dateDateTime: fhirtypes.DateTime = Field(
        None,
        alias="dateDateTime",
        title="Relevant date for this case",
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
        title="Relevant date for this case",
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
        title="Identifier by which this case can be referenced",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title="The status associated with the case",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="The defining type of case",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``RegulatedAuthorizationCase`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "identifier",
            "type",
            "status",
            "datePeriod",
            "dateDateTime",
            "application",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2881(
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
