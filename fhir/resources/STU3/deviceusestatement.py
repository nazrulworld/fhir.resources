from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceUseStatement
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import domainresource, fhirtypes


class DeviceUseStatement(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Record of use of a device.
    A record of a device being used by a patient where the record is the result
    of a report from the patient or another clinician.
    """

    __resource_type__ = "DeviceUseStatement"

    bodySite: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="bodySite",
        title="Target body site",
        description=(
            "Indicates the site on the subject's body where the device was used ( "
            "i.e. the target site)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    device: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="device",
        title="Reference to device used",
        description="The details of the device used.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Device"],
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="External identifier for this record",
        description="An external identifier for this statement such as an IRI.",
        json_schema_extra={
            "element_property": True,
        },
    )

    indication: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="indication",
        title="Why device was used",
        description="Reason or justification for the use of the device.",
        json_schema_extra={
            "element_property": True,
        },
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="note",
        title="Addition details (comments, instructions)",
        description=(
            "Details about the device statement that were not represented at all or"
            " sufficiently in one of the attributes provided in a class. These may "
            "include for example a comment, an instruction, or a note associated "
            "with the statement."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    recordedOn: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="recordedOn",
        title="When statement was recorded",
        description="The time at which the statement was made/recorded.",
        json_schema_extra={
            "element_property": True,
        },
    )
    recordedOn__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_recordedOn", title="Extension field for ``recordedOn``."
    )

    source: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="source",
        title="Who made the statement",
        description="Who reported the device was being used by the patient.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "Practitioner", "RelatedPerson"],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="active | completed | entered-in-error +",
        description=(
            "A code representing the patient or other source's judgment about the "
            "state of the device used that this statement is about.  Generally this"
            " will be active or completed."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["active", "completed", "entered-in-error", "+"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="subject",
        title="Patient using device",
        description="The patient who used the device.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "Group"],
        },
    )

    timingDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="timingDateTime",
        title="How often  the device was used",
        description="How often the device was used.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e timing[x]
            "one_of_many": "timing",
            "one_of_many_required": False,
        },
    )
    timingDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_timingDateTime", title="Extension field for ``timingDateTime``."
    )

    timingPeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="timingPeriod",
        title="How often  the device was used",
        description="How often the device was used.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e timing[x]
            "one_of_many": "timing",
            "one_of_many_required": False,
        },
    )

    timingTiming: fhirtypes.TimingType | None = Field(  # type: ignore
        None,
        alias="timingTiming",
        title="How often  the device was used",
        description="How often the device was used.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e timing[x]
            "one_of_many": "timing",
            "one_of_many_required": False,
        },
    )

    whenUsed: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="whenUsed",
        title="Period device was used",
        description="The time period over which the device was used.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceUseStatement`` according specification,
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
            "status",
            "subject",
            "whenUsed",
            "timingTiming",
            "timingPeriod",
            "timingDateTime",
            "recordedOn",
            "source",
            "device",
            "indication",
            "bodySite",
            "note",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        return required_fields

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
        one_of_many_fields = {
            "timing": ["timingDateTime", "timingPeriod", "timingTiming"]
        }
        return one_of_many_fields
