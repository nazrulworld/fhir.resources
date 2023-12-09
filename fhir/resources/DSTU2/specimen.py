# -*- coding: utf-8 -*-
"""
Profile: None
Release: DSTU2
Version: 1.0.2
Revision: None
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic.v1 import Field, root_validator

from . import fhirtypes
from .backboneelement import BackboneElement
from .domainresource import DomainResource


class Specimen(DomainResource):
    """
    Any material sample:
        - taken from a biological entity, living or dead
        - taken from a physical object or the environment
    Some specimens are biological and can contain one or more components
    including but not limited to cellular molecules, cells, tissues, organs,
    body fluids, embryos, and body excretory products (source: NCI Thesaurus,
    modified).

    The specimen resource covers substances used for diagnostic and
    environmental testing. The focus of the specimen resource is the process
    for gathering, maintaining and processing the specimen as well as where
    the specimen originated. This is distinct from the use of Substance which
    is only used when these other aspects are not relevant.
    """

    resource_type = Field("Specimen", const=True)

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON).",
        description="External Identifier",
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code`",
        description=("available | unavailable | unsatisfactory | entered-in-error"),
        enum_values=["available", "unavailable", "unsatisfactory", "entered-in-error"],
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="type",
        description="Kind of material that forms the specimen",
        # if property is element of this resource.
        element_property=True,
    )

    parent: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="parent",
        title="parent",
        description=("Specimen from which this specimen originated"),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Specimen"],
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="subject",
        description=(
            "Where the specimen came from. This may be from the patient(s) or "
            "from the environment or a device."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group", "Device", "Substance"],
    )

    accessionIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="accessionIdentifier",
        title="accessionIdentifier",
        description="Identifier assigned by the lab",
        # if property is element of this resource.
        element_property=True,
    )

    receivedTime: fhirtypes.DateTime = Field(
        None,
        alias="receivedTime",
        title="receivedTime",
        description="The time when specimen was received for processing",
        # if property is element of this resource.
        element_property=True,
    )

    collection_fhir: fhirtypes.SpecimenCollectionType = Field(
        None,
        alias="collection",
        title="collection",
        description="Collection details",
        # if property is element of this resource.
        element_property=True,
    )

    treatment: ListType[fhirtypes.SpecimenTreatmentType] = Field(
        None,
        alias="treatment",
        title="treatment",
        description="Treatment and processing step details",
        # if property is element of this resource.
        element_property=True,
    )

    container: ListType[fhirtypes.SpecimenContainerType] = Field(
        None,
        alias="container",
        title="container",
        description="Direct container of specimen (tube/slide, etc.)",
        # if property is element of this resource.
        element_property=True,
    )


class SpecimenCollection(BackboneElement):
    resource_type = Field("SpecimenCollection", const=True)

    collector: fhirtypes.ReferenceType = Field(
        None,
        alias="collector",
        title="collector",
        description="Who collected the specimen",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    comment: ListType[fhirtypes.String] = Field(
        None,
        alias="comment",
        title="Type `String` (represented as `dict` in JSON)",
        description="Collector comments",
        element_property=True,
    )

    collectedDateTime: fhirtypes.DateTime = Field(
        None,
        alias="collectedDateTime",
        title="collectedDateTime",
        description="Collection time",
        element_property=True,
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
        title="collectedPeriod",
        description="Collection time",
        element_property=True,
        # Choice of Data Types. i.e collected[x]
        one_of_many="collected",
        one_of_many_required=False,
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title=(
            "Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in "
            "JSON)."
        ),
        description="The quantity of specimen collected",
        element_property=True,
    )

    method: fhirtypes.CodeableConceptType = Field(
        None,
        alias="method",
        title="method",
        description="Technique used to perform collection",
        # if property is element of this resource.
        element_property=True,
    )

    bodySite: fhirtypes.CodeableConceptType = Field(
        None,
        alias="bodySite",
        title="bodySite",
        description="Anatomical collection site",
        # if property is element of this resource.
        element_property=True,
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
            "collected": ["collectedDateTime", "collectedPeriod"],
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


class SpecimenTreatment(BackboneElement):
    resource_type = Field("SpecimenTreatment", const=True)
    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Textual description of procedure",
        element_property=True,
    )

    procedure: fhirtypes.CodeableConceptType = Field(
        None,
        alias="procedure",
        title="procedure",
        description="Indicates the treatment or processing step applied to the specimen",
        # if property is element of this resource.
        element_property=True,
    )

    additive: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="additive",
        title="additive",
        description="Material used in the processing step",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Substance"],
    )


class SpecimenContainer(BackboneElement):
    resource_type = Field("SpecimenContainer", const=True)

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON).",
        description="Id for the container",
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Textual description of the container",
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="type",
        description="Kind of container directly associated with specimen",
        # if property is element of this resource.
        element_property=True,
    )

    capacity: fhirtypes.QuantityType = Field(
        None,
        alias="capacity",
        title=(
            "Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in "
            "JSON)."
        ),
        description="Container volume or size",
        element_property=True,
    )

    specimenQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="specimenQuantity",
        title=(
            "Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in "
            "JSON)."
        ),
        description="Quantity of specimen within container",
        element_property=True,
    )

    additiveCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="additiveCodeableConcept",
        title="additiveCodeableConcept",
        description="Additive associated with container",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e additive[x]
        one_of_many="additive",
        one_of_many_required=False,
    )

    additiveReference: fhirtypes.ReferenceType = Field(
        None,
        alias="additiveReference",
        title="additiveReference",
        description="Additive associated with container",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e additive[x]
        one_of_many="additive",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Reference"],
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
            "additive": ["additiveCodeableConcept", "additiveReference"],
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
