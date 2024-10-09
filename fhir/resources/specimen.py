from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Specimen
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Specimen(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Sample for analysis.
    A sample to be used for analysis.
    """

    __resource_type__ = "Specimen"

    accessionIdentifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="accessionIdentifier",
        title="Identifier assigned by the lab",
        description=(
            "The identifier assigned by the lab when accessioning specimen(s). This"
            " is not necessarily the same as the specimen identifier, depending on "
            "local lab procedures."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    collection: fhirtypes.SpecimenCollectionType | None = Field(  # type: ignore
        None,
        alias="collection",
        title="Collection details",
        description="Details concerning the specimen collection.",
        json_schema_extra={
            "element_property": True,
        },
    )

    combined: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="combined",
        title="grouped | pooled",
        description="This element signifies if the specimen is part of a group or pooled.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["grouped", "pooled"],
        },
    )
    combined__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_combined", title="Extension field for ``combined``."
    )

    condition: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="condition",
        title="State of the specimen",
        description="A mode or state of being that describes the nature of the specimen.",
        json_schema_extra={
            "element_property": True,
        },
    )

    container: typing.List[fhirtypes.SpecimenContainerType] | None = Field(  # type: ignore
        None,
        alias="container",
        title="Direct container of specimen (tube/slide, etc.)",
        description=(
            "The container holding the specimen.  The recursive nature of "
            "containers; i.e. blood in tube in tray in rack is not addressed here."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    feature: typing.List[fhirtypes.SpecimenFeatureType] | None = Field(  # type: ignore
        None,
        alias="feature",
        title="The physical feature of a specimen",
        description=(
            "A physical feature or landmark on a specimen, highlighted for context "
            "by the collector of the specimen (e.g. surgeon), that identifies the "
            "type of feature as well as its meaning (e.g. the red ink indicating "
            "the resection margin of the right lobe of the excised prostate tissue "
            "or wire loop at radiologically suspected tumor location)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="External Identifier",
        description="Id for specimen.",
        json_schema_extra={
            "element_property": True,
        },
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="note",
        title="Comments",
        description=(
            "To communicate any details or issues about the specimen or during the "
            "specimen collection. (for example: broken vial, sent with patient, "
            "frozen)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    parent: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="parent",
        title="Specimen from which this specimen originated",
        description=(
            "Reference to the parent (source) specimen which is used when the "
            "specimen was either derived from or a component of another specimen."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Specimen"],
        },
    )

    processing: typing.List[fhirtypes.SpecimenProcessingType] | None = Field(  # type: ignore
        None,
        alias="processing",
        title="Processing and processing step details",
        description="Details concerning processing and processing steps for the specimen.",
        json_schema_extra={
            "element_property": True,
        },
    )

    receivedTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="receivedTime",
        title="The time when specimen is received by the testing laboratory",
        description=(
            "Time when specimen is received by the testing laboratory for "
            "processing or testing."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    receivedTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_receivedTime", title="Extension field for ``receivedTime``."
    )

    request: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="request",
        title="Why the specimen was collected",
        description=(
            "Details concerning a service request that required a specimen to be "
            "collected."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ServiceRequest"],
        },
    )

    role: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="role",
        title="The role the specimen serves",
        description="The role or reason for the specimen in the testing workflow.",
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="available | unavailable | unsatisfactory | entered-in-error",
        description="The availability of the specimen.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "available",
                "unavailable",
                "unsatisfactory",
                "entered-in-error",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="subject",
        title=(
            "Where the specimen came from. This may be from patient(s), from a "
            "location (e.g., the source of an environmental sample), or a sampling "
            "of a substance, a biologically-derived product, or a device"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Patient",
                "Group",
                "Device",
                "BiologicallyDerivedProduct",
                "Substance",
                "Location",
            ],
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Kind of material that forms the specimen",
        description="The kind of material that forms the specimen.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Specimen`` according specification,
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
            "accessionIdentifier",
            "status",
            "type",
            "subject",
            "receivedTime",
            "parent",
            "request",
            "combined",
            "role",
            "feature",
            "collection",
            "processing",
            "container",
            "condition",
            "note",
        ]


class SpecimenCollection(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Collection details.
    Details concerning the specimen collection.
    """

    __resource_type__ = "SpecimenCollection"

    bodySite: fhirtypes.CodeableReferenceType | None = Field(  # type: ignore
        None,
        alias="bodySite",
        title="Anatomical collection site",
        description=(
            "Anatomical location from which the specimen was collected (if subject "
            "is a patient). This is the target site.  This element is not used for "
            "environmental specimens."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["BodyStructure"],
        },
    )

    collectedDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="collectedDateTime",
        title="Collection time",
        description=(
            "Time when specimen was collected from subject - the physiologically "
            "relevant time."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e collected[x]
            "one_of_many": "collected",
            "one_of_many_required": False,
        },
    )
    collectedDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_collectedDateTime",
        title="Extension field for ``collectedDateTime``.",
    )

    collectedPeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="collectedPeriod",
        title="Collection time",
        description=(
            "Time when specimen was collected from subject - the physiologically "
            "relevant time."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e collected[x]
            "one_of_many": "collected",
            "one_of_many_required": False,
        },
    )

    collector: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="collector",
        title="Who collected the specimen",
        description="Person who collected the specimen.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Patient",
                "RelatedPerson",
            ],
        },
    )

    device: fhirtypes.CodeableReferenceType | None = Field(  # type: ignore
        None,
        alias="device",
        title="Device used to perform collection",
        description=(
            "A coded value specifying the technique that is used to perform the "
            "procedure."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Device"],
        },
    )

    duration: fhirtypes.DurationType | None = Field(  # type: ignore
        None,
        alias="duration",
        title="How long it took to collect specimen",
        description="The span of time over which the collection of a specimen occurred.",
        json_schema_extra={
            "element_property": True,
        },
    )

    fastingStatusCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="fastingStatusCodeableConcept",
        title="Whether or how long patient abstained from food and/or drink",
        description=(
            "Abstinence or reduction from some or all food, drink, or both, for a "
            "period of time prior to sample collection."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e fastingStatus[x]
            "one_of_many": "fastingStatus",
            "one_of_many_required": False,
        },
    )

    fastingStatusDuration: fhirtypes.DurationType | None = Field(  # type: ignore
        None,
        alias="fastingStatusDuration",
        title="Whether or how long patient abstained from food and/or drink",
        description=(
            "Abstinence or reduction from some or all food, drink, or both, for a "
            "period of time prior to sample collection."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e fastingStatus[x]
            "one_of_many": "fastingStatus",
            "one_of_many_required": False,
        },
    )

    method: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="method",
        title="Technique used to perform collection",
        description=(
            "A coded value specifying the technique that is used to perform the "
            "procedure."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    procedure: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="procedure",
        title="The procedure that collects the specimen",
        description=(
            "The procedure event during which the specimen was collected (e.g. the "
            "surgery leading to the collection of a pathology sample)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Procedure"],
        },
    )

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="The quantity of specimen collected",
        description=(
            "The quantity of specimen collected; for instance the volume of a blood"
            " sample, or the physical measurement of an anatomic pathology sample."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SpecimenCollection`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "collector",
            "collectedDateTime",
            "collectedPeriod",
            "duration",
            "quantity",
            "method",
            "device",
            "procedure",
            "bodySite",
            "fastingStatusCodeableConcept",
            "fastingStatusDuration",
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
            "collected": ["collectedDateTime", "collectedPeriod"],
            "fastingStatus": ["fastingStatusCodeableConcept", "fastingStatusDuration"],
        }
        return one_of_many_fields


class SpecimenContainer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Direct container of specimen (tube/slide, etc.).
    The container holding the specimen.  The recursive nature of containers;
    i.e. blood in tube in tray in rack is not addressed here.
    """

    __resource_type__ = "SpecimenContainer"

    device: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="device",
        title="Device resource for the container",
        description=(
            "The device resource for the the container holding the specimen. If the"
            " container is in a holder then the referenced device will point to a "
            "parent device."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Device"],
        },
    )

    location: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="location",
        title="Where the container is",
        description="The location of the container holding the specimen.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    specimenQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="specimenQuantity",
        title="Quantity of specimen within container",
        description=(
            "The quantity of specimen in the container; may be volume, dimensions, "
            "or other appropriate measurements, depending on the specimen type."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SpecimenContainer`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "device",
            "location",
            "specimenQuantity",
        ]


class SpecimenFeature(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The physical feature of a specimen.
    A physical feature or landmark on a specimen, highlighted for context by
    the collector of the specimen (e.g. surgeon), that identifies the type of
    feature as well as its meaning (e.g. the red ink indicating the resection
    margin of the right lobe of the excised prostate tissue or wire loop at
    radiologically suspected tumor location).
    """

    __resource_type__ = "SpecimenFeature"

    description: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Information about the feature",
        description="Description of the feature of the specimen.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Highlighted feature",
        description="The landmark or feature being highlighted.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SpecimenFeature`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "description"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("description", "description__ext")]
        return required_fields


class SpecimenProcessing(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Processing and processing step details.
    Details concerning processing and processing steps for the specimen.
    """

    __resource_type__ = "SpecimenProcessing"

    additive: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="additive",
        title="Material used in the processing step",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Substance"],
        },
    )

    description: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Textual description of procedure",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    method: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="method",
        title="Indicates the treatment step  applied to the specimen",
        description="A coded value specifying the method used to process the specimen.",
        json_schema_extra={
            "element_property": True,
        },
    )

    timeDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="timeDateTime",
        title="Date and time of specimen processing",
        description=(
            "A record of the time or period when the specimen processing occurred."
            "  For example the time of sample fixation or the period of time the "
            "sample was in formalin."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e time[x]
            "one_of_many": "time",
            "one_of_many_required": False,
        },
    )
    timeDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_timeDateTime", title="Extension field for ``timeDateTime``."
    )

    timePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="timePeriod",
        title="Date and time of specimen processing",
        description=(
            "A record of the time or period when the specimen processing occurred."
            "  For example the time of sample fixation or the period of time the "
            "sample was in formalin."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e time[x]
            "one_of_many": "time",
            "one_of_many_required": False,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SpecimenProcessing`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "description",
            "method",
            "additive",
            "timeDateTime",
            "timePeriod",
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
        one_of_many_fields = {"time": ["timeDateTime", "timePeriod"]}
        return one_of_many_fields
