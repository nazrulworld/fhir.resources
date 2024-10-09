from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/RegulatedAuthorization
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

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

    __resource_type__ = "RegulatedAuthorization"

    attachedDocument: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="attachedDocument",
        title=(
            "Additional information or supporting documentation about the "
            "authorization"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DocumentReference"],
        },
    )

    basis: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )

    case: fhirtypes.RegulatedAuthorizationCaseType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="General textual supporting information",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    holder: fhirtypes.ReferenceType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title=(
            "Business identifier for the authorization, typically assigned by the "
            "authorizing body"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    indication: typing.List[fhirtypes.CodeableReferenceType] | None = Field(  # type: ignore
        None,
        alias="indication",
        title="Condition for which the use of the regulated product applies",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ClinicalUseDefinition"],
        },
    )

    intendedUse: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="intendedUse",
        title="The intended use of the product, e.g. prevention, treatment",
        description=(
            "The intended use of the product, e.g. prevention, treatment, " "diagnosis."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    region: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="region",
        title="The territory in which the authorization has been granted",
        description=(
            "The territory (e.g., country, jurisdiction etc.) in which the "
            "authorization has been granted."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    regulator: fhirtypes.ReferenceType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    status: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )

    statusDate: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="statusDate",
        title="The date at which the current status was assigned",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    statusDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_statusDate", title="Extension field for ``statusDate``."
    )

    subject: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="subject",
        title=(
            "The product type, treatment, facility or activity that is being "
            "authorized"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "MedicinalProductDefinition",
                "BiologicallyDerivedProduct",
                "NutritionProduct",
                "PackagedProductDefinition",
                "ManufacturedItemDefinition",
                "Ingredient",
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
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title=(
            "Overall type of this authorization, for example drug marketing "
            "approval, orphan drug designation"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    validityPeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
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
            "attachedDocument",
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

    __resource_type__ = "RegulatedAuthorizationCase"

    application: typing.List[fhirtypes.RegulatedAuthorizationCaseType] | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )

    dateDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="dateDateTime",
        title="Relevant date for this case",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e date[x]
            "one_of_many": "date",
            "one_of_many_required": False,
        },
    )
    dateDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_dateDateTime", title="Extension field for ``dateDateTime``."
    )

    datePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="datePeriod",
        title="Relevant date for this case",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e date[x]
            "one_of_many": "date",
            "one_of_many_required": False,
        },
    )

    identifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Identifier by which this case can be referenced",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="status",
        title="The status associated with the case",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="The defining type of case",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
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

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
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
        return one_of_many_fields
