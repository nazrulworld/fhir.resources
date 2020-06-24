# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Specimen
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Specimen(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Sample for analysis.
    A sample to be used for analysis.
    """

    resource_type = Field("Specimen", const=True)

    accessionIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="accessionIdentifier",
        title="Identifier assigned by the lab",
        description=(
            "The identifier assigned by the lab when accessioning specimen(s). This"
            " is not necessarily the same as the specimen identifier, depending on "
            "local lab procedures."
        ),
    )

    collection: fhirtypes.SpecimenCollectionType = Field(
        None,
        alias="collection",
        title="Collection details",
        description="Details concerning the specimen collection.",
    )

    container: ListType[fhirtypes.SpecimenContainerType] = Field(
        None,
        alias="container",
        title="Direct container of specimen (tube/slide, etc.)",
        description=(
            "The container holding the specimen.  The recursive nature of "
            "containers; i.e. blood in tube in tray in rack is not addressed here."
        ),
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="External Identifier",
        description="Id for specimen.",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Comments",
        description=(
            "To communicate any details or issues about the specimen or during the "
            "specimen collection. (for example: broken vial, sent with patient, "
            "frozen)."
        ),
    )

    parent: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="parent",
        title="Specimen from which this specimen originated",
        description=(
            "Reference to the parent (source) specimen which is used when the "
            "specimen was either derived from or a component of another specimen."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Specimen"],
    )

    processing: ListType[fhirtypes.SpecimenProcessingType] = Field(
        None,
        alias="processing",
        title="Processing and processing step details",
        description="Details concerning processing and processing steps for the specimen.",
    )

    receivedTime: fhirtypes.DateTime = Field(
        None,
        alias="receivedTime",
        title="The time when specimen was received for processing",
        description="Time when specimen was received for processing or testing.",
    )
    receivedTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_receivedTime", title="Extension field for ``receivedTime``."
    )

    request: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="request",
        title="Why the specimen was collected",
        description=(
            "Details concerning a test or procedure request that required a "
            "specimen to be collected."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ProcedureRequest"],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="available | unavailable | unsatisfactory | entered-in-error",
        description="The availability of the specimen.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["available", "unavailable", "unsatisfactory", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title=(
            "Where the specimen came from. This may be from the patient(s) or from "
            "the environment or a device"
        ),
        description=None,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group", "Device", "Substance"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Kind of material that forms the specimen",
        description="The kind of material that forms the specimen.",
    )


class SpecimenCollection(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Collection details.
    Details concerning the specimen collection.
    """

    resource_type = Field("SpecimenCollection", const=True)

    bodySite: fhirtypes.CodeableConceptType = Field(
        None,
        alias="bodySite",
        title="Anatomical collection site",
        description=(
            "Anatomical location from which the specimen was collected (if subject "
            "is a patient). This is the target site.  This element is not used for "
            "environmental specimens."
        ),
    )

    collectedDateTime: fhirtypes.DateTime = Field(
        None,
        alias="collectedDateTime",
        title="Collection time",
        description=(
            "Time when specimen was collected from subject - the physiologically "
            "relevant time."
        ),
        # Choice of Data Types. i.e collected[x]
        one_of_many="collected",
        one_of_many_required=False,
    )
    collectedDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_collectedDateTime",
        title="Extension field for ``collectedDateTime``.",
    )

    collectedPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="collectedPeriod",
        title="Collection time",
        description=(
            "Time when specimen was collected from subject - the physiologically "
            "relevant time."
        ),
        # Choice of Data Types. i.e collected[x]
        one_of_many="collected",
        one_of_many_required=False,
    )

    collector: fhirtypes.ReferenceType = Field(
        None,
        alias="collector",
        title="Who collected the specimen",
        description="Person who collected the specimen.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    method: fhirtypes.CodeableConceptType = Field(
        None,
        alias="method",
        title="Technique used to perform collection",
        description=(
            "A coded value specifying the technique that is used to perform the "
            "procedure."
        ),
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="The quantity of specimen collected",
        description=(
            "The quantity of specimen collected; for instance the volume of a blood"
            " sample, or the physical measurement of an anatomic pathology sample."
        ),
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
        one_of_many_fields = {"collected": ["collectedDateTime", "collectedPeriod"]}
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


class SpecimenContainer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Direct container of specimen (tube/slide, etc.).
    The container holding the specimen.  The recursive nature of containers;
    i.e. blood in tube in tray in rack is not addressed here.
    """

    resource_type = Field("SpecimenContainer", const=True)

    additiveCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="additiveCodeableConcept",
        title="Additive associated with container",
        description=(
            "Introduced substance to preserve, maintain or enhance the specimen. "
            "Examples: Formalin, Citrate, EDTA."
        ),
        # Choice of Data Types. i.e additive[x]
        one_of_many="additive",
        one_of_many_required=False,
    )

    additiveReference: fhirtypes.ReferenceType = Field(
        None,
        alias="additiveReference",
        title="Additive associated with container",
        description=(
            "Introduced substance to preserve, maintain or enhance the specimen. "
            "Examples: Formalin, Citrate, EDTA."
        ),
        # Choice of Data Types. i.e additive[x]
        one_of_many="additive",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Substance"],
    )

    capacity: fhirtypes.QuantityType = Field(
        None,
        alias="capacity",
        title="Container volume or size",
        description="The capacity (volume or other measure) the container may contain.",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Textual description of the container",
        description=None,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Id for the container",
        description=(
            "Id for container. There may be multiple; a manufacturer's bar code, "
            "lab assigned identifier, etc. The container ID may differ from the "
            "specimen id in some circumstances."
        ),
    )

    specimenQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="specimenQuantity",
        title="Quantity of specimen within container",
        description=(
            "The quantity of specimen in the container; may be volume, dimensions, "
            "or other appropriate measurements, depending on the specimen type."
        ),
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Kind of container directly associated with specimen",
        description=(
            "The type of container associated with the specimen (e.g. slide, "
            "aliquot, etc.)."
        ),
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
            "additive": ["additiveCodeableConcept", "additiveReference"]
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


class SpecimenProcessing(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Processing and processing step details.
    Details concerning processing and processing steps for the specimen.
    """

    resource_type = Field("SpecimenProcessing", const=True)

    additive: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="additive",
        title="Material used in the processing step",
        description=None,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Substance"],
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Textual description of procedure",
        description=None,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    procedure: fhirtypes.CodeableConceptType = Field(
        None,
        alias="procedure",
        title="Indicates the treatment step  applied to the specimen",
        description="A coded value specifying the procedure used to process the specimen.",
    )

    timeDateTime: fhirtypes.DateTime = Field(
        None,
        alias="timeDateTime",
        title="Date and time of specimen processing",
        description=(
            "A record of the time or period when the specimen processing occurred."
            "  For example the time of sample fixation or the period of time the "
            "sample was in formalin."
        ),
        # Choice of Data Types. i.e time[x]
        one_of_many="time",
        one_of_many_required=False,
    )
    timeDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_timeDateTime", title="Extension field for ``timeDateTime``."
    )

    timePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="timePeriod",
        title="Date and time of specimen processing",
        description=(
            "A record of the time or period when the specimen processing occurred."
            "  For example the time of sample fixation or the period of time the "
            "sample was in formalin."
        ),
        # Choice of Data Types. i.e time[x]
        one_of_many="time",
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
        one_of_many_fields = {"time": ["timeDateTime", "timePeriod"]}
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
