# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Specimen
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class Specimen(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
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
        # if property is element of this resource.
        element_property=True,
    )

    collection: fhirtypes.SpecimenCollectionType = Field(
        None,
        alias="collection",
        title="Collection details",
        description="Details concerning the specimen collection.",
        # if property is element of this resource.
        element_property=True,
    )

    combined: fhirtypes.Code = Field(
        None,
        alias="combined",
        title="grouped | pooled",
        description="This element signifies if the specimen is part of a group or pooled.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["grouped", "pooled"],
    )
    combined__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_combined", title="Extension field for ``combined``."
    )

    condition: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="condition",
        title="State of the specimen",
        description="A mode or state of being that describes the nature of the specimen.",
        # if property is element of this resource.
        element_property=True,
    )

    container: typing.List[fhirtypes.SpecimenContainerType] = Field(
        None,
        alias="container",
        title="Direct container of specimen (tube/slide, etc.)",
        description=(
            "The container holding the specimen.  The recursive nature of "
            "containers; i.e. blood in tube in tray in rack is not addressed here."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    feature: typing.List[fhirtypes.SpecimenFeatureType] = Field(
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
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="External Identifier",
        description="Id for specimen.",
        # if property is element of this resource.
        element_property=True,
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Comments",
        description=(
            "To communicate any details or issues about the specimen or during the "
            "specimen collection. (for example: broken vial, sent with patient, "
            "frozen)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    parent: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="parent",
        title="Specimen from which this specimen originated",
        description=(
            "Reference to the parent (source) specimen which is used when the "
            "specimen was either derived from or a component of another specimen."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Specimen"],
    )

    processing: typing.List[fhirtypes.SpecimenProcessingType] = Field(
        None,
        alias="processing",
        title="Processing and processing step details",
        description="Details concerning processing and processing steps for the specimen.",
        # if property is element of this resource.
        element_property=True,
    )

    receivedTime: fhirtypes.DateTime = Field(
        None,
        alias="receivedTime",
        title="The time when specimen is received by the testing laboratory",
        description=(
            "Time when specimen is received by the testing laboratory for "
            "processing or testing."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    receivedTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_receivedTime", title="Extension field for ``receivedTime``."
    )

    request: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="request",
        title="Why the specimen was collected",
        description=(
            "Details concerning a service request that required a specimen to be "
            "collected."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ServiceRequest"],
    )

    role: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="role",
        title="The role the specimen serves",
        description="The role or reason for the specimen in the testing workflow.",
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="available | unavailable | unsatisfactory | entered-in-error",
        description="The availability of the specimen.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["available", "unavailable", "unsatisfactory", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title=(
            "Where the specimen came from. This may be from patient(s), from a "
            "location (e.g., the source of an environmental sample), or a sampling "
            "of a substance, a biologically-derived product, or a device"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "Group",
            "Device",
            "BiologicallyDerivedProduct",
            "Substance",
            "Location",
        ],
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Kind of material that forms the specimen",
        description="The kind of material that forms the specimen.",
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("SpecimenCollection", const=True)

    bodySite: fhirtypes.CodeableReferenceType = Field(
        None,
        alias="bodySite",
        title="Anatomical collection site",
        description=(
            "Anatomical location from which the specimen was collected (if subject "
            "is a patient). This is the target site.  This element is not used for "
            "environmental specimens."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["BodyStructure"],
    )

    collectedDateTime: fhirtypes.DateTime = Field(
        None,
        alias="collectedDateTime",
        title="Collection time",
        description=(
            "Time when specimen was collected from subject - the physiologically "
            "relevant time."
        ),
        # if property is element of this resource.
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
        title="Collection time",
        description=(
            "Time when specimen was collected from subject - the physiologically "
            "relevant time."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e collected[x]
        one_of_many="collected",
        one_of_many_required=False,
    )

    collector: fhirtypes.ReferenceType = Field(
        None,
        alias="collector",
        title="Who collected the specimen",
        description="Person who collected the specimen.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "Patient",
            "RelatedPerson",
        ],
    )

    device: fhirtypes.CodeableReferenceType = Field(
        None,
        alias="device",
        title="Device used to perform collection",
        description=(
            "A coded value specifying the technique that is used to perform the "
            "procedure."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device"],
    )

    duration: fhirtypes.DurationType = Field(
        None,
        alias="duration",
        title="How long it took to collect specimen",
        description="The span of time over which the collection of a specimen occurred.",
        # if property is element of this resource.
        element_property=True,
    )

    fastingStatusCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="fastingStatusCodeableConcept",
        title="Whether or how long patient abstained from food and/or drink",
        description=(
            "Abstinence or reduction from some or all food, drink, or both, for a "
            "period of time prior to sample collection."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fastingStatus[x]
        one_of_many="fastingStatus",
        one_of_many_required=False,
    )

    fastingStatusDuration: fhirtypes.DurationType = Field(
        None,
        alias="fastingStatusDuration",
        title="Whether or how long patient abstained from food and/or drink",
        description=(
            "Abstinence or reduction from some or all food, drink, or both, for a "
            "period of time prior to sample collection."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e fastingStatus[x]
        one_of_many="fastingStatus",
        one_of_many_required=False,
    )

    method: fhirtypes.CodeableConceptType = Field(
        None,
        alias="method",
        title="Technique used to perform collection",
        description=(
            "A coded value specifying the technique that is used to perform the "
            "procedure."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    procedure: fhirtypes.ReferenceType = Field(
        None,
        alias="procedure",
        title="The procedure that collects the specimen",
        description=(
            "The procedure event during which the specimen was collected (e.g. the "
            "surgery leading to the collection of a pathology sample)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Procedure"],
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="The quantity of specimen collected",
        description=(
            "The quantity of specimen collected; for instance the volume of a blood"
            " sample, or the physical measurement of an anatomic pathology sample."
        ),
        # if property is element of this resource.
        element_property=True,
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2049(
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
        one_of_many_fields = {
            "collected": ["collectedDateTime", "collectedPeriod"],
            "fastingStatus": ["fastingStatusCodeableConcept", "fastingStatusDuration"],
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


class SpecimenContainer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Direct container of specimen (tube/slide, etc.).
    The container holding the specimen.  The recursive nature of containers;
    i.e. blood in tube in tray in rack is not addressed here.
    """

    resource_type = Field("SpecimenContainer", const=True)

    device: fhirtypes.ReferenceType = Field(
        ...,
        alias="device",
        title="Device resource for the container",
        description=(
            "The device resource for the the container holding the specimen. If the"
            " container is in a holder then the referenced device will point to a "
            "parent device."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device"],
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title="Where the container is",
        description="The location of the container holding the specimen.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    specimenQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="specimenQuantity",
        title="Quantity of specimen within container",
        description=(
            "The quantity of specimen in the container; may be volume, dimensions, "
            "or other appropriate measurements, depending on the specimen type."
        ),
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("SpecimenFeature", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Information about the feature",
        description="Description of the feature of the specimen.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Highlighted feature",
        description="The landmark or feature being highlighted.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SpecimenFeature`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "description"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1720(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("description", "description__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class SpecimenProcessing(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Processing and processing step details.
    Details concerning processing and processing steps for the specimen.
    """

    resource_type = Field("SpecimenProcessing", const=True)

    additive: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="additive",
        title="Material used in the processing step",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Substance"],
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Textual description of procedure",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    method: fhirtypes.CodeableConceptType = Field(
        None,
        alias="method",
        title="Indicates the treatment step  applied to the specimen",
        description="A coded value specifying the method used to process the specimen.",
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e time[x]
        one_of_many="time",
        one_of_many_required=False,
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2059(
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
