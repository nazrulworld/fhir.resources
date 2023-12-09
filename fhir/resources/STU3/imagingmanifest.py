# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ImagingManifest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class ImagingManifest(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Key Object Selection.
    A text description of the DICOM SOP instances selected in the
    ImagingManifest; or the reason for, or significance of, the selection.
    """

    resource_type = Field("ImagingManifest", const=True)

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title="Author (human or machine)",
        description=(
            "Author of ImagingManifest. It can be a human author or a device which "
            "made the decision of the SOP instances selected. For example, a "
            "radiologist selected a set of imaging SOP instances to attach in a "
            "diagnostic report, and a CAD application may author a selection to "
            "describe SOP instances it used to generate a detection conclusion."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "Device",
            "Organization",
            "Patient",
            "RelatedPerson",
        ],
    )

    authoringTime: fhirtypes.DateTime = Field(
        None,
        alias="authoringTime",
        title="Time when the selection of instances was made",
        description=(
            "Date and time when the selection of the referenced instances were "
            "made. It is (typically) different from the creation date of the "
            "selection resource, and from dates associated with the referenced "
            "instances (e.g. capture time of the referenced image)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    authoringTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_authoringTime", title="Extension field for ``authoringTime``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Description text",
        description=(
            "Free text narrative description of the ImagingManifest.   The value "
            "may be derived from the DICOM Standard Part 16, CID-7010 descriptions "
            "(e.g. Best in Set, Complete Study Content). Note that those values "
            "cover the wide range of uses of the DICOM Key Object Selection object,"
            " several of which are not supported by ImagingManifest. Specifically, "
            "there is no expected behavior associated with descriptions that "
            "suggest referenced images be removed or not used."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="SOP Instance UID",
        description=(
            "Unique identifier of the DICOM Key Object Selection (KOS) that this "
            "resource represents."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Patient of the selected objects",
        description=(
            "A patient resource reference which is the patient subject of all DICOM"
            " SOP Instances in this ImagingManifest."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    study: typing.List[fhirtypes.ImagingManifestStudyType] = Field(
        ...,
        alias="study",
        title="Study identity of the selected instances",
        description=(
            "Study identity and locating information of the DICOM SOP instances in "
            "the selection."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImagingManifest`` according specification,
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
            "patient",
            "authoringTime",
            "author",
            "description",
            "study",
        ]


class ImagingManifestStudy(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Study identity of the selected instances.
    Study identity and locating information of the DICOM SOP instances in the
    selection.
    """

    resource_type = Field("ImagingManifestStudy", const=True)

    endpoint: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="endpoint",
        title="Study access service endpoint",
        description=(
            "The network service providing access (e.g., query, view, or retrieval)"
            " for the study. See implementation notes for information about using "
            "DICOM endpoints. A study-level endpoint applies to each series in the "
            "study, unless overridden by a series-level endpoint with the same "
            "Endpoint.type."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Endpoint"],
    )

    imagingStudy: fhirtypes.ReferenceType = Field(
        None,
        alias="imagingStudy",
        title="Reference to ImagingStudy",
        description="Reference to the Imaging Study in FHIR form.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ImagingStudy"],
    )

    series: typing.List[fhirtypes.ImagingManifestStudySeriesType] = Field(
        ...,
        alias="series",
        title="Series identity of the selected instances",
        description=(
            "Series identity and locating information of the DICOM SOP instances in"
            " the selection."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    uid: fhirtypes.Oid = Field(
        None,
        alias="uid",
        title="Study instance UID",
        description="Study instance UID of the SOP instances in the selection.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    uid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_uid", title="Extension field for ``uid``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImagingManifestStudy`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "uid",
            "imagingStudy",
            "endpoint",
            "series",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2254(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("uid", "uid__ext")]
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


class ImagingManifestStudySeries(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Series identity of the selected instances.
    Series identity and locating information of the DICOM SOP instances in the
    selection.
    """

    resource_type = Field("ImagingManifestStudySeries", const=True)

    endpoint: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="endpoint",
        title="Series access endpoint",
        description=(
            "The network service providing access (e.g., query, view, or retrieval)"
            " for this series. See implementation notes for information about using"
            " DICOM endpoints. A series-level endpoint, if present, has precedence "
            "over a study-level endpoint with the same Endpoint.type."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Endpoint"],
    )

    instance: typing.List[fhirtypes.ImagingManifestStudySeriesInstanceType] = Field(
        ...,
        alias="instance",
        title="The selected instance",
        description="Identity and locating information of the selected DICOM SOP instances.",
        # if property is element of this resource.
        element_property=True,
    )

    uid: fhirtypes.Oid = Field(
        None,
        alias="uid",
        title="Series instance UID",
        description="Series instance UID of the SOP instances in the selection.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    uid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_uid", title="Extension field for ``uid``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImagingManifestStudySeries`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "uid", "endpoint", "instance"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2867(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("uid", "uid__ext")]
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


class ImagingManifestStudySeriesInstance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The selected instance.
    Identity and locating information of the selected DICOM SOP instances.
    """

    resource_type = Field("ImagingManifestStudySeriesInstance", const=True)

    sopClass: fhirtypes.Oid = Field(
        None,
        alias="sopClass",
        title="SOP class UID of instance",
        description="SOP class UID of the selected instance.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    sopClass__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sopClass", title="Extension field for ``sopClass``."
    )

    uid: fhirtypes.Oid = Field(
        None,
        alias="uid",
        title="Selected instance UID",
        description="SOP Instance UID of the selected instance.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    uid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_uid", title="Extension field for ``uid``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImagingManifestStudySeriesInstance`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "sopClass", "uid"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3674(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sopClass", "sopClass__ext"), ("uid", "uid__ext")]
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
