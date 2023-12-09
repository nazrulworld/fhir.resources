# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ImagingStudy
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


class ImagingStudy(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A set of images produced in single study (one or more series of references
    images).
    Representation of the content produced in a DICOM imaging study. A study
    comprises a set of series, each of which includes a set of Service-Object
    Pair Instances (SOP Instances - images or other data) acquired or produced
    in a common context.  A series is of only one modality (e.g. X-ray, CT, MR,
    ultrasound), but a study may have multiple series of different modalities.
    """

    resource_type = Field("ImagingStudy", const=True)

    accession: fhirtypes.IdentifierType = Field(
        None,
        alias="accession",
        title='Related workflow identifier ("Accession Number")',
        description=(
            "Accession Number is an identifier related to some aspect of imaging "
            "workflow and data management. Usage may vary across different "
            "institutions.  See for instance [IHE Radiology Technical Framework "
            "Volume 1 Appendix A](http://www.ihe.net/uploadedFiles/Documents/Radiol"
            "ogy/IHE_RAD_TF_Rev13.0_Vol1_FT_2014-07-30.pdf)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    availability: fhirtypes.Code = Field(
        None,
        alias="availability",
        title="ONLINE | OFFLINE | NEARLINE | UNAVAILABLE",
        description="Availability of study (online, offline, or nearline).",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["ONLINE", "OFFLINE", "NEARLINE", "UNAVAILABLE"],
    )
    availability__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_availability", title="Extension field for ``availability``."
    )

    basedOn: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="Request fulfilled",
        description=(
            "A list of the diagnostic requests that resulted in this imaging study "
            "being performed."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ReferralRequest", "CarePlan", "ProcedureRequest"],
    )

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title="Originating context",
        description="The encounter or episode at which the request is initiated.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter", "EpisodeOfCare"],
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Institution-generated description",
        description=(
            "Institution-generated description or classification of the Study "
            "performed."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    endpoint: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="endpoint",
        title="Study access endpoint",
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

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Other identifiers for the study",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    interpreter: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="interpreter",
        title="Who interpreted images",
        description="Who read the study and interpreted the images or other content.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    modalityList: typing.List[fhirtypes.CodingType] = Field(
        None,
        alias="modalityList",
        title="All series modality if actual acquisition modalities",
        description=(
            "A list of all the Series.ImageModality values that are actual "
            "acquisition modalities, i.e. those in the DICOM Context Group 29 "
            "(value set OID 1.2.840.10008.6.1.19)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    numberOfInstances: fhirtypes.UnsignedInt = Field(
        None,
        alias="numberOfInstances",
        title="Number of Study Related Instances",
        description=(
            "Number of SOP Instances in Study. This value given may be larger than "
            "the number of instance elements this resource contains due to resource"
            " availability, security, or other factors. This element should be "
            "present if any instance elements are present."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    numberOfInstances__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_numberOfInstances",
        title="Extension field for ``numberOfInstances``.",
    )

    numberOfSeries: fhirtypes.UnsignedInt = Field(
        None,
        alias="numberOfSeries",
        title="Number of Study Related Series",
        description=(
            "Number of Series in the Study. This value given may be larger than the"
            " number of series elements this Resource contains due to resource "
            "availability, security, or other factors. This element should be "
            "present if any series elements are present."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    numberOfSeries__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_numberOfSeries", title="Extension field for ``numberOfSeries``."
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Who the images are of",
        description="The patient imaged in the study.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    procedureCode: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="procedureCode",
        title="The performed procedure code",
        description="The code for the performed procedure type.",
        # if property is element of this resource.
        element_property=True,
    )

    procedureReference: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="procedureReference",
        title="The performed Procedure reference",
        description="A reference to the performed Procedure.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Procedure"],
    )

    reason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reason",
        title="Why the study was requested",
        description=(
            "Description of clinical condition indicating why the ImagingStudy was "
            "requested."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    referrer: fhirtypes.ReferenceType = Field(
        None,
        alias="referrer",
        title="Referring physician",
        description="The requesting/referring physician.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    series: typing.List[fhirtypes.ImagingStudySeriesType] = Field(
        None,
        alias="series",
        title="Each study has one or more series of instances",
        description="Each study has one or more series of images or other content.",
        # if property is element of this resource.
        element_property=True,
    )

    started: fhirtypes.DateTime = Field(
        None,
        alias="started",
        title="When the study was started",
        description="Date and time the study started.",
        # if property is element of this resource.
        element_property=True,
    )
    started__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_started", title="Extension field for ``started``."
    )

    uid: fhirtypes.Oid = Field(
        None,
        alias="uid",
        title="Formal DICOM identifier for the study",
        description="Formal identifier for the study.",
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
        ``ImagingStudy`` according specification,
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
            "uid",
            "accession",
            "identifier",
            "availability",
            "modalityList",
            "patient",
            "context",
            "started",
            "basedOn",
            "referrer",
            "interpreter",
            "endpoint",
            "numberOfSeries",
            "numberOfInstances",
            "procedureReference",
            "procedureCode",
            "reason",
            "description",
            "series",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1431(
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


class ImagingStudySeries(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Each study has one or more series of instances.
    Each study has one or more series of images or other content.
    """

    resource_type = Field("ImagingStudySeries", const=True)

    availability: fhirtypes.Code = Field(
        None,
        alias="availability",
        title="ONLINE | OFFLINE | NEARLINE | UNAVAILABLE",
        description="Availability of series (online, offline or nearline).",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["ONLINE", "OFFLINE", "NEARLINE", "UNAVAILABLE"],
    )
    availability__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_availability", title="Extension field for ``availability``."
    )

    bodySite: fhirtypes.CodingType = Field(
        None,
        alias="bodySite",
        title="Body part examined",
        description=(
            "The anatomic structures examined. See DICOM Part 16 Annex L (http://di"
            "com.nema.org/medical/dicom/current/output/chtml/part16/chapter_L.html)"
            " for DICOM to SNOMED-CT mappings. The bodySite may indicate the "
            "laterality of body part imaged; if so, it shall be consistent with any"
            " content of ImagingStudy.series.laterality."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="A short human readable summary of the series",
        description="A description of the series.",
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

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

    instance: typing.List[fhirtypes.ImagingStudySeriesInstanceType] = Field(
        None,
        alias="instance",
        title="A single SOP instance from the series",
        description=(
            "A single SOP instance within the series, e.g. an image, or "
            "presentation state."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    laterality: fhirtypes.CodingType = Field(
        None,
        alias="laterality",
        title="Body part laterality",
        description=(
            "The laterality of the (possibly paired) anatomic structures examined. "
            "E.g., the left knee, both lungs, or unpaired abdomen. If present, "
            "shall be consistent with any laterality information indicated in "
            "ImagingStudy.series.bodySite."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    modality: fhirtypes.CodingType = Field(
        ...,
        alias="modality",
        title="The modality of the instances in the series",
        description="The modality of this series sequence.",
        # if property is element of this resource.
        element_property=True,
    )

    number: fhirtypes.UnsignedInt = Field(
        None,
        alias="number",
        title="Numeric identifier of this series",
        description="The numeric identifier of this series in the study.",
        # if property is element of this resource.
        element_property=True,
    )
    number__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_number", title="Extension field for ``number``."
    )

    numberOfInstances: fhirtypes.UnsignedInt = Field(
        None,
        alias="numberOfInstances",
        title="Number of Series Related Instances",
        description=(
            "Number of SOP Instances in the Study. The value given may be larger "
            "than the number of instance elements this resource contains due to "
            "resource availability, security, or other factors. This element should"
            " be present if any instance elements are present."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    numberOfInstances__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_numberOfInstances",
        title="Extension field for ``numberOfInstances``.",
    )

    performer: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="performer",
        title="Who performed the series",
        description=(
            "The physician or operator (often the radiology technician)  who "
            "performed the series. The performer is recorded at the series level, "
            "since each series in a study may be performed by a different "
            "practitioner, at different times, and using different devices. A "
            "series may be performed by multiple practitioners."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    started: fhirtypes.DateTime = Field(
        None,
        alias="started",
        title="When the series started",
        description="The date and time the series was started.",
        # if property is element of this resource.
        element_property=True,
    )
    started__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_started", title="Extension field for ``started``."
    )

    uid: fhirtypes.Oid = Field(
        None,
        alias="uid",
        title="Formal DICOM identifier for this series",
        description="Formal identifier for this series.",
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
        ``ImagingStudySeries`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "uid",
            "number",
            "modality",
            "description",
            "numberOfInstances",
            "availability",
            "endpoint",
            "bodySite",
            "laterality",
            "started",
            "performer",
            "instance",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2044(
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


class ImagingStudySeriesInstance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A single SOP instance from the series.
    A single SOP instance within the series, e.g. an image, or presentation
    state.
    """

    resource_type = Field("ImagingStudySeriesInstance", const=True)

    number: fhirtypes.UnsignedInt = Field(
        None,
        alias="number",
        title="The number of this instance in the series",
        description="The number of instance in the series.",
        # if property is element of this resource.
        element_property=True,
    )
    number__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_number", title="Extension field for ``number``."
    )

    sopClass: fhirtypes.Oid = Field(
        None,
        alias="sopClass",
        title="DICOM class type",
        description="DICOM instance  type.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    sopClass__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sopClass", title="Extension field for ``sopClass``."
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Description of instance",
        description="The description of the instance.",
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    uid: fhirtypes.Oid = Field(
        None,
        alias="uid",
        title="Formal DICOM identifier for this instance",
        description="Formal identifier for this image or other content.",
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
        ``ImagingStudySeriesInstance`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "uid",
            "number",
            "sopClass",
            "title",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2851(
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
