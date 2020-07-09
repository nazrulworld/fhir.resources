# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceUseStatement
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import domainresource, fhirtypes


class DeviceUseStatement(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Record of use of a device.
    A record of a device being used by a patient where the record is the result
    of a report from the patient or another clinician.
    """

    resource_type = Field("DeviceUseStatement", const=True)

    basedOn: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="Fulfills plan, proposal or order",
        description=(
            "A plan, proposal or order that is fulfilled in whole or in part by "
            "this DeviceUseStatement."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ServiceRequest"],
    )

    bodySite: fhirtypes.CodeableConceptType = Field(
        None,
        alias="bodySite",
        title="Target body site",
        description=(
            "Indicates the anotomic location on the subject's body where the device"
            " was used ( i.e. the target)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    derivedFrom: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="derivedFrom",
        title="Supporting information",
        description=(
            "Allows linking the DeviceUseStatement to the underlying Request, or to"
            " other information that supports or is used to derive the "
            "DeviceUseStatement."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "ServiceRequest",
            "Procedure",
            "Claim",
            "Observation",
            "QuestionnaireResponse",
            "DocumentReference",
        ],
    )

    device: fhirtypes.ReferenceType = Field(
        ...,
        alias="device",
        title="Reference to device used",
        description="The details of the device used.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device"],
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="External identifier for this record",
        description="An external identifier for this statement such as an IRI.",
        # if property is element of this resource.
        element_property=True,
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Addition details (comments, instructions)",
        description=(
            "Details about the device statement that were not represented at all or"
            " sufficiently in one of the attributes provided in a class. These may "
            "include for example a comment, an instruction, or a note associated "
            "with the statement."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    reasonCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="Why device was used",
        description="Reason or justification for the use of the device.",
        # if property is element of this resource.
        element_property=True,
    )

    reasonReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title="Why was DeviceUseStatement performed?",
        description=(
            "Indicates another resource whose existence justifies this "
            "DeviceUseStatement."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Condition",
            "Observation",
            "DiagnosticReport",
            "DocumentReference",
            "Media",
        ],
    )

    recordedOn: fhirtypes.DateTime = Field(
        None,
        alias="recordedOn",
        title="When statement was recorded",
        description="The time at which the statement was made/recorded.",
        # if property is element of this resource.
        element_property=True,
    )
    recordedOn__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_recordedOn", title="Extension field for ``recordedOn``."
    )

    source: fhirtypes.ReferenceType = Field(
        None,
        alias="source",
        title="Who made the statement",
        description="Who reported the device was being used by the patient.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "Practitioner",
            "PractitionerRole",
            "RelatedPerson",
        ],
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="active | completed | entered-in-error +",
        description=(
            "A code representing the patient or other source's judgment about the "
            "state of the device used that this statement is about.  Generally this"
            " will be active or completed."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "completed", "entered-in-error", "+"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Patient using device",
        description="The patient who used the device.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group"],
    )

    timingDateTime: fhirtypes.DateTime = Field(
        None,
        alias="timingDateTime",
        title="How often  the device was used",
        description="How often the device was used.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e timing[x]
        one_of_many="timing",
        one_of_many_required=False,
    )
    timingDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_timingDateTime", title="Extension field for ``timingDateTime``."
    )

    timingPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="timingPeriod",
        title="How often  the device was used",
        description="How often the device was used.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e timing[x]
        one_of_many="timing",
        one_of_many_required=False,
    )

    timingTiming: fhirtypes.TimingType = Field(
        None,
        alias="timingTiming",
        title="How often  the device was used",
        description="How often the device was used.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e timing[x]
        one_of_many="timing",
        one_of_many_required=False,
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
            "timing": ["timingDateTime", "timingPeriod", "timingTiming"]
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
