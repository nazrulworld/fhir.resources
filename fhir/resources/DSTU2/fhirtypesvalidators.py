# _*_ coding: utf-8 _*_
"""Validators for ``pydantic`` Custom DataType"""
import importlib
import typing
from pathlib import Path
from typing import Union

from pydantic.v1.class_validators import make_generic_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.types import StrBytes
from pydantic.v1.utils import ROOT_KEY

from .fhirabstractmodel import FHIRAbstractModel

if typing.TYPE_CHECKING:
    from pydantic.v1 import BaseModel

__author__ = "Md Nazrul Islam<email2nazrul@gmail.com>"

MODEL_CLASSES = {
    "FHIRPrimitiveExtension": (None, ".fhirprimitiveextension"),
    "Element": (None, ".element"),
    "Resource": (None, ".resource"),
    "DomainResource": (None, ".domainresource"),
    "BackboneElement": (None, ".backboneelement"),
    "Extension": (None, ".extension"),
    "Meta": (None, ".meta"),
    "Narrative": (None, ".narrative"),
    "Address": (None, ".address"),
    "Period": (None, ".period"),
    "Attachment": (None, ".attachment"),
    "CodeableConcept": (None, ".codeableconcept"),
    "Coding": (None, ".coding"),
    "ContactPoint": (None, ".contactpoint"),
    "HumanName": (None, ".humanname"),
    "Identifier": (None, ".identifier"),
    "Reference": (None, ".reference"),
    "Quantity": (None, ".quantity"),
    "Range": (None, ".range"),
    "Ratio": (None, ".ratio"),
    "Signature": (None, ".signature"),
    "Timing": (None, ".timing"),
    "TimingRepeat": (None, ".timing"),
    "Duration": (None, ".duration"),
    "Age": (None, ".age"),
    "Count": (None, ".count"),
    "Money": (None, ".money"),
    "Distance": (None, ".distance"),
    "SampledData": (None, ".sampleddata"),
    "Annotation": (None, ".annotation"),
    "Media": (None, ".media"),
    "Basic": (None, ".basic"),
    "Binary": (None, ".binary"),
    "BodySite": (None, ".bodysite"),
    "Flag": (None, ".flag"),
    "Location": (None, ".location"),
    "LocationPosition": (None, ".location"),
    "Slot": (None, ".slot"),
    "Schedule": (None, ".schedule"),
    "Account": (None, ".account"),
    "AllergyIntolerance": (None, ".allergyintolerance"),
    "AllergyIntoleranceReaction": (None, ".allergyintolerance"),
    "Appointment": (None, ".appointment"),
    "AppointmentParticipant": (None, ".appointment"),
    "AppointmentResponse": (None, ".appointmentresponse"),
    "AuditEvent": (None, ".auditevent"),
    "AuditEventEvent": (None, ".auditevent"),
    "AuditEventObject": (None, ".auditevent"),
    "AuditEventObjectDetail": (None, ".auditevent"),
    "AuditEventParticipant": (None, ".auditevent"),
    "AuditEventParticipantNetwork": (None, ".auditevent"),
    "AuditEventSource": (None, ".auditevent"),
    "Bundle": (None, ".bundle"),
    "BundleEntry": (None, ".bundle"),
    "BundleEntryRequest": (None, ".bundle"),
    "BundleEntryResponse": (None, ".bundle"),
    "BundleEntrySearch": (None, ".bundle"),
    "BundleLink": (None, ".bundle"),
    "CarePlan": (None, ".careplan"),
    "CarePlanActivity": (None, ".careplan"),
    "CarePlanActivityDetail": (None, ".careplan"),
    "CarePlanParticipant": (None, ".careplan"),
    "CarePlanRelatedPlan": (None, ".careplan"),
    "Claim": (None, ".claim"),
    "ClaimCoverage": (None, ".claim"),
    "ClaimDiagnosis": (None, ".claim"),
    "ClaimItem": (None, ".claim"),
    "ClaimItemDetail": (None, ".claim"),
    "ClaimItemDetailSubDetail": (None, ".claim"),
    "ClaimItemProsthesis": (None, ".claim"),
    "ClaimMissingTeeth": (None, ".claim"),
    "ClaimPayee": (None, ".claim"),
    "ClaimResponse": (None, ".claimresponse"),
    "ClaimResponseAddItem": (None, ".claimresponse"),
    "ClaimResponseAddItemAdjudication": (None, ".claimresponse"),
    "ClaimResponseAddItemDetail": (None, ".claimresponse"),
    "ClaimResponseAddItemDetailAdjudication": (None, ".claimresponse"),
    "ClaimResponseCoverage": (None, ".claimresponse"),
    "ClaimResponseItem": (None, ".claimresponse"),
    "ClaimResponseItemAdjudication": (None, ".claimresponse"),
    "ClaimResponseItemDetail": (None, ".claimresponse"),
    "ClaimResponseItemDetailAdjudication": (None, ".claimresponse"),
    "ClaimResponseItemDetailSubDetail": (None, ".claimresponse"),
    "ClaimResponseItemDetailSubDetailAdjudication": (None, ".claimresponse"),
    "ClaimResponseNote": (None, ".claimresponse"),
    "ClinicalImpression": (None, ".clinicalimpression"),
    "ClinicalImpressionFinding": (None, ".clinicalimpression"),
    "ClinicalImpressionInvestigations": (None, ".clinicalimpression"),
    "ClinicalImpressionRuledOut": (None, ".clinicalimpression"),
    "Communication": (None, ".communication"),
    "CommunicationPayload": (None, ".communication"),
    "CommunicationRequest": (None, ".communicationrequest"),
    "CommunicationRequestPayload": (None, ".communicationrequest"),
    "Composition": (None, ".composition"),
    "CompositionAttester": (None, ".composition"),
    "CompositionEvent": (None, ".composition"),
    "CompositionSection": (None, ".composition"),
    "ConceptMap": (None, ".conceptmap"),
    "ConceptMapContact": (None, ".conceptmap"),
    "ConceptMapElement": (None, ".conceptmap"),
    "ConceptMapElementTarget": (None, ".conceptmap"),
    "ConceptMapElementTargetDependsOn": (None, ".conceptmap"),
    "Condition": (None, ".condition"),
    "ConditionEvidence": (None, ".condition"),
    "ConditionStage": (None, ".condition"),
    "Conformance": (None, ".conformance"),
    "ConformanceContact": (None, ".conformance"),
    "ConformanceDocument": (None, ".conformance"),
    "ConformanceImplementation": (None, ".conformance"),
    "ConformanceMessaging": (None, ".conformance"),
    "ConformanceMessagingEndpoint": (None, ".conformance"),
    "ConformanceMessagingEvent": (None, ".conformance"),
    "ConformanceRest": (None, ".conformance"),
    "ConformanceRestInteraction": (None, ".conformance"),
    "ConformanceRestOperation": (None, ".conformance"),
    "ConformanceRestResource": (None, ".conformance"),
    "ConformanceRestResourceInteraction": (None, ".conformance"),
    "ConformanceRestResourceSearchParam": (None, ".conformance"),
    "ConformanceRestSecurity": (None, ".conformance"),
    "ConformanceRestSecurityCertificate": (None, ".conformance"),
    "ConformanceSoftware": (None, ".conformance"),
    "Patient": (None, ".patient"),
    "PatientAnimal": (None, ".patient"),
    "PatientCommunication": (None, ".patient"),
    "PatientContact": (None, ".patient"),
    "PatientLink": (None, ".patient"),
    "Organization": (None, ".organization"),
    "OrganizationContact": (None, ".organization"),
    "Person": (None, ".person"),
    "PersonLink": (None, ".person"),
    "Practitioner": (None, ".practitioner"),
    "PractitionerPractitionerRole": (None, ".practitioner"),
    "PractitionerQualification": (None, ".practitioner"),
    "ValueSet": (None, ".valueset"),
    "ValueSetCodeSystem": (None, ".valueset"),
    "ValueSetCodeSystemConcept": (None, ".valueset"),
    "ValueSetCodeSystemConceptDesignation": (None, ".valueset"),
    "ValueSetCompose": (None, ".valueset"),
    "ValueSetComposeInclude": (None, ".valueset"),
    "ValueSetComposeIncludeConcept": (None, ".valueset"),
    "ValueSetComposeIncludeFilter": (None, ".valueset"),
    "ValueSetContact": (None, ".valueset"),
    "ValueSetExpansion": (None, ".valueset"),
    "ValueSetExpansionContains": (None, ".valueset"),
    "ValueSetExpansionParameter": (None, ".valueset"),
    "Procedure": (None, ".procedure"),
    "ProcedureFocalDevice": (None, ".procedure"),
    "ProcedurePerformer": (None, ".procedure"),
    "ProcedureRequest": (None, ".procedurerequest"),
    "DiagnosticReport": (None, ".diagnosticreport"),
    "DiagnosticReportImage": (None, ".diagnosticreport"),
    "Goal": (None, ".goal"),
    "GoalOutcome": (None, ".goal"),
    "GroupCharacteristic": (None, ".group"),
    "GroupMember": (None, ".group"),
    "EligibilityRequest": (None, ".eligibilityrequest"),
    "EligibilityResponse": (None, ".eligibilityresponse"),
    "Encounter": (None, ".encounter"),
    "EncounterHospitalization": (None, ".encounter"),
    "EncounterLocation": (None, ".encounter"),
    "EncounterParticipant": (None, ".encounter"),
    "EncounterStatusHistory": (None, ".encounter"),
    "EnrollmentRequest": (None, ".enrollmentrequest"),
    "EnrollmentResponse": (None, ".enrollmentresponse"),
    "Immunization": (None, ".immunization"),
    "ImmunizationExplanation": (None, ".immunization"),
    "ImmunizationReaction": (None, ".immunization"),
    "ImmunizationVaccinationProtocol": (None, ".immunization"),
    "MedicationAdministration": (None, ".medicationadministration"),
    "MedicationAdministrationDosage": (None, ".medicationadministration"),
    "MedicationStatement": (None, ".medicationstatement"),
    "MedicationStatementDosage": (None, ".medicationstatement"),
    "Observation": (None, ".observation"),
    "ObservationComponent": (None, ".observation"),
    "ObservationReferenceRange": (None, ".observation"),
    "ObservationRelated": (None, ".observation"),
    "OperationOutcome": (None, ".operationoutcome"),
    "OperationOutcomeIssue": (None, ".operationoutcome"),
    "Medication": (None, ".medication"),
    "MedicationPackage": (None, ".medication"),
    "MedicationPackageContent": (None, ".medication"),
    "MedicationProduct": (None, ".medication"),
    "MedicationProductBatch": (None, ".medication"),
    "MedicationProductIngredient": (None, ".medication"),
    "MedicationOrder": (None, ".medicationorder"),
    "MedicationOrderDispenseRequest": (None, ".medicationorder"),
    "MedicationOrderDosageInstruction": (None, ".medicationorder"),
    "MedicationOrderSubstitution": (None, ".medicationorder"),
    "Contract": (None, ".contract"),
    "ContractActor": (None, ".contract"),
    "ContractFriendly": (None, ".contract"),
    "ContractLegal": (None, ".contract"),
    "ContractRule": (None, ".contract"),
    "ContractSigner": (None, ".contract"),
    "ContractTerm": (None, ".contract"),
    "ContractTermActor": (None, ".contract"),
    "ContractTermValuedItem": (None, ".contract"),
    "ContractValuedItem": (None, ".contract"),
    "Device": (None, ".device"),
    "ElementDefinition": (None, ".elementdefinition"),
    "ElementDefinitionBase": (None, ".elementdefinition"),
    "ElementDefinitionBinding": (None, ".elementdefinition"),
    "ElementDefinitionConstraint": (None, ".elementdefinition"),
    "ElementDefinitionMapping": (None, ".elementdefinition"),
    "ElementDefinitionSlicing": (None, ".elementdefinition"),
    "ElementDefinitionType": (None, ".elementdefinition"),
    "DataElement": (None, ".dataelement"),
    "DataElementContact": (None, ".dataelement"),
    "DataElementMapping": (None, ".dataelement"),
    "DetectedIssue": (None, ".detectedissue"),
    "DetectedIssueMitigation": (None, ".detectedissue"),
    "DeviceComponent": (None, ".devicecomponent"),
    "DeviceComponentProductionSpecification": (None, ".devicecomponent"),
    "DeviceMetric": (None, ".devicemetric"),
    "DeviceMetricCalibration": (None, ".devicemetric"),
    "DeviceUseRequest": (None, ".deviceuserequest"),
    "DeviceUseStatement": (None, ".deviceusestatement"),
    "DiagnosticOrder": (None, ".diagnosticorder"),
    "DiagnosticOrderEvent": (None, ".diagnosticorder"),
    "DiagnosticOrderItem": (None, ".diagnosticorder"),
    "DocumentManifest": (None, ".documentmanifest"),
    "DocumentManifestContent": (None, ".documentmanifest"),
    "DocumentManifestRelated": (None, ".documentmanifest"),
    "DocumentReference": (None, ".documentreference"),
    "DocumentReferenceContent": (None, ".documentreference"),
    "DocumentReferenceContext": (None, ".documentreference"),
    "DocumentReferenceContextRelated": (None, ".documentreference"),
    "DocumentReferenceRelatesTo": (None, ".documentreference"),
    "EpisodeOfCare": (None, ".episodeofcare"),
    "EpisodeOfCareCareTeam": (None, ".episodeofcare"),
    "EpisodeOfCareStatusHistory": (None, ".episodeofcare"),
    "FamilyMemberHistory": (None, ".familymemberhistory"),
    "FamilyMemberHistoryCondition": (None, ".familymemberhistory"),
    "ExplanationOfBenefit": (None, ".explanationofbenefit"),
    "HealthcareService": (None, ".healthcareservice"),
    "HealthcareServiceAvailableTime": (None, ".healthcareservice"),
    "HealthcareServiceNotAvailable": (None, ".healthcareservice"),
    "HealthcareServiceServiceType": (None, ".healthcareservice"),
    "ImagingObjectSelection": (None, ".imagingobjectselection"),
    "ImagingObjectSelectionStudy": (None, ".imagingobjectselection"),
    "ImagingObjectSelectionStudySeries": (None, ".imagingobjectselection"),
    "ImagingObjectSelectionStudySeriesInstance": (None, ".imagingobjectselection"),
    "ImagingObjectSelectionStudySeriesInstanceFrames": (
        None,
        ".imagingobjectselection",
    ),
    "NutritionOrder": (None, ".nutritionorder"),
    "NutritionOrderOralDiet": (None, ".nutritionorder"),
    "NutritionOrderSupplement": (None, ".nutritionorder"),
    "NutritionOrderEnteralFormula": (None, ".nutritionorder"),
    "NutritionOrderOralDietNutrient": (None, ".nutritionorder"),
    "NutritionOrderOralDietTexture": (None, ".nutritionorder"),
    "NutritionOrderEnteralFormulaAdministration": (None, ".nutritionorder"),
    "Order": (None, ".order"),
    "OrderWhen": (None, ".order"),
    "OrderResponse": (None, ".orderresponse"),
    "OperationDefinition": (None, ".operationdefinition"),
    "OperationDefinitionContact": (None, ".operationdefinition"),
    "OperationDefinitionParameter": (None, ".operationdefinition"),
    "OperationDefinitionParameterBinding": (None, ".operationdefinition"),
    "Parameter": (None, ".parameters"),
    "ParametersParameter": (None, ".parameters"),
    "ProcessResponse": (None, ".processresponse"),
    "ProcessResponseNotes": (None, ".processresponse"),
    "ProcessRequest": (None, ".processrequest"),
    "ProcessRequestItem": (None, ".processrequest"),
    "PaymentReconciliation": (None, ".paymentreconciliation"),
    "PaymentReconciliationDetail": (None, ".paymentreconciliation"),
    "PaymentReconciliationNote": (None, ".paymentreconciliation"),
    "PaymentNotice": (None, ".paymentnotice"),
    "Provenance": (None, ".provenance"),
    "ProvenanceAgent": (None, ".provenance"),
    "ProvenanceEntity": (None, ".provenance"),
    "ProvenanceAgentRelatedAgent": (None, ".provenance"),
    "QuestionnaireResponse": (None, ".questionnaireresponse"),
    "QuestionnaireResponseGroup": (None, ".questionnaireresponse"),
    "QuestionnaireResponseGroupQuestion": (None, ".questionnaireresponse"),
    "QuestionnaireResponseGroupQuestionAnswer": (None, ".questionnaireresponse"),
    "Questionnaire": (None, ".questionnaire"),
    "QuestionnaireGroup": (None, ".questionnaire"),
    "QuestionnaireGroupQuestion": (None, ".questionnaire"),
    "ReferralRequest": (None, ".referralrequest"),
    "RiskAssessment": (None, ".riskassessment"),
    "RiskAssessmentPrediction": (None, ".riskassessment"),
    "SearchParameter": (None, ".searchparameter"),
    "SearchParameterContact": (None, ".searchparameter"),
    "Subscription": (None, ".subscription"),
    "SubscriptionChannel": (None, ".subscription"),
    "Substance": (None, ".substance"),
    "SubstanceInstance": (None, ".substance"),
    "SubstanceIngredient": (None, ".substance"),
    "SupplyDelivery": (None, ".supplydelivery"),
    "SupplyRequest": (None, ".supplyrequest"),
    "SupplyRequestWhen": (None, ".supplyrequest"),
    "VisionPrescription": (None, ".visionprescription"),
    "VisionPrescriptionDispense": (None, ".visionprescription"),
    "Specimen": (None, ".specimen"),
    "SpecimenCollection": (None, ".specimen"),
    "SpecimenTreatment": (None, ".specimen"),
    "SpecimenContainer": (None, ".specimen"),
    "TestScript": (None, ".testscript"),
    "TestScriptContact": (None, ".testscript"),
    "TestScriptMetadata": (None, ".testscript"),
    "TestScriptFixture": (None, ".testscript"),
    "TestScriptVariable": (None, ".testscript"),
    "TestScriptSetup": (None, ".testscript"),
    "TestScriptTest": (None, ".testscript"),
    "TestScriptTeardown": (None, ".testscript"),
    "TestScriptMetadataLink": (None, ".testscript"),
    "TestScriptMetadataCapability": (None, ".testscript"),
    "TestScriptSetupAction": (None, ".testscript"),
    "TestScriptTestAction": (None, ".testscript"),
    "TestScriptTeardownAction": (None, ".testscript"),
    "TestScriptSetupActionOperation": (None, ".testscript"),
    "TestScriptSetupActionAssert": (None, ".testscript"),
    "TestScriptSetupActionOperationRequestHeader": (None, ".testscript"),
}


def get_fhir_model_class(model_name: str) -> typing.Type[FHIRAbstractModel]:
    """"""
    global MODEL_CLASSES
    klass, module_name = MODEL_CLASSES[model_name]
    if klass is not None:
        return klass
    module = importlib.import_module(module_name, package=__package__)
    klass = getattr(module, model_name)
    MODEL_CLASSES[model_name] = (klass, module_name)
    return klass


def run_validator_for_fhir_type(model_type_cls, v, values, config, field):
    """ """
    cls = get_fhir_model_class(model_type_cls.__resource_type__)
    for validator in model_type_cls.__get_validators__():
        func = make_generic_validator(validator)
        v = func(cls, v, values, config, field)
    return v


def fhir_model_validator(
    model_name: str, v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    """ """
    if typing.TYPE_CHECKING:
        model_class: typing.Union[
            typing.Type[BaseModel], typing.Type[FHIRAbstractModel]
        ]
    model_class = get_fhir_model_class(model_name)

    if isinstance(v, (str, bytes)):
        try:
            v = model_class.parse_raw(v)
        except ValidationError as exc:
            if typing.TYPE_CHECKING:
                model_class = typing.cast(typing.Type[BaseModel], model_class)
            errors = exc.errors()
            if (
                len(errors) == 1
                and errors[0]["type"] == "value_error.jsondecode"
                and errors[0]["loc"][0] == ROOT_KEY
            ):
                raise ValidationError(
                    [
                        ErrorWrapper(
                            ValueError(
                                "Invalid json str value has been provided for "
                                f"class {model_class}"
                            ),
                            loc=ROOT_KEY,
                        )
                    ],
                    model_class,
                )

            raise

    elif isinstance(v, Path):
        _p = v
        try:
            v = model_class.parse_file(_p)
        except (ValueError, TypeError) as exc:
            if exc.__class__.__name__ in ("JSONDecodeError", "UnicodeDecodeError"):
                raise ValidationError(
                    [
                        ErrorWrapper(
                            ValueError(
                                f"Provided file '{_p}' for class '{model_class.__name__}' "
                                "as value, contains invalid json data. errors from "
                                f"decoder-> ''{str(exc)}''"
                            ),
                            loc=ROOT_KEY,
                        )
                    ],
                    model_class,
                )

            raise

        except FileNotFoundError:
            raise ValidationError(
                [
                    ErrorWrapper(
                        ValueError(
                            f"Provided file '{_p}' for class {model_class} "
                            "as value, doesn't exists."
                        ),
                        loc=ROOT_KEY,
                    )
                ],
                model_class,
            )

    elif isinstance(v, dict):
        v = model_class.parse_obj(v)

    if not isinstance(v, model_class):
        raise ValidationError(
            [
                ErrorWrapper(
                    ValueError(
                        "Value is expected from the instance of "
                        f"{model_class}, but got type {type(v)}"
                    ),
                    loc=ROOT_KEY,
                )
            ],
            model_class,
        )
    if model_name != v.resource_type:
        raise ValidationError(
            [
                ErrorWrapper(
                    ValueError(
                        f"Expected resource_type is '{model_name}', "
                        f"but value has resource_type '{v.resource_type}'"
                    ),
                    loc=ROOT_KEY,
                )
            ],
            model_class,
        )
    return v


def fhirprimitiveextension_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("FHIRPrimitiveExtension", v)


def element_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Element", v)


def resource_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Resource", v)


def domainresource_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DomainResource", v)


def backboneelement_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("BackboneElement", v)


def extension_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Extension", v)


def meta_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Meta", v)


def narrative_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Narrative", v)


def address_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Address", v)


def period_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Period", v)


def attachment_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Attachment", v)


def codeableconcept_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CodeableConcept", v)


def coding_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Coding", v)


def contactpoint_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ContactPoint", v)


def humanname_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("HumanName", v)


def identifier_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Identifier", v)


def reference_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Reference", v)


def quantity_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Quantity", v)


def range_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Range", v)


def ratio_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Ratio", v)


def signature_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Signature", v)


def timing_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Timing", v)


def timingrepeat_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TimingRepeat", v)


def duration_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Duration", v)


def age_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Age", v)


def count_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Count", v)


def money_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Money", v)


def distance_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Distance", v)


def sampleddata_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SampledData", v)


def annotation_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Annotation", v)


def media_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Media", v)


def basic_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Basic", v)


def binary_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Binary", v)


def bodysite_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("BodySite", v)


def flag_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Flag", v)


def location_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Location", v)


def locationposition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("LocationPosition", v)


def slot_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Slot", v)


def schedule_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Slot", v)


def account_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Account", v)


def allergyintolerance_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AllergyIntolerance", v)


def allergyintolerancereaction_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("AllergyIntoleranceReaction", v)


def appointment_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Appointment", v)


def appointmentparticipant_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AppointmentParticipant", v)


def appointmentresponse_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AppointmentResponse", v)


def auditevent_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AuditEvent", v)


def auditeventevent_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AuditEventEvent", v)


def auditeventobject_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AuditEventObject", v)


def auditeventobjectdetail_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AuditEventObjectDetail", v)


def auditeventparticipant_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AuditEventParticipant", v)


def auditeventparticipantnetwork_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("AuditEventParticipantNetwork", v)


def auditeventsource_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AuditEventSource", v)


def bundle_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Bundle", v)


def bundleentry_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("BundleEntry", v)


def bundleentryrequest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("BundleEntryRequest", v)


def bundleentryresponse_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("BundleEntryResponse", v)


def bundleentrysearch_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("BundleEntrySearch", v)


def bundlelink_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("BundleLink", v)


def careplan_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CarePlan", v)


def careplanactivity_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CarePlanActivity", v)


def careplanactivitydetail_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CarePlanActivityDetail", v)


def careplanparticipant_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CarePlanParticipant", v)


def careplanrelatedplan_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CarePlanRelatedPlan", v)


def claim_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Claim", v)


def claimcoverage_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimCoverage", v)


def claimdiagnosis_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimDiagnosis", v)


def claimitem_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimItem", v)


def claimitemdetail_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimItemDetail", v)


def claimitemdetailsubdetail_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClaimItemDetailSubDetail", v)


def claimitemprosthesis_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimItemProsthesis", v)


def claimmissingteeth_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimMissingTeeth", v)


def claimpayee_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimPayee", v)


def claimresponse_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimResponse", v)


def claimresponseadditem_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimResponseAddItem", v)


def claimresponseadditemadjudication_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClaimResponseAddItemAdjudication", v)


def claimresponseadditemdetail_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClaimResponseAddItemDetail", v)


def claimresponseadditemdetailadjudication_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClaimResponseAddItemDetailAdjudication", v)


def claimresponsecoverage_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimResponseCoverage", v)


def claimresponseerror_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimResponseError", v)


def claimresponseitem_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimResponseItem", v)


def claimresponseitemadjudication_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClaimResponseItemAdjudication", v)


def claimresponseitemdetail_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClaimResponseItemDetail", v)


def claimresponseitemdetailadjudication_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClaimResponseItemDetailAdjudication", v)


def claimresponseitemdetailsubdetail_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClaimResponseItemDetailSubDetail", v)


def claimresponseitemdetailsubdetailadjudication_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClaimResponseItemDetailSubDetailAdjudication", v)


def claimresponsenote_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimResponseNote", v)


def clinicalimpression_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClinicalImpression", v)


def clinicalimpressionfinding_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClinicalImpressionFinding", v)


def clinicalimpressioninvestigations_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClinicalImpressionInvestigations", v)


def clinicalimpressionruledout_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClinicalImpressionRuledOut", v)


def communication_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Communication", v)


def communicationpayload_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CommunicationPayload", v)


def communicationrequest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CommunicationRequest", v)


def communicationrequestpayload_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CommunicationRequestPayload", v)


def composition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Composition", v)


def compositionattester_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CompositionAttester", v)


def compositionevent_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CompositionEvent", v)


def compositionsection_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CompositionSection", v)


def conceptmap_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConceptMap", v)


def conceptmapcontact_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConceptMapContact", v)


def conceptmapelement_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConceptMapElement", v)


def conceptmapelementtarget_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ConceptMapElementTarget", v)


def conceptmapelementtargetdependson_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ConceptMapElementTargetDependsOn", v)


def condition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Condition", v)


def conditionevidence_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConditionEvidence", v)


def conditionstage_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConditionStage", v)


def conformance_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Conformance", v)


def conformancecontact_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConformanceContact", v)


def conformancedocument_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConformanceDocument", v)


def conformanceimplementation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ConformanceImplementation", v)


def conformancemessaging_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConformanceMessaging", v)


def conformancemessagingendpoint_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ConformanceMessagingEndpoint", v)


def conformancemessagingevent_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ConformanceMessagingEvent", v)


def conformancerest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConformanceRest", v)


def conformancerestinteraction_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ConformanceRestInteraction", v)


def conformancerestoperation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ConformanceRestOperation", v)


def conformancerestresource_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ConformanceRestResource", v)


def conformancerestresourceinteraction_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ConformanceRestResourceInteraction", v)


def conformancerestsecurity_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ConformanceRestSecurity", v)


def conformancerestsecuritycertificate_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ConformanceRestSecurityCertificate", v)


def conformancesoftware_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConformanceSoftware", v)


def conformancerestresourcesearchparam_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ConformanceRestResourceSearchParam", v)


def patient_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Patient", v)


def patientanimal_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("PatientAnimal", v)


def patientcommunication_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("PatientCommunication", v)


def patientcontact_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("PatientContact", v)


def patientlink_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("PatientLink", v)


def organization_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Organization", v)


def organizationcontact_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("OrganizationContact", v)


def person_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Person", v)


def personlink_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("PersonLink", v)


def practitioner_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Practitioner", v)


def practitionerpractitionerrole_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PractitionerPractitionerRole", v)


def practitionerqualification_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PractitionerQualification", v)


def valueset_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ValueSet", v)


def valuesetcodesystem_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ValueSetCodeSystem", v)


def valuesetcodesystemconcept_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ValueSetCodeSystemConcept", v)


def valuesetcodesystemconceptdesignation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ValueSetCodeSystemConceptDesignation", v)


def valuesetcompose_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ValueSetCompose", v)


def valuesetcomposeinclude_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ValueSetComposeInclude", v)


def valuesetcomposeincludeconcept_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ValueSetComposeIncludeConcept", v)


def valuesetcomposeincludefilter_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ValueSetComposeIncludeFilter", v)


def valuesetcontact_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ValueSetContact", v)


def valuesetexpansion_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ValueSetExpansion", v)


def valuesetexpansioncontains_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ValueSetExpansionContains", v)


def valuesetexpansionparameter_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ValueSetExpansionParameter", v)


def procedure_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Procedure", v)


def procedurefocaldevice_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ProcedureFocalDevice", v)


def procedureperformer_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ProcedurePerformer", v)


def procedurerequest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ProcedureRequest", v)


def diagnosticreport_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DiagnosticReport", v)


def diagnosticreportimage_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DiagnosticReportImage", v)


def goal_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Goal", v)


def goaloutcome_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("GoalOutcome", v)


def group_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Group", v)


def groupcharacteristic_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("GroupCharacteristic", v)


def groupmember_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("GroupMember", v)


def eligibilityrequest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EligibilityRequest", v)


def eligibilityresponse_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EligibilityResponse", v)


def encounter_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Encounter", v)


def encounterhospitalization_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("EncounterHospitalization", v)


def encounterlocation_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EncounterLocation", v)


def encounterparticipant_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EncounterParticipant", v)


def encounterstatushistory_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EncounterStatusHistory", v)


def enrollmentrequest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EnrollmentRequest", v)


def enrollmentresponse_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EnrollmentResponse", v)


def immunization_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Immunization", v)


def immunizationexplanation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImmunizationExplanation", v)


def immunizationreaction_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ImmunizationReaction", v)


def immunizationvaccinationprotocol_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImmunizationVaccinationProtocol", v)


def medicationadministration_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationAdministration", v)


def medicationadministrationdosage_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationAdministrationDosage", v)


def medicationstatement_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MedicationStatement", v)


def medicationstatementdosage_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationStatementDosage", v)


def observation_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Observation", v)


def observationcomponent_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ObservationComponent", v)


def observationreferencerange_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ObservationReferenceRange", v)


def observationrelated_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ObservationRelated", v)


def operationoutcome_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("OperationOutcome", v)


def operationoutcomeissue_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("OperationOutcomeIssue", v)


def medication_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Medication", v)


def medicationpackage_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MedicationPackage", v)


def medicationpackagecontent_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationPackageContent", v)


def medicationproduct_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MedicationProduct", v)


def medicationproductbatch_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MedicationProductBatch", v)


def medicationproductingredient_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationProductIngredient", v)


def contract_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Contract", v)


def contractactor_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ContractActor", v)


def contractfriendly_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ContractFriendly", v)


def contractlegal_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ContractLegal", v)


def contractrule_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ContractRule", v)


def contractsigner_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ContractSigner", v)


def contractterm_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ContractTerm", v)


def contracttermactor_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ContractTermActor", v)


def contracttermvalueditem_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ContractTermValuedItem", v)


def contractvalueditem_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ContractValuedItem", v)


def device_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Device", v)


def dataelement_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DataElement", v)


def dataelementcontact_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DataElementContact", v)


def dataelementmapping_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DataElementMapping", v)


def detectedissue_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DetectedIssue", v)


def detectedissuemitigation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DetectedIssueMitigation", v)


def devicecomponent_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceComponent", v)


def devicecomponentproductionspecification_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DeviceComponentProductionSpecification", v)


def devicemetric_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceMetric", v)


def devicemetriccalibration_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DeviceMetricCalibration", v)


def deviceuserequest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceUseRequest", v)


def deviceusestatement_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceUseStatement", v)


def diagnosticorder_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DiagnosticOrder", v)


def diagnosticorderevent_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DiagnosticOrderEvent", v)


def diagnosticorderitem_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DiagnosticOrderItem", v)


def documentmanifest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DocumentManifest", v)


def documentmanifestcontent_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DocumentManifestContent", v)


def documentmanifestrelated_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DocumentManifestRelated", v)


def documentreference_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DocumentReference", v)


def documentreferencecontent_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DocumentReferenceContent", v)


def documentreferencecontext_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DocumentReferenceContext", v)


def documentreferencecontextrelated_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DocumentReferenceContextRelated", v)


def documentreferencerelatesto_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DocumentReferenceRelatesTo", v)


def elementdefinition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ElementDefinition", v)


def elementdefinitionbase_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ElementDefinitionBase", v)


def elementdefinitionbinding_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ElementDefinitionBinding", v)


def elementdefinitionconstraint_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ElementDefinitionConstraint", v)


def elementdefinitionmapping_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ElementDefinitionMapping", v)


def elementdefinitionslicing_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ElementDefinitionSlicing", v)


def elementdefinitiontype_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ElementDefinitionType", v)


def episodeofcare_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EpisodeOfCare", v)


def episodeofcarecareteam_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EpisodeOfCareCareTeam", v)


def episodeofcarestatushistory_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("EpisodeOfCareStatusHistory", v)


def familymemberhistory_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("FamilyMemberHistory", v)


def familymemberhistorycondition_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("FamilyMemberHistoryCondition", v)


def explanationofbenefit_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ExplanationOfBenefit", v)


def healthcareservice_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("HealthcareService", v)


def healthcareserviceavailabletime_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("HealthcareServiceAvailableTime", v)


def healthcareservicenotavailable_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("HealthcareServiceNotAvailable", v)


def healthcareserviceservicetype_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("HealthcareServiceServiceType", v)


def imagingobjectselection_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ImagingObjectSelection", v)


def imagingobjectselectionstudy_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImagingObjectSelectionStudy", v)


def imagingobjectselectionstudyseries_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImagingObjectSelectionStudySeries", v)


def imagingobjectselectionstudyseriesinstance_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImagingObjectSelectionStudySeriesInstance", v)


def imagingobjectselectionstudyseriesinstanceframes_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImagingObjectSelectionStudySeriesInstanceFrames", v)


def imagingstudy_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ImagingStudy", v)


def imagingstudyseries_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ImagingStudySeries", v)


def imagingstudyseriesinstance_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImagingStudySeriesInstance", v)


def immunizationrecommendation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImmunizationRecommendation", v)


def immunizationrecommendationrecommendation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImmunizationRecommendationRecommendation", v)


def immunizationrecommendationrecommendationdatecriterion_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator(
        "ImmunizationRecommendationRecommendationDateCriterion", v
    )


def immunizationrecommendationrecommendationprotocol_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImmunizationRecommendationRecommendationProtocol", v)


def implementationguide_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ImplementationGuide", v)


def implementationguidecontact_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImplementationGuideContact", v)


def implementationguidedependency_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImplementationGuideDependency", v)


def implementationguideglobal_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImplementationGuideGlobal", v)


def implementationguidepackage_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImplementationGuidePackage", v)


def implementationguidepackageresource_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImplementationGuidePackageResource", v)


def implementationguidepage_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImplementationGuidePage", v)


def list_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("List", v)


def listentry_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ListEntry", v)


def medicationdispense_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MedicationDispense", v)


def medicationdispensedosageinstruction_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationDispenseDosageInstruction", v)


def medicationdispensesubstitution_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationDispenseSubstitution", v)


def medicationorder_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MedicationOrder", v)


def medicationorderdispenserequest_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationOrderDispenseRequest", v)


def medicationorderdosageinstruction_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationOrderDosageInstruction", v)


def medicationordersubstitution_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationOrderSubstitution", v)


def messageheader_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MessageHeader", v)


def messageheaderdestination_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MessageHeaderDestination", v)


def messageheaderresponse_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MessageHeaderResponse", v)


def messageheadersource_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MessageHeaderSource", v)


def namingsystem_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("NamingSystem", v)


def namingsystemcontact_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("NamingSystemContact", v)


def namingsystemuniqueid_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("NamingSystemUniqueId", v)


def nutritionorder_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("NutritionOrder", v)


def nutritionorderoraldiet_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("NutritionOrderOralDiet", v)


def nutritionordersupplement_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("NutritionOrderSupplement", v)


def nutritionorderenteralformula_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("NutritionOrderEnteralFormula", v)


def nutritionorderoraldietnutrient_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("NutritionOrderOralDietNutrient", v)


def nutritionorderoraldiettexture_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("NutritionOrderOralDietTexture", v)


def nutritionorderenteralformulaadministration_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("NutritionOrderEnteralFormulaAdministration", v)


def operationdefinition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("OperationDefinition", v)


def operationdefinitioncontact_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("OperationDefinitionContact", v)


def operationdefinitionparameter_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("OperationDefinitionParameter", v)


def operationdefinitionparameterbinding_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("OperationDefinitionParameterBinding", v)


def order_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Order", v)


def orderwhen_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("OrderWhen", v)


def orderresponse_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("OrderResponse", v)


def parameters_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Parameters", v)


def parametersparameter_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ParametersParameter", v)


def processresponse_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ProcessResponse", v)


def processresponsenotes_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ProcessResponseNotes", v)


def processrequest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ProcessRequest", v)


def processrequestitem_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ProcessRequestItem", v)


def paymentreconciliation_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("PaymentReconciliation", v)


def paymentreconciliationdetail_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PaymentReconciliationDetail", v)


def paymentreconciliationnote_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PaymentReconciliationNote", v)


def paymentnotice_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("PaymentNotice", v)


def provenance_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Provenance", v)


def provenanceagent_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ProvenanceAgent", v)


def provenanceagentrelatedagent_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ProvenanceAgentRelatedAgent", v)


def provenanceentity_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ProvenanceEntity", v)


def questionnaireresponse_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("QuestionnaireResponse", v)


def questionnaireresponsegroup_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("QuestionnaireResponseGroup", v)


def questionnaireresponsegroupquestion_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("QuestionnaireResponseGroupQuestion", v)


def questionnaireresponsegroupquestionanswer_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("QuestionnaireResponseGroupQuestionAnswer", v)


def questionnaire_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Questionnaire", v)


def questionnairegroup_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("QuestionnaireGroup", v)


def questionnairegroupquestion_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("QuestionnaireGroupQuestion", v)


def referralrequest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ReferralRequest", v)


def riskassessment_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("RiskAssessment", v)


def riskassessmentprediction_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("RiskAssessmentPrediction", v)


def searchparameter_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SearchParameter", v)


def searchparametercontact_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SearchParameterContact", v)


def subscription_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Subscription", v)


def subscriptionchannel_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SubscriptionChannel", v)


def substance_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Substance", v)


def substanceinstance_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SubstanceInstance", v)


def substanceingredient_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SubstanceIngredient", v)


def supplydelivery_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SupplyDelivery", v)


def supplyrequest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SupplyRequest", v)


def supplyrequestwhen_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SupplyRequestWhen", v)


def visionprescription_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("VisionPrescription", v)


def visionprescriptiondispense_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("VisionPrescriptionDispense", v)


def specimen_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Specimen", v)


def specimencollection_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SpecimenCollection", v)


def specimentreatment_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SpecimenTreatment", v)


def specimencontainer_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SpecimenContainer", v)


def testscript_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScript", v)


def testscriptcontact_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScriptContact", v)


def testscriptmetadata_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScriptMetadata", v)


def testscriptfixture_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScriptFixture", v)


def testscriptvariable_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScriptVariable", v)


def testscriptsetup_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScriptSetup", v)


def testscripttest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScriptTest", v)


def testscriptteardown_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScriptTeardown", v)


def testscriptmetadatalink_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScriptMetadataLink", v)


def testscriptmetadatacapability_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TestScriptMetadataCapability", v)


def testscriptsetupaction_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScriptSetupAction", v)


def testscripttestaction_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScriptTestAction", v)


def testscriptteardownaction_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TestScriptTeardownAction", v)


def testscriptsetupactionoperation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TestScriptSetupActionOperation", v)


def testscriptsetupactionassert_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TestScriptSetupActionAssert", v)


def testscriptsetupactionoperationrequestheader_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TestScriptSetupActionOperationRequestHeader", v)


__all__ = [
    "element_validator",
    "resource_validator",
    "domainresource_validator",
    "backboneelement_validator",
    "extension_validator",
    "meta_validator",
    "narrative_validator",
    "address_validator",
    "period_validator",
    "attachment_validator",
    "codeableconcept_validator",
    "coding_validator",
    "contactpoint_validator",
    "humanname_validator",
    "identifier_validator",
    "reference_validator",
    "quantity_validator",
    "range_validator",
    "ratio_validator",
    "signature_validator",
    "timing_validator",
    "timingrepeat_validator",
    "duration_validator",
    "age_validator",
    "count_validator",
    "money_validator",
    "distance_validator",
    "sampleddata_validator",
    "annotation_validator",
    "media_validator",
    "basic_validator",
    "binary_validator",
    "bodysite_validator",
    "flag_validator",
    "location_validator",
    "locationposition_validator",
    "slot_validator",
    "schedule_validator",
    "account_validator",
    "allergyintolerance_validator",
    "allergyintolerancereaction_validator",
    "appointment_validator",
    "appointmentparticipant_validator",
    "appointmentresponse_validator",
    "auditevent_validator",
    "auditeventevent_validator",
    "auditeventobjectdetail_validator",
    "auditeventparticipantnetwork_validator",
    "auditeventsource_validator",
    "bundle_validator",
    "bundleentry_validator",
    "bundleentryrequest_validator",
    "bundleentryresponse_validator",
    "bundleentrysearch_validator",
    "bundlelink_validator",
    "careplan_validator",
    "careplanactivity_validator",
    "careplanactivity_validator",
    "careplanactivitydetail_validator",
    "careplanparticipant_validator",
    "careplanrelatedplan_validator",
    "claim_validator",
    "claimcoverage_validator",
    "claimdiagnosis_validator",
    "claimitem_validator",
    "claimitemdetail_validator",
    "claimitemdetailsubdetail_validator",
    "claimitemprosthesis_validator",
    "claimmissingteeth_validator",
    "claimpayee_validator",
    "claimresponse_validator",
    "claimresponseadditem_validator",
    "claimresponseadditemadjudication_validator",
    "claimresponseadditemdetail_validator",
    "claimresponseadditemdetailadjudication_validator",
    "claimresponseerror_validator",
    "claimresponseitem_validator",
    "claimresponseitemadjudication_validator",
    "claimresponseitemdetail_validator",
    "claimresponseitemdetailadjudication_validator",
    "claimresponseitemdetailsubdetail_validator",
    "claimresponseitemdetailsubdetailadjudication_validator",
    "claimresponsenote_validator",
    "clinicalimpression_validator",
    "clinicalimpressionfinding_validator",
    "clinicalimpressioninvestigations_validator",
    "clinicalimpressionruledout_validator",
    "communication_validator",
    "communicationpayload_validator",
    "communicationrequest_validator",
    "communicationrequestpayload_validator",
    "composition_validator",
    "compositionattester_validator",
    "compositionevent_validator",
    "compositionsection_validator",
    "conceptmap_validator",
    "conceptmapcontact_validator",
    "conceptmapelement_validator",
    "conceptmapelementtargetdependson_validator",
    "condition_validator",
    "conditionevidence_validator",
    "conditionstage_validator",
    "conformance_validator",
    "conformancecontact_validator",
    "conformancedocument_validator",
    "conformanceimplementation_validator",
    "conformancemessaging_validator",
    "conformancemessagingendpoint_validator",
    "conformancemessagingevent_validator",
    "conformancerest_validator",
    "conformancerestinteraction_validator",
    "conformancerestoperation_validator",
    "conformancerestresource_validator",
    "conformancerestresourceinteraction_validator",
    "conformancerestsecurity_validator",
    "conformancerestsecuritycertificate_validator",
    "conformancesoftware_validator",
    "conformancerestresourcesearchparam_validator",
    "patient_validator",
    "patientanimal_validator",
    "patientcommunication_validator",
    "patientcontact_validator",
    "patientlink_validator",
    "organization_validator",
    "organizationcontact_validator",
    "person_validator",
    "personlink_validator",
    "practitioner_validator",
    "practitionerpractitionerrole_validator",
    "practitionerqualification_validator",
    "valueset_validator",
    "valuesetcodesystem_validator",
    "valuesetcodesystemconcept_validator",
    "valuesetcodesystemconceptdesignation_validator",
    "valuesetcompose_validator",
    "valuesetcomposeinclude_validator",
    "valuesetcomposeincludeconcept_validator",
    "valuesetcomposeincludefilter_validator",
    "valuesetcontact_validator",
    "valuesetexpansion_validator",
    "valuesetexpansioncontains_validator",
    "valuesetexpansionparameter_validator",
    "procedure_validator",
    "procedurefocaldevice_validator",
    "procedureperformer_validator",
    "procedurerequest_validator",
    "diagnosticreport_validator",
    "diagnosticreportimage_validator",
    "goal_validator",
    "goaloutcome_validator",
    "group_validator",
    "groupcharacteristic_validator",
    "groupmember_validator",
    "eligibilityrequest_validator",
    "eligibilityresponse_validator",
    "encounter_validator",
    "encounterhospitalization_validator",
    "encounterlocation_validator",
    "encounterparticipant_validator",
    "encounterstatushistory_validator",
    "enrollmentrequest_validator",
    "enrollmentresponse_validator",
    "immunization_validator",
    "immunizationexplanation_validator",
    "immunizationreaction_validator",
    "immunizationvaccinationprotocol_validator",
    "medicationadministration_validator",
    "medicationadministrationdosage_validator",
    "medicationstatement_validator",
    "medicationstatementdosage_validator",
    "observation_validator",
    "observationcomponent_validator",
    "observationreferencerange_validator",
    "observationrelated_validator",
    "operationoutcome_validator",
    "operationoutcomeissue_validator",
    "medication_validator",
    "medicationpackage_validator",
    "medicationpackagecontent_validator",
    "medicationproduct_validator",
    "medicationproductbatch_validator",
    "medicationproductingredient_validator",
    "contract_validator",
    "contractactor_validator",
    "contractfriendly_validator",
    "contractlegal_validator",
    "contractrule_validator",
    "contractsigner_validator",
    "contractterm_validator",
    "contracttermactor_validator",
    "contracttermvalueditem_validator",
    "contractvalueditem_validator",
    "device_validator",
    "elementdefinition_validator",
    "elementdefinitionbase_validator",
    "elementdefinitionbinding_validator",
    "elementdefinitionconstraint_validator",
    "elementdefinitionmapping_validator",
    "elementdefinitionslicing_validator",
    "elementdefinitiontype_validator",
    "dataelement_validator",
    "dataelementcontact_validator",
    "dataelementmapping_validator",
    "detectedissue_validator",
    "detectedissuemitigation_validator",
    "devicecomponent_validator",
    "devicecomponentproductionspecification_validator",
    "devicemetric_validator",
    "devicemetriccalibration_validator",
    "deviceuserequest_validator",
    "deviceusestatement_validator",
    "diagnosticorder_validator",
    "diagnosticorderevent_validator",
    "diagnosticorderitem_validator",
    "documentmanifest_validator",
    "documentmanifestcontent_validator",
    "documentmanifestrelated_validator",
    "documentreference_validator",
    "documentreferencecontent_validator",
    "documentreferencecontext_validator",
    "documentreferencecontextrelated_validator",
    "documentreferencerelatesto_validator",
    "episodeofcare_validator",
    "episodeofcarecareteam_validator",
    "episodeofcarestatushistory_validator",
    "familymemberhistory_validator",
    "familymemberhistorycondition_validator",
    "explanationofbenefit_validator",
    "healthcareservice_validator",
    "healthcareserviceavailabletime_validator",
    "healthcareservicenotavailable_validator",
    "healthcareserviceservicetype_validator",
    "imagingobjectselection_validator",
    "imagingobjectselectionstudy_validator",
    "imagingobjectselectionstudyseries_validator",
    "imagingobjectselectionstudyseriesinstance_validator",
    "imagingobjectselectionstudyseriesinstanceframes_validator",
    "imagingstudy_validator",
    "imagingstudyseries_validator",
    "imagingstudyseriesinstance_validator",
    "immunizationrecommendation_validator",
    "immunizationrecommendationrecommendation_validator",
    "immunizationrecommendationrecommendationdatecriterion_validator",
    "immunizationrecommendationrecommendationprotocol_validator",
    "implementationguide_validator",
    "implementationguidecontact_validator",
    "implementationguidedependency_validator",
    "implementationguideglobal_validator",
    "implementationguidepackage_validator",
    "implementationguidepackageresource_validator",
    "implementationguidepage_validator",
    "list_validator",
    "listentry_validator",
    "medicationdispense_validator",
    "medicationdispensedosageinstruction_validator",
    "medicationdispensesubstitution_validator",
    "medicationorder_validator",
    "medicationorderdispenserequest_validator",
    "medicationorderdosageinstruction_validator",
    "medicationordersubstitution_validator",
    "messageheader_validator",
    "messageheaderdestination_validator",
    "messageheaderresponse_validator",
    "messageheadersource_validator",
    "namingsystem_validator",
    "namingsystemcontact_validator",
    "namingsystemuniqueid_validator",
    "nutritionorder_validator",
    "nutritionorderoraldiet_validator",
    "nutritionordersupplement_validator",
    "nutritionorderenteralformula_validator",
    "nutritionorderoraldietnutrient_validator",
    "nutritionorderoraldiettexture_validator",
    "nutritionorderenteralformulaadministration_validator",
    "operationdefinition_validator",
    "operationdefinitioncontact_validator",
    "operationdefinitionparameter_validator",
    "operationdefinitionparameterbinding_validator",
    "parameters_validator",
    "parametersparameter_validator",
    "processresponse_validator",
    "processresponsenotes_validator",
    "processrequest_validator",
    "processrequestitem_validator",
    "paymentreconciliation_validator",
    "paymentreconciliationdetail_validator",
    "paymentreconciliationnote_validator",
    "paymentnotice_validator",
    "provenance_validator",
    "provenanceagent_validator",
    "provenanceagentrelatedagent_validator",
    "provenanceentity_validator",
    "questionnaireresponse_validator",
    "questionnaireresponsegroup_validator",
    "questionnaireresponsegroupquestion_validator",
    "questionnaireresponsegroupquestionanswer_validator",
    "questionnaire_validator",
    "questionnairegroup_validator",
    "questionnairegroupquestion_validator",
    "referralrequest_validator",
    "riskassessment_validator",
    "riskassessmentprediction_validator",
    "searchparameter_validator",
    "searchparametercontact_validator",
    "subscription_validator",
    "subscriptionchannel_validator",
    "substance_validator",
    "substanceinstance_validator",
    "substanceingredient_validator",
    "supplydelivery_validator",
    "supplyrequest_validator",
    "supplyrequestwhen_validator",
    "order_validator",
    "orderwhen_validator",
    "orderresponse_validator",
    "visionprescription_validator",
    "visionprescriptiondispense_validator",
    "specimen_validator",
    "specimencollection_validator",
    "specimentreatment_validator",
    "specimencontainer_validator",
    "testscript_validator",
    "testscriptcontact_validator",
    "testscriptmetadata_validator",
    "testscriptfixture_validator",
    "testscriptvariable_validator",
    "testscriptsetup_validator",
    "testscripttest_validator",
    "testscriptteardown_validator",
    "testscriptmetadatalink_validator",
    "testscriptmetadatacapability_validator",
    "testscriptsetupaction_validator",
    "testscripttestaction_validator",
    "testscriptteardownaction_validator",
    "testscriptsetupactionoperation_validator",
    "testscriptsetupactionassert_validator",
    "testscriptsetupactionoperationrequestheader_validator",
]
