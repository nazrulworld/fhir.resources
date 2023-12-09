# _*_ coding: utf-8 _*_
"""Validators for ``pydantic.v1`` Custom DataType"""
import importlib
import typing
from pathlib import Path
from typing import Union

from pydantic.v1.class_validators import make_generic_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.types import StrBytes
from pydantic.v1.utils import ROOT_KEY

from fhir.resources.core.fhirabstractmodel import FHIRAbstractModel

if typing.TYPE_CHECKING:
    from pydantic.v1 import BaseModel

__author__ = "Md Nazrul Islam<email2nazrul@gmail.com>"

MODEL_CLASSES = {
    "FHIRPrimitiveExtension": (None, ".fhirprimitiveextension"),
    "Account": (None, ".account"),
    "AccountCoverage": (None, ".account"),
    "AccountGuarantor": (None, ".account"),
    "ActivityDefinition": (None, ".activitydefinition"),
    "ActivityDefinitionDynamicValue": (None, ".activitydefinition"),
    "ActivityDefinitionParticipant": (None, ".activitydefinition"),
    "Address": (None, ".address"),
    "AdverseEvent": (None, ".adverseevent"),
    "AdverseEventSuspectEntity": (None, ".adverseevent"),
    "Age": (None, ".age"),
    "AllergyIntolerance": (None, ".allergyintolerance"),
    "AllergyIntoleranceReaction": (None, ".allergyintolerance"),
    "Annotation": (None, ".annotation"),
    "Appointment": (None, ".appointment"),
    "AppointmentParticipant": (None, ".appointment"),
    "AppointmentResponse": (None, ".appointmentresponse"),
    "Attachment": (None, ".attachment"),
    "AuditEvent": (None, ".auditevent"),
    "AuditEventAgent": (None, ".auditevent"),
    "AuditEventAgentNetwork": (None, ".auditevent"),
    "AuditEventEntity": (None, ".auditevent"),
    "AuditEventEntityDetail": (None, ".auditevent"),
    "AuditEventSource": (None, ".auditevent"),
    "BackboneElement": (None, ".backboneelement"),
    "Basic": (None, ".basic"),
    "Binary": (None, ".binary"),
    "BodySite": (None, ".bodysite"),
    "Bundle": (None, ".bundle"),
    "BundleEntry": (None, ".bundle"),
    "BundleEntryRequest": (None, ".bundle"),
    "BundleEntryResponse": (None, ".bundle"),
    "BundleEntrySearch": (None, ".bundle"),
    "BundleLink": (None, ".bundle"),
    "CapabilityStatement": (None, ".capabilitystatement"),
    "CapabilityStatementDocument": (None, ".capabilitystatement"),
    "CapabilityStatementImplementation": (None, ".capabilitystatement"),
    "CapabilityStatementMessaging": (None, ".capabilitystatement"),
    "CapabilityStatementMessagingEndpoint": (None, ".capabilitystatement"),
    "CapabilityStatementMessagingEvent": (None, ".capabilitystatement"),
    "CapabilityStatementMessagingSupportedMessage": (None, ".capabilitystatement"),
    "CapabilityStatementRest": (None, ".capabilitystatement"),
    "CapabilityStatementRestInteraction": (None, ".capabilitystatement"),
    "CapabilityStatementRestOperation": (None, ".capabilitystatement"),
    "CapabilityStatementRestResource": (None, ".capabilitystatement"),
    "CapabilityStatementRestResourceInteraction": (None, ".capabilitystatement"),
    "CapabilityStatementRestResourceSearchParam": (None, ".capabilitystatement"),
    "CapabilityStatementRestSecurity": (None, ".capabilitystatement"),
    "CapabilityStatementRestSecurityCertificate": (None, ".capabilitystatement"),
    "CapabilityStatementSoftware": (None, ".capabilitystatement"),
    "CarePlan": (None, ".careplan"),
    "CarePlanActivity": (None, ".careplan"),
    "CarePlanActivityDetail": (None, ".careplan"),
    "CareTeam": (None, ".careteam"),
    "CareTeamParticipant": (None, ".careteam"),
    "ChargeItem": (None, ".chargeitem"),
    "ChargeItemParticipant": (None, ".chargeitem"),
    "Claim": (None, ".claim"),
    "ClaimAccident": (None, ".claim"),
    "ClaimCareTeam": (None, ".claim"),
    "ClaimDiagnosis": (None, ".claim"),
    "ClaimInformation": (None, ".claim"),
    "ClaimInsurance": (None, ".claim"),
    "ClaimItem": (None, ".claim"),
    "ClaimItemDetail": (None, ".claim"),
    "ClaimItemDetailSubDetail": (None, ".claim"),
    "ClaimPayee": (None, ".claim"),
    "ClaimProcedure": (None, ".claim"),
    "ClaimRelated": (None, ".claim"),
    "ClaimResponse": (None, ".claimresponse"),
    "ClaimResponseAddItem": (None, ".claimresponse"),
    "ClaimResponseAddItemDetail": (None, ".claimresponse"),
    "ClaimResponseError": (None, ".claimresponse"),
    "ClaimResponseInsurance": (None, ".claimresponse"),
    "ClaimResponseItem": (None, ".claimresponse"),
    "ClaimResponseItemAdjudication": (None, ".claimresponse"),
    "ClaimResponseItemDetail": (None, ".claimresponse"),
    "ClaimResponseItemDetailSubDetail": (None, ".claimresponse"),
    "ClaimResponsePayment": (None, ".claimresponse"),
    "ClaimResponseProcessNote": (None, ".claimresponse"),
    "ClinicalImpression": (None, ".clinicalimpression"),
    "ClinicalImpressionFinding": (None, ".clinicalimpression"),
    "ClinicalImpressionInvestigation": (None, ".clinicalimpression"),
    "CodeSystem": (None, ".codesystem"),
    "CodeSystemConcept": (None, ".codesystem"),
    "CodeSystemConceptDesignation": (None, ".codesystem"),
    "CodeSystemConceptProperty": (None, ".codesystem"),
    "CodeSystemFilter": (None, ".codesystem"),
    "CodeSystemProperty": (None, ".codesystem"),
    "CodeableConcept": (None, ".codeableconcept"),
    "Coding": (None, ".coding"),
    "Communication": (None, ".communication"),
    "CommunicationPayload": (None, ".communication"),
    "CommunicationRequest": (None, ".communicationrequest"),
    "CommunicationRequestPayload": (None, ".communicationrequest"),
    "CommunicationRequestRequester": (None, ".communicationrequest"),
    "CompartmentDefinition": (None, ".compartmentdefinition"),
    "CompartmentDefinitionResource": (None, ".compartmentdefinition"),
    "Composition": (None, ".composition"),
    "CompositionAttester": (None, ".composition"),
    "CompositionEvent": (None, ".composition"),
    "CompositionRelatesTo": (None, ".composition"),
    "CompositionSection": (None, ".composition"),
    "ConceptMap": (None, ".conceptmap"),
    "ConceptMapGroup": (None, ".conceptmap"),
    "ConceptMapGroupElement": (None, ".conceptmap"),
    "ConceptMapGroupElementTarget": (None, ".conceptmap"),
    "ConceptMapGroupElementTargetDependsOn": (None, ".conceptmap"),
    "ConceptMapGroupUnmapped": (None, ".conceptmap"),
    "Condition": (None, ".condition"),
    "ConditionEvidence": (None, ".condition"),
    "ConditionStage": (None, ".condition"),
    "Consent": (None, ".consent"),
    "ConsentActor": (None, ".consent"),
    "ConsentData": (None, ".consent"),
    "ConsentExcept": (None, ".consent"),
    "ConsentExceptActor": (None, ".consent"),
    "ConsentExceptData": (None, ".consent"),
    "ConsentPolicy": (None, ".consent"),
    "ContactDetail": (None, ".contactdetail"),
    "ContactPoint": (None, ".contactpoint"),
    "Contract": (None, ".contract"),
    "ContractAgent": (None, ".contract"),
    "ContractFriendly": (None, ".contract"),
    "ContractLegal": (None, ".contract"),
    "ContractRule": (None, ".contract"),
    "ContractSigner": (None, ".contract"),
    "ContractTerm": (None, ".contract"),
    "ContractTermAgent": (None, ".contract"),
    "ContractTermValuedItem": (None, ".contract"),
    "ContractValuedItem": (None, ".contract"),
    "Contributor": (None, ".contributor"),
    "Count": (None, ".count"),
    "Coverage": (None, ".coverage"),
    "CoverageGrouping": (None, ".coverage"),
    "DataElement": (None, ".dataelement"),
    "DataElementMapping": (None, ".dataelement"),
    "DataRequirement": (None, ".datarequirement"),
    "DataRequirementCodeFilter": (None, ".datarequirement"),
    "DataRequirementDateFilter": (None, ".datarequirement"),
    "DetectedIssue": (None, ".detectedissue"),
    "DetectedIssueMitigation": (None, ".detectedissue"),
    "Device": (None, ".device"),
    "DeviceComponent": (None, ".devicecomponent"),
    "DeviceComponentProductionSpecification": (None, ".devicecomponent"),
    "DeviceMetric": (None, ".devicemetric"),
    "DeviceMetricCalibration": (None, ".devicemetric"),
    "DeviceRequest": (None, ".devicerequest"),
    "DeviceRequestRequester": (None, ".devicerequest"),
    "DeviceUdi": (None, ".device"),
    "DeviceUseStatement": (None, ".deviceusestatement"),
    "DiagnosticReport": (None, ".diagnosticreport"),
    "DiagnosticReportImage": (None, ".diagnosticreport"),
    "DiagnosticReportPerformer": (None, ".diagnosticreport"),
    "Distance": (None, ".distance"),
    "DocumentManifest": (None, ".documentmanifest"),
    "DocumentManifestContent": (None, ".documentmanifest"),
    "DocumentManifestRelated": (None, ".documentmanifest"),
    "DocumentReference": (None, ".documentreference"),
    "DocumentReferenceContent": (None, ".documentreference"),
    "DocumentReferenceContext": (None, ".documentreference"),
    "DocumentReferenceContextRelated": (None, ".documentreference"),
    "DocumentReferenceRelatesTo": (None, ".documentreference"),
    "DomainResource": (None, ".domainresource"),
    "Dosage": (None, ".dosage"),
    "Duration": (None, ".duration"),
    "Element": (None, ".element"),
    "ElementDefinition": (None, ".elementdefinition"),
    "ElementDefinitionBase": (None, ".elementdefinition"),
    "ElementDefinitionBinding": (None, ".elementdefinition"),
    "ElementDefinitionConstraint": (None, ".elementdefinition"),
    "ElementDefinitionExample": (None, ".elementdefinition"),
    "ElementDefinitionMapping": (None, ".elementdefinition"),
    "ElementDefinitionSlicing": (None, ".elementdefinition"),
    "ElementDefinitionSlicingDiscriminator": (None, ".elementdefinition"),
    "ElementDefinitionType": (None, ".elementdefinition"),
    "EligibilityRequest": (None, ".eligibilityrequest"),
    "EligibilityResponse": (None, ".eligibilityresponse"),
    "EligibilityResponseError": (None, ".eligibilityresponse"),
    "EligibilityResponseInsurance": (None, ".eligibilityresponse"),
    "EligibilityResponseInsuranceBenefitBalance": (None, ".eligibilityresponse"),
    "EligibilityResponseInsuranceBenefitBalanceFinancial": (
        None,
        ".eligibilityresponse",
    ),
    "Encounter": (None, ".encounter"),
    "EncounterClassHistory": (None, ".encounter"),
    "EncounterDiagnosis": (None, ".encounter"),
    "EncounterHospitalization": (None, ".encounter"),
    "EncounterLocation": (None, ".encounter"),
    "EncounterParticipant": (None, ".encounter"),
    "EncounterStatusHistory": (None, ".encounter"),
    "Endpoint": (None, ".endpoint"),
    "EnrollmentRequest": (None, ".enrollmentrequest"),
    "EnrollmentResponse": (None, ".enrollmentresponse"),
    "EpisodeOfCare": (None, ".episodeofcare"),
    "EpisodeOfCareDiagnosis": (None, ".episodeofcare"),
    "EpisodeOfCareStatusHistory": (None, ".episodeofcare"),
    "ExpansionProfile": (None, ".expansionprofile"),
    "ExpansionProfileDesignation": (None, ".expansionprofile"),
    "ExpansionProfileDesignationExclude": (None, ".expansionprofile"),
    "ExpansionProfileDesignationExcludeDesignation": (None, ".expansionprofile"),
    "ExpansionProfileDesignationInclude": (None, ".expansionprofile"),
    "ExpansionProfileDesignationIncludeDesignation": (None, ".expansionprofile"),
    "ExpansionProfileExcludedSystem": (None, ".expansionprofile"),
    "ExpansionProfileFixedVersion": (None, ".expansionprofile"),
    "ExplanationOfBenefit": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitAccident": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitAddItem": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitAddItemDetail": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitBenefitBalance": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitBenefitBalanceFinancial": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitCareTeam": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitDiagnosis": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitInformation": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitInsurance": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitItem": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitItemAdjudication": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitItemDetail": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitItemDetailSubDetail": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitPayee": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitPayment": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitProcedure": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitProcessNote": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitRelated": (None, ".explanationofbenefit"),
    "Extension": (None, ".extension"),
    "FamilyMemberHistory": (None, ".familymemberhistory"),
    "FamilyMemberHistoryCondition": (None, ".familymemberhistory"),
    "Flag": (None, ".flag"),
    "Goal": (None, ".goal"),
    "GoalTarget": (None, ".goal"),
    "GraphDefinition": (None, ".graphdefinition"),
    "GraphDefinitionLink": (None, ".graphdefinition"),
    "GraphDefinitionLinkTarget": (None, ".graphdefinition"),
    "GraphDefinitionLinkTargetCompartment": (None, ".graphdefinition"),
    "Group": (None, ".group"),
    "GroupCharacteristic": (None, ".group"),
    "GroupMember": (None, ".group"),
    "GuidanceResponse": (None, ".guidanceresponse"),
    "HealthcareService": (None, ".healthcareservice"),
    "HealthcareServiceAvailableTime": (None, ".healthcareservice"),
    "HealthcareServiceNotAvailable": (None, ".healthcareservice"),
    "HumanName": (None, ".humanname"),
    "Identifier": (None, ".identifier"),
    "ImagingManifest": (None, ".imagingmanifest"),
    "ImagingManifestStudy": (None, ".imagingmanifest"),
    "ImagingManifestStudySeries": (None, ".imagingmanifest"),
    "ImagingManifestStudySeriesInstance": (None, ".imagingmanifest"),
    "ImagingStudy": (None, ".imagingstudy"),
    "ImagingStudySeries": (None, ".imagingstudy"),
    "ImagingStudySeriesInstance": (None, ".imagingstudy"),
    "Immunization": (None, ".immunization"),
    "ImmunizationExplanation": (None, ".immunization"),
    "ImmunizationPractitioner": (None, ".immunization"),
    "ImmunizationReaction": (None, ".immunization"),
    "ImmunizationRecommendation": (None, ".immunizationrecommendation"),
    "ImmunizationRecommendationRecommendation": (None, ".immunizationrecommendation"),
    "ImmunizationRecommendationRecommendationDateCriterion": (
        None,
        ".immunizationrecommendation",
    ),
    "ImmunizationRecommendationRecommendationProtocol": (
        None,
        ".immunizationrecommendation",
    ),
    "ImmunizationVaccinationProtocol": (None, ".immunization"),
    "ImplementationGuide": (None, ".implementationguide"),
    "ImplementationGuideDependency": (None, ".implementationguide"),
    "ImplementationGuideGlobal": (None, ".implementationguide"),
    "ImplementationGuidePackage": (None, ".implementationguide"),
    "ImplementationGuidePackageResource": (None, ".implementationguide"),
    "ImplementationGuidePage": (None, ".implementationguide"),
    "Library": (None, ".library"),
    "Linkage": (None, ".linkage"),
    "LinkageItem": (None, ".linkage"),
    "List": (None, ".list"),
    "ListEntry": (None, ".list"),
    "Location": (None, ".location"),
    "LocationPosition": (None, ".location"),
    "Measure": (None, ".measure"),
    "MeasureGroup": (None, ".measure"),
    "MeasureGroupPopulation": (None, ".measure"),
    "MeasureGroupStratifier": (None, ".measure"),
    "MeasureReport": (None, ".measurereport"),
    "MeasureReportGroup": (None, ".measurereport"),
    "MeasureReportGroupPopulation": (None, ".measurereport"),
    "MeasureReportGroupStratifier": (None, ".measurereport"),
    "MeasureReportGroupStratifierStratum": (None, ".measurereport"),
    "MeasureReportGroupStratifierStratumPopulation": (None, ".measurereport"),
    "MeasureSupplementalData": (None, ".measure"),
    "Media": (None, ".media"),
    "Medication": (None, ".medication"),
    "MedicationAdministration": (None, ".medicationadministration"),
    "MedicationAdministrationDosage": (None, ".medicationadministration"),
    "MedicationAdministrationPerformer": (None, ".medicationadministration"),
    "MedicationDispense": (None, ".medicationdispense"),
    "MedicationDispensePerformer": (None, ".medicationdispense"),
    "MedicationDispenseSubstitution": (None, ".medicationdispense"),
    "MedicationIngredient": (None, ".medication"),
    "MedicationPackage": (None, ".medication"),
    "MedicationPackageBatch": (None, ".medication"),
    "MedicationPackageContent": (None, ".medication"),
    "MedicationRequest": (None, ".medicationrequest"),
    "MedicationRequestDispenseRequest": (None, ".medicationrequest"),
    "MedicationRequestRequester": (None, ".medicationrequest"),
    "MedicationRequestSubstitution": (None, ".medicationrequest"),
    "MedicationStatement": (None, ".medicationstatement"),
    "MessageDefinition": (None, ".messagedefinition"),
    "MessageDefinitionAllowedResponse": (None, ".messagedefinition"),
    "MessageDefinitionFocus": (None, ".messagedefinition"),
    "MessageHeader": (None, ".messageheader"),
    "MessageHeaderDestination": (None, ".messageheader"),
    "MessageHeaderResponse": (None, ".messageheader"),
    "MessageHeaderSource": (None, ".messageheader"),
    "Meta": (None, ".meta"),
    "MetadataResource": (None, ".metadataresource"),
    "Money": (None, ".money"),
    "NamingSystem": (None, ".namingsystem"),
    "NamingSystemUniqueId": (None, ".namingsystem"),
    "Narrative": (None, ".narrative"),
    "NutritionOrder": (None, ".nutritionorder"),
    "NutritionOrderEnteralFormula": (None, ".nutritionorder"),
    "NutritionOrderEnteralFormulaAdministration": (None, ".nutritionorder"),
    "NutritionOrderOralDiet": (None, ".nutritionorder"),
    "NutritionOrderOralDietNutrient": (None, ".nutritionorder"),
    "NutritionOrderOralDietTexture": (None, ".nutritionorder"),
    "NutritionOrderSupplement": (None, ".nutritionorder"),
    "Observation": (None, ".observation"),
    "ObservationComponent": (None, ".observation"),
    "ObservationReferenceRange": (None, ".observation"),
    "ObservationRelated": (None, ".observation"),
    "OperationDefinition": (None, ".operationdefinition"),
    "OperationDefinitionOverload": (None, ".operationdefinition"),
    "OperationDefinitionParameter": (None, ".operationdefinition"),
    "OperationDefinitionParameterBinding": (None, ".operationdefinition"),
    "OperationOutcome": (None, ".operationoutcome"),
    "OperationOutcomeIssue": (None, ".operationoutcome"),
    "Organization": (None, ".organization"),
    "OrganizationContact": (None, ".organization"),
    "ParameterDefinition": (None, ".parameterdefinition"),
    "Parameters": (None, ".parameters"),
    "ParametersParameter": (None, ".parameters"),
    "Patient": (None, ".patient"),
    "PatientAnimal": (None, ".patient"),
    "PatientCommunication": (None, ".patient"),
    "PatientContact": (None, ".patient"),
    "PatientLink": (None, ".patient"),
    "PaymentNotice": (None, ".paymentnotice"),
    "PaymentReconciliation": (None, ".paymentreconciliation"),
    "PaymentReconciliationDetail": (None, ".paymentreconciliation"),
    "PaymentReconciliationProcessNote": (None, ".paymentreconciliation"),
    "Period": (None, ".period"),
    "Person": (None, ".person"),
    "PersonLink": (None, ".person"),
    "PlanDefinition": (None, ".plandefinition"),
    "PlanDefinitionAction": (None, ".plandefinition"),
    "PlanDefinitionActionCondition": (None, ".plandefinition"),
    "PlanDefinitionActionDynamicValue": (None, ".plandefinition"),
    "PlanDefinitionActionParticipant": (None, ".plandefinition"),
    "PlanDefinitionActionRelatedAction": (None, ".plandefinition"),
    "PlanDefinitionGoal": (None, ".plandefinition"),
    "PlanDefinitionGoalTarget": (None, ".plandefinition"),
    "Practitioner": (None, ".practitioner"),
    "PractitionerQualification": (None, ".practitioner"),
    "PractitionerRole": (None, ".practitionerrole"),
    "PractitionerRoleAvailableTime": (None, ".practitionerrole"),
    "PractitionerRoleNotAvailable": (None, ".practitionerrole"),
    "Procedure": (None, ".procedure"),
    "ProcedureFocalDevice": (None, ".procedure"),
    "ProcedurePerformer": (None, ".procedure"),
    "ProcedureRequest": (None, ".procedurerequest"),
    "ProcedureRequestRequester": (None, ".procedurerequest"),
    "ProcessRequest": (None, ".processrequest"),
    "ProcessRequestItem": (None, ".processrequest"),
    "ProcessResponse": (None, ".processresponse"),
    "ProcessResponseProcessNote": (None, ".processresponse"),
    "Provenance": (None, ".provenance"),
    "ProvenanceAgent": (None, ".provenance"),
    "ProvenanceEntity": (None, ".provenance"),
    "Quantity": (None, ".quantity"),
    "Questionnaire": (None, ".questionnaire"),
    "QuestionnaireItem": (None, ".questionnaire"),
    "QuestionnaireItemEnableWhen": (None, ".questionnaire"),
    "QuestionnaireItemOption": (None, ".questionnaire"),
    "QuestionnaireResponse": (None, ".questionnaireresponse"),
    "QuestionnaireResponseItem": (None, ".questionnaireresponse"),
    "QuestionnaireResponseItemAnswer": (None, ".questionnaireresponse"),
    "Range": (None, ".range"),
    "Ratio": (None, ".ratio"),
    "Reference": (None, ".reference"),
    "ReferralRequest": (None, ".referralrequest"),
    "ReferralRequestRequester": (None, ".referralrequest"),
    "RelatedArtifact": (None, ".relatedartifact"),
    "RelatedPerson": (None, ".relatedperson"),
    "RequestGroup": (None, ".requestgroup"),
    "RequestGroupAction": (None, ".requestgroup"),
    "RequestGroupActionCondition": (None, ".requestgroup"),
    "RequestGroupActionRelatedAction": (None, ".requestgroup"),
    "ResearchStudy": (None, ".researchstudy"),
    "ResearchStudyArm": (None, ".researchstudy"),
    "ResearchSubject": (None, ".researchsubject"),
    "Resource": (None, ".resource"),
    "RiskAssessment": (None, ".riskassessment"),
    "RiskAssessmentPrediction": (None, ".riskassessment"),
    "SampledData": (None, ".sampleddata"),
    "Schedule": (None, ".schedule"),
    "SearchParameter": (None, ".searchparameter"),
    "SearchParameterComponent": (None, ".searchparameter"),
    "Sequence": (None, ".sequence"),
    "SequenceQuality": (None, ".sequence"),
    "SequenceReferenceSeq": (None, ".sequence"),
    "SequenceRepository": (None, ".sequence"),
    "SequenceVariant": (None, ".sequence"),
    "ServiceDefinition": (None, ".servicedefinition"),
    "Signature": (None, ".signature"),
    "Slot": (None, ".slot"),
    "Specimen": (None, ".specimen"),
    "SpecimenCollection": (None, ".specimen"),
    "SpecimenContainer": (None, ".specimen"),
    "SpecimenProcessing": (None, ".specimen"),
    "StructureDefinition": (None, ".structuredefinition"),
    "StructureDefinitionDifferential": (None, ".structuredefinition"),
    "StructureDefinitionMapping": (None, ".structuredefinition"),
    "StructureDefinitionSnapshot": (None, ".structuredefinition"),
    "StructureMap": (None, ".structuremap"),
    "StructureMapGroup": (None, ".structuremap"),
    "StructureMapGroupInput": (None, ".structuremap"),
    "StructureMapGroupRule": (None, ".structuremap"),
    "StructureMapGroupRuleDependent": (None, ".structuremap"),
    "StructureMapGroupRuleSource": (None, ".structuremap"),
    "StructureMapGroupRuleTarget": (None, ".structuremap"),
    "StructureMapGroupRuleTargetParameter": (None, ".structuremap"),
    "StructureMapStructure": (None, ".structuremap"),
    "Subscription": (None, ".subscription"),
    "SubscriptionChannel": (None, ".subscription"),
    "Substance": (None, ".substance"),
    "SubstanceIngredient": (None, ".substance"),
    "SubstanceInstance": (None, ".substance"),
    "SupplyDelivery": (None, ".supplydelivery"),
    "SupplyDeliverySuppliedItem": (None, ".supplydelivery"),
    "SupplyRequest": (None, ".supplyrequest"),
    "SupplyRequestOrderedItem": (None, ".supplyrequest"),
    "SupplyRequestRequester": (None, ".supplyrequest"),
    "Task": (None, ".task"),
    "TaskInput": (None, ".task"),
    "TaskOutput": (None, ".task"),
    "TaskRequester": (None, ".task"),
    "TaskRestriction": (None, ".task"),
    "TestReport": (None, ".testreport"),
    "TestReportParticipant": (None, ".testreport"),
    "TestReportSetup": (None, ".testreport"),
    "TestReportSetupAction": (None, ".testreport"),
    "TestReportSetupActionAssert": (None, ".testreport"),
    "TestReportSetupActionOperation": (None, ".testreport"),
    "TestReportTeardown": (None, ".testreport"),
    "TestReportTeardownAction": (None, ".testreport"),
    "TestReportTest": (None, ".testreport"),
    "TestReportTestAction": (None, ".testreport"),
    "TestScript": (None, ".testscript"),
    "TestScriptDestination": (None, ".testscript"),
    "TestScriptFixture": (None, ".testscript"),
    "TestScriptMetadata": (None, ".testscript"),
    "TestScriptMetadataCapability": (None, ".testscript"),
    "TestScriptMetadataLink": (None, ".testscript"),
    "TestScriptOrigin": (None, ".testscript"),
    "TestScriptRule": (None, ".testscript"),
    "TestScriptRuleParam": (None, ".testscript"),
    "TestScriptRuleset": (None, ".testscript"),
    "TestScriptRulesetRule": (None, ".testscript"),
    "TestScriptRulesetRuleParam": (None, ".testscript"),
    "TestScriptSetup": (None, ".testscript"),
    "TestScriptSetupAction": (None, ".testscript"),
    "TestScriptSetupActionAssert": (None, ".testscript"),
    "TestScriptSetupActionAssertRule": (None, ".testscript"),
    "TestScriptSetupActionAssertRuleParam": (None, ".testscript"),
    "TestScriptSetupActionAssertRuleset": (None, ".testscript"),
    "TestScriptSetupActionAssertRulesetRule": (None, ".testscript"),
    "TestScriptSetupActionAssertRulesetRuleParam": (None, ".testscript"),
    "TestScriptSetupActionOperation": (None, ".testscript"),
    "TestScriptSetupActionOperationRequestHeader": (None, ".testscript"),
    "TestScriptTeardown": (None, ".testscript"),
    "TestScriptTeardownAction": (None, ".testscript"),
    "TestScriptTest": (None, ".testscript"),
    "TestScriptTestAction": (None, ".testscript"),
    "TestScriptVariable": (None, ".testscript"),
    "Timing": (None, ".timing"),
    "TimingRepeat": (None, ".timing"),
    "TriggerDefinition": (None, ".triggerdefinition"),
    "UsageContext": (None, ".usagecontext"),
    "ValueSet": (None, ".valueset"),
    "ValueSetCompose": (None, ".valueset"),
    "ValueSetComposeInclude": (None, ".valueset"),
    "ValueSetComposeIncludeConcept": (None, ".valueset"),
    "ValueSetComposeIncludeConceptDesignation": (None, ".valueset"),
    "ValueSetComposeIncludeFilter": (None, ".valueset"),
    "ValueSetExpansion": (None, ".valueset"),
    "ValueSetExpansionContains": (None, ".valueset"),
    "ValueSetExpansionParameter": (None, ".valueset"),
    "VisionPrescription": (None, ".visionprescription"),
    "VisionPrescriptionDispense": (None, ".visionprescription"),
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


def account_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Account", v)


def accountcoverage_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AccountCoverage", v)


def accountguarantor_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AccountGuarantor", v)


def activitydefinition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ActivityDefinition", v)


def activitydefinitiondynamicvalue_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ActivityDefinitionDynamicValue", v)


def activitydefinitionparticipant_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ActivityDefinitionParticipant", v)


def address_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Address", v)


def adverseevent_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AdverseEvent", v)


def adverseeventsuspectentity_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("AdverseEventSuspectEntity", v)


def age_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Age", v)


def allergyintolerance_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AllergyIntolerance", v)


def allergyintolerancereaction_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("AllergyIntoleranceReaction", v)


def annotation_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Annotation", v)


def appointment_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Appointment", v)


def appointmentparticipant_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AppointmentParticipant", v)


def appointmentresponse_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AppointmentResponse", v)


def attachment_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Attachment", v)


def auditevent_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AuditEvent", v)


def auditeventagent_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AuditEventAgent", v)


def auditeventagentnetwork_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AuditEventAgentNetwork", v)


def auditevententity_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AuditEventEntity", v)


def auditevententitydetail_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AuditEventEntityDetail", v)


def auditeventsource_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AuditEventSource", v)


def backboneelement_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("BackboneElement", v)


def basic_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Basic", v)


def binary_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Binary", v)


def bodysite_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("BodySite", v)


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


def capabilitystatement_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CapabilityStatement", v)


def capabilitystatementdocument_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CapabilityStatementDocument", v)


def capabilitystatementimplementation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CapabilityStatementImplementation", v)


def capabilitystatementmessaging_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CapabilityStatementMessaging", v)


def capabilitystatementmessagingendpoint_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CapabilityStatementMessagingEndpoint", v)


def capabilitystatementmessagingevent_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CapabilityStatementMessagingEvent", v)


def capabilitystatementmessagingsupportedmessage_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CapabilityStatementMessagingSupportedMessage", v)


def capabilitystatementrest_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CapabilityStatementRest", v)


def capabilitystatementrestinteraction_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CapabilityStatementRestInteraction", v)


def capabilitystatementrestoperation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CapabilityStatementRestOperation", v)


def capabilitystatementrestresource_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CapabilityStatementRestResource", v)


def capabilitystatementrestresourceinteraction_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CapabilityStatementRestResourceInteraction", v)


def capabilitystatementrestresourcesearchparam_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CapabilityStatementRestResourceSearchParam", v)


def capabilitystatementrestsecurity_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CapabilityStatementRestSecurity", v)


def capabilitystatementrestsecuritycertificate_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CapabilityStatementRestSecurityCertificate", v)


def capabilitystatementsoftware_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CapabilityStatementSoftware", v)


def careplan_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CarePlan", v)


def careplanactivity_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CarePlanActivity", v)


def careplanactivitydetail_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CarePlanActivityDetail", v)


def careteam_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CareTeam", v)


def careteamparticipant_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CareTeamParticipant", v)


def chargeitem_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ChargeItem", v)


def chargeitemparticipant_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ChargeItemParticipant", v)


def claim_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Claim", v)


def claimaccident_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimAccident", v)


def claimcareteam_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimCareTeam", v)


def claimdiagnosis_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimDiagnosis", v)


def claiminformation_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimInformation", v)


def claiminsurance_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimInsurance", v)


def claimitem_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimItem", v)


def claimitemdetail_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimItemDetail", v)


def claimitemdetailsubdetail_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClaimItemDetailSubDetail", v)


def claimpayee_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimPayee", v)


def claimprocedure_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimProcedure", v)


def claimrelated_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimRelated", v)


def claimresponse_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimResponse", v)


def claimresponseadditem_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimResponseAddItem", v)


def claimresponseadditemdetail_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClaimResponseAddItemDetail", v)


def claimresponseerror_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimResponseError", v)


def claimresponseinsurance_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimResponseInsurance", v)


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


def claimresponseitemdetailsubdetail_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClaimResponseItemDetailSubDetail", v)


def claimresponsepayment_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimResponsePayment", v)


def claimresponseprocessnote_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClaimResponseProcessNote", v)


def clinicalimpression_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClinicalImpression", v)


def clinicalimpressionfinding_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClinicalImpressionFinding", v)


def clinicalimpressioninvestigation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClinicalImpressionInvestigation", v)


def codesystem_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CodeSystem", v)


def codesystemconcept_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CodeSystemConcept", v)


def codesystemconceptdesignation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CodeSystemConceptDesignation", v)


def codesystemconceptproperty_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CodeSystemConceptProperty", v)


def codesystemfilter_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CodeSystemFilter", v)


def codesystemproperty_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CodeSystemProperty", v)


def codeableconcept_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CodeableConcept", v)


def coding_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Coding", v)


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


def communicationrequestrequester_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CommunicationRequestRequester", v)


def compartmentdefinition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CompartmentDefinition", v)


def compartmentdefinitionresource_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CompartmentDefinitionResource", v)


def composition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Composition", v)


def compositionattester_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CompositionAttester", v)


def compositionevent_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CompositionEvent", v)


def compositionrelatesto_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CompositionRelatesTo", v)


def compositionsection_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CompositionSection", v)


def conceptmap_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConceptMap", v)


def conceptmapgroup_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConceptMapGroup", v)


def conceptmapgroupelement_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConceptMapGroupElement", v)


def conceptmapgroupelementtarget_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ConceptMapGroupElementTarget", v)


def conceptmapgroupelementtargetdependson_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ConceptMapGroupElementTargetDependsOn", v)


def conceptmapgroupunmapped_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ConceptMapGroupUnmapped", v)


def condition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Condition", v)


def conditionevidence_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConditionEvidence", v)


def conditionstage_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConditionStage", v)


def consent_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Consent", v)


def consentactor_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConsentActor", v)


def consentdata_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConsentData", v)


def consentexcept_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConsentExcept", v)


def consentexceptactor_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConsentExceptActor", v)


def consentexceptdata_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConsentExceptData", v)


def consentpolicy_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConsentPolicy", v)


def contactdetail_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ContactDetail", v)


def contactpoint_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ContactPoint", v)


def contract_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Contract", v)


def contractagent_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ContractAgent", v)


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


def contracttermagent_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ContractTermAgent", v)


def contracttermvalueditem_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ContractTermValuedItem", v)


def contractvalueditem_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ContractValuedItem", v)


def contributor_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Contributor", v)


def count_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Count", v)


def coverage_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Coverage", v)


def coveragegrouping_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CoverageGrouping", v)


def dataelement_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DataElement", v)


def dataelementmapping_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DataElementMapping", v)


def datarequirement_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DataRequirement", v)


def datarequirementcodefilter_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DataRequirementCodeFilter", v)


def datarequirementdatefilter_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DataRequirementDateFilter", v)


def detectedissue_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DetectedIssue", v)


def detectedissuemitigation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DetectedIssueMitigation", v)


def device_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Device", v)


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


def devicerequest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceRequest", v)


def devicerequestrequester_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceRequestRequester", v)


def deviceudi_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceUdi", v)


def deviceusestatement_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceUseStatement", v)


def diagnosticreport_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DiagnosticReport", v)


def diagnosticreportimage_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DiagnosticReportImage", v)


def diagnosticreportperformer_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DiagnosticReportPerformer", v)


def distance_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Distance", v)


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


def domainresource_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DomainResource", v)


def dosage_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Dosage", v)


def duration_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Duration", v)


def element_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Element", v)


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


def elementdefinitionexample_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ElementDefinitionExample", v)


def elementdefinitionmapping_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ElementDefinitionMapping", v)


def elementdefinitionslicing_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ElementDefinitionSlicing", v)


def elementdefinitionslicingdiscriminator_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ElementDefinitionSlicingDiscriminator", v)


def elementdefinitiontype_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ElementDefinitionType", v)


def eligibilityrequest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EligibilityRequest", v)


def eligibilityresponse_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EligibilityResponse", v)


def eligibilityresponseerror_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("EligibilityResponseError", v)


def eligibilityresponseinsurance_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("EligibilityResponseInsurance", v)


def eligibilityresponseinsurancebenefitbalance_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("EligibilityResponseInsuranceBenefitBalance", v)


def eligibilityresponseinsurancebenefitbalancefinancial_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator(
        "EligibilityResponseInsuranceBenefitBalanceFinancial", v
    )


def encounter_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Encounter", v)


def encounterclasshistory_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EncounterClassHistory", v)


def encounterdiagnosis_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EncounterDiagnosis", v)


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


def endpoint_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Endpoint", v)


def enrollmentrequest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EnrollmentRequest", v)


def enrollmentresponse_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EnrollmentResponse", v)


def episodeofcare_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EpisodeOfCare", v)


def episodeofcarediagnosis_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EpisodeOfCareDiagnosis", v)


def episodeofcarestatushistory_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("EpisodeOfCareStatusHistory", v)


def expansionprofile_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ExpansionProfile", v)


def expansionprofiledesignation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExpansionProfileDesignation", v)


def expansionprofiledesignationexclude_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExpansionProfileDesignationExclude", v)


def expansionprofiledesignationexcludedesignation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExpansionProfileDesignationExcludeDesignation", v)


def expansionprofiledesignationinclude_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExpansionProfileDesignationInclude", v)


def expansionprofiledesignationincludedesignation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExpansionProfileDesignationIncludeDesignation", v)


def expansionprofileexcludedsystem_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExpansionProfileExcludedSystem", v)


def expansionprofilefixedversion_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExpansionProfileFixedVersion", v)


def explanationofbenefit_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ExplanationOfBenefit", v)


def explanationofbenefitaccident_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExplanationOfBenefitAccident", v)


def explanationofbenefitadditem_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExplanationOfBenefitAddItem", v)


def explanationofbenefitadditemdetail_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExplanationOfBenefitAddItemDetail", v)


def explanationofbenefitbenefitbalance_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExplanationOfBenefitBenefitBalance", v)


def explanationofbenefitbenefitbalancefinancial_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExplanationOfBenefitBenefitBalanceFinancial", v)


def explanationofbenefitcareteam_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExplanationOfBenefitCareTeam", v)


def explanationofbenefitdiagnosis_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExplanationOfBenefitDiagnosis", v)


def explanationofbenefitinformation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExplanationOfBenefitInformation", v)


def explanationofbenefitinsurance_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExplanationOfBenefitInsurance", v)


def explanationofbenefititem_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExplanationOfBenefitItem", v)


def explanationofbenefititemadjudication_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExplanationOfBenefitItemAdjudication", v)


def explanationofbenefititemdetail_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExplanationOfBenefitItemDetail", v)


def explanationofbenefititemdetailsubdetail_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExplanationOfBenefitItemDetailSubDetail", v)


def explanationofbenefitpayee_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExplanationOfBenefitPayee", v)


def explanationofbenefitpayment_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExplanationOfBenefitPayment", v)


def explanationofbenefitprocedure_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExplanationOfBenefitProcedure", v)


def explanationofbenefitprocessnote_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExplanationOfBenefitProcessNote", v)


def explanationofbenefitrelated_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExplanationOfBenefitRelated", v)


def extension_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Extension", v)


def familymemberhistory_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("FamilyMemberHistory", v)


def familymemberhistorycondition_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("FamilyMemberHistoryCondition", v)


def flag_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Flag", v)


def goal_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Goal", v)


def goaltarget_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("GoalTarget", v)


def graphdefinition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("GraphDefinition", v)


def graphdefinitionlink_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("GraphDefinitionLink", v)


def graphdefinitionlinktarget_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("GraphDefinitionLinkTarget", v)


def graphdefinitionlinktargetcompartment_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("GraphDefinitionLinkTargetCompartment", v)


def group_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Group", v)


def groupcharacteristic_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("GroupCharacteristic", v)


def groupmember_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("GroupMember", v)


def guidanceresponse_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("GuidanceResponse", v)


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


def humanname_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("HumanName", v)


def identifier_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Identifier", v)


def imagingmanifest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ImagingManifest", v)


def imagingmanifeststudy_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ImagingManifestStudy", v)


def imagingmanifeststudyseries_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImagingManifestStudySeries", v)


def imagingmanifeststudyseriesinstance_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImagingManifestStudySeriesInstance", v)


def imagingstudy_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ImagingStudy", v)


def imagingstudyseries_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ImagingStudySeries", v)


def imagingstudyseriesinstance_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImagingStudySeriesInstance", v)


def immunization_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Immunization", v)


def immunizationexplanation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImmunizationExplanation", v)


def immunizationpractitioner_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImmunizationPractitioner", v)


def immunizationreaction_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ImmunizationReaction", v)


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


def immunizationvaccinationprotocol_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImmunizationVaccinationProtocol", v)


def implementationguide_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ImplementationGuide", v)


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


def library_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Library", v)


def linkage_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Linkage", v)


def linkageitem_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("LinkageItem", v)


def list_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("List", v)


def listentry_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ListEntry", v)


def location_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Location", v)


def locationposition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("LocationPosition", v)


def measure_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Measure", v)


def measuregroup_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MeasureGroup", v)


def measuregrouppopulation_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MeasureGroupPopulation", v)


def measuregroupstratifier_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MeasureGroupStratifier", v)


def measurereport_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MeasureReport", v)


def measurereportgroup_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MeasureReportGroup", v)


def measurereportgrouppopulation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MeasureReportGroupPopulation", v)


def measurereportgroupstratifier_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MeasureReportGroupStratifier", v)


def measurereportgroupstratifierstratum_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MeasureReportGroupStratifierStratum", v)


def measurereportgroupstratifierstratumpopulation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MeasureReportGroupStratifierStratumPopulation", v)


def measuresupplementaldata_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MeasureSupplementalData", v)


def media_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Media", v)


def medication_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Medication", v)


def medicationadministration_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationAdministration", v)


def medicationadministrationdosage_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationAdministrationDosage", v)


def medicationadministrationperformer_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationAdministrationPerformer", v)


def medicationdispense_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MedicationDispense", v)


def medicationdispenseperformer_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationDispensePerformer", v)


def medicationdispensesubstitution_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationDispenseSubstitution", v)


def medicationingredient_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MedicationIngredient", v)


def medicationpackage_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MedicationPackage", v)


def medicationpackagebatch_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MedicationPackageBatch", v)


def medicationpackagecontent_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationPackageContent", v)


def medicationrequest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MedicationRequest", v)


def medicationrequestdispenserequest_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationRequestDispenseRequest", v)


def medicationrequestrequester_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationRequestRequester", v)


def medicationrequestsubstitution_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationRequestSubstitution", v)


def medicationstatement_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MedicationStatement", v)


def messagedefinition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MessageDefinition", v)


def messagedefinitionallowedresponse_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MessageDefinitionAllowedResponse", v)


def messagedefinitionfocus_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MessageDefinitionFocus", v)


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


def meta_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Meta", v)


def metadataresource_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MetadataResource", v)


def money_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Money", v)


def namingsystem_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("NamingSystem", v)


def namingsystemuniqueid_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("NamingSystemUniqueId", v)


def narrative_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Narrative", v)


def nutritionorder_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("NutritionOrder", v)


def nutritionorderenteralformula_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("NutritionOrderEnteralFormula", v)


def nutritionorderenteralformulaadministration_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("NutritionOrderEnteralFormulaAdministration", v)


def nutritionorderoraldiet_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("NutritionOrderOralDiet", v)


def nutritionorderoraldietnutrient_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("NutritionOrderOralDietNutrient", v)


def nutritionorderoraldiettexture_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("NutritionOrderOralDietTexture", v)


def nutritionordersupplement_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("NutritionOrderSupplement", v)


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


def operationdefinition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("OperationDefinition", v)


def operationdefinitionoverload_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("OperationDefinitionOverload", v)


def operationdefinitionparameter_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("OperationDefinitionParameter", v)


def operationdefinitionparameterbinding_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("OperationDefinitionParameterBinding", v)


def operationoutcome_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("OperationOutcome", v)


def operationoutcomeissue_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("OperationOutcomeIssue", v)


def organization_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Organization", v)


def organizationcontact_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("OrganizationContact", v)


def parameterdefinition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ParameterDefinition", v)


def parameters_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Parameters", v)


def parametersparameter_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ParametersParameter", v)


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


def paymentnotice_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("PaymentNotice", v)


def paymentreconciliation_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("PaymentReconciliation", v)


def paymentreconciliationdetail_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PaymentReconciliationDetail", v)


def paymentreconciliationprocessnote_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PaymentReconciliationProcessNote", v)


def period_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Period", v)


def person_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Person", v)


def personlink_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("PersonLink", v)


def plandefinition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("PlanDefinition", v)


def plandefinitionaction_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("PlanDefinitionAction", v)


def plandefinitionactioncondition_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PlanDefinitionActionCondition", v)


def plandefinitionactiondynamicvalue_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PlanDefinitionActionDynamicValue", v)


def plandefinitionactionparticipant_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PlanDefinitionActionParticipant", v)


def plandefinitionactionrelatedaction_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PlanDefinitionActionRelatedAction", v)


def plandefinitiongoal_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("PlanDefinitionGoal", v)


def plandefinitiongoaltarget_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PlanDefinitionGoalTarget", v)


def practitioner_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Practitioner", v)


def practitionerqualification_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PractitionerQualification", v)


def practitionerrole_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("PractitionerRole", v)


def practitionerroleavailabletime_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PractitionerRoleAvailableTime", v)


def practitionerrolenotavailable_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PractitionerRoleNotAvailable", v)


def procedure_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Procedure", v)


def procedurefocaldevice_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ProcedureFocalDevice", v)


def procedureperformer_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ProcedurePerformer", v)


def procedurerequest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ProcedureRequest", v)


def procedurerequestrequester_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ProcedureRequestRequester", v)


def processrequest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ProcessRequest", v)


def processrequestitem_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ProcessRequestItem", v)


def processresponse_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ProcessResponse", v)


def processresponseprocessnote_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ProcessResponseProcessNote", v)


def provenance_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Provenance", v)


def provenanceagent_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ProvenanceAgent", v)


def provenanceentity_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ProvenanceEntity", v)


def quantity_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Quantity", v)


def questionnaire_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Questionnaire", v)


def questionnaireitem_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("QuestionnaireItem", v)


def questionnaireitemenablewhen_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("QuestionnaireItemEnableWhen", v)


def questionnaireitemoption_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("QuestionnaireItemOption", v)


def questionnaireresponse_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("QuestionnaireResponse", v)


def questionnaireresponseitem_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("QuestionnaireResponseItem", v)


def questionnaireresponseitemanswer_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("QuestionnaireResponseItemAnswer", v)


def range_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Range", v)


def ratio_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Ratio", v)


def reference_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Reference", v)


def referralrequest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ReferralRequest", v)


def referralrequestrequester_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ReferralRequestRequester", v)


def relatedartifact_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("RelatedArtifact", v)


def relatedperson_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("RelatedPerson", v)


def requestgroup_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("RequestGroup", v)


def requestgroupaction_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("RequestGroupAction", v)


def requestgroupactioncondition_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("RequestGroupActionCondition", v)


def requestgroupactionrelatedaction_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("RequestGroupActionRelatedAction", v)


def researchstudy_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ResearchStudy", v)


def researchstudyarm_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ResearchStudyArm", v)


def researchsubject_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ResearchSubject", v)


def resource_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Resource", v)


def riskassessment_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("RiskAssessment", v)


def riskassessmentprediction_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("RiskAssessmentPrediction", v)


def sampleddata_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SampledData", v)


def schedule_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Schedule", v)


def searchparameter_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SearchParameter", v)


def searchparametercomponent_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SearchParameterComponent", v)


def sequence_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Sequence", v)


def sequencequality_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SequenceQuality", v)


def sequencereferenceseq_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SequenceReferenceSeq", v)


def sequencerepository_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SequenceRepository", v)


def sequencevariant_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SequenceVariant", v)


def servicedefinition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ServiceDefinition", v)


def signature_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Signature", v)


def slot_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Slot", v)


def specimen_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Specimen", v)


def specimencollection_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SpecimenCollection", v)


def specimencontainer_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SpecimenContainer", v)


def specimenprocessing_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SpecimenProcessing", v)


def structuredefinition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("StructureDefinition", v)


def structuredefinitiondifferential_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("StructureDefinitionDifferential", v)


def structuredefinitionmapping_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("StructureDefinitionMapping", v)


def structuredefinitionsnapshot_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("StructureDefinitionSnapshot", v)


def structuremap_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("StructureMap", v)


def structuremapgroup_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("StructureMapGroup", v)


def structuremapgroupinput_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("StructureMapGroupInput", v)


def structuremapgrouprule_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("StructureMapGroupRule", v)


def structuremapgroupruledependent_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("StructureMapGroupRuleDependent", v)


def structuremapgrouprulesource_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("StructureMapGroupRuleSource", v)


def structuremapgroupruletarget_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("StructureMapGroupRuleTarget", v)


def structuremapgroupruletargetparameter_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("StructureMapGroupRuleTargetParameter", v)


def structuremapstructure_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("StructureMapStructure", v)


def subscription_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Subscription", v)


def subscriptionchannel_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SubscriptionChannel", v)


def substance_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Substance", v)


def substanceingredient_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SubstanceIngredient", v)


def substanceinstance_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SubstanceInstance", v)


def supplydelivery_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SupplyDelivery", v)


def supplydeliverysupplieditem_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SupplyDeliverySuppliedItem", v)


def supplyrequest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SupplyRequest", v)


def supplyrequestordereditem_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SupplyRequestOrderedItem", v)


def supplyrequestrequester_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SupplyRequestRequester", v)


def task_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Task", v)


def taskinput_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TaskInput", v)


def taskoutput_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TaskOutput", v)


def taskrequester_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TaskRequester", v)


def taskrestriction_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TaskRestriction", v)


def testreport_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestReport", v)


def testreportparticipant_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestReportParticipant", v)


def testreportsetup_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestReportSetup", v)


def testreportsetupaction_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestReportSetupAction", v)


def testreportsetupactionassert_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TestReportSetupActionAssert", v)


def testreportsetupactionoperation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TestReportSetupActionOperation", v)


def testreportteardown_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestReportTeardown", v)


def testreportteardownaction_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TestReportTeardownAction", v)


def testreporttest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestReportTest", v)


def testreporttestaction_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestReportTestAction", v)


def testscript_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScript", v)


def testscriptdestination_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScriptDestination", v)


def testscriptfixture_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScriptFixture", v)


def testscriptmetadata_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScriptMetadata", v)


def testscriptmetadatacapability_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TestScriptMetadataCapability", v)


def testscriptmetadatalink_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScriptMetadataLink", v)


def testscriptorigin_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScriptOrigin", v)


def testscriptrule_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScriptRule", v)


def testscriptruleparam_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScriptRuleParam", v)


def testscriptruleset_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScriptRuleset", v)


def testscriptrulesetrule_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScriptRulesetRule", v)


def testscriptrulesetruleparam_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TestScriptRulesetRuleParam", v)


def testscriptsetup_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScriptSetup", v)


def testscriptsetupaction_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScriptSetupAction", v)


def testscriptsetupactionassert_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TestScriptSetupActionAssert", v)


def testscriptsetupactionassertrule_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TestScriptSetupActionAssertRule", v)


def testscriptsetupactionassertruleparam_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TestScriptSetupActionAssertRuleParam", v)


def testscriptsetupactionassertruleset_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TestScriptSetupActionAssertRuleset", v)


def testscriptsetupactionassertrulesetrule_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TestScriptSetupActionAssertRulesetRule", v)


def testscriptsetupactionassertrulesetruleparam_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TestScriptSetupActionAssertRulesetRuleParam", v)


def testscriptsetupactionoperation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TestScriptSetupActionOperation", v)


def testscriptsetupactionoperationrequestheader_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TestScriptSetupActionOperationRequestHeader", v)


def testscriptteardown_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScriptTeardown", v)


def testscriptteardownaction_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TestScriptTeardownAction", v)


def testscripttest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScriptTest", v)


def testscripttestaction_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScriptTestAction", v)


def testscriptvariable_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScriptVariable", v)


def timing_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Timing", v)


def timingrepeat_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TimingRepeat", v)


def triggerdefinition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TriggerDefinition", v)


def usagecontext_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("UsageContext", v)


def valueset_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ValueSet", v)


def valuesetcompose_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ValueSetCompose", v)


def valuesetcomposeinclude_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ValueSetComposeInclude", v)


def valuesetcomposeincludeconcept_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ValueSetComposeIncludeConcept", v)


def valuesetcomposeincludeconceptdesignation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ValueSetComposeIncludeConceptDesignation", v)


def valuesetcomposeincludefilter_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ValueSetComposeIncludeFilter", v)


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


def visionprescription_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("VisionPrescription", v)


def visionprescriptiondispense_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("VisionPrescriptionDispense", v)


__all__ = [
    "fhirprimitiveextension_validator",
    "account_validator",
    "accountcoverage_validator",
    "accountguarantor_validator",
    "activitydefinition_validator",
    "activitydefinitiondynamicvalue_validator",
    "activitydefinitionparticipant_validator",
    "address_validator",
    "adverseevent_validator",
    "adverseeventsuspectentity_validator",
    "age_validator",
    "allergyintolerance_validator",
    "allergyintolerancereaction_validator",
    "annotation_validator",
    "appointment_validator",
    "appointmentparticipant_validator",
    "appointmentresponse_validator",
    "attachment_validator",
    "auditevent_validator",
    "auditeventagent_validator",
    "auditeventagentnetwork_validator",
    "auditevententity_validator",
    "auditevententitydetail_validator",
    "auditeventsource_validator",
    "backboneelement_validator",
    "basic_validator",
    "binary_validator",
    "bodysite_validator",
    "bundle_validator",
    "bundleentry_validator",
    "bundleentryrequest_validator",
    "bundleentryresponse_validator",
    "bundleentrysearch_validator",
    "bundlelink_validator",
    "capabilitystatement_validator",
    "capabilitystatementdocument_validator",
    "capabilitystatementimplementation_validator",
    "capabilitystatementmessaging_validator",
    "capabilitystatementmessagingendpoint_validator",
    "capabilitystatementmessagingevent_validator",
    "capabilitystatementmessagingsupportedmessage_validator",
    "capabilitystatementrest_validator",
    "capabilitystatementrestinteraction_validator",
    "capabilitystatementrestoperation_validator",
    "capabilitystatementrestresource_validator",
    "capabilitystatementrestresourceinteraction_validator",
    "capabilitystatementrestresourcesearchparam_validator",
    "capabilitystatementrestsecurity_validator",
    "capabilitystatementrestsecuritycertificate_validator",
    "capabilitystatementsoftware_validator",
    "careplan_validator",
    "careplanactivity_validator",
    "careplanactivitydetail_validator",
    "careteam_validator",
    "careteamparticipant_validator",
    "chargeitem_validator",
    "chargeitemparticipant_validator",
    "claim_validator",
    "claimaccident_validator",
    "claimcareteam_validator",
    "claimdiagnosis_validator",
    "claiminformation_validator",
    "claiminsurance_validator",
    "claimitem_validator",
    "claimitemdetail_validator",
    "claimitemdetailsubdetail_validator",
    "claimpayee_validator",
    "claimprocedure_validator",
    "claimrelated_validator",
    "claimresponse_validator",
    "claimresponseadditem_validator",
    "claimresponseadditemdetail_validator",
    "claimresponseerror_validator",
    "claimresponseinsurance_validator",
    "claimresponseitem_validator",
    "claimresponseitemadjudication_validator",
    "claimresponseitemdetail_validator",
    "claimresponseitemdetailsubdetail_validator",
    "claimresponsepayment_validator",
    "claimresponseprocessnote_validator",
    "clinicalimpression_validator",
    "clinicalimpressionfinding_validator",
    "clinicalimpressioninvestigation_validator",
    "codesystem_validator",
    "codesystemconcept_validator",
    "codesystemconceptdesignation_validator",
    "codesystemconceptproperty_validator",
    "codesystemfilter_validator",
    "codesystemproperty_validator",
    "codeableconcept_validator",
    "coding_validator",
    "communication_validator",
    "communicationpayload_validator",
    "communicationrequest_validator",
    "communicationrequestpayload_validator",
    "communicationrequestrequester_validator",
    "compartmentdefinition_validator",
    "compartmentdefinitionresource_validator",
    "composition_validator",
    "compositionattester_validator",
    "compositionevent_validator",
    "compositionrelatesto_validator",
    "compositionsection_validator",
    "conceptmap_validator",
    "conceptmapgroup_validator",
    "conceptmapgroupelement_validator",
    "conceptmapgroupelementtarget_validator",
    "conceptmapgroupelementtargetdependson_validator",
    "conceptmapgroupunmapped_validator",
    "condition_validator",
    "conditionevidence_validator",
    "conditionstage_validator",
    "consent_validator",
    "consentactor_validator",
    "consentdata_validator",
    "consentexcept_validator",
    "consentexceptactor_validator",
    "consentexceptdata_validator",
    "consentpolicy_validator",
    "contactdetail_validator",
    "contactpoint_validator",
    "contract_validator",
    "contractagent_validator",
    "contractfriendly_validator",
    "contractlegal_validator",
    "contractrule_validator",
    "contractsigner_validator",
    "contractterm_validator",
    "contracttermagent_validator",
    "contracttermvalueditem_validator",
    "contractvalueditem_validator",
    "contributor_validator",
    "count_validator",
    "coverage_validator",
    "coveragegrouping_validator",
    "dataelement_validator",
    "dataelementmapping_validator",
    "datarequirement_validator",
    "datarequirementcodefilter_validator",
    "datarequirementdatefilter_validator",
    "detectedissue_validator",
    "detectedissuemitigation_validator",
    "device_validator",
    "devicecomponent_validator",
    "devicecomponentproductionspecification_validator",
    "devicemetric_validator",
    "devicemetriccalibration_validator",
    "devicerequest_validator",
    "devicerequestrequester_validator",
    "deviceudi_validator",
    "deviceusestatement_validator",
    "diagnosticreport_validator",
    "diagnosticreportimage_validator",
    "diagnosticreportperformer_validator",
    "distance_validator",
    "documentmanifest_validator",
    "documentmanifestcontent_validator",
    "documentmanifestrelated_validator",
    "documentreference_validator",
    "documentreferencecontent_validator",
    "documentreferencecontext_validator",
    "documentreferencecontextrelated_validator",
    "documentreferencerelatesto_validator",
    "domainresource_validator",
    "dosage_validator",
    "duration_validator",
    "element_validator",
    "elementdefinition_validator",
    "elementdefinitionbase_validator",
    "elementdefinitionbinding_validator",
    "elementdefinitionconstraint_validator",
    "elementdefinitionexample_validator",
    "elementdefinitionmapping_validator",
    "elementdefinitionslicing_validator",
    "elementdefinitionslicingdiscriminator_validator",
    "elementdefinitiontype_validator",
    "eligibilityrequest_validator",
    "eligibilityresponse_validator",
    "eligibilityresponseerror_validator",
    "eligibilityresponseinsurance_validator",
    "eligibilityresponseinsurancebenefitbalance_validator",
    "eligibilityresponseinsurancebenefitbalancefinancial_validator",
    "encounter_validator",
    "encounterclasshistory_validator",
    "encounterdiagnosis_validator",
    "encounterhospitalization_validator",
    "encounterlocation_validator",
    "encounterparticipant_validator",
    "encounterstatushistory_validator",
    "endpoint_validator",
    "enrollmentrequest_validator",
    "enrollmentresponse_validator",
    "episodeofcare_validator",
    "episodeofcarediagnosis_validator",
    "episodeofcarestatushistory_validator",
    "expansionprofile_validator",
    "expansionprofiledesignation_validator",
    "expansionprofiledesignationexclude_validator",
    "expansionprofiledesignationexcludedesignation_validator",
    "expansionprofiledesignationinclude_validator",
    "expansionprofiledesignationincludedesignation_validator",
    "expansionprofileexcludedsystem_validator",
    "expansionprofilefixedversion_validator",
    "explanationofbenefit_validator",
    "explanationofbenefitaccident_validator",
    "explanationofbenefitadditem_validator",
    "explanationofbenefitadditemdetail_validator",
    "explanationofbenefitbenefitbalance_validator",
    "explanationofbenefitbenefitbalancefinancial_validator",
    "explanationofbenefitcareteam_validator",
    "explanationofbenefitdiagnosis_validator",
    "explanationofbenefitinformation_validator",
    "explanationofbenefitinsurance_validator",
    "explanationofbenefititem_validator",
    "explanationofbenefititemadjudication_validator",
    "explanationofbenefititemdetail_validator",
    "explanationofbenefititemdetailsubdetail_validator",
    "explanationofbenefitpayee_validator",
    "explanationofbenefitpayment_validator",
    "explanationofbenefitprocedure_validator",
    "explanationofbenefitprocessnote_validator",
    "explanationofbenefitrelated_validator",
    "extension_validator",
    "familymemberhistory_validator",
    "familymemberhistorycondition_validator",
    "flag_validator",
    "goal_validator",
    "goaltarget_validator",
    "graphdefinition_validator",
    "graphdefinitionlink_validator",
    "graphdefinitionlinktarget_validator",
    "graphdefinitionlinktargetcompartment_validator",
    "group_validator",
    "groupcharacteristic_validator",
    "groupmember_validator",
    "guidanceresponse_validator",
    "healthcareservice_validator",
    "healthcareserviceavailabletime_validator",
    "healthcareservicenotavailable_validator",
    "humanname_validator",
    "identifier_validator",
    "imagingmanifest_validator",
    "imagingmanifeststudy_validator",
    "imagingmanifeststudyseries_validator",
    "imagingmanifeststudyseriesinstance_validator",
    "imagingstudy_validator",
    "imagingstudyseries_validator",
    "imagingstudyseriesinstance_validator",
    "immunization_validator",
    "immunizationexplanation_validator",
    "immunizationpractitioner_validator",
    "immunizationreaction_validator",
    "immunizationrecommendation_validator",
    "immunizationrecommendationrecommendation_validator",
    "immunizationrecommendationrecommendationdatecriterion_validator",
    "immunizationrecommendationrecommendationprotocol_validator",
    "immunizationvaccinationprotocol_validator",
    "implementationguide_validator",
    "implementationguidedependency_validator",
    "implementationguideglobal_validator",
    "implementationguidepackage_validator",
    "implementationguidepackageresource_validator",
    "implementationguidepage_validator",
    "library_validator",
    "linkage_validator",
    "linkageitem_validator",
    "list_validator",
    "listentry_validator",
    "location_validator",
    "locationposition_validator",
    "measure_validator",
    "measuregroup_validator",
    "measuregrouppopulation_validator",
    "measuregroupstratifier_validator",
    "measurereport_validator",
    "measurereportgroup_validator",
    "measurereportgrouppopulation_validator",
    "measurereportgroupstratifier_validator",
    "measurereportgroupstratifierstratum_validator",
    "measurereportgroupstratifierstratumpopulation_validator",
    "measuresupplementaldata_validator",
    "media_validator",
    "medication_validator",
    "medicationadministration_validator",
    "medicationadministrationdosage_validator",
    "medicationadministrationperformer_validator",
    "medicationdispense_validator",
    "medicationdispenseperformer_validator",
    "medicationdispensesubstitution_validator",
    "medicationingredient_validator",
    "medicationpackage_validator",
    "medicationpackagebatch_validator",
    "medicationpackagecontent_validator",
    "medicationrequest_validator",
    "medicationrequestdispenserequest_validator",
    "medicationrequestrequester_validator",
    "medicationrequestsubstitution_validator",
    "medicationstatement_validator",
    "messagedefinition_validator",
    "messagedefinitionallowedresponse_validator",
    "messagedefinitionfocus_validator",
    "messageheader_validator",
    "messageheaderdestination_validator",
    "messageheaderresponse_validator",
    "messageheadersource_validator",
    "meta_validator",
    "metadataresource_validator",
    "money_validator",
    "namingsystem_validator",
    "namingsystemuniqueid_validator",
    "narrative_validator",
    "nutritionorder_validator",
    "nutritionorderenteralformula_validator",
    "nutritionorderenteralformulaadministration_validator",
    "nutritionorderoraldiet_validator",
    "nutritionorderoraldietnutrient_validator",
    "nutritionorderoraldiettexture_validator",
    "nutritionordersupplement_validator",
    "observation_validator",
    "observationcomponent_validator",
    "observationreferencerange_validator",
    "observationrelated_validator",
    "operationdefinition_validator",
    "operationdefinitionoverload_validator",
    "operationdefinitionparameter_validator",
    "operationdefinitionparameterbinding_validator",
    "operationoutcome_validator",
    "operationoutcomeissue_validator",
    "organization_validator",
    "organizationcontact_validator",
    "parameterdefinition_validator",
    "parameters_validator",
    "parametersparameter_validator",
    "patient_validator",
    "patientanimal_validator",
    "patientcommunication_validator",
    "patientcontact_validator",
    "patientlink_validator",
    "paymentnotice_validator",
    "paymentreconciliation_validator",
    "paymentreconciliationdetail_validator",
    "paymentreconciliationprocessnote_validator",
    "period_validator",
    "person_validator",
    "personlink_validator",
    "plandefinition_validator",
    "plandefinitionaction_validator",
    "plandefinitionactioncondition_validator",
    "plandefinitionactiondynamicvalue_validator",
    "plandefinitionactionparticipant_validator",
    "plandefinitionactionrelatedaction_validator",
    "plandefinitiongoal_validator",
    "plandefinitiongoaltarget_validator",
    "practitioner_validator",
    "practitionerqualification_validator",
    "practitionerrole_validator",
    "practitionerroleavailabletime_validator",
    "practitionerrolenotavailable_validator",
    "procedure_validator",
    "procedurefocaldevice_validator",
    "procedureperformer_validator",
    "procedurerequest_validator",
    "procedurerequestrequester_validator",
    "processrequest_validator",
    "processrequestitem_validator",
    "processresponse_validator",
    "processresponseprocessnote_validator",
    "provenance_validator",
    "provenanceagent_validator",
    "provenanceentity_validator",
    "quantity_validator",
    "questionnaire_validator",
    "questionnaireitem_validator",
    "questionnaireitemenablewhen_validator",
    "questionnaireitemoption_validator",
    "questionnaireresponse_validator",
    "questionnaireresponseitem_validator",
    "questionnaireresponseitemanswer_validator",
    "range_validator",
    "ratio_validator",
    "reference_validator",
    "referralrequest_validator",
    "referralrequestrequester_validator",
    "relatedartifact_validator",
    "relatedperson_validator",
    "requestgroup_validator",
    "requestgroupaction_validator",
    "requestgroupactioncondition_validator",
    "requestgroupactionrelatedaction_validator",
    "researchstudy_validator",
    "researchstudyarm_validator",
    "researchsubject_validator",
    "resource_validator",
    "riskassessment_validator",
    "riskassessmentprediction_validator",
    "sampleddata_validator",
    "schedule_validator",
    "searchparameter_validator",
    "searchparametercomponent_validator",
    "sequence_validator",
    "sequencequality_validator",
    "sequencereferenceseq_validator",
    "sequencerepository_validator",
    "sequencevariant_validator",
    "servicedefinition_validator",
    "signature_validator",
    "slot_validator",
    "specimen_validator",
    "specimencollection_validator",
    "specimencontainer_validator",
    "specimenprocessing_validator",
    "structuredefinition_validator",
    "structuredefinitiondifferential_validator",
    "structuredefinitionmapping_validator",
    "structuredefinitionsnapshot_validator",
    "structuremap_validator",
    "structuremapgroup_validator",
    "structuremapgroupinput_validator",
    "structuremapgrouprule_validator",
    "structuremapgroupruledependent_validator",
    "structuremapgrouprulesource_validator",
    "structuremapgroupruletarget_validator",
    "structuremapgroupruletargetparameter_validator",
    "structuremapstructure_validator",
    "subscription_validator",
    "subscriptionchannel_validator",
    "substance_validator",
    "substanceingredient_validator",
    "substanceinstance_validator",
    "supplydelivery_validator",
    "supplydeliverysupplieditem_validator",
    "supplyrequest_validator",
    "supplyrequestordereditem_validator",
    "supplyrequestrequester_validator",
    "task_validator",
    "taskinput_validator",
    "taskoutput_validator",
    "taskrequester_validator",
    "taskrestriction_validator",
    "testreport_validator",
    "testreportparticipant_validator",
    "testreportsetup_validator",
    "testreportsetupaction_validator",
    "testreportsetupactionassert_validator",
    "testreportsetupactionoperation_validator",
    "testreportteardown_validator",
    "testreportteardownaction_validator",
    "testreporttest_validator",
    "testreporttestaction_validator",
    "testscript_validator",
    "testscriptdestination_validator",
    "testscriptfixture_validator",
    "testscriptmetadata_validator",
    "testscriptmetadatacapability_validator",
    "testscriptmetadatalink_validator",
    "testscriptorigin_validator",
    "testscriptrule_validator",
    "testscriptruleparam_validator",
    "testscriptruleset_validator",
    "testscriptrulesetrule_validator",
    "testscriptrulesetruleparam_validator",
    "testscriptsetup_validator",
    "testscriptsetupaction_validator",
    "testscriptsetupactionassert_validator",
    "testscriptsetupactionassertrule_validator",
    "testscriptsetupactionassertruleparam_validator",
    "testscriptsetupactionassertruleset_validator",
    "testscriptsetupactionassertrulesetrule_validator",
    "testscriptsetupactionassertrulesetruleparam_validator",
    "testscriptsetupactionoperation_validator",
    "testscriptsetupactionoperationrequestheader_validator",
    "testscriptteardown_validator",
    "testscriptteardownaction_validator",
    "testscripttest_validator",
    "testscripttestaction_validator",
    "testscriptvariable_validator",
    "timing_validator",
    "timingrepeat_validator",
    "triggerdefinition_validator",
    "usagecontext_validator",
    "valueset_validator",
    "valuesetcompose_validator",
    "valuesetcomposeinclude_validator",
    "valuesetcomposeincludeconcept_validator",
    "valuesetcomposeincludeconceptdesignation_validator",
    "valuesetcomposeincludefilter_validator",
    "valuesetexpansion_validator",
    "valuesetexpansioncontains_validator",
    "valuesetexpansionparameter_validator",
    "visionprescription_validator",
    "visionprescriptiondispense_validator",
]
