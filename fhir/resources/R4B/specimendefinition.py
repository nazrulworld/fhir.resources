from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/SpecimenDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class SpecimenDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Kind of specimen.
    A kind of specimen with associated set of requirements.
    """

    __resource_type__ = "SpecimenDefinition"

    collection: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="collection",
        title="Specimen collection procedure",
        description="The action to be performed for collecting the specimen.",
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business identifier of a kind of specimen",
        description="A business identifier associated with the kind of specimen.",
        json_schema_extra={
            "element_property": True,
        },
    )

    patientPreparation: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="patientPreparation",
        title="Patient preparation for collection",
        description="Preparation of the patient for specimen collection.",
        json_schema_extra={
            "element_property": True,
        },
    )

    timeAspect: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="timeAspect",
        title="Time aspect for collection",
        description="Time aspect of specimen collection (duration or offset).",
        json_schema_extra={
            "element_property": True,
        },
    )
    timeAspect__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_timeAspect", title="Extension field for ``timeAspect``."
    )

    typeCollected: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="typeCollected",
        title="Kind of material to collect",
        description="The kind of material to be collected.",
        json_schema_extra={
            "element_property": True,
        },
    )

    typeTested: typing.List[fhirtypes.SpecimenDefinitionTypeTestedType] | None = Field(  # type: ignore
        None,
        alias="typeTested",
        title="Specimen in container intended for testing by lab",
        description=(
            "Specimen conditioned in a container as expected by the testing "
            "laboratory."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SpecimenDefinition`` according specification,
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
            "typeCollected",
            "patientPreparation",
            "timeAspect",
            "collection",
            "typeTested",
        ]


class SpecimenDefinitionTypeTested(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Specimen in container intended for testing by lab.
    Specimen conditioned in a container as expected by the testing laboratory.
    """

    __resource_type__ = "SpecimenDefinitionTypeTested"

    container: fhirtypes.SpecimenDefinitionTypeTestedContainerType | None = Field(  # type: ignore
        None,
        alias="container",
        title="The specimen's container",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    handling: typing.List[fhirtypes.SpecimenDefinitionTypeTestedHandlingType] | None = Field(  # type: ignore
        None,
        alias="handling",
        title="Specimen handling before testing",
        description=(
            "Set of instructions for preservation/transport of the specimen at a "
            "defined temperature interval, prior the testing process."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    isDerived: bool | None = Field(  # type: ignore
        None,
        alias="isDerived",
        title="Primary or secondary specimen",
        description="Primary of secondary specimen.",
        json_schema_extra={
            "element_property": True,
        },
    )
    isDerived__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_isDerived", title="Extension field for ``isDerived``."
    )

    preference: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="preference",
        title="preferred | alternate",
        description="The preference for this type of conditioned specimen.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["preferred", "alternate"],
        },
    )
    preference__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_preference", title="Extension field for ``preference``."
    )

    rejectionCriterion: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="rejectionCriterion",
        title="Rejection criterion",
        description=(
            "Criterion for rejection of the specimen in its container by the "
            "laboratory."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    requirement: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="requirement",
        title="Specimen requirements",
        description=(
            "Requirements for delivery and special handling of this kind of "
            "conditioned specimen."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    requirement__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_requirement", title="Extension field for ``requirement``."
    )

    retentionTime: fhirtypes.DurationType | None = Field(  # type: ignore
        None,
        alias="retentionTime",
        title="Specimen retention time",
        description=(
            "The usual time that a specimen of this kind is retained after the "
            "ordered tests are completed, for the purpose of additional testing."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Type of intended specimen",
        description="The kind of specimen conditioned for testing expected by lab.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SpecimenDefinitionTypeTested`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "isDerived",
            "type",
            "preference",
            "container",
            "requirement",
            "retentionTime",
            "rejectionCriterion",
            "handling",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("preference", "preference__ext")]
        return required_fields


class SpecimenDefinitionTypeTestedContainer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The specimen's container.
    """

    __resource_type__ = "SpecimenDefinitionTypeTestedContainer"

    additive: typing.List[fhirtypes.SpecimenDefinitionTypeTestedContainerAdditiveType] | None = Field(  # type: ignore
        None,
        alias="additive",
        title="Additive associated with container",
        description=(
            "Substance introduced in the kind of container to preserve, maintain or"
            " enhance the specimen. Examples: Formalin, Citrate, EDTA."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    cap: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="cap",
        title="Color of container cap",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    capacity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="capacity",
        title="Container capacity",
        description="The capacity (volume or other measure) of this kind of container.",
        json_schema_extra={
            "element_property": True,
        },
    )

    description: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Container description",
        description="The textual description of the kind of container.",
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    material: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="material",
        title="Container material",
        description="The type of material of the container.",
        json_schema_extra={
            "element_property": True,
        },
    )

    minimumVolumeQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="minimumVolumeQuantity",
        title="Minimum volume",
        description="The minimum volume to be conditioned in the container.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e minimumVolume[x]
            "one_of_many": "minimumVolume",
            "one_of_many_required": False,
        },
    )

    minimumVolumeString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="minimumVolumeString",
        title="Minimum volume",
        description="The minimum volume to be conditioned in the container.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e minimumVolume[x]
            "one_of_many": "minimumVolume",
            "one_of_many_required": False,
        },
    )
    minimumVolumeString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_minimumVolumeString",
        title="Extension field for ``minimumVolumeString``.",
    )

    preparation: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="preparation",
        title="Specimen container preparation",
        description=(
            "Special processing that should be applied to the container for this "
            "kind of specimen."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    preparation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_preparation", title="Extension field for ``preparation``."
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Kind of container associated with the kind of specimen",
        description="The type of container used to contain this kind of specimen.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SpecimenDefinitionTypeTestedContainer`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "material",
            "type",
            "cap",
            "description",
            "capacity",
            "minimumVolumeQuantity",
            "minimumVolumeString",
            "additive",
            "preparation",
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
        one_of_many_fields = {
            "minimumVolume": ["minimumVolumeQuantity", "minimumVolumeString"]
        }
        return one_of_many_fields


class SpecimenDefinitionTypeTestedContainerAdditive(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additive associated with container.
    Substance introduced in the kind of container to preserve, maintain or
    enhance the specimen. Examples: Formalin, Citrate, EDTA.
    """

    __resource_type__ = "SpecimenDefinitionTypeTestedContainerAdditive"

    additiveCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="additiveCodeableConcept",
        title="Additive associated with container",
        description=(
            "Substance introduced in the kind of container to preserve, maintain or"
            " enhance the specimen. Examples: Formalin, Citrate, EDTA."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e additive[x]
            "one_of_many": "additive",
            "one_of_many_required": True,
        },
    )

    additiveReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="additiveReference",
        title="Additive associated with container",
        description=(
            "Substance introduced in the kind of container to preserve, maintain or"
            " enhance the specimen. Examples: Formalin, Citrate, EDTA."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e additive[x]
            "one_of_many": "additive",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Substance"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SpecimenDefinitionTypeTestedContainerAdditive`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "additiveCodeableConcept",
            "additiveReference",
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
        one_of_many_fields = {
            "additive": ["additiveCodeableConcept", "additiveReference"]
        }
        return one_of_many_fields


class SpecimenDefinitionTypeTestedHandling(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Specimen handling before testing.
    Set of instructions for preservation/transport of the specimen at a defined
    temperature interval, prior the testing process.
    """

    __resource_type__ = "SpecimenDefinitionTypeTestedHandling"

    instruction: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="instruction",
        title="Preservation instruction",
        description=(
            "Additional textual instructions for the preservation or transport of "
            "the specimen. For instance, 'Protect from light exposure'."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    instruction__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_instruction", title="Extension field for ``instruction``."
    )

    maxDuration: fhirtypes.DurationType | None = Field(  # type: ignore
        None,
        alias="maxDuration",
        title="Maximum preservation time",
        description=(
            "The maximum time interval of preservation of the specimen with these "
            "conditions."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    temperatureQualifier: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="temperatureQualifier",
        title="Temperature qualifier",
        description=(
            "It qualifies the interval of temperature, which characterizes an "
            "occurrence of handling. Conditions that are not related to temperature"
            " may be handled in the instruction element."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    temperatureRange: fhirtypes.RangeType | None = Field(  # type: ignore
        None,
        alias="temperatureRange",
        title="Temperature range",
        description="The temperature interval for this set of handling instructions.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SpecimenDefinitionTypeTestedHandling`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "temperatureQualifier",
            "temperatureRange",
            "maxDuration",
            "instruction",
        ]
