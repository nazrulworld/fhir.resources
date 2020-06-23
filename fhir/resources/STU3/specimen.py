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
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Identifier assigned by the lab",
    )

    collection: fhirtypes.SpecimenCollectionType = Field(
        None,
        alias="collection",
        title="Type `SpecimenCollection` (represented as `dict` in JSON)",
        description="Collection details",
    )

    container: ListType[fhirtypes.SpecimenContainerType] = Field(
        None,
        alias="container",
        title="List of `SpecimenContainer` items (represented as `dict` in JSON)",
        description="Direct container of specimen (tube/slide, etc.)",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="External Identifier",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Comments",
    )

    parent: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="parent",
        title=(
            "List of `Reference` items referencing `Specimen` (represented as "
            "`dict` in JSON)"
        ),
        description="Specimen from which this specimen originated",
    )

    processing: ListType[fhirtypes.SpecimenProcessingType] = Field(
        None,
        alias="processing",
        title="List of `SpecimenProcessing` items (represented as `dict` in JSON)",
        description="Processing and processing step details",
    )

    receivedTime: fhirtypes.DateTime = Field(
        None,
        alias="receivedTime",
        title="Type `DateTime`",
        description="The time when specimen was received for processing",
    )
    receivedTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_receivedTime", title="Extension field for ``receivedTime``."
    )

    request: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="request",
        title=(
            "List of `Reference` items referencing `ProcedureRequest` (represented "
            "as `dict` in JSON)"
        ),
        description="Why the specimen was collected",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code`",
        description="available | unavailable | unsatisfactory | entered-in-error",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title=(
            "Type `Reference` referencing `Patient, Group, Device, Substance` "
            "(represented as `dict` in JSON)"
        ),
        description=(
            "Where the specimen came from. This may be from the patient(s) or from "
            "the environment or a device"
        ),
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Kind of material that forms the specimen",
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
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Anatomical collection site",
    )

    collectedDateTime: fhirtypes.DateTime = Field(
        None,
        alias="collectedDateTime",
        title="Type `DateTime`",
        description="Collection time",
        one_of_many="collected",  # Choice of Data Types. i.e value[x]
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
        title="Type `Period` (represented as `dict` in JSON)",
        description="Collection time",
        one_of_many="collected",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    collector: fhirtypes.ReferenceType = Field(
        None,
        alias="collector",
        title=(
            "Type `Reference` referencing `Practitioner` (represented as `dict` in "
            "JSON)"
        ),
        description="Who collected the specimen",
    )

    method: fhirtypes.CodeableConceptType = Field(
        None,
        alias="method",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Technique used to perform collection",
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="The quantity of specimen collected",
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
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Additive associated with container",
        one_of_many="additive",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    additiveReference: fhirtypes.ReferenceType = Field(
        None,
        alias="additiveReference",
        title=(
            "Type `Reference` referencing `Substance` (represented as `dict` in "
            "JSON)"
        ),
        description="Additive associated with container",
        one_of_many="additive",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    capacity: fhirtypes.QuantityType = Field(
        None,
        alias="capacity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Container volume or size",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Textual description of the container",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Id for the container",
    )

    specimenQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="specimenQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Quantity of specimen within container",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Kind of container directly associated with specimen",
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
        title=(
            "List of `Reference` items referencing `Substance` (represented as "
            "`dict` in JSON)"
        ),
        description="Material used in the processing step",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Textual description of procedure",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    procedure: fhirtypes.CodeableConceptType = Field(
        None,
        alias="procedure",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Indicates the treatment step  applied to the specimen",
    )

    timeDateTime: fhirtypes.DateTime = Field(
        None,
        alias="timeDateTime",
        title="Type `DateTime`",
        description="Date and time of specimen processing",
        one_of_many="time",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    timeDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_timeDateTime", title="Extension field for ``timeDateTime``."
    )

    timePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="timePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Date and time of specimen processing",
        one_of_many="time",  # Choice of Data Types. i.e value[x]
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
