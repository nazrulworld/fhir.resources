# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SpecimenDefinition
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class SpecimenDefinition(domainresource.DomainResource):
    """ Kind of specimen.
    A kind of specimen with associated set of requirements.
    """

    resource_type = Field("SpecimenDefinition", const=True)

    collection: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="collection",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Specimen collection procedure",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Business identifier of a kind of specimen",
    )

    patientPreparation: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="patientPreparation",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Patient preparation for collection",
    )

    timeAspect: fhirtypes.String = Field(
        None,
        alias="timeAspect",
        title="Type `String` (represented as `dict` in JSON)",
        description="Time aspect for collection",
    )

    typeCollected: fhirtypes.CodeableConceptType = Field(
        None,
        alias="typeCollected",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Kind of material to collect",
    )

    typeTested: ListType[fhirtypes.SpecimenDefinitionTypeTestedType] = Field(
        None,
        alias="typeTested",
        title="List of `SpecimenDefinitionTypeTested` items (represented as `dict` in JSON)",
        description="Specimen in container intended for testing by lab",
    )


class SpecimenDefinitionTypeTested(backboneelement.BackboneElement):
    """ Specimen in container intended for testing by lab.
    Specimen conditioned in a container as expected by the testing laboratory.
    """

    resource_type = Field("SpecimenDefinitionTypeTested", const=True)

    container: fhirtypes.SpecimenDefinitionTypeTestedContainerType = Field(
        None,
        alias="container",
        title="Type `SpecimenDefinitionTypeTestedContainer` (represented as `dict` in JSON)",
        description="The specimen\u0027s container",
    )

    handling: ListType[fhirtypes.SpecimenDefinitionTypeTestedHandlingType] = Field(
        None,
        alias="handling",
        title="List of `SpecimenDefinitionTypeTestedHandling` items (represented as `dict` in JSON)",
        description="Specimen handling before testing",
    )

    isDerived: bool = Field(
        None,
        alias="isDerived",
        title="Type `bool`",
        description="Primary or secondary specimen",
    )

    preference: fhirtypes.Code = Field(
        ...,
        alias="preference",
        title="Type `Code` (represented as `dict` in JSON)",
        description="preferred | alternate",
    )

    rejectionCriterion: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="rejectionCriterion",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Rejection criterion",
    )

    requirement: fhirtypes.String = Field(
        None,
        alias="requirement",
        title="Type `String` (represented as `dict` in JSON)",
        description="Specimen requirements",
    )

    retentionTime: fhirtypes.DurationType = Field(
        None,
        alias="retentionTime",
        title="Type `Duration` (represented as `dict` in JSON)",
        description="Specimen retention time",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of intended specimen",
    )


class SpecimenDefinitionTypeTestedContainer(backboneelement.BackboneElement):
    """ The specimen's container.
    """

    resource_type = Field("SpecimenDefinitionTypeTestedContainer", const=True)

    additive: ListType[
        fhirtypes.SpecimenDefinitionTypeTestedContainerAdditiveType
    ] = Field(
        None,
        alias="additive",
        title="List of `SpecimenDefinitionTypeTestedContainerAdditive` items (represented as `dict` in JSON)",
        description="Additive associated with container",
    )

    cap: fhirtypes.CodeableConceptType = Field(
        None,
        alias="cap",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Color of container cap",
    )

    capacity: fhirtypes.QuantityType = Field(
        None,
        alias="capacity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Container capacity",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Container description",
    )

    material: fhirtypes.CodeableConceptType = Field(
        None,
        alias="material",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Container material",
    )

    minimumVolumeQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="minimumVolumeQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Minimum volume",
        one_of_many="minimumVolume",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    minimumVolumeString: fhirtypes.String = Field(
        None,
        alias="minimumVolumeString",
        title="Type `String` (represented as `dict` in JSON)",
        description="Minimum volume",
        one_of_many="minimumVolume",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    preparation: fhirtypes.String = Field(
        None,
        alias="preparation",
        title="Type `String` (represented as `dict` in JSON)",
        description="Specimen container preparation",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Kind of container associated with the kind of specimen",
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
            "minimumVolume": ["minimumVolumeQuantity", "minimumVolumeString",],
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


class SpecimenDefinitionTypeTestedContainerAdditive(backboneelement.BackboneElement):
    """ Additive associated with container.
    Substance introduced in the kind of container to preserve, maintain or
    enhance the specimen. Examples: Formalin, Citrate, EDTA.
    """

    resource_type = Field("SpecimenDefinitionTypeTestedContainerAdditive", const=True)

    additiveCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="additiveCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Additive associated with container",
        one_of_many="additive",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    additiveReference: fhirtypes.ReferenceType = Field(
        None,
        alias="additiveReference",
        title="Type `Reference` referencing `Substance` (represented as `dict` in JSON)",
        description="Additive associated with container",
        one_of_many="additive",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
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
            "additive": ["additiveCodeableConcept", "additiveReference",],
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


class SpecimenDefinitionTypeTestedHandling(backboneelement.BackboneElement):
    """ Specimen handling before testing.
    Set of instructions for preservation/transport of the specimen at a defined
    temperature interval, prior the testing process.
    """

    resource_type = Field("SpecimenDefinitionTypeTestedHandling", const=True)

    instruction: fhirtypes.String = Field(
        None,
        alias="instruction",
        title="Type `String` (represented as `dict` in JSON)",
        description="Preservation instruction",
    )

    maxDuration: fhirtypes.DurationType = Field(
        None,
        alias="maxDuration",
        title="Type `Duration` (represented as `dict` in JSON)",
        description="Maximum preservation time",
    )

    temperatureQualifier: fhirtypes.CodeableConceptType = Field(
        None,
        alias="temperatureQualifier",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Temperature qualifier",
    )

    temperatureRange: fhirtypes.RangeType = Field(
        None,
        alias="temperatureRange",
        title="Type `Range` (represented as `dict` in JSON)",
        description="Temperature range",
    )
